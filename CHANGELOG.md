# Cambios

Versionado semántico. Criterios en [docs/mantencion.md](docs/mantencion.md).

## [1.0.0] — 2026-11-06

Primera versión pública. Se publica para recibir evaluaciones de uso real.

### Limitaciones conocidas

- Medida con un solo modelo (OpenCode y DeepSeek V4.1 Flash), por reglas y sin juez automático. Esta versión no se midió con Claude Code ni con Codex.
- La auditoría a mano no salió limpia: de 18 respuestas, 1 tenía un valor incorrecto y 1 una cita incorrecta. Los datos de la skill estaban bien, pero el modelo se equivocó.
- El borrador de informe solo se probó con un proyecto ficticio.
- Hay fuentes pendientes de verificación, declaradas en `docs/verificaciones.md` y `sources/manifest.yaml`.

### Agregado

- Skill para Claude Code, Codex y OpenCode: Art. 4.1.10 OGUC (DS 15/2024), PDA/PPA, LOSCAT E14, vías de acreditación y expediente.
- Datos transcritos de fuentes oficiales: tablas del DS 15, zonas por comuna, clima de la Res. Ex. 1802 y valores de 11 planes.
- Scripts `zona.py`, `pda.py`, `u_check.py`, `ventanas.py` y `checklist.py`.
- `informe.py`: borrador de informe de un proyecto.
- Evaluaciones automáticas (90 casos y 20 preguntas de control), manual, guía de uso, ejemplos y plantillas de feedback.

### Corregido antes de publicar

- Arnés de evals: OpenCode corría dentro del repo y con la copia instalada de la skill. Se invalidaron las mediciones anteriores con ese agente y se volvió a medir.
- Las ventanas "por definir MINVU" de Talca, Valdivia y Osorno ya no se dan como pendientes: los actos MINVU las resuelven como % según el U.
- Título de la NCh 853:2021, según el D.Ex. 40/2025 leído en el Diario Oficial.
