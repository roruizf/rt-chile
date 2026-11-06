# Auditoría de 2026-11-06_0649_opencode.jsonl

**Resultado:** 8 de 10 sin errores; 1 valor incorrecto (`pda-08`) y 1 cita incorrecta (`zona-01`). No cumple el criterio de 10 sin valores incorrectos.

Muestra: 10 de 88 aprobados (semilla 611).
Comparar cada cifra y cita con `data/` y `references/`. Veredicto: correcto, o el error y si es de la skill, del modelo o del caso.

## condensacion-03

**Pregunta:** ¿Qué temperatura y humedad exterior uso para condensación en Punta Arenas?

**Rúbrica:** Anexo 1 Res. Ex. 1802.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

**Respuesta directa:** Para el cálculo de condensación (exigencia B) en Punta Arenas usa **T° exterior = −1,6 °C** y **HR exterior = 93 %**, con **19 °C y HR interior ≤ 75 %**. Sale del Anexo 1 de la Res. Ex. 1802, no de la tabla de zonas del DS 15.

**Datos del caso**

| Dato | Valor |
|---|---|
| Uso | Residencial (por defecto; si es hotel, está exento de B) |
| Comuna | Punta Arenas, provincia de Magallanes |
| Zona térmica | **I**, toda la comuna (sin condición de altitud/meridiano) |
| PDA/PPA | No registrado → rige el Art. 4.1.10 |
| Fecha considerada | 06-11-2026 (norma vigente desde el 28-11-2025) |

**Condiciones de cálculo — Res. Ex. 1802, num. 1.2 y Anexo 1**

| Parámetro | Valor | Cita |
|---|---|---|
| T° exterior | **−1,6 °C** | Res. Ex. 1802, Anexo 1 (fila Punta Arenas, zona I) |
| HR exterior | **93 %** | Res. Ex. 1802, Anexo 1 |
| T° interior | 19 °C | Res. Ex. 1802, num. 1.2 |
| HR interior | hasta 75 % (inclusive) | Res. Ex. 1802, num. 1.2 |
| φsi,cr superficial | 1,0 (100 %); opcional 0,8 (80 %) para moho | Res. Ex. 1802, num. 1.1 |
| Rsi / Rse | Techo 0,10/0,04 · Muro 0,13/0,04 · Piso ventilado 0,17/0,04 | Res. Ex. 1802, Anexo 2 |

Notas:
- Punta Arenas **no** es particularidad climática (p): no corresponde aplicar los valores de la Antártica.
- Si acreditas la misma solución para varias zonas, la macrozona **H/I** da exactamente −1,6 °C / 93 % (Res. Ex. 1802, final del Anexo 1). La zona I no puede agruparse con la zona A ni con territorios insulares/antárticos.
- Estas cifras son solo para condensación. No las uses como temperatura de diseño de calefacción ni como dato de demanda.
- El cálculo debe incluir **sección A** (mayor R) y **sección B** (puente térmico) y los puentes térmicos en la condensación superficial (Res. Ex. 1802, num. 1.1). Única vía: **memoria de cálculo**; el LOSCAT o la CEV no la acreditan.

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 05-11-2026.

*Fuentes oficiales a revisar:*
- Res. Ex. 1802 (condiciones de cálculo): https://www.minvu.gob.cl/wp-content/uploads/2025/11/Condiciones-de-Calculos-Condensacion_Res.-Ex.-1802.pdf
- DS 15 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- NCh 1973 en el visor: https://normastecnicas.minvu.cl/

</details>

## exigencia-09

**Pregunta:** ¿Puedo usar la alternativa Upvm en una vivienda en Iquique?

**Rúbrica:** Iquique zona A: Upvm solo en zonas B a I.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**No.** La alternativa **Upvm de la Tabla 5** solo existe para las zonas **B a I**; en **zona A** la Tabla 5 no tiene valores ("na"). Iquique es zona **A** en toda la comuna, así que no puedes usarla: las ventanas se justifican con la **Tabla 3** (% máximo de ventanas por orientación) — DS 15/2024, Art. 4.1.10 num. 1.A.5, Tablas 3–5.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda |
| Comuna | Iquique (Región de Tarapacá, provincia de Iquique) |
| Zona térmica | **A** (toda la comuna, sin condición de altitud) |
| PDA/PPA | No registrado: rige el Art. 4.1.10 |
| Fecha considerada | 06-11-2026 |

## Exigencias que aplican (zona A, vivienda)

| Elemento | Exigencia | Fuente |
|---|---|---|
| Techumbre | U ≤ 0,84 W/m²K (Rt ≥ 1,19) | DS 15, Tabla 1, zona A |
| Muro | U ≤ 2,10 W/m²K (Rt ≥ 0,48) | DS 15, Tabla 1, zona A |
| Piso ventilado | U ≤ 3,60 W/m²K (Rt ≥ 0,28) | DS 15, Tabla 1, zona A |
| Puerta opaca | Sin exigencia | DS 15, Tabla 1, zona A |
| Ventanas | **Tabla 3**: % máximo de vanos por orientación según U | DS 15, num. 1.A.5 |
| Sobrecimiento | Sin exigencia de R100 | DS 15, Tabla 6, zona A |
| Infiltración | Sin exigencia (provincia de Iquique) | DS 15, Tablas 7 y 14 |
| Permeabilidad | Sin clase mínima exigida | DS 15, Tablas 9 y 16 |
| Ventilación | Sistema según NCh 3308/3309, "según corresponda" (interior de vivienda: NCh 3309) | DS 15, num. 1.D |

