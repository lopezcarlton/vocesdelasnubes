## IDENTIFICACIÓN DEL CONTEXTO

Tema principal del chat: Especificaciones técnicas de postproducción de audio (captura, mezcla, loudness, nomenclatura de archivos)
Fecha aproximada: 05/08/2026
Notas sobre timing: Posterior a la primera sesión de grabación con Vicente Gutiérrez; el usuario trajo un resumen previo generado en otra plataforma (Gemini) sobre técnica de grabación y especificaciones de exportación, que fue auditado y corregido en este chat
Participante principal: Emiliano
Autoridades consultadas: Ninguna interviene directamente en este chat (es trabajo técnico de audio, no validación lingüística)
Duración estimada: Medio (2-6h equivalente)

---

# 1. Descripción general

Con las primeras grabaciones de audio ya hechas (formato español-pausa-Didxazá-pausa-Didxazá), Emiliano necesitaba resolver el flujo de postproducción: qué nivel de sonoridad usar, si normalizar o no en Ableton, a qué frecuencia/profundidad de bits exportar, cómo nombrar los archivos para que sean localizables sin perder trazabilidad con el corpus, y cómo balancear el volumen entre su propia voz (español) y la de Vicente (Didxazá) dentro del mismo clip. Emiliano trajo a la conversación un resumen técnico generado previamente en Gemini sobre su setup de grabación (micrófono dual Neumann KM 184 + Shure SM58, tratamiento acústico del cuarto, especificaciones LUFS) que fue revisado, parcialmente confirmado y parcialmente corregido en este chat. El resultado es un protocolo operativo completo de captura → edición → exportación por lotes.

---

# 2. Decisiones finales

## Targets de loudness para exportación final

**Decisión:** Exportar dos derivados por frase: versión "iTunes"/escucha completa a -16 LUFS integrados, y versión Anki a -14 LUFS integrados, ambas con techo de -1.0 dBTP.

**Porque:** -24 LUFS (estándar de broadcast ATSC A/85) es demasiado bajo para escucha en audífonos o bocina de celular, que es el contexto real de uso del material. -16/-14 LUFS está alineado con el estándar de consumo de podcasts/contenido hablado móvil (Apple Podcasts, Spotify).

**Validado por:** No validado por hablante — es decisión puramente técnica de Emiliano en el chat.

**Aplicar a:** Todo el pipeline de exportación de audio (AUD y ANK).

**Conflictúa con:** El resumen previo de Gemini ya proponía -16/-14 LUFS correctamente para este punto — no hay conflicto ahí. Sí conflictuó con una consideración inicial de Emiliano de exportar a -24 LUFS, que fue descartada.

**Causa/depende de:**
- Causada por: pregunta de Emiliano sobre a qué LUFS exportar sus primeras grabaciones.
- Causó después: decisión de mover el ajuste de LUFS fuera de Ableton, a un script por lotes (ver decisión siguiente).
- Depende de: que la etapa de captura/edición en Ableton entregue el archivo seco, sin normalizar ni limitar previamente.

**Status:** Firmemente decidida.

**Notas:** La medición LUFS integrada es menos confiable en clips muy cortos (1-3 segundos); se recomendó revisión auditiva del lote además de confiar solo en el medidor.

---

## Ajuste de loudness fuera de Ableton, por lote

**Decisión:** El ajuste a target LUFS no se hace dentro de Ableton (ni con el botón "Normalize", ni con plugins de medición como WLM salvo que tengan corrector automático). Se hace con un script (`ffmpeg` + filtro `loudnorm`) que procesa toda una carpeta de exportaciones secas de una sola vez y genera ambos derivados (iTunes/Anki) automáticamente.

**Porque:** El botón "Normalize" de Ableton es normalización de pico, no de sonoridad LUFS — no resuelve el problema. Ajustar manualmente cientos de clips uno por uno (incluso viendo el número correcto en un medidor como WLM) es insostenible dado el volumen del corpus (224+ frases, cada una con dos derivados).

**Validado por:** No aplica (decisión técnica de flujo de trabajo).

