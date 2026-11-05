# Planes de Descontaminación/Prevención (PDA/PPA) y vivienda

Verificado: **2026-11-05**. Fuentes: los 13 decretos MMA verificados con sha256 (`pda-temuco-ds8-2025`,
`pda-ohiggins-ds1-2021`, `ppa-quillota-ds18-2023`, `pda-talca-ds49-2016`, `pda-chillan-ds48`, `pda-curico-ds44-2017`,
`ppa-concepcion-ds6-2018`, `pda-los-angeles-ds4-2017`, `pda-valdivia-ds25-2016`, `pda-osorno-ds47-2015`,
`pda-coyhaique-ds7-2018`, `ppa-cqp-ds105-2018`, `ppda-rm-ds31-2016`) y `ds15-2024` (Art. 4.1.10 inc. 2°).

## 1. Regla de prevalencia

En **permisos de obra nueva, ampliación o reconstrucción de viviendas** en un área con plan vigente (Ley 19.300),
las exigencias térmicas son **las del plan** (Art. 4.1.10 inc. 2°). Lo que el plan no regule se acredita por el
4.1.10.

> [!WARNING] Criterio declarado
> Esto último (que el 4.1.10 cubre lo que el plan no regula) no está escrito en el DS 15. Es la lectura conservadora
> de la skill. Ejemplo: si un plan no fija la U de ventana, se usa la del 4.1.10.

Educación, salud y hoteles siguen el 4.1.10 aunque estén en zona PDA.

## 2. Datos

