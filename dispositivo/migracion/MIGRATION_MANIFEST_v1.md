# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Estado:** ACTIVE_INVENTORY / NO_BLOCKING  
**Alcance:** recuperación selectiva del estado técnico y documental del dispositivo

## 1. Principio

La migración preserva conocimiento, procedencia y capacidad reproducible. **No congela la investigación ni convierte la arquitectura recuperada en arquitectura definitiva.**

Se rige por `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`.

```text
MIGRATED_ARTIFACT != IMMUTABLE_RULE
IMPLEMENTED_CAPABILITY != RESEARCH_AUTHORITY
MIGRATION_STATUS != PEDAGOGICAL_PRIORITY
MIGRATION_INCOMPLETE != RESEARCH_BLOCKED
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

Ningún estado concede autoridad lingüística o pedagógica.

## 3. Migrado

| Artefacto | Función |
|---|---|
| `dispositivo/README.md` | arquitectura y frontera del dispositivo |
| `dispositivo/ESTADO_ACTUAL_2026-08-31.md` | snapshot técnico |
| `dispositivo/ANALYZER_SCOPE_MULTIESCALA_2026-08-31.md` | alcance palabra → discurso |
| `dispositivo/PROVENANCE_LABEL_CROSSWALK_v0_1.md` | equivalencias de procedencia |
| `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` | discusión pedagógica no normativa |
| `dispositivo/migracion/fuentes/MVP_REUSE_MAP_v1.md` | mapa de reutilización/cuarentena del vertical slice |

## 4. P0 ya localizado, pendiente de migración íntegra

### `JUCHITAN_LINGUISTIC_CORE_v0_27.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`

Fuente localizada en File Library. Coincide en encabezado y alcance con el núcleo experimental citado por el snapshot. Es largo; **no se migrará desde una vista truncada**. Debe copiarse íntegro o no copiarse.

Destino previsto:

`dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md`

### Genealogía de `NUCLEO_CONVERSACIONAL_001`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`

`RESPUESTA_CLAUDE_PAQUETE_LLUVIAS_IDEAS_DIDXAZA_v0_2.md` contiene una especificación temprana explícita del vertical slice, con objetivos, salidas, tests y no-objetivos.

No se tratará como especificación final. Debe contrastarse con la implementación posterior y con los artefactos del MVP antes de decidir qué documento representa mejor el estado de NC001.

### `COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`

Reporte de cobertura del Analyzer. Mantiene COR001 como `ANALYSIS_TARGET_ONLY` y documenta el hueco de un orquestador general. Debe migrarse como reporte, no como benchmark lingüístico.

## 5. Artefactos referenciados por el reuse map

| Artefacto | Estado | Nota |
|---|---|---|
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | hash histórico observado, no retroactivamente canónico |
| `didxaza_vertical_slice_v0_1.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | ReviewCandidate histórico; requiere inspección |
| `mvp_review_candidate_adapter_v0.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | conserva procedencia de candidatos |
| `generator_view(claims)` v0.2.6 | `REFERENCED_BY_LOCATED_ARTIFACT` | reutilizado mediante adapter hash-gated |

El reuse map conserva explícitamente en cuarentena para `Generator_v0`: near-match con `SequenceMatcher`, normalización destructiva de diacríticos, propuestas de superficie derivadas de paradigma, dependencia de COR001 como licencia, confidence legado, handlers particulares de COR001 y owner review como licencia de generación.

## 6. Estado técnico conocido todavía no migrado

| Artefacto / familia | Estado | Prioridad |
|---|---|---|
| runtime lingüístico v0.2.15.3 | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| base SQLite v2.20 | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `Generator_v0` conservador | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| inventario de verbos y construcciones | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `ParadigmTable` | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `ValidationQueue_v0` | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `ConceptMapping` | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| `OrthographicProfile_v1_DRAFT` / AdoptionRecords | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| protocolos de adquisición oral del slice | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| schemas/tests/adapters asociados | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |

## 7. Nombres todavía no localizados en esta pasada

| Artefacto | Estado |
|---|---|
| `CURRENT_STATE_NC001_v2_POST_GENERATOR_V0` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `GENERATION_READINESS_MATRIX_v1` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `DevelopmentCorpusProtocol_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.*` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |

Antes de reconstruir cualquiera se revisarán ZIPs, paquetes migratorios y documentos contenedores.

## 8. Orden

**P0 — conservar estado:** core v0.27; estado real de NC001; runtime/DB verificables; Generator_v0; inventarios, paradigmas y ValidationQueue.

**P1 — reproducibilidad y límites:** schemas, tests, adapters, guardrails, DevelopmentCorpusProtocol, reportes, readiness matrices, perfiles ortográficos y AdoptionRecords.

**P2 — ejecutables útiles:** sólo después de conocer versión, dependencias y vigencia.

**P3 — historia:** auditorías, lluvias de ideas y migraciones previas como `ARCHIVE_ONLY` cuando expliquen genealogía. No reconstruir todas las versiones intermedias.

## 9. Criterio de migración

Antes de incorporar una pieza:

1. identificar versión;
2. identificar función original;
3. separar vigente / provisional / superseded / cuarentena;
4. conservar procedencia y dependencias;
5. determinar si es estado, ejecutable o historia;
6. impedir que su copia sea interpretada como nueva regla lingüística o pedagógica.

## 10. Próxima acción

Localizar el paquete o artefacto que permita recuperar **íntegramente** `JUCHITAN_LINGUISTIC_CORE_v0_27` y, en paralelo, los archivos posteriores de NC001/Generator_v0. No escribir ni reconstruir código hasta agotar recuperación documental y de paquetes existentes.
