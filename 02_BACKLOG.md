# BACKLOG

**Proyecto:** Voces de las Nubes  
**Versión:** 2.0  
**Última actualización:** 2026-09-03

---

# Filosofía del backlog

El backlog registra únicamente **deuda estructural permanente del Sistema de Conocimiento**.

No es un planificador general del proyecto y no debe intentar representar todas las tareas operativas en curso.

Una tarea entra al backlog cuando:

- existe una laguna documentada en el Sistema de Conocimiento;
- esa laguna obstaculiza decisiones posteriores o requiere una resolución estructural reutilizable;
- requiere investigación, análisis o formulación no trivial;
- su resolución debe quedar integrada de forma permanente en el sistema.

Una tarea no debe permanecer abierta únicamente porque sería conveniente añadir una referencia cruzada, mejorar una redacción o completar mantenimiento documental menor.

El trabajo operativo —corpus, revisión ortográfica, audio, sesiones con hablantes, solicitudes, producción de materiales— puede continuar fuera del backlog. Solo entra aquí cuando revela una deuda estructural que deba resolverse de forma permanente.

La existencia de una tarea abierta **no implica bloqueo automático**. Conforme a `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`, una pregunta estructural puede permanecer abierta mientras el proyecto continúa produciendo evidencia por vías suficientemente seguras y trazables.

## Relación con el repositorio técnico

Voces de las Nubes puede consultar, citar y usar como coordenadas de recuperación artefactos del repositorio `lopezcarlton/didxaza-dispositivo`.

```text
VOCES_MAY_CONSULT_DEVICE = true
DEVICE_MAY_PROVIDE_TECHNICAL_STATE = true
DEVICE_RESULT_AS_AUTOMATIC_KNOWLEDGE_AUTHORITY = false
```

Una tarea técnica transferida puede conservar aquí una referencia al backlog técnico para mantener genealogía, sin volver a convertirse por ello en deuda activa del Sistema de Conocimiento.

---

# Registro compacto de tareas cerradas o superadas

Los detalles completos permanecen reconstruibles en el historial de Git. Este registro conserva IDs y resultado sin convertir el backlog en archivo histórico extenso.

| ID | Estado | Resultado / destino |
|---|---|---|
| BL-001 | Completado | `01_JERARQUIA_DE_VERDAD.md` |
| BL-002 | Completado | `00_ARQUITECTURA_DEL_CONOCIMIENTO.md` |
| BL-003 | Completado como base operativa | `conocimiento/METODOLOGIA.md` |
| BL-004 | Completado como arquitectura inicial | `conocimiento/CORPUS.md` |
| BL-005 | Completado como base operativa | `conocimiento/VALIDACION.md` |
| BL-006 | Completado como base operativa | `conocimiento/AUDIO.md` |
| BL-007 | Completado como base operativa | `conocimiento/PEDAGOGIA.md` |
| BL-008 | Completado como sistema | `conocimiento/BIBLIOGRAFIA.md` |
| BL-009 | Completado | Preparación de sesiones integrada en `conocimiento/METODOLOGIA.md` |
| BL-010 | Superado como tarea independiente | Referencia cruzada, no deuda estructural |
| BL-011 | Superado como tarea independiente | Incorporar sólo reglas generalizables de validación cuando aparezcan |
| BL-016 | Cerrado | `conocimiento/TEORIA.md` proporciona base operativa evolutiva |
| BL-017 | Transferido | Tarea técnica en `lopezcarlton/didxaza-dispositivo` → `dispositivo/BACKLOG_TECNICO.md` → `DT-001` |
| BL-026 | Completado | Reconciliación bibliográfica BIB001–BIB091 cerrada; nuevas asignaciones sólo desde hoja maestra |

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

### BL-021 — Investigar y formalizar los límites de la escala P

**Estado:** Abierto  
**Prioridad:** Media / investigación continua

Conservar P como escala válida de complejidad pragmático-discursiva y estudiar de manera sistemática sus fronteras P1–P5, la ponderación de sus dimensiones internas y su relación con la experiencia real de aprendices.

La investigación debe partir de la fundamentación pedagógica ya documentada, donde P fue concebida deliberadamente como una medida multidimensional que puede incluir riesgo social, negociación, densidad discursiva y marco reflexivo o metalingüístico.

No se trata de decidir de nuevo si P existe, sino de determinar con evidencia:

- qué distingue de manera reproducible P1, P2, P3, P4 y P5;
- cómo resolver casos donde distintas dimensiones de P divergen;
- si la escala necesita ejemplos de referencia o criterios más explícitos;
- cómo debe relacionarse con futuras secuencias curriculares y usos operativos;
- qué cambios, si alguno, resultan de pruebas con hablantes y aprendices.

**No bloquea:** el piloto actual de COR002 ni la producción de nueva evidencia.

**Dependencias útiles:** escenas aceptadas, realizaciones en Didxazá, corpus oral y validación futura con aprendices.

**Criterio de cierre:** existe una formulación suficientemente reproducible de P1–P5, respaldada por ejemplos y evidencia, o una decisión documentada que sustituye esa formulación por otra arquitectura mejor sustentada.

---

### BL-022 — Investigar la relevancia pedagógica de capas analíticas finas derivadas de BIB065

**Estado:** Abierto  
**Prioridad:** Media / investigación continua

Determinar cuáles de las distinciones descriptivas derivadas de BIB065/Bueno Holle tienen consecuencias pedagógicas reales, cuáles ya quedan suficientemente representadas por G o P, cuáles requieren una descripción adicional y cuáles son únicamente propiedades lingüísticas sin necesidad de convertirse en escala curricular.

