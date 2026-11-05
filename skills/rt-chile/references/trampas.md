# Trampas frecuentes (errores que la skill debe detectar y corregir)

Verificado: **2026-11-05**. Cada trampa cita dónde se resuelve. Fuentes principales: `ds15-2024`, `oguc-2026-03`,
`res-ex-1802-2025`, `loscat-e14`, `ds5-2024-cev`. Contradicciones entre fuentes: `docs/contradicciones.md`.

| # | Trampa | Lo correcto | Dónde |
|---|---|---|---|
| T01 | **"Me dieron un U, ¿qué espesor de aislante pongo?"** como si fuera directo | U es del **complejo completo**, con todas sus capas y resistencias superficiales. El espesor sale de un cálculo (NCh 853 + Res. Ex. 1802) o de una ficha LOSCAT/R100 vigente. La vía R100 da un R100 mínimo del aislante (Tabla 2), no un U | `exigencias-A-envolvente.md`; `vias-acreditacion.md` |
| T02 | **"Con la CEV cumplo la RT"** | La vía por demanda (Informe de Precalificación) es **solo para viviendas**, reemplaza **solo A** y su **umbral no está publicado** (rige ≈ mayo 2027). Condensación, infiltración y ventilación se acreditan siempre. La **CEV del DS 5/2024** (etiqueta en la recepción) es otro régimen y no acredita el 4.1.10 | `vias-acreditacion.md` §3 |
| T03 | **Usar la "OGUC septiembre 2025"** como vigente para el 4.1.10 | Ese texto (DS 21) **no incluye** el 4.1.10 del DS 15, que rige desde el **28-11-2025**. Usar el DS 15 (D.O.) o la OGUC MINVU de marzo 2026 | `alcance-y-vigencia.md` §4; `oguc-2025-09` vs `oguc-2026-03` |
| T04 | **Hoteles con la Tabla 10** y obligados a condensación e infiltración | Hotel = residencial: **Tablas 1, 2 y 6** + ventanas por **Tabla 12**. **Exentos de B, C y D** | C11; `alcance-y-vigencia.md` |
| T05 | **Ignorar el PDA** en vivienda | En permisos de vivienda (obra nueva, ampliación, reconstrucción) en área con plan vigente **mandan las exigencias del plan** (inc. 2°). Primero, ¿la comuna está en un PDA/PPA con capítulo térmico? | `pda-ppa.md` |
| T06 | Aplicar el PDA a **colegios u hospitales** | El inciso 2° habla de **viviendas**. Educación y salud siguen el 4.1.10 aunque estén en zona PDA | `alcance-y-vigencia.md` §3 |
| T07 | **Un solo "informe térmico"** para todo | Son documentos distintos con firmas distintas: U/Rt (cálculo, ensayo, LOSCAT o R100), % ventanas/Upvm, **memoria de condensación**, **ensayo de infiltración en obra terminada**, permeabilidad y **informe de ventilación** | `roles-firmas-expediente.md` |
| T08 | Exigir **ventilación a salud** | Salud está **eximida** (num. 2.D). Educación solo por NCh 3308 | C25; `exigencias-D-ventilacion.md` |
| T09 | Asignar zona a una **comuna multizona** sin altitud | 59 comunas cambian de zona por altitud o meridiano. Pedir la cota o responder por escenarios. Ojo con las brechas de la tabla (Putre, General Lagos, Camiña, Antuco) | `zonificacion.md` |
| T10 | Confundir **zona** con **provincia** | La infiltración (Tablas 7 y 14) va **por provincia**. Todo lo demás va por zona | `exigencias-C-infiltracion.md` |
| T11 | Suponer que la exigencia **crece de A a I** en todo | En muros, la zona I (0,35) es **menos** exigente que la H (0,30). En piso ventilado, C (0,87) es menos exigente que B (0,70) | `exigencias-A-envolvente.md` |
| T12 | **Permeabilidad** leída como máximo | Se exige clase **≥** la de tabla (3 es más exigente que 1). La infiltración, en cambio, es un **máximo** en ach | `exigencias-C-infiltracion.md` |
| T13 | **Solución LOSCAT vencida** o de la E13 | Las fichas E13 vencieron el 26-11-2025. La mayoría de las E14 vencen en **diciembre de 2026**. Verificar contra la fecha de la consulta | `loscat.md`; `docs/cambios-fuentes.md` |
| T14 | **75 % HR vs. 100 %** en condensación como si fueran contradictorios | 75 % es la HR **interior** del cálculo; 100 % (u 80 % para moho) es el **umbral crítico superficial** | C03; `exigencias-B-condensacion.md` |
| T15 | Omitir el **puente térmico** en condensación | La Res. Ex. 1802 exige al menos las secciones A (mayor R) y B (menor R, puente térmico) | `exigencias-B-condensacion.md` |
| T16 | Ofrecer la **alternativa de sellos** a cualquiera | Solo si en la región no hay ensayadores registrados, en residencial con lote **≤ 10**, y mientras MINVU no la elimine por resolución | `exigencias-C-infiltracion.md` |
| T17 | Valores PDA "de memoria" o del **informe-resumen** interno | Usar **solo** las tablas del decreto (Temuco muro 0,45; O'Higgins techo 0,38; Talca piso 0,60), con su artículo y tabla | C12; `pda-ppa.md`, `data/pda.csv` |
| T18 | Responder que el PDA de Temuco es "DS 8/2025" | Es el **DS 8/2023** (MMA), publicado en el D.O. el 07-03-2025 | C13 |
| T19 | Presentar el **ensayo de infiltración en el permiso** | Se hace con la **obra terminada** y va en la **recepción** | `roles-firmas-expediente.md` |
| T20 | Usar la **NCh 3136** como exigible para puentes térmicos | El DS 15 y la Res. Ex. 1802 no la citan | `docs/verificaciones.md` §3 |
| T21 | Hacer depender una respuesta de la **edición de la NCh 1079** | La zona se asigna con la **tabla oficial MINVU**. Edición "probablemente 2019, oficial pendiente" | `zonificacion.md` |
| T22 | **Mezclar tablas FSEV o VIT** con las del 4.1.10 | Son regímenes distintos y quedan fuera de alcance. Detectar, avisar en una línea y remitir | AGENTS.md regla 9; C06 |
| T23 | Pedir o entregar **texto de una NCh** | Negarse y remitir al visor https://normastecnicas.minvu.cl/ | `normas-nch.md`; `docs/COPYRIGHT-POLICY.md` |
| T24 | Usar la **lámina DITEC** como fuente de la Tabla 7 | La lámina omite Malleco. Manda el DS 15 (Malleco = 5,00 ach) | C24 |
| T25 | Decir que **Upvm solo existe en comunas sin plan** | Los planes de O'Higgins (DS 1/2021) y Quillota (DS 18/2023) sí admiten una vía Upvm propia, con sus condiciones. En los demás planes con tablas de ventanas, revisar el plan con `scripts/pda.py` | `pda-ppa.md`; `data/pda.csv` |
| T26 | **Mezclar las exenciones** de hoteles y salud | Hotel: exento de B, C y D. **Salud: exenta solo de D**; sí cumple condensación e infiltración | `alcance-y-vigencia.md`; `exigencias-D-ventilacion.md` |

## Cómo usar este archivo

Ante cualquier pregunta, la skill revisa si cae en alguna de estas trampas antes de responder. Si cae, corrige la
premisa en una línea y cita la fuente. Cada trampa debería tener al menos un caso en `evals/cases/`.
