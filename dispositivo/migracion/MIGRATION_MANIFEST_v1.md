# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Última actualización:** 2026-09-02 — slice unitario de semántica de superficie v0.2.15.3 reproducible

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
| `dispositivo/ESTADO_ACTUAL_2026-08-31.md` | snapshot técnico previo a esta pasada |
| `dispositivo/ANALYZER_SCOPE_MULTIESCALA_2026-08-31.md` | alcance palabra → discurso |
| `dispositivo/PROVENANCE_LABEL_CROSSWALK_v0_1.md` | equivalencias de procedencia |
| `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` | discusión pedagógica no normativa |
| `dispositivo/migracion/fuentes/MVP_REUSE_MAP_v1.md` | mapa de reutilización/cuarentena del vertical slice |
| `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md` | protocolo de migración directa |
| `dispositivo/core/NUCLEO_CONVERSACIONAL_001_SCOPE_v1.md` | scope exacto del vertical slice NC001 |
| `dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md` | fuente completa migrada desde el archivo adjunto del chat; `EXPERIMENTAL_CORE`, no autoridad lingüística definitiva |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` | estado post Generator_v0; hashes runtime/SQLite y ausencia del orquestador canónico en ese hito |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v3_POST_ROUNDTRIP_BRIDGE.md` | checkpoint histórico del primer bridge round-trip y primera recombinación novedosa licenciada; `ARCHIVE_ONLY` frente a estados posteriores |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v4_POST_ROUNDTRIP_STABILIZATION.md` | checkpoint histórico de estabilización del contrato round-trip v0.2 y gate de valencia; `ARCHIVE_ONLY` frente a estados posteriores |
| `dispositivo/migracion/fuentes/ROUNDTRIP_CONTRACT_v0_2.md` | contrato estrecho estabilizado `STRUCTURAL_COMPATIBILITY_ONLY_NON_LICENSING`; histórico, no política actual |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v34_POST_C02_DEFAULT_QUI_MIGRATION.md` | transición C02 al default juchiteco `quí`; `qué` preservado como variante secundaria |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v35_POST_EVIDENCE_GAP_PRIORITIZER.md` | estado del grafo/priorizador v0.34; COR001 continúa `ANALYSIS_TARGET_ONLY` |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v36_POST_KNOWLEDGE_INGESTION_GUARDRAILS.md` | guardrails de degradación elegante y ruta literatura+audio |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md` | estado posterior al cierre BIB065; ruta activa más reciente localizada |
| `dispositivo/generator/inputs/ConstructionInventory_v1.jsonl` | seis construcciones NC001 con alcance y abstenciones |
| `dispositivo/generator/inputs/ParadigmTable_v1.csv` | tabla de celdas TAM/persona y procedencia del slice |
| `dispositivo/validation/ValidationQueue_v0.jsonl` | cola de validación/desarrollo audio-first |
| `dispositivo/analyzer/non_licensing_analyzer_orchestrator_v0_35.py` | Analyzer parcial no licenciante con contexto opcional |
| `dispositivo/analyzer/analyzer_v0_35_migrated_adapter.py` | adaptador no normativo que fija las rutas de las dependencias exactas migradas del Analyzer v0.35 |
| `dispositivo/analyzer/DIC_VERB_2385_v0_1.csv` | inventario operacional exacto de 2,385 verbos; SHA-256 verificado; ruta por defecto del Analyzer v0.35 |
| `dispositivo/runtime/v0_2_15_3/BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite` | SQLite v2.20 transferida byte por byte; hash, integridad, claves foráneas y tablas críticas verificados |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_entries_v0_2_15_2.csv` | inventario exacto de 9,012 entradas consumido por Analyzer v0.35 |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_senses_v0_2_15_2.csv` | inventario exacto de 9,046 sentidos consumido por Analyzer v0.35 |
| `dispositivo/runtime/v0_2_15_3/DICTIONARIA_examples_v0_2_15_2.csv` | inventario exacto de 9,686 ejemplos consumido por Analyzer v0.35 |
| `dispositivo/generator/generator_v0_5.py` | implementación más reciente del Generator_v0 localizada en paquete v0.36.2 |
| `dispositivo/generator/generator_v0_5_migrated_adapter.py` | adaptador no normativo que instancia el subconjunto migrado desde una única ruta de inputs sin alterar la implementación histórica |
| `dispositivo/generator/GENERATION_READINESS_MATRIX_v14.csv` | snapshot de readiness más reciente localizado en paquete v0.36.2 |
| `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md` | checkpoint que separa presencia, ejecutabilidad, snapshots no reproducibles y preguntas abiertas |
| `dispositivo/migracion/test_migrated_state.py` | verificaciones de SQLite, DIC_VERB, Dictionaria, Analyzer, Generator, slice unitario de semántica de superficie y hashes presentes del release |
| `dispositivo/tutor/tutor_v0_33.py` | Tutor renderer conservador: sólo explica análisis con binding exacto y licencia activa; no analiza/corrige/genera |
| `dispositivo/generator/inputs/GenerationLicense_v0_33_c02_default_qui.jsonl` | licencias activas localizadas, incluida migración C02 a `quí` |
| `dispositivo/generator/inputs/GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl` | átomos documentales/campo vinculados a las licencias v0.33 |
| `dispositivo/generator/inputs/AuthorizedSlotFillers_v0_33.jsonl` | fillers autorizados por slot, con `quí` default Juchitán y `qué` variante secundaria |
| `dispositivo/generator/inputs/IntegrationBlockers_v0_1.jsonl` | bloqueadores explícitos C03–C06 del slice histórico |
| `dispositivo/generator/inputs/OrthographicResolutions_v0_9.jsonl` | resoluciones ortográficas exactas por celda; no reglas globales |
| `dispositivo/generator/inputs/AdoptionRecords_v1.jsonl` | guardas/adopciones ortográficas NC001 |
| `dispositivo/generator/inputs/ConceptMapping_v1.jsonl` | mapping conceptual HABITUAL/COMPLETIVE sin proyección automática a superficie |
| `dispositivo/generator/inputs/OrthographicProfile_v1_DRAFT.json` | vector ortográfico conservador, explícitamente no norma global |

### 3.1 Runtime v0.2.15.3 localizado y presencia textual verificada

Fuente exacta localizada en este chat:

`didxaza_v0_2_15_3_surface_semantics_resolution_integrity_CLOSED_PASS(1).zip`

SHA-256 del ZIP:

```text
6e5c3e8ee9bb5dbd04666537dc423724eb4bc402440e670e5be81cfa54b5d7e5
```

Coincide con la identidad histórica ya registrada para el runtime v0.2.15.3.

En el repositorio ya se localizaron bajo `dispositivo/runtime/v0_2_15_3/` el README del checkpoint, estado maestro del Corrector, manifiesto de release, DB integrity y módulos de runtime. Para varios módulos críticos se verificó identidad exacta por Git blob frente al archivo contenido en el ZIP:

```text
didxaza_runtime_v0_2_0_foundation.py      Git blob 734c3670f1a9edfbb3a6dddc270ab9e5b6df1901
didxaza_runtime_v0_2_1_retrieval.py       Git blob 057c37460dcea9ddf383dbf69d63f85caf6bf7ce
didxaza_runtime_v0_2_2_context_provenance.py Git blob 14f7786c2f6fd5d79844750768878c7a75889f2c
didxaza_runtime_v0_2_3_morphology_i.py    Git blob 00077c987fab1c49144c0f853e23226c82fac9e9
didxaza_runtime_v0_2_4_bound.py           Git blob 183e02d73e83a34e3675548ccf8fbb51763f3390
didxaza_runtime_v0_2_5_morphology_ii.py   Git blob 50e3a121d20d65b4f94b300fa34e2b80980b5c66
README_v0_2_15_3.md                       Git blob 0dddbbf8ca1d0282b840e2c76e5aeb150db09575
ESTADO_MAESTRO_CORRECTOR_DIDXAZA_v2_21.md Git blob 4707a4a8371eb072451f46d5cb6c2b2e98286353
```

`didxaza_runtime_v0_2_2_context_provenance.py` fue comparado con la fuente raw exacta del release. La copia inicialmente migrada tenía SHA-256 `8ce24975ad88bbbe352afcec6cd438d785fbe335bed12bd14c51a7551a5e8744` y difería en un único valor de `evidence_roles`: `TONE_PEDAGOGY` en vez de `TONE_PEDAGOGICAL`. El historial no registra esa variante como revisión posterior; entró con el commit inicial de migración.

La fuente exacta compila, no tiene consumidores que dependan del valor discrepante y coincide con el manifiesto del release:

```text
SHA256 = 57fcc152333c7817046cec6004bb77832a0c0f34bb4ddf75b4f4444ecfe9b347
GIT_BLOB = 14f7786c2f6fd5d79844750768878c7a75889f2c
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

