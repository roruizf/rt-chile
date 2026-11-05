# Instalación de la skill rt-chile

Un solo comando, desde la raíz del repo:

```bash
./install.sh
```

Copia `skills/rt-chile/` (sin los tests) a:

| Agente | Carpeta | Fuente |
|---|---|---|
| Claude Code | `~/.claude/skills/rt-chile/` | carpeta estándar de skills de usuario de Claude Code |
| Codex CLI/IDE | `~/.agents/skills/rt-chile/` | scope `USER` en https://developers.openai.com/codex/skills (verificado 2026-11-05) |
| OpenCode | lee las dos anteriores (`~/.claude/skills` y `~/.agents/skills`) | https://opencode.ai/docs/skills (verificado 2026-11-05) |

Para desarrollo, `./install.sh --link` crea symlinks al repo (se actualiza con `git pull`). Para desinstalar:
`./install.sh --uninstall`.

**Por proyecto** (sin instalar globalmente): copiar `skills/rt-chile/` a `.claude/skills/rt-chile/` (Claude Code y
OpenCode) o a `.agents/skills/rt-chile/` (Codex y OpenCode) del repositorio de trabajo.

**Requisitos:** Python 3.8 o superior para los scripts, que usan solo la biblioteca estándar. Para `checklist.py` e
`informe.py` con entrada YAML se necesita `pyyaml`; con JSON no se necesita.

**Uso:** [guía con 3 casos completos](guia-de-uso.md) y [ejemplos de preguntas y respuestas](ejemplos.md).

**Prueba rápida** después de reiniciar el agente: "¿Qué zona térmica es Mostazal a 600 msnm, aplica el PDA y qué U
de muro se exige?"
