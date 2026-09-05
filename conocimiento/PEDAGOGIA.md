# PEDAGOGIA

**Proyecto:** Voces de las Nubes  
**Versión:** 1.6  
**Estado:** Borrador consolidado y evolutivo  
**Fecha:** 2026-09-05

## 1. Objetivo pedagógico

Voces de las Nubes busca favorecer el aprendizaje inicial del Didxazá mediante una progresión basada en escucha, comprensión, recuperación activa y producción oral.

El sistema no se organiza como curso gramatical ni como colección de vocabulario temático. Su propósito es ayudar a que una persona reconozca y produzca funciones comunicativas reales mediante materiales breves, contextualizados y progresivos.

## 1.1 Públicos escolares y segmentación por edad

Desde el 2 de septiembre de 2026 el proyecto adopta como requisito que los materiales puedan dirigirse a **públicos escolares diferenciados**, además de personas con transmisión intergeneracional interrumpida u otros aprendices.

La educación secundaria técnica constituye el primer anclaje institucional prioritario por la relación real de Casa de las Ciencias de Oaxaca con ese nivel y con su base de docentes, pero **no es el público exclusivo**. El proyecto debe investigar también materiales adecuados para estudiantes más pequeños y otros perfiles.

La segmentación todavía no está resuelta. Debe investigarse qué diferencias requieren adaptación pedagógica, entre ellas potencialmente:

- edad y etapa escolar;
- trayectoria lingüística familiar;
- competencia previa en didxazá;
- longitud y estructura de las escenas;
- velocidad y claridad del habla;
- soporte visual, juego, explicación y producción;
- formas apropiadas de evaluación y práctica.

No se equiparan automáticamente estas dimensiones:

```text
AGE_GROUP != LANGUAGE_LEVEL
SCHOOL_GRADE != G_LEVEL
SCHOOL_GRADE != P_LEVEL
```

La decisión de segmentar está vigente; las bandas concretas y sus metodologías permanecen abiertas a trabajo con docentes, especialistas y estudiantes.

Durante la fase activa definida en `DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN`, esta investigación se restringe a **materiales de escucha para principiantes**. Las edades pueden variar, pero no se abre todavía una línea de lectoescritura ni se intenta resolver simultáneamente perfiles avanzados.

```text
CURRENT_PROFILE_RESEARCH = BEGINNER_LISTENING_BY_AGE
LITERACY_TRACK = OUTSIDE_ACTIVE_SCOPE
```

## 2. Principios de adquisición

### 2.1 Comprensión antes de explicación exhaustiva

El aprendizaje comienza con materiales que puedan comprenderse parcialmente mediante contexto, repetición y apoyo en español. La explicación gramatical puede acompañar el proceso, pero no constituye el punto de entrada principal.

### 2.2 Progresión controlada

Cada nuevo material debe apoyarse en estructuras ya conocidas e introducir una cantidad limitada de novedades. La dificultad depende de la relación entre conocimiento previo, patrón nuevo, función comunicativa, carga pragmática y posibilidad de producción.

### 2.3 Reutilización

Las estructuras deben reaparecer en distintos contextos. La repetición es pedagógicamente útil cuando permite reconocer productividad y transferir lo aprendido.

### 2.4 Producción activa

La producción oral forma parte deliberada del método. BIB044/Swain aporta fundamento para distinguir comprensión de capacidad productiva y para considerar que el output puede crear oportunidades de uso significativo, prueba de hipótesis y procesamiento sintáctico (`HALL-0208`–`HALL-0210`; `TEO-SWAIN-OUTPUT-VOCES`).

La regla operativa actual de **intentar producir antes de escuchar el modelo completo o antes de su segunda repetición** es, sin embargo, una elección de diseño de Voces. BIB044 no prescribe ese formato, no determina la posición ni duración de una pausa y no demuestra por sí sola que esta secuencia produzca mayor aprendizaje.

```text
OUTPUT_RELEVANCE = BIBLIOGRAPHICALLY_SUPPORTED
PAUSE_BEFORE_MODEL = PROJECT_DESIGN_TO_BE_TESTED
```

### 2.5 Aprendizaje sin presión

El material debe reducir el temor al error y permitir repetición privada. La producción se plantea como ensayo, no como examen inmediato.

La producción activa y la baja presión no se consideran incompatibles: el proyecto busca oportunidades reales de intento sin convertir cada producción en evaluación pública o sanción inmediata.

### 2.6 Memoria como componente central bajo justificación explícita