La copia discrepante permanece recuperable en el historial Git; no se conserva como variante activa.

La presencia de fuentes textuales del runtime no sustituye los binarios/datasets referenciados por el release.

Después de transferir el slice unitario de semántica de superficie, el árbol contiene 21 de los 75 payloads enumerados por el manifiesto original y los 21 coinciden exactamente. La fuente raw de `DB_INTEGRITY_v0_2_15_3.json` confirmó que la copia previa difería sólo por un salto de línea final; la identidad exacta fue restaurada:

```text
SHA256 = fa2b88c95b8d567b4165b49636f67cdf8c00fa1a036cf8c162d03a6bceb193bb
STATUS = EXACT_RELEASE_IDENTITY_VERIFIED
```

La copia discrepante permanece recuperable en la genealogía Git.

### 3.2 `DIC_VERB_2385_v0_1.csv` transferido y verificado

**Estado:** `MIGRATED`

El archivo raw completo quedó disponible el 2026-09-01 y fue transferido sin transformación a:

`dispositivo/analyzer/DIC_VERB_2385_v0_1.csv`

Verificación:

```text
SHA256 = 2bdf4afd4b61234c54585cda17ad648bfb71194e9463d193eb04a5a06aa3183d
SIZE = 767310 bytes
DATA_ROWS = 2385
COLUMNS = 27
RAGGED_ROWS = 0
UNIQUE_ENTRY_IDS = 2385
```

