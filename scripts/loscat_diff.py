"""Compara dos ediciones del LOSCAT por códigos de solución (no copia descripciones).

Uso: .venv/bin/python scripts/loscat_diff.py sources/private/loscat-e13.pdf sources/private/loscat-e14.pdf
Imprime un resumen por capítulo: códigos nuevos, eliminados y comunes. Los códigos son identificadores
públicos del listado oficial MINVU.
"""
import re
import sys
from collections import Counter

import pymupdf

CODE = re.compile(r"\b([1-3]\.[1-4]\.(?:[GMP]\.)?[A-Z0-9]{1,3}(?:\.[A-Z0-9]{1,3}){1,4})\b")
CHAPTERS = {
    "1.1": "Cubiertas/techumbres", "1.2": "Muros", "1.3": "Pisos ventilados", "1.4": "Sobrecimientos",
    "2.1": "Materiales aislantes (R100)", "3.1": "Puertas", "3.2": "Ventanas",
}


def codes(path):
    doc = pymupdf.open(path)
    found = set()
    for page in doc:
        found.update(CODE.findall(page.get_text()))
    # descarta prefijos que son solo agrupadores (p.ej. 1.1.M.B1) si existe un código más largo bajo ellos
    return {c for c in found if not any(o != c and o.startswith(c + ".") for o in found)}, doc.page_count


def chapter(code):
    return CHAPTERS.get(code[:3], code[:3])


if __name__ == "__main__":
    (a, pa), (b, pb) = codes(sys.argv[1]), codes(sys.argv[2])
    print(f"páginas: {pa} -> {pb}; códigos: {len(a)} -> {len(b)}; nuevos {len(b - a)}; eliminados {len(a - b)}")
    new, gone, both = Counter(map(chapter, b - a)), Counter(map(chapter, a - b)), Counter(map(chapter, a & b))
    for ch in sorted(set(new) | set(gone) | set(both)):
        print(f"  {ch:28s} comunes {both[ch]:4d}  nuevos {new[ch]:4d}  eliminados {gone[ch]:4d}")
    if "-v" in sys.argv:
        print("NUEVOS:", " ".join(sorted(b - a)))
        print("ELIMINADOS:", " ".join(sorted(a - b)))
