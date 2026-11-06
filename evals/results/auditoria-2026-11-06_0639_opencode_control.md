# Auditoría de 2026-11-06_0639_opencode_control.jsonl

**Resultado:** 8 de 8 sin errores.

Muestra: 8 de 20 aprobados (semilla 611).
Comparar cada cifra y cita con `data/` y `references/`. Veredicto: correcto, o el error y si es de la skill, del modelo o del caso.

## control-02

**Pregunta:** Vivienda nueva en Pucón: zona térmica, U de muro y clase de infiltración.

**Rúbrica:** Pucón: zona H, provincia de Cautín; Tablas 1 y 7.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

Pucón es **zona térmica H** (toda la comuna) y **no tiene PDA/PPA vigente**, así que rige el Art. 4.1.10 del DS 15/2024. Para vivienda nueva: **U muro ≤ 0,30 W/m²K** y **infiltración de la envolvente ≤ 5,00 ach a 50 Pa** (provincia de Cautín).

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Residencial — vivienda nueva (numeral 1 completo: A, B, C y D) |
| Comuna / provincia / región | Pucón / Cautín / La Araucanía |
| Zona térmica | **H** — toda la comuna, sin condición de altitud ni meridiano |
| PDA/PPA | Ninguno registrado → se aplica el Art. 4.1.10 |
| Fecha considerada | 06-11-2026 (permiso que ingresa desde el 28-11-2025 rige con el DS 15) |

**Supuestos:** el permiso de obra nueva aún no ha ingresado y se presentará con la normativa vigente. Si hubiera ingresado antes del 28-11-2025, rige el texto anterior de la OGUC (Art. 1.1.3 OGUC).

## Exigencias que aplican

| Parámetro | Exigencia | Fuente |
|---|---|---|
| **U muro** | **≤ 0,30 W/m²K** (o Rt ≥ 3,33 m²K/W) | DS 15, Art. 4.1.10 num. 1.A, Tabla 1, zona H |
| **Infiltración de la envolvente** | **≤ 5,00 ach a 50 Pa** (clase medida ≤ tabla) | DS 15, Tabla 7 (= Tabla 14), provincia Cautín |
| **Permeabilidad de puertas opacas y ventanas** | Clase **≥ 3** a 100 Pa (no confundir con la infiltración) | DS 15, Tabla 9 (= Tabla 16), zona H |

Contexto de la misma zona H (también exigible en vivienda nueva):

| Elemento | Exigencia |
|---|---|
| Techumbre | U ≤ 0,25 (Rt ≥ 4,00) |
| Piso ventilado | U ≤ 0,32 (Rt ≥ 3,13) |
| Puerta opaca | U ≤ 1,70 |
| Sobrecimiento | R100 ≥ 91 |
| Ventanas | Tabla 3 (% por orientación según U) o Upvm de Tabla 5 |
| Condensación (B) y ventilación (D) | También aplican |

## Cómo acreditar

- **U de muro:** aislante rotulado NCh 2251 con **R100 ≥ 333** en las EETT; o Informe de Ensayo de laboratorio DS 10 (≤ 10 años); o Memoria de Cálculo NCh 853/NCh 3117; o solución LOSCAT E14 vigente. El U es del complejo completo, no solo del aislante (DS 15 num. 1.A).
- **Infiltración:** Informe de Ensayo **en terreno, con la obra terminada**, según NCh 3295 (arquitecto, consultor DS 135 o laboratorio DS 10). Va en la **recepción definitiva**, no en el permiso. Muestra: lote de 11 a 50 → 2 viviendas; si el lote es de 1 a 10, la Tabla 8 no fija muestra (supuesto prudente: 1 vivienda representativa; pendiente de criterio MINVU).
- **Permeabilidad:** ensayo NCh 3296/3297 de laboratorio DS 10 o solución LOSCAT del elemento.
- **Firmas:** los informes y memorias los suscribe un profesional competente y además el arquitecto del proyecto (Art. 4.1.10 inc. 4°). En el permiso: EETT y, según vía, informe/memoria/LOSCAT (OGUC 5.1.6 N° 11).

## Advertencias

