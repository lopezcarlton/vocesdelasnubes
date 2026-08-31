# COR002 — Checkpoint metodológico del piloto para principiantes
## Cómo llegamos al flujo manual actual y por qué

**Estado:** FROZEN_WORKFLOW_CHECKPOINT  
**Fecha:** 2026-08-31  
**Alcance:** COR002 — piloto de conversaciones para principiantes  
**Naturaleza del documento:** registro interno de decisiones y aprendizaje del proceso.

> Este documento **no convierte las decisiones provisionales en teoría pedagógica definitiva**. Congela el modo de trabajo que, por ahora, parece más productivo para construir unas cuantas conversaciones útiles y aprender de ellas antes de volver a automatizar.

---

# 1. Punto de partida

El trabajo comenzó con una pregunta más simple que la arquitectura a la que después llegamos:

> revisar la secuencia pedagógica, las situaciones, el prompt, el léxico y una muestra real del corpus para identificar debilidades que permitieran una mejora inmediata.

El material de partida ya tenía fortalezas importantes:

- una secuencia de dificultad gramatical **G1–G5**;
- una secuencia de dificultad pragmática **P1–P5**;
- un banco amplio de situaciones cotidianas;
- léxico cultural y situacional considerable;
- intención de progresión en espiral;
- escenas en español destinadas a ser reconstruidas posteriormente en didxazá por hablantes.

Pero la muestra producida revelaba varios problemas inmediatos.

---

# 2. Primeras debilidades identificadas

## 2.1. El mínimo rígido de longitud deformaba las escenas

El prompt v7 imponía un mínimo de aproximadamente veinte líneas.

Eso provocaba que situaciones simples, que podrían resolverse en pocos intercambios, se alargaran mediante:

- comentarios accesorios;
- pequeños incidentes;
- información de contexto no necesaria;
- saludos, cierres o transiciones añadidas para sostener la longitud;
- cambios de tema que no aportaban a la función principal.

La primera conclusión fue sencilla:

> **una conversación no debe durar más sólo para cumplir una cuota de turnos.**

## 2.2. La situación no bastaba para producir una buena conversación

“Mercado”, “visita”, “fiesta”, “casa” o “transporte” son escenarios, pero no especifican necesariamente una necesidad comunicativa.

Una escena mejora cuando existe una función clara:

- preguntar si hay algo;
- pedir una cantidad;
- elegir;
- ofrecer;
- rechazar;
- pedir ayuda;
- localizar;
- explicar;
- reparar;
- contar;
- confirmar.

Esto llevó a distinguir con más claridad:

**situación + función comunicativa + relación entre interlocutores + dificultad G/P**

*en lugar de depender únicamente de:*

**situación → conversación**.

## 2.3. Había situaciones habilitadas por pasos accesorios

Algunas situaciones podían aparecer en niveles tempranos únicamente porque ya tenían disponible un saludo, agradecimiento, despedida o elemento escénico, aunque todavía no estuviera disponible la acción comunicativa que justificaba la situación.

De ahí surgió la distinción:

- **CORE** — función que justifica la escena;
- **SUPPORT** — sostiene la interacción;
- **RITUAL** — saludo, agradecimiento, despedida;
- **SCENIC** — información de contexto.

Y el principio:

> **una situación sólo debe habilitarse cuando exista al menos un CORE compatible.**

Esta corrección sigue siendo útil y debe conservarse independientemente del generador que usemos.

---

# 3. Lo que pasó al intentar corregir el sistema

En vez de quedarnos en esas correcciones simples, comenzamos a iterar sucesivas versiones del generador.

Cada versión resolvió un problema real, pero con frecuencia abrió otro.

## 3.1. v7 — conversaciones con vida, pero deformadas por sus propias obligaciones

**Fortalezas:**

- conversaciones reconocibles como escenas;
- personajes;
- relaciones;
- cierta continuidad;
- naturalidad como prioridad declarada;
- repetición cualitativa de uno o dos patrones;
- progresión G/P ya presente.

**Problemas:**

- mínimo duro de veinte líneas;
- tendencia a rellenar;
- inconsistencias G/P;
- situaciones habilitadas sin CORE;
- clasificación pedagógica duplicada o contradictoria;
- el español intentaba a veces hacer demasiado visible la gramática que después debía realizarse en didxazá.

## 3.2. v8 — más control, pero escenas demasiado fragmentarias

Se intentó resolver:

- longitud artificial;
- inconsistencias pedagógicas;
- control de nivel;
- léxico funcional;
- activación por CORE.

