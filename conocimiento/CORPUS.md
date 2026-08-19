# CORPUS

**Proyecto:** Voces de las Nubes  
**Versión:** 1.1  
**Estado:** Borrador consolidado y evolutivo  
**Fecha:** 2026-08-19  

---

# 1. Objetivo del corpus

El corpus de Voces de las Nubes reúne materiales lingüísticos destinados a construir una progresión de aprendizaje auditivo del Didxazá basada en situaciones comunicativas reales.

Su función no es acumular frases ni producir un inventario temático exhaustivo. Su función es ofrecer unidades de habla que permitan al aprendiz:

- reconocer expresiones frecuentes;
- comprender acciones comunicativas;
- producir enunciados breves;
- reutilizar patrones;
- ampliar progresivamente su capacidad de interacción;
- relacionar lengua, contexto y uso.

El corpus constituye la base lingüística y dramatúrgica de los materiales de aprendizaje, pero no sustituye:

- la metodología general del proyecto;
- la producción técnica del audio;
- la fundamentación pedagógica;
- la bibliografía;
- la validación lingüística y comunitaria.

---

# 2. Unidad de diseño

## 2.1 La escena comunicativa

La unidad inicial de diseño es la escena comunicativa.

Una escena representa una interacción reconocible dentro de la vida cotidiana y contiene:

- un contexto;
- uno o más participantes;
- una necesidad;
- un objetivo comunicativo;
- una secuencia posible de turnos;
- restricciones pragmáticas y culturales;
- recursos lingüísticos necesarios.

La escena no se convierte automáticamente en lección ni en bloque del corpus.

Primero debe descomponerse en funciones comunicativas.

## 2.2 La función comunicativa

La unidad funcional del corpus es la acción que una persona puede realizar mediante la lengua.

Ejemplos:

- saludar;
- responder a un saludo;
- presentarse;
- preguntar por alguien;
- pedir ayuda;
- localizar un objeto;
- expresar hambre, cansancio o dolor;
- confirmar;
- negar;
- agradecer;
- despedirse.

Una misma escena puede contener varias funciones.

Una misma función puede aparecer en distintas escenas.

## 2.3 El patrón

Un patrón es una estructura lingüística productiva.

No equivale a:

- una palabra;
- un verbo;
- un tema;
- una frase superficialmente parecida;
- una variación de dato dentro de la misma estructura.

Por ejemplo, expresiones que comparten un verbo pueden representar patrones distintos si cambia su estructura sintáctica.

El corpus debe permitir que un patrón ya introducido aparezca en varios contextos.

## 2.4 El enunciado

El enunciado es la unidad mínima concreta que se registra, transcribe, cataloga y utiliza en los materiales.

Todo enunciado debe justificar su presencia mediante al menos uno de estos criterios:

- introduce una función necesaria;
- introduce un patrón productivo;
- refuerza una estructura previa en un contexto nuevo;
- aporta una expresión de alta utilidad;
- completa una microescena;
- representa una forma validada culturalmente;
- permite producción oral;
- resuelve un vacío detectado.

## 2.5 La microescena

La microescena es una secuencia breve de turnos con suficiente contexto para que los enunciados no aparezcan como frases aisladas.

Debe conservar:

- coherencia;
- economía;
- propósito;
- naturalidad;
- relación entre turnos;
- progresión interna.

No debe crecer mediante relleno ni cumplir una lista rígida de movimientos dramáticos.

---

# 3. Arquitectura del corpus

## 3.1 COR001

COR001 constituye el primer bloque de 107 frases trabajado y validado oralmente con hablantes, pero **no está cerrado como producto final**.

Su estado vigente es de consolidación final. Permanecen pendientes, entre otros aspectos:

- revisión ortográfica sistemática de las traducciones;
- incorporación de correcciones derivadas de esa revisión;
- regrabación de materiales que no hayan quedado suficientemente bien;
- normalización final del audio;
- preparación y entrega de derivados para Anki y escucha.

Por tanto, la expresión «validado» en COR001 describe principalmente el trabajo lingüístico y oral realizado hasta ahora; no significa que texto, ortografía, audio y distribución estén definitivamente cerrados.

COR001 se conserva como base de referencia para:

- detectar repeticiones;
- identificar estructuras ya cubiertas;
- medir novedades;
- construir progresión;
- conservar trazabilidad entre texto y audio.

COR001 no debe ampliarse retroactivamente sin una razón documentada, pero sí puede corregirse, regrabarse o normalizarse mientras permanezca abierto.

## 3.2 COR002

El primer borrador de COR002, correspondiente a las frases 108–224, dejó de considerarse una continuación válida de COR001.

El bloque anterior presentaba:

- repeticiones;
- variantes sin ganancia pedagógica;
- vocabulario aislado;
- baja productividad de varios enunciados;
- dependencia de categorías temáticas;
- falta de progresión clara;
- expresiones seleccionadas por valor poético o cultural sin suficiente función comunicativa.

Las frases de ese borrador no están prohibidas de manera individual.

Pueden recuperarse únicamente si superan una nueva revisión basada en:

