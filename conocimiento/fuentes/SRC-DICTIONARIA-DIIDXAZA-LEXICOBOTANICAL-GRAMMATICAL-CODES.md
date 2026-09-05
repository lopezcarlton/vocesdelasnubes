# SRC-DICTIONARIA-DIIDXAZA-LEXICOBOTANICAL-GRAMMATICAL-CODES

```yaml
id: SRC-DICTIONARIA-DIIDXAZA-LEXICOBOTANICAL-GRAMMATICAL-CODES
tipo: fuente_digital_documental
titulo: "La Ventosa Diidxazá Lexico-Botanical Dictionary — grammatical category legend"
autor_o_participantes:
  - Gabriela Pérez Báez
  - Terrence Kaufman
fecha: s.f.
fecha_de_consulta: 2026-09-05
ubicacion: "https://dictionaria.clld.org/contributions/diidxaza"
descripcion: >
  Contribución pública de Dictionaria que explicita la leyenda de abreviaturas de
  categorías gramaticales usada para entradas verbales del diidxazá y remite a
  Pérez Báez 2015 para el sistema de valencia.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
```

## Uso autorizado en Voces

La sección de categorías gramaticales define explícitamente, entre otras, las etiquetas:

```text
vA:caus = verbo de clase A, causativo
vB:caus = verbo de clase B, causativo
vA:i    = verbo de clase A, intransitivo
vA:t    = verbo de clase A, transitivo
vB:i    = verbo de clase B, intransitivo
vC:i    = verbo de clase C, intransitivo
vC:t    = verbo de clase C, transitivo
vD:i    = verbo de clase D, intransitivo
vD:t    = verbo de clase D, transitivo
```

La contribución señala además que la información sobre valencia del diidxazá debe consultarse en Pérez Báez 2015 y en el trabajo relacionado sobre clases verbales.

## Relación con el diccionario general

El derivado técnico `DIC_VERB_2385_v0_1.csv`, procedente del diccionario general de Dictionaria, conserva cadenas del mismo sistema de análisis como `vB:caus`, `vC:i` y `vC:t`. La leyenda de esta contribución permite interpretar esas cadenas cuando coinciden literalmente con una categoría definida aquí.

Esto no autoriza a interpretar abreviaturas o modificadores que la leyenda consultada no define explícitamente. En particular:

```text
DEFINED_CODE_MEANING = REUSABLE_WHEN_LITERAL_CODE_MATCHES
UNDEFINED_MODIFIER != INFERRED_VALENCY_MEANING
vers = UNADJUDICATED_IN_THIS_SOURCE_PASS
LEXICAL_CODE != V1_V2_V3_C1_C2_C3_C4_GROUP_ASSIGNMENT
```

## Restricción

La etiqueta léxica causativa/transitiva/intransitiva es información del registro. No basta por sí sola para reconstruir la relación derivativa con una raíz básica, asignar un grupo de Pérez Báez 2015, generar una causativa ni corregir una forma de superficie.
