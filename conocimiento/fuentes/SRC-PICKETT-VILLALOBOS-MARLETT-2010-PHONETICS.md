# SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS

```yaml
id: SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS
tipo: fuente_bibliografica
bib_id: BIB061
titulo: "Isthmus (Juchitán) Zapotec"
autor_o_participantes:
  - Velma B. Pickett
  - María Villalobos Villalobos
  - Stephen A. Marlett
fecha: 2010
ubicacion: "https://doi.org/10.1017/S0025100310000174"
doi: "10.1017/S0025100310000174"
descripcion: >
  Ilustración fonética de la variedad de Juchitán publicada en Journal of the
  International Phonetic Association 40(3), pp. 365–372. Incluye descripción
  segmental, tonos, acento y transcripción de un pasaje grabado con María Villalobos,
  hablante y escritora nacida en Juchitán.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: semantic_backfill_p0_sufficient_2026-09-04
```

## Identidad bibliográfica

La hoja bibliográfica maestra distingue dos objetos relacionados:

- `BIB016`: versión española/ilustración fonética registrada con fecha 2009;
- `BIB061`: publicación JIPA de 2010 descrita aquí.

```text
BIB016 != BIB061
```

No colapsar las identidades, aunque compartan autores, datos y análisis.

## Corrigendum

Corrigendum publicado en 2011:

- *Journal of the International Phonetic Association* 41(1), p. 135;
- DOI `10.1017/S0025100311000053`;
- corrige/completa la lista de datos que ilustran las consonantes en la página 367 del artículo de 2010.

→ `HALL-0147`.

```text
EXACT_PVM2010_CONSONANT_EXAMPLE_DATA -> CONSULT_2011_CORRIGENDUM
CORRIGENDUM_SCOPE != GENERAL_RETRACTION_OF_ANALYSIS
```

## Memoria persistente de lectura — backfill P0 2026-09-04

- oposición fortis/lenis multirrasgo y contextual → `HALL-0141`;
- trill/tap como excepción inicial de sonorantes y trill extremadamente escasa → `HALL-0142`;
- cinco vocales y fonación modal/cortada/laringizada → `HALL-0143`;
- tres tonos fonémicos vs propuesta tentativa de cinco melodías de raíces nominales → `HALL-0144`;
- acento, peso silábico, clíticos y reducción prosódica en compuestos/frases → `HALL-0145`;
- alófonos de `b/d/g`, `g` inicial, asimilación nasal y centralización vocálica átona → `HALL-0146`;
- inventario consonántico/vocálico explícito → `HALL-0148`;
- separación entre forma fonológica, superficie fonética y ortografía popular → `HALL-0149`.

## Reglas de uso

```text
PHONEMIC_FORM != PHONETIC_SURFACE != POPULAR_ORTHOGRAPHY
FORTIS_LENIS != VOICE_ONLY
FORTIS_LENIS != LENGTH_ONLY
THREE_PHONEMIC_TONES != FIVE_ROOT_MELODIES
FIVE_ROOT_MELODIES = PROPOSAL_WITH_UNRESOLVED_DETAILS
ALLOPHONE != SPELLING_CORRECTION
PHONETIC_GLOTTAL_CLOSURE != AUTOMATIC_CODA_GLOTTAL_PHONEME
```

## Relación con dispositivo

Esta fuente es autoritativa como bibliografía para los hechos que documenta; cualquier registry, tabla acústica o regla ejecutable del dispositivo es una representación derivada y debe enlazarse a los HALL pertinentes y al commit canónico de Voces.

## Estado

```text
PVM2010_PLUS_CORRIGENDUM_P0_BACKFILL = SUFFICIENT
EXHAUSTIVE_TOKEN_OR_AUDIO_INGESTA = false
REOPEN_FOR = EXACT_EXAMPLE | ACOUSTIC_MEASUREMENT | IMPLEMENTATION_GRANULARITY | CONTRADICTION
```
