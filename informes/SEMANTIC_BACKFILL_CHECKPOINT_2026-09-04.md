# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `ACTIVE / PBK2016_DONE / GP_P0_DONE / PVM_P0_DONE / XNEZA_P0_DONE / BUENO_HOLLE_P0_DONE / NEXT_P1_PICKETT_VOCABULARIO`  
**Repositorio autoritativo:** `lopezcarlton/vocesdelasnubes`  
**Método:** `LAZY_TARGETED_LOADING`

## 1. Problema que resuelve este frente

La separación física reveló que varias fuentes lingüísticas estaban identificadas en Voces mientras parte de su conocimiento reutilizable sobrevivía principalmente en compilaciones técnicas históricas.

```text
SOURCE_IDENTITY_MIGRATED = YES
LEGACY_TECHNICAL_EXTRACTIONS_EXIST = YES
CANONICAL_SEMANTIC_PROMOTION_TO_VOCES = INCOMPLETE
```

La reparación conserva la arquitectura vigente:

```text
SRC = SOURCE_IDENTITY + PERSISTENT_READING_MEMORY
HALL / TEO / VAL / DEC = ADJUDICATED_KNOWLEDGE
DEVICE = DERIVED_SYSTEM
```

No se crean capas conceptuales nuevas.

## 2. Regla operativa

### Consulta rutinaria

```text
ROUTINE_QUERY
-> RELEVANT_HALL / TEO / DEC / VAL
-> SRC_ONLY_IF_PROVENANCE_OR_SCOPE_IS_NEEDED
-> ANSWER
```

### Nueva adjudicación

```text
NEW_OR_CHANGED_CLAIM
-> USE_LEGACY_INDEX_ONLY_TO_LOCATE_TOPIC
-> REOPEN_RELEVANT_ORIGINAL_SOURCE_PASSAGE
-> ADJUDICATE_IN_VOCES
-> UPDATE_ONLY_NECESSARY_SRC / HALL / VIEW
-> SYNC_MINIMAL_DERIVED_DEVICE_REPRESENTATION_IF_NEEDED
```

```text
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
LEGACY_DEVICE_RULE_AS_RECOVERY_INDEX = allowed
LEGACY_DEVICE_RULE_AS_KNOWLEDGE_AUTHORITY = forbidden
```

## 3. Piloto PBK2016 — COMPLETADO

`SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES`

Promovido:

- `HALL-0073` — cuatro clases A–D, diagnosticadas principalmente por potencial y completivo;
- `HALL-0074` — habitual como vía para aislar la raíz y apoyar predictibilidad del paradigma una vez conocida la clase;
- `HALL-0075` — distribución e irregularidad;
- `HALL-0076` — notación analítica PBK/PDLMA ≠ superficie ortográfica del proyecto.

```text
GENERAL_PBK_CLASS_QUERY_FROM_VOCES = true
DEVICE_REQUIRED_FOR_GENERAL_PBK_QUERY = false
```

## 4. P0-A Gramática Popular — SUFICIENCIA ESTRUCTURAL

`SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`

Promoción canónica principal: `HALL-0077`–`HALL-0140`.

Cobertura estructural adjudicada:

- aspecto/TAM y juegos verbales;
- persona independiente/dependiente;
- posesión;
- causatividad y valencia;
- imperativos y movimiento;
- negación, partículas y preguntas;
- coordinación, subordinación y relativas;
- apéndice fonético;
- frase nominal/determinación;
- preposiciones y relaciones espaciales;
- oración básica, predicación, existencia y meteorología;
- verbos compuestos y frases verbales;
- conjunciones, interjecciones y cohesión narrativa.

```text
GRAMATICA_POPULAR_P0_STRUCTURAL_BACKFILL = SUFFICIENT
GRAMATICA_POPULAR_EXHAUSTIVE_SEMANTIC_INGESTA = false
```

## 5. P0-B Pickett–Villalobos–Marlett 2009/2010 + corrigendum — SUFICIENTE

Fuentes conservadas por separado:

- `SRC-PICKETT-VILLALOBOS-MARLETT-2009-ZAPOTECO-ISTMO-JUCHITAN` = BIB016;
- `SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS` = BIB061;
- corrigendum JIPA 2011, DOI `10.1017/S0025100311000053`.

Promovido: `HALL-0141`–`HALL-0150`.

Cobertura:

- inventario segmental;
- fortis/lenis multirrasgo;
- vibrantes;
- fonación;
- tono y melodías de raíz;
- acento;
- alofonía;
- capas fonema/alófono/grafía;
- alcance del corrigendum.

Discrepancia abierta:

`HALL-0150` conserva el desacuerdo GP2001/PVM2010 sobre `b/d/g` intervocálicas.

```text
BIBLIOGRAPHIC_DISCREPANCY_b_d_g = OPEN
CHOOSE_ONE_AS_UNIVERSAL_RULE = forbidden
ALLOPHONE != SPELLING_CORRECTION
UNRESOLVED != INCORRECT
```

## 6. P0-C Xneza diidxazá 2015 — SUFICIENCIA ESTRUCTURAL

`SRC-PEREZ-BAEZ-CATA-BUENO-HOLLE-2015-XNEZA`

