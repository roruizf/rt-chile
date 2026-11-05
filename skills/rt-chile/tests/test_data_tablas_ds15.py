"""Integridad de las tablas del DS 15 transcritas a data/ds15_t*.csv (valores de acto público).

Controles de transcripción: Rt ≈ 1/U, R100 = Rt·100, monotonía de la Tabla 3, y verificación literal
contra las láminas DITEC cuando la copia privada existe (si no, se omite).
"""
import csv
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "skills" / "rt-chile" / "data"
PRIV = ROOT / "sources" / "private"
ZONAS = list("ABCDEFGHI")


def rows(name):
    with (DATA / f"{name}.csv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


@pytest.mark.parametrize("name", ["ds15_t01_u_rt_residencial", "ds15_t10_u_rt_edu_salud"])
def test_u_rt_inverse(name):
    rs = rows(name)
    assert [r["zona"] for r in rs] == ZONAS
    for r in rs:
        for el in ("techumbre", "muro", "piso_ventilado", "puerta_opaca"):
            u, rt = r[f"{el}_u"], r[f"{el}_rt"]
            if not u:
                assert r["zona"] == "A" and el == "puerta_opaca" and not rt
                continue
            assert abs(1 / float(u) - float(rt)) <= 0.011, (name, r["zona"], el)


@pytest.mark.parametrize("t_u,t_r", [("ds15_t01_u_rt_residencial", "ds15_t02_r100_residencial"),
                                     ("ds15_t10_u_rt_edu_salud", "ds15_t11_r100_edu_salud")])
def test_r100_equals_rt_times_100(t_u, t_r):
    for ru, rr in zip(rows(t_u), rows(t_r)):
        for el in ("techumbre", "muro", "piso_ventilado"):
            assert round(float(ru[f"{el}_rt"]) * 100) == int(rr[f"{el}_r100"]), (t_r, ru["zona"], el)


def test_t12_u_rt_inverse():
    for r in rows("ds15_t12_ventanas_edu_salud_hoteles"):
        assert abs(1 / float(r["ventana_u"]) - float(r["ventana_rt"])) <= 0.011, r


def test_t03_shape_and_monotonic():
    rs = rows("ds15_t03_ventanas_pct_residencial")
    assert len(rs) == 36
    for r in rs:
        vals = [int(v) for k, v in r.items() if k.startswith("u_le_")]
        assert all(0 <= v <= 100 for v in vals)
        assert vals == sorted(vals, reverse=True), (r["zona"], r["orientacion"])


def test_t05_zones_b_to_i():
    rs = rows("ds15_t05_upvm_residencial")
    assert sorted({r["zona"] for r in rs}) == ZONAS[1:]
    assert len(rs) == 24


def test_sobrecimientos_equal_6_13():
    assert rows("ds15_t06_r100_sobrecimiento_residencial") == rows("ds15_t13_r100_sobrecimiento_edu_salud")


def test_t10_differs_from_t01_only_in_walls():
    for a, b in zip(rows("ds15_t01_u_rt_residencial"), rows("ds15_t10_u_rt_edu_salud")):
        diff = {k for k in a if a[k] != b[k]}
        assert diff <= {"muro_u", "muro_rt"}, (a["zona"], diff)


@pytest.mark.skipif(not (PRIV / "ditec-lamina-puertas-ventanas.pdf").exists(), reason="copia privada ausente")
@pytest.mark.parametrize("name,fmt", [("ds15_t03_ventanas_pct_residencial", "{}%"),
                                      ("ds15_t05_upvm_residencial", "{}")])
def test_cross_check_lamina_ditec(name, fmt):
    import pymupdf

    text = re.sub(r"\s+", " ", " ".join(p.get_text() for p in pymupdf.open(PRIV / "ditec-lamina-puertas-ventanas.pdf")))
    for r in rows(name):
        seq = " ".join(fmt.format(v.replace(".", ",")) for k, v in r.items() if k.startswith("u_le_"))
        assert seq in text, (name, r["zona"], r["orientacion"])


def test_res1802_anexo2_and_macrozonas():
    rs = {r["elemento"]: r for r in rows("res1802_anexo2_rs")}
    assert (rs["techo"]["rsi_m2k_w"], rs["muro"]["rsi_m2k_w"], rs["piso_ventilado"]["rsi_m2k_w"]) == ("0.10", "0.13", "0.17")
    assert {r["rse_m2k_w"] for r in rs.values()} == {"0.04"}
    mz = {r["macrozona"]: (float(r["t_ext_c"]), int(r["hr_ext_pct"])) for r in rows("res1802_macrozonas")}
    assert mz["F/G"] == (3.5, 98) and mz["H/I"] == (-1.6, 93) and mz["H/I(p)"] == (-5.6, 86)
    assert all(0 < hr <= 100 for _, hr in mz.values())


def test_res1802_anexo1_clima():
    a = rows("res1802_anexo1_clima")
    assert len(a) == 423
    zonas = {(r["comuna"], r["zona"]): r["condicion_original"] for r in rows("zonas_comunas")}
    com = [r for r in a if r["tipo"] == "comuna"]
    assert len(com) == 409
    for r in com:  # cada comuna del Anexo 1 existe con esa zona en la tabla oficial, con la misma condición
        assert (r["comuna_zonas"], r["zona"]) in zonas, r
        assert r["condicion"] == zonas[(r["comuna_zonas"], r["zona"])], r
    for r in a:
        assert -10 < float(r["t_ext_c"]) < 20 and 0 < int(r["hr_ext_pct"]) <= 100, r
        assert r["particularidad"] in ("0", "1")
    # cobertura: toda comuna-zona de la tabla de zonas tiene fila propia, salvo Juan Fernández (grupo de islas C(p))
    covered = {(r["comuna_zonas"], r["zona"]) for r in com}
    assert set(zonas) - covered == {("Juan Fernández", "C")}
    by = {(r["localidad"], r["zona"]): (r["t_ext_c"], r["hr_ext_pct"]) for r in a}
    assert by[("Isla de Pascua", "A")] == ("16", "85")
    assert by[("Punta Arenas", "I")] == ("-1.6", "93")
    assert by[("San José de Maipo", "D")] == ("1.8", "90")
    assert by[("Antártica chilena", "I")] == ("-6.8", "88")


def test_infiltracion_provincias_cover_zone_table():
    t7 = rows("ds15_t07_t14_infiltracion_provincia")
    assert {r["provincia_tabla_zonas"] for r in t7} == {r["provincia"] for r in rows("zonas_comunas")}
    assert len(t7) == 56
    assert {r["clase_infiltracion_ach50"] for r in t7} == {"", "4.00", "5.00", "8.00"}
    assert {r["provincia"] for r in t7 if not r["clase_infiltracion_ach50"]} == {
        "Arica", "Iquique", "Tocopilla", "Chañaral", "Isla de Pascua"}


def test_permeabilidad_and_muestras():
    perm = {r["zona"]: r["clase_permeabilidad_min_100pa"] for r in rows("ds15_t09_t16_permeabilidad_zona")}
    assert perm == {"A": "", "B": "1", "C": "1", "D": "2", "E": "2", "F": "2", "G": "3", "H": "3", "I": "3"}
    t8 = rows("ds15_t08_muestra_infiltracion_residencial")
    assert [(r["lote_min"], r["tamano_muestra"]) for r in t8] == [("11", "2"), ("51", "3"), ("502", "5")]
    t15 = rows("ds15_t15_muestra_infiltracion_educacion")
    assert [r["tamano_muestra"] for r in t15] == ["2", "3", "4", "10%"]


def test_loscat_indice():
    rs = rows("loscat_e14_indice")
    assert len(rs) == 348 and len({r["codigo"] for r in rs}) == 348
    assert {r["vigencia_fuente"] for r in rs} <= {"ficha", "indice", "no_extraida"}
    for r in rs:
        if r["vigencia_hasta"]:
            assert re.fullmatch(r"20\d\d-\d\d", r["vigencia_hasta"]), r
            assert r["vigencia_fuente"] != "no_extraida"
    opacos = [r for r in rs if r["capitulo"] in ("Muros", "Pisos ventilados")]
    assert all(r["vigencia_hasta"] for r in opacos)
