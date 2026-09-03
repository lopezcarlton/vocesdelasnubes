# EVIDENCIA LOCAL DIDXAZÁ PARA SEGMENTACIÓN ESCOLAR — v0.1

**Fecha:** 2026-09-02  
**Estado:** `RESEARCH_NOTE / NON_NORMATIVE`

Complementa `AGE_SEGMENTATION_RESEARCH_MAP_v0_1.md` con estudios directamente realizados con niñas y niños bilingües zapoteco-español del Istmo.

## 1. Coronado Cisneros — segmentación gráfica

`SRC-CORONADO-2020-SEGMENTACION-DIIDXAZA-NINOS`

Trabajó con estudiantes bilingües de quinto y sexto grado de una primaria bilingüe de Rancho El Llano, San Blas Atempa, alfabetizados inicialmente en español y enfrentados a escritura en zapoteco.

**Implicación para BL-023:** dentro de un mismo tramo escolar puede haber estudiantes que ya poseen competencia oral en la lengua pero no han desarrollado convenciones escritas en didxazá. Ese perfil no debe confundirse con un estudiante L2 que comienza la lengua desde cero.

## 2. De Anda Trejo — representación escrita de sonidos distintivos

`SRC-DE-ANDA-2023-ESCRITURA-SONIDOS-DIIDXAZA-NINOS`

Trabajó con 27 niños bilingües zapoteco-español de 10–12 años de Rancho El Llano mediante escritura espontánea, reconocimiento gráfico, entrevistas y perfil de dominancia bilingüe.

El resumen institucional reporta procesos interlingüísticos y que la dominancia lingüística no fue la única variable que influyó en las decisiones de escritura.

**Implicación para BL-023:** edad, oralidad, dominancia bilingüe y alfabetización son dimensiones relacionadas pero no intercambiables.

## 3. Evidencia adicional por estudiar

El capítulo Cardona & Vicente (2025) cita una tesis de maestría de 2025 de Aguilar sobre la escritura de vocales glotalizadas/rearticuladas por niños bilingües. En esta pasada no se localizó todavía un registro institucional estable del manuscrito completo, por lo que no se crea aún una entidad `SRC` independiente.

El mismo capítulo reporta que esos estudiantes identifican la constricción de las vocales rearticuladas de San Blas Atempa y evalúan alternativas gráficas, dato particularmente relevante para estudiar cómo variedad y alfabetización interactúan en la escuela. Debe volver a la tesis original antes de cualquier promoción pedagógica o ortográfica.

## 4. Resultado para la arquitectura de públicos

La matriz de investigación debe incorporar al menos tres dimensiones separadas:

```text
DEVELOPMENT_SCHOOL_STAGE
ORAL_LANGUAGE_PROFILE
LITERACY_PROFILE
```

Y, cuando corresponda:

```text
VARIETY_LOCALITY_PROFILE
```

Ejemplos de perfiles que pueden coexistir en un mismo grado:

- hablante activo + alfabetizado sólo en español;
- comprensor pasivo + producción limitada;
- exposición familiar parcial + L2 escolar;
- estudiante con poca exposición a didxazá;
- hablante de una localidad cuya realización no coincide exactamente con la convención juchiteca enseñada.

Por tanto:

```text
SAME_GRADE != SAME_PEDAGOGICAL_STARTING_POINT
ORAL_COMPETENCE != LITERACY_COMPETENCE
VARIETY_DIFFERENCE != LEARNER_ERROR
```

## 5. Consecuencia metodológica provisional

Antes de diseñar “material para quinto de primaria” o “material para secundaria”, conviene caracterizar la composición lingüística real del grupo. Una versión escolar puede necesitar rutas o actividades diferenciadas incluso dentro del mismo salón.

Esto no significa crear materiales individualizados para cada estudiante; significa evitar que la edad se convierta en sustituto de información lingüística que puede obtenerse con un diagnóstico breve y con conocimiento del docente.
