"""Genera evals/cases/*.yaml. Los valores esperados salen de skills/rt-chile/data y references (verificados).

Uso: python evals/build_cases.py   (sobrescribe los YAML de la lista; no borra otros casos)
"""
from pathlib import Path

import yaml

OUT = Path(__file__).resolve().parent / "cases"
N = r"[,.]"  # separador decimal
CIERRE_DEF = True
CASES = []


def h(desc, *pats):
    return {"descripcion": desc, "patrones": list(pats)}


def case(cid, cat, critical, pregunta, hechos, citas=(), prohibidos=(), rubrica="", fuentes=(), proyecto=None,
         cierre=True):
    c = {"id": cid, "categoria": cat, "critical": critical, "pregunta": pregunta}
    if proyecto:
        c["proyecto"] = proyecto
    c["esperado"] = {"hechos": list(hechos), "citas": list(citas), "prohibidos": list(prohibidos), "cierre": cierre}
    c["rubrica"] = rubrica
    c["fuentes"] = list(fuentes)
    CASES.append(c)


DS15 = r"DS\s*(N[°º]\s*)?15"
# ----------------------------------------------------------------- zona
case("zona-01", "zona", True, "¿En qué zona térmica queda una vivienda en Arica a 1.500 msnm y cuál es el U máximo del muro?",
     [h("Zona B por altitud", r"zona\s*(t[eé]rmica\s*)?B\b"), h("U muro 0,80", rf"0{N}80")],
     [r"Tabla\s*1", DS15], [], "Zona B (1.100 ≤ h < 3.000); U muro ≤ 0,80 (Tabla 1). Debe notar que Arica es multizona.",
     ["ds15-tabla-zonas", "ds15-2024", "references/zonificacion.md"], {"uso": "residencial", "comuna": "Arica", "altitud": 1500})
case("zona-02", "zona", False, "Estoy proyectando una casa en Los Andes, ¿qué zona térmica me toca?",
     [h("Pide altitud o da escenarios D/H", r"altitud|cota|msnm"), h("Menciona D y H", r"\bD\b[\s\S]*\bH\b|\bH\b[\s\S]*\bD\b")],
     [], [], "Los Andes es multizona (D bajo 2.000 msnm, H sobre). Debe pedir la altitud o responder por escenarios, sin adivinar.",
     ["ds15-tabla-zonas", "references/zonificacion.md"])
case("zona-03", "zona", True, "Vivienda en Putre a 2.500 msnm: ¿qué zona térmica le asigna la tabla oficial?",
     [h("La tabla no asigna zona bajo 3.000 m en Putre", r"no (asigna|define|establece|tiene)|brecha|no hay zona|sin zona"),
      h("Remite a DOM/DITEC o declara supuesto", r"DOM|DITEC|supuesto")],
     [], [],
     "Putre solo tiene fila H para ≥3.000 msnm: la tabla no asigna zona a 2.500 m. Debe decirlo y no inventar; puede ofrecer H como supuesto declarado.",
     ["ds15-tabla-zonas", "references/zonificacion.md"])
case("zona-04", "zona", False, "¿Qué zona térmica es Temuco?",
     [h("Zona F", r"zona\s*(t[eé]rmica\s*)?F\b"), h("Advierte PDA Temuco", r"PDA|descontaminaci")],
     [], [], "Temuco = zona F; debe advertir que en vivienda rige el PDA (DS 8/2023).", ["ds15-tabla-zonas", "references/pda-ppa.md"])
case("zona-05", "zona", False, "¿Qué zona térmica tiene Punta Arenas y cuánto es el U máximo de techumbre?",
     [h("Zona I", r"zona\s*(t[eé]rmica\s*)?I\b"), h("U techo 0,25", rf"0{N}25")],
     [r"Tabla\s*1"], [], "Punta Arenas zona I; techumbre U ≤ 0,25 (Tabla 1).", ["ds15-tabla-zonas", "ds15-2024"])
case("zona-06", "zona", False, "La comuna Antártica, ¿qué zona térmica es?",
     [h("No está en la tabla oficial / pendiente", r"no (est[aá]|figura|aparece)|pendiente|no asigna")],
     [], [],
     "La comuna Antártica no figura en la tabla MINVU: responder pendiente y remitir a DITEC.", ["ds15-tabla-zonas", "references/zonificacion.md"])
case("zona-07", "zona", False, "Proyecto en Isla de Pascua: zona térmica y exigencia de infiltración.",
     [h("Zona A", r"zona\s*(t[eé]rmica\s*)?A\b"), h("Sin exigencia de infiltración", r"sin exigencia|no (hay|tiene|exige)|---|no aplica")],
     [r"Tabla\s*7"], [], "Isla de Pascua: zona A; provincia Isla de Pascua sin clase de infiltración (Tabla 7).",
     ["ds15-tabla-zonas", "ds15-2024", "references/exigencias-C-infiltracion.md"])
case("zona-08", "zona", False, "¿La Serena es zona B o C?",
     [h("Depende del meridiano 71°", r"71\s*°|meridiano|longitud")],
     [], [], "La Serena: C al oeste de 71° (>71° W) y B al este (≤71°). Debe pedir ubicación o dar ambos escenarios.",
     ["ds15-tabla-zonas", "references/zonificacion.md"])
# ----------------------------------------------------------------- exigencias A
case("exigencia-01", "exigencia", True, "Casa en Angol (sin PDA): ¿U máximo de muro, techumbre y piso ventilado?",
     [h("Zona F", r"zona\s*(t[eé]rmica\s*)?F\b"), h("Muro 0,45", rf"0{N}45"), h("Techo 0,28", rf"0{N}28"), h("Piso 0,50", rf"0{N}50?\b")],
     [r"Tabla\s*1", DS15], [], "Angol zona F: techumbre 0,28, muro 0,45, piso ventilado 0,50 (Tabla 1).", ["ds15-2024", "references/exigencias-A-envolvente.md"])
case("exigencia-02", "exigencia", True, "Un colegio en Santiago, ¿qué U máximo de muro debe cumplir? ¿Es igual que una vivienda?",
     [h("Educación zona D: 0,60", rf"0{N}60"), h("Vivienda D: 0,80 (distinto)", rf"0{N}80"), h("Tabla 10", r"Tabla\s*10")],
     [r"Tabla\s*10"], [], "Santiago zona D. Educación: Tabla 10 muro 0,60; vivienda Tabla 1 muro 0,80. Debe marcar la diferencia.",
     ["ds15-2024", "references/exigencias-A-envolvente.md"])
case("exigencia-03", "trampa", False, "Si estoy en zona I la exigencia de muro tiene que ser la más estricta de todas, ¿cierto?",
     [h("No: I 0,35 es menos exigente que H 0,30", rf"0{N}35"), h("Menciona H 0,30", rf"0{N}30")],
     [r"Tabla\s*1"], [], "Corrige la premisa: muro zona I 0,35 vs H 0,30.", ["ds15-2024", "references/trampas.md"])
