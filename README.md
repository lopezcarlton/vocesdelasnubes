# Voces de las Nubes

Corpus lingüístico digital del Didxazá (zapoteco del Istmo) y herramienta de aprendizaje auditivo basada en grabaciones y trabajo con hablantes.

---

## Reentrada desde GitHub

Para continuar **Voces de las Nubes** en un chat nuevo sin depender de memoria de conversaciones ni de paquetes ZIP, leer primero:

`INICIAR_AQUI_CHAT_NUEVO.md`

Ese archivo reconstruye por defecto el **Sistema de Conocimiento**: arquitectura, fuentes, hallazgos, decisiones, teoría, metodología, pedagogía, corpus y validación.

El trabajo explícitamente técnico sobre Analyzer, Corrector, Tutor, Generator, runtime, pruebas o migración tiene un punto de entrada separado:

`dispositivo/REENTRY_TECNICO.md`

La separación de reentrada evita que una conversación pedagógica o bibliográfica cargue por defecto el estado de implementación y evita que el dispositivo adquiera autoridad por proximidad documental.

---

## Descripción

**Voces de las Nubes** es un proyecto de documentación, aprendizaje y revitalización del Didxazá, la lengua zapoteca del Istmo de Tehuantepec, Oaxaca. Se desarrolla en Casa de las Ciencias de Oaxaca, institución pública dedicada a acompañar a docentes con herramientas pedagógicas y didácticas, bajo el principio de que el conocimiento indígena y el conocimiento científico deben sostener un diálogo en igualdad de condiciones.

El proyecto incluye a personas que tienen la lengua en su historia familiar pero no la recibieron y, desde septiembre de 2026, adopta además como requisito explícito el diseño para **públicos escolares diferenciados por edad y trayectoria lingüística**. La educación secundaria técnica constituye el primer anclaje institucional prioritario por la relación de Casa de las Ciencias de Oaxaca con ese nivel, sin convertirse en público exclusivo.

### Objetivo

Construir materiales de aprendizaje auditivo del Didxazá a partir de situaciones comunicativas reales, mediante:

- grabaciones y trabajo directo con hablantes;
- una progresión organizada por complejidad gramatical y pragmática, todavía en revisión;
- funciones comunicativas y conversación contextualizada;
- documentación lingüística trazable;
- procedimientos de validación con hablantes y especialistas;
- herramientas internas subordinadas al Sistema de Conocimiento para análisis, revisión, apoyo pedagógico y producción controlada de materiales.

---

## Complejidad dual

El proyecto separa actualmente dos ejes de dificultad:

**Eje gramatical (G1–G5)** — estructuras lingüísticas que el material intenta introducir o elicitar de manera controlada.

**Eje pragmático (P1–P5)** — profundidad de contenido, relación entre interlocutores y exigencia comunicativa.

Esta arquitectura está vigente como marco de trabajo, pero **no se considera terminada ni equivale automáticamente a un currículo del aprendiz**. Debe seguir revisándose a la luz de evidencia lingüística, conversación real, trabajo con hablantes y experiencia pedagógica.

---

## Estructura del repositorio

```text
vocesdelasnubes/
├── README.md
├── INICIAR_AQUI_CHAT_NUEVO.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
├── 01_JERARQUIA_DE_VERDAD.md
├── 02_BACKLOG.md
├── 03_REGLAS_DE_ACTUALIZACIÓN.md
├── 04_RELACION_CON_ELDP.md
├── conocimiento/        # Sistema de Conocimiento y vistas canónicas
├── informes/            # investigación/auditorías no normativas
├── archivo/             # historia, checkpoints y contextos
├── dispositivo/         # sistema derivado temporal, pendiente de separación
└── .github/
```

La raíz se mantiene deliberadamente pequeña. Los checkpoints fechados y contextos históricos no viven en la raíz y no gobiernan el estado vigente.

---


## Sistema de Conocimiento

El proyecto se gobierna mediante un conjunto de documentos versionados que constituyen su memoria permanente.

Reglas centrales:

1. **Una sola fuente de verdad.** Los documentos del sistema prevalecen sobre la memoria de trabajo.
2. **Las contradicciones se documentan, no se ocultan.**
3. **Toda afirmación relevante debe ser trazable** hasta su fuente, justificación, fecha y alcance.
4. **Ninguna modificación silenciosa.** Los cambios sustantivos se registran mediante control de versiones.
5. **Los sistemas derivados no adoptan conocimiento.** Pueden leer, analizar, detectar problemas y proponer candidatos; la incorporación requiere adjudicación dentro de Voces de las Nubes.

