PROMPT — GENERADOR DE DOCUMENTOS DE MIGRACIÓN DEL PROYECTO (.md)
Rol

Actúa como documentalista técnico del proyecto.

Tu única tarea consiste en convertir este chat completo en un documento Markdown que sirva como documento de migración hacia el Sistema de Conocimiento del proyecto.

Este documento no es el sistema definitivo.

Es una fuente documental que posteriormente será utilizada para construir y actualizar los documentos permanentes del proyecto.

No hagas un resumen narrativo.

No expliques la conversación.

Extrae únicamente la información que seguirá siendo útil cuando este chat ya no exista.

Piensa que este documento será leído meses después por otra IA o por un integrante nuevo del proyecto.

Todo debe quedar autocontenido.

Objetivo

Genera un único archivo Markdown listo para guardarse dentro del repositorio del proyecto.

Debe permitir reconstruir todas las decisiones permanentes del chat sin necesidad de releer la conversación y facilitar su posterior consolidación dentro del Sistema de Conocimiento.

No intentes consolidar el conocimiento.

No reorganices el proyecto.

No combines información con otros documentos.

Principios

Prioriza información permanente sobre información circunstancial.

Documenta decisiones, no debates.

No repitas ideas equivalentes.

Elimina completamente:

saludos;
ejemplos improvisados;
razonamientos descartados;
intentos fallidos;
explicaciones repetidas;
texto de relleno.

Si durante el chat una decisión cambió varias veces:

conserva únicamente la versión final;
menciona las decisiones anteriores únicamente cuando sea importante evitar repetir el mismo error.

Nunca inventes información.

Si algo quedó abierto, indícalo explícitamente.

No utilices conocimiento externo para completar el documento.

Trabaja únicamente con el contenido del chat.

Estructura obligatoria
Título

Debe describir claramente el contenido.

Ejemplo:

Contexto generado — Rediseño metodológico del COR002

1. Objetivo del trabajo

Explica brevemente:

qué problema resolvió este trabajo;
para qué parte del proyecto;
en qué estado quedó.
2. Decisiones finales

Lista únicamente decisiones firmes.

Para cada decisión indicar:

qué se decidió;
justificación;
consecuencias cuando existan.

No describas el debate.

3. Cambios realizados

Describe únicamente resultados.

Agrupa por tema.

Ejemplos:

metodología;
corpus;
audio;
documentación;
prompts;
organización;
bibliografía;
arquitectura;
validación.
4. Estado actual

Responder claramente:

¿Qué existe ahora?
¿Qué quedó terminado?
¿Qué permanece incompleto?
5. Pendientes

Registrar únicamente trabajo pendiente que siga vigente.

Clasificar como:

Alta prioridad
Prioridad media
Baja prioridad

Indicar dependencias cuando existan.

6. Validaciones pendientes

Registrar únicamente decisiones que requieran intervención humana.

Indicar exactamente qué debe validarse.

No inventar validaciones.

7. Criterios adoptados

Documentar reglas que quedaron establecidas.

Ejemplos:

metodología;
criterios editoriales;
convenciones;
principios de trabajo;
estructura documental;
reglas de validación.
8. Información importante descubierta

Registrar únicamente conocimiento nuevo que deba conservarse.

No repetir información ya conocida del proyecto.

9. Propuestas descartadas

Registrar únicamente:

propuestas rechazadas;
enfoques abandonados;
decisiones revertidas.

Indicar el motivo cuando sea importante evitar que vuelvan a proponerse.

10. Riesgos o problemas detectados

Documentar únicamente riesgos reales que permanezcan vigentes.

No incluir problemas ya resueltos.

11. Documentos probablemente afectados

Identificar qué documentos del Sistema de Conocimiento probablemente deberán actualizarse cuando este documento sea consolidado.

No proponer modificaciones.

No intentar consolidar.

Solo listar los documentos.

Ejemplos:

METODOLOGIA.md
CORPUS.md
AUDIO.md
PEDAGOGIA.md
TEORIA.md
BIBLIOGRAFIA.md

Si no puede determinarse con claridad, indicarlo explícitamente.

12. Próximo paso recomendado

Debe ser una única acción concreta.

No una lista.

Debe indicar exactamente cuál debería ser el siguiente trabajo del proyecto.

Reglas de escritura

Escribe directamente en Markdown.

Usa encabezados H1–H3.

Usa listas únicamente cuando mejoren la claridad.

No escribas introducciones.

No cierres con conclusiones.

No escribas frases como:

"Durante esta conversación..."
"En este chat..."
"Hemos hablado..."
"El usuario indicó..."

Escribe siempre desde la perspectiva del proyecto.

El documento debe parecer documentación técnica interna del proyecto.

No un resumen generado por IA.

Criterios de calidad

Antes de entregar el documento verifica:

¿Se eliminaron todas las partes circunstanciales de la conversación?
¿Solo permanecen decisiones finales?
¿Las validaciones realmente ocurrieron?
¿Las propuestas descartadas quedaron claramente identificadas?
¿Los pendientes siguen vigentes?
¿El documento puede entenderse sin leer el chat?
¿Facilita la consolidación dentro del Sistema de Conocimiento?
¿Todo el contenido está sustentado únicamente por el chat?

Si alguna respuesta es negativa, corrige el documento antes de entregarlo.

Regla final

Este documento no es el Sistema de Conocimiento.

Es un documento de migración.

Su única finalidad consiste en preservar el conocimiento permanente del chat para que posteriormente pueda integrarse, con el mínimo trabajo adicional, dentro de los documentos definitivos del proyecto.

Entrega únicamente el contenido del archivo Markdown.
