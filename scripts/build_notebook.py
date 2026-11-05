"""Genera el material del notebook de NotebookLM desde el manifiesto y data/ (sin copiar a mano).

Escribe notebooklm/fuentes.md, notebooklm/tablas-ds15.md y notebooklm/tablas-pda.md. Solo incluye actos públicos y
publicaciones MINVU `verified` y resúmenes propios: nunca normas NCh.
Uso: .venv/bin/python scripts/build_notebook.py
"""
from __future__ import annotations

import csv
import sys
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


def tabla_md(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as fh:
        filas = list(csv.reader(fh))
    return ["| " + " | ".join(filas[0]) + " |", "|" + "---|" * len(filas[0]),
            *["| " + " | ".join(c or "—" for c in f) + " |" for f in filas[1:]]]


def fuentes() -> str:
    data = yaml.safe_load((ROOT / "sources/manifest.yaml").read_text(encoding="utf-8"))["sources"]
    sel = [s for s in data if s.get("status") == "verified" and s.get("license") in ("public-act", "minvu-pub")
           and s.get("scope") != "out" and s["id"] not in EXCLUIR]
    refs = sorted(p.name for p in (SKILL / "references").glob("*.md"))
    out = ["# Fuentes del notebook", "", AVISO, "",
           f"Total: {len(sel)} oficiales + {len(refs)} resúmenes propios + 2 tablas = {len(sel) + len(refs) + 2} fuentes (revisar el límite de fuentes de tu plan de NotebookLM).",
           "", "**Nunca subir normas NCh**, aunque vengan del visor MINVU. Los resúmenes propios no contienen su texto.", "",
           "## 1. Fuentes oficiales", "", "| ID | Título | Enlace |", "|---|---|---|"]
    out += [f"| `{s['id']}` | {' '.join(str(s['title']).split())} | {s.get('mirror') or s.get('url')} |" for s in sel]
    out += ["", "Si un enlace no se puede cargar, subir la copia de `sources/private/` que indica el manifiesto.", "",
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
    return "\n".join(out)


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
        out += [f"# {p['nombre']}: {p['decreto']}", "", f"Comunas: {comunas}", "", pmod.resumen(pmod.exigencias(p["plan_id"])), ""]
    return "\n".join(out)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for nombre, texto in (("fuentes.md", fuentes()), ("tablas-ds15.md", tablas_ds15()), ("tablas-pda.md", tablas_pda())):
        (OUT / nombre).write_text(texto, encoding="utf-8")
        print(nombre, len(texto.splitlines()), "líneas")


if __name__ == "__main__":
    main()
