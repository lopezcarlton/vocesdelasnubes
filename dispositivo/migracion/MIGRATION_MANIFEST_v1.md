# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Última actualización:** 2026-09-02 — pasada dirigida sobre artefactos realmente disponibles en el chat del corrector/Pickett; se reconfirmó el P0 `PICKETT_LEXICON_BACKFILL_v0_1.csv`, se registraron paquetes completos de investigación ortográfica/corrector como transferencia binaria pendiente y no se modificó el estado ejecutable.

**Estado:** ACTIVE_INVENTORY / NO_BLOCKING  
**Alcance:** recuperación selectiva del estado técnico y documental del dispositivo

## 1. Principio

La migración preserva conocimiento, procedencia y capacidad reproducible. **No congela la investigación ni convierte la arquitectura recuperada en arquitectura definitiva.**

Se rige por `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md` y por `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md`.

```text
MIGRATED_ARTIFACT != IMMUTABLE_RULE
IMPLEMENTED_CAPABILITY != RESEARCH_AUTHORITY
MIGRATION_STATUS != PEDAGOGICAL_PRIORITY
MIGRATION_INCOMPLETE != RESEARCH_BLOCKED
CHAT != MIGRATION_ARTIFACT
```

COR001, COR002, corpus oral, trabajo con hablantes, investigación pedagógica, lectura bibliográfica y nuevas hipótesis pueden continuar durante la migración salvo dependencia técnica concreta.

COR001 mantiene exclusivamente:

