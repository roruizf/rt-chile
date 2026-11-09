# Cambios

Versionado semántico. Criterios en [docs/mantencion.md](docs/mantencion.md).

## [1.0.1] — 2026-11-09

Correcciones de instalación y documentación tras una prueba de instalación desde cero. Sin cambios en los datos normativos.

### Corregido

- `informe.py` y `checklist.py` con entrada YAML: si falta `pyyaml`, muestran un mensaje en español con qué instalar, en vez de un traceback. El README lo indica en la sección del informe.
- `install.sh`: acepta `-h`/`--help` (muestra el uso y sale sin instalar), rechaza opciones desconocidas con error y avisa antes de reemplazar una instalación existente.
- Dependencias separadas: `requirements.txt` solo con lo que necesita el usuario (`pyyaml`) y `requirements-dev.txt` con lo de desarrollo (pytest, pypdf, pymupdf, rapidocr).
- Misma pregunta de prueba en el README, `docs/instalacion.md` e `install.sh`. Aclarado que los scripts funcionan con Python 3.8+ y que 3.12 es el entorno de desarrollo.
- `SKILL.md`: los archivos temporales se escriben en el directorio de trabajo del usuario, no en `/tmp`.

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
