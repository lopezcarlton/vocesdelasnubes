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

La decisión de diseño central del proyecto es separar explícitamente dos ejes de dificultad:

**Eje gramatical (G1–G5)** — qué estructuras lingüísticas está permitido usar.

**Eje pragmático (P1–P5)** — qué profundidad de contenido y qué registro se incluyen.

El eje gramatical opera como restricción dura; el pragmático, como restricción blanda. Esto permite que el aprendiz avance en estructura sin que la carga conceptual lo rebase. Las decisiones y principios que sustentan esta separación están documentados en `conocimiento/decisiones/` y `conocimiento/principios/`.

---

## Estructura del repositorio

```
vocesdelasnubes/
├── README.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md   # Organización del sistema
├── 01_JERARQUIA_DE_VERDAD.md             # Resolución de conflictos entre fuentes
├── 02_BACKLOG.md                         # Deuda técnica del sistema
├── 03_REGLAS_DE_ACTUALIZACIÓN.md         # Cómo se modifica el sistema
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

---

## Estado del proyecto

**COR001** — corpus inicial de frases básicas, grabado y procesado.

**COR002** — en construcción. El borrador original fue descartado tras una revisión crítica que detectó repeticiones, baja productividad y selección por valor poético más que comunicativo. La versión actual se organiza según la arquitectura de complejidad dual. Se encuentra en revisión y traducción con hablante nativo. **No se ha realizado ninguna grabación de COR002.**

El trabajo pendiente del Sistema de Conocimiento está registrado en `02_BACKLOG.md`.

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
