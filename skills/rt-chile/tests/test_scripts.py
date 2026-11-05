"""Tests unitarios de los scripts de mantención de fuentes (no requieren PDFs privados)."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def _load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_loscat_code_regex_and_chapter():
    m = _load("loscat_diff")
    text = "1.1.M.B1.2.1 Losa ... 3.2.V.A.0.12 ventana ... 3.1.P.M.0.04 puerta"
    assert set(m.CODE.findall(text)) == {"1.1.M.B1.2.1", "3.2.V.A.0.12", "3.1.P.M.0.04"}
    assert m.chapter("3.2.V.A.0.12") == "Ventanas"
    assert m.chapter("1.2.G.A1.1") == "Muros"


def test_source_ids_num_pattern():
    import re

    m = _load("source_ids")
    pat = re.compile(m.PATTERNS["num"])
    assert pat.search("ORDEN GENERAL Núm. 43.860 | Lunes ... Núm. 15. Visto:").group(1) == "15"
