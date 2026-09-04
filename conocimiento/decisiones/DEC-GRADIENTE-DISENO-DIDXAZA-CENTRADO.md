# DEC-GRADIENTE-DISENO-DIDXAZA-CENTRADO — El diseño didxazá-centrado se evalúa por autoría y trazabilidad, no por una prohibición binaria del español

```yaml
id: DEC-GRADIENTE-DISENO-DIDXAZA-CENTRADO
titulo: "El diseño didxazá-centrado se evalúa por autoría y trazabilidad, no por una prohibición binaria del español"
decision: >
  A partir del 4 de septiembre de 2026 se sustituye la prohibición binaria del diseño
  Spanish-first por un gradiente de cuatro niveles de precomposición. El idioma en que se
  formula una propuesta sigue siendo parte relevante de su procedencia, pero no determina
  por sí solo si un material puede llegar a ser didxazá-centrado. Para los materiales
  precompuestos, el criterio central pasa a ser la autoridad efectiva de la persona hablante
  para rechazar, suprimir, reordenar, reformular y añadir contenido, junto con un registro
  recuperable de esas modificaciones.

  Los cuatro niveles son:

  NIVEL 0 — Traducción. Se entrega una frase o un turno en español y la persona hablante
  lo traslada o reformula en Didxazá.

  NIVEL 1 — Guion. Los turnos y su orden se proponen previamente en español; la persona
  hablante puede conservarlos, reformularlos, suprimirlos, reordenarlos o añadir otros al
  construir la realización en Didxazá.

  NIVEL 2 — Situación. Se entregan situación, participantes y propósito; la persona
  hablante decide qué se dice, quién lo dice y en qué orden.

  NIVEL 3 — Ámbito. Se entrega únicamente el ámbito o dominio; la persona hablante escoge
  la situación completa y su organización conversacional.

  El NIVEL 0 no puede originar por sí mismo la estructura discursiva de un producto final.
  Su resultado puede conservarse como evidencia léxica, frasal o de reformulación y puede
  reutilizarse posteriormente cuando corresponda, pero no establece por sí solo la
  arquitectura conversacional.

  Los NIVELES 1 y 2 pueden originar material candidato a producto final cuando se cumplan
  conjuntamente las dos condiciones de autoría establecidas más abajo. El NIVEL 3 es la
  forma de menor precomposición y constituye una referencia preferente cuando resulte
  practicable, no una obligación universal.

  Se mantiene sin cambios que las herramientas de chat o sistemas derivados no autorizan
  por sí mismas un producto final, que el material marcado como experimental no adquiere
  estatus final por resultar plausible y que la incorporación definitiva sigue sujeta a
  la validación lingüística y metodológica pertinente.
estado: vigente
fecha: 2026-09-04
responsable: Emiliano López Carlton
validadores:
  - Emiliano López Carlton
hallazgos_que_la_sustentan: []
fuentes_directas:
  - "Decisión explícita de coordinación de Emiliano López Carlton, 2026-09-04"
  - "Condición de revisión prevista en DEC-CORPUS-FINAL-NO-SPANISH-FIRST: necesidad de precisar qué cuenta como diseño Spanish-first"
principios_relacionados:
  - PRIN-INVESTIGACION-ABIERTA
supuestos_implicados:
  - "La autoridad explícita de modificación y el registro de cambios reducen el riesgo de que una propuesta precompuesta gobierne indebidamente la realización en Didxazá; este supuesto debe comprobarse empíricamente."
alternativas_consideradas:
  - "mantener la prohibición binaria y tramitar cada trabajo con hablantes como excepción experimental"
  - "derogar la decisión anterior sin sustituirla, dejando el criterio a juicio caso por caso"
  - "condicionar el permiso a credenciales o formación docente específica de la persona hablante en lugar de a su autoridad declarada"
justificacion: >
  La formulación anterior trataba el idioma de la propuesta como un criterio binario de
  admisión. Ese criterio protegía contra la proyección del español, pero resultaba demasiado
  restrictivo para trabajar colaborativamente con hablantes y para comparar distintas formas
  de elicitación y diseño.

  Una propuesta en español puede influir en la organización de la respuesta incluso cuando
  la persona hablante tiene poder de rechazo; por ello esta decisión no considera que la
  autoridad elimine automáticamente el riesgo de priming, encuadre o calco. En cambio, exige
  dos condiciones que permiten reducir ese riesgo, hacerlo visible y someterlo a evaluación:
  autoridad explícita para modificar la propuesta y trazabilidad de lo que efectivamente se
  conservó, cambió, eliminó o añadió.

  El criterio deja así de ser una prohibición por idioma y pasa a ser una regla de autoría,
  procedencia y registro. Esto permite usar el español como herramienta de trabajo sin
  confundir una propuesta española con evidencia autónoma de la organización del Didxazá.
impacta_a:
  - conocimiento/CORPUS.md
  - conocimiento/METODOLOGIA.md
  - conocimiento/PEDAGOGIA.md
  - conocimiento/VALIDACION.md
  - futuros corpus y productos pedagógicos
reemplaza: DEC-CORPUS-FINAL-NO-SPANISH-FIRST
reemplazada_por: null
condiciones_de_revision:
  - "evidencia de que los niveles 1 o 2 proyectan de manera sistemática estructura española incluso con autoridad declarada y registro de modificaciones"
  - "un caso en que el registro de modificaciones resulte insuficiente para reconstruir el origen de una estructura"
  - "resultados del primer trabajo de diseño con hablantes bajo este gradiente"
```