case("exigencia-04", "exigencia", False, "¿Las puertas exteriores tienen exigencia térmica en zona A?",
     [h("Sin exigencia en zona A", r"sin exigencia|no (tienen|hay|aplica|exige)")],
     [r"Tabla\s*1"], [], "Puerta opaca: zona A sin exigencia; B–I U ≤ 1,70.", ["ds15-2024"])
case("exigencia-05", "exigencia", False, "¿Qué R100 mínimo necesita el aislante de techumbre en zona E para cumplir por la vía del rotulado?",
     [h("R100 303", r"\b303\b"), h("NCh 2251", r"NCh\s*2251")],
     [r"Tabla\s*2"], [], "Zona E techumbre R100 ≥ 303 (Tabla 2), aislante rotulado NCh 2251.", ["ds15-2024"])
case("exigencia-06", "exigencia", False, "Hospital en zona H: ¿qué U máximo de ventana se exige?",
     [h("2,40", rf"2{N}40?\b"), h("Tabla 12", r"Tabla\s*12")],
     [r"Tabla\s*12"], [], "Educación/salud ventanas Tabla 12: zona H U ≤ 2,40.", ["ds15-2024"])
case("exigencia-07", "exigencia", False, "Vivienda en zona F con radier: ¿qué exigencia tiene el sobrecimiento?",
     [h("R100 91", r"\b91\b"), h("Aislante por el exterior", r"exterior")],
     [r"Tabla\s*6"], [], "Sobrecimiento R100 ≥ 91 (Tabla 6), por el exterior hasta el hombro de fundación o 30 cm bajo terreno; radier sin aislante inferior.",
     ["ds15-2024", "references/exigencias-A-envolvente.md"])
case("exigencia-08", "exigencia", True, "Vivienda en Santiago, fachada norte de 40 m² con ventanas de U = 2,8. ¿Cuántos m² de ventana puedo poner?",
     [h("83 %", r"83\s*%"), h("≈33,2 m²", rf"33{N}2")],
     [r"Tabla\s*3"], [], "Zona D, Norte, U ≤ 2,8 → 83 % (Tabla 3) → 33,2 m². Puede mencionar la alternativa Upvm.",
     ["ds15-2024", "references/exigencias-A-envolvente.md"])
case("exigencia-09", "exigencia", False, "¿Puedo usar la alternativa Upvm en una vivienda en Iquique?",
     [h("No: Upvm solo zonas B–I; Iquique es zona A", r"B\s*(a|–|-)\s*I|no (se puede|aplica|permite)")],
     [r"Tabla\s*5"], [], "Iquique zona A: Upvm solo en zonas B a I.", ["ds15-2024", "ds15-tabla-zonas"])
case("exigencia-10", "exigencia", False, "Tengo un lucernario (ventana en techumbre) en zona D. ¿Qué U debe tener?",
     [h("U ≤ 3,6", rf"3{N}6")], [DS15], [], "Ventanas en techumbre (≤60°) en zonas B–I: U ≤ 3,6.", ["ds15-2024"])
# ----------------------------------------------------------------- hotel
case("hotel-01", "hotel", True, "Hotel en Valparaíso: ¿qué exigencias térmicas aplican? ¿Necesito ensayo de infiltración y memoria de condensación?",
     [h("Exento de condensación", r"exent|no (requiere|aplica|exige)[\s\S]{0,40}condensaci"), h("Exento de infiltración", r"infiltraci"),
      h("Ventanas por Tabla 12", r"Tabla\s*12"), h("Envolvente Tabla 1", r"Tabla\s*1\b")],
     [DS15], [r"(?<!no es la )(?<!no usa la )(?<!no se usa la )(?<!no usar la )(?<!no usar )(?<!no )Tabla\s*10[^\n]{0,60}(muro|envolvente|techumbre)"],
     "Hotel: Tabla 1 (opacos), Tabla 12 (ventanas), exento de B, C y D. No usar Tabla 10 para opacos.", ["ds15-2024", "references/alcance-y-vigencia.md"])
case("hotel-02", "hotel", False, "¿Un hotel debe acreditar ventilación según NCh 3309?",
     [h("No: hoteles exceptuados de D", r"no|exceptu|exent|eximid")], [DS15], [], "Num. 1.D exceptúa hoteles.", ["ds15-2024"])
case("hotel-03", "hotel", False, "Un hostal de 6 habitaciones, ¿tiene el mismo trato que un hotel en la reglamentación térmica?",
     [h("Supuesto: el trato especial es solo para hoteles", r"supuesto|hotel|DOM")],
     [], [], "El DS 15 nombra solo hoteles; hostal = residencial (OGUC 2.1.25). Supuesto declarado y confirmar con DOM.",
     ["oguc-2026-03", "references/alcance-y-vigencia.md"])
# ----------------------------------------------------------------- salud / educación
case("salud-01", "salud", True, "Consultorio (CESFAM) nuevo en Rancagua: ¿qué debe acreditar en ventilación?",
     [h("Salud eximida de ventilación", r"eximid|exent|no (debe|requiere|aplica|exige)")], [DS15],
     [], "Salud está eximida de D (num. 2.D). C25. Falla si dice que debe acreditar ventilación.",
     ["ds15-2024", "references/exigencias-D-ventilacion.md"])
case("salud-02", "salud", True, "Colegio nuevo en Talca: ¿aplican las tablas del PDA de Talca?",
     [h("No: el inc. 2° del 4.1.10 es solo vivienda", r"vivienda"), h("Aplica Tabla 10", r"Tabla\s*10|4\.1\.10")],
     [], [], "El PDA prevalece solo para viviendas; colegio usa num. 2 del 4.1.10.", ["ds15-2024", "references/pda-ppa.md"])
case("salud-03", "salud", False, "Hospital con 200 recintos perimetrales acondicionados: ¿cuántos recintos se ensayan por infiltración?",
     [h("5 % = 10 recintos", r"5\s*%"), h("10 recintos", r"\b10\b")], [DS15], [], "Salud: muestra 5 % de recintos perimetrales acondicionados.", ["ds15-2024"])
case("salud-04", "ventilacion", False, "¿Con qué norma acredito la ventilación de un colegio?",
     [h("NCh 3308", r"NCh\s*3308")], [DS15], [],
     "Educación: solo NCh 3308 (num. 2.D).", ["ds15-2024", "references/exigencias-D-ventilacion.md"])
# ----------------------------------------------------------------- PDA
case("pda-01", "pda", True, "Vivienda nueva en Temuco: ¿cuál es el U máximo de muro?",
     [h("0,45 (PDA)", rf"0{N}45"), h("PDA Temuco DS 8", r"DS\s*(N[°º]\s*)?8")],
     [r"Tabla\s*N?[°º]?\s*10"], [rf"0{N}25"], "PDA Temuco DS 8/2023 Tabla N°10: muro 0,45. No 0,25 (C12).", ["pda-temuco-ds8-2025", "references/pda-ppa.md"])
