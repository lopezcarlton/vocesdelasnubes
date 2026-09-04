# SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES

```yaml
id: SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES
tipo: fuente_bibliografica
bib_id: BIB059
titulo: "Verb Classes in Juchitán Zapotec"
autor_o_participantes:
  - Gabriela Pérez Báez
  - Terrence Kaufman
fecha: 2016
ubicacion: "https://repository.si.edu/bitstream/handle/10088/32808/P_rez_B_ez_Gabriela-20170522-perez_baez1abx.pdf"
publicacion: "Anthropological Linguistics 58(3), 217–257"
descripcion: >
  Estudio de clasificación verbal de Juchitán basado en la revisión de más de dos mil
  verbos y en un sistema de cuatro clases. Dictionaria declara que su codificación de
  clases verbales se basa en este trabajo; por ello es una fuente subyacente relevante
  para los inventarios verbales técnicos del dispositivo.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_repositorio_smithsonian
estado_de_lectura: "ingesta_historica_recuperada + verificacion_directa_selectiva_2026-09-04"
restriccion_de_derechos: "All rights reserved; no almacenar ni reproducir tablas completas por defecto"
```

## Identidad bibliográfica

`BIB059` está confirmado por la hoja bibliográfica maestra reconciliada el 2026-09-03.

El PDF accesible desde Smithsonian corresponde al artículo publicado en *Anthropological Linguistics* 58(3), 217–257. La disponibilidad pública del archivo no se interpreta como licencia abierta para redistribuir el texto o las tablas.

## Estado de ingesta y recuperación

Antes de la separación física del dispositivo, esta fuente ya había sido explotada lingüísticamente. Sobreviven en el runtime histórico once reglas `PBK-VERB-*` / `PBK-DER-*`, con `source_id = BIB059_PBK2016` y coordenadas de sección/página. La SQLite histórica conserva además once filas en `morphology_rule_registry_v023` atribuidas a esta fuente.

Esos artefactos técnicos prueban que hubo una ingesta previa y sirven para recuperar coordenadas, pero no son autoridad bibliográfica por sí mismos.

El 2026-09-04 se hizo una **reverificación directa y selectiva del artículo original** sobre los pasajes necesarios para recuperar el núcleo de la clasificación verbal. No se releyó el PDF completo porque la tarea era reconstruir conocimiento ya estudiado, no iniciar una lectura desde cero.

```text
LEGACY_TECHNICAL_INGESTION = RECOVERY_COORDINATES
DIRECT_SOURCE_PASSAGE = AUTHORITY_FOR_NEW_ADJUDICATION
FULL_PDF_REREAD_REQUIRED_BY_DEFAULT = false
```

## Cobertura temática verificada

### §3 y tabla 5 — TAM y diagnóstico de clase

La fuente describe siete marcadores TAM en el marco de este artículo. Para **asignar clase verbal**, los datos cruciales son la interacción de la raíz con **potencial** y **completivo**. El habitual se presenta porque permite aislar la forma básica de la raíz: `ri=` aparece ante consonante y `r=` ante vocal o semivocal.

La fuente afirma además que, una vez conocida la clase del verbo, el comportamiento de los demás marcadores es predecible dentro del análisis propuesto.

### §4 y tabla 6 — sistema de cuatro clases

La clasificación distingue cuatro clases `A`, `B`, `C` y `D`.

Resumen para consulta, **parafraseado y no sustitutivo de la tabla fuente**:

- **Clase A:** completivo `be=` (con realización superficial descrita como `bi=`); potencial del tipo `gi=` con perturbación tonal.
- **Clase B:** completivo `gu=`; potencial del tipo `gi=` con perturbación tonal.
- **Clase C:** completivo `gu=`; el potencial contiene `g=` y, en raíces consonánticas, desencadena geminación/fortificación predecible de la consonante inicial.
- **Clase D:** comparte con C el patrón general de potencial, pero se distingue por una alternancia de consonante inicial en el completivo.

No usar esta paráfrasis para reconstruir automáticamente formas superficiales: la interacción entre tono, fonación, vocales y consonantes requiere los análisis específicos de cada sección.

### §4.1–4.4 — tamaño y composición

La fuente reporta aproximadamente:

