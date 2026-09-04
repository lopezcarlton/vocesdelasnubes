# SRC-BIYUBI-DICCIONARIO-DIDXAZA-ESPANOL

```yaml
id: SRC-BIYUBI-DICCIONARIO-DIDXAZA-ESPANOL
tipo: dataset_lexical_documental
bib_id: null
titulo: "Diccionario Biyubi — Didxazá / español"
autor_o_participantes: null
fecha: null
fecha_de_consulta: 2026-09-03
ubicacion: "copia controlada del proyecto; payload no publicado en este repositorio"
archivo_snapshot: "diccionario biyubi(1).xlsx"
sha256_snapshot: "53a01c4661e465930289ff042a2def58627ab8fc26d0b812feb65b47714e3b75"
tamano_bytes: 782774
hoja: "Hoja 1"
filas_con_datos: 23601
elementos_de_fila_en_hoja: 23893
filas_vacias_formateadas_finales: 292
estructura_observada:
  - "columna A: forma/entrada en Didxazá"
  - "columna B: glosa o traducción en español"
licencia_o_derechos: "NO_DOCUMENTADOS_EN_EL_SNAPSHOT / REDISTRIBUCION_PUBLICA_NO_INFERIDA"
nivel_de_fuente: secundaria
estado_de_acceso: copia_controlada_disponible
estatus_operativo: FUENTE_CONSULTABLE_SECUNDARIA_NO_NORMATIVA
```

## Decisión de uso

Biyubi es una fuente consultable del proyecto. Su función es aportar evidencia secundaria de superficie, contraste entre fuentes y candidatos de paradigma. Su presencia no convierte una grafía en norma ni autoriza corrección ortográfica.

```text
BIYUBI = SOURCE
BIYUBI_ROLE = SURFACE_EVIDENCE_SECONDARY / CONTRAST_EVIDENCE / PARADIGM_CANDIDATE
BIYUBI != ORTHOGRAPHIC_AUTHORITY
BIYUBI_ATTESTATION != CORRECTNESS_LICENSE
BIYUBI_ABSENCE != INCORRECTNESS
```

La escritura de Biyubi debe mantenerse aislada y trazable. Cuando se cruce contra otras fuentes, el dispositivo debe identificar Biyubi explícitamente y no mezclar silenciosamente sus formas con Dictionaria, Pickett, BOUND u otras capas.

## Contrato de coincidencia exacta

Para los cruces documentales exactos:

- preservar tonos y diacríticos;
- preservar apóstrofos;
- no usar `near-match`;
- no usar `strip-tone`;
- no convertir una forma PDLMA a superficie para producir un `CROSS_SOURCE_EXACT`;
- distinguir una entrada exacta completa de una forma atestiguada como token dentro de una entrada o frase;
- la puntuación externa de la oración de consulta puede excluirse del token de búsqueda sin alterar la forma documental conservada.

```text
BIYUBI_EXACT_ENTRY != BIYUBI_EXACT_TOKEN_ATTESTATION
EXACT_ATTESTATION = EVIDENCE_ONLY
EXACT_ATTESTATION != FULL_MORPHOLOGICAL_ANALYSIS
```

## Snapshot materializado el 2026-09-03

La copia disponible para el proyecto contiene **23,601 filas con datos** en las columnas A/B. La hoja contiene además 292 elementos de fila vacíos/formateados al final (filas 23,602–23,893), por lo que el XML de la hoja contiene 23,893 elementos de fila en total. El conteo operativo del diccionario es 23,601 pares.

El archivo no incluye una fila de encabezado separada: la primera fila ya contiene el par `A nja'` / `Así, si, cierto, es cierto, es verdad (interjección)`. La última fila con datos es la 23,601: `Zuzuubalu' diidxa` / `Obedecerás, aceptarás disciplinadamente órdenes, aceptarás órdenes`.

El hash SHA-256 identifica esta copia concreta. Un archivo Biyubi posterior con hash distinto debe registrarse como nuevo snapshot o revisión; no debe sustituirse silenciosamente.

## Relación con el dispositivo

El dispositivo puede implementar un loader o índice técnico de Biyubi, pero ese índice es un derivado técnico y debe conservar este `SRC` y el hash del snapshot como provenance.

El payload `.xlsx` no se publica automáticamente en el repositorio público mientras los derechos de redistribución no estén documentados. Esto no limita su uso como fuente de investigación dentro del proyecto.

```text
SRC_RECORD = CANONICAL_SOURCE_IDENTITY
BIYUBI_XLSX = CONTROLLED_SOURCE_PAYLOAD
DEVICE_LOADER_OR_INDEX = TECHNICAL_DERIVATIVE
SOURCE_USED_BY_DEVICE != DEVICE_OWNED_KNOWLEDGE
```

## Primera prueba de realidad vinculada

En `REAL_TEXT_PROBE_002`, el cruce exacto del snapshot recuperó evidencia para seis de trece tipos que habían quedado sin evidencia en las capas entonces consultadas por el Analyzer: `ladxidua'`, `chua'`, `nanna'`, `nadxiilu`, `nayaani'` y `mani`.

Ese resultado demuestra por qué Biyubi debe formar parte de la ruta de consulta documental del dispositivo. No adjudica corrección ni análisis morfológico a esas formas por sí solo.
