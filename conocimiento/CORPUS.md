# CORPUS

**Proyecto:** Voces de las Nubes  
**Versión:** 1.0  
**Estado:** Borrador consolidado  
**Fecha:** 2026-08-05  

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

COR001 constituye el primer bloque validado de frases básicas.

Su versión consolidada contiene 107 frases.

Incluye materiales relacionados con:

- saludos y despedidas;
- presentación;
- familia;
- cuerpo;
- comida;
- entorno;
- verbos cotidianos;
- preguntas esenciales;
- números y tiempo;
- cortesía y afecto;
- negación.

COR001 se conserva como base de referencia para:

- detectar repeticiones;
- identificar estructuras ya cubiertas;
- medir novedades;
- construir progresión;
- conservar trazabilidad entre texto y audio.

COR001 no debe ampliarse retroactivamente sin una razón documentada.

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

## 3.3 Corpus posteriores

Los corpus posteriores deben conservar continuidad con lo ya aprendido y ampliar capacidad comunicativa real.

No se estructuran como:

- repetición de los mismos bloques temáticos;
- listas de vocabulario;
- capítulos gramaticales;
- colecciones de frases traducidas;
- secuencias arbitrarias de dificultad.

Deben construirse mediante matrices que relacionen:

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

## 3.4 Arquitectura de tres capas para generación de borradores

El sistema de generación automática de conversaciones en español se organiza en tres capas.

### Capa 1: Motor

Contiene las reglas estables sobre:

- naturalidad;
- gramática;
- pragmática;
- dramatización;
- longitud;
- ritmo;
- formato;
- prohibiciones.

La versión vigente es `prompt_generador_corpus_v7.md`.

Las versiones v5 y v6 quedan obsoletas.

### Capa 2: Datos

Contiene los bancos actualizables:

- situaciones;
- niveles gramaticales;
- niveles pragmáticos;
- léxico;
- patrones;
- personajes.

Los archivos identificados son:

- `corpus_v2.txt`;
- `lexico_v2.txt`.

### Capa 3: Tarea

Contiene las decisiones concretas para cada conversación:

- situación;
- patrón;
- léxico;
- personajes;
- presencia o ausencia de saludo;
- restricciones particulares.

El motor no debe recibir déficits numéricos crudos para decidir qué compensar.

La tarea debe llegar resuelta por un controlador externo o por preparación manual.

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

Cada elemento lingüístico debe relacionarse con su material de audio.

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

Un elemento no debe presentarse como definitivo únicamente por haber sido grabado.

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
- nivel;
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

Las decisiones ortográficas permanecen sujetas a validación por hablantes y revisión especializada.

La escritura no debe reemplazar la referencia al audio.

## 6.7 Variación

Cuando existan formas distintas, debe registrarse si la diferencia corresponde a:

- localidad;
- generación;
- estilo;
- persona;
- contexto;
- preferencia;
- incertidumbre;
- posible error;
- cambio lingüístico.

No se debe fusionar automáticamente la variación en una sola forma normalizada.

---

# 7. Generación de borradores en español

## 7.1 Alcance

El generador produce conversaciones dramatúrgicas únicamente en español.

No produce Didxazá.

Su función es crear material de partida para:

- revisión;
- selección;
- elicitación;
- adaptación;
- traducción por hablantes.

## 7.2 Registro

El español debe reflejar habla humana situada en Oaxaca y el Istmo.

Debe evitar:

- español neutro artificial;
- tono de manual;
- diálogo didáctico explícito;
- explicaciones excesivas;
- dramatización literaria ajena al nivel;
- estructuras que no puedan sostenerse al traducir.

## 7.3 Longitud

Cada conversación debe tener al menos 20 líneas cuando la tarea lo requiera.

La longitud se logra mediante turnos naturales, no alargando cada intervención.

La calidad y completitud tienen prioridad sobre una cuota fija de conversaciones por mensaje.

## 7.4 Productividad de patrón

El generador debe reutilizar un patrón ya sembrado en dos o tres contextos cuando sea posible.

