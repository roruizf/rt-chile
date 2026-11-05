# Exigencia C — Infiltraciones de aire y permeabilidad de puertas y ventanas

Verificado: **2026-11-05**. Fuente: `ds15-2024` (num. 1.C residencial y 2.C educación y salud; Tablas 7, 8, 9, 14, 15
y 16, que son imágenes en el D.O. y se transcribieron a `data/`). Es una paráfrasis propia del acto público. La NCh
3295, 3296 y 3297 no se reproducen.

> [!IMPORTANT]
> - **Hoteles: exentos** de toda la exigencia C (num. 1.C).
> - En **viviendas en zona PDA** mandan las clases del plan (`pda-ppa.md`).

## 1. Dos exigencias distintas

| | (a) Infiltración de la **envolvente** | (b) Permeabilidad de **puertas opacas y ventanas** |
|---|---|---|
| Qué se mide | Clase de infiltración a **50 Pa**, en renovaciones por hora (ach), de la envolvente **sin** puertas ni ventanas | Clase final de permeabilidad al aire a **100 Pa** del elemento |
| Depende de | **Provincia** (Tablas 7 y 14) | **Zona térmica** (Tablas 9 y 16) |
| Criterio | Clase medida **≤** la de tabla | Clase **≥** la de tabla (clase 3 es más exigente que 1) |
| Cuándo | **Obra terminada** (ensayo en terreno), se adjunta en la recepción | Antes: ensayo de laboratorio o LOSCAT del elemento |
| Datos | `data/ds15_t07_t14_infiltracion_provincia.csv` | `data/ds15_t09_t16_permeabilidad_zona.csv` |

## 2. (a) Infiltración de la envolvente: clase máxima por provincia (Tabla 7 = Tabla 14)

| Clase (ach a 50 Pa) | Provincias |
|---|---|
| **Sin exigencia** | Arica, Iquique, Tocopilla, Chañaral, Isla de Pascua |
| **4,00** | Parinacota, Tamarugal, El Loa, Coyhaique, Aysén, General Carrera, Capitán Prat, Última Esperanza, Magallanes, Tierra del Fuego, Antártica Chilena |
| **5,00** | Copiapó, Limarí, Los Andes, Valparaíso, Santiago, Cordillera, Maipo, Melipilla, Talagante, Cachapoal, Cardenal Caro, Colchagua, Talca, Concepción, Arauco, Malleco, Cautín, Valdivia, Ranco, Osorno, Llanquihue, Palena, Chiloé |
| **8,00** | Antofagasta, Huasco, Elqui, Choapa, Petorca, Quillota, San Felipe de Aconcagua, San Antonio, Marga Marga, Chacabuco, Curicó, Linares, Cauquenes, Diguillín, Punilla, Itata, Biobío |

Nota de las tablas: la clase se mide **sellando los dispositivos de ventilación**. La tabla de zonas escribe algunas
provincias con otra grafía (Aisén, Coihaique, San Felipe, Bío-Bío, etc.). La columna `provincia_tabla_zonas` del CSV
hace la unión.

### Cómo se acredita (num. 1.C y 2.C)

- **Informe de Ensayo en terreno según NCh 3295**, con la obra terminada. Lo pueden hacer:
  - el arquitecto del proyecto;
  - un profesional competente o especialista **inscrito en el Registro de Consultores MINVU (DS 135)**;
  - un **laboratorio del registro DS 10**.
- **Muestra, residencial (Tabla 8, `data/ds15_t08_muestra_infiltracion_residencial.csv`):**

  | Tamaño del lote (viviendas) | Muestra | Ítemes no conformes que rechazan |
  |---|---|---|
  | 11 a 50 | 2 | 1 |
  | 51 a 500 | 3 | 1 |
  | más de 501 (">501") | 5 | 1 |

  Si se llega al número de no conformes, el lote se **rechaza** y se **repite el ensayo con el doble de muestra**.
- **Muestra, educación (Tabla 15):** según los recintos docentes: 5–16 → 2; 17–24 → 3; 25–32 → 4; más de 32 → 10 %.
  Cuentan como docentes: laboratorios, talleres y multitalleres, aulas, aulas de integración, sala de profesores, salas
  de actividades de párvulos y biblioteca/CRA.
