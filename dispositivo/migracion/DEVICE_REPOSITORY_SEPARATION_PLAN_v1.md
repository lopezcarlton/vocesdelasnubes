# DEVICE_REPOSITORY_SEPARATION_PLAN_v1

**Estado:** `PLANNED / NON_DESTRUCTIVE / NOT_YET_EXECUTED`  
**Fecha:** 2026-09-02

## Objetivo

Separar físicamente el dispositivo del repositorio canónico de Voces de las Nubes sin perder genealogía, hashes, artefactos binarios, reproducibilidad del replay ni trazabilidad entre conocimiento aprobado e implementación.

La separación implementará la decisión `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO`; no la crea.

## Baselines que deben preservarse

### Pre-Irma / post-migración

```text
repository = lopezcarlton/vocesdelasnubes
branch = checkpoint/pre-irma-post-migration-2026-09-02
commit = e1f9f4ef2852b9e0453ef757a291816e1faa10e2
```

Este baseline permite reconstruir el dispositivo tal como quedó inmediatamente después de la consolidación histórica y antes de la limpieza de autoridad.

### Estado técnico reproducible

Antes del corte, el repositorio técnico nuevo debe reproducir al menos el cierre ya demostrado para runtime v0.2.15.3:

- clausura recursiva de imports esperada;
- dependencias directas exactas;
- replay histórico `exit 0`;
- hashes semánticos históricos coincidentes;
- `SUMMARY` y `METRICS` deterministas exactos;
- 38/38 pruebas históricas;
- `COR001 = ANALYSIS_TARGET_ONLY`.

## Fase 0 — Preparación ya realizada

- frontera constitucional formalizada;
- `DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO` vigente;
- `CODEOWNERS` documenta ownership del Sistema de Conocimiento;
- reentrada general y reentrada técnica separadas;
- backlog técnico separado;
- cero referencias `provenance` desde `conocimiento/` hacia `dispositivo/` en la auditoría post-limpieza;
- contrato de consumo definido en `dispositivo/KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md`.

## Fase 1 — Crear repositorio técnico

Crear un repositorio técnico separado bajo el control de Emiliano. El nombre no se fija en este plan para no convertir una decisión de nomenclatura aún no tomada en arquitectura.

El repositorio nuevo debe recibir el árbol activo de `dispositivo/` preservando, en la medida posible, historia relevante de Git. Si la extracción de historia por subdirectorio altera hashes de commits, conservar además referencias al repo/commit de origen.

Debe contener como mínimo:

- `REENTRY_TECNICO.md` adaptado a la nueva raíz;
- `README.md` técnico;
- Analyzer / Corrector / Tutor / Generator recuperados;
- core experimental;
- runtime y bases necesarias;
- tests;
- migración/manifiesto/estado ejecutable;
- `BACKLOG_TECNICO.md`;
- `KNOWLEDGE_CONSUMPTION_CONTRACT_v1.md`;
- workflow manual del replay histórico.

## Fase 2 — Vincular conocimiento aprobado

El repositorio técnico no debe copiar silenciosamente el estado canónico de Voces como una segunda autoridad.

Cada versión técnica deberá registrar:

```text
KNOWLEDGE_SOURCE_REPOSITORY = lopezcarlton/vocesdelasnubes
KNOWLEDGE_SOURCE_COMMIT = <commit aprobado consumido>
```

Puede existir un snapshot técnico derivado por razones de ejecución, pero deberá identificarse como copia/compilación derivada y conservar la procedencia al commit canónico.

## Fase 3 — Verificación antes del corte

En el repositorio técnico separado:

1. verificar presencia e identidad de artefactos críticos;
2. ejecutar la prueba manual de replay;
3. ejecutar la cadena de 38 pruebas;
4. comprobar rutas del reentry técnico;
5. comprobar que ninguna instrucción técnica conceda autoridad de escritura sobre Voces;
6. producir un `SEPARATION_VERIFICATION` con los commits de origen y destino.

**No retirar el dispositivo activo de Voces hasta que esta fase pase.**

## Fase 4 — Cambiar Voces a modo de referencia

Después de la verificación:

- retirar de `main` la copia activa del dispositivo o sustituirla por una referencia/archivo mínimo según convenga;
- conservar en Git la historia previa y el branch pre-Irma;
- dejar en Voces únicamente la interfaz de autoridad necesaria para indicar dónde vive el sistema derivado;
- actualizar `README.md`, `INICIAR_AQUI_CHAT_NUEVO.md` y documentos constitucionales sólo si la ubicación física exige ajustar enlaces;
- no trasladar documentos técnicos a `conocimiento/` para “no perderlos”.

## Fase 5 — Permisos

Objetivo de permisos:

```text
vocesdelasnubes:
  knowledge curators = write
  device developers = read only by default

technical device repository:
  approved device developers = write
```

`CODEOWNERS` por sí solo no garantiza esta separación. Deben configurarse permisos, protección de `main` o rulesets adecuados en GitHub.

## Criterio de éxito

La separación se considera terminada cuando:

```text
DEVICE_REPO_REPLAY = PASS
DEVICE_REPO_TECHNICAL_TESTS = PASS
KNOWLEDGE_SOURCE_COMMIT = EXPLICIT
CANONICAL_PROVENANCE_TO_DEVICE = 0
DEVICE_DEVELOPER_CANONICAL_WRITE_BY_DEFAULT = false
VOCES_REENTRY_DOES_NOT_REQUIRE_DEVICE_REPO = true
DEVICE_REENTRY_CAN_RESOLVE_APPROVED_KNOWLEDGE = true
```

## Lo que este plan no autoriza

- no cambia P1–P5;
- no adjudica BIB065;
- no incorpora la reunión con Irma;
- no convierte el runtime histórico en arquitectura futura;
- no permite borrar genealogía sólo para simplificar el repositorio;
- no autoriza un corte físico sin replay/verificación previa.