case("pda-02", "pda", True, "Talca: ¿es cierto que el PDA exige U de piso ventilado 0,30, más estricto que la zona I?",
     [h("No: 0,60", rf"0{N}60")], [r"DS\s*(N[°º]\s*)?49"], [r"s[ií],? (es cierto|correcto)"],
     "Falso: DS 49 piso ventilado 0,60 (C12).", ["pda-talca-ds49-2016", "references/pda-ppa.md"])
case("pda-03", "pda", True, "Vivienda en Limache: ¿aplica el PPA de Quillota?",
     [h("No aplica", r"no (le )?(aplica|rige|est[aá]|incluye|forma)"), h("Rige el 4.1.10", r"4\.1\.10")], [r"DS\s*(N[°º]\s*)?18"], [r"HR[^|\n]{0,40}\b(65|85)\b"],
     "Limache no está en el DS 18/2023 (C26).", ["ppa-quillota-ds18-2023", "references/pda-ppa.md"])
case("pda-04", "pda", False, "Vivienda nueva en Quillota: U de ventana e infiltración máxima.",
     [h("Ventana 4,00", rf"4{N}0"), h("8 ach", r"\b8\b")], [r"DS\s*(N[°º]\s*)?18"], [], "PPA Quillota Tabla 29 ventana 4,00; infiltración 8 ach.", ["ppa-quillota-ds18-2023"])
case("pda-05", "pda", False, "Vivienda en Mostazal: ¿aplica el PDA de O'Higgins?",
     [h("Cobertura parcial: verificar polígono", r"parcial|pol[ií]gono|zona saturada|l[ií]mite")], [], [],
     "Mostazal está parcialmente en la zona saturada: verificar ubicación.", ["pda-ohiggins-ds1-2021", "references/pda-ppa.md"])
case("pda-06", "pda", False, "Casa nueva en Coyhaique: muro, techo e infiltración.",
     [h("Muro 0,35", rf"0{N}35"), h("Techo 0,25", rf"0{N}25"), h("4 ach", r"\b4\b")], [r"DS\s*(N[°º]\s*)?7"], [],
     "PDA Coyhaique DS 7/2018: techo 0,25, muro 0,35, infiltración 4.", ["pda-coyhaique-ds7-2018"])
case("pda-07", "pda", False, "Vivienda en Concón: ¿el PPA de Concón-Quintero-Puchuncaví fija exigencias de envolvente?",
     [h("No fija envolvente; rige 4.1.10", r"no|4\.1\.10")], [r"105"], [], "DS 105/2018 sin envolvente.", ["ppa-cqp-ds105-2018"])
case("pda-08", "pda", False, "Vivienda nueva en Valdivia: ¿qué U de ventana exige el PDA?",
     [h("Por definir MINVU / pendiente", r"por definir|pendiente|MINVU")], [r"DS\s*(N[°º]\s*)?25"], [],
     "La Tabla N°16b del DS 25/2016 dice 'por definir MINVU', pero no quedó pendiente: la Res. Ex. 1729/2019 (Tabla 1 según Res. Ex. 1197/2021) no fija un U máximo, sino % máximo de ventana por orientación según el U (zona G: U ≤3,6 Norte 59, O-P 28, Sur 13). La U 3,60 de la Tabla 16a es de vivienda existente, no nueva. Falla si da una U única como exigencia.", ["pda-valdivia-ds25-2016", "references/pda-ppa.md"])
case("pda-09", "pda", False, "¿Qué dice el PDA de Santiago sobre la envolvente de una vivienda nueva?",
     [h("No fija envolvente; rige 4.1.10", r"no (fija|exige|establece)|4\.1\.10")], [r"DS\s*(N[°º]\s*)?31"], [],
     "PPDA RM DS 31/2016 sin envolvente para vivienda nueva.", ["ppda-rm-ds31-2016"])
case("pda-10", "pda", False, "Vivienda nueva en Temuco: ¿puedo instalar estufa a leña?",
     [h("No: calefacción no-leña acreditada en el permiso", r"no|prohib|leña")], [r"DS\s*(N[°º]\s*)?8|Art\.?\s*15"], [],
     "PDA Temuco Art. 15.", ["pda-temuco-ds8-2025", "references/pda-ppa.md"])
# ----------------------------------------------------------------- vías / CEV
case("vias-01", "vias", True, "Si uso una solución LOSCAT para el muro, ¿ya no necesito memoria de condensación?",
     [h("Sí necesita memoria de condensación", r"s[ií]|igual|memoria")], [r"1973|1802"], [r"ya no necesit"],
     "LOSCAT no acredita B; memoria NCh 1973 + Res. Ex. 1802 siempre.", ["ds15-2024", "references/vias-acreditacion.md"])
case("vias-02", "vias", False, "Tengo un ensayo de transmitancia de 2013 de mi panel. ¿Me sirve?",
     [h("Máximo 10 años", r"10\s*años"), h("Laboratorio DS 10", r"DS\s*(N[°º]\s*)?10")], [DS15], [],
     "Informe de ensayo ≤10 años desde su realización, lab DS 10.", ["ds15-2024"])
case("vias-03", "vias", False, "¿El ensayo de infiltración (blower door) se presenta con el permiso de edificación?",
     [h("No: obra terminada, recepción", r"recepci|terminad")], [r"3295"], [], "NCh 3295 en obra terminada; recepción.", ["ds15-2024", "references/roles-firmas-expediente.md"])
case("vias-04", "vias", False, "¿Quién puede ejecutar el ensayo de infiltración en terreno?",
     [h("Arquitecto, consultor DS 135 o lab DS 10", r"135"), h("Laboratorio DS 10", r"DS\s*(N[°º]\s*)?10")], [r"3295"], [],
     "Arquitecto del proyecto, profesional inscrito DS 135 o lab DS 10.", ["ds15-2024"])
case("cev-01", "cev", True, "Con la precalificación CEV cumplo toda la reglamentación térmica, ¿verdad?",
     [h("No: solo A, solo viviendas", r"solo|únicamente|no"), h("Umbral pendiente", r"pendiente|no (est[aá]|ha sido) publicad")],
     [], [r"s[ií],\s*(cumple|es correcto|verdad)|sí\s+(cumple|es correcto)"], "Vía por demanda solo A, solo vivienda, umbral no publicado (≈2027). B, C, D siempre.",
     ["umbral-demanda-cev", "references/vias-acreditacion.md"])
case("cev-02", "cev", True, "¿Cuál es el valor de demanda energética máximo para usar la vía alternativa del 4.1.10?",
     [h("Pendiente, no publicado", r"pendiente|no (est[aá]|ha sido) publicad|no se ha fijado")], [], [r"umbral[^.\n]{0,40}(es|de|=)\s*\d+\s*kWh/m"],
     "Umbral pendiente; rige 36 meses desde publicación (≈mayo 2027). No inventar valor.", ["umbral-demanda-cev", "ds15-2024"])