**Aplicar a:** Pipeline completo de postproducción, a partir de ahora.

**Conflictúa con:** El enfoque inicial de Emiliano de intentar resolver todo (EQ, compresión, reverb, loudness) dentro de Ableton usando WLM Meter.

**Causa/depende de:**
- Causada por: Emiliano reportó que editar y exportar clip por clip en Ableton es "artesanal" e insostenible.
- Causó después: definición de qué SÍ se queda en Ableton (EQ correctivo ligero, compresión suave, calibración de ganancia entre pistas) vs. qué se mueve al script (loudness target, limitación de pico).
- Complementa: la decisión de exportar sin normalizar y sin reverb desde Ableton.

**Status:** Firmemente decidida.

**Notas:** Se proveyó un script bash de ejemplo con `ffmpeg loudnorm` en modo de una pasada; se dejó abierta la posibilidad de migrar a dos pasadas si se detectan inconsistencias de volumen entre frases.

---

## Formato de exportación desde Ableton (previo al script)

**Decisión:** Exportar desde Ableton en mono, 24-bit / 48 kHz, con "Normalize" desactivado, sin reverb, conservando el headroom natural de la grabación (picos alrededor de -11 dBFS, sin necesidad de subir ganancia).

**Porque:** Mono es suficiente porque es una sola voz por pista sin necesidad de imagen estereofónica. 24-bit es formato de entrega adecuado (32-bit float es formato de trabajo, no de exportación final). Reverb contamina de forma irreversible la señal y puede enmascarar las distinciones vocálicas finas (cortada vs. quebrada) que el proyecto necesita preservar con claridad. Normalizar el pico en Ableton antes de que el script ajuste LUFS genera doble procesamiento innecesario y resultados menos predecibles.

**Validado por:** No aplica.

**Aplicar a:** Toda exportación de audio desde Ableton, tanto para AUD (maestro) como insumo del script.

**Conflictúa con:** Directamente contradice la sugerencia del resumen de Gemini de aplicar reverb en la etapa de exportación.

**Causa/depende de:**
- Causada por: pregunta de Emiliano sobre si convenía convertir a mono, normalizar, y a qué frecuencia exportar, tras haber grabado a 32-bit float/48kHz.
- Causó después: aclaración de que EQ correctivo y compresión ligera sí pueden aplicarse en Ableton, pero reverb y limitación de pico no.

**Status:** Firmemente decidida.

**Notas:** Si en el setup de grabación se usaron simultáneamente el Neumann KM 184 y el Shure SM58 en pistas separadas, no deben sumarse a mono automáticamente por riesgo de cancelación de fase; debe elegirse una pista fuente única (recomendado: Neumann, por rango dinámico y detalle en agudos) y usar la otra solo como respaldo de contingencia.

---

## Calibración de ganancia entre voces distintas dentro del mismo clip

**Decisión:** Cuando dos o más voces coexisten en el mismo clip (español de Emiliano + Didxazá de Vicente, y en el futuro la voz femenina adicional), se calibra una sola vez la ganancia fija de cada pista (usando el device "Utility" de Ableton, no el fader), comparando nivel RMS o loudness momentáneo entre hablantes, hasta que ambas voces suenen parejas al oído. Esa ganancia queda fija en la pista y se hereda automáticamente en todas las exportaciones siguientes.

**Porque:** El script de ajuste por lotes mide y corrige la sonoridad integrada de todo el archivo, no de segmentos dentro de él — no puede corregir que una voz suene más baja que otra dentro del mismo clip. Ese desbalance debe resolverse antes de exportar, en Ableton.

**Validado por:** No aplica (decisión técnica).

**Aplicar a:** Todas las pistas de hablantes (Emiliano, Vicente, y la futura hablante femenina).

**Conflictúa con:** No hay conflicto; es complementaria al pipeline de loudness por lote.

**Causa/depende de:**
- Causada por: Emiliano reportó que su voz se escucha más suave que la de Vicente en las grabaciones ya hechas.
- Causó después: definición del mismo protocolo para cuando se incorpore la tercera voz (hablante femenina).
- Depende de: que la diferencia de nivel entre hablantes sea sistemática (proyección vocal, distancia al mic) y no algo que varíe frase a frase — si no es sistemática, este método no aplica igual.

