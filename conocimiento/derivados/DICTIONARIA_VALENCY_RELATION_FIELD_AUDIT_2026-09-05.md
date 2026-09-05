# Auditoría dirigida de campos de relaciones de valencia en Dictionaria — 2026-09-05

**Rol:** `RECOVERY_AUDIT / TECHNICAL_SOURCE_INSPECTION / NOT_LINGUISTIC_NEGATIVE_EVIDENCE`

## Fuente inspeccionada

```text
repository = dictionaria/didxazageneral
commit = 76c22cf30c23d8f4bc5c83c11013a8cb24fe0f85
raw_sqlite = raw/jzd.dictionaria.sqlite
sqlite_sha256 = e4d7dca563e01b5bdf7821326962ea684e6539ea2628724bfd52cf14e6fb0e1f
inspection_date = 2026-09-05
```

La inspección se ejecutó sobre un checkout limpio del commit fijado y abrió el SQLite en modo de sólo lectura.

## Pregunta

El generador oficial `cldfbench_didxazageneral.py` contiene convertidores para:

```text
ACT+X -> More_Active
ACT-X -> Less_Active
CAUSX -> Causative
VERSX -> Versive
```

La auditoría verificó si esos campos, o campos de relación equivalentes, estaban realmente poblados en el snapshot fuente.

## Resultado

No hay filas de `sense_field` con `ACT+X`, `ACT-X`, `CAUSX` ni `VERSX` en este snapshot.

Inventario completo de `field_id` realmente presente:

```text
AND      38
CMP    1850
CTF     148
ETYMX  1646
FUT     439
HAB    2090
POT    1690
PRF       7
PRG     489
PUB_DEF 9046
SEMFX   9012
STA       1
```

```text
sense_field_rows = 26456
distinct_present_field_ids = 12
relation_like_present_fields = 0
```

La tabla de metadatos `field` declara únicamente esos mismos tipos pertinentes; tampoco contiene un tipo alternativo para díadas, tríadas, raíz básica, valencia, causativo o miembro más/menos activo.

## Qué sí está poblado

Las entradas conservan códigos `pos_id` como `vA:caus`, `vA:i`, `vA:t` y otros modificadores. La semántica de `:caus`, `:i` y `:t` ya fue adjudicada por separado en `HALL-0192`. Estos códigos son propiedades de entradas individuales y **no constituyen por sí mismos enlaces entre miembros de una relación derivativa**.

## Consecuencia

```text
GENERATOR_SUPPORT_FOR_RELATION_FIELDS != POPULATED_RELATION_DATA
NO_RELATION_FIELD_ROWS_IN_PINNED_SNAPSHOT != LINGUISTIC_ABSENCE_OF_RELATIONS
ENTRY_LEVEL_CAUSATIVE_CODE != BASIC_TO_CAUSATIVE_LINK
```

Por tanto, las relaciones concretas `BASIC ↔ CAUSATIVE`, `LESS_ACTIVE ↔ BASIC ↔ MORE_ACTIVE` y la pertenencia específica a V1–V3/C1–C4 no deben reconstruirse desde este SQLite por semejanza formal. Para esas relaciones se vuelve a la fuente lingüística pertinente, en este caso Pérez Báez 2015.

## Reproducibilidad

La inspección no modificó ni redistribuyó el SQLite fuente. Los scripts temporales usados para la recuperación se retiran de la rama antes de integrar el conocimiento canónico; este informe conserva la pregunta, el commit, el hash, el inventario y el resultado necesarios para no repetir la exploración.