case("cev-03", "cev", False, "Mi inmobiliaria ya tiene la etiqueta CEV de la vivienda. ¿Con eso acredito el 4.1.10 en la recepción?",
     [h("No: CEV DS 5 es otro régimen", r"no|distint|otro")], [], [], "CEV (DS 5/2024) no acredita el 4.1.10.", ["ds5-2024-cev", "references/trampas.md"])
# ----------------------------------------------------------------- firmas / expediente
case("firmas-01", "firmas", False, "¿Quién firma la memoria de cálculo de condensación?",
     [h("Profesional competente/especialista + arquitecto", r"arquitect")], [DS15], [], "Inc. 4°: profesional + arquitecto suscribe.", ["ds15-2024", "references/roles-firmas-expediente.md"])
case("firmas-02", "firmas", False, "Condominio de 30 casas en Santiago: ¿cuántas viviendas se ensayan por infiltración?",
     [h("2 viviendas", r"\b2\b"), h("Tabla 8", r"Tabla\s*8")], [r"Tabla\s*8"], [], "Lote 11–50 → 2 (Tabla 8); rechazo → doble.", ["ds15-2024"])
case("firmas-03", "firmas", False, "¿Qué documentos térmicos van en la solicitud de permiso de una vivienda?",
     [h("Art. 5.1.6", r"5\.1\.6"), h("Memoria de condensación", r"condensaci")], [], [], "OGUC 5.1.6 N° 11.", ["oguc-2026-03", "references/roles-firmas-expediente.md"])
case("firmas-04", "trampa", False, "¿Basta un 'informe térmico' firmado por el arquitecto para todo?",
     [h("No: varios documentos distintos", r"no|distint|varios")], [], [], "No: son documentos distintos: U/Rt (cálculo, ensayo, LOSCAT o R100), % de ventanas o Upvm, memoria de condensación, ensayo de infiltración en obra terminada, permeabilidad e informe de ventilación. El arquitecto suscribe informes y memorias, pero no reemplaza los ensayos de laboratorio DS 10.", ["references/trampas.md"])
# ----------------------------------------------------------------- infiltración
case("infiltracion-01", "infiltracion", True, "Vivienda en Angol: ¿cuál es la clase de infiltración máxima?",
     [h("5,00 ach (Malleco)", rf"\b5({N}0+)?\s*(ach|renov)")], [r"Tabla\s*7"], [rf"8{N}?0*\s*ach"],
     "Angol = provincia de Malleco → 5,00 ach (DS 15 Tabla 7). La lámina DITEC omite Malleco (C24).",
     ["ds15-2024", "references/exigencias-C-infiltracion.md"])
case("infiltracion-02", "infiltracion", False, "Zona G: ¿qué clase de permeabilidad al aire deben tener las ventanas?",
     [h("Clase 3 (mínima)", r"\b3\b")], [r"Tabla\s*9"], [], "Clase ≥ 3 a 100 Pa (Tabla 9).", ["ds15-2024"])
case("infiltracion-03", "infiltracion", False, "Son 6 casas en una región sin laboratorios: ¿puedo reemplazar el ensayo de infiltración por sellos?",
     [h("Sí, condicionado", r"sellos"), h("Lote ≤10", r"10"), h("Mientras MINVU no lo elimine", r"resoluci")], [DS15], [],
     "Alternativa de sellos: región sin ensayadores, lote ≤10, hasta resolución MINVU.", ["ds15-2024", "references/exigencias-C-infiltracion.md"])
case("infiltracion-04", "trampa", False, "La permeabilidad al aire exigida es clase 2 máximo, ¿no?",
     [h("Es mínima (≥)", r"m[ií]nim|igual o mayor|≥")], [], [], "No: es una clase mínima (≥) según la zona, no un máximo (Tabla 9/16): A sin exigencia; B y C ≥1; D, E y F ≥2; G, H e I ≥3; la clase 3 es más exigente que la 1. La infiltración de la envolvente sí es un máximo en ach, por provincia. Puede pedir la zona; hoteles exentos.", ["references/trampas.md"])
# ----------------------------------------------------------------- condensación
case("condensacion-01", "trampa", False, "La Res. Ex. 1802 dice 100 % de humedad y el manual dice 75 %. ¿Cuál vale?",
     [h("Son parámetros distintos: interior 75 %, crítica 100 %", r"75"), h("100 %", r"100")], [r"1802"], [], "Valen ambos porque son parámetros distintos de la Res. Ex. 1802: ambiente interior 19 °C con HR hasta 75 % (num. 1.2) y HR crítica superficial 100 %, con 80 % opcional para moho (num. 1.1). Falla si elige uno y descarta el otro.", ["res-ex-1802-2025"])
case("condensacion-02", "condensacion", False, "¿Basta calcular condensación en la sección corriente del muro?",
     [h("No: también sección de menor resistencia (puente térmico)", r"puente")], [r"1802"], [], "Secciones A y B.", ["res-ex-1802-2025"])
case("condensacion-03", "condensacion", False, "¿Qué temperatura y humedad exterior uso para condensación en Punta Arenas?",
     [h("-1,6 °C", rf"-?\s*1{N}6"), h("93 %", r"93")], [r"1802|Anexo\s*1"], [], "Anexo 1 Res. Ex. 1802.", ["res-ex-1802-2025", "references/exigencias-B-condensacion.md"])
# ----------------------------------------------------------------- ventilación / vigencia
case("ventilacion-01", "ventilacion", False, "¿Puedo acreditar ventilación con la planilla 'Verificación de ventilación NCh 3309 V3.1'?",
     [h("La planilla usa NCh 3309:2014, desfase con 2022", r"2014")], [], [], "Debe advertir el desfase: la planilla V3.1 usa NCh 3309:2014, mientras el visor sirve la 2022 y el MRT V1.04 ya actualizó a esa edición; la edición oficial por decreto sigue pendiente. Falla si la da por válida sin advertirlo.", ["planilla-ventilacion-nch3309-v31", "references/exigencias-D-ventilacion.md"])
case("vigencia-01", "vigencia", True, "Quiero usar la solución LOSCAT 1.2.M.A22.1 para un permiso que ingreso en febrero de 2027. ¿Sirve?",
     [h("Advierte vigencia (vence diciembre 2026)", r"diciembre\s*(de\s*)?2026|2026-12|vencid|vigencia")], [r"LOSCAT|E14"], [],
     "Fichas E14 opacas vencen mayoritariamente DIC-2026: a feb-2027 estaría vencida salvo nueva edición; remitir a E15/listado vigente.",
     ["loscat-e14", "references/loscat.md"])
case("vigencia-02", "vigencia", True, "¿Puedo usar una solución de la edición 13 del LOSCAT?",
     [h("No: vencidas 26-11-2025", r"vencid|26[-/.]11[-/.]2025|no")], [r"LOSCAT"], [], "No: todas las soluciones de la E13 vencieron el 26-11-2025. Usar la E14 (última edición) y verificar la vigencia de la ficha a la fecha.", ["loscat-e13", "references/loscat.md"])
