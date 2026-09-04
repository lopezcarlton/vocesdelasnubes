# SRC-CARDONA-VICENTE-2025-VARIACION-ESCRITURA

```yaml
id: SRC-CARDONA-VICENTE-2025-VARIACION-ESCRITURA
tipo: fuente_bibliografica
bib_id: BIB064
titulo: "Implicaciones de la variación dialectal en la escritura del zapoteco del Istmo"
autor_o_participantes:
  - Pedro David Cardona Fuentes
  - David Eduardo Vicente Jiménez
fecha: 2025
obra_contenedora: "Geolingüística y variación en lenguas otomangues"
coordinadores:
  - Pedro David Cardona Fuentes
  - Mario Ulises Hernández Luna
editorial: "Universidad Intercultural del Estado de Puebla"
isbn: "978-607-69276-0-1"
paginas: "112-131 según registro de capítulo accesible; el índice del libro inicia el capítulo en p. 111"
ubicacion: "Repositorio Institucional UAQ — handle 123456789/13070; copia de capítulo accesible públicamente"
descripcion: >
  Capítulo arbitrado sobre las consecuencias de la variación dialectal del zapoteco del
  Istmo para el diseño de la escritura, apoyado en la dialectología de Cardona (2020).
nivel_de_fuente: secundaria
disponibilidad: acceso_abierto_en_repositorio
licencia_registrada_en_repositorio: CC_BY_NC_SA_4_0
estado_de_acceso: disponible
estado_de_ingesta: semantic_backfill_p1_variation_writing_sufficient_2026-09-04
```

`BIB064` está confirmado por la hoja bibliográfica maestra reconciliada el 2026-09-03.

## Memoria persistente de lectura — P1 2026-09-04

### Cobertura y zonas amplias

El capítulo trabaja con nueve municipios documentados por el proyecto dialectológico:

- Juchitán de Zaragoza;
- Santa María Xadani;
- Tehuantepec;
- San Blas Atempa;
- Unión Hidalgo;
- El Espinal;
- Asunción Ixtaltepec;
- San Pedro Comitancillo;
- Ixtepec.

`HALL-0180` registra la síntesis zonal usada en 2025:

- sur: San Blas Atempa / Tehuantepec;
- centro: Juchitán / Xadani / Unión Hidalgo / El Espinal;
- norte: Comitancillo / Ixtaltepec / Ixtepec.

Esta clasificación amplia no elimina el carácter transicional que Cardona 2020 reporta para El Espinal, Unión Hidalgo y Comitancillo.

```text
BROAD_DIALECT_ZONE != LOCALITY
BROAD_ZONE_LABEL != ERASE_TRANSITION_STATUS
```

### Fonación y variación regional

`HALL-0181`:

En los fenómenos discutidos, las realizaciones rearticuladas se asocian especialmente con la zona sur, mientras realizaciones laringizadas/creaky tienen amplia difusión en zonas central y norte. La diferencia puede importar para la transparencia oral–escritura.

```text
SAME_MACRO_PHENOMENON != SAME_LOCAL_PHONETIC_REALIZATION
DIALECT_TENDENCY != ABSOLUTE_LEXEME_RULE
```

### Alcance histórico del Alfabeto Popular

`HALL-0182`:

Los autores caracterizan el Alfabeto Popular como una solución históricamente centrada en el habla de Juchitán para su discusión del problema regional. Esa caracterización no invalida el Alfabeto ni adopta por sí misma una norma diferente dentro de Voces.

```text
JUCHITAN_CENTERED_REFERENCE != PAN_ISTHMUS_PHONETIC_IDENTITY
ACADEMIC_CRITIQUE != ADOPTED_PROJECT_NORM
```

### Propuesta multilectal

`HALL-0183`:

El capítulo propone considerar un enfoque multilectal para una futura norma regional. En ciertos fenómenos, más de una representación podría ser compatible con realizaciones dialectales distintas; la propuesta se extiende a algunas alternancias segmentales y elisiones.

```text
MULTILECTAL_ORTHOGRAPHY = ACADEMIC_PROPOSAL
MULTILECTAL_PROPOSAL != CURRENT_ADOPTED_PROJECT_NORM
MULTILECTAL_PROPOSAL != FREE_VARIANT_INTERCHANGEABILITY
VARIANT_LOCALITY_METADATA = REQUIRED_FOR_SAFE_USE
```

### Otras deudas que el capítulo identifica

La discusión final señala que una normalización regional tendría que considerar además:

- marcación de tonos;
- segmentación gráfica entre palabras;
- puntuación y organización de enunciados complejos.

Estas menciones no resuelven esos problemas ni sustituyen Xneza 2015, la Norma 2016 o futuras decisiones del proyecto.

## Relevancia para Voces

```text
JUCHITAN = PRIORITY_VARIETY
OTHER_LOCALITY_FORM != INCORRECT
EL_ESPINAL != JUCHITAN_ALIAS
GENERATOR_TARGET_VARIETY_MUST_BE_EXPLICIT_FOR_CROSS_LOCALITY_USE = true
CORRECTOR_MAY_RETURN_VARIANT_BY_LOCALITY = true
```

Una arquitectura multilectal no se adopta automáticamente. El proyecto puede seguir priorizando Juchitán mientras conserva evidencia de otras localidades y evita sobrecorregir variación legítima.

## Límites

- El capítulo es análisis/propuesta académica, no norma adoptada.
- No sustituye metadata local por una sola etiqueta regional.
- No reemplaza la necesidad de leer la Norma de escritura 2016 directamente.

## Estado

```text
CARDONA_VICENTE_2025_P1_VARIATION_WRITING_BACKFILL = SUFFICIENT
EXHAUSTIVE_ISOGLOSS_INGESTA = false
REOPEN_FOR = TARGETED_ORTHOGRAPHIC_VARIANT | DIALECT_COMPARISON | EXACT_ISOGLOSS | NORM_DESIGN_QUESTION
```
