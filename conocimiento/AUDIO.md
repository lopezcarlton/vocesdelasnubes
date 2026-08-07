# AUDIO

**Proyecto:** Voces de las Nubes  
**Versión:** 1.1  
**Estado:** Borrador consolidado  
**Fecha:** 2026-08-06

---

# 1. Objetivo del audio

El componente de audio constituye la fuente primaria para el aprendizaje y la referencia lingüística del proyecto. Su función es registrar producciones orales de alta calidad que permitan comprensión, comparación y producción por parte del aprendiz.

Este documento describe únicamente el proceso de producción de audio. No documenta la metodología general, el diseño del corpus, la teoría pedagógica ni la bibliografía.

---

# 2. Filosofía de producción

- El audio tiene prioridad sobre la representación escrita cuando exista incertidumbre ortográfica.
- Las grabaciones deben conservar la mayor fidelidad posible a la producción oral.
- La edición debe mejorar la claridad técnica sin alterar las características lingüísticas relevantes.
- El procesamiento debe ser reproducible y escalable mediante automatización cuando sea apropiado.

---

# 3. Flujo de grabación

## 3.1 Preparación

1. Preparar las frases o secuencias aprobadas.
2. Vincular cada unidad con un identificador estable del corpus.
3. Verificar el orden pedagógico previsto antes de grabar.
4. Registrar al menos dos tomas por frase o enunciado cuando sea posible.

## 3.2 Formato de producción vigente a partir de COR002

La secuencia pedagógica completa se graba en vivo en un único acto de grabación:

> Español → pausa → Didxazá → pausa → Didxazá

No se graban por separado español y Didxazá para ensamblarlos posteriormente. El hablante produce la secuencia completa en el orden pedagógico previsto.

Las pausas forman parte del diseño del material y no son silencios accidentales.

Este procedimiento deriva de `DEC-GRABAR-EN-VIVO`, sustentada por `HALL-0002`.

COR001 constituye el antecedente histórico: se grabó mediante flujo separado y requirió ensamblaje posterior.

## 3.3 Número de tomas

Se registran como mínimo dos tomas de cada frase o enunciado cuando las condiciones de la sesión lo permitan.

Los criterios para aceptar o rechazar una toma incluyen:

- ausencia de ruido contaminante relevante;
- naturalidad del ritmo y las pausas;
- pronunciación clara;
- correspondencia con la estructura pedagógica prevista;
- ausencia de interrupciones en la secuencia completa.

## 3.4 Técnica de captura

### Resolución

- 32-bit flotantes.
- 48 kHz.
- Mono.

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

## 3.5 Referencia histórica de COR001 con Vicente Gutiérrez

En la sesión de COR001 con Vicente Gutiérrez se utilizaron:

- Canal 1: Neumann KM184, micrófono primario, +29 dB de ganancia de interfaz.
- Canal 2: Shure SM58, respaldo, +47 dB de ganancia de interfaz.

Estos valores son históricos y específicos de esa voz y ese contexto acústico. No constituyen una configuración fija para sesiones futuras.

---

# 4. Flujo de edición

En Ableton se realiza únicamente:

- selección de tomas;
- limpieza básica;
- ecualización correctiva ligera cuando sea necesaria;
- compresión suave;
- calibración fija entre voces.

No se aplica:

- normalización de pico;
- reverb;
- limitación final.

La normalización de sonoridad se realiza posteriormente mediante procesamiento por lotes.

A partir de COR002, el flujo vigente busca eliminar el ensamblaje artesanal de segmentos grabados por separado. La edición debe concentrarse en selección de tomas, limpieza y preparación técnica del material ya registrado en la secuencia pedagógica completa.

---

# 5. Estándares técnicos

## Captura y exportación

- Mono.
- 32-bit flotantes en captura.
- 48 kHz.
- Normalize desactivado.
- Sin reverb.
- Conservando margen dinámico natural.

## Loudness

Se generan dos derivados:

- Escucha general: −16 LUFS integrados.
- Anki: −14 LUFS integrados.

Ambos utilizan un techo de −1.0 dBTP.

El ajuste de LUFS se realiza mediante procesamiento automatizado (`ffmpeg` + `loudnorm`), no manualmente dentro de Ableton.

## Balance entre hablantes

Las diferencias sistemáticas de volumen entre voces se corrigen mediante un ajuste fijo de ganancia por pista antes de la exportación.

---

# 6. Participación de hablantes

Los hablantes participan como productores del contenido oral y validadores de naturalidad.

La grabación no sustituye la validación lingüística posterior cuando esta sea necesaria.

La primera aplicación de `DEC-GRABAR-EN-VIVO` en COR002 debe observar si la secuencia completa resulta operativamente cómoda para el hablante. Si aparecen dificultades recurrentes, la decisión deberá revisarse conforme a sus condiciones de revisión.

---

# 7. Control de calidad

Debe verificarse:

- correspondencia entre audio y corpus;
- identificadores correctos;
- ausencia de procesamiento que comprometa la inteligibilidad lingüística;
- consistencia de niveles entre archivos;
- revisión auditiva del lote exportado;
- verificación de que la secuencia completa se capturó sin interrupciones cuando se aplica el procedimiento vigente.

---

# 8. Publicación

Los archivos conservan un identificador técnico estable (por ejemplo, AUD001-...).

Los nombres descriptivos de las frases se almacenan en metadatos (Título), no como nombre del archivo.

---

# 9. Evolución del proceso

La metodología de audio evolucionó desde un flujo completamente manual hacia un flujo híbrido:

- edición creativa en Ableton;
- procesamiento masivo por script para normalización de sonoridad y derivados.

También se descartó el uso de reverb y la normalización de pico como parte del flujo estándar.

El análisis de COR001 produjo además cuatro cambios o precisiones operativas:

- adopción de grabación en vivo de la secuencia completa a partir de COR002 (`DEC-GRABAR-EN-VIVO`, sustentada por `HALL-0002`);
- técnica de posicionamiento descentrado cuando no exista antipop físico (`HALL-0003`);
- incorporación de room tone en cada sesión (`HALL-0004`);
- estructura de ganancia objetivo para futuras capturas (`HALL-0005`).

La primera sesión de COR002 deberá generar evidencia para confirmar, ajustar o revisar el nuevo flujo de grabación.

---

# 10. Limitaciones del documento

Con la evidencia disponible todavía no puede documentarse de forma definitiva:

- protocolo completo de archivado de masters;
- política de respaldo y preservación;
- protocolo detallado para incorporación de nuevas voces;
- flujo completo de publicación y distribución de todos los derivados.

Estos aspectos requieren evidencia adicional antes de incorporarse al documento definitivo.

---

# 11. Entidades relacionadas

- `conocimiento/hallazgos/HALL-0002.md`
- `conocimiento/hallazgos/HALL-0003.md`
- `conocimiento/hallazgos/HALL-0004.md`
- `conocimiento/hallazgos/HALL-0005.md`
- `conocimiento/decisiones/DEC-GRABAR-EN-VIVO.md`
