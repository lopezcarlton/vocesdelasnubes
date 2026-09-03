# AUDITORÍA DE ESQUEMAS DE ENTIDADES — POST-IRMA — 2026-09-02

**Estado:** `AUDIT_REPORT / NON_NORMATIVE`

- Entidades auditadas: **28**
- Entidades nuevas post-Irma con incumplimiento tras normalización: **0**
- Deuda histórica/preexistente detectada: **7**

## Entidades nuevas post-Irma

- **PASS:** todos los SRC/HALL/DEC creados en esta fase cumplen campos mínimos y vocabularios controlados auditados.

## Deuda histórica/preexistente

- `conocimiento/hallazgos/HALL-0006.md` — missing=['fecha_del_hecho', 'fecha_de_registro']; vocab=—
- `conocimiento/hallazgos/HALL-0007.md` — missing=['fecha_del_hecho', 'fecha_de_registro']; vocab=—
- `conocimiento/decisiones/DEC-COBERTURA-CORPUS-PROGRESIVA.md` — missing=['validadores', 'hallazgos_que_la_sustentan', 'principios_relacionados', 'supuestos_implicados', 'alternativas_consideradas', 'justificacion', 'reemplaza', 'reemplazada_por']; vocab=—
- `conocimiento/decisiones/DEC-CORPUS-ORAL-PILOTO-ITERATIVO.md` — missing=['validadores', 'hallazgos_que_la_sustentan', 'principios_relacionados', 'supuestos_implicados', 'alternativas_consideradas', 'justificacion', 'reemplaza', 'reemplazada_por', 'condiciones_de_revision']; vocab=['estado=vigente_como_linea_experimental']
- `conocimiento/decisiones/DEC-G-P-SEPARATION.md` — missing=['fecha', 'supuestos_implicados', 'alternativas_consideradas', 'justificacion', 'reemplaza', 'reemplazada_por']; vocab=['estado=vigente_como_separacion_de_dimensiones']
- `conocimiento/decisiones/DEC-GRABAR-EN-VIVO.md` — missing=['fecha', 'principios_relacionados', 'supuestos_implicados', 'alternativas_consideradas', 'reemplazada_por']; vocab=['estado=vigente_revisado']
- `conocimiento/decisiones/DEC-TRIANGULACION-EMPIRICA.md` — missing=['principios_relacionados', 'supuestos_implicados', 'alternativas_consideradas', 'reemplazada_por']; vocab=—

## Regla

La deuda histórica listada no se corrige automáticamente: puede reflejar entidades antiguas, variantes de esquema o decisiones que requieren adjudicación. El objetivo de esta pasada es impedir que la fase post-Irma añada deuda nueva.