El resultado produjo escenas de cuatro a seis turnos que podían ser limpias desde el punto de vista pedagógico, pero ya no daban:

- suficiente contexto al hablante;
- suficiente material al estudiante;
- una interacción que pudiera sostenerse más allá de una pareja pregunta–respuesta.

**Aprendizaje:**

> **la microinteracción puede ser una unidad interna, pero no debe sustituir a la escena completa como corpus fuente.**

## 3.3. v8.1 — recuperó la escena completa, pero empezó a sobreactuar

Se devolvió:

- longitud suficiente;
- varios movimientos conversacionales;
- entrada, desarrollo y resolución.

Pero aparecieron:

- personajes demasiado caracterizados;
- regionalismos acumulados;
- exceso de elementos culturales;
- pequeñas “tramas” construidas para que la escena tuviera arco.

**Aprendizaje:**

> **localidad no equivale a imitar un sociolecto ni a acumular marcas culturales.**

## 3.4. v8.2 — menos caricatura, pero demasiado ritmo de entrevista

Se naturalizó el registro, pero muchas escenas quedaron organizadas así:

> pregunta → respuesta → pregunta → respuesta → pregunta → respuesta

Las frases podían ser individualmente plausibles y, aun así, la conversación sonaba artificial.

**Aprendizaje:**

> los hablantes también ofrecen información, anticipan, reaccionan, corrigen, asocian y dejan cosas sin preguntar.

## 3.5. v8.3/v8.4 — mejor flujo, pero comenzaron las regresiones de reglas

Se añadieron:

- información voluntaria;
- asimetría de turnos;
- cobertura no exhaustiva;
- distinción entre elección funcional y comparación completa;
- distinción entre condicional instructivo básico y condicional pleno.

Estas correcciones fueron útiles.

Pero también apareció otro problema: al reescribir y compactar prompts se perdían reglas anteriores.

**Aprendizaje:**

> **las reglas pedagógicas y de validación necesitan trazabilidad; no deben depender de que una nueva redacción recuerde todo lo anterior.**

## 3.6. v8.5 — más coherencia, pero demasiada trama

Se intentó controlar:

- referentes;
- objetos;
- acciones;
- compromisos;
- tiempo;
- transacciones;
- estado final.

Esto corrigió contradicciones, pero la coherencia empezó a actuar como **motor de construcción**.

Para tener algo que rastrear, las escenas empezaban a inventar:

- apartados;
- reservas;
- compromisos;
- fechas;
- devoluciones;
- pequeños problemas;
- cierres que resumían explícitamente el estado.

**Aprendizaje:**

> **la coherencia debe servir para rechazar una contradicción, no para obligar a que la escena tenga una trama compleja.**

## 3.7. v8.6 — más adquirible, pero apareció el extremo contrario

Se intentó priorizar:

- repetición del patrón;
- complejidad limitada;
- pocos lexemas nuevos;
- turnos breves;
- material de reuso.

Algunas escenas mejoraron claramente.

Pero otras terminaron pareciendo:

> ejercicios de sustitución con nombres de personajes.

La repetición estaba presente, pero ya no había una razón suficiente para conversar.

**Aprendizaje:**

> **una conversación pedagógica no debe convertirse en un drill disfrazado.**

---

# 4. El hallazgo que cambió el método

Después de varias horas de iteración quedó claro que el problema principal ya no era encontrar otra regla.

El problema era más básico:

> **todavía no existía una escena de COR002 que hubiera sido aprobada explícitamente como modelo de lo que queremos producir.**

Sin una escena aprobada:

- cada nueva regla se calibraba contra una intuición;
- la intuición cambiaba según el último problema encontrado;
- una versión corregía naturalidad y rompía adquisición;
- otra corregía adquisición y rompía conversación;
- otra corregía coherencia y añadía trama.

Se decidió detener temporalmente:

- nuevas versiones;
- auditorías sucesivas;
- expansión masiva del corpus;
- ingeniería adicional del generador.

Y cambiar el orden de trabajo.

---

# 5. Nuevo principio de trabajo

## Primero una escena buena. Después las reglas.

La unidad de aprendizaje metodológico pasa a ser una conversación concreta.

El procedimiento actual es:

1. seleccionar una situación sencilla;
2. decidir quién es el aprendiz;
3. proponer una escena breve;
4. revisar manualmente la conversación;
5. corregirla hasta que el contexto y la interacción sean plausibles;
6. **sólo después** analizar qué G/P, patrones, complejidad, recurrencias y posibilidades de reuso contiene.

