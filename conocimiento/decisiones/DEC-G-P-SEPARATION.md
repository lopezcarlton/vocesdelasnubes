# DEC-G-P-SEPARATION — Adoptar doble etiquetado nivel_gramatical + nivel_pragmático como ejes independientes

```yaml
id: DEC-G-P-SEPARATION
titulo: "Adoptar doble etiquetado nivel_gramatical + nivel_pragmático como ejes independientes"
decision: >
  A partir de agosto 2026, el sistema de etiquetado del corpus COR002 utiliza dos ejes independientes
  por cada paso de cada situación comunicativa:

  1. nivel_gramatical (1–5): mide la complejidad de la estructura lingüística necesaria, desde
     fórmulas fijas memorizadas (1) hasta subordinación, condicionales, cadi, y posesión completa (5).
     Esta escala está anclada en las categorías de la Gramática Popular (Bloques 1-7).

  2. nivel_pragmático (1–5): mide la exigencia social/discursiva del acto de habla en sí, desde
     interacciones rutinarias de bajo riesgo (saludo, pregunta de datos, 1) hasta actos que requieren
     negociación, mediación de conflicto, autoevaluación emocional, reflexión metalingüística,
     o manejo de temas delicados (5).

  Cuando ambos niveles coinciden (caso común), pueden mostrarse juntos como un solo número
  para lectura humana simplificada. Cuando divergen, se escriben separados como G3/P5.

  El generador debe interpretar esta doble etiqueta de la siguiente manera:
  - La restricción gramatical rige la forma: no se puede rebasar nivel_gramatical asignado
    (restricción dura).
  - La etiqueta pragmática rige el contenido, tono, y densidad social: se puede explorar hasta
    ese nivel de riqueza temática incluso si expone al aprendiz a contenido más denso de lo que
    podría producir por sí solo (restricción blanda).
  - Regla de resolución: si hay conflicto, priorizar no rebasar restricción gramatical y ajustar
    contenido a lo que quepa dentro de esa restricción.

estado: vigente
fecha_decision: 2026-08-07
responsable: Emiliano López Carlton
hallazgos_que_la_sustentan:
  - HALL-0006

principios_relacionados:
  - PRIN-G-RESTRICCION-DURA
  - PRIN-P-RESTRICCION-BLANDA
  - PRIN-COMPETENCIA-COMUNICATIVA-MULTIDIMENSIONAL

validadores:
  - Emiliano López Carlton

impacta_a:
  - CORPUS.md (etiquetado de 48 situaciones)
  - PEDAGOGIA.md (sistema de niveles y etapas)
  - prompt_generador_corpus_v5.md (calibración del generador)
  - METODOLOGIA.md (convención de formato)

condiciones_de_revision:
  - Revisar cuando el prompt generador sea implementado y se detecten inconsistencias reales
    en output generado (verificar que respete restricción dura del eje gramatical).
  - Revisar si la experiencia con aprendices reales sugiere que restricción blanda del eje
    pragmático (exposición a contenido denso) produce efectos pedagógicos positivos o negativos.
  - Revisar si hay cuadrantes G/P sistemáticamente no-representados tras análisis de cobertura.

etiquetas:
  - decisión_pedagógica
  - corpus
  - ejes_de_dificultad
  - sistema_de_etiquetado
```

## Nota de nomenclatura

El identificador original de esta decisión (`DEC-G/P-SEPARATION`) contenía una barra, incompatible con nombres de archivo. Se adoptó `DEC-G-P-SEPARATION` como identificador estable, tanto en el nombre del archivo como en el campo `id` interno.
