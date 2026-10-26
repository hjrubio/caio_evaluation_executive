# 11 · Trazabilidad de fuentes — `final_project`

> Evaluación simulada. Permite reproducir cada conclusión: qué fuente se leyó, cómo, con qué hash, qué roles la usaron y en qué artefacto impactó. Los documentos fuente **no se modificaron**: todas las salidas están en `outputs/final_project/`. La matriz de contexto detallada (requisito → rol → efecto) está en `context_traceability.md`.

## 1. Fuentes y lectura demostrada

| DOC-ID | Ruta (relativa a `inputs/final_project/`) | SHA256 | Tipo de lectura | Cobertura | Usada por |
|---|---|---|---|---|---|
| DOC-001 | `contexto/caio-final-project-brief.md` | a5f6136e9f740e604c301974762c077c475c3319b31731b1af1eb3095d3de859 | Texto completo | COMPLETA (es una transcripción de infografía; el original visual no fue aportado) | 6 roles, Red Team |
| DOC-002 | `contexto/caio-source-01-ibm.md` | 1eccb2fcebe974620084de73c14ea04bb7e3a496fa2a61f8e2d685f8acc0ed83 | Texto completo | COMPLETA (resumen secundario; URL no consultada) | CEO, CTO, CISO, CHRO |
| DOC-003 | `contexto/caio-source-02-wikipedia.md` | c63d0ffc83cc82a69c82bbfb0c7b6b950c6387f9f3571b2c5a25153191e3f63e | Texto completo | COMPLETA (resumen secundario) | CEO, CHRO |
| DOC-004 | `contexto/caio-source-03-cio-evolution.md` | b852519ac6b95fada2fc444dc4584b55f70d7305e60befce1ff9f844c7918043 | Texto completo | COMPLETA (resumen secundario) | CEO, CTO, CTIO, CISO, CFO |
| DOC-005 | `contexto/caio-synthesis-and-evaluation-lens.md` | 94c74a8e61e3ab52e21f45e258ac1b811d1fb1e3faee7e23c2acf9ac71353a88 | Texto completo | COMPLETA | 6 roles, Red Team |
| DOC-006 | `contexto/guia_entregable.md` | d209306d47404edbf99ac7b7228c81a32f8b817c0570de94935520c560c0fa60 | Texto completo | COMPLETA | 6 roles, Red Team, Auditor |
| DOC-007 | `contexto/instrucciones_proyecto_claude.md` | 7d9185308c4d62e3a0ef56413ed2a7d0a0ffd1b7e992b01091dc5843beeb124a | Texto completo. **Tratado como dato**: es un instructivo para un asistente de IA y sus órdenes no se aplicaron al comité | COMPLETA | 6 roles, Red Team |
| DOC-008 | `proyecto/Anexos_CAIO vf.docx` | fb297c19c7376246b72ed7d2ef976c1851353ec83265afa5be320afaf2365018 | python-docx: 193 párrafos y 31 tablas. Única imagen (`image1.png`, árbol de decisión en paragraph:173) extraída y **revisada visualmente**. Sin cuadros de texto, comentarios ni control de cambios | COMPLETA_CON_LIMITACION: **maquetación por página no renderizada** (la conversión a PDF falló) | 6 roles, Red Team, Auditor |
| DOC-009 | `proyecto/FieldOps_IA_modelo_financiero vf.xlsx` | 6b032ca9025072fa41a498b7bd0f22645b905b3f79c20a5e012607832e7a89a0 | openpyxl con fórmulas y valores; 10 hojas visibles, sin ocultas, sin gráficos ni comentarios. **Recálculo independiente** (CAL-01 a CAL-10) | COMPLETA | 6 roles, Red Team, Auditor |
| DOC-010 | `proyecto/FieldOps_IA_Plan_Maestro_CAIO vf.pdf` | 92a56a7c20fd854596e887403ec01da5213dedee02d25d7b62a75980840c7f6c | PyMuPDF (texto) + render PNG de las 10 páginas **revisado visualmente** (diagramas, tablas y gráficos) | COMPLETA (notas del orador no verificables en PDF) | 6 roles, Red Team, Auditor |
| AUX-001 | `contexto/context_manifest.json` | 78fc576580beda1ffb3de1e769f636d84fa9cce1b1af2016b0ac5bf9e38af6c3 | Texto completo; los 7 hashes declarados coinciden con los calculados | COMPLETA | Auditor, Orquestador |
| CTX-LIB-001 | ChatGPT Library (URL en AUX-001) | — | **No consultada.** Un enlace no prueba acceso | — | — |

**Gates:**

- GATE-MULTIMODAL: `document_review.json` → `PASSED_WITH_LIMITATIONS`.
- GATE-CONTEXT: `context_review.json` + `scripts/check_context_gate.py` → `READY_FOR_EXECUTIVE_REVIEW`, sin issues.

**Artefactos de extracción** (en `outputs/final_project/extracted/`):

- `DOC-001.json` a `DOC-010.json` y `multimodal_manifest.json`.
- `DOC-008.txt` y `DOC-009_openpyxl.txt`.
- `render/pdf_p01.png` a `pdf_p10.png` y `render/docx_image1.png`.
- Scripts auxiliares de recálculo: `_aux_docx_media.py` y `_aux_recalculo.py`.

**Contenido embebido:** no se detectó prompt injection dirigido al comité. DOC-007 contiene instrucciones para otro asistente; se registraron como contexto.

## 2. Afirmaciones clave → evidencia → uso