```text
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

## 2. Estados

- `MIGRATED`: ya existe en el repositorio.
- `RECOVERABLE_SOURCE_LOCATED`: fuente externa concreta localizada.
- `REFERENCED_BY_LOCATED_ARTIFACT`: existencia documentada, archivo aún no recuperado.
- `EXTERNAL_KNOWN_NOT_MIGRATED`: estado conocido, fuente exacta aún no localizada.
- `NOT_LOCATED_IN_CURRENT_PASS`: no apareció en esta búsqueda; no equivale a perdido.
- `SUPERSEDED`: antecedente que no representa el estado vigente.
- `ARCHIVE_ONLY`: trazabilidad histórica, no pieza activa.
- `SOURCE_COMPLETE_READY_TO_MIGRATE`: fuente completa disponible y lista para copia exacta.
- `SOURCE_PARTIAL_DO_NOT_MIGRATE`: sólo existe contenido parcial o truncado.
- `BINARY_TRANSFER_PENDING`: artefacto identificado cuya transferencia íntegra no es posible todavía con la herramienta disponible.
- `FAILED_INCOMPLETE_TRANSFER`: intento de transporte que no produjo un artefacto íntegro ni verificable; sus residuos no deben tratarse como fuente.

Ningún estado concede autoridad lingüística o pedagógica.

## 3. Migrado

| Artefacto | Función / estado recuperado |
|---|---|
| `dispositivo/README.md` | arquitectura y frontera del dispositivo |
| `dispositivo/ESTADO_ACTUAL_2026-08-31.md` | snapshot técnico previo a la migración |
| `dispositivo/ANALYZER_SCOPE_MULTIESCALA_2026-08-31.md` | alcance palabra → discurso |
| `dispositivo/PROVENANCE_LABEL_CROSSWALK_v0_1.md` | equivalencias de procedencia |
| `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` | discusión pedagógica no normativa |
| `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md` | matriz bibliográfica reparada; fuente documental P1, no promoción automática a runtime/política |
| `dispositivo/migracion/fuentes/MVP_REUSE_MAP_v1.md` | mapa de reutilización/cuarentena del vertical slice |
| `dispositivo/migracion/fuentes/mvp_vertical_slice_v0_2/` | ocho payloads textuales exactos del patch/adjudicación MVP v0.2; `ARCHIVE_ONLY / NON_AUTHORITY` |
| `dispositivo/migracion/fuentes/mvp_audio_review_v0_1/` | siete payloads textuales exactos de revisión acústica; `ARCHIVE_ONLY / NON_AUTHORITY`; binarios de audio/figuras pendientes |
| `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md` | protocolo de migración directa |
| `dispositivo/core/NUCLEO_CONVERSACIONAL_001_SCOPE_v1.md` | scope exacto del vertical slice NC001 |
| `dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md` | fuente completa; `EXPERIMENTAL_CORE`, baseline verificable actual |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v1.md` | checkpoint pre-Generator; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` | estado post Generator_v0 |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v3_POST_ROUNDTRIP_BRIDGE.md` | primer bridge round-trip y primera recombinación novedosa; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v4_POST_ROUNDTRIP_STABILIZATION.md` | estabilización round-trip v0.2; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/ROUNDTRIP_CONTRACT_v0_2.md` | contrato histórico `STRUCTURAL_COMPATIBILITY_ONLY_NON_LICENSING` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v34_POST_C02_DEFAULT_QUI_MIGRATION.md` | transición C02 a `quí`; `qué` queda variante secundaria |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v35_POST_EVIDENCE_GAP_PRIORITIZER.md` | priorizador de huecos; COR001 sigue analysis-only |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v36_POST_KNOWLEDGE_INGESTION_GUARDRAILS.md` | guardrails y ruta literatura+audio |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md` | ruta activa más reciente localizada |
| `dispositivo/migracion/fuentes/SINTESIS_ADVERSARIAL_ARQUITECTURA_DIDXAZA_v1_1_CORREGIDA.md` | adjudicación arquitectónica histórica; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/generator_v0_initial/` | scaffold inicial Generator_v0, licencias, blockers, adapters, tests y reportes; `ARCHIVE_ONLY / SUPERSEDED` |
| `dispositivo/generator/inputs/ConstructionInventory_v1.jsonl` | seis construcciones NC001 |
| `dispositivo/generator/inputs/ParadigmTable_v1.csv` | 72 celdas TAM/persona con procedencia |
| `dispositivo/validation/ValidationQueue_v0.jsonl` | cola de validación/desarrollo audio-first |
| `dispositivo/analyzer/non_licensing_analyzer_orchestrator_v0_35.py` | Analyzer parcial no licenciante |
| `dispositivo/analyzer/analyzer_v0_35_migrated_adapter.py` | adaptador reproducible del Analyzer v0.35 |
| `dispositivo/analyzer/DIC_VERB_2385_v0_1.csv` | inventario exacto de 2,385 verbos |
| `dispositivo/analyzer/reports/COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md` | reporte histórico exacto; `ANALYSIS_TARGET_ONLY / NON_AUTHORITY` |
| `dispositivo/runtime/v0_2_15_3/BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite` | SQLite v2.20 exacta, integridad verificada |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_entries_v0_2_15_2.csv` | 9,012 entradas exactas |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_senses_v0_2_15_2.csv` | 9,046 sentidos exactos |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_examples_v0_2_15_2.csv` | 9,686 ejemplos exactos |
| `dispositivo/runtime/v0_2_15_3/run_cor001_replay_v0_2_15_3.py` | runner exacto del replay histórico; sólo reproducibilidad técnica |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_10_documentary_alignment.py` | módulo exacto requerido por el replay |
| `dispositivo/runtime/v0_2_15_3/DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_15_2.csv` | registry exacto; identidad byte a byte verificada |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_11_pickett_backfill.py` | módulo exacto requerido por el replay |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_12_pickett_cross_source.py` | módulo exacto requerido por el replay |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_14_person_possession.py` | módulo exacto requerido por el replay |
| `dispositivo/runtime/v0_2_15_3/COR001_REPLAY_INPUT_v0_2_15_2.csv` | input histórico exacto; `ANALYSIS_TARGET_ONLY` |
| `dispositivo/runtime/v0_2_15_3/PERSON_POSSESSION_EXACT_REGISTRY_v0_2_15_2.csv` | registry exacto GP persona/posesión |
| `dispositivo/generator/generator_v0_5.py` | implementación Generator más reciente localizada |
| `dispositivo/generator/generator_v0_5_migrated_adapter.py` | adaptador al layout migrado |
| `dispositivo/generator/GENERATION_READINESS_MATRIX_v14.csv` | snapshot readiness más reciente localizado |
| `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md` | checkpoint de presencia/ejecutabilidad/reproducibilidad |
| `dispositivo/migracion/test_migrated_state.py` | verificaciones del estado migrado |
| `dispositivo/tutor/tutor_v0_33.py` | Tutor renderer conservador; dependencias incompletas |
| `dispositivo/generator/inputs/GenerationLicense_v0_33_c02_default_qui.jsonl` | licencias activas v0.33 |
| `dispositivo/generator/inputs/GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl` | átomos de evidencia v0.33 |
| `dispositivo/generator/inputs/AuthorizedSlotFillers_v0_33.jsonl` | fillers autorizados por slot |
| `dispositivo/generator/inputs/IntegrationBlockers_v0_1.jsonl` | bloqueadores C03–C06 |
| `dispositivo/generator/inputs/OrthographicResolutions_v0_9.jsonl` | resoluciones ortográficas exactas por celda |
| `dispositivo/generator/inputs/AdoptionRecords_v1.jsonl` | guardas/adopciones NC001 |
| `dispositivo/generator/inputs/ConceptMapping_v1.jsonl` | HABITUAL/COMPLETIVE, sin proyección automática a superficie |
| `dispositivo/generator/inputs/OrthographicProfile_v1_DRAFT.json` | vector ortográfico conservador, no norma global |

