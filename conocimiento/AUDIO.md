# AUDIO

**Proyecto:** Voces de las Nubes  
**Versión:** 1.3  
**Estado:** Borrador consolidado  
**Fecha:** 2026-09-03

---

# 1. Objetivo del audio

El componente de audio constituye la fuente primaria para el aprendizaje y la referencia lingüística del proyecto. Su función es registrar producciones orales de alta calidad que permitan comprensión, comparación y producción por parte del aprendiz, además de conservar evidencia oral útil para análisis y documentación.

Este documento describe únicamente el proceso de producción de audio. No documenta la metodología general, el diseño del corpus, la teoría pedagógica ni la bibliografía.

## 1.1 Alcance activo de fase

La decisión `DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN` fija actualmente:

```text
ACTIVE_LANGUAGE_LEVEL = BEGINNER
ACTIVE_PRIMARY_MODALITY = LISTENING
ACTIVE_BASELINE_VARIETY = JUCHITAN
ACTIVE_LITERACY_TRACK = false
```

Para AUDIO esto significa priorizar materiales auditivos técnicamente claros y adecuados a principiantes de Juchitán. **No fija por sí mismo una velocidad, un patrón de repetición ni una secuencia única de audio**; esas decisiones requieren justificación pedagógica y pruebas específicas.

---

# 2. Filosofía de producción

- El audio tiene prioridad sobre la representación escrita cuando exista incertidumbre ortográfica.
- Las grabaciones deben conservar la mayor fidelidad posible a la producción oral.
- La edición debe mejorar la claridad técnica sin alterar las características lingüísticas relevantes.
- El procesamiento debe ser reproducible y escalable mediante automatización cuando sea apropiado.
- **No existe un único formato pedagógico de audio válido para todos los corpus, niveles, actividades o etapas del proyecto.**
- Cada momento del proyecto puede requerir derivados o secuencias diferentes según el objetivo de aprendizaje, el nivel del aprendiz, el tipo de actividad y la naturaleza del material.
- Un formato adoptado para una fase concreta no se convierte por ello en plantilla permanente para COR001, COR002 ni corpus posteriores.

El proyecto puede utilizar, entre otros, formatos con apoyo en español, formatos únicamente en Didxazá, derivados específicos para tarjetas o práctica focalizada y registros de habla más continua o naturalista. Esta enumeración no constituye un catálogo cerrado.

---

# 3. Flujo de grabación

## 3.1 Preparación

1. Preparar las frases, secuencias, conversaciones o materiales aprobados según el objetivo de la sesión.
2. Vincular cada unidad con un identificador estable del corpus cuando corresponda.
3. Verificar el formato de audio previsto para ese material antes de grabar.
4. Registrar tomas suficientes para seleccionar material técnicamente y lingüísticamente útil; cuando sea pertinente, se procuran al menos dos tomas de material controlado.

## 3.2 Grabación en vivo de secuencias compuestas

Cuando un material utilice una secuencia pedagógica compuesta —por ejemplo:

> Español → pausa → Didxazá → pausa → Didxazá

— la secuencia puede grabarse completa en vivo en un único acto, en lugar de registrar cada componente por separado y ensamblarlo posteriormente.

Las pausas forman parte del diseño del material cuando ese formato las requiere y no son silencios accidentales.

Este procedimiento deriva de `DEC-GRABAR-EN-VIVO`, sustentada por `HALL-0002`.

La decisión se refiere al **modo de capturar una secuencia compuesta cuando ese formato haya sido elegido**. No establece que esa secuencia sea obligatoria para todo COR002 ni para corpus posteriores.

COR001 constituye el antecedente histórico que motivó esta decisión: parte de su producción requirió ensamblaje posterior de segmentos y mostró el costo de edición artesanal asociado.

## 3.3 Formatos variables por objetivo pedagógico

El formato de audio se determina según la función del material.

Por tanto:

