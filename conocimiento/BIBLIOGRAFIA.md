# BIBLIOGRAFIA

**Proyecto:** Voces de las Nubes  
**Versión:** 1.4  
**Estado:** Borrador consolidado  
**Fecha:** 2026-09-03  

---

# 1. Organización

La bibliografía se administra en una hoja de cálculo con una entrada por fila y once columnas fijas:

1. ID
2. Tipo
3. Autor(es)
4. Año
5. Título
6. Editorial / Revista
7. Disponibilidad
8. Ubicación
9. Pertinencia
10. Notas
11. Revisado

El orden no debe modificarse.

---

# 2. Identificadores

## 2.1 Formato vigente

El formato vigente es `BIB` seguido de tres dígitos: `BIB001`, `BIB002`, `BIB003`.

Es el único formato válido. No existe un sistema paralelo en uso.

## 2.2 Relación con el formato anterior

Hasta junio de 2026 el proyecto utilizó el formato `B` seguido de tres dígitos.

En julio de 2026 el prefijo `BIB` **sustituyó** al prefijo `B` conservando el número de cada entrada. No son dos series distintas ni un rango heredado que convive con uno nuevo. Es la misma serie con otro prefijo.

La equivalencia es directa y sin excepciones:

B001 = BIB001
B016 = BIB016
B041 = BIB041

Toda referencia con formato `B###` encontrada en documentos antiguos, notas de trabajo o versiones previas de este documento debe leerse como `BIB###`. Designa la misma fuente.

El formato `B###` no debe usarse en documentos nuevos ni en referencias nuevas.

## 2.3 Crecimiento y estado vigente

La numeración es secuencial y continua. No existe límite superior ni rango reservado.

La **hoja de cálculo bibliográfica es el registro operativo de asignación de IDs**. La hoja maestra proporcionada por Emiliano el 2026-09-03 fue reconciliada con los `SRC-*` vigentes y sometida a una segunda pasada de consistencia.

Estado después de la sincronización:

```text
MASTER_BIB_RANGE = BIB001-BIB091
BIB_ID_GAPS = 0
BIB_ID_DUPLICATES = 0
```

Las nuevas asignaciones realizadas al sincronizar fueron:

- `BIB089` — Nancy Coronado Cisneros, tesis sobre segmentación gráfica;
- `BIB090` — INALI, *Logros 2016*;
- `BIB091` — catálogo SIL México de zapoteco del Istmo y publicaciones relacionadas.

Además, `SRC-DE-ANDA-2023-ESCRITURA-SONIDOS-DIIDXAZA-NINOS` quedó reconciliado con la entrada ya existente `BIB084`, correspondiente a la tesis fechada en 2022 y publicada en repositorio en 2023.

La presencia futura de una fuente `SRC-*` en el repositorio no autoriza inventar un `BIB###`: toda nueva asignación debe incorporarse a la hoja maestra.

## 2.4 Reglas permanentes

- Un identificador designa siempre la misma fuente.
- No se reutilizan identificadores eliminados.
- No se reasignan identificadores existentes.
- El cambio de prefijo no alteró ninguna asignación numérica.

---

# 3. Bibliografía fundamental

Las fuentes registradas como revisadas a profundidad incluyen:

- BIB001 — Manzo (2009).
- BIB002 — Rafael-Pérez et al. (2024).
- BIB003 — Vocabulario zapoteco del Istmo, ILV (5ª ed.).
- BIB004 — Pickett, Black y Marcial Cerqueda (2001).
- BIB016 — Pickett, Villalobos y Marlett (2009).
- BIB017 — Pérez Báez, Cata y Bueno Holle (2015).
- BIB018 — Proyectolaos / Cortamortaja (2018).
- BIB019 — ALAI (1978).
- BIB041 — Muntzel (1998).
- BIB044 — Swain (1985).
- BIB046 — Austin y Sallabank (2012).
- BIB052 — Calderón Corona (2021).
- BIB065 — Bueno Holle (2019).

El campo `Revisado` de la hoja de cálculo es la fuente operativa de verdad para el estado de lectura. Esta lista sólo destaca fuentes ya utilizadas intensivamente por el proyecto y no pretende sustituir la hoja.

---

# 4. Bibliografía metodológica y pedagógica

