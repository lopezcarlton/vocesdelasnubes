# ESTADO COR002, PEDAGOGÍA Y GENERADOR
## Checkpoint operativo — Voces de las Nubes
**Fecha:** 22 de agosto de 2026  
**Estado:** documento de trabajo / checkpoint, no especificación final  
**Función:** conservar el estado actual de las decisiones, contradicciones, hipótesis y prioridades relacionadas con COR001, COR002, pedagogía, generador de corpus y sistema documental/corrector.

---

# 1. Propósito de este documento

Este documento existe para evitar que las decisiones y preguntas abiertas del proyecto queden dispersas entre chats, borradores, generadores y documentos parciales.

No reemplaza:

- `CORPUS.md`;
- `METODOLOGIA.md`;
- `PEDAGOGIA.md`;
- `TEORIA.md`;
- el generador de corpus;
- el sistema documental/corrector;
- la documentación del Small Grant.

Tampoco pretende cerrar todavía la arquitectura pedagógica de COR002.

Su función es más limitada y operativa:

1. registrar lo que ya está suficientemente claro;
2. identificar contradicciones reales;
3. separar decisiones de hipótesis;
4. impedir que cuestiones todavía abiertas se conviertan accidentalmente en reglas canónicas;
5. definir qué es indispensable resolver para seguir produciendo aprendizaje;
6. dejar un punto de reentrada claro para continuar el trabajo en otros chats o repositorios.

---

# 2. Situación actual

El proyecto está abierto simultáneamente en varios frentes:

- COR001 todavía está en proceso de consolidación, corrección ortográfica, regrabación parcial, normalización de audio y preparación final para Anki/audio;
- COR002 existe como corpus piloto en español, pero su tamaño final, secuenciación, distribución por niveles y sistema de estudio siguen abiertos;
- el generador de corpus dramatúrgico está en v7 y contiene varias contradicciones o deudas de diseño;
- el sistema documental/corrector ha crecido de manera considerable, pero todavía no está claro qué producto operativo debe entregar en el corto plazo;
- la aplicación al Small Grant sigue abierta y requiere resolver asuntos institucionales, metodológicos y de presentación;
- está pendiente preparar una conversación/reunión con Irma Pineda;
- la pedagogía del proyecto todavía no está cerrada;
- la relación entre patrones proyectados desde el español y patrones productivos reales del Didxazá todavía debe comprobarse con traducciones, documentación y hablantes.

La prioridad inmediata no debe ser resolver toda la teoría del proyecto. Debe ser conservar lo ya aprendido, resolver bloqueos reales y volver a producir evidencia mediante traducción, estudio y validación.

---

# 3. Antecedente: qué nos enseñó COR001

COR001 contiene 107 frases validadas.

El aprendizaje realizado hasta ahora permitió:

- memorizar prácticamente todas las frases;
- reconocer una cantidad considerable de vocabulario;
- comenzar a detectar algunos patrones;
- producir muchas expresiones aprendidas;
- construir familiaridad fonológica mediante exposición abundante;
- acumular muchas horas de escucha gracias a un formato compatible con actividades cotidianas.

El formato principal de estudio fue:

**español → pausa → Didxazá → pausa → Didxazá**

Este sistema funcionó bien para exposición, asociación español–Didxazá, memoria de secuencias y familiaridad auditiva.

El límite observado es distinto:

- algunas expresiones todavía requieren varios segundos para recuperarse;
- la recuperación no está suficientemente automatizada;
- la conversación abierta sigue siendo muy limitada;
- las 107 frases no proporcionan todavía suficiente cobertura para sostener intercambios imprevisibles;
- memorizar una frase no implica necesariamente poder recombinar sus componentes ni utilizarla generativamente.

Conclusión provisional:

> COR001 no necesita simplemente más repetición idéntica. Necesita pasar progresivamente de exposición y memorización a recuperación, comprensión directa, mantenimiento y uso contextual.

---

# 4. Distinciones pedagógicas que conviene conservar

Estas distinciones surgieron de la auditoría de COR001 y no contradicen el sistema actual.

## 4.1 Receptivo, productivo y automatizado

No todo el corpus debe necesariamente dominarse del mismo modo.

Conviene distinguir entre:

- **repertorio receptivo:** expresiones que el aprendiz debe comprender;
- **repertorio productivo:** expresiones que debe poder producir;
- **repertorio automatizado:** subconjunto productivo que debe aparecer con poca latencia y sin búsqueda consciente prolongada.

