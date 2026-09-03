from pathlib import Path
import re, shutil

ROOT = Path('.')

def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(s, encoding='utf-8')
def replace_once(s, old, new, label):
    if old not in s:
        raise SystemExit(f'missing anchor: {label}')
    return s.replace(old,new,1)
def move(src,dst):
    s,d=Path(src),Path(dst)
    if s.exists():
        d.parent.mkdir(parents=True, exist_ok=True)
        if d.exists(): raise SystemExit(f'destination exists: {dst}')
        shutil.move(str(s),str(d))

# Root cleanup
moves = {
    'PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md':'archivo/checkpoints/2026-09-02_pre_irma.md',
    'POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md':'archivo/checkpoints/2026-09-02_ingesta_reunion_irma.md',
    'POST_IRMA_ADJUDICATION_CHECKPOINT_2026-09-03.md':'archivo/checkpoints/2026-09-03_estado_adjudicado.md',
    'ESTADO_CIERRE_AGOSTO_2026.md':'archivo/checkpoints/2026-08-31_cierre_agosto.md',
    'ESTADO_COR002_Y_PEDAGOGIA_2026-08-22.md':'archivo/checkpoints/2026-08-22_cor002_pedagogia.md',
}
for a,b in moves.items(): move(a,b)

oldctx=Path('contexto-para-reconstruir-base-de-conocimientos')
if oldctx.exists():
    dst=Path('archivo/contextos'); dst.mkdir(parents=True,exist_ok=True)
    for p in list(oldctx.iterdir()):
        target=dst/p.name
        if target.exists(): raise SystemExit(f'context collision: {target}')
        shutil.move(str(p),str(target))
    oldctx.rmdir()

pd=Path('prompts')
if pd.exists():
    tech={'generadordecorpusv7','verificador de ortografía'}
    for p in list(pd.iterdir()):
        d=(Path('dispositivo/prompts/historicos') if p.name in tech else Path('archivo/prompts'))/p.name
        d.parent.mkdir(parents=True,exist_ok=True)
        if d.exists(): raise SystemExit(f'prompt collision: {d}')
        shutil.move(str(p),str(d))
    pd.rmdir()

write('archivo/README.md', '# Archivo\n\nMaterial histórico y de reconstrucción. Preserva genealogía y evidencia, pero **no constituye estado vigente ni autoridad por ubicación**.\n\n- `checkpoints/`: fotografías históricas del estado del proyecto.\n- `contextos/`: reconstrucciones y contextos de chats anteriores.\n- `prompts/`: herramientas de trabajo históricas o auxiliares no técnicas del dispositivo.\n\nEl estado vigente se reconstruye desde `INICIAR_AQUI_CHAT_NUEVO.md`, las entidades de `conocimiento/` y las decisiones vigentes.\n')
write('archivo/checkpoints/README.md', '# Checkpoints históricos\n\nSnapshots fechados para reconstrucción y comparación. **No gobiernan el estado actual.**\n\nEl punto de entrada vigente es `/INICIAR_AQUI_CHAT_NUEVO.md`.\n')
write('informes/README.md', '# Informes\n\nAnálisis, mapas de investigación y auditorías **no normativos**. Pueden localizar problemas o proponer rutas, pero no adoptan conocimiento ni decisiones.\n\nCuando un informe produzca una conclusión que deba gobernar el proyecto, ésta debe pasar por las entidades y reglas de actualización de `conocimiento/`.\n')

# Architecture v0.3
p=Path('00_ARQUITECTURA_DEL_CONOCIMIENTO.md'); s=read(p)
s=s.replace('version: 0.2','version: 0.3',1).replace('estado: borrador_de_trabajo','estado: vigente',1).replace('fecha: 02/09/2026','fecha: 03/09/2026',1)
s=replace_once(s,
    'Una decisión no es equivalente a un hallazgo. Surge como respuesta a uno o varios hallazgos, necesidades, principios o restricciones.\n',
    'Una decisión no es equivalente a un hallazgo. Normalmente surge como respuesta a uno o varios hallazgos, necesidades, principios o restricciones.\n\n**Decisiones directas de coordinación o alcance.** Cuando la persona responsable adopta explícitamente una decisión de coordinación, alcance o prioridad, no debe fabricarse un `HALL` espejo únicamente para satisfacer el esquema. En esos casos `hallazgos_que_la_sustentan` puede ser una lista vacía y la decisión debe identificar la fuente directa mediante `fuentes_directas` y explicar su justificación. Esta excepción no permite usar una DEC para presentar como hecho empírico algo que no ha sido observado o validado.\n',
    'direct coordination DEC rule')
