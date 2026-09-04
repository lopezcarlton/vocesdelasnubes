# SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR

```yaml
id: SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR
tipo: fuente_bibliografica
titulo: "Gramática popular del zapoteco del Istmo"
autor_o_participantes:
  - Velma B. Pickett
  - Cheryl A. Black
  - Vicente Marcial Cerqueda
fecha: 2001
bib_id: BIB004
edicion: "Segunda edición electrónica"
ubicacion: "https://mexico.sil.org/es/resources/archives/35304"
archivo_publicado: "Imagezai_gramatica_ed2.pdf"
descripcion: >
  Descripción gramatical de la variedad de zapoteco del Istmo hablada en el distrito
  de Juchitán. Es la fuente bibliográfica principal de numerosas reglas que fueron
  compiladas posteriormente en el JUCHITAN_LINGUISTIC_CORE técnico. Voces debe volver
  a esta obra para adjudicar esas afirmaciones; el core no sustituye la fuente.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: semantic_backfill_structural_p0_sufficient_2026-09-04
```

## Identidad y alcance

- Editoriales/instituciones: Centro de Investigación y Desarrollo Binnizá A.C.; Instituto Lingüístico de Verano A.C.
- Extensión: x, 125 páginas.
- Variedad declarada por la ficha editorial: Juchitán, Oaxaca.
- La ficha oficial del SIL/ILV ofrece el archivo electrónico de la segunda edición.

## Backfill semántico confirmado — 2026-09-04

La migración había preservado la identidad de la fuente y parte de sus derivados técnicos, pero no había promovido a Voces varios hechos ya estudiados. Se reabrieron únicamente pasajes originales pertinentes y se formalizaron los bloques siguientes.

### Segunda persona singular

§5.1 declara explícitamente que **no hay diferencia entre `usted` y `tú`**. §5.1.1 registra `lii` con el significado `tú, usted`.

→ `HALL-0066`.

### Sistema tonal

§3.4 trabaja tres categorías de tono en la descripción operativa de la Gramática/Vocabulario:

- `b` = tono bajo;
- `al` = tono alto;
- `a` = tono ascendente.

La escritura ordinaria no necesita marcarlos, pero el aprendiz debe aprenderlos.

→ `HALL-0067`, relacionado con `HALL-0054`.

### `xh-/x-` ante consonante

La morfología posesiva documenta `xh-` ante vocal y `x-` ante consonante, con alternancias condicionadas de la raíz.

→ `HALL-0068`.

### `r` débil / `r` fuerte

La Gramática caracteriza la `r` fuerte como **muy rara en palabras nativas**, más frecuente en préstamos del español, y llama a la `r` débil **lo normal**.

→ `HALL-0069`.

### Sistema verbal y aspectos — §7.2–§7.3

Hallazgos promovidos:

- marcadores principalmente aspectuales; sólo el futuro puede definirse como tiempo → `HALL-0077`;
- perfecto `hua-` como acción repetida a lo largo del tiempo, con restricción de experiencia previa y uso negativo de intervalo → `HALL-0078`;
- progresivo ambulativo `cana-` → `HALL-0079`;
- Juego 1 / Juego 2, con 1A/1B/1C → `HALL-0080`;
- potencial de 1C sin prefijo en la descripción de la obra → `HALL-0081`;
- `u` de Juego 2 como hipótesis de vocal temática causativa, no regla cierta → `HALL-0082`;
- habitual pasado/presente y no futuro → `HALL-0083`;
- completivo como acción terminada, no simple pasado → `HALL-0084`;
- progresivo presente/pasado/futuro por contexto → `HALL-0085`;
- potencial seleccionado por múltiples construcciones → `HALL-0086`;
- irrealizado como contrario a la verdad en los contextos documentados → `HALL-0087`;
- estativo `na-` con distribución limitada y tiempo contextual → `HALL-0088`;
- futuro `z-` restringido a contexto futuro → `HALL-0089`.

```text
GP_GAME_SYSTEM != PBK2016_A_B_C_D_BY_DEFAULT
SOURCE_HYPOTHESIS != CERTAIN_RULE
SPANISH_TENSE != DIDXAZA_ASPECT_BY_DEFAULT
POTENTIAL != CAPACITY_OR_POSSIBILITY_ONLY
STATIVE != PRESENT_TENSE
```

