# Guía de uso

Tres casos completos. Los dos primeros son conversaciones con el agente; el tercero genera un informe. Instala primero la skill ([instrucciones](instalacion.md)).

> [!WARNING]
> Los valores de esta guía se revisaron contra `skills/rt-chile/data/` el 2026-11-05 y pueden cambiar. Verifícalos en la fuente oficial antes de usarlos.

## Qué conviene incluir en la pregunta

| Dato | Para qué sirve |
|---|---|
| **Uso** (vivienda, hotel, educación, salud) | Define las tablas y las exenciones |
| **Comuna** | Da la zona, la provincia y el plan de descontaminación |
| **Altitud o meridiano** | Solo en comunas multizona |
| **Fecha de ingreso del permiso** | Define si rige el DS 15, la etapa del plan y la vigencia del LOSCAT |
| **Capas, U de ventanas y superficies** | Permiten calcular y comparar |

Si falta algo, la skill lo pide o responde con supuestos declarados. Revisa siempre esos supuestos.

## Caso 1: vivienda en una comuna con PDA

**Pregunta al agente:**

> Vivienda nueva en Temuco, permiso a ingresar en noviembre de 2026. ¿Qué exigencias térmicas aplican y qué documentos necesito?

**Qué debe hacer la skill:**

1. **Zona:** F, comuna completa.
2. **Plan:** detecta el PDA de Temuco y Padre Las Casas (DS 8/2023), cuyas tablas prevalecen en vivienda.
3. **Exigencias:** muro U ≤ 0,45, techumbre U ≤ 0,28, piso ventilado U ≤ 0,50 y ventana U ≤ 3,20, más la Res. Ex. 9868/2018 (Art. 27, Tabla N° 10).
4. **Condiciones propias del plan:** toma del plan las muestras de infiltración, los sellos y la humedad de condensación, no las del DS 15.
5. **Documentos:** separa lo del permiso (OGUC 5.1.6 N° 11) de lo de la recepción (5.2.6 N° 7).

**Qué debes revisar tú:** la etapa del plan según tu fecha, la vigencia de la ficha LOSCAT que uses y las condiciones del Art. 27 en el decreto.

También puedes consultarlo directo: `python skills/rt-chile/scripts/pda.py Temuco`

## Caso 2: colegio en una comuna multizona

**Pregunta al agente:**

> Colegio en Arica. ¿Qué valores aplican?

**Qué debe hacer la skill:** como Arica tiene varias zonas según la altitud, pide ese dato o responde por escenarios. Con *"a 350 msnm"*, resuelve:

| Elemento | Exigencia | Fuente |
|---|---|---|
| Zona | A (bajo 1.100 m) | Tabla MINVU de zonas |
| Techumbre, muro y piso ventilado | U ≤ 0,84, 2,00 y 3,60 | DS 15, Tabla 10 |
| Ventanas | U ≤ 5,80 | DS 15, Tabla 12 |
| Condensación | Memoria de cálculo; clima 13,6 °C y 73 % HR | Res. Ex. 1802, Anexo 1 |
| Infiltración | Sin exigencia en la provincia de Arica | DS 15, Tabla 14 |
| Ventilación | Informe de tasa por NCh 3308 | DS 15, num. 2.D |

El contraste importa: si fuera una vivienda se usaría la Tabla 1, con otros valores; si fuera un recinto de salud, estaría eximido de ventilación.

## Caso 3: informe de un proyecto

Puedes pedirle al agente *"prepárame un informe térmico de este proyecto"* y entregarle los datos, o generarlo tú:

**1. Describe el proyecto en un archivo YAML.** Parte desde [este ejemplo](../skills/rt-chile/examples/proyecto-ejemplo.yaml):

```yaml
nombre: "Vivienda de ejemplo (ficticia)"
uso: residencial
comuna: "Santiago"
fecha_ingreso: 2026-11-05
lote_viviendas: 24
elementos:
  - elemento: muro
    capas:
      - {nombre: "EPS", e_m: 0.04, lambda: 0.038, fuente: "ficha del fabricante"}
      # ... resto de las capas, de interior a exterior
ventanas:
  opcion: pct
  orientaciones:
    - {orientacion: Sur, sup_paramentos_m2: 30, sup_ventanas_m2: 16, u_ventana: 3.6}
```

**2. Genera el borrador:**

```bash
python skills/rt-chile/scripts/informe.py mi-proyecto.yaml --salida informe.md
```

**3. Lee el resumen.** Con el ejemplo completo del repo se obtiene:

| Verificación | Estado | Detalle |
|---|---|---|
| A. Muro perimetral | Cumple | U 0,634 / máx. 0,8 |
| A. Techumbre | Cumple | U 0,35 / máx. 0,38 |
| A. Ventanas | **No cumple** | opción pct |
| B. Condensación | Por acreditar | Memoria NCh 1973 + Res. Ex. 1802 |
| C. Infiltración | Por acreditar | Ensayo NCh 3295 en obra terminada, para la recepción |
| C. Permeabilidad | Por acreditar | Ensayo NCh 3296/3297 o LOSCAT |
| D. Ventilación | Por acreditar | Informe de tasa |

Aquí la fachada sur tiene 53,3 % de ventanas frente al máximo de 40 % (Tabla 3, zona D, U ≤ 3,6). Las opciones son reducir la superficie vidriada, usar una ventana de mejor U o evaluar la opción Upvm.

**4. Completa lo que falta.** El informe lista los datos faltantes y los supuestos, como las capas sin fuente declarada o los elementos no entregados.

**Límites del informe:**

- Es un **borrador editable**: no es una memoria de cálculo y no se firma.
- Nunca declara que el proyecto cumple en su totalidad: la condensación, la infiltración y la ventilación se acreditan con sus propios documentos.
- En vivienda con PDA, usa los U del plan, pero las ventanas debes contrastarlas con sus tablas (`scripts/pda.py`).
- El cálculo de U usa las conductividades que tú entregas y no considera puentes térmicos.

## Otros comandos útiles

```bash
python skills/rt-chile/scripts/zona.py Mostazal --altitud 600   # zona, provincia, PDA y clima
python skills/rt-chile/scripts/pda.py Valdivia                  # todas las exigencias del plan
python skills/rt-chile/scripts/checklist.py mi-proyecto.yaml    # exigencias y documentos
python skills/rt-chile/scripts/u_check.py complejo.json         # U de un complejo multicapa
python skills/rt-chile/scripts/ventanas.py ventanas.json        # % de ventanas o Upvm
```

Los archivos YAML requieren `pyyaml`; también se aceptan JSON sin dependencias.

## Si encuentras un error

Repórtalo con la pregunta, el agente, la respuesta y la fuente que la contradice. Instrucciones en [CONTRIBUTING.md](../CONTRIBUTING.md).
