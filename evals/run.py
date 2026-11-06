"""Corre los evals de rt-chile contra un agente con la skill cargada y los califica.

Uso:
  python evals/run.py --agent opencode --model <proveedor/modelo>   # todos los casos, sin juez LLM
  python evals/run.py --judge               # + juez LLM con rúbrica (más caro)
  python evals/run.py --cases zona-01,pda-01 --workers 4
  python evals/run.py --agent opencode --model opencode-go/deepseek-v4.1-flash  # OpenCode (suscripción Go)
  python evals/run.py --regrade evals/results/<f>.jsonl --rejudge g2-04  # vuelve a llamar solo al juez
  python evals/run.py --agent codex         # opcional: `codex exec` (si está instalado)
Cada caso se guarda apenas termina en evals/results/<fecha>.jsonl (si se corta, no se pierde lo gastado).
Umbral (AGENTS.md regla 6): 100 % de casos critical y ≥95 % del resto.
Salida: evals/results/<fecha>.md (resumen) y evals/results/<fecha>.jsonl (detalle; gitignored).
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import tempfile
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "rt-chile"
CASES = ROOT / "evals" / "cases"
RESULTS = ROOT / "evals" / "results"
# Sin hooks: con plugins instalados, cada llamada al CLI del juez podía dejar vivo un proceso y agotar la RAM.
NO_HOOKS = ["--settings", '{"disableAllHooks": true}', "--no-session-persistence"]
HINT = ("El usuario tiene instalada la skill rt-chile (Reglamentación Térmica de Chile) en .claude/skills/rt-chile. "
        "Úsala para cualquier consulta sobre normativa térmica, construcción o certificaciones en Chile.")
CIERRE_LIMITES = r"no reemplaza|orientaci[oó]n t[eé]cnica|profesional competente|l[ií]mites"
CIERRE_FUENTES = r"https?://\S*(minvu|diariooficial|normastecnicas|mma\.gob|bcn\.cl|calificacionenergetica)"


def run_cmd(cmd: list[str], cwd: Path, timeout: int) -> subprocess.CompletedProcess:
    """Como subprocess.run, pero el timeout mata todo el grupo de procesos (herramientas del agente incluidas);
    si no, un nieto que retiene los pipes deja colgado el arnés. stdin cerrado: `opencode run` lo espera si está abierto."""
    # PWD explícito: OpenCode lo prefiere a cwd; heredado, el agente corría en el repo y podía leer casos y tests
    p = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL,
                         text=True, start_new_session=True, env={**os.environ, "PWD": str(cwd)})
    try:
        out, err = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        try:
            p.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            pass
        raise
    return subprocess.CompletedProcess(cmd, p.returncode, out, err)


def wait_for_memory(min_gb: float, max_wait: int = 900) -> None:
    """No lanza otro caso si el PC está corto de RAM."""
    deadline = time.time() + max_wait
    while min_gb > 0 and time.time() < deadline:
        with open("/proc/meminfo", encoding="ascii") as fh:
            info = dict(line.split(":", 1) for line in fh)
        if int(info["MemAvailable"].split()[0]) / 1048576 >= min_gb:
            return
        time.sleep(15)


def opencode_config() -> str:
    """Config del workspace: sin MCP (cada corrida los levantaría) ni snapshots git; la evaluación no los usa."""
    try:
        global_cfg = json.loads((Path.home() / ".config/opencode/opencode.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        global_cfg = {}
    mcp = {name: {**cfg, "enabled": False} for name, cfg in (global_cfg.get("mcp") or {}).items()}
    return json.dumps({"$schema": "https://opencode.ai/config.json", "snapshot": False, "mcp": mcp})


def workspace() -> Path:
    """Directorio aislado con la skill en .claude/skills y .agents/skills (sin las instrucciones del repo)."""
    d = Path(tempfile.mkdtemp(prefix="rtchile-eval-"))
    for sub in (".claude/skills", ".agents/skills"):
        (d / sub).mkdir(parents=True)
        # copia (no symlink): el agente solo puede leer dentro del directorio de trabajo
        shutil.copytree(SKILL, d / sub / "rt-chile", ignore=shutil.ignore_patterns("tests", "__pycache__"))
    (d / "opencode.json").write_text(opencode_config(), encoding="utf-8")
    return d


def ask_judge(prompt: str, cwd: Path, timeout: int, model: str) -> tuple[str, float]:
    """Juez liviano: system prompt mínimo y sin herramientas (no carga el contexto del CLI)."""
    cmd = ["claude", "-p", prompt, "--output-format", "json", "--model", model, "--tools", "", *NO_HOOKS,
           "--setting-sources", "", "--strict-mcp-config",
           "--system-prompt", "Eres un evaluador técnico riguroso y justo. Respondes solo JSON válido."]
    r = run_cmd(cmd, cwd, timeout)
    try:
        j = json.loads(r.stdout)
        return j.get("result", ""), float(j.get("total_cost_usd", 0) or 0)
    except json.JSONDecodeError:
        return r.stdout + r.stderr, 0.0


def firma(raiz: Path) -> dict:
    return {str(f.relative_to(raiz)): hashlib.sha256(f.read_bytes()).hexdigest() for f in raiz.rglob("*")
            if f.is_file() and not set(f.relative_to(raiz).parts) & {"tests", "__pycache__"}}


def huella() -> str:
    """Identifica la versión medida de la skill."""
    return hashlib.sha256(json.dumps(firma(SKILL), sort_keys=True).encode()).hexdigest()[:12]


def copias_desactualizadas() -> list[str]:
    """Copias instaladas que difieren del repo. OpenCode las carga por sobre el workspace, incluso con otro HOME."""
    actual = firma(SKILL)
    return [str(c) for c in (Path.home() / ".agents/skills/rt-chile", Path.home() / ".claude/skills/rt-chile")
            if c.exists() and firma(c.resolve()) != actual]


def parse_opencode(stdout: str, stderr: str = "") -> tuple[str, float]:
    """Respuesta final (último texto) y costo de una salida `opencode run --format json`."""
    texts, cost, errors = [], 0.0, []
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        part = ev.get("part") or {}
        if ev.get("type") == "text" and (part.get("text") or "").strip():
            texts.append(part["text"])
        elif ev.get("type") == "step_finish":
            cost += float(part.get("cost") or 0)
        elif ev.get("type") == "error":
            errors.append(json.dumps(ev.get("error"), ensure_ascii=False))
    if texts:
        return texts[-1], cost
    return "ERROR AGENTE: " + ("; ".join(errors) or stderr or "sin texto en la salida"), cost


def ask(agent: str, prompt: str, cwd: Path, timeout: int, model: str | None = None) -> tuple[str, float]:
    if agent == "claude":
        cmd = ["claude", "-p", prompt, "--output-format", "json", *NO_HOOKS,
               "--allowedTools", "Skill,Read,Glob,Grep,Bash(python3:*),Bash(python:*)"]
        if model:
            cmd += ["--model", model]
        cmd += ["--append-system-prompt", HINT]
        r = run_cmd(cmd, cwd, timeout)
        try:
            j = json.loads(r.stdout)
            return j.get("result", ""), float(j.get("total_cost_usd", 0) or 0)
        except json.JSONDecodeError:
            return r.stdout + r.stderr, 0.0
    if agent == "opencode":
        # --format json separa la respuesta de lo que imprimen las herramientas (si no, los patrones calzarían con los
        # archivos leídos). --standalone: servidor privado que muere con el caso; el servicio compartido se saturó
        # y dejó de responder tras decenas de workspaces (2026-11-05).
        cmd = ["opencode", "run", "--standalone", "--format", "json", HINT + "\n\n" + prompt] + (["--model", model] if model else [])
        r = run_cmd(cmd, cwd, timeout)
        return parse_opencode(r.stdout, r.stderr)
    if agent == "codex":
        # workspace temporal fuera de git; sandbox de solo lectura basta para leer la skill y correr sus scripts
        with tempfile.NamedTemporaryFile("r", suffix=".txt", encoding="utf-8") as last:
            cmd = ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "--sandbox", "read-only",
                   "--output-last-message", last.name, HINT + "\n\n" + prompt] + (["--model", model] if model else [])
            r = run_cmd(cmd, cwd, timeout)
            return last.read() or (r.stdout + r.stderr), 0.0
    if agent == "notebooklm":
        # Consulta el notebook publicado (no carga la skill). Requiere RT_CHILE_NOTEBOOK_ID y sesión iniciada.
        # --new borra la conversación anterior: cada caso parte sin contexto de los demás. Sin terminal exige --yes.
        r = run_cmd(["notebooklm", "ask", "--new", "--yes", "--json", "-n", os.environ["RT_CHILE_NOTEBOOK_ID"], prompt], cwd, timeout)
        if r.returncode != 0:
            return "ERROR AGENTE: " + (r.stderr or r.stdout), 0.0
        return json.loads(r.stdout)["answer"], 0.0
    raise ValueError(agent)


def normalizar(ans: str) -> str:
    """'Tablas 7 y 14' -> 'Tabla 7 y Tabla 14' (para que los patrones de cita no dependan del plural)."""
    ans = re.sub(r"Tablas\s+(N[°º]\s*)?(\d+)((?:\s*,\s*\d+)*)\s+y\s+(\d+)",
                 lambda m: "Tabla " + m.group(2) + "".join(f", Tabla {x.strip()}" for x in m.group(3).split(",") if x.strip())
                 + " y Tabla " + m.group(4), ans)
    ans = re.sub(r"Tablas\s+N[°º]?\s*(\d+)\s+y\s+N[°º]?\s*(\d+)", r"Tabla N° \1 y Tabla N° \2", ans)
    # NotebookLM escribe variables y decimales en LaTeX
    ans = ans.replace("{,}", ",")
    ans = re.sub(r"U_\{?(\\text\{)?pvm\}?\}?", "Upvm", ans)
    return re.sub(r"Tablas\s+(\d)", r"Tabla \1", ans)


def grade_rules(case: dict, ans: str) -> dict:
    ans = normalizar(ans)
    e = case["esperado"]
    flags = re.I
    hechos = [{"descripcion": h["descripcion"], "ok": any(re.search(p, ans, flags) for p in h["patrones"])} for h in e["hechos"]]
    citas = [{"patron": p, "ok": bool(re.search(p, ans, flags))} for p in e.get("citas", [])]
    prohib = [{"patron": p, "hit": bool(re.search(p, ans, flags))} for p in e.get("prohibidos", [])]
    cierre_ok = True
    if e.get("cierre", True):
        cierre_ok = bool(re.search(CIERRE_LIMITES, ans, flags) and re.search(CIERRE_FUENTES, ans, flags))
    ok = all(h["ok"] for h in hechos) and all(c["ok"] for c in citas) and not any(p["hit"] for p in prohib) and cierre_ok
    return {"ok": ok, "hechos": hechos, "citas": citas, "prohibidos": prohib, "cierre_ok": cierre_ok}


def judge(case: dict, ans: str, cwd: Path, timeout: int, model: str | None = None) -> tuple[dict, float]:
    prompt = (
        "Eres un evaluador de respuestas sobre la Reglamentación Térmica de Chile. El agente evaluado tenía acceso a "
        "fuentes verificadas (DS 15, tablas oficiales, decretos PDA) que tú no ves: NO penalices valores citados solo "
        "porque no puedes comprobarlos. Evalúa SOLO contra la rúbrica: información adicional que la rúbrica no menciona "
        "no es motivo de fallo por sí sola.\n"
        "Falla (pass=false) únicamente si: (a) contradice o no cubre lo esencial de la rúbrica; (b) reproduce texto, "
        "tablas o fórmulas de una norma NCh; (c) usa tablas FSEV/VIT para responder la RT; (d) faltan datos y no los "
        "pide ni declara supuestos; (e) afirma como cierto algo que la rúbrica dice que es falso.\n"
        'Devuelve SOLO un JSON {"pass": true|false, "score": 0..1, "motivo": "<= 2 frases"}.\n'
        f"Pregunta: {case['pregunta']}\nRúbrica: {case['rubrica']}\n\nRespuesta:\n<<<\n" + ans + "\n>>>")
    total = 0.0
    verdict = {"pass": False, "score": 0, "motivo": "sin JSON"}
    for _ in range(2):  # un reintento: un JSON mal formado del juez no dice nada sobre la respuesta
        out, cost = ask_judge(prompt, cwd, timeout, model or "sonnet")
        total += cost
        m = re.search(r"\{.*\}", out, re.S)
        try:
            verdict = json.loads(m.group(0)) if m else {"pass": False, "score": 0, "motivo": "sin JSON"}
        except json.JSONDecodeError:
            verdict = {"pass": False, "score": 0, "motivo": "JSON inválido"}
        if verdict.get("motivo") not in ("sin JSON", "JSON inválido"):
            break
    return verdict, total


def run_case(path: Path, args) -> dict:
    case = yaml.safe_load(path.read_text(encoding="utf-8"))
    wait_for_memory(args.min_free_gb)
    ws = workspace()
    try:
        ans, cost = ask(args.agent, case["pregunta"], ws, args.timeout, args.model)
        res = {"id": case["id"], "critical": case["critical"], "categoria": case["categoria"], "respuesta": ans,
               "costo_usd": cost, "reglas": grade_rules(case, ans)}
        if args.judge:
            j, jc = judge(case, ans, ws, args.timeout, args.judge_model)
            res["juez"], res["costo_usd"] = j, cost + jc
        res["pass"] = res["reglas"]["ok"] and (not args.judge or bool(res["juez"].get("pass")))
        return res
    except subprocess.TimeoutExpired:
        return {"id": case["id"], "critical": case["critical"], "categoria": case["categoria"], "pass": False,
                "error": "timeout", "costo_usd": 0}
    finally:
        shutil.rmtree(ws, ignore_errors=True)


def summarize(results: list[dict], args) -> str:
    crit = [r for r in results if r["critical"]]
    rest = [r for r in results if not r["critical"]]
    pc = 100 * sum(r["pass"] for r in crit) / len(crit) if crit else 100.0
    pr = 100 * sum(r["pass"] for r in rest) / len(rest) if rest else 100.0
    ok = pc == 100 and pr >= 95
    lines = [f"# Evals rt-chile — {dt.datetime.now():%Y-%m-%d %H:%M}", "",
             f"- Agente: `{args.agent}` modelo `{args.model or 'default'}` · juez LLM: "
             f"{'sí' if args.judge else 'no'} · casos: {len(results)}",
             f"- Versión de la skill: `{getattr(args, 'huella', None) or 'no registrada'}`",
             f"- **critical: {pc:.1f} %** ({sum(r['pass'] for r in crit)}/{len(crit)}) · **resto: {pr:.1f} %** "
             f"({sum(r['pass'] for r in rest)}/{len(rest)}) · **umbral {'CUMPLIDO' if ok else 'NO cumplido'}**",
             f"- Costo total: {sum(r.get('costo_usd', 0) for r in results):.2f} USD", "", "## Fallos", ""]
    for r in sorted(results, key=lambda r: (not r["critical"], r["id"])):
        if r["pass"]:
            continue
        why = r.get("error") or ""
        if "reglas" in r:
            g = r["reglas"]
            why = "; ".join([f"falta hecho: {h['descripcion']}" for h in g["hechos"] if not h["ok"]] +
                            [f"falta cita {c['patron']}" for c in g["citas"] if not c["ok"]] +
                            [f"prohibido {p['patron']}" for p in g["prohibidos"] if p["hit"]] +
                            ([] if g["cierre_ok"] else ["cierre incompleto"]) +
                            ([f"juez: {r['juez'].get('motivo', '')}"] if r.get("juez") and not r["juez"].get("pass") else []))
        lines.append(f"- {'**[critical]** ' if r['critical'] else ''}`{r['id']}`: {why}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="claude", choices=["claude", "opencode", "codex", "notebooklm"])
    ap.add_argument("--model", help="modelo del agente (en opencode: proveedor/modelo)")
    ap.add_argument("--judge-model", default="sonnet", help="modelo del juez (CLI liviano, sin herramientas)")
    ap.add_argument("--critical-only", action="store_true", help="solo casos critical (iteración barata)")
    ap.add_argument("--regrade", help="recalifica por reglas un .jsonl existente (sin llamar al agente; conserva el juez)")
    ap.add_argument("--rejudge", help="con --regrade: ids a recalificar también con el juez (coma) o 'fallos'; no llama al agente")
    ap.add_argument("--judge", action="store_true")
    ap.add_argument("--cases", help="ids separados por coma")
    ap.add_argument("--cases-dir", type=Path, default=CASES, help="carpeta de casos; evals/control mide sobreajuste")
    ap.add_argument("--prefix", help="solo casos cuyo id empieza con este prefijo (p.ej. g2)")
    ap.add_argument("--resume", help="continúa este .jsonl: conserva los casos con respuesta y corre los demás")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--min-free-gb", type=float, default=1.5, help="no lanza un caso si hay menos RAM disponible")
    args = ap.parse_args()
    if args.agent == "opencode" and not args.regrade and (viejas := copias_desactualizadas()):
        raise SystemExit("Copia instalada distinta del repo; la evaluación no mediría la versión actual: " + ", ".join(viejas) + ". Corre ./install.sh antes.")
    if args.regrade:
        cases = {p.stem: yaml.safe_load(p.read_text(encoding="utf-8")) for p in args.cases_dir.glob("*.yaml")}
        results = []
        for line in Path(args.regrade).read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if "respuesta" in r and r["id"] in cases:
                r["reglas"] = grade_rules(cases[r["id"]], r["respuesta"])
                r["pass"] = r["reglas"]["ok"] and ("juez" not in r or bool(r["juez"].get("pass")))
            results.append(r)
        if args.rejudge:
            want = None if args.rejudge == "fallos" else set(args.rejudge.split(","))
            ws = Path(tempfile.mkdtemp(prefix="rtchile-eval-"))
            for r in results:
                if "respuesta" in r and r["id"] in cases and (r["id"] in want if want else not r["pass"]):
                    r["juez"], jc = judge(cases[r["id"]], r["respuesta"], ws, args.timeout, args.judge_model)
                    r["costo_usd"] = r.get("costo_usd", 0) + jc
                    r["pass"] = r["reglas"]["ok"] and bool(r["juez"].get("pass"))
                    print(f"rejuzgado {r['id']}: {r['juez']}", flush=True)
            shutil.rmtree(ws, ignore_errors=True)
            with (RESULTS / (Path(args.regrade).stem + "_regrade.jsonl")).open("w", encoding="utf-8") as fh:
                fh.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in results)
        args.judge = any("juez" in r for r in results)
        original = Path(args.regrade).with_suffix(".md")  # recalificar no cambia la versión que respondió
        if original.exists() and (m := re.search(r"Versión de la skill: `(\w+)`", original.read_text(encoding="utf-8"))):
            args.huella = m[1]
        md = summarize(results, args).replace("# Evals rt-chile", f"# Evals rt-chile (recalificado de {Path(args.regrade).name})")
        out = RESULTS / (Path(args.regrade).stem + "_regrade.md")
        out.write_text(md, encoding="utf-8")
        print(md)
        return
    paths = sorted(args.cases_dir.glob("*.yaml"))
    args.huella = huella()
    if args.cases:
        want = set(args.cases.split(","))
        paths = [p for p in paths if p.stem in want]
    if args.prefix:
        paths = [p for p in paths if p.stem.startswith(args.prefix + "-")]
    if args.critical_only:
        paths = [p for p in paths if yaml.safe_load(p.read_text(encoding="utf-8"))["critical"]]
    RESULTS.mkdir(parents=True, exist_ok=True)
    results = []
    if args.resume:
        jsonl = Path(args.resume)
        stamp = jsonl.stem
        rows = [json.loads(line) for line in jsonl.read_text(encoding="utf-8").splitlines()]
        results = [r for r in rows if "respuesta" in r and not r["respuesta"].startswith("ERROR AGENTE")]
        jsonl.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in results), encoding="utf-8")
        done = {r["id"] for r in results}
        paths = [p for p in paths if p.stem not in done]
    else:
        # Incluye el agente: dos corridas en el mismo minuto no deben escribir en el mismo archivo
        stamp = f"{dt.datetime.now():%Y-%m-%d_%H%M}_{args.agent}" + ("_control" if args.cases_dir.name == "control" else "")
        jsonl = RESULTS / f"{stamp}.jsonl"
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex, jsonl.open("a", encoding="utf-8") as fh:
        # as_completed: guarda cada caso al terminar, aunque uno anterior siga corriendo
        for fut in cf.as_completed([ex.submit(run_case, p, args) for p in paths]):
            r = fut.result()
            results.append(r)
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            fh.flush()
            print(f"{r['id']}: {'OK' if r['pass'] else 'FALLA'} ({r.get('costo_usd', 0):.3f} USD)", flush=True)
    md = summarize(results, args)
    if huella() != args.huella:
        md = md.replace("## Fallos", "**INVÁLIDA: la skill cambió durante la corrida.**\n\n## Fallos", 1)
    (RESULTS / f"{stamp}.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
