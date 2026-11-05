#!/usr/bin/env bash
# Instala la skill rt-chile para Claude Code, Codex y OpenCode.
#   Claude Code: ~/.claude/skills/rt-chile        (también la lee OpenCode)
#   Codex:       ~/.agents/skills/rt-chile        (USER scope; también la lee OpenCode)
# Uso:
#   ./install.sh            copia la skill (recomendado para usuarios)
#   ./install.sh --link     enlaza (symlink) al repo: útil para desarrollo, se actualiza con git pull
#   ./install.sh --uninstall
# Requisitos de los scripts: Python 3.8+ (stdlib). checklist.py con entrada YAML requiere pyyaml.
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills/rt-chile"
DESTS=("${HOME}/.claude/skills/rt-chile" "${HOME}/.agents/skills/rt-chile")
MODE="${1:-copy}"
[ -f "$SRC/SKILL.md" ] || { echo "No encuentro $SRC/SKILL.md" >&2; exit 1; }
for d in "${DESTS[@]}"; do
  if [ "$MODE" = "--uninstall" ]; then rm -rf "$d"; echo "eliminado: $d"; continue; fi
  mkdir -p "$(dirname "$d")"
  rm -rf "$d"
  if [ "$MODE" = "--link" ]; then
    ln -s "$SRC" "$d"
  else
    mkdir -p "$d"
    (cd "$SRC" && tar --exclude='tests' --exclude='__pycache__' -cf - .) | (cd "$d" && tar -xf -)
  fi
  echo "instalado: $d"
done
[ "$MODE" = "--uninstall" ] || echo "Listo. Reinicia el agente. Prueba: \"¿qué zona térmica es Temuco y qué exige el PDA?\""
