# Voces de las Nubes

Corpus lingüístico digital del Didxazá (zapoteco del Istmo) y herramienta de aprendizaje auditivo basada en grabaciones de hablantes nativos.

---

## Descripción

**Voces de las Nubes** es un proyecto de documentación y revitalización del Didxazá, la lengua zapoteca del Istmo de Tehuantepec, Oaxaca. Se desarrolla en Casa de las Ciencias de Oaxaca, institución pública dedicada a acompañar a docentes con herramientas pedagógicas y didácticas, bajo el principio de que el conocimiento indígena y el conocimiento científico tienen el mismo valor y deben sostener un diálogo en igualdad de condiciones.

El proyecto está dirigido especialmente a personas que tienen la lengua en su historia familiar pero no la recibieron, y que hoy carecen de recursos para aprenderla por cuenta propia.

### Objetivo

Construir materiales de aprendizaje auditivo del Didxazá a partir de situaciones comunicativas reales, mediante:

- grabaciones de hablantes nativos;
- una progresión organizada por complejidad gramatical y pragmática;
- documentación lingüística trazable;
- procedimientos de validación con hablantes y especialistas.

---

## Complejidad dual

El proyecto separa actualmente dos ejes de dificultad:

**Eje gramatical (G1–G5)** — qué estructuras lingüísticas está permitido usar.

**Eje pragmático (P1–P5)** — qué profundidad de contenido y qué registro se incluyen.

El eje gramatical opera como restricción dura y el pragmático como restricción blanda. Esta arquitectura está vigente como marco de trabajo, pero **no se considera terminada**. Debe seguir revisándose a la luz de la evidencia lingüística y gramatical que el proyecto continúa extrayendo y validando. Las decisiones y principios relacionados están documentados en `conocimiento/decisiones/` y `conocimiento/principios/`.

---

## Estructura del repositorio

```
vocesdelasnubes/
├── README.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md   # Organización del sistema
├── 01_JERARQUIA_DE_VERDAD.md             # Resolución de conflictos entre fuentes
├── 02_BACKLOG.md                         # Deuda técnica del sistema
├── 03_REGLAS_DE_ACTUALIZACIÓN.md         # Cómo se modifica el sistema
├── 04_RELACION_CON_ELDP.md               # Frontera de autoridad con la candidatura ELDP
├── conocimiento/
│   ├── METODOLOGIA.md                    # Cómo trabaja el proyecto
│   ├── CORPUS.md                         # Arquitectura del corpus
│   ├── AUDIO.md                          # Producción y postproducción de audio
│   ├── PEDAGOGIA.md                      # Diseño pedagógico
│   ├── TEORIA.md                         # Marcos teóricos adoptados
│   ├── VALIDACION.md                     # Procedimientos de validación
│   ├── BIBLIOGRAFIA.md                   # Sistema de fichas bibliográficas
│   ├── decisiones/                       # Decisiones formales del proyecto
│   ├── principios/                       # Principios de diseño
│   ├── hallazgos/                        # Hallazgos documentados
│   └── fuentes/                          # Fuentes de razonamiento
├── contexto-para-reconstruir-base-de-conocimientos/
└── prompts/
```

---

## Sistema de Conocimiento

El proyecto se gobierna mediante un conjunto de documentos versionados que constituyen su memoria permanente. Cuatro reglas lo rigen:

1. **Una sola fuente de verdad.** Los documentos del sistema prevalecen sobre la memoria de trabajo.
2. **Las contradicciones se documentan, no se ocultan.** Ninguna evidencia se elimina para preservar coherencia documental.
3. **Toda afirmación es trazable** hasta su fuente, justificación, fecha y alcance.
4. **Ninguna modificación silenciosa.** Los cambios al sistema se proponen, se aprueban y se registran.

`01_JERARQUIA_DE_VERDAD.md` establece qué fuente prevalece según el tipo de pregunta. Para el uso contemporáneo de la lengua, la evidencia oral registrada y la validación comunitaria tienen precedencia sobre la bibliografía.

La relación con la candidatura al Small Grant de ELDP se regula en `04_RELACION_CON_ELDP.md`: este repositorio conserva la autoridad sobre el estado lingüístico, pedagógico, metodológico y operativo de Voces de las Nubes; el repositorio ELDP conserva la autoridad sobre la candidatura.

---

## Estado del proyecto

**COR001 — abierto, en consolidación final.** El corpus inicial de 107 frases ya fue grabado y procesado en una primera etapa, pero todavía no está cerrado. Permanecen pendientes la revisión y corrección ortográfica de las traducciones, correcciones derivadas de esa revisión, regrabación de algunos materiales que no quedaron adecuadamente, normalización final del audio y las entregas finales para Anki y para distribución de audio. El proyecto está desarrollando fuera de este repositorio un procedimiento automatizado de corrección ortográfica que todavía no se incorpora formalmente al Sistema de Conocimiento.

**COR002 — en revisión profunda, sin versión definitiva.** El borrador anterior fue descartado tras detectar repeticiones, baja productividad y selección insuficientemente comunicativa. Existe trabajo posterior sobre situaciones y complejidad dual, pero su arquitectura sigue abierta a cambios importantes. Se espera la revisión de Vicente Gutiérrez y deben volver a revisarse las situaciones, la arquitectura G/P y su relación con la evidencia gramatical y lingüística que continúa extrayéndose de la literatura disponible. **No se ha realizado ninguna grabación de COR002.** El generador vigente tampoco debe considerarse estable mientras este trabajo continúe.

**Metodología, teoría y pedagogía — consolidadas como base de trabajo, pero evolutivas.** Los documentos actuales permiten operar y tomar decisiones, pero no se consideran cerrados: deben seguir cambiando cuando nueva evidencia del proyecto, de hablantes o de fuentes especializadas lo justifique.

El trabajo pendiente del Sistema de Conocimiento se registra en `02_BACKLOG.md` únicamente cuando constituye deuda estructural permanente; el backlog no debe utilizarse como planificador general de todas las actividades operativas.

---

## Créditos

**Coordinación:** Emiliano López Carlton
**Validación lingüística:** Vicente Gutiérrez
**Hablantes:** Comunidad del Istmo de Tehuantepec
**Institución:** Casa de las Ciencias de Oaxaca (CaCiO)

---

## Licencia y acceso

La licencia del corpus está **por definir**. Requiere acuerdos comunitarios previos sobre uso, autoría y distribución (ver BL-013 y BL-019 en el backlog).

Los materiales de audio y las transcripciones no se publican en este repositorio. El repositorio contiene únicamente el Sistema de Conocimiento del proyecto.

---

## Cita

```
López Carlton, E. (2026). Voces de las Nubes: corpus digital del Didxazá.
Casa de las Ciencias de Oaxaca.
https://github.com/lopezcarlton/vocesdelasnubes
```

---

## Contacto

lopezcarlton@gmail.com
