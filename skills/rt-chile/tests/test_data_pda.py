"""Integridad de data/pda.csv y data/pda_planes.csv (decretos MMA, actos públicos)."""
import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "skills" / "rt-chile" / "data"
H = "plan_id,decreto,articulo,tabla,aplica_a,etapa,elemento,parametro,condicion,valor,unidad,nota".split(",")


def rows(n):
    with (DATA / n).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ids():
    return {s["id"] for s in yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]}


def test_pda_schema_and_ids():
    with (DATA / "pda.csv").open(encoding="utf-8") as f:
        assert next(csv.reader(f)) == H
    rs = rows("pda.csv")
    assert len(rs) == 650
    assert {r["plan_id"] for r in rs} <= ids()
    assert len({r["plan_id"] for r in rs}) == 11
    for r in rs:
        assert r["articulo"].startswith("Art.") and r["aplica_a"] in ("vivienda_nueva", "vivienda_existente", "ambos")
        if r["parametro"] == "U" and r["valor"] and r["valor"][0].isdigit():
            assert 0.1 <= float(r["valor"]) <= 6, r


def _u(plan, tabla):
    return {r["elemento"]: r["valor"] for r in rows("pda.csv")
            if r["plan_id"] == plan and r["tabla"] == tabla and r["parametro"] == "U"}


def test_control_values_confirmed_against_decrees():
    t = _u("pda-temuco-ds8-2025", "Tabla N° 10")
    assert (t["techo"], t["muro"], t["piso ventilado"], t["ventana"], t["puerta"]) == ("0.28", "0.45", "0.50", "3.20", "1.70")
    o = _u("pda-ohiggins-ds1-2021", "Tabla 7")
    assert (o["techo"], o["muro"], o["piso ventilado"], o["puerta"]) == ("0.38", "0.80", "0.60", "1.70")
    ta = _u("pda-talca-ds49-2016", "Tabla Nº 10")
    assert (ta["techo"], ta["muro"], ta["piso ventilado"]) == ("0.38", "0.80", "0.60")


def test_planes_comunas_exist_and_ids():
    zonas = {r["comuna"] for r in rows("zonas_comunas.csv")}
    pl = rows("pda_planes.csv")
    assert {r["plan_id"] for r in pl} <= ids()
    for r in pl:
        assert r["comuna"].startswith("*") or r["comuna"] in zonas, r
        assert r["exige_envolvente"] in ("si", "no") and r["cobertura"] in ("total", "parcial")
    q = {r["comuna"] for r in pl if r["plan_id"] == "ppa-quillota-ds18-2023"}
    assert "Limache" not in q and "Calera" in q  # C26


def test_minvu_actos():
    rs = rows("pda_minvu_actos.csv")
    with (DATA / "pda_minvu_actos.csv").open(encoding="utf-8") as f:
        assert next(csv.reader(f)) == H
    assert len(rs) == 454
    assert {r["plan_id"] for r in rs} <= ids() | {"minvu-oficios-pda"}
    r100 = {r["plan_id"]: r["valor"] for r in rs if "209" in r["decreto"] and r["parametro"] == "R100"}
    assert r100["pda-talca-ds49-2016"] == "45" and r100["pda-temuco-ds8-2025"] == "91"


def _pda():
    import importlib.util
    spec = importlib.util.spec_from_file_location("pda", ROOT / "skills" / "rt-chile" / "scripts" / "pda.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_comparar_detecta_cuando_el_4110_es_mas_estricto():
    filas = {(f["elemento"], f["parametro"]): f for f in _pda().comparar("pda-talca-ds49-2016", "D", "Talca")}
    piso = filas[("piso ventilado", "R100")]
    assert (piso["plan"], piso["ds15"], piso["relacion"]) == (150, 167, "ds15")
    assert filas[("piso ventilado", "U")]["relacion"] == "igual"


def test_comparar_zona_alta_de_plan_parcial():
    filas = {(f["elemento"], f["parametro"]): f for f in _pda().comparar("pda-ohiggins-ds1-2021", "H", "Cachapoal")}
    assert (filas[("muro", "U")]["plan"], filas[("muro", "U")]["ds15"], filas[("muro", "U")]["relacion"]) == (0.8, 0.3, "ds15")


def test_valores_iguales_en_temuco_y_valdivia_final():
    p = _pda()
    assert {f["relacion"] for f in p.comparar("pda-temuco-ds8-2025", "F", "Cautín")} == {"igual"}
    assert {(f["plan"]) for f in p.comparar("pda-valdivia-ds25-2016", "G", "Valdivia") if f["elemento"] == "piso ventilado" and f["parametro"] == "U"} == {0.39}


def test_nota_4110_avisa_y_recomienda_el_mas_estricto():
    nota = _pda().nota_4110("pda-talca-ds49-2016")
    assert "plan 150" in nota and "Art. 4.1.10 167" in nota and "más estricto" in nota


def test_los_11_planes_registran_la_ventilacion_del_plan():
    planes = {r["plan_id"] for r in rows("pda_planes.csv") if r["exige_envolvente"] == "si"}
    con_ventilacion = {r["plan_id"] for r in rows("pda.csv") if "higrostato" in r["nota"].lower()}
    assert planes <= con_ventilacion, planes - con_ventilacion