start=s.index('# 14. Organización propuesta del repositorio')
end=s.index('---\n\n# 15. Regla de fuente única de verdad', start)
sec='''# 14. Organización física vigente del repositorio

Esta sección **describe la organización real vigente**; no prescribe un árbol ideal independiente del repositorio. Si la organización física cambia por una decisión adoptada, esta sección debe actualizarse. No se debe reestructurar el repositorio sólo para obedecer un diagrama histórico.

```text
/
├── README.md
├── INICIAR_AQUI_CHAT_NUEVO.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
├── 01_JERARQUIA_DE_VERDAD.md
├── 02_BACKLOG.md
├── 03_REGLAS_DE_ACTUALIZACIÓN.md
├── 04_RELACION_CON_ELDP.md
├── conocimiento/        # Sistema de Conocimiento canónico + vistas
├── informes/            # análisis y auditorías no normativos
├── archivo/             # checkpoints, contextos y herramientas históricas
├── dispositivo/         # sistema derivado temporal; pendiente de separación física
└── .github/             # control técnico del repositorio
```

Reglas de ubicación:

- `conocimiento/` contiene fuentes registradas, hallazgos, decisiones, principios válidos y vistas canónicas.
- `informes/` puede orientar investigación, pero no adopta conocimiento.
- `archivo/` preserva historia y contexto; no gobierna el presente.
- `dispositivo/` es un sistema derivado y no forma parte del Sistema de Conocimiento. Su presencia actual es transitoria hasta completar la separación física verificada.
- Los materiales fuente compartidos se adjudican por naturaleza y derechos, no por el lugar donde una herramienta los haya ingerido primero.

---

'''
s=s[:start]+sec+s[end+4:]
m=re.search(r'# 22\. Decisiones arquitectónicas iniciales.*?---\n\n## Regla final',s,flags=re.S)
if m:
    repl='''# 22. Estado arquitectónico actual

La arquitectura vigente ya define los tipos principales de entidad, sus estados, la autoridad de las decisiones, la función de las vistas y la frontera con sistemas derivados. Las cuestiones abiertas deben registrarse en el backlog o mediante entidades del tipo correspondiente; no deben mantenerse como una lista especulativa dentro de la Constitución.

La evolución histórica permanece disponible en Git y en `archivo/`.

---

## Regla final'''
    s=s[:m.start()]+repl+s[m.end():]
s += '''

---

## Actualización v0.3 — 2026-09-03

- Se reemplaza el árbol conceptual obsoleto por la organización física vigente y se aclara que el diagrama no prescribe una reestructuración.
- Se formaliza que decisiones directas de coordinación o alcance pueden sustentarse en una fuente directa sin fabricar un `HALL` espejo.
- Se clasifican `informes/`, `archivo/` y `dispositivo/` por función y autoridad.
- Se retira de la Constitución la lista histórica de cuestiones "para la siguiente versión"; las deudas actuales pertenecen al backlog.
'''
write(p,s)

