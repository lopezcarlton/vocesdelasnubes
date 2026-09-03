# INICIAR AQUÍ — VOCES DE LAS NUBES

## Objetivo

Este archivo es el punto de reentrada general para continuar **Voces de las Nubes** desde `lopezcarlton/vocesdelasnubes`, rama `main`, sin depender de memoria de conversaciones anteriores.

Este reentry reconstruye **el Sistema de Conocimiento**. No carga por defecto el runtime ni el estado técnico del dispositivo.

Para trabajo explícitamente técnico usar `dispositivo/REENTRY_TECNICO.md` mientras la separación física siga pendiente.

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
13. `conocimiento/AUDIO.md`
14. `conocimiento/BIBLIOGRAFIA.md`
15. `conocimiento/fuentes/README.md`

Después, leer las `SRC`, `HALL`, `DEC`, `VAL`, `TEO` u otras entidades pertinentes a la pregunta concreta. Si una ruta no existe, no inventarla ni sustituirla silenciosamente.

Los checkpoints de `archivo/checkpoints/` son **históricos y opcionales**. Se consultan sólo para reconstruir un estado anterior o comparar cambios; no forman parte de la lectura obligatoria del estado vigente.

## 2. Fuente de autoridad

`conocimiento/` y los documentos constitucionales contienen el Sistema de Conocimiento de Voces de las Nubes.

Las vistas —`PEDAGOGIA.md`, `TEORIA.md`, `CORPUS.md`, `METODOLOGIA.md`, etc.— sintetizan conocimiento vigente; no sustituyen las fuentes, hallazgos, validaciones y decisiones que deben sustentar sus afirmaciones.

Una `DEC` vigente gobierna las vistas dentro de su alcance, subordinada a la Arquitectura, la Jerarquía de Verdad, las Reglas de Actualización y los principios válidos.

### Acceso a fuentes

`conocimiento/fuentes/` es la puerta canónica de acceso a gramáticas, vocabularios, artículos, corpus, diccionarios, normas, sesiones y otras fuentes.

Una fuente puede estar registrada mediante `SRC-*` aunque el archivo original viva fuera del repositorio público por derechos, tamaño o condiciones de acceso. El `SRC` debe permitir identificar y localizar el original sin ejecutar el dispositivo.

```text
VOCES_CAN_RESOLVE_SOURCE_WITHOUT_DEVICE = true
DEVICE_OUTPUT != SOURCE
```

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

Una herramienta puede servir como localizador, comparador o detector de contradicciones. Una salida técnica no se convierte por ello en evidencia. Si un descubrimiento ocurre durante trabajo técnico:

```text
resultado técnico / candidato
-> volver a la fuente original
-> registrar o localizar SRC en Voces
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

## 10. Norma de escritura 2016

Emiliano confirmó que la Norma 2016 es el documento al que Irma se refería como la versión más reciente del Alfabeto Popular usada por autores contemporáneos.

Fuentes actuales:

- `SRC-DICTIONARIA-NORMA-ESCRITURA-2016-REFERENCE`
- `SRC-INALI-INFORME-LOGROS-2016-NORMA-PLANICIE-COSTERA`

La referencia está identificada; el manuscrito completo todavía debe localizarse (`BL-024`). No reconstruir una supuesta norma completa a partir de citas secundarias.

## 11. Fuentes lingüísticas centrales accesibles sin dispositivo

Entre las fuentes ya resolubles directamente desde Voces están:

- `SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`
- `SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO`
- `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY`
- `SRC-BUENO-HOLLE-2019`
- `SRC-PEREZ-BAEZ-CATA-BUENO-HOLLE-2015-XNEZA`
- `SRC-PEREZ-BAEZ-2015-VALENCE-CHANGING-JUCHITAN`
- `SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES`
- `SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS`

Los derivados históricos que aparezcan en `dispositivo/` pueden utilizarse para localizar material, pero no sustituyen estas fuentes.

## 12. Estado bibliográfico

La hoja bibliográfica maestra sigue siendo el registro operativo de asignación de `BIB###`. No inventar IDs BIB para fuentes nuevas. `BL-026` permanece abierto hasta reconciliar la hoja con los `SRC-*` actuales.

## 13. Qué sigue

Mientras la arquitectura permanece congelada, las líneas sustantivas activas son:

- localizar y estudiar la Norma 2016;
- justificar pedagógicamente la memoria y su relación con recuperación, espaciamiento, transferencia y tedio;
- definir segmentación por edades dentro de principiantes + escucha;
- continuar literatura lingüística y corpus oral de Juchitán;
- corroborar selectivamente las nuevas atestaciones de Irma;
- completar la separación física del dispositivo cuando exista el repositorio técnico destino.

No crear nuevas capas arquitectónicas por defecto. Una deuda nueva debe resolverse dentro de la arquitectura vigente siempre que ésta ya tenga un lugar apropiado.
