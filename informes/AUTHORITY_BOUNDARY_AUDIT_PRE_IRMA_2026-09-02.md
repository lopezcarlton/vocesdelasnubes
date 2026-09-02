# AUDITORÍA DE FRONTERA DE AUTORIDAD — PRE-IRMA — 2026-09-02

**Estado:** `AUDIT_REPORT / NON_NORMATIVE / NO_AUTOMATIC_PROMOTION`

Este informe localiza dependencias y posibles filtraciones entre el Sistema de Conocimiento y la capa técnica. No decide por sí mismo qué menciones deben eliminarse: una mención puede ser histórica o subordinante y por tanto legítima.

## 1. Referencias directas desde conocimiento/ hacia dispositivo/

- `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md:65` — `- requisitos de procedencia para la capa `dispositivo/`.`
- `conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md:65` — `- dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md`
- `README.md:70` — `├── dispositivo/                         # capa experimental no canónica`
- `README.md:91` — `La carpeta `dispositivo/` conserva el estado de herramientas lingüísticas experimentales que consumen el conocimiento del proyecto. **No constituye una segunda fuente de verdad.** Ningún resultado de esa capa modifica automáticamente `conocimiento/`.`
- `README.md:141` — `Durante agosto avanzó en paralelo un sistema interno compartido por funciones de análisis, revisión, explicación pedagógica y generación controlada. Esta capa se documenta en `dispositivo/` y permanece explícitamente separada del Sistema de Conocimiento canónico.`
- `INICIAR_AQUI_CHAT_NUEVO.md:21` — `11. `dispositivo/README.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:22` — `12. `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:23` — `13. `dispositivo/migracion/MIGRATION_MANIFEST_v1.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:24` — `14. `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:25` — `15. `dispositivo/migracion/REENTRY_CHECKPOINT_2026-09-02.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:26` — `16. `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:27` — `17. `dispositivo/migracion/fuentes/BH2019_READING_STATE_CLOSED_v0_36_1.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:28` — `18. `dispositivo/migracion/fuentes/BH2019_SOURCE_PROVENANCE_v0_36_1.json``
- `INICIAR_AQUI_CHAT_NUEVO.md:29` — `19. `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:30` — `20. `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv``
- `INICIAR_AQUI_CHAT_NUEVO.md:31` — `21. `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:32` — `22. `dispositivo/hardening/ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:33` — `23. `dispositivo/development_corpus/DevelopmentCorpusProtocol_v0_35.md``
- `INICIAR_AQUI_CHAT_NUEVO.md:41` — `- `dispositivo/` es experimental y no constituye una segunda fuente de verdad.`

## 2. Referencias de provenance hacia dispositivo/

- **INVERSIÓN CANDIDATA:** `conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md:65` — `- dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md`
- **INVERSIÓN CANDIDATA:** `INICIAR_AQUI_CHAT_NUEVO.md:28` — `18. `dispositivo/migracion/fuentes/BH2019_SOURCE_PROVENANCE_v0_36_1.json``

## 3. Cumplimiento de esquema de PRIN

| Archivo | estado | estado permitido | campos mínimos faltantes |
|---|---|---|---|
| `conocimiento/principios/PRIN-COMPETENCIA-COMUNICATIVA-MULTIDIMENSIONAL.md` | `vigente_como_principio_general_aplicacion_revisable` | **NO** | `alcance`, `autoridad_que_lo_valida`, `condiciones_de_revision`, `decisiones_derivadas`, `excepciones`, `hallazgos_que_lo_sustentan`, `origen` |
| `conocimiento/principios/PRIN-G-RESTRICCION-DURA.md` | `provisional_suspended_as_hard_generator_rule` | **NO** | `alcance`, `autoridad_que_lo_valida`, `condiciones_de_revision`, `decisiones_derivadas`, `excepciones`, `hallazgos_que_lo_sustentan`, `origen`, `principio` |
| `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md` | `vigente` | sí | `alcance`, `autoridad_que_lo_valida`, `decisiones_derivadas`, `excepciones`, `hallazgos_que_lo_sustentan`, `origen` |
| `conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md` | `provisional_not_automatic_generator_policy` | **NO** | `alcance`, `autoridad_que_lo_valida`, `condiciones_de_revision`, `decisiones_derivadas`, `excepciones`, `hallazgos_que_lo_sustentan`, `origen`, `principio` |

