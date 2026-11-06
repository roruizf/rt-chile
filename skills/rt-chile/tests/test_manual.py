"""El manual no puede desalinearse de los datos ni citar archivos que no existen."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs"
MANUAL = (DOCS / "manual.md").read_text(encoding="utf-8")


def _coma(valor: str) -> str:
    return valor.replace(".", ",") if valor else "—"


def test_tabla_de_zonas_coincide_con_el_ds15():
    with (ROOT / "skills/rt-chile/data/ds15_t01_u_rt_residencial.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            fila = f"| {r['zona']} | {_coma(r['techumbre_u'])} | {_coma(r['muro_u'])} | {_coma(r['piso_ventilado_u'])} | {_coma(r['puerta_opaca_u'])} |"
            assert fila in MANUAL, fila


def test_enlaces_relativos_y_scripts_existen():
    for destino in re.findall(r"\]\((?!https?://|#)([^)#]+)\)", MANUAL):
        assert (DOCS / destino).exists(), destino
    for script in re.findall(r"`(\w+\.py)`", MANUAL):
        assert (ROOT / "skills/rt-chile/scripts" / script).exists(), script


def test_anclas_internas_existen():
    titulos = {re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-") for t in re.findall(r"^#+ (.+)$", MANUAL, re.M)}
    for ancla in re.findall(r"\]\(#([^)]+)\)", MANUAL):
        assert ancla in titulos, ancla


def test_readme_enlaza_el_manual():
    assert "docs/manual.md" in (ROOT / "README.md").read_text(encoding="utf-8")
