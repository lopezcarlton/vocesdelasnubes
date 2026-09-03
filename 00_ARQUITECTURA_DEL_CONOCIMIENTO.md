# Arquitectura del Sistema de Conocimiento

## Voces de las Nubes

```yaml
---
titulo: Arquitectura del Sistema de Conocimiento
proyecto: Voces de las Nubes
autor: Emiliano López Carlton
version: 0.3
estado: vigente
unidad_minima: hallazgo
fecha: 03/09/2026
---
```

---

## 1. Propósito

Este documento define cómo se registra, relaciona, valida, actualiza y reutiliza el conocimiento producido dentro de **Voces de las Nubes**.

Su propósito no es describir el proyecto ni presentar sus resultados. Su función es establecer las reglas mediante las cuales la información dispersa en chats, sesiones de trabajo, lecturas, documentos, grabaciones, revisiones del corpus y conversaciones con colaboradores se convierte en conocimiento permanente del proyecto.

La arquitectura debe permitir:

* conservar la trazabilidad de cada afirmación;
* distinguir hechos, interpretaciones, supuestos y decisiones;
* reconocer la autoridad intelectual de los hablantes y colaboradores;
* registrar cambios de criterio sin borrar la historia del proyecto;
* evitar que decisiones reemplazadas vuelvan a presentarse como vigentes;
* detectar contradicciones, vacíos y validaciones pendientes;
* generar documentos temáticos sin duplicar manualmente la información;
* mantener una fuente de verdad utilizable por personas y sistemas de inteligencia artificial.

El repositorio no debe funcionar como una colección de textos independientes. Debe operar como un **sistema de conocimiento interrelacionado**.

---

# 2. Principio estructural

## 2.1 El hallazgo como unidad mínima

La unidad mínima del sistema es el **hallazgo**.

Un hallazgo es una afirmación concreta, relevante para el proyecto, obtenida a partir de una fuente identificable y formulada de manera suficientemente precisa para ser confirmada, cuestionada, relacionada o reemplazada.

Ejemplos:

* Durante la grabación, Vicente prefirió repetir la frase completa en lugar de segmentarla.
* La escritura proporcionada por un hablante no siempre representa con seguridad la forma producida oralmente.
* Las conversaciones organizadas por situaciones comunicativas permiten integrar vocabulario de distintos campos semánticos.
* En una sesión de prueba, las pausas previstas resultaron insuficientes para repetir la frase en didxazá.
* El enfoque basado en listas temáticas produjo materiales con poca continuidad dramática.

Un hallazgo no es necesariamente una verdad definitiva. Puede contener:

* una observación de campo;
* una afirmación de un colaborador;
* un resultado de revisión;
* una conclusión derivada de varias evidencias;
* una relación detectada entre componentes;
* una contradicción;
* una limitación;
* un descubrimiento metodológico;
* un cambio relevante en la comprensión del proyecto.

## 2.2 Lo que no constituye un hallazgo

No debe registrarse como hallazgo:

* una idea improvisada sin relevancia posterior;
* una propuesta que todavía no ha sido examinada;
* una frase genérica sin fuente;
* una repetición de información ya registrada;
* una interpretación presentada como si fuera observación;
* una afirmación generada por una IA sin respaldo documental;
* una descripción extensa que contenga varios hechos independientes;
* una decisión, principio o supuesto sin identificar los hallazgos que le dieron origen.

Las propuestas todavía no examinadas se registran como **supuestos**, **opciones** o **preguntas abiertas**, según corresponda.

## 2.3 Atomicidad

Cada hallazgo debe expresar una sola idea principal.

Incorrecto:

> Vicente prefirió grabar dos tomas, consideró que la escritura era poco confiable y recomendó incorporar una voz femenina.

Correcto:

* Vicente prefirió registrar dos tomas de cada frase.
* Vicente manifestó inseguridad al escribir algunas formas que produjo oralmente.
* Vicente recomendó incorporar una voz femenina.

La atomicidad permite que cada afirmación tenga relaciones, estados y validaciones diferentes.

---

# 3. Capas del sistema

El sistema se organiza en cuatro capas.

## 3.1 Fuentes

Son los materiales de los cuales se obtiene información:

* chats;
* contextos Markdown;
* grabaciones;
* transcripciones;
* notas de campo;
* corpus;
* entrevistas;
* sesiones de validación;
* bibliografía;
* documentos institucionales;
* correos;
* versiones de prompts;
* pruebas pedagógicas;
* observaciones de uso.

Las fuentes se conservan como evidencia primaria o secundaria. No deben confundirse con el conocimiento extraído de ellas.

## 3.2 Hallazgos

Son las afirmaciones atómicas extraídas de las fuentes.

Cada hallazgo conserva:

* su formulación;
* su fuente;
* el contexto en que apareció;
* su tipo;
* su nivel de respaldo;
* su estado;
* sus relaciones.

Los hallazgos constituyen la base documental del sistema.

## 3.3 Entidades derivadas

Son elementos construidos a partir de uno o varios hallazgos:

