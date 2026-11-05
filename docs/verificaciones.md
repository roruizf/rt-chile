# Verificaciones de fuentes

Registro de los ítems que estaban marcados "NO VERIFICADO" y de cómo se cerraron. Solo metadatos y paráfrasis
propia: aquí no hay texto de normas NCh. Las fuentes están en `sources/manifest.yaml`. Copias privadas en
`sources/private/` (fuera de git).

Última verificación: 2026-11-05.

## 1. Edición oficial de NCh 1079 (¿2019 o 2022?) — **PENDIENTE** (criterio aprobado el 2026-11-05)

- El DS 15 (Art. 4.1.10, num. 1.A) y la Res. Ex. 1802 (num. 1.2) remiten a los planos de zonificación térmica
  "contenidos en la versión oficial de la NCh 1079", **sin año**. Fuentes: `ds15-2024`, `res-ex-1802-2025`.
- La versión oficial es la que un decreto MINVU declara norma oficial. No encontré ese decreto: el D.O. y BCN están
  no consultables en esa revisión, y la búsqueda web no lo muestra.
- Lo que hay hoy:
  - el visor `normastecnicas.minvu.cl` **sirve la NCh 1079:2019** (quinta edición, 23-12-2019). Su catálogo
    dice "2008", pero esa etiqueta está desactualizada: la portada de la copia capturada del visor dice 2019;
  - la copia escaneada `NCh-1079.pdf` es la Of.2008, corregida en 2010;
  - el INN vende una edición **2022** (`ecommerce.inn.cl/nch1079-2022-in81613`), que el visor no sirve.
- Lectura: el hecho de que MINVU publique la 2019 en su visor, junto con las 9 zonas A–I del DS 15, apunta a la
  2019 como la versión que usa la RT. Pero sin el decreto que la declara oficial, la skill dice
  "probablemente 2019 (la que publica MINVU); edición oficial pendiente de decreto".
- **Decisión operativa:** para asignar zona, la skill usa la tabla oficial MINVU de zonas por comuna
  (`ds15-tabla-zonas`, verificada con sha256) y los mapas DITEC, no la NCh 1079. Si alguien pide la edición de la
  NCh 1079, la skill responde "pendiente" y muestra la fecha de esta verificación.
- **Regla aprobada (2026-11-05):** la zona se asigna con la tabla oficial MINVU de comunas. La edición
  se declara "probablemente 2019, oficial pendiente". **Ninguna respuesta de la skill puede depender de la edición
  de la NCh 1079.**
- Para cerrarlo: buscar en el D.O. o en BCN el decreto exento MINVU que declara oficial la NCh 1079 (2019 o 2022).

## 2. Norma de ensayo de elementos opacos — **CERRADO: NCh 851**

- DS 15, num. 1.A y 2.A (vía 2, "Informe de Ensayo"): techumbre, muros perimetrales y piso ventilado se ensayan
  según la NCh 851, en un laboratorio del registro DS 10. Las puertas opacas se ensayan según NCh 3076/1 y NCh 3076/2.
- Vía de cálculo, misma fuente (vía 3, "Memoria de Cálculo"): NCh 853 y NCh 3117 "según corresponda" para los
  opacos, y NCh 3137/1 y /2 para las puertas opacas.
- La NCh 850 no aparece citada en el DS 15.

## 3. Tratamiento de puentes térmicos (¿NCh 3117 o 3136?) — **CERRADO: ninguna de las dos lo regula; lo regulan el DS 15 y la Res. Ex. 1802**

- El DS 15 (num. 1.B) exige que el análisis de **condensación superficial** incluya los puentes térmicos de techos,
  muros y pisos ventilados. También define "puente térmico" en sus definiciones y pide minimizarlo en el
  sobrecimiento con aislante rotulado NCh 2251 (num. 1.A).
- La Res. Ex. 1802 (num. 1.1) baja eso a un método: el cálculo de condensación se hace en al menos dos secciones,
  la de **mayor** y la de **menor** resistencia térmica (puente térmico constructivo). Los puentes térmicos
  **puntuales** que no superen el 10 % de la superficie de la solución pueden exceptuarse del cálculo en esa sección.
- **NCh 3117:** sirve para la transmisión de calor por el terreno (Res. Ex. 1802 num. 4: muros enterrados, pisos
  sobre terreno). No es la norma de puentes térmicos.
- **NCh 3136:** se titula "Puentes térmicos… cálculos detallados" y está en el visor (2008). Ni el DS 15 ni la
  Res. Ex. 1802 la citan, así que no es exigible. A lo más, la skill puede mencionarla como referencia de método
  avanzado, dejando claro que no es obligatoria.

## 4. Res. Ex. 1802: fecha de firma vs. publicación — **firma CERRADA; publicación PENDIENTE de leer**

- **Firma:** la portada del PDF oficial MINVU dice Res. Exenta N° 1802, Santiago, 26-11-2025, con timbre
  "tramitada" del 26-11-2025 (`res-ex-1802-2025`, sha256 en el manifiesto). Es dos días antes de la entrada en vigor
  del DS 15 (28-11-2025).
- **Publicación:** según la búsqueda web, salió en el D.O. el 03-12-2025 (CVE 2735266). No pude leerla porque el host
  del D.O. está bloqueado. Queda como `published` sin confirmar en el manifiesto.
- Efecto práctico: una matriz interna previa daba "26-11-2025" como fecha de la resolución, y eso es correcto como fecha de
  firma. Si hay que citar la publicación, usar la del D.O. una vez confirmada.

## Hallazgos colaterales (pasan a `docs/contradicciones.md`)

- **Etiquetas del catálogo del visor vs. edición servida:** el catálogo del visor muestra años viejos, pero
  sirve ediciones nuevas: NCh 1079 (dice 2008, sirve 2019), 853 (2007 → 2021), 3117 (2008 → 2018), 3137/2
  (2008 → 2018), 3136 (2008 → 2014), 3308 (2013 → 2024) y 3309 (2013 → 2022). Se comprobó con la portada de las
  copias capturadas del visor. Manda la portada. Además, El archivo de trabajo "NCh3137-2_2008" contiene la
  3137/2:2018: está mal rotulado.
- **NCh 853:** la copia de trabajo "NCh853_2014" es la cuarta edición 2014 (licencia INN de una universidad, no
  viene del visor). El D.Ex. 40/2025 deroga el decreto de la Of.2007. Ninguna de las dos (2007 ni 2014) vale para
  permisos regidos por el DS 15: aplica la 2021.
- **NCh 3076/1:** el índice interno decía que no estaba en el visor, pero sí está (2008).
