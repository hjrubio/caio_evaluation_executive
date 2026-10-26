# 00 · Inventario y auditoría de evidencias — `final_project` (FieldOps IA)

> Evaluación simulada por un comité de agentes. No constituye aprobación institucional, académica ni corporativa. Autor: Auditor de Evidencias (sin voto). Fecha: 26/10/2026.

## 1. Intake (R0)

| Campo | Valor |
|---|---|
| Proyecto | FieldOps IA: "de despachar técnicos a resolver problemas" — Plan Maestro CAIO a 12 meses (DOC-010 page:1) |
| Organización | Austral Conecta S.A., **empresa ficticia**, telco de fibra y TV en Argentina, 1,6 M de abonados (DOC-010 page:1; DOC-008 paragraph:4) |
| Alcance elegido | Un área: operación de campo (DOC-008 paragraph:11). Fuera: predictivo y repuestos (DOC-007 §3; DOC-010 page:9 Q4 lo deja como piloto) |
| Audiencia | Board de noviembre 2026 (DOC-010 page:1) y evaluación académica del TP CAIO UTN.BA (DOC-001, DOC-006) |
| Objetivo de la revisión | Evaluar el plan como lo haría un comité ejecutivo, frente a la consigna (DOC-001, DOC-006) y a la lente CAIO (DOC-005) |
| Versión | "vf" en los nombres. Anexos fechados 23/10/2026 (DOC-008 paragraph:2); modelo 24/10/2026 (DOC-009 Léeme!A2); PDF creado 26/10/2026 18:31 (metadatos DOC-010) |
| Confidencialidad | Caso ficticio; no contiene datos personales reales. Se tratan los documentos como internos del equipo |
| Modo | completo (R0–R6) |

## 2. Inventario de fuentes

| DOC-ID | Archivo (relativo a `inputs/final_project/`) | Tipo | SHA256 (16) | Alcance | Estado de lectura |
|---|---|---|---|---|---|
| DOC-001 | `contexto/caio-final-project-brief.md` | Contexto: consigna oficial | `a5f6136e9f740e60` | Requisitos del TP | READ · UNDERSTOOD · APPLIED |
| DOC-002 | `contexto/caio-source-01-ibm.md` | Contexto: fuente secundaria | `1eccb2fcebe97462` | Rol del CAIO | READ · UNDERSTOOD · APPLIED |
| DOC-003 | `contexto/caio-source-02-wikipedia.md` | Contexto: fuente secundaria | `c63d0ffc83cc82a6` | Rol del CAIO | READ · UNDERSTOOD · APPLIED |
| DOC-004 | `contexto/caio-source-03-cio-evolution.md` | Contexto: fuente secundaria | `b852519ac6b95fad` | Madurez 1.0/2.0 | READ · UNDERSTOOD · APPLIED |
| DOC-005 | `contexto/caio-synthesis-and-evaluation-lens.md` | Contexto: lente de evaluación | `94c74a8e61e3ab52` | D1–D7, madurez, red flags | READ · UNDERSTOOD · APPLIED |
| DOC-006 | `contexto/guia_entregable.md` | Contexto: guía del entregable | `d209306d47404edb` | Formato, anexos A–J, checklist | READ · UNDERSTOOD · APPLIED |
| DOC-007 | `contexto/instrucciones_proyecto_claude.md` | Contexto: instructivo para asistente IA | `7d9185308c4d62e3` | Requisitos financieros y de arquitectura | READ · UNDERSTOOD · APPLIED (como dato) |
| DOC-008 | `proyecto/Anexos_CAIO vf.docx` | Proyecto: anexos A–I | `fb297c19c7376246` | 193 párrafos, 31 tablas, 1 imagen | READ · UNDERSTOOD · APPLIED |
| DOC-009 | `proyecto/FieldOps_IA_modelo_financiero vf.xlsx` | Proyecto: modelo financiero | `6b032ca9025072fa` | 10 hojas, fórmulas | READ · UNDERSTOOD · APPLIED |
| DOC-010 | `proyecto/FieldOps_IA_Plan_Maestro_CAIO vf.pdf` | Proyecto: deck de 10 slides | `92a56a7c20fd8545` | 10 páginas | READ · UNDERSTOOD · APPLIED |
| AUX-001 | `contexto/context_manifest.json` | Manifiesto de exportación | `78fc576580beda1f` | Lista de contexto y hashes | READ |

