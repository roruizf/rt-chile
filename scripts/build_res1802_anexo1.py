"""Extrae el Anexo 1 de la Res. Ex. 1802 (PDF escaneado) a CSV crudo vía OCR por coordenadas.

Fuente: `res-ex-1802-2025` (sources/private/res-ex-1802-2025.pdf). Acto público.
Uso: .venv/bin/python scripts/build_res1802_anexo1.py > /tmp/anexo1_raw.csv
El CSV final (skills/rt-chile/data/res1802_anexo1_clima.csv) se revisa contra las imágenes antes de versionarlo.
"""
import csv
import re
import sys
from pathlib import Path

import pymupdf
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "sources" / "private" / "res-ex-1802-2025.pdf"
DPI = 200
# límites de columna en puntos PDF (x0 de cada columna), medidos sobre la tabla de la p. 4
COLS = [("zona", 0), ("localidad", 158), ("meridiano", 300), ("altitud", 355), ("t_ext", 430), ("hr_ext", 465)]


def col_of(x_pt):
    name = COLS[0][0]
    for n, x0 in COLS:
        if x_pt >= x0:
            name = n
    return name


def main():
    eng = RapidOCR()
    doc = pymupdf.open(PDF)
    w = csv.writer(sys.stdout)
    w.writerow(["pagina"] + [c for c, _ in COLS])
    for pno in range(3, 11):
        page = doc[pno]
        res, _ = eng(page.get_pixmap(dpi=DPI).tobytes("png"))
        scale = 72 / DPI
        items = []
        for box, text, _conf in res or []:
            xs = [p[0] * scale for p in box]
            ys = [p[1] * scale for p in box]
            items.append((sum(ys) / 4, min(xs), text.strip()))
        # una fila por cada valor en la columna T°ext; el resto se asigna a la fila más cercana en y
        anchors = sorted(y for y, x, t in items if col_of(x) == "t_ext" and re.fullmatch(r"-?\d+(?:[,.]\d)?", t.replace(" ", "")))
        rows = [[] for _ in anchors]
        for y, x, t in items:
            if not anchors:
                break
            k = min(range(len(anchors)), key=lambda a: abs(anchors[a] - y))
            if abs(anchors[k] - y) <= 4.5:
                rows[k].append((x, t))
        for r in rows:
            cells = {c: "" for c, _ in COLS}
            for x, t in sorted(r):
                c = col_of(x)
                cells[c] = (cells[c] + " " + t).strip()
            if re.fullmatch(r"-?\d+[,.]\d", cells["t_ext"].replace(" ", "")) or cells["hr_ext"].isdigit():
                w.writerow([pno + 1] + [cells[c] for c, _ in COLS])


if __name__ == "__main__":
    main()
