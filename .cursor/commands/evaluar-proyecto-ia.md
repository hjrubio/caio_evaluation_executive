## Precondición bloqueante: contexto documental
Ejecutar primero el protocolo `protocols/context-ingestion.md`, completar `context_review.json` y aprobar `scripts/check_context_gate.py`. Si el estado es `BLOCKED_CONTEXT_INCOMPLETE`, emitir solo reporte preliminar y faltantes; no votación final.

# /evaluar-proyecto-ia

Entradas del usuario (interpretar si están presentes): `proyecto=<id> docs=<ruta> modo=completo|rapido`.

Actúa como `agents/orchestrator.md`. Lee primero `AGENTS.md`, perfiles en `agents/*.md`, protocolos y plantillas. Localiza y analiza los documentos en `docs`; define inventario de fuentes estable con DOC-ID, citas por página o sección cuando sean verificables. Si no se proporciona ruta, utiliza los documentos accesibles en el proyecto y deja declarada la selección, sin inventar otros archivos.

Ejecuta R0–R6 según `protocols/evaluation-workflow.md`; si el modo es rápido, indica rondas omitidas. Las seis evaluaciones R1 deben ser independientes: usa agentes o subagentes aislados cuando estén disponibles; de lo contrario, escribe dictámenes por separado sin utilizar conclusiones de otros roles y declara la limitación. Aplica R2 red team, R3 réplica solo con evidencia real, R4 votos revisados y R5 dictamen. No pretendas haber ejecutado agentes externos si no ocurrió.

Genera exactamente los entregables enumerados en README y valida `evaluation.json` según el schema. No alteres documentos originales. Responde en español con resultado, bloqueantes, votos y rutas de salidas.

## Precondición multimodal
Ejecutar `scripts/ingest_documents.py` con los documentos del proyecto. Inspeccionar visualmente originales que incluyan imágenes, gráficos, páginas o diapositivas. Registrar cobertura en `document_review.json` y aplicar `protocols/multimodal-ingestion.md`. No emitir dictamen final si `BLOCKED_DOCUMENT_REVIEW`.