- **`data/pda_planes.csv`:** comuna → plan, con cobertura `total` o `parcial` y si el plan exige envolvente. En las
  comunas **parciales** (O'Higgins, Curicó, Coyhaique) hay que confirmar si el terreno está dentro del polígono de
  zona saturada que cita el decreto.
- **`data/pda.csv`:** **643 valores**, **todos** los de cada tabla térmica de vivienda de los 11 planes con capítulo
  térmico: U, R100, % de ventanas, Upvm, infiltración, estanqueidad o permeabilidad, muestras y orientaciones. Cada
  fila trae plan, decreto, **artículo**, **tabla**, a qué aplica (vivienda nueva o existente), etapa, elemento,
  parámetro, condición, valor, unidad y nota.
  - Transcrito de los PDF oficiales (D.O. o LeyChile).
  - Verificado con OCR independiente tabla por tabla. Las diferencias se resolvieron mirando la imagen.
  - Además, revisión humana de muestras: Curicó Tabla 15 completa, y los valores de control de Temuco, O'Higgins y
    Talca, confirmados el 2026-11-05.

## 3. Resumen: vivienda nueva, última etapa vigente

| Plan (decreto) | Comunas | Art. / tabla U | U techo · muro · piso vent. · ventana · puerta | Infiltración (ach 50 Pa) | Notas |
|---|---|---|---|---|---|
| Temuco y Padre Las Casas (DS 8/2023, D.O. 07-03-2025) | Temuco, Padre Las Casas | Art. 27, Tabla N°10 | 0,28 · 0,45 · 0,50 · **3,20** · 1,70 | 5 | Rige 12 meses después de la vigencia; antes, Art. 33 del DS 8/2015. Piso sobre terreno y sobrecimiento: R100 91 (Tabla N°11). Ventanas, además, Res. MINVU 9.868/2018. **Art. 15: calefacción sin leña en vivienda nueva, acreditada en el permiso** |
| Valle Central de O'Higgins (DS 1/2021, D.O. 29-03-2023) | 9 totales + 8 **parciales** (ver CSV) | Art. 15, Tabla 12 | 0,38 · 0,80 · 0,60 · — · 1,70 | 5 | Ventanas por % y orientación (Tabla 14) o Upvm. "Vivienda nueva" = permiso ingresado >12 meses desde la vigencia (desde ≈29-03-2024). Art. 18: sin calefacción a leña en vivienda nueva urbana |
| Quillota, Catemu, Panquehue y Llaillay (DS 18/2023, D.O. 23-10-2025) | Quillota, La Cruz, La Calera, Nogales, Hijuelas, Catemu, Panquehue, Llaillay | Art. 56, Tabla 29 | 0,38 · 0,80 · 0,60 · **4,00** · 1,70 | **8** | "Vivienda nueva" desde ≈23-10-2026. % de ventanas (Tabla 31) o Upvm |
| Talca y Maule (DS 49/2015) | Talca, Maule | Art. 31, Tabla Nº18 | 0,38 · 0,80 · 0,60 · **"por definir MINVU"** · 1,70 | 5 | Etapas: existentes 2016, nueva 28-03-2017, ambas 01-01-2018. Control solar y sobrecimiento quedan para MINVU |
| Chillán y Chillán Viejo (DS 48) | Chillán, Chillán Viejo | Art. 25, Tabla N°16 | 0,28 · 0,45 · 0,50 · 3,60 · 1,70 | 8 | Desde 01-01-2018. La "expansión 2025" que menciona una matriz interna previa: **pendiente** (instrumento no identificado) |
| Valle Central de Curicó (DS 44/2017, D.O. 20-12-2019) | Curicó, Teno, Rauco, Romeral, Sagrada Familia, Molina (**parcial**) | Art. 18, Tabla 11 | 0,38 · 0,80 · 0,60 · — · 1,70 | 8 | Ventanas por % (Tabla 15). Techumbre U ≤ 3,6. Sobrecimiento R100 45 |
| Concepción Metropolitano (DS 6/2018, D.O. 17-12-2019) | Lota, Coronel, San Pedro de la Paz, Hualqui, Chiguayante, Concepción, Penco, Tomé, Hualpén, Talcahuano | Art. 25, Tabla Nº11 | 0,33 · 0,60 · 0,60 · — · 1,70 | 5 | % ventanas (Tabla Nº15, Sur con U ≤ 5,8 = 0 %). Sobrecimiento R100 45. Art. 14: sin leña en edificios de departamentos |
| Los Ángeles (DS 4/2017, D.O. 25-01-2019) | Los Ángeles | Art. 20, Tabla 15b | 0,28 · 0,45 · 0,50 · — · 1,70 | 8 | % ventanas (Tabla 19). Sobrecimiento R100 91. **Art. 24: proyectos urbanos >140 m² con calefacción sin leña o distrital** |
| Valdivia (DS 25/2016) | Valdivia | Art. 28, Tabla N°16b | 0,28 · 0,40 · **0,39** · **"por definir MINVU"** · 1,70 | 5 | % de ventanas y sobrecimiento: los define MINVU |
| Osorno (DS 47/2015) | Osorno | Art. 8, Tabla N°24a | 0,28 · 0,40 · **0,39** · **"por definir MINVU"** · 1,70 | 5 | Desde 01-01-2019. Art. 20 c): sin leña en departamentos y condominios sociales nuevos |
| Coyhaique (DS 7/2018, D.O. 17-07-2019) | Coyhaique (**polígono**) | Art. 20, Tabla 10 | **0,25 · 0,35 · 0,32** · — · 1,70 | **4** | % ventanas (Tabla 12). Sobrecimiento R100 91. Techumbre U ≤ 3,6 |

"—" = la tabla U del plan no fija ventana; las ventanas se regulan por % y orientación, o no se regulan. En "por
definir MINVU" (Talca, Valdivia, Osorno) la celda del decreto no está pendiente: **MINVU la resolvió sin fijar un U
máximo; la exigencia opera como % de ventana según el U**, en los actos de §3b. Los R100, la estanqueidad o permeabilidad, las tablas de % y
las etapas anteriores están completas en `data/pda.csv`.

## 3b. Actos MINVU que completan los planes (`data/pda_minvu_actos.csv`, 356 valores)

Los decretos dejaron ítems "por definir MINVU". MINVU los fijó con estos actos (verificados con sha256, transcritos
de imagen y con OCR; registro en `docs/pda-verificacion/minvu-actos-pda.md`):

