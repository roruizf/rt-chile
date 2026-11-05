# Vías de acreditación (Art. 4.1.10, DS 15)

Verificado: **2026-11-05**. Fuentes: `ds15-2024` (inc. 3°–5° del Art. 4.1.10 y las "alternativas de cumplimiento" de
cada literal de los num. 1 y 2; arts. 1° y 2° transitorios), `res-ex-1802-2025`, `loscat-e14`, `oguc-2026-03`
(Arts. 5.1.6 y 5.2.6). El detalle de cada exigencia está en `exigencias-A…D-*.md`.

## 1. Regla general

- Cada exigencia (A, B, C, D) se acredita con **la vía que permite su literal**. Se pueden **combinar vías** entre
  elementos: por ejemplo, LOSCAT para muros, R100 para techumbre y ensayo para ventanas (inc. 3° y 4°).
- Formas de acreditar que nombra el inc. 4°: Informe de acreditación, Informe de Ensayo, Memoria de Cálculo, solución
  LOSCAT, o un material propuesto por el arquitecto (que además consta en las EETT).
- Los informes y memorias los puede hacer un **profesional competente o especialista**, y los **suscribe además el
  arquitecto** del proyecto (inc. 4°). Los ensayos de laboratorio son de un **laboratorio del registro DS 10**.
- En **viviendas en zona PDA** mandan las vías del plan (`pda-ppa.md`).

## 2. Matriz exigencia × vía

| Exigencia | Aislante rotulado NCh 2251 (R100) | Informe de Ensayo | Memoria de Cálculo | Solución LOSCAT | Otra |
|---|---|---|---|---|---|
| **A** techumbre, muros, piso ventilado | ✔ R100 ≥ Tabla 2/11 | ✔ NCh 851, lab DS 10, **≤ 10 años** | ✔ NCh 853 + NCh 3117 (condiciones Res. Ex. 1802 num. 3 y 4) | ✔ | Vía por demanda (CEV), solo viviendas: **pendiente** (§3) |
| **A** puertas opacas | ✘ (salvo que la solución LOSCAT E14 lo admita: R100 ≥ 70, ver `docs/cambios-fuentes.md`) | ✔ NCh 3076/1-2, lab DS 10, ≤ 10 años | ✔ NCh 3137/1-2 | ✔ | Ídem |
| **A** ventanas (U) | ✘ | ✔ NCh 3076/1-2, lab DS 10 | ✔ NCh 3137/1-2 | ✔ | — |
| **A** ventanas (% por orientación o Upvm, residencial) | — | — | **Informe** por orientación (Tabla 3 o 5) | — | — |
| **A** sobrecimiento | ✔ R100 ≥ Tabla 6/13 | ✘ | ✘ | ✔ | — |
| **B** condensación | ✘ | ✘ | ✔ **única vía**: NCh 1973 + Res. Ex. 1802 | ✘ | Hoteles exentos |
| **C** infiltración de la envolvente | ✘ | ✔ **en terreno** NCh 3295, obra terminada, con muestra (Tablas 8/15). Lo hace el arquitecto, un consultor DS 135 o un lab DS 10 | ✘ | ✘ | Partida de **sellos** en EETT (condicionada, `exigencias-C-infiltracion.md`). Hoteles exentos |
| **C** permeabilidad de puertas y ventanas | ✘ | ✔ NCh 3296/3297, lab DS 10 | ✘ | ✔ (Título III) | Hoteles exentos |
| **D** ventilación | ✘ | ✘ | **Informe de cumplimiento de la tasa** (NCh 3308/3309) | ✘ | Hoteles y salud eximidos |

✔ permitida · ✘ no prevista en el literal · — no aplica.

## 3. Vía alternativa por demanda de energía (Informe de Precalificación Energética)

- **Solo viviendas.** Reemplaza **únicamente la exigencia A**. **No cubre** condensación, infiltración ni ventilación,
  que se acreditan siempre por su literal (inc. 5°).
- La elabora un **Evaluador Energético** inscrito en el Registro Nacional, y demuestra que la demanda de energía es
  igual o menor al valor que fije **una resolución MINVU**.
- **Vigencia:** el valor de demanda rige a los **36 meses** desde la publicación del DS 15 (art. 2° transitorio), o
  sea hacia **mayo de 2027**. La resolución con el umbral **no estaba publicada al 2026-11-05** (`umbral-demanda-cev`).
  Respuesta correcta hoy: **"vía no disponible todavía; umbral pendiente"**.
- Es distinta de la **Calificación Energética (CEV)** obligatoria del DS 5/2024 para la recepción de ciertas
  viviendas. Una cosa no acredita la otra (ver `trampas.md`).

## 4. Requisitos transversales

- **Antigüedad del ensayo de A:** ≤ 10 años desde su realización (num. 1.A, vía 2).
- **LOSCAT:** la solución debe estar **vigente** al acreditar. Las fichas vencidas no sirven. La E14 vence mayormente
  en **diciembre de 2026** (`docs/cambios-fuentes.md`). La skill siempre informa la vigencia y la fecha de la consulta.
- **Registros MINVU:** laboratorios (DS 10, `ds10-2002-registro-lab`) y consultores (DS 135,
  `ds135-1978-registro-consultores`). Verificar que la inscripción esté vigente en el registro oficial.
- **Dónde se entregan:** en el permiso (OGUC Art. 5.1.6 N° 11), y en la recepción (Art. 5.2.6 N° 7), donde además va
  el ensayo de infiltración en terreno. Ver `roles-firmas-expediente.md`.

## 5. Respuesta tipo de la skill

1. Por cada elemento: la vía más simple que encaje con lo que el usuario ya tiene (LOSCAT vigente o aislante
   rotulado), y la alternativa (cálculo o ensayo).
2. Para B, C y D, decir explícitamente que **no hay atajo**: la memoria (B), el ensayo en obra (C) y el informe de
   tasa (D) se hacen siempre, salvo en los usos eximidos.
3. Cerrar con quién firma, en qué etapa se presenta y el aviso de límites.

## Fuentes oficiales a revisar

- DS 15/2024 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- LOSCAT vigente (página DITEC): https://www.minvu.gob.cl/ditec/
- Registro de Evaluadores Energéticos y CEV: https://www.calificacionenergetica.cl/
