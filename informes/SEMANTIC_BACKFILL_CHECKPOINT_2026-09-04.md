# SEMANTIC_BACKFILL_CHECKPOINT_2026-09-04

**Estado:** `ACTIVE / PBK2016_PILOT_COMPLETED / GRAMATICA_POPULAR_BACKFILL_IN_PROGRESS`  
**Repositorio autoritativo:** `lopezcarlton/vocesdelasnubes`

## 1. Diagnóstico

Durante la revisión conjunta del *Alfabeto Popular para la escritura del zapoteco del Istmo* de 1956 se detectó un problema de migración del conocimiento:

```text
SOURCE_IDENTITY_MIGRATED = YES
LEGACY_TECHNICAL_EXTRACTIONS_EXIST = YES
CANONICAL_SEMANTIC_PROMOTION_TO_VOCES = INCOMPLETE
```

Varias fuentes prioritarias estaban correctamente identificadas en `conocimiento/fuentes/`, y el repositorio técnico histórico conservaba reglas derivadas de ellas, pero algunos hechos lingüísticos ya estudiados no habían sido promovidos como `HALL` canónicos ni habían quedado suficientemente resumidos en sus `SRC`.

Esto produjo dos síntomas:

1. falsa apariencia de incertidumbre sobre asuntos ya estudiados;
2. consultas lentas que reconstruían demasiado estado y terminaban entrando al dispositivo para recuperar conocimiento bibliográfico.

No se crea una nueva capa arquitectónica para resolverlo. Los `SRC` existentes funcionan como identidad y **memoria persistente de lectura**; `HALL/TEO/VAL/DEC` conservan la promoción/adjudicación; el dispositivo permanece como sistema derivado.

## 2. Casos que revelaron el problema

Quedaron reparados de inmediato:

- segunda persona singular sin oposición gramatical `tú/usted` → `HALL-0066`;
- inventario contemporáneo de tres tonos fonémicos → `HALL-0067`;
- continuidad de la regla contextual `xh/x` ante consonante → `HALL-0068`;
- `r` débil como patrón general y `r` fuerte como excepción léxica / préstamos → `HALL-0069`;
- atestación dialectal `tobi` Juchitán / `tubi` El Espinal → `HALL-0070`, `HALL-0071`;
- Alfabeto Popular como base fundacional y referencia de la tradición ortográfica posterior → `HALL-0072`.

Se corrigieron además hallazgos del Alfabeto que habían quedado demasiado abiertos:

- `HALL-0032` — cuatro tonos de 1956 recontextualizados frente al sistema contemporáneo de tres;
- `HALL-0048` — `xh/x` vinculado con fuentes posteriores;
- `HALL-0052` — `r` histórica vinculada con distribución contemporánea;
- `HALL-0061` — `tú/usted` resuelto por contraste con Gramática Popular y Vocabulario.

## 3. Piloto PBK2016 — clases verbales

El caso `SRC-PEREZ-BAEZ-KAUFMAN-2016-VERB-CLASSES` confirmó que la fuente había sido ingerida antes de la separación, aunque esa ingesta no quedó suficientemente visible desde Voces.

Evidencia de recuperación histórica:

- once reglas `PBK-VERB-*` / `PBK-DER-*` sobreviven en el runtime;
- la SQLite histórica conserva once filas `BIB059_PBK2016` en `morphology_rule_registry_v023`;
- `DIC_VERB_2385_v0_1.csv` conserva 2,385 registros verbales derivados de Dictionaria con clase, TAM, provenance y otros campos.

Para no promover conocimiento desde artefactos técnicos, se reabrieron directamente **sólo los pasajes pertinentes** del artículo original y se materializó:

- `HALL-0073` — sistema A–D diagnosticado principalmente por potencial y completivo;
- `HALL-0074` — habitual como vía de aislamiento de raíz y predictibilidad del resto del paradigma una vez conocida la clase;
- `HALL-0075` — distribución cuantitativa e irregularidad del sistema descrito;
- `HALL-0076` — separación entre notación analítica PBK/PDLMA y superficie del Alfabeto Popular.

Se amplió además el `SRC` de PBK2016 con cobertura, coordenadas, notación, límites, derechos y memoria persistente de lectura.

Resultado:

```text
GENERAL_VERB_CLASS_QUERY_CAN_BE_ANSWERED_FROM_VOCES = true
FULL_PBK_PDF_REREAD_REQUIRED = false
DEVICE_REQUIRED_FOR_GENERAL_CLASS_SYSTEM = false
```

