# rt-chile: Reglamentación Térmica de Chile para tu agente de IA

Una skill abierta para revisar y desarrollar proyectos según el **Art. 4.1.10 de la OGUC** (modificado por el DS 15/2024, vigente desde el 28-11-2025) y los **planes de descontaminación (PDA/PPA)**. Funciona en **Claude Code, Codex y OpenCode**.

Le preguntas por un proyecto y responde qué exigencias aplican, de dónde sale cada valor, cómo se acredita y quién firma cada documento.

> [!WARNING]
> **Es una herramienta de apoyo y puede equivocarse.** Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza al profesional competente, al arquitecto, al laboratorio DS 10, al consultor DS 135 ni a la DOM, y no firma documentos.

## Qué hace

- **Zona térmica por comuna**, incluidas las comunas multizona por altitud o meridiano.
- **Exigencias A–D:** envolvente (U, Rt, R100, ventanas, sobrecimientos), condensación, infiltración y permeabilidad, y ventilación, según el uso: vivienda, hotel, educación o salud.
- **PDA/PPA:** 11 planes con capítulo térmico y los actos MINVU que los completan. En vivienda, las tablas del plan prevalecen.
- **Vías de acreditación:** LOSCAT con vigencia por fecha, ensayo DS 10, memoria de cálculo, R100 y vía por demanda (umbral aún pendiente).
- **Expediente:** qué va en el permiso y qué en la recepción, y quién elabora y firma cada documento.
- **Cálculos de apoyo:** U de un complejo multicapa, % de ventanas o Upvm y checklist del proyecto.
- **Borrador de informe por proyecto:** reúne todo lo anterior en un documento editable.

Cada cifra viene de una tabla transcrita de la fuente oficial y verificada. Cuando la norma no fija algo, responde **"pendiente"** en vez de inventar.

## Instalación

```bash
git clone https://github.com/roruizf/rt-chile.git
cd rt-chile
./install.sh
```

Reinicia tu agente y prueba: *"¿Qué zona térmica es Temuco y qué U de muro exige el PDA a una vivienda nueva?"*

Más opciones, como instalar en un solo proyecto o desinstalar, en [docs/instalacion.md](docs/instalacion.md).

## Cómo usarla

Pregunta en lenguaje natural e incluye lo que tengas: uso, comuna, altitud, fecha de ingreso y capas del muro. Si falta un dato, lo pide o responde por escenarios con supuestos declarados.

| Pregunta | Qué obtienes |
|---|---|
| *"Hotel en Valparaíso: ¿necesito ensayo de infiltración y memoria de condensación?"* | Exigencias del hotel y sus exenciones, con cita |
| *"Muro de yeso-cartón, OSB, EPS 40 mm y ladrillo: ¿cumple en zona D?"* | U calculado con supuestos declarados y comparación con la tabla |
| *"¿Qué documentos van en el permiso y en la recepción para este colegio?"* | Lista por etapa, con quién elabora y firma |
| *"Prepárame un informe térmico de este proyecto"* | Borrador editable con el estado de cada verificación |

- [Guía de uso con 3 casos completos](docs/guia-de-uso.md)
- [Ejemplos de preguntas y respuestas](docs/ejemplos.md)

### Informe de un proyecto

Pídeselo al agente o genéralo tú con los datos del proyecto en un archivo YAML ([formato](skills/rt-chile/examples/proyecto-ejemplo.yaml)):

```bash
python skills/rt-chile/scripts/informe.py skills/rt-chile/examples/proyecto-ejemplo.yaml --salida informe.md
```

Entrega un borrador con el estado de cada verificación, los supuestos, lo que falta y quién elabora cada documento. **No declara que el proyecto cumpla** ni reemplaza una memoria de cálculo. Las conductividades las entregas tú, con su fuente.

## Límites que debes conocer

- **Las normas NCh son propiedad del INN.** La skill no reproduce su texto, tablas ni fórmulas. Se consultan en el [visor oficial del MINVU](https://normastecnicas.minvu.cl/).
- **Los modelos de IA pueden equivocarse aunque la skill tenga el dato correcto.** En las pruebas ocurrió, como se explica abajo.
- **La vigencia importa.** La mayoría de las soluciones del LOSCAT E14 vence en diciembre de 2026. Revisa la ficha a la fecha de tu permiso.
- **Hay temas pendientes o fuera de alcance:**
  - Pendientes: el umbral de la vía CEV por demanda, la edición oficial de varias NCh y algunas brechas de la tabla de zonas.
  - Fuera de alcance: FSEV, VIT, CES y CVS. La skill los detecta y deriva a su fuente.

## Cómo se probó

La skill se evalúa con casos calificados por reglas y por un juez automático. Umbral: 100 % en los casos críticos y 95 % o más en el resto.

| Agente | Críticos | Resto | Evidencia |
|---|---|---|---|
| OpenCode + DeepSeek V4.1 Flash | 27/27 | 58/59 (86 casos) | [resultado](evals/results/2026-11-05_1143.md) |
| Codex | 5/5 en las preguntas de validación | no corrido | [resultado](evals/results/2026-11-05_1014_regrade.md) |

El caso que falló respondía el puntaje de una certificación fuera de alcance. Se reforzó esa regla y [los 3 casos de ese tema pasan](evals/results/2026-11-05_1222.md).

**Lo que estas cifras no garantizan.** El juez automático no ve las fuentes, así que además se auditaron a mano 10 respuestas aprobadas, elegidas al azar. [El resultado](evals/results/auditoria-2026-11-05_1038.md), en una corrida previa: las cifras y citas estaban bien, pero **2 de las 10 incluían una afirmación secundaria falsa** que el juez no detectó. Una aprobación del 100 % no significa que cada frase sea correcta. Por eso importa verificar cada respuesta, y por eso tu evaluación con proyectos reales es tan útil.

## Evalúala y cuéntame

Busco que la uses en proyectos reales y me digas dónde falla:

- [Reportar un error normativo](../../issues/new?template=error-normativo.yml): un valor, cita o criterio incorrecto.
- [Enviar tu evaluación](../../issues/new?template=evaluacion.yml): para qué la usaste y qué le falta.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar. No incluyas datos de clientes ni texto de normas NCh.

## Organización del repo

```text
skills/rt-chile/    La skill: SKILL.md, references/, data/, scripts/, examples/
evals/              Casos de prueba, arnés y resultados
sources/            Manifiesto de fuentes con su estado de verificación
docs/               Guías, verificaciones, contradicciones entre fuentes y política de copyright
notebooklm/         Material para el notebook de NotebookLM
```

## Licencia

- Scripts y código: [MIT](LICENSE).
- Contenido propio (referencias, resúmenes, casos, documentación): [CC BY-NC 4.0](LICENSE-CONTENT.txt).
- Los actos públicos citados pertenecen a sus emisores, y las normas NCh, al INN: no se incluyen ni se licencian aquí.

Creado por Roberto Ruiz. Proyecto independiente, sin relación oficial con el MINVU ni el INN.