Se permite coordinación simple con elementos conocidos.

No debe introducir patrones sintácticos nuevos fuera de lo autorizado por la tarea.

## 7.5 Marcadores conversacionales

Un conjunto básico de marcadores puede aparecer desde los niveles iniciales porque funciona como pegamento pragmático.

Ejemplos:

- ajá;
- a ver;
- pues;
- oye;
- ¿verdad?

Su presencia debe ser natural y no convertirse en muletilla automática.

## 7.6 Regla anti-ping-pong

No deben aparecer más de tres turnos consecutivos de pregunta–respuesta limpia.

La secuencia debe romperse mediante:

- eco;
- reacción;
- duda;
- autocorrección;
- comentario;
- respuesta incompleta;
- iniciativa del otro interlocutor;
- cambio menor en la situación.

## 7.7 Aperturas y cierres

Las conversaciones que abren con saludo o cierran con despedida o agradecimiento verbalizado no deben superar aproximadamente un tercio del total, salvo situaciones donde estas fórmulas sean socialmente centrales.

El inventario de pasos pragmáticos no funciona como checklist.

## 7.8 Jerarquía de prioridades

La versión vigente del generador aplica esta prioridad:

1. naturalidad;
2. gramática;
3. pragmática;
4. instrucciones de la tarea;
5. balance residual.

Esta jerarquía evita sacrificar naturalidad para cumplir métricas secundarias.

## 7.9 Límites

El generador no mantiene de forma confiable entre mensajes:

- historial;
- balance acumulado;
- déficit de situaciones;
- déficit de patrones;
- balance de personajes;
- cobertura léxica.

Estas funciones corresponden a un controlador externo.

---

# 8. Validación del corpus

## 8.1 Validación lingüística

Debe revisar:

- significado;
- naturalidad;
- pronunciación;
- segmentación;
- orden;
- equivalencia;
- escritura;
- variante;
- contexto de uso.

## 8.2 Validación comunitaria

Debe revisar:

- pertinencia;
- realidad de la escena;
- relación social;
- posibles implicaciones;
- fórmulas de cortesía;
- uso local;
- representatividad.

La validación de una persona no se presenta como consenso de toda la comunidad.

## 8.3 Validación pedagógica

Debe revisar:

- función;
- novedad;
- progresión;
- producibilidad;
- reutilización;
- relación con COR001;
- carga acumulada;
- transferencia.

## 8.4 Validación dramatúrgica

Debe revisar:

- coherencia;
- ritmo;
- economía;
- continuidad;
- naturalidad;
- ausencia de relleno;
- variación de turnos;
- plausibilidad.

## 8.5 Validación técnica

Debe verificar:

- correspondencia entre entrada y audio;
- integridad de identificadores;
- versiones;
- metadatos;
- disponibilidad de archivos;
- relación con derivados.

---

# 9. Evolución del corpus

## 9.1 Primera etapa: frases básicas

La primera etapa organizó 107 frases en bloques temáticos.

Este enfoque permitió crear una base inicial clara y manejable.

## 9.2 Crisis de COR002

La ampliación mediante los mismos bloques mostró límites:

- repetición;
- falta de progresión;
- frases poco productivas;
- acumulación temática;
- baja continuidad;
- artificialidad.

El problema no se resolvía reemplazando algunas frases.

Requería cambiar la arquitectura.

## 9.3 Paso a situaciones

Las situaciones comunicativas se adoptaron como origen del material.

Esto permitió pensar en:

- actores;
- objetivos;
- contexto;
- secuencias;
- funciones;
- pragmática;
- cultura.

## 9.4 Paso a funciones

Las funciones comunicativas se adoptaron como unidad principal para medir avance.

Esto permitió distinguir entre:

- frases nuevas;
- funciones nuevas;
- patrones nuevos;
- variantes;
- repeticiones vacías.

## 9.5 Paso a corpus dramatúrgico

Se desarrolló un generador de conversaciones en español para producir escenas más naturales.