La identidad coincide exactamente con el hash registrado antes de la transferencia. La ubicación coincide además con la resolución por defecto de `non_licensing_analyzer_orchestrator_v0_35.py`; no requiere pasar `--verb-inventory` para localizar este inventario. El intento provisional anterior mediante fragmentos base64 permanece documentado como `FAILED_INCOMPLETE_TRANSFER`: no produjo este archivo, no es su fuente y sus residuos fueron retirados del árbol activo.

### 3.3 Dictionaria transferida y Analyzer v0.35 reproducible

**Estado:** `MIGRATED / REPRODUCIBLE_NON_LICENSING_PARTIAL_ANALYZER`

Los tres CSV fueron extraídos sin transformación del ZIP canónico y verificados contra `RELEASE_FILE_MANIFEST_v0_2_15_3.json`:

```text
DICTIONARIA_entries_v0_2_15_2.csv
SHA256 = a093b8eb5087affb7d7d7f364bb0a423921c20e959d61fe7efcd85de62b249d0
DATA_ROWS = 9012

DICTIONARIA_senses_v0_2_15_2.csv
SHA256 = 244769e4b3d724e5373feb3ccd26405c517340d05b70d962564ed4a4142d2afb
DATA_ROWS = 9046

DICTIONARIA_examples_v0_2_15_2.csv
SHA256 = 2a6e906e8cc8dc43d69306a0a69332f257ae470b5caeb47d3aef72d17ba9af8b
DATA_ROWS = 9686
```

