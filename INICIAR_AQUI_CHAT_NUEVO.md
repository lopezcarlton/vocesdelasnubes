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
14. `POST_IRMA_ADJUDICATION_CHECKPOINT_2026-09-03.md`

Para reconstruir la primera captura post-Irma usar `POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md`.

Para reconstruir específicamente el estado anterior a Irma, usar `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md` y la rama congelada indicada allí.

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

## 5. Alcance activo de COR002 y materiales nuevos

Existe una decisión vigente desde el 3 de septiembre de 2026:

`conocimiento/decisiones/DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN.md`

```text
ACTIVE_LANGUAGE_LEVEL = BEGINNER
ACTIVE_PRIMARY_MODALITY = LISTENING
ACTIVE_BASELINE_VARIETY = JUCHITAN
ACTIVE_LITERACY_TRACK = false
```

Por tanto, la fase actual desarrolla **materiales de escucha para principiantes en la variante de Juchitán**.

Esto no niega futuras líneas de lectoescritura, niveles avanzados o trabajo multivarietal; simplemente las mantiene fuera del alcance activo actual.

G/P continúa como arquitectura de trabajo revisable. Las fronteras exactas P1–P5 no están cerradas y `BL-021` permanece abierto. No derivar una tabla definitiva de P a partir de bibliografía general sin adjudicación explícita.

## 6. Públicos escolares

Sigue vigente:

`conocimiento/decisiones/DEC-PUBLICOS-ESCOLARES-MULTIETARIOS.md`

Voces de las Nubes debe diseñarse para **públicos escolares diferenciados**, además de otros aprendices. La educación secundaria técnica es el primer anclaje institucional prioritario por la relación real de Casa de las Ciencias de Oaxaca con ese nivel, pero no es público exclusivo.

Durante la fase actual, la segmentación escolar se investiga dentro del alcance común de **principiantes + escucha + Juchitán**.

```text
AGE_GROUP != LANGUAGE_LEVEL
SCHOOL_GRADE != G_LEVEL
SCHOOL_GRADE != P_LEVEL
BEGINNER_LISTENING != ONE_AGE_GROUP
```

Las bandas concretas de edad y adaptaciones permanecen abiertas en `BL-023`.

## 7. Memorización — deuda pedagógica prioritaria

La memoria y la recuperación de expresiones forman parte deliberada del método actual, pero el proyecto no considera suficiente la repetición mecánica.

`BL-025` debe justificar pedagógicamente la función de la memorización frente a la crítica al tedio y la pasividad presente en el entorno docente constructivista de Casa de las Ciencias.

Mapa inicial:

`informes/MEMORIZATION_PEDAGOGICAL_JUSTIFICATION_RESEARCH_MAP_v0_1.md`

Distinciones vigentes de investigación:

```text
ROTE_RESTUDY != RETRIEVAL_PRACTICE
RETRIEVAL_PRACTICE != SPACED_PRACTICE
MEMORIZATION != COMPLETE_PEDAGOGY
RETENTION_EFFECT != LEARNER_ENGAGEMENT
```

No presentar todavía como resuelta la compatibilidad con el constructivismo. Debe fundamentarse con bibliografía, diseño real del método y pruebas con aprendices.

## 8. Reunión con Irma Pineda

Las fuentes disponibles son:

- `conocimiento/fuentes/SRC-IRMA-PINEDA-REUNION-2026-09-02.md`
- `conocimiento/fuentes/SRC-IRMA-PINEDA-NOTAS-LINGUISTICAS-2026-09-03.md`
- `conocimiento/fuentes/SRC-EMILIANO-DECISIONES-ALCANCE-2026-09-03.md`

Las dos primeras son reconstrucciones posteriores de la reunión, no transcripción literal.

```text
MEMORIA_POSTERIOR != CITA_LITERAL
SUGERENCIA_DE_IRMA != DECISION_AUTOMATICA
IDEA_DE_EMILIANO != AFIRMACION_DE_IRMA
```

La lista de palabras y observaciones lingüísticas de Irma **ya fue capturada**. Incluye materiales sobre trato social, `Lia`/`dxe`, `bitaagu'`/`biseegu'`, `ñaa`/`la'dxi`, el neologismo `bichuga le` y `qui`/`qué`.

No todas esas notas tienen el mismo estado. Ver `HALL-0013` a `HALL-0019`.

## 9. Negación `qui` / `qué` — equivalencia cerrada

La equivalencia queda adoptada mediante:

- `SRC-NEGACION-QUI-QUE-ATESTACIONES-2026-09-03`
- `HALL-0019`
- `DEC-NEGACION-QUI-QUE-EQUIVALENTES`