* decisiones;
* supuestos;
* principios;
* validaciones;
* riesgos;
* preguntas abiertas;
* lecciones aprendidas;
* procedimientos;
* aplicaciones teóricas;
* criterios;
* requisitos;
* cambios de posición.

Una entidad derivada nunca debe existir sin indicar qué hallazgos la sustentan, salvo que se identifique expresamente como provisional.

## 3.4 Vistas documentales

Son documentos elaborados a partir del conocimiento registrado:

* teoría;
* metodología;
* pedagogía;
* corpus;
* audio;
* documentación lingüística;
* ética y gobernanza;
* ELDP;
* manual operativo;
* informes institucionales;
* cronologías;
* estado actual del proyecto.

Estas vistas no constituyen la fuente primaria de verdad. Son representaciones organizadas del conocimiento vigente.

## 3.5 Sistemas derivados y frontera de autoridad

Las herramientas, implementaciones, repositorios técnicos y otros sistemas derivados **no constituyen una quinta capa del Sistema de Conocimiento** ni adquieren autoridad por consumirlo o procesarlo.

Pueden:

* leer conocimiento aprobado;
* ejecutar análisis y pruebas;
* detectar contradicciones o vacíos;
* formular requisitos;
* proponer candidatos de hallazgo, supuesto, interpretación o decisión.

No pueden por sí mismos:

* adoptar conocimiento;
* promover un candidato a entidad vigente;
* modificar una decisión, principio o vista canónica;
* convertir una salida técnica en evidencia lingüística, pedagógica o comunitaria.

Cuando una lectura o descubrimiento ocurra durante trabajo en un sistema derivado, debe volver a la fuente original y seguir el procedimiento de actualización de Voces de las Nubes antes de incorporarse. Un informe técnico puede documentar el comportamiento de la herramienta que lo produjo, pero no sustituye la autoridad pertinente sobre otros dominios.

La relación es bidireccional en información y unidireccional en autoridad:

```text
VOCES -> conocimiento aprobado -> sistemas derivados
sistemas derivados -> candidatos / contradicciones / requisitos -> VOCES
VOCES -> adjudicación -> conocimiento aprobado
```

Los futuros desarrolladores de sistemas derivados no tendrán por defecto capacidad de escritura sobre el Sistema de Conocimiento. Los controles de acceso y, cuando sea viable, la separación física de repositorios deben reflejar esta regla.

Referencia: `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO`.

---

# 4. Entidades del sistema

## 4.1 Fuente

**Código:** `SRC`

Una fuente es el objeto original del que procede la información.

Ejemplos:

* un Markdown de contexto;
* una grabación con Vicente;
* una conversación con Vidal;
* un libro;
* un artículo;
* una versión del corpus;
* un informe;
* una sesión de revisión.

Campos mínimos:

```yaml
id:
tipo:
titulo:
autor_o_participantes:
fecha:
ubicacion:
descripcion:
nivel_de_fuente:
estado_de_acceso:
```

### Nivel de fuente

* `primaria`: registro directo del hecho o intervención;
* `secundaria`: interpretación o síntesis de una fuente primaria;
* `terciaria`: compilación construida a partir de otras síntesis.

Los Markdown de contexto generados desde chats son generalmente **fuentes secundarias**, no fuentes primarias. Cuando sea posible, deben conservar referencia al chat, documento o sesión original.

---

## 4.2 Hallazgo

**Código:** `HALL`

Es la unidad mínima del conocimiento.

Campos mínimos:

```yaml
id:
titulo:
afirmacion:
tipo:
estado:
fecha_del_hecho:
fecha_de_registro:
fuentes:
participantes:
grado_de_respaldo:
alcance:
etiquetas:
relaciones:
```

### Tipos de hallazgo

* `observacion`: algo percibido o registrado directamente;
* `declaracion`: afirmación atribuible a una persona;
* `resultado`: producto de una prueba, revisión o medición;
* `patron`: recurrencia detectada en varios casos;
* `contradiccion`: incompatibilidad entre fuentes o posiciones;
* `limitacion`: condición que restringe el trabajo;
* `necesidad`: carencia identificada;
* `oportunidad`: posibilidad de mejora;
* `cambio`: modificación significativa;
* `interpretacion`: explicación construida a partir de evidencias;
* `hallazgo_bibliografico`: idea relevante obtenida de una fuente académica;
* `hallazgo_institucional`: condición o criterio derivado de CaCiO, IEEPO, PTEO, ELDP u otra institución.

### Estados del hallazgo

* `registrado`: extraído y documentado;
* `corroborado`: respaldado por fuentes independientes o repetidas;
* `cuestionado`: existe evidencia que lo pone en duda;
* `contradicho`: entra en conflicto directo con otro hallazgo;
* `reemplazado`: una formulación posterior explica mejor el fenómeno;
* `descartado`: se determinó que era incorrecto o irrelevante;
* `pendiente_de_revision`: requiere volver a la fuente;
* `pendiente_de_validacion`: requiere revisión por una autoridad pertinente.

### Grado de respaldo

El grado de respaldo no sustituye al estado.