## Regla operativa

```text
DIDXAZA_CENTERED_CANDIDATE = SPEAKER_AUTHORSHIP + CHANGE_RECORD + PERTINENT_VALIDATION
LANGUAGE_OF_PROMPT = PROVENANCE_FACTOR_NOT_BINARY_GATE

PRECOMPOSITION_LEVEL_0_TRANSLATION -> LEXICAL_PHRASAL_OR_REFORMULATION_EVIDENCE
PRECOMPOSITION_LEVEL_0_TRANSLATION -> NOT_SUFFICIENT_FOR_DISCOURSE_ARCHITECTURE
PRECOMPOSITION_LEVEL_1_SCRIPT      -> FINAL_CANDIDATE_IF_AUTHORSHIP_CONDITIONS
PRECOMPOSITION_LEVEL_2_SITUATION   -> FINAL_CANDIDATE_IF_AUTHORSHIP_CONDITIONS
PRECOMPOSITION_LEVEL_3_DOMAIN      -> PREFERRED_WHEN_PRACTICABLE

AUTHORSHIP_CONDITIONS = DECLARED_REJECTION_AUTHORITY AND MODIFICATION_RECORD
MISSING_EITHER_CONDITION -> EXPERIMENTAL_ONLY

EXPERIMENTAL_OUTPUT != FINAL_CORPUS_PRODUCT
CHAT_OR_DERIVED_TOOL_OUTPUT != AUTOMATIC_FINAL_CORPUS_PRODUCT
FINAL_ENTRY_REQUIRES_PERTINENT_VALIDATION = true
```

## Condiciones de autoría

### Primera. Autoridad declarada

Antes de entregar cualquier material de nivel 1 o 2, se comunica de manera explícita a la persona hablante que puede:

- suprimir turnos;
- cambiar el orden;
- reformular cualquier propuesta;
- añadir lo que falte;
- sustituir una secuencia completa;
- declarar que la situación o interacción no ocurriría así.

No basta con que esa autoridad exista de hecho: debe estar dicha antes del trabajo.

### Segunda. Registro de modificaciones

Debe quedar constancia recuperable de:

- qué se propuso;
- qué conservó la persona hablante;
- qué reformuló;
- qué eliminó;
- qué reordenó;
- qué añadió;
- qué rechazó por resultar impropio, improbable o ajeno al uso esperado.

El registro no exige un formato elaborado. Exige que después pueda reconstruirse la diferencia entre el estímulo recibido y el material producido.

Cuando falte cualquiera de las dos condiciones, el material conserva condición experimental. No se convierte en producto final por resultar plausible ni por estar bien formado.

## Interpretación del gradiente

El gradiente describe **cuánta arquitectura se decide antes de la intervención de la persona hablante**. No constituye una escala de calidad automática.

Un material de nivel 3 puede resultar pobre, artificial o poco útil. Un material de nivel 1 puede resultar excelente después de una intervención profunda del hablante y de la validación pertinente. El nivel de precomposición debe conservarse como metadato de procedencia para poder comparar resultados.

Por tanto:

```text
LOWER_PRECOMPOSITION != AUTOMATICALLY_BETTER_MATERIAL
HIGHER_PRECOMPOSITION != AUTOMATICALLY_INVALID_MATERIAL
PRECOMPOSITION_LEVEL = PROVENANCE_AND_EXPERIMENTAL_VARIABLE
```

## Relación con la decisión reemplazada

Esta decisión no revierte el diagnóstico de `DEC-CORPUS-FINAL-NO-SPANISH-FIRST`. Conserva el riesgo identificado: proyectar sobre el Didxazá secuencias, estructuras y expectativas conversacionales propias del español.

Lo que cambia es el instrumento para controlarlo. La decisión anterior utilizaba una prohibición binaria del diseño Spanish-first. La decisión vigente utiliza un gradiente de precomposición, autoridad explícita de la persona hablante, trazabilidad de modificaciones y validación posterior.

El español vuelve así a ser una herramienta ordinaria posible de preparación y trabajo, sin adquirir por ello autoridad lingüística sobre la forma final del Didxazá.
