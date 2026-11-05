import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "ventanas", Path(__file__).resolve().parents[1] / "scripts" / "ventanas.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def test_columna_u():
    cols = [0.6, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 4.4, 5.8]
    assert v.columna_u(2.8, cols) == 2.8
    assert v.columna_u(2.81, cols) == 3.2
    assert v.columna_u(6.0, cols) is None


def test_azimut():
    assert [v.azimut_a_orientacion(a) for a in (0, 44.9, 45, 134, 135, 224, 225, 314, 315)] == \
        ["Norte", "Norte", "Oriente", "Oriente", "Sur", "Sur", "Poniente", "Poniente", "Norte"]


def test_pct_zona_d():
    # D, Norte, U 2.8 -> 83 % (Tabla 3); Sur U 2.8 -> 48 %
    assert v.pct_max("D", "Norte", 2.8) == 83
    assert v.pct_max("D", "Poniente", 2.8) == 60
    r = v.verificar({"zona": "D", "orientaciones": [
        {"orientacion": "Norte", "sup_paramentos_m2": 40, "sup_ventanas_m2": 30, "u_ventana": 2.8},
        {"orientacion": "Sur", "sup_paramentos_m2": 40, "sup_ventanas_m2": 20, "u_ventana": 2.8}]})
    norte, sur = r["resultado"]
    assert norte["cumple"] and abs(norte["SMV_m2"] - 33.2) < 1e-9
    assert not sur["cumple"] and abs(sur["SMV_m2"] - 19.2) < 1e-9


def test_ogt_cuando_exposicion_menor_60():
    r = v.verificar({"zona": "F", "exposicion_muros_pct": 50, "orientaciones": [
        {"orientacion": "Norte", "sup_paramentos_m2": 30, "sup_ventanas_m2": 5, "u_ventana": 2.0},
        {"orientacion": "Sur", "sup_paramentos_m2": 30, "sup_ventanas_m2": 4, "u_ventana": 2.4}]})
    (ogt,) = r["resultado"]
    assert ogt["orientacion"] == "OGT" and ogt["pct_max"] == 28  # F OGT U<=2.4
    assert ogt["cumple"]  # 9 m2 <= 60*0.28=16.8


def test_upvm():
    # zona D, Norte, U ventana 2.8 -> Upvm máx 2.46; muro 0.6 40 m2 total, 10 m2 ventana
    r = v.verificar({"zona": "D", "opcion": "upvm", "orientaciones": [
        {"orientacion": "Norte", "sup_paramentos_m2": 40, "sup_ventanas_m2": 10, "u_ventana": 2.8, "u_muro": 0.6}]})
    (o,) = r["resultado"]
    assert o["Upvm_max"] == 2.46 and abs(o["Upvm"] - 1.15) < 1e-9 and o["cumple"]


def test_upvm_na_y_zona_a():
    assert v.upvm_max("B", "Norte", 0.6) is None  # 'na'
    with pytest.raises(ValueError):
        v.verificar({"zona": "A", "opcion": "upvm", "orientaciones": []})
