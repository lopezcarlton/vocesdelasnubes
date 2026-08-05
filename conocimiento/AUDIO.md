# AUDIO

**Proyecto:** Voces de las Nubes  
**Versión:** 1.0  
**Estado:** Borrador consolidado  
**Fecha:** 2026-08-05

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

1. Preparación de las frases aprobadas.
2. Grabación con hablantes.
3. Registro de al menos dos tomas por frase cuando sea posible.
4. Conservación de identificadores estables que vinculen audio y corpus.

Formato de producción utilizado:

> Español → pausa → Didxazá → pausa → Didxazá

Las pausas forman parte del diseño del material y no son silencios accidentales.

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

---

# 5. Estándares técnicos

## Captura y exportación

- Mono.
- 24 bits.
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

---

# 7. Control de calidad

Debe verificarse:

- correspondencia entre audio y corpus;
- identificadores correctos;
- ausencia de procesamiento que comprometa la inteligibilidad lingüística;
- consistencia de niveles entre archivos;
- revisión auditiva del lote exportado.

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

---

# 10. Limitaciones del documento

Con base exclusivamente en los Markdown de audio disponibles, no puede documentarse todavía:

- protocolo completo de preparación de sesiones de grabación;
- criterios de selección entre múltiples tomas;
- procedimiento formal de archivado de masters;
- política de respaldo y preservación;
- protocolo detallado para incorporación de nuevas voces;
- criterios de aceptación o rechazo de una toma;
- flujo completo de publicación y distribución de todos los derivados.

Estos aspectos requieren evidencia adicional antes de incorporarse al documento definitivo.