Entre las capas candidatas se encuentran:

- introducción, mantenimiento y reintroducción de referentes;
- continuidad y cambio de tópico;
- tipos y posiciones de foco;
- estado informativo e información compartida;
- relaciones entre preguntas y respuestas;
- unidades entonacionales y organización prosódica;
- forma explícita, clítico u omisión según contexto.

La investigación debe volver a la fuente bibliográfica original y contrastarse con escenas, corpus oral, hablantes y aprendices. Voces puede consultar los artefactos correspondientes del dispositivo para localizar estado técnico o preguntas, pero esos artefactos no constituyen la autoridad de esta tarea.

**No bloquea:** COR002, el corpus oral ni otras líneas de investigación.

**Criterio de cierre:** existe una decisión documentada sobre qué relevancia pedagógica tienen las capas priorizadas, o se determina explícitamente que deben permanecer sólo como descripción lingüística.

**Componente técnico relacionado:** la eventual representación computacional de capas ya adjudicadas se sigue en `lopezcarlton/didxaza-dispositivo` → `dispositivo/BACKLOG_TECNICO.md` → `DT-002`.

---

### BL-023 — Definir la segmentación de públicos escolares y perfiles de aprendizaje

**Estado:** Abierto  
**Prioridad:** Alta / estructural

Desarrollar una arquitectura de públicos escolares **dentro del alcance activo de principiantes y escucha**, sin equiparar edad, grado escolar y competencia lingüística. La lectoescritura y los perfiles avanzados quedan fuera del alcance de esta fase.

Debe determinarse con evidencia:

- qué tramos de edad o etapas educativas resultan pedagógicamente útiles;
- qué cambia realmente entre esos segmentos;
- qué papel tiene la trayectoria lingüística familiar;
- qué dimensiones pueden mantenerse comunes;
- cómo probar comprensibilidad, participación y progresión con docentes y estudiantes.

La educación secundaria técnica es el primer anclaje institucional prioritario, pero no cierra el alcance del proyecto.

**Sustento:** `HALL-0009`, `DEC-PUBLICOS-ESCOLARES-MULTIETARIOS`.

**Criterio de cierre:** existe una segmentación suficientemente justificada y revisable, con criterios de adaptación y una ruta de validación escolar.

---

### BL-024 — Localizar e ingerir la Norma de escritura de 2016 y adjudicar fuentes ortográficas contemporáneas

**Estado:** Abierto  
**Prioridad:** Alta / lingüística y documental

La referencia ya fue identificada: Emiliano confirmó que Irma se refería a la **`Norma del sistema de escritura de la lengua zapoteca` de 2016** (`HALL-0021`). La deuda actual es localizar el texto completo, documentar su procedencia y determinar qué textos contemporáneos pueden incorporarse como evidencia ortográfica, con qué alcance y con qué peso.

La tarea debe distinguir:

- versión y procedencia exacta del alfabeto;
- autor, edición, fecha y variedad de cada texto;
- prosa, poesía y otros géneros;
- convención ortográfica compartida frente a decisiones autorales o editoriales;
- variación legítima frente a error suficientemente documentado.

La afirmación atribuida a Irma sobre autores contemporáneos se conserva como evidencia experta recordada, pero **no se convierte todavía en licencia automática de corrección**.

**Criterio de cierre:** existe una política de fuentes ortográficas contemporáneas trazable, vinculada a una versión identificable del Alfabeto Popular y compatible con la variación documentada.

---

### BL-025 — Justificar pedagógicamente la memorización y delimitar su función en Voces de las Nubes

**Estado:** Abierto  
**Prioridad:** Alta / pedagógica e institucional

Voces de las Nubes utiliza memoria y repetición como componentes centrales del aprendizaje, mientras que el entorno docente de Casa de las Ciencias se identifica con principios constructivistas y cuestiona el tedio y la pasividad asociados con la memorización mecánica.

La tarea no es defender toda memorización. Debe distinguir con evidencia:

- repetición pasiva o masiva;
- recuperación activa;
- práctica espaciada;
- memorización de secuencias formulaicas y frases con función comunicativa;
- automatización útil para producción oral;
- reutilización, variación y transferencia;
- carga y tedio según edad y formato.

Debe además explicar qué papel ocupa la memoria dentro de una pedagogía más amplia y comprobar con aprendices que recordar material no se reduzca a recitarlo literalmente.

**Mapa inicial:** `informes/MEMORIZATION_PEDAGOGICAL_JUSTIFICATION_RESEARCH_MAP_v0_1.md`.

**Criterio de cierre:** existe una justificación pedagógica trazable, comprensible para docentes de Casa de las Ciencias y contrastada con pruebas de aprendices, o una reformulación documentada del método si la evidencia muestra límites relevantes.

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

# Estado operativo relacionado con COR002

El modo de trabajo del piloto COR002 está documentado en `conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md`. Ese flujo es trabajo operativo y metodológico vigente, no una entrada adicional de backlog.

La validación del material COR002 continúa abierta: todavía deben producirse escenas de referencia aceptadas, realizarse con hablantes y probarse pedagógicamente. La existencia de una ruta de trabajo definida no equivale a que los materiales resultantes estén validados.

La investigación de P, las capas BIB065, la segmentación de públicos y la justificación de la memorización son deudas estructurales, pero **no se convierten en candados para las líneas de investigación que ya pueden seguir produciendo evidencia**.
