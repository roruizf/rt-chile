"""Consistencia entre references/ y el manifiesto."""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
REFS = ROOT / "skills" / "rt-chile" / "references"


def _nch():
    src = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]
    return [s for s in src if s["license"] == "inn-copyright"]


def test_normas_nch_covers_all_manifest_nch():
    text = (REFS / "normas-nch.md").read_text(encoding="utf-8")
    rows = set(re.findall(r"^\| (\d{3,4}(?:/\d)?) \|", text, re.M))
    for s in _nch():
        code = s["id"].removeprefix("nch").replace("-", "/")
        assert code in rows, f"{code} falta en normas-nch.md"


def test_normas_nch_cited_flag_matches_section():
    text = (REFS / "normas-nch.md").read_text(encoding="utf-8")
    cited_part, _, not_cited_part = text.partition("## Relacionadas que el DS 15 **no** cita")
    for s in _nch():
        code = s["id"].removeprefix("nch").replace("-", "/")
        part = cited_part if s["cited_by_ds15"] else not_cited_part
        assert re.search(rf"^\| {re.escape(code)} \|", part, re.M), code


def test_references_carry_copyright_notice():
    for md in REFS.glob("*.md"):
        if "nch" in md.stem.lower():
            assert "no contiene texto de normas NCh" in md.read_text(encoding="utf-8"), md.name


def _manifest_ids():
    src = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]
    return {s["id"] for s in src}


def test_references_declare_verification_date():
    for md in REFS.glob("*.md"):
        assert re.search(r"Verificado:\s*\*{0,2}\d{4}-\d{2}-\d{2}", md.read_text(encoding="utf-8")), md.name


def test_cited_source_ids_exist_in_manifest():
    """Toda ID de fuente citada entre backticks (p.ej. `ds15-2024`) debe existir en el manifiesto."""
    ids = _manifest_ids()
    shaped = re.compile(r"`((?:ds|res|dex|oguc|ley|loscat|mrt|ditec|minvu|manual|pda|ppa|ppda|fsev|vit|umbral|nch)[a-z0-9]*-[a-z0-9-]+)`")
    for md in REFS.glob("*.md"):
        for ref in shaped.findall(md.read_text(encoding="utf-8")):
            if ref.endswith(".md"):
                continue
            assert ref in ids, f"{md.name}: `{ref}` no está en el manifiesto"