La memorización forma parte deliberada del método actual: el aprendiz necesita conservar expresiones y recuperarlas con suficiente rapidez para producirlas oralmente. Sin embargo, el proyecto **no da por demostrada** la equivalencia entre memorizar y aprender una lengua ni considera suficiente la repetición mecánica.

`BL-025` debe fundamentar con bibliografía y pruebas de aprendizaje qué papel cumplen la recuperación activa, el espaciamiento, las secuencias formulaicas, la reutilización y la transferencia, y cómo se evita el tedio señalado por docentes de orientación constructivista.

BIB044 fortalece la justificación de **producir** y poner a prueba recursos lingüísticos, pero no cierra esta deuda: no constituye evidencia específica sobre memorización, espaciamiento o automatización dentro del formato de Voces.

```text
MEMORY = CENTRAL_COMPONENT
ROTE_REPETITION = NOT_SUFFICIENT
CONSTRUCTIVIST_COMPATIBILITY = OPEN_FOR_JUSTIFICATION
SWAIN_OUTPUT != SPACING_OR_MEMORY_EVIDENCE
```

### 2.7 Material pedagógico no equivale automáticamente a revitalización

BIB046/Sallabank permite clasificar la producción de gramáticas, diccionarios y materiales de aprendizaje como parte del `corpus planning` (`HALL-0211`). También distingue expansión de dominios y una ruta fática ligada al hogar, socialización e identidad (`HALL-0212`).

Para Voces esto obliga a separar dos afirmaciones:

1. producir buenos materiales puede aumentar recursos disponibles para aprender y usar didxazá;
2. producir esos materiales **no demuestra por sí solo** recuperación de transmisión intergeneracional, uso familiar ni revitalización efectiva.

El anclaje escolar actual puede ampliar un dominio de uso y aprendizaje, pero no debe presentarse automáticamente como restablecimiento de transmisión familiar. Del mismo modo, trabajar con diálogos cotidianos no basta para afirmar que Voces pertenece a la `phatic route` (`TEO-SALLABANK-CORPUS-PLANNING-REVITALIZACION`).

```text
LEARNING_MATERIALS = CORPUS_PLANNING_CONTRIBUTION
SCHOOL_USE != FAMILY_TRANSMISSION_BY_DEFAULT
EVERYDAY_DIALOGUE != PHATIC_ROUTE_BY_DEFAULT
```

### 2.8 Rendición de cuentas comunitaria y no esencialismo

BIB047/McCarty y Lee propone, para contextos indígenas de Estados Unidos, una pedagogía culturalmente sostenida/revitalizadora con rendición de cuentas basada en la comunidad y atención no homogeneizante a necesidades expresadas localmente (`HALL-0214`, `HALL-0215`). También documenta dimensiones emocionales de recuperación lingüística (`HALL-0216`) y advierte contra usar la competencia en la lengua patrimonial como criterio de autenticidad indígena (`HALL-0217`).

Voces adopta estos hallazgos como **marco de vigilancia teórica**, no como prueba de consenso local ni como receta transferible sin ajustes. En particular:

- los públicos y necesidades locales no deben suponerse homogéneos;
- una persona con dominio limitado del didxazá no debe ser tratada como culturalmente menos auténtica por ese hecho;
- vergüenza, pérdida o exclusión pueden ser dimensiones relevantes, pero no se atribuyen automáticamente a cada participante;
- las reglas concretas de autoría, rechazo y validación de hablantes dentro de Voces proceden de decisiones propias del proyecto, aunque sean compatibles con este marco.

Esta sección no crea por sí sola un nuevo `PRIN` constitucional. La aplicación formal queda registrada en `TEO-MCCARTY-LEE-CSRP-COMUNIDAD`.

## 3. Papel del input

El input principal es oral. Debe ser comprensible en grado suficiente, breve, contextualizado, repetible, lingüísticamente confiable, adecuado al nivel y relacionado con una función comunicativa.

El equivalente en español sirve como apoyo para anticipar significado, no como estructura que deba traducirse literalmente.

BIB044 no elimina la función del input: su aporte relevante es mostrar que comprensión y exposición abundantes no garantizan por sí solas desarrollo productivo equivalente (`HALL-0208`). Voces trabaja por tanto con una combinación de input y producción, no con una sustitución de uno por otra.

## 4. Papel de la escucha

La escucha reiterada permite reconocer unidades sonoras, familiarizarse con ritmo y pronunciación, anticipar expresiones, comparar la producción propia y reforzar memoria.

Las funciones exactas de la escucha reiterada dentro de la retención y transferencia de Voces siguen necesitando evaluación empírica con aprendices.

## 5. Papel de la repetición

