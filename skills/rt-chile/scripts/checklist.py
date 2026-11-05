"""Checklist de exigencias térmicas y documentos (permiso / recepción) para un proyecto.

Uso: python checklist.py proyecto.yaml   (o .json)
  uso: residencial | hotel | educacion | salud
  comuna: "Temuco"; altitud: 350 (opcional); lon_oeste: 72.6 (opcional)
  lote_viviendas: 24 (residencial; opcional)   recintos_docentes: 12 (educación; opcional)
Salida: Markdown con exigencias (A–D), vías, documentos y firmantes, con la fuente de cada ítem.
Se basa en references/roles-firmas-expediente.md y en zona.py. No reemplaza la revisión profesional.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import zona as zmod  # noqa: E402

TABLAS = {"residencial": ("Tabla 1", "Tabla 2", "Tablas 3–5 (% u Upvm)", "Tabla 6"),
          "hotel": ("Tabla 1", "Tabla 2", "Tabla 12 (U)", "Tabla 6"),
          "educacion": ("Tabla 10", "Tabla 11", "Tabla 12 (U)", "Tabla 13"),
          "salud": ("Tabla 10", "Tabla 11", "Tabla 12 (U)", "Tabla 13")}


def _load(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    if path.endswith((".yaml", ".yml")):
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


def muestra_residencial(lote: int | None) -> str:
    if lote is None:
        return "según Tabla 8 (indicar tamaño del lote)"
    if lote <= 10:
        return "lote ≤10: Tabla 8 no fija muestra (pendiente; supuesto: ≥1 vivienda); posible alternativa de sellos si no hay ensayadores en la región"
    if lote <= 50:
        return "2 viviendas (Tabla 8)"
    if lote <= 500:
        return "3 viviendas (Tabla 8)"
    return "5 viviendas (Tabla 8; lote 501 = brecha, supuesto 5)"


def muestra_educacion(n: int | None) -> str:
    if n is None:
        return "según Tabla 15 (indicar recintos docentes)"
    if n < 5:
        return "<5 recintos: Tabla 15 no fija muestra (pendiente)"
    return "2" if n <= 16 else "3" if n <= 24 else "4" if n <= 32 else "10 % de los recintos docentes"


def checklist(p: dict) -> str:
    uso = p["uso"]
    if uso not in TABLAS:
        raise ValueError("uso debe ser residencial, hotel, educacion o salud")
    z = zmod.zona(p["comuna"], p.get("altitud"), p.get("lon_oeste"))
    t_u, t_r, t_v, t_s = TABLAS[uso]
    zona_txt = z["zona"] or f"{z['estado']}: {', '.join(e['zona'] + ' (' + e['condicion'] + ')' for e in z['zonas_posibles']) or '—'}"
    out = [f"# Checklist térmico — {uso}, {z['comuna']} ({z['provincia']})", "",
           f"- **Zona térmica:** {zona_txt} — tabla MINVU de zonas",
           f"- **Infiltración máx. (provincia):** {z['infiltracion_ach50_max']} ach a 50 Pa — DS 15 Tablas 7/14"]
    pda_env = [x for x in z["pda"] if x["exige_envolvente"] == "si"]
    if pda_env and uso in ("residencial",):
        for x in pda_env:
            out.append(f"- **PDA/PPA:** {x['nombre']} ({x['decreto']}), cobertura {x['cobertura']} → **mandan sus tablas** "
                       "en lo que regulen (Art. 4.1.10 inc. 2°; data/pda.csv)")
    elif pda_env:
        out.append(f"- PDA/PPA presente ({pda_env[0]['nombre']}), pero el inc. 2° solo aplica a viviendas: rige el 4.1.10.")
    out += [f"- Avisos: {a}" for a in z["avisos"]]
    out += ["", "## Exigencias y documentos", "",
            "| Ex. | Qué | Vía / documento | Elabora · firma | Etapa |", "|---|---|---|---|---|",
            f"| A | Techumbre, muros, piso ventilado, puertas: U máx. ({t_u}) | R100 rotulado NCh 2251 ({t_r}) · ensayo NCh 851/3076 lab DS 10 ≤10 años · memoria NCh 853/3117/3137 · LOSCAT vigente | Profesional competente/especialista + **arquitecto** (memoria); lab DS 10 (ensayo) | Permiso |",
            f"| A | Ventanas: {t_v}; techumbre ≤3,6 (B–I) | Ensayo NCh 3076 · cálculo NCh 3137 · LOSCAT; informe por orientación (residencial) | Profesional + arquitecto | Permiso |",
            f"| A | Sobrecimiento R100 ({t_s}) | Aislante rotulado NCh 2251 · LOSCAT | Arquitecto (EETT) | Permiso |"]
    if uso == "hotel":
        out.append("| B, C, D | — | **Exento** (num. 1.B, 1.C, 1.D) | — | — |")
    else:
        out.append("| B | Sin riesgo de condensación (sup. + intersticial, con puente térmico) | **Memoria de cálculo** NCh 1973 + Res. Ex. 1802 (única vía) | Profesional + arquitecto | Permiso |")
        muestra = muestra_residencial(p.get("lote_viviendas")) if uso == "residencial" else (
            muestra_educacion(p.get("recintos_docentes")) if uso == "educacion" else "5 % de los recintos perimetrales acondicionados")
        out.append(f"| C | Infiltración envolvente ≤ clase provincial | **Ensayo en terreno NCh 3295**, obra terminada; muestra: {muestra} | Arquitecto, consultor DS 135 o lab DS 10 | **Recepción** |")
        out.append("| C | Permeabilidad puertas/ventanas ≥ clase por zona (Tablas 9/16) | Ensayo NCh 3296/3297 lab DS 10 · LOSCAT | Lab DS 10 | Permiso |")
        if uso == "salud":
            out.append("| D | — | **Eximida** (num. 2.D) | — | — |")
        else:
            norma = "NCh 3308" if uso == "educacion" else "NCh 3308/3309 según corresponda"
            out.append(f"| D | Tasa de ventilación ({norma}) | Informe de cumplimiento de tasa | Profesional (p.ej. ing. mecánico) + arquitecto | Permiso |")
    out += ["", "Documentos en permiso: OGUC Art. 5.1.6 N° 11. En recepción: Art. 5.2.6 N° 7 (+ ensayo de infiltración).",
            "", "> Orientación técnica; no reemplaza la revisión del profesional competente ni de la DOM. "
            "Verificar vigencia LOSCAT a la fecha y registros DS 10 / DS 135."]
    return "\n".join(out)


if __name__ == "__main__":
    print(checklist(_load(sys.argv[1])))
