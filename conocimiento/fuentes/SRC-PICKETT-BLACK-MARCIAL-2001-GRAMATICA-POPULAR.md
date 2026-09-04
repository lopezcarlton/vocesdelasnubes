# SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR

```yaml
id: SRC-PICKETT-BLACK-MARCIAL-2001-GRAMATICA-POPULAR
tipo: fuente_bibliografica
titulo: "Gramática popular del zapoteco del Istmo"
autor_o_participantes:
  - Velma B. Pickett
  - Cheryl A. Black
  - Vicente Marcial Cerqueda
fecha: 2001
bib_id: BIB004
edicion: "Segunda edición electrónica"
ubicacion: "https://mexico.sil.org/es/resources/archives/35304"
archivo_publicado: "Imagezai_gramatica_ed2.pdf"
descripcion: >
  Descripción gramatical de la variedad de zapoteco del Istmo hablada en el distrito
  de Juchitán. Es la fuente bibliográfica principal de numerosas reglas que fueron
  compiladas posteriormente en el JUCHITAN_LINGUISTIC_CORE técnico. Voces debe volver
  a esta obra para adjudicar esas afirmaciones; el core no sustituye la fuente.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: parcial_con_backfill_prioritario_2026-09-04
```

## Identidad y alcance

- Editoriales/instituciones: Centro de Investigación y Desarrollo Binnizá A.C.; Instituto Lingüístico de Verano A.C.
- Extensión: x, 125 páginas.
- Variedad declarada por la ficha editorial: Juchitán, Oaxaca.
- La ficha oficial del SIL/ILV ofrece el archivo electrónico de la segunda edición.

## Backfill semántico confirmado — 2026-09-04

La migración había preservado la identidad de la fuente y parte de sus derivados técnicos, pero no había promovido a Voces varios hechos ya estudiados. Se reabrieron los pasajes originales y quedaron formalizados al menos los siguientes puntos:

### Segunda persona singular

§5.1 declara explícitamente que **no hay diferencia entre `usted` y `tú`**. §5.1.1 registra `lii` con el significado `tú, usted`.

→ `HALL-0066`.

### Sistema tonal

§3.4 trabaja tres categorías de tono en la descripción operativa de la Gramática/Vocabulario:

- `b` = tono bajo;
- `al` = tono alto;
- `a` = tono ascendente.

La escritura ordinaria no necesita marcarlos, pero el aprendiz debe aprenderlos.

→ `HALL-0067`, relacionado con `HALL-0054`.

### `xh-/x-` ante consonante

La morfología posesiva documenta `xh-` ante vocal y `x-` ante consonante, con alternancias condicionadas de la raíz. Esta información ya había sido compilada técnicamente en `JLC-POS-003` y reglas relacionadas, pero faltaba promover su condición de conocimiento canónico de Voces.

→ `HALL-0068`.

### `r` débil / `r` fuerte

La Gramática caracteriza la `r` fuerte como **muy rara en palabras nativas**, más frecuente en préstamos del español, y llama a la `r` débil **lo normal**. Algunas grafías de préstamos siguen la convención española (`r` inicial/final, `rr` intervocálica).

→ `HALL-0069`.

### Sistema verbal y aspectos — bloque dirigido §7.2–7.3

Se reabrieron directamente los pasajes impresos 51–61 (PDF pp. 60–70) para verificar un bloque de alto valor señalado por los índices históricos. La adjudicación no usa el JLC como autoridad.

Hallazgos promovidos:

- §7.2 distingue los marcadores principalmente como aspectos/tipos de acción y señala que sólo el futuro puede definirse como tiempo → `HALL-0077`;
- §7.2.4 define el perfecto `hua-` como acción repetida a lo largo del tiempo, con restricción de experiencia previa y uso negativo de intervalo → `HALL-0078`;
- §7.2.3 documenta `cana-` como progresivo ambulativo, con movimiento durante la acción → `HALL-0079`;
- §7.3 organiza variantes aspectuales en Juego 1 y Juego 2, subdividiendo Juego 1 en 1A/1B/1C → `HALL-0080`;
- §7.3 afirma explícitamente que el potencial de Juego 1C no lleva prefijo y el cuadro 26 presenta `sa'` → `HALL-0081`;
- §7.3 formula sólo como posibilidad el análisis de `u` de Juego 2 como vocal temática asociada al causativo → `HALL-0082`.

Límites conservados:

```text
GP_GAME_SYSTEM != PBK2016_A_B_C_D_BY_DEFAULT
SOURCE_HYPOTHESIS != CERTAIN_RULE
SPANISH_TENSE != DIDXAZA_ASPECT_BY_DEFAULT
```

## Relación con el dispositivo

`dispositivo/core/JUCHITAN_LINGUISTIC_CORE_v0_27.md`, registries de persona/posesión, paradigmas y otras compilaciones técnicas contienen conocimiento derivado de esta obra.

```text
JUCHITAN_LINGUISTIC_CORE != SOURCE
PERSON_POSSESSION_REGISTRY != SOURCE
GRAMATICA_POPULAR = SOURCE
```

Las compilaciones técnicas pueden servir para localizar temas o ejemplos; cualquier afirmación que se promueva o revise en Voces debe poder justificarse en la Gramática Popular o en evidencia posterior de autoridad pertinente.

## Deuda restante

El backfill anterior corrige los huecos detectados durante la lectura del Alfabeto de 1956 y el primer bloque verbal/aspectual prioritario, pero **no equivale a una reingesta semántica exhaustiva de toda la Gramática Popular**. La obra debe seguir revisándose por bloques contra las coordenadas de ingesta histórica para asegurar que todo conocimiento reutilizable haya sido promovido a Voces con provenance y sin depender del core derivado.
