# Exigencia B — Condensación superficial e intersticial

Verificado: **2026-11-05**. Fuentes: `ds15-2024` (num. 1.B y 2.B) y `res-ex-1802-2025` (Res. Ex. N°1802 MINVU,
26-11-2025: condiciones de cálculo). La Res. Ex. 1802 es un PDF escaneado: se leyó por OCR y se revisaron las
imágenes de las pp. 1–3, 11 y 12. Este archivo **no reproduce la NCh 1973**: describe el método en palabras propias y
remite al visor `normastecnicas.minvu.cl`.

## 1. Qué exige el Art. 4.1.10

- **Alcance:** complejos de techumbre, muros perimetrales y piso ventilado (num. 1.B residencial; num. 2.B educación
  y salud).
- **Exigencia:** que **no exista riesgo** de condensación **superficial** ni **intersticial**, calculado con el
  procedimiento de la **NCh 1973** y las **condiciones de cálculo que fija MINVU por resolución**, que hoy son la
  Res. Ex. 1802.
- **Única vía:** **Memoria de Cálculo**. No hay LOSCAT, ensayo ni R100 para B. La CEV tampoco la reemplaza
  (Art. 4.1.10 inc. 5°).
- **Puentes térmicos:** el análisis de condensación **superficial** debe incluirlos.
- **Residencial, además:** el diseño debe permitir que el vapor que entra al complejo **salga al exterior**
  (num. 1.B).
