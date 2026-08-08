# PRIN-G-RESTRICCION-DURA — El eje gramatical tiene restricción dura no negociable

```yaml
id: PRIN-G-RESTRICCION-DURA
titulo: "El eje gramatical tiene restricción dura no negociable"
principio: >
  El nivel_gramatical asignado a un paso constituye una restricción dura sobre la estructura
  lingüística que el generador puede producir. Esta restricción no se puede violar.

  Fundamento: la lógica del input comprensible de Krashen (i+1). El material debe estar un paso
  arriba del nivel actual del aprendiz, no cinco pasos arriba. Exposición prematura a estructuras
  fuera del alcance del aprendiz genera ruido más que aprendizaje.

  Implicaciones operativas:
  - Si un paso está etiquetado nivel_gramatical 2, el generador NO debe producir cadi, subordinación
    condicional, posesión completa (todas nivel 5).
  - Si un paso está etiquetado nivel_gramatical 3, se pueden usar estructuras hasta nivel 3
    (existenciales, potencial simple, imperativo suave, algunas fórmulas de cortesía), pero no nivel 4-5.
  - Las excepciones internas de una situación (ej. "un paso sube a G4 por esto") deben estar
    anotadas explícitamente en el encabezado.
  - El generador debe calibrar cada oración a la restricción más baja presentada en su paso.

aplicacion_concreta:
  - Caso Quién soy: aunque pragmáticamente es trivial (P1), incluye pasos con G4 (posesión completa
    en "¿Cuántos hermanos tienes?"). El generador respeta G4 ≤ estructura ≤ G4, no baja a G1
    solo porque la pregunta es socialmente fácil.

  - Caso Estoy aprendiendo zapoteco: aunque pragmáticamente es denso (P5), la estructura
    gramaticalmente es moderada (G3). El generador produce oración con estructura G3 ≤ ≤ G3,
    pero explora la densidad emocional/reflexiva dentro de lo que permite esa estructura.

validado_por:
  - Krashen, Stephen. The Input Hypothesis (1985)
  - Análisis de casos del inventario COR002
  - SRC-PEDAGOGICAL-FUNDAMENTOS

etiquetas:
  - pedagogia
  - restricción_dura
  - input_comprensible
  - corpus
```