- **No aplicar la zonificación antigua de 7 zonas:** con la tabla oficial del DS 15, Pucón es **H**.
- La **alternativa de sellos** para infiltración solo procede si en la región no hay ensayadores registrados y el lote es ≤ 10 viviendas; verifíquelo antes de usarla.
- Si usa LOSCAT para ventanas, revise la vigencia de la ficha E14 (la mayoría vence en diciembre de 2026).
- Pucón no aparece en un PDA/PPA con capítulo térmico; si el terreno estuviera en un polígono especial, confírmelo con la DOM.

---

**Límites:** Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 05-11-2026.

**Fuentes oficiales a revisar:**
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Tabla de zonas por comuna: https://www.calificacionenergetica.cl/media/TABLA-ZT_REGIONES_PROVINCIAS-Y-COMUNAS.pdf
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-04

**Pregunta:** Escuela nueva en Melipilla: ¿qué U máximo de muro exige?

**Rúbrica:** Educación en zona D: Tabla 10, distinto de vivienda.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**U muro ≤ 0,60 W/m²K** (Rt mínima 1,67 m²K/W). Así lo exige la **Tabla 10** del Art. 4.1.10 para **educación en zona D**, que es la zona de Melipilla.

> Ojo: no uses el 0,80 de vivienda. En educación el muro es más estricto en zona D (Tabla 10, no Tabla 1).

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Equipamiento clase **educación** (escuela) → Art. 4.1.10, numeral 2 (A–D) |
| Comuna | Melipilla, Región Metropolitana |
| Zona térmica | **D** (fila única en la tabla oficial MINVU; sin ambigüedad por altitud) |
| PDA/PPA | No aparece plan para Melipilla en la base de la skill. En todo caso, los planes aplican **solo a viviendas**: un colegio sigue el 4.1.10 |
| Fecha considerada | **06-11-2026** (consulta) |

**Supuestos:** permiso de obra nueva ingresado después del **28-11-2025**, por lo que rige el Art. 4.1.10 del DS 15/2024 (OGUC Art. 1.1.3).

## Exigencias de envolvente (A) que aplican

| Elemento | Exigencia | Fuente |
|---|---|---|
| **Muro** | **U ≤ 0,60 W/m²K / Rt ≥ 1,67 m²K/W** | DS 15/2024, Art. 4.1.10 num. 2.A, **Tabla 10**, zona D |
| R100 del aislante en muro (vía rotulado) | **R100 ≥ 167** | DS 15/2024, **Tabla 11**, zona D |
| Techumbre | U ≤ 0,38 / Rt ≥ 2,63 | Tabla 10, zona D |
| Piso ventilado | U ≤ 0,60 / Rt ≥ 1,67 | Tabla 10, zona D |
| Puertas opacas | U ≤ 1,70 / Rt ≥ 0,59 | Tabla 10, zona D |
| Ventanas | U ≤ 3,60 W/m²K (sin % por orientación) | Tabla 12, zona D |
| Sobrecimiento | R100 ≥ 45 (por el exterior) | Tabla 13, zona D |

También aplican **B** (condensación, NCh 1973 + Res. Ex. 1802), **C** (infiltración por provincia y permeabilidad) y **D** (ventilación, solo NCh 3308 en educación). Salud sí está exenta de D; educación no.

## Cómo acreditar el muro

Una de estas vías, con el U del **complejo completo** (todas las capas y resistencias superficiales):
1. Aislante **rotulado NCh 2251** con R100 ≥ 167, especificado en las EETT (vía R100; no fija un U directamente).
2. **Informe de ensayo** de laboratorio del registro DS 10, de ≤ 10 años (NCh 851).
3. **Memoria de cálculo** según NCh 853 y NCh 3117, con condiciones de la Res. Ex. 1802.
4. **Solución LOSCAT E14 vigente** a la fecha del permiso.

El espesor del aislante no sale del U: requiere cálculo o ficha R100/LOSCAT.

## Advertencias

- Verifica la vigencia de la ficha LOSCAT: la mayoría de las E14 vence en **diciembre de 2026**.
- Si el anteproyecto se aprobó con la norma anterior, el régimen transitorio no está resuelto oficialmente; conviene confirmarlo por escrito con la DOM.
- El expediente de permiso y recepción tiene documentos y firmas distintas (cálculo U/Rt, condensación, infiltración en obra terminada, permeabilidad, ventilación).

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **05-11-2026**.

*Fuentes oficiales a revisar:*
- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-05

