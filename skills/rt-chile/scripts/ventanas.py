"""Verifica el complejo de ventanas residencial (Art. 4.1.10 num. 1.A.5, DS 15/2024).

Opción 1: % máximo de ventanas por orientación según el U de la ventana (Tabla 3).
Opción 2 (zonas B–I): U ponderado ventana + muro, Upvm (Tabla 5).
Datos: skills/rt-chile/data/ds15_t03_*.csv y ds15_t05_*.csv (acto público, verificados).

Uso:
  python ventanas.py proyecto.json
  {"zona": "D", "opcion": "pct" | "upvm", "exposicion_muros_pct": 100,
   "orientaciones": [{"orientacion": "Norte", "sup_paramentos_m2": 40, "sup_ventanas_m2": 12,
                      "u_ventana": 2.8, "u_muro": 0.6}, ...]}
  "sup_paramentos_m2" es la suma de las superficies INTERIORES de los paramentos verticales de esa orientación:
  incluye medianeros en la opción pct y los excluye en la opción upvm (DS 15, 1.A.5 c/b).
  Orientaciones válidas: Norte, Oriente, Sur, Poniente (Oriente y Poniente usan la fila "O-P"), u OGT.
Salida: JSON con el resultado por orientación. Es una herramienta de apoyo, no un informe firmado.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
FILA = {"Norte": "Norte", "Oriente": "O-P", "Poniente": "O-P", "Sur": "Sur", "OGT": "OGT"}


def _tabla(nombre: str) -> dict[tuple[str, str], dict[float, str]]:
    out = {}
    with (DATA / nombre).open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[(r["zona"], r["orientacion"])] = {float(k[5:]): v for k, v in r.items() if k.startswith("u_le_")}
    return out


T3 = _tabla("ds15_t03_ventanas_pct_residencial.csv")
T5 = _tabla("ds15_t05_upvm_residencial.csv")


def columna_u(u_ventana: float, columnas: list[float]) -> float | None:
    """Primera columna 'U ≤ x' que contiene el U de la ventana (None si supera la última)."""
    for x in sorted(columnas):
        if u_ventana <= x + 1e-9:
            return x
    return None


def azimut_a_orientacion(azimut: float) -> str:
    """Tabla 4: N [315,45), O [45,135), S [135,225), P [225,315); 0° = norte geográfico."""
    a = azimut % 360
    if a >= 315 or a < 45:
        return "Norte"
    if a < 135:
        return "Oriente"
    if a < 225:
        return "Sur"
    return "Poniente"


def pct_max(zona: str, orientacion: str, u_ventana: float) -> float | None:
    fila = T3[(zona, FILA[orientacion])]
    col = columna_u(u_ventana, list(fila))
    return None if col is None else float(fila[col])


def upvm_max(zona: str, orientacion: str, u_ventana: float) -> float | None:
    if orientacion == "OGT":
        raise ValueError("La Tabla 5 no tiene fila OGT")
    fila = T5[(zona, FILA[orientacion])]
    col = columna_u(u_ventana, list(fila))
    if col is None or fila[col] in ("na", ""):
        return None
    return float(fila[col])


def verificar(p: dict) -> dict:
    zona, opcion = p["zona"].upper(), p.get("opcion", "pct")
    if zona not in "ABCDEFGHI" or len(zona) != 1:
        raise ValueError(f"zona inválida: {zona}")
    if opcion == "upvm" and zona == "A":
        raise ValueError("Upvm solo se permite en zonas B a I (DS 15, 1.A.5)")
    avisos = []
    orients = p["orientaciones"]
    if opcion == "pct" and p.get("exposicion_muros_pct", 100) < 60:
        # menos del 60 % expuesto: solo OGT sobre el total de paramentos
        avisos.append("Exposición < 60 %: se aplica solo la fila OGT sobre el total de paramentos (1.A.5).")
        orients = [{"orientacion": "OGT",
                    "sup_paramentos_m2": sum(o["sup_paramentos_m2"] for o in orients),
                    "sup_ventanas_m2": sum(o["sup_ventanas_m2"] for o in orients),
                    "u_ventana": max(o["u_ventana"] for o in orients)}]
    res = []
    for o in orients:
        ori = o["orientacion"]
        if ori not in FILA:
            raise ValueError(f"orientación inválida: {ori}")
        sp, sv, uv = float(o["sup_paramentos_m2"]), float(o["sup_ventanas_m2"]), float(o["u_ventana"])
        if opcion == "pct":
            lim = pct_max(zona, ori, uv)
            smv = None if lim is None else sp * lim / 100
            ok = smv is not None and sv <= smv + 1e-9
            res.append({"orientacion": ori, "u_ventana": uv, "pct_max": lim, "SMV_m2": smv,
                        "sup_ventanas_m2": sv, "pct_proyecto": round(100 * sv / sp, 2) if sp else None,
                        "cumple": ok, "fuente": "DS 15 Tabla 3"})
        else:
            um = float(o["u_muro"])
            sm = sp - sv
            if sm < 0:
                raise ValueError(f"{ori}: superficie de ventanas mayor que la de paramentos")
            upvm = (um * sm + uv * sv) / (sm + sv) if (sm + sv) else 0.0
            lim = upvm_max(zona, ori, uv)
            res.append({"orientacion": ori, "u_ventana": uv, "u_muro": um, "Upvm": round(upvm, 3),
                        "Upvm_max": lim, "cumple": lim is not None and upvm <= lim + 1e-9,
                        "fuente": "DS 15 Tabla 5"})
        if res[-1]["cumple"] is False and (res[-1].get("pct_max") is None and res[-1].get("Upvm_max") is None):
            avisos.append(f"{ori}: U de ventana {uv} fuera del rango de la tabla (o 'na').")
    if zona != "A":
        avisos.append("Recordar: ventanas en techumbre (≤60°) en zonas B–I deben tener U ≤ 3,6 W/m²K.")
    if opcion == "upvm":
        avisos.append("Upvm: el muro debe cumplir además la Tabla 1 por sí solo; paramentos sin medianeros.")
    return {"zona": zona, "opcion": opcion, "resultado": res,
            "cumple_todo": all(r["cumple"] for r in res), "avisos": avisos}


if __name__ == "__main__":
    print(json.dumps(verificar(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))),
                     ensure_ascii=False, indent=2))
