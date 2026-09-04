# SRC-PEREZ-BAEZ-CATA-BUENO-HOLLE-2015-XNEZA

```yaml
id: SRC-PEREZ-BAEZ-CATA-BUENO-HOLLE-2015-XNEZA
tipo: fuente_bibliografica
titulo: "Xneza diidxazá: retos en la escritura del zapoteco del Istmo vistos desde el texto Teria"
autor_o_participantes:
  - Gabriela Pérez Báez
  - Víctor Cata
  - Juan José Bueno Holle
fecha: 2015
bib_id: BIB017
ubicacion: "https://www.revistas-filologicas.unam.mx/tlalocan/index.php/tl/article/view/241"
doi: "10.19130/iifl.tlalocan.2015.241"
licencia: "CC BY-NC 4.0"
descripcion: >
  Artículo en Tlalocan 20, pp. 135–172, que presenta el relato contemporáneo Teria
  de Víctor Cata y analiza retos en la implementación del Alfabeto Popular, en especial
  la delimitación de la palabra ortográfica frente a palabra fonológica y gramatical.
  Es fuente central para el trabajo ortográfico del proyecto.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: semantic_backfill_p0_sufficient_2026-09-04
```

## Identidad y alcance

El artículo aparece en el volumen 20 de *Tlalocan* con año editorial 2015 y publicación web en enero de 2016. Se conserva `2015` como identidad bibliográfica del volumen/DOI del proyecto.

El texto `Teria` y su versión española son obras de Víctor Cata incluidas en el artículo. La versión española no debe tratarse como traducción literal automática: los autores advierten que funciona también como obra literaria propia.

## Memoria persistente de lectura — backfill P0 2026-09-04

### Continuidad del Alfabeto Popular y fonología ya recuperada

El artículo adopta el Alfabeto Popular por su uso comunitario y tradición desde 1956 y documenta procesos posteriores de normalización sin identificarlos mecánicamente con la Norma 2016.

- continuidad histórica del Alfabeto Popular → `HALL-0072`;
- tres tonos y tres tipos vocálicos; tono no representado sistemáticamente por el Alfabeto Popular descrito → `HALL-0067`;
- coexistencia de análisis fortis/lenis y sencilla/geminada debe conservarse por nivel analítico.

### Palabra fonológica

`HALL-0151`:

- palabra fonológica analizada alrededor de la raíz léxica;
- mínimo de una sílaba abierta;
- ausencia de codas consonánticas en el sistema descrito;
- restricción fuerte contra inicio vocálico, con debilitamiento/omisión opcional de /g/ inicial;
- acento de raíces bisilábicas relacionado con raíz y composición morfológica.

### Palabra gramatical, compuestos y colocaciones

- compuestos como palabras gramaticales diagnosticables mediante contigüidad, argumentos externos y hospedaje de clíticos al final de la unidad → `HALL-0152`;
- debilitamiento prosódico, orden fijo o significado convencional no bastan por sí solos para diagnosticar compuesto → `HALL-0153`;
- colocaciones pueden tener significado convencional sin constituir una sola palabra gramatical y pueden permitir material argumental/persona dentro de la secuencia → `HALL-0157`.

```text
COMPOUND != COLLOCATION
PROSODIC_WEAKENING != COMPOUND_PROOF
CONVENTIONAL_MEANING != SINGLE_GRAMMATICAL_WORD_PROOF
```

### Palabra ortográfica

`HALL-0154` establece el principio central del artículo:

```text
PHONOLOGICAL_WORD != GRAMMATICAL_WORD != ORTHOGRAPHIC_WORD_BY_DEFAULT
ORTHOGRAPHIC_WORD = CONVENTIONAL_ADJUDICATION_PROBLEM
LINGUISTIC_ANALYSIS != PRESCRIPTIVE_NORM
```

Los autores proponen criterios de análisis para facilitar homologación, pero concluyen explícitamente que no pretenden establecer normas prescriptivas.

### Clíticos

`HALL-0155`:

- un clítico no es palabra fonológica independiente por defecto;
- `má=` puede portar acento prosódico en ciertos contextos;
- `ca'` puede funcionar como enclítico verbal o proclítico nominal;
- hospedaje del clítico y espacio ortográfico son problemas relacionados pero no idénticos.

### Superficie fonética vs representación de compuestos

`HALL-0156`:

La fuente documenta la elección abierta entre representar cambios fonéticos contextuales de compuestos o conservar mayor transparencia de los componentes. Usa la coexistencia `didxazá` / `diidxazá` como ejemplo de prácticas observadas y no prescribe una solución universal.

### Acento prosódico vs tilde española

`HALL-0158`:

Los autores consideran innecesario representar ortográficamente el acento prosódico predecible en el análisis presentado y critican la aplicación mecánica de las reglas españolas de aguda/grave/esdrújula al diidxazá.

```text
PROSODIC_STRESS != TONE
PROSODIC_STRESS != SPANISH_TILDE_RULES
SPANISH_STRESS_ORTHOGRAPHY_AS_TEMPLATE = unsafe
XNEZA_STRESS_PROPOSAL != AUTOMATIC_CURRENT_NORM
```

## Consecuencias para el dispositivo

```text
TOKEN_BOUNDARY != PHONOLOGICAL_BOUNDARY_BY_DEFAULT
TOKEN_BOUNDARY != GRAMMATICAL_WORD_BOUNDARY_BY_DEFAULT
AUDIO_PAUSE != ORTHOGRAPHIC_SPACE_BY_DEFAULT
ROOT_RECOGNITION != AUTOMATIC_TOKEN_SPLIT
CLITIC_HOSTING != AUTOMATIC_SPACING_POLICY
PHONETIC_REDUCTION != AUTOMATIC_SPELLING_NORMALIZATION
```

Analyzer debe poder mantener simultáneamente capas fonológica, morfológica/gramatical y ortográfica. Corrector sólo puede imponer una convención de espacio/unión cuando exista una decisión ortográfica autorizada adicional.

## Estado

```text
XNEZA2015_P0_STRUCTURAL_BACKFILL = SUFFICIENT
XNEZA2015_EXHAUSTIVE_EXAMPLE_INGESTA = false
FULL_LINEAR_REREAD_REQUIRED = false
REOPEN_FOR = TARGETED_ORTHOGRAPHIC_QUERY | EXACT_EXAMPLE | CONTRADICTION | IMPLEMENTATION_GRANULARITY
```

Los ejemplos individuales de `Teria` permanecen disponibles como evidencia contextual y literaria, no como estilo conversacional neutral por defecto.
