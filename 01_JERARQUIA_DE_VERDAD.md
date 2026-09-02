# 01_JERARQUÍA_DE_VERDAD

Versión: 1.1
Estado: Vigente

---

# Propósito

Este documento establece cómo resolver conflictos entre fuentes, evidencias, documentos, decisiones y validaciones dentro del proyecto Voces de las Nubes.

No define metodología.

No define teoría.

No define procedimientos.

Su única función consiste en responder:

> ¿Qué debe considerarse verdadero cuando existen afirmaciones incompatibles?

Todas las decisiones del proyecto deberán respetar estas reglas.

---

# Principios generales

## P1. La realidad tiene prioridad sobre su representación.

Siempre que exista conflicto entre un registro directo y una representación posterior, prevalecerá el registro directo.

Ejemplos:

- audio sobre transcripción;
- fotografía sobre descripción;
- video sobre memoria.

---

## P2. Ninguna fuente posee autoridad absoluta.

Toda fuente tiene un ámbito de autoridad.

Las decisiones deberán respetar dicho ámbito.

---

## P3. Las contradicciones no deben ocultarse.

Cuando dos fuentes válidas entren en conflicto, el sistema documentará la contradicción antes de intentar resolverla.

Nunca se eliminará una evidencia únicamente para mantener coherencia documental.

---

## P4. Toda decisión debe ser trazable.

Toda afirmación incorporada al sistema debe poder reconstruir:

- su fuente;
- su justificación;
- su fecha;
- su alcance.

---

# Precedencia de autoridad

La autoridad depende del tipo de pregunta.

No existe una jerarquía universal.

---

## Lengua viva

Para cuestiones de uso contemporáneo prevalece:

1. evidencia oral registrada;
2. validación comunitaria pertinente;
3. consenso entre hablantes;
4. bibliografía;
5. interpretación del equipo;
6. hipótesis de IA.

---

## Metodología

Para cuestiones metodológicas prevalece:

1. decisiones vigentes del proyecto;
2. evidencia obtenida durante el proyecto;
3. literatura especializada;
4. propuestas aún no adoptadas.

---

## Aspectos técnicos

Para audio, software, edición y procesos técnicos prevalece:

1. pruebas realizadas;
2. especialistas responsables;
3. documentación técnica;
4. recomendaciones generales.

---

## Aspectos administrativos

Para compromisos institucionales prevalece:

1. acuerdos oficialmente adoptados;
2. requisitos institucionales;
3. decisiones operativas del proyecto.

---

# Precedencia documental

Cuando dos documentos del sistema entren en conflicto prevalecerá el documento de mayor jerarquía.

El orden es:

1. Arquitectura del conocimiento
2. Jerarquía de verdad
3. Reglas de actualización
4. Convenciones
5. Principios
6. Metodología
7. Procedimientos
8. Documentos temáticos
9. Productos del proyecto

Los documentos inferiores deberán actualizarse cuando contradigan a uno superior.

Nunca ocurrirá el proceso inverso.

---

# Autoridad de las entidades del Sistema de Conocimiento

La precedencia documental anterior no sustituye la función de las entidades definidas por `00_ARQUITECTURA_DEL_CONOCIMIENTO.md`.

Las entidades no forman una sola escala lineal. Su autoridad depende de su función:

- **SRC — Fuente:** conserva evidencia. No adopta por sí sola una política, principio o interpretación del proyecto.
- **HALL — Hallazgo:** registra una afirmación extraída o derivada de evidencia con estado y alcance. Puede obligar a revisar una decisión, pero no la reemplaza automáticamente.
- **SUP — Supuesto:** orienta trabajo bajo incertidumbre. No tiene autoridad normativa.
- **VAL — Validación:** tiene autoridad únicamente dentro del objeto, alcance y tipo de autoridad documentados.
- **TEO — Aplicación teórica:** registra una interpretación del proyecto sobre bibliografía. No sustituye evidencia ni decisión vigente.
- **DEC — Decisión:** es el mecanismo mediante el cual el proyecto adopta una elección. Una `DEC` marcada `vigente` o `vigente_con_reservas` gobierna las vistas, procedimientos y productos dentro de su alcance, siempre subordinada a los documentos constitucionales y a los principios válidos del proyecto.
- **PRIN — Principio:** orienta decisiones recurrentes de manera general. Sólo ejerce autoridad cuando cumple el esquema de principio y utiliza uno de los estados permitidos por la Arquitectura.
- **PROC — Procedimiento:** operacionaliza decisiones y principios; no puede reemplazarlos.
- **Vistas documentales** —por ejemplo `PEDAGOGIA.md`, `TEORIA.md`, `CORPUS.md`, `METODOLOGIA.md`— sintetizan el conocimiento vigente. No crean por proximidad una autoridad superior a las entidades que deben representar.

