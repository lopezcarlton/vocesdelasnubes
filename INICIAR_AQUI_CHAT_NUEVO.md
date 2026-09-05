# INICIAR AQUÍ — VOCES DE LAS NUBES

**Estado:** `ACTIVE_REENTRY / LAZY_TARGETED_LOADING`  
**Actualizado:** 2026-09-05

## Objetivo

Este archivo es el punto de reentrada general para continuar **Voces de las Nubes** desde `lopezcarlton/vocesdelasnubes`, rama `main`, sin depender de memoria de conversaciones anteriores.

La reentrada debe ser **dirigida por la tarea**. No se reconstruye todo el repositorio antes de cada consulta.

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
VOCES = AUTHORITY_FOR_KNOWLEDGE
```

Para trabajo explícitamente técnico usar el repositorio separado `lopezcarlton/didxaza-dispositivo`, comenzando por su `REENTRY_TECNICO.md`. Una consulta lingüística, pedagógica, metodológica, bibliográfica o de corpus no debe cargar el dispositivo por defecto.

---

# 1. Reentrada mínima

Al iniciar un chat nuevo:

1. leer **este archivo**;
2. identificar el tipo de tarea;
3. buscar y abrir únicamente las entidades y vistas pertinentes;
4. ampliar la lectura sólo si aparece una contradicción, una dependencia de autoridad o una necesidad concreta de adjudicación.

No existe ya una lista obligatoria de quince documentos para toda consulta.

Los checkpoints de `archivo/checkpoints/` son históricos y opcionales. Se consultan sólo para reconstruir un estado anterior o comparar cambios.

---

# 2. Carga según tipo de tarea

## 2.1 Consulta de conocimiento ya registrado

Ejemplos:

- “¿Cuántos tonos reconoce el análisis actual?”
- “¿Qué sabemos sobre `qui/qué`?”
- “¿Qué clase verbal tiene X?”
- “¿Qué dice el proyecto sobre `xh/x`?”

Ruta:

```text
PREGUNTA
-> buscar HALL / TEO / DEC / VAL pertinentes
-> localizar SRC relacionado cuando haga falta provenance o cobertura
-> consultar vista temática sólo si ayuda a sintetizar
-> responder
```

Los `TEO-*` materializados se encuentran en `conocimiento/aplicaciones_teoricas/`. Deben consultarse cuando la pregunta no sea simplemente “qué dice la fuente”, sino **cómo interpreta o utiliza Voces una propuesta bibliográfica**.

Para una consulta ordinaria **no es necesario abrir de nuevo el PDF, libro, audio o fuente original** cuando el conocimiento requerido ya esté suficientemente registrado y adjudicado en Voces.

Tampoco es necesario leer por defecto:

- `02_BACKLOG.md`;
- todas las vistas temáticas;
- toda la bibliografía;
- todos los `SRC`;
- todas las aplicaciones teóricas;
- el repositorio del dispositivo.

## 2.2 Consulta de una fuente ya estudiada

Un `SRC-*` puede conservar, además de la identidad de la fuente:

- estado y cobertura de lectura;
- secciones, páginas, tablas o ejemplos trabajados;
- contenido fuente parafraseado de manera trazable;
- sistema de notación u ortografía usado por la obra;
- límites de interpretación y redistribución;
- relaciones con HALL/TEO/DEC y derivados documentales pertinentes.

Esta información sirve como **memoria persistente de lectura y acceso rápido**. Su función es evitar releer fuentes completas para preguntas ya cubiertas.

```text
ROUTINE_SOURCE_QUERY -> SRC + KNOWLEDGE_ENTITIES
FULL_SOURCE_REREAD_BY_DEFAULT = false
```

Si la consulta exige una precisión que no quedó capturada, una cita exacta, una cuestión fuera de la cobertura registrada o resolver una contradicción, abrir únicamente el pasaje pertinente de la fuente original.

## 2.3 Nueva adjudicación o promoción de conocimiento

Si se va a crear o modificar un `HALL`, `TEO`, `VAL`, `DEC`, `PRIN`, una vista canónica o cualquier afirmación con nueva autoridad, entonces sí aplicar el procedimiento completo de actualización.

Lectura mínima para ese trabajo:

1. `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`;
2. `01_JERARQUIA_DE_VERDAD.md`;
3. `03_REGLAS_DE_ACTUALIZACIÓN.md`;
4. `conocimiento/decisiones/DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO.md` cuando intervenga un sistema derivado;
5. las entidades ya existentes sobre el mismo asunto;
6. la fuente original y **el pasaje pertinente** que sustenta la nueva adjudicación;
7. la vista temática afectada, si corresponde.

Se conserva la garantía:

```text
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
```

Una lectura previa bien documentada acelera la localización, pero una formulación técnica antigua no sustituye la verificación del pasaje cuando se está promoviendo conocimiento nuevo.

## 2.4 Cambio estructural, epistemológico o de gobernanza

Sólo para cambios que afecten la arquitectura, jerarquía de verdad, reglas de actualización, tipos de entidad, autoridad entre repositorios o gobernanza general, leer además:

- `README.md`;
- `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`;
- `01_JERARQUIA_DE_VERDAD.md`;
- `03_REGLAS_DE_ACTUALIZACIÓN.md`;
- `02_BACKLOG.md` cuando la deuda estructural sea parte del problema;
- decisiones y principios directamente relacionados.

No modificar documentos constitucionales para resolver un caso aislado.

## 2.5 Trabajo por dominio

Abrir sólo la vista temática correspondiente y sus entidades de respaldo:

- pedagogía → `conocimiento/PEDAGOGIA.md`;
- metodología → `conocimiento/METODOLOGIA.md`;
- corpus → `conocimiento/CORPUS.md`;
- validación → `conocimiento/VALIDACION.md`;
- teoría → `conocimiento/TEORIA.md` y, sólo cuando haga falta la aplicación bibliográfica concreta, `conocimiento/aplicaciones_teoricas/`;
- audio → `conocimiento/AUDIO.md`;
- bibliografía → `conocimiento/BIBLIOGRAFIA.md` y `conocimiento/fuentes/README.md`.

Una tarea no debe cargar vistas de otros dominios salvo dependencia concreta.

---

# 3. Fuente de autoridad

`conocimiento/` y los documentos constitucionales contienen el Sistema de Conocimiento de Voces de las Nubes.

Las vistas —`PEDAGOGIA.md`, `TEORIA.md`, `CORPUS.md`, `METODOLOGIA.md`, etc.— sintetizan conocimiento vigente; no sustituyen las fuentes, hallazgos, validaciones y decisiones que deben sustentarlas.

Una `DEC` vigente gobierna las vistas dentro de su alcance, subordinada a la Arquitectura, la Jerarquía de Verdad, las Reglas de Actualización y los principios válidos.

`conocimiento/fuentes/` es la puerta canónica de acceso a gramáticas, vocabularios, artículos, corpus, diccionarios, normas, sesiones y otras fuentes.

`conocimiento/aplicaciones_teoricas/` conserva las entidades `TEO-*`: no son fuentes nuevas ni decisiones del proyecto, sino la capa explícita que separa **lo que una fuente propone** de **cómo Voces la interpreta o aplica**.

Una fuente puede estar registrada mediante `SRC-*` aunque el payload original viva fuera del repositorio por derechos, tamaño o condiciones de acceso.

```text
SRC_RECORD = CANONICAL_SOURCE_IDENTITY
TEO_RECORD = PROJECT_INTERPRETATION_OF_BIBLIOGRAPHIC_PROPOSAL
PAYLOAD_MAY_LIVE_OUTSIDE_REPOSITORY = true
DEVICE_OUTPUT != SOURCE
```

El repositorio puede conservar hechos lingüísticos parafraseados, coordenadas de recuperación, cobertura de lectura y derivados documentales permitidos sin almacenar necesariamente el PDF original.

---

# 4. Recuperación de conocimiento pre-split

Si una pregunta sugiere que conocimiento estudiado antes de la separación no quedó promovido a Voces, consultar de forma excepcional:

`informes/KNOWLEDGE_RECOVERY_INDEX_PRE_SPLIT_2026-09-03.md`

Ese índice sirve para localizar temas, IDs y coordenadas. No es autoridad.

```text
RECOVERY_INDEX_AS_COORDINATES = allowed
RECOVERY_INDEX_AS_CLAIM_SUMMARY = not_authoritative
```

Si el índice no cubre el artefacto pertinente, puede consultarse `lopezcarlton/didxaza-dispositivo` **sólo como recuperación histórica** para encontrar la fuente, regla, tabla, registry o coordenada que quedó atrapada en un derivado técnico.

La ruta correcta es:

```text
TECHNICAL_RECOVERY
-> IDENTIFY ORIGINAL SRC / SOURCE COORDINATE
-> VERIFY SOURCE_PASSAGE IF NEW_ADJUDICATION_IS_NEEDED
-> PROMOTE_OR_CORRECT_IN_VOCES
-> DEVICE_LATER_CONSUMES_APPROVED_KNOWLEDGE
```

No convertir runtime, SQLite, JLC, registry, Analyzer, Tutor o Generator en autoridad lingüística.

---

# 5. Frontera con el dispositivo

El dispositivo y cualquier futura herramienta o repositorio técnico son sistemas derivados.

```text
DERIVED_SYSTEM_MAY_READ = true
DERIVED_SYSTEM_MAY_ANALYZE = true
DERIVED_SYSTEM_MAY_PROPOSE = true
DERIVED_SYSTEM_MAY_CHALLENGE = true

