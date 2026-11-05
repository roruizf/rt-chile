# Alcance y vigencia del Art. 4.1.10 OGUC (DS 15/2024)

Verificado: **2026-11-05**. Fuentes (IDs de `sources/manifest.yaml`): `ds15-2024` (D.O. 27-05-2024, CVE 2494861),
`oguc-2026-03` (texto MINVU actualizado a DS 02, D.O. 16-03-2026), `minvu-comunicado-rt`, `ditec-lamina-rt`,
`ditec-lamina-edu-salud-2026-01`. Paráfrasis propia de actos públicos.

## 1. Qué edificaciones alcanza

| Uso | ¿Alcanzado? | Cómo | Fuente |
|---|---|---|---|
| **Residencial**: vivienda, hogares de acogida y hospedaje sin servicios comerciales adjuntos | Sí | Numeral 1 completo: A (U/Rt, ventanas, sobrecimientos), B (condensación), C (infiltración y permeabilidad), D (ventilación) | Art. 4.1.10 inc. 1° y num. 1; definición del uso en OGUC Art. 2.1.25 |
| **Hoteles** (uso residencial destinado a hoteles) | Sí, con régimen propio | Envolvente opaca por Tabla 1 (num. 1.A). Ventanas por Tabla 12 (num. 2.A.5). **Exentos de B, C y D** | Art. 4.1.10 num. 1.A.5, 1.B, 1.C y 1.D; num. 2 (encabezado y A.5). Ver `docs/contradicciones.md` C11 |
| **Equipamiento clase educación**: educación superior, técnica, media, básica, especial, prebásica y centros de capacitación, orientación o rehabilitación conductual | Sí | Numeral 2 completo (A–D). Ventilación (2.D) solo por NCh 3308 | Art. 4.1.10 inc. 1° y num. 2; clases en OGUC Art. 2.1.33 |
| **Equipamiento clase salud**: hospitales, clínicas, policlínicos, consultorios, postas, centros de rehabilitación | Sí | Numeral 2 A–C. **Eximida de ventilación (D)** | Art. 4.1.10 num. 2 (2.D: "las edificaciones de la clase salud estarán eximidas"); OGUC Art. 2.1.33 |
| Cementerios y crematorios (aunque la OGUC los clasifique como salud) | **No** | Excluidos de forma expresa | Art. 4.1.10 inc. 1° |
| Resto del equipamiento (comercio, oficinas/servicios, culto, deporte, esparcimiento, seguridad, etc.), actividades productivas, infraestructura | **No** | El Art. 4.1.10 no los menciona | Art. 4.1.10 inc. 1° (enumeración cerrada) |

> [!WARNING] Casos sin regla explícita: respuesta con supuestos declarados
> - **Hospedajes que no son "hoteles"** (hostal, motel, apart-hotel, cabañas turísticas). Son uso residencial por
>   la OGUC Art. 2.1.25. El trato especial del DS 15 solo nombra a los **hoteles**. Supuesto por defecto: si el
>   permiso no los califica como hotel, se les aplica el numeral 1 completo. Que la DOM lo confirme.
> - **Edificios mixtos** (por ejemplo, vivienda con locales comerciales): el Art. 4.1.10 aplica a la envolvente de
>   las partes con uso alcanzado. Supuesto: se exige por destino del recinto. **Pendiente** de criterio oficial
>   (circular DDU).
> - **Ampliaciones, alteraciones y regularizaciones**: el inciso 1° habla de "edificaciones" sin distinguir tipo de
>   permiso. Solo la regla PDA (inc. 2°) nombra obra nueva, ampliación y reconstrucción. Cómo se trata la parte
>   ampliada o alterada queda **pendiente** de criterio oficial. Supuesto: la parte nueva de la envolvente cumple
>   el 4.1.10.

## 2. Qué se exige (mapa)

- **A.** Transmitancia/resistencia térmica de techumbre, muros, piso ventilado y puertas opacas; superficie y
  transmitancia de ventanas; R100 de sobrecimientos.
- **B.** Que no haya riesgo de condensación superficial ni intersticial (NCh 1973 + condiciones de la Res. Ex. 1802).
- **C.** Clase de infiltración de la envolvente y clase de permeabilidad al aire de puertas y ventanas.
- **D.** Tasa de ventilación (NCh 3308/3309). Solo residencial (sin hoteles) y educación. **Salud y hoteles, eximidos.**

El detalle está en `exigencias-A…D-*.md` y la ficha de las NCh en `normas-nch.md`.

## 3. Relación con los PDA/PPA

En **permisos de obra nueva, ampliación o reconstrucción de viviendas** emplazadas en un área con plan de
prevención o descontaminación vigente (Ley 19.300), las exigencias térmicas son **las del plan** (Art. 4.1.10
inc. 2°). La regla vale solo para viviendas. Educación, salud y hoteles en zona PDA siguen el Art. 4.1.10. Ver
`pda-ppa.md`.