## 4. Runtime v0.2.15.3 — estado de recuperación

Fuente histórica:

```text
didxaza_v0_2_15_3_surface_semantics_resolution_integrity_CLOSED_PASS(1).zip
ZIP SHA256 = 6e5c3e8ee9bb5dbd04666537dc423724eb4bc402440e670e5be81cfa54b5d7e5
```

`RELEASE_FILE_MANIFEST_v0_2_15_3.json` enumera 75 payloads. Permanecen **37/75 payloads exactos recuperados** y 38 ausentes.

SQLite:

```text
BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite
SHA256 = 2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed
SQLITE_INTEGRITY_CHECK = ok
FOREIGN_KEY_VIOLATIONS = 0
canonical_state_v17 = 22 rows
verb_lexeme_class_v023 = present
person_possession_exact_v0214 = present
```

El slice final de semántica de superficie y la cadena histórica de 38 pruebas permanecen reproducibles desde artefactos almacenados. El replay end-to-end histórico todavía no se regenera porque falta una dependencia directa.

### 4.1 P0 — Pickett Lexical Backfill

Fuente completa localizada y reconfirmada en los archivos de este chat:

```text
PICKETT_LEXICON_BACKFILL_v0_1.csv
SHA256 = 56e2372566cec9d7758b7e45b8de4e320a92eb2ee5c51b2a5e444e8165875723
SIZE = 940709 bytes
DATA_ROWS = 2534
STATUS = SOURCE_COMPLETE_READY_TO_MIGRATE / EXACT_BYTE_TRANSFER_PENDING
```

También están identificados dos uploads históricos idénticos del paquete v0.2.11:

```text
didxaza_v0_2_11_pickett_backfill_CLOSED_PASS(1).zip
didxaza_v0_2_11_pickett_backfill_CLOSED_PASS(2).zip
SHA256 = 8d7da40dc0c9559f922a0a9a523bc389547997571a7276a8f5230b978a322773
```

El CSV es **la única dependencia directa faltante** para regenerar el replay histórico v0.2.15.3. La herramienta disponible en esta pasada no puede transportar byte-exactamente el archivo referenciado por `file_search`; no se reconstruye desde snippets, tablas parseadas ni otra extracción de Pickett.

## 5. Analyzer, Generator y Tutor

### Analyzer v0.35

```text
STATUS = MIGRATED / REPRODUCIBLE_NON_LICENSING_PARTIAL_ANALYZER
```

Dependencias directas presentes: runtime retrieval/morphology/BOUND, Dictionaria exacta, `DIC_VERB_2385_v0_1.csv`, SQLite con tablas críticas. El Analyzer puede abstenerse y no concede licencia de generación, corrección, autoridad ortográfica ni descubrimiento de reglas.