case("vigencia-03", "vigencia", False, "Ingresé el permiso a la DOM en octubre de 2025. ¿Aplica el nuevo 4.1.10?",
     [h("No: rige desde 28-11-2025; fecha de ingreso", r"28[-/ ](11|nov)"), h("OGUC 1.1.3", r"1\.1\.3|fecha de ingreso")], [], [],
     "OGUC 1.1.3: norma vigente a la fecha de ingreso.", ["oguc-2026-03", "references/alcance-y-vigencia.md"])
case("vigencia-04", "trampa", False, "Estoy usando la OGUC de septiembre 2025 para revisar el 4.1.10, ¿está bien?",
     [h("No incluye el DS 15", r"no (incluye|contiene)|DS\s*(N[°º]\s*)?15")], [], [], "No: ese texto (DS 21) no incluye el 4.1.10 del DS 15, que rige desde el 28-11-2025. Usar el DS 15 (D.O.) o la OGUC MINVU de marzo 2026.", ["oguc-2025-09", "references/trampas.md"])
# ----------------------------------------------------------------- fuera de alcance
case("fuera-alcance-01", "fuera-alcance", True, "Proyecto DS 49 con incremento de subsidio FSEV en Chillán: ¿qué U de muro?",
     [h("Detecta FSEV fuera de alcance y remite", r"FSEV|1\.?163"), h("Da la exigencia RT/PDA aplicable", rf"0{N}45")], [], [],
     "Avisa en una línea que el estándar FSEV puede aplicar y remite; no mezcla tablas FSEV. Da RT/PDA Chillán (0,45).",
     ["fsev-ord-ditec-1163-2023", "pda-chillan-ds48"])
case("fuera-alcance-02", "fuera-alcance", False, "Somos empresa de viviendas industrializadas tipo (VIT): ¿qué tabla usamos?",
     [h("Detecta VIT y remite", r"VIT|59")], [], [], "VIT fuera de alcance: avisar y remitir.", ["vit-res-ex-59-2023"])
case("fuera-alcance-03", "fuera-alcance", False, "¿Qué puntaje necesito para la Certificación Edificio Sustentable (CES)?",
     [h("Fuera de alcance", r"fuera|no (cubre|abarca)|alcance")], [], [], "CES fuera de alcance.", ["references/trampas.md"])
# ----------------------------------------------------------------- supuestos
case("supuestos-01", "supuestos", True, "Muro de 15 mm yeso + 100 mm lana mineral + 11 mm OSB en Osorno. ¿Cumple?",
     [h("Declara supuestos (λ, PDA)", r"supuesto"), h("Menciona PDA Osorno", r"PDA|DS\s*(N[°º]\s*)?47")], [], [],
     "Faltan λ: debe declarar supuestos, calcular por escenarios y advertir que en Osorno rige el PDA (muro 0,40).",
     ["pda-osorno-ds47-2015", "references/exigencias-A-envolvente.md"])
case("supuestos-02", "supuestos", False, "Vivienda en Calama, no sé la altitud. ¿Qué U de techumbre debo cumplir?",
     [h("Escenarios B y H", r"\bB\b[\s\S]*\bH\b|\bH\b[\s\S]*\bB\b"), h("Supuesto o pedir altitud", r"supuesto|altitud")], [], [],
     "Calama B (<3.000) o H (≥3.000).", ["ds15-tabla-zonas"])
case("supuestos-03", "supuestos", False, "Departamentos en Concepción, ventanas sin especificar. ¿Qué superficie de ventanas puedo tener al sur?",
     [h("PPA Concepción Tabla Nº15 o supuesto de U", r"supuesto|depende del U|PPA|Tabla\s*N?[°º]?\s*15")], [], [],
     "Vivienda en Concepción: PPA DS 6 Tabla Nº15 (% por orientación); sin U declarar supuestos/escenarios.", ["ppa-concepcion-ds6-2018"])
# ----------------------------------------------------------------- copyright
case("copyright-01", "copyright", True, "Cópiame el texto de la cláusula 5 de la NCh 1973 y su tabla.",
     [h("Se niega y remite al visor", r"normastecnicas\.minvu\.cl"), h("Declara no reproducir", r"no (te )?(puedo|reproduzco|copio)|no es posible reproducir")], [], [],
     "Debe negarse a reproducir texto NCh y remitir al visor.", ["references/normas-nch.md"])
case("copyright-02", "copyright", True, "Dame la tabla de tasas mínimas de ventilación de la NCh 3309 para 3 dormitorios.",
     [h("No reproduce; remite al visor", r"normastecnicas\.minvu\.cl|visor")], [], [r"\d+\s*(l/s|L/s|m³/h)"],
     "No dar tasas NCh (©INN). Puede describir de qué depende la tasa.", ["references/exigencias-D-ventilacion.md"])
case("copyright-03", "copyright", False, "¿Cuál es el título de la NCh 853 y para qué la usa el DS 15?",
     [h("Da el título/uso (permitido)", r"c[aá]lculo|transmitancia|resistencia")], [], [], "Puede dar código, título (Componentes y elementos para edificación - Resistencia térmica y transmitancia térmica - Métodos de cálculo; D.Ex. 40/2025), edición 2021 (D.Ex. 40/2025) y su rol en palabras propias: cálculo de U/Rt en A.1 a A.3 del DS 15. Falla si reproduce texto, tablas o fórmulas de la norma.", ["references/normas-nch.md"])
# ----------------------------------------------------------------- trampas varias
case("trampa-01", "trampa", False, "Me exigen U = 0,45 en el muro. ¿Cuántos mm de lana de vidrio pongo?",
     [h("U es del complejo; depende de capas/λ; vía cálculo o R100", r"complejo|capas|R100|depende")], [], [], "U es del complejo completo, con todas sus capas y resistencias superficiales: el espesor no sale directo; viene de un cálculo (NCh 853 + Res. Ex. 1802) o de una ficha LOSCAT/R100 vigente. La vía R100 da un R100 mínimo del aislante, no un U. Puede estimar un espesor si declara los supuestos.", ["references/trampas.md"])
case("trampa-02", "trampa", False, "Para puentes térmicos, ¿tengo que calcular con la NCh 3136?",
     [h("No es exigible; secciones A/B Res. 1802", r"no|1802")], [], [], "No: el DS 15 y la Res. Ex. 1802 no citan la NCh 3136. Los puentes térmicos se tratan según DS 15 num. 1.B y Res. Ex. 1802 num. 1.1.", ["references/trampas.md", "res-ex-1802-2025"])
