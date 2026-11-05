# Zonificación térmica: cómo asignar la zona (A–I)

Verificado: **2026-11-05**. Fuentes: `ds15-tabla-zonas` (tabla oficial MINVU "Zona Térmica, Regiones, Provincias y
Comunas", verified con sha256), `ds15-2024` (el Art. 4.1.10 remite a los planos de zonificación de la NCh 1079),
`res-ex-1802-2025` (num. 1.2, particularidades climáticas), `ds15-zonificacion-termica` (mapa nacional DITEC).

## Regla de la skill (aprobada el 2026-11-05)

1. La zona se asigna con la **tabla oficial MINVU de comunas**, cargada en `data/zonas_comunas.csv` y regenerable
   con `scripts/build_zonas_csv.py`, que valida el sha256 del PDF.
2. Edición de la NCh 1079: "probablemente 2019, oficial pendiente" (`docs/verificaciones.md` §1). **Ninguna
   respuesta puede depender de la edición de la NCh 1079.**
3. Hay **9 zonas, A a I**. Las tablas del DS 15 asignan exigencias por zona (Tablas 1–3, 5, 6 y 9 en residencial;
   10–13 y 16 en educación y salud). La infiltración (Tablas 7 y 14) va por **provincia**, no por zona.

## Cómo usar `data/zonas_comunas.csv`

Columnas: `region, provincia, comuna, zona, alt_min, alt_min_incl, alt_max, alt_max_incl, lon_oeste_min,
lon_oeste_min_incl, lon_oeste_max, lon_oeste_max_incl, condicion_original`.

- 410 filas y **345 comunas**. 286 comunas tienen una sola zona. **59 comunas tienen más de una**: 51 se separan por
  altitud y 8 por meridiano (Antofagasta, Copiapó, La Higuera, La Ligua, La Serena, La Unión, Ovalle y Taltal; en
  algunas también cuenta la altitud).
- Altitud en msnm. Los cortes que usa la tabla son 1.000, 1.100, 2.000 y 3.000. Meridiano en grados de longitud
  **oeste**, en decimales (71° 15' = 71,25).
- `*_incl` = 1 si el límite es inclusivo (≤, ≥) y 0 si es estricto (<, >). Un campo vacío significa "sin límite".
- `condicion_original` guarda la notación de la tabla para poder citarla.

### Procedimiento

1. Buscar la comuna. Si tiene **una fila**, esa es la zona.
2. Si tiene **varias filas**, se necesita la **altitud** del terreno (msnm) y, en las 8 comunas con meridiano, la
   **longitud**. Elegir la fila cuyas condiciones se cumplan.
3. Si falta el dato, no adivinar. Hay dos caminos:
   - pedir la cota o la ubicación; o
   - responder **por escenarios** con supuesto declarado (por ejemplo, "si el terreno está bajo 1.000 msnm es zona
     F; si está sobre, es H") y advertir que la zona la fija el emplazamiento real.
4. Si el proyecto queda en un límite exacto, o en una brecha o traslape de la tabla (abajo), decirlo y remitir a la
   DOM o a DITEC.

## Brechas y traslapes de la tabla oficial (detectados el 2026-11-05)

Sale de recorrer cada comuna multizona en una grilla de altitud × meridiano. La tabla no los resuelve. La skill debe
decir que la tabla no define la zona en ese caso, en vez de inventarla.

| Comuna | Problema | Qué dice la tabla | Respuesta de la skill |
|---|---|---|---|
| Putre, General Lagos | **Brecha**: no hay zona bajo 3.000 msnm | Una sola fila: H para ≥ 3.000 | Sobre 3.000 m → H. Bajo 3.000 m → "la tabla no asigna zona; consultar a DITEC/DOM". Supuesto razonable si se pide criterio: H (zona de toda la comuna en la tabla) |
| Camiña | **Brecha** bajo 1.100 msnm | B (1.100–3.000) y H (≥ 3.000) | Igual que arriba. Bajo 1.100 m no hay zona en la tabla |
| Antuco | **Brecha en exactamente 1.000 msnm** (los dos límites son estrictos) | F (< 1.000) y H (> 1.000) | Para 1.000 m exactos, decir la ambigüedad. Supuesto conservador: H, la más exigente |
| Antofagasta, Taltal, Copiapó | **Traslape**: A se define solo por meridiano (≥ 70° o > 70° 44' W) y H solo por altitud (≥ 3.000), así que un punto al oeste del meridiano y sobre 3.000 m cumple ambas | A, B y H | Es improbable en la práctica (costa sobre 3.000 m). Si ocurre, declarar el traslape y aplicar la más exigente como supuesto |

## Comuna Antártica y particularidades climáticas

- La comuna de **Antártica** (Región de Magallanes) **no está** en la tabla MINVU: la tabla tiene 345 comunas. La
  skill responde "zona no asignada por la tabla oficial; pendiente" y remite a DITEC.
- La Res. Ex. 1802 (num. 1.2) define **"particularidades climáticas" (p)** con datos climáticos propios para el
  **cálculo de condensación**: Antártica chilena; las islas de Pascua, Alejandro Selkirk, Robinson Crusoe, Santa
  Clara, Salas y Gómez, San Ambrosio y San Félix; y otras localidades que nombra la resolución. Esto **no cambia la
  zona térmica**: cambia la temperatura y la humedad exterior que se usan en el cálculo (ver
  `exigencias-B-condensacion.md`).

## Trampas frecuentes

- Usar la zonificación antigua de 7 zonas (OGUC previa al DS 15) o mapas de la NCh 1079:2008. Siempre A–I.
- Asignar la zona de una comuna multizona sin preguntar la altitud. Una diferencia de 100 m puede cambiar la zona.
- Confundir **zona** (exigencias A, ventanas, sobrecimiento, permeabilidad) con **provincia** (clase de infiltración,
  Tablas 7 y 14).
- Suponer que una comuna con PDA usa la zona para todo: en viviendas de zona PDA mandan las tablas del plan
  (`pda-ppa.md`).

## Fuentes oficiales a revisar

- Tabla de zonas por comuna (MINVU): https://www.calificacionenergetica.cl/media/TABLA-ZT_REGIONES_PROVINCIAS-Y-COMUNAS.pdf
- Mapa nacional y mapas por macrozona: https://www.minvu.gob.cl/nueva-reglamentacion-termica/ (sección Descargables)
- NCh 1079 en el visor MINVU: https://normastecnicas.minvu.cl/
