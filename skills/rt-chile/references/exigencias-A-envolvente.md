# Exigencia A — Transmitancia y resistencia térmica de la envolvente

Verificado: **2026-11-05**. Fuente: `ds15-2024` (Art. 4.1.10 según el DS 15, D.O. 27-05-2024, num. 1.A y 2.A,
Tablas 1–6 y 10–13). Las tablas son **valores de un acto público**, transcritos a `data/ds15_t*.csv` y verificados
así: OCR independiente de las imágenes del D.O., verificación literal contra las láminas DITEC (`ditec-lamina-puertas-ventanas`, Tablas 3
y 5) y tests de consistencia (Rt ≈ 1/U, R100 = Rt·100). Unidades: U en W/m²K, Rt en m²K/W, R100 = Rt × 100.

> [!IMPORTANT]
> En **viviendas** emplazadas en zona con PDA/PPA vigente mandan las tablas del plan (Art. 4.1.10 inc. 2°; ver
> `pda-ppa.md`). Estas tablas aplican fuera de zona PDA, y siempre a educación, salud y hoteles.

## 1. Qué tabla usar según el uso

| Elemento | Residencial (num. 1) | Hoteles | Educación y salud (num. 2) |
|---|---|---|---|
| Techumbre, muros, piso ventilado, puertas opacas: U máx. / Rt mín. | **Tabla 1** → `ds15_t01_u_rt_residencial.csv` | Tabla 1 | **Tabla 10** → `ds15_t10_u_rt_edu_salud.csv` |
| R100 mín. del aislante (vía rotulado) | **Tabla 2** → `ds15_t02_r100_residencial.csv` | Tabla 2 | **Tabla 11** → `ds15_t11_r100_edu_salud.csv` |
| Ventanas | **Tabla 3** (% máx. según orientación y U), con orientaciones de la **Tabla 4**, o bien la alternativa **Upvm de la Tabla 5** | **Tabla 12** (U máx.) | **Tabla 12** (U máx.) → `ds15_t12_ventanas_edu_salud_hoteles.csv` |
| Sobrecimiento (R100 mín.) | **Tabla 6** | Tabla 6 | **Tabla 13** |

Tabla 10 vs. Tabla 1: solo cambian los **muros**. En zona A el muro exige 2,00 en vez de 2,10; en zona D, 0,60 en
vez de 0,80. Lo mismo pasa con el R100 de muros en la Tabla 11 frente a la 2 (A: 50 vs. 48; D: 167 vs. 125). Lo
demás es idéntico.

## 2. Tabla 1 — U máx. / Rt mín., residencial (DS 15, num. 1.A)

| Zona | Techumbre U / Rt | Muro U / Rt | Piso ventilado U / Rt | Puerta opaca U / Rt |
|---|---|---|---|---|
| A | 0,84 / 1,19 | 2,10 / 0,48 | 3,60 / 0,28 | sin exigencia |
| B | 0,47 / 2,13 | 0,80 / 1,25 | 0,70 / 1,43 | 1,70 / 0,59 |
| C | 0,47 / 2,13 | 0,80 / 1,25 | 0,87 / 1,15 | 1,70 / 0,59 |
| D | 0,38 / 2,63 | 0,80 / 1,25 | 0,60 / 1,67 | 1,70 / 0,59 |
| E | 0,33 / 3,03 | 0,60 / 1,67 | 0,60 / 1,67 | 1,70 / 0,59 |
| F | 0,28 / 3,57 | 0,45 / 2,22 | 0,50 / 2,00 | 1,70 / 0,59 |
| G | 0,28 / 3,57 | 0,40 / 2,50 | 0,39 / 2,56 | 1,70 / 0,59 |
| H | 0,25 / 4,00 | 0,30 / 3,33 | 0,32 / 3,13 | 1,70 / 0,59 |
| I | 0,25 / 4,00 | 0,35 / 2,86 | 0,32 / 3,13 | 1,70 / 0,59 |

