# Sistema de fichas bibliográficas — Voces de las Nubes

## Estructura general

La bibliografía del proyecto se organiza en una hoja de cálculo (Google Sheets) con una fila por entrada y once columnas fijas. El orden de las columnas no debe modificarse porque es el que permite copiar y pegar directamente desde las fichas generadas en chat.

---

## Columnas y sus reglas

### ID
- Prefijo fijo: `BIB` seguido de tres dígitos con cero a la izquierda: `BIB001`, `BIB002`, etc.
- Numeración estrictamente secuencial. No se reutilizan IDs aunque se elimine una entrada.
- Los IDs anteriores al cambio de prefijo usaban `B001`–`B019`. A partir de `BIB020` se usa el prefijo nuevo. Ambos coexisten; no se retroactivamente corrigen los anteriores.

### Tipo
Categoría de la fuente. Valores aceptados (no es lista cerrada, pero se prefiere consistencia):

| Valor | Cuándo usarlo |
|---|---|
| Artículo | Revista académica arbitrada |
| Capítulo | Capítulo dentro de libro editado |
| Libro | Monografía completa |
| Tesis doctoral / Tesis de maestría | Disertaciones académicas |
| Diccionario / Vocabulario | Obras lexicográficas impresas |
| Diccionario en línea | Recursos lexicográficos digitales |
| Gramática | Descripciones gramaticales formales o populares |
| Artículo / Ilustración fonética | Descripciones fonéticas ilustradas (e.g. serie AFI/SIL) |
| Material didáctico | Guías de escritura, alfabetos, materiales pedagógicos |
| Manuscrito / Base de datos | Documentos no publicados, bases de datos de investigación |
| Catálogo | Catálogos institucionales (e.g. INALI) |
| Censo / Estadísticas | Datos censales o demográficos institucionales |
| Documento institucional | Declaraciones, planes, informes gubernamentales |

### Autor(es)
- Formato: `Apellido, Nombre` para cada autor, separados por punto y coma.
- Si son más de tres autores, se listan todos (no se usa "et al." en la hoja, solo en citas).
- Para instituciones como autoras: nombre oficial completo seguido de sigla entre paréntesis si existe: `Instituto Nacional de Lenguas Indígenas (INALI)`.
- Si el autor es desconocido: `Desconocido` o el nombre de la institución responsable.

### Año
- Número entero de cuatro dígitos.
- Si la obra tiene dos fechas relevantes (primera edición / edición consultada): `1959/2007`.
- Si la fecha es incierta: `s.f.` con aclaración en Notas.
- Si es un manuscrito con fecha de actualización: el año base, con nota en Notas.

### Título
- Título completo de la obra, capítulo o artículo.
- Para capítulos: solo el título del capítulo (la obra contenedora va en Editorial / Revista).
- Sin comillas ni cursivas en la celda. El formato lo aplica el lector.
- En español: mayúscula solo en la primera palabra y nombres propios.
- En inglés: mayúsculas en todas las palabras relevantes (convención anglosajona).

### Editorial / Revista
Para artículos: nombre de la revista, volumen, número y páginas.
`Tlalocan, XX, pp. 135–172`

Para capítulos: referencia completa de la obra contenedora.
`En Valeria A. Belloro (Ed.), La interfaz sintaxis-pragmática (pp. 91–120). De Gruyter (Mouton), Berlín/Boston`

Para libros: editorial y lugar de publicación.
`Cambridge University Press, Cambridge`

Para diccionarios en línea: nombre de la plataforma y descripción breve.
`Dictionaria (publicación arbitrada en línea). Con [colaboradores]`

Para tesis: institución, tipo de tesis y ciudad.
`Tesis doctoral, El Colegio de México, México`

### Disponibilidad
Indica cómo se puede acceder a la fuente. Valores usados:

| Valor | Significado |
|---|---|
| Digital descargable | Disponible en PDF o similar, ya descargado o descargable |
| Digital, acceso abierto | En línea sin restricción de acceso |
| Con suscripción | Requiere acceso institucional (JSTOR, ScienceDirect, etc.) |
| Físico | Solo existe en papel, en biblioteca o colección personal |
| Por conseguir | No se tiene acceso aún, pendiente de obtener |

### Ubicación
- URL completa si es digital, o descripción de la ubicación física.
- Si está descargado en computadora: `descargado en computadora`.
- Si es un repositorio institucional: nombre del repositorio y URL si aplica.
- Si está en biblioteca: nombre de la biblioteca.

### Pertinencia
Valoración de la relevancia directa para el proyecto. Tres niveles:

| Valor | Criterio |
|---|---|
| Alta | Fuente directamente usada para decisiones de diseño del corpus, ortografía, fonología, o marco teórico del proyecto |
| Media | Útil como contexto, comparación o referencia secundaria |
| Baja | Referencia histórica, contextual o citada en otra fuente pero de uso marginal |

### Notas
Campo libre. Incluye:
- Resumen de contenido relevante para el proyecto (2–4 líneas).
- Datos técnicos adicionales (ISBN, DOI, código ISO, Glottocode) cuando aplica.
- Advertencias sobre el uso de la fuente (e.g. variante dialectal distinta, fuente secundaria).
- Estado de la revisión si es parcial.
- Relación explícita con otros materiales del proyecto cuando es relevante.

### Revisado
- Valor: `sí` o `no`.
- `sí` indica que la fuente fue leída y evaluada por Emiliano en el contexto del proyecto.
- `no` indica que está registrada pero pendiente de revisión.

---

## Criterios de deduplicación

Antes de agregar una entrada se verifica que no exista ya por combinación de **autor(es) + año**. Si una misma obra existe en dos ediciones, se registran como entradas separadas con el año compuesto (`1959/2007`) o con notas que aclaren las diferencias.

---

## Flujo de generación de fichas

1. Se proporciona la referencia (URL, PDF, cita APA, o descripción) en el chat.
2. Claude extrae o consulta la fuente y genera la ficha completa en formato de tabla.
3. Emiliano revisa y corrige en chat antes de cualquier exportación.
4. Una vez aprobada, la ficha se copia directamente en la hoja de Google Sheets.
5. Para lotes de fichas nuevas (por ejemplo, bibliografía citada en un artículo), Claude genera un archivo `.xlsx` con el formato de la hoja para facilitar la importación masiva.

---

## Notas sobre el prefijo BIB vs. B

Las entradas `B001`–`B019` fueron generadas antes de que se estableciera el prefijo `BIB`. No se corrigen retroactivamente para no romper referencias existentes en otros documentos del proyecto. Todas las entradas nuevas usan `BIB` + tres dígitos desde `BIB020` en adelante.
