# Fuentes

Esta carpeta es la **puerta canónica de acceso a las fuentes** del Sistema de Conocimiento de Voces de las Nubes.

Cada fuente formal se registra con un identificador estable `SRC-*` y conserva, cuando sea posible:

- identidad bibliográfica o documental;
- versión o edición;
- autoría;
- localidad/variedad cuando corresponda;
- ubicación del archivo o dataset;
- estado de acceso;
- hash del archivo disponible para el proyecto;
- licencia o restricciones de redistribución;
- derivados documentales relevantes.

## Fuente no significa archivo público

El repositorio es público. Por tanto, una fuente puede estar registrada aquí aunque el payload original viva en otra ubicación por derechos, tamaño o condiciones de acceso.

```text
SRC_RECORD = CANONICAL_SOURCE_IDENTITY
PAYLOAD_LOCATION = MAY_BE_REPOSITORY_OR_EXTERNAL
PAYLOAD_LOCATION != AUTHORITY
```

Cuando una fuente pueda redistribuirse legalmente, sus materiales o derivados documentales neutrales pueden almacenarse bajo esta carpeta o en una subcarpeta claramente vinculada al `SRC`.

Cuando no pueda redistribuirse, el `SRC` debe indicar dónde se encuentra el original o la copia controlada. No se creará un segundo Sistema de Conocimiento ni una autoridad paralela sólo para almacenar archivos.

## SRC como memoria persistente de lectura

Un `SRC-*` no tiene que limitarse a una ficha bibliográfica mínima. Cuando una fuente ya fue estudiada, puede conservar de forma trazable y compacta:

- `estado_de_lectura`;
- cobertura efectivamente trabajada;
- capítulos, secciones, páginas, tablas o ejemplos usados como coordenadas;
- hechos fuente **parafraseados**, sin confundirlos con decisiones del proyecto;
- sistema de notación, ortografía o transcripción empleado por la obra;
- límites de interpretación;
- restricciones de derechos y redistribución;
- relaciones con `HALL`, `TEO`, `VAL`, `DEC` y derivados documentales pertinentes.

Su función es permitir que una fuente ya estudiada siga siendo consultable sin releer el PDF, libro o dataset completo cada vez.

```text
ROUTINE_QUERY -> SRC + KNOWLEDGE_ENTITIES
FULL_SOURCE_REREAD_BY_DEFAULT = false
NEW_ADJUDICATION -> READ_RELEVANT_SOURCE_PASSAGE
```

### Consulta no equivale a adjudicación

Para responder una pregunta sobre conocimiento ya registrado puede usarse la memoria de lectura del `SRC` y las entidades vigentes relacionadas.

Para **crear o modificar** conocimiento con nueva autoridad (`HALL`, `TEO`, `VAL`, `DEC`, `PRIN` o una vista canónica), debe abrirse el pasaje pertinente de la fuente original conforme a `03_REGLAS_DE_ACTUALIZACIÓN.md`.

```text
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
```

Una extracción técnica antigua puede ayudar a localizar el pasaje; no sustituye esa verificación cuando se promueve conocimiento nuevo.

### Derechos de autor

Acceso público a una fuente no equivale a permiso de redistribución. Para obras sin licencia compatible:

- no guardar el PDF por defecto;
- no reproducir tablas completas ni largos pasajes;
- conservar hechos lingüísticos abstraídos/parafraseados, coordenadas, provenance y límites;
- usar citas breves únicamente cuando sean necesarias y compatibles con el uso permitido.

La memoria persistente de lectura debe reducir la dependencia del payload original **sin convertirse en una copia sustitutiva de la obra**.

## Relación con el dispositivo

Una gramática, vocabulario, corpus, diccionario o dataset documental **no pertenece al dispositivo por haber sido ingerido primero durante su desarrollo**.

El dispositivo puede conservar:

- copias exactas necesarias como fixtures históricos;
- tablas normalizadas;
- índices;
- registries;
- SQLite;
- backfills;
- otras compilaciones ejecutables.

Pero esas representaciones son derivados técnicos. Deben poder rastrearse al `SRC` pertinente y al estado de conocimiento de Voces que las autorizó.

```text
SOURCE_USED_BY_DEVICE != DEVICE_OWNED_KNOWLEDGE
DOCUMENTARY_SOURCE -> SRC
PROJECT_INTERPRETATION -> HALL / TEO / VAL / SUP / DEC
EXECUTABLE_COMPILATION -> DEVICE
```

Si conocimiento bibliográfico previamente estudiado sólo sobrevive dentro de un artefacto técnico pre-split, ese artefacto puede utilizarse como **índice de recuperación**. El objetivo es reconstruir en Voces la identidad, cobertura, coordenadas y entidades de conocimiento pertinentes; no convertir el runtime en autoridad ni crear una nueva capa arquitectónica.
