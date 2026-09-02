# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Última actualización:** 2026-09-02 — v0.2.12 + v0.2.14 + person/possession registry exactos recuperados; replay histórico queda a una dependencia directa

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
| `dispositivo/migracion/fuentes/MVP_REUSE_MAP_v1.md` | mapa de reutilización/cuarentena del vertical slice |
| `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md` | protocolo de migración directa |
| `dispositivo/core/NUCLEO_CONVERSACIONAL_001_SCOPE_v1.md` | scope exacto del vertical slice NC001 |
| `dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md` | fuente completa; `EXPERIMENTAL_CORE`, no autoridad definitiva |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v1.md` | checkpoint pre-Generator; `ARCHIVE_ONLY` frente a estados posteriores |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` | estado post Generator_v0 |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v3_POST_ROUNDTRIP_BRIDGE.md` | primer bridge round-trip y primera recombinación novedosa; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v4_POST_ROUNDTRIP_STABILIZATION.md` | estabilización round-trip v0.2; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/ROUNDTRIP_CONTRACT_v0_2.md` | contrato histórico `STRUCTURAL_COMPATIBILITY_ONLY_NON_LICENSING` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v34_POST_C02_DEFAULT_QUI_MIGRATION.md` | transición C02 a `quí`; `qué` queda variante secundaria |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v35_POST_EVIDENCE_GAP_PRIORITIZER.md` | priorizador de huecos; COR001 sigue analysis-only |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v36_POST_KNOWLEDGE_INGESTION_GUARDRAILS.md` | guardrails y ruta literatura+audio |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md` | ruta activa más reciente localizada |
| `dispositivo/migracion/fuentes/SINTESIS_ADVERSARIAL_ARQUITECTURA_DIDXAZA_v1_1_CORREGIDA.md` | adjudicación arquitectónica histórica v1.1; `ARCHIVE_ONLY`, investigación revisable |
| `dispositivo/migracion/fuentes/generator_v0_initial/ARCHITECTURE_FREEZE_v1_1.md` | freeze local del slice; `ARCHIVE_ONLY` frente a estados posteriores |
| `dispositivo/generator/inputs/ConstructionInventory_v1.jsonl` | seis construcciones NC001 |
| `dispositivo/generator/inputs/ParadigmTable_v1.csv` | 72 celdas TAM/persona con procedencia |
| `dispositivo/validation/ValidationQueue_v0.jsonl` | cola de validación/desarrollo audio-first |
| `dispositivo/analyzer/non_licensing_analyzer_orchestrator_v0_35.py` | Analyzer parcial no licenciante |
| `dispositivo/analyzer/analyzer_v0_35_migrated_adapter.py` | adaptador reproducible del Analyzer v0.35 |
| `dispositivo/analyzer/DIC_VERB_2385_v0_1.csv` | inventario exacto de 2,385 verbos |
| `dispositivo/runtime/v0_2_15_3/BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite` | SQLite v2.20 exacta, integridad verificada |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_entries_v0_2_15_2.csv` | 9,012 entradas exactas |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_senses_v0_2_15_2.csv` | 9,046 sentidos exactos |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_examples_v0_2_15_2.csv` | 9,686 ejemplos exactos |
| `dispositivo/runtime/v0_2_15_3/run_cor001_replay_v0_2_15_3.py` | runner exacto del replay histórico v0.2.15.3; sólo reproducibilidad técnica |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_10_documentary_alignment.py` | módulo exacto v0.2.10 requerido por el runner v0.2.15.3 |
| `dispositivo/runtime/v0_2_15_3/DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_15_2.csv` | registry exacto reutilizado desde v0.2.10; SHA-256 y Git blob verificados |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_11_pickett_backfill.py` | módulo exacto v0.2.11 requerido por el runner v0.2.15.3 |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_12_pickett_cross_source.py` | módulo exacto v0.2.12 requerido por el runner v0.2.15.3 |
| `dispositivo/runtime/v0_2_15_3/didxaza_runtime_v0_2_14_person_possession.py` | módulo exacto v0.2.14 requerido por el runner v0.2.15.3 |
| `dispositivo/runtime/v0_2_15_3/COR001_REPLAY_INPUT_v0_2_15_2.csv` | input histórico exacto; sólo reproducibilidad técnica, COR001 sigue `ANALYSIS_TARGET_ONLY` |
| `dispositivo/runtime/v0_2_15_3/PERSON_POSSESSION_EXACT_REGISTRY_v0_2_15_2.csv` | registry exacto GP person/possession requerido por el replay |
| `dispositivo/generator/generator_v0_5.py` | implementación Generator más reciente localizada |
| `dispositivo/generator/generator_v0_5_migrated_adapter.py` | adaptador al layout migrado |
| `dispositivo/generator/GENERATION_READINESS_MATRIX_v14.csv` | snapshot readiness más reciente localizado |
| `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md` | checkpoint de presencia/ejecutabilidad/reproducibilidad |
| `dispositivo/migracion/test_migrated_state.py` | verificaciones del estado migrado |
| `dispositivo/tutor/tutor_v0_33.py` | Tutor renderer conservador; dependencias incompletas |
| `dispositivo/generator/inputs/GenerationLicense_v0_33_c02_default_qui.jsonl` | licencias activas v0.33 |
| `dispositivo/generator/inputs/GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl` | átomos de evidencia de licencias v0.33 |
| `dispositivo/generator/inputs/AuthorizedSlotFillers_v0_33.jsonl` | fillers autorizados por slot |
| `dispositivo/generator/inputs/IntegrationBlockers_v0_1.jsonl` | bloqueadores C03–C06 |
| `dispositivo/generator/inputs/OrthographicResolutions_v0_9.jsonl` | resoluciones ortográficas exactas por celda |
| `dispositivo/generator/inputs/AdoptionRecords_v1.jsonl` | guardas/adopciones NC001 |
| `dispositivo/generator/inputs/ConceptMapping_v1.jsonl` | HABITUAL/COMPLETIVE, sin proyección automática a superficie |
| `dispositivo/generator/inputs/OrthographicProfile_v1_DRAFT.json` | vector ortográfico conservador, no norma global |
| `dispositivo/migracion/fuentes/generator_v0_initial/generator_v0.py` | primer scaffold Generator_v0; `ARCHIVE_ONLY / SUPERSEDED` |
| `dispositivo/migracion/fuentes/generator_v0_initial/GenerationLicense_v0.jsonl` | dos licencias `ZERO_NOVELTY_ATTESTED_ASSEMBLY`; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/generator_v0_initial/IntegrationBlockers_v0.jsonl` | blockers iniciales C03–C06; `ARCHIVE_ONLY` |
| `dispositivo/migracion/fuentes/generator_v0_initial/runtime_reuse_adapter_v0.py` | adapter hash-gated a `generator_view` v0.2.6; histórico |
| `dispositivo/migracion/fuentes/generator_v0_initial/mvp_review_candidate_adapter_v0.py` | ReviewCandidate histórico no licenciante |
| `dispositivo/migracion/fuentes/generator_v0_initial/test_generator_v0.py` | suite exacta del scaffold inicial |
| `dispositivo/migracion/fuentes/generator_v0_initial/test_runtime_reuse.py` | test exacto del reuse del runtime canónico |
| `dispositivo/migracion/fuentes/generator_v0_initial/INTEGRATION_REPORT_GENERATOR_v0.md` | reporte de integración inicial |
| `dispositivo/migracion/fuentes/generator_v0_initial/HASH_GATE_REPORT.md` | hashes canónicos runtime/SQLite y hashes observados MVP |
| `dispositivo/migracion/fuentes/generator_v0_initial/TEST_RESULTS.txt` | reporte histórico 11/11 PASS |

