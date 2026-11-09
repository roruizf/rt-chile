# rt-chile: Reglamentación Térmica de Chile para tu agente de IA

Una skill abierta para revisar y desarrollar proyectos según el **Art. 4.1.10 de la OGUC** (modificado por el DS 15/2024, vigente desde el 28-11-2025) y los **planes de descontaminación (PDA/PPA)**. Funciona en **Claude Code, Codex y OpenCode**.

Le preguntas por un proyecto y responde qué exigencias aplican, de dónde sale cada valor, cómo se acredita y quién firma cada documento.

> [!WARNING]
> **Es una herramienta de apoyo y puede equivocarse.** Verifica cada valor en la fuente oficial antes de usarlo. No reemplaza al profesional competente, al arquitecto, al laboratorio DS 10, al consultor DS 135 ni a la DOM, y no firma documentos.

## Qué hace

- **Zona térmica por comuna**, incluidas las comunas multizona por altitud o meridiano.
- **Exigencias A–D:** envolvente (U, Rt, R100, ventanas, sobrecimientos), condensación, infiltración y permeabilidad, y ventilación, según el uso: vivienda, hotel, educación o salud.
- **PDA/PPA:** 11 planes con capítulo térmico y los actos MINVU que los completan. En vivienda, manda el plan en lo que regula, con nota del valor del 4.1.10.
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

Pídeselo al agente o genéralo tú con los datos del proyecto en un archivo YAML ([formato](skills/rt-chile/examples/proyecto-ejemplo.yaml)). Para leer YAML, `informe.py` necesita `pyyaml`; el resto de los scripts usa solo la biblioteca estándar de Python 3.8 o superior:

```bash
pip install -r requirements.txt   # instala pyyaml
python skills/rt-chile/scripts/informe.py skills/rt-chile/examples/proyecto-ejemplo.yaml --salida informe.md
```

Entrega un borrador con el estado de cada verificación, los supuestos, lo que falta y quién elabora cada documento. **No declara que el proyecto cumpla** ni reemplaza una memoria de cálculo. Las conductividades las entregas tú, con su fuente.

## Límites que debes conocer

- **Las normas NCh son propiedad del INN.** La skill no reproduce su texto, tablas ni fórmulas. Se consultan en el [visor oficial del MINVU](https://normastecnicas.minvu.cl/).
- **Los modelos de IA pueden equivocarse aunque la skill tenga el dato correcto.** En las pruebas ocurrió, como se explica abajo.
- **La vigencia importa.** La mayoría de las soluciones del LOSCAT E14 vence en diciembre de 2026. Revisa la ficha a la fecha de tu permiso.
- **El borrador de informe solo se probó con un proyecto ficticio.** Revisa con especial cuidado lo que genere con un proyecto real.
- **Hay temas pendientes o fuera de alcance:**
  - Pendientes: el umbral de la vía CEV por demanda, la edición oficial de varias NCh y algunas brechas de la tabla de zonas.
  - Fuera de alcance: FSEV, VIT, CES y CVS. La skill los detecta y deriva a su fuente.

## Cómo se probó

Medición del 2026-11-06, versión `043d4cd34839`, con OpenCode y DeepSeek V4.1 Flash. Se califica por reglas, sin juez automático. Umbral: 100 % en los casos críticos y 95 % o más en el resto.

| Prueba | Resultado | Evidencia |
|---|---|---|
| 90 casos | Críticos 31/31, resto 59/59 | [resultado](evals/results/2026-11-06_0649_opencode_regrade.md) |
| 20 preguntas de control, fuera de esos casos | 20/20 | [resultado](evals/results/2026-11-06_0639_opencode_control.md) |
| Auditoría a mano de 18 respuestas al azar | 16 sin errores; 1 valor y 1 cita incorrectos | [casos](evals/results/auditoria-2026-11-06_0649_opencode.md), [control](evals/results/auditoria-2026-11-06_0639_opencode_control.md) |

En la primera calificación, los casos críticos dieron 29/31. Esas dos respuestas estaban bien y fallaba su patrón, así que se corrigió el patrón y se recalificó sin volver a preguntar al modelo.

**Lo que estas cifras no garantizan.** Los patrones no detectan todos los errores. En la auditoría, una respuesta transcribió mal una fila de una tabla de ventanas, y otra citó NCh 853 en vez de NCh 851. No venían de la skill: el primero no se repitió en 3 intentos, y el segundo reapareció en 1 de 3. La versión actual no se midió con Claude Code ni con Codex. Por eso cada respuesta termina pidiendo verificar en la fuente oficial.

## Evalúala y cuéntame

Es la primera versión pública. Busco que la uses en proyectos reales y me digas dónde falla:

- [Reportar un error normativo](../../issues/new?template=error-normativo.yml): un valor, cita o criterio incorrecto.
- [Enviar tu evaluación](../../issues/new?template=evaluacion.yml): para qué la usaste y qué le falta.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar. No incluyas datos de clientes ni texto de normas NCh.

## Organización del repo

Para partir de cero, lee el [manual](docs/manual.md): cómo usar la skill, qué es la RT y cómo se construyó. El detalle de qué fuente manda en cada materia está en [`docs/como-funciona.md`](docs/como-funciona.md).

```text
skills/rt-chile/    La skill: SKILL.md, references/, data/, scripts/, examples/
evals/              Casos de prueba, arnés y resultados
sources/            Manifiesto de fuentes con su estado de verificación
docs/               Cómo funciona y qué manda sobre qué, guías, verificaciones, contradicciones y copyright
notebooklm/         Material para el notebook de NotebookLM
```

## Licencia

- Scripts y código: [MIT](LICENSE).
- Contenido propio (referencias, resúmenes, casos, documentación): [CC BY-NC 4.0](LICENSE-CONTENT.txt).
- Los actos públicos citados pertenecen a sus emisores, y las normas NCh, al INN: no se incluyen ni se licencian aquí.

Creado por Roberto Ruiz. Proyecto independiente, sin relación oficial con el MINVU ni el INN.