Esta distinción todavía no debe convertirse automáticamente en una nueva taxonomía formal del repositorio.

## 4.2 Operación cognitiva y dificultad lingüística no son lo mismo

Una misma expresión puede utilizarse para tareas diferentes:

- reconocer;
- comprender;
- recuperar;
- seleccionar;
- responder;
- variar;
- recombinar.

Esto describe la tarea del aprendiz, no el nivel G/P del material.

Por ahora no se adopta un tercer eje formal D1–D6 ni equivalente.

## 4.3 COR001 debe pasar a mantenimiento, no ser abandonado

La transición hacia COR002 no debe depender de que COR001 llegue a una perfección indefinida.

Las expresiones dominadas deben consumir cada vez menos tiempo; las difíciles deben seguir reapareciendo.

---

# 5. Qué está bien encaminado en COR002

El piloto de COR002 muestra características pedagógicamente prometedoras:

- situaciones humanas reconocibles;
- funciones comunicativas recurrentes;
- variación contextual;
- cambio de interlocutores y roles;
- reutilización de vocabulario;
- recurrencia de secuencias formulaicas;
- posibilidad de construir familias comunicativas;
- posibilidad futura de pasar de secuencias aprendidas a estructuras reutilizables.

Ejemplos observados en el piloto:

- tienda, mercado, venta y pescado comparten disponibilidad, precio, cantidad y pago;
- funeral, vela, boda y visita comparten hospitalidad, recepción, ofrecimiento, agradecimiento y despedida;
- transporte, mercado, pesca y visita permiten reutilizar comentarios sobre condiciones, clima, trayecto o contexto.

Esto sugiere que COR002 puede convertirse en algo más que una colección de nuevas frases:

> una red de funciones, escenas, patrones y vocabulario que se refuerzan en contextos diferentes.

---

# 6. Arquitectura canónica que debe respetarse

La discusión confirmó que varias ideas que parecían nuevas ya estaban previstas en la arquitectura del proyecto.

Debe conservarse la terminología canónica existente:

- **escena comunicativa**;
- **función comunicativa**;
- **patrón**;
- **enunciado**;
- **microescena**.

No se adopta el término “microinteracción”.

La función comunicativa sigue siendo una unidad central para medir avance y cobertura.

La escena sirve como origen de diseño y contexto.

La microescena es una unidad breve de interacción con suficiente contexto para evitar frases aisladas.

---

# 7. Contradicciones confirmadas en el generador v7

## 7.1 Microescena

### Problema

El generador v7 ordena construir una “micro-escena” con:

- arco completo;
- apertura;
- tensión o necesidad;
- desarrollo;
- resolución;
- mínimo de 20 líneas.

Esto contradice la definición canónica de microescena como secuencia breve, económica y sin obligación de cumplir movimientos dramáticos rígidos.

### Corrección propuesta

La unidad de 20 líneas debe llamarse **escena comunicativa** o conversación.

Una escena puede contener varias microescenas.

La microescena:

- no tiene mínimo obligatorio de 20 líneas;
- no exige arco dramático completo;
- no debe crecer para cumplir una plantilla.

**Estado:** CORRECCIÓN NECESARIA.

---

## 7.2 Patrón español tratado como si ya fuera patrón productivo del Didxazá

### Problema

El generador define “patrón” como estructura sintáctica y obliga a exhibirla en varias variantes dentro del español.

El proyecto, sin embargo, ya establece que las propuestas españolas son apoyo o punto de partida y no deben convertirse en molde obligatorio de la estructura final en Didxazá.

### Riesgo

El español puede sugerir una familia estructural que:

- no exista de la misma forma en Didxazá;
- se divida en varias construcciones;
- corresponda a una sola construcción diferente;
- dependa de factores que el español no marca.

### Corrección conceptual propuesta

Separar explícitamente:

- **patrón_ES_objetivo / objetivo_de_elicitación**;
- **patrón_DID_observado**;
- **patrón_DID_analizado**;
- **patrón_DID_validado**;
- **patrón_DID_productivo**, cuando exista evidencia suficiente para utilizarlo pedagógicamente de forma generativa.

El generador en español solo puede trabajar directamente con el primer nivel.

**Estado:** CORRECCIÓN ARQUITECTÓNICA PRIORITARIA.

---

## 7.3 Comparación G5 vs. G3

### Problema

El generador v7 todavía coloca “comparación” dentro de G5.