```text
QUI_QUE_NEGATION_EQUIVALENT = true
MARK_OTHER_FORM_AS_INCORRECT_BY_VARIANT_ALONE = false
DIALECT_DISTRIBUTION = OPEN
HISTORICAL_RELATION = OPEN
PROJECT_EDITORIAL_DEFAULT = NOT_DECIDED_HERE
```

No reabrir la equivalencia por defecto. Sí pueden seguir investigándose distribución, frecuencia, historia y preferencia editorial.

## 10. Norma de escritura de 2016 y ortografía contemporánea

Emiliano confirmó que la **`Norma del sistema de escritura de la lengua zapoteca` de 2016** es el documento al que Irma se refería como versión reciente del sistema de escritura utilizada por autores contemporáneos.

```text
NORMA_2016_IDENTIFIED_AS_IRMA_REFERENCE = true
NORMA_2016_FULL_TEXT_IN_PROJECT = false
```

Entidades principales:

- `HALL-0010`
- `HALL-0021`
- `SRC-DICTIONARIA-NORMA-ESCRITURA-2016-REFERENCE`
- `SRC-INALI-INFORME-LOGROS-2016-NORMA-PLANICIE-COSTERA`

`BL-024` ya no pregunta qué documento es: debe **localizar e ingerir el texto completo de la Norma 2016**, reconstruir su procedencia y adjudicar cómo modifica la política de fuentes ortográficas contemporáneas.

El **Alfabeto Popular de 1956** queda como antecedente histórico fundamental. Emiliano ya descargó una copia, todavía no incorporada al repositorio.

No asumir:

```text
CONTEMPORARY_AUTHOR_TEXT -> AUTOMATIC_CORRECTION_RULE
NORMA_REFERENCE -> FULL_NORM_CONTENT_KNOWN
```

## 11. Variedades

El baseline activo queda reafirmado:

```text
CURRENT_BASELINE = JUCHITAN
ESPINAL_RESEARCH = ALLOWED
MULTIVARIETAL_MERGE = false
```

La investigación dialectológica sobre El Espinal y otras localidades puede continuar, pero no debe mezclar formas con el corpus juchiteco sin metadatos y decisión explícita.

## 12. Bibliografía SIL / ILV

La página de publicaciones de SIL México para zapoteco del Istmo ya fue cartografiada en:

- `conocimiento/fuentes/SRC-SIL-MEXICO-CATALOGO-ZAPOTECO-ISTMO-2026-09-03.md`
- `informes/SIL_ISTHMUS_ZAPOTEC_BIBLIOGRAPHY_SCAN_v0_1.md`

Antes de asignar nuevos `BIB###`, deduplicar contra la hoja bibliográfica operativa. El catálogo sirve para localizar fuentes; no confiere el mismo peso epistemológico a todas ellas.

## 13. BIB065 / Bueno Holle

La fuente registrada dentro del Sistema de Conocimiento es `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md`.

Los artefactos BIB065 bajo `dispositivo/` pueden reconstruir genealogía y candidatos, pero **no deben promoverse automáticamente** a pedagogía, teoría o metodología. Cuando sea necesario incorporar resultados posteriores de la lectura, volver a la obra original y adjudicarlos dentro de Voces de las Nubes.

`BL-022` conserva abierta la investigación sobre relevancia pedagógica de sus capas analíticas finas.

## 14. Estado pre-Irma congelado

```text
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

Ver `PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md`.

Esa referencia sirve para comparar cambios y no debe confundirse con política vigente.

## 15. Ruta inmediata

1. profundizar `BL-025` hasta formular una justificación pedagógica de la memoria que pueda discutirse con docentes;
2. investigar `BL-023` dentro de principiantes + escucha antes de fijar bandas escolares;
3. localizar el texto completo de la Norma 2016 y adjudicar `BL-024` antes de cambiar reglas ortográficas del Corrector;
4. corroborar selectivamente las notas lingüísticas de Irma que siguen en `pendiente_de_validacion`;
5. continuar investigación de corpus natural, co-diseño, dificultad auditiva, P y BIB065 sin convertir hipótesis en políticas;
6. publicar estados aprobados mediante commits identificables;
7. permitir que el dispositivo consuma sólo conocimiento adjudicado mediante `KNOWLEDGE_SOURCE_COMMIT`.

## 16. Trabajo técnico

No cargar por defecto el estado técnico para conversaciones sobre bibliografía, pedagogía, corpus o metodología humana.

Cuando la tarea sea desarrollar Analyzer, Corrector, Tutor, Generator, runtime, pruebas o migración, cambiar explícitamente al punto de entrada:

`dispositivo/REENTRY_TECNICO.md`
