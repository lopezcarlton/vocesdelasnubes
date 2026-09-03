# DEC-G-P-SEPARATION — Mantener complejidad gramatical y pragmática como dimensiones separables

```yaml
id: DEC-G-P-SEPARATION
titulo: "Mantener complejidad gramatical y pragmática como dimensiones separables"
decision: >
  A partir de agosto de 2026, el proyecto conserva la distinción entre complejidad gramatical (G)
  y complejidad pragmática (P) como dos dimensiones que pueden divergir y que resultan útiles para
  analizar, comparar y calibrar materiales de COR002.

  Esta decisión NO establece que las definiciones actuales G1–G5 y P1–P5 sean una taxonomía
  definitiva, ni que deban funcionar como secuencia curricular cerrada, ni que deban
  aplicarse automáticamente antes de construir una escena.

  Durante el piloto principiante de COR002, el orden operativo es:

  escena -> revisión contextual -> corrección -> análisis G/P -> hablante -> aprendizaje metodológico

  Por tanto, G/P se utiliza después de contar con una escena contextual y conversacionalmente
  aceptable para entender qué complejidad contiene y si cabe en el alcance provisional del piloto.

  La ventana actual G1–G3 / P1–P3 es experimental y reversible. P3 funciona como borde de prueba.
  Este corte no redefine el sistema general G/P.

estado: vigente
estado_descriptivo_anterior: vigente_como_separacion_de_dimensiones
fecha: 2026-08-07
fecha_decision_original: 2026-08-07
fecha_revision: 2026-08-31
responsable: Emiliano López Carlton

hallazgos_que_la_sustentan:
  - HALL-0006

principios_relacionados:
  - PRIN-COMPETENCIA-COMUNICATIVA-MULTIDIMENSIONAL
  - PRIN-G-RESTRICCION-DURA
  - PRIN-P-RESTRICCION-BLANDA

supuestos_implicados: []
alternativas_consideradas:
  - "mantener un único eje de dificultad que comprima complejidad gramatical y pragmática"
  - "mantener G/P como restricciones automáticas previas a la construcción de escenas"
justificacion: >
  HALL-0006 documentó que un único nivel comprimía dimensiones que pueden divergir.
  La revisión posterior mostró además que aplicar G/P como restricciones automáticas antes
  de disponer de escenas aceptables producía una arquitectura demasiado rígida. La decisión
  conserva la separación analítica y retira esa implementación fuerte.

validadores:
  - Emiliano López Carlton

impacta_a:
  - CORPUS.md
  - PEDAGOGIA.md
  - METODOLOGIA.md

implementacion_anterior_ya_no_vigente: >
  La formulación original interpretaba G como restricción dura no negociable de generación y P como
  restricción blanda que gobernaba contenido y tono. Esa implementación produjo una arquitectura
  demasiado rígida cuando se aplicó antes de disponer de escenas de referencia aceptadas.

  Al 2026-08-31 queda suspendida como regla automática del generador durante el piloto.
  Se conserva como hipótesis histórica que podrá reevaluarse con escenas reales, realizaciones de
  hablantes y pruebas con aprendices.

reemplaza: null
reemplazada_por: null

condiciones_de_revision:
  - Revisar las fronteras G1–G5 y P1–P5 a partir de escenas aceptadas y realizaciones en Didxazá.
  - Revisar si la carga discursiva/referencial queda suficientemente representada dentro de P o necesita otra descripción.
  - Revisar si alguna forma de restricción previa resulta pedagógicamente útil al diseñar materiales futuros.
  - Revisar con aprendices reales qué complejidad resulta comprensible, producible y transferible.

provenance:
  - conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md

etiquetas:
  - decisión_pedagógica
  - corpus
  - ejes_de_dificultad
  - sistema_de_etiquetado
  - revisable
```

## Historial

### 2026-08-07

Se adoptó la separación G/P con una implementación fuerte: G como restricción dura de forma y P como restricción blanda de contenido.

### 2026-08-31

Se conserva la separación entre dimensiones, pero se retira su interpretación automática como regla obligatoria de generación durante el piloto principiante. G/P pasa a operar principalmente como capa posterior de análisis y calibración mientras se construyen las primeras escenas de referencia.
