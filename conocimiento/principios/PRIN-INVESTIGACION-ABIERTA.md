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

implicaciones:
  - >
    El conocimiento canónico representa la posición operativa vigente del proyecto, no una verdad
    definitiva inmune a nueva evidencia.
  - >
    Una decisión puede revisarse, acotarse, suspenderse o sustituirse cuando nuevas fuentes,
    hablantes, corpus, experimentos, experiencia de aprendizaje o pruebas del dispositivo aporten
    evidencia suficiente.
  - >
    Los artefactos del dispositivo sirven para investigar, analizar y conservar capacidad operativa;
    no adquieren autoridad lingüística o pedagógica por estar implementados en código, bases de datos,
    schemas, prompts o runtimes.
  - >
    La migración del dispositivo tiene como objetivo evitar pérdida de conocimiento, procedencia y
    capacidad reproducible. No fija la arquitectura actual como arquitectura definitiva y no debe
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

etiquetas:
  - metodologia
  - investigacion
  - arquitectura
  - dispositivo
  - conocimiento
  - revisabilidad
```

## Alcance

Este principio no elimina la necesidad de decisiones operativas. El proyecto necesita poder decir qué versión, regla, protocolo o hipótesis utiliza actualmente para trabajar de forma reproducible.

La diferencia es que **vigente** significa "adoptado para el estado actual de la investigación", no "cerrado para siempre".

La trazabilidad histórica permite cambiar sin perder el camino recorrido: cuando una decisión deja de ser útil, se registra qué la sustituyó y por qué, en lugar de mantenerla únicamente porque ya estaba documentada o implementada.
