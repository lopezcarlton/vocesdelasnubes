# KNOWLEDGE RECOVERY INDEX — PRE-SPLIT — 2026-09-03

**Estado:** `NON_AUTHORITATIVE_RECOVERY_INDEX`  
**Fecha:** 2026-09-03  
**Snapshot pre-index (commit):** `e669397d08ac8c3c266faa4045a4cbf63702ca68`  
**Función:** índice de recuperación para localizar material histórico que permanece en compilaciones técnicas antes de la separación física del dispositivo.

## 1. Regla de uso

Este documento **no incorpora conocimiento al Sistema de Conocimiento** y no valida ninguna formulación contenida en los artefactos técnicos inventariados.

```text
NO_TECHNICAL_FORMULATION_IS_EVIDENCE = true
NO_TECHNICAL_SUMMARY_ESTABLISHES_SOURCE_CLAIM = true
SOURCE_PASSAGE_MUST_BE_READ_BEFORE_ADJUDICATION = true
RECOVERY_INDEX != HALL
RECOVERY_INDEX != TEO
RECOVERY_INDEX != DEC
RECOVERY_INDEX != TEORIA
```

Su función es responder, después de la separación del dispositivo:

1. qué temas fueron registrados históricamente en artefactos técnicos;
2. qué obra o fuente decía usar ese artefacto;
3. qué coordenada de recuperación declaró cuando existe;
4. qué estatuto declaró el propio artefacto cuando ya lo tenía;
5. dónde volver a buscar si una pregunta futura exige adjudicar ese tema.

No debe utilizarse la formulación de un artefacto técnico para decidir **qué dice** una fuente. Si una entrada conduce a Bueno Holle, Gramática Popular, Pérez Báez, Dictionaria u otra fuente, debe abrirse la fuente original pertinente antes de cualquier promoción.

## 2. Convención de etiquetas

El índice distingue dos procedencias de etiqueta:

- `ARTIFACT_DECLARED`: el estatuto se copia literalmente del propio artefacto. No expresa una nueva evaluación de Voces.
- `INVENTORY_ASSIGNED`: la etiqueta sólo describe qué clase de material contiene el artefacto para facilitar recuperación. No juzga su verdad ni su autoridad.

Cuando una entrada se marca `TECHNICAL_OR_BENCHMARK_DERIVED`, significa únicamente que la formulación histórica está ligada a implementación, COR001, benchmark, pipeline o decisión interna del dispositivo y **no debe promoverse desde el artefacto**. La fuente original o la evidencia independiente debe recuperarse primero.

No existe columna de «destino futuro». La investigación futura decide qué pregunta activa el material y si corresponde adjudicarlo.

## 3. Cobertura declarada

### 3.1 Artefactos recorridos de forma completa

| Artefacto | Blob SHA | Tamaño | Cobertura |
|---|---|---:|---|
| `dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md` | `5e621c75bda5c25497273205951da7d8153c1a55` | 105274 B | contenido completo; todos los bloques `JLC-*` agrupados abajo |
| `dispositivo/pedagogia/PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065_v0_36_2.md` | `26280630a5a97e5e67c3156d9ff8503079917655` | 20859 B | contenido completo; secciones pedagógicas agrupadas abajo |
| `dispositivo/migracion/fuentes/SINTESIS_ADVERSARIAL_ARQUITECTURA_DIDXAZA_v1_1_CORREGIDA.md` | `a2c57101d4b16fe0b3e42e1f87f7aa21741c81bf` | 15044 B | contenido completo; bloques de síntesis agrupados abajo |
| `dispositivo/core/NUCLEO_CONVERSACIONAL_001_SCOPE_v1.md` | `00ff6b08866f02e49d7edfcb9f70b79f25d9b4ad` | 10340 B | contenido completo; alcance y construcciones agrupados abajo |
| `dispositivo/migracion/fuentes/PEDAGOGICAL_BACKLOG_BH2019_PARTIAL_v0_35.md` | `e2e84d656df77f43eba5accfc9f96d52ffa4c511` | 2155 B | contenido completo |
| `dispositivo/runtime/v0_2_15_3/PERSON_POSSESSION_EXACT_REGISTRY_v0_2_15_2.csv` | `3ce56a39c33b6ebcd89018540fbe450872aceaf0` | 14154 B | todas las filas; agrupadas por coordenada fuente |
| `dispositivo/runtime/v0_2_15_3/DOCUMENTARY_ALIGNMENT_REGISTRY_v0_2_15_2.csv` | `127c48ddfdac41f34359f3871f65e6aa4e759452` | 20746 B | todas las filas; agrupadas por familia documental |
| `dispositivo/generator/inputs/AdoptionRecords_v1.jsonl` | `e79fbaf80bf2986a5e18703a44d9fc9dc42f3cec` | 8089 B | todos los registros `AR-NC001-ORTH-001..011` |
| `dispositivo/migracion/fuentes/BIB065_BUENO_HOLLE_INGESTION_MATRIX_v0_36_1.md` | `77ef38e088e2a6a7fb8f847fa349bd77229d6a4e` | 10286 B | las 28 filas de la matriz |