## 4. Vigencia

| Hito | Fecha | Fuente |
|---|---|---|
| Firma del DS 15 | 09-06-2021 | `ds15-2024` (encabezado del decreto) |
| Publicación en el D.O. | 27-05-2024 | `ds15-2024` |
| **Entrada en vigor del nuevo Art. 4.1.10** (reemplaza el 4.1.10 y el 4.1.10 Bis anteriores) | **28-11-2025**: rige "una vez transcurridos" 18 meses desde la publicación | DS 15 art. 1° transitorio; MINVU (`minvu-comunicado-rt`); OGUC actualizada, tabla de modificaciones ("15 D.O. 27.05.24 — 28.11.25") |
| Condiciones de cálculo de condensación (Res. Ex. 1802) | Firmada el 26-11-2025; D.O. 03-12-2025 según búsqueda, sin confirmar | `res-ex-1802-2025` |
| NCh 853:2021 oficial | Desde 27-11-2025 | `dex-40-2025` |
| Vía alternativa por **demanda de energía** (Informe de Precalificación, solo viviendas) | El valor de demanda rige a los **36 meses** desde la publicación, o sea **mayo de 2027** (aprox. 27/28-05-2027). La resolución con el umbral **no está publicada** al 2026-11-05 → **PENDIENTE** | DS 15 art. 2° transitorio; `umbral-demanda-cev` |

## 5. Régimen transitorio: ¿qué norma se aplica a mi proyecto?

1. **Regla general:** la DOM evalúa la solicitud de permiso con las normas vigentes **a la fecha de su ingreso**
   (OGUC Art. 1.1.3). Si el permiso ingresó el 28-11-2025 o después, rige el nuevo Art. 4.1.10. Si ingresó antes,
   rige el texto anterior.
2. **Anteproyecto aprobado:** mantiene, para obtener el permiso, la vigencia de las normas de la OGUC "consideradas
   en aquél y con las que se hubiere aprobado", por **180 días** (o **1 año** en los casos del artículo: loteos de
   más de 5 ha, edificación de más de 10.000 m², o si se requiere pronunciamiento de otra repartición) (OGUC
   Art. 1.4.11). Si un anteproyecto aprobado con la norma anterior "congela" el estándar térmico depende de que esa
   norma se haya considerado en él. Ese criterio no está publicado: **pendiente**. Recomendación: que la DOM lo
   confirme por escrito.
3. **El DS 15 no trae otra regla de transición** de permisos: solo los dos artículos transitorios (vigencia a
   18 meses y umbral de demanda a 36 meses).
4. **Alternativa de sellos (C, infiltración):** mientras en la **región** del proyecto no haya profesionales,
   especialistas ni laboratorios registrados en MINVU que puedan ensayar según NCh 3295, se puede reemplazar la clase
   de infiltración exigida por una partida de sellos especificada en las EETT. En residencial, solo para **lotes de
   10 unidades o menos** (num. 1.C). En educación y salud no hay tope de lote en el texto (num. 2.C). No vence en
   una fecha: dura mientras se cumpla la condición. Ver `exigencias-C-infiltracion.md`.

## 6. Dónde se acredita ante la DOM

| Etapa | Qué se adjunta | Fuente |
|---|---|---|
| **Solicitud de permiso de edificación** | EETT con las partidas de acondicionamiento térmico. Además, según corresponda: Informe de acreditación, Informe de Ensayo, Memoria de Cálculo o detalle de la solución LOSCAT adoptada. En viviendas, alternativamente, el Informe de Precalificación Energética (cuando rija el umbral) | OGUC Art. 5.1.6 N° 11 |
| **Recepción definitiva** | Según el destino: Informe de Precalificación Energética, Informe de Ensayo, Memoria de Cálculo, o descripción del material o de las soluciones adoptadas y en qué parte de la obra | OGUC Art. 5.2.6 N° 7 |

Los informes y memorias los puede elaborar un profesional competente o especialista, y **los suscribe además el
arquitecto del proyecto** (Art. 4.1.10 inc. 4°). Quién firma qué, y el ensayo de infiltración en obra terminada,
están en `roles-firmas-expediente.md`.

## 7. Fuera de alcance de esta skill (solo detectar y remitir)

Si el proyecto postula a **FSEV** (DS 49 con incremento), es una **Vivienda Industrializada Tipo (VIT)**, o pide
**CES/CVS** u otros estándares de subsidio, la skill lo dice en una línea y remite a la fuente (`fsev-ord-ditec-1163-2023`,
`vit-res-ex-59-2023`). No mezcla sus tablas con las del 4.1.10 (AGENTS.md regla 9).

## Fuentes oficiales a revisar

- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Página RT de MINVU: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- OGUC actualizada (MINVU, marzo 2026): https://www.minvu.gob.cl/wp-content/uploads/2019/05/OGUC-Marzo-2026-D.S.-N%C2%B02-D.O.-16-03-2026.pdf
