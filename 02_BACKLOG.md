# 02_BACKLOG

**Versión:** 2.0

**Estado:** APROBADO

**Fecha:** 2026-08-05

---

# Propósito

Este documento constituye el registro oficial del trabajo pendiente del proyecto.

Su objetivo es mantener una única lista priorizada de tareas necesarias para completar, mantener o mejorar el Sistema de Conocimiento de **Voces de las Nubes**.

El backlog evita la apertura de frentes de trabajo paralelos y sirve como mecanismo de control del alcance del proyecto.

---

# Principios

## P1. Fuente única

Todo trabajo pendiente deberá registrarse en este documento.

No deberán mantenerse listas paralelas de tareas.

## P2. Una tarea, un objetivo

Cada elemento del backlog debe representar un objetivo completo y claramente identificable.

No se utilizará para registrar ideas sueltas, notas o recordatorios.

## P3. Sin desarrollo anticipado

Registrar una tarea en el backlog no implica comenzar a trabajar en ella.

Las tareas permanecerán registradas hasta que les corresponda su turno.

## P4. Prioridad explícita

Toda tarea deberá indicar su prioridad.

La prioridad solo podrá modificarse mediante revisión explícita.

## P5. Trabajo secuencial

El proyecto desarrollará únicamente la tarea activa.

No se iniciará una nueva tarea mientras la actual permanezca abierta, salvo que exista una dependencia crítica.

## P6. El trabajo real determina la documentación

No se crearán documentos, reglas o procedimientos para resolver problemas hipotéticos.

Un vacío se incorporará al backlog cuando aparezca durante el trabajo, se repita o impida continuar con claridad.

---

# Estados

Cada elemento del backlog utilizará uno de los siguientes estados:

- Detectado
- En análisis
- En ejecución
- Pendiente de validación
- Completado
- Descartado

---

# Prioridades

- Crítica
- Alta
- Media
- Baja

---

# Categorías

- Sistema
- Documentación
- Metodología
- Corpus
- Audio
- Pedagogía
- Bibliografía
- ELDP
- Validación comunitaria

---

# Tarea activa

## BL-009

**Título:** Documentar la preparación de materiales para sesiones con hablantes

**Categoría:** Metodología

**Prioridad:** Alta

**Estado:** En ejecución

**Descripción**

Documentar el procedimiento que conecta el material aprobado del corpus con una sesión de trabajo con hablantes. Debe aclarar qué significa preparar las frases, quién realiza cada paso y cómo se construyen las guías de elicitación sin convertirlas en traducciones rígidas desde el español.

**Dependencias**

METODOLOGIA.md, CORPUS.md y la experiencia ya realizada con COR001.

**Criterio de cierre**

Existe un procedimiento reproducible que define insumos, responsable, pasos, productos y puntos de validación para preparar una sesión con hablantes. El conocimiento se incorpora al documento permanente correspondiente.

**Notas**

Esta tarea reúne los dos procedimientos huérfanos identificados en la auditoría: preparación de frases y diseño de guías de elicitación.

---

# Tareas pendientes

## BL-010

**Título:** Formalizar el protocolo de validación comunitaria

**Categoría:** Validación comunitaria

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Definir cómo se registra una validación realizada por hablantes, cuál es su alcance, cómo se documentan ajustes y desacuerdos, y cómo se reconocen autoría, consentimiento y condiciones de uso.

**Dependencias**

BL-009 y VALIDACION.md.

**Criterio de cierre**

Existe un protocolo aplicable en sesiones reales que registra objeto validado, participante, autoridad, resultado, alcance, cambios y acuerdos de uso.

**Notas**

No debe confundirse una validación individual con consenso comunitario. No se definirán métricas artificiales de consenso sin evidencia de que sean necesarias.

---

## BL-011

**Título:** Reconstruir COR002

**Categoría:** Corpus

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Construir una nueva versión de COR002 desde situaciones comunicativas, funciones, patrones, cobertura de COR001 y trabajo con hablantes, sin recuperar automáticamente el bloque anterior de frases 108–224.

**Dependencias**

BL-009 y BL-010.

**Criterio de cierre**

Existe una versión completa de COR002 con trazabilidad, revisión contra COR001 y estado de validación explícito para cada unidad.

---

## BL-012

**Título:** Validar la progresión con aprendices

**Categoría:** Pedagogía

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Diseñar y realizar pruebas iniciales con aprendices para observar comprensión, recuperación, producción, duración de pausas, retención y transferencia.

**Dependencias**

BL-011 y disponibilidad de materiales auditivos utilizables.

**Criterio de cierre**

Existe evidencia documentada de una primera prueba con aprendices y se registraron los ajustes pedagógicos derivados.

---

## BL-013

**Título:** Implementar control externo de cobertura

**Categoría:** Corpus

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Construir una herramienta o procedimiento externo para mantener historial de situaciones, funciones, patrones, léxico, personajes y balance acumulado.

**Dependencias**

La construcción de COR002 debe demostrar que el control manual ya no es suficiente.

**Criterio de cierre**

Existe un mecanismo reproducible que genera las decisiones concretas del bloque TAREA sin delegar al modelo la interpretación de déficits acumulados.

**Notas**

