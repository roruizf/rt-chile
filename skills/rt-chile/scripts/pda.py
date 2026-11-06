"""Todas las exigencias de un PDA/PPA para vivienda: decreto (data/pda.csv) + actos MINVU (data/pda_minvu_actos.csv).

Uso:
  python pda.py Temuco                 # por comuna (usa data/pda_planes.csv)
  python pda.py pda-temuco-ds8-2025    # por plan_id
  python pda.py Temuco --json
Filtra SIEMPRE por plan_id (no por texto de las columnas): así no se pierden filas como tablas de muestra o
la HR de condensación, cuyo texto no repite el nombre del plan.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
DATA = Path(__file__).resolve().parents[1] / "data"


def _rows(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def planes_de(comuna_o_plan: str) -> list[dict]:
    planes = _rows("pda_planes.csv")
    ids = {p["plan_id"] for p in planes}
    if comuna_o_plan in ids:
        return [p for p in planes if p["plan_id"] == comuna_o_plan][:1]
    import zona
    c = zona.resolver_comuna(comuna_o_plan)
    return [p for p in planes if p["comuna"] == c]


def exigencias(plan_id: str) -> dict:
    dec = [r for r in _rows("pda.csv") if r["plan_id"] == plan_id]
    act = [r for r in _rows("pda_minvu_actos.csv") if r["plan_id"] == plan_id]
    return {"plan_id": plan_id, "decreto": dec, "actos_minvu": act}


COMPARABLES = [
    # (elemento, parámetro, patrón en los datos del plan, archivo DS 15, columna, tabla DS 15, el menor es más estricto)
    ("techumbre", "U", r"^(techo|techumbre)$", "ds15_t01_u_rt_residencial.csv", "techumbre_u", "Tabla 1", True),
    ("muro", "U", r"^muros?( perimetral(es)?)?$", "ds15_t01_u_rt_residencial.csv", "muro_u", "Tabla 1", True),
    ("piso ventilado", "U", r"^piso ventilado$", "ds15_t01_u_rt_residencial.csv", "piso_ventilado_u", "Tabla 1", True),
    ("puerta opaca", "U", r"^puertas?( opacas?)?$", "ds15_t01_u_rt_residencial.csv", "puerta_opaca_u", "Tabla 1", True),
    ("techumbre", "R100", r"^(techo|techumbre)$", "ds15_t02_r100_residencial.csv", "techumbre_r100", "Tabla 2", False),
    ("muro", "R100", r"^muros?( perimetral(es)?)?$", "ds15_t02_r100_residencial.csv", "muro_r100", "Tabla 2", False),
    ("piso ventilado", "R100", r"^piso ventilado$", "ds15_t02_r100_residencial.csv", "piso_ventilado_r100", "Tabla 2", False),
    ("sobrecimiento", "R100", r"^sobrecimientos?$", "ds15_t06_r100_sobrecimiento_residencial.csv", "sobrecimiento_r100", "Tabla 6", False),
]
RELACION = {"igual": "igual", "plan": "el plan es más estricto", "ds15": "**el 4.1.10 es más estricto**"}


def _numero(v: str) -> float | None:
    try:
        return float(str(v).replace(",", "."))
    except ValueError:
        return None


def _ultimo_valor(rows: list[dict], parametro: str, patron: str) -> dict | None:
    """Fila de la última etapa para vivienda nueva: las tablas del plan están en el orden del decreto."""
    filas = [r for r in rows if r["aplica_a"] in ("vivienda_nueva", "ambos") and r["parametro"] == parametro
             and re.match(patron, r["elemento"].strip().lower()) and "upvm" not in r["condicion"].lower()
             and _numero(r["valor"]) is not None]
    return filas[-1] if filas else None


def _relacion(plan: float, ds15: float, menor_estricto: bool) -> str:
    if plan == ds15:
        return "igual"
    return "plan" if (plan < ds15) == menor_estricto else "ds15"


def comparar(plan_id: str, zona: str, provincia: str) -> list[dict]:
    """Valor del plan frente al Art. 4.1.10 para una zona y provincia. Solo vivienda nueva; informativo."""
    ex = exigencias(plan_id)
    out = []
    for elemento, parametro, patron, archivo, columna, tabla, menor in COMPARABLES:
        ds15 = next((_numero(r[columna]) for r in _rows(archivo) if r["zona"] == zona), None)
        fila = _ultimo_valor(ex["decreto"], parametro, patron) or _ultimo_valor(ex["actos_minvu"], parametro, patron)
        if ds15 is None or fila is None:
            continue
        plan = _numero(fila["valor"])
        out.append({"elemento": elemento, "parametro": parametro, "plan": plan, "ds15": ds15, "tabla_ds15": tabla, "zona": zona,
                    "fuente_plan": f"{fila['decreto']}, {fila['articulo']}, {fila['tabla']}".rstrip(", "),
                    "relacion": _relacion(plan, ds15, menor)})
    ach = _ultimo_valor(ex["decreto"], "clase_infiltracion_ach50", r".*")
    ds15 = next((_numero(r["clase_infiltracion_ach50"]) for r in _rows("ds15_t07_t14_infiltracion_provincia.csv")
                 if r["provincia_tabla_zonas"] == provincia), None)
    if ach and ds15 is not None:
        plan = _numero(ach["valor"])
        out.append({"elemento": "infiltración", "parametro": "ach a 50 Pa", "plan": plan, "ds15": ds15, "tabla_ds15": "Tabla 7", "zona": zona,
                    "fuente_plan": f"{ach['decreto']}, {ach['articulo']}, {ach['tabla']}".rstrip(", "),
                    "relacion": _relacion(plan, ds15, True)})
    return out


def _zonas(plan_id: str, comuna: str | None = None) -> list[tuple[str, str, str, str]]:
    """(comuna, zona, condición, provincia) de las comunas del plan, o de una sola."""
    comunas = {p["comuna"] for p in _rows("pda_planes.csv") if p["plan_id"] == plan_id}
    if comuna:
        comunas &= {comuna}
    import zona as zmod
    resueltas = {zmod.resolver_comuna(c): c for c in comunas}
    return [(z["comuna"], z["zona"], z["condicion_original"], z["provincia"]) for z in _rows("zonas_comunas.csv") if z["comuna"] in resueltas]


def nota_4110(plan_id: str, comuna: str | None = None) -> str:
    """Nota informativa: de dónde sale cada valor y qué dice el 4.1.10, con los casos en que es más estricto."""
    combos = sorted({(z, c, pr) for _, z, c, pr in _zonas(plan_id, comuna)})
    if not combos:
        return ""
    out = ["## Comparación informativa con el Art. 4.1.10 (vivienda nueva, última etapa del plan)", "",
           "El inc. 2° remite al plan y no compara exigencias. Si el 4.1.10 es más estricto o hay ambigüedad, no hay interpretación "
           "oficial confirmada: se recomienda usar el valor más estricto o consultar a la DOM.", ""]
    vistos = set()
    for zona, condicion, provincia in combos:
        filas = comparar(plan_id, zona, provincia)
        clave = (zona, tuple(sorted((f["elemento"], f["parametro"], f["relacion"], f["ds15"]) for f in filas)))
        if clave in vistos:
            continue
        vistos.add(clave)
        out += [f"Zona {zona}" + (f" ({condicion})" if condicion else "") + ":"]
        out += [f"- {f['elemento']} {f['parametro']}: plan {f['plan']:g} ({f['fuente_plan']}); Art. 4.1.10 {f['ds15']:g} ({f['tabla_ds15']}): "
                f"{RELACION[f['relacion']]}" for f in filas]
        out.append("")
    return "\n".join(out)


def resumen(ex: dict) -> str:
    out = []
    for titulo, rows in (("Decreto", ex["decreto"]), ("Actos MINVU complementarios", ex["actos_minvu"])):
        if not rows:
            continue
        out.append(f"## {titulo} ({len(rows)} valores)")
        grupos = defaultdict(list)
        for r in rows:
            grupos[(r["decreto"], r["articulo"], r["tabla"], r["aplica_a"], r["etapa"])].append(r)
        for (dec, art, tab, ap, et), rs in grupos.items():
            out.append(f"\n### {art} {tab} — {dec} — aplica a: {ap}\n- Etapa: {et}")
            for r in rs:
                cond = f" [{r['condicion']}]" if r["condicion"] else ""
                detalle = [f"**{r['valor']}** {r['unidad']}".strip()] if r["valor"] else []
                detalle += [r["nota"]] if r["nota"] else []
                out.append(f"- {r['elemento']} · {r['parametro']}{cond}: " + " — ".join(detalle))
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("comuna_o_plan")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    planes = planes_de(a.comuna_o_plan)
    if not planes:
        print(f"Sin PDA/PPA registrado para {a.comuna_o_plan!r}: rige el Art. 4.1.10 (verificar en pda-ppa.md).")
        sys.exit(0)
    for p in planes:
        ex = exigencias(p["plan_id"])
        if a.json:
            print(json.dumps({"plan": p, **ex}, ensure_ascii=False, indent=2))
            continue
        print(f"# {p['nombre']} — {p['decreto']}\nCobertura: {p['cobertura']} · Exige envolvente: {p['exige_envolvente']}"
              + (f" · Nota: {p['nota']}" if p["nota"] else ""))
        print("Prevalece sobre el 4.1.10 solo en viviendas (inc. 2°). Lo no regulado por el plan: Art. 4.1.10 (criterio declarado).\n")
        ventilacion = [r for r in ex["decreto"] if r["aplica_a"] in ("vivienda_nueva", "ambos") and "higrostato" in r["nota"].lower()]
        if ventilacion:
            r = ventilacion[-1]
            print(f"**Ventilación propia del plan ({r['articulo']}):** {r['nota']}\n")
        print(resumen(ex) or "(el plan no fija exigencias de envolvente)")
        if p["exige_envolvente"] == "si":
            print("\n" + nota_4110(p["plan_id"], None if a.comuna_o_plan == p["plan_id"] else p["comuna"]))
