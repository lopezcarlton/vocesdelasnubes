# DISPOSITIVO LINGÜÍSTICO — CAPA EXPERIMENTAL

**Proyecto:** Voces de las Nubes  
**Estado:** no canónico / experimental  
**Fecha de creación:** 2026-08-31

## Propósito

Esta carpeta documenta el trabajo interno desarrollado en paralelo para convertir el conocimiento lingüístico del proyecto en capacidades operativas de:

- análisis;
- revisión y normalización;
- explicación pedagógica;
- generación controlada de estímulos y materiales.

La carpeta existe para evitar que ese trabajo quede disperso entre chats, bases locales, scripts, paquetes de migración y documentos técnicos.

## Regla fundamental

**`dispositivo/` no es una segunda fuente de verdad lingüística.**

El Sistema de Conocimiento canónico permanece en `conocimiento/` y en los documentos constitucionales del repositorio.

El dispositivo:

- consume conocimiento documentado;
- representa hipótesis de forma ejecutable;
- prueba reglas y relaciones;
- detecta vacíos o contradicciones;
- puede producir candidatos de análisis o revisión.

El dispositivo **no puede modificar automáticamente el conocimiento canónico**.

Cuando una prueba del dispositivo revele un hallazgo relevante, éste debe seguir el procedimiento normal del proyecto:

> evidencia → hallazgo → revisión → decisión → incorporación al Sistema de Conocimiento

## Investigación abierta

El dispositivo se rige por `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`.

Su función es ampliar la capacidad de investigar, no cerrar la investigación. Una representación implementada puede ser provisional, quedar superseded, ser útil sólo para una prueba o necesitar revisión posterior.

```text
IMPLEMENTED_CAPABILITY != RESEARCH_AUTHORITY
MIGRATED_ARTIFACT != IMMUTABLE_RULE
CURRENT_RUNTIME != FINAL_ARCHITECTURE
```

La reproducibilidad exige saber qué se utilizó en una prueba concreta; no exige mantenerlo indefinidamente cuando nueva evidencia justifique cambiarlo.

## Relación con los cuatro componentes

La arquitectura de trabajo distingue cuatro funciones que comparten un núcleo lingüístico:

### ANALYZER

Intenta reconocer estructura, morfología, persona, aspecto, referencia, procedencia y otras capas documentadas sin convertir automáticamente un análisis plausible en verdad.

Su alcance requerido es multiescala: palabra o forma aislada, frase/enunciado, microescena, conversación completa y discurso continuo cuando exista. El contexto enriquece el análisis, pero no se convierte en requisito universal.

Referencia: `ANALYZER_SCOPE_MULTIESCALA_2026-08-31.md`.

### CORRECTOR

Busca distinguir entre:

- forma documentada;
- variante;
- error suficientemente respaldado;
- normalización posible;
- caso no resuelto.

Debe conservar siempre la forma original y abstenerse cuando la evidencia no sea suficiente.

### TUTOR

Transforma conocimiento documentado en explicaciones pedagógicas por capas. Debe distinguir con claridad qué parte de una explicación proviene de una fuente, qué parte es análisis y qué parte permanece incierta.

### GENERATOR

Ayuda a construir situaciones, escenas, estímulos y restricciones para el corpus. No debe usar el español como plantilla gramatical dominante ni tratar una propuesta generada como Didxazá validado.

El español continúa siendo el puente semántico y de trabajo vigente del sistema. Al 2026-08-31 no existe una decisión de sustituirlo por una representación previa obligatoria. Cualquier arquitectura alternativa deberá discutirse y adoptarse explícitamente antes de modificar este principio.

## Núcleo compartido

Los cuatro componentes deben consumir un núcleo lingüístico común para evitar que cada uno mantenga reglas propias incompatibles.

Entre los artefactos desarrollados fuera del repositorio se encuentra `JUCHITAN_LINGUISTIC_CORE`, actualmente experimental, además de bases, runtimes, inventarios, pruebas y paquetes de migración.

La incorporación de esta carpeta **no implica que todos esos artefactos hayan sido migrados ya al repositorio**. El estado exacto se registra en `ESTADO_ACTUAL_2026-08-31.md`.

## Discusión pedagógica derivada del dispositivo

La subcarpeta `pedagogia/` conserva documentos de discusión producidos durante el trabajo del dispositivo cuando puedan afectar preguntas pedagógicas.

Estos documentos **no son política pedagógica** y no modifican automáticamente `conocimiento/PEDAGOGIA.md`, COR002 ni las reglas del Generator.

Actualmente contiene:

- `pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` — discusión congelada posterior a la lectura intensiva de Bueno Holle 2019. Su estado interno es `FROZEN_DISCUSSION_INPUT_NOT_POLICY`.

La función de esta subcarpeta es impedir que el razonamiento quede fuera del repositorio sin confundirlo con una decisión adoptada.

Reglas de frontera útiles:

```text
ANALYZER_CAPABILITY != BEGINNER_REQUIREMENT
GENERATION_LICENSE != TEACHING_PRIORITY
PEDAGOGICAL_DISCUSSION != AUTOMATIC_POLICY
```

## Procedencia y migración

La migración puede encontrar etiquetas históricas diferentes para métodos de obtención de evidencia.

No se reescribirán silenciosamente. Se conservará la etiqueta original y, cuando sea posible, una equivalencia canónica separada.

Referencia: `PROVENANCE_LABEL_CROSSWALK_v0_1.md`.

La recuperación técnica se organiza en:

`migracion/MIGRATION_MANIFEST_v1.md`

Ese manifiesto clasifica artefactos por estado y prioridad. La migración es una línea de preservación paralela: **su incompletitud no bloquea automáticamente COR002, corpus oral, trabajo con hablantes, lectura bibliográfica ni nueva investigación lingüística o pedagógica**.

## Frontera con documentos institucionales

Esta capa utiliza nombres funcionales internos para permitir trabajo técnico y trazable.

Los informes institucionales y documentos de cara al público describen sus resultados mediante expresiones como:

- sistema lingüístico documental;
- herramientas internas de análisis y revisión;
- apoyo pedagógico;
- generación controlada de materiales;
- documentación lingüística trazable.

No es necesario describir en esos documentos los mecanismos tecnológicos internos.

## Regla de publicación

Los archivos de esta carpeta son documentación de trabajo. No deben citarse como norma del Didxazá ni como consenso comunitario.
