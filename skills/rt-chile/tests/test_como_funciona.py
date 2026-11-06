"""El documento de prevalencia no puede quedar desalineado con las contradicciones ni con el código."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOC = (ROOT / "docs" / "como-funciona.md").read_text(encoding="utf-8")


def test_cada_hipotesis_declara_su_base():
    filas = re.findall(r"^\| (H\d+) \| [^|]+ \| ([^|]+) \|", DOC, re.M)
    assert len(filas) >= 10
    for hid, base in filas:
        assert re.match(r"(Norma expresa|Criterio declarado|Pendiente)", base.strip()), hid


def test_contradicciones_citadas_existen():
    contradicciones = (ROOT / "docs" / "contradicciones.md").read_text(encoding="utf-8")
    for c in set(re.findall(r"\bC\d{2}\b", DOC)):
        assert f"| {c} |" in contradicciones, c


def test_rutas_citadas_existen():
    for ruta in ("data/pda.csv", "data/pda_minvu_actos.csv", "references/pda-ppa.md", "scripts/pda.py"):
        assert ruta in DOC and (ROOT / "skills" / "rt-chile" / ruta).exists(), ruta


def test_cita_el_texto_del_inciso_2_tal_como_el_decreto():
    assert "deberá estarse, en materia de exigencias de acondicionamiento térmico, a lo dispuesto en dicho Plan" in DOC
