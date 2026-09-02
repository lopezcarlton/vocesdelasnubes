# PRIN-INVESTIGACION-ABIERTA — Voces de las Nubes como investigación abierta

```yaml
id: PRIN-INVESTIGACION-ABIERTA
titulo: "Voces de las Nubes como investigación abierta"
estado: vigente
fecha: 2026-08-31
responsable: Emiliano López Carlton

principio: >
  Voces de las Nubes es una investigación lingüística, pedagógica, documental y tecnológica abierta.
  El repositorio conserva el mejor estado de conocimiento y de decisión disponible en cada momento,
  pero no convierte hipótesis, taxonomías, artefactos técnicos, versiones de software ni decisiones
  metodológicas en reglas inamovibles.

alcance: >
  Todo el proyecto Voces de las Nubes: Sistema de Conocimiento, corpus, metodología, pedagogía,
  documentación lingüística, decisiones operativas y relación con sistemas derivados. El principio
  gobierna la revisabilidad de los estados de trabajo, pero está subordinado a obligaciones éticas,
  legales, de consentimiento, atribución y preservación.

origen: >
  Adopción explícita de gobernanza del proyecto por Emiliano López Carlton, formalizada el
  31 de agosto de 2026 para impedir que estados documentales o implementaciones provisionales
  se conviertan por inercia en reglas permanentes.

hallazgos_que_lo_sustentan:
  - HALL-0008

autoridad_que_lo_valida:
  - Emiliano López Carlton

decisiones_derivadas:
  - DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO

excepciones:
  - >
    Obligaciones éticas, legales, de consentimiento, atribución o preservación pueden exigir
    restricciones que no son opcionales ni se suspenden por invocar investigación abierta.
  - >
    Una metodología o prueba controlada puede congelar localmente una versión o condición cuando
    ese congelamiento se documente como temporal, acotado y reversible.

implicaciones:
  - >
    El conocimiento canónico representa la posición operativa vigente del proyecto, no una verdad
    definitiva inmune a nueva evidencia.
  - >
    Una decisión puede revisarse, acotarse, suspenderse o sustituirse cuando nuevas fuentes,
    hablantes, corpus, experimentos, experiencia de aprendizaje o hallazgos debidamente adjudicados
    procedentes de pruebas técnicas aporten evidencia pertinente.
  - >
    Los artefactos de sistemas derivados sirven para investigar, analizar y conservar capacidad
    operativa; no adquieren autoridad lingüística o pedagógica por estar implementados en código,
    bases de datos, schemas, prompts o runtimes.
  - >
    La migración de una capa técnica tiene como objetivo evitar pérdida de conocimiento, procedencia
    y capacidad reproducible. No fija la arquitectura actual como arquitectura definitiva y no debe
    retrasar investigación segura que pueda seguir produciendo evidencia nueva.
  - >
    Un artefacto migrado puede conservarse como CURRENT, EXPERIMENTAL, SUPERSEDED, ARCHIVE_ONLY u otro
    estado explícito sin que su mera presencia obligue a seguir utilizándolo.
  - >
    Las preguntas abiertas deben registrarse y estudiarse, pero no deben convertirse automáticamente
    en bloqueos de trabajo cuando existe una vía suficientemente segura para seguir produciendo datos.
  - >
    Un resultado negativo o una prueba que no funcione a la primera no clausura por sí sola una línea
    de investigación. Puede motivar modificación, repetición, suspensión temporal o cambio de diseño.

regla_de_frontera: >
  DOCUMENTED_CURRENT_STATE != PERMANENT_TRUTH
  IMPLEMENTED_CAPABILITY != RESEARCH_AUTHORITY
  MIGRATED_ARTIFACT != IMMUTABLE_RULE
  OPEN_QUESTION != AUTOMATIC_BLOCKER

condiciones_de_revision:
  - Si el principio entra en conflicto con obligaciones éticas, legales, de consentimiento o preservación.
  - Si una metodología específica requiere congelamiento temporal para una prueba controlada; dicho congelamiento debe declararse como local y reversible.
  - Si la aplicación del principio produce pérdida sistemática de reproducibilidad, trazabilidad o capacidad de adjudicar decisiones vigentes.

etiquetas:
  - metodologia
  - investigacion
  - arquitectura
  - sistemas_derivados
  - conocimiento
  - revisabilidad
```

## Alcance

Este principio no elimina la necesidad de decisiones operativas. El proyecto necesita poder decir qué versión, regla, protocolo o hipótesis utiliza actualmente para trabajar de forma reproducible.

La diferencia es que **vigente** significa "adoptado para el estado actual de la investigación", no "cerrado para siempre".

La trazabilidad histórica permite cambiar sin perder el camino recorrido: cuando una decisión deja de ser útil, se registra qué la sustituyó y por qué, en lugar de mantenerla únicamente porque ya estaba documentada o implementada.

## Revisión de esquema — 2026-09-02

Se completaron los campos mínimos exigidos por `00_ARQUITECTURA_DEL_CONOCIMIENTO.md` §4.5 sin cambiar el contenido sustantivo del principio. `HALL-0008` se registra como respaldo posterior de la necesidad de mantener separadas implementación y autoridad; no se presenta como origen histórico del principio.
