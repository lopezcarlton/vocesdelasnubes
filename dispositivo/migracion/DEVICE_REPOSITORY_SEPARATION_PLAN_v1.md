# DEVICE_REPOSITORY_SEPARATION_PLAN_v1

**Estado:** `SOURCE_IDENTITY_PASS_COMPLETE / WAITING_FOR_DEVICE_REPOSITORY`  
**Versión interna:** 1.2  
**Fecha:** 2026-09-03

## Objetivo

Separar físicamente el dispositivo del repositorio canónico de Voces de las Nubes sin perder genealogía, reproducibilidad ni acceso a las fuentes que lo alimentaron.

La separación implementa `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO`; no crea una nueva autoridad.

## Regla simple

Sólo existen dos dominios de autoridad:

```text
VOCES DE LAS NUBES = conocimiento + fuentes + decisiones
DISPOSITIVO = implementación derivada
```

No se crea un tercer sistema de acervo.

Las gramáticas, vocabularios, corpus, diccionarios, normas y bibliografía se identifican desde `conocimiento/fuentes/` mediante `SRC-*`. El payload puede vivir en el repositorio o en una ubicación externa/restringida según derechos y acceso.

El dispositivo conserva sus representaciones técnicas y los fixtures exactos necesarios para reproducibilidad.

```text
SOURCE_USED_BY_DEVICE != DEVICE_OWNED_KNOWLEDGE
SRC_RECORD = CANONICAL_SOURCE_IDENTITY
EXECUTABLE_DERIVATIVE = DEVICE
```

## Baseline que debe preservarse