Para dimensionar la Tabla 3 en A, algunos puntos de referencia (% máximo de vanos):

| U ventana | Norte | Oriente-Poniente | Sur | OGT (si <60 % de muro expuesto) |
|---|---|---|---|---|
| ≤ 3,6 | 94 % | 80 % | 69 % | 44 % |
| ≤ 2,0 | 100 % | 94 % | 85 % | 50 % |
| ≤ 5,8 | 50 % | 30 % | 25 % | 25 % |

En la práctica, la zona A es poco restrictiva para ventanas, pero **el % no es automático**: hay que calcularlo con las superficies interiores de paramentos por orientación (incluyendo medianeros) y el U mayor de cada orientación.

## Cómo acreditar

- **Ventanas (Tabla 3):** informe por orientación que demuestre SMV ≥ superficie de vanos. El U de cada ventana sale de Informe de Ensayo NCh 3076/1-2 (laboratorio registro DS 10), Memoria de Cálculo NCh 3137/1-2 o solución LOSCAT vigente.
- **Techumbre, muros y piso:** aislante rotulado NCh 2251 con R100 ≥ Tabla 2, ensayo NCh 851 (≤ 10 años), memoria de cálculo NCh 853/3117 o LOSCAT.
- **Ventilación:** informe de cumplimiento de la tasa NCh 3309 (no hay vía LOSCAT ni por demanda para D).
- Todo se presenta en el permiso (OGUC Art. 5.1.6 N° 11); los informes los suscribe el profesional competente y además el arquitecto.

## Advertencias

- No confundas esto con la **vía por demanda (CEV)**: es la única alternativa general para viviendas, reemplaza solo la exigencia A y su **umbral sigue pendiente** de resolución MINVU (vigencia prevista hacia mayo de 2027). No es lo mismo que el Upvm.
- Si menos del 60 % de la superficie de muros perimetrales está expuesta, aplica la fila **OGT** de la Tabla 3 sobre el total de paramentos.
- En zona A no hay Upvm ni exigencia de infiltración/permeabilidad, pero sí sigue aplicando condensación (B) y ventilación (D).

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 05-11-2026.

