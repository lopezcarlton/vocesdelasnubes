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

## Relación con los cuatro componentes

La arquitectura de trabajo distingue cuatro funciones que comparten un núcleo lingüístico:

### ANALYZER

Intenta reconocer estructura, morfología, persona, aspecto, referencia, procedencia y otras capas documentadas sin convertir automáticamente un análisis plausible en verdad.

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

## Núcleo compartido

Los cuatro componentes deben consumir un núcleo lingüístico común para evitar que cada uno mantenga reglas propias incompatibles.

Entre los artefactos desarrollados fuera del repositorio se encuentra `JUCHITAN_LINGUISTIC_CORE`, actualmente experimental, además de bases, runtimes, inventarios, pruebas y paquetes de migración.

La incorporación de esta carpeta **no implica que todos esos artefactos hayan sido migrados ya al repositorio**. El estado exacto se registra en `ESTADO_ACTUAL_2026-08-31.md`.

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
