# DEC-CORPUS-FINAL-NO-SPANISH-FIRST — Los productos finales del corpus no se diseñan desde el español

```yaml
id: DEC-CORPUS-FINAL-NO-SPANISH-FIRST
titulo: "Los productos finales del corpus no se diseñan desde el español"
decision: >
  A partir del 3 de septiembre de 2026, los nuevos productos finales de corpus de
  Voces de las Nubes no podrán concebirse, estructurarse ni generarse a partir de
  una escena, secuencia, construcción o lógica discursiva diseñada primero en español
  para después ser trasladada al Didxazá.

  El español puede utilizarse como apoyo de comprensión, glosa, traducción de referencia,
  contraste, documentación o instrumento de pruebas experimentales explícitamente marcadas
  como tales. También puede utilizarse para formular hipótesis que luego deban comprobarse.
  En esos casos, el resultado no adquiere por ello estatus de producto final del corpus.

  Para entrar al corpus final, el material debe construirse desde evidencia y organización
  propias del Didxazá: producción de hablantes, corpus oral, elicitación, fuentes documentales,
  patrones suficientemente respaldados y otras vías que permitan que la estructura final
  responda al idioma y no a una precomposición española.

  Las herramientas de chat o sistemas derivados pueden asistir en investigación, análisis,
  contraste o generación experimental, pero no autorizan por sí mismas un producto final.
  La incorporación final continúa sujeta a la validación lingüística y metodológica pertinente.
estado: vigente
fecha: 2026-09-03
responsable: Emiliano López Carlton
validadores:
  - Emiliano López Carlton
hallazgos_que_la_sustentan: []
fuentes_directas:
  - "Decisión explícita de coordinación de Emiliano López Carlton, 2026-09-03"
principios_relacionados:
  - PRIN-INVESTIGACION-ABIERTA
supuestos_implicados: []
alternativas_consideradas:
  - "seguir diseñando escenas finales en español como matriz estructural para su posterior realización en Didxazá"
  - "prohibir por completo el uso del español incluso como glosa, contraste o instrumento experimental"
justificacion: >
  La experiencia acumulada del proyecto mostró que un corpus pensado primero desde el español
  corre el riesgo de proyectar sobre el Didxazá estructuras, secuencias discursivas, selección
  de información y expectativas conversacionales propias de la lengua de partida. Mantener el
  español como herramienta auxiliar sigue siendo útil, pero no debe gobernar la arquitectura de
  los nuevos productos finales. La investigación experimental conserva libertad para utilizar
  diseños Spanish-first cuando precisamente se quiera medir, contrastar o estudiar sus efectos.
impacta_a:
  - conocimiento/CORPUS.md
  - conocimiento/METODOLOGIA.md
  - conocimiento/PEDAGOGIA.md
  - futuros corpus y productos pedagógicos
  - diseño de futuras herramientas de generación
reemplaza: null
reemplazada_por: null
condiciones_de_revision:
  - "evidencia empírica que obligue a precisar qué cuenta como diseño Spanish-first"
  - "resultados de nuevas vías de generación o elicitación centradas en Didxazá"
  - "necesidad de distinguir con mayor precisión entre material experimental y producto final"
```

## Regla operativa

```text
FINAL_CORPUS_PRODUCT = DIDXAZA_CENTERED
SPANISH_FIRST_FINAL_DESIGN = NOT_ALLOWED
SPANISH_AS_GLOSS_OR_REFERENCE = ALLOWED
SPANISH_FIRST_EXPERIMENT = ALLOWED_IF_EXPLICITLY_EXPERIMENTAL
EXPERIMENTAL_OUTPUT != FINAL_CORPUS_PRODUCT
CHAT_OR_DERIVED_TOOL_OUTPUT != AUTOMATIC_FINAL_CORPUS_PRODUCT
FINAL_ENTRY_REQUIRES_PERTINENT_VALIDATION = true
```

## Alcance de la excepción experimental

Una prueba experimental puede partir deliberadamente del español cuando el objetivo sea observar,
comparar o medir qué problemas produce esa vía, o contrastarla con otra arquitectura de generación.
Ese material debe conservar claramente su condición experimental y no podrá incorporarse al corpus
final únicamente porque resulte plausible o haya sido técnicamente bien formado.

La excepción protege la investigación abierta; no reabre el español como matriz ordinaria de producción.