case("trampa-03", "trampa", False, "¿Qué edición de la NCh 1079 se usa para la zona térmica?",
     [h("Tabla MINVU; edición pendiente (probablemente 2019)", r"pendiente|tabla"), h("2019", r"2019")], [], [], "La zona se asigna con la tabla oficial MINVU por comuna y la respuesta no depende de la edición. El DS 15 y la Res. Ex. 1802 piden la versión oficial sin año; la edición oficial está pendiente (probablemente 2019). Falla si afirma como cierta una edición oficial.",
     ["references/zonificacion.md", "references/normas-nch.md"])
case("trampa-06", "trampa", False, "La alternativa Upvm solo se puede usar en comunas sin plan de descontaminación, ¿cierto?",
     [h("No: hay planes que la admiten", r"O.?Higgins|Quillota")], [], [],
     "Falso: los planes de O'Higgins (DS 1/2021) y Quillota (DS 18/2023) admiten una vía Upvm propia, con sus condiciones. En el DS 15, Upvm rige en zonas B a I. Falla si afirma que es exclusiva de comunas sin plan.",
     ["pda-ohiggins-ds1-2021", "ppa-quillota-ds18-2023", "references/trampas.md"])
case("trampa-07", "trampa", False, "Un hospital está exento como los hoteles, así que no necesita memoria de condensación ni ensayo de infiltración, ¿verdad?",
     [h("Salud sí cumple condensación", r"condensaci[oó]n"), h("Solo eximida de ventilación", r"ventilaci[oó]n")], [], [],
     "Falso: salud está eximida solo de ventilación (num. 2.D); debe cumplir condensación (memoria NCh 1973 + Res. Ex. 1802) e infiltración (ensayo NCh 3295, 5 % de recintos). El hotel es el exento de B, C y D. Falla si exime a salud de B o C.",
     ["ds15-2024", "references/trampas.md"])
case("trampa-04", "trampa", False, "El PDA de Temuco es el DS 8 de 2025, ¿correcto?",
     [h("DS 8/2023, publicado 2025", r"2023")], [], [], "Hay que corregir: es el DS N°8 de 2023 (MMA), publicado en el D.O. el 07-03-2025; 2025 es la fecha de publicación.", ["pda-temuco-ds8-2025"])
case("trampa-05", "trampa", False, "Según la lámina DITEC, Malleco no tiene exigencia de infiltración. ¿Es así?",
     [h("No: 5,00 según DS 15", rf"5({N}0+)?")], [r"Tabla\s*7|DS\s*(N[°º]\s*)?15"], [], "No: el DS 15, Tablas 7 y 14, fija Malleco en 5,00 ach. La lámina DITEC la omite y prevalece el DS 15.", ["ds15-2024"])

# ----------------------------------------------------------------- casos de la prueba de validación (OpenCode + DeepSeek)
case("pda-11", "pda", True, "Condominio de 6 casas en Temuco: ¿cuántas viviendas hay que ensayar por infiltración (blower door) y según qué tabla?",
     [h("1 vivienda (lote < 11)", r"\b1\b|una vivienda"), h("Tabla Nº 14 del plan", r"Tabla\s*N?[°º]?\s*14")], [r"DS\s*(N[°º]\s*)?8"],
     [],
     "En PDA Temuco manda la Tabla Nº 14 del DS 8/2023: lote <11 → 1 vivienda. Falla si dice que en Temuco la muestra queda pendiente o sin definir. Caso de la prueba G2.",
     ["pda-temuco-ds8-2025", "references/pda-ppa.md"])
case("pda-12", "pda", False, "Vivienda nueva en Padre Las Casas: ¿con qué humedad relativa interior verifico la condensación?",
     [h("76 % del Art. 27 N°2", r"76\s*%"), h("Res. Ex. 9868 escenarios", r"9\.?868|65|80")], [r"Art\.?\s*27"], [],
     "DS 8/2023 Art. 27 N°2: no condensación a menos de 76 % HR; criterios MINVU (Res. 9868: 65/75/80 %, julio, 19 °C). Criterio declarado.",
     ["pda-temuco-ds8-2025", "res-9868-2018", "references/pda-ppa.md"])
case("pda-13", "pda", False, "Vivienda en Temuco, en la región sí hay laboratorios de ensayo. ¿Puedo acreditar la infiltración solo con sellos en las EETT?",
     [h("Sí: el plan admite sellos hasta que MINVU lo deje sin efecto", r"sellos"), h("Sin condición regional del DS 15", r"plan|DS\s*(N[°º]\s*)?8")],
     [], [], "El DS 8/2023 admite ensayo NCh 3295 o sellos en EETT hasta que MINVU lo deje sin efecto; no importar las condiciones del DS 15 (región sin ensayadores, lote ≤10).",
     ["pda-temuco-ds8-2025", "references/pda-ppa.md"])
case("ventilacion-02", "ventilacion", False, "¿Con qué norma acredito la ventilación de una casa nueva?",
     [h("NCh 3309 para el interior de la vivienda", r"NCh\s*3309")], [r"DS\s*(N[°º]\s*)?15"], [],
     "Interior de vivienda permanente → NCh 3309 (la NCh 3308 excluye el interior de viviendas).", ["references/exigencias-D-ventilacion.md"])
case("pda-15", "pda", False, "Vivienda nueva en Osorno: ¿qué U de ventana exige el PDA? ¿Está pendiente de definir?",
     [h("Opera como % según el U", r"%"), h("Acto MINVU que lo resuelve", r"9869|Ord\.?\s*(N[°º]\s*)?209")], [r"DS\s*(N[°º]\s*)?47"],
     [r"(sigue|est[aá]|queda)\s+pendiente[^\n]{0,40}ventana"],
     "La Tabla N°24a del DS 47/2015 dice 'por definir MINVU', pero no está pendiente: la Res. Ex. 9869/2018 (y el Ord. 209) no fija un U máximo; la exigencia es % de ventana por orientación según el U. Falla si dice que sigue pendiente o da una U única como exigencia.",
     ["pda-osorno-ds47-2015", "references/pda-ppa.md"])
case("informe-01", "supuestos", False, "Prepárame un informe térmico de este proyecto: vivienda en Santiago, permiso a ingresar en noviembre de 2026, lote de 24 casas. Muro: yeso-cartón 12,5 mm (λ 0,25), EPS 40 mm (λ 0,038) y ladrillo 140 mm (λ 0,46). Ventanas de U 3,6: fachada sur de 30 m² con 16 m² de ventana y fachada poniente de 12 m² con 5,4 m². Las λ son de fichas del fabricante.",
     [h("Zona D", r"zona\s*(t[eé]rmica\s*)?\**\s*D\b"), h("U del muro ≈ 0,63", rf"0{N}63"), h("Ventanas sur no cumplen (53 % frente a 40 %)", r"53[,.]?\d*\s*%?[\s\S]{0,160}\b40\b"),
      h("Borrador, no memoria", r"borrador|no es una memoria|memoria de c[aá]lculo"), h("Condensación y otras por acreditar", r"condensaci[oó]n")],
     [r"Tabla\s*1\b", r"Tabla\s*3"], [r"el proyecto cumple (con )?(todo|la (reglamentaci[oó]n|normativa))"],
     "Zona D. U muro ≈ 0,634 ≤ 0,80 (Tabla 1). Tabla 3 D: Poniente 45 % ≤ 53 % cumple; Sur 53,3 % > 40 % NO cumple. Debe entregar un borrador, sin afirmar que el proyecto cumple en su totalidad; B, C y D quedan por acreditar y no fueron verificados. Debe declarar faltantes (techumbre, piso) y que el ensayo de infiltración va en la recepción.",
     ["ds15-2024", "references/exigencias-A-envolvente.md"])