No se inicia mientras el trabajo manual siga siendo suficiente.

---

## BL-014

**Título:** Formalizar niveles G1–G5 y P1–P5

**Categoría:** Pedagogía

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Definir los niveles gramaticales y pragmáticos a partir de ejemplos reales y decisiones surgidas durante la reconstrucción de COR002.

**Dependencias**

BL-011.

**Criterio de cierre**

Cada nivel cuenta con definición operacional, límites, ejemplos reales y criterios suficientes para clasificar material nuevo de forma consistente.

**Notas**

No debe formalizarse antes de que COR002 produzca evidencia suficiente.

---

# Tareas completadas

## BL-001

**Título:** Consolidar documentos constitucionales

**Categoría:** Sistema

**Prioridad:** Crítica

**Estado:** Completado

**Descripción**

Consolidar el marco mínimo necesario para gobernar el Sistema de Conocimiento.

**Criterio de cierre alcanzado**

El repositorio cuenta con Arquitectura del Conocimiento, Jerarquía de Verdad y Backlog operativo.

---

## BL-004

**Título:** Migrar los Markdown de contexto

**Categoría:** Documentación

**Prioridad:** Alta

**Estado:** Completado

**Descripción**

Integrar el conocimiento relevante de los Markdown históricos en documentos permanentes.

**Criterio de cierre alcanzado**

Los documentos históricos permanecen como fuentes de migración y el conocimiento consolidado se encuentra en `conocimiento/`.

---

## BL-005

**Título:** Consolidar metodología

**Categoría:** Metodología

**Prioridad:** Media

**Estado:** Completado

**Criterio de cierre alcanzado**

`conocimiento/METODOLOGIA.md` fue construido y publicado.

---

## BL-006

**Título:** Consolidar corpus

**Categoría:** Corpus

**Prioridad:** Media

**Estado:** Completado

**Criterio de cierre alcanzado**

`conocimiento/CORPUS.md` fue construido y publicado.

---

## BL-007

**Título:** Consolidar teoría

**Categoría:** Bibliografía

**Prioridad:** Media

**Estado:** Completado

**Criterio de cierre alcanzado**

`conocimiento/TEORIA.md` fue construido y publicado.

---

## BL-008

**Título:** Consolidar metodología de audio

**Categoría:** Audio

**Prioridad:** Media

**Estado:** Completado

**Criterio de cierre alcanzado**

`conocimiento/AUDIO.md` fue construido y publicado.

---

## BL-015

**Título:** Consolidar pedagogía, bibliografía y validación

**Categoría:** Documentación

**Prioridad:** Media

**Estado:** Completado

**Descripción**

Construir los documentos temáticos adicionales exigidos por el trabajo real de consolidación.

**Criterio de cierre alcanzado**

`conocimiento/PEDAGOGIA.md`, `conocimiento/BIBLIOGRAFIA.md` y `conocimiento/VALIDACION.md` fueron construidos y publicados.

---

# Tareas descartadas

## BL-002

**Título:** Definir reglas de actualización como documento constitucional independiente

**Categoría:** Sistema

**Prioridad:** Alta

**Estado:** Descartado

**Motivo**

La consolidación pudo realizarse sin este documento. Las reglas necesarias ya están distribuidas entre la Arquitectura, la Jerarquía de Verdad, el Backlog y los documentos temáticos. Se reconsiderará únicamente si una actualización real produce conflictos repetidos.

---

## BL-003

**Título:** Definir convenciones documentales como documento constitucional independiente

**Categoría:** Sistema

**Prioridad:** Alta

**Estado:** Descartado

**Motivo**

No se justificó crear un documento adicional antes de observar problemas reales de nomenclatura, versiones o referencias. Las convenciones existentes son suficientes para el tamaño actual del sistema.

---

# Trabajo deliberadamente aplazado

No se incorpora como tarea activa por ahora:

- automatización de referencias cruzadas;
- implementación general del sistema de identificadores `TIPO-0001`;
- matriz exhaustiva de autoridad para un equipo ampliado;
- criterios de completitud para cada vacío documental;
- nuevos documentos constitucionales.

Estos temas se incorporarán al backlog solo si el crecimiento del proyecto demuestra que son necesarios.

---

# Reglas de mantenimiento

1. Ninguna tarea podrá eliminarse sin quedar registrada como **Descartada** o **Completada**.
2. Cuando una tarea genere otras nuevas, deberán añadirse al backlog antes de iniciar su desarrollo.
3. Ninguna idea surgida durante el trabajo interrumpirá la tarea activa.
4. Las dependencias tienen precedencia sobre la prioridad.
5. El backlog constituye la única referencia oficial del trabajo pendiente.
6. Solo puede existir una tarea en estado **En ejecución**, salvo dependencia crítica documentada.

---

# Historial

## v2.0 — 2026-08-05

- Se cerró la fase de migración y consolidación documental.
- Se marcaron como completados los documentos temáticos construidos.
- Se descartaron reglas y convenciones independientes que no resultaron necesarias.
- Se incorporaron los vacíos confirmados por la auditoría posterior a la consolidación.
- Se estableció BL-009 como única tarea activa.

## v1.0 — 2026-08-05

- Primera versión aprobada.