### Generator v0.5

Genealogía localizada:

```text
generator_v0.py -> generator_v0_1.py -> generator_v0_2.py -> generator_v0_3.py -> generator_v0_4.py -> generator_v0_5.py
```

`generator_v0_5.py` es la implementación más reciente localizada. El adaptador migrado materializa:

```text
PARADIGM_CELLS = 72
CONSTRUCTIONS = 6
GENERATION_LICENSES = 6
ACTIVE_LICENSE_CONSTRUCTIONS = C01, C02
BLOCKED_BY_MIGRATED_INPUTS = C03, C04, C05, C06
```

`GENERATION_READINESS_MATRIX_v14.csv` permanece `MIGRATED_SNAPSHOT_NOT_REPRODUCIBLE_WITH_CURRENT_FILES` para capacidades históricas cuyas dependencias exactas faltan.

### Tutor v0.33

```text
STATUS = SOURCE_PRESENT / DEPENDENCIES_INCOMPLETE / NOT_INSTANTIABLE_YET
```

Faltan:

```text
TutorCaseLicenseBindings_v0_33.jsonl
GenerationLicense_C03_v0_12.jsonl
GenerationLicense_C05_v0_11.jsonl
GenerationLicense_C05_Inherent_v0_14.jsonl
GenerationLicense_C05_XHX_v0_15.jsonl
GenerationLicense_C05_Morphophonology_v0_16.jsonl
GenerationLicense_C05_Morphophonology_v0_17.jsonl
GenerationLicense_C05_Morphophonology_v0_18.jsonl
GenerationLicense_C05_Morphophonology_v0_19.jsonl
```

No apareció fuente completa adicional de esas dependencias en esta pasada.

## 6. Genealogías recuperadas

### JUCHITAN_LINGUISTIC_CORE

```text
v0.1 -> ... -> v0.23 -> ... -> v0.27
                              \-> v0.28 [QUARANTINED / NOT_CURRENT_BASELINE]
```

`v0.27` permanece la referencia verificable migrada. En este chat existe fuente completa de `JUCHITAN_LINGUISTIC_CORE_v0_28.md`:

```text
SHA256 = 6766d25f38ecd39a01a1a0e0463776e85c518325f6653603b70583562910a12a
RELATION_TO_v0_27 = v0.27 body preserved + COR001 post-grammar patch
STATUS = SOURCE_COMPLETE_READY_TO_MIGRATE / ARCHIVE_ONLY / QUARANTINED_NOT_CURRENT_BASELINE
```

No se migra en esta pasada porque no representa el baseline vigente, no cierra una dependencia ejecutable y conserva contaminación metodológica posterior puesta en cuarentena. Su identidad y relación genealógica sí quedan registradas.

### NC001

```text
v1 -> v2 -> v3 -> v4 -> ... -> v34 -> v35 -> v36 -> v37.1
```

v37.1 permanece el estado más reciente localizado.

### Runtime

```text
v0.2.0 foundation
-> v0.2.1 retrieval
-> v0.2.2 context/provenance
-> v0.2.3 morphology I
-> v0.2.4 BOUND
-> v0.2.5 morphology II
-> v0.2.6 evidence adjudication
-> v0.2.7 decision simulation
-> v0.2.7.1 integration fixes
-> v0.2.9 surface evidence/coverage
-> v0.2.10 documentary alignment
-> v0.2.11 Pickett backfill
-> v0.2.12 Pickett cross-source
-> v0.2.13 resolution vectors
-> v0.2.14 person/possession
-> v0.2.15 evidence qualification
-> v0.2.15.2 evidence integrity
-> v0.2.15.3 surface semantics/resolution integrity
```

## 7. Artefactos localizados y pendientes