### Persona pronominal — §5.1–§5.1.2

- pronombres independientes separables y con funciones de complemento/respuesta/énfasis → `HALL-0090`;
- pronombres dependientes no autónomos y con distintos huéspedes → `HALL-0091`;
- tercera persona recuperable sin marca segmental y plural indefinido con `ca'` → `HALL-0092`;
- 2SG `-lu'/-u'` con alternancias → `HALL-0093`;
- 1SG `-ya'/-a'` con fusiones → `HALL-0094`;
- tercera persona persona/animal/cosa → `HALL-0095`;
- inclusivo `laanu/nu` vs exclusivo `laadu/du` → `HALL-0096`.

```text
PERSON != FIXED_SUFFIX_STRING
UNMARKED_3RD_PERSON != ERROR
INDEPENDENT_PRONOUN != REQUIRED_SUBJECT_WORD
SOURCE_DOCUMENTED_INCLUSIVE_EXCLUSIVE_CONTRAST != FIXED_PEDAGOGICAL_LEVEL
```

### Posesión — §4.2 y §6.6

- tres estrategias: `xh-/x-`, sustantivos siempre poseídos y `xti'` → `HALL-0097`;
- alternancias iniciales y pérdida de `bi-` en ciertos lemas → `HALL-0098`;
- sustantivos siempre poseídos no aceptan `xh-/x-` → `HALL-0099`;
- `xti'` con pronombre dependiente o frase nominal y cadenas posesivas → `HALL-0100`;
- `xti'` + pronombre dependiente sin concordancia con género/número del objeto poseído → `HALL-0101`.

```text
POSSESSION != SINGLE_UNIVERSAL_TEMPLATE
POSSESSED_SURFACE != BLIND_PREFIX_CONCATENATION
INHERENTLY_POSSESSED_NOUN + xh/x = NOT_THE_DOCUMENTED_STRATEGY
```

### Causatividad y valencia — §7.1 y §7.4

- aumento de valencia causativa → `HALL-0102`;
- `si-` como marcador más común, no único → `HALL-0103`;
- otros prefijos/cambios iniciales y Juego 2 mayoritario, no universal → `HALL-0104`;
- grupos limitados con dos prefijos, dos causativos o causativo sin prefijo → `HALL-0105`.

```text
CAUSATIVE_SEMANTICS != CAUSATIVE_SURFACE_FORM
CAUSATIVE != si_ONLY
MOST_CAUSATIVES_GAME2 != ALL_CAUSATIVES_GAME2
CAUSATIVE_FORMATION = LEXEME/PARADIGM_SENSITIVE
BLIND_CAUSATIVE_GENERATION = forbidden_without_lexeme_or_paradigm_evidence
```

### Imperativos y movimiento — §7.5–§7.6

- imperativo singular = completivo sin pronombre; plural = `la-` + potencial → `HALL-0106`;
- progresivo especial de `ir/venir` → `HALL-0107`;
- progresivo/futuro de `venir` pueden compartir segmentos y distinguirse por tono → `HALL-0108`;
- auxiliares de movimiento + potencial para movimiento con intención y conjunto léxico restringido → `HALL-0109`.

```text
IMPERATIVE != SINGLE_UNIVERSAL_SURFACE_TEMPLATE
GO_COME_PROGRESSIVE != ORDINARY_VERB_PROGRESSIVE
SAME_SEGMENTAL_FORM != SAME_VERBAL_ANALYSIS
STRIP_TONE_BEFORE_ANALYSIS = unsafe
MOVEMENT_AUXILIARY_PATTERN != UNIVERSAL_FOR_ALL_VERBS
```

### Negación, partículas y preguntas — §§8.4–8.6 y 13.1–13.3

- `HALL-0110`–`HALL-0113` registran negadores, partículas dependientes, énfasis y preguntas;
- `guiruti'`/`gasti'` cambian de posición según la construcción negativa; con `qué` no pueden intervenir entre negador y verbo; `cadi` no aparece con `qué` en la descripción de la obra → `HALL-0114`.

