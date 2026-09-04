# SRC-BUENO-HOLLE-2019

```yaml
id: SRC-BUENO-HOLLE-2019
tipo: fuente_bibliografica
bib_id: BIB065
titulo: "Information structure in Isthmus Zapotec narrative and conversation"
autor_o_participantes:
  - Juan José Bueno Holle
fecha: 2019
ubicacion: "https://langsci-press.org/catalog/book/219"
doi: "10.5281/zenodo.2538324"
licencia: "CC BY 4.0"
ubicacion_copia_trabajo: "archivo digital de trabajo del proyecto"
sha256_copia_trabajo: "fd3f5a8705d63a5a1b2849870ff51b16978e6307eb7d935af9d9573be2f4aff5"
descripcion: >
  Monografía de acceso abierto sobre estructura informativa en zapoteco del Istmo,
  basada en trabajo de campo en Juchitán. Relevante para metodología de corpus,
  discurso, prosodia, tópico/foco, elicitación y análisis de conversación.
  La fuente puede localizarse y leerse directamente desde Voces sin ejecutar el dispositivo.
nivel_de_fuente: primaria
estado_de_acceso: disponible_abierto
estado_de_ingesta: semantic_backfill_p0_sufficient_2026-09-04
```

`BIB065` está confirmado por la hoja bibliográfica maestra reconciliada el 2026-09-03.

## Memoria persistente de lectura — backfill P0 2026-09-04

### Ortografía y tono ya recuperados

La obra usa una ortografía basada en el Alfabeto Popular de 1956, no marca tono en la línea ortográfica principal y mantiene la información tonal en la representación analítica. Documenta además la relación contextual `xh/x`.

→ `HALL-0067`, `HALL-0068`.

### Metodología de evidencia

Bueno Holle reporta 17 meses de trabajo de campo en Juchitán y combina:

- habla espontánea grabada;
- elicitación controlada;
- juicios de hablantes;
- transcripción, glosa, traducción y análisis;
- estímulos no lingüísticos como juegos, imágenes y videos.

El discurso espontáneo y la elicitación se presentan como fuentes complementarias con fortalezas distintas.

→ `HALL-0007`.

```text
SPONTANEOUS_DISCOURSE != SUFFICIENT_FOR_ALL_RARE_STRUCTURES
ELICITATION != SUBSTITUTE_FOR_NATURAL_DISCOURSE
PRIMARY_RECORDING != LATER_ANALYTIC_LAYER
```

### Accesibilidad y referencia

- frases nominales léxicas se correlacionan inversamente con saliencia/accesibilidad del referente; es tendencia del corpus, no regla categórica → `HALL-0159`;
- tercera persona explícita/cero está condicionada por sintaxis, correferencia y organización discursiva; forma cero no equivale a sujeto ausente → `HALL-0160`.

```text
REFERENCE_FORM_SELECTION = DISCOURSE_SENSITIVE
CORPUS_TENDENCY != CATEGORICAL_GENERATION_RULE
OVERT_3RD != ZERO_3RD_FREE_VARIATION
ZERO_FORM != MISSING_SUBJECT
```

### Foco

- foco de predicado y foco de oración son consistentemente verbo-iniciales en los datos estudiados;
- foco de argumento puede usar constituyente preverbal o, en ciertos casos, alternativa verbo-inicial;
- no se identifica un pitch accent especial que por sí mismo marque foco → `HALL-0161`;
- `nga` en construcciones de foco de argumento aporta lectura exhaustiva; foco sin `nga` no implica esa exhaustividad → `HALL-0162`.

```text
FOCUS != GENERIC_EMPHASIS
FOCAL_MATERIAL != SPECIAL_PITCH_ACCENT_BY_DEFAULT
nga != GENERIC_EMPHASIS_PARTICLE_BY_DEFAULT
```

### Tópico

