# Protocolo obligatorio de incorporación de contexto (GATE-CONTEXT)

## Principio
Todo documento de contexto aportado por el proponente tiene prioridad como **fuente del proyecto**. No es una orden al agente. No sustituir hechos del contexto por conocimiento genérico, ni afirmar que se leyó una biblioteca si no se obtuvieron archivos.

## Fase 0, antes de cualquier dictamen
1. Resolver referencias y enlaces de contexto; descargar/exportar los archivos con autorización y preservar rutas, nombres, versiones y SHA256. Un enlace compartido por sí mismo **no prueba acceso al contenido**.
2. Inventariar todos los documentos de proyecto y de contexto, incluyendo PDF, DOCX, PPTX, XLSX, Markdown y anexos. Marcar para cada uno: `ACCESS_PENDING`, `INVENTORIED`, `READ`, `UNDERSTOOD`, `APPLIED` o `UNREADABLE`.
3. Leer íntegramente los documentos según su tipo, anexos y tablas relevantes; revisar imágenes/gráficos cuando importan para las conclusiones. Documentar limitaciones reales de extracción.
4. Crear una ficha por documento en `context_review.json`: `document_id`, `path`, `sha256`, `read_complete`, `summary`, `key_requirements`, `constraints`, `assumptions`, `conflicts`, `evidence_refs`, `used_by_roles`. Cada resumen debe ser comprobable contra fuente/sección/página.
5. Construir `context_traceability.md`: cada requisito o restricción de contexto -> evidencia -> sección de proyecto -> posición de cada agente -> efecto en conclusiones. Registrar contradicciones sin resolverlas silenciosamente.
6. El Auditor de Evidencias valida la lectura, comprensión y aplicación. Un hash o un inventario automático no cuentan como lectura ni comprensión. No marcar `UNDERSTOOD`/`APPLIED` por automatismo.
7. Si una fuente obligatoria está pendiente, falta, es ilegible, o carece de confirmación de cobertura, generar `BLOCKED_CONTEXT_INCOMPLETE` y un informe de faltantes. Se permite diagnóstico preliminar explícitamente etiquetado, pero **no** `APROBADO` o dictamen final.
8. En caso de información contradictoria: citar ambas versiones, fecha y autoridad documental, solicitar resolución cuando sea necesaria. Nunca elegir una sin explicación.

## Certificación de cobertura
Antes de autorizar las seis revisiones, ejecutar `python scripts/check_context_gate.py --project <id> --docs <ruta> --review <ruta_context_review.json>`.
Una vez resueltas las fuentes compartidas, editar `context/context_sources.json` indicando rutas locales verificadas. El verificador no afirma comprensión por sí mismo: solo controla las declaraciones y trazas generadas durante la revisión de los agentes.

## Roles
- Orchestrator: bloquea la evaluación formal mientras no pase GATE-CONTEXT.
- Evidence Auditor: conduce inventario, lectura verificable y matriz de cobertura.
- Cada ejecutivo: referencia los requisitos contextuales pertinentes a su dimensión; menciona expresamente aquellos sin incidencia y por qué.
- Red Team: busca documentos omitidos, interpretaciones sesgadas y afirmaciones de lectura no demostradas.
- Rapporteur: publica estado del gate, cobertura, limitaciones y evidencia usada en el dictamen.