`analyzer_v0_35_migrated_adapter.py` fija explícitamente las rutas a runtime, SQLite y `DIC_VERB` sin modificar el orquestador histórico. Las pruebas verifican carga completa, análisis parcial de una forma documentada y abstención ante una forma deliberadamente inexistente. En ambos casos permanecen en `false` las aserciones de licencia de generación, corrección, autoridad ortográfica y descubrimiento de reglas.

La reproducibilidad declarada corresponde al Analyzer parcial no licenciante v0.35; no implica cobertura total, validación lingüística de sus salidas ni autoridad sobre COR001 o COR002.

## 4. P0 localizado y transferencia binaria

### runtime lingüístico v0.2.15.3 — transferencia selectiva

**Estado:** `RECOVERABLE_SOURCE_LOCATED` / `REPRODUCIBLE_SURFACE_SEMANTICS_UNIT_SLICE` / transferencia todavía incompleta para componentes no presentes.

El ZIP exacto está disponible y su hash coincide. La raíz contiene la genealogía del runtime y, además, bases SQLite y datasets. Se migraron sin transformación los siete módulos que forman el cierre importable de la prueba unitaria final, más la prueba exacta:

```text
didxaza_runtime_v0_2_6_evidence_adjudication.py
didxaza_runtime_v0_2_7_decision_simulation.py
didxaza_runtime_v0_2_7_1_integration_fixes.py
didxaza_runtime_v0_2_9_surface_evidence_coverage.py
didxaza_runtime_v0_2_13_resolution_vectors.py
didxaza_runtime_v0_2_15_2_evidence_integrity.py
didxaza_runtime_v0_2_15_3_surface_semantics_resolution_integrity.py
test_surface_semantics_v0_2_15_3.py
```

Sus SHA-256 coinciden con `RELEASE_FILE_MANIFEST_v0_2_15_3.json`. La prueba exacta ejecuta 10 casos y pasa desde el árbol migrado. El wrapper conserva desactivados autocorrección, sugerencias ortográficas, ejecución de ediciones y sugerencias visibles.

Este resultado no reproduce todavía la clausura histórica de 38 pruebas, el replay de COR001 ni los 26 criterios del reporte `SURFACE_SEMANTICS_PASS_FAIL_v0_2_15_3.csv`. El nombre `CLOSED_PASS` describe el paquete histórico; no convierte el subconjunto actual en runtime completo ni concede autoridad lingüística. Los módulos v0.2.10, v0.2.11, v0.2.12, v0.2.14 y v0.2.15 tampoco son importados por esta prueba final, por lo que su ausencia no impide los 10 casos pero sí deja incompleta la genealogía funcional.

La transferencia puede continuar archivo por archivo, pero la presencia de una fuente o reporte histórico no debe usarse para atribuir una capacidad que aún no se reprodujo.

### SQLite v2.20

**Estado:** `MIGRATED`

Los bytes completos quedaron disponibles y se transfirieron sin transformación a:

`dispositivo/runtime/v0_2_15_3/BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite`

La identidad coincide con el release:

`BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite`

Identidad verificada:

```text
SHA256 = 2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed
SQLITE_INTEGRITY_CHECK = ok
FOREIGN_KEY_VIOLATIONS = 0
canonical_state_v17 = 22 rows
verb_lexeme_class_v023 = present
person_possession_exact_v0214 = present
```

No se creó un sustituto textual ni una base reconstruida. La copia del repositorio es byte por byte idéntica a la fuente raw recibida y a la identidad registrada por el release.

## 5. Generator_v0 — estado de reproducibilidad recuperado

Los inputs que el manifiesto anterior marcaba como pendientes fueron recuperados y migrados en esta pasada:

```text
GenerationLicense_v0_33_c02_default_qui.jsonl
GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl
AuthorizedSlotFillers_v0_33.jsonl
IntegrationBlockers_v0_1.jsonl
OrthographicResolutions_v0_9.jsonl
AdoptionRecords_v1.jsonl
ConceptMapping_v1.jsonl
OrthographicProfile_v1_DRAFT.json
```

