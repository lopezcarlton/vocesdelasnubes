# MIGRATION_MANIFEST_v1 — Dispositivo lingüístico

**Proyecto:** Voces de las Nubes  
**Fecha de inicio:** 2026-08-31  
**Estado:** ACTIVE_INVENTORY / NO_BLOCKING  
**Alcance:** recuperación selectiva del estado técnico y documental del dispositivo

## 1. Propósito

Este manifiesto registra qué piezas del dispositivo ya están en el repositorio, cuáles han sido localizadas fuera de él, cuáles sabemos que existen pero todavía no hemos recuperado y cuáles sólo deben conservarse como antecedente histórico.

La migración tiene tres objetivos:

1. evitar pérdida de conocimiento y procedencia;
2. recuperar capacidad reproducible que siga siendo útil;
3. permitir retomar Analyzer, Corrector, Tutor y Generator sin reconstruir su historia desde chats.

**La migración no tiene como objetivo congelar la arquitectura actual.**

Se rige por `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`.

```text
MIGRATED_ARTIFACT != IMMUTABLE_RULE
IMPLEMENTED_CAPABILITY != RESEARCH_AUTHORITY
MIGRATION_STATUS != PEDAGOGICAL_PRIORITY
MIGRATION_INCOMPLETE != RESEARCH_BLOCKED
```

El trabajo lingüístico, bibliográfico, pedagógico, de corpus y con hablantes puede continuar mientras se realiza esta recuperación, salvo que una tarea concreta dependa técnicamente de un artefacto todavía no recuperado.

---

## 2. Estados de migración

- `MIGRATED` — ya existe dentro del repositorio.
- `RECOVERABLE_SOURCE_LOCATED` — se localizó una fuente externa concreta que puede inspeccionarse antes de migrar.
- `REFERENCED_BY_LOCATED_ARTIFACT` — su existencia está documentada por una fuente localizada, pero el archivo mismo todavía no ha sido recuperado.
- `EXTERNAL_KNOWN_NOT_MIGRATED` — sabemos que forma parte del estado del dispositivo, pero todavía no se localiza aquí una fuente exacta para copiar.
- `NOT_LOCATED_IN_CURRENT_PASS` — se buscó por nombre o función en esta pasada y no apareció; no equivale a perdido definitivamente.
- `SUPERSEDED` — conserva valor histórico pero no representa el estado vigente.
- `ARCHIVE_ONLY` — debe conservarse por trazabilidad, no como pieza activa.

Ningún estado concede autoridad lingüística o pedagógica.

---

## 3. Ya migrado al repositorio

| Artefacto | Estado | Función |
|---|---|---|
| `dispositivo/README.md` | `MIGRATED` | frontera y arquitectura general del dispositivo |
| `dispositivo/ESTADO_ACTUAL_2026-08-31.md` | `MIGRATED` | snapshot técnico previo a la migración detallada |
| `dispositivo/ANALYZER_SCOPE_MULTIESCALA_2026-08-31.md` | `MIGRATED` | requisito de análisis desde palabra hasta discurso |
| `dispositivo/PROVENANCE_LABEL_CROSSWALK_v0_1.md` | `MIGRATED` | compatibilidad entre nomenclaturas históricas de procedencia |
| `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` | `MIGRATED` | discusión pedagógica no normativa derivada del trabajo del dispositivo |

---

## 4. Fuentes externas ya localizadas

### 4.1 `JUCHITAN_LINGUISTIC_CORE_v0_27.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`  
**Prioridad de inspección:** P0

Fuente localizada en File Library. Contiene el núcleo experimental de Juchitán y reglas/documentación para sintaxis, morfología, referencia, discurso, procedencia y otros dominios.

Antes de migrarlo debe comprobarse:

- que sea exactamente la versión v0.27 que corresponde al snapshot de cierre;
- qué secciones son estado consolidado y cuáles son hipótesis o planes;
- que no reactive reglas superseded únicamente por estar presentes en el documento.

