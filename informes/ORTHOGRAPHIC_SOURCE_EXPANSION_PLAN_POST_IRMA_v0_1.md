# PLAN DE EXPANSIÓN DE FUENTES ORTOGRÁFICAS POST-IRMA — v0.1

**Fecha:** 2026-09-02  
**Estado:** `RESEARCH_PLAN / NON_NORMATIVE / NO_CORRECTOR_EFFECT`

Fuente detonante: `SRC-IRMA-PINEDA-REUNION-2026-09-02.md`.  
Backlog relacionado: `BL-024`.

## 1. Problema

La reunión abre una posibilidad importante: ampliar la base ortográfica desde gramáticas/diccionarios y un conjunto reducido de fuentes hacia literatura contemporánea producida por escritores que trabajan dentro de la tradición del Alfabeto Popular.

Pero no es seguro convertir directamente:

```text
TEXTO_DE_AUTOR_CONTEMPORANEO -> REGLA_DE_CORRECCION
```

Un texto puede contener variación dialectal, idiolectal, histórica, estilística, poética, editorial o tipográfica. La expansión debe aumentar evidencia sin borrar esa diversidad.

## 2. Objetivo

Construir un inventario trazable de **atestaciones ortográficas contemporáneas** que permita saber:

- quién escribió una forma;
- en qué obra;
- cuándo y dónde se publicó;
- qué variedad/localidad representa cuando pueda saberse;
- qué género es;
- si hubo edición o normalización externa conocida;
- si la forma aparece una vez o recurrentemente;
- qué otras fuentes la respaldan o contradicen.

El primer producto no será un corrector más agresivo. Será una capa documental más rica.

## 3. Paso cero — localizar el documento actualizado de escritura

La página actual de INALI sobre lengua zapoteca confirma que hablantes del diidxazá, acompañados por INALI, realizaron reuniones para actualizar el documento de uso estandarizado de la escritura.

Prioridad máxima:

1. identificar título exacto;
2. fecha/versión;
3. participantes y autoridad de adopción;
4. disponibilidad pública o institucional;
5. relación con el Alfabeto Popular de 1956 y con `Xneza diidxazá` (2015);
6. alcance varietal declarado.

Hasta encontrarlo, **“última versión del Alfabeto Popular” permanece como referencia por localizar**, no como artefacto conocido.

## 4. Corpus inicial de autores candidatos

La memoria de la reunión menciona:

- Irma Pineda;
- Víctor Cata;
- Víctor Terán;
- Natalia Toledo;
- Vicente Marcial;
- otros autores no conservados todavía en la reconstrucción.

El artículo Pérez Báez, Cata y Bueno Holle (2015) ofrece apoyo independiente a la afirmación de que autores contemporáneos como Natalia Toledo, Irma Pineda y Víctor Terán utilizan el Alfabeto Popular, pero también documenta problemas de homologación ortográfica. Por tanto, esta coincidencia aumenta su valor como corpus de evidencia sin volverlos intercambiables.

## 5. Metadatos mínimos por obra

Cada obra incorporada deberá registrar, cuando sea posible:

```text
source_id
bibliographic_id
writer
work_title
edition
publication_year
publisher
text_date_if_known
genre
subgenre
variety_claimed
locality_claimed
section_or_neighborhood_if_relevant
editorial_normalization_known
orthography_statement_present
source_format
page_or_location
rights_or_license
acquisition_route
```

Cada forma extraída añadirá:

```text
surface_form
context_sentence_or_short_span
normalized_lookup_key   # sólo para búsqueda; nunca reemplaza surface_form
lemma_if_independently_supported
morphological_analysis_if_supported
source_exact_location
attestation_status
notes
```

## 6. Género y función de evidencia

### Prosa narrativa, ensayo, crónica, material didáctico

Potencialmente alta utilidad para:

- segmentación de palabras;
- grafías léxicas;
- puntuación/convenciones;
- morfología en contexto;
- distribución de variantes.

La naturalidad conversacional no se presupone.

### Poesía