## 4. Runtime v0.2.15.3 — estado de recuperación

Fuente de release histórica:

```text
didxaza_v0_2_15_3_surface_semantics_resolution_integrity_CLOSED_PASS(1).zip
ZIP SHA256 = 6e5c3e8ee9bb5dbd04666537dc423724eb4bc402440e670e5be81cfa54b5d7e5
```

`RELEASE_FILE_MANIFEST_v0_2_15_3.json` enumera 75 payloads. En este checkpoint hay **37/75 payloads exactos recuperados** y 38 aún ausentes.

La SQLite v2.20 es byte por byte idéntica al release:

```text
BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite
SHA256 = 2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed
SQLITE_INTEGRITY_CHECK = ok
FOREIGN_KEY_VIOLATIONS = 0
canonical_state_v17 = 22 rows
verb_lexeme_class_v023 = present
person_possession_exact_v0214 = present
```

La copia exacta de `didxaza_runtime_v0_2_2_context_provenance.py` fue restaurada frente a una copia de migración con `TONE_PEDAGOGY` en lugar de `TONE_PEDAGOGICAL`:

```text
SHA256 = 57fcc152333c7817046cec6004bb77832a0c0f34bb4ddf75b4f4444ecfe9b347
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

`DB_INTEGRITY_v0_2_15_3.json` también fue restaurado a identidad exacta:

```text
SHA256 = fa2b88c95b8d567b4165b49636f67cdf8c00fa1a036cf8c162d03a6bceb193bb
```

### 4.1 Cierre de pruebas recuperado

La prueba exacta `test_surface_semantics_v0_2_15_3.py` pasa 10 casos y conserva:

```text
AUTO_CORRECT_ENABLED = false
ORTHOGRAPHIC_SUGGESTIONS_ENABLED = false
EDIT_EXECUTION_ENABLED = false
USER_VISIBLE_SUGGESTIONS_ENABLED = false
ANALYSIS_ONLY_SURFACE_PROMOTION = false
```

La cadena histórica recuperada ejecuta 38/38 pruebas:

```text
5  adversariales de integridad
12 sobre resultados de replay almacenados
11 sobre schema / SQLite v2.19
10 sobre semántica de superficie v0.2.15.3
```

Las 12 pruebas de replay leen artefactos almacenados; no regeneran COR001. Por tanto verifican consistencia del cierre histórico, no validez lingüística ni gold/regression authority.

### 4.2 Runner v0.2.15.3

Migrado sin modificación:

```text
run_cor001_replay_v0_2_15_3.py
SHA256 = 02a540651c7bb884638581f6be72e2133a3624df0cadd3eede95920b50178485
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