DERIVED_SYSTEM_MAY_ADOPT_KNOWLEDGE = false
DERIVED_SYSTEM_MAY_PROMOTE_CANDIDATE = false
DERIVED_SYSTEM_MAY_WRITE_KNOWLEDGE = false
```

Una consulta normal de Voces no debe reconstruir el estado ejecutable del dispositivo.

Entrar a `lopezcarlton/didxaza-dispositivo` únicamente cuando:

- la tarea sea explícitamente técnica;
- haya que comprobar comportamiento ejecutable;
- se esté recuperando conocimiento pre-split todavía no materializado en Voces.

---

# 6. Invariantes actuales de alta prioridad

Estas reglas son suficientemente importantes para permanecer visibles en la reentrada general.

## COR001

```text
COR001_DEVICE_ROLE = ANALYSIS_TARGET_ONLY
COR001_PROJECT_STATUS = OPEN_MAINTENANCE
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

## Alcance activo de materiales nuevos

La decisión vigente es:

`conocimiento/decisiones/DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN.md`

```text
ACTIVE_LANGUAGE_LEVEL = BEGINNER
ACTIVE_PRIMARY_MODALITY = LISTENING
ACTIVE_BASELINE_VARIETY = JUCHITAN
ACTIVE_LITERACY_TRACK = false
```