- una secuencia con español puede ser útil en una fase y dejar de serlo en otra;
- un material puede necesitar una versión únicamente en Didxazá;
- una actividad de recuperación, una tarjeta, una conversación completa o un material avanzado pueden requerir derivados diferentes;
- la evolución pedagógica puede justificar nuevos formatos sin que ello invalide los anteriores dentro del uso para el que fueron diseñados.

La política general es **preservar la flexibilidad de formatos y documentar qué objetivo cumple cada uno**.

## 3.4 Número de tomas

En materiales controlados se registran como referencia al menos dos tomas de cada frase, enunciado o secuencia cuando las condiciones de la sesión lo permitan.

En habla espontánea, interacción naturalista u otros formatos abiertos, la unidad útil puede ser un tramo continuo y no resulta apropiado imponer automáticamente el mismo criterio de tomas repetidas.

Los criterios para aceptar o rechazar material incluyen, según el tipo de grabación:

- ausencia de ruido contaminante relevante;
- naturalidad del ritmo y las pausas;
- pronunciación suficientemente clara;
- correspondencia con el objetivo de la grabación;
- ausencia de interrupciones técnicas que inutilicen el material.

## 3.5 Técnica de captura

### Resolución

- 32-bit flotantes.
- 48 kHz.
- Mono cuando el diseño de la sesión lo permita y corresponda.

### Estructura de ganancia

- Objetivo promedio: −18 dBFS a −12 dBFS.
- Picos máximos: −6 dBFS.
- La ganancia concreta de interfaz se ajusta según hablante, micrófono y contexto acústico.

Referencia: `HALL-0005`.

### Posicionamiento de micrófono sin antipop físico

Cuando no exista antipop físico, se utiliza como referencia:

- distancia aproximada: 30 cm;
- altura: nariz/pómulo del hablante;
- ángulo: aproximadamente 45° hacia la barbilla.

El objetivo es reducir golpes de aire sin comprometer la captación de voz.

Referencia: `HALL-0003`.

### Room tone

En cada sesión se registra silencio ambiental puro de la sala:

- duración: 10–15 segundos;
- momento: al inicio de la sesión;
- uso: reducción de ruido y consistencia ambiental en postproducción.

Referencia: `HALL-0004`.

## 3.6 Referencia histórica de COR001 con Vicente Gutiérrez

En la sesión de COR001 con Vicente Gutiérrez se utilizaron:

- Canal 1: Neumann KM184, micrófono primario, +29 dB de ganancia de interfaz.
- Canal 2: Shure SM58, respaldo, +47 dB de ganancia de interfaz.

Estos valores son históricos y específicos de esa voz y ese contexto acústico. No constituyen una configuración fija para sesiones futuras.

---

# 4. Flujo de edición

En Ableton se realiza principalmente, cuando corresponda:

- selección de tomas;
- limpieza básica;
- ecualización correctiva ligera cuando sea necesaria;
- compresión suave;
- calibración fija entre voces.

No se aplica por defecto:

- normalización de pico;
- reverb;
- limitación final.

La normalización de sonoridad se realiza posteriormente mediante procesamiento por lotes cuando el producto final lo requiere.

Cuando una secuencia compuesta se haya grabado completa en vivo, la edición debe concentrarse en selección de tomas, limpieza y preparación técnica del material ya registrado, evitando reconstruir artesanalmente una secuencia que pudo capturarse de forma natural.

Los registros naturalistas o continuos pueden requerir otro tratamiento editorial y deben conservar siempre el registro primario antes de producir derivados.

---

# 5. Estándares técnicos

## Captura y exportación

Como referencia para los materiales controlados:

- 32-bit flotantes en captura.
- 48 kHz.
- Normalize desactivado.
- Sin reverb por defecto.
- Conservando margen dinámico natural.

La configuración de canales y el formato final pueden variar cuando la sesión tenga más de un participante o un objetivo documental distinto.

## Loudness

Para los derivados ya utilizados en el proyecto se han adoptado como referencias:

- Escucha general: −16 LUFS integrados.
- Anki: −14 LUFS integrados.

Ambos utilizan un techo de −1.0 dBTP.

