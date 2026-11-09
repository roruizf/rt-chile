#!/usr/bin/env bash
# Instala la skill rt-chile para Claude Code, Codex y OpenCode.
#   Claude Code: ~/.claude/skills/rt-chile        (también la lee OpenCode)
#   Codex:       ~/.agents/skills/rt-chile        (USER scope; también la lee OpenCode)
# Requisitos de los scripts: Python 3.8+ (solo biblioteca estándar). informe.py y checklist.py con entrada YAML
# requieren pyyaml (pip install -r requirements.txt).
set -euo pipefail

usage() {
  cat <<'USO'
Uso: ./install.sh [opción]

  (sin opción)   copia la skill (recomendado para usuarios)
  --link         enlaza (symlink) al repo: útil para desarrollo, se actualiza con git pull
  --uninstall    elimina la skill instalada
  -h, --help     muestra esta ayuda y sale sin instalar

Destinos: ~/.claude/skills/rt-chile y ~/.agents/skills/rt-chile
Si ya hay una instalación, se reemplaza (se avisa antes).
USO
}

if [ "$#" -gt 1 ]; then
  echo "Error: se esperaba como máximo una opción." >&2; usage >&2; exit 2
fi
case "${1:-}" in
  "")          MODE="copy" ;;
  --link)      MODE="--link" ;;
  --uninstall) MODE="--uninstall" ;;
  -h|--help)   usage; exit 0 ;;
  *)           echo "Error: opción desconocida: $1" >&2; usage >&2; exit 2 ;;
esac

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills/rt-chile"
DESTS=("${HOME}/.claude/skills/rt-chile" "${HOME}/.agents/skills/rt-chile")
[ -f "$SRC/SKILL.md" ] || { echo "No encuentro $SRC/SKILL.md" >&2; exit 1; }
for d in "${DESTS[@]}"; do
  if [ "$MODE" = "--uninstall" ]; then rm -rf "$d"; echo "eliminado: $d"; continue; fi
  mkdir -p "$(dirname "$d")"
  if [ -e "$d" ] || [ -L "$d" ]; then
    echo "aviso: ya existe una instalación en $d; se reemplaza."
  fi
  rm -rf "$d"
  if [ "$MODE" = "--link" ]; then
    ln -s "$SRC" "$d"
  else
    mkdir -p "$d"
    (cd "$SRC" && tar --exclude='tests' --exclude='__pycache__' -cf - .) | (cd "$d" && tar -xf -)
  fi
  echo "instalado: $d"
done
[ "$MODE" = "--uninstall" ] || echo "Listo. Reinicia el agente. Prueba: \"¿Qué zona térmica es Temuco y qué U de muro exige el PDA a una vivienda nueva?\""
