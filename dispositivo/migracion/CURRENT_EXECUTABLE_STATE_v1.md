# CURRENT_EXECUTABLE_STATE_v1 — Estado materializado del dispositivo

**Proyecto:** Voces de las Nubes

**Fecha:** 2026-09-01

**Estado:** `CURRENT_MIGRATION_CHECKPOINT / NON_CANONICAL / REVISABLE`

## 1. Función

Este documento distingue entre:

- artefactos presentes;
- componentes que pueden instanciarse o ejecutarse con esos artefactos;
- snapshots históricos más avanzados cuyas dependencias todavía no están materializadas;
- preguntas de investigación que permanecen abiertas.

No reemplaza los estados históricos ni concede autoridad lingüística o pedagógica al código.

```text
MIGRATED != RUNNABLE
RUNNABLE_SUBSET != COMPLETE_COMPONENT
HISTORICAL_READINESS != CURRENT_CAPABILITY
TECHNICAL_CHECK != RESEARCH_CLOSURE
```

## 2. Runtime v0.2.15.3

El manifiesto original enumera 75 payloads. En este checkpoint hay 10 payloads presentes:

- 9 coinciden con el SHA-256 del release, incluida la SQLite v2.20;
- `DB_INTEGRITY_v0_2_15_3.json` está presente pero no coincide con el hash del release;
- 65 payloads del release todavía no están migrados.

La SQLite exacta está en:

`runtime/v0_2_15_3/BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite`

Verificación:

```text
SHA256 = 2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed
SQLITE_INTEGRITY_CHECK = ok
FOREIGN_KEY_VIOLATIONS = 0
canonical_state_v17 = 22 rows
verb_lexeme_class_v023 = present
person_possession_exact_v0214 = present
```

Discrepancia preservada, no corregida retrospectivamente:

```text
DB_INTEGRITY expected = fa2b88c95b8d567b4165b49636f67cdf8c00fa1a036cf8c162d03a6bceb193bb
DB_INTEGRITY present  = bcd0cf4046eb0d949dce29f098bd5d5f5e9e657f2636ce592f76ddcbd082eae4
```

## 3. Analyzer v0.35

Estado: `SOURCE_PRESENT / DEPENDENCIES_INCOMPLETE / NOT_REPRODUCIBLE_YET`.

Presentes:

- orquestador v0.35;
- `DIC_VERB_2385_v0_1.csv` exacto;
- módulos runtime v0.2.1, v0.2.3, v0.2.4 y v0.2.5;
- SQLite v2.20 exacta con las tablas críticas verificadas.

Faltan:

- `DICTIONARIA_entries_v0_2_15_2.csv`;
- `DICTIONARIA_senses_v0_2_15_2.csv`;
- `DICTIONARIA_examples_v0_2_15_2.csv`.

No debe declararse reproducible hasta incorporar y verificar esos tres archivos.

## 4. Generator_v0.5

`generator_v0_5.py` se preserva como la implementación histórica más reciente localizada. Su entrada por defecto no es ejecutable en el árbol migrado porque combina rutas de dos layouts distintos y espera `NovelRecombinationAttempt_v0_1.json`, que no está presente.

Para no alterar silenciosamente el artefacto histórico se añadió:

`generator/generator_v0_5_migrated_adapter.py`

El adaptador usa exclusivamente `generator/inputs/` y permite instanciar el subconjunto realmente materializado:

```text
PARADIGM_CELLS = 72
CONSTRUCTIONS = 6
GENERATION_LICENSES = 6
ACTIVE_LICENSE_CONSTRUCTIONS = C01, C02
BLOCKED_BY_MIGRATED_INPUTS = C03, C04, C05, C06
```

`GENERATION_READINESS_MATRIX_v14.csv` se conserva como el snapshot más reciente localizado, pero sus capacidades C03/C05 no son reproducibles con los archivos actualmente migrados. No se rebajó ni se reescribió la matriz: queda clasificada como:

`MIGRATED_SNAPSHOT_NOT_REPRODUCIBLE_WITH_CURRENT_FILES`.

## 5. Tutor_v0.33

Estado: `SOURCE_PRESENT / DEPENDENCIES_INCOMPLETE / NOT_INSTANTIABLE_YET`.

Faltan `TutorCaseLicenseBindings_v0_33.jsonl` y las licencias C03/C05 enumeradas en el manifiesto. La presencia del renderer no equivale a un Tutor ejecutable.

## 6. COR001 y terminología histórica

`core/JUCHITAN_LINGUISTIC_CORE_v0_27.md` conserva una referencia a “benchmarks COR001”. Esa formulación no representa la política vigente y no se usa como contrato de ejecución.

El rol actual es:

```text
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

La frase histórica no se reescribió dentro del core experimental para no alterar silenciosamente el artefacto migrado.

## 7. Interpretación

Este checkpoint no decide si C03, C05, la escala P, las capas BIB065 u otra hipótesis deben mantenerse o cambiar. Sólo evita atribuir al repositorio capacidades que sus archivos actuales no pueden reproducir.

Las líneas de investigación, COR002, el trabajo con hablantes y la incorporación de nueva evidencia continúan abiertas conforme a `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`.
