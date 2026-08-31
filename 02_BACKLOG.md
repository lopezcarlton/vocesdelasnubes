# BACKLOG

**Proyecto:** Voces de las Nubes  
**Versión:** 1.4  
**Última actualización:** 2026-08-31

---

# Filosofía del backlog

El backlog registra únicamente **deuda estructural permanente del Sistema de Conocimiento**.

No es un planificador general del proyecto y no debe intentar representar todas las tareas operativas en curso.

Una tarea entra al backlog cuando:

- existe una laguna documentada en el Sistema de Conocimiento;
- esa laguna obstaculiza decisiones posteriores;
- requiere investigación, análisis o formulación no trivial;
- su resolución debe quedar integrada de forma permanente en el sistema.

Una tarea no debe permanecer abierta únicamente porque sería conveniente añadir una referencia cruzada, mejorar una redacción o completar mantenimiento documental menor.

El trabajo operativo —corpus, revisión ortográfica, audio, sesiones con hablantes, solicitudes, producción de materiales— puede continuar fuera del backlog. Solo entra aquí cuando revela una deuda estructural que deba resolverse de forma permanente.

---

# Tareas completadas o superadas

### BL-001 — Establecer la Jerarquía de Verdad
- **Estado:** Completado
- **Documento:** `01_JERARQUIA_DE_VERDAD.md`
- **Fecha:** 2026-06-15

### BL-002 — Definir la Arquitectura del Conocimiento
- **Estado:** Completado
- **Documento:** `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`
- **Fecha:** 2026-06-20

### BL-003 — Formulación de Metodología
- **Estado:** Completado como base operativa; documento evolutivo
- **Documento:** `conocimiento/METODOLOGIA.md`
- **Fecha:** 2026-07-30

### BL-004 — Definición de Corpus
- **Estado:** Completado como arquitectura inicial; documento evolutivo
- **Documento:** `conocimiento/CORPUS.md`
- **Fecha:** 2026-07-15

### BL-005 — Establecer pautas de validación
- **Estado:** Completado como base operativa; documento evolutivo
- **Documento:** `conocimiento/VALIDACION.md`
- **Fecha:** 2026-07-20

### BL-006 — Documentar procedimientos de audio
- **Estado:** Completado como base operativa; sujeto a actualización por trabajo real
- **Documento:** `conocimiento/AUDIO.md`
- **Fecha:** 2026-07-25

### BL-007 — Fundamentación pedagógica
- **Estado:** Completado como base operativa; documento evolutivo
- **Documento:** `conocimiento/PEDAGOGIA.md`
- **Fecha:** 2026-07-22

### BL-008 — Compilar y organizar bibliografía
- **Estado:** Completado como sistema; la bibliografía continúa creciendo
- **Documento:** `conocimiento/BIBLIOGRAFIA.md`
- **Fecha:** 2026-08-01

### BL-009 — Documentar la preparación de materiales para sesiones con hablantes
- **Estado:** Completado
- **Documento:** `conocimiento/METODOLOGIA.md`, sección 12
- **Fecha:** 2026-08-05

### BL-010 — Vincular CORPUS.md con el procedimiento de sesión de validación
- **Estado:** Superado como tarea independiente
- **Fecha:** 2026-08-19
- **Razón:** La tarea describía una referencia cruzada entre documentos, no una deuda metodológica real. El procedimiento vive en `METODOLOGIA.md` y la arquitectura de validación en `CORPUS.md`. La ausencia de un enlace explícito no justifica mantener una tarea activa que obstaculiza la lectura del estado del proyecto. La referencia puede añadirse durante mantenimiento ordinario si resulta útil.

### BL-011 — Actualizar VALIDACION.md con puntos específicos de la sesión
- **Estado:** Superado como tarea independiente
- **Fecha:** 2026-08-19
- **Razón:** Los detalles surgidos de sesiones con hablantes deben incorporarse a `VALIDACION.md` cuando constituyan reglas estables y suficientemente generalizables. No existe actualmente una deuda estructural claramente formulada que justifique mantener este identificador abierto.

### BL-016 — Documentación de teoría del aprendizaje vigente
- **Estado:** Completado como base operativa
- **Documento:** `conocimiento/TEORIA.md`
- **Fecha de cierre:** 2026-08-19
- **Razón:** La descripción anterior decía incorrectamente que `TEORIA.md` permanecía vacío. El documento ya contiene marcos de adquisición, revitalización, estructura del Didxazá y decisiones pedagógicas. La teoría seguirá evolucionando, pero esa evolución normal no constituye por sí misma una tarea abierta de backlog.

---

# Tareas abiertas

### BL-012 — Prueba de procedimiento con nuevo hablante

**Estado:** Abierto  
**Prioridad:** Alta

Aplicar el procedimiento de trabajo documentado con un segundo hablante para comprobar su reproducibilidad y registrar qué ajustes exige la práctica.

**Responsable:** Emiliano  
**Dependencias:** disponibilidad de un segundo hablante.