* `directo`: aparece explícitamente en una fuente primaria;
* `múltiple`: aparece en varias fuentes independientes;
* `parcial`: existe evidencia, pero no es suficiente;
* `inferido`: se deriva razonablemente de las fuentes;
* `débil`: depende de una fuente ambigua o incompleta;
* `sin_respaldo`: propuesta todavía no apoyada por evidencia.

Una afirmación inferida debe estar marcada como tal. No puede redactarse como observación directa.

---

## 4.3 Decisión

**Código:** `DEC`

Una decisión registra una elección vigente o histórica que orienta el proyecto.

Una decisión no es equivalente a un hallazgo. Normalmente surge como respuesta a uno o varios hallazgos, necesidades, principios o restricciones.

**Decisiones directas de coordinación o alcance.** Cuando la persona responsable adopta explícitamente una decisión de coordinación, alcance o prioridad, no debe fabricarse un `HALL` espejo únicamente para satisfacer el esquema. En esos casos `hallazgos_que_la_sustentan` puede ser una lista vacía y la decisión debe identificar la fuente directa mediante `fuentes_directas` y explicar su justificación. Esta excepción no permite usar una DEC para presentar como hecho empírico algo que no ha sido observado o validado.

Campos mínimos:

```yaml
id:
titulo:
decision:
estado:
fecha:
responsable:
validadores:
hallazgos_que_la_sustentan:
principios_relacionados:
supuestos_implicados:
alternativas_consideradas:
justificacion:
impacta_a:
reemplaza:
reemplazada_por:
condiciones_de_revision:
```

### Estados de decisión

* `propuesta`;
* `en_validacion`;
* `vigente`;
* `vigente_con_reservas`;
* `suspendida`;
* `reemplazada`;
* `revocada`;
* `descartada`.

### Regla de vigencia

Solo las decisiones marcadas como `vigente` o `vigente_con_reservas` deben presentarse como instrucciones actuales del proyecto.

Las decisiones reemplazadas se conservan para explicar la evolución, pero no deben reincorporarse automáticamente en documentos nuevos.

---

## 4.4 Supuesto

**Código:** `SUP`

Un supuesto es una afirmación utilizada para orientar el trabajo cuya validez todavía no ha sido suficientemente demostrada.

Campos mínimos:

```yaml
id:
supuesto:
estado:
grado_de_confianza:
origen:
hallazgos_relacionados:
decisiones_que_dependen_de_el:
como_puede_comprobarse:
como_puede_refutarse:
responsable_de_revision:
fecha_de_revision:
```

### Estados de supuesto

* `propuesto`;
* `en_observacion`;
* `parcialmente_respaldado`;
* `confirmado`;
* `cuestionado`;
* `refutado`;
* `reemplazado`.

Un supuesto confirmado no necesariamente se convierte en principio. Puede convertirse en hallazgo corroborado, criterio, decisión o conclusión, según su naturaleza.

---

## 4.5 Principio

**Código:** `PRIN`

Un principio es una regla general que orienta decisiones recurrentes y expresa compromisos centrales del proyecto.

Ejemplos:

* El audio tiene prioridad epistemológica cuando la escritura no ha sido validada.
* La participación de los colaboradores será siempre voluntaria.
* Los hablantes participan como autoridades intelectuales, no solo como proveedores de datos.
* No se presentará como consenso comunitario una opinión individual.

Campos mínimos:

```yaml
id:
principio:
estado:
alcance:
origen:
hallazgos_que_lo_sustentan:
autoridad_que_lo_valida:
decisiones_derivadas:
excepciones:
condiciones_de_revision:
```

### Estados de principio

* `propuesto`;
* `vigente`;
* `en_revision`;
* `reformulado`;
* `retirado`.

Los principios deben ser pocos y relativamente estables. No debe elevarse una decisión operativa temporal al rango de principio.

---

## 4.6 Validación

**Código:** `VAL`

Una validación registra el acto mediante el cual una persona o instancia con autoridad pertinente revisa una afirmación, decisión, forma lingüística, procedimiento o interpretación.

Campos mínimos:

```yaml
id:
objeto_validado:
validador:
tipo_de_autoridad:
fecha:
resultado:
alcance:
observaciones:
fuente:
afecta_a:
```

### Resultados posibles

* `confirma`;
* `confirma_con_ajustes`;
* `cuestiona`;
* `rechaza`;
* `propone_alternativa`;
* `no_concluyente`.

### Tipos de autoridad

* `linguistica`;
* `comunitaria`;
* `pedagogica`;
* `institucional`;
* `tecnica`;
* `academica`;
* `operativa`.

### Regla de autoridad pertinente

No toda validación sirve para cualquier tema.

Por ejemplo:

* un hablante puede validar naturalidad, significado, uso o adecuación cultural;
* un especialista en audio puede validar niveles y procedimientos técnicos;
* CaCiO puede validar coherencia institucional;
* una fuente bibliográfica puede fundamentar una interpretación teórica;
* Emiliano puede tomar decisiones de coordinación, pero no convertirlas por sí mismo en consenso comunitario.

Debe registrarse exactamente **qué se validó y dentro de qué alcance**.

