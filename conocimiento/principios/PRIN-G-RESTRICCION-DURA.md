# PRIN-G-RESTRICCION-DURA — Hipótesis histórica sobre restricción gramatical previa

```yaml
id: PRIN-G-RESTRICCION-DURA
titulo: "Hipótesis histórica sobre restricción gramatical previa"
estado: en_revision
fecha_revision: 2026-08-31

principio_original: >
  La formulación inicial sostenía que el nivel_gramatical asignado a un paso debía constituir una
  restricción dura no negociable sobre la estructura que un generador podía producir.

  Esta formulación buscaba proteger la progresión y evitar exposición prematura a estructuras que
  el aprendiz no pudiera procesar.

estado_actual: >
  El proyecto conserva la intuición de que la complejidad gramatical importa y que un material de
  principiantes no debe sobrecargarse arbitrariamente. Sin embargo, la regla "G asignado = techo duro
  obligatorio antes de generar" queda suspendida durante el piloto actual de COR002.

  El piloto trabaja primero una escena plausible y después analiza qué complejidad gramatical contiene.
  Si la escena rebasa el alcance provisional del piloto, puede simplificarse, posponerse o descartarse.
  G funciona por ahora como instrumento de análisis y calibración, no como candado automático que
  deba gobernar cada oración antes de que exista una escena de referencia aceptada.

razon_de_revision: >
  Las iteraciones del generador mostraron que imponer de antemano demasiadas restricciones podía
  resolver un problema y crear otro: escenas demasiado fragmentarias, artificiales o parecidas a
  ejercicios de sustitución. El proyecto decidió invertir el orden de trabajo y aprender primero de
  conversaciones concretas.

no_se_concluye:
  - que la complejidad gramatical deje de importar;
  - que cualquier estructura sea adecuada para principiantes;
  - que G1–G5 deba eliminarse;
  - que la hipótesis de un techo gramatical no pueda recuperarse en un futuro generador.

criterio_actual_piloto:
  - producir y revisar una escena contextualmente plausible;
  - analizar después sus estructuras y carga gramatical;
  - contrastarla con la ventana experimental G1–G3;
  - simplificar, posponer o descartar cuando la carga resulte incompatible;
  - revisar el criterio con realizaciones de hablantes y aprendices reales.

provenance:
  - conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md
  - conocimiento/decisiones/DEC-G-P-SEPARATION.md

etiquetas:
  - pedagogia
  - complejidad_gramatical
  - hipótesis
  - revisable
  - corpus
```

## Nota histórica

La versión del 7 de agosto de 2026 declaraba esta restricción como "dura no negociable" y la vinculaba directamente con la ejecución del generador. Esa implementación se conserva en el historial del repositorio, pero no gobierna el piloto de COR002 al cierre de agosto.

## Auditoría de esquema — 2026-09-02

**Autoridad normativa temporal:** `SUSPENDED_PENDING_ENTITY_ADJUDICATION`

Este archivo fue localizado con un estado y/o campos que no cumplen el esquema `PRIN` definido en `00_ARQUITECTURA_DEL_CONOCIMIENTO.md` §4.5. Se conserva íntegramente como antecedente, pero no debe utilizarse como principio vigente hasta decidir qué contenido corresponde realmente a principio, decisión, supuesto, aplicación teórica o historia de implementación.

La suspensión no resuelve el fondo de G/P ni modifica sus preguntas de investigación.