La revisión más reciente reportada del Sistema de Conocimiento indica que la comparación fue reclasificada a G3 después de revisar evidencia descriptiva que mostró una estructura menos compleja de lo supuesto inicialmente.

### Acción

Verificar la decisión canónica más reciente en `TEORIA.md` / decisión correspondiente y sincronizar el generador.

Si la reclasificación G3 está confirmada y no existen dos tipos diferentes de comparación, eliminar “comparación” de G5 y colocarla en G3.

**Estado:** BUG DE STALENESS / CORRECCIÓN NECESARIA.

---

## 7.4 Conflicto interno Naturalidad / G / TAREA / silencio

### Problema

El generador establece simultáneamente que:

1. la naturalidad tiene prioridad máxima;
2. el nivel G activo es obligatorio;
3. los campos resueltos por TAREA deben ejecutarse y no reevaluarse;
4. la salida no puede contener advertencias ni comentarios.

Puede llegar una TAREA incompatible con las demás restricciones y el motor no tiene ninguna salida válida.

### Corrección

La compatibilidad debe resolverse antes de llegar al motor.

El controlador/pipeline debe ejecutar un **preflight de TAREA** y enviar al generador únicamente tareas compatibles.

El motor no debe convertirse en árbitro de inconsistencias del pipeline.

**Estado:** FALLA LÓGICA INTERNA / CORRECCIÓN NECESARIA.

---

# 8. Deudas de diseño importantes, pero no contradicciones cerradas

## 8.1 Función comunicativa ausente de TAREA

El bloque TAREA actual incluye:

- situación;
- patrón;
- léxico;
- personajes;
- saludo/cierre.

No incluye función comunicativa.

Esto deja incompleto el flujo metodológico:

**situación real → función comunicativa → microescena → elicitación → organización pedagógica → producción**

### Mejora propuesta

Añadir al controlador/TAREA una distinción como:

- función objetivo;
- funciones de refuerzo.

No es necesario resolver la forma definitiva de los campos todavía.

**Estado:** DEUDA DE DISEÑO PRIORITARIA.

---

## 8.2 “Etapa del aprendiz” en la bifurcación G/P

El generador describe algunas bifurcaciones como el mismo paso en “etapas distintas del aprendiz”.

Esto mezcla:

- progresión del corpus;
- progresión del estudiante.

Todavía no existe evidencia suficiente para afirmar que criterio_1, criterio_2, etc. sean también las etapas reales de adquisición.

### Mejora provisional

Hablar de:

**etapas de cobertura / generación del corpus**

en vez de:

**etapas del aprendiz**

hasta que PEDAGOGIA defina la progresión del estudio.

**Estado:** REFORMULACIÓN RECOMENDADA.

---

## 8.3 G debe entenderse como restricción de elicitación

El generador produce solo español, pero algunas metas G están formuladas directamente en términos de Didxazá:

- `cadi`;
- `qué`;
- `la'dxi'`;
- VSO;
- inclusivo/exclusivo;
- etc.

El generador no puede producir esas formas.

Sí puede construir contextos españoles que intenten provocar esos contrastes durante la traducción.

### Mejora

Reformular G operativamente como:

> objetivo o restricción de elicitación lingüística.

Esto no elimina la escala G; cambia lo que afirmamos que el generador puede garantizar.

**Estado:** REFORMULACIÓN ARQUITECTÓNICA RECOMENDADA.

---

# 9. Recurrencia: local vs. longitudinal

El generador v7 exige actualmente que cada conversación muestre uno o dos patrones en 2–3 variantes.

Esto puede aumentar artificialmente la densidad del patrón dentro de una sola escena.

La recurrencia pedagógica más valiosa puede estar distribuida:

- conversación 1;
- conversación 5;
- conversación 12;
- conversación 30.

### Principio propuesto

La recurrencia debe ser principalmente una propiedad **longitudinal del corpus**, controlada por el pipeline.

Dentro de una escena, el patrón debe reaparecer varias veces solo cuando resulte natural.

### Implicación

El controlador debe conocer:

- qué funciones ya aparecieron;
- qué patrones_ES ya aparecieron;
- qué vocabulario ya apareció;
- cuándo aparecieron;
- en qué contextos;
- cuántas veces;
- qué elementos están subrepresentados.

**Estado:** MEJORA FUTURA DE PIPELINE.

---

# 10. Relación futura COR001 → COR002

COR002 no debe diseñarse ignorando COR001.