Junto con `ParadigmTable_v1.csv`, `ConstructionInventory_v1.jsonl` y `generator_v0_5.py` ya migrados, esto recupera el núcleo documental de la implementación Generator_v0 localizada.

No se declara autonomía completa: `generator_v0_5.py` acepta un `canonical_analyzer` para el round-trip de recombinaciones novedosas y ese contrato debe seguir verificándose de forma explícita.

La auditoría de ejecución encontró que la entrada por defecto de `generator_v0_5.py` mezcla el layout histórico `inputs_nc001/` con archivos ubicados junto al script y además espera `NovelRecombinationAttempt_v0_1.json`, ausente. El archivo histórico no se modificó. `generator_v0_5_migrated_adapter.py` fija explícitamente una sola ruta, `generator/inputs/`, y permite instanciar el subconjunto realmente presente.

Ese subconjunto contiene seis licencias activas sólo para C01/C02 y bloqueadores explícitos para C03–C06. Por ello, `GENERATION_READINESS_MATRIX_v14.csv` se conserva como `MIGRATED_SNAPSHOT_NOT_REPRODUCIBLE_WITH_CURRENT_FILES`: sus capacidades C03/C05 no se degradaron retrospectivamente ni se atribuyen al ejecutable actual hasta recuperar sus dependencias exactas.

`JUCHITAN_LINGUISTIC_CORE_v0_27.md` conserva además la frase histórica “benchmarks COR001”. No se modificó el core migrado, pero esa frase queda explícitamente subordinada a la política vigente `COR001 = ANALYSIS_TARGET_ONLY`; no autoriza gold, benchmark, regression ni descubrimiento de reglas.

## 6. Tutor_v0 — implementación y dependencias nuevas

`tutor_v0_33.py` fue recuperado directamente desde el paquete v0.34 y migrado sin reinterpretar su función.

Dependencias exactas nuevas que expone y que todavía deben recuperarse/migrarse:

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

**Estado:** `SOURCE_COMPLETE_READY_TO_MIGRATE` cuando la fuente completa del paquete v0.34 esté disponible para la siguiente pasada.

El Tutor preserva el contrato histórico:

```text
ANALYZED != GENERATION_LICENSED
```

y se abstiene si no existe binding exacto/licencia activa.

## 7. Genealogías recuperadas

### JUCHITAN_LINGUISTIC_CORE

Se localizaron al menos:

```text
v0.1 -> ... -> v0.23 -> ... -> v0.27
```

`v0.27` es la versión de referencia más reciente verificable en este entorno y quedó migrada íntegramente desde la fuente completa adjunta en este chat. Los `BLIND_STRICT_FIXTURE` de v0.27 son derivados de evaluación y no una nueva baseline lingüística.

### Generator_v0

```text
generator_v0.py
-> generator_v0_1.py
-> generator_v0_2.py
-> generator_v0_3.py
-> generator_v0_4.py
-> generator_v0_5.py
```

`generator_v0_5.py` es la implementación más reciente localizada. Sus bindings activos de C02 usan:

```text
GenerationLicense_v0_33_c02_default_qui.jsonl
GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl
AuthorizedSlotFillers_v0_33.jsonl
```

La fuente histórica exacta del checkpoint `generator_v0_2.py` está contenida en:

```text
PAQUETE_MIGRACION_DIDXAZA_ROUNDTRIP_CONTRACT_STABILIZED_v0_2.zip
SHA256 = e5410545a103951fc035429e8de9834bc178bde249c0fbd5b8a0e751cd14947d
```

Ese paquete también contiene el bridge canónico v0.2, licencias/evidence atoms v0.2 y los estados NC001 v3/v4. Se preserva como genealogía histórica y no sustituye a `generator_v0_5.py`.

### Analyzer no licenciante

```text
v0_25 -> v0_26 -> v0_35
```

v0.35 añade canal opcional `context_segments` sin convertir el contexto en requisito universal de análisis local.

