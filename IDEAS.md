# Voces de las Nubes — Ideas no adoptadas

**Archivo:** `IDEAS.md`  
**Creado:** 2026-09-05  
**Estado:** EXPLORATORIO / NO NORMATIVO / NO BLOQUEANTE

## Propósito

Este archivo conserva propuestas, intuiciones y posibles mejoras que todavía **no han sido adoptadas como decisiones, metodología, teoría, pedagogía, arquitectura del corpus ni requisitos del dispositivo**.

Su función es evitar perder ideas valiosas sin convertirlas prematuramente en obligaciones del proyecto.

## Regla fundamental

Nada contenido en `IDEAS.md` puede por sí solo:

- crear tareas en `02_BACKLOG.md`;
- bloquear COR001, COR002, ingesta lingüística, validación, audio, dispositivo o trabajo de campo;
- modificar `METODOLOGIA.md`, `CORPUS.md`, `PEDAGOGIA.md`, `TEORIA.md`, `AUDIO.md` o `VALIDACION.md`;
- convertirse en requisito de publicación, archivo, corpus o producto;
- gobernar el dispositivo;
- desplazar una prioridad activa;
- tratarse como principio metodológico aceptado.

Una idea solo adquiere autoridad si existe una decisión explícita posterior y se promueve al documento correspondiente siguiendo las reglas normales del repositorio.

---

# IDEAS-ELDP-001 — Separar con mayor claridad documentación primaria, análisis, pedagogía y ejecución

**Origen:** aprendizajes de la sesión ELDP Office Hours 2026, conservados en `lopezcarlton/ELDP/12_OFFICE_HOURS_2026-08-27.md`.

**Estado:** IDEA / NO ADOPTADA / NO BLOQUEANTE.

## Propuesta

Explorar si resulta útil distinguir conceptualmente cuatro capas que pueden relacionarse pero no deben confundirse:

1. **Documentación primaria**
   - grabación de audio/video;
   - consentimiento;
   - metadatos;
   - transcripción;
   - traducción.

2. **Análisis lingüístico**
   - segmentación;
   - glosado;
   - análisis morfológico, sintáctico, fonológico o semántico;
   - relaciones con el grafo de conocimiento.

3. **Transformación pedagógica**
   - selección y progresión para aprendizaje;
   - microescenas;
   - ejercicios;
   - materiales de escucha;
   - tutoría y secuenciación.

4. **Capa ejecutable**
   - Normalizer;
   - Analyzer;
   - Corrector;
   - Generator;
   - Tutor y demás componentes computacionales.

## Posible valor

- evitar que un registro dependa de una herramienta concreta para seguir siendo inteligible;
- evitar que documentación, análisis y pedagogía se mezclen innecesariamente;
- permitir que un mismo material tenga distintos niveles de enriquecimiento sin exigir que todos estén completos al mismo tiempo.

## No implica

- reestructurar ahora la arquitectura del repositorio;
- introducir nuevas obligaciones de anotación;
- frenar corpus existentes;
- exigir archivo documental completo a cada unidad;
- adoptar estándares ELDP/ELAR para Voces.

---

# IDEAS-ELDP-002 — Transcripción y traducción como posible llave mínima de acceso documental

**Estado:** IDEA / NO ADOPTADA / NO BLOQUEANTE.

## Origen

En Office Hours, ELDP explicó que una grabación documental debe contar con transcripción y traducción para que exista una vía de acceso a su contenido.

## Propuesta

Explorar si, para determinados materiales documentales de Voces, puede resultar útil definir un nivel mínimo reutilizable compuesto por:

**grabación + metadatos + transcripción + traducción**

sin exigir necesariamente análisis lingüístico exhaustivo en esa misma fase.

## Posible valor

- conservar materiales útiles aunque el análisis posterior tarde en completarse;
- reducir la dependencia de glosado exhaustivo para reconocer valor documental;
- facilitar futuras reutilizaciones lingüísticas o pedagógicas.