El controlador futuro debería poder identificar al menos:

- funciones ya cubiertas en COR001;
- expresiones de alta frecuencia;
- vocabulario reutilizable;
- construcciones potencialmente relacionadas;
- elementos que conviene reforzar;
- novedades verdaderas.

No es necesario introducir COR001 completo dentro del prompt del generador.

La comparación debe hacerse en la capa de control/datos.

**Estado:** NECESARIO ANTES DE ESCALAMIENTO MASIVO, NO BLOQUEA PILOTO.

---

# 11. Papel del sistema documental/corrector

El sistema documental/corrector no debe confundirse con el generador ni con PEDAGOGIA.

Su estado actual incluye una infraestructura considerable de:

- procedencia;
- evidencia documental;
- alcance dialectal;
- alineamiento;
- registros lingüísticos;
- reproducibilidad;
- clasificación de evidencia;
- casos abiertos.

Sin embargo, su utilidad operativa inmediata debe acotarse.

## Productos que debe intentar entregar

### Producto A — revisión ortográfica

Ayudar a decidir, documentar o reducir casos ortográficos abiertos en COR001/COR002 sin sustituir la autoridad de hablantes.

### Producto B — evidencia para análisis de patrones

Proporcionar evidencia estructurada para investigar:

- recurrencias;
- alternancias;
- persona;
- posesión;
- aspecto;
- negación;
- otras estructuras relevantes.

No debe declarar automáticamente productividad solo por encontrar similitudes o múltiples fuentes.

## Regla operativa

Si el sistema no empieza a acercarse de forma visible a A o B, su expansión debe poder congelarse temporalmente.

**Estado:** NECESITA CRITERIOS DE ÉXITO EXPLÍCITOS.

---

# 12. Registro de patrones futuro

No es necesario construirlo ahora, pero conviene conservar la idea.

Un futuro `Pattern Registry` podría distinguir:

1. patrón observado;
2. patrón analizado;
3. patrón documentado;
4. patrón validado;
5. patrón productivo pedagógicamente utilizable.

Podría registrar:

- ID;
- descripción provisional;
- ejemplos COR001/COR002;
- ejemplos documentales;
- elementos constantes;
- slots variables;
- restricciones;
- alternancias;
- contraejemplos;
- hablantes;
- comunidad;
- procedencia;
- nivel de evidencia;
- estado de validación.

**Estado:** BACKLOG DE INVESTIGACIÓN / NO IMPLEMENTAR TODAVÍA.

---

# 13. Qué es indispensable para empezar a producir aprendizaje

No es necesario resolver toda la arquitectura antes de estudiar COR002.

El mínimo viable es:

1. disponer de un lote pequeño de COR002 traducido y revisado por hablantes;
2. distinguir provisionalmente qué expresiones se estudiarán productivamente y cuáles se usarán principalmente como input;
3. estudiar con un protocolo mínimo:
   - escucha;
   - intento de recuperación;
   - comprobación;
   - mantenimiento espaciado;
4. mantener COR001 activo con menor intensidad;
5. observar:
   - comprensión;
   - precisión;
   - latencia;
   - retención;
   - capacidad de respuesta;
6. registrar qué estructuras empiezan a generalizarse realmente.

No es indispensable todavía:

- saber el número final de conversaciones de COR002;
- cerrar G1–G5 como currículo del aprendiz;
- construir un sistema completo de niveles cognitivos;
- terminar el corrector;
- tener un Pattern Registry;
- tener PEDAGOGIA completamente cerrada;
- demostrar todos los patrones productivos antes de estudiar.

---

# 14. Experimento COR001

La auditoría propuso un experimento personal de 2–4 semanas para comparar:

- repetición actual;
- recuperación activa;
- recuperación + variabilidad.

Variables posibles:

- precisión;
- latencia;
- estabilidad;
- retención;
- transferencia.

Este experimento sigue siendo útil, pero responde a una pregunta limitada:

> cómo convertir material ya memorizado en acceso más rápido y flexible.

No debe utilizarse para resolver:

- número de conversaciones COR002;
- estructura final G/P;
- productividad real del Didxazá;
- arquitectura completa de COR002.

**Estado:** ÚTIL, NO PRIORIDAD 1.

---

# 15. Qué debe poder explicarse ante Irma Pineda

Para una conversación institucional no es necesario explicar:

- arquitectura completa del generador;
- versionado de prompts;
- corrector;
- Pattern Registry;
- detalles internos del pipeline.

