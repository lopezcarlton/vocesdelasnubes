# REENTRY_CHECKPOINT_2026-09-02

**Proyecto:** Voces de las Nubes  
**Fecha:** 2026-09-02  
**Estado:** `HISTORICAL_CHAT_MIGRATION_SUFFICIENT / FINAL_REENTRY_CLOSURE_PENDING / NON_CANONICAL`

## 1. Función

Este checkpoint registra que la recuperación histórica desde chats del dispositivo ha llegado a un punto suficiente para continuar el proyecto desde GitHub sin seguir recorriendo conversaciones por defecto.

No reemplaza el Sistema de Conocimiento canónico ni convierte el estado técnico recuperado en autoridad lingüística o pedagógica.

```text
HISTORICAL_CHAT_MIGRATION_SUFFICIENT != ALL_HISTORICAL_PAYLOADS_RECOVERED
REPOSITORY_REENTRY_READY != RUNTIME_COMPLETE
TECHNICAL_REPLAY != LINGUISTIC_VALIDATION
```

## 2. Estado técnico materializado

Consultar como fuente técnica vigente:

- `dispositivo/migracion/MIGRATION_MANIFEST_v1.md`
- `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md`
- `dispositivo/ESTADO_ACTUAL_2026-08-31.md`

A este corte:

- runtime v0.2.15.3: subconjunto exacto materializado, con dependencias directas conocidas para el replay histórico presentes;
- Analyzer v0.35: subconjunto parcial no licenciante reproducible;
- Generator v0.5: fuente histórica + adaptador al layout migrado;
- Tutor v0.33: fuente presente, dependencias incompletas;
- NC001/core: artefactos principales migrados con genealogía;
- COR001: exclusivamente `ANALYSIS_TARGET_ONLY`.

## 3. BIB065 / Bueno Holle

La lectura intensiva de Bueno Holle 2019 está cerrada para esta pasada.

Estado:

`STUDIED_IN_DEPTH / HIGH_VALUE_DISCOURSE_SOURCE / NOT_NORMATIVE / PARTIALLY_EXECUTABLE`

Artefactos disponibles en el repositorio:

- `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md`
- `dispositivo/migracion/fuentes/BH2019_READING_STATE_CLOSED_v0_36_1.md`
- `dispositivo/migracion/fuentes/BH2019_SOURCE_PROVENANCE_v0_36_1.json`
- `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md`

La matriz CSV exacta puede permanecer como pendiente de transporte hasta que su identidad byte a byte quede verificada en GitHub.

## 4. Guardrails recuperados

Quedan materializados para reentrada:

- `dispositivo/hardening/ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md`
- `dispositivo/development_corpus/DevelopmentCorpusProtocol_v0_35.md`

Protecciones centrales:

- la frase aislada sigue siendo una unidad válida de análisis;
- el contexto puede enriquecer, nunca bloquear el análisis local;
- `UNRESOLVED != INCORRECT`;
- frecuencia no equivale a gramaticalidad;
- ninguna fuente individual se convierte en gramática global;
- audio, transcripción y análisis permanecen en capas separadas;
- las propiedades discursivas/prosódicas pueden conservarse sin volverse campos obligatorios.

## 5. Pedagogía

El documento `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` es un insumo de discusión no normativo.

Debe conservarse explícitamente:

```text
COR002_BEGINNER_SCOPE = STRONG_WORKING_IDEA / DISCUSS
PEDAGOGICAL_ARTIFACT != STYLE_AUTHORITY
NC001_TECHNICAL_SCOPE != COR002_PEDAGOGICAL_SCOPE
```

No reescribe automáticamente COR002, P1–P5, Generator, Tutor o Analyzer.

El estado canónico de pedagogía sigue gobernado por `conocimiento/PEDAGOGIA.md` y las decisiones vigentes del Sistema de Conocimiento.

## 6. Pendientes que NO bloquean reentrada

No es necesario recuperar los 75 payloads históricos del runtime para seguir investigando.

Tampoco bloquean la reentrada:

- ZIPs históricos completos cuyo contenido textual relevante ya fue migrado;
- runners/reports COR001 históricos que sólo sirven a genealogía;
- artefactos explícitamente `ARCHIVE_ONLY` o `SUPERSEDED`;
- la regeneración técnica del replay v0.2.15.3.

El replay puede ejecutarse una sola vez desde el repositorio como prueba de reproducibilidad técnica. Un `PASS` no concede autoridad lingüística a COR001.

## 7. Cierre documental pendiente

Antes de declarar el repositorio como punto de reentrada completamente autocontenido conviene:

1. verificar/migrar la matriz CSV exacta BIB065;
2. reconciliar `MIGRATION_MANIFEST_v1.md` con los artefactos recuperados en la última pasada;
3. comprobar que ningún estado vigente apunte a rutas inexistentes;
4. enlazar el entrypoint de reentrada desde el README o desde la navegación principal si se considera útil.

Estos son pendientes documentales, no recuperación histórica P0.

## 8. Ruta de investigación activa

1. continuar literatura lingüística con la siguiente fuente pertinente;
2. iniciar/desarrollar corpus oral independiente de Juchitán, audio-first;
3. mantener COR002 como piloto pedagógico revisable orientado a principiantes;
4. contrastar literatura, hablantes, corpus oral y conocimiento existente;
5. promover conocimiento al dispositivo sólo según evidencia y autoridad explícitas;
6. no reabrir por defecto la cola caso por caso de COR001.