## 4. Menciones técnicas por archivo

### `00_ARQUITECTURA_DEL_CONOCIMIENTO.md` — 16 coincidencias
- L186: `**Código:** `SRC``
- L227: `**Código:** `HALL``
- L292: `**Código:** `DEC``
- L340: `**Código:** `SUP``
- L376: `**Código:** `PRIN``
- L416: `**Código:** `VAL``
- L472: `**Código:** `TEO``
- L506: `**Código:** `PROC``
- L552: `**Código:** `CRIT``
- L584: `**Código:** `RISK``
- L623: `**Código:** `OPEN``
- L657: `**Código:** `LESS``
- L679: `**Código:** `CAMB``
- L704: `**Código:** `OUT``
- L713: `* prompt generador;`
- L1507: `* cómo se automatizará la detección de duplicados;`

### `01_JERARQUIA_DE_VERDAD.md` — 1 coincidencias
- L101: `Para audio, software, edición y procesos técnicos prevalece:`

### `02_BACKLOG.md` — 7 coincidencias
- L144: `### BL-017 — Evaluación futura del generador de borradores`
- L149: `Evaluar el desempeño de un generador de borradores en español: aceptación por hablantes, artificialidad, errores, cobertura y utilidad real.`
- L151: `**Actualización 2026-08-31:** El generador v7 y las iteraciones v8.x se conservan como antecedentes experimentales, pero no constituyen el motor activo de COR002. El piloto actual suspende la generación masiva y prioriza obtener primero unas pocas escenas de referencia aceptadas mediante revisión manual y trabajo con hablantes.`
- L153: `Esta tarea se reactivará cuando exista suficiente evidencia concreta para decidir qué debe hacer un generador nuevo o reducido. No se considera necesario evaluar v7 “a escala” como requisito previo.`
- L225: `**Prioridad:** Media / dispositivo`
- L227: `Convertir progresivamente las distinciones relevantes derivadas de BIB065/Bueno Holle en capacidades o anotaciones explícitas del dispositivo, sin convertirlas automáticamente en niveles pedagógicos.`
- L245: `**Criterio de cierre:** las distinciones priorizadas pueden representarse y analizarse de forma trazable en el dispositivo, con procedencia explícita, sin haber sido convertidas indebidamente en reglas curriculares.`

### `INICIAR_AQUI_CHAT_NUEVO.md` — 16 coincidencias
- L21: `11. `dispositivo/README.md``
- L22: `12. `dispositivo/migracion/MIGRATION_AGENT_PROTOCOL_v1.md``
- L23: `13. `dispositivo/migracion/MIGRATION_MANIFEST_v1.md``
- L24: `14. `dispositivo/migracion/CURRENT_EXECUTABLE_STATE_v1.md``
- L25: `15. `dispositivo/migracion/REENTRY_CHECKPOINT_2026-09-02.md``
- L26: `16. `dispositivo/migracion/fuentes/CURRENT_STATE_NC001_v37_1_POST_BIB065_REPAIR.md``
- L27: `17. `dispositivo/migracion/fuentes/BH2019_READING_STATE_CLOSED_v0_36_1.md``
- L28: `18. `dispositivo/migracion/fuentes/BH2019_SOURCE_PROVENANCE_v0_36_1.json``
- L29: `19. `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md``
- L30: `20. `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.csv``
- L31: `21. `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md``
- L32: `22. `dispositivo/hardening/ANALYSIS_CAPABILITY_GUARDRAILS_v0_35.md``
- L33: `23. `dispositivo/development_corpus/DevelopmentCorpusProtocol_v0_35.md``
- L41: `- `dispositivo/` es experimental y no constituye una segunda fuente de verdad.`
- L74: `## 5. Analyzer y contexto`
- L110: `4. usar la evidencia nueva para probar/refinar el dispositivo;`

