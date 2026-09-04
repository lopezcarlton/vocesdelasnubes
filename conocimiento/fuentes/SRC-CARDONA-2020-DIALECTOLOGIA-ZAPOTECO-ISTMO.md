# SRC-CARDONA-2020-DIALECTOLOGIA-ZAPOTECO-ISTMO

```yaml
id: SRC-CARDONA-2020-DIALECTOLOGIA-ZAPOTECO-ISTMO
tipo: fuente_bibliografica
bib_id: BIB063
titulo: "Dialectología del zapoteco del istmo"
autor_o_participantes:
  - Pedro David Cardona Fuentes
fecha: 2020-01-13
institucion: "Universidad Autónoma de Querétaro"
programa: "Doctorado en Lingüística, Facultad de Lenguas y Letras"
extension: "199 páginas"
ubicacion: "Repositorio Institucional UAQ — handle 123456789/1926"
descripcion: >
  Tesis doctoral dedicada a definir zonas dialectales del zapoteco del Istmo mediante
  documentación en nueve municipios, análisis de isoglosas fonológicas y léxicas y
  análisis dialectométrico.
nivel_de_fuente: primaria
disponibilidad: acceso_abierto
licencia_registrada_en_repositorio: CC_BY_NC_ND_4_0
estado_de_acceso: disponible
estado_de_ingesta: semantic_backfill_p1_dialectology_sufficient_2026-09-04
```

`BIB063` está confirmado por la hoja bibliográfica maestra reconciliada el 2026-09-03.

## Memoria persistente de lectura — P1 2026-09-04

### Diseño y alcance

La investigación trabajó en nueve municipios y combinó:

- isoglosas de variación fonológica;
- isoglosas de variación léxica;
- agrupamiento jerárquico;
- sistemas de nodos de similitud.

El objetivo fue delimitar relaciones dialectales, no fijar una ortografía normativa.

### Núcleos de alta similitud y transición

`HALL-0179`:

- San Blas Atempa–Tehuantepec = núcleo de alta similitud;
- Ixtaltepec–Ixtepec = núcleo de alta similitud;
- Juchitán–Xadani = núcleo de alta similitud;
- El Espinal, Unión Hidalgo y Comitancillo = zonas de transición en el análisis reportado.

```text
DIALECT_ZONE != INTERNALLY_UNIFORM_VARIETY
TRANSITION != FREE_FORM_INTERCHANGEABILITY
LOCALITY_METADATA = REQUIRED
```

El resultado es especialmente importante para el proyecto porque impide reducir El Espinal a “Juchitán con otras palabras”. Una proximidad dialectal puede justificar comparación; no autoriza sustitución automática de formas.

### Relación con la síntesis de 2025

Cardona & Vicente (2025) reutilizan estos resultados en una clasificación amplia sur/centro/norte y adscriben los municipios transicionales a zonas operativas más grandes.

→ `HALL-0180`.

```text
BROAD_ZONE_LABEL != ERASE_TRANSITION_STATUS
```

### Variación fonológica con relevancia ortográfica

Los datos de la tesis sustentan las isoglosas que Cardona & Vicente 2025 discuten para fonaciones laringizadas/rearticuladas y alternancias segmentales.

→ `HALL-0181`.

No extrapolar una isoglosa a cada palabra o cada hablante sin evidencia local.

## Uso para Voces

```text
JUCHITAN = PRIORITY_VARIETY
EL_ESPINAL != JUCHITAN_ALIAS
LOCAL_VARIANT != ERROR
DIALECTOMETRIC_SIMILARITY != ORTHOGRAPHIC_DECISION
```

Cada fuente, texto, audio y validación debe conservar localidad y, cuando sea pertinente, zona amplia/estatus transicional como metadatos distintos.

## Estado

```text
CARDONA2020_P1_DIALECTOLOGY_BACKFILL = SUFFICIENT
EXHAUSTIVE_ISOGLOSS_INGESTA = false
REOPEN_FOR = TARGETED_VARIANT | LOCALITY_COMPARISON | EXACT_ISOGLOSS | ORTHOGRAPHIC_IMPLICATION
```
