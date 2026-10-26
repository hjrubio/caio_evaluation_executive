# /validar-contexto-ia

Parámetros: `proyecto=<id> docs=<ruta>`.
1. Leer `protocols/context-ingestion.md` y `context/context_sources.json`.
2. Resolver referencias a la Library. Si no hay acceso, reportar el bloqueo sin inventar contenidos.
3. Incluir todos los archivos fuente en el inventario, leerlos, resumirlos con localizadores y escribir `outputs/<proyecto>/context_review.json`.
4. Preparar `context_traceability.md`; comprobar conflictos, cobertura y hashes.
5. Ejecutar `python scripts/check_context_gate.py --project <id> --docs <ruta> --review outputs/<proyecto>/context_review.json`.
6. Devolver resultado de gate y lista precisa de fuentes pendientes. No autorizar evaluación formal si está bloqueado.

## Precondición multimodal
Ejecutar `scripts/ingest_documents.py` con los documentos del proyecto. Inspeccionar visualmente originales que incluyan imágenes, gráficos, páginas o diapositivas. Registrar cobertura en `document_review.json` y aplicar `protocols/multimodal-ingestion.md`. No emitir dictamen final si `BLOCKED_DOCUMENT_REVIEW`.