### Runtime lingüístico

El ZIP v0.2.15.3 contiene módulos desde la foundation v0.2.0 y etapas sucesivas de retrieval, context/provenance, morphology I, BOUND, morphology II, evidence adjudication, decision simulation, surface evidence, documentary alignment, Pickett backfill/cross-source, resolution vectors, person/possession, evidence qualification/integrity y el cierre `v0.2.15.3_surface_semantics_resolution_integrity`.

La genealogía exacta debe preservarse archivo por archivo; no se debe inferir que cada módulo anterior permaneció semánticamente idéntico en el wrapper final.

### NC001 state

Secuencia de estados localizada desde `CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` hasta `CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md`.

Checkpoints de alto valor ya preservados:

```text
v2 -> v3 -> v4 -> v34 -> v35 -> v36 -> v37.1
```

- v3: primer bridge round-trip compuesto sobre runtime canónico + schemas NC001; primera recombinación novedosa licenciada `Ma' beedabe`.
- v4: contrato round-trip v0.2 estabilizado; separación `ANALYZED != GENERATION_LICENSED` y gate de compatibilidad de valencia.
- v34: cambio del default C02 a `quí` sin invalidar `qué`.
- v35: materialización/priorización de huecos del grafo de COR001, sin convertir COR001 en evidencia.
- v36: congela la expansión técnica de COR001 y activa literatura + audio independiente.
- v37.1: cierre de la pasada BIB065 y preservación del Analyzer de frase aislada.

### Readiness

Se localizaron matrices `GENERATION_READINESS_MATRIX` sucesivas hasta `v14`; `v14` sigue siendo la más reciente localizada en los paquetes inspeccionados y está migrada.

## 8. Dependencias del Analyzer v0.35

Requiere:

```text
didxaza_runtime_v0_2_1_retrieval.py
didxaza_runtime_v0_2_4_bound.py
didxaza_runtime_v0_2_5_morphology_ii.py
didxaza_runtime_v0_2_3_morphology_i.py
DICTIONARIA_entries_v0_2_15_2.csv
DICTIONARIA_senses_v0_2_15_2.csv
DICTIONARIA_examples_v0_2_15_2.csv
DIC_VERB_2385_v0_1.csv
SQLite table verb_lexeme_class_v023
SQLite table person_possession_exact_v0214
```

Todas las dependencias enumeradas están presentes y verificadas. El Analyzer v0.35 puede instanciarse desde el repositorio mediante `analyzer_v0_35_migrated_adapter.py` y conserva su contrato `NON_LICENSING_PARTIAL_COMPONENT_ANALYSIS`.

Smoke test documentado:

```text
"Quí rasé'" -> PARTIAL_ANALYSIS_NON_LICENSING
forma deliberadamente inexistente -> ABSTAIN_NO_COMPONENT_EVIDENCE
COR001 benchmark/gold/rule discovery -> false
```

## 9. Otros artefactos localizados y pendientes