SHA256 completos en `document_review.json` y `context_review.json`. Los 7 hashes de contexto coinciden con `context_manifest.json`.

## 3. Gates de ingreso

| Gate | Resultado | Fundamento |
|---|---|---|
| GATE-MULTIMODAL | **APROBADO CON LIMITACIONES** | El script marcó `BLOCKED_DOCUMENT_REVIEW` (DOC-008 y DOC-009 en `PENDING_VISUAL_REVIEW`). Revisión del agente: DOC-010 renderizado y 10 páginas inspeccionadas visualmente; DOC-008 texto y 31 tablas completos y su única imagen (árbol de decisión, paragraph:173) inspeccionada; sin cuadros de texto, comentarios, control de cambios, gráficos ni SmartArt; DOC-009 con 10 hojas, sin ocultas ni gráficos, fórmulas leídas y VAN/TIR recalculados. **Limitación:** no se pudo renderizar la maquetación de páginas del DOCX (la conversión con Word se colgó). |
| GATE-CONTEXT | **APROBADO** (`READY_FOR_EXECUTIVE_REVIEW`) | `scripts/check_context_gate.py` sin observaciones. **Limitación:** el enlace a ChatGPT Library no se consultó; se usó la exportación local, con hashes verificados contra su manifiesto. |
| Prompt injection | Sin instrucciones dirigidas al comité en DOC-008/009/010. DOC-007 es un instructivo para un asistente ("Sos el asistente del equipo…"): se trata **solo como dato de requisitos**. |

## 4. Verificaciones aritméticas (recálculo independiente)

| ID | Afirmación | Fuente | Verificación | Resultado |
|---|---|---|---|---|
| CAL-01 | Pérdida actual USD 25,6 M/año = 13,9 + 5,8 + 4,6 + 1,3 | DOC-010 page:3; DOC-009 Línea base!B19 | 434.000×32 + 181.000×32 + 144.700×32 + 1,3 = 25,61 | CORRECTO |
| CAL-02 | Palancas 3,54 + 1,71 + 3,68 + 0,77 = 9,70; +0,36 = 10,06; −1,30 = 8,76 | DOC-010 page:4; DOC-009 Beneficios!D4:D13 | Reproducido | CORRECTO |
| CAL-03 | Captura 34% neta / 39% bruta | DOC-010 page:3 | 8,76/25,61 = 34,2%; 10,06/25,61 = 39,3% | CORRECTO |
| CAL-04 | Métrica norte 47,3 → 40,3 | DOC-010 page:4; DOC-008 paragraph:36 | 57,0/1,2056 = 47,28; (57,0 − 9,70 + 1,30)/1,2056 = 40,31 | CORRECTO (incluye opex IA) |
| CAL-05 | Inversión 5,40 = 1,35 + 1,94 + 1,29 + 0,82; tramo 1 = 3,29; tramo 2 = 2,11; contingencia 0,69 | DOC-010 page:8; DOC-009 Inversión!B15:F15 | Reproducido | CORRECTO |
| CAL-06 | Acumulado −1,35 / −2,89 / −2,90 / −1,80 / +0,39 … +6,96 | DOC-010 page:8; DOC-009 Flujo y ROI!C22:J22 | Reproducido | CORRECTO |
| CAL-07 | VAN 5 años 16% = 21,0 (13,4 después de impuestos); TIR 276% (175%) | DOC-010 page:8; DOC-009 Proyección 5 años!B37:C38 | Recálculo con flujos trimestrales a mitad de período: VAN 21,04; TIR 275,6%. Con descuento anual a fin de año el VAN sería 19,66 | CORRECTO según la convención declarada (DOC-008 paragraph:52) |
| CAL-08 | Escenarios: VAN 3,7 / 21,0 / 30,3; esperado 19,0; beneficio esperado 8,2 M/año; −0,7 M por mes | DOC-010 page:10; DOC-009 Escenarios!B7:E9, B17:B19 | Reproducido (3,67; 21,04; 30,29; 19,01; 8,19; 0,68) | CORRECTO |
| CAL-09 | 175 técnicos de terceros menos; factura −29% (34,2 → 24,2) | DOC-010 page:1, page:5 | 312.500/(7×255) = 175,1; 312.500×32 = 10,0 M | CORRECTO |
| CAL-10 | RPU neto de campo 18,96 → 19,42 | DOC-010 page:5; DOC-009 Línea base!B29 | 22 − 2,97 − 0,07 = 18,96; +8,76/1,6/12 = +0,46 | CORRECTO (métrica definida por el equipo) |

