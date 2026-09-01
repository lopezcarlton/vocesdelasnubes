# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Última actualización:** 2026-09-01 — primera pasada P0 desde paquete v0.36.2  
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
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` | estado post Generator_v0; hashes runtime/SQLite y ausencia del orquestador canónico en ese hito |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v34_POST_C02_DEFAULT_QUI_MIGRATION.md` | transición C02 al default juchiteco `quí`; `qué` preservado como variante secundaria |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v36_POST_KNOWLEDGE_INGESTION_GUARDRAILS.md` | guardrails de degradación elegante y ruta literatura+audio |
| `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md` | estado posterior al cierre BIB065; ruta activa más reciente localizada |
| `dispositivo/generator/inputs/ConstructionInventory_v1.jsonl` | seis construcciones NC001 con alcance y abstenciones |
| `dispositivo/generator/inputs/ParadigmTable_v1.csv` | tabla de celdas TAM/persona y procedencia del slice |
| `dispositivo/validation/ValidationQueue_v0.jsonl` | cola de validación/desarrollo audio-first |
| `dispositivo/analyzer/non_licensing_analyzer_orchestrator_v0_35.py` | Analyzer parcial no licenciante con contexto opcional |
| `dispositivo/generator/generator_v0_5.py` | implementación más reciente del Generator_v0 localizada en paquete v0.36.2 |
| `dispositivo/generator/GENERATION_READINESS_MATRIX_v14.csv` | snapshot de readiness más reciente localizado en el paquete |

### 3.1 Verificación de fuentes migradas en esta pasada

- `non_licensing_analyzer_orchestrator_v0_35.py`: SHA-256 de fuente `9ff7965bd1c7304ed1527f14896d2539c45b5ba5733a7062f8433ae56a6f0735`; Git blob del repo coincide exactamente con el Git blob calculado sobre la fuente local.
- `generator_v0_5.py`: SHA-256 de fuente `6db94a8cc73fa1cee6f73a4d1404adebb53bc3ec58133a073584ed5ed59a726c`; Git blob del repo coincide exactamente con el Git blob calculado sobre la fuente local.
- `ParadigmTable_v1.csv`: SHA-256 del archivo fuente `ecef1339c9d8e7ad11689770efaa108dffa76866e34c24d85a5d0ee46aa05ed4`. Fue copiado como texto mediante Contents API; **no se afirma identidad binaria** del archivo transportado porque la fuente usa CRLF/BOM y el transporte textual puede normalizar bytes. La tabla fuente y su hash quedan registrados para auditoría posterior.
- `GENERATION_READINESS_MATRIX_v14.csv`: SHA-256 de fuente `2735a757d625d478db2fbaab240b425839ed62fdc8d2a6da20cbc9c25d8f010b`.

## 4. P0 localizado, todavía pendiente

### `JUCHITAN_LINGUISTIC_CORE_v0_27.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`

Fuente completa claramente identificada en File Library con encabezado `JUCHITAN_LINGUISTIC_CORE — v0.27`, estado `EXPERIMENTAL_CORE` y consumidores Analyzer/Corrector/Tutor/Generator. La interfaz disponible devuelve vistas truncadas del archivo largo. **No se migró desde fragmentos.**

Destino previsto:

`dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md`

### runtime lingüístico v0.2.15.3

**Estado:** `REFERENCED_BY_LOCATED_ARTIFACT`

`CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` verifica la identidad histórica:

```text
SHA256 = 6e5c3e8ee9bb5dbd04666537dc423724eb4bc402440e670e5be81cfa54b5d7e5
MATCH_EXACT
```

La raíz fuente del runtime no apareció en el paquete v0.36.2. El Analyzer v0.35 añade dependencias explícitas sobre módulos de este runtime.

### SQLite v2.20

**Estado:** `REFERENCED_BY_LOCATED_ARTIFACT`

Identidad verificada por el estado v2:

```text
SHA256 = 2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed
SQLITE_INTEGRITY_CHECK = ok
FOREIGN_KEY_VIOLATIONS = 0
```

El binario `.sqlite/.db` no está presente en el paquete v0.36.2, por lo que no se creó un sustituto.

### `DIC_VERB_2385_v0_1.csv`

**Estado:** `SOURCE_COMPLETE_READY_TO_MIGRATE`

Fuente exacta presente en `analyzer_v0/` del paquete v0.36.2.

```text
SHA256 = 2bdf4afd4b61234c54585cda17ad648bfb71194e9463d193eb04a5a06aa3183d
SIZE ≈ 767 KB
```

Es dependencia local por defecto del Analyzer v0.35. Sigue pendiente por tamaño/transferencia textual; no debe reconstruirse.

## 5. P0/P1: dependencias del Generator localizadas y pendientes

El Generator migrado no se considera reproducible todavía hasta recuperar sus inputs exactos restantes.

| Artefacto | Estado | SHA-256 fuente |
|---|---|---|
| `GenerationLicense_v0_33_c02_default_qui.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `c4d2b01ea183830a9abc41f4bd94ef3856226055a5b692754868163151c03cea` |
| `GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `e0b2f12c38ef92e8fd7f0310acc0cb73187a5278835f2ee3f884eb83ae336a09` |
| `AuthorizedSlotFillers_v0_33.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `f09df507b1a1d1b97dbdff35c0535eca19ef856531c878b3f1eabbb2d790c842` |
| `IntegrationBlockers_v0_1.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `22cc7998d5fa572c66a72aafab578041a3753c75e5c7aa6fd20112af036f53ce` |
| `OrthographicResolutions_v0_9.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `4be2110b0408f6a5cf72d8e65a95bf17381cfa3eaa0357fd35e6749fec7135bd` |
| `AdoptionRecords_v1.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `107636011643c352750af44793ac1370967219042ad596e199362be19c5e3904` |
| `ConceptMapping_v1.jsonl` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `bfa8d3f4d384ff73fbcf0c5c5166c39c4df70762a6fededccc8e07e2df0ea9fe` |
| `OrthographicProfile_v1_DRAFT.json` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `9f97928c88d529647dd027235a95b9219a4fffd45004dfa5b482f73a43772e70` |

## 6. Genealogías recuperadas

### Generator_v0

El paquete contiene:

```text
generator_v0.py
-> generator_v0_1.py
-> generator_v0_2.py
-> generator_v0_3.py
-> generator_v0_4.py
-> generator_v0_5.py
```

`generator_v0_5.py` es la versión más reciente localizada y cambia sus bindings activos de C02 a:

```text
GenerationLicense_v0_33_c02_default_qui.jsonl
GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl
AuthorizedSlotFillers_v0_33.jsonl
```

No se borraron ni se reinterpretaron versiones anteriores; quedan como genealogía histórica en el paquete fuente.

### Analyzer no licenciante

```text
v0_25 -> v0_26 -> v0_35
```

v0.35 añade un canal opcional `context_segments` sin volver contexto requisito del análisis local.

### NC001 state

El paquete v0.36.2 contiene una secuencia de estados desde `CURRENT_STATE_NC001_v2_POST_GENERATOR_V0.md` hasta `CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md`. Para la primera pasada se migraron cuatro checkpoints de alto valor: v2, v34, v36 y v37.1.

- v34 documenta el cambio del default C02 a `quí` sin invalidar `qué`.
- v36 congela la cola COR001 y activa literatura + audio independiente.
- v37.1 cierra BIB065 para esa pasada y preserva el Analyzer de frase aislada.

### Readiness

Se localizaron matrices `GENERATION_READINESS_MATRIX` sucesivas hasta `v14`; `v14` es la más reciente presente en el paquete y fue migrada.

## 7. Dependencias nuevas explicitadas por esta recuperación

### Analyzer v0.35

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

### Generator v0_5

Requiere:

```text
ParadigmTable_v1.csv
ConstructionInventory_v1.jsonl
GenerationLicense_v0_33_c02_default_qui.jsonl
IntegrationBlockers_v0_1.jsonl
GenerationEvidenceAtoms_v0_33_c02_default_qui.jsonl
AuthorizedSlotFillers_v0_33.jsonl
AdoptionRecords_v1.jsonl
OrthographicResolutions_v0_9.jsonl
```

Además acepta `canonical_analyzer` como callback para round-trip de recombinación novedosa. La existencia del Analyzer no licenciante v0.35 **no implica por sí sola** que satisfaga ese contrato de round-trip.

## 8. Otros artefactos antes marcados como no localizados que sí aparecieron

| Artefacto | Estado actual | SHA-256 si aplica |
|---|---|---|
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `61fd21298c1260924fdc95b7e201b8d601dc83820f3d4f3686f508a74ae57c6a` |
| `DevelopmentCorpusProtocol_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `563dc30977a1f6175e823c60a8f79f8c78f1ec81ff09b27ad0943ceaff5fd8ad` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `3ea1d5b4598067f3fe51a03c6e3afa65131c5a543b16f8843b6f1727be094de7` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `acffea79fe7d228a0b28f740094e5a15fd4ec0ba6d36b257cc3aaef918a83c54` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` / historical provisional | `f3308483c3135e43d49f2641f518aecd0dbf3c1fcbdc98f349511751ce86b295` |
| `COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md` | `SOURCE_COMPLETE_READY_TO_MIGRATE` | `b369215edec07a98b59b6ee22a87995b20614d7a45dd16541f0deb71b93fd0d3` |

El backlog pedagógico v0.35 es provisional/histórico y no reemplaza el freeze pedagógico post-BIB065 ya migrado.

## 9. Reuse map y artefactos históricos referenciados

| Artefacto | Estado | Nota |
|---|---|---|
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `didxaza_vertical_slice_v0_1.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | ReviewCandidate histórico; requiere inspección |
| `mvp_review_candidate_adapter_v0.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | conserva procedencia de candidatos |
| `generator_view(claims)` v0.2.6 | `REFERENCED_BY_LOCATED_ARTIFACT` | reutilizado mediante adapter hash-gated |

El reuse map mantiene en cuarentena para Generator_v0: near-match con `SequenceMatcher`, normalización destructiva de diacríticos, propuestas de superficie derivadas de paradigma, dependencia de COR001 como licencia, confidence legado, handlers particulares de COR001 y owner review como licencia de generación.

## 10. Orden de recuperación restante

**P0 — conservar estado reproducible:**

1. `JUCHITAN_LINGUISTIC_CORE_v0_27.md` completo, sin vista truncada;
2. runtime v0.2.15.3 exacto;
3. SQLite v2.20 exacta;
4. `DIC_VERB_2385_v0_1.csv`;
5. inputs restantes del Generator_v0_5.

**P1 — reproducibilidad y límites:** guardrails, DevelopmentCorpusProtocol, AdoptionRecords/OrthographicProfile, ConceptMapping, reportes y tests/adapters.

**P2 — ejecutables útiles:** sólo después de conocer versión, dependencias y vigencia.

**P3 — historia:** auditorías y versiones intermedias como `ARCHIVE_ONLY` cuando expliquen genealogía. No reconstruir toda la historia.

## 11. Criterio de migración

Antes de incorporar una pieza:

1. identificar versión;
2. identificar función original;
3. separar vigente / provisional / superseded / cuarentena;
4. conservar procedencia y dependencias;
5. determinar si es estado, ejecutable o historia;
6. impedir que su copia sea interpretada como nueva regla lingüística o pedagógica.

## 12. Próxima acción

**Siguiente P0 recomendado:** recuperar y transferir íntegramente `JUCHITAN_LINGUISTIC_CORE_v0_27.md` desde su fuente completa de File Library, sin reconstruirlo desde fragmentos.

En paralelo, localizar la raíz exacta del runtime `v0.2.15.3` y el binario SQLite `v2.20`, porque son los dos bloqueadores externos principales para ejecutar el Analyzer v0.35 ya migrado.