La asignación individual de clase a los 2,385 registros sigue siendo primariamente una cuestión documental de Dictionaria. El CSV técnico puede ayudar temporalmente a recuperar un registro, pero no se copia completo a Voces por defecto para evitar peso y duplicación.

## 4. Regla consulta vs adjudicación

La optimización no modifica la garantía epistemológica.

### Consulta

```text
ROUTINE_QUERY
-> HALL / TEO / DEC / VAL PERTINENTE
-> SRC PARA PROVENANCE / COBERTURA SI HACE FALTA
-> RESPONDER
```

No reabrir el PDF/libro completo si el conocimiento ya está suficientemente registrado.

### Nueva adjudicación

```text
NEW_OR_CHANGED_CANONICAL_CLAIM
-> LOCATE RELEVANT SOURCE COORDINATE
-> OPEN RELEVANT SOURCE PASSAGE
-> ADJUDICATE
-> UPDATE ONLY NECESSARY ENTITIES/VIEWS
```

Se conserva:

```text
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
FULL_SOURCE_MUST_BE_REREAD_BEFORE_ADJUDICATION = false
```

Los derivados del dispositivo pueden utilizarse sólo para localizar coordenadas o detectar huecos:

```text
LEGACY_DEVICE_RULE_AS_RECOVERY_INDEX = ALLOWED
LEGACY_DEVICE_RULE_AS_KNOWLEDGE_AUTHORITY = FORBIDDEN
```

## 5. Fuentes prioritarias para backfill sistemático

La reparación puntual y el piloto PBK2016 no sustituyen el backfill de las otras fuentes prioritarias.

### P0-A — Gramática Popular

`SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR`

Objetivo: recorrer el conocimiento históricamente compilado en `JUCHITAN_LINGUISTIC_CORE_v0_27` únicamente como índice de recuperación, verificar por bloques los pasajes necesarios y promover a Voces reglas, paradigmas, excepciones y límites todavía ausentes.

No releer el libro linealmente desde cero si las coordenadas de ingesta histórica permiten una revisión dirigida.

### P0-B — Pickett–Villalobos–Marlett 2009/2010 + corrigendum

Objetivo: formalizar inventario segmental/tonal, fortis-lenis, vibrantes, fonación, acento y realizaciones contextuales, distinguiendo fonema, alófono, convención ortográfica y dato acústico.

### P0-C — Xneza diidxazá 2015

Objetivo: completar la ingesta de fonología, genealogía del Alfabeto Popular, palabra fonológica/gramatical/ortográfica, compuestos, colocaciones, clíticos y problemas de normalización.

### P0-D — Bueno Holle 2019

Objetivo: completar fonología/prosodia relevante, metodología de corpus, sintaxis de discurso, referencia, tópico/foco y cualquier consecuencia real para analizador, tutor y generador.

### P1 — Vocabulario Pickett

Objetivo: promover notas gramaticales y ortográficas reutilizables que actualmente existen principalmente como backfills técnicos o evidencia lexicográfica dispersa.

### P1 — Cardona 2020 y Cardona–Vicente 2025

Objetivo: consolidar distribución dialectal y representación ortográfica de variación para evitar que `variante local` se convierta en `error` por falta de contexto.

### P0 bloqueado por acceso — Norma 2016

`SRC-CATA-ETAL-2016-NORMA-ESCRITURA`

La identidad está localizada, pero el texto completo sigue pendiente. No reconstruir su contenido desde citas indirectas.

## 6. Reentrada y rendimiento

`INICIAR_AQUI_CHAT_NUEVO.md` fue cambiado el 2026-09-04 de reconstrucción exhaustiva a `LAZY_TARGETED_LOADING`.

```text
READ_EVERYTHING_BY_DEFAULT = false
LOAD_ONLY_RELEVANT_KNOWLEDGE = true
NORMAL_VOCES_QUERY_DOES_NOT_LOAD_DEVICE = true
```

La mejora estructural puede evaluarse por reducción de lecturas necesarias. La latencia real de la aplicación debe medirse en un chat nuevo, porque un chat largo conserva su propio contexto anterior y no permite aislar el efecto del nuevo reentry.

## 7. Consecuencia para la revisión del Alfabeto de 1956

La revisión sección por sección queda **pausada temporalmente** después de las narraciones de las páginas impresas 12–13.

No se continúa a poesía hasta haber reparado el baseline mínimo suficiente para que la lectura histórica no vuelva a crear huecos falsos o a presentar como hipótesis cuestiones ya resueltas por fuentes posteriores.