| Acto | Fecha | Para qué planes | Qué fija |
|---|---|---|---|
| **Ord. N°1773** DITEC (`minvu-ord1773-2017`) | 16-11-2017 | Osorno | Criterios de condensación (julio, interior 19 °C, HR 65/75/85 %), % de ventanas, sobrecimiento R100 91 (hasta ≥30 cm bajo terreno) e infiltración por EETT |
| **Ord. N°209** Ministro (`minvu-ord209-2018`) | 20-04-2018 | Talca-Maule, Temuco-PLC, Coyhaique, Osorno/Valdivia, Chillán | **Tabla 1:** sobrecimiento R100 (Talca-Maule 45; los demás 91). **Tabla 2:** % máx. de ventanas por orientación y U, por plan. Ventana en techumbre U ≤ 3,6 |
| **Res. Ex. N°9869** (`minvu-res-ex-9869-2018`) | 29-11-2018 | Osorno | Formaliza control solar y sobrecimiento, **exigibles desde 01-01-2019**. Condensación con HR 65/75/80 % |
| **Ord. N°840** SEREMI Los Lagos (`minvu-ord840-2019`) | 30-04-2019 | Osorno | Contenido mínimo de las EETT de puertas y ventanas (Art. 8 b) |
| **Res. Ex. N°9868** (`res-9868-2018`) | 29-11-2018 (D.O. 10-12-2018) | **Temuco-Padre Las Casas** | % máx. de ventanas (Tabla 1, igual al Ord. 209), sobrecimiento R100 91, ventana en techumbre U ≤ 3,6, condensación (julio, 19 °C, HR 65/75/80 %). Exigible desde 01-01-2019. **El DS 8/2023 remite a ella** ("o la que la reemplace") |
| **Res. Ex. N°1729** (`res-1729-2019-valdivia`), mod. Res. Ex. 1197 (D.O. 21-07-2021) | 30-07-2019 (D.O. 05-08-2019) | **Valdivia** | % máx. de ventanas (Tabla 1 vigente con 12 columnas: agrega U ≤ 0,6 y ≤ 0,8), sobrecimiento R100 91, techumbre U ≤ 3,6, condensación (julio, 19 °C, HR 65/75/80 %) |

Qué resuelven:
- **Talca (Art. 31):** control solar y sobrecimiento 45, por el Ord. 209.
- **Temuco (DS 8/2023 Art. 27):** % de ventanas y sobrecimiento por la Res. Ex. 9868/2018.
- **Valdivia (Art. 28):** control solar y sobrecimiento 91 por la **Res. Ex. 1729/2019** (Tabla 1 según Res. Ex. 1197/2021).
- **Osorno (Art. 8):** resuelto por la Res. Ex. 9869 + Ord. 840.
- **Chillán:** % de ventanas y sobrecimiento por el Ord. 209.

**U de ventana "por definir MINVU"** (Talca, Valdivia, Osorno): ningún acto fija un U máximo. La exigencia de
ventanas opera como **% de superficie según el U** de la ventana (Tabla 2 del Ord. 209 / Res. Ex. 9869).

Temuco: el DS 8/2023 remite a la **Res. Ex. N°9868/2018** (verificada). Sus valores coinciden con el Ord. 209 y están
en `data/pda_minvu_actos.csv`. Valdivia: el Art. 28 pedía una resolución publicada en el D.O.: es la **Res. Ex. 1729/2019**, cuya Tabla 1 vigente es la
de la Res. Ex. 1197/2021 (verificadas). Usarla en lugar del Ord. 209.

## 3c. Lo que más se omite (usar `scripts/pda.py <comuna>`, que trae TODAS las filas del plan)

> [!WARNING]
> Nunca filtrar `data/pda.csv` por texto (p.ej. "Temuco"): varias filas solo llevan el `plan_id`. Usar
> `python scripts/pda.py <comuna o plan_id>`, que filtra por `plan_id` y junta decreto + actos MINVU.

- **Muestra del ensayo de infiltración (NCh 3295):** en PDA con tabla propia manda la del plan, no la Tabla 8 del DS 15.
  **Temuco (DS 8/2023, Art. 27, Tabla Nº 14): lote < 11 → 1 vivienda**; 11–50 → 2; 51–500 → 3; > 501 → 5; 1 no conforme
  rechaza y se repite con el doble. O'Higgins (Tablas 11 y 20) y Quillota (Tablas 28 y 37) también tienen tabla propia.
  Por eso en esos planes **no existe** el "hueco" de lotes de 1 a 10 del DS 15.
