# INICIAR AQUÍ — VOCES DE LAS NUBES

## Objetivo

Este archivo es el punto de reentrada general para continuar **Voces de las Nubes** desde `lopezcarlton/vocesdelasnubes`, rama `main`, sin depender de memoria de conversaciones anteriores.

Este reentry reconstruye **el Sistema de Conocimiento**. No carga por defecto el runtime ni el estado técnico del dispositivo.

Para trabajo explícitamente técnico usar `dispositivo/REENTRY_TECNICO.md`.

## 1. Reconstrucción obligatoria antes de trabajar

Leer, en este orden:

1. `README.md`
2. `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`
3. `01_JERARQUIA_DE_VERDAD.md`
4. `03_REGLAS_DE_ACTUALIZACIÓN.md`
5. `02_BACKLOG.md`
6. `conocimiento/decisiones/DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO.md`
7. `conocimiento/PEDAGOGIA.md`
8. `conocimiento/METODOLOGIA.md`
9. `conocimiento/CORPUS.md`
10. `conocimiento/VALIDACION.md`
11. `conocimiento/TEORIA.md`
12. `conocimiento/BIBLIOGRAFIA.md`
13. `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`
14. `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md`

Leer después las `SRC`, `HALL`, `DEC`, `VAL`, `TEO` u otras entidades que correspondan a la pregunta concreta.

Si una ruta no existe, no inventarla ni sustituirla silenciosamente.

## 2. Fuente de autoridad

`conocimiento/` y los documentos constitucionales contienen el Sistema de Conocimiento de Voces de las Nubes.

Las vistas documentales —`PEDAGOGIA.md`, `TEORIA.md`, `CORPUS.md`, `METODOLOGIA.md`, etc.— sintetizan conocimiento vigente; no sustituyen las fuentes, hallazgos, validaciones y decisiones que deben sustentar sus afirmaciones.

Una `DEC` vigente gobierna las vistas dentro de su alcance, subordinada a la Arquitectura, la Jerarquía de Verdad, las Reglas de Actualización y los principios válidos.

## 3. Frontera con sistemas derivados

El dispositivo y cualquier futura herramienta o repositorio técnico son **sistemas derivados**.

```text
DERIVED_SYSTEM_MAY_READ = true
DERIVED_SYSTEM_MAY_ANALYZE = true
DERIVED_SYSTEM_MAY_PROPOSE = true
DERIVED_SYSTEM_MAY_CHALLENGE = true

DERIVED_SYSTEM_MAY_ADOPT_KNOWLEDGE = false
DERIVED_SYSTEM_MAY_PROMOTE_CANDIDATE = false
DERIVED_SYSTEM_MAY_WRITE_KNOWLEDGE = false
```

Una mención a una herramienta es admisible cuando la subordina al Sistema de Conocimiento. Existe filtración cuando una vista pedagógica, lingüística o metodológica defiere a la herramienta la decisión sobre qué debe considerarse conocimiento.

Si un descubrimiento ocurre durante trabajo técnico:

```text
hallazgo_candidato
-> volver a la fuente original
-> registrar en Voces
-> adjudicar con autoridad pertinente
-> adoptar si corresponde
-> actualizar vistas
```

Nunca modificar `conocimiento/` directamente desde el resultado técnico.

## 4. COR001

```text
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

No reanudar por defecto la resolución caso por caso de huecos de COR001.

## 5. G/P y COR002

G/P continúa como arquitectura de trabajo revisable.

Las fronteras exactas G1–G5 y P1–P5 no están cerradas. No derivar una tabla definitiva de P a partir de una bibliografía general sin una adjudicación explícita del proyecto.

La idea de COR002 como material básico para principiantes sigue siendo una hipótesis de trabajo fuerte para discusión, no una especificación irrevocable.

## 6. BIB065 / Bueno Holle

La investigación realizada alrededor de Bueno Holle produjo hallazgos útiles y también mostró el riesgo de que conocimiento descubierto durante desarrollo técnico se incorpore sin una frontera suficientemente clara.

La fuente registrada dentro del Sistema de Conocimiento es `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md`.

Los artefactos BIB065 que existan bajo `dispositivo/` pueden utilizarse para reconstruir genealogía y candidatos, pero **no deben promoverse automáticamente** a pedagogía, teoría o metodología. Cuando sea necesario incorporar resultados posteriores de la lectura, volver a la obra original y adjudicarlos dentro de Voces de las Nubes.

## 7. Estado pre-Irma

El estado anterior a cualquier incorporación de la reunión con Irma Pineda está congelado en:

```text
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

Ver `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md`.

Cuando se aporte el contenido de la reunión, registrarlo primero como `SRC` crudo o evidencia claramente identificada. No modificar de inmediato `PEDAGOGIA.md`, `CORPUS.md`, `TEORIA.md`, `METODOLOGIA.md` ni decisiones vigentes.

## 8. Ruta inmediata

1. completar la limpieza de la frontera de autoridad pre-Irma;
2. capturar la reunión con Irma como fuente sin adjudicar cuando esté disponible;
3. adjudicar después sus hallazgos con la autoridad pertinente;
4. actualizar únicamente entonces las decisiones y vistas afectadas;
5. publicar un nuevo estado aprobado de conocimiento;
6. hacer que el dispositivo consuma ese estado sin adquirir autoridad de escritura sobre él.

## 9. Trabajo técnico

No cargar por defecto el estado técnico para conversaciones sobre bibliografía, pedagogía, corpus o metodología humana.

Cuando la tarea sea desarrollar Analyzer, Corrector, Tutor, Generator, runtime, pruebas o migración, cambiar explícitamente al punto de entrada:

`dispositivo/REENTRY_TECNICO.md`
