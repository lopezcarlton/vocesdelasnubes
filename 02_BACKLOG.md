# BACKLOG

**Proyecto:** Voces de las Nubes

**Versión:** 1.2

**Última actualización:** 2026-08-06

---

# Filosofía del backlog

El backlog representa la deuda técnica permanente del Sistema de Conocimiento.

Una tarea entra al backlog cuando:

- existe una laguna documentada en el Sistema de Conocimiento;
- esa laguna obstaculiza decisiones posteriores;
- la laguna requiere investigación, análisis o formulación;
- la solución no es evidente ni inmediata.

Una tarea sale del backlog cuando:

- se ha documentado la solución en el sistema;
- esa solución ha sido validada según corresponda;
- se ha integrado en el documento pertinente;
- está disponible como referencia para trabajo futuro.

---

# Separación entre tarea activa y trabajo operativo

La tarea activa del backlog representa la deuda técnica prioritaria del Sistema de Conocimiento. El trabajo operativo del proyecto (corpus, audio, sesiones con hablantes, solicitudes) puede continuar en paralelo. Solo se registran nuevas tareas cuando el trabajo real genera deuda permanente.

---

# Estado actual

## Tareas completadas

### BL-001 — Establecer la Jerarquía de Verdad

- **Estado:** Completado
- **Documento:** `01_JERARQUIA_DE_VERDAD.md`
- **Fecha:** 2026-06-15

### BL-002 — Definir la Arquitectura del Conocimiento

- **Estado:** Completado
- **Documento:** `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`
- **Fecha:** 2026-06-20

### BL-003 — Formulación de Metodología

- **Estado:** Completado
- **Documento:** `conocimiento/METODOLOGIA.md`
- **Fecha:** 2026-07-30

### BL-004 — Definición de Corpus

- **Estado:** Completado
- **Documento:** `conocimiento/CORPUS.md`
- **Fecha:** 2026-07-15

### BL-005 — Establecer pautas de validación

- **Estado:** Completado
- **Documento:** `conocimiento/VALIDACION.md`
- **Fecha:** 2026-07-20

### BL-006 — Documentar procedimientos de audio

- **Estado:** Completado
- **Documento:** `conocimiento/AUDIO.md`
- **Fecha:** 2026-07-25

### BL-007 — Fundamentación pedagógica

- **Estado:** Completado
- **Documento:** `conocimiento/PEDAGOGIA.md`
- **Fecha:** 2026-07-22

### BL-008 — Compilar y organizar bibliografía

- **Estado:** Completado
- **Documento:** `conocimiento/BIBLIOGRAFIA.md`
- **Fecha:** 2026-08-01

### BL-009 — Documentar la preparación de materiales para sesiones con hablantes

- **Estado:** Completado
- **Documento:** `conocimiento/METODOLOGIA.md` (sección 12)
- **Criterio de cierre alcanzado:** Se documentó el procedimiento metodológico de validación con hablantes a partir de evidencia obtenida durante las primeras sesiones del proyecto. Integrado en METODOLOGIA.md sección 12.
- **Fecha:** 2026-08-05

---

## Tareas pendientes

### BL-010 — Actualizar CORPUS.md con procedimiento de sesión

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Integrar la sección 12 de METODOLOGIA.md (sesión de validación) en CORPUS.md sección 4.5, reemplazando la descripción incompleta de "elicitación y construcción con hablantes".

**Responsable:** Emiliano
**Dependencias:** BL-009 (Completado)

---

### BL-011 — Actualizar VALIDACION.md con puntos de validación específicos

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Expandir VALIDACION.md con los puntos de validación específicos de la sesión de hablantes (rechazo, reformulación, audio, regrabación en español, inventario léxico). Referencia: METODOLOGIA.md sección 12.

**Responsable:** Emiliano
**Dependencias:** BL-009 (Completado)

---

### BL-012 — Prueba de procedimiento con nuevo hablante

**Estado:** Abierto
**Prioridad:** Alta

**Descripción**

Aplicar el procedimiento documentado en METODOLOGIA.md sección 12 con un segundo hablante para validar que el procedimiento es reproducible y que genera decisiones consistentes. Recolectar evidencia de funcionamiento.

**Responsable:** Emiliano
**Dependencias:** BL-009 (Completado)

---

### BL-013 — Formalización de acuerdos con hablantes

**Estado:** Abierto
**Prioridad:** Alta

**Descripción**

Desarrollar un protocolo formal de consentimiento, uso de materiales, reconocimiento de autoría y participación. Debe ser claro, accesible en español, y acordado con los colaboradores participantes.

**Responsable:** Emiliano + Institución
**Dependencias:** BL-009 (recomendable), disponibilidad legal/institucional

---

### BL-014 — Sistema de control externo de cobertura

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Establecer un sistema (herramienta, registro, formato) que mantenga control sobre:

- situaciones cubiertas;
- patrones introducidos;
- léxico acumulado;
- balance entre dominios;
- dependencias entre funciones.

Este sistema debe permitir al coordinador tomar decisiones sobre qué generar a continuación sin confiar únicamente en la memoria.

**Responsable:** Emiliano
**Dependencias:** Ninguna inmediata

---