## 5. Hallazgos del auditor (no son votos)

| ID | Tipo | Hallazgo | Evidencia | Severidad sugerida |
|---|---|---|---|---|
| AUD-01 | Inconsistencia de redacción | La slide 1 dice "1.500 técnicos: en domicilio, 400 propios y 600 de empresas contratistas"; la suma es 1.000. Los anexos aclaran que 1.000 hacen visitas a domicilio y 500 hacen red, mantenimiento y supervisión | DOC-010 page:1; DOC-008 paragraph:53, table:13 | baja |
| AUD-02 | Cálculo no derivado | Palanca 3: 115.000 revisitas evitadas es un valor cargado a mano, no una fórmula. La derivación proporcional (7 pp de 25 pp sobre 337.600) daría ≈ 94.500, una diferencia de ≈ USD 0,66 M/año. Además, 337.600 revisitas con FTF 75% implican ≈ 1,35 M órdenes de reparación, más que las 1,21 M órdenes totales: la base de la palanca no es coherente o falta su definición | DOC-009 Supuestos!B33, Beneficios!C6; DOC-008 table:8/row:4 | alta |
| AUD-03 | Posible solapamiento | Palanca 2 aplica 3 pp sobre 1,784 M de visitas de la línea base, sin descontar las visitas que eliminan las palancas 1, 3 y 4. Sobre las visitas remanentes serían ≈ 45.750 (no 53.500), ≈ USD 0,25 M/año menos. Tampoco se ve un ajuste por la interacción entre las palancas 1 y 3 | DOC-009 Beneficios!C5 | media |
| AUD-04 | Afirmación no trazable en fórmulas | "Las cifras ya excluyen el 10% de órdenes que queda como grupo de control" y "Costo: ya descontado". Sin embargo, la contención (10%) se aplica sobre el 100% de las órdenes y las demás palancas sobre el total de visitas; no hay un factor 0,9 visible. Si no estuviera descontado, el bruto se sobreestima ≈ USD 1,0 M/año | DOC-008 paragraph:32, paragraph:117; DOC-009 Beneficios!A2, C4:C7 | alta |
| AUD-05 | Origen circular de supuestos | La columna "Origen" de la hoja Supuestos remite casi siempre a "Anexo B", y el Anexo B remite al modelo. No se distingue dato interno, benchmark público o estimación del equipo, como piden DOC-006 §6 (Anexo A) y DOC-007 §2.2. No hay benchmarks externos ni resultados de pilotos que respalden FTF 75→82%, la contención del 10% ni fallidas 8→5% | DOC-009 Supuestos!D5:D59; DOC-008 paragraph:190–193 | alta |
| AUD-06 | Dato de base vs. calidad declarada | El diagnóstico declara "códigos de cierre de orden poco confiables", pero las visitas evitables (181.000) y el FTF de base salen de "la muestra de cierres del diagnóstico". No se informa el tamaño ni el método de la muestra | DOC-008 paragraph:19, paragraph:30 | alta |
| AUD-07 | Supuesto contractual no documentado | El ahorro supone que cada visita no realizada deja de facturarse a USD 32 desde Q1 2027. No se documentan las cláusulas vigentes con las contratistas (mínimos de volumen, preaviso, tarifas escalonadas). El nuevo contrato por orden resuelta rige desde mediados de 2028, pero el modelo mantiene USD 32 por visita hasta 2031 | DOC-008 paragraph:57, table:25; DOC-009 Supuestos!B14 | crítica |
| AUD-08 | Costos recurrentes posiblemente incompletos | El opex de IA a régimen (1,30 M) incluye modelos 0,55, nube 0,35 y MLOps 0,40. No aparecen explícitos: equipo del CAIO desde 2028 (11 personas, financiado en 2027 dentro de "talento y equipo 1,3 M"), curadores (10), despachadores supervisores, costos del canal de mensajería/voz, licencias de proveedores de decisión, ni el costo de oportunidad de los 10 curadores extraídos de la dotación de red. No se muestra derivación unitaria (volumen × costo por decisión) | DOC-008 table:8/row:8, paragraph:42, paragraph:146; DOC-009 Supuestos!B38:B40 | alta |
| AUD-09 | Escenario pesimista vs. decisión preacordada | El VAN pesimista (3,7) supone gastar todo el plan, pero la decisión preacordada es no liberar el tramo 2. El texto dice "la exposición baja **hasta** USD 2,11 M", cuando el tramo 1 es 3,29 M (3,95 M con +20%). Además, el árbol dice "No libera el tramo 2" y la slide 10 "No liberar el tramo 2 completo" | DOC-008 paragraph:172, image:1; DOC-009 Escenarios!A2; DOC-010 page:10 | media |
| AUD-10 | Tabla de conciliación obsoleta | La tabla "Cifras que cambian respecto de la presentación" compara contra una versión del deck que ya no coincide con DOC-010 (p. ej. "Deck: VAN 20,7"; DOC-010 ya muestra 21,0). Puede confundir al board | DOC-008 table:2; DOC-010 page:8 | baja |
| AUD-11 | Inconsistencia menor | Sensibilidad "Inversión y reinversión +30%": el anexo muestra "—" en neto a 24 meses y el modelo calcula 5,34 | DOC-008 table:12/row:9; DOC-009 Sensibilidad!D12 | baja |
| AUD-12 | Formato de entrega | DOC-006 §2 exige un único PDF de menos de 10 MB con los anexos al final. El paquete recibido trae el deck en PDF (10 slides, cumple el máximo), los anexos en DOCX y el modelo en XLSX por separado | DOC-006 §2, §8; inventario | alta (cumplimiento de consigna) |
| AUD-13 | Contenido exigido ausente | Falta el Anexo J (referencias, benchmarks, glosario): solo hay dos fuentes legales. El Anexo I no contiene un registro de objeciones con respuestas, que piden DOC-006 §6 y DOC-001 §4/§5 | DOC-008 paragraph:178–193 | alta (cumplimiento de consigna) |
| AUD-14 | Requisito de consigna parcialmente cubierto | La distinción entre decisiones reversibles e irreversibles (DOC-001 §1 bloque 4) aparece solo para la autonomía de la IA ("tareas de bajo riesgo y reversibles"). No se aplica a las decisiones del board: acuerdo gremial de no despidos, contrato con contratistas con preaviso de 6 meses, proveedor de decisión, registro inmutable | DOC-008 paragraph:99 | media |
| AUD-15 | Dependencia de proveedor no verificada | La decisión del triage depende de "Jev (TypeSafe AI)", con respaldo en la "Decisions API de OpenAI". El propio contexto los describe en "acceso anticipado" y "beta pública". El comité no verificó su existencia, sus SLA ni sus condiciones contractuales | DOC-010 page:6; DOC-008 paragraph:82; DOC-007 §7.4 | alta |
| AUD-16 | Tensión de privacidad | "A los proveedores de IA solo viaja el estado del caso, nunca datos personales". Pero la capa de captura es un LLM conversacional por WhatsApp y voz, y hay visión por foto: el texto libre, la voz y las fotos del cliente llegan a algún modelo. Se declara "seudonimización y enmascaramiento de PII antes del gateway", sin describir cómo se hace con texto libre o voz, ni si el LLM o el reconocimiento de voz se alojan en infraestructura propia | DOC-010 page:6–7; DOC-008 paragraph:111, table:22/row:5, table:23/row:6 | alta |
| AUD-17 | Tensión de retención | El registro de Jev es inmutable (append-only, hash encadenado), dura 3 años e incluye un ID seudonimizado y el JSON de captura. Al mismo tiempo se declara que se cumple el derecho de supresión (art. 16). No se describe el mecanismo para compatibilizar ambos | DOC-008 paragraph:89–90, table:17, table:23/row:7 | media |
| AUD-18 | Gates con definiciones abiertas | Gate Q1 "triage en sombra acierta ≥ 80%": no se define qué es "acierto" ni cómo se observa el contrafactual cuando hubo visita. Gate Q2: medición en 6 semanas con 10% de control, sin cálculo de tamaño muestral ni de potencia estadística | DOC-008 table:27/row:6, paragraph:158 | media |
| AUD-19 | Higiene del modelo | El Léeme declara Supuestos como "única hoja que se edita". Sin embargo, la rampa trimestral (Beneficios!B27:E27), la inversión por componente y el opex trimestral (Inversión!B4:E14, B31:E31) se cargan fuera de esa hoja | DOC-009 Léeme!B9; DOC-007 §6.1 | baja |
| AUD-20 | No verificable | Notas del orador por slide (DOC-007 §5.3): no se pueden verificar en un PDF | DOC-010 | baja |