---

## 4.7 Aplicación teórica

**Código:** `TEO`

Una aplicación teórica no es un resumen de autor. Registra cómo una propuesta bibliográfica se interpreta y utiliza dentro del proyecto.

Campos mínimos:

```yaml
id:
autor_o_marco:
propuesta_relevante:
fuente_bibliografica:
interpretacion_en_el_proyecto:
hallazgos_relacionados:
decisiones_que_fundamenta:
limitaciones:
tensiones:
estado:
```

### Estados

* `identificada`;
* `en_evaluacion`;
* `aplicada`;
* `aplicada_con_ajustes`;
* `cuestionada`;
* `descartada`.

La literatura puede fundamentar una decisión, pero no reemplaza la observación de campo ni la validación comunitaria.

---

## 4.8 Procedimiento o metodología operativa

**Código:** `PROC`

Un procedimiento describe una secuencia reproducible para realizar una tarea.

Ejemplos:

* validar una conversación;
* preparar una sesión;
* grabar una serie;
* editar audio;
* revisar naturalidad;
* actualizar el corpus;
* registrar cambios.

Campos mínimos:

```yaml
id:
titulo:
objetivo:
estado:
entradas:
responsables:
pasos:
criterios_de_control:
salidas:
decisiones_que_implementa:
hallazgos_que_lo_originaron:
riesgos:
version:
```

### Estados

* `borrador`;
* `en_prueba`;
* `vigente`;
* `vigente_con_excepciones`;
* `en_revision`;
* `reemplazado`;
* `retirado`.

---

## 4.9 Criterio

**Código:** `CRIT`

Un criterio permite evaluar, seleccionar, aprobar o rechazar algo de manera consistente.

Ejemplos:

* criterio de naturalidad;
* criterio de dificultad;
* criterio de selección léxica;
* criterio de calidad de audio;
* criterio de inclusión de escenas;
* criterio de validación.

Campos mínimos:

```yaml
id:
criterio:
aplica_a:
estado:
fundamento:
forma_de_evaluacion:
umbral_o_condicion:
excepciones:
```

Los criterios evitan que cada revisión dependa solamente de impresiones circunstanciales.

---

## 4.10 Riesgo

**Código:** `RISK`

Un riesgo es una condición incierta que puede afectar negativamente el proyecto.

Campos mínimos:

```yaml
id:
riesgo:
categoria:
probabilidad:
impacto:
indicadores:
componentes_afectados:
hallazgos_relacionados:
medidas_de_mitigacion:
responsable:
estado:
```

### Categorías posibles

* lingüístico;
* comunitario;
* ético;
* pedagógico;
* metodológico;
* técnico;
* institucional;
* financiero;
* documental;
* operativo;
* continuidad;
* gobernanza.

---

## 4.11 Pregunta abierta

**Código:** `OPEN`

Una pregunta abierta registra algo que todavía no está resuelto y que puede afectar decisiones posteriores.

Campos mínimos:

```yaml
id:
pregunta:
origen:
por_que_importa:
estado:
requiere:
responsable:
fecha_objetivo:
afecta_a:
respuesta:
```

### Estados

* `abierta`;
* `en_investigacion`;
* `pendiente_de_validacion`;
* `respondida`;
* `cerrada_sin_respuesta`;
* `reemplazada`.

La respuesta debe relacionarse con los hallazgos que permitieron resolverla.

---

## 4.12 Lección aprendida

**Código:** `LESS`

Una lección aprendida es una conclusión generalizable obtenida de la experiencia del proyecto.

Campos mínimos:

```yaml
id:
leccion:
situacion_de_origen:
hallazgos_relacionados:
alcance:
aplicacion_futura:
estado:
```

Una lección no debe formularse prematuramente a partir de un único incidente, salvo que se marque como provisional.

---

## 4.13 Cambio de posición

**Código:** `CAMB`

Registra una modificación sustantiva en la comprensión, los criterios o las decisiones del proyecto.

Campos mínimos:

```yaml
id:
tema:
posicion_anterior:
posicion_actual:
disparador_del_cambio:
hallazgos_relacionados:
decision_anterior:
decision_actual:
consecuencias:
fecha:
```

El cambio de posición no elimina la postura anterior. Explica por qué dejó de utilizarse.

---

## 4.14 Entregable o implementación

**Código:** `OUT`

Registra un producto concreto del proyecto.

Ejemplos:

* COR001;
* COR002;
* archivo de audio;
* prompt generador;
* informe;
* baraja de Anki;
* protocolo;
* solicitud ELDP;
* documento teórico.

Campos mínimos:

```yaml
id:
titulo:
tipo:
version:
estado:
ubicacion:
decisiones_que_implementa:
procedimientos_utilizados:
hallazgos_generados:
dependencias:
fecha:
responsable:
```

Los entregables no son únicamente el final del flujo. Su producción y evaluación pueden generar nuevos hallazgos.

---

# 5. Relaciones permitidas

Las relaciones deben escribirse mediante identificadores estables.

## 5.1 Relaciones principales