| Artefacto | Estado actual | SHA-256 si aplica |
|---|---|---|
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `61fd21298c1260924fdc95b7e201b8d601dc83820f3d4f3686f508a74ae57c6a` |
| `DevelopmentCorpusProtocol_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `563dc30977a1f6175e823c60a8f79f8c78f1ec81ff09b27ad0943ceaff5fd8ad` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `3ea1d5b4598067f3fe51a03c6e3afa65131c5a543b16f8843b6f1727be094de7` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `acffea79fe7d228a0b28f740094e5a15fd4ec0ba6d36b257cc3aaef918a83c54` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / historical provisional | `f3308483c3135e43d49f2641f518aecd0dbf3c1fcbdc98f349511751ce86b295` |
| `COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `b369215edec07a98b59b6ee22a87995b20614d7a45dd16541f0deb71b93fd0d3` |
| `generator_v0_2.py` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / `SUPERSEDED` / `ARCHIVE_ONLY` | `54257f9a6dae12aba003e50e81b14bc25fba1d3e54e2eeecce009130c01fbacc` |
| `canonical_analyzer_roundtrip_bridge_v0_2.py` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / `SUPERSEDED` / `ARCHIVE_ONLY` | `bf1c3604f59aa559f8c1e5a6e7cfd1c78b16315f0dbbd1c1218f4e0a09cd0436` |
| `GenerationLicense_v0_2_roundtrip.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / `SUPERSEDED` / `ARCHIVE_ONLY` | `0afb4d10fb96d8d0f264ad4ace18b2174b101aa86a593835b7530dfc57746861` |
| `GenerationEvidenceAtoms_v0_2_roundtrip.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / `SUPERSEDED` / `ARCHIVE_ONLY` | `eb12fd80cae634c3f66ba4003b6804bfd65a06f35d96726eef18d6d38635c191` |
| `STABILIZATION_REPORT_v0_2.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / `ARCHIVE_ONLY` | `76d2655f9cd95eec69c0d143a264a49aa51b67cf55e609fc882c9dffdd530447` |

El backlog pedagógico v0.35 es provisional/histórico y no reemplaza el freeze pedagógico post-BIB065 ya migrado.

## 10. Reuse map y artefactos históricos referenciados

| Artefacto | Estado | Nota |
|---|---|---|
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `didxaza_vertical_slice_v0_1.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | ReviewCandidate histórico; requiere inspección |
| `mvp_review_candidate_adapter_v0.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | conserva procedencia de candidatos |
| `generator_view(claims)` v0.2.6 | `REFERENCED_BY_LOCATED_ARTIFACT` | reutilizado mediante adapter hash-gated |

El reuse map mantiene en cuarentena para Generator_v0: near-match con `SequenceMatcher`, normalización destructiva de diacríticos, propuestas de superficie derivadas de paradigma, dependencia de COR001 como licencia, confidence legado, handlers particulares de COR001 y owner review como licencia de generación.

## 11. Commits de esta pasada

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
```

`CURRENT_STATE_NC001_v35_POST_EVIDENCE_GAP_PRIORITIZER.md` y varios archivos textuales del runtime ya estaban presentes al verificarlos; no se les atribuye un commit nuevo de esta pasada.

## 12. Orden de recuperación restante

**P0 — conservar estado reproducible:**

1. trazar y migrar el conjunto mínimo necesario para reproducir la clausura histórica de 38 pruebas de v0.2.15.3, sin convertir el replay de COR001 en benchmark ni fuente de reglas;
2. recuperar bindings/licencias exactas restantes del Tutor_v0.33.

**P1 — reproducibilidad y límites:** guardrails, DevelopmentCorpusProtocol, reportes/tests/adapters y matrices BIB065.

**P2 — ejecutables útiles:** sólo después de conocer versión, dependencias y vigencia.

**P3 — historia:** auditorías y versiones intermedias como `ARCHIVE_ONLY` cuando expliquen genealogía. No reconstruir toda la historia.

## 13. Criterio de migración

Antes de incorporar una pieza:

1. identificar versión;
2. identificar función original;
3. separar vigente / provisional / superseded / cuarentena;
4. conservar procedencia y dependencias;
5. determinar si es estado, ejecutable o historia;
6. impedir que su copia sea interpretada como nueva regla lingüística o pedagógica.

## 14. Próxima acción

**Siguiente P0 recomendado:** inspeccionar la clausura histórica de 38 pruebas y migrar sólo sus dependencias directas todavía ausentes —tests v0.2.15.2, schemas/registries y runner estrictamente necesarios— para distinguir qué parte del `CLOSED_PASS` completo puede reproducirse. COR001 debe permanecer `ANALYSIS_TARGET_ONLY`: el replay puede verificar estabilidad técnica, nunca funcionar como gold, benchmark o fuente de reglas.

La reconciliación técnica no cambia reglas lingüísticas, no convierte la readiness histórica en política actual y no bloquea COR002, corpus oral ni trabajo con hablantes.