## 8. Consecuencia para el dispositivo

Voces se corrige primero. Después de cada bloque suficientemente estable, el dispositivo puede actualizar su representación técnica conservando enlaces a `HALL`/`DEC` y al `KNOWLEDGE_SOURCE_COMMIT` utilizado.

```text
VOCES = AUTHORITY_FOR_KNOWLEDGE
DEVICE = DERIVED_IMPLEMENTATION
```

## 9. P0-A Gramática Popular — checkpoint intermedio 2026-09-04

La ejecución dirigida confirmó que `JUCHITAN_LINGUISTIC_CORE_v0_27` era útil como índice de recuperación, pero no suficientemente fiable como autoridad: contenía simplificaciones antiguas, grados de certeza desalineados y al menos una atribución de sección incorrecta. Cada promoción nueva se verificó contra el pasaje original pertinente de la Gramática Popular.

Bloques cerrados hasta este checkpoint:

1. **Sistema verbal/aspectual §7.2–§7.3** → `HALL-0077`–`HALL-0089`.
   - perfecto corregido: acción repetida a lo largo del tiempo + uso negativo de intervalo;
   - habitual/completivo/progresivo/estativo no se equiparan mecánicamente a tiempos del español;
   - potencial = construcción sensible, no sólo capacidad/posibilidad;
   - Juego 1C: la fuente afirma explícitamente potencial sin prefijo;
   - `u` del Juego 2 como vocal temática causativa permanece hipótesis de la fuente;
   - Juego 1A/1B/1C/2 de GP no se iguala automáticamente a A/B/C/D de PBK2016.
2. **Persona §5.1–§5.1.2** → `HALL-0090`–`HALL-0096`.
   - independientes y dependientes conservados como tipos funcionales distintos;
   - 3P puede quedar sin marca segmental si el contexto recupera el referente;
   - 1SG/2SG incluyen fusiones y alternancias de raíz;
   - inclusivo/exclusivo documentado sin convertirlo en nivel pedagógico fijo.
3. **Posesión §4.2 y §6.6** → `HALL-0097`–`HALL-0101`.
   - tres estrategias distintas;
   - alternancias bajo `xh-/x-`;
   - sustantivos siempre poseídos no aceptan `xh-/x-`;
   - `xti'` admite poseedor dependiente o nominal y no concuerda con género/número de lo poseído.
4. **Causatividad/valencia §7.1 y §7.4** → `HALL-0102`–`HALL-0105`.
   - causatividad incrementa valencia;
   - `si-` es la forma más común, no la única;
   - otros prefijos, alternancias y excepciones requieren evidencia por lema/paradigma;
   - no generar causativos ciegamente por analogía.
5. **Imperativos/movimiento §7.5–§7.6** → `HALL-0106`–`HALL-0109`.
   - singular y plural imperativo tienen construcciones distintas;
   - `ir/venir` tienen progresivo especial;
   - tono puede distinguir progresivo y futuro de `venir` aun con la misma forma segmental;
   - auxiliares de movimiento seleccionan verbo principal en potencial para movimiento con intención.

Entidades/vistas actualizadas sin crear capas nuevas:

```text
SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR = UPDATED_READING_MEMORY
HALL-0077..HALL-0109 = CANONICAL_ADJUDICATED_KNOWLEDGE
TEORIA.md = v1.6
NEW_CONCEPTUAL_LAYER = false
```

Reglas de seguridad reforzadas:

```text
UNMARKED_3RD_PERSON != ERROR
UNRESOLVED != INCORRECT
STRIP_TONE_BEFORE_ANALYSIS = unsafe
BLIND_SUFFIX_OR_PREFIX_STRIPPING = unsafe
BLIND_CAUSATIVE_GENERATION = forbidden_without_lexeme_or_paradigm_evidence
COR001 = ANALYSIS_TARGET_ONLY
```

### Próximo bloque dirigido dentro de P0-A

Continuar por **negación, partículas dependientes y orden/interrogación** (cap. 8 y cap. 13), porque tienen impacto directo en Analyzer/Corrector/Tutor y el índice técnico histórico contiene reglas resumidas que deben verificarse contra la fuente. Después, cubrir subordinación/relativas y sólo entonces los géneros textuales/apéndice técnico que sigan pendientes de promoción semántica.

P0-A permanece `IN_PROGRESS`; no se declara completa la Gramática Popular ni se relee linealmente el libro.
