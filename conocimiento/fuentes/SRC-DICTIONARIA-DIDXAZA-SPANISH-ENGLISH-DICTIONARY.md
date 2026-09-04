# SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY

```yaml
id: SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY
tipo: fuente_digital_documental
bib_id: BIB054
titulo: "Didxazá–Spanish–English Dictionary"
autor_o_participantes:
  - Gabriela Pérez Báez
  - Terrence Kaufman
  - Christian Brendel
fecha: s.f.
fecha_de_consulta: 2026-09-03
ubicacion: "https://dictionaria.clld.org/contributions/didxazageneral"
licencia_sitio: "CC BY 4.0"
descripcion: >
  Diccionario digital de Didxazá compilado a partir de décadas de documentación en
  La Ventosa, Santa María Xadani y Juchitán de Zaragoza, con contribuciones de más de
  veinte hablantes y atribuciones a fuentes publicadas. La versión consultada presenta
  9,012 entradas léxicas. Sus propios compiladores advierten que no debe tratarse como
  autoridad que invalide la diversidad dialectal de los hablantes.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
```

## Identidad bibliográfica

`BIB054` está confirmado por la hoja bibliográfica maestra reconciliada el 2026-09-03.

## Datos documentales relevantes

La contribución identifica como compiladores a Gabriela Pérez Báez, Terrence Kaufman y Christian Brendel, y reconoce además la colaboración de Rosaura López Cartas, Javier López Cartas, Rosalino Gallegos Luis y Víctor Cata, entre otras personas contribuyentes registradas por código.

La versión consultada declara:

- 9,012 entradas léxicas;
- 2,385 verbos, muchos con formas habitual, potencial y completiva;
- variedades representadas: La Ventosa, Juchitán de Zaragoza y Santa María Xadani;
- headwords escritos siguiendo el borrador 2016 de la `Norma del sistema de escritura de la lengua zapoteca`;
- representaciones adicionales PDLMA para documentación fonológica y morfológica.

## Clases verbales

Dictionaria señala que la clasificación morfológica de sus verbos se basa en Pérez Báez y Kaufman (2016). Por ello deben distinguirse dos preguntas:

```text
WHAT_IS_THE_FOUR_CLASS_SYSTEM -> SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES + HALL-0073..0076
WHAT_CLASS_IS_THIS_LEXICAL_ENTRY -> DICTIONARIA_RECORD_WITH_ITS_ATTRIBUTION
```

La teoría general de las clases A–D no debe reconstruirse desde un registro aislado de Dictionaria. A la inversa, la clase asignada a un verbo concreto no debe atribuirse automáticamente al artículo PBK2016 si la evidencia consultada es el registro lexicográfico de Dictionaria.

Para consultas ordinarias de un verbo concreto, preferir el registro fuente de Dictionaria y conservar los códigos de atribución del registro. Si una clase sólo puede recuperarse temporalmente desde `DIC_VERB_2385_v0_1.csv`, tratar ese CSV como derivado de recuperación hasta volver al registro documental pertinente.

## Derechos y atribución

La contribución declara CC BY 4.0, pero la atribución no debe reducirse al nombre del sitio. Los registros incluyen códigos que acreditan hablantes y fuentes publicadas. Cualquier derivado reutilizable debe conservar la atribución pertinente por registro cuando esté disponible.

```text
DICTIONARIA_SITE_LICENSE = CC_BY_4_0
PER_RECORD_ATTRIBUTION = PRESERVE
```

## Relación con el dispositivo

El runtime histórico conserva:

- `DICTIONARIA_entries_v0_2_15_2.csv` — 9,012 entradas;
- `DICTIONARIA_senses_v0_2_15_2.csv`;
- `DICTIONARIA_examples_v0_2_15_2.csv`;
- `DIC_VERB_2385_v0_1.csv`.

Esos archivos son fixtures/derivados técnicos necesarios para reproducibilidad histórica. No son una segunda autoridad documental.

```text
DICTIONARIA_WEB_CONTRIBUTION = SOURCE
RUNTIME_CSV = TECHNICAL_DERIVATIVE_OR_HISTORICAL_FIXTURE
```

La coincidencia de 9,012 entradas y 2,385 verbos vincula materialmente los datasets técnicos recuperados con esta contribución. La fecha o mecanismo exacto de exportación de los CSV históricos debe conservarse como genealogía técnica cuando esté disponible; no es requisito para que Voces pueda consultar la fuente original.

## Estado de recuperación

La consulta general de **cómo funciona el sistema de clases verbales** ya no depende del dispositivo: quedó promovida a Voces en `HALL-0073`–`HALL-0076` y en el `SRC` de PBK2016.

La consulta masiva o por lote de las 2,385 asignaciones individuales todavía tiene un derivado técnico histórico útil (`DIC_VERB_2385_v0_1.csv`). No se copia completo a Voces por defecto: hacerlo aumentaría peso y duplicación. Se materializará un derivado documental más ligero sólo si la recuperación directa desde Dictionaria resulta insuficiente para el uso cotidiano.