**Pregunta:** Clínica nueva en Castro: ¿qué U de ventana exige y debe acreditar ventilación?

**Rúbrica:** Salud en zona G: Tabla 12; eximida de ventilación.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

Para una clínica en Castro (zona **G**, uso **salud**), la ventana debe tener **U ≤ 3,00 W/m²K** (Rt ≥ 0,33). **No debe acreditar ventilación**: la clase salud está **eximida** de la exigencia D del Art. 4.1.10. Sí debe acreditar condensación e infiltración.

## Datos del caso

- **Uso:** equipamiento clase salud (clínica) → Art. 4.1.10 num. 2 (A–C; exenta de D).
- **Comuna/zona:** Castro, provincia de Chiloé, **zona G** para toda la comuna.
- **PDA/PPA:** no hay plan aplicable; además, los PDA solo rigen para vivienda.
- **Fecha considerada:** 06-11-2026. **Supuesto:** permiso ingresado después del 28-11-2025, por lo que rige el DS 15/2024.

## Exigencias que aplican

| Elemento | Exigencia | Fuente |
|---|---|---|
| **U de ventana** (vertical) | **≤ 3,00 W/m²K** (Rt ≥ 0,33) | DS 15, Art. 4.1.10 num. 2.A.5, **Tabla 12**, zona G |
| Ventana en techumbre (si existe) | U ≤ 3,6 W/m²K | DS 15, num. 2.A.5 (regla zonas B–I) |
| **Ventilación (D)** | **Eximida**: no se exige informe de tasa | DS 15, num. 2.D; lámina DITEC Edu-Salud (ene-2026) |
| Condensación (B) | **Aplica** (salud no está exenta) | DS 15, num. 2.B; Res. Ex. 1802 |
| Infiltración y permeabilidad (C) | **Aplica** (salud no está exenta); infiltración ≤ 5,00 ach₅₀ en Chiloé | DS 15, num. 2.C, Tablas 7/14 |

En salud **no hay % máximo de vidriado por orientación** ni Upvm: solo el U máximo de la Tabla 12.

## Cómo acreditar

- **U de ventana:** Informe de Ensayo NCh 3076/1-2 de laboratorio del registro DS 10 (ensayo de hasta 10 años), **o** Memoria de Cálculo NCh 3137/1-2, **o** solución LOSCAT E14 vigente.
- **Firma:** lo elabora un profesional competente o especialista y lo **suscribe además el arquitecto** del proyecto (Art. 4.1.10 inc. 4°).
- **Etapa:** en el permiso, EETT con las partidas térmicas más el informe, memoria o detalle LOSCAT (OGUC Art. 5.1.6 N° 11); en la recepción, según corresponda (OGUC Art. 5.2.6 N° 7).
- **Ventilación:** no se presenta informe de tasa de ventilación ante la DOM por el 4.1.10.

## Advertencias

- La exención de ventilación es **solo frente al Art. 4.1.10**. No libera de exigencias sectoriales de la autoridad sanitaria ni de las condiciones de habitabilidad de la OGUC; esas reglas son ajenas a esta skill.
- Si el proyecto incluye una parte de **vivienda** (por ejemplo, casa del cuidador), esa parte se rige por el régimen residencial y sí exige ventilación.
- Si usa LOSCAT, verifique que la ficha esté vigente: la mayoría de las E14 vence en **diciembre de 2026**.
- Si el permiso ingresó **antes** del 28-11-2025, rige la norma anterior (OGUC Art. 1.1.3).

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

**Fuentes oficiales a revisar:**
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Lámina DITEC Edu-Salud: https://www.minvu.gob.cl/wp-content/uploads/2026/01/Art-4-1-10-OGUC_RES-EDU-SAL_DITEC.pdf
- Reglamentación térmica MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-08

**Pregunta:** Casa nueva en Los Ángeles: ¿el plan de descontaminación dice algo sobre ventilación?

**Rúbrica:** DS 4/2017 Art. 20 N°4.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**Sí, y de forma expresa.** El PDA de Los Ángeles regula la ventilación de la vivienda nueva: exige **extracción mecánica en baños y cocina con higrostato** y remite a **NCh 3308/3309**. No es un tema que el plan deje al Art. 4.1.10.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda nueva (residencial) |
| Comuna / zona | Los Ángeles, zona **F** (toda la comuna) |
| PDA | **Sí**, DS 4/2017 MMA (D.O. 25-01-2019), cobertura total, zona saturada DS 11/2015 |
| Fecha considerada | 06-11-2026 |

