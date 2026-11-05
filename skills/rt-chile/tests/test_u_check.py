import importlib.util
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location("u_check", Path(__file__).resolve().parents[1] / "scripts" / "u_check.py")
u = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(u)

# λ ilustrativos entregados "por el usuario" (no provienen de la NCh 853)
YESO = {"e_m": 0.015, "lambda": 0.25}
LANA = {"e_m": 0.10, "lambda": 0.04}
OSB = {"e_m": 0.011, "lambda": 0.10}


def test_homogenea_a_mano():
    # Rt = 0.13 + 0.06 + 2.5 + 0.11 + 0.04 = 2.84 -> U = 0.352
    r = u.calcular({"elemento": "muro", "zona": "F", "secciones": [{"fraccion": 1, "capas": [YESO, LANA, OSB]}]})
    assert r["Rt"] == pytest.approx(2.84, abs=1e-3) and r["U"] == pytest.approx(0.352, abs=1e-3)
    assert r["U_max"] == 0.45 and r["cumple"] is True


def test_exigencias_por_uso():
    assert u.exigencia("muro", "D", "residencial") == 0.80
    assert u.exigencia("muro", "D", "educacion") == 0.60   # Tabla 10 difiere en muros
    assert u.exigencia("muro", "D", "hotel") == 0.80       # hotel = residencial (Tabla 1)
    assert u.exigencia("techumbre", "H", "salud") == 0.25
    assert u.exigencia("puerta_opaca", "A", "residencial") is None


def test_heterogenea_limites():
    pie = {"e_m": 0.10, "lambda": 0.13}  # pie derecho de madera en la capa de aislación
    r = u.calcular({"elemento": "muro", "secciones": [
        {"fraccion": 0.85, "capas": [YESO, LANA, OSB]},
        {"fraccion": 0.15, "capas": [YESO, pie, OSB]}]})
    assert r["limite_superior_Rt"] >= r["Rt"] >= r["limite_inferior_Rt"]
    assert r["calculo_valido"] and 0 <= r["error_relativo"] <= 0.2


def test_techo_usa_rsi_ascendente_y_educacion():
    r = u.calcular({"elemento": "techumbre", "zona": "D", "uso": "educacion",
                    "secciones": [{"fraccion": 1, "capas": [{"R": 2.4}]}]})
    assert r["Rsi"] == 0.10 and r["Rt"] == pytest.approx(2.54) and r["U_max"] == 0.38 and r["cumple"] is False


def test_validaciones():
    with pytest.raises(ValueError):
        u.calcular({"elemento": "muro", "secciones": [{"fraccion": 0.5, "capas": [YESO]}]})