`01_JERARQUIA_DE_VERDAD.md` establece qué autoridad prevalece según el tipo de pregunta y cómo se relacionan `SRC`, `HALL`, `VAL`, `SUP`, `TEO`, `DEC`, `PRIN`, procedimientos y vistas documentales.

La carpeta `dispositivo/` conserva temporalmente el estado de herramientas lingüísticas experimentales que consumen conocimiento del proyecto. **No constituye una segunda fuente de verdad y no tiene autoridad para escribir, adoptar o promover conocimiento.** La regla vigente se documenta en `conocimiento/decisiones/DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO.md`.

---

## Estado del proyecto — cierre de agosto 2026

### COR001

**Artefacto históricamente abierto; rol operativo actual: `ANALYSIS_TARGET_ONLY`.**

COR001 contiene 107 frases. El trabajo lingüístico y la grabación fueron realizados con **Vicente Gutiérrez**, hasta ahora el único colaborador activo y sostenido en esta fase. Vicente realizó las traducciones al Didxazá y la grabación.

El estudio intensivo del material mostró resultados claros en familiaridad auditiva, vocabulario y memorización, pero también límites de cobertura, velocidad de recuperación y capacidad de sostener una conversación abierta.

Permanecen pendientes la revisión ortográfica, correcciones derivadas, algunas regrabaciones, normalización final del audio y productos finales de estudio.

Estos pendientes describen el estado histórico del corpus y sus productos. **No constituyen una cola activa de resolución caso por caso ni autorizan usar COR001 como benchmark, gold, regresión o fuente de reglas.**

### COR002

**En desarrollo, sin audio y sin versión definitiva.**

El banco activo se ha reducido a **46 situaciones comunicativas**. Se retiraron "Ir al médico" y "Comprar medicina / ir a la farmacia" porque se consideró que esas interacciones probablemente ocurren principalmente en español y no son prioridades adecuadas para el corpus inicial de uso del Didxazá.

La arquitectura actual distingue:

- situación;
- función comunicativa;
- objetivo lingüístico/pedagógico;
- relación entre interlocutores;
- núcleo funcional;
- léxico de escena y reciclaje;
- complejidad gramatical y pragmática.

La conversación completa es la unidad primaria del corpus; fragmentos, microescenas y ejercicios se derivan después para el estudio.

### Ampliación metodológica de agosto

A partir de la revisión de Juan José Bueno Holle (2019), el proyecto incorporó una vía complementaria de construcción y comprobación del corpus:

- habla espontánea o relativamente libre;
- elicitación dirigida mediante estímulos no lingüísticos;
- juicios explícitos de hablantes;
- conservación de la procedencia de cada dato;
- separación entre grabación primaria y capas posteriores de transcripción, traducción y análisis.

Esta ampliación **no reemplaza** las escenas pedagógicamente diseñadas ni la traducción/reformulación con hablantes. Añade fuentes independientes de evidencia y reduce la dependencia de estructuras proyectadas desde el español.

### Sistema derivado de apoyo

Durante agosto avanzó en paralelo una capa experimental para análisis, revisión, explicación y producción controlada. Se conserva bajo `dispositivo/` por genealogía y reproducibilidad técnica, pero su autoridad está subordinada al Sistema de Conocimiento. Los descubrimientos que surjan durante su desarrollo deben volver a las fuentes originales y al procedimiento de actualización antes de modificar teoría, pedagogía, metodología o corpus.

### ELDP

**No existe una candidatura activa.** El ciclo exploratorio de ELDP 2026 fue cerrado. El repositorio `lopezcarlton/ELDP` se conserva únicamente como archivo de conocimiento y antecedente para una posible iniciativa futura.

---

## Créditos

**Coordinación:** Emiliano López Carlton  
**Colaborador lingüístico activo en COR001:** Vicente Gutiérrez  
**Institución:** Casa de las Ciencias de Oaxaca (CaCiO)

Las futuras colaboraciones se acreditarán según su participación efectiva y alcance.

---

## Licencia y acceso

La licencia del corpus está **por definir**. Requiere acuerdos previos sobre uso, autoría y distribución.

Los materiales de audio y las transcripciones no se publican en este repositorio. El repositorio contiene principalmente el Sistema de Conocimiento, documentación metodológica y capas internas de trabajo.

---

## Cita

```text
López Carlton, E. (2026). Voces de las Nubes: corpus digital del Didxazá.
Casa de las Ciencias de Oaxaca.
https://github.com/lopezcarlton/vocesdelasnubes
```

---

## Contacto

lopezcarlton@gmail.com