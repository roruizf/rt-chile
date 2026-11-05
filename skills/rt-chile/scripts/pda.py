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
                nota = f" — {r['nota']}" if r["nota"] else ""
                out.append(f"- {r['elemento']} · {r['parametro']}{cond}: **{r['valor']}** {r['unidad']}{nota}")
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
        print("Prevalece sobre el 4.1.10 solo en viviendas (inc. 2°). Lo no regulado por el plan: Art. 4.1.10.\n")
        print(resumen(ex) or "(el plan no fija exigencias de envolvente)")