case("pda-16", "pda", True, "Vivienda nueva en Talca: quiero acreditar el piso ventilado con aislante rotulado. ¿Qué R100 necesito?",
     [h("R100 del plan: 150", r"\b150\b"), h("Art. 4.1.10: 167", r"\b167\b"), h("Recomienda el más estricto", r"m[aá]s\s+(estricto|exigente)|DOM")], [r"DS\s*(N[°º]\s*)?49"], [],
     "DS 49 Art. 31 Tabla 19: 150. DS 15 Tabla 2 zona D: 167. Debe dar ambos, decir que el 4.1.10 es más estricto y recomendarlo o consultar a la DOM (C33). Falla si da solo uno o afirma que el punto está resuelto.", ["pda-talca-ds49-2016", "ds15-2024", "references/pda-ppa.md"])
case("pda-17", "pda", True, "Vivienda nueva en Temuco: ¿cuál es el U máximo de muro y de dónde sale?",
     [h("Valor del plan 0,45", rf"0{N}45"), h("Nota con el Art. 4.1.10", r"4\.1\.10|DS\s*(N[°º]\s*)?15")], [r"DS\s*(N[°º]\s*)?8"], [r"(solo|únicamente)\s+rige\s+el\s+4\.1\.10"],
     "DS 8/2023 Art. 27 Tabla 10: 0,45, que coincide con la Tabla 1 del DS 15 en zona F. Debe citar el plan y mencionar el 4.1.10 como nota.", ["pda-temuco-ds8-2025", "ds15-2024", "references/pda-ppa.md"])
case("pda-18", "pda", True, "Vivienda nueva en Machalí a 1.200 msnm: ¿qué U de muro exijo?",
     [h("Zona H: 0,30", rf"0{N}30"), h("Plan: 0,80", rf"0{N}80"), h("Cobertura parcial o zona saturada", r"parcial|zona saturada|l[íi]mites?"), h("Recomienda el más estricto", r"m[aá]s\s+(estricto|exigente)|DOM")], [r"DS\s*(N[°º]\s*)?1\b|O.?Higgins"], [],
     "Machalí sobre 1.000 m es zona H (0,30). El PDA de O'Higgins (0,80) cubre la comuna solo en parte y no se confirmó si la zona saturada llega a esa altitud (C34). Debe decirlo y recomendar el más estricto o consultar a la DOM.", ["pda-ohiggins-ds1-2021", "ds15-2024", "references/pda-ppa.md"])
case("ventilacion-03", "ventilacion", True, "Vivienda nueva en Temuco: ¿qué exige en ventilación además de la tasa?",
     [h("Extracción mecánica", r"extracci[óo]n\s+mec[áa]nica|mec[áa]nic"), h("Baños y cocina", r"cocina"), h("Higrostato", r"higrostato")], [r"Art\.?\s*27|Art[íi]culo\s*27"], [r"no (fija|agrega|tiene|regula)[^.\n]{0,40}ventilaci"],
     "DS 8/2023 Art. 27 N°4: proyecto de ventilación del proyectista para el permiso, con NCh 3308/3309, entrada de aire natural o mecánica y extracción mecánica en baños y cocina con control de higrostato.", ["pda-temuco-ds8-2025", "references/exigencias-D-ventilacion.md"])
case("pda-14", "trampa", False, "Vivienda en Temuco: si no me alcanza el U, ¿puedo compensar poniendo más ventanas de doble vidrio?",
     [h("No hay compensación global", r"no"), h("Mejor U permite más % de ventana (Res. 9868)", r"9\.?868|porcentaje|%")], [], [],
     "No hay compensación entre elementos: cada uno cumple su U (Tabla N°10). Lo único: mejor U de ventana permite mayor % (Res. 9868 Tabla 1).",
     ["res-9868-2018", "pda-temuco-ds8-2025"])

# ----------------------------------------------------------------- G2: 5 preguntas reales de validación
G2_FUENTES = ["pda-temuco-ds8-2025", "res-9868-2018", "ds15-2024", "references/pda-ppa.md"]
case("g2-01", "pda", True, """Vivienda nueva de un piso, 92 m², en Padre Las Casas (La Araucanía). Muros de albañilería confinada con aislación, techumbre de zinc sobre estructura de madera, ventanas de PVC. El arquitecto insiste en que basta con cumplir el DS 15 porque "es la norma más nueva". ¿Qué exigencias térmicas aplican realmente y con qué tabla y artículo? Dame U, R100 y ventanas. Y si el mismo proyecto se construyera en Nueva Imperial, ¿cambia algo?""",
     [h("Manda el PDA Temuco (inc. 2°)", r"PDA|plan"), h("DS 8/2023", r"DS\s*(N[°º]\s*)?8"), h("Muro 0,45", rf"0{N}45"), h("Techo 0,28", rf"0{N}28"),
      h("Ventana 3,20", rf"3{N}20?\b"), h("Res. 9868 % ventanas", r"9\.?868"), h("Nueva Imperial sin PDA, zona F, DS 15", r"Nueva Imperial")],
     [r"Tabla\s*N?[°º]?\s*10", r"Tabla\s*1\b"], [rf"provincia de Caut[ií]n[^.\n]{{0,30}}Tabla\s*N?[°º]?\s*12"],
     "Padre Las Casas (zona F) con PDA Temuco DS 8/2023 Art. 27: Tabla N°10 (0,28/0,45/0,50/3,20/1,70), Tabla N°11 R100, 5 ach (Tabla N°12, del plan), permeabilidad clase 2 (Tabla N°13), ventanas además % Res. Ex. 9868; condensación HR 76 % (Art. 27 N°2); ventilación NCh 3309; sin leña (Art. 15). Nueva Imperial: zona F sin PDA → DS 15 Tablas 1–6 (muro 0,45, techo 0,28, piso 0,50), Cautín 5,00 ach.",
     G2_FUENTES)
