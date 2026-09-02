# DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO — Los sistemas derivados no modifican ni promueven conocimiento por sí mismos

```yaml
id: DEC-AUTORIDAD-SISTEMA-CONOCIMIENTO
titulo: "Los sistemas derivados no modifican ni promueven conocimiento por sí mismos"
decision: >
  Voces de las Nubes conserva autoridad exclusiva sobre la adopción, promoción y
  modificación de su Sistema de Conocimiento. El dispositivo y cualquier sistema,
  herramienta o repositorio derivado pueden consumir conocimiento aprobado, producir
  análisis, detectar contradicciones, formular requisitos y proponer candidatos, pero
  no pueden convertir esos resultados directamente en conocimiento, decisiones,
  principios o modificaciones de las vistas canónicas.

  Toda propuesta procedente de un sistema derivado debe volver al procedimiento de
  actualización de Voces de las Nubes, conservar su procedencia y ser adjudicada con la
  autoridad pertinente antes de incorporarse.

  Los futuros desarrolladores de sistemas derivados no tendrán por defecto permisos de
  escritura sobre el Sistema de Conocimiento. La implementación técnica de esta frontera
  deberá usar controles de acceso suficientes; la separación física en repositorios es
  una implementación preferente cuando sea viable, pero esta decisión de autoridad no
  depende de que esa separación ya haya ocurrido.
estado: vigente
fecha: 2026-09-02
responsable: Emiliano López Carlton
validadores:
  - Emiliano López Carlton
hallazgos_que_la_sustentan:
  - HALL-0008
principios_relacionados:
  - PRIN-INVESTIGACION-ABIERTA
supuestos_implicados: []
alternativas_consideradas:
  - "Mantener una sola frontera basada únicamente en disciplina documental"
  - "Permitir escritura técnica con revisión posterior"
justificacion: >
  La coexistencia del Sistema de Conocimiento y el dispositivo en un mismo repositorio
  permitió dependencias de provenance y formulaciones pedagógicas que deferían a la
  implementación. Una frontera únicamente conceptual no garantiza que futuros
  desarrolladores carezcan de capacidad de modificación. La separación entre capacidad
  de descubrir/proponer y autoridad de adoptar permite mantener intercambio de
  información sin invertir la jerarquía epistemológica.
impacta_a:
  - 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
  - 01_JERARQUIA_DE_VERDAD.md
  - 03_REGLAS_DE_ACTUALIZACIÓN.md
  - INICIAR_AQUI_CHAT_NUEVO.md
  - dispositivo/README.md
  - conocimiento/PEDAGOGIA.md
  - 02_BACKLOG.md
reemplaza: null
reemplazada_por: null
condiciones_de_revision:
  - "Revisar si la frontera impide de manera innecesaria el flujo de evidencia útil entre proyectos."
  - "Revisar controles de acceso cuando se incorporen desarrolladores o repositorios adicionales."
```

## Regla operativa

```text
DERIVED_SYSTEM_MAY_READ = true
DERIVED_SYSTEM_MAY_ANALYZE = true
DERIVED_SYSTEM_MAY_PROPOSE = true
DERIVED_SYSTEM_MAY_CHALLENGE = true

DERIVED_SYSTEM_MAY_ADOPT_KNOWLEDGE = false
DERIVED_SYSTEM_MAY_PROMOTE_CANDIDATE = false
DERIVED_SYSTEM_MAY_WRITE_KNOWLEDGE = false
```

Un resultado técnico puede constituir evidencia sobre el comportamiento de la herramienta que lo produjo. No adquiere por ello autoridad lingüística, pedagógica, comunitaria o metodológica sobre Voces de las Nubes.