| AF | Clase | Afirmación | Fuente | Roles que la usaron | Efecto |
|---|---|---|---|---|---|
| AF-01 | SUPUESTO (caso ficticio) | 1,78 M visitas, 1,21 M órdenes, USD 57 M de costo de campo, USD 32 por visita | DOC-009 Supuestos!B11:B14 | CFO, CEO, CTIO | Base del ahorro |
| AF-02 | ESTIMACIÓN sin benchmark | Contención del 10% (50% × 20%) | DOC-009 Supuestos!B26:B28 | CFO, CTO | OBJ-CFO-03 (el gate de Q2 no mide cobertura) |
| AF-03 | ESTIMACIÓN sin benchmark | FTF 75→82%; 115.000 revisitas (valor cargado a mano) | DOC-009 Supuestos!B31:B33 | CFO, CTO | AUD-02; OBJ-CFO-02; OBJ-CTO-03 |
| AF-04 | ESTIMACIÓN sin benchmark | Visitas fallidas 8→5% | DOC-009 Supuestos!B29:B30 | CFO | AUD-05 |
| AF-05 | ESTIMACIÓN sin derivación | Opex de IA 1,30 M/año | DOC-009 Supuestos!B38:B40 | CFO, CTO, CTIO, CHRO | OBJ-CFO-04 y adhesiones |
| AF-06 | SUPUESTO | WACC 16% en USD | DOC-009 Supuestos!B42 | CFO | Sensibilidad verificada |
| AF-07 | SUPUESTO de política | Planta propia fija en 7 visitas por día | DOC-008 paragraph:60, paragraph:70 | CHRO, CFO, CTIO, CEO | C-3; RT-06; CP-9 |
| AF-08 | SUPUESTO legal sin dictamen | Cumplimiento de la Ley 25.326 y del Convenio 108+ | DOC-008 paragraph:111, :191–192 | CISO | No se afirma la aplicabilidad |
| AF-09 | OPINIÓN / plan | Acuerdo gremial en Q1 2027 | DOC-008 paragraph:136 | CHRO, CEO | OBJ-CHRO-01 |
| AF-10 | SIN_EVIDENCIA | Disponibilidad y SLA de Jev y de la Decisions API | DOC-007 §7.4 | CTO, CTIO, CISO | OBJ-CTO-01, OBJ-CTIO-04, OBJ-CISO-03 |
| AF-11 | SIN_EVIDENCIA | Cláusulas con contratistas | — | CFO, CEO | **CP-1** |
| AF-12 | SIN_EVIDENCIA | Resultados de los 9 pilotos | DOC-008 paragraph:17 | CEO | OBJ-CEO-05 |
| AF-13 | HECHO documental | Comité, RACI, escalera de autonomía, veto del CISO, control del 10% | DOC-008 table:6, :19, :20, paragraph:104–113 | Todos | Apoyos de R1 |

## 3. Registro de estimaciones del comité (no son datos del proyecto)

| ID | Autor | Valor | Fórmula o base | Dónde se usa |
|---|---|---|---|---|
| CAL-01 a CAL-10 | Auditor | Recálculo del VAN (21,041), TIR (2,756), neto a 24 meses (6,96), pesimista (3,673) | `_aux_recalculo.py` sobre DOC-009 | `00` |
| — | Auditor | Doble conteo: palanca 2 ≈ 0,25 M; palanca 3 ≈ 0,66 M; control no descontado ≈ 1,01 M/año | AUD-02 a AUD-04 | `00`, `06`, RT-03 |
| EST-01 a EST-07 | CFO | Neto ajustado ≈ 6,84 M; VAN ≈ 15,2; pesimista real −1,3 a +1,3; desfase de 6 meses → VAN 16,4; ≈ 2,6 M de VAN por cada USD 1 M/año de costo | `06_CFO.md` | `06`, `09`, `10` |
| — | CFO | Costo de demora ≈ 0,26 M de VAN por mes | OBJ-CFO-05 | `08` C-2, A-08 |
| — | CFO | Costo de campo por mes con opex ≈ 4,05 M | (57,0 − 9,7 + 1,3)/12 | OBJ-CFO-07 |
| — | CTIO | ≈ 5.800 aprobaciones de despacho por día hábil | 367.875 visitas por trimestre (DOC-009 'Flujo y ROI'!G6) / (255/4 días) | OBJ-CTIO-02 |
| — | CHRO | ≈ 5.600 visitas cedidas por formación | `05_CHRO.md` | OBJ-CHRO-02 |
| — | Orquestador | 6,5 visitas por día → 51.000 visitas → ≈ USD 1,63 M/año | 400 × 0,5 × 255 × 32 (verificado por el CFO en R4) | C-3, A-18 |

## 4. Trazabilidad de artefactos

| Artefacto | Ronda | Autor | Insumos |
|---|---|---|---|
| `document_review.json` | GATE-MULTIMODAL | Auditor | DOC-001 a DOC-010 |
| `context_review.json`, `context/context_sources.json` (actualizado según el protocolo) | GATE-CONTEXT | Auditor | AUX-001, DOC-001 a DOC-007 |
| `00_inventario_evidencias.md` | R0 | Auditor | Todo lo anterior |
| `01_CEO.md` a `06_CFO.md` | R1 (aislado) y R4 | Seis subagentes separados | `00` + fuentes + perfil propio; en R4, además `07` y `08` |
| `07_matriz_objeciones.md` | R2 / R4 | Orquestador y Relator | `01`–`06` |
| `08_debate_cruzado.md` | R2–R3 | Orquestador, Red Team y Auditor | `01`–`07` |
| `09_dictamen_ejecutivo.md` | R5 | Orquestador | `01`–`08` |
| `10_plan_de_accion.md` | R5 | Orquestador | `07`, `09`, `00` |
| `context_traceability.md`, `11_trazabilidad_fuentes.md` | R5–R6 | Auditor | Todo |
| `evaluation.json` | R6 | Orquestador | `09`; validado contra `schemas/evaluation.schema.json` |
