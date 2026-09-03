# PLAN DE REUBICACIÓN DEL ACERVO DE FUENTES — v0.1

**Fecha:** 2026-09-03  
**Estado:** `ARCHITECTURE_PREPARATION / NON_NORMATIVE / DEVICE_SPLIT_PREREQUISITE`

## Problema

Parte importante de la evidencia lingüística y bibliográfica utilizada durante el desarrollo del dispositivo quedó físicamente materializada dentro de `dispositivo/`: matrices de lectura, extracciones, datasets y copias transformadas de fuentes como Bueno Holle, Dictionaria y Pickett.

Eso fue útil para recuperar y reproducir el dispositivo, pero no debe convertirse en la arquitectura permanente.

```text
SOURCE_USED_BY_DEVICE != DEVICE_OWNED_KNOWLEDGE
```

La separación física del dispositivo no debe dejar atrapado del lado técnico el acervo documental necesario para la investigación de Voces de las Nubes.

## Principio de propiedad

Las fuentes lingüísticas, bibliográficas, documentales y corpus externos pertenecen al **dominio de evidencia de Voces de las Nubes**, independientemente de qué herramienta las haya ingerido primero.

El dispositivo puede consumirlas o compilar representaciones técnicas, pero no convertirse en su repositorio canónico.

## Cuatro clases que deben distinguirse

### A. Fuente original o dataset documental

Ejemplos:

- libros, artículos y gramáticas;
- vocabularios y diccionarios;
- corpus externos;
- exportaciones oficiales de datasets;
- audio documental;
- Norma de escritura y alfabetos;
- Dictionaria en su forma fuente identificable.

**Propiedad:** Voces de las Nubes / acervo de fuentes.

### B. Derivado documental neutral

Ejemplos:

- texto extraído de un PDF;
- tabla extraída conservando las columnas originales;
- split por capítulos o páginas;
- mapa de páginas;
- transcripción o conversión de formato trazable;
- exportación de entries/senses/examples cuando reproduce un dataset externo sin adjudicación lingüística propia.

**Propiedad objetivo:** acervo de Voces, siempre que licencia, derechos y condiciones de acceso lo permitan.

Debe conservar:

- fuente de origen;
- versión/fecha;
- método de extracción;
- SHA-256;
- transformaciones aplicadas;
- licencia o restricción de redistribución.

### C. Interpretación o conocimiento extraído

Ejemplos:

- afirmación sobre una construcción;
- lectura de una regla;
- comparación entre autores;
- hipótesis pedagógica;
- decisión ortográfica;
- inferencia sobre variedad o uso.

**Propiedad:** Sistema de Conocimiento de Voces mediante `HALL`, `TEO`, `VAL`, `SUP`, `DEC` u otra entidad pertinente.

Una matriz creada durante desarrollo técnico no debe convertirse automáticamente en conocimiento. Debe volver a la fuente original y adjudicarse.

### D. Compilación o representación ejecutable

Ejemplos:

- SQLite del Corrector;
- registries del runtime;
- embeddings o índices;
- tablas normalizadas para ejecución;
- backfills con lógica específica del dispositivo;
- licencias de generación;
- fixtures y datos para tests;
- `JUCHITAN_LINGUISTIC_CORE` experimental;
- outputs y caches derivados.

**Propiedad:** repositorio técnico del dispositivo.

Deben declarar qué estado de Voces y qué fuentes/documentos los originaron cuando sea materialmente relevante.

## Arquitectura lógica objetivo

```text
VOCES DE LAS NUBES
│
├── Sistema de Conocimiento
│   ├── SRC
│   ├── HALL / VAL / TEO / SUP
│   ├── DEC / PRIN
│   └── vistas canónicas
│
└── ACERVO DE FUENTES
    ├── originales redistribuibles
    ├── referencias a originales restringidos
    ├── derivados documentales neutrales permitidos
    └── manifiesto de identidad, derechos y ubicación
            │
            │ fuente + conocimiento aprobado
            ▼
DISPOSITIVO DIDXAZÁ
    ├── compilaciones
    ├── índices
    ├── runtime
    ├── registries
    ├── bases ejecutables
    └── tests
```

El acervo puede vivir físicamente dentro de `vocesdelasnubes` cuando la redistribución sea legal y práctica, o en almacenamiento privado/controlado por Voces cuando los derechos, tamaño o condiciones de acceso impidan publicarlo. **La ubicación física no crea una tercera autoridad.** El manifiesto canónico de Voces debe identificar cada payload y su ubicación.

## Restricción por derechos y acceso

El repositorio `lopezcarlton/vocesdelasnubes` es actualmente público. Por tanto, no debe trasladarse automáticamente a él ningún PDF, extracción extensa, audio o dataset únicamente porque ya exista una copia de trabajo.