### `README.md` — 4 coincidencias
- L13: `Ese archivo define el orden de reconstrucción del estado vigente y obliga a distinguir conocimiento canónico, dispositivo experimental, snapshots históricos y pendientes de migración.`
- L70: `├── dispositivo/                         # capa experimental no canónica`
- L91: `La carpeta `dispositivo/` conserva el estado de herramientas lingüísticas experimentales que consumen el conocimiento del proyecto. **No constituye una segunda fuente de verdad.** Ningún resultado de esa capa modifica automáticamente `conocimiento/`.`
- L141: `Durante agosto avanzó en paralelo un sistema interno compartido por funciones de análisis, revisión, explicación pedagógica y generación controlada. Esta capa se documenta en `dispositivo/` y permanece explícitamente separada del Sistema de Conocimiento canónico.`

### `conocimiento/AUDIO.md` — 2 coincidencias
- L23: `- El procesamiento debe ser reproducible y escalable mediante automatización cuando sea apropiado.`
- L182: `El ajuste de LUFS se realiza mediante procesamiento automatizado (`ffmpeg` + `loudnorm`) cuando corresponda, no manualmente dentro de Ableton.`

### `conocimiento/CORPUS.md` — 3 coincidencias
- L532: `Las versiones v7 y v8.x del generador se conservan como antecedentes experimentales. Permitieron descubrir problemas reales —longitud rígida, activación sin CORE, exceso de trama, ritmo de entrevista, artificialidad por repetición y regresiones entre reglas—, pero ninguna se considera actualmente un generador general aprobado.`
- L540: `- sólo después de contar con escenas aceptadas se decidirá qué reglas o capacidades debe recuperar un futuro generador.`
- L564: `La evidencia procedente de hablantes, habla espontánea, elicitación dirigida, juicios, corrección ortográfica, bibliografía, pruebas del dispositivo, validación pedagógica y trabajo de audio puede modificar sus categorías y relaciones.`

### `conocimiento/METODOLOGIA.md` — 7 coincidencias
- L774: `La automatización es adecuada para conversiones, normalización técnica, metadatos, comparaciones, detección preliminar de duplicados y reportes de cobertura.`
- L776: `La revisión auditiva, lingüística o cultural no debe eliminarse por el hecho de automatizar el procesamiento.`
- L814: `## 9.5 Evolución del generador de borradores`
- L881: `- escalar tareas repetitivas mediante automatización controlada.`
- L905: `La automatización reduce carga operativa, pero no elimina la revisión especializada.`
- L932: `- automatización limitada a tareas apropiadas;`
- L943: `- validación a escala del generador vigente;`

### `conocimiento/PEDAGOGIA.md` — 8 coincidencias
- L75: `Lo que permanece en investigación son las fronteras exactas P1–P5, la ponderación entre esas dimensiones, su relación con la dificultad real del aprendiz y la forma en que deberían utilizarse en una futura secuenciación o generación automatizada.`
- L77: `Para evitar una ambigüedad que produjo problemas en versiones anteriores del generador, se distinguen tres afirmaciones diferentes:`
- L85: `Las etiquetas G1–G5 y P1–P5 deben seguir contrastándose con la evidencia gramatical extraída de la literatura disponible, observaciones de hablantes, comportamiento real de COR001 y COR002, resultados de la corrección ortográfica y análisis lingüístico en curso, pruebas del dispositivo y futura validación con aprendices.`
- L105: `Por ahora deben tratarse primero como capas analíticas descriptivas que el dispositivo pueda reconocer y conservar. Posteriormente, escenas reales, corpus oral y pruebas con aprendices deberán mostrar:`
- L109: `- cuáles son útiles para Analyzer/Tutor pero no necesitan una escala curricular;`
- L112: `La capacidad lingüística del dispositivo puede ser más fina que la taxonomía pedagógica vigente. Descubrir o modelar una distinción no obliga a convertirla inmediatamente en requisito de enseñanza.`
- L151: `8. aprender de la realización en Didxazá antes de volver a escalar la automatización.`
- L155: `El generador masivo permanece fuera del flujo activo mientras no existan escenas de referencia aprobadas suficientes para calibrarlo.`