**Status:** Firmemente decidida.

**Notas:** Para calibrar la pista de la hablante femenina, las frases de prueba usadas deben cubrir los tres tonos del sistema (Alto, Bajo, Bajo Ascendente), no solo un fragmento parcial de su habla, para que el offset calculado sea representativo.

---

## Nomenclatura de archivos vs. metadatos de búsqueda

**Decisión:** Los archivos de audio conservan su nombre técnico de catálogo (AUD001-VG-T1, etc.) en disco. El nombre de la frase (ej. "Hola", "Naa, Vicente lá'") se agrega en los metadatos de Título (y ya se agregaron Artista/Álbum), no en el nombre del archivo.

**Porque:** Nombrar archivos por el texto de la frase los hace frágiles ante correcciones futuras de traducción (habría que renombrar cada vez), introduce problemas de compatibilidad entre sistemas por acentos/apóstrofes/espacios, y rompe la relación uno-a-uno silenciosa con la numeración de COR001. Los metadatos permiten búsqueda humana en iTunes sin sacrificar trazabilidad.

**Validado por:** No aplica.

**Aplicar a:** Todos los archivos AUD ya existentes y futuros.

**Conflictúa con:** La intuición inicial de Emiliano de renombrar los archivos como 001_Hola, 002_Como_estás.

**Causa/depende de:**
- Causada por: Emiliano reportó dificultad para localizar frases específicas en iTunes usando solo el nombre AUD.
- Causó después: definición de que los derivados ANK llevan su propio prefijo (mismo número, distinto prefijo), ya que solo contienen la porción en Didxazá sin el español precedente.

**Status:** Firmemente decidida.

---

# 3. Cambios realizados

### Especificación de audio para el pipeline de postproducción

**Antes:** No existía un protocolo formal; Emiliano tenía un resumen generado en Gemini con especificaciones (-24 LUFS considerado inicialmente, sugerencia de aplicar reverb, compresión agresiva "para inteligibilidad en ambientes ruidosos", exportación directa desde Ableton con normalización activada).

**Ahora:** Protocolo de dos etapas — (1) Ableton: captura/edición seca, mono, 24-bit/48kHz, sin normalizar, sin reverb, con calibración de ganancia fija entre pistas de hablantes; (2) script por lote (`ffmpeg loudnorm`) que genera automáticamente los derivados a -16 LUFS (iTunes/escucha) y -14 LUFS (Anki), ambos con techo -1.0 dBTP.

**Motivo:** Insostenibilidad del ajuste manual clip por clip dado el volumen del corpus; corrección de varias recomendaciones técnicas incorrectas o subóptimas del resumen de Gemini (target LUFS demasiado bajo, reverb, doble limitación).

**Quién lo propuso/hizo:** Emiliano planteó las preguntas; se definieron las correcciones en este chat.

**Archivos/secciones afectados:** Todo el flujo AUD → ANK; ítem #8 (Herramientas y recursos técnicos) del documento de contexto del proyecto debería actualizarse con estas especificaciones.

**Reversible:** Sí — son parámetros de script, ajustables si se detectan problemas al escuchar el lote resultante.

---

### Convención de nomenclatura de archivos y metadatos

**Antes:** Solo definida la convención AUD001-VG-T1 a nivel de archivo, sin resolver cómo hacer los clips buscables por frase en un reproductor.

**Ahora:** Nombre técnico se mantiene en disco; nombre de frase va en metadato de Título; Artista y Álbum ya fueron definidos por Emiliano ("Voces de las Nubes – Didxazá (Zapoteco del Istmo)" / "Frases básicas nivel inicial - Saludos y despedidas").

**Motivo:** Necesidad de búsqueda rápida por frase sin perder trazabilidad con el corpus.

**Quién lo propuso/hizo:** Emiliano identificó el problema; la solución (separar identificador técnico de capa de metadatos) se definió en el chat.

