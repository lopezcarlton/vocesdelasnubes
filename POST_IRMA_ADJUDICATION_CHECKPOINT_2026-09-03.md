# POST-IRMA ADJUDICATION CHECKPOINT — 2026-09-03

**Proyecto:** Voces de las Nubes  
**Estado:** `CURRENT_REENTRY_CHECKPOINT / PARTIAL_ADJUDICATION / OPEN_RESEARCH`

## 1. Genealogía

El estado pre-Irma permanece congelado en:

```text
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

La primera captura post-Irma se conserva en `POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md`.

Este archivo registra el estado posterior a la incorporación de las notas lingüísticas adicionales de Irma y de nuevas decisiones explícitas de Emiliano.

## 2. Fuentes de reunión y notas posteriores

- `conocimiento/fuentes/SRC-IRMA-PINEDA-REUNION-2026-09-02.md`
- `conocimiento/fuentes/SRC-IRMA-PINEDA-NOTAS-LINGUISTICAS-2026-09-03.md`
- `conocimiento/fuentes/SRC-EMILIANO-DECISIONES-ALCANCE-2026-09-03.md`

La primera y segunda son reconstrucciones posteriores de la reunión, no transcripción literal.

## 3. Alcance activo adoptado

Decisión vigente:

`conocimiento/decisiones/DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN.md`

```text
ACTIVE_LANGUAGE_LEVEL = BEGINNER
ACTIVE_PRIMARY_MODALITY = LISTENING
ACTIVE_BASELINE_VARIETY = JUCHITAN
ACTIVE_LITERACY_TRACK = false
```

Esto modifica la interpretación de la segmentación por edad: durante la fase actual se investigan **materiales de escucha para principiantes en distintos grupos escolares**, no una arquitectura simultánea de alfabetización o fortalecimiento escrito.

## 4. Públicos escolares

Sigue vigente:

`DEC-PUBLICOS-ESCOLARES-MULTIETARIOS`

La educación secundaria técnica es el primer anclaje institucional prioritario, pero no el público exclusivo. `BL-023` debe investigar diferencias por edad dentro del alcance principiante/auditivo actual.

## 5. Memorización

Emiliano identifica como deuda pedagógica prioritaria justificar la función de la memorización frente a un entorno docente constructivista que combate el tedio de la repetición mecánica.

Mapa inicial:

`informes/MEMORIZATION_PEDAGOGICAL_JUSTIFICATION_RESEARCH_MAP_v0_1.md`

Distinción de investigación:

```text
ROTE_RESTUDY != RETRIEVAL_PRACTICE
RETRIEVAL_PRACTICE != SPACED_PRACTICE
MEMORIZATION != COMPLETE_PEDAGOGY
FORMULAIC_SEQUENCE_MEMORY = HIGH_RELEVANCE_CANDIDATE
```

La compatibilidad con los principios pedagógicos de Casa de las Ciencias no se declara resuelta hasta discutir evidencia, diseño real y riesgo de tedio con docentes y aprendices.

## 6. Norma de escritura 2016

Emiliano confirmó que la `Norma del sistema de escritura de la lengua zapoteca` de 2016 es el documento al que Irma se refería.

Entidades:

- `HALL-0010`
- `HALL-0021`
- `SRC-DICTIONARIA-NORMA-ESCRITURA-2016-REFERENCE`
- `SRC-INALI-INFORME-LOGROS-2016-NORMA-PLANICIE-COSTERA`

```text
NORMA_2016_IDENTIFIED_AS_IRMA_REFERENCE = true
NORMA_2016_FULL_TEXT_IN_PROJECT = false
```

`BL-024` debe concentrarse ahora en localizar el texto completo, reconstruir su procedencia y adjudicar qué efectos tiene sobre la política de fuentes ortográficas contemporáneas.

El Alfabeto Popular de 1956 queda como antecedente histórico fundamental; Emiliano ya dispone de una copia descargada, todavía no incorporada al repositorio.

## 7. Negación `qui` / `qué`

La cuestión de equivalencia queda cerrada mediante:

- `SRC-NEGACION-QUI-QUE-ATESTACIONES-2026-09-03`
- `HALL-0019`
- `DEC-NEGACION-QUI-QUE-EQUIVALENTES`

```text
QUI_QUE_NEGATION_EQUIVALENT = true
MARK_OTHER_FORM_AS_INCORRECT_BY_VARIANT_ALONE = false
DIALECT_DISTRIBUTION = OPEN
HISTORICAL_RELATION = OPEN
PROJECT_EDITORIAL_DEFAULT = NOT_DECIDED_HERE
```

## 8. Nuevas atestaciones de Irma aún no promovidas a reglas

- `HALL-0013`: forma léxica vs trato social / jerarquía — pendiente de precisar y validar.
- `HALL-0014`: distribución de `Lia` y `dxe` por género — pendiente de corroboración y análisis funcional.
- `HALL-0015`: `bitaagu'` / `biseegu'` entre Séptima y Octava Sección — pendiente de corroboración local.
- `HALL-0016`: `ñaa` actual vs `la'dxi` arcaico para campo de cultivo — pendiente de contraste.
- `HALL-0017`: asociaciones etimológicas de `ñaa` y `la'dxi` — no tratarlas como etimología establecida todavía.
- `HALL-0018`: `bichuga le` atribuido a Mariano Martínez como neologismo para teléfono — pendiente de fuente primaria y uso.

## 9. Variedad

La investigación sobre El Espinal y otras variedades puede continuar, pero no cambia el baseline activo:

```text
CURRENT_BASELINE = JUCHITAN
ESPINAL_RESEARCH = ALLOWED
MULTIVARIETAL_MERGE = false
```

## 10. Bibliografía SIL/ILV

Se registró:

- `SRC-SIL-MEXICO-CATALOGO-ZAPOTECO-ISTMO-2026-09-03`
- `informes/SIL_ISTHMUS_ZAPOTEC_BIBLIOGRAPHY_SCAN_v0_1.md`

La prioridad es deduplicar contra `BIB###` y leer fuentes por función; el catálogo no confiere autoridad uniforme a todas las publicaciones.

## 11. Estado del dispositivo

Ninguna atestación lingüística pendiente de Irma se transfiere automáticamente al dispositivo.

Las decisiones ya adoptadas pueden ser consumidas sólo cuando exista un estado de conocimiento aprobado y se registre el `KNOWLEDGE_SOURCE_COMMIT` correspondiente.

## 12. Resumen

```text
IRMA_WORD_LIST_CAPTURED = true
BEGINNER_SCOPE_ADOPTED = true
LISTENING_ONLY_ACTIVE_SCOPE = true
JUCHITAN_BASELINE_REAFFIRMED = true
LITERACY_ACTIVE_SCOPE = false
MEMORIZATION_JUSTIFICATION = OPEN_HIGH_PRIORITY
NORMA_2016_IDENTIFIED = true
NORMA_2016_FULL_TEXT_LOCATED = false
QUI_QUE_EQUIVALENCE_CLOSED = true
IRMA_OTHER_LEXICAL_NOTES = CAPTURED_NOT_GLOBAL_RULES
DEVICE_POST_IRMA_AUTOMATIC_PROMOTION = false
```