Los documentos de contexto mencionan como relevantes:

- Krashen.
- Swain.
- Sallabank.
- McCarty y Lee.

No se dispone en las fuentes de fichas completas suficientes para consolidar todas sus referencias exactas.

---

# 5. Bibliografía lingüística

Se identifican como centrales:

- Gramática popular del zapoteco del Istmo.
- Vocabulario zapoteco del Istmo.
- Descripción fonética de Pickett, Villalobos y Marlett.
- Pérez Báez, Cata y Bueno Holle.
- Bueno Holle 2019.
- Fuentes sobre ortografía, fonología, tonos y transcripción del Didxazá.

---

# 6. Bibliografía histórica y crítica

Se registra una línea de lectura crítica sobre:

- historia de la documentación;
- Instituto Lingüístico de Verano;
- alfabetos;
- políticas lingüísticas;
- ideología de la documentación;
- vitalidad y desplazamiento.

ALAI (1978) se utiliza para contextualizar críticamente la actividad del ILV.

---

# 7. Reglas de captura

## Autoría

- Formato `Apellido, Nombre`.
- Autores separados por punto y coma.
- Se listan todos los autores.
- Las instituciones se registran con nombre oficial y sigla.

## Año

- Cuatro dígitos cuando la fuente lo permite.
- Dos ediciones: formato compuesto cuando corresponda.
- Sin fecha: `s.f.` con explicación.

## Título

- Título completo.
- Sin comillas ni cursivas en la celda.
- Convenciones de mayúsculas según idioma.

## Disponibilidad

La hoja no usa un vocabulario cerrado. Valores frecuentes incluyen:

- Digital descargable.
- Digital, acceso abierto.
- Con suscripción.
- Físico.
- Por conseguir.

Cuando una fuente tiene más de una condición real de acceso, pueden combinarse descripciones mediante `/` o una nota suficientemente clara. No normalizar una condición específica a otra distinta sólo para forzar un catálogo corto de valores.

## Pertinencia

Valores habituales:

- Alta.
- Media.
- Baja.
- `(pendiente)` cuando todavía no existe evaluación suficiente.

## Revisado

La hoja maestra utiliza actualmente tres estados:

- `si`: leído y evaluado con profundidad suficiente para considerarlo revisado;
- `no`: registrado pero pendiente de revisión suficiente;
- `superficialmente`: identidad y relevancia comprobadas sin lectura integral suficiente para marcarlo como revisado a profundidad.

El literal `si` se conserva sin acento porque es el valor operativo de la hoja; semánticamente equivale a “sí”.

---

# 8. Criterios de deduplicación

Antes de agregar una entrada se verifica la identidad bibliográfica completa: autoría, año, título, obra contenedora/edición y naturaleza del objeto.

Las ediciones, traducciones o publicaciones relacionadas pueden conservar IDs separados cuando son objetos bibliográficos distintos.

Objetos bibliográficos relacionados pero distintos conservan IDs separados. En particular:

```text
BIB016 = Pickett, Villalobos y Marlett, versión española/ilustración fonética de 2009
BIB061 = Pickett, Villalobos y Marlett, publicación JIPA de 2010
BIB016 != BIB061
```

Un título idéntico tampoco prueba duplicidad. La segunda pasada confirmó títulos repetidos legítimos —por ejemplo, *Orthography development* y *Clases verbales en el zapoteco del Istmo*— correspondientes a autores/años u objetos distintos. No fusionar entradas sólo por coincidencia exacta de título.

---

# 9. Flujo de trabajo

1. Se proporciona la referencia o fuente.
2. Se extraen los datos.
3. Se genera una ficha.
4. Emiliano revisa y corrige.
5. La ficha aprobada se incorpora a la hoja.
6. Para lotes, puede generarse un archivo XLSX compatible.

---

# 10. Estado de revisión

La sección 3 es una selección de fuentes ya trabajadas intensivamente; no debe utilizarse para inferir el número total actual de fuentes.

La asignación completa de IDs se administra en la hoja maestra, actualmente sincronizada hasta `BIB091`. El campo `Revisado` de cada fila sigue siendo la fuente de verdad para el estado de lectura.

---

# 11. Limitaciones del documento