**Archivos/secciones afectados:** Todos los AUD existentes (requieren revisión de que ya tengan el tag de Título correcto) y futuros.

**Reversible:** Sí.

---

# 6. Criterios y reglas adoptadas

## Regla de separación EQ/compresión (Ableton) vs. loudness/limitación (script)

**Definición:** La limpieza correctiva (EQ ligero, compresión suave con ratio bajo 2:1–3:1 para parejar dinámica dentro de una frase) se hace en Ableton, con oído, cuando el clip lo requiera. El ajuste a un nivel LUFS objetivo y la limitación de pico (techo -1.0 dBTP) se hacen exclusivamente en el script por lote, nunca en Ableton.

**Aplica a:** Todo el pipeline de postproducción de audio.

**Porque:** Evita doble procesamiento (doble limitación, doble ajuste de nivel) que hace el resultado impredecible y difícil de diagnosticar. Compresión agresiva tipo "podcast/radio" no es apropiada para material fonético de una lengua tonal, donde se prioriza preservar la envolvente natural de la voz.

**Validado por:** No aplica (decisión técnica).

**Excepciones:** Ninguna definida.

**¿Cómo se verifica cumplimiento?** Revisión auditiva del lote de salida antes de darlo por cerrado.

---

## Regla: sin reverb en material fuente

**Definición:** Nunca añadir reverb a las grabaciones en la etapa de exportación/masterización. Las grabaciones deben conservarse lo más secas posible.

**Aplica a:** Todas las grabaciones de voz del corpus (AUD y sus derivados).

**Porque:** La reverb enmascara la envolvente temporal exacta de la señal, de la cual dependen distinciones fonéticas finas (vocal cortada vs. quebrada). Es un proceso irreversible sobre el archivo fuente; si en algún momento se necesita ambiente, se puede añadir después sobre una fuente limpia, pero no se puede quitar si se grabó con reverb encima.

**Validado por:** No aplica.

**Excepciones:** Ninguna.

**¿Cómo se verifica cumplimiento?** Revisión de la cadena de exportación de Ableton antes de correr el script.

---

# 7. Pendientes explícitos

## Alta prioridad

### Actualizar el documento de contexto interno del proyecto con las especificaciones de audio definidas en este chat

**Qué hay que hacer:** Incorporar al documento maestro (sección de herramientas/recursos técnicos) los targets de LUFS finales, el flujo Ableton→script, y la regla de calibración de ganancia entre pistas.

**Por qué:** El documento de contexto actual (v. Mayo 2026) tiene especificaciones parcialmente distintas o incompletas respecto a lo decidido aquí.

**Depende de:** Nada, puede hacerse de inmediato.

**Quién debería hacerlo:** Emiliano.

**Bloqueador:** Ninguno.

### Calibrar ganancia de pista para la futura hablante femenina

**Qué hay que hacer:** Grabar frases de prueba de la nueva hablante que cubran los tres tonos (Alto, Bajo, Bajo Ascendente), medir su nivel contra la pista de referencia (Vicente), y fijar el offset de ganancia en su pista.

**Por qué:** Sin esto, su voz podría quedar desbalanceada respecto a las demás dentro del mismo clip, igual que ocurrió inicialmente con Emiliano y Vicente.

**Depende de:** Que la hablante femenina ya esté grabando (pendiente de campo, ver documento de contexto general — colaboradora aún no formalizada).

**Quién debería hacerlo:** Emiliano.

**Bloqueador:** Formalización de la colaboradora.

## Prioridad media

### Correr el script de procesamiento por lote sobre las grabaciones ya existentes

**Qué hay que hacer:** Aplicar el pipeline `ffmpeg loudnorm` a las primeras grabaciones ya hechas con Vicente, generando ambos derivados (iTunes/Anki).

**Por qué:** Las primeras grabaciones aún no han pasado por este proceso definido en el chat.

**Depende de:** Confirmar que las exportaciones de Ableton ya están en mono/24-bit/48kHz/sin normalizar.

**Quién debería hacerlo:** Emiliano.