# Bibliography registry de-sync containment
p=Path('conocimiento/BIBLIOGRAFIA.md'); s=read(p)
s=s.replace('**Versión:** 1.1','**Versión:** 1.2',1).replace('**Fecha:** 2026-08-14','**Fecha:** 2026-09-03',1)
old='''La numeración es secuencial y continua. No existe límite superior ni rango reservado.

La numeración alcanza `BIB055` a la fecha de esta versión. Las entradas siguientes continúan a partir del último identificador asignado en la hoja de cálculo, que es el registro operativo de la bibliografía.

Este documento no se actualiza cada vez que se añade una fuente. Solo se actualiza cuando cambian las reglas del sistema.
'''
new='''La numeración es secuencial y continua. No existe límite superior ni rango reservado.

La **hoja de cálculo bibliográfica es el registro operativo de asignación de IDs**. Este Markdown no declara cuál es el último `BIB###`, porque puede quedar desactualizado entre revisiones. La presencia de una fuente `SRC-*` en el repositorio no autoriza inventar o asignar un `BIB###` sin consultar ese registro.

Hasta reconciliar la hoja maestra con las fuentes incorporadas recientemente, las nuevas fuentes pueden conservarse con su `SRC-*` estable sin recibir un identificador BIB provisional.
'''
s=replace_once(s,old,new,'BIB max')
s=s.replace('Doce fuentes están registradas como revisadas a profundidad. Se enumeran en la sección 3.\n\nOtras fuentes están registradas y parcialmente consultadas.\n\nEl estado de revisión de cada entrada se administra en la hoja de cálculo, no en este documento.',
'''La sección 3 es una **fotografía histórica parcial** de fuentes que habían sido registradas como revisadas a profundidad; no debe utilizarse para inferir el número total actual de fuentes o el último identificador BIB.

El estado de revisión y la asignación completa de IDs se administran en la hoja de cálculo bibliográfica. Hasta reconciliarla con los `SRC-*` recientes, este documento evita afirmar conteos globales.''',1)
s += '''

---

# 13. Reconciliación pendiente del registro bibliográfico

Al 2026-09-03 existen fuentes `SRC-*` incorporadas después de la última sincronización documentada de la hoja bibliográfica. No deben recibir IDs BIB por inferencia.

`BL-026` gobierna la reconciliación. Hasta cerrarlo:

```text
SRC_ID = VALID_SOURCE_ID
BIB_ID = ASSIGN_ONLY_FROM_MASTER_SPREADSHEET
NO_GUESSED_BIB_IDS = true
```
'''
write(p,s)

# AUDIO propagation
p=Path('conocimiento/AUDIO.md'); s=read(p)
s=s.replace('**Versión:** 1.2','**Versión:** 1.3',1).replace('**Fecha:** 2026-08-31','**Fecha:** 2026-09-03',1)
anchor='Este documento describe únicamente el proceso de producción de audio. No documenta la metodología general, el diseño del corpus, la teoría pedagógica ni la bibliografía.\n'
add='''Este documento describe únicamente el proceso de producción de audio. No documenta la metodología general, el diseño del corpus, la teoría pedagógica ni la bibliografía.

## 1.1 Alcance activo de fase

La decisión `DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN` fija actualmente:

```text
ACTIVE_LANGUAGE_LEVEL = BEGINNER
ACTIVE_PRIMARY_MODALITY = LISTENING
ACTIVE_BASELINE_VARIETY = JUCHITAN
ACTIVE_LITERACY_TRACK = false
```

Para AUDIO esto significa priorizar materiales auditivos técnicamente claros y adecuados a principiantes de Juchitán. **No fija por sí mismo una velocidad, un patrón de repetición ni una secuencia única de audio**; esas decisiones requieren justificación pedagógica y pruebas específicas.
'''
s=replace_once(s,anchor,add,'AUDIO scope')
write(p,s)

# Residual technical deference in suspended PRIN-P
p=Path('conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md'); s=read(p)
s=s.replace('''  Primero deben implementarse como propiedades analíticas descriptivas del dispositivo. La evidencia
  futura deberá mostrar cuáles tienen consecuencias pedagógicas, cuáles ya quedan representadas por G
  o P, cuáles requieren descripción separada y cuáles son simplemente propiedades lingüísticas sin
  necesidad de una escala curricular propia.''',
'''  Primero deben mantenerse como propiedades descriptivas de investigación, sin convertirlas
  automáticamente en requisitos curriculares. La evidencia futura deberá mostrar cuáles tienen
  consecuencias pedagógicas, cuáles ya quedan representadas por G o P, cuáles requieren descripción
  separada y cuáles son simplemente propiedades lingüísticas sin necesidad de una escala curricular propia.''',1)
