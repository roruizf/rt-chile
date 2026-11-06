"""Valida los casos de evals/cases/ contra evals/schema.yaml (estructura y regex compilables)."""
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[3]
CASES = sorted((ROOT / "evals" / "cases").glob("*.yaml")) + sorted((ROOT / "evals" / "control").glob("*.yaml"))
CATS = {"zona", "exigencia", "pda", "vias", "cev", "hotel", "salud", "firmas", "trampa", "fuera-alcance", "supuestos",
        "copyright", "vigencia", "infiltracion", "condensacion", "ventilacion", "control"}


def _ids():
    return {s["id"] for s in yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]}


def test_hay_casos():
    assert CASES


@pytest.mark.parametrize("path", CASES, ids=[p.stem for p in CASES])
def test_caso(path):
    c = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert c["id"] == path.stem and re.fullmatch(r"[a-z0-9-]+-\d{2}", c["id"])
    assert c["categoria"] in CATS and isinstance(c["critical"], bool)
    assert len(c["pregunta"]) > 10 and c["rubrica"]
    e = c["esperado"]
    assert e["hechos"] or e.get("prohibidos")
    for h in e["hechos"]:
        assert h["descripcion"] and h["patrones"]
        for p in h["patrones"]:
            re.compile(p)
    for p in e.get("citas", []) + e.get("prohibidos", []):
        re.compile(p)
    ids = _ids()
    for f in c["fuentes"]:
        assert f in ids or (ROOT / "skills" / "rt-chile" / f).exists(), f