Estas referencias corresponden a productos concretos y no obligan a que todo registro primario o futuro derivado deba entregarse en esos niveles.

El ajuste de LUFS se realiza mediante procesamiento automatizado (`ffmpeg` + `loudnorm`) cuando corresponda, no manualmente dentro de Ableton.

## Balance entre hablantes

Las diferencias sistemáticas de volumen entre voces pueden corregirse mediante ajustes consistentes de ganancia antes de la exportación, sin borrar diferencias lingüísticamente relevantes ni alterar el registro primario.

---

# 6. Participación de hablantes

Los hablantes participan como productores del contenido oral y validadores de naturalidad dentro del alcance de cada sesión.

La grabación no sustituye la validación lingüística posterior cuando ésta sea necesaria.

Cuando se pruebe un nuevo formato de grabación, debe observarse si resulta operativamente cómodo y productivo para las personas participantes. La utilidad de un formato puede depender del tipo de hablante, su relación con el interlocutor, su soltura comunicativa y el objetivo de la sesión.

Un resultado débil en una sola sesión no basta para descartar definitivamente un formato de trabajo si existen razones para pensar que otras condiciones o participantes pueden producir resultados diferentes.

---

# 7. Control de calidad

Debe verificarse, según el tipo de material:

- correspondencia entre audio y corpus o sesión;
- identificadores correctos cuando existan;
- ausencia de procesamiento que comprometa la inteligibilidad lingüística;
- consistencia técnica de los derivados;
- revisión auditiva del material exportado;
- conservación del registro primario;
- correspondencia entre el formato elegido y el objetivo pedagógico o documental.

---

# 8. Publicación

Los archivos conservan un identificador técnico estable cuando forman parte de un corpus o producto versionado (por ejemplo, `AUD001-...`).

Los nombres descriptivos pueden almacenarse en metadatos y no necesariamente como nombre del archivo.

Un mismo registro primario puede producir varios derivados pedagógicos sin que ninguno de ellos sustituya al original.

---

# 9. Evolución del proceso

La metodología de audio evolucionó desde un flujo completamente manual hacia un flujo híbrido y seguirá modificándose según los materiales y niveles que se desarrollen.

Se conservan como aprendizajes técnicos:

- evitar ensamblaje artesanal cuando una secuencia compuesta puede grabarse completa en vivo (`DEC-GRABAR-EN-VIVO`, sustentada por `HALL-0002`);
- técnica de posicionamiento descentrado cuando no exista antipop físico (`HALL-0003`);
- incorporación de room tone en cada sesión (`HALL-0004`);
- estructura de ganancia objetivo para futuras capturas (`HALL-0005`).

La evolución pedagógica ya ha mostrado que el proyecto necesitará múltiples formatos de audio. Ninguno debe convertirse en plantilla universal únicamente porque haya sido útil en una etapa anterior.

La incorporación progresiva de habla naturalista constituye otra línea experimental. Sus primeras pruebas deberán evaluarse por la calidad y utilidad del material obtenido, sin convertir una sola sesión exitosa o fallida en una conclusión definitiva sobre el método.

---

# 10. Limitaciones del documento

Con la evidencia disponible todavía no puede documentarse de forma definitiva:

- protocolo completo de archivado de masters;
- política de respaldo y preservación;
- protocolo detallado para incorporación de nuevas voces;
- catálogo completo de formatos pedagógicos futuros;
- flujo completo de publicación y distribución de todos los derivados;
- procedimiento técnico definitivo para corpus oral naturalista con múltiples participantes.

Estos aspectos requieren evidencia adicional antes de incorporarse como procedimientos definitivos.

---

# 11. Entidades relacionadas

- `conocimiento/hallazgos/HALL-0002.md`
- `conocimiento/hallazgos/HALL-0003.md`
- `conocimiento/hallazgos/HALL-0004.md`
- `conocimiento/hallazgos/HALL-0005.md`
- `conocimiento/decisiones/DEC-GRABAR-EN-VIVO.md`