write(p,s)

# DEC G/P neutral current formulation
p=Path('conocimiento/decisiones/DEC-G-P-SEPARATION.md'); s=read(p)
s=s.replace('''  definitiva, ni que deban funcionar como secuencia curricular cerrada, ni que un generador deba
  aplicarlas automáticamente antes de construir una escena.''',
'''  definitiva, ni que deban funcionar como secuencia curricular cerrada, ni que deban
  aplicarse automáticamente antes de construir una escena.''',1)
s=s.replace('  - futuros generadores, cuando vuelvan a activarse\n','',1)
s=s.replace('  - Revisar si alguna forma de restricción previa resulta útil cuando vuelva a existir un generador general.\n','  - Revisar si alguna forma de restricción previa resulta pedagógicamente útil al diseñar materiales futuros.\n',1)
write(p,s)

# Coordination decision no longer needs mirror HALL
p=Path('conocimiento/hallazgos/HALL-0020.md'); s=read(p)
s=s.replace('estado: corroborado','estado: reemplazado',1)
s += '\n\n## Revisión arquitectónica — 2026-09-03\n\nEste registro se conserva por genealogía, pero deja de utilizarse como sustento necesario de la decisión de alcance. La Arquitectura v0.3 permite que una decisión explícita de coordinación se apoye directamente en su `SRC` sin crear un hallazgo que sólo repita la decisión.\n'
write(p,s)

p=Path('conocimiento/decisiones/DEC-ALCANCE-ACTIVO-PRINCIPIANTES-ESCUCHA-JUCHITAN.md'); s=read(p)
s=s.replace('''hallazgos_que_la_sustentan:
  - HALL-0020
  - HALL-0009
''','''hallazgos_que_la_sustentan:
  - HALL-0009
fuentes_directas:
  - SRC-EMILIANO-DECISIONES-ALCANCE-2026-09-03
''',1)
s=s.replace('  - POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md\n','  - archivo/checkpoints/2026-09-02_ingesta_reunion_irma.md\n',1)
write(p,s)

# Negation explicit scope
p=Path('conocimiento/decisiones/DEC-NEGACION-QUI-QUE-EQUIVALENTES.md'); s=read(p)
s=s.replace('''  representar formas equivalentes de negación dentro del alcance documentado por las
  consultas actuales.''','''  representar formas equivalentes de negación dentro del alcance documentado actualmente
  para Juchitán y El Espinal.''',1)
s=s.replace('''impacta_a:
  - "política lingüística de negación"
  - "futuras reglas de revisión ortográfica"
  - "futuro dispositivo cuando consuma un estado aprobado que incluya esta decisión"
''','''alcance: "Equivalencia semántico-funcional documentada actualmente en consultas de Juchitán y El Espinal; no establece distribución ni frecuencia fuera de ese alcance."
impacta_a:
  - "política lingüística de negación"
  - "futuras reglas de revisión ortográfica derivadas"
''',1)
write(p,s)

# Backlog BIB reconciliation
p=Path('02_BACKLOG.md'); s=read(p)
if '### BL-026 —' not in s:
    marker='\n---\n\n# Criterios de cierre\n'
    entry='''
---

### BL-026 — Reconciliar la hoja bibliográfica maestra con las fuentes SRC actuales

**Estado:** Abierto  
**Prioridad:** Alta / documental

La hoja de cálculo bibliográfica es el registro operativo de asignación de `BIB###`, pero el repositorio contiene fuentes incorporadas después de la última sincronización documentada y `BIBLIOGRAFIA.md` había quedado congelado en un máximo obsoleto.

No asignar nuevos IDs BIB por inferencia. Reconciliar la hoja maestra con los `SRC-*` actuales, confirmar específicamente la identidad de `BIB065`/Bueno Holle y asignar IDs sólo a las fuentes que todavía no los tengan.

**Criterio de cierre:** hoja maestra y repositorio coinciden; ningún `SRC` bibliográfico relevante tiene un BIB ambiguo, duplicado o inventado.
'''
    if marker not in s: raise SystemExit('backlog marker missing')
    s=s.replace(marker,entry+marker,1)
