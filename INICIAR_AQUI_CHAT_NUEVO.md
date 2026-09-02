# INICIAR AQUÍ — CHAT NUEVO

## Objetivo

Este archivo es el punto de reentrada recomendado para continuar **Voces de las Nubes** desde el repositorio GitHub `lopezcarlton/vocesdelasnubes`, rama `main`, sin depender de paquetes ZIP ni de memoria de conversaciones anteriores.

## 1. Reconstrucción obligatoria antes de trabajar

Lee, en este orden:

1. `README.md`
2. `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`
3. `01_JERARQUIA_DE_VERDAD.md`
4. `02_BACKLOG.md`
5. `03_REGLAS_DE_ACTUALIZACIÓN.md`
6. `conocimiento/PEDAGOGIA.md`
7. `conocimiento/METODOLOGIA.md`
8. `conocimiento/CORPUS.md`
9. `conocimiento/VALIDACION.md`
10. `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`
11. `dispositivo/README.md`
12. `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md`
13. `dispositivo/migracion/MIGRATION_MANIFEST_v1.md`
14. `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md`
15. `dispositivo/migracion/REENTRY_CHECKPOINT_2026-09-02.md`
16. `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md`
17. `dispositivo/migracion/fuentes/BH2019_READING_STATE_CLOSED_v0_36_1.md`
18. `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md`
19. `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md`
20. `dispositivo/hardening/ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md`
21. `dispositivo/development_corpus/DevelopmentCorpusProtocol_v0_35.md`

Si alguna ruta no existe, no la inventes ni sustituyas silenciosamente: registra la discrepancia y usa la jerarquía de verdad para determinar qué estado sí está materializado.

## 2. Reglas de reentrada

- El repositorio es la memoria de trabajo persistente; la conversación nueva no debe intentar reconstruir el proyecto desde recuerdos.
- `conocimiento/` contiene el Sistema de Conocimiento canónico.
- `dispositivo/` es experimental y no constituye una segunda fuente de verdad.
- Un artefacto migrado conserva estado e historia; no adquiere autoridad por estar implementado.
- Las contradicciones se documentan; no se armonizan silenciosamente.

## 3. COR001

```text
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

No reanudes por defecto la resolución caso por caso de huecos de COR001 (`zanda`, `stobi`, etc.).

Un replay histórico puede servir para reproducibilidad técnica, nunca para convertir COR001 en autoridad lingüística.

## 4. Bueno Holle / BIB065

La lectura intensiva de Bueno Holle 2019 está cerrada para esta pasada.

```text
BIB065 = STUDIED_IN_DEPTH
BIB065 = HIGH_VALUE_DISCOURSE_SOURCE
BIB065 = NOT_NORMATIVE
BIB065 = PARTIALLY_EXECUTABLE
```

No retomes §5.2 como si la lectura siguiera incompleta.

Las tendencias y análisis de BIB065 no se convierten automáticamente en reglas de corrección, generación o pedagogía.

## 5. Analyzer y contexto

La frase aislada sigue siendo un objeto de análisis de primera clase.

```text
MISSING_CONTEXT != ANALYZER_BLOCK
UNRESOLVED != INCORRECT
OPTIONAL_CONTEXT -> MAY_REFINE_CONTEXT_SENSITIVE_CLAIMS
```

El contexto puede enriquecer correferencia, tópico/foco, accesibilidad o naturalidad discursiva, pero no debe bloquear análisis lexical, morfológico o sintáctico local que tenga evidencia independiente.

## 6. COR002 y pedagogía

COR002 continúa en desarrollo como piloto revisable para principiantes.

La idea de mantenerlo deliberadamente básico es una **hipótesis de trabajo fuerte para discusión**, no una regla cerrada.

```text
PEDAGOGICAL_ARTIFACT != STYLE_AUTHORITY
PAST_CORPUS_OUTPUT != PEDAGOGICAL_GOLD_STANDARD
CURRENT_TEMPLATE != PERMANENT_TEMPLATE
NC001_TECHNICAL_SCOPE != COR002_PEDAGOGICAL_SCOPE
```

G/P continúa siendo un marco de trabajo útil, pero las fronteras exactas G1–G5/P1–P5 y su uso curricular permanecen abiertas a investigación.

No conviertas las capas finas de BIB065 automáticamente en P, G ni en un tercer eje pedagógico.

## 7. Ruta activa

La ruta de trabajo vigente es:

1. continuar literatura lingüística con la siguiente fuente pertinente;
2. desarrollar en paralelo corpus oral independiente de Juchitán, audio-first;
3. contrastar nueva evidencia con hablantes, literatura y conocimiento existente;
4. usar la evidencia nueva para probar/refinar el dispositivo;
5. mantener la discusión pedagógica abierta sin congelar prematuramente estilos o currículos;
6. no ampliar infraestructura sin una necesidad concreta de investigación o reproducibilidad.

## 8. Qué hacer al iniciar un chat

Antes de modificar archivos o proponer una nueva arquitectura, devuelve un diagnóstico breve con:

- estado actual reconstruido;
- documentos que consideras vigentes;
- snapshots históricos o superseded que detectaste;
- contradicciones o rutas rotas;
- siguiente paso que corresponde según el repositorio.

No modifiques nada hasta que el usuario confirme que la reconstrucción es correcta.
