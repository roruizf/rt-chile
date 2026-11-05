"""Transmitancia U de un complejo multicapa y comparación con la exigencia del Art. 4.1.10 (DS 15/2024).

Método propio (no reproduce la NCh 853): resistencias en serie con las resistencias superficiales del Anexo 2 de la
Res. Ex. 1802 y, para capas heterogéneas, promedio de los límites superior e inferior con control del error relativo
≤ 20 % (Res. Ex. 1802, num. 3). Las conductividades λ y las resistencias de cámaras de aire las ENTREGA EL USUARIO
(ficha técnica, NCh 853 en el visor oficial o un ensayo). Herramienta de apoyo, no reemplaza la Memoria de Cálculo.

Uso:
  python u_check.py complejo.json
  {"elemento": "muro" | "techumbre" | "piso_ventilado", "zona": "F", "uso": "residencial" | "educacion" | "salud" | "hotel",
   "secciones": [                                  # una sección = solución homogénea; varias = heterogénea
      {"fraccion": 0.85, "capas": [{"nombre": "yeso", "e_m": 0.015, "lambda": 0.26},
                                   {"nombre": "lana", "e_m": 0.08, "lambda": 0.04},
                                   {"nombre": "cámara", "R": 0.17}]},
      {"fraccion": 0.15, "capas": [...misma cantidad de capas, en el mismo orden...]}]}
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
ELEMENTO_RS = {"techumbre": "techo", "muro": "muro", "piso_ventilado": "piso_ventilado"}


def _rs() -> dict[str, tuple[float, float]]:
    with (DATA / "res1802_anexo2_rs.csv").open(encoding="utf-8") as f:
        return {r["elemento"]: (float(r["rsi_m2k_w"]), float(r["rse_m2k_w"])) for r in csv.DictReader(f)}


def exigencia(elemento: str, zona: str, uso: str) -> float | None:
    """U máx. según Tabla 1 (residencial y hotel) o Tabla 10 (educación y salud)."""
    tabla = "ds15_t10_u_rt_edu_salud.csv" if uso in ("educacion", "salud") else "ds15_t01_u_rt_residencial.csv"
    with (DATA / tabla).open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["zona"] == zona:
                v = r[f"{elemento}_u"]
                return float(v) if v else None
    raise ValueError(f"zona inválida: {zona}")


def r_capa(c: dict) -> float:
    if "R" in c:
        return float(c["R"])
    lam = float(c["lambda"])
    if lam <= 0:
        raise ValueError(f"λ debe ser > 0 en {c}")
    return float(c["e_m"]) / lam


def calcular(p: dict) -> dict:
    elemento = p["elemento"]
    rsi, rse = _rs()[ELEMENTO_RS[elemento]]
    secs = p["secciones"]
    fr = [float(s["fraccion"]) for s in secs]
    if abs(sum(fr) - 1) > 1e-6:
        raise ValueError(f"las fracciones deben sumar 1 (suman {sum(fr)})")
    n = {len(s["capas"]) for s in secs}
    if len(n) != 1:
        raise ValueError("todas las secciones deben tener la misma cantidad de capas, en el mismo orden")
    rt_sec = [rsi + rse + sum(r_capa(c) for c in s["capas"]) for s in secs]
    if len(secs) == 1:
        rt, err, sup, inf = rt_sec[0], 0.0, rt_sec[0], rt_sec[0]
    else:
        sup = 1 / sum(f / r for f, r in zip(fr, rt_sec))  # caminos en paralelo
        capas_eq = []
        for i in range(n.pop()):  # capas en serie, cada una con conductancia ponderada
            capas_eq.append(1 / sum(f / r_capa(s["capas"][i]) for f, s in zip(fr, secs)))
        inf = rsi + rse + sum(capas_eq)
        rt = (sup + inf) / 2
        err = (sup - inf) / (2 * rt)
    u = 1 / rt
    out = {"elemento": elemento, "Rsi": rsi, "Rse": rse, "Rt": round(rt, 3), "U": round(u, 3),
           "limite_superior_Rt": round(sup, 3), "limite_inferior_Rt": round(inf, 3), "error_relativo": round(err, 3),
           "calculo_valido": err <= 0.20 + 1e-9, "avisos": []}
    if not out["calculo_valido"]:
        out["avisos"].append("Error relativo > 20 %: usar el método detallado de la NCh 853 o acreditar por R100 "
                             "(Res. Ex. 1802 num. 3).")
    if "zona" in p:
        uso = p.get("uso", "residencial")
        umax = exigencia(elemento, p["zona"].upper(), uso)
        out.update({"zona": p["zona"].upper(), "uso": uso, "U_max": umax,
                    "fuente_exigencia": "DS 15 Tabla 10" if uso in ("educacion", "salud") else "DS 15 Tabla 1",
                    "cumple": None if umax is None else u <= umax + 1e-9})
        if uso in ("residencial", "hotel"):
            out["avisos"].append("Si la vivienda está en zona PDA, mandan las tablas del plan (pda-ppa.md).")
    return out


if __name__ == "__main__":
    print(json.dumps(calcular(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))), ensure_ascii=False, indent=2))
