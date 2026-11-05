"""Muestra al azar de casos aprobados para auditarlos a mano contra data/ y references/ (el juez no ve las fuentes).

Uso: .venv/bin/python evals/audit_sample.py evals/results/<archivo>.jsonl [--n 10] [--seed 1]
Escribe evals/results/auditoria-<archivo>.md con cada pregunta, rúbrica y respuesta, y un veredicto por completar.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("resultados")
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    path = Path(args.resultados)
    filas = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    aprobados = sorted((r for r in filas if r.get("pass")), key=lambda r: r["id"])
    muestra = sorted(random.Random(args.seed).sample(aprobados, min(args.n, len(aprobados))), key=lambda r: r["id"])
    out = [f"# Auditoría de {path.name}", "", f"Muestra: {len(muestra)} de {len(aprobados)} aprobados (semilla {args.seed}).",
           "Comparar cada cifra y cita con `data/` y `references/`. Veredicto: correcto, o el error y si es de la skill, del modelo o del caso.", ""]
    for r in muestra:
        caso = yaml.safe_load((ROOT / "cases" / f"{r['id']}.yaml").read_text(encoding="utf-8"))
        out += [f"## {r['id']}", "", f"**Pregunta:** {caso['pregunta']}", "", f"**Rúbrica:** {caso['rubrica']}", "", "**Veredicto:** por completar", "",
                "<details><summary>Respuesta</summary>", "", r["respuesta"], "", "</details>", ""]
    destino = path.parent / f"auditoria-{path.stem}.md"
    destino.write_text("\n".join(out), encoding="utf-8")
    print(destino)


if __name__ == "__main__":
    main()
