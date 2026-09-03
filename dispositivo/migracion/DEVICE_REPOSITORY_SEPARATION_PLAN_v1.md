# DEVICE_REPOSITORY_SEPARATION_PLAN_v1

**Estado:** `PLANNED / NON_DESTRUCTIVE / NOT_YET_EXECUTED`  
**Versión interna:** 1.1  
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

No se crea un tercer "sistema de acervo".

Las gramáticas, vocabularios, corpus, diccionarios, datasets documentales, normas y bibliografía se identifican desde `conocimiento/fuentes/` mediante `SRC-*`. El payload puede vivir en el repositorio o en una ubicación externa/restringida según derechos y acceso.

El dispositivo conserva únicamente sus representaciones técnicas y los fixtures exactos necesarios para reproducibilidad.

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

## Fase 0 — Ya realizada

- frontera constitucional formalizada;
- `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO` vigente;
- reentrada general y técnica separadas;
- backlog técnico separado;
- provenance canónica hacia `dispositivo/` eliminada;
- `KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md` activo;
- raíz del repositorio simplificada y sistemas derivados clasificados.

## Fase 1 — Resolver fuentes que hoy están atrapadas dentro de `dispositivo/`

Antes del corte, revisar únicamente los materiales que el dispositivo contiene y que podrían ser fuente documental o derivado neutral.

Para cada caso hay que responder:

1. ¿Existe ya un `SRC-*` en Voces?
2. ¿Cuál es la fuente original, edición o versión?
3. ¿Dónde vive el payload accesible al proyecto?
4. ¿Puede redistribuirse públicamente?
5. ¿Qué archivo del dispositivo es sólo una transformación técnica o fixture histórico?

Casos prioritarios:

- Gramática Popular / Pickett–Black–Marcial;
- Vocabulario zapoteco del Istmo;
- Bueno Holle / BIB065;
- Dictionaria;
- fuentes fonéticas y morfológicas;
- datasets léxicos de Pickett;
- corpus externos utilizados por el dispositivo.

Cuando el original sea restringido, basta con que el `SRC` conserve identidad, ubicación, acceso, hash cuando exista y restricciones conocidas. **No hay que copiar el archivo al repositorio público para que Voces sea dueño epistemológico de la fuente.**

No retirar de `dispositivo/` la única copia identificable de un material hasta que su fuente quede resuelta en Voces.

## Fase 2 — Crear el repositorio técnico separado

Mover el árbol activo de `dispositivo/` preservando, en la medida posible, historia y referencias al repo/commit de origen.

Debe contener como mínimo:

- Analyzer / Corrector / Tutor / Generator;
- runtime y bases ejecutables;
- tests;
- migración y estado técnico;
- `REENTRY_TECNICO.md`;
- `BACKLOG_TECNICO.md`;
- `KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md`;
- workflow manual del replay histórico.

Los prompts técnicos históricos ya están bajo `dispositivo/prompts/` y deben viajar con esta capa.

## Fase 3 — Vincular el estado de Voces

Toda versión reproducible del dispositivo debe registrar:

```text
KNOWLEDGE_SOURCE_REPOSITORY = lopezcarlton/vocesdelasnubes
KNOWLEDGE_SOURCE_COMMIT = <commit exacto>
```

Cuando una compilación dependa de fuentes concretas, puede registrar además sus `SRC-*` correspondientes.

No hace falta otro manifiesto de autoridad si la procedencia puede reconstruirse desde esos `SRC` y el commit de conocimiento.

## Fase 4 — Verificar antes del corte

En el repositorio técnico separado:

1. verificar artefactos críticos;
2. ejecutar replay histórico;
3. ejecutar 38 pruebas;
4. comprobar reentry técnico;
5. comprobar `KNOWLEDGE_SOURCE_COMMIT`;
6. comprobar que las fuentes documentales críticas pueden resolverse desde Voces sin depender del repo técnico;
7. comprobar que ninguna instrucción técnica concede autoridad de escritura sobre Voces.

**No retirar el dispositivo activo de Voces hasta que esta fase pase.**

## Fase 5 — Retirar la copia activa de Voces y aplicar permisos

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