## Conflicto entre una DEC y una vista documental

Cuando una decisión vigente y una vista documental diverjan sobre la misma materia:

1. verificar que la decisión sea válida, esté vigente y pertenezca al mismo alcance;
2. si es así, actualizar la vista para representar la decisión;
3. si existe nueva evidencia que cuestiona la decisión, registrar primero el hallazgo o validación correspondiente y abrir revisión de la decisión;
4. no modificar silenciosamente la decisión desde la vista.

```text
VIEW != ADOPTION_MECHANISM
SOURCE != POLICY
FINDING != AUTOMATIC_DECISION
VALID_DECISION -> GOVERNS_VIEW_WITHIN_SCOPE
```

## Entidades inválidas o fuera de esquema

Un archivo cuyo identificador declare un tipo de entidad pero incumpla los estados o campos mínimos definidos por la Arquitectura **no adquiere autoridad normativa por su nombre, ubicación o proximidad**.

Debe marcarse para revisión y corregirse, reformularse, reclasificarse o retirarse antes de utilizarlo como autoridad.

---

# Sistemas y repositorios derivados

Los resultados de herramientas, sistemas o repositorios derivados pueden constituir evidencia sobre el comportamiento técnico de esos sistemas, detectar contradicciones o producir propuestas.

No pueden adoptar, promover o modificar por sí mismos el Sistema de Conocimiento.

La incorporación de cualquier propuesta derivada requiere el procedimiento de actualización de Voces de las Nubes y la autoridad pertinente.

Esta regla se desarrolla en `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO` y `03_REGLAS_DE_ACTUALIZACIÓN.md`.

---

# Precedencia temporal

Entre dos versiones de una misma decisión:

1. decisión vigente;
2. decisión vigente con reservas;
3. decisión histórica;
4. decisión reemplazada.

Las decisiones reemplazadas se conservan únicamente para reconstruir la evolución del proyecto.

Nunca deberán recuperarse automáticamente.

---

# Resolución de conflictos

Cuando aparezca una contradicción se seguirá este orden:

1. verificar si ambas afirmaciones pertenecen al mismo ámbito;
2. verificar si realmente existe contradicción;
3. verificar si se trata de variación;
4. verificar si una decisión posterior reemplaza a la anterior;
5. documentar la contradicción cuando no pueda resolverse.

Nunca se elegirá una respuesta únicamente por parecer más lógica.

---

# Casos particulares

## Audio vs escritura

Prevalece el audio validado.

---

## Hablante vs bibliografía

Para describir el uso actual de la lengua prevalece la validación comunitaria.

La bibliografía permanece como referencia histórica o teórica.

---

## Dos hablantes en desacuerdo

No existe precedencia automática.

Debe documentarse:

- alcance;
- contexto;
- posible variación;
- necesidad de nuevas validaciones.

---

## Teoría vs evidencia del proyecto

La teoría fundamenta.

La evidencia decide.

Cuando ambas entren en conflicto deberá documentarse la discrepancia y revisar la metodología.

---

## IA vs cualquier otra fuente

Las propuestas generadas por IA nunca constituyen evidencia.

Solo podrán incorporarse al sistema después de ser adoptadas explícitamente mediante los procedimientos del proyecto.

---

# Modificación de este documento

Este documento solo podrá modificarse cuando:

- una regla produzca conflictos sistemáticos;
- aparezca un nuevo tipo de fuente;
- cambie la filosofía epistemológica del proyecto.

Toda modificación deberá registrarse explícitamente.

No se modificará este documento para resolver un caso aislado.

Los casos particulares deberán resolverse mediante decisiones del proyecto, no modificando la constitución del sistema.

---

## Historial

### v1.1 — 2026-09-02

- Se corrige el hueco de precedencia que omitía `SRC`, `HALL`, `SUP`, `VAL`, `TEO` y `DEC`.
- Se establece que una `DEC` vigente gobierna las vistas dentro de su alcance, subordinada a la constitución y a principios válidos.
- Se establece que entidades fuera de esquema no adquieren autoridad por nombre o ubicación.
- Se formaliza que sistemas derivados pueden proponer, pero no adoptar ni modificar conocimiento.

### v1.0 — 2026-08-05

- Primera versión aprobada.
