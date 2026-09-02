# ISOLATED_REPLAY_VERIFICATION_v0_2_15_3 — 2026-09-02

**Proyecto:** Voces de las Nubes  
**Estado:** `TECHNICAL_REPRODUCIBILITY_PASS / NON_CANONICAL / NON_LINGUISTIC_AUTHORITY`

## 1. Alcance

Esta verificación reproduce el runner histórico `run_cor001_replay_v0_2_15_3.py` en un checkout limpio de GitHub Actions y compara las dependencias directas y los outputs deterministas contra `RELEASE_FILE_MANIFEST_v0_2_15_3.json`.

No es una evaluación lingüística de COR001 y no modifica su rol:

```text
COR001 = ANALYSIS_TARGET_ONLY
COR001 != GOLD_STANDARD
COR001 != BENCHMARK
COR001 != REGRESSION_AUTHORITY
COR001 != RULE_DISCOVERY_SOURCE
```

## 2. Ejecución de cierre

GitHub Actions:

```text
workflow = replay-v0-2-15-3-reproducibility
run_id = 33680809372
job_id = 100416640022
head_sha = feb0a994f877f22f680a849a5cdda605208348f6
runner = Ubuntu 24.04 / Python 3.12.3
result = SUCCESS
```

Criterio del replay:

```text
runner_exit_0
+ exact_direct_dependencies
+ exact_deterministic_outputs
```

Resultado:

```text
STATUS = PASS
DIRECT_DEPENDENCIES_OK = true
DETERMINISTIC_OUTPUTS_OK = true
```

## 3. Discrepancia de transporte detectada y reparada

La primera ejecución aislada encontró una única discrepancia entre una dependencia migrada y el hash del release:

```text
PERSON_POSSESSION_EXACT_REGISTRY_v0_2_15_2.csv
migrated SHA256 = 4eb026a6e6b713dec9eeee804a376d3e75884addbfb10096e3fc881adbc85ac7
release SHA256  = 3f1e955a285c2ce9c66d3953def6b41fd993d6b8dd81567c5f95a28281d20bdb
```

El diagnóstico exhaustivo de representación demostró que el contenido tabular era el mismo y que la diferencia provenía únicamente de terminadores de línea:

```text
migrated representation = UTF-8 BOM + LF + final newline
release representation  = UTF-8 BOM + CRLF + final newline
```

La variante `UTF-8 BOM + CRLF + final newline` reprodujo exactamente el SHA-256 histórico del release. No se alteró ninguna celda ni decisión lingüística.

La representación byte-exacta se restauró y se publicó en `main` mediante:

```text
commit = 44e8b04
message = restore exact person-possession registry bytes v0.2.15.2
verified SHA256 = 3f1e955a285c2ce9c66d3953def6b41fd993d6b8dd81567c5f95a28281d20bdb
```

## 4. Outputs reproducidos

Los outputs deterministas del replay coinciden byte por byte con el release histórico:

```text
COR001_REPLAY_METRICS_v0_2_15_3.json
SHA256 = d7184c94af1eff07b54c63ab3da5e83f81e037342265ba8e20a74dbf0dd0bd22
EXACT_MATCH = true

COR001_REPLAY_SUMMARY_v0_2_15_3.csv
SHA256 = ce4b799d9cb800eea9e220a3166fcf532246ac9e92f6ec000a36f7f9e0fb06b4
EXACT_MATCH = true
```

El `COR001_REPLAY_DETAILED_v0_2_15_3.jsonl` no coincide byte por byte porque contiene identificadores UUID efímeros generados en cada ejecución. Esa diferencia no se usa como criterio de fallo. El runner produjo los siguientes hashes semánticos en la ejecución de cierre:

```text
details = eb68bb9a4a3d21e59fa889c5d214f6a7d108c54df228741a2920bec14f5d3d46
metrics = 336db0939a8712b101766f28ebdd841936d8c539736820510c881cf1dbb47dec
summary = adf75622ec8062b74826535a39ab50ced989e3390bf5e88ad19738d56bb13fa5
```

## 5. Conclusión técnica

El subconjunto materializado del runtime v0.2.15.3 es suficiente para regenerar el replay histórico aislado y reproducir exactamente sus outputs deterministas relevantes.

Esto permite cerrar el pendiente de **reproducibilidad técnica del replay v0.2.15.3**.

No demuestra:

- que COR001 sea lingüísticamente correcto;
- que COR001 pueda servir como benchmark o regresión;
- que las salidas del runtime constituyan reglas;
- que los 75 payloads del release estén migrados;
- que el runtime histórico deba convertirse en la arquitectura futura del proyecto.

El workflow debe conservarse únicamente como herramienta manual de reproducibilidad histórica, no como gate automático sobre cambios futuros.