Este Markdown no sustituye la hoja maestra y no intenta reproducir sus 91 filas.

No documenta exhaustivamente:

- referencias completas de cada entrada;
- ubicación exacta de todos los archivos locales;
- DOI, ISBN y URL de cada fuente;
- historial completo de cambios de cada fila.

Esos datos permanecen en la hoja bibliográfica y, cuando una fuente adquiere función explícita dentro del Sistema de Conocimiento, en su `SRC-*` correspondiente.

---

# 12. Cambio de sistema de identificadores (julio 2026)

A partir de julio 2026, el proyecto cambió el sistema de identificadores de fuentes.

## 12.1 Sistemas en uso

El sistema de identificadores está definido en la sección 2 de este documento.

En julio de 2026 el prefijo `B` fue sustituido por `BIB` conservando la numeración. Esta sección conserva la tabla de equivalencias elaborada durante ese cambio, con valor histórico.

## 12.2 Remapeo de fuentes revisadas en mayo 2026

Las siete fuentes documentadas como revisadas a profundidad en mayo de 2026 tienen ahora los siguientes identificadores en el sistema vigente:

| Anterior | Vigente | Referencia |
|----------|---------|-----------|
| B001 | BIB001 | Manzo (2009) |
| B002 | BIB002 | Rafael-Pérez et al. (2024) — Aplicación web preexistente para Didxazá |
| B003 | BIB003 | Vocabulario zapoteco del Istmo (revisión parcial en mayo) |
| B017 | BIB017 | Pérez Báez, Cata y Bueno Holle (2015) |
| B018 | BIB018 | Proyectolaos / Cortamortaja (2018) |
| B019 | BIB019 | ALAI (1978) |
| B041 | BIB041 | Muntzel (1998) |

**Nota:** BIB002 (Rafael-Pérez et al. 2024) es un antecedente conocido del proyecto que requiere análisis de diferenciadores y cobertura para evitar que sea usada como argumento en contra del proyecto en presentaciones futuras.

## 12.3 Nuevas entradas

Las entradas nuevas continúan la numeración secuencial vigente conforme a la sección 2.3.

**Nota de corrección:** una versión anterior indicó incorrectamente que las fuentes incorporadas después de julio de 2026 usarían el formato `BIB020` en adelante. El rango `BIB020`–`BIB041` ya correspondía a fuentes anteriores al cambio de prefijo. No existe rango reservado para entradas nuevas.

## 12.4 Hoja de cálculo

La hoja de cálculo de administración bibliográfica utiliza los identificadores vigentes en todas sus entradas.

Los identificadores con formato `B###` que aparezcan en documentos o notas anteriores al cambio de prefijo corresponden a la misma fuente que el identificador `BIB###` con igual número.

---

# 13. Reconciliación del registro bibliográfico

`BL-026` quedó cerrado el 2026-09-03 usando la hoja maestra proporcionada por Emiliano y los `SRC-*` actualmente materializados en `conocimiento/fuentes/`.

Se confirmó, entre otras, la identidad de:

- `BIB003` — Vocabulario zapoteco del Istmo;
- `BIB004` — Gramática Popular;
- `BIB015` — Alfabeto Popular de 1956;
- `BIB016` — Pickett, Villalobos y Marlett 2009;
- `BIB017` — Pérez Báez, Cata y Bueno Holle 2015;
- `BIB054` — Dictionaria;
- `BIB058` — Norma de escritura de 2016;
- `BIB059` — Pérez Báez y Kaufman 2016;
- `BIB060` — Pérez Báez 2015;
- `BIB061` — Pickett, Villalobos y Marlett 2010;
- `BIB063` — Cardona 2020;
- `BIB064` — Cardona y Vicente 2025;
- `BIB065` — Bueno Holle 2019;
- `BIB084` — De Anda 2022;
- `BIB089` — Coronado 2019;
- `BIB090` — INALI Logros 2016;
- `BIB091` — catálogo SIL México.

La segunda pasada confirmó además que la serie `BIB001–BIB091` permanece continua y sin IDs duplicados.

La regla permanente queda:

```text
SRC_ID = VALID_SOURCE_ID
BIB_ID = ASSIGN_ONLY_FROM_MASTER_SPREADSHEET
NO_GUESSED_BIB_IDS = true
```