`dispositivo/inputs_nc001/AdoptionRecords_v1.jsonl` es una copia con el **mismo blob SHA** que `dispositivo/generator/inputs/AdoptionRecords_v1.jsonl`; se inventarió una sola vez para no duplicar entradas.

### 3.2 Datasets grandes inventariados sólo como conjunto

| Artefacto | Blob SHA | Tamaño | Identidad fuente canónica |
|---|---|---:|---|
| `dispositivo/runtime/v0_2_15_3/PICKETT_LEXICON_BACKFILL_v0_1.csv` | `98b4e87282b996e837356f41ead2f859d53face1` | 940709 B | `SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO` / `BIB003` |
| `dispositivo/analyzer/DIC_VERB_2385_v0_1.csv` | `fc235a6444c2bb15d4aef32ff575a01d2343b1a4` | 767310 B | `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / `BIB054` |
| `DICTIONARIA_entries_v0_2_15_2.csv` | `f921717a59c33b244aff7ed1888b5a02db30f147` | 462257 B | `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / `BIB054` |
| `DICTIONARIA_senses_v0_2_15_2.csv` | `2c59e20f1438c532eb624042875f62272ae2883f` | 1328363 B | `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / `BIB054` |
| `DICTIONARIA_examples_v0_2_15_2.csv` | `0f0a9bc301f64534eeaaafebf3930de2b44b7270` | 1148451 B | `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / `BIB054` |

No se inventariaron fila por fila porque son datasets/derivados ejecutables y el objetivo pre-split es preservar la ruta hacia la fuente, no convertir inventarios técnicos en entidades del conocimiento.

### 3.3 Exclusiones explícitas

No se inventariaron de forma exhaustiva:

- código Python del Analyzer/Corrector/Tutor/Generator/runtime;
- tests y workflows;
- replay, métricas y salidas de COR001;
- bases SQLite;
- `GenerationLicense`, `GenerationEvidenceAtoms`, `AuthorizedSlotFillers`, `IntegrationBlockers`, `OrthographicResolutions` y otros productos de ejecución del generador;
- checkpoints de estado técnico y manifests de migración;
- reportes de benchmark y casos COR001.

Razón: son ejecución, genealogía, pruebas o productos técnicos que continuarán en el repositorio del dispositivo. No constituyen por sí mismos fuentes de Voces. `AdoptionRecords_v1.jsonl` se incluyó como excepción porque contiene enunciados de decisión ortográfica con apariencia de política que deben quedar localizables sin confundirse con decisiones canónicas de Voces.

La exclusión **no afirma que esos archivos carezcan de información**; afirma que no se los convierte en inventario de conocimiento. El repositorio técnico preservará su genealogía.

---

# 4. JUCHITAN_LINGUISTIC_CORE v0.27

**Etiqueta global:** `INVENTORY_ASSIGNED: TECHNICAL_COMPILATION_WITH_SOURCE_DERIVATIONS`  
**Autoridad:** ninguna dentro de Voces.  
**Fuente principal declarada por el artefacto:** Pickett, Black & Marcial Cerqueda, *Gramática popular del zapoteco del Istmo* (`BIB004`), con bloques adicionales que citan Pérez Báez 2015 y otros materiales.

La tabla registra **temas neutros e IDs**, no las proposiciones del JLC.