```text
SRC  → origina → HALL

HALL → sustenta → DEC
HALL → cuestiona → DEC
HALL → contradice → HALL
HALL → confirma → SUP
HALL → refuta → SUP
HALL → revela → RISK
HALL → abre → OPEN

SUP  → condiciona → DEC
SUP  → requiere → VAL

PRIN → orienta → DEC
PRIN → restringe → PROC

TEO  → fundamenta → DEC
TEO  → entra_en_tension_con → TEO
TEO  → entra_en_tension_con → HALL

VAL  → confirma → HALL
VAL  → modifica → DEC
VAL  → rechaza → OUT

DEC  → genera → PROC
DEC  → modifica → OUT
DEC  → reemplaza → DEC

PROC → implementa → DEC
PROC → produce → OUT
PROC → genera → HALL

OUT  → materializa → DEC
OUT  → genera → HALL

HALL → produce → LESS
HALL → provoca → CAMB
CAMB → reemplaza → DEC
```

## 5.2 Regla contra relaciones inventadas

Una relación solo debe registrarse cuando:

* aparezca explícitamente en las fuentes;
* sea una consecuencia lógica directa;
* haya sido reconocida durante el análisis;
* se marque como inferida cuando no sea explícita.

No deben construirse conexiones solo porque parezcan conceptualmente elegantes.

---

# 6. Flujo del conocimiento

## 6.1 Flujo básico

```text
FUENTE
  ↓
EXTRACCIÓN
  ↓
HALLAZGO
  ↓
CLASIFICACIÓN Y TRAZABILIDAD
  ↓
RELACIÓN CON CONOCIMIENTO EXISTENTE
  ↓
SUPUESTO / VALIDACIÓN / DECISIÓN / RIESGO / PREGUNTA
  ↓
PROCEDIMIENTO
  ↓
IMPLEMENTACIÓN
  ↓
NUEVA OBSERVACIÓN
  ↓
NUEVO HALLAZGO
```

El sistema es cíclico. Los productos del proyecto generan nuevas evidencias que pueden confirmar, modificar o revocar decisiones anteriores.

## 6.2 Flujo de una decisión

Una decisión debe poder reconstruirse así:

```text
¿Qué ocurrió?
HALL-___

¿Qué interpretación produjo?
HALL-___ o SUP-___

¿Qué principio o marco intervino?
PRIN-___ / TEO-___

¿Quién validó lo pertinente?
VAL-___

¿Qué se decidió?
DEC-___

¿Cómo se implementó?
PROC-___

¿En qué producto aparece?
OUT-___

¿Qué resultado produjo?
HALL-___
```

No todos los pasos serán obligatorios en cada caso, pero cualquier ausencia relevante debe quedar visible.

---

# 7. Jerarquía de evidencia

El sistema debe distinguir entre tipos de respaldo.

## Nivel 1 — Registro directo

* audio original;
* video;
* transcripción revisada;
* documento institucional oficial;
* corpus identificado;
* intervención registrada de un colaborador;
* notas de campo tomadas durante la actividad.

## Nivel 2 — Síntesis verificable

* Markdown de contexto;
* informe construido desde registros;
* minuta;
* resumen de una sesión;
* tabla derivada de datos identificables.

## Nivel 3 — Interpretación

* análisis de Emiliano;
* análisis de un colaborador;
* relación inferida entre hallazgos;
* aplicación conceptual;
* conclusión provisional.

## Nivel 4 — Propuesta

* sugerencia de IA;
* posibilidad todavía no discutida;
* diseño hipotético;
* alternativa futura.

### Regla de transformación

Una propuesta no se convierte en hallazgo confirmado solo porque haya sido redactada con seguridad.

Para cambiar de nivel necesita:

* evidencia;
* revisión;
* validación pertinente;
* implementación observable;
* o una decisión explícita que reconozca su carácter provisional.

---

# 8. Autoridad y validación comunitaria

La arquitectura debe reconocer que la autoridad dentro del proyecto es distribuida.

No existe una sola persona capaz de validar todos los componentes.

## 8.1 Autoridades lingüísticas y comunitarias

Los hablantes y colaboradores pueden aportar:

* juicios de naturalidad;
* significados;
* formas de uso;
* diferencias regionales;
* pertinencia cultural;
* interpretaciones comunitarias;
* conocimiento sobre contextos comunicativos;
* decisiones sobre representación de su propia voz.

Sus intervenciones deben registrarse como contribuciones intelectuales específicas.

## 8.2 Coordinación

Emiliano puede:

* integrar hallazgos;
* definir prioridades;
* decidir procedimientos;
* aceptar o rechazar alternativas operativas;
* formular interpretaciones;
* coordinar validaciones;
* documentar cambios;
* establecer decisiones dentro de su responsabilidad.

La coordinación no debe presentarse como validación lingüística o comunitaria cuando no lo sea.

## 8.3 Autoridad institucional

CaCiO, IEEPO, PTEO, ELDP u otras instancias pueden validar:

* coherencia institucional;
* requisitos;
* compromisos;
* entregables;
* condiciones éticas;
* viabilidad administrativa;
* compatibilidad con programas específicos.