**Supuestos:** obra nueva (no ampliación ni reconstrucción) y permiso ingresado después de ~25-01-2021, cuando ya rige la etapa de vivienda nueva del plan (Art. 20, 24 meses desde la vigencia).

## Exigencia que aplica

| Materia | Exigencia | Fuente |
|---|---|---|
| **Ventilación (manda el plan)** | Extracción **mecánica en baños y cocina con control de higrostato**; NCh 3308/3309; la acredita el profesional competente para el permiso de edificación | PDA Los Ángeles, DS 4/2017, **Art. 20 N°4** |
| *Art. 4.1.10 (informativo)* | Sistema de ventilación con tasa **no menor** a la de las NCh; interior de vivienda → **NCh 3309** | DS 15/2024, Art. 4.1.10 num. 1.D |

El inc. 2° del Art. 4.1.10 remite al plan en esta materia, así que **rige el Art. 20 N°4**. No hay contradicción con el 4.1.10: el plan agrega el requisito de higrostato y de extracción local mecánica.

## Cómo acreditar

- **Informe de acreditación de la tasa de ventilación** según NCh 3309 (interior de vivienda), adjunto en el permiso con los antecedentes térmicos — OGUC Art. 5.1.6 N°11.
- Lo elabora un **profesional competente o especialista**; lo suscribe además el **arquitecto** (Art. 4.1.10 inc. 4°).
- **No existe vía LOSCAT, de ensayo ni CEV** para ventilación: la vía por demanda no cubre este punto.

## Advertencias

- **Solo ventanas operables probablemente no cumple** la NCh 3309:2022: la norma pide componente mecánico en la ventilación general y extracción local mecánica en cocina y baño. Que lo confirme quien firme el informe.
- **Edición oficial de las NCh: pendiente.** El visor sirve NCh 3308:2024 y NCh 3309:2022; la planilla DITEC "V3.1" evalúa con la edición 2014 y **no hay planilla MINVU para la 2022**.
- Si la casa lleva **calefactor a leña**, el plan también trae el **Art. 24** (proyectos urbanos > 140 m² con calefacción sin leña o distrital) y la NCh 3309 pide control de aparatos de combustión y alarma de CO: conviene resolverlo junto con el diseño de ventilación.
- La **infiltración** (8 ach a 50 Pa, plan Tabla 17) se ensaya con los dispositivos de ventilación sellados, así que hermeticidad y ventilación se diseñan en conjunto.

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **2026-11-05**.

*Fuentes oficiales a revisar:*
- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- Portal PPDA del MMA: https://ppda.mma.gob.cl/
- Visor NCh (3308/3309): https://normastecnicas.minvu.cl/

</details>

## control-10

**Pregunta:** Vivienda nueva en Los Ángeles: ¿cuál es el U máximo de muro y de dónde sale?

**Rúbrica:** Plan: DS 4/2017 Art. 20; el 4.1.10 fija el mismo valor.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

**U muro ≤ 0,45 W/m²K** (o **Rt ≥ 2,22 m²K/W**). En Los Ángeles manda el **PDA Los Ángeles (DS 4/2017 MMA), Art. 20, Tabla 15b**, que fija ese valor para vivienda nueva; el **DS 15, Tabla 1, zona F** fija el mismo 0,45, así que no hay diferencia entre ambos.

**Datos del caso**
- Uso: vivienda nueva (obra nueva).
- Comuna: Los Ángeles, Región del Bío-Bío; **zona F** (toda la comuna, sin depender de altitud).
- PDA: **PDA Los Ángeles, DS 4/2017 MMA (D.O. 25-01-2019)**, cobertura **total**.
- Fecha considerada: **06-11-2026**.

**Supuestos:** permiso de edificación de vivienda nueva; no se consideran aquí las demás exigencias del plan (ventanas, sobrecimiento, infiltración). El Art. 24 del plan (calefacción sin leña en proyectos urbanos > 140 m²) puede aplicar según el proyecto, pero no altera el U de muro.

**Exigencia**