| IDs / bloque | Tema neutral | Coordenada/fuente declarada por el artefacto | Origen de etiqueta | Nota de recuperación |
|---|---|---|---|---|
| `JLC-OVERVIEW-001`, `MORPH-001`, `NOUN-001`, `PRON-001–002`, `PHON-001`, `TONE-001`, `STRESS-001` | panorama gramatical, morfología, pronombres, fonología, tono/acento | Gramática Popular, introducción/capítulos iniciales | `INVENTORY_ASSIGNED` | volver a `BIB004`; no usar la síntesis JLC como fuente |
| `JLC-POS-001–007`, `JLC-DERIV-001` | posesión nominal y derivación | GP §§4.2–4.3; cuadros 7–9 | `INVENTORY_ASSIGNED` | coordina con registry persona/posesión |
| `JLC-PRON-003–007`, `JLC-PERS-001–003` | persona y pronombres dependientes | GP §5.1.2; cuadros 13–18 | `INVENTORY_ASSIGNED` | volver a paradigmas/cuadros originales |
| `JLC-PERS-004` | persona/tono en caso COR001 | COR001 + referencia a alineación con GP | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde COR001 |
| `JLC-ADJ-001–004`, `JLC-STATE-001–002` | adjetivos, predicación y estados | GP cap. 6 / secciones de adjetivos | `INVENTORY_ASSIGNED` | relectura fuente necesaria |
| `JLC-STATE-003` | predicación adjetival en casos COR001 | COR001 FB-050/057 + arquitectura técnica | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde COR001 |
| `JLC-VERB-001–011` | estructura verbal, TAM/aspecto y juegos verbales | GP cap. 7; paradigmas/tablas indicados | `INVENTORY_ASSIGNED` | incluye formulaciones posteriormente corregidas por `JLC-SP2-*` |
| `JLC-CAUS-001–006` | causatividad y cambio de valencia | GP §§7.1, 7.4 según corrección posterior | `INVENTORY_ASSIGNED` | usar coordenada corregida de segunda pasada |
| `JLC-CAUS-007–008` | valencia/derivación y variación de causativos | Pérez Báez 2015 + notas del proyecto | `INVENTORY_ASSIGNED` | volver a `SRC-PEREZ-BAEZ-2015-VALENCE-CHANGING-JUCHITAN` |
| `JLC-IMP-001–006` | imperativos/mandatos y función pragmática | GP cap. 7 y derivación técnica | `INVENTORY_ASSIGNED` | separar descripción fuente de diseño del motor |
| `JLC-MOVE-001–008` | verbos de movimiento y auxiliares | GP §7.6; cuadros 35–36 | `INVENTORY_ASSIGNED` | volver a ejemplos/paradigmas originales |
| `JLC-MOVE-009` | movimiento en COR001 | COR001 + paradigmas GP | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde benchmark |
| `JLC-COMP-001–006` | composición verbal/lexicalización | GP + síntesis técnica | `INVENTORY_ASSIGNED` | verificar cada patrón en fuente |
| `JLC-COMP-007` | hipótesis `zeenda` | COR001 FB-062 + hipótesis técnica | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde artefacto |
| `JLC-VP-001–008` | frases verbales, dependencia, propósito/capacidad | GP + corpus/derivación técnica | `INVENTORY_ASSIGNED` | localizar construcción concreta antes de afirmar |
| `JLC-NEG-001–004`, `NEG-006–007` | negación como construcción y alcance | GP §§7–8/13 + síntesis técnica | `INVENTORY_ASSIGNED` | revisar fuente original |
| `JLC-NEG-005` | negación/persona con COR001 | COR001 FB-099 | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde COR001 |
| `JLC-INT-001–004`, `INT-006–007` | interrogación y función pragmática | GP + síntesis técnica | `INVENTORY_ASSIGNED` | distinguir descripción gramatical de inferencia pragmática |
| `JLC-INT-005` | interrogación/precio con COR001 | COR001 FB-079 | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde COR001 |
| `JLC-ADV-001–004`, `PREP-001–002`, `PART-001`, `PART-003` | adverbios, relaciones espaciales, partículas | GP caps. 8–9 + síntesis técnica | `INVENTORY_ASSIGNED` | volver a ejemplos/contextos originales |
| `JLC-PART-002` | partícula `nda'` / hipótesis `zeenda` | COR001 FB-062 + material técnico | `INVENTORY_ASSIGNED: TECHNICAL_OR_BENCHMARK_DERIVED` | no promover desde artefacto |
| `JLC-SYN-001–008` | orden de constituyentes, tópico/foco y sintaxis | GP + interpretaciones del dispositivo | `INVENTORY_ASSIGNED` | contraste obligatorio con BIB004/BIB065 según fenómeno |
| `JLC-CLAUSE-001`, `COORD-001`, `SUB-001–008` | coordinación y subordinación | GP cap. 14, especialmente §§14.1–14.2.3 | `INVENTORY_ASSIGNED` | abrir capítulo original |
| `JLC-REL-001–008` | relativas | GP §14.3 | `INVENTORY_ASSIGNED` | abrir ejemplos originales |
| `JLC-TEXT-001–023` | narrativa, diálogo, referencia, inferencia/perspectiva | GP cap. 15, textos corridos | `INVENTORY_ASSIGNED` | mezcla observación textual e interpretación técnica; no asumir equivalencia |
| `JLC-TEXT-024–032`, `JLC-ASPECT-REV-001` | narración, irrealizado y secuencias aspectuales | GP §15.2, ejs. 188–192 | `INVENTORY_ASSIGNED` | volver a ejemplos fuente |
| `JLC-TEXT-033–047` | poesía, aspecto, negación, relativización y personificación | GP §15.3, ejs. 193–196 | `INVENTORY_ASSIGNED` | género poético requiere alcance explícito |
| `JLC-TEXT-048–059` | sueño/poesía, composición, espacio, progresivo y metáfora | GP §15.4, ejs. 197–198 | `INVENTORY_ASSIGNED` | relectura directa de texto/glosa |
| `JLC-TONGUE-001–007` | trabalenguas, contraste fonológico y usos técnicos | GP textos finales + derivación técnica | `INVENTORY_ASSIGNED` | uso técnico no equivale a hallazgo pedagógico |
| `JLC-PROC-001–011` | receta/procedimiento, instrucciones y secuenciación | GP texto `Caldu Benda` + derivación técnica | `INVENTORY_ASSIGNED` | abrir texto original antes de generalizar |
| `JLC-SYNTH-001–013` | síntesis técnica del contenido de GP | síntesis interna del JLC | `INVENTORY_ASSIGNED: TECHNICAL_SYNTHESIS` | la frase histórica «conocimiento consolidado» no tiene autoridad canónica |
| `JLC-SP2-001–007` | segunda pasada: propósito de GP, tono/ortografía, causativo, perfecto, progresivo ambulativo, juegos verbales | GP: Propósito, §§7.1–7.4 y coordenadas declaradas | `INVENTORY_ASSIGNED` | estos bloques corrigen formulaciones técnicas anteriores; aun así requieren fuente para Voces |
| `JLC-SP2-NP-001` | estructura de frase nominal | GP §§4.4, 6 | `INVENTORY_ASSIGNED` | volver a fuente |
| `JLC-SP2-PRON-001–003` | pronombres independientes, reflexivo y negativos | GP §§5.1.1, 5.6, 5.7 | `INVENTORY_ASSIGNED` | volver a fuente |
| `JLC-SP2-ADJ-001–006`, `SP2-DET-001` | calificativos, estativos, cantidad, determinación, posesivos, interrogativos | GP §§6.1–6.8 | `INVENTORY_ASSIGNED` | volver a fuente |
| `JLC-SP2-ADV-001–004`, `SP2-PART-001`, `SP2-DISC-001` | adverbios, partículas y conectores | GP cap. 8, §§8.2, 8.5–8.7 | `INVENTORY_ASSIGNED` | volver a ejemplos fuente |
| `JLC-SP2-PREP-001–002`, `SP2-CONJ-001`, `SP2-INTJ-001` | preposiciones, conjunciones, interjecciones | GP caps. 9–11 | `INVENTORY_ASSIGNED` | inventario léxico no debe reconstruirse desde resumen |
| `JLC-SP2-CLAUSE-001`, `COP-001`, `WEATHER-001`, `ORDER-001`, `Q-001`, `NEG-001` | oración simple, copulativas, clima, orden, preguntas, negación | GP §§12.1–13.3 | `INVENTORY_ASSIGNED` | volver a fuente |
| `JLC-SP2-SUB-001–002`, `SP2-REL-001` | preguntas indirectas, subordinación y relativas | GP §§14.2–14.3 | `INVENTORY_ASSIGNED` | volver a fuente |
| `JLC-SP2-TEXT-001`, `SP2-RECIPE-001`, `SP2-TONGUE-001` | inventario de géneros/textos finales | GP cap. 15 | `INVENTORY_ASSIGNED` | género es metadato del artefacto, no decisión de Voces |
| `JLC-SP2-APP-001–002`, `SP2-CLOSE-001–003` | cobertura del apéndice y cierre técnico de cobertura | GP Apéndice + control técnico | `INVENTORY_ASSIGNED: TECHNICAL_COVERAGE` | «CUBIERTO/CLOSED» describe el core, no el conocimiento canónico |
| `JLC-APP-PHON-001–005`, `APP-VOW-001`, `APP-PROS-001–004`, `APP-ORTH-001` | fonética/fonología y forma de cita/superficie | GP Apéndice para lingüistas, pp. 123–125 | `INVENTORY_ASSIGNED` | abrir apéndice fuente |
| `JLC-APP-ENGINE-001–003`, `APP-TEST-001`, `APP-CERTAINTY-001` | pipeline, pruebas y límites técnicos derivados del apéndice | GP Apéndice + ingeniería | `INVENTORY_ASSIGNED: TECHNICAL_DERIVATION` | separar hechos fuente de decisiones de implementación |

