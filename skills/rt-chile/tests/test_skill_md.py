import re
from pathlib import Path

import yaml

SKILL = Path(__file__).resolve().parents[1]


def _parts():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    assert m, "SKILL.md sin frontmatter"
    return yaml.safe_load(m.group(1)), m.group(2)


def test_frontmatter():
    fm, _ = _parts()
    assert fm["name"] == "rt-chile"
    assert 200 < len(fm["description"]) <= 1024


def test_map_files_exist():
    _, body = _parts()
    for ref in set(re.findall(r"`((?:references|data|scripts)/[\w\-.]+\.(?:md|csv|py))`", body)):
        assert (SKILL / ref).exists(), ref


def test_flow_and_closing_rules_present():
    _, body = _parts()
    for k in ("Flujo obligatorio", "Supuestos", "Fuentes oficiales a revisar", "normastecnicas.minvu.cl",
              "FSEV", "Pendiente", "trampas.md"):
        assert k.lower() in body.lower(), k
