# rt-chile — reglas para agentes

Repo de la skill pública "Reglamentación Térmica Chile" (OGUC Art. 4.1.10, modificado por DS 15/2024) y su
notebook NotebookLM. Mantenedor: Roberto Ruiz.

## Reglas duras

1. **Copyright NCh:** prohibido versionar o pegar texto, tablas o figuras de normas NCh (© INN), aunque vengan
   del visor MINVU. Se permite: código y título de la norma, edición, alcance en palabras propias, el método
   expresado como algoritmo propio (scripts), y valores numéricos puntuales indispensables con cita
   (norma, cláusula/tabla). Ante la duda: no se incluye y se remite al visor `normastecnicas.minvu.cl`.
   Ver `docs/COPYRIGHT-POLICY.md`.
2. **Fuente o no existe:** toda exigencia, umbral o valor numérico lleva cita (instrumento, artículo/numeral,
   tabla) y debe existir en `sources/manifest.yaml` con estado `verified`. Nada desde memoria.
3. **Prevalencia:** PDA/PPA vigente > Art. 4.1.10 OGUC (DS 15) > resoluciones MINVU > manuales/guías (MRT,
   DITEC) > material secundario. Ante contradicción se gana la fuente superior y se registra en
   `docs/contradicciones.md`.
4. **Pendiente es una respuesta válida:** si una norma no fija algo (p.ej. umbral de demanda de la vía CEV),
   la skill dice "pendiente" con fecha de última verificación. Nunca inventa.
5. **Límites profesionales:** la skill orienta y verifica; no firma, no reemplaza al profesional competente,
   al arquitecto, al laboratorio DS 10 ni al consultor DS 135.
6. **Pruebas antes de declarar éxito:** `python -m pytest skills/rt-chile/tests` y `python evals/run.py` deben
   pasar el umbral (100 % casos `critical`, ≥95 % el resto) antes de cerrar una tarea de contenido.
7. **Python:** usar `uv venv --python 3.12` y `.venv/bin/python`. No tocar el Python del sistema.
8. **Criterio bajo supuestos:** la skill puede calcular y dar su criterio técnico cuando faltan datos, declarando
   los supuestos explícitamente. Toda respuesta sustantiva cierra con un aviso breve de límites y la lista de
   fuentes oficiales a revisar (con link). Cada afirmación normativa indica de dónde viene, sin saturar: una cita
   por exigencia o tabla, no por oración.
9. **Alcance:** v1 = Art. 4.1.10 OGUC + PDA/PPA + LOSCAT + vías + expediente. FSEV, VIT y otros estándares
   (subsidios, CES, CVS) quedan **fuera**: la skill solo detecta que podrían aplicar, lo avisa en una línea y
   remite a la fuente; no mezcla sus tablas con las de la RT. Integrarlos exige decisión explícita del mantenedor.