**Cobertura JLC:** todos los bloques e IDs del archivo fueron recorridos. La agrupación evita copiar sus afirmaciones. Una ausencia de un claim concreto en esta tabla significa que quedó absorbido por su rango/bloque, no que se haya adjudicado o descartado.

---

# 5. BIB065 — matriz de Bueno Holle

**Fuente canónica:** `SRC-BUENO-HOLLE-2019` / `BIB065`.  
**Regla especial:** usar la matriz sólo como coordenada de recuperación.  
**Etiquetas:** copiadas del artefacto (`ARTIFACT_DECLARED`).

| ID | Tema neutral | `epistemic_status` declarado | `promotion_status` declarado | Origen etiqueta |
|---|---|---|---|---|
| `BH2019-METH-01` | metodología / combinación de métodos | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-METH-02` | metodología / habla espontánea | `SOURCE_HYPOTHESIS` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-METH-03` | metodología / elicitación con estímulos | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-PROS-01` | prosodia / unidad entonacional | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-PROS-02` | prosodia / realización superficial | `SOURCE_REPORTED_TENDENCY` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-SYN-01` | sintaxis / orden de constituyentes | `SOURCE_REPORTED_TENDENCY` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-SYN-02` | estructura informativa / posición preverbal | `SOURCE_REPORTED_TENDENCY` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-REF-01` | referencia / accesibilidad | `SOURCE_HYPOTHESIS` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-REF-02` | referencia / introducción de referentes | `SOURCE_REPORTED_TENDENCY` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-REF-03` | referencia / rol S y episodios | `SOURCE_REPORTED_TENDENCY` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-REF-04` | referencia / dimensiones discursivas | `SOURCE_REPORTED_TENDENCY` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-COREF-01` | correferencia / tercera persona | `SOURCE_ASSERTED_CONSTRAINT` | `READY_FOR_ADJUDICATION` | `ARTIFACT_DECLARED` |
| `BH2019-COREF-02` | correferencia / saliencia temática | `SOURCE_REPORTED_TENDENCY` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-FOC-01` | foco / foco de predicado-oración | `SOURCE_REPORTED_TENDENCY` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-FOC-02` | foco / foco de argumento | `SOURCE_HYPOTHESIS` | `READY_FOR_ADJUDICATION` | `ARTIFACT_DECLARED` |
| `BH2019-FOC-03` | foco / prosodia | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-FOC-04` | foco / `nga` | `SOURCE_HYPOTHESIS` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-TOP-01` | tópico / construcciones | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-TOP-02` | tópico / topicalización | `SOURCE_ATTESTED_PATTERN` | `READY_FOR_ADJUDICATION` | `ARTIFACT_DECLARED` |
| `BH2019-TOP-03` | tópico / desprendimiento y marcos | `SOURCE_REPORTED_TENDENCY` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-LA-01` | partícula `la` / distribución | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-LA-02` | partícula `la` / análisis del autor | `SOURCE_HYPOTHESIS` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-LA-03` | partícula `la` / análisis unificador | `SOURCE_HYPOTHESIS` | `BLOCKED_FROM_EXECUTION` | `ARTIFACT_DECLARED` |
| `BH2019-CONV-01` | conversación / secuencia de foco | `SOURCE_ATTESTED_PATTERN` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-GEN-01` | empaquetamiento informativo / derivación de proyecto | `PROJECT_DERIVATION` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |
| `BH2019-PED-01` | pedagogía / operaciones discursivas | `PROJECT_DERIVATION` | `BACKLOG_ONLY` | `ARTIFACT_DECLARED` |
| `BH2019-OPEN-01` | pregunta abierta / objeto inanimado | `SOURCE_HYPOTHESIS` | `REQUIRES_ORAL_VALIDATION` | `ARTIFACT_DECLARED` |
| `BH2019-OPEN-02` | límite de generalización | `SOURCE_ATTESTED_PATTERN` | `SAFE_TO_RECORD_NOW` | `ARTIFACT_DECLARED` |