No se ha ejecutado todavía porque falta una dependencia directa: `PICKETT_LEXICON_BACKFILL_v0_1.csv`.

### 4.3 Documentary Alignment v0.2.10

Fuente completa recibida:

```text
didxaza_v0_2_10_documentary_alignment_CLOSED_PASS(1).zip
SHA256 = 1b767731e26c744c695c90d7e753509254140dae1cac04e508c83e850790dbdf
```

El módulo del ZIP coincide exactamente con la identidad esperada por el release v0.2.15.3 y quedó migrado:

```text
didxaza_runtime_v0_2_10_documentary_alignment.py
SHA256 = ef9ce3b38308312224dafd459f90c7407af0e4645c376911e3f97303a0f1bb18
GIT_BLOB = 0b45aaea93244ae895fe91a5eb63d3f2231638c9
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

El mismo paquete contiene:

```text
DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_10.csv
SIZE = 20746 bytes
DATA_ROWS = 147
SHA256 = a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf
```

Ese SHA-256 es **idéntico** al registrado en el release v0.2.15.3 para:

```text
SHA256 = a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf
```

Por tanto la evidencia disponible demuestra continuidad byte a byte del contenido del registry entre el nombre histórico v0.2.10 y el nombre de release v0.2.15.2. El archivo fue transferido al árbol sin normalización ni reconstrucción. Conserva BOM UTF-8 y terminadores CRLF. Verificación: `SHA256 = a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf`; `GIT_BLOB = 127c48ddfdac41f34359f3871f65e6aa4e759452`; `STATUS = EXACT_RELEASE_IDENTITY_VERIFIED`.

### 4.4 Pickett Lexical Backfill v0.2.11

Fuente completa localizada en este chat:

```text
didxaza_v0_2_11_pickett_backfill_CLOSED_PASS(1).zip
didxaza_v0_2_11_pickett_backfill_CLOSED_PASS(2).zip
SHA256 (ambos) = 8d7da40dc0c9559f922a0a9a523bc389547997571a7276a8f5230b978a322773
STATUS = IDENTICAL_DUPLICATE_UPLOADS / RECOVERABLE_SOURCE_LOCATED
```

El paquete contiene el módulo exacto v0.2.11 y `PICKETT_LEXICON_BACKFILL_v0_1.csv` con 2,534 registros (1,949 entradas principales + 585 subentradas). El módulo fue migrado y verificado contra el release. El CSV conserva SHA-256 `56e2372566cec9d7758b7e45b8de4e320a92eb2ee5c51b2a5e444e8165875723` y sigue `SOURCE_COMPLETE_READY_TO_MIGRATE / EXACT_BYTE_TRANSFER_PENDING`; no se reconstruye ni normaliza.

El mismo paquete contiene `COR001_REGRESSION_INPUT_v0_2_11.csv`, byte-idéntico al `COR001_REPLAY_INPUT_v0_2_15_2.csv` del release (SHA-256 `045b3abc83ec2035f6d20895d4584f5c028b7855f0cfb198b366b24d0ea5a8e9`); se migró bajo el nombre esperado por v0.2.15.3 exclusivamente para reproducibilidad técnica.

### 4.5 Pickett cross-source v0.2.12 y person/possession v0.2.14

Fuentes exactas disponibles en el release histórico de este chat y migradas sin modificación:

```text
didxaza_runtime_v0_2_12_pickett_cross_source.py
SHA256 = ac27a5b08f8fff78ef95db5c70e0ae4418c65f258f37c808e9d65344a552e16e
GIT_BLOB = 333e13a5ffb10c1cca53cdb78aa84d75fc0b0bc2
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED

didxaza_runtime_v0_2_14_person_possession.py
SHA256 = f86df6f055c83d6b74ae22647091c2b39df1b071e457170bded108cd61817ca9
GIT_BLOB = 762e66bd6b3233d02494e1be713401646e9551a6
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED

PERSON_POSSESSION_EXACT_REGISTRY_v0_2_15_2.csv
SHA256 = 3f1e955a285c2ce9c66d3953def6b41fd993d6b8dd81567c5f95a28281d20bdb
GIT_BLOB = 3ce56a39c33b6ebcd89018540fbe450872aceaf0
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

Estos tres artefactos cierran tres de las cuatro dependencias directas que todavía bloqueaban el replay histórico.

## 5. Inventario verbal, Dictionaria y Analyzer

`DIC_VERB_2385_v0_1.csv`:

```text
SHA256 = 2bdf4afd4b61234c54585cda17ad648bfb71194e9463d193eb04a5a06aa3183d
SIZE = 767310 bytes
DATA_ROWS = 2385
COLUMNS = 27
RAGGED_ROWS = 0
UNIQUE_ENTRY_IDS = 2385
```

Dictionaria exacta:

```text
DICTIONARIA_entries_v0_2_15_2.csv
SHA256 = a093b8eb5087affb7d7f364bb0a423921c20e959d61fe7efcd85de62b249d0
DATA_ROWS = 9012

DICTIONARIA_senses_v0_2_15_2.csv
SHA256 = 244769e4b3d724e5373feb3ccd26405c517340d05b70d962564ed4a4142d2afb
DATA_ROWS = 9046

DICTIONARIA_examples_v0_2_15_2.csv
SHA256 = 2a6e906e8cc8dc43d69306a0a69332f257ae470b5caeb47d3aef72d17ba9af8b
DATA_ROWS = 9686
```

Analyzer v0.35:

```text
STATUS = MIGRATED / REPRODUCIBLE_NON_LICENSING_PARTIAL_ANALYZER
```

Dependencias directas presentes:

```text
didxaza_runtime_v0_2_1_retrieval.py
didxaza_runtime_v0_2_3_morphology_i.py
didxaza_runtime_v0_2_4_bound.py
didxaza_runtime_v0_2_5_morphology_ii.py
DICTIONARIA_entries_v0_2_15_2.csv
DICTIONARIA_senses_v0_2_15_2.csv
DICTIONARIA_examples_v0_2_15_2.csv
DIC_VERB_2385_v0_1.csv
SQLite: verb_lexeme_class_v023
SQLite: person_possession_exact_v0214
```

`analyzer_v0_35_migrated_adapter.py` permite instanciar el Analyzer parcial. Smoke test histórico:

```text
"Quí rasé'" -> PARTIAL_ANALYSIS_NON_LICENSING
forma inexistente -> ABSTAIN_NO_COMPONENT_EVIDENCE
generation_license_assertion = false
correction_assertion = false
orthographic_authority_assertion = false
rule_discovery_assertion = false
```

## 6. Generator_v0 — genealogía y estado materializado

Genealogía localizada:

```text
generator_v0.py
-> generator_v0_1.py
-> generator_v0_2.py
-> generator_v0_3.py
-> generator_v0_4.py
-> generator_v0_5.py
```

`generator_v0_5.py` es la implementación más reciente localizada.

El scaffold inicial quedó archivado íntegramente bajo `dispositivo/migracion/fuentes/generator_v0_initial/`. Sus identidades principales:

```text
generator_v0.py SHA256 = 29631133f885409d16599a2d21e72d5c047f660aa6ce680563637c52a8cd8856
GenerationLicense_v0.jsonl SHA256 = ec153dad5a40e360ae0815a909eaa8e57cba02697e0c44f8b0e40c93b1cb9461
IntegrationBlockers_v0.jsonl SHA256 = 2481125d6ad1583c37169f862ae0c49aee872a0431ade77347d554b0ad9cfdbc
runtime_reuse_adapter_v0.py SHA256 = 2755d7cbffa54089c8bfaff05543b620239787e51e5c892670fcac630e54cc9b
mvp_review_candidate_adapter_v0.py SHA256 = 50283fd48216cbb56b6ab312635d2a80b526d47917930172ffb67970d499b5fc
test_generator_v0.py SHA256 = e5be3ce4e9dc593d4d097f43d0a61dfe3b9614f6f4a5ce1c4867f480a17a82be
test_runtime_reuse.py SHA256 = 64e488b95cfc91c3e17ebb333f081c51dae3892544b94b1d3bf1fc8e6d8e8b36
```

El scaffold inicial sólo licencia C01/C02 como:

```text
ZERO_NOVELTY_ATTESTED_ASSEMBLY
may_license_new_combinations = false
```

y bloquea históricamente:

```text
C03 = MISSING_QUESTION_PATTERN
C04 = INTERROGATIVE_DOMAIN_SCOPE_MISMATCH
C05 = MISSING_NOUN_POSSESSION_LICENSE_SET
C06 = DEPENDENT_POTENTIAL_OUT_OF_SCOPE
```

El paquete binario histórico del scaffold sigue fuera del repo:

```text
PAQUETE_MIGRACION_DIDXAZA_GENERATOR_V0_INTEGRATED_v1(1).zip
SHA256 = 270dff08371f6b35bbb817d5440db85811ab87f11b2c7a96a9cf8f485ed76b9a
STATUS = BINARY_TRANSFER_PENDING / ARCHIVE_ONLY
```

### 6.1 Generator_v0.5 materializado

Inputs activos localizados y migrados:

```text
GenerationLicense_v0_33_c02_default_qui.jsonl
GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl
AuthorizedSlotFillers_v0_33.jsonl
IntegrationBlockers_v0_1.jsonl
OrthographicResolutions_v0_9.jsonl
AdoptionRecords_v1.jsonl
ConceptMapping_v1.jsonl
OrthographicProfile_v1_DRAFT.json
ParadigmTable_v1.csv
ConstructionInventory_v1.jsonl
```

`generator_v0_5.py` acepta un `canonical_analyzer` para round-trip de recombinaciones novedosas. El archivo histórico mezcla dos layouts y espera `NovelRecombinationAttempt_v0_1.json`, ausente; no se modificó. `generator_v0_5_migrated_adapter.py` fija `generator/inputs/` y permite instanciar el subconjunto presente:

```text
PARADIGM_CELLS = 72
CONSTRUCTIONS = 6
GENERATION_LICENSES = 6
ACTIVE_LICENSE_CONSTRUCTIONS = C01, C02
BLOCKED_BY_MIGRATED_INPUTS = C03, C04, C05, C06
```

`GENERATION_READINESS_MATRIX_v14.csv` se conserva como `MIGRATED_SNAPSHOT_NOT_REPRODUCIBLE_WITH_CURRENT_FILES` para capacidades históricas C03/C05 cuyas dependencias exactas aún faltan.

## 7. Tutor_v0.33 — pendiente P0

`tutor_v0_33.py` está migrado pero todavía no es instanciable.

Dependencias exactas ausentes:

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

El contrato histórico permanece:

```text
ANALYZED != GENERATION_LICENSED
```

## 8. Genealogías recuperadas

### JUCHITAN_LINGUISTIC_CORE

```text
v0.1 -> ... -> v0.23 -> ... -> v0.27
```

`v0.27` es la versión de referencia más reciente verificable y está migrada íntegramente. La presencia de formulaciones históricas sobre COR001 no altera la política posterior `ANALYSIS_TARGET_ONLY`.

### NC001 state

```text
v1 -> v2 -> v3 -> v4 -> ... -> v34 -> v35 -> v36 -> v37.1
```

- v1: foundations materialized, antes de montar runtime/Generator.
- v2: Generator_v0 inicial.
- v3: primer bridge round-trip y primera recombinación novedosa licenciada `Ma' beedabe`.
- v4: contrato round-trip v0.2 estabilizado; `ANALYZED != GENERATION_LICENSED`.
- v34: C02 adopta `quí` default Juchitán sin borrar `qué`.
- v35: priorizador de huecos; COR001 sólo objeto de análisis.
- v36: guardrails y giro a literatura + audio independiente.
- v37.1: cierre de BIB065 y preservación del Analyzer de frase aislada.