*Fuentes oficiales:* [DS 15/2024 en el D.O.](https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf) · [Reglamentación térmica MINVU](https://www.minvu.gob.cl/nueva-reglamentacion-termica/) · [LOSCAT y listados DITEC](https://www.minvu.gob.cl/ditec/) · [Visor NCh](https://normastecnicas.minvu.cl/)

</details>

## fuera-alcance-02

**Pregunta:** Somos empresa de viviendas industrializadas tipo (VIT): ¿qué tabla usamos?

**Rúbrica:** VIT fuera de alcance: avisar y remitir.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

**Respuesta directa:** No hay una tabla del Art. 4.1.10 para VIT. La Vivienda Industrializada Tipo es un régimen distinto (**Res. Ex. 59/2023**), está **fuera del alcance de esta skill** y sus tablas no se mezclan con las del DS 15.

**Datos del caso**
- Uso: vivienda (industrializada tipo).
- Comuna / zona: no informada.
- PDA: no evaluado (sin comuna).
- Fecha considerada: 06-11-2026 (DS 15 vigente desde el 28-11-2025).

**Qué sí puedo hacer**
- Remitirte a la fuente VIT: **Res. Ex. 59/2023** y sus anexos. No reproduzco ni aplico sus requisitos, puntajes ni tablas (regla de alcance).
- Revisar el **mismo proyecto** contra el Art. 4.1.10 (envolvente, condensación, infiltración, ventilación) y contra el PDA/PPA si la comuna lo tiene. Para eso necesito: comuna (y altitud o meridiano si es multizona), fecha de ingreso del permiso y uso exacto.

**Exigencias 4.1.10 que aplicarían a la vivienda (informativo)**
Dependen de la zona térmica; sin comuna no hay valores. En vivienda las tablas son, en general, **Tablas 1 y 2** (U/Rt y R100), **Tabla 6** (sobrecimiento), **Tablas 3 a 5** (ventanas por orientación o Upvm) —la Tabla 12 es solo educación, salud y hoteles—, más B (Res. Ex. 1802), C (Tablas 7–9 y 14–16) y D.

**Advertencia**
No uses una tabla VIT para acreditar el 4.1.10 ni viceversa: son regímenes separados y una misma vivienda puede quedar sujeta a ambos controles. Si el proyecto postula a VIT, la tabla y sus condiciones están en la Res. Ex. 59/2023, no en esta skill.

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

**Fuentes oficiales a revisar**
- Res. Ex. 59/2023 (VIT) y listados DITEC: https://www.minvu.gob.cl/ditec/
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## pda-07

**Pregunta:** Vivienda en Concón: ¿el PPA de Concón-Quintero-Puchuncaví fija exigencias de envolvente?

**Rúbrica:** DS 105/2018 sin envolvente.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**No.** El PPDA de Concón, Quintero y Puchuncaví (DS 105/2018 MMA, D.O. 30-03-2019) **no fija exigencias de envolvente térmica** para vivienda. No tiene capítulo térmico: solo regula el recambio voluntario de calefactores (Art. 41) y el tratamiento de emisiones de proyectos inmobiliarios que ingresan al SEIA (Art. 42 b). Por lo tanto, en Concón rige **íntegro el Art. 4.1.10 OGUC (DS 15/2024)**.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda (residencial) |
| Comuna | Concón, Región de Valparaíso |
| Zona térmica | **C** — toda la comuna (tabla MINVU de zonas) |
| PDA/PPA | PPDA Concón-Quintero-Puchuncaví, DS 105/2018 — cobertura total, **sin envolvente** |
| Infiltración | Provincia de **Valparaíso** → 5,00 ach a 50 Pa |
| Fecha considerada | 06-11-2026 (DS 15 vigente desde el 28-11-2025) |

## Exigencias que aplican (Art. 4.1.10, zona C)

| Elemento | Exigencia | Fuente |
|---|---|---|
| Techumbre | U ≤ 0,47 W/m²K / Rt ≥ 2,13 | DS 15, Tabla 1 |
| Muros perimetrales | U ≤ 0,80 W/m²K / Rt ≥ 1,25 | DS 15, Tabla 1 |
| Piso ventilado | U ≤ 0,87 W/m²K / Rt ≥ 1,15 | DS 15, Tabla 1 |
| Puertas opacas | U ≤ 1,70 W/m²K | DS 15, Tabla 1 |
| Ventanas | % máx. por orientación según su U (Tabla 3) **o** Upvm (Tabla 5); en techumbre, U ≤ 3,6 | DS 15, num. 1.A.5 |
| R100 del aislante | Techumbre 213 · Muro 125 · Piso ventilado 115 | DS 15, Tabla 2 |
| Sobrecimiento | R100 ≥ 45 | DS 15, Tabla 6 |
| Condensación (B) | Sin riesgo superficial ni intersticial; NCh 1973 + Res. Ex. 1802 (19 °C, HR hasta 75 %) | DS 15, num. 1.B |
| Infiltración (C) | Clase ≤ 5,00 ach a 50 Pa (provincia de Valparaíso) | DS 15, Tabla 7 |
| Permeabilidad (C) | Clase ≥ 1 a 100 Pa en puertas y ventanas | DS 15, Tabla 9 |
| Ventilación (D) | Tasa según NCh 3308/3309 | DS 15, num. 1.D |

Para ventanas en zona C, a modo de referencia con U ≤ 3,6: Norte 83 %, Oriente-Poniente 62 %, Sur 49 %, OGT 35 % del paramento respectivo (DS 15, Tabla 3). Con un U menor se permite más superficie; el porcentaje exacto se lee según el U de la ventana.

## Cómo acreditar

- **U/Rt de opacos:** aislante rotulado NCh 2251 con el R100 de la Tabla 2, informe de ensayo DS 10 (≤ 10 años), memoria de cálculo (NCh 853/NCh 3117) o solución LOSCAT vigente.
- **Ventanas:** ensayo NCh 3076/1-2, cálculo NCh 3137/1-2 o LOSCAT, más el informe de % por orientación o Upvm.
- **Condensación:** solo memoria de cálculo higrotérmica; no hay LOSCAT ni ensayo que la reemplace.
- **Infiltración:** ensayo NCh 3295 **en obra terminada**, en la recepción (arquitecto, consultor DS 135 o laboratorio DS 10). Para lotes de 1 a 10 viviendas no hay muestra fijada: supuesto prudente, 1 vivienda representativa.
- **Ventilación:** informe de tasa según NCh 3309 (interior de vivienda).
- Los informes los elabora un profesional competente y los suscribe además el arquitecto (Art. 4.1.10 inc. 4°).

## Advertencias

- Si el permiso ingresó **antes del 28-11-2025**, se evalúa con la norma anterior (OGUC Art. 1.1.3); confirma la fecha de ingreso.
- No hay que comparar valores "del plan" contra el 4.1.10: el plan simplemente no regula la materia.
- La mayoría de las fichas LOSCAT E14 vencen en diciembre de 2026: verifica vigencia a la fecha de tu permiso.
- La vía por demanda (Informe de Precalificación Energética) sigue con **umbral pendiente** (rige ≈ mayo 2027) y no reemplaza B, C ni D.

---

**Límites:** Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

**Fuentes oficiales a revisar:**
- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Portal PPDA del MMA: https://ppda.mma.gob.cl/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## pda-08

**Pregunta:** Vivienda nueva en Valdivia: ¿qué U de ventana exige el PDA?

**Rúbrica:** La Tabla N°16b del DS 25/2016 dice 'por definir MINVU', pero no quedó pendiente: la Res. Ex. 1729/2019 (Tabla 1 según Res. Ex. 1197/2021) no fija un U máximo, sino % máximo de ventana por orientación según el U (zona G: U ≤3,6 Norte 59, O-P 28, Sur 13). La U 3,60 de la Tabla 16a es de vivienda existente, no nueva. Falla si da una U única como exigencia.

**Veredicto:** **Error del modelo:** la fila U ≤ 4,4 dice 0/0/0/0 y la fuente dice 46/20/0/0; también afirma que sobre U 4,0 no se admite ventana. `pda.py` y `data/` están bien. Repetido 3 veces: correcto las 3.

<details><summary>Respuesta</summary>

## Respuesta directa

El PDA de Valdivia **no exige una U máxima única de ventana**. Exige un **porcentaje máximo de ventana por orientación en función de la U de la ventana**: mientras mejor sea la U, más superficie de ventana se permite. La celda “por definir MINVU” del DS 25/2016 no se completó con un U máximo, sino con esa tabla de porcentajes (Res. Ex. 1729/2019, Tabla 1 vigente según Res. Ex. 1197/2021). Por eso, si buscas “el U que exige el PDA”, la premisa es incorrecta: no hay un valor único.

## Datos del caso

- **Uso:** vivienda nueva.
- **Comuna:** Valdivia, Región de Los Ríos; **zona G** (toda la comuna).
- **PDA:** Valdivia, **DS 25/2016 MMA** (D.O. 23-06-2017), cobertura total, exige envolvente.
- **Acto que completa ventanas:** **Res. Ex. N°1729 MINVU** (30-07-2019; D.O. 05-08-2019), **Tabla 1 reemplazada por Res. Ex. N°1197** (D.O. 21-07-2021).
- **Fecha considerada:** 06-11-2026.
- **Supuesto:** permiso de obra nueva ingresado después del 28-11-2025 (Art. 4.1.10 del DS 15 vigente). El PDA de Valdivia igualmente aplica por el inc. 2° del Art. 4.1.10.

## Exigencia de ventanas

**Porcentaje máximo de vanos por orientación, según la U de la ventana** — Res. Ex. 1729/2019, Tabla 1 (texto vigente Res. Ex. 1197/2021), zona PDA Valdivia:

| U de la ventana | Norte | Oriente-Poniente | Sur | POND |
|---|---:|---:|---:|---:|
| ≤ 1,6 W/m²K | 76 % | 40 % | 26 % | 27 % |
| ≤ 2,0 | 74 % | 38 % | 24 % | 26 % |
| ≤ 2,4 | 71 % | 36 % | 21 % | 24 % |
| ≤ 2,8 | 67 % | 34 % | 19 % | 21 % |
| ≤ 3,2 | 64 % | 31 % | 16 % | 19 % |
| ≤ 3,6 | 59 % | 28 % | 13 % | 16 % |
| ≤ 4,0 | 54 % | 24 % | 8 % | 12 % |
| ≤ 4,4 | 0 % | 0 % | 0 % | 0 % |

Notas de aplicación:

- El porcentaje se calcula sobre la **superficie interior de los paramentos verticales perimetrales de cada orientación, incluidos los medianeros**. Norte: [315°, 45°); Oriente: [45°, 135°); Sur: [135°, 225°); Poniente: [225°, 315°); Oriente y Poniente se agrupan como “O-P”.
- Si hay ventanas con distinto U en una misma orientación, se usa **la U mayor**.
- La fila **POND** se usa si menos del **60 %** de los muros perimetrales está expuesto; se aplica al total de paramentos verticales.
- Con **U > 4,0 W/m²K** el porcentaje permitido es **0 %**: en la práctica, no podrías incorporar ventanas en esa orientación. No es que el PDA “prohíba” la ventana, sino que no otorga superficie.
- **Ventana en techumbre** (plano de 60° o menos): **U ≤ 3,6 W/m²K** — Res. Ex. 1729/2019, A.1/B.
- La Tabla 1 del plan coincide con la **Tabla 3 del Art. 4.1.10 para zona G**; no hay una exigencia del 4.1.10 más estricta que obligue a corregir el valor. La vía **Upvm de la Tabla 5** del 4.1.10 no está incorporada en este plan; no la uses sin confirmación de la DOM.

## Cómo acreditar

- **U de la ventana:** Informe de Ensayo **NCh 3076/1-2** de laboratorio inscrito en el registro DS 10, Memoria de Cálculo **NCh 3137/1-2**, o solución **LOSCAT E14 vigente**.
- **% de ventanas por orientación:** informe firmado por **profesional competente o especialista**; el arquitecto lo suscribe. Se presenta en el **permiso de edificación** (OGUC Art. 5.1.6 N° 11).
- **Permeabilidad al aire de la ventana:** el plan exige **clase 7 a 100 Pa** para puertas y ventanas (DS 25/2016, Art. 28, Tabla N°19), acreditada por **laboratorio DS 10**.
- La **infiltración** de la vivienda (5 ach a 50 Pa, Tabla N°18) es un ensayo distinto, de obra terminada, y va en la **recepción**.

## Advertencias

- **LOSCAT:** la mayoría de las fichas E14 vencen en **diciembre de 2026**. Si usas LOSCAT para la U, verifica que la ficha esté vigente a la fecha del permiso y que cumpla el valor del plan.
- El PDA también exige **condensación** (Res. Ex. 1729: julio, 19 °C, HR 65/75/80 %), **infiltración** y **ventilación** con extracción mecánica en baño y cocina; esta respuesta cubre solo ventanas.
- Si el permiso ingresó **antes del 28-11-2025**, revisa el régimen transitorio; la Tabla 1 del plan, en todo caso, rige desde 2019.

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **2026-11-05**.

**Fuentes oficiales a revisar:**
- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Portal PPDA del MMA: https://ppda.mma.gob.cl/

</details>

## supuestos-01

**Pregunta:** Muro de 15 mm yeso + 100 mm lana mineral + 11 mm OSB en Osorno. ¿Cumple?

**Rúbrica:** Faltan λ: debe declarar supuestos, calcular por escenarios y advertir que en Osorno rige el PDA (muro 0,40).

**Veredicto:** Valores normativos correctos. Los U con entramado son una estimación propia, sin fuente, con 1 a 2 % de diferencia respecto de un promedio por áreas.

<details><summary>Respuesta</summary>

## Respuesta directa

**Depende de la estructura y de la condensación.** En cálculo homogéneo el complejo da **U ≈ 0,36 W/m²K** y cumple el máximo de **0,40** de la zona G/PDA Osorno. Pero con un entramado de madera típico (≈10 % del paño) el U sube a **0,41–0,45** y **deja de cumplir**. Además, el OSB en la cara fría sin barrera de vapor hace **muy probable** la condensación intersticial, que es una exigencia aparte.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda nueva (supuesto) |
| Comuna | Osorno, Región de Los Lagos |
| Zona térmica | **G** — toda la comuna |
| PDA/PPA | **PDA Osorno, DS 47/2015 MMA** (D.O. 28-03-2016), cobertura total, exige envolvente |
| Fecha considerada | **2026-11-06**; DS 15 vigente desde el 28-11-2025 |

**Supuestos:** λ yeso 0,25; lana mineral 0,040; OSB 0,13 W/m·K; Rsi 0,13 y Rse 0,04 m²K/W; OSB en la cara exterior; sin cámara de aire ni revestimiento exterior; 100 mm de lana continua o en cavidad.

## Exigencias que aplican al muro

| Exigencia | Valor | Fuente |
|---|---|---|
| U máx. muro | **0,40 W/m²K** | PDA Osorno, DS 47/2015, Art. 8, Tabla 24a (vivienda nueva desde 2019). Art. 4.1.10, Tabla 1, zona G: **0,40**, igual |
| R100 mín. del aislante | **250** (m²K/W ×100) | PDA Osorno, Tabla 25; Art. 4.1.10, Tabla 2: 250 |
| Condensación superficial e intersticial | Sin riesgo, NCh 1973 + condiciones del plan | DS 15, num. 1.B; Ord. 1773 y Res. Ex. 9869 (PDA Osorno) |

> El mismo 0,40 se aplica a hotel, educación y salud en zona G (Tabla 10). Lo que cambia por uso son B, C y D, no el U del muro.

## Cálculo del U

| Capa | Espesor | R (m²K/W) |
|---|---:|---:|
| Yeso | 15 mm | 0,060 |
| Lana mineral (λ 0,040) | 100 mm | 2,500 |
| OSB | 11 mm | 0,085 |
| Rsi + Rse | — | 0,170 |
| **Total** | | **2,815** |

**U = 1 / 2,815 = 0,355 W/m²K → cumple 0,40.**

Sensibilidad: con λ 0,035 → U 0,315; con λ 0,045 → U 0,394. Con λ sobre 0,045 el cálculo homogéneo ya se acerca o supera el límite.

### El punto crítico: los puentes térmicos

El cálculo anterior supone lana continua. Si la lana va entre pies derechos de madera (λ ≈ 0,13), el U real sube:

| Fracción de madera | U resultante | ¿Cumple 0,40? |
|---|---:|---|
| 6,25 % (2×4 cada 600 mm) | 0,395 | Sí, al límite |
| 9,5 % (2×4 cada 400 mm) | **0,415** | **No** |
| 15 % (con soleras, dinteles, esquinas) | **0,449** | **No** |

El umbral está alrededor de **7–8 %** de madera. Un tabique real con soleras, jambas y dinteles suele superarlo. Si es un panel sin entramado, el U 0,355 sí cumple.

## Condensación: el otro requisito

El OSB está en la **cara fría** y es un freno de vapor; el yeso interior no es una barrera de vapor fiable. Con 19 °C y 75 % HR, el punto de rocío es ≈14,3 °C, mientras la cara interna del OSB queda cerca de 4 °C en régimen estacionario. Sin barrera de vapor interior ni cámara ventilada exterior, el riesgo intersticial es alto.

El PDA Osorno exige calcularlo con **julio, 19 °C interior, HR 65/75/80 % (Res. 9869; Ord. 1773 indica 85 % en el tercer caso) y clima exterior de la provincia: 3,5 °C / 98 %**. La única vía es **memoria de cálculo NCh 1973**. El DS 15 además exige que el vapor pueda salir al exterior (num. 1.B); el OSB exterior sin cámara lo dificulta.

## Cómo acreditar

| Elemento | Vía | Quién firma | Etapa |
|---|---|---|---|
| U del muro | Memoria de cálculo NCh 853 + Res. Ex. 1802; o R100 ≥ 250 en EETT; o ensayo NCh 851 de laboratorio DS 10 (≤10 años); o LOSCAT E14 vigente | Profesional competente/especialista + arquitecto (memoria); arquitecto (EETT/LOSCAT); laboratorio DS 10 (ensayo) | Permiso (OGUC 5.1.6 N°11) |
| Condensación | Memoria NCh 1973 con condiciones del plan | Profesional competente/especialista + arquitecto | Permiso |
| Infiltración | Ensayo NCh 3295 en obra terminada | Arquitecto, consultor DS 135 o laboratorio DS 10 | Recepción (5.2.6 N°7) |

Para la vía R100: 100 mm con λ 0,040 dan **R100 = 250 exacto**. Solo sirve si la ficha del producto declara **R ≥ 2,50 m²K/W**; si declara menos, esa vía no cumple aunque el U calculado sí.

## Pendientes y advertencias

- **Falta definir la estructura**: madera o metal, separación y fracción. Con metal el puente térmico es peor. Hay que recalcular el U con las secciones reales (NCh 853).
- **La solución descrita no acredita condensación**. Agregar revestimiento exterior con cámara ventilada y definir el control de vapor del lado cálido; luego verificar con NCh 1973.
- **R100 al límite exacto**: no confiar en 250 si la ficha no lo respalda.
- **LOSCAT**: si se usa una ficha E14, verificar vigencia a la fecha; la mayoría vence en diciembre de 2026.
- **Vía CEV por demanda**: no disponible todavía; el umbral está pendiente (≈mayo 2027). No acredita condensación.

---

**Límites:** Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **2026-11-05**.

**Fuentes oficiales:**
- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## ventilacion-01

**Pregunta:** ¿Puedo acreditar ventilación con la planilla 'Verificación de ventilación NCh 3309 V3.1'?

**Rúbrica:** Debe advertir el desfase: la planilla V3.1 usa NCh 3309:2014, mientras el visor sirve la 2022 y el MRT V1.04 ya actualizó a esa edición; la edición oficial por decreto sigue pendiente. Falla si la da por válida sin advertirlo.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**No por sí sola.** La planilla "Verificación de ventilación NCh 3309 V3.1" es una herramienta de cálculo de apoyo, no el instrumento que acredita la exigencia D: lo que se presenta es un **Informe de acreditación de cumplimiento de la tasa de ventilación** (Art. 4.1.10 num. 1.D, DS 15/2024). Además, la V3.1 declara evaluar con la **NCh 3309:2014**, mientras el visor MINVU sirve la **2022** y el MRT V1.04 ya actualizó ventilación a esa edición.

## Datos del caso

Asumo, por ser una consulta general: **vivienda** (interior de unidad), sin comuna ni fecha de ingreso indicadas. Fecha considerada: **2026-11-06**.

**Supuestos:** si el proyecto es educación, hotelería o salud, o está en una comuna con PDA, la respuesta cambia (ver abajo).

## Qué exige la norma

| Punto | Regla | Cita |
|---|---|---|
| Uso | Interior de vivienda → **NCh 3309**; educación → **solo NCh 3308**; hoteles y salud → **eximidos** | DS 15/2024, Art. 4.1.10 num. 1.D y 2.D |
| Acreditación | **Informe de cumplimiento de la tasa** según la NCh que corresponda | Art. 4.1.10 num. 1.D |
| Vías | **No hay** LOSCAT, ensayo de laboratorio ni CEV para D | Art. 4.1.10 inc. 3°–5° |
| Edición | Visor y MRT V1.04: **NCh 3309:2022**; edición oficial: **pendiente de decreto** | `normas-nch.md`, verificado 2026-11-05 |

## Por qué la V3.1 no basta

- **Desfase de edición:** la planilla evalúa con la NCh 3309:**2014** y criterios DITEC. No existe planilla MINVU para la edición **2022** (verificado 2026-11-05). Usarla sin más te deja acreditando contra una edición anterior a la que sirve el visor.
- **Ámbito:** la NCh 3309 aplica solo a unidades de vivienda con ocupantes permanentes. En **educación** corresponde NCh 3308 y la planilla no aplica; en **hoteles y salud** no se exige ventilación.
- **No es el documento:** una planilla completada no reemplaza el informe firmado. Puede servir como **respaldo de cálculo**, declarando expresamente la edición usada y conciliando con la 2022.

## Cómo acreditar, en la práctica

1. Confirmar uso y comuna (y si hay PDA/PPA con capítulo térmico).
2. Diseñar/verificar con la **NCh 3309:2022** (visor MINVU). Si usas la V3.1, deja constancia de que es 2014 y revisa que los criterios sigan siendo válidos frente a la 2022.
3. Emitir el **Informe de cumplimiento de la tasa**; lo elabora un profesional competente o especialista y lo **suscribe además el arquitecto** (Art. 4.1.10 inc. 4°).
4. Adjuntarlo en el **permiso** con los antecedentes térmicos (OGUC Art. 5.1.6 N° 11).
5. Si hay PDA: el plan suele exigir además **extracción mecánica en baños y cocina con control de higrostato**; revisar con `scripts/pda.py <comuna>`.

## Pendientes y advertencias

- **Edición oficial: pendiente.** El DS 15 cita las NCh sin año; no hay decreto identificado que fije la edición. La referencia práctica es la que sirve el visor (2022).
- No reproducimos cláusulas, tablas ni fórmulas de las NCh (© INN). Para tasas y procedimientos: **https://normastecnicas.minvu.cl/**.
- Si el proyecto es FSEV/VIT/CES-CVS, queda **fuera del alcance** de esta skill.

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **2026-11-05**.

*Fuentes oficiales a revisar:*
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Visor NCh: https://normastecnicas.minvu.cl/
- Registro de cambios MRT (ventilación V1.04): https://www.reglamentaciontermica.cl/registro-de-cambio

</details>

## ventilacion-03

**Pregunta:** Vivienda nueva en Temuco: ¿qué exige en ventilación además de la tasa?

**Rúbrica:** DS 8/2023 Art. 27 N°4: proyecto de ventilación del proyectista para el permiso, con NCh 3308/3309, entrada de aire natural o mecánica y extracción mecánica en baños y cocina con control de higrostato.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa
En Temuco, además de la **tasa** de ventilación, el PDA exige **extracción mecánica en baños y cocina con control de higrostato** (DS 8/2023 MMA, Art. 27 N°4). A eso se suman los demás requisitos de la NCh 3309/3308 y el informe de acreditación para el permiso.

## Datos del caso
| Dato | Valor |
|---|---|
| Uso | Vivienda nueva |
| Comuna | Temuco (zona F) |
| PDA | **Sí**: DS 8/2023 MMA, D.O. 07-03-2025, cobertura total |
| Etapa | Exigible desde 12 meses de la vigencia (≈ 07-03-2026); antes regía el Art. 33 del DS 8/2015 |
| Fecha considerada | 06-11-2026 |

**Supuestos:** el permiso de edificación ingresa después de ≈ 07-03-2026. Si ingresó antes, hay que revisar la etapa anterior del plan.

## Exigencias de ventilación
| Exigencia | Fuente |
|---|---|
| Tasa de ventilación no menor a la de la NCh, con diseño orientado a calidad de aire interior aceptable. Interior de la vivienda: **NCh 3309**; recintos que no son interior de vivienda permanente (p. ej. espacios comunes): **NCh 3308** | DS 8/2023, Art. 27 N°4; DS 15, Art. 4.1.10 num. 1.D |
| **Extracción mecánica en baños y cocina, con control de higrostato** | DS 8/2023, Art. 27 N°4 (exigencia propia del plan) |
| Componente mecánico en la ventilación general; extracción local mecánica en cocina y baños; aberturas operables; hermeticidad; control de aparatos de combustión; alarmas de CO | NCh 3309 (alcance, en palabras propias; contenido en el visor) |
| Documentación de diseño, puesta en marcha y manual de operación y mantención (si aplica NCh 3308) | NCh 3308 (alcance, en palabras propias) |

No hay vía LOSCAT, de ensayo de laboratorio ni CEV para ventilación: la vía por demanda no cubre D (DS 15, Art. 4.1.10 inc. 5°).

## Cómo acreditar
- **Informe de acreditación de cumplimiento de la tasa de ventilación** según la NCh que corresponda, más las **EETT del sistema de ventilación** (incluido el higrostato).
- Va en el **permiso de edificación** (OGUC Art. 5.1.6 N° 11).
- Lo elabora un **profesional competente o especialista** (p. ej. ingeniero mecánico) y lo suscribe además el **arquitecto** (DS 15, Art. 4.1.10 inc. 4°).
- En Temuco, la ventilación la **acredita el proyectista para el permiso** (DS 8/2023, Art. 27 N°4).

## Pendientes y advertencias
- **Edición oficial de las NCh: pendiente.** El visor sirve NCh 3308:2024 y NCh 3309:2022, pero la edición exigible aún no se fija por decreto.
- Si usan la **planilla DITEC "Verificación de ventilación NCh 3309 V3.1"**, ojo: evalúa según la **NCh 3309:2014** y no hay planilla MINVU para la edición 2022 (verificado 2026-11-05).
- La infiltración (C) se ensaya **sellando** los dispositivos de ventilación: hermeticidad y ventilación se diseñan juntas.
- El higrostato es exigencia del plan; no basta con cumplir solo la tasa de la NCh.

---

**Límites:** Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 05-11-2026.

**Fuentes oficiales a revisar:**
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Visor NCh: https://normastecnicas.minvu.cl/
- Portal PPDA del MMA: https://ppda.mma.gob.cl/

</details>

## vigencia-04

**Pregunta:** Estoy usando la OGUC de septiembre 2025 para revisar el 4.1.10, ¿está bien?

**Rúbrica:** No: ese texto (DS 21) no incluye el 4.1.10 del DS 15, que rige desde el 28-11-2025. Usar el DS 15 (D.O.) o la OGUC MINVU de marzo 2026.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

**No, no está bien.** La OGUC de septiembre 2025 (DS 21) es anterior a la entrada en vigor del nuevo Art. 4.1.10 y **no lo contiene**: sigue con el texto anterior (4.1.10 y 4.1.10 Bis). El Art. 4.1.10 del DS 15/2024 rige desde el **28-11-2025**, y hoy (06-11-2026) ya lleva casi un año vigente.

**Qué usar en su lugar**

| Fuente | Uso | Cita |
|---|---|---|
| **DS 15/2024** (D.O. 27-05-2024, CVE 2494861) | Texto normativo del nuevo 4.1.10 | DS 15 art. 1° transitorio; `ds15-2024` |
| **OGUC MINVU marzo 2026** (DS 02, D.O. 16-03-2026) | Compendio actualizado, con el 4.1.10 vigente | `oguc-2026-03` |
| OGUC septiembre 2025 | Solo como referencia histórica | No incluye el DS 15 |

**Matiz importante:** la OGUC de septiembre 2025 sí sirve si está revisando un permiso **ingresado antes del 28-11-2025**, porque la DOM evalúa con las normas vigentes a la fecha de ingreso (OGUC Art. 1.1.3). Pero para revisar "el 4.1.10 vigente" —o un proyecto que ingresará ahora— no sirve.

**Ojo con otros cambios:** ese compendio tampoco incorpora el DS 02/2026, así que aunque lo use para otras materias de la OGUC, conviene contrastarlo con la versión de marzo 2026.

**Pendientes:** la vía por demanda de energía (CEV) sigue sin umbral publicado (rige ≈ mayo 2027); no la busque en el texto de septiembre 2025.

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 05-11-2026.

*Fuentes oficiales a revisar:*
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- OGUC actualizada marzo 2026: https://www.minvu.gob.cl/wp-content/uploads/2019/05/OGUC-Marzo-2026-D.S.-N%C2%B02-D.O.-16-03-2026.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/

</details>

## zona-01

**Pregunta:** ¿En qué zona térmica queda una vivienda en Arica a 1.500 msnm y cuál es el U máximo del muro?

**Rúbrica:** Zona B (1.100 ≤ h < 3.000); U muro ≤ 0,80 (Tabla 1). Debe notar que Arica es multizona.

**Veredicto:** **Cita incorrecta del modelo:** atribuye el informe de ensayo a NCh 853; corresponde NCh 851. La exigencia y el valor están bien, y la skill cita NCh 851. Repetido 3 veces: reaparece 1.

<details><summary>Respuesta</summary>

## Respuesta directa

A 1.500 msnm, esa vivienda en Arica queda en **zona térmica B**. El muro debe cumplir **U ≤ 0,80 W/m²K** (Rt ≥ 1,25 m²K/W) — DS 15/2024, Art. 4.1.10, Tabla 1, zona B.

> Ojo con la trampa habitual: la costa de Arica (bajo 1.100 msnm) es zona **A**, pero sobre 1.100 msnm cambia a **B**.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda (residencial) |
| Comuna | Arica, Región de Arica y Parinacota |
| Altitud | 1.500 msnm |
| Zona | **B** — condición de tabla: 1.100 ≤ altitud < 3.000 msnm |
| PDA/PPA | No registrado; rige el Art. 4.1.10 |
| Fecha considerada | 06-11-2026 |

**Supuestos:** vivienda nueva o ampliación en zona no cubierta por PDA; la cota de 1.500 msnm corresponde al emplazamiento real (la zona la fija el terreno, no la comuna).

## Exigencia que aplica

| Elemento | Exigencia | Fuente |
|---|---|---|
| Muro | **U ≤ 0,80 W/m²K** (Rt ≥ 1,25 m²K/W) | DS 15/2024, Art. 4.1.10, Tabla 1, zona B |
| Vía R100 del aislante (alternativa) | R100 ≥ 125 | DS 15/2024, Tabla 2, zona B |

El U es del **complejo completo** (todas las capas y resistencias superficiales), no un espesor de aislante. No aplica exigencia de condensación reforzada por PDA en Arica, pero sí las exigencias B (condensación), C (infiltración) y D (ventilación) del 4.1.10.

## Cómo acreditarlo

- **U del muro:** Informe de Ensayo de laboratorio del registro DS 10 (≤ 10 años, NCh 853), **memoria de cálculo** (NCh 853/3117 + Res. Ex. 1802), **aislante rotulado NCh 2251 con R100 ≥ 125**, o **solución LOSCAT** vigente.
- Va en el **expediente de permiso** (OGUC 5.1.6 N° 11), firmado por el profesional competente.

## Advertencias

- Verificar la vigencia de la ficha LOSCAT a la fecha de ingreso del permiso (la mayoría de las E14 vence en diciembre de 2026).
- Si el proyecto finalmente queda justo en el límite de 1.100 msnm, confirmar la cota antes de fijar la zona.

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

*Fuentes oficiales a revisar:*
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Reglamentación térmica MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Tabla de zonas por comuna: https://www.calificacionenergetica.cl/media/TABLA-ZT_REGIONES_PROVINCIAS-Y-COMUNAS.pdf
- LOSCAT / DITEC: https://www.minvu.gob.cl/ditec/

</details>