Notas que suelen generar errores:
- En **muros, la zona I es menos exigente que la H** (0,35 vs. 0,30). No suponer que la exigencia crece de A a I.
- En piso ventilado, **C (0,87) es menos exigente que B (0,70)**.
- R100 de la Tabla 2 = Rt de la Tabla 1 × 100, salvo en puertas, que no tienen vía R100.

## 3. Reglas de aplicación de A.1–A.4 (residencial; el num. 2 repite lo esencial)

- **Recintos contiguos** a la edificación (residencial: bodegas, logias, instalaciones, quinchos, estacionamientos
  cubiertos u otros similares; educación y salud: también talleres) se consideran **recintos abiertos** y **no
  tienen exigencia** (num. 1.A, a continuación de la Tabla 1; num. 2.A).
- **Continuidad:** el aislante debe cubrir en forma continua el máximo de la superficie.
  - Techumbre: incluye la parte superior de los muros (cadenas, vigas, soleras). Los muros, antepechos o dinteles de
    lucarnas y ventanas de techo cumplen la exigencia de techumbre.
  - Muros: el aislante solo puede interrumpirse en los vanos.
  - Piso ventilado: los elementos salientes cumplen la exigencia de piso.
  - Techumbre con entretecho: debe tener ventilación cruzada (rejilla o celosía en frontones, cumbreras o aleros)
    (A.1–A.3).
- **Puertas opacas:** la Tabla 1 aplica al marco y a la parte opaca de puertas entre un recinto acondicionado y el
  exterior o un recinto no acondicionado. Las partes vidriadas de la puerta cuentan como **ventana** (A.4). En zona A
  la puerta no tiene exigencia.
- **Definiciones:** techumbre = plano interior con inclinación **menor a 60°**; muro = **más de 60°** (mansardas con
  60° o menos cuentan como techumbre). Piso ventilado = piso que no está en contacto directo con el terreno,
  incluidos los voladizos cerrados y los planos inferiores de escaleras o rampas cerradas en contacto con el exterior
  (Art. 4.1.10, definiciones).

### Vías de cumplimiento (techumbre, muros, piso ventilado y puertas opacas)

1. **Aislante rotulado NCh 2251** con R100 ≥ Tabla 2 (o 11). Solo para techumbre, muros y piso ventilado. Debe
   constar en las EETT.
2. **Informe de Ensayo** de un laboratorio del registro DS 10, de **≤ 10 años** desde su realización. Opacos según NCh
   851; puertas opacas según NCh 3076/1-2.
3. **Memoria de Cálculo**. Opacos según NCh 853 y NCh 3117 "según corresponda"; puertas según NCh 3137/1-2. Las
   condiciones de cálculo de Rt y U están en la Res. Ex. 1802 (`res-ex-1802-2025`).
4. **Solución LOSCAT** vigente (`loscat-e14`). Ojo con la vigencia: la mayoría vence en diciembre de 2026
   (`docs/cambios-fuentes.md`).

Alternativa general, solo para viviendas: Informe de Precalificación Energética por demanda. Su umbral está
**pendiente** (`umbral-demanda-cev`). Ver `vias-acreditacion.md`.

## 4. Ventanas — residencial (num. 1.A.5, Tablas 3, 4 y 5)

**Opción 1: % máximo de ventanas por orientación (Tabla 3, `ds15_t03_ventanas_pct_residencial.csv`).**
1. Orientar cada muro perimetral según la normal a la fachada, con 0° = norte geográfico (Tabla 4): Norte [315°, 45°),
   Oriente [45°, 135°), Sur [135°, 225°), Poniente [225°, 315°). La Tabla 3 agrupa **Oriente y Poniente** ("O-P").
2. Con el **U de la ventana**, leer el % máximo en la columna "U ≤ x" que corresponda. Si en una orientación hay
   ventanas con distinto U, se usa el **U mayor**.
3. Superficie de paramentos por orientación = suma de las superficies **interiores** de los paramentos verticales
   perimetrales, **incluyendo medianeros**.
