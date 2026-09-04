# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `SYSTEMATIC_BACKFILL_PASS_COMPLETE_TO_AVAILABLE_SOURCES / NORMA_2016_BLOCKED_BY_ACCESS`  
**Repositorio autoritativo:** `lopezcarlton/vocesdelasnubes`  
**Método:** `LAZY_TARGETED_LOADING`

## 1. Regla arquitectónica preservada

```text
SRC = SOURCE_IDENTITY + PERSISTENT_READING_MEMORY
HALL / TEO / VAL / DEC = ADJUDICATED_KNOWLEDGE
DEVICE = DERIVED_SYSTEM
```

No se creó ninguna capa conceptual paralela.

## 2. Regla de recuperación/adjudicación

```text
ROUTINE_QUERY
-> RELEVANT_HALL / TEO / DEC / VAL
-> SRC_ONLY_IF_PROVENANCE_OR_SCOPE_IS_NEEDED
-> ANSWER

NEW_OR_CHANGED_CLAIM
-> USE_LEGACY_INDEX_ONLY_TO_LOCATE_TOPIC
-> REOPEN_RELEVANT_ORIGINAL_SOURCE_PASSAGE
-> ADJUDICATE_IN_VOCES
-> UPDATE_ONLY_NECESSARY_ENTITIES/VIEWS
```

```text
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
LEGACY_DEVICE_RULE_AS_RECOVERY_INDEX = allowed
LEGACY_DEVICE_RULE_AS_KNOWLEDGE_AUTHORITY = forbidden
```

## 3. PBK2016 — COMPLETADO

`HALL-0073`–`HALL-0076`.

- cuatro clases verbales A–D;
- diagnóstico principal por potencial/completivo;
- habitual útil para aislar raíz y apoyar predictibilidad;
- notación PBK/PDLMA ≠ superficie ortográfica del proyecto.

```text
GENERAL_PBK_CLASS_QUERY_FROM_VOCES = true
DEVICE_REQUIRED_FOR_GENERAL_PBK_QUERY = false
```

## 4. Gramática Popular — P0 ESTRUCTURAL SUFICIENTE

`SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`  
Promoción principal: `HALL-0077`–`HALL-0140`.

Cobertura:

- aspecto/TAM y juegos verbales;
- persona y posesión;
- causatividad/valencia;
- imperativos y movimiento;
- negación, partículas y preguntas;
- subordinación y relativas;
- fonética del apéndice;
- frase nominal/determinación;
- preposiciones;
- oración básica/predicación/existencia;
- compuestos/frases verbales;
- conjunciones, interjecciones y cohesión narrativa.

```text
GRAMATICA_POPULAR_P0_STRUCTURAL_BACKFILL = SUFFICIENT
GRAMATICA_POPULAR_EXHAUSTIVE_SEMANTIC_INGESTA = false
```

## 5. PVM 2009/2010 + corrigendum — P0 SUFICIENTE

`HALL-0141`–`HALL-0150`.

Cobertura:

- inventario segmental;
- fortis/lenis multirrasgo;
- vibrantes;
- fonación;
- tonos vs melodías de raíz;
- acento;
- alofonía;
- fonema/alófono/grafía;
- alcance del corrigendum 2011.

Contradicción abierta:

`HALL-0150` — GP2001 vs PVM2010 sobre realización intervocálica de `b/d/g`.

```text
CHOOSE_ONE_AS_UNIVERSAL_RULE = forbidden
ALLOPHONE != SPELLING_CORRECTION
UNRESOLVED != INCORRECT
```

## 6. Xneza 2015 — P0 ESTRUCTURAL SUFICIENTE

`HALL-0151`–`HALL-0158`.

Cobertura:

- palabra fonológica;
- palabra gramatical;
- palabra ortográfica;
- compuestos vs colocaciones;
- clíticos;
- límites de prosodia/significado como diagnóstico de unión;
- superficie fonética vs transparencia morfológica;
- acento prosódico vs modelo español de tildes.

```text
PHONOLOGICAL_WORD != GRAMMATICAL_WORD != ORTHOGRAPHIC_WORD_BY_DEFAULT
CLITIC_HOSTING != AUTOMATIC_SPACING_POLICY
LINGUISTIC_ANALYSIS != PRESCRIPTIVE_NORM
```

## 7. Bueno Holle 2019 — P0 ESTRUCTURAL SUFICIENTE

`HALL-0007`, `HALL-0159`–`HALL-0167`.

Cobertura:

- complementariedad discurso espontáneo/elicitación;
- accesibilidad y forma referencial;
- tercera persona explícita/cero;
- foco de predicado/oración/argumento;
- `nga` y exhaustividad;
- tópico-comentario;
- `la` y common ground;
- unidades entonacionales;
- secuencias quiasmáticas y manejo del turno;
- tópicos marcados y cambio de referente.

```text
REFERENCE_FORM_SELECTION = DISCOURSE_SENSITIVE
FOCUS != GENERIC_EMPHASIS
TOPIC != FOCUS
la != SIMPLE_COMMA
IU != ORTHOGRAPHIC_SENTENCE_BY_DEFAULT
CORPUS_TENDENCY != CATEGORICAL_GENERATION_RULE
```

## 8. Vocabulario Pickett 2007 — P1 LEXICOGRÁFICO SUFICIENTE

`HALL-0168`–`HALL-0178`.

Cobertura de alto valor:

- ausencia lexicográfica de préstamos != ausencia de uso;
- base juchiteca + variación entre pueblos e interna a Juchitán;
- variantes con/sin `g` inicial;
- grafías de préstamos no zapotequizados;
- contradicción con Xneza sobre reglas españolas de tilde (`HALL-0172`);
- `xh-` posesivo vs `xh-` “otro”;
- forma verbal lexicográfica habitual/3SG != raíz desnuda;
- entradas españolas separadas pueden representar formas sencilla/causativa relacionadas;
- espacios editoriales de partículas != palabra gramatical;
- notación tonal interna específica de Pickett;
- `r/l` marcadas como ayudas lexicográficas para aprendices.

```text
NOT_IN_PICKETT != NOT_USED
NO_ENTRY != NEGATIVE_EVIDENCE
PRINTED_SPACE_IN_PICKETT != GRAMMATICAL_BOUNDARY_BY_DEFAULT
PICKETT_SURFACE_VERB != BARE_ROOT
PICKETT_NO_MARK != UNIVERSAL_LOW_TONE_RULE
```

## 9. Cardona 2020 + Cardona–Vicente 2025 — P1 VARIACIÓN/ESCRITURA SUFICIENTE

`HALL-0179`–`HALL-0183`.

### Cardona 2020

- núcleos de alta similitud:
  - Juchitán–Xadani;
  - San Blas Atempa–Tehuantepec;
  - Ixtaltepec–Ixtepec;
- El Espinal, Unión Hidalgo y Comitancillo = municipios de transición en el análisis dialectométrico.

### Cardona–Vicente 2025

- zonas amplias operativas:
  - sur = San Blas Atempa / Tehuantepec;
  - centro = Juchitán / Xadani / Unión Hidalgo / El Espinal;
  - norte = Comitancillo / Ixtaltepec / Ixtepec;
- la zonificación amplia no borra el estatus transicional de 2020;
- fonaciones laringizadas/rearticuladas muestran distribución regional relevante para escritura;
- el Alfabeto Popular es caracterizado por los autores como históricamente centrado en Juchitán para la discusión regional;
- enfoque multilectal = propuesta académica, no norma adoptada.

```text
JUCHITAN = PRIORITY_VARIETY
EL_ESPINAL != JUCHITAN_ALIAS
LOCAL_VARIANT != ERROR
BROAD_DIALECT_ZONE != LOCALITY
MULTILECTAL_PROPOSAL != CURRENT_ADOPTED_PROJECT_NORM
MULTILECTAL_PROPOSAL != FREE_VARIANT_INTERCHANGEABILITY
```

## 10. Norma 2016 — BLOQUEO REAL POR ACCESO

`SRC-CATA-ETAL-2016-NORMA-ESCRITURA`

Estado verificado:

```text
NORMA_2016_IDENTITY = RESOLVED
NORMA_2016_FULL_TEXT = NOT_ACCESSED
SECONDARY_QUOTATIONS != FULL_NORM
```

No reconstruir reglas desde Dictionaria, Cardona, informes institucionales ni citas indirectas.

Este bloqueo es material para cuestiones normativas aún abiertas, entre ellas:

- tratamiento contemporáneo del acento/tilde ante la contradicción Pickett 2007 ↔ Xneza 2015 (`HALL-0172`);
- alcance normativo actual de convenciones históricas del Alfabeto Popular;
- cualquier decisión que pretenda atribuirse específicamente a la Norma 2016.

## 11. Contradicciones abiertas que deben permanecer visibles

### `HALL-0150`

GP2001 vs PVM2010 sobre `b/d/g` intervocálicas.

### `HALL-0172`

Pickett 2007 vs Xneza 2015 sobre aplicar reglas españolas de acento ortográfico.

```text
CONTRADICTION != FAILURE
CONTRADICTION != CHOOSE_LATEST_AUTOMATICALLY
UNRESOLVED != INCORRECT
```

## 12. Deuda de consistencia de vista

`conocimiento/TEORIA.md` todavía debe representar explícitamente `HALL-0150` en vez de dejar una sola formulación heredada de GP2001.

```text
TEORIA_VIEW_b_d_g_CONFLICT_SYNC = PENDING
CANONICAL_HALL_CONFLICT_ALREADY_REGISTERED = true
VIEW_MUST_NOT_SILENTLY_RESOLVE_CONFLICT = true
```

La deuda es de vista, no de conocimiento canónico.

## 13. Estado del systematic semantic backfill

```text
AVAILABLE_PRIORITY_SOURCES_BACKFILLED_TO_TARGET_SUFFICIENCY = true
NORMA_2016 = BLOCKED_BY_FULL_TEXT_ACCESS
FULL_LINEAR_REREADS_PERFORMED = false
NEW_CONCEPTUAL_LAYER = false
```

A partir de este checkpoint, nuevas reaperturas deben ser dirigidas por:

- consulta concreta;
- contradicción;
- necesidad de granularidad para implementación;
- nueva fuente disponible;
- acceso al manuscrito de la Norma 2016.

## 14. Invariantes

```text
VOCES = AUTHORITY_FOR_KNOWLEDGE
DEVICE = DERIVED_IMPLEMENTATION
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD
COR001 != RULE_DISCOVERY_SOURCE
UNRESOLVED != INCORRECT
```

## 15. Rendimiento esperado

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
NORMAL_VOCES_QUERY_DOES_NOT_LOAD_DEVICE = true
```

Los `SRC` actualizados funcionan como memoria persistente de lectura y permiten responder consultas generales desde Voces sin reconstruir el dispositivo ni releer fuentes completas.