| Elemento | Valor | Fuente |
|---|---|---|
| Muro — U máximo | **0,45 W/m²K** (Rt ≥ 2,22 m²K/W) | PDA Los Ángeles, DS 4/2017 MMA, **Art. 20, Tabla 15b** (vivienda nueva, etapa a 24 meses, desde ~25-01-2021) |
| Muro — vía R100 | **R100 ≥ 222** (equivalente a 2,22 m²K/W) | PDA Los Ángeles, **Art. 20, Tabla 16** |
| Muro — referencia DS 15 | U ≤ 0,45 W/m²K | DS 15, Art. 4.1.10, **Tabla 1, zona F** |

La etapa anterior del plan (Art. 19, Tabla 11, desde ~25-01-2020) también fija **0,45**, por lo que el valor no depende de la fecha exacta de ingreso del permiso dentro de la vigencia actual.

**Cómo acreditarlo** (en el permiso de edificación, OGUC Art. 5.1.6 N° 11):
1. **Aislante rotulado NCh 2251** con R100 ≥ 222, especificado en las EETT (lo suscribe el arquitecto).
2. **Informe de Ensayo** de U del muro, de laboratorio inscrito en el registro DS 10, con antigüedad ≤ 10 años (NCh 851).
3. **Memoria de Cálculo** de U/Rt (NCh 853 y NCh 3117 según corresponda), elaborada por profesional competente o especialista y suscrita por el arquitecto del proyecto.
4. **Solución LOSCAT E14 vigente**, si se opta por esa vía; verificar su vigencia a la fecha del permiso.

**Advertencias**
- El plan regula la materia y prevalece por el Art. 4.1.10 inc. 2°; no corresponde “elegir” entre plan y DS 15, pero ambos coinciden en 0,45.
- Si se usa LOSCAT, revisar la vigencia: la mayoría de las fichas E14 vencen en diciembre de 2026.
- La comuna no tiene polígono parcial: la cobertura del plan es total.

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al **2026-11-05**.

*Fuentes oficiales a revisar:*
- DS 15 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-11

**Pregunta:** Vivienda nueva en Valdivia: ¿cuál es el U máximo de piso ventilado?

**Rúbrica:** Última etapa del plan de Valdivia: igual a la Tabla 1, zona G.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**U máximo de piso ventilado = 0,39 W/m²K** (Rt mínima 2,56 m²K/W). En Valdivia rige el PDA Valdivia (DS 25/2016), que fija ese valor para vivienda nueva en su etapa vigente. Coincide con el Art. 4.1.10 para la zona G.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Vivienda nueva |
| Comuna | Valdivia, Región de Los Ríos |
| Zona térmica | **G** (toda la comuna) |
| PDA/PPA | **PDA Valdivia, DS 25/2016 MMA** (D.O. 23-06-2017), cobertura total, exige envolvente |
| Fecha considerada | 06-11-2026 (etapa del plan vigente desde ≈23-06-2019) |

**Supuestos:** se trata de un **piso ventilado** (sin contacto directo con el terreno, incluidos voladizos cerrados); el permiso se ingresa en la fecha indicada.

## Exigencia que aplica

| Elemento | Exigencia | Fuente |
|---|---|---|
| Piso ventilado | **U ≤ 0,39 W/m²K** (o **R100 ≥ 256**) | PDA Valdivia, DS 25/2016, **Art. 28, Tabla N°16b** (U) y **Tabla N°17** (R100) |
| Piso ventilado — nota informativa | U ≤ 0,39 W/m²K (Rt 2,56) | DS 15/2024, Art. 4.1.10, **Tabla 1, zona G** |

⚠️ **No uses 0,50 W/m²K.** Ese valor corresponde a la etapa de 12 meses (Art. 27, Tabla N°12) y fue superado por la etapa de 24 meses (Art. 28, Tabla N°16b), vigente desde 2019.

## Cómo acreditar

Una de estas vías, por elemento:

- **Aislante rotulado NCh 2251** con R100 ≥ 256, especificado en las EETT.
- **Informe de Ensayo de U** de laboratorio del registro DS 10, de ≤ 10 años (NCh 851).
- **Memoria de Cálculo de U/Rt** (NCh 853 y NCh 3117), con las condiciones de la Res. Ex. 1802; la elabora un profesional competente o especialista y la suscribe el arquitecto del proyecto.
- **Solución LOSCAT E14 vigente** (la especifica el arquitecto).

