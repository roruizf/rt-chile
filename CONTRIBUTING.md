# Cómo evaluar y aportar

Lo más útil es que uses la skill con proyectos reales o con preguntas de tu trabajo, y cuentes dónde falla.

## Cómo evaluarla

1. Instálala ([instrucciones](docs/instalacion.md)) y anota qué agente y modelo usas.
2. Hazle una pregunta que ya sepas responder, o que puedas revisar contra la fuente.
3. Revisa tres cosas: si el valor está bien, si la cita lleva a la fuente correcta y si te dice lo que falta o lo que no sabe.
4. Cuéntalo con la plantilla que corresponda:
   - [Error normativo](../../issues/new?template=error-normativo.yml): un valor, cita o criterio incorrecto.
   - [Evaluación general](../../issues/new?template=evaluacion.yml): para qué la usaste, qué sirvió y qué falta.

## Qué no debes enviar

- **Texto, tablas ni fórmulas de normas NCh.** Son propiedad del INN. Basta con el código de la norma y la cláusula.
- **Datos de clientes o de proyectos identificables.** Quita nombres, direcciones y roles.

## Reglas para aportar contenido

Las reglas completas están en [AGENTS.md](AGENTS.md). Las principales:

- **Fuente o no existe:** cada valor lleva cita y su fuente debe estar en [`sources/manifest.yaml`](sources/manifest.yaml).
- **Prevalencia:** por materia y por uso, según [`docs/como-funciona.md`](docs/como-funciona.md). Las contradicciones se registran en [`docs/contradicciones.md`](docs/contradicciones.md).
- **"Pendiente" es válido:** si la norma no lo fija, no se inventa.
- **Pruebas:** un cambio de contenido debe pasar los tests y las evaluaciones.

```bash
uv venv --python 3.12 && uv pip install --python .venv/bin/python -r requirements.txt -r requirements-dev.txt
.venv/bin/python -m pytest skills/rt-chile/tests -q
.venv/bin/python evals/run.py --agent opencode --model <proveedor/modelo> --judge
```

Para descargar las fuentes públicas que usan algunos tests: `.venv/bin/python scripts/fetch_private.py`. Se guardan en `sources/private/`, que no se versiona. Las evaluaciones consumen cuota de tu proveedor. El detalle de cómo usarlas y calificarlas está en [`docs/mantencion.md`](docs/mantencion.md).
