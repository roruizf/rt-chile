# Exigencia D — Ventilación

Verificado: **2026-11-05**. Fuentes:
- `ds15-2024` (Art. 4.1.10 num. 1.D y 2.D) y `ditec-lamina-edu-salud-2026-01`.
- El alcance de las NCh 3308 y 3309 está resumido **en palabras propias**, a partir de las copias de trabajo de
  NCh 3308:2024 y NCh 3309:2022 (portadas e índice; ediciones en `normas-nch.md`). **No hay texto, tablas, fórmulas
  ni valores de las normas.** Para tasas y procedimientos, ir al visor https://normastecnicas.minvu.cl/.

## 1. Quién debe cumplir

| Uso | Exigencia | Norma | Fuente |
|---|---|---|---|
| **Residencial** (vivienda, hogares, hospedaje). **Interior de una vivienda → NCh 3309** | Sistema de ventilación que asegure una tasa **no menor** a la de las NCh, con un diseño orientado a una calidad de aire interior aceptable | **NCh 3308 y NCh 3309, "según corresponda"** | num. 1.D |
| **Hoteles** | **Eximidos** | — | num. 1.D ("exceptuando los hoteles") |
| **Educación** | Igual, más los requisitos del sistema necesarios para una calidad de aire aceptable | **Solo NCh 3308** | num. 2.D |
| **Salud** | **Eximida** | — | num. 2.D. Confirmado en la lámina DITEC Edu-Salud ("EXIMIDAS"). Ver `docs/contradicciones.md` C25 |

En **viviendas en zona PDA**, los 11 planes con envolvente regulan la ventilación: remiten a NCh 3308/3309 y **exigen extracción mecánica en baños y cocina con control de higrostato**, además de lo que pida la norma. Citar el artículo del plan con `scripts/pda.py <comuna>` (`pda-ppa.md`). Revisado en el texto de cada decreto el 2026-11-05.

## 2. Cómo se acredita

- **Informe de acreditación de cumplimiento de la tasa de ventilación** según la NCh que corresponda (num. 1.D). En
  educación: **Informe de cumplimiento de la tasa de ventilación** según NCh 3308 (num. 2.D).
- Se adjunta en el permiso con los demás antecedentes térmicos (OGUC Art. 5.1.6 N° 11). **No hay vía LOSCAT, de
  ensayo de laboratorio ni CEV** para D: la vía por demanda no cubre ventilación (Art. 4.1.10 inc. 5°).
- Quién elabora y firma: ver `roles-firmas-expediente.md`. El inciso 4° permite que los informes los haga un
  profesional competente o especialista, y los suscribe además el arquitecto.

## 3. ¿NCh 3308 o NCh 3309? ("según corresponda")

| | NCh 3309 | NCh 3308 |
|---|---|---|
| Alcance (resumido) | **Unidades de vivienda con ocupantes permanentes.** Edición 2022; el título habla de edificios residenciales "de baja altura", pero la cláusula 1 no pone límite de pisos | Recintos con ocupación humana en **edificios en general**. **Excluye el interior de las viviendas permanentes**, que quedan para la NCh 3309 |
| Uso típico en el Art. 4.1.10 | Interior de cada vivienda (casas y departamentos) | Educación. En residencial: recintos que no son interior de vivienda permanente (por ejemplo, espacios comunes, o hospedaje y hogares de ocupación no permanente). **Esta lectura es criterio propio**: el DS solo dice "según corresponda" |
| Qué determina la tasa (a alto nivel) | Superficie de la vivienda y número de dormitorios, como indicador de ocupantes | Uso del recinto, ocupación y superficie (vía prescriptiva). También hay vía de desempeño (calidad de aire) y de ventilación natural |
| Otros requisitos que trae la norma | Componente mecánico en la ventilación general; **extracción local mecánica en cocina y baños**; aberturas operables; hermeticidad; control de aparatos de combustión; alarmas de CO | Extracción obligatoria aparte; documentación de diseño, puesta en marcha y manual de operación y mantención |
| Cómo se verifica en la norma | Medición del caudal instalado; certificados para ventilación variable o equivalente | Documentación de diseño con supuestos y cálculos; Anexo M con planilla de verificación |
| Cláusulas para buscar en el visor | 1 Alcance; 4 Ventilación de la vivienda (4.1 tasa, 4.2 tipo de sistema, 4.3 medición); 5 Extracción local; 6 Otros requisitos; Anexos A y B | 1 Alcance; 6 Procedimientos (6.2 tasa, 6.3 calidad de aire, 6.4 natural, extracción y documentación de diseño); 7 Puesta en marcha; 8 Operación; Anexo M |

**Edición exigible:** pendiente de decreto. El visor MINVU sirve NCh 3308:2024 y NCh 3309:2022, y el MRT V1.04 (IC,
02-10-2026) actualizó su capítulo de ventilación a esas ediciones (`docs/cambios-fuentes.md`). La skill puede decirlo,
pero debe declarar "edición oficial: pendiente" (`normas-nch.md`).

## 4. Implicancias prácticas (criterio, con supuestos declarados)

- Una vivienda que solo tiene ventanas operables **probablemente no cumple** la NCh 3309:2022, porque la norma pide
  un componente mecánico en la ventilación general y extracción mecánica local en cocina y baño. Que lo confirme quien
  firme el informe.
- La infiltración (C) se mide **sellando** los dispositivos de ventilación (nota de las Tablas 7 y 14). Hermeticidad
  y ventilación se diseñan juntas: más hermeticidad exige ventilación controlada.
- **Planilla de ventilación DITEC "Verificación de ventilación NCh 3309 V3.1"**
  (`planilla-ventilacion-nch3309-v31`, sitio PDA Osorno del MMA; y su versión 2018 en csustentable.minvu.gob.cl,
  `planilla-ventilacion-nch3309-v31-2018`). La planilla misma declara que
  evalúa según la **NCh 3309:2014** y criterios DITEC. La edición vigente en el visor es la **2022**, y el MRT V1.04
  ya actualizó ventilación a esa edición. **No hay planilla MINVU para la NCh 3309:2022** (verificado 2026-11-05); la V3.1 no sirve por sí sola para acreditar con la edición 2022. Si el usuario
  la usa, advertir el desfase de edición y que la exigencia está en la norma (C28).

## 5. Trampas

- Exigir ventilación a **salud** o a **hoteles**: ambos están eximidos.
- Aplicar la NCh 3309 a un colegio: educación va **solo** por NCh 3308.
- Creer que la CEV o el LOSCAT acreditan D: no lo hacen.
- Citar tasas o fórmulas "de memoria": las tasas son de la NCh (©INN). Remitir al visor y, si hace falta un valor
  puntual, citarlo con su cláusula solo si está verificado en el manifiesto.

## Fuentes oficiales a revisar

- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Lámina DITEC Edu-Salud (ene-2026): https://www.minvu.gob.cl/wp-content/uploads/2026/01/Art-4-1-10-OGUC_RES-EDU-SAL_DITEC.pdf
- NCh 3308 y NCh 3309 en el visor: https://normastecnicas.minvu.cl/
- Registro de cambios del MRT (ventilación V1.04): https://www.reglamentaciontermica.cl/registro-de-cambio