En el permiso va la memoria o el informe; el ensayo de infiltración, en cambio, es de recepción.

## Advertencias

- **Piso sobre terreno (radier) no es piso ventilado:** no tiene U máximo; lo que se exige es el **sobrecimiento R100 ≥ 91** (Ord. N°209/2018 y Res. Ex. 1729/2019 para Valdivia).
- **LOSCAT:** la mayoría de las fichas E14 vence en **diciembre de 2026**; si usas esa vía, verifica la vigencia a la fecha de ingreso.
- En vivienda con PDA, el plan también regula **ventanas (% por orientación), sobrecimiento, infiltración y ventilación**; no las reemplaces por las tablas del 4.1.10.

## Límites y fuentes

*Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.*

- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-12

**Pregunta:** Colegio nuevo en Curicó, en el valle: ¿le aplican las tablas del PDA? ¿Qué U de muro exige?

**Rúbrica:** El inc. 2° alcanza solo a viviendas: Tabla 10.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

## Respuesta directa

**No.** Las tablas del PDA no rigen para un colegio: el Art. 4.1.10 inc. 2° remite al plan **solo para viviendas**; educación sigue el Art. 4.1.10 completo (numeral 2). En Curicó, terreno de valle (bajo 1.000 msnm = **zona D**), el muro exige **U ≤ 0,60 W/m²K (Rt ≥ 1,67 m²K/W)** — DS 15, Art. 4.1.10 num. 2.A, **Tabla 10**.

## Datos del caso

| Dato | Valor |
|---|---|
| Uso | Educación (colegio) → numeral 2, exigencias A–D completas |
| Comuna | Curicó, provincia de Curicó, Región del Maule |
| Zona | **D** si el terreno está **bajo 1.000 msnm**; **H** si está a 1.000 msnm o más (**comuna multizona**) |
| PDA | PDA Valle Central de la Provincia de Curicó (DS 44/2017, D.O. 20-12-2019), cobertura **parcial** — **no aplica a este uso** |
| Fecha considerada | 06-11-2026; el Art. 4.1.10 del DS 15 rige desde el **28-11-2025** |

**Supuestos:** el permiso ingresa después del 28-11-2025 (si ingresó antes, rige el texto anterior, OGUC Art. 1.1.3); "en el valle" = terreno bajo 1.000 msnm. La zona la fija la cota real del emplazamiento, no el nombre de la comuna.

## Exigencias que aplican (zona D)

| Elemento | Exigencia | Cita |
|---|---|---|
| **Muro** | **U ≤ 0,60 W/m²K** (Rt ≥ 1,67) | DS 15, Tabla 10, zona D |
| Techumbre | U ≤ 0,38 (Rt ≥ 2,63) | DS 15, Tabla 10 |
| Piso ventilado | U ≤ 0,60 (Rt ≥ 1,67) | DS 15, Tabla 10 |
| Puerta opaca | U ≤ 1,70 | DS 15, Tabla 10 |
| R100 del aislante de muro | ≥ 167 | DS 15, Tabla 11 |
| Sobrecimiento | R100 ≥ 45 | DS 15, Tabla 13 |
| Ventanas | U ≤ 3,60 (sin % por orientación) | DS 15, Tabla 12 |
| Permeabilidad puertas/ventanas | clase **≥ 2** a 100 Pa | DS 15, Tabla 16 |
| Infiltración de la envolvente | ≤ **8,00 ach a 50 Pa** (provincia de Curicó) | DS 15, Tabla 14 |
| Condensación (B) | sin riesgo superficial ni intersticial | DS 15 num. 2.B; Res. Ex. 1802 |
| Ventilación (D) | tasa según **NCh 3308** | DS 15 num. 2.D |

> Nota: si el terreno resultara en zona **H**, el muro baja a **U ≤ 0,30** (Rt ≥ 3,33) y el R100 de muro sube a 333. El valor 0,80 de muro del PDA de Curicó es para **vivienda** y no se usa aquí.

## Cómo acreditar

