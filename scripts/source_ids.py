"""Extrae identificadores (no contenido) de los PDF en sources/private/ para verificar el manifiesto.

Uso: .venv/bin/python scripts/source_ids.py [archivo.pdf ...]
Imprime sha256, páginas, CVE, edición D.O., "Núm." y fecha "Santiago, ..." de las primeras páginas.
Nunca imprime cuerpo de texto: solo patrones de identificación.
"""
import hashlib
import re
import sys
from pathlib import Path

import pymupdf

PRIVATE = Path(__file__).resolve().parents[1] / "sources" / "private"
PATTERNS = {
    "cve": r"CVE\s*(\d{6,8})",
    "do": r"Núm\.\s*([\d.]+)\s*\|\s*(\w+ \d{1,2} de \w+ de \d{4})",
    "num": r"Núm\.\s*(\d{1,4})(?!\.\d|\d)",
    "leychile": r"Decreto (\d{1,4})\b.{0,200}?Fecha Publicaci[oó]n ?:\s*([\w-]+).{0,5}?\|?\s*Fecha Promulgaci[oó]n ?:\s*([\w-]+)",
    "fecha": r"Santiago,\s*(\d{1,2}\s+de\s+\w+\s+(?:de\s+)?\d{4})",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ids(path: Path) -> dict:
    doc = pymupdf.open(path)
    text = re.sub(r"\s+", " ", " ".join(doc[i].get_text() for i in range(min(3, doc.page_count))))
    out = {"file": path.name, "sha256": sha256(path), "pages": doc.page_count, "has_text": bool(text.strip())}
    for key, pat in PATTERNS.items():
        m = re.search(pat, text)
        out[key] = " | ".join(m.groups()) if m else None
    return out


if __name__ == "__main__":
    files = [Path(a) for a in sys.argv[1:]] or sorted(PRIVATE.glob("*.pdf"))
    for f in files:
        print(ids(f))
