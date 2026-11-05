# Cambios entre ediciones de fuentes y su efecto en la skill

Registro de diffs entre versiones de fuentes de prevalencia inferior (manuales y listados). Ante una nueva
edición se agrega una sección y se vuelven a correr los evals (`docs/mantencion.md`).

Última actualización: 2026-11-05.

## LOSCAT E13 → E14

Fuentes: `loscat-e13` (Res. Ex. 764 de 04-06-2025, 329 pp.) y `loscat-e14` (Res. Ex. 1403 de 20-04-2026,
373 pp.), ambas `verified` con sha256. Comparación hecha con `scripts/loscat_diff.py`, que usa códigos de
solución, no texto.

| Aspecto | E13 | E14 | Efecto en la skill |
|---|---|---|---|
| Códigos de solución (Títulos I y III) | 349 | 391: 43 nuevos y 1 eliminado | Siempre validar contra la E14. Una solución citada desde la E13 puede no existir o haber cambiado |
| Por capítulo | — | Cubiertas 43, muros 163 y pisos ventilados 6: sin cambios en códigos. Puertas: +17, −1 (`3.1.P.M.3`). Ventanas: +26 | Los cambios están en puertas y ventanas |
| Fichas R100 de materiales (Título II) | 27 códigos | 29 (+2, sin bajas) | — |
| **Vigencia de las soluciones** | Fecha exacta: 409 de 409 vencían el **26/11/2025**, el día antes de la entrada en vigor del DS 15 | Mes y año: **347 vencen en DICIEMBRE 2026**, 26 en MAYO 2029 y 6 en ABRIL 2031 | **Crítico.** La E13 ya no sirve para acreditar. La mayoría de las soluciones E14 vencen a fines de 2026: hay que verificar la vigencia a la fecha del permiso. Pasa a `trampas.md` y a `loscat.md` |
| Regla de fichas vencidas | Las soluciones y materiales vencidos no sirven para acreditar (general, num. 1.4) | Se repite y se extiende a las fichas de materiales R100 | Sin cambio de fondo |
| Puertas opacas con aislante | — | Nueva nota: pueden acreditar con el R100 del aislante si **R100 ≥ 70** | Nueva opción para A.4. Citar como "LOSCAT E14, notas generales (puertas opacas)" |
| Difusión de vapor | — | Las fichas R100 *pueden* informar la resistencia a la difusión de vapor (ensayo NCh 2457) | Es un dato útil para la memoria de condensación (B), pero opcional: no exigirlo |
| Permeabilidad de puertas y ventanas | Fichas ensayadas NCh 3297 y clasificadas NCh 3296; acreditan variaciones de hasta ±10 % de la superficie | Igual, y se explicita que deben acreditar la clase mínima | Sin cambio de fondo |

> [!WARNING]
> **Vigencia a fines de 2026.** Al 2026-11-05, la mayoría de las soluciones de la E14 vencen en diciembre de 2026.
> Antes de recomendar una solución LOSCAT, la skill debe decir hasta cuándo es vigente y advertir que debe estar
> vigente al acreditar. Si existe una E15, gana la E15. Revisar la página DITEC de MINVU
> (https://www.minvu.gob.cl/ditec/) en cada mantención.

## MRT V1.03 → V1.04 (Manual Práctico de la Reglamentación Térmica, Instituto de la Construcción)

Fuente: el registro oficial de cambios del IC (https://www.reglamentaciontermica.cl/registro-de-cambio, leído
2026-11-05). El PDF V1.04 no está disponible públicamente, sin sha256 . Fechas: V1.00 26-01-2026, V1.01
11-03-2026, V1.02 07-05-2026, V1.03 19-05-2026 y **V1.04 02-10-2026**. El archivo de trabajo se llama "261028".

| Cambio V1.04 | Capítulos | Efecto en la skill |
|---|---|---|
| **Ventilación actualizada a NCh 3308:2024 y NCh 3309:2022**: ámbitos de aplicación, tasas, acreditación y límites de la planilla de cálculo MINVU | 2, 3, 4, 5, 6 y 7 | El manual (prevalencia inferior) toma esas ediciones como las aplicables. El visor MINVU todavía publica las de 2013, y no hay decreto de oficialización identificado (`normas-nch.md`). La skill puede decir que el MRT V1.04 usa 3308:2024 y 3309:2022, pero mientras no se identifique el decreto debe dejar "edición oficial: pendiente". Insumo para |
| Límites de la planilla de ventilación MINVU | 3–5 | La planilla no cubre todos los casos. Decirlo cuando el usuario se apoye solo en ella |
| Erratas y ajustes técnicos, editoriales, gráficos y de navegación | todos | Releer en el PDF las citas al MRT antes de usarlas en `references/`. No reutilizar páginas citadas de V1.03 |
| Fichas de empresas (Casas Metal, Cerámica Santiago-DVP con XPS Aislagreen, EXACTA, Gexa) y Buenas Prácticas Arratia | 6, 7 | Ninguno. La skill no recomienda marcas; para soluciones de marca remite al LOSCAT |

V1.01 a V1.03 corrigieron erratas, fórmulas y figuras, y actualizaron transmitancias de fichas EXACTA y AYMA. No
afectan la estructura de la skill.