La repetición se utiliza con tres finalidades de diseño: reconocimiento, recuperación y consolidación.

No se considera suficiente repetir una frase de forma mecánica. El material debe favorecer que una estructura aparezca en diferentes situaciones.

La repetición espaciada mediante tarjetas puede servir como formato inicial de práctica, pero no define la totalidad del sistema pedagógico y su efecto específico dentro de Voces permanece abierto en `BL-025`.

## 6. Diseño de progresión

### 6.1 Funciones comunicativas

La progresión debe ampliar lo que el aprendiz puede hacer con la lengua.

### 6.2 Patrones productivos

Un patrón debe reutilizarse antes de introducir demasiadas estructuras nuevas.

### 6.3 Complejidad gramatical y pragmática

El proyecto trabaja actualmente con la hipótesis de separar dos dimensiones de complejidad:

- **complejidad gramatical (G):** estructuras lingüísticas necesarias;
- **complejidad pragmática (P):** exigencia social, discursiva y contextual del acto comunicativo.

Esta separación sigue siendo una **arquitectura de trabajo, no un sistema terminado**.

La escala P permanece vigente como instrumento de análisis. Su concepción pedagógica original fue deliberadamente multidimensional e incluyó factores como riesgo social, negociación, densidad discursiva y marco reflexivo o metalingüístico. La existencia de varias dimensiones dentro de P no se considera por sí misma un error.

Lo que permanece en investigación son las fronteras exactas P1–P5, la ponderación entre esas dimensiones, su relación con la dificultad real del aprendiz y la forma en que deberían utilizarse en una futura secuenciación o aplicación operativa.

Para evitar una ambigüedad detectada durante aplicaciones operativas anteriores, se distinguen tres afirmaciones diferentes:

1. **G/P sigue activo como instrumento de análisis, comparación y calibración pedagógica.** No se abandona la separación entre complejidad gramatical y pragmática.
2. **Las definiciones exactas de G1–G5 y P1–P5 no constituyen todavía una taxonomía definitiva ni una secuencia curricular aprobada.** Sus límites, contenidos y relaciones pueden cambiar con nueva evidencia.
3. **El piloto actual de COR002 utiliza provisionalmente una ventana G1–G3 / P1–P3.** P3 funciona como borde experimental y reversible. Este corte sirve únicamente para limitar el piloto de principiantes y no redefine por sí mismo el sistema general G/P.

La consecuencia metodológica es que, durante el piloto, G/P no se utiliza como sustituto del juicio sobre una conversación. Primero se revisa si la escena es contextual y conversacionalmente plausible; después se analiza qué G/P, patrones y cargas contiene y si son compatibles con el alcance del piloto.

Las etiquetas G1–G5 y P1–P5 deben seguir contrastándose con la evidencia gramatical extraída de la literatura disponible, observaciones de hablantes, comportamiento real de COR001 y COR002, resultados de la corrección ortográfica y análisis lingüístico en curso, hallazgos adjudicados procedentes de líneas técnicas y futura validación con aprendices.

La hipótesis operativa de que la restricción gramatical puede funcionar como límite más duro que la pragmática permanece como antecedente útil, pero no se convierte en regla universal. Un contenido socialmente complejo puede a veces expresarse con estructuras relativamente simples, mientras que una estructura gramatical avanzada no debería introducirse sólo porque el tema sea sencillo; la aplicación concreta debe probarse en escenas reales.

Las propuestas anteriores de definiciones cerradas para G1–G5, P1–P5 o etapas curriculares se conservan como antecedentes de diseño, pero **no gobiernan automáticamente el piloto actual ni futuras generaciones de materiales**.

#### 6.3.1 Capas analíticas finas derivadas de BIB065

La investigación posterior a BIB065/Bueno Holle introduce distinciones más finas sobre organización de la información y del discurso, entre ellas:

- introducción, mantenimiento y reintroducción de referentes;
- continuidad y cambio de tópico;
- tipos y posiciones de foco;
- estado informativo e información compartida;
- relaciones entre preguntas y respuestas;
- unidades entonacionales y organización prosódica;
- formas explícitas, clíticos y omisión según contexto.

Estas propiedades **no se convierten automáticamente en subcomponentes de P, en niveles de G ni en un tercer eje pedagógico**.

Por ahora deben tratarse primero como capas analíticas descriptivas del conocimiento lingüístico. Posteriormente, escenas reales, corpus oral y pruebas con aprendices deberán mostrar:

- cuáles ya quedan suficientemente representadas por G o P;
- cuáles añaden una carga pedagógica independiente;
- cuáles son útiles para análisis y explicación pero no necesitan una escala curricular;
- y si alguna combinación justifica en el futuro una descripción adicional de dificultad discursiva o referencial.

La descripción lingüística puede ser más fina que la taxonomía pedagógica vigente. Descubrir o modelar una distinción no obliga a convertirla inmediatamente en requisito de enseñanza.

### 6.4 Escenas

Las escenas sirven como origen contextual, pero no se ordenan automáticamente como lecciones.

En el piloto actual de COR002, la conversación concreta funciona además como unidad de aprendizaje metodológico: antes de añadir nuevas reglas al sistema se busca obtener escenas que el proyecto considere suficientemente plausibles y útiles como para llevarlas al trabajo con un hablante.

### 6.5 Marcadores conversacionales

Un conjunto básico de marcadores puede utilizarse desde etapas tempranas para evitar que los diálogos suenen artificiales.

### 6.6 Secuenciación curricular

No existe todavía una secuencia curricular definitiva.

El piloto de COR002 no intenta resolverla. Su alcance inmediato es más reducido: producir y revisar unas pocas conversaciones para principiantes, observar qué pueden aprenderse de ellas y usar esa evidencia para revisar después la progresión general.

Las propuestas anteriores de etapas deben entenderse como modelos exploratorios.

### 6.7 Diseño en espiral

El principio de revisitar situaciones comunicativas con mayor profundidad sigue siendo una hipótesis pedagógica útil y forma parte del piloto actual.

Una situación puede reaparecer cuando cambia lo que el aprendiz puede hacer dentro de ella. Por ejemplo, una primera escena puede trabajar disponibilidad o cantidad y una revisita posterior añadir elección o preferencia sencilla.

No se mantiene una cifra fija de cuántas situaciones pertenecen a cada etapa ni cuántas veces deben revisitarse.

### 6.8 Piloto metodológico actual de COR002

Al cierre de agosto de 2026 queda congelado, como flujo de trabajo provisional, el siguiente orden:

1. seleccionar una situación concreta y cotidiana;
2. declarar quién es el aprendiz y qué necesita hacer;
3. producir una escena sencilla;
4. revisar manualmente plausibilidad contextual y conversacional;
5. corregir la escena antes de imponer análisis pedagógico adicional;
6. analizar después G/P, patrones, complejidad y posibilidades de reuso;
7. llevar al hablante únicamente escenas fuente suficientemente aceptables;
8. aprender de la realización en Didxazá antes de escalar la producción de materiales.

Este flujo no convierte sus parámetros provisionales en teoría permanente. En particular, no fija de manera definitiva G1–G3/P1–P3, longitud, número de repeticiones, cantidad de léxico nuevo ni número ideal de escenas.

La producción masiva de borradores permanece fuera del flujo activo mientras no existan escenas de referencia aprobadas suficientes para calibrar sus requisitos.

## 7. Papel del error

El error es parte del intento de producción. La secuencia de pausa y modelo utilizada por Voces permite formular una hipótesis de producción, escuchar una forma validada, comparar, ajustar y repetir.

BIB044 respalda específicamente la función del output como oportunidad para **probar hipótesis sobre la lengua meta** (`HALL-0210`). No demuestra que el ciclo exacto `pausa → modelo → comparación → repetición` sea superior a otras formas de retroalimentación; esa aplicación permanece como diseño del proyecto.

Las fuentes actualmente adjudicadas no documentan todavía un sistema formal de corrección, retroalimentación o clasificación de errores para Voces.

## 8. Papel de la producción

La producción oral está integrada desde el diseño del material. Las pausas deben permitir un intento real conforme al formato que se esté probando.

BIB044 aporta tres soportes precisos para mantener producción activa: la comprensión alta puede coexistir con debilidad productiva (`HALL-0208`), el output puede empujar hacia una expresión más precisa (`HALL-0209`) y puede ofrecer uso significativo, prueba de hipótesis y procesamiento sintáctico (`HALL-0210`).

La producción no debe limitarse a repetir después del audio; el proyecto explora también anticipación y recuperación. Estas últimas son **aplicaciones propias** y no deben adjudicarse automáticamente a Swain 1985.

## 9. Evaluación del aprendizaje

El proyecto considera relevantes, como dimensiones posibles de evaluación, comprensión auditiva, recuperación sin apoyo, producción, transferencia a otra situación, retención y disposición para continuar usando el material. Esta lista es una agenda de evaluación de Voces, no un instrumento validado derivado de una sola fuente.

No existe todavía un sistema de evaluación validado con aprendices.