Las etiquetas anteriores son **históricas del artefacto**. `SAFE_TO_RECORD_NOW`, `READY_FOR_ADJUDICATION`, etc. no crean permisos actuales ni sustituyen `BL-022`, las decisiones vigentes o la lectura del libro.

---

# 6. PEDAGOGICAL_DISCUSSION_FREEZE_POST_BIB065 v0.36.2

**Estado declarado por el artefacto:** `FROZEN_DISCUSSION_INPUT_NOT_POLICY` / `NON_NORMATIVE`.  
**Origen etiqueta:** `ARTIFACT_DECLARED`.

| Bloque | Tema neutral | Fuente/coordenada declarada | Nota |
|---|---|---|---|
| apertura / §1 | alcance pedagógico de COR002 y estatus de artefactos previos | discusión de proyecto post-BIB065 | no convertir el freeze en política |
| §2 | protecciones entre alcance técnico y alcance pedagógico | decisiones/guardrails del proyecto | formulación histórica |
| A1–A6 | alcance y progresión pedagógica | discusión post-BIB065 | candidatos, no currículo |
| B1–B5 | coherencia conversacional | BIB065 + discusión de proyecto | no adjudicado |
| C1–C9 | referencia y seguimiento de participantes | BIB065 + discusión | no adjudicado |
| D1–D7 | foco, tópico, orden, `nga`, prosodia | BIB065 + discusión | no adjudicado |
| E1–E6 | audio y prosodia | BIB065 + diseño pedagógico | no adjudicado |
| F1–F6 | métodos de adquisición/elicitación | BIB065 + discusión | contrastar con `SRC-BUENO-HOLLE-2019` |
| G1–G4 | español y representación interna del generador | diseño técnico-pedagógico | `INVENTORY_ASSIGNED: TECHNICAL_DERIVATION` |
| H1–H6 | ideas de actividades pedagógicas | discusión del proyecto | no política |
| correcciones/deferrals | límites de contexto obligatorio, capas finas y autoridad pedagógica | freeze histórico | consultar decisiones actuales antes de reutilizar |
| preguntas futuras / cierre | agenda de discusión | freeze histórico | no crea backlog por sí sola |

