"""Borrador de informe térmico de un proyecto (Art. 4.1.10 OGUC, DS 15/2024, y PDA/PPA).

Reúne zona.py, pda.py, u_check.py, ventanas.py y checklist.py en un Markdown editable. No emite un veredicto global:
informa el estado de cada verificación, lo que falta y qué documento debe elaborar cada profesional. Es un borrador
de trabajo: no es una memoria de cálculo ni reemplaza al profesional competente, y no se firma.

Uso: python informe.py proyecto.yaml [--salida informe.md]     (ver examples/proyecto-ejemplo.yaml)

  nombre: "Casa Ejemplo"            # obligatorio
  uso: residencial                  # residencial | hotel | educacion | salud
  comuna: "Temuco"                  # obligatorio
  altitud: 350                      # opcional; exigida en comunas multizona
  lon_oeste: 72.6                   # opcional; exigida en comunas multizona por meridiano
  fecha_ingreso: 2026-11-05         # ingreso del permiso a la DOM; opcional
  lote_viviendas: 24                # residencial; opcional
  recintos_docentes: 12             # educación; opcional
  elementos:                        # opcional; U calculada con las λ que ENTREGA EL USUARIO, con su fuente
    - elemento: muro                # muro | techumbre | piso_ventilado
      capas:                        # o "secciones" (ver u_check.py) para una solución heterogénea
        - {nombre: "Yeso-cartón", e_m: 0.0125, lambda: 0.25, fuente: "ficha del fabricante"}
    - elemento: techumbre
      u_declarado: 0.28             # alternativa al cálculo: U ya acreditado
      acreditacion: "LOSCAT, código de la ficha, vigencia"
  ventanas:                         # opcional. Residencial: por orientación. Hotel, educación, salud: solo u_ventana
    opcion: pct                     # pct | upvm
    exposicion_muros_pct: 100
    orientaciones:
      - {orientacion: Norte, sup_paramentos_m2: 40, sup_ventanas_m2: 12, u_ventana: 2.8}
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checklist as chk  # noqa: E402
import pda as pmod  # noqa: E402
import u_check as ucheck  # noqa: E402
import ventanas as vmod  # noqa: E402
import zona as zmod  # noqa: E402

DATA = Path(__file__).resolve().parents[1] / "data"
VERIFICADO = "2026-11-05"  # fecha de la última verificación del corpus de la skill
VIGENCIA_DS15 = dt.date(2025, 11, 28)
NOMBRE = {"muro": "Muro perimetral", "techumbre": "Techumbre", "piso_ventilado": "Piso ventilado"}
PATRON_PDA = {"muro": r"^muros?( perimetral(es)?)?$", "techumbre": r"^(techo|techumbre)$", "piso_ventilado": r"^piso ventilado$"}
FUENTES = [
    ("DS 15/2024 en el Diario Oficial", "https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf"),
    ("Reglamentación térmica, MINVU", "https://www.minvu.gob.cl/nueva-reglamentacion-termica/"),
    ("LOSCAT y listados DITEC", "https://www.minvu.gob.cl/ditec/"),
    ("Planes de descontaminación, MMA", "https://ppda.mma.gob.cl/"),
    ("Visor de normas NCh, MINVU", "https://normastecnicas.minvu.cl/"),
]


def limite_pda(plan_id: str, elemento: str) -> dict | None:
    """Límite U del plan para vivienda nueva; con varias etapas devuelve el más exigente y lo declara."""
    filas = []
    for r in pmod.exigencias(plan_id)["decreto"]:
        if r["aplica_a"] not in ("vivienda_nueva", "ambos") or r["parametro"] != "U" or "upvm" in r["condicion"].lower():
            continue
        if not re.match(PATRON_PDA[elemento], r["elemento"].strip().lower()):
            continue
        try:
            filas.append((float(r["valor"].replace(",", ".")), r))
        except ValueError:
            continue
    if not filas:
        return None
    valor, r = min(filas, key=lambda x: x[0])
    return {"valor": valor, "fuente": f"{r['decreto']}, {r['articulo']}, {r['tabla']}".rstrip(", "),
            "varias_etapas": len({f[0] for f in filas}) > 1}


def u_max_tabla12(zona: str) -> float | None:
    with (DATA / "ds15_t12_ventanas_edu_salud_hoteles.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["zona"] == zona and r["ventana_u"]:
                return float(r["ventana_u"])
    return None


def _num(v: float | None) -> str:
    return "—" if v is None else f"{v:.3f}".rstrip("0").rstrip(".").replace(".", ",")


def _estado(cumple: bool | None) -> str:
    return "**Falta dato**" if cumple is None else ("Cumple" if cumple else "**No cumple**")


def _planes_envolvente(z: dict, uso: str) -> list[dict]:
    return [x for x in z["pda"] if x["exige_envolvente"] == "si"] if uso == "residencial" else []


def seccion_elementos(p: dict, z: dict, faltantes: list[str], supuestos: list[str]) -> tuple[list[str], list[tuple]]:
    uso, zona = p["uso"], z["zona"]
    elementos = p.get("elementos") or []
    planes = _planes_envolvente(z, uso)
    out, resumen = ["## 3. Envolvente opaca (exigencia A)", ""], []
    if not elementos:
        faltantes.append("Composición o U acreditado de techumbre, muros y piso ventilado.")
        return out + ["Sin elementos en los datos del proyecto: no se verificó ningún U.", ""], [("A. Envolvente opaca", "**Falta dato**", "")]
    tabla = ["| Elemento | U proyecto (W/m²K) | U máx. (W/m²K) | Fuente de la exigencia | Estado |", "|---|---:|---:|---|---|"]
    detalles = []
    for e in elementos:
        el = e["elemento"]
        if el not in NOMBRE:
            raise ValueError(f"elemento inválido: {el}")
        u, avisos = None, []
        if "u_declarado" in e:
            u = float(e["u_declarado"])
            if not e.get("acreditacion"):
                faltantes.append(f"{NOMBRE[el]}: indicar cómo se acredita el U declarado.")
        elif e.get("capas") or e.get("secciones"):
            secciones = e.get("secciones") or [{"fraccion": 1, "capas": e["capas"]}]
            calc = ucheck.calcular({"elemento": el, "secciones": secciones})
            u, avisos = calc["U"], calc["avisos"]
            sin_fuente = [c.get("nombre", "capa") for s in secciones for c in s["capas"] if not c.get("fuente")]
            if sin_fuente:
                supuestos.append(f"{NOMBRE[el]}: λ o R sin fuente declarada en {', '.join(sin_fuente)}; reemplazar por ficha técnica, "
                                 "NCh 853 (visor oficial) o ensayo.")
            filas = [f"| {c.get('nombre', '—')} | {_num(c['e_m'] * 1000 if c.get('e_m') else None)} | {_num(c.get('lambda'))} | {_num(c.get('R'))} | {c.get('fuente', 'sin fuente')} |"
                     for s in secciones for c in s["capas"]]
            detalles += [f"**{NOMBRE[el]}: capas de interior a exterior** (Rsi {_num(calc['Rsi'])}, Rse {_num(calc['Rse'])}; "
                         f"Res. Ex. 1802 Anexo 2; Rt {_num(calc['Rt'])} m²K/W)", "",
                         "| Capa | e (mm) | λ (W/mK) | R (m²K/W) | Fuente del dato |", "|---|---:|---:|---:|---|", *filas, ""]
            detalles += [f"> [!WARNING] {a}\n" for a in avisos]
        else:
            faltantes.append(f"{NOMBRE[el]}: capas o U acreditado.")
        limites = [limite_pda(x["plan_id"], el) for x in planes]
        limites = [x for x in limites if x]
        if limites:
            lim = min(limites, key=lambda x: x["valor"])
            umax, fuente = lim["valor"], lim["fuente"]
            u_4110 = ucheck.exigencia(el, zona, uso)
            if u_4110 is not None:
                fuente += f"; Art. 4.1.10, Tabla 1: {_num(u_4110)} (informativo)"
                if u_4110 < umax:
                    supuestos.append(f"{NOMBRE[el]}: el Art. 4.1.10 ({_num(u_4110)}) es más estricto que el plan ({_num(umax)}). El inc. 2° remite al "
                                     "plan, pero no hay interpretación oficial confirmada: se recomienda usar el valor más estricto o consultar a la DOM.")
            if lim["varias_etapas"]:
                supuestos.append(f"{NOMBRE[el]}: el plan tiene varias etapas con límites distintos; se usó el más exigente. "
                                 "Confirmar la etapa según la fecha de ingreso.")
        else:
            umax = ucheck.exigencia(el, zona, uso)
            fuente = "DS 15 Tabla 10" if uso in ("educacion", "salud") else "DS 15 Tabla 1"
        cumple = None if u is None or umax is None else u <= umax + 1e-9
        if e.get("acreditacion"):
            fuente += f"; acreditación declarada: {e['acreditacion']}"
        tabla.append(f"| {NOMBRE[el]} | {_num(u)} | {_num(umax)} | {fuente} | {_estado(cumple)} |")
        resumen.append((f"A. {NOMBRE[el]}", _estado(cumple), f"U {_num(u)} / máx. {_num(umax)}"))
    faltan = [NOMBRE[k] for k in NOMBRE if k not in {e["elemento"] for e in elementos}]
    if faltan:
        faltantes.append(f"Elementos no entregados: {', '.join(faltan)}.")
    return out + tabla + ["", *detalles], resumen


def seccion_ventanas(p: dict, z: dict, faltantes: list[str]) -> tuple[list[str], list[tuple]]:
    uso, zona = p["uso"], z["zona"]
    v = p.get("ventanas")
    out = ["## 4. Ventanas (exigencia A)", ""]
    if not v:
        faltantes.append("Ventanas: superficies y U por orientación (residencial) o U de la ventana (otros usos).")
        return out + ["Sin ventanas en los datos del proyecto: no se verificaron.", ""], [("A. Ventanas", "**Falta dato**", "")]
    if uso != "residencial":
        umax = u_max_tabla12(zona)
        u = max((float(o["u_ventana"]) for o in v.get("orientaciones", [])), default=v.get("u_ventana"))
        cumple = None if u is None or umax is None else float(u) <= umax + 1e-9
        return out + [f"U de ventana {_num(u)} W/m²K frente a U máx. {_num(umax)} (DS 15 Tabla 12): {_estado(cumple)}. "
                      "Este uso no verifica % por orientación ni Upvm.", ""], [("A. Ventanas", _estado(cumple), f"U {_num(u)} / máx. {_num(umax)}")]
    if _planes_envolvente(z, uso):
        nombres = ", ".join(x["nombre"] for x in _planes_envolvente(z, uso))
        comando = f"python scripts/pda.py \"{z['comuna']}\""
        faltantes.append(f"Ventanas: contrastar con las tablas del plan ({nombres}) usando `{comando}`.")
        return out + [f"Rigen las tablas de ventanas de **{nombres}**, que prevalecen en vivienda (Art. 4.1.10 inc. 2°). "
                      f"Este borrador no las evalúa de forma automática: revísalas con `{comando}`.", ""], \
            [("A. Ventanas", "**Revisar con el plan**", nombres)]
    r = vmod.verificar({**v, "zona": zona})
    if r["opcion"] == "pct":
        tabla = ["| Orientación | U ventana | % proyecto | % máx. | Estado |", "|---|---:|---:|---:|---|"]
        tabla += [f"| {x['orientacion']} | {_num(x['u_ventana'])} | {_num(x['pct_proyecto'])} | {_num(x['pct_max'])} | {_estado(x['cumple'])} |" for x in r["resultado"]]
        cita = "DS 15 Tablas 3 y 4"
    else:
        tabla = ["| Orientación | U ventana | Upvm proyecto | Upvm máx. | Estado |", "|---|---:|---:|---:|---|"]
        tabla += [f"| {x['orientacion']} | {_num(x['u_ventana'])} | {_num(x['Upvm'])} | {_num(x['Upvm_max'])} | {_estado(x['cumple'])} |" for x in r["resultado"]]
        cita = "DS 15 Tabla 5"
    return out + tabla + ["", f"Fuente: {cita}.", *[f"- {a}" for a in r["avisos"]], ""], \
        [("A. Ventanas", _estado(r["cumple_todo"]), f"opción {r['opcion']}")]


def generar(p: dict, hoy: dt.date | None = None) -> str:
    hoy = hoy or dt.date.today()
    if p.get("uso") not in chk.TABLAS:
        raise ValueError("uso debe ser residencial, hotel, educacion o salud")
    if not p.get("comuna") or not p.get("nombre"):
        raise ValueError("faltan datos obligatorios: nombre y comuna")
    uso, faltantes, supuestos = p["uso"], [], ["Obra nueva."]
    z = zmod.zona(p["comuna"], p.get("altitud"), p.get("lon_oeste"))
    ingreso = p.get("fecha_ingreso")
    if ingreso is None:
        supuestos.append(f"Permiso ingresado desde el {VIGENCIA_DS15:%d-%m-%Y}, cuando rige el DS 15 (OGUC Art. 1.1.3).")
    elif dt.date.fromisoformat(str(ingreso)) < VIGENCIA_DS15:
        supuestos.append("El ingreso es anterior al 28-11-2025: podría regir el texto anterior del 4.1.10. Este informe aplica el DS 15 solo como referencia.")

    cab = [f"# Informe térmico preliminar: {p['nombre']}", "",
           "> [!WARNING] Borrador de trabajo generado con la skill rt-chile. **No es una memoria de cálculo, no se firma** y no "
           "reemplaza al profesional competente, al arquitecto, al laboratorio DS 10, al consultor DS 135 ni a la DOM. "
           "Verifica cada exigencia en las fuentes oficiales de la sección 7 antes de usarla.", "",
           f"Generado: {hoy:%d-%m-%Y}. Corpus verificado: {VERIFICADO}.", ""]

    datos = ["## 2. Datos, zona y plan de descontaminación", "",
             f"- **Uso:** {uso}", f"- **Comuna:** {z['comuna']} ({z['provincia']}, {z['region']})",
             f"- **Fecha de ingreso:** {ingreso or 'no indicada'}"]
    if z["estado"] != "determinada":
        escenarios = "; ".join(f"{e['zona']} ({e['condicion']})" for e in z["zonas_posibles"]) or "sin zona en la tabla oficial"
        faltantes.append("Altitud o meridiano del terreno para determinar la zona térmica.")
        cuerpo = cab + ["## 1. Resumen", "", f"No se puede verificar la envolvente: **la zona térmica no está determinada** ({z['estado']}).", "",
                        *datos, f"- **Zonas posibles:** {escenarios}", *[f"- {a}" for a in z["avisos"]], "",
                        "## Datos faltantes", "", *[f"- {x}" for x in faltantes], ""]
        return "\n".join(cuerpo + cierre())
    datos += [f"- **Zona térmica:** {z['zona']} (tabla MINVU de zonas)",
              f"- **Infiltración máx. de la provincia:** {z['infiltracion_ach50_max']} (ach a 50 Pa; DS 15 Tablas 7 y 14)"]
    planes = _planes_envolvente(z, uso)
    for x in planes:
        datos.append(f"- **PDA/PPA:** {x['nombre']}, {x['decreto']}, cobertura {x['cobertura']}: **mandan sus tablas** en vivienda (Art. 4.1.10 inc. 2°)")
    if not planes and any(x["exige_envolvente"] == "si" for x in z["pda"]):
        datos.append("- **PDA/PPA:** existe un plan en la comuna, pero el inc. 2° solo aplica a viviendas: rige el 4.1.10.")
    if not z["pda"]:
        datos.append("- **PDA/PPA:** sin plan registrado para la comuna a la fecha de verificación.")
    elif all(x["exige_envolvente"] != "si" for x in z["pda"]):
        datos.append(f"- **PDA/PPA:** {z['pda'][0]['nombre']}, {z['pda'][0]['decreto']}: sin exigencia de envolvente registrada; rige el 4.1.10.")
    if uso != "hotel" and z["clima_condensacion"]:
        c = z["clima_condensacion"][0]
        datos.append(f"- **Clima para condensación:** {_num(c['t_ext_c'])} °C y {c['hr_ext_pct']} % HR exterior (Res. Ex. 1802, Anexo 1)")
    datos += [f"- Aviso: {a}" for a in z["avisos"]]

    sec_e, res_e = seccion_elementos(p, z, faltantes, supuestos)
    sec_v, res_v = seccion_ventanas(p, z, faltantes)
    documentos = chk.checklist(p).split("## Exigencias y documentos", 1)[1].split("> Orientación técnica", 1)[0].strip()

    aviso_plan = ["> [!WARNING] Esta tabla describe el régimen general del DS 15. En vivienda con plan, las muestras de infiltración, "
                  "los sellos y las condiciones de condensación son **las del plan**: revísalas con `scripts/pda.py`.", ""]
    resumen = ["## 1. Resumen", "", "Estado de cada verificación. Este informe **no declara que el proyecto cumpla**: las exigencias "
               "pendientes se acreditan con los documentos de la sección 5.", "",
               "| Verificación | Estado | Detalle |", "|---|---|---|"]
    resumen += [f"| {a} | {b} | {c} |" for a, b, c in res_e + res_v]
    if uso == "hotel":
        resumen.append("| B, C y D | Exento | DS 15 num. 1.B, 1.C y 1.D |")
    else:
        resumen += ["| B. Condensación | Por acreditar | Memoria NCh 1973 + Res. Ex. 1802 |",
                    "| C. Infiltración | Por acreditar | Ensayo NCh 3295 en obra terminada, para la recepción |",
                    "| C. Permeabilidad | Por acreditar | Ensayo NCh 3296/3297 o LOSCAT |"]
        resumen.append("| D. Ventilación | Eximida | DS 15 num. 2.D |" if uso == "salud" else "| D. Ventilación | Por acreditar | Informe de tasa |")

    pendientes = ["## 6. Supuestos y datos faltantes", "", "**Supuestos:**", "", *[f"- {x}" for x in supuestos], "", "**Datos faltantes:**", ""]
    pendientes += [f"- {x}" for x in faltantes] or ["- Ninguno en lo que este borrador verifica."]
    pendientes += ["", "**A revisar siempre:** vigencia de la ficha LOSCAT a la fecha del permiso (la mayoría de la E14 vence en diciembre de 2026) "
                   "y registros vigentes DS 10 y DS 135.", ""]
    return "\n".join(cab + resumen + [""] + datos + [""] + sec_e + sec_v + ["## 5. Exigencias, documentos y firmas", "", *(aviso_plan if planes else []), documentos, ""] + pendientes + cierre())


def cierre() -> list[str]:
    return ["## 7. Límites y fuentes oficiales", "",
            "Orientación técnica para apoyar el trabajo profesional. La responsabilidad de los cálculos y de lo que se presente a la DOM es de quien los firma. "
            "Las normas NCh son propiedad del INN y este informe no reproduce su contenido.", "",
            *[f"- {t}: {u}" for t, u in FUENTES], ""]


def main() -> None:
    ap = argparse.ArgumentParser(description="Borrador de informe térmico de un proyecto")
    ap.add_argument("proyecto", help="archivo .yaml o .json")
    ap.add_argument("--salida", help="archivo Markdown de salida (por defecto, la pantalla)")
    args = ap.parse_args()
    texto = generar(chk._load(args.proyecto))
    if args.salida:
        Path(args.salida).write_text(texto, encoding="utf-8")
    else:
        print(texto)


if __name__ == "__main__":
    main()