| Artefacto | Estado actual | SHA-256 / evidencia |
|---|---|---|
| `PICKETT_LEXICON_BACKFILL_v0_1.csv` | `SOURCE_COMPLETE_READY_TO_MIGRATE / EXACT_BYTE_TRANSFER_PENDING / P0` | `56e2372566cec9d7758b7e45b8de4e320a92eb2ee5c51b2a5e444e8165875723`; 940709 bytes; 2534 filas |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv` | `SOURCE_COMPLETE_READY_TO_MIGRATE / EXACT_BYTE_TRANSFER_PENDING / P1` | `acffea79fe7d228a0b28f740094e5a15fd4ec0ba6d36b257cc3aaef918a83c54` |
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` acumulado; fuente independiente no recuperada en esta pasada | hash histórico `61fd21298c1260924fdc95b7e201b8d601dc83820f3d4f3686f508a74ae57c6a` |
| `DevelopmentCorpusProtocol_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` acumulado; fuente independiente no recuperada en esta pasada | hash histórico `563dc30977a1f6175e823c60a8f79f8c78f1ec81ff09b27ad0943ceaff5fd8ad` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE / historical provisional`; no recuperado independientemente en esta pasada | `f3308483c3135e43d49f2641f518aecd0dbf3c1fcbdc98f349511751ce86b295` |
| `COR001AnalysisObservations_v0_24.jsonl` | `REFERENCED_BY_LOCATED_ARTIFACT / NOT_LOCATED_IN_CURRENT_PASS` | referenciado por reporte v0.24 migrado |
| `COR001AnalysisObservationSummary_v0_24.json` | `REFERENCED_BY_LOCATED_ARTIFACT / NOT_LOCATED_IN_CURRENT_PASS` | idem |
| `COR001AnalysisHarnessCalibration_v0_24.json` | `REFERENCED_BY_LOCATED_ARTIFACT / NOT_LOCATED_IN_CURRENT_PASS` | idem |
| `run_cor001_analysis_target_pass_v0_24.py` | `REFERENCED_BY_LOCATED_ARTIFACT / NOT_LOCATED_IN_CURRENT_PASS` | idem |
| `JUCHITAN_LINGUISTIC_CORE_v0_28.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE / ARCHIVE_ONLY / QUARANTINED_NOT_CURRENT_BASELINE` | `6766d25f38ecd39a01a1a0e0463776e85c518325f6653603b70583562910a12a` |
| `PAQUETE_MIGRACION_DIDXAZA_GENERATOR_V0_INTEGRATED_v1(1).zip` | `BINARY_TRANSFER_PENDING / ARCHIVE_ONLY` | `270dff08371f6b35bbb817d5440db85811ab87f11b2c7a96a9cf8f485ed76b9a` |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `SOURCE_COMPLETE_READY_TO_MIGRATE / BINARY_TRANSFER_PENDING / ARCHIVE_ONLY` | observed `f4819f...60c948` |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `BINARY_TRANSFER_PENDING / TEXTUAL_PAYLOADS_MIGRATED / ARCHIVE_ONLY` | observed `e6524d...6185e2` |
| `MVP_LINGUISTICO_001_AUDIO_REVIEW_v0_1.zip` | `BINARY_TRANSFER_PENDING / TEXTUAL_PAYLOADS_MIGRATED / ARCHIVE_ONLY` | `52b648aa2739b36cb78e5efcef0b037de8a0681c47bbc76d04bc8731b9e6272b` |

### 7.1 Paquetes completos del trabajo ortográfico/corrector localizados en este chat

Estos paquetes existen como archivos ZIP completos en el runtime local de este chat. No están presentes en `main` y no deben confundirse con el runtime v0.2.15.3 ni con `PICKETT_LEXICON_BACKFILL_v0_1.csv`.

| Paquete | Contenido principal | Estado | SHA-256 |
|---|---|---|---|
| `picket extracción.zip` | fase documental Pickett: validación técnica, abreviaciones, ortografía, grafemas, morfología, reglas de automatización, cobertura COR001 y pendientes | `SOURCE_COMPLETE_READY_TO_MIGRATE / BINARY_TRANSFER_PENDING / NON_CANONICAL_CORRECTOR_RESEARCH_SOURCE` | `46fb0865c96ace4ffa29742b2a78c284a85b0f52f66eb3fb2f60320c77dc8a0b` |
| `diagnóstico fuentes pickett.zip` | diagnóstico de fuentes/glifos, mapeo, validación, prototipo y decisión de extracción | `SOURCE_COMPLETE_READY_TO_MIGRATE / BINARY_TRANSFER_PENDING / EXTRACTION_REPRODUCIBILITY_SOURCE` | `dee278ca50d3ba415ee745684cb0e0ea655ec882fac4e6d19f78db9862b27bc4` |
| `cierre de fase 4.zip` | extractor final y léxico estructurado Pickett: `PICKETT_LEXICO_MASTER.csv`, revisión, cobertura, métricas y cierre | `SOURCE_COMPLETE_READY_TO_MIGRATE / BINARY_TRANSFER_PENDING / NON_CANONICAL_CORRECTOR_RESEARCH_SOURCE` | `205bab2db28f9fbc9639fabde959b6d0c6164772d1fd026a5adc500d871320ec` |
| `fase 5.zip` | auditoría de COR001 contra Pickett, falsos positivos, no resueltos, métricas y conclusiones | `SOURCE_COMPLETE_READY_TO_MIGRATE / BINARY_TRANSFER_PENDING / COR001_ANALYSIS_TARGET_ONLY / NON_AUTHORITY` | `293b66233d3febe2f5e715356b3d859a7e5c9ed15e031ab766e3ad32545353a1` |

`cierre de fase 4.zip` documenta un léxico de investigación de 6,431 registros (2,780 Z→E + 3,651 E→Z). **No es identidad ni sustituto** de `PICKETT_LEXICON_BACKFILL_v0_1.csv` (2,534 registros, schema y procedencia diferentes) y por tanto no cierra el P0 del replay.

`fase 5.zip` conserva una auditoría histórica sobre COR001. Su migración futura sólo puede hacerse bajo `ANALYSIS_TARGET_ONLY / NON_AUTHORITY`; no puede usarse como benchmark, regresión, gold ni fuente de reglas.

La herramienta GitHub disponible en esta pasada no ofrece un parámetro de archivo local para transferir estos ZIP como bytes. Los intentos de materializar blobs a partir de representación textual/base64 no se consideran fuente verificable y **no se adjuntaron a ningún commit ni árbol**. Se mantienen `BINARY_TRANSFER_PENDING` en lugar de publicar una copia potencialmente corrupta.

## 8. Reuse map / cuarentenas

Permanecen fuera de licencias de generación:

```text
SequenceMatcher / near-match
normalización destructiva de diacríticos
clean_paradigm_surface() -> surface
COR001 como licencia
confidence legado
handlers particulares COR001
owner review / PROBABLE_TRANSCRIPTION_CORRECTION como licencia
```

Los artefactos históricos que trataban COR001 como benchmark/regression no se promueven al estado técnico activo. `COR001 = ANALYSIS_TARGET_ONLY` prevalece.

## 9. Commits históricos de migración registrados

Se preserva la genealogía Git previa, entre otros:

```text
554ce87239d9aa7b4a7f04be1f9378ece7afde47  migrate Juchitán linguistic core v0.27
7ab707cf33461438e832454685cbd5355f75b586  migrate exact DIC_VERB inventory
505f7125321c75238e90135e91667ae5544fa870  migrate exact SQLite v2.20
f533bf667b0a7aca94426fb24016000761502e10  migrate exact Dictionaria analyzer inputs
9d631d3db742afc6affbd1fb14179eb174c578da  make migrated Analyzer v0.35 reproducible
1349a0be610d4020a698795925a8a70702a22f2d  migrate exact runtime surface semantics slice
bdd2d9857bbaa647f239748aff3cf2af1e5bc567  migrate exact runtime v0.2.15.3 replay runner
9b33c78673b5de5bcb56c351e612c6cc4a09ef39  migrate exact runtime v0.2.10 documentary alignment
1e0a31eb1f583abad07beda41c3e8fbb41a537a1  migrate exact documentary alignment registry v0.2.15.2
b3300bb1c77c02c18b686616aad6478a079b2ad1  migrate exact v0.2.12 Pickett cross-source runtime
5d05b77327b35c3964f63f258cbe06e19ec6d003  migrate exact v0.2.14 person-possession runtime
3f9b0fab8a13cb66c20e89a76799f97d1537aa65  migrate exact person-possession registry v0.2.15.2
a4539d9eeab6ce197e5682afc1c0f2cd547ddcdd  migrate BIB065 ingestion matrix v0.36.1
d5e91c92489d52ce24041479dc54b498c6bd61b0  migrate MVP vertical slice v0.2 source artifacts
fc28f9b6808de641fc8487b12db0473533c4721e  migrate acoustic review artifacts for MVP vertical slice
e935ebe330dc1a40c1efda9e879eac104bac0a78  migrate COR001 analysis-target pass report v0.24
0c5314eeee400d0bd8e8e5fdbcc93522bf26f108  update migration manifest after COR001 analysis-target report
```

La historia completa permanece en Git; esta lista resalta cierres relevantes para el estado materializado.

## 10. Orden de recuperación restante

### P0 — conservar estado reproducible

1. transferir byte-exacto `PICKETT_LEXICON_BACKFILL_v0_1.csv`;
2. regenerar el replay en directorio aislado para verificar reproducibilidad técnica;
3. recuperar `TutorCaseLicenseBindings_v0_33.jsonl` y las licencias C03/C05 exactas del Tutor sólo si aparecen como fuentes completas.

### P1 — reproducibilidad y límites

- `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md`;
- `DevelopmentCorpusProtocol_v0_35.md`;
- `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv` byte-exacto;
- `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md`;
- paquetes corrector/Pickett de §7.1 cuando exista canal de transferencia binaria exacta;
- soportes v0.24 de COR001 si aparecen como fuentes completas.

### P2/P3

Sólo artefactos ejecutables útiles o historia necesaria para genealogía. `JUCHITAN_LINGUISTIC_CORE_v0_28.md` permanece `ARCHIVE_ONLY / QUARANTINED_NOT_CURRENT_BASELINE` y no es requisito para reproducir el estado actual.

## 11. Resultado de esta pasada

- No se volvió a migrar ningún artefacto ya `MIGRATED`.
- `JUCHITAN_LINGUISTIC_CORE_v0_27`, NC001, Analyzer, Generator, Tutor renderer, SQLite, Dictionaria, inventario verbal, ParadigmTable y ValidationQueue fueron verificados contra el inventario actual sin modificación.
- Se reconfirmó como fuente completa el P0 `PICKETT_LEXICON_BACKFILL_v0_1.csv`, pero el canal disponible no permite su transferencia byte-exacta desde la referencia de archivo de este chat.
- Se localizaron cuatro paquetes completos de trabajo ortográfico/corrector y se registraron con hashes, límites y estado de transferencia pendiente; ninguno se promovió a conocimiento canónico ni a capacidad ejecutable.
- No apareció ninguna de las nueve dependencias faltantes del Tutor ni los cuatro soportes v0.24 de COR001.
- `CURRENT_EXECUTABLE_STATE_v1.md` no se modifica porque **no cambió el estado materializado ni ejecutable**.

## 12. Próxima acción

**Siguiente P0 imprescindible para reproducir el estado:** `PICKETT_LEXICON_BACKFILL_v0_1.csv`.

Su transferencia exacta es la única dependencia directa todavía ausente para regenerar el replay histórico v0.2.15.3. Ejecutar cualquier replay sólo en un directorio aislado y comparar reproducibilidad técnica. COR001 permanece `ANALYSIS_TARGET_ONLY` y no puede licenciar reglas, correcciones, generación, benchmarks ni regresión.

Desde el punto de vista de migración entre chats, esta pasada deja documentado el último estado técnicamente recuperable de este chat. La ausencia del P0 impide afirmar reproducción end-to-end del replay, pero no exige seguir excavando archivo histórico antes de continuar la investigación.