No se intenta primero construir la arquitectura perfecta.

Se intenta primero responder:

> **¿esto es algo que realmente queremos grabar y estudiar?**

---

# 6. Reparto de responsabilidades

## 6.1. Juicio contextual y social

La persona que conoce el contexto local decide principalmente:

- si alguien diría realmente una línea;
- si una acción tiene sentido en esa situación;
- si una cantidad, precio, unidad o práctica es verosímil;
- si una conversación tiene una lógica social plausible;
- si falta algo que normalmente ocurriría;
- si algo está artificialmente escrito desde una lógica externa.

El procedimiento de revisión manual se simplifica deliberadamente a:

- **SÍ** — esto puede quedar;
- **NO** — esto no se diría / no funciona;
- **FALTA** — aquí falta algo necesario.

Si una línea es casi correcta, se corrige directamente.

## 6.2. Diseño pedagógico y complejidad

La secuencia **G/P se conserva**.

No se espera que el juicio contextual resuelva:

- clasificación gramatical;
- patrones de adquisición;
- techo de complejidad;
- progresión entre niveles;
- reciclaje estructural;
- qué puede aparecer antes o después pedagógicamente.

Eso se analiza después de tener una escena contextual y conversacionalmente aceptable.

El reparto actual es:

> **contexto y plausibilidad primero; análisis pedagógico después.**

## 6.3. Papel del hablante de didxazá

El hablante no entra para rescatar una conversación en español que ya parece mala.

Orden actual:

1. se construye la escena fuente;
2. se corrige manualmente hasta que la escena parece adecuada;
3. entonces el hablante trabaja la realización en didxazá;
4. a partir de esa realización se evalúa qué partes realmente sobreviven, cambian, se reestructuran o deben descartarse.

Principio:

> **si la escena fuente todavía no convence, no tiene sentido pedir al hablante que la resuelva.**

Esto evita usar la traducción como mecanismo para reparar problemas que pertenecen al diseño del corpus.

---

# 7. Alcance provisional de COR002

Se tomó una decisión deliberada de reducción de alcance:

> **por ahora COR002 se concentrará en unas cuantas conversaciones para principiantes.**

No se pretende resolver todavía:

- todo el banco de situaciones;
- todos los niveles G1–G5;
- toda la progresión pragmática;
- el generador general;
- una pedagogía definitiva.

El objetivo inmediato es conseguir **unas pocas conversaciones que realmente funcionen**.

---

# 8. Qué significa “principiante” en este checkpoint

La definición de trabajo propuesta es:

> **El aprendiz puede resolver solo una interacción cotidiana breve, cara a cara, con un interlocutor cooperativo y sobre algo presente o concreto.**

Esto no se adopta como definición universal de “principiante”.

Se usa como frontera operativa para el piloto.

Sus implicaciones aproximadas son:

- interacción breve;
- contexto claro;
- poca inferencia;
- un interlocutor que coopera;
- necesidad comunicativa inmediata;
- el aprendiz produce una parte sustancial de la conversación;
- no depende de explicar una postura compleja;
- no depende de narración extensa;
- no depende de subordinación o negociación avanzada.

---

# 9. Corte G/P provisional

La primera propuesta fue:

**G1–G3 / P1–P2**

porque:

- G4 introduce saltos importantes de complejidad;
- P3 puede introducir negociación, postura o mayor riesgo social.

Después se decidió **probar P3**, porque algunas interacciones cotidianas pueden necesitar una preferencia o elección sencilla para no volverse artificiales.

Checkpoint actual:

> **G1–G3 / P1–P3, con P3 en prueba y completamente reversible.**

Esto NO significa que P3 quede aprobado como parte definitiva del nivel principiante.

Regla operativa:

> si P3 empieza a exigir demasiada negociación, complejidad o estructuras que rompen la escena, se vuelve a dejar fuera.

---

# 10. Qué tipo de P3 estamos probando

P3 no se abre de manera indiscriminada.

En una compra, por ejemplo, se prueba como:

- elegir entre dos opciones presentes;
- expresar una preferencia;
- sostener una elección sencilla.

No se abre automáticamente a:

- regatear;
- reclamar;
- convencer;
- mediar;
- negociar una condición compleja.

Ejemplo del límite buscado:

> “Sí, pero me gusta más el chiquito.”

Esto puede funcionar como preferencia sencilla.

No equivale a abrir toda la comparación productiva o la negociación avanzada.

---

# 11. Primera escena de referencia: mercado