```text
repository = lopezcarlton/vocesdelasnubes
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

Antes del corte, el nuevo repositorio técnico debe reproducir el cierre ya demostrado para runtime v0.2.15.3:

- dependencias históricas exactas necesarias;
- replay `exit 0`;
- hashes semánticos coincidentes;
- `SUMMARY` y `METRICS` deterministas exactos;
- 38/38 pruebas históricas;
- `COR001 = ANALYSIS_TARGET_ONLY`.

## Fase 0 — realizada

- frontera constitucional formalizada;
- `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO` vigente;
- reentrada general y técnica separadas;
- backlog técnico separado;
- provenance canónica hacia `dispositivo/` eliminada;
- `KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md` activo;
- raíz del repositorio simplificada y sistemas derivados clasificados.

## Fase 1 — identidad de fuentes críticas — realizada 2026-09-03

La revisión del core y del runtime muestra que las fuentes externas centrales materializadas o citadas por el dispositivo ya pueden resolverse desde Voces sin ejecutar el runtime.

Registros canónicos principales:

- `SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR` — Gramática Popular / `BIB004`;
- `SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO` — Vocabulario / `BIB003`;
- `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` — fuente de los inventarios Dictionaria y `DIC_VERB_2385`;
- `SRC-BUENO-HOLLE-2019` — monografía, ubicación pública, DOI, licencia y hash de la copia de trabajo;
- `SRC-PEREZ-BAEZ-CATA-BUENO-HOLLE-2015-XNEZA` — ortografía/palabra gráfica;
- `SRC-PEREZ-BAEZ-2015-VALENCE-CHANGING-JUCHITAN` — cambio de valencia/causatividad;
- `SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES` — clases verbales usadas por la capa PBK;
- `SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS` — descripción fonética de Juchitán.

Comprobaciones de las capas técnicas recuperadas:

- `BOUND` cita `BIB004_GRAMATICA_POPULAR` y `BIB054_DICTIONARIA`;
- Morphology I cita `BIB059_PBK2016`, correspondiente al trabajo de Pérez Báez y Kaufman sobre clasificación verbal;
- Morphology II cita Dictionaria, PBK2016 y Pérez Báez 2015;
- `PERSON_POSSESSION_EXACT_REGISTRY` vuelve a `BIB004_GRAMATICA_POPULAR` con secciones/cuadros exactos;
- el backfill Pickett permanece derivado técnico del Vocabulario;
- `JUCHITAN_LINGUISTIC_CORE_v0_27` permanece compilación experimental y no fuente.

Los aliases históricos `BIB054`, `BIB059`, `BIB060` usados dentro del dispositivo **no deben promoverse ni corregirse por inferencia en Voces** hasta reconciliar la hoja bibliográfica maestra mediante `BL-026`. Los `SRC-*` bastan para resolver la identidad documental durante el corte.

No es requisito reingerir de golpe todo el contenido de estas obras. La lectura/adjudicación se hará incrementalmente cuando una pregunta de investigación lo requiera.

## Fase 2 — crear el repositorio técnico separado — bloqueada por infraestructura

Crear un repositorio técnico separado bajo el control de Emiliano y mover el árbol activo de `dispositivo/`, preservando en la medida posible historia y referencias al repo/commit de origen.

Debe contener como mínimo:

- Analyzer / Corrector / Tutor / Generator;
- runtime y bases ejecutables;
- tests;
- migración y estado técnico;
- `REENTRY_TECNICO.md`;
- `BACKLOG_TECNICO.md`;
- `KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md`;
- workflow manual del replay histórico;
- prompts técnicos históricos.

**Bloqueo actual:** las herramientas disponibles en esta sesión permiten escribir dentro de repositorios existentes pero no crear un repositorio GitHub nuevo. No existe aún un repositorio técnico destino bajo `lopezcarlton`.

No utilizar `lopezcarlton/ELDP` como destino.

## Fase 3 — vincular el estado de Voces

Toda versión reproducible del dispositivo debe registrar:

```text
KNOWLEDGE_SOURCE_REPOSITORY = lopezcarlton/vocesdelasnubes
KNOWLEDGE_SOURCE_COMMIT = <commit exacto>
```

Cuando una compilación dependa de fuentes concretas, puede registrar además sus `SRC-*` correspondientes.

## Fase 4 — verificar antes del corte

En el repositorio técnico separado:

1. verificar artefactos críticos;
2. ejecutar replay histórico;
3. ejecutar 38 pruebas;
4. comprobar reentry técnico;
5. comprobar `KNOWLEDGE_SOURCE_COMMIT`;
6. comprobar que las fuentes documentales críticas pueden resolverse desde Voces sin depender del repo técnico;
7. comprobar que ninguna instrucción técnica concede autoridad de escritura sobre Voces.

**No retirar el dispositivo activo de Voces hasta que esta fase pase.**

## Fase 5 — retirar la copia activa de Voces y aplicar permisos

Después de la verificación:

- retirar de `main` la copia activa de `dispositivo/` o dejar únicamente una referencia mínima;
- conservar la historia previa en Git y el baseline congelado;
- configurar el repositorio de Voces para que desarrolladores del dispositivo sean read-only por defecto;
- configurar el repositorio técnico con permisos propios de desarrollo.

`CODEOWNERS` documenta ownership, pero la frontera física sólo queda completa con permisos/rulesets adecuados.

## Criterio de éxito

```text
DEVICE_REPO_REPLAY = PASS
DEVICE_REPO_TECHNICAL_TESTS = PASS
KNOWLEDGE_SOURCE_COMMIT = EXPLICIT
CRITICAL_SOURCE_IDENTITY_UNRESOLVED = 0
DEVICE_DEVELOPER_CANONICAL_WRITE_BY_DEFAULT = false
VOCES_REENTRY_DOES_NOT_REQUIRE_DEVICE_REPO = true
VOCES_CAN_RESOLVE_SHARED_SOURCES_WITHOUT_DEVICE_REPO = true
```

## Lo que este plan no autoriza

- no cambia P1–P5;
- no convierte una tabla técnica en fuente canónica;
- no publica materiales con derechos no verificados;
- no convierte el runtime histórico en arquitectura futura;
- no borra genealogía para simplificar el repositorio;
- no corta el dispositivo antes de verificar replay y pruebas.