- **Hoteles: exentos** (num. 1.B). Ver `docs/contradicciones.md` C11.
- En **viviendas en zona PDA** rige lo que diga el plan. Algunos (por ejemplo O'Higgins DS 1/2021 y Quillota DS 18/2023, según una matriz interna previa) piden condensación NCh 1973. Se detalla y verifica por plan en `pda-ppa.md`.

## 2. Condiciones de cálculo (Res. Ex. 1802, num. 1)

| Parámetro | Valor / regla | Num. |
|---|---|---|
| Momento del análisis | Un momento determinado del año, con los datos de temperatura y humedad del emplazamiento | 1.1 |
| Humedad relativa crítica superficial (φsi,cr) | **1,0 (100 %)**. Opcional: **0,8 (80 %)** para evaluar **moho** | 1.1 |
| Resistencias superficiales | Las del **Anexo 2** según el elemento (`data/res1802_anexo2_rs.csv`). Opcional: efecto del mobiliario | 1.1, Anexo 2 |
| Secciones mínimas | **A** = la de mayor resistencia térmica; **B** = la de menor resistencia (**puente térmico constructivo**). Cada sección incluye todas sus capas homogéneas, con espesor, conductividad y resistencia a la difusión de vapor de cada una | 1.1 |
| Ambiente **interior** | **19 °C** y **HR hasta 75 % (inclusive)** | 1.2 |
| Ambiente **exterior** | T y HR **según emplazamiento** (comuna o localidad y zona), en el **Anexo 1** | 1.2, Anexo 1 |
| Factor de resistencia al vapor "infinito" | Se modela como **1×10⁶** | Nota del 1.3 |

### Anexo 2 — Resistencias superficiales (m²K/W)

| Elemento | Flujo de calor | Rsi | Rse |
|---|---|---|---|
| Techo | Ascendente | 0,10 | 0,04 |
| Muro | Horizontal | 0,13 | 0,04 |
| Piso ventilado | Descendente | 0,17 | 0,04 |
| Mobiliario (opcional, cualquier elemento) | Todas | 0,25 | 0,04 |

### Excepciones (num. 1.3)

1. **Revestimiento interior con resistencia al vapor infinita:** basta el cálculo de condensación **superficial**. Se
   exceptúa el **intersticial**.
2. **Revestimiento exterior con cámara de aire:** ese revestimiento **no se considera** en el cálculo.
3. **Techumbre con barrera hidrófuga bajo un revestimiento exterior con resistencia al vapor infinita:** ese
   revestimiento no se considera en el cálculo **intersticial**.
4. **Puentes térmicos puntuales** que no superan el **10 %** de la superficie de la solución: se puede exceptuar el
   cálculo superficial e intersticial **en esa sección**.

### Clima exterior: Anexo 1 y macrozonas

- El **Anexo 1** fija T°ext y HRext por **zona térmica** y por comuna o localidad. Algunas comunas se distinguen por
  meridiano o altitud, igual que en `data/zonas_comunas.csv`. **Particularidades climáticas (p)** con datos propios:
  Antártica chilena, las islas de Pascua, Alejandro Selkirk, Robinson Crusoe, Santa Clara, Salas y Gómez, San Ambrosio
  y San Félix, y localidades como Calama, María Elena, San Pedro de Atacama, Sierra Gorda, Futaleufú y Palena.
  El Anexo 1 completo está en **`data/res1802_anexo1_clima.csv`** (423 filas: 409 comuna-zona, 5 grupos y 9 filas
  "todas las comunas…"). Para obtener el clima de una comuna:
  1. Fila `tipo=comuna` con su `comuna_zonas` y su `zona`. Si la comuna tiene varias zonas, `condicion` repite la
     condición de altitud o meridiano de la tabla de zonas.
  2. Si no hay fila propia, buscar el `grupo` que la nombre (por ejemplo, las islas de C(p) incluyen Juan Fernández).
  3. Si no, usar la fila `resto` ("Todas las comunas…") de la zona.
  4. `particularidad=1` marca las (p).
- **Macrozonas** (final del Anexo 1, `data/res1802_macrozonas.csv`): si una misma solución se acredita para **varias
  zonas**, se pueden agrupar con estos datos:

| Macrozona | T°ext (°C) | HRext (%) | Alcance resumido |
|---|---|---|---|
| B/C/D y B/C/D/E | 2,2 | 92 | Todas, salvo Calama, María Elena, San Pedro de Atacama, Sierra Gorda, islas oceánicas y San José de Maipo |
| B/C/D(p) y B/C/D/E(p) | 0,4 | 27 | Todas, salvo islas oceánicas (para las particularidades (p) del norte) |
| F/G | 3,5 | 98 | Todas las comunas |
| H/I | −1,6 | 93 | Todas, salvo Calama, San Pedro de Atacama, Antártica, Futaleufú y Palena |
| H/I(p) | −5,6 | 86 | Todas, salvo Antártica |

  La **zona A** y los territorios insulares y antárticos **no pueden** agruparse en macrozonas.

## 3. Cómo se calcula, en palabras propias (sin reproducir la NCh 1973)

1. Se arma la sección (A y B) con sus capas, y las resistencias superficiales del Anexo 2.
2. **Superficial:** con las temperaturas interior y exterior se obtiene la temperatura de la cara interior. Hay riesgo
   si la humedad relativa en esa superficie supera el valor crítico (100 %, u 80 % si se evalúa moho), dada la
   humedad interior de 75 %. Los puentes térmicos (sección B) suelen ser los que definen el resultado.
3. **Intersticial:** se comparan, capa por capa, la presión de vapor que se da en el complejo (según la resistencia a
   la difusión de cada capa) con la presión de saturación que corresponde a la temperatura en ese punto. Hay riesgo
   si la primera alcanza a la segunda en alguna interfaz. Las barreras de vapor del lado caliente y las capas abiertas
   a la difusión del lado frío reducen el riesgo. Esto es coherente con la exigencia de que el vapor pueda salir al
   exterior.
4. Los detalles (ecuaciones, criterios por mes, tratamiento de la condensación acumulada) están en la NCh 1973.
   Consultarla en el visor oficial; la skill no los reproduce.

**Herramientas oficiales MINVU** (página RT): planilla "Análisis higrotérmico" (v2026-07-13) y "Condensaciones DITEC
V2026.04". Ambas son material de apoyo; la exigencia está en el DS 15 y en la Res. Ex. 1802.

## 4. Trampas

- **"Hasta 75 % HR" y "100 %" no se contradicen:** son el ambiente interior y el umbral crítico superficial
  (`docs/contradicciones.md` C03).
- Calcular solo la sección corriente y omitir el **puente térmico** (sección B).
- Usar la NCh 3136 como si fuera exigible: no lo es. Los puentes se tratan con las secciones A/B.
- Creer que la CEV o el LOSCAT acreditan condensación: **no**. Siempre se necesita Memoria de Cálculo.
- Aplicar condensación a un **hotel**: está exento.
- Usar el clima de la zona sin revisar si la comuna es una **particularidad climática (p)**.

## 5. Observación sobre el texto de la Res. Ex. 1802

La numeración pasa del num. 1 (condensación) al num. 3 (NCh 853) y al num. 4 (NCh 3117). No hay un num. 2 visible en
el PDF oficial. No cambia las exigencias. Para citar, usar el numeral tal como aparece.

## Fuentes oficiales a revisar

- Res. Ex. 1802 (PDF MINVU): https://www.minvu.gob.cl/wp-content/uploads/2025/11/Condiciones-de-Calculos-Condensacion_Res.-Ex.-1802.pdf
- Página RT de MINVU (planillas higrotérmicas): https://www.minvu.gob.cl/nueva-reglamentacion-termica/
- NCh 1973 en el visor: https://normastecnicas.minvu.cl/