El proceso mostró que:

- JSON y metadatos excesivos hacían inviable la generación;
- la prohibición rígida de complejidad producía diálogos robóticos;
- los marcadores conversacionales eran necesarios desde etapas tempranas;
- el ritmo requería una regla concreta contra la alternancia mecánica;
- el historial no podía depender del modelo.

## 9.6 Paso a arquitectura de tres capas

El generador se separó en:

- motor;
- datos;
- tarea.

Esto permite modificar situaciones y léxico sin reescribir las reglas estables.

## 9.7 Estado vigente

La arquitectura actual combina:

- COR001 como base;
- reconstrucción pendiente de COR002;
- escenas;
- funciones;
- patrones;
- léxico rotativo;
- niveles gramaticales y pragmáticos;
- borradores dramatúrgicos en español;
- validación y traducción por hablantes;
- control externo futuro de cobertura.

---

# 10. Estado actual

## 10.1 Existe

- COR001 con 107 frases validadas;
- audios relacionados con COR001;
- un borrador anterior de COR002 descartado como bloque definitivo;
- inventarios de situaciones;
- niveles gramaticales G1–G5;
- niveles pragmáticos P1–P5;
- bancos de léxico;
- `corpus_v2.txt`;
- `lexico_v2.txt`;
- `prompt_generador_corpus_v7.md`;
- reglas de naturalidad y dramatización;
- criterio de balance de género;
- regla de límite de saludos y despedidas;
- arquitectura de tres capas.

## 10.2 Está terminado

- decisión de no generar Didxazá automáticamente;
- decisión de no usar listas temáticas como arquitectura principal;
- definición de escena, función y patrón;
- separación entre motor, datos y tarea;
- abandono de v5 y v6;
- adopción de v7 como versión vigente;
- identificación de COR002 anterior como borrador reemplazable.

## 10.3 Permanece incompleto

- COR002 definitivo;
- matriz completa de funciones;
- mapa consolidado de patrones;
- controlador externo;
- medición acumulada de cobertura;
- pruebas a escala de v7;
- validación comunitaria de las escenas;
- validación lingüística de nuevas conversaciones;
- formalización completa de metadatos;
- secuenciación final entre niveles.

---

# 11. Pendientes

## Alta prioridad

### Reconstruir COR002

Debe construirse desde:

- escenas;
- funciones;
- cobertura de COR001;
- patrones;
- validación comunitaria;
- progresión.

No debe reutilizar automáticamente el bloque anterior.

### Probar `prompt_generador_corpus_v7.md`

Debe ejecutarse un lote real para verificar:

- naturalidad;
- economía;
- regla anti-ping-pong;
- techo de saludos y despedidas;
- balance de género;
- productividad de patrones;
- cumplimiento de la tarea.

### Construir la matriz de cobertura

Debe relacionar:

- escena;
- función;
- patrón;
- nivel G;
- nivel P;
- léxico;
- cobertura previa;
- novedad;
- validación.

## Prioridad media

### Diseñar el controlador externo

Debe gestionar:

- historial;
- selección;
- balance;
- déficits;
- personajes;
- léxico;
- patrones;
- generación del bloque TAREA.

### Formalizar el esquema de metadatos

Debe definir campos obligatorios, estados y reglas de versionado.

### Validar las situaciones con hablantes

Debe revisar realidad cultural, frecuencia y naturalidad.

## Baja prioridad

### Evaluar un sistema externo de frecuencia léxica

Debe determinarse si conviene reintroducir medición cuantitativa fuera del prompt.

### Revisar materiales recuperables del COR002 anterior

Solo después de contar con la nueva arquitectura y la matriz de cobertura.

---

# 12. Límites del documento

Este documento describe cómo está diseñado y organizado el corpus.

No define:

- la metodología general del proyecto;
- la fundamentación pedagógica;
- el marco teórico;
- los parámetros técnicos de audio;
- la bibliografía;
- la arquitectura del repositorio;
- los procedimientos administrativos;
- los acuerdos de colaboración.
