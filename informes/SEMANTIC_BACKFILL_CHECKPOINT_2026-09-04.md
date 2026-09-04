# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `ACTIVE / PBK2016_PILOT_COMPLETED / BROADER_BACKFILL_PENDING`  
**Repositorio autoritativo:** `lopezcarlton/vocesdelasnubes`

## 1. Diagnóstico

Durante la revisión conjunta del *Alfabeto Popular para la escritura del zapoteco del Istmo* de 1956 se detectó un problema de migración del conocimiento:

```text
SOURCE_IDENTITY_MIGRATED = YES
LEGACY_TECHNICAL_EXTRACTIONS_EXIST = YES
CANONICAL_SEMANTIC_PROMOTION_TO_VOCES = INCOMPLETE
```

Varias fuentes prioritarias estaban correctamente identificadas en `conocimiento/fuentes/`, y el repositorio técnico histórico conservaba reglas derivadas de ellas, pero algunos hechos lingüísticos ya estudiados no habían sido promovidos como `HALL` canónicos ni habían quedado suficientemente resumidos en sus `SRC`.

Esto produjo dos síntomas:

1. falsa apariencia de incertidumbre sobre asuntos ya estudiados;
2. consultas lentas que reconstruían demasiado estado y terminaban entrando al dispositivo para recuperar conocimiento bibliográfico.

No se crea una nueva capa arquitectónica para resolverlo. Los `SRC` existentes funcionan como identidad y **memoria persistente de lectura**; `HALL/TEO/VAL/DEC` conservan la promoción/adjudicación; el dispositivo permanece como sistema derivado.

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

## 3. Piloto PBK2016 — clases verbales

El caso `SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES` confirmó que la fuente había sido ingerida antes de la separación, aunque esa ingesta no quedó suficientemente visible desde Voces.

Evidencia de recuperación histórica:

- once reglas `PBK-VERB-*` / `PBK-DER-*` sobreviven en el runtime;
- la SQLite histórica conserva once filas `BIB059_PBK2016` en `morphology_rule_registry_v023`;
- `DIC_VERB_2385_v0_1.csv` conserva 2,385 registros verbales derivados de Dictionaria con clase, TAM, provenance y otros campos.

Para no promover conocimiento desde artefactos técnicos, se reabrieron directamente **sólo los pasajes pertinentes** del artículo original y se materializó:

- `HALL-0073` — sistema A–D diagnosticado principalmente por potencial y completivo;
- `HALL-0074` — habitual como vía de aislamiento de raíz y predictibilidad del resto del paradigma una vez conocida la clase;
- `HALL-0075` — distribución cuantitativa e irregularidad del sistema descrito;
- `HALL-0076` — separación entre notación analítica PBK/PDLMA y superficie del Alfabeto Popular.

Se amplió además el `SRC` de PBK2016 con cobertura, coordenadas, notación, límites, derechos y memoria persistente de lectura.

Resultado:

```text
GENERAL_VERB_CLASS_QUERY_CAN_BE_ANSWERED_FROM_VOCES = true
FULL_PBK_PDF_REREAD_REQUIRED = false
DEVICE_REQUIRED_FOR_GENERAL_CLASS_SYSTEM = false
```

La asignación individual de clase a los 2,385 registros sigue siendo primariamente una cuestión documental de Dictionaria. El CSV técnico puede ayudar temporalmente a recuperar un registro, pero no se copia completo a Voces por defecto para evitar peso y duplicación.

## 4. Regla consulta vs adjudicación

La optimización no modifica la garantía epistemológica.

### Consulta

```text
ROUTINE_QUERY
-> HALL / TEO / DEC / VAL PERTINENTE
-> SRC PARA PROVENANCE / COBERTURA SI HACE FALTA
-> RESPONDER
```

No reabrir el PDF/libro completo si el conocimiento ya está suficientemente registrado.

### Nueva adjudicación

```text
NEW_OR_CHANGED_CANONICAL_CLAIM
-> LOCATE RELEVANT SOURCE COORDINATE
-> OPEN RELEVANT SOURCE PASSAGE
-> ADJUDICATE
-> UPDATE ONLY NECESSARY ENTITIES/VIEWS
```

Se conserva:

```text
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
```

Los derivados del dispositivo pueden utilizarse sólo para localizar coordenadas o detectar huecos:

```text
LEGACY_DEVICE_RULE_AS_RECOVERY_INDEX = ALLOWED
LEGACY_DEVICE_RULE_AS_KNOWLEDGE_AUTHORITY = FORBIDDEN
```

## 5. Fuentes prioritarias para backfill sistemático

La reparación puntual y el piloto PBK2016 no sustituyen el backfill de las otras fuentes prioritarias.

### P0-A — Gramática Popular

`SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`

Objetivo: recorrer el conocimiento históricamente compilado en `JUCHITAN_LINGUISTIC_CORE_v0_27` únicamente como índice de recuperación, verificar por bloques los pasajes necesarios y promover a Voces reglas, paradigmas, excepciones y límites todavía ausentes.

No releer el libro linealmente desde cero si las coordenadas de ingesta histórica permiten una revisión dirigida.

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

## 6. Reentrada y rendimiento

`INICIAR_AQUI_CHAT_NUEVO.md` fue cambiado el 2026-09-04 de reconstrucción exhaustiva a `LAZY_TARGETED_LOADING`.

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
NORMAL_VOCES_QUERY_DOES_NOT_LOAD_DEVICE = true
```

La mejora estructural puede evaluarse por reducción de lecturas necesarias. La latencia real de la aplicación debe medirse en un chat nuevo, porque un chat largo conserva su propio contexto anterior y no permite aislar el efecto del nuevo reentry.

## 7. Consecuencia para la revisión del Alfabeto de 1956

La revisión sección por sección queda **pausada temporalmente** después de las narraciones de las páginas impresas 12–13.

No se continúa a poesía hasta haber reparado el baseline mínimo suficiente para que la lectura histórica no vuelva a crear huecos falsos o a presentar como hipótesis cuestiones ya resueltas por fuentes posteriores.

## 8. Consecuencia para el dispositivo

Voces se corrige primero. Después de cada bloque suficientemente estable, el dispositivo puede actualizar su representación técnica conservando enlaces a `HALL`/`DEC` y al `KNOWLEDGE_SOURCE_COMMIT` utilizado.

```text
VOCES = AUTHORITY_FOR_KNOWLEDGE
DEVICE = DERIVED_IMPLEMENTATION
```