- la construcción tópico-comentario no marcada es verbo-inicial y el sujeto tópico puede aparecer como enclítico; tópico no equivale automáticamente a constituyente preverbal → `HALL-0163`;
- tópicos marcados con pronombre independiente pueden ocupar una IU previa; en la muestra discutida `la` aparece al final en 23/25 casos y éstos se asocian frecuentemente con cambio de sujeto/tópico → `HALL-0167`.

```text
TOPIC_COMMENT != TOPICALIZATION
TOPIC != SIMPLY_PREVERBAL_NP
CORPUS_TENDENCY != CATEGORICAL_TOPIC_RULE
```

### Partícula `la`

Bueno Holle analiza `la` como recurso interactivo de gestión del common ground / try-marking. La misma superficie participa en tópicos, cláusulas adverbiales y preguntas sí/no.

→ `HALL-0164`.

```text
la != SIMPLE_COMMA
la != YES_NO_QUESTION_PARTICLE_ONLY
la = INTERACTIONAL_COMMON_GROUND_RESOURCE_IN_BH_ANALYSIS
```

### Unidades entonacionales

La IU es una unidad prosódica de transcripción/análisis. Tiende a coincidir con cláusulas simples, mientras ciertos tópicos marcados pueden ocupar una IU separada.

→ `HALL-0165`.

```text
IU_TENDS_TO_OVERLAP_SIMPLE_CLAUSE = true
IU != ORTHOGRAPHIC_SENTENCE_BY_DEFAULT
IU != COR002_PEDAGOGICAL_CONVERSATION_UNIT
```

### Estructura informativa y manejo del turno

Una secuencia documentada de foco de predicado seguida de foco de argumento puede formar una organización quiasmática entre dos IUs, prolongar el turno y usar la segunda IU para marcar cierre o cesión del piso.

→ `HALL-0166`.

```text
CHIastic_SEQUENCE_CAN_EXTEND_TURN = true
SECOND_IU_CAN_MARK_TURN_COMPLETION = true
CHIastic_SEQUENCE != DEFAULT_EMPHATIC_TEMPLATE
```

## Consecuencias para Analyzer / Tutor / Generator

```text
DISCOURSE_CONTEXT_REQUIRED_FOR_REFERENCE_RESOLUTION = true
INFORMATION_STRUCTURE_REQUIRED_BEFORE_WORD_ORDER_JUDGMENT = true
PREVERBAL_CONSTITUENT != ERROR_BY_DEFAULT
TOPIC != FOCUS
FOCUS != EMPHASIS
COMMON_GROUND_STATE_CAN_MATTER = true
PROSODIC_BOUNDARY != ORTHOGRAPHIC_BOUNDARY_BY_DEFAULT
```

Generator debe partir de intención discursiva, accesibilidad de referentes, tópico/foco y estado de interacción antes de escoger forma pronominal, orden o partículas. Tutor debe explicar forma gramatical, estructura informativa y función conversacional como capas distintas.

## Relación con artefactos técnicos históricos

`BIB065_BUENO_HOLLE_INGESTION_MATRIX` y derivados históricos sirven únicamente como coordenadas de recuperación.

```text
BIB065_MATRIX_AS_COORDINATES = allowed
BIB065_MATRIX_AS_CLAIM_SUMMARY = not_authoritative
SOURCE_PASSAGE_MUST_BE_OPENED_BEFORE_ADJUDICATION = true
```

## Estado

```text
BUENO_HOLLE_2019_P0_STRUCTURAL_BACKFILL = SUFFICIENT
BUENO_HOLLE_EXHAUSTIVE_EXAMPLE_INGESTA = false
FULL_LINEAR_REREAD_REQUIRED = false
REOPEN_FOR = TARGETED_DISCOURSE_QUERY | EXACT_EXAMPLE | CONTRADICTION | IMPLEMENTATION_GRANULARITY
```

Las observaciones de corpus no se convierten automáticamente en norma pedagógica, gramatical universal o regla categórica de generación.