- clase A: unos 1,600 verbos;
- clase B: 125 verbos atestiguados, 25 raíces;
- clase C: 237 verbos, 43 raíces;
- clase D: 294 verbos, 35 raíces básicas.

Los conteos pertenecen al dataset analizado por los autores y no deben proyectarse como frecuencias de uso conversacional.

### §4.5 — irregularidad y transición entre clases

La fuente identifica dieciséis verbos que no siguen estrictamente los patrones generales. Distingue, entre otros casos, alternancias entre clase A y otra clase, así como comportamientos segmentales inusuales. Los autores interpretan parte de las alternancias como posible transición/regularización hacia clase A.

Esto exige conservar estados como `A~B`, `A~C` u otras alternancias cuando estén documentadas, en lugar de forzar una única clase por conveniencia técnica.

### Conclusión

La conclusión vuelve a formular el sistema de cuatro clases y sostiene que permite analizar el inventario con pocas excepciones. Esta es una **afirmación analítica de los autores**; no equivale por sí sola a una decisión pedagógica sobre el orden de enseñanza.

## Notación y ortografía

La notación del artículo **no debe confundirse con la superficie ortográfica contemporánea del proyecto**.

La obra utiliza convenciones derivadas del PDLMA y, en el apéndice, explica explícitamente diferencias respecto del Alfabeto Popular. Entre ellas:

- representación analítica explícita de tono y material extramétrico;
- uso de `k/g` para velares en contextos donde la tradición basada en español/Alfabeto Popular emplea otras convenciones gráficas;
- distinción entre representación analítica y forma ortográfica práctica.

```text
PBK_ANALYTICAL_FORM != PROJECT_SURFACE_ORTHOGRAPHY
PDLMA_TO_ALFABETO_POPULAR = NOT_A_BLIND_REWRITE
```

Una raíz o paradigma copiado del artículo sirve como **dato analítico y coordenada de fuente**, no como grafía lista para materiales pedagógicos.

## Derechos y memoria persistente de lectura

El proyecto no necesita guardar el PDF dentro del repositorio para conservar lo aprendido de esta fuente. Este `SRC` registra identidad, cobertura, hechos lingüísticos parafraseados, coordenadas y límites suficientes para consultas ordinarias.

```text
ROUTINE_QUERY -> SRC + HALL/TEO/DEC
NEW_ADJUDICATION -> OPEN_RELEVANT_SOURCE_PASSAGE
FULL_SOURCE_REREAD_BY_DEFAULT = false
```

No reproducir tablas completas, largas listas tomadas literalmente del artículo ni pasajes extensos. Cuando haga falta verificar una forma concreta, volver sólo a la tabla/pasaje correspondiente.

## Relación con Dictionaria y el dispositivo

La contribución Dictionaria de Didxazá documenta 2,385 verbos y señala que su análisis de clases verbales se basa en Pérez Báez y Kaufman (2016). El dispositivo conserva `DIC_VERB_2385_v0_1.csv` como inventario técnico exacto y sus módulos históricos usan el alias `BIB059_PBK2016`.

```text
PEREZ_BAEZ_KAUFMAN_2016 = SOURCE_FOR_VERB_CLASS_ANALYSIS
DICTIONARIA = DOCUMENTARY_LEXICOGRAPHIC_SOURCE
DIC_VERB_2385 = TECHNICAL_DERIVATIVE
```

Las tres capas deben mantenerse distinguibles. Las reglas generales de clasificación se justifican en PBK2016; la atribución de una clase a un registro léxico concreto puede provenir de Dictionaria y debe conservar su propia provenance.

## Entidades de conocimiento relacionadas

- `HALL-0073` — las clases A–D se diagnostican principalmente mediante potencial y completivo;
- `HALL-0074` — el habitual permite aislar la raíz y la clase predice el comportamiento del resto del paradigma dentro del análisis;
- `HALL-0075` — distribución cuantitativa e irregularidad documentada del sistema;
- `HALL-0076` — la notación analítica de PBK2016 no equivale a superficie del Alfabeto Popular.

## Límite pedagógico

La existencia de clases verbales y la predictibilidad paradigmática **no adoptan una secuencia curricular**. No se deriva de esta fuente que los verbos deban enseñarse agrupados por clase ni que conocer una forma útil obligue a enseñar el paradigma completo.