---

# 7. SINTESIS_ADVERSARIAL_ARQUITECTURA_DIDXAZA v1.1 corregida

**Etiqueta global:** `INVENTORY_ASSIGNED: HISTORICAL_TECHNICAL_SYNTHESIS`.

| Bloque temático | Coordenadas/fuentes declaradas | Nota de recuperación |
|---|---|---|
| rol histórico de COR001 y firewall | COR001 + arquitectura técnica | usar sólo como genealogía; autoridad actual está en Voces |
| convergencias y desacuerdos entre auditorías externas | auditorías históricas | no son evidencia lingüística por sí mismas |
| decisiones `ACCEPT/MODIFY/REJECT/DEFER/EXPERIMENT` | síntesis adversarial | etiquetas del artefacto describen triaje técnico histórico |
| Analyzer / Normalizer / Corrector / Tutor / Generator | arquitectura técnica | permanece en dispositivo |
| guardas contra evidence laundering | metodología técnica | comparar con `DEC-AUTORIDAD` si alguna vez se reutiliza |
| inventario/operación Biyubi | artefactos técnicos y fuentes citadas | no convertir cruces técnicos en fuente |
| adquisición oral / fieldwork | metodología propuesta | volver a fuentes/metodología canónica antes de adoptar |
| textos traducidos y evidencia | discusión metodológica | no política actual por sí sola |
| holdout/generalización | diseño de evaluación | técnico |
| NC001 / vertical slice | diseño del dispositivo | técnico |
| invariantes/tests/scope | ingeniería | técnico |

No se copian aquí los argumentos ni conclusiones de la síntesis. Si una pregunta futura depende de ellos, debe reconstruirse desde sus fuentes y decisiones canónicas pertinentes.

---

# 8. NUCLEO_CONVERSACIONAL_001_SCOPE v1

**Etiqueta global:** `INVENTORY_ASSIGNED: TECHNICAL_SCOPE_NOT_PEDAGOGICAL_SCOPE`.

| Bloque | Tema neutral | Fuente/coordenada declarada | Nota |
|---|---|---|---|
| alcance general | variedad, habla, verbos/personas/TAM incluidos | fuentes y registries del dispositivo | no equivale a currículo beginner |
| selección léxica | conjunto reducido de verbos y criterio técnico | Dictionaria/JLC/registries | «high-frequency» no debe inferirse si no fue medido |
| paradigmas | celdas atestiguadas/no atestiguadas | tablas técnicas | volver a fuente para conocimiento |
| construcciones `C01–C06` | inventario de construcciones del slice | artefactos del generador | licencia técnica, no teoría canónica |
| `C06` | deseo/querer y potencial fuera de generación libre | alcance técnico | no convierte una restricción técnica en restricción pedagógica |
| capability matrix | capacidades por construcción | implementación | técnico |
| ConceptMapping H/C | mapeo TAM limitado | implementación | no define todo el sistema TAM |
| perfil ortográfico | reglas/guardas técnicas del slice | AdoptionRecords/OrthographicProfile | no norma ortográfica de Voces |
| development corpus | 120–180 utterances, audio-first | protocolo técnico histórico | contrastar con CORPUS/METODOLOGIA vigentes |
| holdout | aislamiento de evaluación | protocolo técnico | técnico |
| tests/exclusiones | criterios de implementación | NC001 | técnico |

