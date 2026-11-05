# Roles, firmas y expediente térmico

Verificado: **2026-11-05**. Fuentes: `ds15-2024` (Art. 4.1.10 inc. 4° y 5°, y las alternativas de cumplimiento de
cada literal), `oguc-2026-03` (Arts. 1.1.2, 5.1.6 N° 11 y 5.2.6 N° 7), `res-ex-1802-2025`. La skill **orienta**: no
firma, no reemplaza al arquitecto, al profesional competente o especialista, al laboratorio DS 10, al consultor DS 135
ni al evaluador energético.

## 1. Quién es quién (definiciones OGUC Art. 1.1.2)

- **Profesional competente:** arquitecto, ingeniero civil, ingeniero constructor o constructor civil, cada uno dentro
  de su ámbito de competencia.
- **Profesional especialista:** un profesional competente, u otros profesionales (por ejemplo, ingeniero mecánico)
  cuya especialidad tenga relación directa con el estudio que suscriben.
- **Laboratorio DS 10:** inscrito en el Registro Oficial de Laboratorios de Control Técnico de Calidad de la
  Construcción (DS 10 V. y U. de 2002).
- **Consultor DS 135:** inscrito en el Registro de Consultores MINVU (DS 135 de 1978).
- **Evaluador Energético:** inscrito en el Registro Nacional de Evaluadores Energéticos. Solo para la vía por demanda
  (pendiente) y para la CEV, que es otro régimen.

## 2. Quién elabora y quién firma cada documento

| Documento | Exigencia | Elabora | Firma además | Fuente |
|---|---|---|---|---|
| EETT con aislante rotulado NCh 2251 (R100) | A opacos y sobrecimiento | Arquitecto, en las EETT | — | num. 1.A/2.A vía 1; A.6 |
| Informe de Ensayo de U (NCh 851, 3076/1-2) | A | **Laboratorio DS 10** (≤10 años) | — | num. 1.A vía 2, 1.A.5 |
| Memoria de Cálculo de U/Rt (NCh 853, 3117, 3137) | A | Profesional competente o especialista | **Arquitecto del proyecto** | inc. 4°; num. 1.A vía 3 |
| Detalle de solución LOSCAT vigente | A, C (permeabilidad) | Arquitecto (la especifica) | — | num. 1.A vía 4; 1.C |
| Informe de % de ventanas por orientación o de Upvm | A ventanas (residencial) | Profesional competente o especialista | Arquitecto | num. 1.A.5; inc. 4° |
| **Memoria de Cálculo de condensación** (NCh 1973 + Res. Ex. 1802) | B | Profesional competente o especialista | Arquitecto | num. 1.B/2.B; inc. 4° |
| **Informe de Ensayo de infiltración en terreno** (NCh 3295) | C envolvente | **Arquitecto del proyecto**, o profesional competente o especialista **inscrito en el registro DS 135**, o **laboratorio DS 10** | (inc. 4°: el arquitecto suscribe informes de terceros) | num. 1.C/2.C |
| Informe de Ensayo de permeabilidad (NCh 3296/3297) | C puertas y ventanas | **Laboratorio DS 10** | — | num. 1.C/2.C |
| Partida de sellos en EETT (alternativa condicionada) | C envolvente | Arquitecto, en las EETT | — | num. 1.C/2.C |
| **Informe de cumplimiento de la tasa de ventilación** (NCh 3308/3309) | D | Profesional competente o especialista (p. ej. ingeniero mecánico) | Arquitecto | num. 1.D/2.D; inc. 4° |
| Informe de Precalificación Energética (vía por demanda, **pendiente**) | Solo A, solo viviendas | **Evaluador Energético** | — | inc. 5° |

> [!NOTE]
> El inciso 4° dice que los informes o la memoria "podrán ser elaborados por un profesional competente o un
> profesional especialista" **"en los casos que así se establezca"**, y que los suscribe además el arquitecto. La
> skill lo aplica a memorias e informes de A, B y D. El DS no exige otra firma especial (por ejemplo, un registro) para
> la memoria de condensación ni para el informe de ventilación.

## 3. Expediente: qué va en cada etapa

**Permiso de edificación (OGUC Art. 5.1.6 N° 11):**
- EETT con las partidas térmicas: aislantes, ventanas, sellos si corresponde, sistema de ventilación.
- Según corresponda: Informes de acreditación (% de ventanas/Upvm, ventilación), Informes de Ensayo (U, permeabilidad),
  Memorias de Cálculo (U/Rt y **condensación**), y el detalle de las soluciones LOSCAT.
- Viviendas, alternativa para A: Informe de Precalificación Energética, cuando rija el umbral.
- **Zona PDA:** acreditar el estándar del plan (`pda-ppa.md`). Algunos planes exigen además informar al solicitar el
  permiso la alternativa adoptada o el sistema de calefacción.

**Recepción definitiva (OGUC Art. 5.2.6 N° 7):**
- Según el destino: Informe de Precalificación Energética, Informes de Ensayo, Memorias de Cálculo, o descripción del
  material o soluciones adoptadas y en qué parte de la obra.
- **Informe de Ensayo de infiltración en terreno (NCh 3295)**, con la muestra de las Tablas 8/15 y la obra terminada.
  Es la pieza que **solo existe al final de la obra**.
- La CEV (DS 5/2024), cuando sea obligatoria para la vivienda, es un requisito **aparte** de la recepción. No
  reemplaza nada del 4.1.10 (`trampas.md`).

## 4. Checklist mínimo por uso

| Documento | Residencial | Hotel | Educación | Salud |
|---|---|---|---|---|
| A (U/Rt opacos, puertas, sobrecimiento) | ✔ | ✔ (Tablas 1, 2, 6) | ✔ (10, 11, 13) | ✔ (10, 11, 13) |
| A ventanas | ✔ % u Upvm (Tablas 3–5) | ✔ U (Tabla 12) | ✔ U (Tabla 12) | ✔ U (Tabla 12) |
| B condensación | ✔ | — exento | ✔ | ✔ |
| C infiltración en terreno + permeabilidad | ✔ | — exento | ✔ | ✔ |
| D ventilación | ✔ (NCh 3308/3309) | — eximido | ✔ (NCh 3308) | — eximida |

`scripts/checklist.py` genera esta lista para un proyecto concreto.

## Límites (decirlo siempre)

La skill no valida firmas, inscripciones ni la vigencia de registros. Verificar en los registros oficiales de MINVU
(laboratorios DS 10, consultores DS 135) y del Registro Nacional de Evaluadores Energéticos. La DOM decide la
admisibilidad del expediente.

## Fuentes oficiales a revisar

- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- OGUC actualizada (MINVU, marzo 2026): https://www.minvu.gob.cl/wp-content/uploads/2019/05/OGUC-Marzo-2026-D.S.-N%C2%B02-D.O.-16-03-2026.pdf
- Registros técnicos MINVU: https://www.minvu.gob.cl/