Se eligió:

- **situación:** mercado;
- **rol del aprendiz:** comprador.

La escena se escribió sin intentar demostrar de antemano un aparato completo de reglas.

La revisión se hizo sobre:

- verosimilitud;
- forma de pedir;
- disponibilidad;
- selección;
- cantidad;
- información del vendedor;
- cierre.

Durante la revisión surgieron preguntas contextuales muy concretas:

- si una expresión como “se acabó temprano” es natural;
- cómo se pide realmente cierta mercancía;
- qué unidades son verosímiles;
- qué precio tiene sentido;
- qué distinciones entre productos existen realmente;
- qué explicación daría una vendedora;
- qué parte de la conversación sobra.

Este tipo de duda se considera ahora **productiva**, porque señala exactamente qué información contextual necesita COR002.

No se intenta resolver con una regla genérica.

---

# 12. Primera revisita de la situación

La misma situación se volvió a usar un escalón arriba.

Esto recupera una idea valiosa de la progresión en espiral:

> **una situación no se “termina” en una sola conversación.**

La primera escena puede trabajar disponibilidad y cantidad.

La revisita puede añadir:

- elección;
- preferencia;
- contraste simple;
- una instrucción breve.

El lugar es el mismo, pero cambia lo que el aprendiz puede hacer.

Esta lógica de revisita se conserva.

---

# 13. Qué se conserva del trabajo técnico anterior

Aunque se haya detenido la escalada de versiones, no se descarta todo el trabajo anterior.

Se conservan especialmente las correcciones que son independientes del estilo del generador.

## 13.1. La secuencia G/P

Sigue siendo una pieza central.

No se abandona.

Lo que cambia es el orden:

> **primero se corrige la escena; después se usa G/P para analizar y calibrar.**

## 13.2. CORE / SUPPORT / RITUAL / SCENIC

Se conserva como herramienta para evitar situaciones vacías.

## 13.3. Exclusión de dominios no prioritarios

Por ahora se mantienen fuera del banco prioritario:

- Ir al médico;
- Comprar medicina.

Esto forma parte del recorte actual del corpus y puede revisarse más adelante si aparece evidencia nueva.

## 13.4. Correcciones de clasificación ya detectadas

No se vuelven a introducir conscientemente inconsistencias ya identificadas en:

- comparación;
- interrogativas;
- condicional;
- activación por etapa;
- variantes de pasos.

Pero estas correcciones deben seguir siendo revisables conforme avance el conocimiento lingüístico.

---

# 14. Qué NO se congela como regla

Este checkpoint congela un **modo de trabajo**, no una pedagogía definitiva.

No quedan congelados como verdad:

- G1–G3 / P1–P3 como frontera definitiva;
- diez a catorce turnos como longitud obligatoria;
- un número mínimo de repeticiones;
- un número máximo de lexemas;
- un banco automático de marcos;
- perfiles aritméticos de adquisición;
- state sheets;
- contadores de estructuras superiores;
- un supuesto número ideal de escenas;
- la idea de que toda conversación deba terminar del mismo modo;
- las escenas experimentales producidas durante v8.x.

En particular:

> **no se deben convertir automáticamente los materiales pedagógicos producidos durante esta fase en reglas permanentes del proyecto.**

Las hipótesis pedagógicas siguen abiertas a revisión.

---

# 15. Qué se congela para el piloto actual

Mientras dure este piloto, sí se toma como flujo de trabajo por defecto:

1. **No generar COR002 masivamente.**
2. Trabajar **pocas conversaciones de principiantes**.
3. Empezar por situaciones concretas y cotidianas.
4. Declarar quién es el aprendiz.
5. Producir una primera escena sencilla.
6. Entregar la conversación en **tabla de dos columnas**:
   - `Personaje`
   - `Conversación`
7. Revisar manualmente:
   - SÍ;
   - NO;
   - FALTA.
8. Corregir incoherencias, prácticas improbables y turnos artificiales antes de hacer análisis pedagógico.
9. Usar después G/P, patrones y complejidad para entender qué contiene la escena.
10. Mantener **G1–G3 / P1–P3 como ventana experimental**, con P3 reversible.
11. Revisitar situaciones para construir una progresión en espiral.
12. No enviar una escena al hablante hasta que la fuente en español sea aceptable.
13. No convertir automáticamente la traducción posterior en validación de todas las decisiones pedagógicas.
14. No volver todavía a la expansión general del banco ni al generador masivo.

---

# 16. Formato de entrega congelado

Cada conversación se presenta únicamente con dos columnas:

