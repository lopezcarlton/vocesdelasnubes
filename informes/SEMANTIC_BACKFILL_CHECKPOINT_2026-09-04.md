# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `ACTIVE / PBK2016_DONE / GP_P0_DONE / PVM_P0_DONE / XNEZA_P0_DONE / NEXT_P0_BUENO_HOLLE_2019`  
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

Correcciones de alto impacto:

```text
GP_PERFECT != GENERIC_PRESENT_RESULT_PERFECT
SPANISH_TENSE != DIDXAZA_ASPECT_BY_DEFAULT
POTENTIAL != CAPACITY_ONLY
UNMARKED_3RD_PERSON != ERROR
POSSESSION != SINGLE_TEMPLATE
CAUSATIVE != si_ONLY
SPANISH_SER_ESTAR != SINGLE_DIDXAZA_COPULA
SPANISH_PREPOSITION_GLOSS != UNIQUE_DIDXAZA_FORM
```

Estado:

```text
GRAMATICA_POPULAR_P0_STRUCTURAL_BACKFILL = SUFFICIENT
GRAMATICA_POPULAR_EXHAUSTIVE_SEMANTIC_INGESTA = false
REOPEN_ONLY_FOR_TARGETED_QUERY_CONTRADICTION_OR_MISSING_GRANULARITY = true
```

## 5. P0-B Pickett–Villalobos–Marlett 2009/2010 + corrigendum — SUFICIENTE

Fuentes conservadas por separado:

- `SRC-PICKETT-VILLALOBOS-MARLETT-2009-ZAPOTECO-ISTMO-JUCHITAN` = BIB016, versión española;
- `SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS` = BIB061, publicación JIPA;
- corrigendum JIPA 2011, DOI `10.1017/S0025100311000053`, vinculado a BIB061.

Promovido: `HALL-0141`–`HALL-0150`.

Cobertura:

- inventario segmental juchiteco;
- fortis/lenis como oposición multirrasgo;
- trill/tap y rareza léxica de la trill;
- cinco vocales + fonación modal/cortada/laringizada;
- tres tonos fonémicos vs propuesta tentativa de cinco melodías de raíz nominal;
- acento, peso y clíticos;
- alofonía contextual;
- separación fonema/alófono/grafía;
- alcance exacto del corrigendum.

Discrepancia abierta:

`HALL-0150` registra que GP2001 niega la fricativización intervocálica de `b/d/g` al estilo español, mientras PVM2010 documenta realizaciones lenis frecuentemente fricativas o aproximantes intervocálicamente.

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

- palabra fonológica centrada en raíz y propiedades segmentales/prosódicas;
- palabra gramatical;
- pruebas de compuestos por contigüidad, argumentos y hospedaje de clíticos;
- distinción compuesto/colocación;
- límites de orden fijo, prosodia y significado convencional como diagnósticos;
- palabra ortográfica como problema de convención, no consecuencia automática de otra capa;
- clíticos `má=` y `ca'` como casos que rompen reglas simples de espaciado;
- superficie fonética vs transparencia morfológica en compuestos;
- crítica a usar las reglas españolas de tilde para representar el acento prosódico del diidxazá.

Regla central:

```text
PHONOLOGICAL_WORD != GRAMMATICAL_WORD != ORTHOGRAPHIC_WORD_BY_DEFAULT
TOKEN_BOUNDARY != PHONOLOGICAL_BOUNDARY_BY_DEFAULT
CLITIC_HOSTING != AUTOMATIC_SPACING_POLICY
PHONETIC_REDUCTION != AUTOMATIC_SPELLING_NORMALIZATION
LINGUISTIC_ANALYSIS != PRESCRIPTIVE_NORM
```

Estado:

```text
XNEZA2015_P0_STRUCTURAL_BACKFILL = SUFFICIENT
XNEZA2015_EXHAUSTIVE_EXAMPLE_INGESTA = false
REOPEN_FOR = TARGETED_ORTHOGRAPHIC_QUERY | EXACT_EXAMPLE | CONTRADICTION | IMPLEMENTATION_GRANULARITY
```

## 7. Siguiente P0 — Bueno Holle 2019

`SRC-BUENO-HOLLE-2019`

Objetivo dirigido:

- fonología/prosodia sólo donde aporte algo no cubierto o contradiga PVM/Xneza;
- metodología y naturaleza del corpus;
- referencia y seguimiento discursivo;
- tópico/foco y estructura informativa;
- clíticos/realización cuando cambien análisis;
- consecuencias reales para Analyzer, Tutor y Generator.

No releer linealmente la obra si el `SRC` y los índices permiten localizar los bloques pertinentes.

## 8. Fuentes posteriores

Después de Bueno Holle 2019:

- P1 Vocabulario Pickett — notas gramaticales/ortográficas reutilizables;
- P1 Cardona 2020 + Cardona–Vicente 2025 — variación dialectal y escritura;
- P0 Norma 2016 — bloqueado hasta tener acceso al texto completo; no reconstruir desde citas indirectas.

## 9. Invariantes

```text
VOCES = AUTHORITY_FOR_KNOWLEDGE
DEVICE = DERIVED_IMPLEMENTATION
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD
COR001 != RULE_DISCOVERY_SOURCE
UNRESOLVED != INCORRECT
NEW_CONCEPTUAL_LAYER = false
```

## 10. Estado de rendimiento

El objetivo del backfill es que consultas generales puedan responderse desde Voces con pocos archivos:

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
NORMAL_VOCES_QUERY_DOES_NOT_LOAD_DEVICE = true
```

Los `SRC` actualizados funcionan como memoria persistente para localizar rápidamente qué ya fue estudiado y qué requiere reabrir la fuente original.
