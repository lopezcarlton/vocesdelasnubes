# SRC-MUNTZEL-1998-RESENA-GRAMATICA-POPULAR

```yaml
id: SRC-MUNTZEL-1998-RESENA-GRAMATICA-POPULAR
tipo: fuente_bibliografica
bib_id: BIB041
titulo: "Reseña de Gramática popular del zapoteco del Istmo"
autor_o_participantes:
  - Martha C. Muntzel
fecha: 1998
publicacion: "Dimensión Antropológica, Año 5, Vol. 14, pp. 170–174"
ubicacion: "https://revistas.inah.gob.mx/index.php/dimension/article/view/9066"
ubicacion_pdf: "https://revistas.inah.gob.mx/index.php/dimension/article/download/9066/9843"
descripcion: >
  Reseña académica de la primera edición en español de la Gramática popular del
  zapoteco del Istmo de Velma B. Pickett, Cheryl Black y Vicente Marcial Cerqueda.
  Sitúa la obra en la tradición de estudios zapotecos y explica el propósito práctico
  de una gramática popular para público no especializado.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web_editor_institucional
estado_de_lectura: backfill_dirigido_completado_2026-09-05
```

## Memoria persistente de lectura — backfill desde informe institucional

El informe de mayo de 2026 había destacado tres ideas: naturaleza práctica de una gramática popular, centralidad de un corpus amplio y fiel, y prestigio social del zapoteco del Istmo.

La revisión directa del PDF oficial del INAH permite precisar la procedencia:

- Muntzel caracteriza las gramáticas populares como obras simplificadas para público no especializado, sin terminología ni fórmulas innecesariamente complejas, cuyo objetivo es proporcionar datos básicos y estructura general de la lengua → `HALL-0205`.
- En p. 173 Muntzel afirma que lo fundamental es contar con un corpus amplio y fiel del idioma y que sin él no puede construirse una teoría de la naturaleza del lenguaje → `HALL-0206`.
- La afirmación sobre el orgullo de hablantes istmeños al expresarse en zapoteco aparece en la reseña como material procedente del prólogo del *Vocabulario zapoteco del Istmo*. BIB041 confirma su circulación, pero la autoridad documental más directa para esa afirmación es BIB003 → `HALL-0207`.

## Corrección de procedencia respecto del informe de mayo

El informe institucional presentó la frase sobre corpus como una cita de Pickett. En el PDF de Muntzel, el pasaje aparece en la voz expositiva de la reseñista y remite en nota 12 a un trabajo inédito suyo de 1983 (`A survey of grammars`). Por tanto:

```text
CORPUS_QUOTE_IN_BIB041 = MUNTZEL_1998
CORPUS_QUOTE_ATTRIBUTION_TO_PICKETT = NOT_SUPPORTED_BY_BIB041
```

La idea sigue siendo válida como hallazgo de BIB041, pero su autoría debe corregirse.

## Límites

La reseña es una fuente secundaria sobre la Gramática Popular y el Vocabulario. Cuando una afirmación dependa de esas obras, debe preferirse la obra original para adjudicar contenido lingüístico o lexicográfico específico.

```text
BIB041 = REVIEW_SOURCE
BIB041 != GRAMATICA_POPULAR_ORIGINAL
BIB041 != VOCABULARIO_ORIGINAL
```
