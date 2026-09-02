# Voces de las Nubes

Corpus lingüístico digital del Didxazá (zapoteco del Istmo) y herramienta de aprendizaje auditivo basada en grabaciones y trabajo con hablantes.

---

## Reentrada desde GitHub

Para continuar el proyecto en un chat nuevo sin depender de memoria de conversaciones ni de paquetes ZIP, leer primero:

`INICIAR_AQUI_CHAT_NUEVO.md`

Ese archivo define el orden de reconstrucción del estado vigente y obliga a distinguir conocimiento canónico, dispositivo experimental, snapshots históricos y pendientes de migración.

---

## Descripción

**Voces de las Nubes** es un proyecto de documentación, aprendizaje y revitalización del Didxazá, la lengua zapoteca del Istmo de Tehuantepec, Oaxaca. Se desarrolla en Casa de las Ciencias de Oaxaca, institución pública dedicada a acompañar a docentes con herramientas pedagógicas y didácticas, bajo el principio de que el conocimiento indígena y el conocimiento científico deben sostener un diálogo en igualdad de condiciones.

El proyecto está dirigido especialmente a personas que tienen la lengua en su historia familiar pero no la recibieron y que hoy carecen de una ruta clara para desarrollar comprensión auditiva y capacidad de conversación.

### Objetivo

Construir materiales de aprendizaje auditivo del Didxazá a partir de situaciones comunicativas reales, mediante:

- grabaciones y trabajo directo con hablantes;
- una progresión organizada por complejidad gramatical y pragmática, todavía en revisión;
- funciones comunicativas y conversación contextualizada;
- documentación lingüística trazable;
- procedimientos de validación con hablantes y especialistas;
- herramientas internas de análisis, revisión, apoyo pedagógico y generación controlada de materiales.

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
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
├── 01_JERARQUIA_DE_VERDAD.md
├── 02_BACKLOG.md
├── 03_REGLAS_DE_ACTUALIZACIÓN.md
├── 04_RELACION_CON_ELDP.md
├── conocimiento/
│   ├── METODOLOGIA.md
│   ├── CORPUS.md
│   ├── AUDIO.md
│   ├── PEDAGOGIA.md
│   ├── TEORIA.md
│   ├── VALIDACION.md
│   ├── BIBLIOGRAFIA.md
│   ├── decisiones/
│   ├── principios/
│   ├── hallazgos/
│   └── fuentes/
├── dispositivo/                         # capa experimental no canónica
├── informes/                            # borradores y productos institucionales
├── contexto-para-reconstruir-base-de-conocimientos/
└── prompts/
```

---

## Sistema de Conocimiento

El proyecto se gobierna mediante un conjunto de documentos versionados que constituyen su memoria permanente.

Reglas centrales:

1. **Una sola fuente de verdad.** Los documentos del sistema prevalecen sobre la memoria de trabajo.
2. **Las contradicciones se documentan, no se ocultan.**
3. **Toda afirmación relevante debe ser trazable** hasta su fuente, justificación, fecha y alcance.
4. **Ninguna modificación silenciosa.** Los cambios sustantivos se registran mediante control de versiones.

`01_JERARQUIA_DE_VERDAD.md` establece qué fuente prevalece según el tipo de pregunta. Para el uso contemporáneo de la lengua, la evidencia oral registrada y la validación comunitaria tienen precedencia sobre la bibliografía.

La carpeta `dispositivo/` conserva el estado de herramientas lingüísticas experimentales que consumen el conocimiento del proyecto. **No constituye una segunda fuente de verdad.** Ningún resultado de esa capa modifica automáticamente `conocimiento/`.

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

### Sistema lingüístico documental

Durante agosto avanzó en paralelo un sistema interno compartido por funciones de análisis, revisión, explicación pedagógica y generación controlada. Esta capa se documenta en `dispositivo/` y permanece explícitamente separada del Sistema de Conocimiento canónico.

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