Debe poder explicarse con claridad:

## COR001

- fue una primera capa de expresiones de uso;
- permitió comprobar que la exposición y memorización producen un repertorio inicial;
- también mostró límites: poca cobertura, latencia de recuperación y baja capacidad generativa.

## COR002

Busca pasar de frases relativamente aisladas a:

- escenas reales;
- funciones comunicativas;
- recurrencia;
- variación contextual;
- redes de expresiones relacionadas;
- mayor cobertura;
- posibilidad progresiva de reutilización.

## Principio lingüístico

El español sirve como punto de partida para elicitar situaciones y contrastes.

La forma final en Didxazá pertenece a los hablantes y a la evidencia lingüística.

No se presupone que las categorías o estructuras del español se transfieran directamente.

## Principio pedagógico

El objetivo no es memorizar diálogos completos.

El corpus debe permitir progresivamente:

- comprender;
- recuperar;
- responder;
- reutilizar;
- mantener interacción.

## Estado honesto

La metodología está en desarrollo y se está refinando con:

- experiencia de COR001;
- traducciones de COR002;
- documentación lingüística;
- trabajo con hablantes;
- observación del aprendizaje real.

---

# 16. Relación con Small Grant

El repositorio de Small Grant no debe convertirse en una segunda fuente de verdad sobre la pedagogía.

La fuente metodológica debe permanecer en Voces de las Nubes.

Small Grant debe consumir solo lo necesario para:

- explicar problema;
- justificar método;
- describir actividades;
- definir productos;
- presentar equipo y gobernanza;
- explicar validación;
- defender impacto y viabilidad.

---

# 17. Prioridades operativas

## PRIORIDAD 1 — Small Grant / Irma Pineda

Resolver:

- institución administradora o financiadora;
- estrategia para reunión con Irma;
- narrativa metodológica suficientemente clara;
- pendientes propios de la solicitud.

Razón:

depende de actores externos y oportunidades que no controla el proyecto.

---

## PRIORIDAD 2 — congelar este checkpoint

Este documento debe servir como memoria operativa.

No convertir inmediatamente todas sus propuestas en cambios canónicos.

---

## PRIORIDAD 3 — traducción y validación del piloto COR002

Generar datos reales en Didxazá.

Esto es indispensable para responder preguntas sobre:

- productividad;
- equivalencias estructurales;
- reutilización;
- dificultades de traducción;
- naturalidad.

---

## PRIORIDAD 4 — producir aprendizaje

Continuar COR001 bajo mantenimiento y comenzar COR002 cuando exista material suficientemente validado.

No esperar a que toda la teoría esté cerrada.

---

## PRIORIDAD 5 — corrector con alcance limitado

Definir productos A/B y detener expansión no alineada con ellos.

---

## PRIORIDAD 6 — generador v8

No rehacer el generador todavía como sistema pedagógico completo.

Preparar una **v8 de saneamiento arquitectónico** con las correcciones ya detectadas.

---

# 18. Alcance propuesto de una futura v8

La v8 debería corregir como mínimo:

1. microescena;
2. patrón_ES vs. patrón_Didxazá;
3. formulación de G como objetivo de elicitación;
4. comparación G3/G5;
5. conflicto interno TAREA/naturalidad;
6. función comunicativa en TAREA;
7. lenguaje de “etapas del aprendiz”.

No debería intentar todavía resolver:

- número final de conversaciones;
- currículo cognitivo completo;
- porcentaje COR001/COR002;
- Pattern Registry;
- Anki definitivo;
- pedagogía completa;
- automaticidad final.

---

# 19. Preguntas abiertas

## COR002

- ¿Cuántas conversaciones necesita realmente?
- ¿Qué determina que una función tenga cobertura suficiente?
- ¿Cuántas veces debe reaparecer un patrón?
- ¿Qué recurrencia debe existir dentro de una escena y cuál entre escenas?
- ¿Cómo se distribuyen G1–G5?
- ¿Qué significa exactamente superar un nivel?
- ¿G/P debe conservarse en su forma actual después de revisar más evidencia?

## Didxazá

- ¿Qué patrones proyectados desde el español corresponden realmente a estructuras productivas?
- ¿Qué construcciones aparentemente iguales en español se resuelven de manera diferente?
- ¿Qué fórmulas deben aprenderse como bloques?
- ¿Qué estructuras permiten sustitución o recombinación?
- ¿Qué diferencias dialectales afectan estas decisiones?

