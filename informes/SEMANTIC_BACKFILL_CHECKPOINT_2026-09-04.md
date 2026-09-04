# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `ACTIVE / KNOWLEDGE_MIGRATION_GAP_CONFIRMED`  
**Repositorio autoritativo:** `lopezcarlton/vocesdelasnubes`

## 1. Diagnóstico

Durante la revisión conjunta del *Alfabeto Popular para la escritura del zapoteco del Istmo* de 1956 se detectó un problema de migración del conocimiento:

```text
SOURCE_IDENTITY_MIGRATED = YES
LEGACY_TECHNICAL_EXTRACTIONS_EXIST = YES
CANONICAL_SEMANTIC_PROMOTION_TO_VOCES = INCOMPLETE
```

Varias fuentes prioritarias estaban correctamente identificadas en `conocimiento/fuentes/`, y el repositorio técnico histórico conservaba reglas derivadas de ellas, pero algunos hechos lingüísticos ya estudiados no habían sido promovidos como `HALL` canónicos en Voces.

Esto produjo una falsa apariencia de incertidumbre al leer la fuente de 1956 de manera demasiado aislada.

## 2. Casos que revelaron el problema

Quedaron reparados de inmediato:

- segunda persona singular sin oposición gramatical `tú/usted` → `HALL-0066`;
- inventario contemporáneo de tres tonos fonémicos → `HALL-0067`;
- continuidad de la regla contextual `xh/x` ante consonante → `HALL-0068`;
- `r` débil como patrón general y `r` fuerte como excepción léxica / préstamos → `HALL-0069`;
- atestación dialectal `tobi` Juchitán / `tubi` El Espinal → `HALL-0070`, `HALL-0071`;
- Alfabeto Popular como base fundacional y referencia de la tradición ortográfica posterior → `HALL-0072`.

Se corrigieron además hallazgos del Alfabeto que habían quedado demasiado abiertos:

- `HALL-0032` — cuatro tonos de 1956 recontextualizados frente al sistema contemporáneo de tres;
- `HALL-0048` — `xh/x` vinculado con fuentes posteriores;
- `HALL-0052` — `r` histórica vinculada con distribución contemporánea;
- `HALL-0061` — `tú/usted` resuelto por contraste con Gramática Popular y Vocabulario.

## 3. Fuentes prioritarias para backfill sistemático

La reparación puntual no sustituye una reingesta semántica controlada. Prioridad propuesta:

### P0-A — Gramática Popular

`SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`

Objetivo: recorrer el conocimiento históricamente compilado en `JUCHITAN_LINGUISTIC_CORE_v0_27` únicamente como índice de recuperación y comprobar cada regla contra la fuente original. Promover a Voces reglas, paradigmas, excepciones y límites todavía ausentes.

### P0-B — Pickett–Villalobos–Marlett 2009/2010 + corrigendum

Objetivo: formalizar inventario segmental/tonal, fortis-lenis, vibrantes, fonación, acento y realizaciones contextuales, distinguiendo fonema, alófono, convención ortográfica y dato acústico.

### P0-C — Xneza diidxazá 2015

Objetivo: completar la ingesta de fonología, genealogía del Alfabeto Popular, palabra fonológica/gramatical/ortográfica, compuestos, colocaciones, clíticos y problemas de normalización.

### P0-D — Bueno Holle 2019

Objetivo: completar fonología/prosodia relevante, metodología de corpus, sintaxis de discurso, referencia, tópico/foco y cualquier consecuencia real para analizador, tutor y generador.

### P1 — Vocabulario Pickett

Objetivo: promover notas gramaticales y ortográficas reutilizables que actualmente existen principalmente como backfills técnicos o evidencia lexicográfica dispersa.

### P1 — Cardona 2020 y Cardona–Vicente 2025

Objetivo: consolidar distribución dialectal y representación ortográfica de variación para evitar que `variante local` se convierta en `error` por falta de contexto.

### P0 bloqueado por acceso — Norma 2016

`SRC-CATA-ETAL-2016-NORMA-ESCRITURA`

La identidad está localizada, pero el texto completo sigue pendiente. No reconstruir su contenido desde citas indirectas.

## 4. Regla de trabajo desde este checkpoint

Antes de afirmar durante la lectura de una fuente histórica que una cuestión contemporánea está `OPEN`:

```text
1. LEER PASAJE HISTORICO
2. BUSCAR HALL/DEC/TEO VIGENTE EN VOCES
3. BUSCAR FICHA DE FUENTES POSTERIORES YA TRABAJADAS
4. SI FALTA PROMOCION, REABRIR FUENTE ORIGINAL
5. PROMOVER HALL CANONICO
6. RECIEN ENTONCES CLASIFICAR COMO RESUELTO / CONFLICTIVO / ABIERTO
```

Los derivados del dispositivo pueden utilizarse sólo para localizar coordenadas de una regla previamente estudiada:

```text
LEGACY_DEVICE_RULE_AS_RECOVERY_INDEX = ALLOWED
LEGACY_DEVICE_RULE_AS_KNOWLEDGE_AUTHORITY = FORBIDDEN
```

## 5. Consecuencia para la revisión del Alfabeto de 1956

La revisión sección por sección queda **pausada temporalmente** después de las narraciones de las páginas impresas 12–13.

No se continúa a poesía hasta haber reparado el baseline mínimo suficiente para que la lectura histórica no vuelva a crear huecos falsos o a presentar como hipótesis cuestiones ya resueltas por fuentes posteriores.

## 6. Consecuencia para el dispositivo

Voces se corrige primero. Sólo después de establecer un commit canónico que contenga los hallazgos promovidos se actualizará la representación técnica del dispositivo, conservando enlaces a `HALL`/`DEC` y al `KNOWLEDGE_SOURCE_COMMIT` utilizado.