### `conocimiento/VALIDACION.md` — 8 coincidencias
- L89: `- software;`
- L92: `- automatización;`
- L198: `El dispositivo lingüístico puede producir análisis, candidatos o restricciones útiles, pero una capacidad implementada en Analyzer, Corrector, Tutor o Generator no se convierte automáticamente en validación pedagógica ni lingüística.`
- L238: `- necesidad de automatizar el procesamiento de audio;`
- L241: `- oscilaciones entre exceso de trama, ritmo de entrevista y repetición tipo drill en distintas iteraciones del generador.`
- L265: `- el generador general;`
- L325: `- Evaluación futura de un generador general **después** de disponer de escenas de referencia aceptadas.`
- L327: `La antigua tarea “validar el generador v7 a escala” deja de representar el estado operativo actual: v7 y las iteraciones posteriores son antecedentes experimentales, no el motor activo del piloto.`

### `conocimiento/decisiones/DEC-COBERTURA-CORPUS-PROGRESIVA.md` — 3 coincidencias
- L12: `Las capacidades globales del dispositivo, la complejidad discursiva descubierta`
- L28: `- selección pedagógica de capacidades del dispositivo`
- L35: `- No convertir una capacidad nueva del Analyzer/Tutor/Generator en requisito pedagógico automático.`

### `conocimiento/decisiones/DEC-G-P-SEPARATION.md` — 3 coincidencias
- L12: `definitiva, ni que deban funcionar como secuencia curricular cerrada, ni que un generador deba`
- L52: `Al 2026-08-31 queda suspendida como regla automática del generador durante el piloto.`
- L59: `- Revisar si alguna forma de restricción previa resulta útil cuando vuelva a existir un generador general.`

### `conocimiento/decisiones/DEC-TRIANGULACION-EMPIRICA.md` — 1 coincidencias
- L30: `- dispositivo lingüístico`

### `conocimiento/fuentes/COR002_CHECKPOINT_METODOLOGICO_PILOTO_PRINCIPIANTES_v1.md` — 10 coincidencias
- L9: `> Este documento **no convierte las decisiones provisionales en teoría pedagógica definitiva**. Congela el modo de trabajo que, por ahora, parece más productivo para construir unas cuantas conversaciones útiles y aprender de ellas antes de volver a automatizar.`
- L91: `Esta corrección sigue siendo útil y debe conservarse independientemente del generador que usemos.`
- L97: `En vez de quedarnos en esas correcciones simples, comenzamos a iterar sucesivas versiones del generador.`
- L264: `- ingeniería adicional del generador.`
- L363: `- el generador general;`
- L509: `Se conservan especialmente las correcciones que son independientes del estilo del generador.`
- L596: `14. No volver todavía a la expansión general del banco ni al generador masivo.`
- L680: `- rediseñar, si hace falta, un generador mucho más pequeño y mejor fundado.`
- L715: `- generador masivo;`
- L746: `> Sólo entonces decidimos qué debe aprender el generador de ella.**`

### `conocimiento/fuentes/README.md` — 1 coincidencias
- L5: `Cada fuente formal se almacena en un archivo independiente identificado por su código estable (`SRC-*`), con el mismo formato que hallazgos y decisiones: encabezado y bloque YAML con los metadatos de la fuente.`

### `conocimiento/fuentes/SRC-BUENO-HOLLE-2019.md` — 1 coincidencias
- L65: `- requisitos de procedencia para la capa `dispositivo/`.`

### `conocimiento/fuentes/SRC-PEDAGOGICAL-FUNDAMENTOS.md` — 1 coincidencias
- L41: `Si etiqueta como nivel_1, generador produce oraciones fuera del alcance del principiante.`