## Pedagogía

- ¿Qué debe ser receptivo?
- ¿Qué debe ser productivo?
- ¿Qué debe automatizarse?
- ¿Qué latencia es un criterio operativo útil?
- ¿Cómo medir estabilidad?
- ¿Cuándo introducir material nuevo?
- ¿Cómo mezclar COR001 y COR002?
- ¿Qué papel exacto tendrán Anki, audio, texto y producción?
- ¿Cuándo introducir variación y recombinación?

## Corrector / documentación

- ¿Cuándo deja un análisis de ser hipótesis?
- ¿Qué evidencia es suficiente para considerar un patrón usable?
- ¿Cómo se conecta la evidencia documental con la validación de hablantes?
- ¿Qué funcionalidades del corrector producen valor inmediato?

---

# 20. Decisiones que NO deben tomarse todavía

No fijar todavía:

- número final de conversaciones COR002;
- cantidad fija por nivel G/P;
- regla “terminar G1 antes de ver G2”;
- tercer eje cognitivo formal;
- porcentaje permanente COR001/COR002;
- obligatoriedad de memorizar conversaciones completas;
- productividad Didxazá inferida desde español;
- un número universal de segundos para definir automaticidad;
- arquitectura definitiva de Anki;
- implementación completa del Pattern Registry.

---

# 21. Regla de trabajo para evitar el loop de análisis

Se adopta provisionalmente esta regla operativa:

> **Una pregunta teórica nueva no debe detener una actividad que ya es suficientemente segura para producir evidencia nueva.**

Cuando aparezca una idea nueva:

1. registrar;
2. clasificar;
3. decidir si bloquea trabajo real;
4. si no bloquea, enviarla al backlog;
5. continuar la actividad que produce datos.

La creatividad del proyecto debe conservarse sin permitir que cada nueva hipótesis cambie inmediatamente la ruta de ejecución.

---

# 22. Estados de este checkpoint

## DECIDIDO / suficientemente estable

- conservar escena, función comunicativa, patrón, enunciado y microescena como terminología base;
- no adoptar “microinteracción”;
- COR001 pasa progresivamente de memorización a mantenimiento/recuperación;
- COR002 debe aumentar cobertura y recurrencia, no solo número de frases;
- español no es molde obligatorio del Didxazá;
- el generador no puede declarar por sí mismo productividad en Didxazá;
- G/P describe el material/generación y no debe asumirse todavía como currículo exacto del aprendiz;
- Small Grant no debe duplicar la fuente metodológica de Voces de las Nubes.

## CORREGIR PRONTO

- definición operativa de microescena en v7;
- patrón_ES vs. patrón_Didxazá;
- comparación G3/G5;
- conflicto TAREA/naturalidad;
- lenguaje de “etapa del aprendiz”;
- función comunicativa en TAREA.

## PROVISIONAL

- arquitectura exacta de estudio COR002;
- criterios de consolidación;
- distribución receptivo/productivo/automatizado;
- recurrencia longitudinal;
- forma final de G/P;
- diseño de v8.

## BLOQUEADO POR DATOS

- productividad real de muchos patrones;
- correspondencia entre patrones españoles y Didxazá;
- secuenciación basada en dificultad real;
- parte del léxico COR002 pendiente de revisión;
- decisiones que requieren traducciones y validación de hablantes.

## FUTURO

- Pattern Registry;
- integración plena corrector ↔ generador;
- currículo adaptativo;
- métricas automáticas de cobertura;
- arquitectura definitiva de Anki;
- formalización completa de PEDAGOGIA.

---

# 23. Próximo punto de reentrada recomendado

Cuando se retome este frente:

1. verificar y guardar este checkpoint en el repositorio de Voces de las Nubes;
2. no reabrir todas las preguntas;
3. atender primero Small Grant / Irma;
4. después revisar traducciones reales del piloto COR002;
5. usar esos datos para decidir qué cambios de v8 son realmente necesarios;
6. solo entonces actualizar documentos canónicos.

---

# 24. Nota final de estatus

Este documento congela una etapa de análisis.

No representa una metodología definitiva.

Su valor está en impedir dos riesgos:

1. perder hallazgos importantes al cambiar de chat o frente de trabajo;
2. convertir hipótesis interesantes en arquitectura obligatoria antes de producir suficiente evidencia.

La siguiente fase debe recuperar equilibrio entre:

**documentar → probar → aprender → corregir → volver a documentar.**