"""Re-descarga a sources/private/ las fuentes del manifiesto que tienen `local` + URL directa, y verifica sha256.

Uso: .venv/bin/python scripts/fetch_private.py [--check]
  --check  solo informa qué falta o no calza, sin descargar.
Las fuentes sin URL directa (aportadas a mano) se listan como MANUAL al final.
"""
import hashlib
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DIRECT = (".pdf", ".xlsx", ".xls", ".zip")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    check = "--check" in sys.argv
    src = yaml.safe_load((ROOT / "sources/manifest.yaml").read_text(encoding="utf-8"))["sources"]
    manual, ok, bad = [], 0, []
    for s in src:
        local, h = s.get("local"), s.get("sha256")
        if not local:
            continue
        dest = ROOT / local
        if dest.exists() and h and sha(dest) == h:
            ok += 1
            continue
        url = str(s.get("mirror") or s.get("url_official") or s.get("url") or "")
        if check or not url.lower().split("?")[0].endswith(DIRECT):
            (manual if not url.lower().split("?")[0].endswith(DIRECT) else bad).append((s["id"], local, url))
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            # urllib solo acepta ASCII: los nombres con "°" del manifiesto se codifican aquí
            safe_url = urllib.parse.quote(url, safe=":/?&=%#+,;@")
            req = urllib.request.Request(safe_url, headers={"User-Agent": "rt-chile-fetch"})
            dest.write_bytes(urllib.request.urlopen(req, timeout=180).read())
            if h and sha(dest) != h:
                bad.append((s["id"], local, "sha256 distinto (¿el sitio cambió el archivo?)"))
            else:
                ok += 1
                print("descargado:", local)
        except Exception as e:  # noqa: BLE001
            bad.append((s["id"], local, f"error: {e}"))
    print(f"\nOK: {ok}")
    for i, l, u in bad:
        print(f"FALTA/NO CALZA  {i}  {l}  {u}")
    for i, l, u in manual:
        print(f"MANUAL          {i}  {l}  {u or '(sin URL directa: obtenerla a mano)'}")


if __name__ == "__main__":
    main()