---

# 9. PEDAGOGICAL_BACKLOG_BH2019_PARTIAL v0.35

**Estado declarado:** `PROVISIONAL_BACKLOG_NOT_AUTOMATICALLY_EXECUTABLE`.  
**Origen:** `ARTIFACT_DECLARED`.

| Bloque | Tema neutral | Nota |
|---|---|---|
| A | cambios estructurales considerados seguros en el contexto técnico histórico | no equivale a adopción pedagógica vigente |
| B | preguntas para adjudicación pedagógica posterior | se solapan con preguntas ahora formalizadas en `BL-022` |
| C | aplazamientos explícitos | incluye no reescribir P, no productivizar foco/tópico, no convertir =be/∅ o `nga` en reglas globales, no hacer contexto/prosodia obligatorios |

Este archivo es un antecedente técnico de preguntas que hoy deben resolverse desde el backlog y las fuentes originales, no un backlog canónico paralelo.

---

# 10. PERSON_POSSESSION_EXACT_REGISTRY v0.2.15.2

**Etiqueta global:** `INVENTORY_ASSIGNED: TECHNICAL_REGISTRY_WITH_SOURCE_COORDINATES`.

Todas las filas fueron recorridas. Se agrupan por coordenada declarada:

| Familia | Fuente/coordenada histórica | Fuente canónica para relectura | Nota |
|---|---|---|---|
| tercera persona dependiente: humano/animal/cosa y plurales; inclusivo/exclusivo | `BIB004_GRAMATICA_POPULAR`, GP §5.1.2, Cuadro 13 | `SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR` | registry no sustituye cuadro |
| persona dependiente en posesión | GP §5.1.2, Cuadro 14 | mismo SRC | volver a cuadro |
| 2SG y alternancias | GP Cuadro 15 | mismo SRC | volver a paradigma |
| 1SG y fusiones | GP Cuadros 16–17 | mismo SRC | volver a paradigmas |
| ejemplos de persona | GP ejs. 22–23 y secciones asociadas | mismo SRC | coordenadas técnicas |
| posesión `x-/xh-` y alternancias | GP §4.2.1, cuadros asociados | mismo SRC | volver a fuente |
| sustantivos siempre poseídos | GP §4.2.2 | mismo SRC | volver a fuente |
| posesión con `xti'` y cadenas | GP §4.2.3 | mismo SRC | volver a fuente |

No se promueve ninguna superficie ni regla desde el registry.

---

# 11. DOCUMENTARY_ALIGNMENT_REGISTRY v0.2.15.2

**Etiqueta global:** `INVENTORY_ASSIGNED: TECHNICAL_ALIGNMENT_REGISTRY`.

Todas las filas fueron recorridas. Familias principales:

| Familia | Etiqueta/coordenada histórica | Fuente canónica actual | Nota |
|---|---|---|---|
| persona 2SG/1SG | `BIB004_GRAMATICA_POPULAR`, GP §5.1.2 / cuadros | `SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR` / BIB004 | alineación técnica |
| posesión | GP §4.2–4.2.3 | mismo SRC | alineación técnica |
| nominalización `guenda/enda` | GP §4.3 | mismo SRC | alineación técnica |
| TAM/paradigmas | GP §§7.1–7.2 | mismo SRC | alineación técnica |
| negación/construcciones | GP §§7.2.5–8.5 y coordenadas registradas | mismo SRC | verificar sección exacta al reabrir fuente |
| frases frecuentes / vocabulario Pickett | etiqueta histórica `BIB055_PICKETT_VOCABULARIO` | **`SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO` / BIB003** | el `BIB055` técnico histórico no es el ID bibliográfico canónico actual |

La discrepancia `BIB055_PICKETT_VOCABULARIO` se conserva como etiqueta histórica del artefacto para rastreabilidad, pero la bibliografía reconciliada vigente identifica el Vocabulario como **BIB003**.

---

# 12. AdoptionRecords v1 — decisiones ortográficas técnicas históricas

**Etiqueta global:** `INVENTORY_ASSIGNED: TECHNICAL_ADOPTION_RECORDS_NOT_CANONICAL_DECISIONS`.

Se copiaron únicamente IDs, temas y `status` declarados. Ningún `ADOPTED_*` de este archivo equivale a una `DEC` vigente de Voces.

