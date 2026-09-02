# CIERRE DE LIMPIEZA DE AUTORIDAD PRE-IRMA — 2026-09-02

**Estado:** `PRE_IRMA_AUTHORITY_CLEANUP_SUFFICIENT / PHYSICAL_SPLIT_PENDING / IRMA_NOT_INGESTED / NON_NORMATIVE_REPORT`

## 1. Qué quedó resuelto

- Se congeló el estado post-migración / pre-Irma en la rama `checkpoint/pre-irma-post-migration-2026-09-02`, commit `e1f9f4ef2852b9e0453ef757a291816e1faa10e2`.
- `00_ARQUITECTURA_DEL_CONOCIMIENTO.md` v0.2 formaliza que los sistemas derivados pueden leer, analizar y proponer, pero no adoptar, promover ni escribir conocimiento.
- `01_JERARQUIA_DE_VERDAD.md` v1.1 define la función de autoridad de `SRC`, `HALL`, `SUP`, `VAL`, `TEO`, `DEC`, `PRIN`, procedimientos y vistas.
- `03_REGLAS_DE_ACTUALIZACIÓN.md` v1.2 define el retorno obligatorio desde resultados técnicos a la fuente original y al proceso de adjudicación de Voces de las Nubes.
- `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO` está vigente.
- Se separó la reentrada general (`INICIAR_AQUI_CHAT_NUEVO.md`) de la reentrada técnica (`dispositivo/REENTRY_TECNICO.md`).
- Se separó el backlog técnico del backlog estructural canónico.
- `PEDAGOGIA.md` y `CORPUS.md` fueron limpiados de formulaciones que deferían decisiones humanas a implementaciones técnicas.
- Los componentes técnicos de los antiguos BL-017/BL-022 fueron transferidos al backlog técnico; BL-022 canónico quedó como investigación sobre relevancia pedagógica.
- La auditoría post-limpieza confirmó **0 referencias de provenance desde `conocimiento/` hacia `dispositivo/`**.
- Los tres PRIN irregulares (`G`, `P`, `COMPETENCIA-COMUNICATIVA`) quedaron `en_revision` con autoridad normativa suspendida hasta adjudicación de tipo.
- `PRIN-INVESTIGACION-ABIERTA` conserva estado `vigente` y ahora cumple los campos mínimos de su tipo.
- `.github/CODEOWNERS` documenta ownership del Sistema de Conocimiento.
- El contrato `dispositivo/KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md` define la identidad `KNOWLEDGE_SOURCE_COMMIT` y el flujo de candidatos de regreso a Voces.
- `dispositivo/migracion/DEVICE_REPOSITORY_SEPARATION_PLAN_v1.md` define un corte físico no destructivo con replay/verificación previa.
- Los workflows temporales de limpieza fueron eliminados. Sólo permanece el workflow manual de replay histórico.

## 2. Qué deliberadamente NO se hizo

- no se modificó P1–P5;
- no se adoptó la tabla P propuesta por Claude;
- no se adjudicaron las capas BIB065 como pedagogía;
- no se incorporó ningún contenido de la reunión con Irma;
- no se creó `SRC-IRMA` sin evidencia;
- no se reclasificaron a la fuerza los tres PRIN irregulares;
- no se movió todavía el dispositivo a otro repositorio;
- no se retiró ningún artefacto técnico necesario para genealogía o replay.

## 3. Único bloqueo de infraestructura restante

La garantía física requerida —que futuros desarrolladores del dispositivo no puedan escribir en el Sistema de Conocimiento— todavía necesita:

1. crear el repositorio técnico separado;
2. verificar replay/tests en el destino;
3. configurar permisos/rulesets/protección de `main` en GitHub.

`CODEOWNERS` documenta ownership pero no sustituye esos controles. La integración disponible devolvió `403` al intentar inspeccionar protección de rama, por lo que no se declara esa protección como activa.

La tarea queda registrada como `DT-003` en `dispositivo/BACKLOG_TECNICO.md`.

## 4. Próximo evento de conocimiento

Cuando el material de la reunión con Irma Pineda esté disponible:

```text
EVIDENCIA_REUNION
-> SRC CRUDO
-> separar cita / nota contemporánea / memoria posterior / interpretación
-> identificar ámbitos de autoridad
-> extraer HALL después
-> detectar conflictos con decisiones vigentes
-> adjudicar
-> adoptar DEC si corresponde
-> actualizar vistas
-> publicar nuevo KNOWLEDGE_SOURCE_COMMIT
-> actualizar dispositivo después
```

La captura como `SRC` puede ocurrir antes de la separación física del repositorio técnico. La adjudicación sustantiva debe utilizar la arquitectura de autoridad ya reparada.

## 5. Veredicto

La limpieza arquitectónica que podía hacerse sin contenido nuevo de Irma ni configuración manual de GitHub está suficientemente cerrada.

```text
CAN_INGEST_IRMA_AS_RAW_SOURCE = true
CAN_ADJUDICATE_IRMA_WITH_REPAIRED_HIERARCHY = true
CAN_CONTINUE_KNOWLEDGE_RESEARCH = true
PHYSICAL_DEVICE_PERMISSION_BOUNDARY_COMPLETE = false
P_SCALE_CLOSED = false
IRMA_DECISIONS_IMPLEMENTED = false
```
