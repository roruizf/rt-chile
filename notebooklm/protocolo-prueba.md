# Protocolo de prueba del notebook

Objetivo: comprobar que el notebook cumple el mismo umbral que la skill antes de compartirlo.

## Requisitos

- Notebook creado con las fuentes de `fuentes.md` y las instrucciones de `instrucciones.md`.
- CLI `notebooklm` con sesión iniciada (`notebooklm login`).
- ID del notebook, visible con `notebooklm list`.

## Pasos

```bash
export RT_CHILE_NOTEBOOK_ID=<id>
# 0. Cada fuente tiene contenido: "ready" no lo prueba. Si sale con código 1, reparar antes de evaluar
.venv/bin/python scripts/build_notebook.py --verificar "$RT_CHILE_NOTEBOOK_ID"
# 1. Las 5 preguntas de validación
.venv/bin/python evals/run.py --agent notebooklm --prefix g2 --judge --workers 1
# 2. Los casos críticos
.venv/bin/python evals/run.py --agent notebooklm --critical-only --judge --workers 1
# 3. Todos, si los anteriores pasan
.venv/bin/python evals/run.py --agent notebooklm --judge --workers 1
```

Usar un solo worker: el servicio limita la cantidad de consultas. Si se corta, continuar con `--resume evals/results/<archivo>.jsonl`.

Cada caso borra la conversación anterior del notebook, para que las preguntas no se influyan entre sí.

## Fuentes de la web y escaneos

- Subir el PDF de `sources/private/`, no el enlace. Una página de LeyChile puede quedar `ready` con un error 403 o con solo parte del decreto, y además desvía la descripción del notebook.
- En un PDF escaneado, `source fulltext` no entrega texto, pero el chat puede leer sus imágenes. `--verificar` mide texto extraído, así que solo acepta los escaneos de la lista `SOLO_IMAGEN`, comprobados con preguntas contra `data/`. Un escaneo nuevo falla hasta hacer esa misma prueba. No se les sube OCR, porque puede alterar cifras.

## Qué no aplica en el notebook

El notebook no corre scripts. Por eso, los casos `informe-01` y los que exijan un cálculo se evalúan por su razonamiento y por si declara ese límite, no por el formato del informe. Registrar estas diferencias en el resultado.

## Cómo evaluar el éxito

| Criterio | Umbral |
|---|---|
| Casos `critical` | 100 % |
| Resto | 95 % o más |
| Respuestas revisadas a mano contra `data/` (muestra al azar) | 10, sin valores incorrectos |
| Texto de normas NCh en fuentes o respuestas | Ninguno |

Para cada fallo, aplicar el criterio de `docs/mantencion.md`. Si la causa es una fuente mal leída, reforzar `tablas-ds15.md` o `tablas-pda.md` o las instrucciones, y volver a probar.

## Registro

Dejar el resultado en `evals/results/`. El notebook se comparte en modo lectura solo después de cumplir estos criterios.