### Analyzer

```text
v0_25 -> v0_26 -> v0_35
```

v0.35 añade `context_segments` opcional sin hacer obligatorio el contexto para análisis local.

### Runtime lingüístico

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

La presencia de un módulo histórico no implica que toda su semántica permanezca activa en etapas posteriores; se preserva genealogía archivo por archivo.

### DocumentaryAlignment registry

La fuente recuperada demuestra:

```text
DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_10.csv
SHA256 a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf
=
SHA256 a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf
```

Es identidad de bytes demostrada, no inferencia de contenido.

### Readiness

Se localizaron matrices sucesivas hasta `GENERATION_READINESS_MATRIX_v14.csv`, la más reciente localizada.

### MVP_LINGUISTICO_001

Hashes históricos observados, no retroactivamente canónicos:

```text
MVP v0.1 ZIP = f4819f1525036742e6915a2a9cbaf6cd7417d8ea4bdb7914fafdff93f960c948
MVP v0.2 ZIP = e6524d5d89ed42ff233f6216d29553de644de86e601af21e658627605a6185e2
```

`mvp_review_candidate_adapter_v0.py` ya fue recuperado. `didxaza_vertical_slice_v0_1.py` y ambos ZIP MVP siguen sólo referenciados/localizados históricamente; no se reconstruyen.

## 9. Otros artefactos localizados y pendientes

| Artefacto | Estado actual | SHA-256 si aplica |
|---|---|---|
| `didxaza_v0_2_10_documentary_alignment_CLOSED_PASS(1).zip` | `RECOVERABLE_SOURCE_LOCATED / ARCHIVE_ONLY` | `1b767731e26c744c695c90d7e753509254140dae1cac04e508c83e850790dbdf` |
| `DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_10.csv` → release name `DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_15_2.csv` | `MIGRATED / EXACT_RELEASE_IDENTITY_VERIFIED` | `a4103fa943d6a5770d441c8b6db82b79fd98020de4d185d0cc8b725cf58d92cf` |
| `PAQUETE_MIGRACION_DIDXAZA_GENERATOR_V0_INTEGRATED_v1(1).zip` | `BINARY_TRANSFER_PENDING / ARCHIVE_ONLY` | `270dff08371f6b35bbb817d5440db85811ab87f11b2c7a96a9cf8f485ed76b9a` |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | observed `f4819f...60c948` |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | observed `e6524d...6185e2` |
| `didxaza_vertical_slice_v0_1.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | — |
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `61fd21298c1260924fdc95b7e201b8d601dc83820f3d4f3686f508a74ae57c6a` |
| `DevelopmentCorpusProtocol_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `563dc30977a1f6175e823c60a8f79f8c78f1ec81ff09b27ad0943ceaff5fd8ad` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `3ea1d5b4598067f3fe51a03c6e3afa65131c5a543b16f8843b6f1727be094de7` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `acffea79fe7d228a0b28f740094e5a15fd4ec0ba6d36b257cc3aaef918a83c54` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE / historical provisional` | `f3308483c3135e43d49f2641f518aecd0dbf3c1fcbdc98f349511751ce86b295` |
| `COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `b369215edec07a98b59b6ee22a87995b20614d7a45dd16541f0deb71b93fd0d3` |
| `generator_v0_2.py` | `SOURCE_COMPLETE_READY_TO_MIGRATE / SUPERSEDED / ARCHIVE_ONLY` | `54257f9a6dae12aba003e50e81b14bc25fba1d3e54e2eeecce009130c01fbacc` |
| `canonical_analyzer_roundtrip_bridge_v0_2.py` | `SOURCE_COMPLETE_READY_TO_MIGRATE / SUPERSEDED / ARCHIVE_ONLY` | `bf1c3604f59aa559f8c1e5a6e7cfd1c78b16315f0dbbd1c1218f4e0a09cd0436` |
| `GenerationLicense_v0_2_roundtrip.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE / SUPERSEDED / ARCHIVE_ONLY` | `0afb4d10fb96d8d0f264ad4ace18b2174b101aa86a593835b7530dfc57746861` |
| `GenerationEvidenceAtoms_v0_2_roundtrip.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE / SUPERSEDED / ARCHIVE_ONLY` | `eb12fd80cae634c3f66ba4003b6804bfd65a06f35d96726eef18d6d38635c191` |
| `STABILIZATION_REPORT_v0_2.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE / ARCHIVE_ONLY` | `76d2655f9cd95eec69c0d143a264a49aa51b67cf55e609fc882c9dffdd530447` |