Destino provisional sugerido:

`dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md`

### 4.2 `MVP_REUSE_MAP_v1.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`  
**Prioridad de inspección:** P0

Fuente localizada. Registra artefactos del vertical slice, reutilización permitida y mecanismos explícitamente puestos en cuarentena para `Generator_v0`.

Es especialmente valioso porque distingue qué piezas históricas pueden reutilizarse y cuáles no deben convertirse en licencia de generación.

Destino provisional sugerido:

`dispositivo/migracion/fuentes/MVP_REUSE_MAP_v1.md`

### 4.3 `RESPUESTA_CLAUDE_PAQUETE_LLUVIAS_IDEAS_DIDXAZA_v0_2.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED` como fuente de diseño, no como autoridad final  
**Prioridad de inspección:** P0

Contiene una formulación explícita del vertical slice `NUCLEO_CONVERSACIONAL_001`, incluyendo objetivos, salidas, tests y no-objetivos. Sirve para localizar y reconstruir la genealogía de NC001.

No debe migrarse como si fuera por sí sola la especificación canónica de NC001. Primero debe contrastarse con los artefactos posteriores que materializaron el slice.

Destino provisional si se conserva:

`dispositivo/migracion/fuentes/RESPUESTA_CLAUDE_PAQUETE_LLUVIAS_IDEAS_DIDXAZA_v0_2.md`

### 4.4 `COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md`

**Estado:** `RECOVERABLE_SOURCE_LOCATED`  
**Prioridad de inspección:** P1

Reporte posterior que documenta el comportamiento del Analyzer sobre COR001 como `ANALYSIS_TARGET_ONLY`: 107/107 abstenciones del conjunto estrecho de bridges existentes, junto con controles positivos y la conclusión de que faltaba un orquestador general de análisis.

Debe conservarse como reporte de cobertura/estado, no como benchmark lingüístico de COR001.

Destino provisional sugerido:

`dispositivo/analyzer/reports/COR001_ANALYSIS_TARGET_PASS_REPORT_v0_24.md`

---

## 5. Artefactos referenciados por fuentes localizadas

| Artefacto | Estado | Nota |
|---|---|---|
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_1.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | `MVP_REUSE_MAP_v1` registra hash histórico observado |
| `MVP_LINGUISTICO_001_VERTICAL_SLICE_v0_2.zip` | `REFERENCED_BY_LOCATED_ARTIFACT` | `MVP_REUSE_MAP_v1` registra hash histórico observado |
| `didxaza_vertical_slice_v0_1.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | antecedente `ReviewCandidate`; no migrar como implementación vigente sin inspección |
| `mvp_review_candidate_adapter_v0.py` | `REFERENCED_BY_LOCATED_ARTIFACT` | conserva procedencia de candidatos según reuse map |
| runtime canónico reutilizado por adapter | `REFERENCED_BY_LOCATED_ARTIFACT` | verificar versión/hash antes de incorporar |

Los hashes históricos observados no deben convertirse retroactivamente en hashes canónicos si la fuente misma aclara que no lo eran.

---

## 6. Estado técnico conocido todavía no migrado

Los siguientes elementos aparecen en el snapshot del dispositivo o en la historia de trabajo reciente, pero requieren localizar su fuente exacta antes de copiar o reconstruir.

| Artefacto / familia | Estado | Prioridad |
|---|---|---|
| runtime lingüístico v0.2.15.3 | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| base SQLite v2.20 | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `Generator_v0` conservador | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| inventario de verbos / construcciones | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `ParadigmTable` y celdas atestadas/no atestadas | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| `ConceptMapping` | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| `OrthographicProfile_v1_DRAFT` / AdoptionRecords | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| `ValidationQueue_v0` | `EXTERNAL_KNOWN_NOT_MIGRATED` | P0 |
| protocolos/prompts de adquisición oral del slice | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |
| schemas/tests/adapters asociados | `EXTERNAL_KNOWN_NOT_MIGRATED` | P1 |

---

## 7. Documentos de estado buscados por nombre y todavía no localizados en esta pasada

Estos nombres aparecen en la historia reciente del dispositivo. La búsqueda actual de File Library no devolvió una coincidencia inequívoca por nombre.

| Artefacto | Estado |
|---|---|
| `CURRENT_STATE_NC001_v2_POST_GENERATOR_V0` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `GENERATION_READINESS_MATRIX_v1` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `DevelopmentCorpusProtocol_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.*` | `NOT_LOCATED_IN_CURRENT_PASS` |
| `PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `NOT_LOCATED_IN_CURRENT_PASS` |