- **Muestra, salud:** el **5 %** del total de recintos perimetrales acondicionados (num. 2.C).

> [!WARNING] Huecos del texto oficial (responder con supuesto declarado)
> - **Si la vivienda está en un PDA con tabla propia de muestras** (Temuco Tabla Nº 14, O'Higgins Tablas 11/20, Quillota
>   Tablas 28/37), **manda la del plan y no hay hueco**: lote < 11 → 1 vivienda (`scripts/pda.py`).
> - **Lotes residenciales de 1 a 10 viviendas:** la Tabla 8 parte en 11. El texto no fija la muestra para lotes
>   chicos con ensayo. Supuesto prudente: ensayar al menos 1 vivienda representativa. **Pendiente** de criterio
>   MINVU.
> - **Lote de exactamente 501:** la Tabla 8 dice "51 a 500" y ">501". Supuesto conservador: muestra de 5.
> - **Educación con menos de 5 recintos docentes:** la Tabla 15 parte en 5. Mismo tratamiento: pendiente, con
>   supuesto declarado.
> - **Salud:** el 5 % puede dar fracción. Supuesto: redondear hacia arriba, mínimo 1.

### Alternativa de sellos (num. 1.C y 2.C)

En lugar de cumplir la clase de la tabla, se puede especificar en las **EETT** una partida de **sellos** en: encuentros
marco-vano de puertas y ventanas; uniones de distinta y de igual materialidad; perforaciones de instalaciones;
encuentros de solera inferior y superior con su soporte; dispositivos de ventilación; ductos de evacuación de gases; y
otros encuentros similares. Condiciones:

1. **Mientras en la región no existan** profesionales, especialistas ni laboratorios registrados en MINVU habilitados
   para el ensayo NCh 3295.
2. En **residencial**, solo para **lotes de 10 unidades o menos**. En educación y salud el texto no pone tope de lote.
3. **Caduca cuando MINVU lo establezca por resolución.** Al 2026-11-05 no se conoce esa resolución: verificarlo
   antes de recomendarla.
4. En **educación y salud**, el num. 2.C dice que los proyectos en las provincias de clase 4,00 (Parinacota a
   Antártica Chilena) "solo podrán utilizar esta alternativa de acreditación". Por dónde está esa frase en el texto,
   se lee como que **en esas provincias solo cabe el ensayo en terreno**, sin sellos. Es una interpretación: hay que
   declararla como tal y sugerir confirmarla con la DOM o DITEC.

## 3. (b) Permeabilidad al aire de puertas opacas y ventanas: clase mínima por zona (Tabla 9 = Tabla 16)

| Zona | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| Clase mínima a 100 Pa | sin exigencia | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 |

- Las clases son las de la **NCh 3296** y se refieren a la clasificación final del elemento ensayado según la **NCh
  3297**.
- **Vías:**
  1. **Informe de Ensayo** NCh 3296/3297 de un **laboratorio DS 10**; o
  2. **solución LOSCAT** de puerta o ventana (Título III del LOSCAT E14; las fichas acreditan variaciones de hasta ±10 %
     de la superficie, `docs/cambios-fuentes.md`).

## 4. Trampas

- Confundir 50 Pa (envolvente, por provincia) con 100 Pa (puertas y ventanas, por zona).
- Leer la permeabilidad como un máximo: **una clase mayor es más exigente**, y se pide clase **≥** la de tabla.
- Pensar que el ensayo de infiltración va en el permiso: se hace en **obra terminada** y se presenta en la
  **recepción**.
- Aplicar la exigencia C a un hotel: está exento.
- Ofrecer la alternativa de sellos sin verificar las tres condiciones (región sin ensayadores, lote ≤10 en
  residencial, y que no haya resolución que la elimine).

## Fuentes oficiales a revisar

- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Lámina DITEC "Actualización RT" (resumen de infiltración por provincia): https://www.minvu.gob.cl/wp-content/uploads/2025/11/Actualizacion-RT_DITEC.pdf
- Registro de Consultores (DS 135) y de Laboratorios (DS 10): https://www.minvu.gob.cl/