## No implica

- cambiar el criterio actual de completitud de COR001 o COR002;
- crear una nueva condición de cierre;
- hacer obligatoria esta estructura para todos los materiales;
- introducir trabajo retroactivo.

---

# IDEAS-ELDP-003 — Archivo durable independiente del producto pedagógico

**Estado:** IDEA / NO ADOPTADA / NO BLOQUEANTE.

## Propuesta

Explorar a largo plazo una forma de preservar determinados registros primarios de manera que sigan siendo accesibles aunque desaparezcan Anki, el dispositivo actual, una interfaz específica o cualquier otra herramienta pedagógica/computacional.

## Posible valor

- preservación de largo plazo;
- reutilización por futuras generaciones del proyecto;
- independencia entre patrimonio documental y software;
- posibilidad de evaluar calidad y procedencia de materiales sin depender del producto final.

## No implica

- adoptar ELAR;
- iniciar ahora un proyecto de archivo;
- convertir archivo en requisito previo para corpus o dispositivo;
- migrar materiales existentes de inmediato.

---

# IDEAS-ELDP-004 — Documentación comunitaria distribuida

**Estado:** IDEA / NO ADOPTADA / NO BLOQUEANTE.

## Origen

La sesión ELDP mostró ejemplos de proyectos donde miembros de la comunidad asumen distintos roles de grabación, consentimiento, transcripción, traducción, coordinación y gestión de datos.

## Propuesta

Explorar en el futuro si algunos procesos de Voces podrían distribuirse entre hablantes y colaboradores locales, en lugar de concentrar toda la producción documental en un investigador o coordinador.

## Posible valor

- mayor capacidad de producción;
- mayor autonomía comunitaria;
- distribución de responsabilidades;
- continuidad aun cuando el coordinador no esté presente.

## No implica

- cambiar ahora los roles de Vicente, Vidal, Laura u otros colaboradores;
- crear un programa de capacitación;
- modificar la gobernanza actual;
- asumir que el modelo comunitario de ELDP es automáticamente adecuado para Voces.

---

# IDEAS-ELDP-005 — Consultar vacíos documentales como una fuente adicional para diseñar futuras colecciones

**Estado:** IDEA / NO ADOPTADA / NO BLOQUEANTE.

## Propuesta

Además de las necesidades pedagógicas y lingüísticas propias de Voces, podría ser útil en el futuro preguntar:

> ¿Qué tipos de habla, géneros, situaciones, generaciones o registros del didxazá están poco representados en los corpus disponibles?

Esta pregunta podría servir como una fuente adicional de ideas para futuras colecciones.

## Posible valor

- evitar duplicación innecesaria;
- ampliar diversidad de registros;
- conectar trabajo pedagógico con preservación de usos reales de la lengua.

## No implica

- que ELDP defina la agenda de Voces;
- priorizar automáticamente lo menos documentado;
- abandonar necesidades pedagógicas;
- convertir revisión de archivos externos en requisito previo para COR002.

---

## Relación con ELDP

Estas ideas provienen de aprendizajes metodológicos extraídos de una sesión de ELDP, pero **no convierten a ELDP en autoridad metodológica de Voces de las Nubes**.

La autoridad sobre metodología, corpus, pedagogía, teoría, audio, validación y dispositivo sigue estando en los documentos y decisiones propios de `lopezcarlton/vocesdelasnubes`.

## Regla de promoción

Para promover cualquier elemento de este archivo debe ocurrir explícitamente:

1. revisión contra la arquitectura y decisiones vigentes del repositorio;
2. comprobación de que no duplica un principio ya existente;
3. decisión explícita del usuario;
4. incorporación al documento autoritativo correspondiente;
5. solo después, si procede, creación de tareas de implementación.

Hasta entonces:

**IDEA ≠ DECISIÓN ≠ REQUISITO ≠ BACKLOG.**
