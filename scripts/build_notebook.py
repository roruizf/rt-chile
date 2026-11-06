"""Genera el material del notebook de NotebookLM desde el manifiesto y data/ (sin copiar a mano).

Escribe notebooklm/fuentes.md, notebooklm/tablas-ds15.md y notebooklm/tablas-pda.md. Solo incluye actos públicos y
publicaciones MINVU `verified` y resúmenes propios: nunca normas NCh.
Uso: .venv/bin/python scripts/build_notebook.py
     .venv/bin/python scripts/build_notebook.py --verificar <notebook_id>

--verificar lee el texto de cada fuente del notebook y sale con código 1 si alguna quedó vacía, con texto de error,
duplicada o si el total no calza. El estado "ready" de NotebookLM no prueba que una fuente tenga contenido.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "rt-chile"
OUT = ROOT / "notebooklm"
sys.path.insert(0, str(SKILL / "scripts"))
import pda as pmod  # noqa: E402

# Reemplazadas o de apoyo: subirlas confunde al notebook sin agregar exigencias vigentes
EXCLUIR = {"loscat-e13", "manual-cev-2019", "planilla-ventilacion-nch3309-v31", "planilla-ventilacion-nch3309-v31-2018", "minvu-comunicado-rt"}
TABLAS_DS15 = [
    ("Tabla 1: U y Rt, residencial y hoteles", "ds15_t01_u_rt_residencial.csv"),
    ("Tabla 2: R100, residencial y hoteles", "ds15_t02_r100_residencial.csv"),
    ("Tabla 3: % máximo de ventanas, residencial", "ds15_t03_ventanas_pct_residencial.csv"),
    ("Tabla 4: orientaciones", "ds15_t04_orientaciones.csv"),
    ("Tabla 5: Upvm, residencial", "ds15_t05_upvm_residencial.csv"),
    ("Tabla 6: R100 de sobrecimiento, residencial y hoteles", "ds15_t06_r100_sobrecimiento_residencial.csv"),
    ("Tablas 7 y 14: infiltración por provincia (ach a 50 Pa)", "ds15_t07_t14_infiltracion_provincia.csv"),
    ("Tabla 8: muestra de infiltración, residencial", "ds15_t08_muestra_infiltracion_residencial.csv"),
    ("Tablas 9 y 16: clase mínima de permeabilidad por zona", "ds15_t09_t16_permeabilidad_zona.csv"),
    ("Tabla 10: U y Rt, educación y salud", "ds15_t10_u_rt_edu_salud.csv"),
    ("Tabla 11: R100, educación y salud", "ds15_t11_r100_edu_salud.csv"),
    ("Tabla 12: U de ventanas, educación, salud y hoteles", "ds15_t12_ventanas_edu_salud_hoteles.csv"),
    ("Tabla 13: R100 de sobrecimiento, educación y salud", "ds15_t13_r100_sobrecimiento_edu_salud.csv"),
    ("Tabla 15: muestra de infiltración, educación", "ds15_t15_muestra_infiltracion_educacion.csv"),
]
AVISO = "Generado desde el repo rt-chile; no editar a mano. Verificar siempre en la fuente oficial."
MIN_CARACTERES = 1000
# Se buscan solo al inicio: una norma larga puede contener estas palabras sin ser una página de error
ERRORES = re.compile(r"request could not be satisfied|403 error|404 not found|access denied|service unavailable"
                     r"|enable javascript|este proceso demora demasiado|protegido por recaptcha", re.I)
INICIO_ERROR = 2000
# En un PDF escaneado, el texto completo trae solo la URL y el identificador de cada imagen de página
# Escaneos aceptados por el mantenedor: el chat lee sus imágenes y no se les agrega OCR, que puede alterar cifras.
# Sus valores están verificados en data/. La excepción cubre solo la falta de texto, no un texto de error.
SOLO_IMAGEN = {"res-ex-1802-2025.pdf", "pdao-ord840-2019-con-ord209.pdf", "pdao-criterios-art-6-7-8.pdf",
               "pdao-criterio-ganancias-solares.pdf"}
RELLENO = re.compile(r"https?://\S+|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")


def tabla_md(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as fh:
        filas = list(csv.reader(fh))
    return ["| " + " | ".join(filas[0]) + " |", "|" + "---|" * len(filas[0]),
            *["| " + " | ".join(c or "—" for c in f) + " |" for f in filas[1:]]]


def oficiales() -> list[list[dict]]:
    """Fuentes oficiales por subir, agrupadas por archivo: dos IDs con el mismo PDF son una sola fuente."""
    data = yaml.safe_load((ROOT / "sources/manifest.yaml").read_text(encoding="utf-8"))["sources"]
    grupos: dict[str, list[dict]] = {}
    for s in data:
        if s.get("status") == "verified" and s.get("license") in ("public-act", "minvu-pub") \
                and s.get("scope") != "out" and s["id"] not in EXCLUIR:
            grupos.setdefault(s.get("local") or s["id"], []).append(s)
    return list(grupos.values())


def referencias() -> list[str]:
    return sorted(p.name for p in (SKILL / "references").glob("*.md"))


def total_esperado() -> int:
    return len(oficiales()) + len(referencias()) + 2


def fuentes() -> str:
    sel = oficiales()
    refs = referencias()
    out = ["# Fuentes del notebook", "", AVISO, "",
           f"Total: {len(sel)} oficiales + {len(refs)} resúmenes propios + 2 tablas = {total_esperado()} fuentes (revisar el límite de fuentes de tu plan de NotebookLM).",
           "", "**Nunca subir normas NCh**, aunque vengan del visor MINVU. Los resúmenes propios no contienen su texto.", "",
           "## 1. Fuentes oficiales", "",
           "Subir el archivo de `sources/private/` cuando exista: algunos enlaces cargan una página de error o de espera.", "",
           "| ID | Título | Enlace oficial | Archivo |", "|---|---|---|---|"]
    for grupo in sel:
        for s in grupo:
            out.append(f"| `{s['id']}` | {' '.join(str(s['title']).split())} | {s.get('mirror') or s.get('url')} | {s.get('local') or '—'} |")
    out += ["", "Después de subirlas, correr `scripts/build_notebook.py --verificar <notebook_id>`.", "",
            "## 2. Resúmenes propios (`skills/rt-chile/references/`)", "",
            "Incluyen los métodos en palabras propias, y `normas-nch.md` resume el rol de cada NCh sin su texto.", ""]
    out += [f"- `{r}`" for r in refs]
    out += ["", "## 3. Tablas en texto (`notebooklm/`)", "",
            "Las tablas del DS 15 son imágenes en el PDF, y NotebookLM puede leerlas mal. Estos archivos las entregan como texto.", "",
            "- `tablas-ds15.md`", "- `tablas-pda.md`", ""]
    return "\n".join(out)


def tablas_ds15() -> str:
    out = ["# Tablas del Art. 4.1.10 OGUC (DS 15/2024)", "", AVISO, "", "U en W/m²K; Rt en m²K/W; R100 = Rt × 100. Fuente: DS 15/2024, D.O. 27-05-2024.", ""]
    for titulo, archivo in TABLAS_DS15:
        out += [f"## {titulo}", "", *tabla_md(SKILL / "data" / archivo), ""]
    return "\n".join(out + clima_anexo1())


def clima_anexo1() -> list[str]:
    """Una línea autosuficiente por localidad: el PDF es escaneado y una tabla perdería su encabezado al recuperarse."""
    with (SKILL / "data" / "res1802_anexo1_clima.csv").open(encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    out = ["## Res. Ex. 1802, Anexo 1: clima exterior para el cálculo de condensación", "",
           "Temperatura y humedad relativa exterior por comuna o localidad. Transcrito del PDF escaneado y revisado contra sus imágenes.", ""]
    for f in filas:
        cond = f", condición {f['condicion']}" if f["condicion"] else ""
        part = " (p)" if f["particularidad"] != "0" else ""
        out.append(f"- {' '.join(f['localidad'].split())}, zona {f['zona']}{part}{cond}: T° exterior {f['t_ext_c'].replace('.', ',')} °C, HR exterior {f['hr_ext_pct']} %")
    return out + [""]


def tablas_pda() -> str:
    with (SKILL / "data" / "pda_planes.csv").open(encoding="utf-8") as fh:
        planes = list(csv.DictReader(fh))
    out = ["# Exigencias térmicas de los PDA/PPA", "", AVISO, "", "Prevalecen sobre el 4.1.10 solo en viviendas (inc. 2°).", ""]
    vistos = set()
    for p in planes:
        if p["plan_id"] in vistos or p["exige_envolvente"] != "si":
            continue
        vistos.add(p["plan_id"])
        comunas = ", ".join(x["comuna"] for x in planes if x["plan_id"] == p["plan_id"])
        out += [f"# {p['nombre']}: {p['decreto']}", "", f"Comunas: {comunas}", "", pmod.resumen(pmod.exigencias(p["plan_id"])), "", pmod.nota_4110(p["plan_id"]), ""]
    return "\n".join(out)


def defecto(titulo: str, texto: str) -> str | None:
    """Motivo por el que una fuente no sirve, o None si tiene contenido."""
    if ERRORES.search(texto[:INICIO_ERROR]) or titulo.upper().startswith("ERROR"):
        return "texto de error"
    util = len(" ".join(RELLENO.sub(" ", texto).split()))
    if util < MIN_CARACTERES and titulo not in SOLO_IMAGEN:
        return f"solo {util} caracteres de texto (mínimo {MIN_CARACTERES})"
    return None


def _cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["notebooklm", *args], capture_output=True, text=True)


def verificar(notebook: str, cli=_cli, esperado: int | None = None) -> list[str]:
    """Lista los problemas de contenido del notebook; vacía si todo está bien."""
    r = cli("source", "list", "-n", notebook, "--json")
    if r.returncode:
        return [f"no se pudo listar el notebook: {r.stderr.strip() or r.stdout.strip()}"]
    lista = json.loads(r.stdout)["sources"]
    esperado = total_esperado() if esperado is None else esperado
    problemas = [] if len(lista) == esperado else [f"hay {len(lista)} fuentes y se esperaban {esperado}"]
    problemas += [f"duplicada: {t} ({n} veces)" for t, n in Counter(s["title"] for s in lista).items() if n > 1]
    with tempfile.TemporaryDirectory() as tmp:
        for s in lista:
            ruta = Path(tmp) / f"{s['id']}.txt"
            r = cli("source", "fulltext", s["id"], "-n", notebook, "-o", str(ruta), "--force", "--json")
            if r.returncode or not ruta.exists():
                problemas.append(f"{s['title']}: no se pudo leer su texto")
                continue
            motivo = defecto(s["title"], ruta.read_text(encoding="utf-8"))
            if motivo:
                problemas.append(f"{s['title']}: {motivo}")
    return problemas


def main() -> None:
    if "--verificar" in sys.argv:
        problemas = verificar(sys.argv[sys.argv.index("--verificar") + 1])
        for p in problemas:
            print("DEFECTO", p)
        print("Fuentes con contenido: OK" if not problemas else f"{len(problemas)} problema(s)")
        sys.exit(1 if problemas else 0)
    OUT.mkdir(exist_ok=True)
    for nombre, texto in (("fuentes.md", fuentes()), ("tablas-ds15.md", tablas_ds15()), ("tablas-pda.md", tablas_pda())):
        (OUT / nombre).write_text(texto, encoding="utf-8")
        print(nombre, len(texto.splitlines()), "líneas")


if __name__ == "__main__":
    main()