La validación institucional no sustituye la validación comunitaria ni lingüística.

## 8.4 Desacuerdo entre autoridades

Cuando dos colaboradores difieran:

* se registran ambas posiciones;
* no se fuerza un consenso;
* se especifica si puede tratarse de variación;
* se limita el alcance de cada afirmación;
* se abre una pregunta cuando sea necesario;
* se evita declarar una forma como universal sin evidencia suficiente.

---

# 9. Identificadores persistentes

Cada entidad debe recibir un identificador único y permanente.

Formato:

```text
TIPO-0001
```

Ejemplos:

```text
SRC-0001
HALL-0001
DEC-0001
SUP-0001
PRIN-0001
VAL-0001
TEO-0001
PROC-0001
CRIT-0001
RISK-0001
OPEN-0001
LESS-0001
CAMB-0001
OUT-0001
```

## Reglas

1. Un identificador nunca se reutiliza.
2. Una entidad reemplazada conserva su identificador.
3. Una reformulación sustantiva crea una entidad nueva.
4. Una corrección menor puede conservar el mismo identificador y aumentar la versión.
5. Los nombres de archivo pueden cambiar; los identificadores no.
6. Las relaciones deben usar IDs, no depender únicamente de enlaces o títulos.

---

# 10. Estado, confianza y vigencia

Estos tres elementos no deben confundirse.

## Estado

Indica en qué etapa se encuentra una entidad:

* propuesta;
* registrada;
* en revisión;
* validada;
* vigente;
* cuestionada;
* reemplazada;
* descartada.

## Confianza

Indica qué tan fuerte es el respaldo disponible:

* alta;
* media;
* baja;
* no determinada.

## Vigencia

Indica si debe utilizarse actualmente:

* vigente;
* vigente con reservas;
* no vigente;
* histórica;
* pendiente.

Una decisión puede tener confianza media y estar vigente provisionalmente. Un hallazgo puede tener confianza alta, pero ya no ser operativo porque cambió el contexto.

---

# 11. Contradicciones

Las contradicciones no deben eliminarse durante la síntesis.

Cuando dos afirmaciones entren en conflicto se debe:

1. conservar ambos hallazgos;
2. crear una relación `contradice`;
3. identificar las fuentes;
4. distinguir diferencia real, variación o cambio temporal;
5. registrar el alcance de cada afirmación;
6. abrir una pregunta si no existe resolución;
7. documentar una decisión si se adopta una solución operativa.

Formato mínimo:

```yaml
contradiccion:
  entre:
    - HALL-____
    - HALL-____
  tipo:
  posible_explicacion:
  estado:
  requiere_validacion_de:
  decision_operativa_temporal:
```

Tipos posibles:

* contradicción factual;
* diferencia de interpretación;
* variación lingüística;
* diferencia generacional;
* diferencia regional;
* cambio temporal;
* conflicto entre teoría y campo;
* conflicto entre objetivo y viabilidad;
* inconsistencia documental.

---

# 12. Vacíos de conocimiento

El sistema debe detectar activamente:

* decisiones sin hallazgos que las sustenten;
* supuestos tratados como hechos;
* afirmaciones atribuidas sin fuente;
* validaciones sin alcance definido;
* procedimientos sin decisión de origen;
* teoría citada pero no aplicada;
* aplicaciones sin fundamento bibliográfico;
* hallazgos que contradicen decisiones vigentes;
* riesgos sin mitigación;
* preguntas abiertas que bloquean trabajo;
* entregables que no implementan decisiones identificables;
* decisiones vigentes que no aparecen en los productos;
* conocimiento importante presente solo en un chat;
* referencias a documentos no localizados;
* validaciones comunitarias todavía pendientes.

Los vacíos se registran como preguntas abiertas, riesgos o tareas de revisión, según corresponda.

---

# 13. Documentos temáticos como vistas

Los archivos temáticos se generan a partir de las entidades del sistema.

## 13.1 Teoría

Incluye:

* aplicaciones teóricas;
* hallazgos bibliográficos;
* decisiones fundamentadas por teoría;
* tensiones entre autores y realidad de campo;
* cambios de interpretación;
* vacíos de fundamentación.

## 13.2 Metodología

Incluye:

* decisiones metodológicas vigentes;
* procedimientos;
* criterios;
* riesgos operativos;
* hallazgos de campo que modificaron el método;
* validaciones pertinentes.

## 13.3 Pedagogía

Incluye:

* supuestos de aprendizaje;
* decisiones pedagógicas;
* aplicaciones teóricas;
* criterios de progresión;
* resultados de pruebas;
* preguntas abiertas;
* tensiones entre adquisición, enseñanza e identidad.

## 13.4 Corpus

Incluye:

* decisiones de diseño;
* criterios de inclusión;
* estructura vigente;
* versiones;
* cambios;
* hallazgos producidos durante la revisión;
* relaciones con pedagogía, audio y validación lingüística.

## 13.5 Audio

Incluye:

* decisiones técnicas;
* procedimientos de grabación y edición;
* criterios de calidad;
* hallazgos de sesiones;
* riesgos;
* versiones y entregables.