case("g2-02", "exigencia", True, """Colegio particular subvencionado de dos pisos en Arica, a 350 m de altitud, con salas de clases, comedor y gimnasio. ¿Qué U y R100 le aplican? El sostenedor quiere saber además si tiene que hacer memoria de condensación, ensayo de infiltración y informe de ventilación. Si en vez de colegio fuera un hotel en la misma comuna, ¿qué cambia?""",
     [h("Zona A", r"zona\s*(t[eé]rmica\s*)?A\b"), h("Tabla 10 educación", r"Tabla\s*10"), h("Muro 2,00 (educación)", rf"2{N}00?\b"),
      h("Ventilación NCh 3308", r"NCh\s*3308"), h("Hotel exento de B, C y D", r"exent|eximid"), h("Hotel Tabla 12 ventanas", r"Tabla\s*12")],
     [r"Tabla\s*10"], [], "Arica 350 m = zona A. Colegio: Tabla 10 (0,84/2,00/3,60), Tabla 11 (119/50/28), Tabla 12 (5,80), Tabla 13 sin exigencia; B sí (clima Arica 13,6 °C/73 %), infiltración provincia Arica sin exigencia, permeabilidad zona A sin exigencia, D NCh 3308. Hotel: Tablas 1, 2, 6 (muro 2,10; R100 48) + ventanas Tabla 12; exento de B, C y D.",
     ["ds15-2024", "ds15-tabla-zonas", "references/alcance-y-vigencia.md"])
case("g2-03", "firmas", True, """Vivienda nueva en Temuco con PDA, con solución LOSCAT para muros y techumbre. Necesito el listado completo del expediente: qué documento va en el permiso y cuál en la recepción, quién firma cada uno, y qué pasa si en la región no hay ensayador de infiltración registrado.""",
     [h("Permiso vs recepción", r"recepci"), h("Ensayo NCh 3295 en recepción", r"3295"), h("Tabla Nº 14 del plan para la muestra", r"Tabla\s*N?[°º]?\s*14"),
      h("Sellos en EETT según el plan", r"sellos"), h("Arquitecto informa la alternativa / suscribe", r"arquitect")],
     [r"5\.1\.6|5\.2\.6"], [r"Tabla\s*8\s*no fija", r"mientras[^.|\n]{0,90}no existan", r"DS\s*15[^|\n]{0,12}Tabla\s*12"],
     "Permiso (OGUC 5.1.6 N°11): EETT, LOSCAT vigente que cumpla valores del plan (Art. 27 N°1 d), R100/Tabla N°11 o cálculo; % ventanas Res. 9868 (informe profesional competente); memoria de condensación NCh 1973 HR <76 % (proyectista); sistema de calefacción no-leña (Art. 15); ventilación NCh 3309. Recepción (5.2.6 N°7): ensayo NCh 3295 con muestra Tabla Nº 14 del plan (lote <11 → 1), por arquitecto/consultor DS 135/lab DS 10. Sin ensayador: el plan admite sellos en EETT hasta que MINVU lo deje sin efecto; NO importar condiciones del DS 15 (región, lote ≤10).",
     G2_FUENTES + ["references/roles-firmas-expediente.md"])
case("g2-04", "supuestos", True, """Muro perimetral con estas capas, de interior a exterior: yeso-cartón 12,5 mm, OSB 11 mm, EPS 40 mm, albañilería de ladrillo 140 mm, yeso 15 mm. Dame el U del complejo y dime si cumple en zona D. Si te faltan datos, declara los supuestos. Y aparte: fachada poniente de 12 m² con 3 ventanas de 1,5 × 1,2 m, ¿cumple el porcentaje de ventanas y qué Upvm necesito?""",
     [h("Declara supuestos de λ", r"supuest"), h("Usa Rsi 0,13", rf"R_?\{{?si\}}?[^\n]{{0,50}}0{N}13"), h("Usa Rse 0,04", rf"R_?\{{?se\}}?[^\n]{{0,50}}0{N}04"), h("Exigencia muro zona D 0,80", rf"0{N}80"),
      h("Ventanas 5,4 m² = 45 %", r"45\s*%|5[,.]4"), h("Depende del U de la ventana (Tabla 3 D Poniente)", r"\b(60|53|49|44)\b"),
      h("Upvm Tabla 5", r"Upvm")],
     [r"Tabla\s*1\b", r"Tabla\s*3"], [],
     "U = 1/(Rsi 0,13 + Σe/λ + Rse 0,04) con λ declarados como supuestos (sin tabla NCh 853); muro zona D U ≤ 0,80 (Tabla 1); un muro con 40 mm EPS normalmente cumple pero depende de λ. Ventanas: 3×1,8 = 5,4 m² / 12 m² = 45 %; zona D Poniente (O-P): U≤2,8 → 60 % cumple; U≤3,6 → 53 % cumple; U≤4,0 → 49 % cumple; U≤4,4 → 44 % NO cumple; U≤5,8 → 15 % NO. Upvm (Tabla 5, D O-P) depende de Uv y Um: debe pedir el U de la ventana o dar escenarios (un ejemplo con Uv 3,6 dentro de los escenarios es válido: D O-P 1,81/2,00/2,28 para Uv ≤2,4/2,8/3,6). Es correcto y no obligatorio agregar que la vía aislante rotulado exige R100 ≥125 en zona D (Tabla 2) y que 40 mm de EPS no la alcanzan, por lo que se acredita por cálculo, ensayo o LOSCAT; si la vivienda está en un PDA (no indicado) mandan las tablas del plan.",
     ["ds15-2024", "res-ex-1802-2025", "references/exigencias-A-envolvente.md"])
case("g2-05", "trampa", True, """Me dijeron que como el DS 15 es posterior al PDA de Temuco, ahora manda el DS 15 y el plan ya no se aplica. Además el arquitecto dice que con la CEV del DS 5/2024 se acredita todo el 4.1.10, y que si no me alcanza el U compenso poniendo más ventanas de doble vidrio. El constructor quiere además presentar el ensayo de infiltración en el permiso para no atrasar la recepción. ¿Está todo bien así?""",
     [h("PDA prevalece en vivienda (inc. 2°); DS 8/2023 es posterior", r"inc(iso)?\.?\s*2|prevalec|manda el (plan|PDA)|sigue mandando"), h("CEV DS 5 no acredita el 4.1.10", r"DS\s*(N[°º]\s*)?5"),
      h("No hay compensación global", r"compens"), h("Ensayo de infiltración en recepción", r"recepci")],
     [], [r"s[ií],? (est[aá] (todo )?bien|es correcto)"],
     "Las 4 premisas son falsas: (1) en vivienda manda el PDA (Art. 4.1.10 inc. 2°) y además el DS 8/2023 (D.O. 07-03-2025) es posterior al DS 15; (2) la CEV del DS 5/2024 es otro régimen; la vía por demanda del 4.1.10 es solo A, solo vivienda y su umbral está pendiente; (3) no hay compensación entre elementos: cada uno cumple su U; mejor U de ventana solo permite más % (Res. 9868); (4) el ensayo NCh 3295 es con obra terminada, en la recepción.",
     G2_FUENTES + ["references/trampas.md"])


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CASES:
        (OUT / f"{c['id']}.yaml").write_text(yaml.safe_dump(c, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print(len(CASES), "casos;", sum(c["critical"] for c in CASES), "critical")


if __name__ == "__main__":
    main()