## 10. P0 localizado pero aún incompleto

### Runtime v0.2.15.3 — 38/75 payloads aún ausentes

Para regenerar técnicamente el replay histórico queda una sola dependencia directa sin migrar:

```text
PICKETT_LEXICON_BACKFILL_v0_1.csv
```

La fuente exacta está localizada en este chat y en el release histórico; conserva:

```text
SHA256 = 56e2372566cec9d7758b7e45b8de4e320a92eb2ee5c51b2a5e444e8165875723
SIZE = 940709 bytes
STATUS = SOURCE_COMPLETE_READY_TO_MIGRATE / EXACT_BYTE_TRANSFER_PENDING
```

La herramienta GitHub disponible en esta pasada no ofrece transferencia directa de archivo local y el payload textual excede una transferencia razonable por el wrapper de contenido. No se reconstruye, fragmenta ni normaliza.

La regeneración del replay sólo verificaría reproducibilidad técnica; **COR001 no se convierte en benchmark, gold, regression authority ni fuente de reglas**.

### Tutor_v0.33

Faltan las nueve dependencias listadas en §7 para hacer instanciable el renderer histórico.

## 11. Reuse map / cuarentenas

El reuse map mantiene fuera de licencias de generación:

```text
SequenceMatcher / near-match
normalización destructiva de diacríticos
clean_paradigm_surface() -> surface
COR001 como licencia
confidence legado
handlers particulares COR001
owner review / PROBABLE_TRANSCRIPTION_CORRECTION como licencia
```

El checkpoint inicial Generator confirma esa cuarentena mediante fuente, adapter y tests exactos.

## 12. Commits históricos de migración registrados