- **Condensación en Temuco:** el Art. 27 N°2 exige verificar la no ocurrencia de condensación superficial e
  intersticial **a menos de 76 % de HR interior**, con NCh 1973 y los criterios de cálculo MINVU; la acredita el
  proyectista para el permiso. La Res. Ex. 9868/2018 (dictada bajo el plan anterior) fija julio, 19 °C y HR 65/75/80 %.
  **Criterio declarado:** calcular con los escenarios de la Res. 9868 y exigir cumplimiento al menos hasta 75 % (bajo el
  76 % del decreto); informar el resultado a 80 % como referencia.
- **Alternativa de sellos en Temuco:** el plan admite acreditar la clase de infiltración con ensayo NCh 3295 **o** con
  especificación de sellos en EETT, **hasta que MINVU la deje sin efecto por resolución**. El plan **no** pone las
  condiciones del DS 15 (región sin ensayadores, lote ≤ 10): no importarlas.
- **LOSCAT bajo PDA:** los planes admiten el **Listado Oficial MINVU** como alternativa (Temuco: Art. 27 N°1 d) para U;
  Tabla N°13 para permeabilidad). La ficha debe cumplir el **valor del plan** (no solo la zona del DS 15) y estar vigente.
- **Ventanas en Temuco:** U ≤ 3,20 (Tabla N°10) **y además** % máx. por orientación (Res. Ex. 9868 Tabla 1). Mejor U
  permite más superficie (p.ej. Norte: U ≤ 3,6 → 65 %; U ≤ 1,2 → 83 %); no hay otra "compensación".
- **Infiltración en Temuco:** clase 5 ach la fija el **plan** (Tabla N°12), no la provincia.

## 4. Planes sin exigencia de envolvente a vivienda nueva

| Plan | Qué regula para vivienda | Fuente |
|---|---|---|
| Concón, Quintero y Puchuncaví (DS 105/2018) | Nada de envolvente. Art. 41: recambio voluntario de calefactores. Art. 42 b): la calefacción de proyectos inmobiliarios que entran al SEIA se cuenta como emisión a compensar | Texto completo revisado |
| Región Metropolitana (DS 31/2016) | Nada de envolvente para vivienda nueva. Arts. 74–77: prohibiciones de leña (zonas A y B). Art. 89: subsidios de acondicionamiento en zona B | Texto completo revisado |
| Tocopilla, Calama (anulado), Huasco, Andacollo | Planes de foco industrial sin envolvente | Matriz interna previa 2026-09-22; **no reverificado** aquí (`pda-industriales-sin-envolvente`) |

En estas comunas rige el **Art. 4.1.10** completo.

## 5. Pendientes (a la fecha de verificación)

- **Macrozona Valle Central del Maule:** solo hay anteproyecto (Res. Ex. 8086, `pda-maule-anteproyecto-8086`); **no
  es exigible**.
- **Puerto Aysén:** el DS 3/2025 está en trámite (`pda-puerto-aysen-ds3-2025`).
- Diferencia Talca (Ord. 209) vs. Curicó (DS 44) en la columna U ≤ 5,8 (C29).
- **Chillán:** el instrumento de la "expansión 2025".

## 6. Quién firma en los planes

- U por cálculo: un **"profesional competente"** en todos los planes.
- Ensayos: un laboratorio del registro MINVU.
- Vivienda nueva: la alternativa adoptada la informa, según el plan, el **arquitecto** (Talca, Chillán, Osorno) o el
  **profesional competente** (Quillota, Curicó, Concepción).
- Condensación y ventilación: las acredita el proyectista.
- Existentes con subsidio: informa el profesional del **PSAT** al ingresar al SERVIU.

Citar siempre el artículo del plan respectivo (C09 abierta).

## 7. Trampas

- Usar valores del informe-resumen o de la matriz (C12). Usar solo `data/pda.csv`.
- Atribuir a Quillota las comunas Limache, Olmué o Villa Alemana: **el DS 18/2023 no las incluye** (C26).
- Suponer que toda la comuna está en la zona saturada cuando la cobertura es parcial (O'Higgins, Curicó, Coyhaique).
- Aplicar el plan a educación o salud: el inciso 2° es solo para viviendas.

## Fuentes oficiales a revisar

- Portal PPDA del MMA: https://ppda.mma.gob.cl/
- LeyChile (texto de cada decreto): https://www.bcn.cl/leychile/