## 13.6 Ética y gobernanza

Incluye:

* principios;
* decisiones sobre participación;
* consentimiento;
* atribución;
* autoridad;
* propiedad y acceso;
* distribución de recursos;
* responsabilidades;
* validaciones comunitarias e institucionales.

## 13.7 ELDP

Incluye únicamente el conocimiento relevante para:

* alcance de documentación;
* metodología;
* equipo;
* gobernanza;
* ética;
* productos;
* acceso;
* preservación;
* riesgos;
* sostenibilidad;
* transición futura.

ELDP debe ser una vista del proyecto, no la estructura dominante de todo el repositorio.

---

# 14. Organización física vigente del repositorio

Esta sección **describe la organización real vigente**; no prescribe un árbol ideal independiente del repositorio. Si la organización física cambia por una decisión adoptada, esta sección debe actualizarse. No se debe reestructurar el repositorio sólo para obedecer un diagrama histórico.

```text
/
├── README.md
├── INICIAR_AQUI_CHAT_NUEVO.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
├── 01_JERARQUIA_DE_VERDAD.md
├── 02_BACKLOG.md
├── 03_REGLAS_DE_ACTUALIZACIÓN.md
├── 04_RELACION_CON_ELDP.md
├── conocimiento/        # Sistema de Conocimiento canónico + vistas
├── informes/            # análisis y auditorías no normativos
├── archivo/             # checkpoints, contextos y herramientas históricas
├── dispositivo/         # sistema derivado temporal; pendiente de separación física
└── .github/             # control técnico del repositorio
```

Reglas de ubicación:

- `conocimiento/` contiene fuentes registradas, hallazgos, decisiones, principios válidos y vistas canónicas.
- `informes/` puede orientar investigación, pero no adopta conocimiento.
- `archivo/` preserva historia y contexto; no gobierna el presente.
- `dispositivo/` es un sistema derivado y no forma parte del Sistema de Conocimiento. Su presencia actual es transitoria hasta completar la separación física verificada.
- Los materiales fuente compartidos se adjudican por naturaleza y derechos, no por el lugar donde una herramienta los haya ingerido primero.

---


# 15. Regla de fuente única de verdad

Una afirmación no debe mantenerse manualmente en varios lugares como si cada copia fuera independiente.

La fuente de verdad será:

1. el registro de fuente;
2. el hallazgo;
3. la entidad derivada correspondiente.

Los documentos temáticos deben citar o referenciar estas entidades.

Cuando una decisión cambie:

* se actualiza su estado;
* se crea la nueva decisión cuando corresponda;
* se relacionan ambas;
* se identifican los documentos y productos afectados;
* se regeneran o revisan las vistas.

No se debe corregir únicamente el documento narrativo dejando intacta la base de conocimiento.

---

# 16. Reglas para la extracción desde chats

Al procesar un Markdown de contexto:

1. No asumir que todo lo escrito es correcto.
2. Identificar la fuente original cuando esté disponible.
3. Separar afirmaciones atómicas.
4. Distinguir observación, interpretación, propuesta y decisión.
5. No inventar validaciones.
6. No atribuir una afirmación a una persona si la fuente no lo permite.
7. Detectar si la información ya existe.
8. Fusionar duplicados solo cuando sean realmente equivalentes.
9. Conservar diferencias de alcance.
10. Registrar contradicciones.
11. Identificar decisiones reemplazadas.
12. Señalar información incompleta.
13. Separar conocimiento vigente de antecedentes históricos.
14. Marcar como inferidas las conexiones no explícitas.
15. No elevar una sugerencia de IA a decisión del proyecto.

Los contextos de chat son instrumentos de recuperación. No son automáticamente la autoridad final.

---

# 17. Control de duplicados

Dos registros pueden fusionarse cuando:

* expresan la misma afirmación;
* tienen el mismo alcance;
* no difieren en estado;
* no corresponden a momentos históricos distintos.

No deben fusionarse cuando:

* una afirmación es general y otra local;
* provienen de hablantes con posiciones diferentes;
* representan etapas distintas;
* una es observación y otra interpretación;
* una reemplaza a la otra;
* existe una diferencia significativa de formulación.

Cuando se fusionen registros, deben conservarse todas las fuentes relevantes.

---

# 18. Auditoría del sistema

La base de conocimiento debe poder responder periódicamente:

* ¿Qué decisiones están vigentes?
* ¿Qué decisiones dependen de supuestos no confirmados?
* ¿Qué afirmaciones carecen de fuente primaria?
* ¿Qué validaciones siguen pendientes?
* ¿Qué decisiones fueron reemplazadas?
* ¿Qué riesgos no tienen mitigación?
* ¿Qué preguntas abiertas bloquean trabajo?
* ¿Qué procedimientos están desactualizados?
* ¿Qué productos implementan decisiones ya reemplazadas?
* ¿Qué hallazgos nuevos contradicen el método actual?
* ¿Qué componentes dependen excesivamente de una sola persona?
* ¿Qué teoría se cita sin aplicación concreta?
* ¿Qué aplicaciones operativas carecen de fundamentación?
* ¿Qué conocimiento solo existe en los chats y aún no fue incorporado?

