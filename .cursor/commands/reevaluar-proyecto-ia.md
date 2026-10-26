## Precondición bloqueante: contexto documental
Ejecutar primero el protocolo `protocols/context-ingestion.md`, completar `context_review.json` y aprobar `scripts/check_context_gate.py`. Si el estado es `BLOCKED_CONTEXT_INCOMPLETE`, emitir solo reporte preliminar y faltantes; no votación final.

# /reevaluar-proyecto-ia

Entradas: `proyecto=<id> docs=<ruta_actualizada> previo=<directorio_resultados_previos>`.

Actúa como orquestador MoE. Compara versiones de documentos y resultados anteriores preservando IDs de hallazgos y objeciones cuando correspondan. Identifica hechos nuevos, rectificaciones, requisitos cerrados (con evidencia) y nuevos riesgos; **no cambies estados a resueltos por la mera actualización de un archivo**. Reejecuta las seis revisiones, debate y voto conforme a AGENTS.md; registra un changelog de decisiones en `outputs/<proyecto>/12_cambios_reevaluacion.md`. Si la información previa no está disponible, tratar como nueva evaluación y explicar limitación. Todas las salidas en español.

## Precondición multimodal
Ejecutar `scripts/ingest_documents.py` con los documentos del proyecto. Inspeccionar visualmente originales que incluyan imágenes, gráficos, páginas o diapositivas. Registrar cobertura en `document_review.json` y aplicar `protocols/multimodal-ingestion.md`. No emitir dictamen final si `BLOCKED_DOCUMENT_REVIEW`.