Puede aportar evidencia fuerte sobre grafías y formas léxicas, pero requiere cautela adicional para:

- segmentación motivada por verso;
- elipsis;
- orden de palabras;
- formas estilizadas;
- grafías elegidas por ritmo o identidad autoral.

```text
POETIC_ORTHOGRAPHIC_ATTESTATION = VALID_EVIDENCE
POETIC_SYNTAX = NOT_AUTOMATIC_CONVERSATIONAL_MODEL
```

### Diccionarios, materiales normativos y textos explícitamente ortográficos

Tienen otra función y deben etiquetarse por separado. Una forma prescrita y una forma literariamente atestiguada no son el mismo tipo de evidencia.

## 7. Variación

La nueva capa debe poder representar simultáneamente:

```text
FORM_A attested_by SOURCE_X
FORM_B attested_by SOURCE_Y
FORM_A and FORM_B accepted_by SPEAKER_Z
SOURCE_SCOPE differs
```

No se debe resolver automáticamente por mayoría de ocurrencias.

```text
MORE_ATTESTED != MORE_CORRECT
AUTHOR_PRESTIGE != GLOBAL_NORM
SINGLE_VARIANT != ERROR
```

La frecuencia sí puede ser un dato descriptivo, nunca el único criterio de corrección.

## 8. Separar tres preguntas

### Q1. ¿Está atestiguada?

Respuesta documental.

### Q2. ¿Es compatible con una convención ortográfica identificada?

Respuesta ortográfica/documental.

### Q3. ¿Debe el Corrector marcar otra forma como error o sugerir ésta?

Decisión mucho más conservadora que requiere política aprobada, alcance varietal y evidencia suficiente.

El proyecto debe poder responder Q1 mucho antes de tener derecho a responder Q3.

## 9. Caso `qui` / `qué`

La reunión añade una nueva atestación atribuida a Irma: equivalencia semántico-funcional y preferencia gráfica personal por `qui` para evitar confusión con el español.

Debe triangularse con las atestaciones existentes de otros hablantes y con corpus escrito contemporáneo.

No adoptar todavía:

```text
qui == qué  # regla global ejecutable
```

Sí investigar:

- distribución por escritor/localidad/generación;
- contextos sintácticos;
- uso en prosa vs poesía;
- normalización editorial;
- preferencias explícitas de hablantes;
- tratamiento en documento actualizado de escritura, si se localiza.

## 10. Flujo de incorporación

```text
ADQUIRIR_OBRA
-> registrar metadatos y derechos
-> conservar texto fuente sin normalización destructiva
-> extraer atestaciones
-> agrupar por forma/lexema sólo cuando identidad esté respaldada
-> comparar entre fuentes
-> registrar variantes y contradicciones
-> revisión lingüística
-> adjudicación en Voces de las Nubes
-> decisión explícita sobre uso ortográfico
-> publicar KNOWLEDGE_SOURCE_COMMIT
-> sólo entonces exportar al dispositivo
```

## 11. Consecuencia para el dispositivo — todavía no ejecutable

La dirección técnica probable es una arquitectura de evidencia donde el Corrector pueda distinguir:

- `ATTESTED_EXACT`;
- `ATTESTED_VARIANT`;
- `SOURCE_SCOPED_FORM`;
- `ORTHOGRAPHIC_CONVENTION_SUPPORTED`;
- `CONFLICTING_ATTESTATIONS`;
- `UNRESOLVED`;
- `CORRECTION_LICENSED` sólo tras adjudicación.

Estos nombres son candidatos de diseño. **No se implementan desde este plan.**

## 12. Criterio de éxito de BL-024

BL-024 podrá cerrarse cuando exista:

1. una versión identificable del documento contemporáneo de escritura o una constatación documentada de su estado;
2. un inventario inicial de obras contemporáneas con metadatos y derechos;
3. una política explícita sobre qué evidencia aporta cada género/fuente;
4. un tratamiento formal de variación;
5. criterios conservadores para pasar de atestación a sugerencia/corrección.
