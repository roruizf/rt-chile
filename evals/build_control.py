"""Genera evals/control/: preguntas que no sirven para ajustar la skill, solo para detectar sobreajuste.

Usan comunas y combinaciones fuera de evals/cases/ y leen los valores esperados de data/. Se fijan antes de ver
respuestas. Un fallo se registra; solo se corrige la skill si revela un dato o una cita incorrectos, y en ese caso la
pregunta deja de contar como control.
Uso: .venv/bin/python evals/build_control.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
from build_cases import N, h  # noqa: E402

DATA = ROOT / "skills" / "rt-chile" / "data"
OUT = ROOT / "evals" / "control"
DS15 = ["ds15-2024"]
LIMITE = r"no (puedo|reproduzco|transcribo|es posible)|no se puede|copyright|derechos"


def valor(archivo: str, zona: str, columna: str) -> str:
    """Patrón del valor de una tabla, con coma o punto y sin exigir ceros finales."""
    with (DATA / archivo).open(encoding="utf-8") as fh:
        fila = next(f for f in csv.DictReader(fh) if f["zona"] == zona)
    entero, _, decimal = fila[columna].partition(".")
    if not decimal:
        return rf"\b{entero}\b"
    return rf"\b{entero}{N}{decimal.rstrip('0') or '0'}0?\b"


def u(zona: str, elemento: str, tabla: str = "ds15_t01_u_rt_residencial.csv") -> str:
    return valor(tabla, zona, f"{elemento}_u")


EDU = "ds15_t10_u_rt_edu_salud.csv"
VENTANA = "ds15_t12_ventanas_edu_salud_hoteles.csv"
VENTILACION = [h("Extracción mecánica", r"mec[áa]nic"), h("Baños y cocina", r"cocina"), h("Higrostato", r"higrostato")]

CASOS = [
    ("Casa nueva en Lautaro: ¿qué U máximo de muro y de techumbre debo cumplir? ¿Tiene plan de descontaminación?",
     [h("Zona F", r"zona\s*\**F\b"), h("Muro", u("F", "muro")), h("Techumbre", u("F", "techumbre")),
      h("Sin plan registrado", r"sin (PDA|plan|PPA)|no (aplica|hay|tiene|est[aá]|registra|cuenta|rige)")],
     [r"Tabla\s*(N[°º]\s*)?1\b"], "Lautaro: zona F, sin plan; Tabla 1.", DS15),
    ("Vivienda nueva en Pucón: zona térmica, U de muro y clase de infiltración.",
     [h("Zona H", r"zona\s*\**H\b"), h("Muro", u("H", "muro")), h("Infiltración 5", r"\b5(,0+|\.0+)?\s*(ach|1/h|h)|clase\s*5|5\s*\(")],
     [], "Pucón: zona H, provincia de Cautín; Tablas 1 y 7.", DS15),
    ("Casa en Cauquenes: acredito el muro por rotulado del aislante. ¿Qué R100 necesito?",
     [h("Zona E", r"zona\s*\**E\b"), h("R100 muro", valor("ds15_t02_r100_residencial.csv", "E", "muro_r100"))],
     [r"Tabla\s*(N[°º]\s*)?2\b"], "Cauquenes: zona E; R100 de muro de la Tabla 2.", DS15),
    ("Escuela nueva en Melipilla: ¿qué U máximo de muro exige?",
     [h("Zona D", r"zona\s*\**D\b"), h("Muro educación", u("D", "muro", EDU))], [r"Tabla\s*(N[°º]\s*)?10\b"],
     "Educación en zona D: Tabla 10, distinto de vivienda.", DS15),
    ("Clínica nueva en Castro: ¿qué U de ventana exige y debe acreditar ventilación?",
     [h("Zona G", r"zona\s*\**G\b"), h("Ventana", valor(VENTANA, "G", "ventana_u")), h("Salud eximida de ventilación", r"exim|exent|no (debe|aplica|exige|requiere|tiene|necesita)")],
     [r"Tabla\s*(N[°º]\s*)?12\b"], "Salud en zona G: Tabla 12; eximida de ventilación.", DS15),
    ("Hotel nuevo en Puerto Varas: ¿qué U de muro exige y necesita memoria de condensación y ensayo de infiltración?",
     [h("Muro zona G", u("G", "muro")), h("Hotel exento", r"exent|exim|no (necesita|requiere|aplica|debe|exige)")], [],
     "Hotel usa Tabla 1; exento de B, C y D.", DS15),
    ("Vivienda nueva en Chillán Viejo: además de cumplir la NCh 3309, ¿me piden algo más en ventilación?",
     VENTILACION, [r"Art\.?\s*25|Art[íi]culo\s*25"], "DS 48 Art. 25: extracción mecánica en baño y cocina con higrostato.", ["pda-chillan-ds48"]),
    ("Casa nueva en Los Ángeles: ¿el plan de descontaminación dice algo sobre ventilación?",
     VENTILACION, [r"Art\.?\s*20|Art[íi]culo\s*20"], "DS 4/2017 Art. 20 N°4.", ["pda-los-angeles-ds4-2017"]),
    ("¿Qué pide el plan de Valdivia sobre ventilación en una vivienda nueva?",
     VENTILACION, [r"Art\.?\s*28|Art[íi]culo\s*28"], "DS 25/2016 Art. 28 N°4.", ["pda-valdivia-ds25-2016"]),
    ("Vivienda nueva en Los Ángeles: ¿cuál es el U máximo de muro y de dónde sale?",
     [h("Muro", u("F", "muro")), h("Plan DS 4", r"DS\s*(N[°º]\s*)?4\b"), h("Nota del 4.1.10", r"4\.1\.10")], [r"Art\.?\s*20|Art[íi]culo\s*20"],
     "Plan: DS 4/2017 Art. 20; el 4.1.10 fija el mismo valor.", ["pda-los-angeles-ds4-2017"]),
    ("Vivienda nueva en Valdivia: ¿cuál es el U máximo de piso ventilado?",
     [h("Piso ventilado", u("G", "piso_ventilado")), h("Plan DS 25", r"DS\s*(N[°º]\s*)?25\b")], [],
     "Última etapa del plan de Valdivia: igual a la Tabla 1, zona G.", ["pda-valdivia-ds25-2016"]),
    ("Colegio nuevo en Curicó, en el valle: ¿le aplican las tablas del PDA? ¿Qué U de muro exige?",
     [h("El plan no aplica a educación", r"no\b"), h("Muro educación zona D", u("D", "muro", EDU))], [r"Tabla\s*(N[°º]\s*)?10\b"],
     "El inc. 2° alcanza solo a viviendas: Tabla 10.", DS15),
    ("Vivienda nueva en Rengo a 1.100 msnm: ¿qué U de muro debo cumplir?",
     [h("Valor del plan", r"\b0[,.]80?\b"), h("Valor del 4.1.10", u("H", "muro")), h("Estricto o DOM", r"estrict|DOM")], [],
     "Zona H: el plan fija 0,80 y el 4.1.10, 0,30. Muestra ambos y recomienda el más estricto o consultar a la DOM.", ["pda-ohiggins-ds1-2021"]),
    ("Casa en Illapel, no sé la altitud. ¿Qué U de muro debo cumplir?",
     [h("Bajo 2.000 m", u("B", "muro")), h("Desde 2.000 m", u("H", "muro")), h("Depende de la altitud", r"altitud|msnm|2\.?000")], [],
     "Illapel es multizona: B bajo 2.000 m y H desde esa altitud.", DS15),
    ("¿Qué zona térmica tiene Ovalle?",
     [h("Zona B", r"\bB\b"), h("Zona C", r"\bC\b"), h("Depende del meridiano", r"meridiano|longitud|71")], [],
     "Ovalle es multizona por meridiano 71° 15'.", DS15),
    ("¿Qué temperatura y humedad exterior uso para calcular condensación en Ancud?",
     [h("Temperatura", rf"\b3{N}5\b"), h("Humedad", r"\b98\b"), h("Res. Ex. 1802", r"1\.?802")], [],
     "Anexo 1 de la Res. Ex. 1802: 3,5 °C y 98 %.", ["references/exigencias-B-condensacion.md"]),
    ("Loteo de 60 casas en Villa Alemana: ¿qué infiltración máxima aplica y cuántas casas se ensayan?",
     [h("8 ach", r"\b8(,0+|\.0+)?\s*(ach|1/h|h|renovaciones)|\b8\b[^\n]{0,30}50\s*Pa|clase\s*8"), h("Muestra de 3", r"\b3\s*(casas|viviendas|unidades)|\btres\b|muestra[^\n]{0,30}\b3\b")], [r"Tabla\s*(N[°º]\s*)?8\b"],
     "Marga Marga, 8 ach; lote de 51 a 500: muestra de 3.", DS15),
    ("Transcríbeme el procedimiento de ensayo de la NCh 3295 y sus tablas.",
     [h("No reproduce la norma", LIMITE), h("Visor oficial", r"normastecnicas\.minvu\.cl")], [],
     "Se niega a reproducir la NCh y remite al visor.", ["references/normas-nch.md"]),
    ("Proyecto con subsidio FSEV en Ancud: ¿qué U de ventana pide el FSEV?",
     [h("Fuera de alcance", r"fuera (del|de) (alcance|la skill)"), h("Remite a la fuente", r"1\.?163|DITEC")], [],
     "No responde requisitos FSEV; remite al Ord. DITEC 1.163/2023.", ["references/alcance-y-vigencia.md"]),
    ("¿Puedo usar la solución LOSCAT 1.2.M.B17.5 en un permiso que ingreso en marzo de 2027?",
     [h("No vigente en esa fecha", r"\bno\b|venc"), h("Vigencia hasta diciembre de 2026", r"(diciembre|dic\.?)\s*(de\s*|/)?2026|2026-12|12[-/]2026")], [],
     "El índice LOSCAT E14 la da vigente hasta 2026-12.", ["references/loscat.md"]),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for i, (pregunta, hechos, citas, rubrica, fuentes) in enumerate(CASOS, 1):
        cid = f"control-{i:02d}"
        caso = {"id": cid, "categoria": "control", "critical": False, "pregunta": pregunta,
                "esperado": {"hechos": hechos, "citas": citas, "prohibidos": [], "cierre": True}, "rubrica": rubrica,
                "fuentes": fuentes}
        (OUT / f"{cid}.yaml").write_text(yaml.safe_dump(caso, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")
    print(len(CASOS), "preguntas de control")


if __name__ == "__main__":
    main()