Promovido: `HALL-0151`–`HALL-0158`.

Cobertura:

- palabra fonológica;
- palabra gramatical;
- compuestos y colocaciones;
- clíticos;
- palabra ortográfica;
- límites de prosodia/significado como diagnóstico de unión;
- superficie fonética vs transparencia morfológica;
- acento prosódico vs reglas españolas de tilde.

```text
PHONOLOGICAL_WORD != GRAMMATICAL_WORD != ORTHOGRAPHIC_WORD_BY_DEFAULT
TOKEN_BOUNDARY != PHONOLOGICAL_BOUNDARY_BY_DEFAULT
CLITIC_HOSTING != AUTOMATIC_SPACING_POLICY
PHONETIC_REDUCTION != AUTOMATIC_SPELLING_NORMALIZATION
LINGUISTIC_ANALYSIS != PRESCRIPTIVE_NORM
```

## 7. P0-D Bueno Holle 2019 — SUFICIENCIA ESTRUCTURAL

`SRC-BUENO-HOLLE-2019`

La metodología básica ya estaba promovida en `HALL-0007`; el backfill dirigido añadió `HALL-0159`–`HALL-0167`.

Cobertura:

- forma referencial sensible a saliencia/accesibilidad → `HALL-0159`;
- tercera persona explícita/cero condicionada por sintaxis y organización discursiva → `HALL-0160`;
- foco de predicado/oración vs foco de argumento → `HALL-0161`;
- `nga` y lectura exhaustiva en foco de argumento → `HALL-0162`;
- tópico-comentario no marcado verbo-inicial → `HALL-0163`;
- `la` como recurso de common ground / try-marking → `HALL-0164`;
- unidad entonacional como capa prosódica con fuerte solapamiento con cláusula simple → `HALL-0165`;
- secuencia quiasmática foco de predicado + foco de argumento y manejo del turno → `HALL-0166`;
- tópicos pronominales marcados en IU previa y fuerte coocurrencia con `la` en la muestra estudiada → `HALL-0167`.

```text
REFERENCE_FORM_SELECTION = DISCOURSE_SENSITIVE
OVERT_3RD != ZERO_3RD_FREE_VARIATION
FOCUS != GENERIC_EMPHASIS
TOPIC != FOCUS
TOPIC != SIMPLY_PREVERBAL_NP
nga != GENERIC_EMPHASIS_PARTICLE_BY_DEFAULT
la != SIMPLE_COMMA
IU != ORTHOGRAPHIC_SENTENCE_BY_DEFAULT
IU != COR002_PEDAGOGICAL_CONVERSATION_UNIT
CORPUS_TENDENCY != CATEGORICAL_GENERATION_RULE
```

Estado:

```text
BUENO_HOLLE_2019_P0_STRUCTURAL_BACKFILL = SUFFICIENT
BUENO_HOLLE_EXHAUSTIVE_EXAMPLE_INGESTA = false
REOPEN_FOR = TARGETED_DISCOURSE_QUERY | EXACT_EXAMPLE | CONTRADICTION | IMPLEMENTATION_GRANULARITY
```

## 8. Deuda de consistencia de vista

`conocimiento/TEORIA.md` conserva todavía una formulación heredada del Apéndice de GP2001 según la cual `b/d/g` no presentan fricativización intervocálica al estilo español. Desde el backfill PVM existe `HALL-0150`, que documenta la discrepancia con PVM2010.

La vista deberá actualizarse para representar **la discrepancia abierta**, no para escoger una de las dos descripciones.

```text
TEORIA_VIEW_b_d_g_CONFLICT_SYNC = PENDING
CANONICAL_HALL_CONFLICT_ALREADY_REGISTERED = true
VIEW_MUST_NOT_SILENTLY_RESOLVE_CONFLICT = true
```

Esta deuda de vista no bloquea el siguiente backfill porque el conocimiento canónico y su estado de incertidumbre ya están correctamente registrados.

## 9. Siguiente frente — P1 Vocabulario Pickett

`SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO`

Objetivo dirigido:

- promover notas gramaticales y ortográficas reutilizables que actualmente sobrevivan principalmente como backfills técnicos o notas lexicográficas;
- priorizar excepciones, variantes, restricciones de uso y convenciones que cambien Analyzer/Corrector/Tutor/Generator;
- no copiar el vocabulario completo a HALL;
- no convertir una entrada lexicográfica aislada en regla productiva.

Después:

- P1 Cardona 2020 + Cardona–Vicente 2025 — variación dialectal y escritura;
- Norma 2016 — sigue bloqueada hasta acceso al texto completo; no reconstruir desde citas indirectas.

## 10. Invariantes

```text
VOCES = AUTHORITY_FOR_KNOWLEDGE
DEVICE = DERIVED_IMPLEMENTATION
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD
COR001 != RULE_DISCOVERY_SOURCE
UNRESOLVED != INCORRECT
NEW_CONCEPTUAL_LAYER = false
```

## 11. Estado de rendimiento

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
NORMAL_VOCES_QUERY_DOES_NOT_LOAD_DEVICE = true
```

Los `SRC` actualizados funcionan como memoria persistente para localizar rápidamente qué ya fue estudiado y qué requiere reabrir la fuente original.
