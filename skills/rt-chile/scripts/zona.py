"""Comuna (+ altitud, + meridiano) → zona térmica, provincia, clase de infiltración, PDA/PPA y clima de condensación.

Datos (actos públicos, verificados): data/zonas_comunas.csv (tabla MINVU), data/ds15_t07_t14_infiltracion_provincia.csv,
data/pda_planes.csv, data/res1802_anexo1_clima.csv.

Uso:
  python zona.py "Los Andes" [--altitud 2100] [--lon 70.5]
  (--lon = longitud OESTE en grados decimales, p.ej. 71°15' = 71.25)
Salida JSON. Si la comuna tiene varias zonas y falta el dato, devuelve todos los escenarios.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
ALIAS = {"aysen": "Aisén", "coyhaique": "Coihaique", "lacalera": "Calera", "sanvicentedetaguatagua": "San Vicente"}


def _key(s: str) -> str:
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode())


def _rows(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


ZONAS = _rows("zonas_comunas.csv")
NOMBRES = {_key(r["comuna"]): r["comuna"] for r in ZONAS}
INFIL = {r["provincia_tabla_zonas"]: r for r in _rows("ds15_t07_t14_infiltracion_provincia.csv")}
PDA = _rows("pda_planes.csv")
CLIMA = _rows("res1802_anexo1_clima.csv")


def resolver_comuna(nombre: str) -> str:
    k = _key(nombre)
    if k in ALIAS:
        return ALIAS[k]
    if k in NOMBRES:
        return NOMBRES[k]
    cand = [v for kk, v in NOMBRES.items() if k and (k in kk or kk in k)]
    if len(cand) == 1:
        return cand[0]
    raise ValueError(f"comuna no encontrada en la tabla MINVU: {nombre!r}" + (f" (¿{', '.join(cand)}?)" if cand else ""))


def _en_rango(v: float | None, lo: str, lo_inc: str, hi: str, hi_inc: str) -> bool | None:
    """True/False si se puede decidir; None si la condición existe y falta el dato."""
    if not lo and not hi:
        return True
    if v is None:
        return None
    if lo and (v < float(lo) or (v == float(lo) and lo_inc == "0")):
        return False
    if hi and (v > float(hi) or (v == float(hi) and hi_inc == "0")):
        return False
    return True


def zona(comuna: str, altitud: float | None = None, lon_oeste: float | None = None) -> dict:
    c = resolver_comuna(comuna)
    filas = [r for r in ZONAS if r["comuna"] == c]
    avisos, escenarios, match = [], [], []
    for r in filas:
        a = _en_rango(altitud, r["alt_min"], r["alt_min_incl"], r["alt_max"], r["alt_max_incl"])
        g = _en_rango(lon_oeste, r["lon_oeste_min"], r["lon_oeste_min_incl"], r["lon_oeste_max"], r["lon_oeste_max_incl"])
        esc = {"zona": r["zona"], "condicion": r["condicion_original"] or "toda la comuna"}
        if a is False or g is False:
            continue
        (match if (a and g) else escenarios).append(esc)
    if len(match) == 1 and not escenarios:
        estado = "determinada"
    elif len(match) > 1:
        estado = "traslape"
        avisos.append("La tabla oficial asigna más de una zona a este punto: declarar el traslape; supuesto conservador = "
                      "la más exigente (zonificacion.md).")
    elif escenarios:
        estado = "faltan_datos"
        avisos.append("Comuna multizona: indicar altitud (msnm) y/o meridiano, o responder por escenarios.")
    else:
        estado = "sin_zona"
        avisos.append("La tabla oficial no asigna zona para estos datos (brecha). Consultar DOM/DITEC (zonificacion.md).")
    prov = filas[0]["provincia"]
    inf = INFIL.get(prov)
    pdas = [{"plan_id": p["plan_id"], "nombre": p["nombre"], "decreto": p["decreto"],
             "exige_envolvente": p["exige_envolvente"], "cobertura": p["cobertura"], "nota": p["nota"]}
            for p in PDA if p["comuna"] == c or (p["comuna"] == "*Región Metropolitana"
                                                and filas[0]["region"].startswith("Metropolitana"))]
    if any(p["cobertura"] == "parcial" for p in pdas):
        avisos.append("PDA con cobertura parcial: verificar si el terreno está dentro del polígono de zona saturada.")
    zonas_ok = {e["zona"] for e in match} or {e["zona"] for e in escenarios}
    clima = [{"zona": r["zona"], "particularidad": r["particularidad"] == "1", "condicion": r["condicion"],
              "t_ext_c": float(r["t_ext_c"]), "hr_ext_pct": int(r["hr_ext_pct"])}
             for r in CLIMA if r["comuna_zonas"] == c and r["zona"] in zonas_ok]
    if not clima:
        avisos.append("Clima de condensación: sin fila propia en el Anexo 1; usar el grupo o 'Todas las comunas' "
                      "de la zona (exigencias-B-condensacion.md).")
    return {"comuna": c, "region": filas[0]["region"], "provincia": prov, "estado": estado,
            "zona": match[0]["zona"] if estado == "determinada" else None,
            "zonas_posibles": match or escenarios,
            "infiltracion_ach50_max": (inf["clase_infiltracion_ach50"] or "sin exigencia") if inf else None,
            "pda": pdas, "clima_condensacion": clima,
            "fuentes": ["Tabla MINVU zonas (ds15-tabla-zonas)", "DS 15 Tablas 7/14", "decretos PDA (pda_planes.csv)",
                        "Res. Ex. 1802 Anexo 1"],
            "avisos": avisos}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("comuna")
    ap.add_argument("--altitud", type=float)
    ap.add_argument("--lon", type=float, help="longitud oeste, grados decimales")
    a = ap.parse_args()
    print(json.dumps(zona(a.comuna, a.altitud, a.lon), ensure_ascii=False, indent=2))