| Personaje | Conversación |
|---|---|
| Rita | ¿Hay camarón seco? |
| Marchanta | Ya no hay camarón, se acabó temprano. |

Los metadatos pedagógicos pueden aparecer fuera de la tabla cuando sea necesario.

No se añaden columnas pedagógicas dentro del diálogo.

---

# 17. Criterio para saber si una escena avanza

En esta fase, una conversación no se considera buena porque:

- cumpla un número de turnos;
- alcance una cuota de patrones;
- contenga cierto número de palabras;
- pase un checklist formal.

La pregunta principal es:

> **¿esta conversación merece convertirse en material de COR002?**

Para avanzar debe satisfacer, al menos de manera práctica:

- la situación tiene sentido;
- el aprendiz tiene algo útil que hacer;
- los turnos no parecen escritos sólo para enseñar una estructura;
- no hay incoherencias obvias;
- la conversación puede imaginarse ocurriendo;
- hay material que parece potencialmente aprendible;
- el nivel de dificultad parece compatible con el piloto;
- la escena merece ser llevada al siguiente paso con el hablante.

---

# 18. Por qué se congela este método ahora

Se congela porque el proceso anterior mostró repetidamente que:

- corregir el prompt sin escenas de referencia produce oscilaciones;
- una regla nueva puede resolver un síntoma y crear otro;
- naturalidad, adquisición y coherencia no se optimizan bien si se intentan imponer todas desde una sola instrucción;
- el conocimiento contextual no puede sustituirse por reglas abstractas;
- la secuencia pedagógica sí aporta valor, pero funciona mejor como capa de análisis y calibración que como sustituto del juicio sobre la conversación.

El cambio de orden es entonces:

## Antes

**reglas → generación → auditoría → nueva regla**

## Ahora

**escena → revisión contextual → corrección → análisis G/P → hablante → aprendizaje metodológico**

Este cambio es el contenido central del checkpoint.

---

# 19. Objetivo inmediato

El objetivo inmediato NO es producir COR002 completo.

Es conseguir unas pocas escenas que podamos señalar y decir:

> **“Esto empieza a parecer COR002.”**

Después de contar con varias escenas aceptadas podremos:

- comparar qué tienen en común;
- detectar qué patrones se adquieren de manera natural;
- observar qué G/P funciona realmente;
- estudiar cuánto reuso ofrece cada escena;
- decidir qué partes del trabajo técnico anterior vuelven a entrar;
- rediseñar, si hace falta, un generador mucho más pequeño y mejor fundado.

Hasta entonces, las escenas aprobadas son evidencia de diseño más importante que una nueva versión del prompt.

---

# 20. Estado de decisiones

## CONGELADO PARA EL PILOTO

- pocas conversaciones;
- principiantes;
- revisión manual antes de escalar;
- G/P se conserva;
- CORE gate se conserva;
- formato `Personaje | Conversación`;
- el juicio contextual decide plausibilidad;
- el análisis pedagógico decide patrones y complejidad;
- el hablante entra después de que la escena fuente es aceptable;
- progresión por revisita;
- sin generación masiva por ahora.

## PROVISIONAL / EN PRUEBA

- G1–G3;
- P1–P3;
- P3 como borde reversible;
- definición funcional actual de “principiante”;
- longitud aproximada de escenas;
- cantidad de repetición;
- cantidad de léxico nuevo;
- qué situaciones exactas forman el piloto.

## NO ACTIVO POR AHORA

- generador masivo;
- nuevas auditorías de arquitectura;
- expansión a todo el banco;
- perfiles numéricos rígidos;
- banco automático de reuso como obligación;
- nueva versión general del prompt antes de tener escenas aceptadas.

---

# 21. Nota de comunicación externa

Este documento registra el razonamiento interno del proyecto.

Cuando estos resultados se discutan con colaboradores externos, el foco debe ponerse en:

- metodología pedagógica;
- secuencia G/P;
- situaciones;
- naturalidad;
- revisión contextual;
- trabajo con hablantes;
- aprendizaje obtenido de las escenas.

Por ahora no es necesario compartir detalles sobre las herramientas internas utilizadas para producir, comparar o revisar borradores.

---

# 22. Fórmula resumida del nuevo estilo de trabajo

> **Primero conseguimos una conversación que valga la pena.  
> Después entendemos pedagógicamente por qué funciona.  
> Sólo entonces decidimos qué debe aprender el generador de ella.**

Ese es el método que queda congelado para la siguiente fase de COR002.
