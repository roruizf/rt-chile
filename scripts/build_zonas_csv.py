"""Construye skills/rt-chile/data/zonas_comunas.csv desde la tabla oficial MINVU de zonas térmicas.

Fuente: `ds15-tabla-zonas` (sources/private/ds15-tabla-zonas.pdf, acto público, verificado con sha256).
Uso: .venv/bin/python scripts/build_zonas_csv.py

Columnas: region, provincia, comuna, zona,
  alt_min, alt_min_incl, alt_max, alt_max_incl          (msnm)
  lon_oeste_min, lon_oeste_min_incl, lon_oeste_max, lon_oeste_max_incl  (grados de longitud oeste, decimales)
  condicion_original                                    (notación de la tabla, para trazabilidad)
Vacío = sin límite. *_incl: 1 = inclusivo, 0 = estricto.
"""
import csv
import hashlib
import re
from pathlib import Path

import pymupdf
import yaml

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "sources" / "private" / "ds15-tabla-zonas.pdf"
OUT = ROOT / "skills" / "rt-chile" / "data" / "zonas_comunas.csv"
FIELDS = ["region", "provincia", "comuna", "zona",
          "alt_min", "alt_min_incl", "alt_max", "alt_max_incl",
          "lon_oeste_min", "lon_oeste_min_incl", "lon_oeste_max", "lon_oeste_max_incl",
          "condicion_original"]


def cell_text(words, rect):
    """Texto de una celda, reconstruido con espacios desde las palabras cuyo centro cae dentro."""
    ws = [w for w in words if rect.contains(pymupdf.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2))]
    ws.sort(key=lambda w: (round(w[1]), w[0]))
    text = re.sub(r"\s+", " ", " ".join(w[4] for w in ws)).strip(" .")
    return re.sub(r"(\w)- (\w)", r"\1-\2", text)  # palabras partidas por salto de línea ("Bío- Bío")


def _num(x, kind):
    x = x.strip()
    if kind == "alt":
        return str(int(x.replace(".", "")))
    m = re.fullmatch(r"(\d+)°\s*(?:(\d+)')?", x)
    if not m:
        raise ValueError(f"meridiano no reconocido: {x!r}")
    val = int(m.group(1)) + int(m.group(2) or 0) / 60
    return f"{val:.4f}".rstrip("0").rstrip(".")


def parse_cond(s, kind):
    """(min, min_incl, max, max_incl) desde la notación de la tabla ('< 1.000', '1.100 ≤ < 3.000', "> 71° 15'")."""
    raw = re.sub(r"(?i)msnm|altitud", "", s).strip()
    if raw in ("", "-"):
        return "", "", "", ""
    m = re.fullmatch(r"([\d.]+)\s*≤\s*<\s*([\d.]+)", raw)
    if m:
        return _num(m.group(1), kind), "1", _num(m.group(2), kind), "0"
    m = re.fullmatch(r"(<|≤|>|≥)\s*(.+)", raw)
    if not m:
        raise ValueError(f"condición no reconocida: {s!r}")
    op, v = m.group(1), _num(m.group(2), kind)
    return {"<": ("", "", v, "0"), "≤": ("", "", v, "1"), ">": (v, "0", "", ""), "≥": (v, "1", "", "")}[op]


def extract_rows():
    rows = []
    for page in pymupdf.open(PDF):
        words = page.get_text("words")
        for tb in page.find_tables().tables:
            for r in tb.rows:
                cells = [cell_text(words, pymupdf.Rect(c)) if c else "" for c in r.cells]
                if len(cells) != 6:
                    continue
                reg, prov, com, zona, mer, alt = cells
                if not re.fullmatch(r"[A-I]", zona):  # encabezados y filas partidas
                    continue
                a, g = parse_cond(alt, "alt"), parse_cond(mer, "mer")
                rows.append(dict(zip(FIELDS, [reg, prov, com, zona, *a, *g,
                                              " | ".join(x for x in (alt, mer) if x not in ("", "-"))])))
    return rows


def main():
    manifest = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]
    expected = next(s["sha256"] for s in manifest if s["id"] == "ds15-tabla-zonas")
    assert hashlib.sha256(PDF.read_bytes()).hexdigest() == expected, "PDF distinto al verificado"
    rows = extract_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} filas, {len({(r['region'], r['comuna']) for r in rows})} comunas -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