**Bloqueador:** Ninguno grave; puede requerir instalar `ffmpeg` si no está disponible.

---

# 10. Cosas descartadas

## Exportar a -24 LUFS integrados

**Descripción:** Propuesta inicial de Emiliano de usar -24 LUFS como nivel de exportación, por parecerle "un volumen agradable".

**Por qué se rechazó:** -24 LUFS es el estándar de broadcast de TV (ATSC A/85), pensado para sistemas de reproducción calibrados, no para escucha cercana en audífonos o bocina de celular. Sonaría notablemente más bajo que el resto del contenido en el dispositivo del aprendiz.

**Quién lo rechazó / validó rechazo:** Definido en este chat, sin validación de hablante (es decisión puramente técnica).

**¿Por qué documentarlo?** Para evitar reconsiderar este valor sin razón técnica de por medio.

---

## Nombrar archivos de audio con el texto de la frase (ej. 001_Hola)

**Descripción:** Propuesta de Emiliano de renombrar los archivos AUD directamente con el nombre de la frase en español, para facilitar la búsqueda en iTunes.

**Por qué se rechazó:** Fragilidad ante correcciones futuras de traducción, problemas de compatibilidad de caracteres especiales entre sistemas, y pérdida de la relación directa y estable con la numeración de COR001.

**Quién lo rechazó / validó rechazo:** Definido en este chat.

**¿Por qué documentarlo?** La solución alternativa (metadatos de Título) resuelve el mismo problema sin los riesgos — evitar reconsiderar el renombrado directo.

---

## Aplicar reverb en la exportación final (sugerencia del resumen de Gemini)

**Descripción:** El resumen técnico que Emiliano trajo de una sesión previa en Gemini sugería aplicar "un poco de reverb" en Ableton al exportar, junto con EQ y compresión.

**Por qué se rechazó:** Contradice directamente el tratamiento acústico ya invertido en la grabación (lana de roca, difusores) y el objetivo de preservar distinciones fonéticas finas del Didxazá; es un proceso irreversible sobre el archivo fuente.

**Quién lo rechazó / validó rechazo:** Corregido en este chat.

**¿Por qué documentarlo?** El resumen de Gemini sigue siendo una fuente de referencia que Emiliano puede consultar de nuevo; es importante que quede registrado que este punto específico fue corregido, no solo confirmado.

---

## Compresión agresiva para la versión Anki ("inteligibilidad en ambientes ruidosos")

**Descripción:** El resumen de Gemini sugería mayor compresión en la versión Anki bajo la lógica de asegurar inteligibilidad en entornos ruidosos, siguiendo convenciones de podcast/radio comercial.

**Por qué se rechazó:** Para material fonético de una lengua tonal, se prioriza preservar la envolvente dinámica natural de la voz; el contexto de uso real (estudio enfocado) no justifica ese trade-off.

**Quién lo rechazó / validó rechazo:** Corregido en este chat.

**¿Por qué documentarlo?** Evitar reintroducir esta lógica en futuras iteraciones del pipeline de Anki.

---

# 13. Próximo paso recomendado

## Próximo paso

**Acción:** Correr el script `ffmpeg loudnorm` sobre el lote de grabaciones ya hechas con Vicente, verificar auditivamente el resultado, y actualizar el documento de contexto interno del proyecto con las especificaciones técnicas definidas en este chat.

**Por qué es natural después de este chat:** Todas las decisiones técnicas de captura, mezcla y exportación ya están cerradas; falta aplicarlas al material existente y dejarlas registradas fuera de este chat.

**Quién debería hacerlo:** Emiliano.

**Contexto para continuación:** Los targets finales son -16 LUFS/-1dBTP (iTunes, WAV 24-bit/48kHz) y -14 LUFS/-1dBTP (Anki, MP3 192kbps u Ogg/Opus); la calibración de ganancia entre pistas de hablantes debe hacerse en Ableton antes de exportar, no en el script.

**Depende de que primero:** Confirmar disponibilidad de `ffmpeg` en el sistema de Emiliano (instalable vía Homebrew en macOS).
