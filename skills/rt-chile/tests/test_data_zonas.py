"""Integridad de data/zonas_comunas.csv (derivado de la tabla oficial MINVU, ver scripts/build_zonas_csv.py)."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CSV = ROOT / "skills" / "rt-chile" / "data" / "zonas_comunas.csv"


def _rows():
    with CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_shape():
    rows = _rows()
    assert len(rows) == 410
    assert len({(r["region"], r["comuna"]) for r in rows}) == 345
    assert {r["zona"] for r in rows} == set("ABCDEFGHI")
    for r in rows:
        assert r["region"] and r["provincia"] and r["comuna"]
        for k in ("alt_min_incl", "alt_max_incl", "lon_oeste_min_incl", "lon_oeste_max_incl"):
            assert r[k] in ("", "0", "1")


def test_known_rows_from_official_table():
    by = defaultdict(set)
    for r in _rows():
        by[r["comuna"]].add((r["zona"], r["alt_min"], r["alt_max"], r["lon_oeste_min"], r["lon_oeste_max"]))
    assert by["Arica"] == {("A", "", "1100", "", ""), ("B", "1100", "3000", "", ""), ("H", "3000", "", "", "")}
    assert ("I", "", "", "", "") in by["Punta Arenas"]
    assert by["Isla de Pascua"] == {("A", "", "", "", "")}
    assert ("A", "", "", "70.7333", "") in by["Copiapó"]  # > 70° 44' W
    assert by["Antuco"] == {("F", "", "1000", "", ""), ("H", "1000", "", "", "")}


def test_no_hyphen_artifacts():
    for r in _rows():
        assert "- " not in r["provincia"] and "- " not in r["comuna"], r