---

# 19. Ciclo de actualización

Cada nueva sesión de trabajo debe seguir este ciclo:

```text
1. Registrar o incorporar la fuente.
2. Extraer hallazgos nuevos.
3. Compararlos con el conocimiento existente.
4. Detectar duplicados, contradicciones y cambios.
5. Crear o actualizar entidades derivadas.
6. Identificar productos afectados.
7. Revisar decisiones vigentes.
8. Actualizar las vistas necesarias.
9. Registrar pendientes.
10. Conservar los cambios mediante control de versiones.
```

No todas las sesiones requerirán modificar todas las capas.

---

# 20. Criterio de suficiencia

La arquitectura estará funcionando correctamente cuando sea posible reconstruir, para cualquier decisión importante:

* qué se decidió;
* quién tenía autoridad para decidirlo;
* qué hallazgos la sustentaron;
* qué supuestos intervienen;
* qué teoría la fundamenta;
* quién validó cada aspecto;
* qué alternativas fueron descartadas;
* qué procedimiento la implementa;
* en qué producto aparece;
* qué resultados produjo;
* si continúa vigente;
* qué tendría que ocurrir para revisarla.

Si alguno de estos puntos no puede reconstruirse, existe un vacío documental.

---

# 21. Ejemplo mínimo

```yaml
id: HALL-0001
titulo: Inseguridad de la escritura frente a la producción oral
afirmacion: >
  Durante la sesión de grabación, el hablante mostró inseguridad al
  escribir algunas formas que había producido oralmente con fluidez.
tipo: observacion
estado: registrado
fuentes:
  - SRC-0001
participantes:
  - Vicente Gutiérrez
grado_de_respaldo: directo
alcance: sesión específica
etiquetas:
  - audio
  - escritura
  - validacion_linguistica
```

```yaml
id: DEC-0001
titulo: Prioridad operativa del audio
decision: >
  Cuando exista discrepancia o inseguridad entre escritura y producción
  oral, el audio validado tendrá prioridad operativa para el desarrollo
  inicial de los materiales.
estado: vigente_con_reservas
hallazgos_que_la_sustentan:
  - HALL-0001
principios_relacionados:
  - PRIN-0001
validadores:
  - VAL-0001
impacta_a:
  - PROC-0002
  - OUT-0003
condiciones_de_revision:
  - Revisar cuando exista una convención ortográfica validada para el corpus.
```

```yaml
id: OPEN-0001
pregunta: >
  ¿Qué procedimiento debe utilizarse para representar por escrito una forma
  oral cuando el hablante no tiene seguridad ortográfica?
origen:
  - HALL-0001
por_que_importa: >
  Afecta la transcripción, la revisión del corpus y la producción de
  materiales escritos.
estado: pendiente_de_validacion
requiere:
  - criterio lingüístico
  - revisión con varios hablantes
afecta_a:
  - COR002
  - metodología
```

Este ejemplo muestra que un mismo hallazgo puede producir una decisión provisional y, al mismo tiempo, mantener abierta una pregunta que todavía no ha sido resuelta.

---

# 22. Estado arquitectónico actual

La arquitectura vigente ya define los tipos principales de entidad, sus estados, la autoridad de las decisiones, la función de las vistas y la frontera con sistemas derivados. Las cuestiones abiertas deben registrarse en el backlog o mediante entidades del tipo correspondiente; no deben mantenerse como una lista especulativa dentro de la Constitución.

La evolución histórica permanece disponible en Git y en `archivo/`.

---

## Regla final

El sistema no debe buscar una apariencia artificial de coherencia.

Su función es conservar con precisión:

* lo que se observó;
* lo que se interpretó;
* lo que se cree;
* lo que se decidió;
* quién validó cada aspecto;
* lo que todavía no se sabe;
* lo que cambió;
* y las razones por las que cambió.

La utilidad de esta arquitectura dependerá menos de la cantidad de información registrada que de la claridad con la que cada elemento conserve su origen, alcance, estado y relación con el resto del proyecto.


---

## Actualización v0.2 — 2026-09-02

- Se formaliza la frontera de autoridad entre el Sistema de Conocimiento y sistemas derivados.
- Se establece que los sistemas derivados pueden descubrir y proponer, pero no adoptar, promover ni escribir conocimiento.
- Se establece que los permisos de desarrollo técnico no implican permisos de escritura sobre el Sistema de Conocimiento.
- La actualización responde a `HALL-0008` y `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO`.


---

## Actualización v0.3 — 2026-09-03

- Se reemplaza el árbol conceptual obsoleto por la organización física vigente y se aclara que el diagrama no prescribe una reestructuración.
- Se formaliza que decisiones directas de coordinación o alcance pueden sustentarse en una fuente directa sin fabricar un `HALL` espejo.
- Se clasifican `informes/`, `archivo/` y `dispositivo/` por función y autoridad.
- Se retira de la Constitución la lista histórica de cuestiones "para la siguiente versión"; las deudas actuales pertenecen al backlog.