El antecedente BIB002/Rafael-Pérez et al. confirma además una distinción útil: probar funcionamiento de una aplicación con usuarios no equivale a demostrar adquisición lingüística. El artículo reporta validación funcional, pero no medidas pre/post, retención, transferencia ni comparación entre grupos (`HALL-0199`).

```text
FUNCTIONAL_TESTING != LEARNING_OUTCOME_EVIDENCE
PROJECT_EVALUATION_DIMENSIONS != VALIDATED_INSTRUMENT
```

El piloto actual permite producir material suficientemente definido para que una evaluación de aprendizaje sea posible más adelante, pero no la sustituye.

## 10. Limitaciones y carácter evolutivo

No puede documentarse todavía de forma definitiva:

- una secuencia curricular completa;
- definiciones consolidadas de G1–G5 y P1–P5;
- ponderación definitiva de las dimensiones internas de P;
- relación pedagógica final entre las capas finas de estructura informativa/discursiva y G/P;
- número definitivo de etapas;
- relación final entre complejidad gramatical y pragmática;
- frontera definitiva del nivel principiante;
- métricas de dominio;
- instrumentos de evaluación;
- resultados de pruebas con aprendices;
- criterios de aprobación por nivel;
- tratamiento diferenciado por edad o perfil;
- protocolo formal de retroalimentación;
- evidencia empírica sobre retención o transferencia;
- evidencia de que los materiales escolares de Voces producen uso familiar o transmisión intergeneracional;
- validación local suficiente para trasladar sin ajustes marcos de CSRP desarrollados en otros contextos indígenas.

Este documento debe evolucionar junto con la evidencia lingüística, metodológica y pedagógica del proyecto. Las clasificaciones actuales son herramientas de trabajo y no deben convertirse en restricciones permanentes por inercia documental.

La investigación pedagógica se rige además por `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md`: el estado vigente organiza el trabajo presente, pero permanece revisable cuando nueva evidencia justifique cambios.

## Cambio 2026-08-31 — checkpoint metodológico del piloto COR002

Se incorpora el flujo documentado en `conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md`.

El cambio resuelve una ambigüedad anterior: **G/P puede seguir siendo una pieza central del trabajo sin que sus definiciones actuales sean una teoría pedagógica cerrada**. El piloto utiliza una ventana provisional para limitar el trabajo inmediato, mientras conserva abierta la revisión del sistema general.

## Cambio 2026-08-31 — P y capas finas BIB065

Se aclara que P continúa siendo una escala válida de análisis cuya delimitación P1–P5 permanece como pregunta de investigación. Las distinciones finas de estructura informativa, referencia, discurso y prosodia derivadas de BIB065 se conservarán primero como capas analíticas descriptivas y no se asignan automáticamente a G, P ni a un tercer eje pedagógico.

## Cambio 2026-09-02 — frontera de autoridad

Se retiran formulaciones que deferían decisiones pedagógicas a una implementación técnica. Las líneas técnicas pueden producir preguntas o hallazgos candidatos, pero sólo participan en esta vista después de ser adjudicadas dentro del Sistema de Conocimiento conforme a `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO`.

La actualización es arquitectónica: **no redefine G/P, no cierra P1–P5 y no incorpora todavía ninguna decisión de la reunión con Irma Pineda.**

## Cambio 2026-09-05 — backfill bibliográfico pedagógico

Se incorporan las aplicaciones teóricas adjudicadas de BIB044, BIB046 y BIB047 y se corrigen cuatro mezclas previas entre fuente y aplicación del proyecto:

- Swain 1985 fundamenta relevancia del output, `pushed output`, prueba de hipótesis y procesamiento sintáctico, pero no la regla exacta de pausa antes del modelo ni la función formal posterior de `noticing the gap`;
- Sallabank permite reconocer materiales de aprendizaje como `corpus planning`, pero no equiparar automáticamente escolarización con transmisión intergeneracional ni diálogo cotidiano con `phatic route`;
- McCarty y Lee fundamentan rendición de cuentas comunitaria, atención local no homogeneizante y crítica del esencialismo hablante/no hablante, pero no determinan los roles concretos de colaboradores de Voces;
- la validación funcional de una aplicación educativa no se trata como evidencia suficiente de adquisición lingüística (`HALL-0199`).

Aplicaciones relacionadas:

- `TEO-SWAIN-OUTPUT-VOCES`;
- `TEO-SALLABANK-CORPUS-PLANNING-REVITALIZACION`;
- `TEO-MCCARTY-LEE-CSRP-COMUNIDAD`.
