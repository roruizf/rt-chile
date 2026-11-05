# Actos MINVU que completan los PDA (ventanas, control solar, sobrecimiento y condensación)

Fuentes: `sources/private/pdao-ord840-2019-con-ord209.pdf` (8 pp.), `pdao-criterio-ganancias-solares.pdf` (4 pp.) y
`pdao-criterios-art-6-7-8.pdf` (2 pp.). Todos son escaneos y las tablas se leyeron desde la imagen. CSV: `minvu-oficios.csv` (356 filas).

## Actos identificados
| Acto | Fecha | Emisor → destinatario | Qué define | PDF (pp.) |
|---|---|---|---|---|
| **Ord. N°1773** (DITEC) | **16-11-2017** | Jocelyn Figueroa Yousef, Jefa DITEC → Eduardo Carmona J., SEREMI MINVU Los Lagos | Criterios de los arts. 6, 7 y 8 del PDA Osorno: A) condensación (NCh1973/2014 con planilla MINVU; julio; Ti 19 °C; HR 65/75/**85** %; 2 secciones); B) tabla de % de ventanas por orientación y U (Osorno); C) R100 = 91 del sobrecimiento, hasta el hombro de la fundación o **mín. 30 cm bajo el terreno natural**; EETT de infiltración = fichas tipo | art-6-7-8 pp.1-2; copia en oficio pp.4-5 |
| **Ord. N°209** (Ministro) | 20-04-2018 | Cristián Monckeberg B., Ministro V. y U. → "según distribución" (SEREMI Araucanía, Aysén, Los Lagos, Los Ríos, Biobío y Maule) | Instruye informar a las DOM de las comunas con PDA. Tabla 1: R100 del sobrecimiento por PDA. Tabla 2: % máx. de ventanas por orientación y U por PDA. Tabla 3: orientaciones. Ventana en techumbre ≤ 60° con U ≤ 3,6. Acreditación. ANT: Of. DITEC N°1772 a 1777 del 16/11/2017 | oficio pp.6-8 |
| **Res. Ex. N°9869** (Subsecretaría) | 29-11-2018 | Guillermo Rolando Vicente, Subsecretario V. y U. ("Anótese, publíquese en el D.O.") | Formaliza para el **PDA Osorno** el control de ganancias solares y el sobrecimiento, exigibles **desde el 01-01-2019**. Tabla 1: % de ventanas (Osorno). Tabla 2: orientaciones. Tabla 3: R100 = 91. Condensación: HR **65/75/80 %** | ganancias-solares pp.1-4 |
| **Ord. N°840** (SEREMI Los Lagos) | 30-04-2019 | Rodrigo Wainraihgt Galilea, SEREMI MINVU Los Lagos → Ángela Villarroel M., DOM Osorno | Responde los Of. DOM N°354, 355 y 385/2019. Fija el contenido mínimo de las EETT de puertas y ventanas para acreditar la infiltración (art. 8 b) del DS 47). Adjunta los Ord. 1773 y 209 | oficio pp.1-3 |

> [!WARNING] El oficio SEREMI tiene el número **840**, estampado y legible a 400 dpi (`img/o340_num.png`). No es el 340 que dice el nombre del archivo, y el OCR también lee "840". Conviene renombrar la referencia en el repo.

> [!INFO] **Fecha del Ord. 1773: es del 16-11-2017.** Lo confirman el timbre "16 NOV 2017" en las dos copias, el ANT del Ord. 209 ("Of. DITEC N° 1772 … 1777 del 16/11/2017") y el Considerando 1 de la Res. Ex. 9869 ("16 de noviembre de 2017"). El Ord. 840 se contradice: escribe "16.11.2018" en MAT, en el cuerpo y en ADJUNTO, y "16.11.2017" en la p.3. El 2018 es un error del Ord. 840.

## Qué ítem "por definir MINVU" resuelve cada acto
- **Talca-Maule (DS 49, Art. 31)**: el Ord. 209 fija el control solar (Tabla 2, bloque Talca-Maule) y el R100 del sobrecimiento (**45**). No entrega una U de ventana por sí sola: la celda "Por definir – MINVU" de la Tabla 18 queda cubierta por la combinación de % de ventanas y U. No se encontró una Res. Ex. para Talca.
- **Valdivia (DS 25, Art. 28)**: el Ord. 209 fija el control solar (bloque compartido Osorno/Valdivia) y el R100 (91). El Art. 28 pide una *resolución publicada en el D.O.* dentro de 18 meses. En estos PDF no hay una resolución para Valdivia, solo el oficio.
- **Osorno (DS 47, Art. 8)**: el Ord. 1773 da los criterios, el Ord. 209 los instruye y la **Res. Ex. 9869** los formaliza: control solar (Tabla 1), sobrecimiento R100 91 (Tabla 3), criterios de condensación y vigencia desde el 01-01-2019. El Ord. 840 fija las EETT mínimas de infiltración (art. 8 b).
- **Chillán (DS 48, Art. 25 N°5)**: el Ord. 209 fija el control solar (bloque compartido con Temuco) y el R100 (91).
- **Temuco-PLC y Coyhaique**: el Ord. 209 se dictó bajo los planes anteriores (DS 8/2015 y el PDA Coyhaique previo al DS 7/2018). El DS 8/2025 remite a la "Res. N° 9.868/2018 MINVU", que sería la resolución paralela a la 9869 para Temuco. No está en estos PDF.
- **Criterio general** (`minvu-oficios-pda`): ventana en techumbre ≤ 60° con U ≤ 3,6 W/(m²K); orientaciones N, O, S y P (315/45/135/225°); aislación periférica vertical exterior del sobrecimiento desde el NPT hasta el hombro de la fundación; acreditación según NCh3137, NCh3076 o el Listado Oficial MINVU.

## Comparación con los decretos ya transcritos
- **Talca-Maule (Ord. 209) frente a la Tabla 15 de Curicó (DS 44)**: 38 de 40 celdas coinciden. **Difiere la columna U ≤ 5,8**:
  - Ord. 209: O-P = **10 %** y Sur = **15 %**.
  - Curicó: O-P = **15 %** y Sur = **10 %**.
  Los valores están invertidos entre O-P y Sur. La imagen del Ord. 209 se revisó a 300 dpi. El OCR de Curicó (`verif_raw.txt`) también muestra O-P '158' y Sur '108', así que ambas transcripciones son fieles a su fuente. La diferencia está entre los documentos (es plausible un error en uno de ellos).
- **Coyhaique**: el Ord. 209 coincide 40/40 con la Tabla 12 del DS 7/2018 y el R100 91 coincide con la Tabla 14.
- **Temuco/Chillán (Ord. 209)**: coincide 40/40 con la Tabla 19 de Los Ángeles (DS 4/2017). El R100 91 coincide con la Tabla 11 del DS 8/2025 y la Tabla 21 de Los Ángeles.
- **R100 del sobrecimiento de Talca-Maule = 45**: coincide con la Tabla 17 de Curicó y la Tabla Nº17 de Concepción.
- **Osorno**: los tres actos (Ord. 1773, Ord. 209 y Res. Ex. 9869) traen la misma tabla de % (40/40) y el mismo R100 91. El "119 %" del .ocr.txt hermano es en realidad un **19 %**.
- **HR interior para condensación**: el Ord. 1773 dice 65/75/**85 %** y la Res. Ex. 9869 dice 65/75/**80 %**. Los decretos posteriores (Curicó Art. 17-18 y Concepción Art. 24-25) usan 65/75/80 %, igual que la Res. Ex. Ambas imágenes se confirmaron.
- El Ord. 1773 exige la aislación del sobrecimiento hasta "mín. 30 cm bajo el NTN". El Ord. 209 y la Res. Ex. 9869 omiten ese mínimo.
- Ninguno de estos actos fija una U máxima para la ventana de vivienda nueva en muros. La exigencia se expresa como % de superficie según la U, y con U ≤ 5,8 se llega a 0 % en Sur/POND para Osorno, Valdivia, Temuco, Chillán y Coyhaique.

## Tablas transcritas (filas del CSV)
- Ord. 209, Tabla 1 (oficio p.6): 6 filas R100.
- Ord. 209, Tabla 2 (p.7): 6 PDA × 40 = 240 filas.
- Ord. 209, Tabla 3 y criterios (p.7-8): 7 filas generales.
- Ord. 1773, letras A, B y C (art-6-7-8 pp.1-2): 7 + 40 + 2 + 1 filas.
- Res. Ex. 9869, Tablas 1-3 y letra B (pp.2-4): 1 + 40 + 1 + 1 + 1 + 7 filas.
- Ord. 840 (pp.2-3): 2 filas (contenido de las EETT).

Filas por plan: Osorno 144; Talca, Temuco, Valdivia, Chillán y Coyhaique 41 c/u; general 7. Verificación: `minvu-oficios_verificacion.txt`.
