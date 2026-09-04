# SRC-PICKETT-VILLALOBOS-MARLETT-2009-ZAPOTECO-ISTMO-JUCHITAN

```yaml
id: SRC-PICKETT-VILLALOBOS-MARLETT-2009-ZAPOTECO-ISTMO-JUCHITAN
tipo: fuente_bibliografica
bib_id: BIB016
titulo: "Zapoteco del Istmo (Juchitán)"
autor_o_participantes:
  - Velma B. Pickett
  - María Villalobos Villalobos
  - Stephen A. Marlett
fecha: 2009
ubicacion: "https://lengamer.org/publicaciones/trabajos/Zapoteco_del_istmo_afi_2009a.pdf"
ubicacion_archivo_sil: "https://mexico.sil.org/es/resources/archives/3725"
descripcion: >
  Ilustración fonética en español de la variedad de Juchitán, con grabaciones de María
  Villalobos Villalobos. Describe consonantes, vocales, tono, acento y un pasaje grabado.
  Está relacionada editorialmente con la publicación inglesa de JIPA de 2010 registrada
  como BIB061, pero ambas identidades bibliográficas se conservan separadas.
nivel_de_fuente: primaria
estado_de_acceso: disponible_en_web
estado_de_ingesta: semantic_backfill_p0_sufficient_2026-09-04
```

## Evidencia de identidad

La hoja bibliográfica maestra registra esta obra como `BIB016`. La ficha del SIL identifica la ilustración fonética en español y sus grabaciones. La publicación JIPA 2010 se conserva como `BIB061`.

```text
BIB016 = VERSION_ESPANOL_ILUSTRACION_FONETICA
BIB061 = JIPA_2010_ENGLISH_PUBLICATION
BIB016 != BIB061
```

## Memoria persistente de lectura — backfill P0 2026-09-04

La revisión dirigida de la ilustración y de su publicación JIPA promovió a Voces:

- fortis/lenis como oposición multirrasgo: duración consonántica contextual, sonoridad de obstruyentes y duración de vocal precedente → `HALL-0141`;
- contraste trill/tap inicial real pero léxicamente muy escaso → `HALL-0142`;
- cinco cualidades vocálicas con tres tipos de fonación en sílaba tónica: modal, cortada y laringizada → `HALL-0143`;
- tres tonos fonémicos usados en la transcripción vs propuesta tentativa de cinco melodías tonales para raíces nominales → `HALL-0144`;
- acento como capa distinta que interactúa con duración, tono y fonación, evita prefijos/enclíticos y puede provocar reducción fonética al perderse → `HALL-0145`;
- alofonía contextual de lenis, asimilación nasal y centralización de vocales átonas → `HALL-0146`;
- inventario segmental juchiteco documentado directamente en los cuadros → `HALL-0148`;
- separación explícita entre análisis fonológico, superficie fonética y ortografía popular → `HALL-0149`.

La versión española conserva una observación ortográfica particularmente útil: la recomendación de `l.l` para la lateral fuerte en 1956 no se siguió de manera general en la práctica. Esto no autoriza al corrector a escoger una grafía contemporánea por sí solo; muestra que inventario fonémico y convención gráfica son capas distintas.

## Límites

```text
PHONEME != ALLOPHONE != ORTHOGRAPHIC_GRAPHEME
FORTIS_LENIS != VOICE_ONLY
THREE_PHONEMIC_TONES != FIVE_ROOT_MELODIES
FIVE_ROOT_MELODIES = TENTATIVE_ANALYSIS
PHONETIC_GLOTTAL_CLOSURE != AUTOMATIC_CODA_SEGMENT
CONTEXTUAL_PRONUNCIATION != SPELLING_CHANGE
```

La fuente describe una variedad típica de Juchitán y reconoce variación fonética entre localidades próximas. No extrapolar automáticamente su inventario o sus realizaciones a todas las variedades del Istmo.

## Relación con BIB061 y corrigendum

Para formulaciones editoriales definitivas y datos de JIPA se conserva `SRC-PICKETT-VILLALOBOS-MARLETT-2010-PHONETICS`. El corrigendum de 2011 corrige/completa la lista de ejemplos consonánticos de la página 367 de la publicación de 2010 → `HALL-0147`.

## Estado

```text
PVM2009_P0_BACKFILL = SUFFICIENT
EXHAUSTIVE_AUDIO_TOKEN_INGESTA = false
REOPEN_FOR = TARGETED_PHONETIC_QUERY | EXACT_EXAMPLE | ACOUSTIC_IMPLEMENTATION
```
