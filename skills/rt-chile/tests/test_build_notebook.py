"""La verificación del notebook detecta fuentes sin contenido, aunque NotebookLM las marque como listas."""
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("build_notebook", ROOT / "scripts" / "build_notebook.py")
bn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bn)

NORMA = "Artículo 4.1.10. Las viviendas deberán cumplir las exigencias de transmitancia térmica. " * 20
ERROR_403 = "ERROR: The request could not be satisfied 403 ERROR The request could not be satisfied. " * 8
ESPERA = "Ley Chile Este proceso demora demasiado, es probable que su conexión esté muy lenta."
IMAGEN = "https://lh3.googleusercontent.com/notebooklm/EjemploSinValorRealEjemploSinValorRealEjemplo12\n" \
         "00000000-0000-4000-8000-000000000000\n"


def test_acepta_fuente_con_contenido():
    assert bn.defecto("ds15.pdf", NORMA) is None


def test_rechaza_vacia_y_corta():
    assert "solo 0 caracteres" in bn.defecto("x.pdf", "")
    assert "caracteres" in bn.defecto("x", "Texto breve sin contenido normativo.")


def test_rechaza_texto_de_error_aunque_supere_el_minimo():
    assert len(ERROR_403) > bn.MIN_CARACTERES / 2
    assert bn.defecto("x", ERROR_403 * 3) == "texto de error"
    assert bn.defecto("x", ESPERA + NORMA) == "texto de error"
    assert bn.defecto("ERROR: algo", NORMA) == "texto de error"


def test_rechaza_pagina_web_que_envuelve_un_decreto_truncado():
    pagina = "Ley Chile Ingresar Registrarse Este sitio está protegido por reCAPTCHA y se aplican " + NORMA
    assert bn.defecto("Ley Chile - Decreto 105", pagina) == "texto de error"


def test_escaneo_no_pasa_por_el_largo_de_sus_urls():
    texto = IMAGEN * 25
    assert len(texto) > bn.MIN_CARACTERES
    assert "solo 0 caracteres" in bn.defecto("otro-escaneo.pdf", texto)


def test_escaneo_aceptado_pasa_salvo_que_traiga_texto_de_error():
    assert bn.defecto("res-ex-1802-2025.pdf", IMAGEN * 25) is None
    assert bn.defecto("res-ex-1802-2025.pdf", "") is None
    assert bn.defecto("res-ex-1802-2025.pdf", ERROR_403) == "texto de error"


def test_palabra_de_error_en_el_cuerpo_de_una_norma_no_es_defecto():
    assert bn.defecto("x.pdf", NORMA * 2 + " access denied " + NORMA) is None


def _cli_falso(textos):
    def cli(*args):
        if args[:2] == ("source", "list"):
            fuentes = [{"id": f"id{i}", "title": t} for i, (t, _) in enumerate(textos)]
            return subprocess.CompletedProcess(args, 0, json.dumps({"sources": fuentes}), "")
        i = int(args[2].removeprefix("id"))
        Path(args[args.index("-o") + 1]).write_text(textos[i][1], encoding="utf-8")
        return subprocess.CompletedProcess(args, 0, "{}", "")
    return cli


def test_verificar_acepta_notebook_sano():
    assert bn.verificar("nb", _cli_falso([("a.pdf", NORMA), ("b.pdf", NORMA)]), esperado=2) == []


def test_verificar_reporta_error_duplicado_y_total():
    problemas = bn.verificar("nb", _cli_falso([("a.pdf", NORMA), ("a.pdf", NORMA), ("c", ERROR_403)]), esperado=2)
    assert "hay 3 fuentes y se esperaban 2" in problemas
    assert "duplicada: a.pdf (2 veces)" in problemas
    assert "c: texto de error" in problemas


def test_main_sale_con_codigo_1_si_hay_defecto(monkeypatch):
    monkeypatch.setattr(bn, "verificar", lambda nb: ["c: texto de error"])
    monkeypatch.setattr("sys.argv", ["build_notebook.py", "--verificar", "nb"])
    try:
        bn.main()
    except SystemExit as e:
        assert e.code == 1
    else:
        raise AssertionError("debió salir con código 1")


def test_un_pdf_con_dos_ids_cuenta_como_una_fuente():
    grupos = bn.oficiales()
    locales = [g[0].get("local") for g in grupos]
    assert len(locales) == len(set(locales))
    assert any(len(g) == 2 for g in grupos)


def test_tablas_incluyen_el_clima_del_anexo_1_con_los_valores_de_data():
    import csv
    texto = bn.tablas_ds15()
    assert "- Peralillo, zona D: T° exterior 4,4 °C, HR exterior 90 %" in texto
    with (bn.SKILL / "data" / "res1802_anexo1_clima.csv").open(encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    assert len([l for l in bn.clima_anexo1() if l.startswith("- ")]) == len(filas)
