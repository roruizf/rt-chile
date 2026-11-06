# Manual de rt-chile

Este manual explica tres cosas: cómo usar la skill, qué es la Reglamentación Térmica (RT) de Chile y cómo se construyó la herramienta. No necesitas saber de la norma ni de agentes de IA para empezar.

> [!WARNING]
> rt-chile orienta y puede equivocarse. Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza al profesional competente, al arquitecto del proyecto, a los laboratorios y consultores registrados ni al pronunciamiento de la Dirección de Obras Municipales (DOM).

| Si quieres... | Ve a |
|---|---|
| Usarla ahora | [Parte 1](#parte-1-usar-la-skill) |
| Entender la norma | [Parte 2](#parte-2-entender-la-rt) |
| Saber por qué confiar en ella, o cuestionarla | [Parte 3](#parte-3-cómo-se-construyó) |
| Aclarar un término | [Glosario](#glosario) |
| Resolver una duda común | [Preguntas frecuentes](#preguntas-frecuentes) |

## Parte 1: usar la skill

### Qué es

Una *skill* es un paquete de instrucciones, datos y scripts que un agente de IA carga para hacer una tarea. Esta responde sobre el Art. 4.1.10 de la OGUC y los planes de descontaminación: qué exigencias aplican, de dónde sale cada valor, cómo se acredita y quién firma.

Sirve para revisar un proyecto, preparar un expediente o aprender. No sirve para firmar, ni para decidir si la DOM aceptará algo.

### Instalar

Sigue [`instalacion.md`](instalacion.md). Funciona con Claude Code, Codex y OpenCode.

### Preguntar bien

Una buena pregunta incluye lo que tengas:

| Dato | Por qué importa |
|---|---|
| Uso: vivienda, hotel, educación o salud | Cambia las tablas y las exenciones |
| Comuna | Da la zona, la provincia y el plan |
| Altitud o meridiano | Solo en comunas con más de una zona |
| Fecha de ingreso del permiso | Define la norma, la etapa del plan y la vigencia del LOSCAT |
| Capas, U de ventanas y superficies | Permiten calcular |

Si falta un dato, la skill lo pide o responde con supuestos. Ejemplos completos en [`guia-de-uso.md`](guia-de-uso.md) y [`ejemplos.md`](ejemplos.md).

### Leer una respuesta

Una respuesta sigue este orden:

1. **Respuesta directa.**
2. **Datos del caso y supuestos.** Revísalos primero: un supuesto equivocado invalida todo lo demás.
3. **Exigencias y su cita.** Con plan, incluye el valor del plan y, como nota, el del 4.1.10.
4. **Cómo acreditar y quién firma.**
5. **Pendientes y advertencias.**
6. **Límites y fuentes oficiales.**

Tres palabras tienen un sentido preciso:

- **"Pendiente":** la norma o las fuentes no lo fijan. No es un error de la herramienta.
- **"Supuesto":** un dato que la skill asumió. Debes confirmarlo.
- **"Criterio declarado":** una decisión de esta herramienta que la norma no escribe. Puedes discrepar: están listadas en [`como-funciona.md`](como-funciona.md).

### Comprobar un valor

Copia la cita de la respuesta y ábrela en la fuente oficial de la lista de cierre. Las normas NCh solo se consultan en el [visor del MINVU](https://normastecnicas.minvu.cl/), porque su texto no puede reproducirse aquí.

### Herramientas incluidas

Puedes pedírselas al agente o ejecutarlas tú:

| Script en `skills/rt-chile/scripts/` | Qué hace |
|---|---|
| `zona.py` | Comuna a zona, provincia, plan y clima |
| `pda.py` | Exigencias de un plan y comparación con el 4.1.10 |
| `u_check.py` | U de un complejo multicapa frente a la exigencia |
| `ventanas.py` | % de ventanas y Upvm |
| `checklist.py` | Exigencias y documentos de un proyecto |
| `informe.py` | Borrador de informe del proyecto, que no declara cumplimiento |

### Skill o notebook

También existe un notebook de NotebookLM con las mismas fuentes, pensado para quien no usa un agente. Todavía no está disponible para el público.

| | Skill | Notebook |
|---|---|---|
| Necesita | Un agente de IA instalado | Solo un navegador |
| Cálculos | Corre scripts | Razona, pero no corre scripts: revisa más sus cifras |
| Datos | Los consulta filtrados por plan | Los busca en sus fuentes |
| Informe de proyecto | Sí | No |
| Mejor para | Revisar y calcular un proyecto | Consultar y aprender |

### Si encuentras un error

[Repórtalo](../CONTRIBUTING.md) con la cita de la fuente. No incluyas datos de clientes ni texto de normas NCh.

## Parte 2: entender la RT

### Para qué existe

La RT fija el desempeño térmico mínimo de la envolvente: el "cascarón" que separa el interior del exterior. Busca menos consumo de energía y de leña, mejor calidad de aire interior y menos patologías por humedad. Esos objetivos están en los considerandos del DS 15/2024.

### Dónde está escrita

| Instrumento | Qué es | Rol |
|---|---|---|
| **OGUC, Art. 4.1.10** | Artículo de la Ordenanza General de Urbanismo y Construcciones, modificado por el DS 15/2024 | La regla general |
| **Planes (PDA y PPA)** | Decretos del Ministerio del Medio Ambiente para zonas contaminadas | En vivienda, mandan en lo que regulan |
| **Resoluciones MINVU** | Actos que completan la norma, como la Res. Ex. 1802 | Condiciones de cálculo y detalles de los planes |
| **LOSCAT** | Listado oficial de soluciones constructivas | Una forma de acreditar |
| **Normas NCh** | Métodos de cálculo y ensayo, del INN | Definen cómo se calcula o se ensaya |
| **Manuales y láminas** | Guías del MINVU y del Instituto de la Construcción | Ayudan a interpretar; no mandan |

El DS 15 se publicó el 27-05-2024 y su Art. 4.1.10 rige desde el **28-11-2025**. La DOM evalúa con las normas vigentes a la fecha de ingreso del permiso (OGUC Art. 1.1.3).

### A qué edificios aplica

| Uso | A: envolvente | B: condensación | C: infiltración | D: ventilación |
|---|---|---|---|---|
| Vivienda | Sí | Sí | Sí | Sí |
| Hotel | Sí | Exento | Exento | Exento |
| Educación | Sí | Sí | Sí | Solo NCh 3308 |
| Salud | Sí | Sí | Sí | Eximida |

Cementerios, crematorios y el resto del equipamiento no están alcanzados.

### Las cuatro exigencias

**A. Envolvente: cuánto calor deja pasar.** Se limita la transmitancia U de techumbre, muros, piso ventilado y puertas opacas. También se regula la superficie o el U de las ventanas y el aislante del sobrecimiento.

**B. Condensación: dónde se moja.** Hay que verificar que no se forme agua en la superficie interior ni dentro de la solución. Se acredita solo con memoria de cálculo (NCh 1973 y Res. Ex. 1802), con el clima de cada comuna.

**C. Infiltración: por dónde se escapa el aire.** Son dos cosas distintas. La envolvente se mide con obra terminada (NCh 3295) y depende de la provincia. Las puertas y ventanas tienen una clase de permeabilidad según la zona.

**D. Ventilación: cómo se renueva el aire.** Una envolvente más hermética necesita ventilación controlada. Se acredita con un informe de cumplimiento de la tasa (NCh 3308 y 3309).

### Zona térmica

Chile se divide en nueve zonas, de la A a la I, asignadas por comuna y a veces por altitud o meridiano. Una exigencia más alta no siempre corresponde a una letra más avanzada: el muro de la zona I es menos exigente que el de la H.

U máximo en vivienda, sin plan (DS 15, Tabla 1, W/m²K):

| Zona | Techumbre | Muro | Piso ventilado | Puerta opaca |
|---|---:|---:|---:|---:|
| A | 0,84 | 2,10 | 3,60 | — |
| B | 0,47 | 0,80 | 0,70 | 1,70 |
| C | 0,47 | 0,80 | 0,87 | 1,70 |
| D | 0,38 | 0,80 | 0,60 | 1,70 |
| E | 0,33 | 0,60 | 0,60 | 1,70 |
| F | 0,28 | 0,45 | 0,50 | 1,70 |
| G | 0,28 | 0,40 | 0,39 | 1,70 |
| H | 0,25 | 0,30 | 0,32 | 1,70 |
| I | 0,25 | 0,35 | 0,32 | 1,70 |

Educación y salud usan otras tablas (10 para opacos y 12 para ventanas). Todas las tablas están en `skills/rt-chile/data/` y en el DS 15; también puedes pedírselas a la skill.

### Planes de descontaminación

Si la vivienda está en un área con plan vigente, el Art. 4.1.10 inc. 2° dice que "deberá estarse, en materia de exigencias de acondicionamiento térmico, a lo dispuesto en dicho Plan". Tres ideas que suelen confundirse:

- **No se trata de que el plan sea "más estricto".** El texto no compara. En los valores comparados de U, R100, sobrecimiento e infiltración, casi todos son iguales al 4.1.10.
- **Las diferencias suelen estar en otros puntos:** muestras de ensayo, sellos, humedad para condensación, % de ventanas y ventilación. Los 11 planes con envolvente exigen extracción mecánica en baños y cocina con higrostato.
- **Solo aplica a vivienda.** Un hotel o un colegio en Temuco siguen el 4.1.10.

Cuando el 4.1.10 es más estricto o hay ambigüedad, esta herramienta muestra ambos valores y recomienda el más estricto o consultar a la DOM. Es un criterio propio, explicado en [`como-funciona.md`](como-funciona.md).

### Cómo se acredita

| Vía | Sirve para | Quién |
|---|---|---|
| Aislante rotulado (R100, NCh 2251) | Opacos y sobrecimiento | Arquitecto, en las EETT |
| Solución LOSCAT vigente | Opacos, puertas, ventanas, permeabilidad | Arquitecto la especifica |
| Ensayo de laboratorio, 10 años o menos para A | U y permeabilidad | Laboratorio del registro DS 10 |
| Memoria de cálculo | U y, como única vía, condensación | Profesional competente o especialista; el arquitecto la suscribe |
| Ensayo en terreno (NCh 3295) | Infiltración de la envolvente | Arquitecto, consultor DS 135 o laboratorio DS 10 |
| Informe de tasa | Ventilación | Profesional competente o especialista; el arquitecto lo suscribe |
| Vía por demanda de energía | Solo A, solo vivienda | Evaluador energético. **Umbral pendiente** |

Se pueden combinar vías entre elementos. En vivienda con plan, mandan las vías del plan en lo que regula.

### Permiso y recepción

- **Permiso de edificación (OGUC Art. 5.1.6 N° 11):** EETT con las partidas térmicas, memorias, informes y soluciones adoptadas.
- **Recepción definitiva (OGUC Art. 5.2.6 N° 7):** antecedentes según el destino y el ensayo de infiltración en terreno, que solo existe con la obra terminada.

Detalle por documento en `skills/rt-chile/references/roles-firmas-expediente.md`.

### Un ejemplo de punta a punta

Vivienda nueva en Temuco, con permiso a ingresar en noviembre de 2026:

1. **Uso:** vivienda. Aplican A, B, C y D.
2. **Norma:** rige el DS 15, porque ingresa después del 28-11-2025.
3. **Zona:** F.
4. **Plan:** PDA de Temuco y Padre Las Casas, DS 8/2023, que manda en lo que regula.
5. **Envolvente:** muro U ≤ 0,45, techumbre 0,28 y piso ventilado 0,50 (Art. 27, Tabla N° 10). El 4.1.10 da los mismos valores en zona F, como nota informativa.
6. **Particularidades del plan:** ventana U ≤ 3,20 y % por orientación de la Res. Ex. 9868; muestra de infiltración propia (Tabla N° 14); sellos como alternativa; ventilación con extracción mecánica en baños y cocina; calefacción sin leña (Art. 15).
7. **Expediente:** memoria de condensación e informe de ventilación en el permiso; ensayo de infiltración, si se usa esa vía, en la recepción.

Antes de usarlo, confirma en el decreto cada cita y la vigencia de la ficha LOSCAT, porque la mayoría de las soluciones de la edición 14 vence en diciembre de 2026.

## Parte 3: cómo se construyó

### Principios

| Principio | Qué significa |
|---|---|
| Fuente o no existe | Toda exigencia lleva cita a una fuente verificada |
| Pendiente es una respuesta | Si la norma no fija algo, se dice |
| Sin texto de NCh | Solo código, título, alcance en palabras propias y método como algoritmo propio |
| Criterios a la vista | Lo que la norma no escribe se marca como criterio |
| Límites profesionales | Orienta; no firma ni reemplaza |

### Método

1. **Fuentes.** Se inventariaron en `sources/manifest.yaml` con su estado: `verified` (leída, con sha256), `located` (identificada) o `pending`. Las copias de trabajo no se publican.
2. **Datos.** Muchas tablas son imágenes en los PDF oficiales, así que se transcribieron a `data/` y se contrastaron con OCR independiente y lectura de imágenes. En `data/README.md` está la procedencia de cada archivo.
3. **Contradicciones.** Cada discrepancia entre fuentes se registró y resolvió, o quedó abierta, en [`contradicciones.md`](contradicciones.md).
4. **Conocimiento.** Las referencias de `skills/rt-chile/references/` explican cada tema en palabras propias, con cita.
5. **Reglas y scripts.** `SKILL.md` fija el flujo obligatorio, y los scripts calculan desde `data/` para no depender de la memoria del modelo.
6. **Evaluación.** Casos de prueba con respuesta esperada, calificados por reglas y a veces por un juez automático, con umbral de 100 % en críticos y 95 % en el resto. Una muestra se audita a mano contra `data/`.
7. **Corrección.** Un error se corrige en su fuente, con cita, y se agrega un caso que lo detecte. Un caso solo se cambia si la respuesta estaba bien y el caso mal.

La herramienta se desarrolló con apoyo de agentes de IA, con decisiones y revisión del mantenedor.

### Por qué un porcentaje no basta

Los errores más importantes no los encontró el puntaje, sino revisar contra la fuente. Tres ejemplos de este proyecto:

- **Valor equivocado que pasaba la prueba:** una respuesta usó una resistencia superficial incorrecta y aprobó porque otro número coincidía con el patrón.
- **Fuente "lista" y vacía:** varias páginas web quedaron marcadas como listas en el notebook, pero tenían un error o solo parte del decreto. Solo se detectó comparando con el PDF.
- **Se medía otra versión:** el agente de prueba cargaba una copia antigua instalada en el equipo, en vez de la versión revisada. Parecía que una corrección no funcionaba. Se detectó registrando cada archivo que leía, y ahora el arnés se detiene si las copias difieren.
- **Dato ausente:** la exigencia de extracción mecánica de varios planes faltaba en los datos. Apareció al leer los decretos para auditar el marco.

Por eso las evaluaciones son necesarias, pero no prueban que todo esté correcto. Los modelos también pueden responder distinto a la misma pregunta.

### Cómo auditarla

| Pregunta | Dónde mirar |
|---|---|
| ¿Qué es norma y qué es criterio? | [`como-funciona.md`](como-funciona.md), hipótesis H01 a H13 |
| ¿De dónde sale este dato? | `sources/manifest.yaml` y `skills/rt-chile/data/README.md` |
| ¿Qué fuentes se contradicen? | [`contradicciones.md`](contradicciones.md) |
| ¿Qué quedó sin confirmar? | [`verificaciones.md`](verificaciones.md) |
| ¿Qué cambió entre ediciones? | [`cambios-fuentes.md`](cambios-fuentes.md) |
| ¿Cómo se prueba y se mantiene? | [`mantencion.md`](mantencion.md) y `evals/results/` |
| ¿Qué se puede citar de las NCh? | [`COPYRIGHT-POLICY.md`](COPYRIGHT-POLICY.md) |

## Glosario

| Término | Significado |
|---|---|
| **ach** | Renovaciones de aire por hora. En la RT se mide a 50 Pa |
| **CEV** | Calificación Energética de Viviendas. Es otro régimen; no acredita el 4.1.10 |
| **Consultor DS 135** | Profesional inscrito en el Registro de Consultores del MINVU |
| **DITEC** | División Técnica del MINVU |
| **DOM** | Dirección de Obras Municipales: revisa el permiso y la recepción |
| **DS 15** | Decreto de 2024 que reemplazó el Art. 4.1.10 de la OGUC |
| **EETT** | Especificaciones técnicas del proyecto |
| **Envolvente térmica** | Elementos que separan el interior del exterior o de espacios no acondicionados |
| **FSEV, VIT, CES, CVS** | Otros programas y estándares. Fuera de alcance: la skill los detecta y deriva |
| **HR** | Humedad relativa |
| **Laboratorio DS 10** | Laboratorio inscrito en el registro oficial del MINVU |
| **LOSCAT** | Listado Oficial de Soluciones Constructivas para Acondicionamiento Térmico |
| **MRT** | Manual de Reglamentación Térmica |
| **NCh** | Norma Chilena, del INN |
| **OGT** | Límite global de ventanas que se usa si los muros expuestos son menos del 60 % |
| **OGUC** | Ordenanza General de Urbanismo y Construcciones |
| **PDA / PPA** | Plan de Descontaminación / de Prevención Atmosférica |
| **Permeabilidad al aire** | Clase de puertas y ventanas, medida a 100 Pa |
| **Profesional competente** | Arquitecto, ingeniero civil, ingeniero constructor o constructor civil, en su ámbito |
| **Puente térmico** | Zona de la envolvente con mayor paso de calor, como un pilar |
| **R100** | Resistencia rotulada de un aislante: Rt × 100 |
| **Rsi / Rse** | Resistencias superficiales interior y exterior |
| **Rt** | Resistencia térmica total, en m²K/W. Es el inverso de U |
| **U** | Transmitancia térmica, en W/m²K. Menor U significa mejor aislación |
| **Upvm** | U ponderado de muro y ventana, en vivienda de zonas B a I |
| **Zona saturada** | Área declarada por superar una norma de calidad del aire. Define dónde rige un plan |

## Preguntas frecuentes

**¿Si cumplo la CEV, cumplo la RT?** No. Son regímenes distintos. La vía por demanda del 4.1.10 cubre solo A, solo en vivienda, y su umbral sigue pendiente.

**¿Si uso una solución LOSCAT, me ahorro la memoria de condensación?** No. LOSCAT acredita el elemento en A o en permeabilidad. Condensación se acredita con memoria.

**¿Puedo usar una ficha de una edición antigua?** Debe estar vigente. Revisa su fecha a la fecha de tu trámite.

**¿Dónde hay PDA me olvido del 4.1.10?** No del todo. Manda el plan en lo que regula, pero conviene conocer el 4.1.10, especialmente si es más estricto. Lo que el plan no regula se revisa con el 4.1.10, según el criterio de esta herramienta.

**¿Hoteles y salud tienen las mismas exenciones?** No. Hotel está exento de B, C y D. Salud está eximida solo de D.

**¿Puede decirme el espesor de aislante?** Solo como cálculo con supuestos. U depende de todas las capas y sus conductividades, y debes confirmar esos datos.

**¿Por qué no me muestra la tabla de una NCh?** Por derechos de autor del INN. Consúltala en el [visor del MINVU](https://normastecnicas.minvu.cl/).

**¿Qué hago si la skill y la DOM no coinciden?** Pide el fundamento y revisa la fuente oficial. La DOM decide la admisibilidad. Si la skill estaba mal, repórtalo.

**¿La herramienta firma o certifica?** No. El informe es un borrador y no declara cumplimiento.