4. **SMV = StPV × %mV / 100.** La superficie de vanos de cada orientación debe ser ≤ SMV. Las ventanas salientes se
   cuentan por su desarrollo completo, con la orientación de cada paño.
5. Si menos del 60 % de la superficie total de muros perimetrales está expuesta (al exterior, a espacios contiguos
   abiertos o a recintos no acondicionados), se usa solo el % de la fila **OGT** sobre el total de paramentos, y se
   puede distribuir entre los muros expuestos.

**Opción 2 (alternativa, solo zonas B–I): U ponderado ventana + muro (Tabla 5, `ds15_t05_upvm_residencial.csv`).**
- **Upvm = (Um·Sm + Uv·Sv) / (Sm + Sv)** por orientación. Aquí la superficie de paramentos **excluye medianeros**.
- Si hay ventanas con distinto U, se usa el **U mayor**. El muro debe cumplir igual la Tabla 1.
- "na" en la Tabla 5 significa que la combinación zona/U no tiene valor. La zona A no tiene Upvm.

**En todas las zonas B–I:** toda ventana en **techumbre** (plano de 60° o menos) debe tener **U ≤ 3,6 W/m²K**.

**Vías para el U de la ventana:** Informe de Ensayo NCh 3076/1-2 (laboratorio DS 10), Memoria de Cálculo NCh
3137/1-2, o solución LOSCAT. El cumplimiento del % o del Upvm se acredita con un **informe** por orientación.

## 5. Ventanas — educación, salud y hoteles (num. 2.A.5, Tabla 12)

| Zona | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| U máx. ventana | 5,80 | 3,60 | 3,60 | 3,60 | 3,00 | 3,00 | 3,00 | **2,40** | 3,00 |
| Rt mín. | 0,17 | 0,28 | 0,28 | 0,28 | 0,33 | 0,33 | 0,33 | 0,42 | 0,33 |

No hay % de vidriado por orientación. Ventanas en techumbre de zonas B–I: U ≤ 3,6. Vías: ensayo NCh 3076/1-2,
cálculo NCh 3137/1-2 o LOSCAT.

## 6. Sobrecimientos (A.6, Tablas 6 y 13): R100 mín. del aislante

| Zona | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| R100 | sin exigencia | 45 | 45 | 45 | 45 | 91 | 91 | 91 | 91 |

Igual para residencial (Tabla 6) y para educación y salud (Tabla 13).
- **Residencial:** el aislante va **por el exterior**, desde el piso terminado hasta el hombro de la fundación, o
  hasta 30 cm bajo el nivel de terreno. El radier o la losa sobre terreno no exige aislante bajo ellos. Si no hay
  sobrecimiento, la exigencia la cumple el elemento que separa el piso terminado del terreno.
- **Vías:** aislante rotulado NCh 2251, o solución LOSCAT.

## 7. Cálculos con datos incompletos (criterio con supuestos)

Si falta la zona, el U de la ventana o la orientación, la skill puede calcular por escenarios declarando los
supuestos. Ejemplo: "si la comuna está bajo 1.000 msnm (zona F), el muro debe tener U ≤ 0,45". Debe cerrar con el
aviso de límites y las fuentes. Los scripts `u_check.py` y `ventanas.py` usan estos CSV.

## Fuentes oficiales a revisar

- DS 15/2024, Art. 4.1.10 (D.O.): https://www.diariooficial.interior.gob.cl/publicaciones/2024/05/27/43860/01/2494861.pdf
- Lámina DITEC "Estándar para puertas y ventanas": https://www.minvu.gob.cl/wp-content/uploads/2025/11/Puertas-y-Ventanas_DITEC-1.pdf
- Planilla MINVU de cálculo de U de ventanas: https://www.minvu.gob.cl/wp-content/uploads/2025/11/Calculo-U-Ventanas-DITEC-V.2024.1.0.xlsx
- LOSCAT E14: https://www.minvu.gob.cl/wp-content/uploads/2026/04/LOSCAT_E14_MAYO_2026.pdf