---

### BL-013 — Formalización de acuerdos con hablantes

**Estado:** Abierto  
**Prioridad:** Alta

Desarrollar un protocolo formal de consentimiento, uso de materiales, reconocimiento de autoría, atribución, acceso y participación, suficientemente claro para utilizarse con colaboradores del proyecto.

**Responsable:** Emiliano + Institución

---

### BL-014 — Sistema de control externo de cobertura

**Estado:** Abierto  
**Prioridad:** Media

Establecer un sistema reutilizable que permita controlar situaciones, patrones, léxico, balance entre dominios y dependencias entre funciones sin depender de la memoria de una sesión o de un modelo.

**Responsable:** Emiliano

---

### BL-015 — Validación pedagógica con aprendices

**Estado:** Abierto  
**Prioridad:** Posterior

Realizar pruebas con aprendices reales para validar comprensibilidad, pausas, dificultad, transferencia, retención y disposición de uso.

No es una tarea inmediata. Requiere materiales suficientemente maduros y acuerdos de participación.

**Responsable:** Emiliano + apoyo especializado cuando corresponda.

---

### BL-017 — Evaluación futura del generador de borradores

**Estado:** Abierto  
**Prioridad:** Posterior al piloto de escenas de referencia

Evaluar el desempeño de un generador de borradores en español: aceptación por hablantes, artificialidad, errores, cobertura y utilidad real.

**Actualización 2026-08-31:** El generador v7 y las iteraciones v8.x se conservan como antecedentes experimentales, pero no constituyen el motor activo de COR002. El piloto actual suspende la generación masiva y prioriza obtener primero unas pocas escenas de referencia aceptadas mediante revisión manual y trabajo con hablantes.

Esta tarea se reactivará cuando exista suficiente evidencia concreta para decidir qué debe hacer un generador nuevo o reducido. No se considera necesario evaluar v7 “a escala” como requisito previo.

**Responsable:** Emiliano

---

### BL-018 — Formalización del estatus de Emiliano López Carlton

**Estado:** Abierto  
**Prioridad:** Alta

Formalizar con la institución rol, tiempo asignado, reconocimiento, autoridad sobre decisiones, acceso a recursos y continuidad del proyecto.

**Responsable:** Institución + Emiliano

---

### BL-019 — Publicación y acceso a materiales

**Estado:** Abierto  
**Prioridad:** Media / posterior

Definir canales de publicación, niveles de acceso, términos de uso, formatos de distribución, plataformas y procedimientos de actualización.

**Dependencias principales:** acuerdos con participantes y madurez suficiente de los materiales.

---

### BL-020 — Validar el inventario léxico base de COR002

**Estado:** Abierto  
**Prioridad:** Alta

Identificar el inventario léxico vigente que servirá como referencia para COR002 y someterlo a revisión con Vicente Gutiérrez para documentar naturalidad, variantes, uso contemporáneo, duplicados, vacíos, contexto y observaciones de escritura cuando puedan validarse con seguridad.

**Actualización 2026-08-31:** La tarea estructural permanece abierta, pero ya no bloquea el inicio del piloto. Para las primeras escenas se revisará primero el léxico que efectivamente entre en ellas. El inventario general podrá consolidarse progresivamente a partir de ese trabajo y de la revisión específica con Vicente.

**Responsable:** Emiliano López Carlton  
**Validador:** Vicente Gutiérrez

**Criterio de cierre:** existe un inventario identificable y reutilizable con términos aceptados, rechazados o sustituidos, observaciones relevantes de variación y vacíos documentados.

---

# Criterios de cierre

Una tarea estructural se considera completada cuando:

1. existe una solución documentada o una decisión explícita que elimina la laguna;
2. otros pueden trabajar sin depender de reconstruir el problema desde conversaciones anteriores;
3. la solución está integrada en el lugar pertinente del Sistema de Conocimiento;
4. se ha validado según corresponda.

Una tarea también puede declararse **superada como tarea independiente** cuando una revisión demuestra que nunca constituyó deuda estructural suficiente para justificar su mantenimiento en el backlog.

---

# Regla de mantenimiento

El backlog debe mantenerse pequeño y legible.

No se abrirán tareas por mantenimiento editorial menor, referencias cruzadas triviales o evolución normal de documentos que ya cumplen su función.

Si mantener una entrada cuesta más trabajo que la deuda que representa, debe revisarse si realmente pertenece al backlog.

---

# Nota de estado 2026-08-31

El modo de trabajo del piloto COR002 quedó definido en `conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md`. Ese flujo es trabajo operativo y metodológico vigente, no una nueva entrada de backlog.

La validación del material COR002 continúa abierta por razones documentadas en `conocimiento/VALIDACION.md`: todavía deben producirse escenas de referencia aceptadas, realizarse con hablantes y probarse pedagógicamente. La existencia de una ruta de trabajo ya definida no equivale a que los materiales resultantes estén validados.