### `conocimiento/fuentes/razonamiento-pedagogico-sistema-niveles.md` — 11 coincidencias
- L25: `**Caso A: Quién soy.** Preguntar por parentesco es pragmáticamente trivial: es una pregunta que se hace en los primeros cinco minutos de conocer a alguien, socialmente de bajísimo riesgo, forma parte del guion de presentación. Pero gramaticalmente involucra el sistema de posesión completo del didxazá, que es de lo más difícil de la lengua para un hispanohablante (posesión inalienable, alternancia xti', formas dependientes del pronombre). Si etiqueto esto como nivel_5 (como estaba originalmente), estoy diciendo "esto es para aprendientes avanzados" — y estoy retrasando artificialmente el momento en que el aprendiz puede tener una conversación básica sobre su familia, que es socialmente central en el Istmo. Si lo etiqueto como nivel_1 (como propuse en la corrección anterior), estoy diciendo "esto es para principiantes" — y el generador puede terminar produciendo oraciones que gramaticalmente están fuera del alcance de un principiante real.`
- L31: `Si comprimo estos tres casos en un solo eje, pierdo información que el generador necesita. En A, ¿genero una oración gramaticalmente simple aunque pragmáticamente trivial, o gramaticalmente compleja aunque pragmáticamente sofisticada? El número "nivel_2" o "nivel_5" no me lo dice. En B, ¿genero una oración con estructura simple pero contenido delicado, o al revés? El número tampoco lo dice.`
- L33: `Con dos ejes, el generador tiene instrucciones desambiguadas: "gramaticalmente estás autorizado a usar hasta X estructura, y pragmáticamente puedes explorar hasta Y densidad social". Son dos restricciones que operan en paralelo y que juntas definen el espacio de oraciones aceptables para ese paso.`
- L43: `Este eje tiene una **restricción dura**: no se puede pedir al generador que produzca una oración que rebase el nivel gramatical asignado, porque eso rompe la progresión pedagógica. Si un aprendiz está trabajando en el nivel_2, no debe encontrarse con cadi ni con subordinación condicional en el material — no porque esté "prohibido", sino porque no tiene el andamiaje para procesarlo, y la exposición prematura genera más ruido que aprendizaje. Esta es la lógica del **input comprensible** de Krashen (i+1): el material debe estar un paso arriba del nivel actual del aprendiz, no cinco pasos arriba.`
- L62: `- Si nivel_gramatical = 2 y nivel_pragmático = 4: el generador debe producir una oración con estructuras solo hasta nivel 2 (existenciales, potencial simple, imperativo suave, fórmulas fijas de cortesía), pero sobre un tema que tenga densidad pragmática — por ejemplo, describir un malestar personal, comentar una preocupación familiar, hacer una petición de algo que importa. El aprendiz recibe modelado gramatical accesible pero contenido social realista.`
- L64: `- Si nivel_gramatical = 5 y nivel_pragmático = 2: el generador puede desplegar estructuras avanzadas (cadi, condicional, posesión completa) pero aplicadas a temas de bajo riesgo social — por ejemplo, un intercambio elaborado sobre parentesco, un regateo animado en el mercado, una conversación extendida sobre el clima o el pueblo. El aprendiz consolida estructuras avanzadas en contextos donde no tiene que preocuparse por el peso social del contenido.`
- L70: `Esto también resuelve un problema secundario que estaba latente en el corpus: la **rotación léxica y temática**. Cuando solo hay un eje, dos situaciones marcadas como "nivel_3" tienden a parecerse entre sí porque el sistema no tiene forma de distinguir por qué son ambas nivel_3. Con dos ejes, "Ir a una fiesta (gram_3 / prag_3)" y "Estoy aprendiendo zapoteco (gram_3 / prag_5)" quedan claramente diferenciadas, y el generador sabe que la segunda debe explorar registro reflexivo aunque las estructuras sean parecidas.`
- L86: `Con todo lo anterior, la instrucción al generador queda así:`
- L91: `2. **nivel_gramatical (1–5)**: restricción dura sobre la estructura; el generador no puede rebasar este nivel al construir la oración. Anclado en los bloques y categorías de la Gramática Popular.`
- L92: `3. **nivel_pragmático (1–5)**: guía sobre la densidad social/discursiva del contenido; el generador puede explorar hasta este nivel de riqueza temática, tono y registro, incluso si eso significa exponer al aprendiz a contenido más denso de lo que podría producir por sí solo.`
- L96: `El generador debe interpretar cualquier discrepancia entre ejes de la siguiente manera: **la estructura obedece al gramatical; el contenido, tono y densidad social obedecen al pragmático**. Si no puede satisfacer los dos al mismo tiempo, prioriza no rebasar la restricción gramatical y ajusta el contenido a lo que quepa dentro de esa restricción, manteniendo el registro pragmático en lo que sí sea posible expresar.`

