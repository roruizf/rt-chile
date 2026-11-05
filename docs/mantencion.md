# Mantención

Cómo mantener la skill vigente y cómo volver a probarla.

## Qué vigilar

La lista viva son las entradas `watch: true` de `sources/manifest.yaml`. Además:

| Fuente | Qué mirar | Dónde | Cuándo |
|---|---|---|---|
| **LOSCAT E15** | Nueva edición: 347 soluciones de la E14 vencen en diciembre de 2026 | https://www.minvu.gob.cl/ditec/ | Mensual; semanal en noviembre y diciembre de 2026 |
| **Umbral de demanda (vía CEV)** | Resolución que lo fije; rige cerca de mayo de 2027 | Diario Oficial y página RT del MINVU | Mensual |
| **PDA Puerto Aysén y Maule** | Publicación o entrada en vigencia | https://ppda.mma.gob.cl/ | Mensual |
| **Decretos de NCh** | Oficialización de ediciones, como la NCh 1079 | Diario Oficial | Trimestral |
| **OGUC y Art. 4.1.10** | Nuevas modificaciones | Diario Oficial | Mensual |

## Si una fuente cambia

1. Descarga la fuente a `sources/private/` (no se versiona) y actualiza `sources/manifest.yaml`: estado, `sha256` y fecha.
2. Si cambian valores, actualiza `data/` y `references/` con su cita, y registra diferencias en `docs/cambios-fuentes.md` y contradicciones en `docs/contradicciones.md`.
3. Corrige los casos en `evals/build_cases.py` y regenéralos con `.venv/bin/python evals/build_cases.py`.
4. Corre las pruebas (siguiente sección).
5. Aumenta la versión en `CHANGELOG.md` y publica la versión nueva.

## Cómo probar

```bash
.venv/bin/python -m pytest skills/rt-chile/tests -q
M=opencode-go/deepseek-v4.1-flash    # o el proveedor y modelo que uses
.venv/bin/python evals/run.py --agent opencode --model $M --judge
```

**Umbral:** 100 % en los casos `critical` y 95 % o más en el resto. Los resultados quedan en `evals/results/` (el `.md` se versiona; el `.jsonl`, no).

**Opciones útiles:**

| Opción | Para qué |
|---|---|
| `--prefix g2`, `--critical-only`, `--cases a,b` | Correr solo una parte |
| `--resume archivo.jsonl` | Continuar una corrida cortada sin repetir lo hecho |
| `--regrade archivo.jsonl` | Recalificar las reglas sin llamar al agente |
| `--regrade archivo.jsonl --rejudge a,b` | Volver a llamar solo al juez en esos casos (`fallos` para todos los fallidos) |
| `--agent notebooklm` | Probar el notebook; requiere `RT_CHILE_NOTEBOOK_ID` |

## Cómo decidir ante un fallo

- Lee la respuesta completa en el `.jsonl`.
- Compárala con `references/` y `data/`: **el juez no ve las fuentes**.
- **Si la respuesta está bien**, el caso está mal: corrige el patrón o la rúbrica.
- **Si la respuesta está mal por la skill**, corrige la skill con su fuente y agrega un caso que lo capture.
- **Si está mal por el modelo**, aunque la skill esté bien, registra el fallo y no relajes el caso.
- Nunca relajes un caso para tapar un error real.

## Cuidados de recursos

- Este arnés corre 2 casos a la vez por defecto, con control de RAM.
- Toda llamada al CLI del juez debe ir **sin hooks** (`NO_HOOKS` en `evals/run.py`). Con algunos plugins, cada llamada dejaba vivo un proceso y agotó la RAM.
- El juez cuesta cerca de 0,01 USD por caso. Revisa el costo en el resumen de cada corrida.

## Versiones

Versionado semántico en `CHANGELOG.md`:

- **Mayor:** cambia la norma de base o la estructura de la skill.
- **Menor:** nueva edición de una fuente, un plan nuevo o una herramienta nueva.
- **Parche:** correcciones de valores, citas o texto.
