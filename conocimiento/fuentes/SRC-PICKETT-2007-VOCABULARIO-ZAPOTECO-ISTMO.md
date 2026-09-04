# SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO

```yaml
id: SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO
tipo: fuente_bibliografica
titulo: "Vocabulario zapoteco del Istmo: Español-zapoteco y zapoteco-español"
autor_o_participantes:
  - Velma B. Pickett
fecha: 2007
bib_id: BIB003
edicion: "Quinta edición electrónica"
ubicacion: "https://mexico.sil.org/es/resources/archives/35335"
archivo_publicado: "Imagezai_vocabulario_ed5.2.pdf"
descripcion: >
  Vocabulario bilingüe de zapoteco del Istmo, con aproximadamente 2000 entradas,
  distintas acepciones, formas derivadas y notas gramaticales. La ficha editorial
  identifica Juchitán, Istmo de Tehuantepec, Oaxaca, como ámbito de la variedad.
  Los backfills y léxicos técnicos construidos para el dispositivo son derivados y
  no sustituyen este objeto documental.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: semantic_backfill_p1_lexicographic_sufficient_2026-09-04
```

## Identidad y alcance

- Instituto Lingüístico de Verano, A.C.
- xiv, 129 páginas.
- Serie de vocabularios y diccionarios indígenas "Mariano Silva y Aceves", 3.
- Quinta edición electrónica, 2007.
- El propio Apéndice III declara que el vocabulario está basado en el habla de Juchitán y reconoce variación interna y entre pueblos.

## Memoria persistente de lectura — P1 2026-09-04

### Cobertura lexicográfica y préstamos

`HALL-0168`:

El Vocabulario omite deliberadamente muchos préstamos españoles que no han sufrido modificación o que sólo presentan adaptaciones regulares. Por tanto:

```text
NOT_IN_PICKETT != NOT_USED
NOT_IN_PICKETT != INCORRECT
PICKETT_LEXICON != EXHAUSTIVE_USAGE_INVENTORY
```

`HALL-0171`:

La obra distingue entre grafías de préstamos aún no zapotequizados y convenciones nativas/adaptadas. Esa política de 2007 es información lexicográfica histórica, no norma contemporánea automática.

### Alcance dialectal y variación

`HALL-0169`:

- base principal = Juchitán;
- diferencias tonales y léxicas entre pueblos;
- variación entre individuos/grupos dentro de Juchitán;
- la propia obra reconoce que no registró toda la variación.

`HALL-0170`:

La presencia/ausencia de `g` inicial está documentada como variación frecuente y aparece mediante entradas paralelas, por ejemplo `guixí'` / `ixí'`. La alternancia medial existe con menor frecuencia.

```text
MISSING_INITIAL_g != ERROR_BY_DEFAULT
DOCUMENTED_VARIANT_PAIR != PRODUCTIVE_DELETE_g_RULE
```

### Convenciones ortográficas históricas y conflicto de acento

`HALL-0172` registra una contradicción abierta:

- Pickett 2007 aplica las reglas ortográficas españolas de acentuación a palabras zapotecas;
- Xneza 2015 cuestiona ese modelo y propone no representar el acento prosódico predecible mediante reglas españolas.

```text
CURRENT_ORTHOGRAPHIC_NORM_FROM_THESE_TWO_SOURCES_ALONE = UNRESOLVED
PROSODIC_STRESS != TONE
CHOOSE_ONE_AS_CURRENT_RULE = forbidden
```

La resolución requiere autoridad ortográfica contemporánea pertinente, incluida la Norma 2016 cuando su texto completo esté accesible.

### Ambigüedad de `xh-`

`HALL-0173`:

Existe un `xh-/x-` con significado `otro` que comparte superficie y alternancias con el prefijo posesivo.

```text
SURFACE_xh_x != POSSESSIVE_BY_DEFAULT
MORPHOPHONOLOGICAL_SIMILARITY != SAME_FUNCTION
```

### Convenciones de presentación verbal

`HALL-0174`:

- la sección español→zapoteco usa formas de tercera persona singular;
- la forma habitual es la forma verbal de presentación declarada por la obra;
- una forma verbal de Pickett no equivale a raíz desnuda ni infinitivo español.

`HALL-0175`:

Formas sencilla y causativa morfológicamente relacionadas pueden aparecer bajo entradas españolas separadas cuando sus traducciones lexicalizan significados diferentes (`aprender` / `enseñar`).

```text
PICKETT_SURFACE_VERB != BARE_ROOT
SPANISH_DICTIONARY_ENTRY_BOUNDARY != ZAPOTEC_LEXEME_BOUNDARY
ENTRY_COUNT != LEMMA_COUNT
```

### Espaciado editorial de partículas

`HALL-0176`:

La obra declara que algunas partículas no son palabras autónomas pero se escriben separadas por razones prácticas de lectura/alfabetización.

```text
PRINTED_SPACE_IN_PICKETT != INDEPENDENT_GRAMMATICAL_WORD_BY_DEFAULT
PICKETT_SPACING_CAN_REFLECT_PEDAGOGICAL_EDITORIAL_CHOICE = true
```

Esto converge con Xneza 2015: espacio gráfico, palabra fonológica y palabra gramatical deben mantenerse separados.

### Notación tonal interna

`HALL-0177`:

Dentro del sistema editorial de Pickett:

- `b` = bajo;
- `al` = alto;
- `a` = ascendente;
- punto = separación de tonos silábicos dentro de palabra;
- guion = separación de indicaciones tonales entre palabras;
- ausencia de indicación tonal = bajo en todas las sílabas **sólo dentro de esta convención fuente**.

```text
PICKETT_NO_TONE_BRACKET = ALL_LOW_BY_SOURCE_CONVENTION
PICKETT_NO_MARK != UNIVERSAL_LOW_TONE_RULE
```

### Marcas auxiliares de aprendizaje

`HALL-0178`:

`r` subrayada y `l` subrayada son ayudas lexicográficas para aprendices en el Vocabulario; no deben copiarse automáticamente como superficie ortográfica ordinaria del proyecto.

```text
DICTIONARY_HELPER_NOTATION != ORDINARY_LITERARY_ORTHOGRAPHY
COPY_HELPER_SYMBOL_TO_PROJECT_SURFACE = forbidden_without_adjudication
```

## Relación con conocimiento ya adjudicado

Los apéndices gramaticales repiten o resumen diversos hechos ya promovidos desde la Gramática Popular —posesión, persona, partículas, aspecto, causatividad y otros—. No se duplicaron como HALL nuevos cuando no añadían alcance o restricciones relevantes.

## Relación con el dispositivo

El runtime histórico contiene `PICKETT_LEXICON_BACKFILL_v0_1.csv` y otras extracciones. Deben consumirse con estas restricciones:

```text
PICKETT_BACKFILL != VOCABULARIO_ORIGINAL
EXTRACTION_PACKAGE != SOURCE_AUTHORITY
NO_ENTRY != NEGATIVE_EVIDENCE
SURFACE_FORM != BARE_LEMMA_BY_DEFAULT
PRINTED_SPACE != GRAMMATICAL_BOUNDARY_BY_DEFAULT
```

## Estado

```text
PICKETT_VOCABULARIO_P1_LEXICOGRAPHIC_BACKFILL = SUFFICIENT
FULL_2000_ENTRY_PROMOTION_TO_HALL = NOT_REQUIRED
REOPEN_FOR = TARGETED_LEXEME | EXACT_EXAMPLE | DIALECT_VARIANT | ORTHOGRAPHIC_CONTRADICTION | IMPLEMENTATION_GRANULARITY
```