| Elemento | Documento | Quién / etapa |
|---|---|---|
| U de muro, techumbre, piso, puertas | R100 rotulado NCh 2251 (≥167 en muro), informe de ensayo DS 10 (≤10 años, NCh 851) o memoria de cálculo NCh 853/3117; también ficha LOSCAT E14 vigente | Profesional competente; lo suscribe el arquitecto. Permiso |
| Ventanas (U ≤ 3,60) | Ensayo NCh 3076/1-2, cálculo NCh 3137/1-2 o LOSCAT | Permiso |
| Sobrecimiento (R100 45) | Aislante rotulado o LOSCAT | Permiso |
| Condensación | Memoria de cálculo NCh 1973 con condiciones de la Res. Ex. 1802 (incluye sección A y puente térmico B) | Profesional competente; suscribe el arquitecto. Permiso |
| Infiltración (8,00 ach) | Ensayo en terreno NCh 3295; muestra Tabla 15 según recintos docentes (5–16 → 2; 17–24 → 3; 25–32 → 4; >32 → 10 %) | **Obra terminada, recepción** |
| Permeabilidad (clase ≥2) | Ensayo NCh 3296/3297 o LOSCAT | Permiso |
| Ventilación | Informe de cumplimiento de tasa NCh 3308 | Permiso |

## Pendientes y advertencias

- **Comuna multizona:** confirmar la cota del terreno; bajo 1.000 msnm es D, desde 1.000 msnm es H.
- **Alternativa de sellos (C):** en educación no tiene tope de lote, pero solo procede si en la Región del Maule no hay ensayadores registrados para NCh 3295 y mientras MINVU no la elimine por resolución; verificar antes de usarla.
- **LOSCAT E14:** la mayoría de las fichas vence en **diciembre de 2026**; revisar vigencia a la fecha del permiso.
- **Edición oficial de las NCh** (1079, 3308): pendiente de decreto; no condiciona esta respuesta.

---

*Límites:* Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

*Fuentes oficiales a revisar:*
- DS 15/2024 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- LOSCAT y listados DITEC: https://www.minvu.gob.cl/ditec/
- Visor NCh: https://normastecnicas.minvu.cl/

</details>

## control-18

**Pregunta:** Transcríbeme el procedimiento de ensayo de la NCh 3295 y sus tablas.

**Rúbrica:** Se niega a reproducir la NCh y remite al visor.

**Veredicto:** Correcto.

<details><summary>Respuesta</summary>

No puedo transcribirte el procedimiento ni las tablas de la NCh 3295: el texto de las normas NCh está protegido por derechos de autor (© INN) y esta skill tiene prohibido reproducir cláusulas, tablas, figuras o fórmulas, incluso a pedido. El contenido completo y oficial está en el visor gratuito de MINVU: **https://normastecnicas.minvu.cl/**

Lo que sí puedo darte es su ficha y el rol que cumple en el Art. 4.1.10:

| Dato | Contenido |
|---|---|
| Código y título | NCh 3295 — *Aislación térmica - Determinación de la permeabilidad del aire en edificios - Método de presurización por medio del ventilador* |
| Edición en el visor | 2013 |
| Edición oficial exigible | **Pendiente de decreto** (el DS 15 la cita sin año; no hay decreto identificado que fije la versión oficial) |
| Uso en el DS 15/2024 | Num. 1.C y 2.C: infiltración de aire de la envolvente; el resultado se clasifica por clase según provincia (junto con NCh 3296 y 3297) |
| Vía de acreditación | **Ensayo en terreno**, sobre obra terminada, con la muestra de las Tablas 8/15 del DS 15 |
| Quién lo suscribe | Arquitecto del proyecto, profesional competente o especialista inscrito en el registro DS 135, o laboratorio DS 10 |
| En PDA/PPA | Si el plan tiene tabla propia de muestras, manda la del plan (p. ej. Temuco admite además la alternativa de sellos en EETT) |

Si lo que necesitas es aplicar el requisito a un proyecto concreto —clase exigida, tamaño de muestra, quién firma y en qué etapa—, puedo orientarte con las tablas del DS 15 y de la Res. Ex. 1802, sin reproducir la norma.

**Límites:** Orientación técnica; puede contener errores. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza la revisión del profesional competente ni el pronunciamiento de la DOM. Verificado contra fuentes al 2026-11-05.

**Fuentes oficiales:**
- Visor NCh: https://normastecnicas.minvu.cl/
- DS 15 en el D.O.: https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/

</details>