```text
GP2001_NEGATION_DESCRIPTION = BIBLIOGRAPHIC_EVIDENCE
GP2001_NEGATION_DESCRIPTION != CONTEMPORARY_NORMATIVE_ADJUDICATION
```

### Combinación de oraciones — capítulo 14

- coordinación con `ne` y sin conjunción → `HALL-0115`;
- complementos oracionales sin equivalente obligatorio de español `que` → `HALL-0116`;
- restricciones distintas según verbo rector → `HALL-0117`;
- preguntas indirectas → `HALL-0118`;
- subordinadas adverbiales por relación semántica y `la?` como frontera posible → `HALL-0119`;
- relativas con `ni` y recuperación de rol por estructura/valencia → `HALL-0120`;
- relativas sin antecedente nominal expreso → `HALL-0121`.

```text
VERB_SEQUENCE != AUTOMATIC_SUBORDINATION
SPANISH_que != UNIVERSAL_DIDXAZA_COMPLEMENTIZER
RECTOR_LEMMA_MATTERS_FOR_CLAUSAL_COMPLEMENTS = true
DIRECT_QUESTION != INDIRECT_QUESTION
ADVERBIAL_RELATION_FIRST = true
ni != FIXED_SPANISH_RELATIVE_TRANSLATION
HEADLESS_RELATIVE_DOES_NOT_REQUIRE_INSERTED_GENERIC_NOUN = true
```

### Apéndice para lingüistas — pp. 123–125

- fuerte/débil no equivale a sordo/sonoro → `HALL-0122`;
- alargamiento postónico, ausencia de fricativización castellana de `b/d/g` y velarización contextual de `n` son fonética, no ortografía → `HALL-0123`;
- neutralización contextual de vocales cortadas/quebradas al perder acento en frases estrechas/compuestos, sin generalización a toda adyacencia → `HALL-0124`.

```text
FORTIS_LENIS != VOICE_ONLY
CONTEXTUAL_PHONETICS != SPELLING_CHANGE
CITATION_FORM != CONTEXTUAL_PHONETIC_SURFACE
PHONETIC_NEUTRALIZATION != ORTHOGRAPHIC_DELETION
AUDIO_SURFACE -> SPELLING_CORRECTION = forbidden_without_independent_orthographic_evidence
NOT_ALL_WORD_ADJACENCY_NEUTRALIZES = true
```

### Frase nominal y determinación — §§4.4, 6.4–6.8

- orden interno de la frase nominal: cantidad/plural antes del sustantivo; modificadores, poseedor, relativa y demostrativo en posiciones postnominales documentadas → `HALL-0125`;
- ausencia de artículos equivalentes exactos a `el/la`; usos documentados de `ca` y `ti` → `HALL-0126`;
- demostrativos dependientes y postnominales → `HALL-0127`;
- interrogativos nominales prenominales y sensibles a clase semántica → `HALL-0128`;
- intensificación con `nabé/dunabé` y construcciones lexicalmente restringidas → `HALL-0129`.

```text
SPANISH_NP_ORDER != DIDXAZA_TEMPLATE
SPANISH_ARTICLE -> BLIND_DIDXAZA_DETERMINER_INSERTION = forbidden
SPANISH_INTERROGATIVE_GLOSS != SUFFICIENT_FOR_SELECTION
SPANISH_muy != SINGLE_UNIVERSAL_DIDXAZA_OPERATOR
```

### Preposiciones y relaciones espaciales — capítulo 9

- gran parte de las relaciones preposicionales se expresan mediante términos de partes del cuerpo, a veces reducidos → `HALL-0130`;
- `runi` tiene uso preposicional causal, `ne` es preposición nativa de compañía en la clasificación de GP y `de/pur/para` son préstamos documentados → `HALL-0131`.

```text
BODY_PART_NOUN_OR_RELATOR = RESOLVE_BY_CONSTRUCTION
SPANISH_PREPOSITION_GLOSS != UNIQUE_DIDXAZA_FORM
ne = PREPOSITION_OR_COORDINATOR_BY_CONSTRUCTION
```