- función;
- frecuencia;
- productividad;
- relación con COR001;
- naturalidad;
- validación comunitaria;
- pertinencia pedagógica.

No existe todavía una versión definitiva de COR002.

Su diseño permanece en revisión profunda. Entre los factores que pueden modificarlo están:

- la revisión pendiente con Vicente Gutiérrez;
- una nueva revisión de situaciones comunicativas;
- la revisión del sistema de complejidad gramatical y pragmática;
- la incorporación de reglas gramaticales y ortográficas extraídas de la literatura disponible;
- los resultados del trabajo de corrección ortográfica y análisis lingüístico actualmente en curso.

No se ha realizado ninguna grabación de COR002.

## 3.3 Corpus posteriores

Los corpus posteriores deben conservar continuidad con lo ya aprendido y ampliar capacidad comunicativa real.

No se estructuran como:

- repetición de los mismos bloques temáticos;
- listas de vocabulario;
- capítulos gramaticales;
- colecciones de frases traducidas;
- secuencias arbitrarias de dificultad.

Deben construirse mediante matrices que relacionen, cuando resulte útil:

- escena;
- función;
- patrón;
- cobertura previa;
- novedad;
- carga gramatical;
- carga pragmática;
- léxico;
- participantes;
- estado de validación.

## 3.4 Arquitectura provisional para generación de borradores

El sistema de generación automática de conversaciones en español ha trabajado con una arquitectura de tres capas: motor, datos y tarea.

Esta arquitectura es **provisional y está sujeta a revisión**. No debe tratarse como diseño definitivo del generador mientras continúe la integración de nueva evidencia gramatical, ortográfica, metodológica y pedagógica.

### Capa 1: Motor

Contiene reglas sobre:

- naturalidad;
- gramática;
- pragmática;
- dramatización;
- longitud;
- ritmo;
- formato;
- prohibiciones.

Las versiones históricas del prompt del generador conservan valor de trazabilidad, pero ninguna debe considerarse estable por el solo hecho de ser la versión más reciente.

### Capa 2: Datos

Puede contener bancos actualizables de:

- situaciones;
- niveles o etiquetas de complejidad;
- léxico;
- patrones;
- personajes.

Su estructura deberá revisarse a la luz de la evidencia lingüística acumulada.

### Capa 3: Tarea

Contiene decisiones concretas para cada conversación, como:

- situación;
- patrón;
- léxico;
- personajes;
- presencia o ausencia de saludo;
- restricciones particulares.

La relación exacta entre estas capas y el futuro controlador externo sigue abierta.

---

# 4. Cobertura comunicativa

## 4.1 Cobertura por funciones

La cobertura principal debe medirse por funciones comunicativas.

El crecimiento del corpus debe responder:

- qué puede hacer ahora el aprendiz;
- qué no podía hacer antes;
- en cuántos contextos puede reutilizar una función;
- qué funciones siguen ausentes;
- qué funciones están sobrerrepresentadas.

## 4.2 Cobertura por patrones

El corpus debe registrar:

- patrones introducidos;
- patrones reforzados;
- contextos en los que aparecen;
- dependencia de patrones anteriores;
- frecuencia de reutilización;
- patrones subrepresentados.

La cobertura de patrones no puede deducirse únicamente por palabras compartidas.

## 4.3 Cobertura léxica

El léxico se organiza como recurso rotativo.

Debe distinguirse entre:

- vocabulario de contenido;
- marcadores conversacionales;
- expresiones fijas;
- palabras funcionales;
- relaciones espaciales;
- relaciones temporales;
- estados físicos;
- estados emocionales;
- preguntas fundamentales.

La repetición léxica debe ser suficiente para favorecer retención, pero no debe producir escenas mecánicas.

## 4.4 Cobertura pragmática

El corpus debe representar variación en:

- formas de iniciar;
- formas de cerrar;
- grados de confianza;
- respuestas breves;
- duda;
- corrección;
- confirmación;
- rechazo;
- cortesía;
- asimetría entre interlocutores;
- cambios naturales de turno.

Los saludos, agradecimientos y despedidas no deben aparecer como requisitos fijos en todas las escenas.

## 4.5 Cobertura de género

El total de personajes debe tender a un balance 50/50 entre mujeres y hombres.

Las combinaciones por conversación son libres:

- mujer–hombre;
- mujer–mujer;
- hombre–hombre;
- grupos mixtos.

El balance se evalúa sobre el conjunto acumulado, no de forma rígida en cada escena.

## 4.6 Cobertura de situaciones

Las situaciones constituyen un inventario de origen, no una secuencia pedagógica definitiva.

Cada situación debe evaluarse según:

- frecuencia;
- pertinencia;
- variedad;
- carga lingüística;
- carga pragmática;
- dependencia de recursos previos;
- oportunidad de producción;
- valor cultural;
- posibilidad de validación.

---

# 5. Criterios de selección

## 5.1 Utilidad comunicativa

Se priorizan enunciados que permiten realizar acciones frecuentes y transferibles.

Se evita incluir expresiones únicamente porque:

- son curiosas;
- son poéticas;
- representan un tema;
- permiten completar una cuota;
- contienen vocabulario nuevo;
- aparecen en una fuente sin contexto de uso.

## 5.2 Productividad

Un enunciado tiene mayor valor cuando su estructura puede reutilizarse.

Se priorizan materiales que permitan:

- sustituir participantes;
- cambiar objetos;
- cambiar lugares;
- cambiar tiempos;
- cambiar polaridad;
- formular respuestas;
- ampliar una interacción.

## 5.3 Frecuencia

La frecuencia orienta, pero no decide por sí sola.

Una expresión frecuente puede ser pedagógicamente compleja.

Una expresión menos frecuente puede ser necesaria para completar una función básica.

La frecuencia debe combinarse con:

- dificultad;
- productividad;
- contexto;
- relevancia;
- posibilidad de validación.

## 5.4 Naturalidad

Todo material debe sonar plausible dentro de la situación.

Se rechazan:

- traducciones literales;
- frases que nadie diría en ese contexto;
- preguntas y respuestas simétricas de forma mecánica;
- cadenas artificiales;
- repeticiones visibles como ejercicio;
- explicaciones impropias de la escena.

## 5.5 Producibilidad

Los enunciados deben poder ser intentados por el aprendiz.

Se consideran:

- longitud;
- número de novedades;
- estructura;
- ritmo;
- posibilidad de segmentación;
- dependencia del contexto;
- memoria necesaria.

## 5.6 Ganancia pedagógica

Cada nueva incorporación debe aportar algo identificable.

No se incorpora una frase cuando únicamente:

- cambia un número;
- cambia un nombre;
- cambia un objeto sin ampliar uso;
- repite la misma función;
- duplica un patrón sin contexto nuevo;
- reformula superficialmente un enunciado previo.

## 5.7 Pertinencia cultural

La escena y los enunciados deben ser revisados para evitar:

- usos ajenos a la vida local;
- situaciones inventadas desde expectativas externas;
- registros inadecuados;
- relaciones sociales mal representadas;
- generalizaciones culturales;
- fórmulas sociales sobrerrepresentadas.

## 5.8 Trazabilidad

Todo enunciado debe conservar relación con:

- corpus;
- número;
- escena;
- fuente;
- hablante;
- toma de audio;
- transcripción;
- traducción;
- validación;
- estado.

---

# 6. Organización interna

## 6.1 Identificadores

Los elementos del corpus utilizan identificadores estables.

La numeración no debe depender del texto de la frase, porque:

- la traducción puede corregirse;
- la escritura puede cambiar;
- la segmentación puede revisarse;
- el título humano puede actualizarse.

Los identificadores deben permanecer estables aunque cambie la representación.

## 6.2 Relación entre COR y AUD

Cada elemento lingüístico debe relacionarse con su material de audio cuando exista.

La relación debe permitir reconstruir:

- qué texto corresponde a qué grabación;
- qué hablante participa;
- qué toma se utiliza;
- qué versión está vigente;
- qué derivados existen;
- qué cambios se realizaron.

El nombre técnico del archivo conserva el identificador.

La frase puede añadirse como metadato de título.

## 6.3 Estados

Cada elemento del corpus debe poder marcarse como:

- propuesto;
- borrador;
- en revisión;
- pendiente de validación;
- validado;
- aprobado;
- reemplazado;
- descartado.

Un elemento no debe presentarse como definitivo únicamente por haber sido grabado o validado oralmente.

## 6.4 Versiones

Los cambios deben distinguir entre:

- corrección ortográfica;
- cambio de traducción;
- cambio de segmentación;
- sustitución del enunciado;
- cambio de hablante;
- nueva toma;
- cambio de contexto;
- cambio de función;
- cambio de patrón.

No todos los cambios requieren crear un nuevo identificador.

Los cambios que alteran sustancialmente la unidad lingüística deben registrarse como nueva versión o nueva entrada, según corresponda.

## 6.5 Metadatos mínimos

Cada entrada debería registrar, como mínimo:

- ID;
- corpus;
- número;
- español de partida;
- Didxazá;
- sistema de escritura;
- transcripción técnica cuando exista;
- función comunicativa;
- patrón;
- escena;
- nivel o etiquetas de complejidad cuando correspondan;
- hablante;
- validador;
- localidad o variante cuando sea pertinente;
- estado;
- audio relacionado;
- notas;
- versión.

## 6.6 Escritura

La forma principal adoptada para los materiales es el Alfabeto Popular.

El AFI se utiliza como sistema técnico secundario cuando sea necesario.

Las decisiones ortográficas permanecen sujetas a validación por hablantes, revisión especializada y al trabajo de corrección sistemática en curso.

La escritura no debe reemplazar la referencia oral cuando exista incertidumbre.

---

# 7. Principio de evolución

Este documento describe una arquitectura de trabajo, no un sistema terminado.

La evidencia procedente de hablantes, corrección ortográfica, bibliografía, pruebas del generador, validación pedagógica y trabajo de audio puede modificar sus categorías y relaciones.

Toda modificación sustantiva debe seguir las reglas de actualización del Sistema de Conocimiento.