### `conocimiento/hallazgos/README.md` — 1 coincidencias
- L5: `Cada hallazgo se almacena en un archivo independiente identificado por su código estable (`HALL-XXXX`). Los documentos temáticos pueden referenciar estos hallazgos, pero no deben duplicar su contenido como fuente primaria.`

### `conocimiento/principios/PRIN-COMPETENCIA-COMUNICATIVA-MULTIDIMENSIONAL.md` — 1 coincidencias
- L28: `- no convertir la riqueza del dispositivo lingüístico en obligación de contenido para principiantes;`

### `conocimiento/principios/PRIN-G-RESTRICCION-DURA.md` — 4 coincidencias
- L11: `restricción dura no negociable sobre la estructura que un generador podía producir.`
- L27: `Las iteraciones del generador mostraron que imponer de antemano demasiadas restricciones podía`
- L36: `- que la hipótesis de un techo gramatical no pueda recuperarse en un futuro generador.`
- L59: `La versión del 7 de agosto de 2026 declaraba esta restricción como "dura no negociable" y la vinculaba directamente con la ejecución del generador. Esa implementación se conserva en el historial del repositorio, pero no gobierna el piloto de COR002 al cierre de agosto.`

### `conocimiento/principios/PRIN-INVESTIGACION-ABIERTA.md` — 6 coincidencias
- L13: `pero no convierte hipótesis, taxonomías, artefactos técnicos, versiones de software ni decisiones`
- L22: `hablantes, corpus, experimentos, experiencia de aprendizaje o pruebas del dispositivo aporten`
- L25: `Los artefactos del dispositivo sirven para investigar, analizar y conservar capacidad operativa;`
- L26: `no adquieren autoridad lingüística o pedagógica por estar implementados en código, bases de datos,`
- L29: `La migración del dispositivo tiene como objetivo evitar pérdida de conocimiento, procedencia y`
- L56: `- dispositivo`

### `conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md` — 5 coincidencias
- L11: `el generador podría explorar contenido social o discursivamente más denso que la capacidad productiva`
- L24: `objetivo del principiante, no por una obligación automática del generador de explotar todo el rango P.`
- L39: `Primero deben implementarse como propiedades analíticas descriptivas del dispositivo. La evidencia`
- L65: `- dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md`
- L77: `La versión del 7 de agosto de 2026 defendía explícitamente la exposición a contenido pragmáticamente denso como política del generador. Esa implementación permanece en el historial del repositorio, pero no gobierna automáticamente el piloto principiante al cierre de agosto.`

### `conocimiento/principios/README.md` — 1 coincidencias
- L5: `Cada principio se almacena en un archivo independiente identificado por su código estable (`PRIN-*`). Un principio documenta una regla operativa derivada de una o más decisiones, junto con su fundamento teórico y su aplicación concreta al corpus.`

## 5. Regla de adjudicación para la limpieza

```text
SUBORDINA_AL_SISTEMA_DERIVADO = admisible
DEFIERE_AUTORIDAD_AL_SISTEMA_DERIVADO = filtración
```

Las referencias históricas se conservan cuando son necesarias para reconstruir genealogía. Las vistas pedagógicas, lingüísticas y metodológicas no deben esperar que una implementación técnica determine su contenido.

## 6. Condición previa a separación física

Toda referencia de `provenance` desde `conocimiento/` hacia `dispositivo/` debe adjudicarse antes de separar repositorios: ref fundamentar en la fuente primaria o entidad válida del Sistema de Conocimiento, o degradar/suspender la afirmación correspondiente.
