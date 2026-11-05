# data/ — tablas normativas en formato máquina

Solo valores de **actos públicos** (DS 15/2024 y tabla MINVU de zonas), con su fuente. Nunca tablas de normas NCh.
Valores numéricos con punto decimal. IDs de fuente en `sources/manifest.yaml`.

| Archivo | Contenido | Fuente | Cómo se obtuvo |
|---|---|---|---|
| `zonas_comunas.csv` | Comuna → zona A–I, con límites de altitud/meridiano | `ds15-tabla-zonas` | `scripts/build_zonas_csv.py` (valida sha256) |
| `ds15_t01_u_rt_residencial.csv` | Tabla 1: U máx./Rt mín. residencial | `ds15-2024`, num. 1.A | Transcripción + OCR + test Rt≈1/U |
| `ds15_t02_r100_residencial.csv` | Tabla 2: R100 mín. residencial | `ds15-2024`, num. 1.A | Transcripción + OCR + test R100=Rt·100 |
| `ds15_t03_ventanas_pct_residencial.csv` | Tabla 3: % máx. de ventanas por zona/orientación/U | `ds15-2024`, num. 1.A.5 | Transcripción + verificación literal en `ditec-lamina-puertas-ventanas` |
| `ds15_t04_orientaciones.csv` | Tabla 4: rangos de azimut por orientación | `ds15-2024`, num. 1.A.5 | Transcripción |
| `ds15_t05_upvm_residencial.csv` | Tabla 5: Upvm máx. (zonas B–I) | `ds15-2024`, num. 1.A.5 | Transcripción + verificación literal en `ditec-lamina-puertas-ventanas` |
| `ds15_t06_r100_sobrecimiento_residencial.csv` | Tabla 6: R100 sobrecimiento | `ds15-2024`, num. 1.A.6 | Transcripción + OCR |
| `ds15_t10_u_rt_edu_salud.csv` | Tabla 10: U/Rt educación y salud | `ds15-2024`, num. 2.A | Transcripción + OCR + test Rt≈1/U |
| `ds15_t11_r100_edu_salud.csv` | Tabla 11: R100 educación y salud | `ds15-2024`, num. 2.A | Transcripción + OCR |
| `ds15_t12_ventanas_edu_salud_hoteles.csv` | Tabla 12: U/Rt de ventanas en educación, salud y hoteles | `ds15-2024`, num. 2.A.5 | Transcripción + OCR |
| `ds15_t13_r100_sobrecimiento_edu_salud.csv` | Tabla 13: R100 sobrecimiento | `ds15-2024`, num. 2.A.6 | Transcripción + OCR |
| `ds15_t07_t14_infiltracion_provincia.csv` | Tablas 7 y 14 (iguales): clase máx. de infiltración por provincia | `ds15-2024`, num. 1.C y 2.C | Transcripción de imagen + test de cobertura de las 56 provincias de la tabla de zonas; contraste con `ditec-lamina-rt` (C24) |
| `ds15_t08_muestra_infiltracion_residencial.csv` | Tabla 8: muestra del ensayo en terreno, residencial | `ds15-2024`, num. 1.C | Transcripción de imagen (">501" registrado como 502+) |
| `ds15_t09_t16_permeabilidad_zona.csv` | Tablas 9 y 16 (iguales): clase mín. de permeabilidad por zona | `ds15-2024`, num. 1.C y 2.C | Transcripción de imagen |
| `ds15_t15_muestra_infiltracion_educacion.csv` | Tabla 15: muestra por recintos docentes | `ds15-2024`, num. 2.C | Transcripción de imagen |
| `res1802_anexo2_rs.csv` | Rsi/Rse para cálculo de condensación | `res-ex-1802-2025`, Anexo 2 | Lectura de imagen (PDF escaneado) + OCR |
| `res1802_anexo1_clima.csv` | T°ext/HRext por zona y comuna o localidad (Anexo 1) | `res-ex-1802-2025`, Anexo 1 | `scripts/build_res1802_anexo1.py` (OCR por coordenadas) + corrección manual con las imágenes de pp. 4–11 + test de unión con `zonas_comunas.csv` |
| `res1802_macrozonas.csv` | T°ext/HRext por macrozona | `res-ex-1802-2025`, Anexo 1 (final) | Lectura de imagen + OCR |
| `pda.csv` | 643 valores de las tablas térmicas de vivienda de 11 PDA/PPA (con artículo, tabla y etapa) | 11 decretos MMA (IDs `pda-*`/`ppa-*`) | Transcripción por plan + OCR independiente por tabla; registros en `docs/pda-verificacion/` |
| `pda_planes.csv` | Comuna → plan, cobertura total/parcial, exige envolvente (sí/no) | Art. 1 de cada decreto | Lectura del texto; nombres alineados con `zonas_comunas.csv` |
| `pda_minvu_actos.csv` | 454 valores de actos MINVU que completan los PDA (Ord. 1773/2017, Ord. 209/2018, Res. Ex. 9868/2018 Temuco, Res. Ex. 1729/2019 Valdivia, Res. Ex. 9869/2018 Osorno, Ord. 840/2019) | `minvu-ord1773-2017`, `minvu-ord209-2018`, `minvu-res-ex-9869-2018`, `minvu-ord840-2019` | Transcripción de imagen + OCR; registro en `docs/pda-verificacion/minvu-actos-pda*.` |

Celdas vacías = "sin exigencia" ("---" o "-" en la tabla original). "na" en la Tabla 5 = sin valor para esa combinación.
