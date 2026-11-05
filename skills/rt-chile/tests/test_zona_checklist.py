import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(n):
    spec = importlib.util.spec_from_file_location(n, SCRIPTS / f"{n}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


z = _load("zona")
c = _load("checklist")


@pytest.mark.parametrize("args,estado,zona", [
    (("Arica", 500), "determinada", "A"),
    (("Arica", 1500), "determinada", "B"),
    (("Arica", 3200), "determinada", "H"),
    (("Punta Arenas",), "determinada", "I"),
    (("Putre", 2500), "sin_zona", None),          # brecha de la tabla oficial
    (("Antuco", 1000), "sin_zona", None),         # límites estrictos en 1.000
    (("Copiapó", 4000, 71.0), "traslape", None),  # A por meridiano y H por altitud
])
def test_zona_casos(args, estado, zona):
    r = z.zona(*args)
    assert r["estado"] == estado and r["zona"] == zona


def test_zona_multizona_sin_altitud_y_alias():
    r = z.zona("Los Andes")
    assert r["estado"] == "faltan_datos" and {e["zona"] for e in r["zonas_posibles"]} == {"D", "H"}
    assert z.zona("Aysén")["comuna"] == "Aisén"
    assert z.zona("la calera")["comuna"] == "Calera"
    with pytest.raises(ValueError):
        z.zona("Gotham")


def test_zona_pda_e_infiltracion():
    t = z.zona("Temuco")
    assert [p["plan_id"] for p in t["pda"]] == ["pda-temuco-ds8-2025"] and t["infiltracion_ach50_max"] == "5.00"
    assert z.zona("Angol")["infiltracion_ach50_max"] == "5.00"   # Malleco (C24)
    assert z.zona("Limache")["pda"] == []                         # C26
    assert z.zona("Mostazal")["pda"][0]["cobertura"] == "parcial"
    assert z.zona("Arica", 100)["infiltracion_ach50_max"] == "sin exigencia"


def test_checklist_exenciones():
    hotel = c.checklist({"uso": "hotel", "comuna": "Valparaíso"})
    assert "Exento" in hotel and "NCh 3295" not in hotel
    salud = c.checklist({"uso": "salud", "comuna": "Talca"})
    assert "Eximida" in salud and "inc. 2° solo aplica a viviendas" in salud
    viv = c.checklist({"uso": "residencial", "comuna": "Temuco", "lote_viviendas": 30})
    assert "mandan sus tablas" in viv and "2 viviendas (Tabla 8)" in viv and "NCh 3308/3309" in viv
    edu = c.checklist({"uso": "educacion", "comuna": "Osorno", "recintos_docentes": 20})
    assert "| D | Tasa de ventilación (NCh 3308)" in edu and "Tabla 10" in edu


def test_pda_script_trae_todo_temuco():
    p = _load("pda")
    (plan,) = p.planes_de("Padre Las Casas")
    ex = p.exigencias(plan["plan_id"])
    tablas = {r["tabla"] for r in ex["decreto"]}
    assert "Tabla Nº 14" in tablas  # muestra propia del plan (no la Tabla 8 del DS 15)
    assert any(r["articulo"] == "Art. 27 N°2" and r["valor"] == "76" for r in ex["decreto"])  # HR condensación
    assert any("9868" in r["decreto"] for r in ex["actos_minvu"])
    assert p.planes_de("Limache") == []
