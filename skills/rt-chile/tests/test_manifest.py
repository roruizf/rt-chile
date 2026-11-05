"""Validación estructural de sources/manifest.yaml (no verifica contenido normativo)."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "sources" / "manifest.yaml"
LICENSES = {"public-act", "minvu-pub", "third-party", "inn-copyright"}
STATUSES = {"verified", "located", "pending"}


def _sources():
    return yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))["sources"]


def test_manifest_parses_and_has_sources():
    assert _sources(), "manifest.yaml sin fuentes"


def test_ids_unique():
    ids = [s["id"] for s in _sources()]
    assert len(ids) == len(set(ids))


def test_license_and_status_valid():
    for s in _sources():
        assert s.get("license") in LICENSES, s["id"]
        assert s.get("status") in STATUSES, s["id"]
        assert s.get("title"), s["id"]


def test_verified_requires_hash_or_url():
    for s in _sources():
        if s["status"] == "verified":
            assert s.get("sha256") or s.get("url"), s["id"]


def test_scope_valid():
    for s in _sources():
        assert s.get("scope", "in") in {"in", "out"}, s["id"]


def test_no_private_drive_references():
    for s in _sources():
        assert "drive" not in s and "edition_drive" not in s, s["id"]


def test_inn_sources_have_no_text_fields():
    for s in _sources():
        if s["license"] == "inn-copyright":
            assert not {"text", "excerpt", "content"} & set(s), s["id"]


def test_local_hash_matches_when_present():
    """Las copias privadas no están en git; si existen localmente, su sha256 debe calzar."""
    import hashlib

    for s in _sources():
        local = s.get("local")
        if local and (ROOT / local).exists():
            assert local.startswith("sources/private/"), s["id"]
            digest = hashlib.sha256((ROOT / local).read_bytes()).hexdigest()
            assert digest == s["sha256"], s["id"]


def test_no_duplicate_keys():
    class Strict(yaml.SafeLoader):
        pass

    def construct(loader, node, deep=False):
        keys = [loader.construct_object(k) for k, _ in node.value]
        dups = {k for k in keys if keys.count(k) > 1}
        assert not dups, f"claves duplicadas {dups} en {node.start_mark}"
        return loader.construct_mapping(node, deep)

    Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct)
    yaml.load(MANIFEST.read_text(encoding="utf-8"), Strict)
