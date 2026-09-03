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
7. `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`
8. `conocimiento/PEDAGOGIA.md`
9. `conocimiento/METODOLOGIA.md`
10. `conocimiento/CORPUS.md`
11. `conocimiento/VALIDACION.md`
12. `conocimiento/TEORIA.md`
13. `conocimiento/BIBLIOGRAFIA.md`
14. `POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md`

Para reconstruir específicamente el estado anterior a Irma, usar después `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md` y la rama congelada indicada allí.

Leer las `SRC`, `HALL`, `DEC`, `VAL`, `TEO` u otras entidades pertinentes a la pregunta concreta. Si una ruta no existe, no inventarla ni sustituirla silenciosamente.

## 2. Fuente de autoridad

`conocimiento/` y los documentos constitucionales contienen el Sistema de Conocimiento de Voces de las Nubes.

Las vistas —`PEDAGOGIA.md`, `TEORIA.md`, `CORPUS.md`, `METODOLOGIA.md`, etc.— sintetizan conocimiento vigente; no sustituyen las fuentes, hallazgos, validaciones y decisiones que deben sustentar sus afirmaciones.

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

Las fronteras exactas G1–G5 y P1–P5 no están cerradas. No derivar una tabla definitiva de P a partir de bibliografía general sin adjudicación explícita.

La idea de COR002 como material básico para principiantes sigue siendo una hipótesis de trabajo fuerte para discusión, no una especificación irrevocable.

## 6. Públicos escolares — cambio vigente post-Irma

Desde el 2 de septiembre de 2026 existe una decisión nueva y vigente:

`conocimiento/decisiones/DEC-PUBLICOS-ESCOLARES-MULTIETARIOS.md`

Voces de las Nubes debe diseñarse para **públicos escolares diferenciados**, además de personas con transmisión intergeneracional interrumpida.

La educación secundaria técnica es el primer anclaje institucional prioritario por la relación real de Casa de las Ciencias de Oaxaca con ese nivel, pero no es público exclusivo.

```text
AGE_GROUP != LANGUAGE_LEVEL
SCHOOL_GRADE != G_LEVEL
SCHOOL_GRADE != P_LEVEL
```

Las bandas concretas de edad, perfiles escolares y metodologías permanecen abiertas en `BL-023`.

## 7. Reunión con Irma Pineda

La reconstrucción disponible está en:

`conocimiento/fuentes/SRC-IRMA-PINEDA-REUNION-2026-09-02.md`

Es memoria posterior de Emiliano, no transcripción literal.

```text
MEMORIA_POSTERIOR != CITA_LITERAL
SUGERENCIA_DE_IRMA != DECISION_AUTOMATICA
IDEA_DE_EMILIANO != AFIRMACION_DE_IRMA
```

La lista exacta de palabras y ejemplos lingüísticos de la reunión sigue pendiente.

Hasta ahora sólo se promovió la decisión de públicos escolares. Las demás líneas —Alfabeto Popular y escritores contemporáneos, `qui/qué`, El Espinal, corpus espontáneo, co-diseño, progresión auditiva e instituciones— permanecen en distintos estados de investigación o candidatura según `POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md`.

## 8. BIB065 / Bueno Holle

La fuente registrada dentro del Sistema de Conocimiento es `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md`.

Los artefactos BIB065 bajo `dispositivo/` pueden reconstruir genealogía y candidatos, pero **no deben promoverse automáticamente** a pedagogía, teoría o metodología. Cuando sea necesario incorporar resultados posteriores de la lectura, volver a la obra original y adjudicarlos dentro de Voces de las Nubes.

`BL-022` conserva abierta la investigación sobre relevancia pedagógica de sus capas analíticas finas.

## 9. Ortografía post-Irma

`BL-024` investiga la versión vigente del Alfabeto Popular y el posible uso de literatura contemporánea como nueva capa de evidencia ortográfica.

No asumir:

```text
CONTEMPORARY_AUTHOR_TEXT -> AUTOMATIC_CORRECTION_RULE
qui == qué -> GLOBAL_EXECUTABLE_RULE
```

Primero localizar fuentes, conservar variedad/género/edición/procedencia y adjudicar.

## 10. Variedades

El foco vigente no se ha cambiado silenciosamente:

```text
CURRENT_FOCUS = JUCHITAN
ESPINAL_EXPANSION = CANDIDATE_RESEARCH_LINE
MULTIVARIETAL_ARCHITECTURE = NOT_YET_ADOPTED
```

No mezclar formas de Juchitán, El Espinal, Unión Hidalgo u otras localidades sin metadatos y decisión explícita.

## 11. Estado pre-Irma congelado

```text
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

Ver `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md`.

Esa referencia sirve para comparar cambios y no debe confundirse con política vigente.

## 12. Ruta inmediata

1. completar la captura de la reunión cuando Emiliano aporte la lista de palabras/ejemplos;
2. investigar `BL-023` con docentes, estudiantes y bibliografía antes de fijar bandas escolares;
3. localizar el documento contemporáneo de escritura y adjudicar `BL-024` antes de modificar el Corrector;
4. evaluar modelo de co-diseño y relación corpus natural → adaptación pedagógica sin promoverlos por defecto;
5. mantener abierta la investigación de dificultad auditiva, P y BIB065;
6. publicar estados aprobados mediante commits identificables;
7. permitir que el dispositivo consuma sólo conocimiento adjudicado mediante `KNOWLEDGE_SOURCE_COMMIT`.

## 13. Trabajo técnico

No cargar por defecto el estado técnico para conversaciones sobre bibliografía, pedagogía, corpus o metodología humana.

Cuando la tarea sea desarrollar Analyzer, Corrector, Tutor, Generator, runtime, pruebas o migración, cambiar explícitamente al punto de entrada:

`dispositivo/REENTRY_TECNICO.md`