Para cada fuente deberá decidirse:

```text
CAN_REDISTRIBUTE_PUBLICLY
CAN_STORE_PRIVATELY
REFERENCE_ONLY
DERIVATIVE_ALLOWED
ACCESS_RESTRICTED
```

Cuando no pueda redistribuirse el original, Voces debe conservar al menos:

- `SRC`;
- referencia bibliográfica exacta;
- URI o ubicación controlada;
- hash del archivo disponible para el proyecto, cuando sea posible;
- versión/edición;
- estado de acceso;
- licencia o restricción conocida;
- derivados permitidos.

## Casos prioritarios del estado actual

### Bueno Holle / BIB065

Actualmente existen en `dispositivo/migracion/fuentes/`:

- `BH2019_READING_STATE_CLOSED_v0_36_1.md`;
- `BH2019_SOURCE_PROVENANCE_v0_36_1.json`;
- `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.{md,csv}`.

Existe además `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md`.

Antes del corte debe distinguirse:

- fuente original;
- derivados documentales neutrales;
- interpretaciones que requieren/promovieron entidades de Voces;
- artefactos históricos propios del dispositivo.

### Dictionaria

Actualmente el runtime contiene:

- `DICTIONARIA_entries_v0_2_15_2.csv`;
- `DICTIONARIA_senses_v0_2_15_2.csv`;
- `DICTIONARIA_examples_v0_2_15_2.csv`.

Antes del corte debe reconstruirse su procedencia exacta, versión, licencia y transformación. Si representan de manera neutral una adquisición de Dictionaria, debe existir un payload fuente/derivado documental identificable desde Voces. Las copias exactas requeridas por el replay histórico pueden permanecer además en el repositorio técnico como fixtures históricos.

### Pickett

`PICKETT_LEXICON_BACKFILL_v0_1.csv` es una pieza del runtime histórico y no debe promoverse automáticamente a fuente canónica. Debe reconstruirse qué registros proceden del Vocabulario/Pickett, qué transformaciones se aplicaron y cuál es el artefacto documental previo al backfill.

La Gramática Popular y el Vocabulario deben tener identidades de fuente en Voces independientemente de las tablas técnicas generadas a partir de ellos.

### JUCHITAN_LINGUISTIC_CORE

`JUCHITAN_LINGUISTIC_CORE_v0_27.md` es una **compilación experimental del dispositivo**. No debe trasladarse a `conocimiento/` como si fuera fuente.

Las afirmaciones válidas que contenga deben poder reconstruirse mediante fuentes y entidades adjudicadas de Voces. El core seguirá siendo una representación técnica derivada.

## Manifiesto del acervo

Antes de la separación física deberá existir un manifiesto con, como mínimo:

```yaml
source_id:
bib_id:
title:
author:
year:
version_or_edition:
source_type:
variety:
canonical_src_record:
original_location:
repository_payload:
external_uri:
sha256:
license_or_rights:
redistribution_status:
access_status:
derivatives:
notes:
```

No todos los campos serán aplicables a toda fuente, pero identidad, procedencia y acceso no pueden quedar implícitos.

## Regla de consumo por el dispositivo

Una compilación técnica debe poder señalar dos identidades distintas:

```text
KNOWLEDGE_SOURCE_COMMIT = <commit exacto de Voces>
SOURCE_LIBRARY_MANIFEST_VERSION = <versión/commit del acervo utilizado>
```

Así se distingue:

- qué decisiones y conocimiento aprobado se consumieron;
- qué payloads documentales se utilizaron para construir la representación técnica.

## Prerrequisito para separar repositorios

No ejecutar el corte final de `dispositivo/` hasta completar una pasada de **SOURCE OWNERSHIP** sobre los artefactos actualmente ingeridos.

Cada artefacto relevante debe terminar clasificado como:

```text
VOCES_SOURCE
VOCES_NEUTRAL_DERIVATIVE
VOCES_KNOWLEDGE_ENTITY
DEVICE_TECHNICAL_DERIVATIVE
DEVICE_HISTORICAL_FIXTURE
RESTRICTED_EXTERNAL_SOURCE
UNRESOLVED
```

`UNRESOLVED` en una fuente necesaria para investigación o ejecución debe resolverse antes de borrar/mover su única copia identificable.

## Resultado buscado

Un chat de Voces debe poder estudiar de manera natural la Gramática Popular, Bueno Holle, el Vocabulario, Dictionaria y otras fuentes sin entrar al repositorio técnico para reconstruir qué sabe el proyecto.

Un desarrollador del dispositivo debe poder construir el sistema desde fuentes y conocimiento identificables sin poseer autoridad para modificar el Sistema de Conocimiento.
