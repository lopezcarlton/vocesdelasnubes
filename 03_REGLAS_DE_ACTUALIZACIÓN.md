# 03_REGLAS_DE_ACTUALIZACIÓN

**Versión:** 1.1

**Estado:** APROBADO

**Fecha:** 2026-08-19

---

# Propósito

Este documento establece las reglas mediante las cuales el Sistema de Conocimiento de **Voces de las Nubes** incorpora nueva información, modifica conocimiento existente y mantiene la trazabilidad de todos los cambios.

Su objetivo es garantizar que el sistema evolucione de manera consistente, evitando modificaciones arbitrarias o pérdida de información.

---

# Principios

## P1. Toda actualización debe tener una causa.

Ningún documento será modificado únicamente porque una nueva redacción parezca mejor.

Toda actualización deberá estar motivada por un hecho identificable.

---

## P2. El conocimiento evoluciona; no se reescribe.

Cuando una decisión cambie, la versión anterior no se elimina.

Se conserva como parte de la historia del proyecto y se registra la nueva decisión como vigente.

---

## P3. Cada actualización debe ser trazable.

Toda modificación deberá permitir responder:

* ¿Qué cambió?
* ¿Por qué cambió?
* ¿Qué evidencia lo motivó?
* ¿Qué documentos fueron afectados?
* ¿Quién realizó la actualización?

---

## P4. El sistema siempre prevalece sobre el documento individual.

Cuando una actualización afecte varios documentos, todos deberán mantenerse consistentes entre sí.

No se aceptarán contradicciones permanentes entre documentos oficiales.

---

## P5. Los repositorios relacionados no duplican autoridad.

Cuando información de Voces de las Nubes sea utilizada por un repositorio relacionado, ese repositorio debe referenciar la fuente vigente en lugar de mantener una segunda versión del mismo estado.

La relación con la candidatura al Small Grant se regula en `04_RELACION_CON_ELDP.md`.

Las decisiones propias de ELDP no modifican este Sistema de Conocimiento salvo adopción explícita dentro de Voces de las Nubes.

---

# Eventos que requieren actualización

Una actualización solo podrá iniciarse cuando ocurra al menos uno de los siguientes eventos:

* nueva evidencia obtenida durante el proyecto;
* validación o corrección realizada por colaboradores competentes;
* adopción de una nueva decisión;
* reemplazo explícito de una decisión anterior;
* incorporación de nueva bibliografía relevante;
* cambio en requisitos institucionales;
* corrección de un error documental;
* detección de una contradicción con un repositorio relacionado sobre una materia gobernada por Voces de las Nubes.

Fuera de estos casos, no deberá iniciarse una actualización.

---

# Procedimiento de actualización

Toda actualización seguirá el siguiente flujo:

1. Identificar el evento que origina el cambio.
2. Determinar qué documentos resultan afectados.
3. Verificar la Jerarquía de Verdad vigente.
4. Verificar, cuando corresponda, qué repositorio tiene autoridad sobre la materia.
5. Actualizar únicamente los documentos necesarios.
6. Revisar la consistencia del sistema.
7. Registrar el cambio mediante control de versiones.

---

# Tipos de actualización

Las actualizaciones podrán clasificarse como:

## Incorporación

Se añade conocimiento que anteriormente no existía.

---

## Corrección

Se corrige información objetivamente errónea.

La versión anterior permanece en el historial del repositorio.

---

## Reemplazo

Una decisión vigente sustituye formalmente a otra.

La decisión anterior pasa a estado histórico.

---

## Ampliación

Se incorpora información adicional sin modificar el conocimiento existente.

---

## Consolidación

Se integran múltiples documentos o registros en un documento definitivo sin alterar su contenido sustantivo.

---

# Manejo de conflictos

Cuando una actualización entre en conflicto con conocimiento existente deberá seguirse este procedimiento:

1. verificar que el conflicto sea real;
2. consultar la Jerarquía de Verdad;
3. determinar si existe una decisión posterior que resuelva el conflicto;
4. si interviene otro repositorio, determinar cuál gobierna la materia;
5. si el conflicto permanece, documentarlo explícitamente;
6. solicitar validación cuando corresponda.

Nunca se eliminará información únicamente para eliminar una contradicción.

---

# Relación con repositorios externos

El repositorio `lopezcarlton/ELDP` puede utilizar información de Voces de las Nubes para desarrollar una candidatura, pero no constituye fuente autoritativa sobre el estado del proyecto lingüístico.

Cuando una afirmación de ELDP sobre COR001, COR002, metodología, pedagogía, teoría, audio, validación u otro componente permanente contradiga este repositorio, deberá corregirse ELDP.

Cuando una regla o decisión corresponda exclusivamente a la candidatura, este repositorio no debe absorberla automáticamente.

---

# Documentos constitucionales

Los documentos constitucionales únicamente podrán modificarse cuando:

* una regla produzca conflictos repetidos;
* aparezca un nuevo tipo de evidencia;
* cambie la estructura del Sistema de Conocimiento;
* el equipo adopte explícitamente una nueva política.

Las modificaciones deberán registrarse como una nueva versión del documento.

---

# Casos que NO requieren actualización

No constituyen motivo suficiente para modificar el sistema:

* mejoras de estilo;
* cambios de redacción sin cambio de significado;
* reorganización visual;
* sugerencias no adoptadas;
* hipótesis no verificadas;
* propuestas generadas por IA que no hayan sido aceptadas por el proyecto.

---

# Control de versiones

Toda actualización deberá registrarse mediante el sistema de control de versiones del repositorio.

Los cambios deberán agruparse de manera lógica y documentarse mediante mensajes de commit descriptivos.

---

# Modificación de este documento

Este documento solo podrá modificarse cuando resulte insuficiente para gestionar la evolución del Sistema de Conocimiento.

No se modificará para resolver casos particulares.

Los casos particulares deberán resolverse mediante decisiones del proyecto o actualizaciones de los documentos correspondientes.

---

# Historial

## v1.1 — 2026-08-19

* Se incorpora la relación de autoridad con repositorios asociados.
* Se establece que ELDP referencia, pero no gobierna, el estado permanente de Voces de las Nubes.
* Se añade la detección de contradicciones entre repositorios como evento válido de actualización.

## v1.0 — 2026-08-05

* Primera versión aprobada.
* Establece el procedimiento oficial para actualizar el Sistema de Conocimiento.
* Define los eventos válidos de actualización y las reglas para preservar la trazabilidad del proyecto.
