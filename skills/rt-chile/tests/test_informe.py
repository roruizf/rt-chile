"""scripts/informe.py: valores contra data/ y casos que no deben dar un resultado falso."""
import datetime as dt
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import informe  # noqa: E402

HOY = dt.date(2026, 11, 5)
MURO = {"elemento": "muro", "capas": [{"nombre": "aislante", "e_m": 0.1, "lambda": 0.04, "fuente": "ficha"}]}  # U = 0,375


def gen(**kw):
    return informe.generar({"nombre": "P", "uso": "residencial", "comuna": "Santiago", **kw}, HOY)


def test_ejemplo_genera_todas_las_secciones():
    txt = informe.generar(yaml.safe_load((ROOT / "examples/proyecto-ejemplo.yaml").read_text(encoding="utf-8")), HOY)
    for titulo in ("## 1. Resumen", "## 2. Datos", "## 3. Envolvente", "## 4. Ventanas", "## 5. Exigencias", "## 6. Supuestos", "## 7. Límites"):
        assert titulo in txt
    assert "No se firma".lower() in txt.lower() and "https://normastecnicas.minvu.cl/" in txt
    assert "| Sur | 3,6 | 53,33 | 40 | **No cumple** |" in txt  # DS 15 Tabla 3, zona D, Sur, U ≤ 3,6
    assert "| Poniente | 3,6 | 45 | 53 | Cumple |" in txt  # fila O-P


def test_nunca_declara_cumplimiento_global():
    txt = gen(elementos=[MURO])
    assert "no declara que el proyecto cumpla" in txt
    assert "| B. Condensación | Por acreditar" in txt and "| C. Infiltración | Por acreditar" in txt


def test_zona_multizona_no_inventa_verificacion():
    txt = informe.generar({"nombre": "P", "uso": "residencial", "comuna": "Arica", "elementos": [MURO]}, HOY)
    assert "la zona térmica no está determinada" in txt and "## 3. Envolvente" not in txt
    assert "Altitud o meridiano" in txt


def test_pda_prevalece_en_vivienda_y_no_en_otros_usos():
    base = {"nombre": "P", "comuna": "Temuco", "elementos": [MURO]}
    viv = informe.generar({**base, "uso": "residencial"}, HOY)
    assert "son **las del plan**" in viv
    assert "mandan sus tablas" in viv and "| Muro perimetral | 0,375 | 0,45 | DS" in viv  # DS 8/2023 Tabla N° 10
    ventanas = {"orientaciones": [{"orientacion": "Norte", "sup_paramentos_m2": 30, "sup_ventanas_m2": 9, "u_ventana": 2.8}]}
    assert "**Revisar con el plan**" in informe.generar({**base, "uso": "residencial", "ventanas": ventanas}, HOY)
    edu = informe.generar({**base, "uso": "educacion"}, HOY)
    assert "solo aplica a viviendas" in edu and "DS 15 Tabla 10" in edu


def test_limite_pda_con_etapas_usa_el_mas_exigente():
    lim = informe.limite_pda("pda-valdivia-ds25-2016", "piso_ventilado")
    assert lim["valor"] == 0.39 and lim["varias_etapas"] and "16b" in lim["fuente"]  # 0,50 en la etapa anterior


def test_hotel_exento_y_ventana_tabla_12():
    txt = informe.generar({"nombre": "H", "uso": "hotel", "comuna": "Valparaíso", "ventanas": {"u_ventana": 3.0}}, HOY)
    assert "| B, C y D | Exento" in txt and "U máx. 3,6" in txt and "Cumple" in txt  # zona C, Tabla 12


def test_salud_eximida_de_ventilacion():
    assert "| D. Ventilación | Eximida" in informe.generar({"nombre": "S", "uso": "salud", "comuna": "Santiago"}, HOY)


def test_faltantes_y_supuestos_quedan_declarados():
    sin_fuente = {"elemento": "muro", "capas": [{"nombre": "lana", "e_m": 0.1, "lambda": 0.04}]}
    txt = gen(elementos=[sin_fuente])
    assert "sin fuente declarada en lana" in txt and "Elementos no entregados: Techumbre, Piso ventilado" in txt
    assert "**Falta dato**" in gen()


def test_ingreso_anterior_al_ds15_se_advierte():
    assert "anterior al 28-11-2025" in gen(fecha_ingreso="2025-01-15")


def test_datos_invalidos_fallan_con_mensaje():
    with pytest.raises(ValueError):
        informe.generar({"nombre": "P", "uso": "bodega", "comuna": "Santiago"}, HOY)
    with pytest.raises(ValueError):
        gen(elementos=[{"elemento": "losa", "u_declarado": 1}])