| ID | Tema neutral | `status` declarado | Origen etiqueta |
|---|---|---|---|
| `AR-NC001-ORTH-001` | preservación de superficie Unicode observada | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-002` | PDLMA vs superficie de salida | `ADOPTED_HARD_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-003` | tono/diacríticos y normalización automática | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-004` | apóstrofo/glotalización | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-005` | espaciado de clíticos | `OPEN_NOT_ADOPTED_GLOBAL` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-006` | espaciado de compuestos | `OPEN_NOT_ADOPTED_GLOBAL` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-007` | near-match/strip-tone/strip-accent | `ADOPTED_HARD_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-008` | variantes documentadas | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-009` | adjudicación histórica de una celda `gusé'` | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-010` | conflicto ortográfico histórico de celdas `dxiichi` | `SUPERSEDED_BY_AR-NC001-ORTH-011` | `ARTIFACT_DECLARED` |
| `AR-NC001-ORTH-011` | uso histórico de Dictionaria como referencia ortográfica técnica | `ADOPTED_CONSERVATIVE_GUARD` | `ARTIFACT_DECLARED` |

Especialmente `AR-NC001-ORTH-009..011` deben tratarse como **historia de implementación**. Cualquier política ortográfica futura se adjudica en Voces usando Norma 2016, fuentes contemporáneas, corpus y hablantes dentro de su alcance; no se hereda por el hecho de que el generador antiguo la marcara `ADOPTED`.

---

# 13. Datasets agregados

## 13.1 PICKETT_LEXICON_BACKFILL

- objeto: derivado técnico masivo;
- fuente que dice representar: Vocabulario zapoteco del Istmo;
- fuente canónica: `SRC-PICKETT-2007-VOCABULARIO-ZAPOTECO-ISTMO` / BIB003;
- acción futura si se necesita una afirmación léxica: volver al Vocabulario o a otra fuente primaria pertinente, no citar el backfill como autoridad.

## 13.2 DIC_VERB_2385

- objeto: inventario técnico de 2,385 entradas verbales con lemas, PDLMA, clases/análisis, TAM y ejemplos;
- procedencia documental dominante: dataset Dictionaria y capas técnicas asociadas;
- fuente canónica: `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / BIB054;
- las columnas de análisis (`pdlma`, `verb_class`, `analysis_codes_raw`, etc.) son material técnico y no se promueven como si fueran campos publicados por Dictionaria sin verificar su procedencia exacta.

## 13.3 Fixtures Dictionaria del runtime

`DICTIONARIA_entries/senses/examples_v0_2_15_2.csv` se conservan como fixtures/datasets del runtime. Su identidad documental vuelve a `SRC-DICTIONARIA-DIDXAZA-SPANISH-ENGLISH-DICTIONARY` / BIB054. No se duplican aquí sus filas.

---

# 14. Qué garantiza este índice — y qué no

Este índice garantiza que, para el snapshot declarado:

- los principales artefactos técnicos identificados como portadores de formulaciones lingüísticas, pedagógicas o de política ortográfica están localizados;
- el JLC completo quedó mapeado por bloques e IDs;
- las 28 filas BIB065 conservan sus estatutos declarados sin copiar sus claims como verdad;
- los artefactos pedagógicos históricos quedan localizables sin convertirlos en política;
- los registries persona/posesión y alineación quedan vinculados a sus fuentes originales;
- las decisiones ortográficas técnicas de `AdoptionRecords` quedan visibles como historia, no como `DEC` canónica;
- los datasets grandes quedan vinculados a su fuente original sin inventariar millones de celdas.

No garantiza que todo tema técnico sea correcto, útil o digno de adjudicación futura. Tampoco afirma que cada archivo dentro de `dispositivo/` haya sido semánticamente resumido. Código, tests, salidas y fixtures permanecen en la genealogía técnica y se excluyeron deliberadamente.

## Regla para uso futuro

```text
QUESTION_BECOMES_ACTIVE
-> CONSULT_RECOVERY_INDEX_FOR_COORDINATES
-> OPEN_CANONICAL_SRC
-> READ_ORIGINAL_PASSAGE_OR_DATA
-> ADJUDICATE_IN_VOCES
-> ONLY_THEN_UPDATE_HALL/TEO/DEC/VIEWS_IF_NEEDED
```

No abrir el resumen técnico para «recordar qué decía la fuente» y después buscar confirmación. El índice debe conducir a la coordenada, y la relectura debe partir del original.

## Estado pre-split

```text
RECOVERY_INDEX_CREATED = true
MASS_ADJUDICATION_REQUIRED_BEFORE_SPLIT = false
BL-016_REMAINS_CLOSED = true
NEW_BACKLOG_ITEM_CREATED = false
ARCHITECTURE_CHANGED = false
PHYSICAL_DEVICE_SPLIT = pending_destination_repository
```