## 6. Mapa de afirmaciones clave (clasificación)

| ID | Clasificación | Afirmación | Fuente |
|---|---|---|---|
| AF-01 | SUPUESTO (caso ficticio) | 1,78 M visitas, 1,21 M órdenes resueltas, USD 57 M de costo de campo, USD 32 por visita | DOC-009 Supuestos!B11:B14 |
| AF-02 | ESTIMACIÓN del equipo, sin benchmark | Contención 10% (50% atendido × 20% resuelto) | DOC-009 Supuestos!B26:B28 |
| AF-03 | ESTIMACIÓN, sin benchmark | FTF 75% → 82%; 115.000 revisitas evitadas | DOC-009 Supuestos!B31:B33 |
| AF-04 | ESTIMACIÓN, sin benchmark | Visitas fallidas 8% → 5% | DOC-009 Supuestos!B29:B30 |
| AF-05 | ESTIMACIÓN, sin derivación | Opex IA 1,30 M/año a régimen | DOC-009 Supuestos!B38:B40 |
| AF-06 | SUPUESTO | WACC 16% en USD con riesgo país | DOC-009 Supuestos!B42 |
| AF-07 | SUPUESTO de política | Planta propia fija en 7 visitas por día; todo el ahorro recae en terceros | DOC-008 paragraph:60 |
| AF-08 | SUPUESTO legal sin dictamen | Cumplimiento de la Ley 25.326 y del Convenio 108+ (Ley 27.699). El comité no verificó la normativa de forma independiente; las fuentes citadas son notas de estudios jurídicos | DOC-008 paragraph:111, paragraph:191–192 |
| AF-09 | OPINIÓN/plan | Acuerdo gremial firmado en Q1 2027 | DOC-008 paragraph:136 |
| AF-10 | SIN_EVIDENCIA | Disponibilidad, SLA y condiciones de Jev y Decisions API | DOC-007 §7.4 |
| AF-11 | SIN_EVIDENCIA | Cláusulas actuales con contratistas (mínimos, preaviso) | — |
| AF-12 | SIN_EVIDENCIA | Resultados de los 9 pilotos previos | DOC-008 paragraph:17 (solo se mencionan) |
| AF-13 | HECHO documental | Diseño de gobierno: comité, RACI, escalera de autonomía, veto del CISO, grupo de control del 10% | DOC-008 table:6, table:19, table:20, paragraph:104–113 |

## 7. Datos faltantes solicitados al proponente

1. Origen primario de cada supuesto clave (dato interno, benchmark con fuente o estimación) y resultados de los 9 pilotos.
2. Derivación de las 115.000 revisitas evitadas y definición de la base de reparaciones.
3. Ubicación del descuento del grupo de control en las fórmulas.
4. Cláusulas vigentes con las contratistas: tarifa, mínimos de volumen, preaviso, penalidades.
5. Desglose unitario del opex (volumen de interacciones × costo) y costo de personas desde 2028.
6. Arquitectura de privacidad de la captura (dónde corren el LLM, la voz a texto y la visión; cómo se enmascara el texto libre).
7. Estado contractual y SLA de los proveedores de decisión y su madurez.
8. Cálculo de tamaño muestral para los gates.
9. Un único PDF con anexos, el Anexo J y el registro de objeciones.

## 8. Declaración de independencia para R1

Los seis dictámenes de R1 se encargan a **subagentes aislados**, uno por rol. Cada uno recibe el mismo material (este inventario, los documentos fuente y los extractos en `extracted/`) y su propio perfil (`agents/<rol>.md`). Se les prohíbe leer los dictámenes de los otros roles. El orquestador no redacta las conclusiones de R1.