`NOT_LOCATED_IN_CURRENT_PASS` significa únicamente que no apareció en estas búsquedas. Antes de reconstruir cualquiera de ellos deben revisarse paquetes de migración, ZIPs, documentos contenedores y archivos recientes relacionados.

---

## 8. Orden de migración

### P0 — Estado que no queremos perder

Primero:

1. núcleo v0.27;
2. especificación/estado real de NC001;
3. runtime y DB canónicos con versión/hash verificables;
4. estado de `Generator_v0`;
5. inventarios, paradigmas y ValidationQueue que determinan qué estaba realmente implementado.

### P1 — Reproducibilidad y límites

Después:

- schemas;
- tests;
- adapters;
- guardrails;
- DevelopmentCorpusProtocol;
- reports de Analyzer;
- readiness matrices;
- perfiles ortográficos y adoption records.

### P2 — Ejecutables útiles

Sólo después de entender su estado:

- scripts;
- runtimes auxiliares;
- bases derivadas;
- tooling de importación/validación.

Un ejecutable no se migra únicamente porque exista: debe ser reproducible, identificable y todavía útil.

### P3 — Historia y auditoría

Paquetes antiguos, respuestas de auditoría, lluvia de ideas y migraciones previas pueden conservarse como `ARCHIVE_ONLY` o como fuentes de genealogía cuando expliquen decisiones que de otro modo serían incomprensibles.

No es necesario reconstruir cada versión intermedia.

---

## 9. Regla de no-candado

La migración se considera una línea de preservación paralela, no una puerta obligatoria para toda la investigación.

Puede continuar en paralelo:

- COR001 bajo mantenimiento;
- piloto COR002;
- investigación de P;
- lectura e implementación conceptual de BIB065;
- corpus oral naturalista;
- trabajo con nuevos hablantes;
- adquisición bibliográfica;
- experimentos pedagógicos;
- investigación lingüística nueva.

Sólo se declarará un bloqueo cuando una tarea concreta requiera directamente una capacidad técnica todavía no recuperada.

---

## 10. Criterio para migrar una pieza

Antes de incorporar un artefacto externo al repositorio se debe responder:

1. ¿qué versión es exactamente?;
2. ¿qué función cumplía?;
3. ¿qué parte sigue vigente?;
4. ¿qué parte quedó superseded o en cuarentena?;
5. ¿qué evidencia/procedencia conserva?;
6. ¿depende de otros archivos?;
7. ¿es fuente de estado, ejecutable reproducible o sólo historia?;
8. ¿su migración puede confundirse con una nueva regla lingüística/pedagógica?;

Si la última respuesta es sí, debe acompañarse de un estado explícito que impida esa lectura.

---

## 11. Próxima acción

La siguiente acción de migración no es escribir código.

Es inspeccionar las fuentes P0 ya localizadas, empezando por:

1. `JUCHITAN_LINGUISTIC_CORE_v0_27.md`;
2. `MVP_REUSE_MAP_v1.md`;
3. la definición y genealogía de `NUCLEO_CONVERSACIONAL_001`;

para determinar qué artefactos exactos deben recuperarse después y evitar reconstrucciones innecesarias.