write(p,s)

# Current references to moved checkpoints
p=Path('INICIAR_AQUI_CHAT_NUEVO.md'); s=read(p)
refs={
    'POST_IRMA_ADJUDICATION_CHECKPOINT_2026-09-03.md':'archivo/checkpoints/2026-09-03_estado_adjudicado.md',
    'POST_IRMA_INTAKE_CHECKPOINT_2026-09-02.md':'archivo/checkpoints/2026-09-02_ingesta_reunion_irma.md',
    'PRE_IRMA_POST_MIGRATION_CHECKPOINT_2026-09-02.md':'archivo/checkpoints/2026-09-02_pre_irma.md',
}
for a,b in refs.items(): s=s.replace(a,b)
write(p,s)

# README physical tree
p=Path('README.md'); s=read(p)
start=s.index('## Estructura del repositorio')
end=s.index('---\n\n## Sistema de Conocimiento',start)
sec='''## Estructura del repositorio

```text
vocesdelasnubes/
├── README.md
├── INICIAR_AQUI_CHAT_NUEVO.md
├── 00_ARQUITECTURA_DEL_CONOCIMIENTO.md
├── 01_JERARQUIA_DE_VERDAD.md
├── 02_BACKLOG.md
├── 03_REGLAS_DE_ACTUALIZACIÓN.md
├── 04_RELACION_CON_ELDP.md
├── conocimiento/        # Sistema de Conocimiento y vistas canónicas
├── informes/            # investigación/auditorías no normativas
├── archivo/             # historia, checkpoints y contextos
├── dispositivo/         # sistema derivado temporal, pendiente de separación
└── .github/
```

La raíz se mantiene deliberadamente pequeña. Los checkpoints fechados y contextos históricos no viven en la raíz y no gobiernan el estado vigente.

---

'''
s=s[:start]+sec+s[end+4:]
write(p,s)

# Update moved path references outside archive
for p in Path('.').rglob('*.md'):
    if '.git' in p.parts or 'archivo' in p.parts: continue
    txt=p.read_text(encoding='utf-8'); orig=txt
    for a,b in moves.items(): txt=txt.replace(a,b)
    if txt!=orig: p.write_text(txt,encoding='utf-8')

# Assertions
assert not Path('prompts').exists()
assert not Path('contexto-para-reconstruir-base-de-conocimientos').exists()
for f in moves: assert not Path(f).exists(), f
arch=read('00_ARQUITECTURA_DEL_CONOCIMIENTO.md')
assert '01_FUENTES/' not in arch
assert 'version: 0.3' in arch
assert 'Decisiones directas de coordinación o alcance' in arch
assert 'ACTIVE_PRIMARY_MODALITY = LISTENING' in read('conocimiento/AUDIO.md')
assert 'propiedades analíticas descriptivas del dispositivo' not in read('conocimiento/principios/PRIN-P-RESTRICCION-BLANDA.md')
gp=read('conocimiento/decisiones/DEC-G-P-SEPARATION.md')
assert 'generador' not in gp.split('implementacion_anterior_ya_no_vigente:',1)[0].lower()
assert 'Juchitán y El Espinal' in read('conocimiento/decisiones/DEC-NEGACION-QUI-QUE-EQUIVALENTES.md')
assert 'La numeración alcanza `BIB055`' not in read('conocimiento/BIBLIOGRAFIA.md')
assert 'BL-026' in read('02_BACKLOG.md')

obsolete=list(moves.keys())
bad=[]
for p in Path('.').rglob('*.md'):
    if 'archivo' in p.parts: continue
    txt=p.read_text(encoding='utf-8')
    for x in obsolete:
        if x in txt: bad.append((str(p),x))
if bad: raise SystemExit(f'obsolete current refs: {bad}')

print('ARCHITECTURE_SIMPLIFICATION_PASS')