```text
e921229d1ad7591fc73ea8cea3f3ecdbd3cc0e83  migrate NC001 post-roundtrip bridge state v3
45dc013cc6558bbc3ba9d5d2a83466e97226660d  migrate NC001 roundtrip stabilization state v4
8dcadfb4d5c37d6fa5a4ac31c84a14d1a7f0d867  migrate stabilized NC001 roundtrip contract v0.2
f4f052dabb1eb94f6a6eda23cc33ed26c0b17e0c  migrate Tutor_v0.33 implementation
399885d7b10d21fb0b858e2188245dfa193107b2  migrate Generator authorized slot fillers v0.33
9d4325270f64dc213ca3f101796fc728e577cf30  migrate Generator integration blockers v0.1
65974208b0a288ebcee35af7326e4722c6f14550  migrate orthographic resolutions v0.9
2dc6bdcad0154c122dc1c33afbc3a4da7541d1f4  migrate NC001 adoption records v1
dc8ce13ad56b848d1b329ec2e2cb2a75fb395459  migrate NC001 concept mapping v1
94d281f825755e0dd6168426140d4317cbc3b216  migrate NC001 orthographic profile draft
05e996c2ce765aa98649978703032a443578a6e6  migrate Generator generation license v0.33
96135569ccb08f0dcc2738bee8bdd2a23cd6b977  migrate Generator evidence atoms v0.33
554ce87239d9aa7b4a7f04be1f9378ece7afde47  migrate Juchitán linguistic core v0.27
294c1a17d15767e9d641dc882a048611fadfa482  retire failed DIC_VERB transport attempt
7ab707cf33461438e832454685cbd5355f75b586  migrate exact DIC_VERB inventory
6f92804d869fc8766f5b7e4bc782af813d5c4bb4  restore exact runtime v0.2.2 identity
505f7125321c75238e90135e91667ae5544fa870  migrate exact SQLite v2.20
64a98385c92c4ab1d31e13c5f9e44c108366fd01  reconcile migrated executable state
f533bf667b0a7aca94426fb24016000761502e10  migrate exact Dictionaria analyzer inputs
6d4de82f9d0062b8adce3efcf1a3e54a40c8dab7  restore exact DB integrity release identity
9d631d3db742afc6affbd1fb14179eb174c578da  make migrated Analyzer v0.35 reproducible
1349a0be610d4020a698795925a8a70702a22f2d  migrate exact runtime surface semantics slice
bf88660d93b043a5894cf283913c1a09436c9b85  verify migrated runtime surface semantics slice
5c1e7a8c1be8492ecb04ca35fff1fc21a58e887d  migrate exact runtime closure test artifacts
c9506439546f55fa4c6ca2417bb1693931a4d29e  verify historical runtime test closure
4a940717302ebb92a5306a29354c88f393e93c76  migrate NC001 pre-Generator state v1
630010a3f8b1341382b973a4f360b26df47ace4e  migrate initial Generator_v0 source checkpoint
f3bac5fb21c100619be2aee27e6fd35894659948  migrate initial Generator_v0 zero-novelty licenses
55a5596fa0005de085c413845fc8675a99d4001b  migrate initial Generator_v0 blockers
4580df35a00d8f21dc2436918f8c4740554f3544  migrate initial Generator_v0 runtime reuse adapter
4c7b28902c43a378d65d1e57d1d147a2729ca042  migrate MVP review-candidate non-licensing adapter
b38480a7ed0c59518cf54d56bf27f5e914b7ff8a  migrate initial Generator_v0 integration report
e3f5736442c2f889d85b2300ee5f3a6d57dca2db  migrate Generator_v0 hash gate report
edf2de5e5e7c802985da530b096c1ef078b3d03e  migrate initial Generator_v0 test results
f92fe107b6d68aa11fa22dd5c7308c135d684e5e  migrate NC001 architecture freeze v1.1
f3edabe3463ccf9c2b267c9f198724f5ae0c3bf8  migrate NC001 adversarial architecture synthesis v1.1
48ed349d8150a7caa8c7c6d9d61246f22bbbfd63  migrate initial Generator_v0 unit tests
7fd7915cd7b0ef655239371d2b8d73692354625f  migrate initial Generator_v0 runtime reuse test
bdd2d9857bbaa647f239748aff3cf2af1e5bc567  migrate exact runtime v0.2.15.3 replay runner
9b33c78673b5de5bcb56c351e612c6cc4a09ef39  migrate exact runtime v0.2.10 documentary alignment
1e0a31eb1f583abad07beda41c3e8fbb41a537a1  migrate exact documentary alignment registry v0.2.15.2
821e9bd6cb6dc38bcbeb378c5c8b66f4f5429902  remove temporary exact registry migration helper
b3300bb1c77c02c18b686616aad6478a079b2ad1  migrate exact v0.2.12 Pickett cross-source runtime
5d05b77327b35c3964f63f258cbe06e19ec6d003  migrate exact v0.2.14 person-possession runtime
3f9b0fab8a13cb66c20e89a76799f97d1537aa65  migrate exact person-possession registry v0.2.15.2
20cffa99d41e271c662cbbb603989822e951352b  update executable state after restoring v0.2.12 and v0.2.14 deps
```

## 13. Criterio de migración

Antes de incorporar una pieza:

1. identificar versión;
2. identificar función original;
3. separar vigente / provisional / superseded / cuarentena;
4. conservar procedencia y dependencias;
5. determinar si es estado, ejecutable o historia;
6. impedir que su copia sea interpretada como nueva regla lingüística o pedagógica.

## 14. Orden de recuperación restante

### P0 — conservar estado reproducible

1. transferir byte-exacto `PICKETT_LEXICON_BACKFILL_v0_1.csv`;
2. regenerar el replay en directorio aislado para verificar reproducibilidad técnica;
3. recuperar en paralelo `TutorCaseLicenseBindings_v0_33.jsonl` y las licencias C03/C05 exactas del Tutor si aparecen como fuentes completas.

### P1 — reproducibilidad y límites

- `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md`;
- `DevelopmentCorpusProtocol_v0_35.md`;
- matrices/reportes BIB065;
- pruebas/adapters adicionales completos y versionados.

### P2 — ejecutables útiles

Sólo después de identificar versión, dependencias y vigencia.

### P3 — historia

Auditorías y versiones intermedias como `ARCHIVE_ONLY` cuando expliquen genealogía. No reconstruir todo el historial.

## 15. Próxima acción

**Siguiente P0 imprescindible:** `PICKETT_LEXICON_BACKFILL_v0_1.csv` (fuente exacta localizada, transferencia byte-exacta aún pendiente).

Ejecutar cualquier replay sólo en un directorio aislado y comparar reproducibilidad técnica. COR001 permanece `ANALYSIS_TARGET_ONLY` y no puede licenciar reglas, correcciones ni generación.

La reconciliación técnica no cambia reglas lingüísticas, no convierte readiness histórica en política actual y no bloquea COR002, corpus oral ni trabajo con hablantes.