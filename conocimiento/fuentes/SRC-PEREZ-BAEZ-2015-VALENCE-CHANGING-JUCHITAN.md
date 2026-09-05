# SRC-PEREZ-BAEZ-2015-VALENCE-CHANGING-JUCHITAN

```yaml
id: SRC-PEREZ-BAEZ-2015-VALENCE-CHANGING-JUCHITAN
tipo: fuente_bibliografica
bib_id: BIB060
titulo: "Morphological valence-changing processes in Juchitán Zapotec"
autor_o_participantes:
  - Gabriela Pérez Báez
fecha: 2015
ubicacion: "https://doi.org/10.1075/tsl.110.06per"
doi: "10.1075/tsl.110.06per"
descripcion: >
  Capítulo de Gabriela Pérez Báez, pp. 93–116, en Valence Changes in Zapotec:
  Synchrony, diachrony, typology, editado por Natalie Operstein y Aaron Huey Sonnenschein.
  Presenta un análisis sincrónico detallado de procesos morfológicos de cambio de
  valencia en zapoteco de Juchitán.
nivel_de_fuente: primaria
estado_de_acceso: fuente_directamente_revisada
fecha_revision_directa: 2026-09-05
autoridad: LINGUISTICA_PRIMARIA
hallazgos_derivados:
  - HALL-0188
  - HALL-0189
  - HALL-0190
  - HALL-0191
  - HALL-0193
```

## Identidad bibliográfica

`BIB060` está confirmado por la hoja bibliográfica maestra y por la ficha editorial del capítulo. La revisión directa del 2026-09-05 se hizo sobre el texto completo de una copia de autor localizada en línea, contrastando identidad, DOI, paginación y metadatos con la ficha editorial.

## Conocimiento recuperado directamente

La fuente permite adjudicar, sin depender del antiguo núcleo técnico, cinco conjuntos de afirmaciones:

1. la morfología de cambio de valencia ocupa posiciones auxiliares y/o derivativas distintas de la posición TAM;
2. las raíces vocálicas se organizan en los grupos analíticos V1–V3, con díadas o tríadas y patrones mediopasivos/causativos documentados;
3. las raíces consonánticas se organizan en C1–C4 según recursos causativos documentados, incluyendo `-g-`, `-u-`, `-u-g-` y concatenaciones mayores;
4. la variación entre hablantes, la productividad desigual y los verbos equipolentes impiden convertir estos patrones en reglas productivas universales;
5. las tablas del capítulo identifican miembros concretos de múltiples díadas y tríadas, por lo que algunas relaciones específicas entre formas pueden recuperarse directamente de la fuente en vez de inferirse por parecido superficial.

La tesis central de la autora incluye analizar reflejos de *o-, especialmente `-u-`, como morfología causativa y no simplemente como material de un alomorfo habitual. Esto mantiene separadas la derivación causativa y la flexión TAM.

## Coordenadas de recuperación

```text
§3 + plantilla verbal + Tabla 2          -> separación TAM / AUX / DER / ROOT
§4.1 + Tabla 5                           -> miembros concretos V1
§4.2 + Tabla 6                           -> miembros concretos V2
§4.3 + Tabla 7                           -> miembros concretos V3
§4.4 + Tabla 8                           -> síntesis V1–V3
§5.1 + Tabla 9                           -> miembros concretos C1
§5.2 + Tabla 10                          -> miembros concretos C2
§5.3 + Tabla 11                          -> miembros concretos C3
§5.4 + Tabla 12                          -> miembros concretos C4
§5.5 + Tablas 13–14                      -> síntesis C1–C4 y excepciones
§6 + Tablas 15–16                        -> equipolentes y triada con variación de aceptabilidad
§7 + Tablas 17–18                        -> síntesis general y morfemas causativos
notas y juicios de aceptabilidad         -> variación entre hablantes / productividad desigual
```

Estas coordenadas son índices de recuperación; no sustituyen al pasaje fuente cuando haya que adjudicar una forma o verbo concreto.

## Derivado selectivo de relaciones concretas

Para que el conocimiento explícito de las tablas sea recuperable sin reproducir el capítulo, se creó:

`conocimiento/derivados/PB2015_VALENCY_RELATIONS_SELECTED_v0_1.csv`

El derivado es **selectivo, no exhaustivo**. Conserva `relation_set_id`, tabla/página, grupo fuente, papel del miembro, forma analítica PDLMA, glosa, clase/valencia sólo cuando la fuente las hace recuperables y notas de variación o aceptabilidad. No contiene formas AP generadas ni relaciones deducidas por semejanza.

```text
SELECTED_RELATION_REGISTRY = SOURCE_RECOVERY_DERIVATIVE
SELECTED_RELATION_REGISTRY != SECOND_LINGUISTIC_AUTHORITY
MEMBERSHIP_COMES_FROM_PB2015_TABLE_OR_IMMEDIATE_DISCUSSION = true
NO_MEMBER_IN_SELECTED_REGISTRY != NEGATIVE_EVIDENCE
```

La evidencia promovida sobre estas relaciones concretas se formaliza en `HALL-0193`.

## Restricción de representación

La propia fuente declara que usa convenciones PDLMA que difieren de la ortografía práctica. Por tanto:

```text
PB2015_ANALYTICAL_FORM != PROJECT_ORTHOGRAPHIC_SURFACE
PDLMA_MORPHEME_SEQUENCE != AUTOMATIC_ALFABETO_POPULAR_FORM
DOCUMENTED_DERIVATIONAL_PATTERN != PRODUCTIVE_RULE
VALENCY_COMPATIBILITY != CORRECTION_LICENSE
SOURCE_VARIATION != ERROR
```

## Relación con el dispositivo

`JUCHITAN_LINGUISTIC_CORE_v0_27` y Morphology II habían citado este trabajo al describir causatividad y derivación. Esas implementaciones históricas siguen siendo derivadas y no son autoridad lingüística:

```text
TECHNICAL_CAUSATIVE_RULE != SOURCE
PEREZ_BAEZ_2015_VALENCE = SOURCE
```

A partir de `HALL-0188`–`HALL-0191`, el dispositivo puede consumir la arquitectura general como análisis y compatibilidad. `HALL-0193` permite además exponer relaciones concretas cuando la identidad con un miembro fuente haya sido resuelta independientemente. Esto no autoriza asignar un verbo nuevo a V1–V3/C1–C4 por parecido superficial ni generar causativos no documentados.

## Derechos y distribución

La copia consultada reproduce aviso de copyright de John Benjamins. No se incorpora ni redistribuye el PDF completo en este repositorio. Voces conserva identidad bibliográfica, coordenadas, paráfrasis y un derivado factual selectivo de relaciones necesario para recuperación y adjudicación; no se reproduce de manera exhaustiva el contenido tabular del capítulo.
