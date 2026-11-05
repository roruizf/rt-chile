"""Índice propio del LOSCAT E14: una fila por ficha (página) con código, capítulo, nombre corto y vigencia.

Fuente: `loscat-e14` (sources/private/loscat-e14.pdf, minvu-pub, sha256 en el manifiesto).
No copia descripciones ni valores de desempeño: solo identificadores para ubicar la ficha en el PDF oficial.
Uso: .venv/bin/python scripts/build_loscat_indice.py
"""
import csv
import hashlib
import re
from pathlib import Path

import pymupdf
import yaml

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "sources" / "private" / "loscat-e14.pdf"
OUT = ROOT / "skills" / "rt-chile" / "data" / "loscat_e14_indice.csv"
CODE = re.compile(r"\b([1-3]\.[1-4]\.(?:[GMP]\.)?[A-Z0-9]{1,3}(?:\.[A-Z0-9]{1,3}){1,4})\b")
R100 = re.compile(r"\b(R100/[A-Z]{1,4}(?:\.\d+){1,3})\b")
VIG = re.compile(r"\b(ENERO|FEBRERO|MARZO|ABRIL|MAYO|JUNIO|JULIO|AGOSTO|SEPTIEMBRE|OCTUBRE|NOVIEMBRE|DICIEMBRE) (20\d\d)\b")
MES = {m: i for i, m in enumerate(["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
                                   "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"], 1)}
CAP = {"1.1": "Cubiertas/techumbres", "1.2": "Muros", "1.3": "Pisos ventilados", "1.4": "Sobrecimientos",
       "3.1": "Puertas", "3.2": "Ventanas"}


def index_vigencias(doc):
    """Empareja código ↔ vigencia en las páginas de índice (varias fichas por página), por fila (misma altura)."""
    code_re = re.compile(r"^(?:" + CODE.pattern.strip("\\b") + "|" + R100.pattern.strip("\\b") + r")$")
    out = {}
    for page in doc:
        words = page.get_text("words")
        codes = [w for w in words if code_re.match(w[4])]
        if len(codes) < 4:
            continue
        months = []
        for w in words:
            if w[4] in MES:
                yr = [x for x in words if x[4].isdigit() and len(x[4]) == 4 and abs(x[1] - w[1]) < 3 and 0 < x[0] - w[2] < 30]
                if yr:
                    months.append(((w[1] + w[3]) / 2, f"{yr[0][4]}-{MES[w[4]]:02d}"))
        for c in codes:
            cy = (c[1] + c[3]) / 2
            cand = {v for y, v in months if abs(y - cy) < 4}
            if len(cand) == 1:
                out.setdefault(c[4], set()).update(cand)
    return {k: next(iter(v)) for k, v in out.items() if len(v) == 1}


def main():
    manifest = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text(encoding="utf-8"))["sources"]
    expected = next(s["sha256"] for s in manifest if s["id"] == "loscat-e14")
    assert hashlib.sha256(PDF.read_bytes()).hexdigest() == expected, "PDF distinto al verificado"
    rows = []
    doc = pymupdf.open(PDF)
    idx = index_vigencias(doc)
    for i, page in enumerate(doc):
        text = re.sub(r"\s+", " ", page.get_text())
        codes = CODE.findall(text) or R100.findall(text)
        vig = VIG.findall(text)
        if not codes or len(set(codes)) > 3:  # páginas de índice/listado: se omiten
            continue
        code = max(set(codes), key=len)
        m = re.search(re.escape(code) + r"\s+(.{5,90}?)(?:\s+DESCRIPCI|\s+Instituci|\s+[A-Z]{3,} ?[A-Z]{3,}\s+DE\s|$)", text)
        nombre = (m.group(1) if m else "").strip()[:90]
        mes, anio = vig[0] if vig else ("", "")
        rows.append({"pagina_pdf": i + 1, "codigo": code,
                     "capitulo": CAP.get(code[:3], "Materiales R100" if code.startswith(("R100", "2.")) else code[:3]),
                     "nombre_corto": nombre, "vigencia_hasta": f"{anio}-{MES[mes]:02d}" if mes else idx.get(code, ""),
                     "vigencia_fuente": "ficha" if mes else ("indice" if code in idx else "no_extraida")})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} fichas -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
