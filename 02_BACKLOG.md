# 02_BACKLOG

**Versión:** 1.0

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

---

## P2. Una tarea, un objetivo

Cada elemento del backlog debe representar un objetivo completo y claramente identificable.

No se utilizará para registrar ideas sueltas, notas o recordatorios.

---

## P3. Sin desarrollo anticipado

Registrar una tarea en el backlog no implica comenzar a trabajar en ella.

Las tareas permanecerán registradas hasta que les corresponda su turno.

---

## P4. Prioridad explícita

Toda tarea deberá indicar su prioridad.

La prioridad solo podrá modificarse mediante revisión explícita.

---

## P5. Trabajo secuencial

El proyecto desarrollará únicamente la tarea activa.

No se iniciará una nueva tarea mientras la actual permanezca abierta, salvo que exista una dependencia crítica.

---

# Estados

Cada elemento del backlog utilizará uno de los siguientes estados:

* Detectado
* En análisis
* En ejecución
* Pendiente de validación
* Completado
* Descartado

---

# Prioridades

Las prioridades del backlog serán:

* Crítica
* Alta
* Media
* Baja

---

# Categorías

Las tareas se clasificarán utilizando una única categoría principal.

Categorías vigentes:

* Sistema
* Documentación
* Metodología
* Corpus
* Audio
* Pedagogía
* Bibliografía
* ELDP
* Validación comunitaria

---

# Estructura de cada tarea

Cada elemento del backlog utilizará el siguiente formato.

```text
ID:

Título:

Categoría:

Prioridad:

Estado:

Descripción:

Dependencias:

Criterio de cierre:

Notas:
```

---

# Backlog vigente

---

## BL-001

**Título:** Consolidar documentos constitucionales

**Categoría:** Sistema

**Prioridad:** Crítica

**Estado:** En ejecución

**Descripción**

Completar y aprobar todos los documentos que gobiernan el funcionamiento del Sistema de Conocimiento.

**Dependencias**

Ninguna.

**Criterio de cierre**

Todos los documentos constitucionales se encuentran aprobados y versionados en el repositorio.

---

## BL-002

**Título:** Definir reglas de actualización

**Categoría:** Sistema

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Establecer el procedimiento oficial mediante el cual nueva información modifica el Sistema de Conocimiento.

**Dependencias**

BL-001.

**Criterio de cierre**

Documento aprobado y publicado.

---

## BL-003

**Título:** Definir convenciones documentales

**Categoría:** Sistema

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Establecer reglas uniformes para nomenclatura, versiones, estados, referencias y formato documental.

**Dependencias**

BL-001.

**Criterio de cierre**

Documento aprobado y publicado.

---

## BL-004

**Título:** Migrar los Markdown de contexto

**Categoría:** Documentación

**Prioridad:** Alta

**Estado:** Detectado

**Descripción**

Integrar el conocimiento contenido en los Markdown históricos dentro del Sistema de Conocimiento y dejar de utilizarlos como fuente principal de trabajo.

**Dependencias**

BL-001, BL-002 y BL-003.

**Criterio de cierre**

Todo el conocimiento relevante ha sido consolidado en los documentos definitivos.

---

## BL-005

**Título:** Consolidar metodología

**Categoría:** Metodología

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Construir el documento metodológico definitivo a partir del conocimiento consolidado.

**Dependencias**

BL-004.

**Criterio de cierre**

Documento metodológico aprobado.

---

## BL-006

**Título:** Consolidar corpus

**Categoría:** Corpus

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Integrar todas las decisiones relativas al diseño, organización y evolución del corpus.

**Dependencias**

BL-004.

**Criterio de cierre**

Documento del corpus aprobado.

---

## BL-007

**Título:** Consolidar teoría

**Categoría:** Bibliografía

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Integrar la fundamentación teórica utilizada por el proyecto y relacionarla con las decisiones metodológicas correspondientes.

**Dependencias**

BL-004.

**Criterio de cierre**

Documento teórico aprobado.

---

## BL-008

**Título:** Consolidar metodología de audio

**Categoría:** Audio

**Prioridad:** Media

**Estado:** Detectado

**Descripción**

Consolidar todas las decisiones relacionadas con grabación, edición, normalización y publicación del audio.

**Dependencias**

BL-004.

**Criterio de cierre**

Documento de audio aprobado.

---

# Reglas de mantenimiento

1. Ninguna tarea podrá eliminarse sin quedar registrada como **Descartada** o **Completada**.

2. Cuando una tarea genere otras nuevas, estas deberán añadirse al backlog antes de iniciar su desarrollo.

3. Ninguna idea surgida durante el trabajo interrumpirá la tarea activa. Si resulta relevante, se registrará como una nueva entrada del backlog.

4. La prioridad de una tarea no modifica automáticamente el orden de ejecución. Las dependencias tienen precedencia.

5. El backlog constituye la única referencia oficial del trabajo pendiente del Sistema de Conocimiento.
