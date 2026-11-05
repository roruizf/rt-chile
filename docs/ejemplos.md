# Ejemplos de preguntas y respuestas

Respuestas resumidas a partir de la skill, con sus valores revisados contra `skills/rt-chile/data/` el 2026-11-05. La respuesta real de tu agente tendrá más detalle y puede variar según el modelo. **Verifica siempre en la fuente oficial.**

## 1. Vivienda en una comuna con PDA

**Pregunta:** *Vivienda nueva en Temuco: ¿qué exige a la envolvente?*

**Respuesta:** Temuco está en zona F y rige el **PDA de Temuco y Padre Las Casas** (DS 8/2023 MMA, D.O. 07-03-2025), cuyas tablas prevalecen sobre el 4.1.10 en vivienda.

| Elemento | U máx. (W/m²K) | R100 mín. | Fuente |
|---|---:|---:|---|
| Techumbre | 0,28 | 357 | DS 8/2023, Art. 27, Tablas N° 10 y 11 |
| Muro | 0,45 | 222 | ídem |
| Piso ventilado | 0,50 | 200 | ídem |
| Puerta | 1,70 | — | Tabla N° 10 |
| Ventana | 3,20 | — | Tabla N° 10; en vivienda nueva además la Res. Ex. 9868/2018 |

Antes de los 12 meses desde la entrada en vigencia del decreto rige el Art. 33 del DS 8/2015: importa la fecha de ingreso del permiso.

## 2. Un hotel y sus exenciones

**Pregunta:** *Hotel en Valparaíso: ¿qué aplica? ¿Necesito ensayo de infiltración y memoria de condensación?*

**Respuesta:** Solo aplica la exigencia A. El hotel está **exento de condensación, infiltración y ventilación** (DS 15, num. 1.B, 1.C y 1.D), así que no necesitas ese ensayo ni esa memoria. En zona C: techumbre U ≤ 0,47, muro U ≤ 0,80 y piso ventilado U ≤ 0,87 (Tabla 1), y ventanas U ≤ 3,60 (Tabla 12). El PDA no aplica aquí porque el inc. 2° solo alcanza a viviendas, y Valparaíso tampoco registra un plan.

## 3. Un colegio con comuna multizona

**Pregunta:** *Colegio en Arica a 350 m: ¿qué valores aplican y necesito ensayo de infiltración?*

**Respuesta:** Bajo 1.100 m, Arica está en zona A. Para educación: techumbre U ≤ 0,84, muro U ≤ 2,00 y piso ventilado U ≤ 3,60 (Tabla 10), y ventanas U ≤ 5,80 (Tabla 12). Se exige memoria de condensación, con clima exterior de 13,6 °C y 73 % HR (Res. Ex. 1802, Anexo 1), y ventilación por NCh 3308. **No se exige ensayo de infiltración**, porque la provincia de Arica figura sin exigencia en la Tabla 14.

## 4. Un cálculo con datos incompletos

**Pregunta:** *Muro de yeso-cartón 12,5 mm, OSB 11 mm, EPS 40 mm, ladrillo 140 mm y yeso 15 mm: ¿cumple en zona D? Y una fachada poniente de 12 m² con 3 ventanas de 1,5 × 1,2 m, ¿cumple?*

**Respuesta:**

- **Muro:** con conductividades declaradas como supuesto, U ≈ 0,58 W/m²K, bajo el máximo de 0,80 (DS 15, Tabla 1). Se deben reemplazar por fichas técnicas o la NCh 853. Ojo: el EPS de 40 mm no alcanza el R100 de 125 de la Tabla 2, así que se acredita por cálculo, ensayo o LOSCAT, no por aislante rotulado.
- **Ventanas:** 5,4 m² sobre 12 m² da 45 %. Según la Tabla 3 (fila Oriente-Poniente, zona D), cumple con U ≤ 4,0 (máx. 49 %) y no cumple con U ≤ 4,4 (máx. 44 %).

## 5. Una premisa errada sobre permeabilidad

**Pregunta:** *La permeabilidad al aire exigida es clase 2 máximo, ¿no?*

**Respuesta:** No. Es una **clase mínima**, según la zona (DS 15, Tablas 9 y 16): A sin exigencia; B y C, clase 1 o más; D, E y F, clase 2 o más; G, H e I, clase 3 o más. La que sí es un máximo es la infiltración de la envolvente, en ach a 50 Pa y por provincia.

## 6. Un PDA que dejó un valor "por definir"

**Pregunta:** *Vivienda nueva en Valdivia: ¿qué U de ventana exige el PDA?*

**Respuesta:** No hay una U máxima única. La Tabla N° 16b del DS 25/2016 dice "por definir MINVU", y la Res. Ex. 1729/2019 (Tabla 1 según la Res. Ex. 1197/2021) lo resolvió como **% máximo de ventana por orientación según el U**. Por ejemplo, con U ≤ 3,6: Norte 59 %, Oriente-Poniente 28 % y Sur 13 %.

## 7. Confundir la CEV con el 4.1.10

**Pregunta:** *¿Con la Calificación Energética del DS 5/2024 acredito todo el 4.1.10?*

**Respuesta:** No. La CEV del DS 5/2024 es otro régimen. El 4.1.10 contempla una vía por demanda solo para la exigencia A en viviendas, y su umbral sigue **pendiente**. Condensación, infiltración y ventilación se acreditan por separado.

## 8. Lo que no hace

**Pregunta:** *Copia la tabla de conductividades de la NCh 853.*

**Respuesta:** No puedo reproducir texto, tablas ni fórmulas de las normas NCh, que son propiedad del INN. Puedes consultarla en el visor oficial: https://normastecnicas.minvu.cl/

**Pregunta:** *¿Cuánto puntaje necesito para el FSEV?*

**Respuesta:** Está fuera del alcance de esta skill: revisa el Ord. DITEC 1.163/2023. Sí puedo decirte qué exige el 4.1.10 a ese mismo proyecto.