## Negación `qui/qué`

La equivalencia está adoptada mediante `HALL-0019` y `DEC-NEGACION-QUI-QUE-EQUIVALENTES`.

```text
QUI_QUE_NEGATION_EQUIVALENT = true
MARK_OTHER_FORM_AS_INCORRECT_BY_VARIANT_ALONE = false
DIALECT_DISTRIBUTION = OPEN
HISTORICAL_RELATION = OPEN
```

## Norma de escritura 2016

La identidad documental está localizada, pero el texto completo sigue pendiente de estudio directo en `BL-024`. No reconstruir la norma completa desde referencias secundarias.

---

# 7. Reglas de rendimiento y recuperación

Para evitar reconstrucciones innecesarias:

```text
SEARCH_TARGETED_FIRST = true
READ_WHOLE_REPOSITORY = false
READ_ALL_VIEWS = false
READ_DEVICE_FOR_NORMAL_KNOWLEDGE_QUERY = false
OPEN_LARGE_DATASET_ONLY_IF_REQUIRED = true
STOP_READING_WHEN_SUFFICIENT_AUTHORITY_IS_FOUND = true
```

En particular:

- buscar primero por concepto, entidad, `SRC`, `HALL`, `TEO` o `DEC`;
- no enumerar árboles completos cuando una búsqueda dirigida pueda localizar el material;
- no abrir CSV grandes, SQLite o artefactos de replay para responder una cuestión ya resuelta en Voces;
- no cargar `02_BACKLOG.md` para una consulta lingüística ordinaria;
- no cargar pedagogía, corpus, audio y metodología simultáneamente salvo que la tarea realmente los cruce.

---

# 8. Bibliografía y nuevos IDs

La hoja bibliográfica maestra conserva la asignación operativa de `BIB###`.

```text
MASTER_BIB_RANGE = BIB001-BIB091
BIB_ID_GAPS = 0
BIB_ID_DUPLICATES = 0
```

No inventar IDs BIB. Toda nueva asignación se incorpora primero a la hoja maestra y después se refleja en el `SRC-*` pertinente.

---

# 9. Regla de simplicidad

No crear nuevas capas arquitectónicas por defecto.

Antes de introducir una nueva entidad, carpeta conceptual o sistema paralelo, comprobar si el problema ya puede resolverse mediante:

- `SRC` para identidad, cobertura y acceso a la fuente;
- `HALL` para afirmaciones atómicas;
- `TEO` para interpretación teórica;
- `VAL` para validación;
- `DEC` para adopción;
- vistas existentes para síntesis;
- derivados técnicos únicamente para ejecución.

```text
NEW_PROBLEM != NEW_ARCHITECTURAL_LAYER
USE_EXISTING_ARCHITECTURE_FIRST = true
```
