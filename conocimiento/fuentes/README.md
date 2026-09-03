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
