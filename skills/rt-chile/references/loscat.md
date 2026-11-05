# LOSCAT E14 — cómo buscar y usar una solución

Verificado: **2026-11-05**. Fuentes: `loscat-e14` (Listado Oficial de Soluciones Constructivas para Acondicionamiento
Térmico, ED14, aprobado por Res. Ex. N°1403 de 20-04-2026, 373 pp., sha256 en el manifiesto), `loscat-e13` (para el
diff), `ds15-2024` (vía LOSCAT en cada literal). Edición 14 confirmada como la última el 2026-11-05. **E15:
fuente a vigilar** (`loscat-e15`, `watch: true`).

## 1. Qué es y para qué sirve

- Es la vía 4 de la exigencia A (opacos, puertas, ventanas, sobrecimiento) y la vía 2 de la permeabilidad de puertas y
  ventanas (C). **No sirve** para condensación (B), infiltración de la envolvente (C) ni ventilación (D)
  (`vias-acreditacion.md`).
- La solución debe estar **vigente** al acreditar. Las fichas vencidas no sirven (notas generales del LOSCAT).

## 2. Estructura y códigos

| Prefijo | Capítulo | Fichas en el índice propio |
|---|---|---|
| `1.1.` | Cubiertas / techumbres (G = genérica, M = de marca) | 6 |
| `1.2.` | Muros | 152 |
| `1.3.` | Pisos ventilados | 5 |
| `2.x` / `R100/…` | Materiales aislantes con su R100 (Título II), p. ej. `R100/LV.2.2` | 12 |
| `3.1.P.` | Puertas (A aluminio, M madera, P PVC…) | 28 |
| `3.2.V.` | Ventanas | 145 |

El índice propio está en **`data/loscat_e14_indice.csv`**: código, capítulo, nombre corto, página del PDF y vigencia.
Lo regenera `scripts/build_loscat_indice.py`, que valida el sha256. No copia descripciones ni valores de desempeño:
para U, R100, clase de permeabilidad o detalles, abrir la ficha en el PDF oficial, en la página indicada.

## 3. Vigencia: regla crítica

- Opacos (techumbres, muros, pisos) y materiales: la vigencia está extraída por ficha o desde las páginas de índice.
  **La gran mayoría vence en diciembre de 2026**; algunas, en mayo de 2029 o abril de 2031.
- Puertas y ventanas: la ficha trae el rótulo "Vigencia" pero el valor no está en el texto (`vigencia_fuente =
  no_extraida`). Hay que revisarlo en el PDF.
- **La skill siempre** informa la vigencia y la compara con la **fecha de la consulta** (o del ingreso del permiso). Si
  la solución vence antes o cerca de esa fecha, lo advierte, y si existe una edición posterior (E15) remite a ella.
  Caso `critical` de evals: "vigencia LOSCAT por fecha de consulta".

## 4. Cómo buscar una solución

1. Filtrar `data/loscat_e14_indice.csv` por capítulo y por palabras del nombre corto (material o marca).
2. Abrir la ficha en el PDF oficial, en `pagina_pdf`, y leer el desempeño por zona térmica (U o R100), la clase de
   permeabilidad (puertas y ventanas) y las condiciones de uso.
3. Revisar que cumpla la **zona** del proyecto (`zonificacion.md`) y la tabla que corresponde al uso
   (`exigencias-A-envolvente.md`).
4. Revisar la vigencia (§3).
5. Notas que cambiaron en la E14 (`docs/cambios-fuentes.md`):
   - las puertas opacas con aislante pueden acreditar con R100 ≥ 70;
   - las fichas R100 pueden informar la difusión de vapor (ensayo NCh 2457), lo que sirve para la memoria de
     condensación;
   - las fichas de puertas y ventanas acreditan variaciones de hasta ±10 % de la superficie.

## 5. Trampas

- Citar una solución de la **E13**: todas vencieron el 26-11-2025.
- Suponer que estar en el LOSCAT acredita también condensación, infiltración o ventilación: no lo hace.
- Recomendar marcas: la skill indica el código y la ficha, sin preferir fabricantes.

## Fuentes oficiales a revisar

- Página DITEC (listados vigentes): https://www.minvu.gob.cl/ditec/
- LOSCAT E14: https://www.minvu.gob.cl/wp-content/uploads/2026/04/LOSCAT_E14_MAYO_2026.pdf