### BL-015 — Validación pedagógica con aprendices

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Realizar pruebas con aprendices reales para validar:

- comprensibilidad del material;
- pausas de duración adecuada;
- nivel de dificultad;
- transferencia a contextos nuevos;
- retención después del uso;
- disposición para seguir usando la herramienta.

Requiere consentimiento informado de participantes y protocolos de investigación.

**Responsable:** Emiliano + Especialista en evaluación pedagógica
**Dependencias:** BL-013 (acuerdos con participantes)

---

### BL-016 — Documentación de teoría del aprendizaje vigente

**Estado:** Abierto
**Prioridad:** Baja

**Descripción**

TEORIA.md existe pero permanece vacío. Desarrollar una sección sobre qué teorías de adquisición de segunda lengua informan el diseño de Voces de las Nubes. Puede incluir: hipótesis de input comprensible (Krashen), output (Swain), conexión de forma-significado (VanPatten y Herschensohn), perspectivas socioculturales, etc.

**Responsable:** Emiliano + Especialista en lingüística aplicada
**Dependencias:** BL-004, BL-007 (ya completados)

---

### BL-017 — Evaluación del generador de borradores vigente

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Realizar análisis sobre el desempeño del modelo automático que genera borradores en español. Métricas: tasa de aceptación por hablantes, tipos de errores más frecuentes, cobertura de funciones, falsos positivos (frases artificiales).

**Responsable:** Emiliano + Especialista en LLM/evaluación
**Dependencias:** Ninguna inmediata

---

### BL-018 — Formalización del estatus de Emiliano López Carlton

**Estado:** Abierto
**Prioridad:** Alta

**Descripción**

Acuerdo formal entre Emiliano y la institución sobre rol, tiempo asignado, reconocimiento, autoridad sobre decisiones, acceso a recursos, y continuidad del proyecto. Necesario para evitar ambigüedades administrativas y para clarificar límites de responsabilidad.

**Responsable:** Institución + Emiliano
**Dependencias:** Institucional

---

### BL-019 — Publicación y acceso a materiales

**Estado:** Abierto
**Prioridad:** Media

**Descripción**

Definir canales de publicación, niveles de acceso (interno/público), términos de uso, formatos de distribución, plataformas tecnológicas y procedimientos de actualización. Requiere análisis de audiencia, sostenibilidad técnica y acuerdos comunitarios.

**Responsable:** Emiliano + Institución + Especialista en tecnología educativa
**Dependencias:** BL-013 (acuerdos), BL-015 (validación)

---

### BL-020 — Validar el inventario léxico base de COR002

**Estado:** Abierto
**Prioridad:** Alta

**Descripción**

Identificar el inventario léxico vigente que servirá como base para COR002 y someterlo a revisión con Vicente Gutiérrez para documentar:

- naturalidad de los términos propuestos;
- variantes por localidad cuando correspondan;
- correspondencia con el uso contemporáneo;
- duplicados o vacíos relevantes;
- contextos de uso adecuados;
- observaciones sobre escritura según el Alfabeto Popular vigente cuando Vicente pueda validarla con seguridad.

La tarea no se considera cerrada únicamente por realizar la sesión. Debe producir un inventario identificable y reutilizable dentro del Sistema de Conocimiento.

**Responsable:** Emiliano López Carlton
**Validador:** Vicente Gutiérrez

**Dependencias:**

- identificar y fijar la versión del inventario léxico que será revisada;
- disponibilidad de Vicente para la sesión de validación.

**Criterio de cierre:**

- existe una versión identificable del inventario léxico revisado;
- quedan registrados términos aceptados, rechazados o sustituidos;
- se documentan observaciones de variación y contexto cuando existan;
- los vacíos relevantes detectados quedan registrados;
- el resultado puede utilizarse como referencia para COR002 y trabajo posterior.

**Fecha objetivo:** A acordar con Vicente.

---

# Criterios de cierre

Una tarea se considera completada cuando:

1. Existe un documento en el Sistema de Conocimiento que resuelve la necesidad.
2. El documento es suficiente para que otros tomen decisiones o ejecuten trabajo basado en él.
3. Ha sido validado según corresponde (por hablantes, especialistas o coordinación).
4. Está integrado en el lugar pertinente de la arquitectura.
5. Es referenciable — tiene título, sección o identificador claro.

Una tarea se reabre si:

- la evidencia posterior contradice la solución adoptada;
- el trabajo operativo revela que la solución es insuficiente;
- aparece información que obliga a revisar la decisión;
- el documento fue completado con alcance limitado que requiere expansión.

---

# Notas

- Este backlog es un registro de deuda técnica permanente, no un planificador de todas las actividades del proyecto.
- Las actividades operativas (grabación, edición, trabajo de campo, solicitudes administrativas) no entran aquí a menos que generen una laguna documentacional.
- La primera sesión de COR002 con `DEC-GRABAR-EN-VIVO` es trabajo operativo y, por tanto, no se registra como BL-021. Su función de validación queda documentada en la decisión y en `conocimiento/AUDIO.md`.
- Cada entrada debe incluir: descripción clara, responsable, prioridad relativa, dependencias, criterio de cierre.
- El estado se revisa regularmente. Las revisiones deben quedar registradas en el historial del documento.