### Oración básica y predicación — capítulo 12

- valencia y orden verbal inicial; V–S–CD–CI como orden más común con dos complementos → `HALL-0132`;
- varias estrategias copulativas/predicativas sin una cópula universal equivalente a `ser/estar` → `HALL-0133`;
- `nuu` para ubicación/existencia y verbos posicionales específicos → `HALL-0134`;
- condiciones atmosféricas con verbos impersonales sin sujeto → `HALL-0135`.

```text
VALENCY_FIRST = true
SPANISH_SVO != DEFAULT_DIDXAZA_TEMPLATE
SPANISH_SER_ESTAR != SINGLE_DIDXAZA_COPULA
POSITIONAL_SEMANTICS_SHOULD_NOT_BE_ERASED_BY_SPANISH_GLOSS = true
EXPLETIVE_SUBJECT = NOT_REQUIRED_IN_GP_DESCRIPTION
```

### Verbos compuestos y frases verbales — §§7.7–7.8

- compuestos con sustantivos, `la'dxi'`, partes del cuerpo, adjetivos y `né`; significado a menudo convencional → `HALL-0136`;
- frases verbales verbo+sustantivo/adjetivo, algunas idiomáticas → `HALL-0137`.

```text
COMPOUND_VERB != VERBAL_PHRASE_BY_DEFAULT
LITERAL_COMPONENT_GLOSSES != GUARANTEED_CONVENTIONAL_MEANING
WORD_BY_WORD_SPANISH_TRANSLATION = unsafe
BLIND_PRODUCTIVE_COMPOUND_GENERATION = forbidden
```

### Conjunciones, interjecciones y cohesión narrativa — §§8.7, 10, 11

- inventarios coordinados/subordinados y multifuncionalidad de `ne` → `HALL-0138`;
- interjecciones con funciones pragmáticas y restricciones sociales documentadas → `HALL-0139`;
- adverbios de introducción como recursos de cohesión, con `sicarí'` ligado explícitamente a apertura de cuento → `HALL-0140`.

```text
INTERJECTION != NEUTRAL_DISCOURSE_FILLER_BY_DEFAULT
REGISTER_OR_SPEAKER_RESTRICTION = MUST_BE_PRESERVED_WHEN_DOCUMENTED
NARRATIVE_CONNECTOR != NEUTRAL_CONVERSATIONAL_FILLER
GENRE_METADATA_REQUIRED_FOR_REUSE = true
```

## Relación con el dispositivo

`dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md`, registries, paradigmas y otras compilaciones técnicas contienen conocimiento derivado de esta obra.

```text
JUCHITAN_LINGUISTIC_CORE != SOURCE
PERSON_POSSESSION_REGISTRY != SOURCE
GRAMATICA_POPULAR = SOURCE
```

Las compilaciones técnicas pueden servir para localizar temas o ejemplos; cualquier afirmación que se promueva o revise en Voces debe poder justificarse en la Gramática Popular o en evidencia posterior de autoridad pertinente.

## Cierre P0 estructural — 2026-09-04

El backfill dirigido alcanza **suficiencia estructural P0** para recuperación rápida y para alimentar Analyzer/Corrector/Tutor/Generator con conocimiento adjudicado de alto valor.

Esto **no significa ingesta exhaustiva** de cada lexema, ejemplo o texto del libro. Permanecen recuperables bajo demanda:

- inventarios léxicos finos;
- ejemplos adicionales de paradigmas ya representados;
- usos de género del capítulo 15 que no sean necesarios para una consulta concreta;
- granularidad adicional cuando una contradicción o implementación específica la exija.

```text
GRAMATICA_POPULAR_P0_STRUCTURAL_BACKFILL = SUFFICIENT
GRAMATICA_POPULAR_EXHAUSTIVE_SEMANTIC_INGESTA = false
FULL_LINEAR_REREAD_REQUIRED = false
REOPEN_ONLY_FOR_TARGETED_QUERY_CONTRADICTION_OR_MISSING_GRANULARITY = true
```

El siguiente P0 del checkpoint es Pickett–Villalobos–Marlett 2009/2010 + corrigendum.
