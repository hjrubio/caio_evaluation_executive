# Matriz de trazabilidad del contexto — `final_project`

> Requisito o restricción del contexto → evidencia en el proyecto → posición de cada rol → efecto en las conclusiones. Las fuentes CTX son la exportación local verificada por hash (`context_review.json`); **la ChatGPT Library (CTX-LIB-001) no fue consultada**. Las contradicciones se registran, no se resuelven en silencio.
>
> **Estados:**
> - `CUMPLE`: evidencia suficiente.
> - `PARCIAL`: presente con brechas.
> - `NO_CUMPLE`: ausente.
> - `NO_VERIFICABLE`: el formato recibido no permite verificarlo.
> - `NO_EVALUADO`: el comité no lo contrastó específicamente.
> - `CONFLICTO`: contradicción entre fuentes de contexto.
>
> En las celdas de rol, "—" significa que el rol no lo trató.

| CTX-ID | Fuente y ubicación exacta | Requisito / restricción | Artefacto del proyecto | CEO | CTO | CTIO | CISO | CHRO | CFO | Estado |
|---|---|---|---|---|---|---|---|---|---|---|
| CTX-001 | DOC-001 §1, §5 | Máximo 10 slides con pedido explícito al board | DOC-010 (10 slides); page:1 y page:10 | Usado: pedido bien estructurado | — | — | — | — | Usado: tramos | CUMPLE |
| CTX-001 | DOC-001 §1 bloque 2 | Roadmap técnico, financiero y cultural con hitos y criterios de éxito | DOC-008 Anexo G (table:27, paragraph:158–166); DOC-010 page:9 | — | OBJ-CTO-02 (gates no medibles) | OBJ-CTIO-03 | — | OBJ-CHRO-05 (gate cultural fuera del Anexo G) | OBJ-CFO-03 (Q2 sin cobertura) | PARCIAL |
| CTX-001 | DOC-001 §5 | Números con supuestos trazables y costos de operación, ROI o payback | DOC-009 (10 hojas); DOC-008 Anexo B | OBJ-CEO-02 | OBJ-CTO-04 | — | — | OBJ-CHRO-04 | OBJ-CFO-02, OBJ-CFO-04 | PARCIAL (AUD-05, AUD-08) |
| CTX-001 | DOC-001 §1 bloque 4, §5 | Escenarios, contingencias y distinción entre decisiones reversibles e irreversibles | DOC-009 Escenarios; DOC-008 paragraph:99, paragraph:172, image:1 | OBJ-CEO-03 | — | — | — | Adopta OBJ-CEO-03 | OBJ-CFO-03; adopta OBJ-CEO-03 | PARCIAL (AUD-09, AUD-14) |
| CTX-001 | DOC-001 §5 | Objeciones anticipadas, en especial del CFO | DOC-008 Anexo I | Usado | — | — | — | — | Usado: sin registro con respuestas | PARCIAL (AUD-13) |
| CTX-001 | DOC-001 §2 | Plan operativo, no solo pilotos | DOC-008 table:27, Anexo C | Usado: CAIO 2.0 | Usado | OBJ-CTIO-01 (sin modelo de operación) | — | — | — | PARCIAL |
| CTX-001 | DOC-001 §4 (checklist) | Anexo con benchmarks, resultados de pilotos o referencias | DOC-008 paragraph:178–193 (solo dos fuentes legales) | OBJ-CEO-02 | HS-14, HS-15 (sin métricas offline) | — | — | — | OBJ-CFO-02 | NO_CUMPLE (AUD-05, AUD-13) |
| CTX-001 | DOC-001 §3 (personas evaluadoras) | Board, CFO y CAIO experimentado como audiencia | Composición del comité MoE (6 roles) | — | — | — | — | — | — | CONFLICTO registrado: la lente CAIO se cubre con DOC-005 en cada rol |
| CTX-002 | DOC-002 "Five areas of responsibility" | Gobierno, riesgo, sesgo y privacidad como responsabilidad del CAIO | DOC-008 Anexo E (paragraph:105–111, table:22–23) | Adopta OBJ-CISO-01 (reputacional) | OBJ-CTO-05 | — | OBJ-CISO-01 a OBJ-CISO-05 | — | — | PARCIAL (AUD-16, AUD-17) |
| CTX-003 | DOC-003 "Key takeaways" | Liderazgo cultural; prueba transformacional frente a incremental | DOC-008 Anexo F; DOC-010 page:3, page:7 | OBJ-CEO-04 | — | — | — | Usado: Anexo F real; OBJ-CHRO-05 | Disiente de OBJ-CEO-04 en 12 meses | PARCIAL |
| CTX-004 | DOC-004 "The two generations…" | Producción, guardrails y métricas de ROI (CAIO 2.0); derechos de decisión explícitos | DOC-008 paragraph:76–101, paragraph:112–116 | Usado | Usado: diseño juzgable | Usado: degradación | Usado: guardrails | — | Usado: control independiente | CUMPLE en diseño, sin prestaciones probadas |
| CTX-004 | DOC-004 "What changed" | Visibilidad de costos por uso (FinOps) | DOC-009 Supuestos!B38:B40 | — | OBJ-CTO-04 (sin costo unitario) | HS-20 | — | — | OBJ-CFO-04 | PARCIAL |
| CTX-004 | DOC-004 | Evitar fragmentación y deuda técnica | DOC-008 paragraph:17 (9 pilotos) | OBJ-CEO-05 | — | — | — | — | — | PARCIAL |
| CTX-005 | DOC-005 §5–§7 | Evaluar D1–D7, escala de madurez y ocho preguntas | Dictámenes 01–06 | Aplicado | Aplicado | Aplicado | Aplicado | Aplicado | Aplicado | Aplicado por el comité |
| CTX-005 | DOC-005 §6 vs. DOC-007 §4 | Etiquetas de la escala de madurez | El proyecto usa la escala de DOC-007 | — | — | — | — | — | — | CONFLICTO registrado; se usan ambas sin elegir |
| CTX-005 | DOC-005 §10 | Las fuentes no cubren regulación específica | DOC-008 cita la Ley 25.326 y el Convenio 108+ / Ley 27.699 | — | — | — | No se afirma la aplicabilidad | — | — | Limitación declarada; normas no verificadas |
| CTX-006 | DOC-006 §2 | Único PDF de menos de 10 MB con anexos al final | Deck en PDF, anexos en DOCX y modelo en XLSX, por separado | — | — | — | — | — | — | NO_CUMPLE (AUD-12) → A-01 |
| CTX-006 | DOC-006 §6 | Anexos A–J, incluido J (referencias) | DOC-008 contiene A–I | — | — | — | — | — | — | NO_CUMPLE (AUD-13) → A-02 |
| CTX-006 | DOC-006 §6 Anexo A | Supuestos con origen: dato interno, benchmark o estimación | DOC-009 Supuestos!D5:D59 (origen circular) | OBJ-CEO-02 | — | — | — | — | OBJ-CFO-02 | NO_CUMPLE (AUD-05) → A-06 |
| CTX-006 | DOC-006 §6 Anexo I | Objeciones probables con respuestas | DOC-008 Anexo I | — | — | — | — | — | — | PARCIAL (AUD-13) → A-02 |
| CTX-006 | DOC-006 §8 | Escenarios con gatillos y decisiones | DOC-010 page:10; DOC-008 image:1 | OBJ-CEO-03 | — | — | — | — | OBJ-CFO-03 (pesimista mal modelado) | PARCIAL (AUD-09) → A-03, A-11 |
| CTX-006 | DOC-006 §4 | "Transformar, no parchear" | DOC-010 page:3–4 | OBJ-CEO-04 | — | — | — | — | Disiente | PARCIAL |
| CTX-007 | DOC-007 §6.1 | Hoja única de supuestos; fórmulas en el resto | DOC-009 Léeme!B9 | — | — | — | — | — | Usado | PARCIAL (AUD-19) |
| CTX-007 | DOC-007 §6.2 | VAN, TIR y payback antes y después de impuestos; pesimista; sensibilidad a la tasa | DOC-009 KPIs, Escenarios, Sensibilidad | — | — | — | — | — | Verificado (CAL-01 a CAL-10) | CUMPLE |
| CTX-007 | DOC-007 §6.3 | Inversión trimestral explicada y tramos con gate | DOC-009 Inversión; DOC-008 paragraph:41 | Usado; acepta desdoblar | — | — | — | — | OBJ-CFO-03 (Q1 sin consecuencia) | CUMPLE con brecha → A-11 |
| CTX-007 | DOC-007 §6.5 | Pérdida ponderada por demorar como llamado a la acción | DOC-010 page:1, page:3, page:10 | HS-07 (cota alta) | — | — | Disenso: la urgencia no justifica el riesgo de privacidad | — | OBJ-CFO-05 | CUMPLE la instrucción; objetado (RT-05) → A-08 |
| CTX-007 | DOC-007 §7.1 | Ningún modelo generativo decide solo | DOC-008 paragraph:76–83 | — | Usado | Usado | Usado | — | — | CUMPLE (diseño) |
| CTX-007 | DOC-007 §7.4 | Jev y Decisions API como capa de decisión | DOC-008 paragraph:82; DOC-010 page:6 | Adopta OBJ-CTO-01 | OBJ-CTO-01 | OBJ-CTIO-04 | OBJ-CISO-03 | — | — | CUMPLE la instrucción; idoneidad no demostrada (RT-07, AUD-15). DOC-007 se trata como dato, no como orden |
| CTX-007 | DOC-007 §7.7 | Resiliencia ante fallas del proveedor | DOC-008 paragraph:97, table:22/row:9 | — | Usado | OBJ-CTIO-04 | — | — | — | PARCIAL |
| CTX-007 | DOC-007 §7.8 | Datos mínimos a proveedores; sin retención ni entrenamiento | DOC-008 paragraph:111, table:22/row:5 ("sin entrenamiento", sin mención de retención) | Adopta | OBJ-CTO-05 | Adopta OBJ-CISO-03 | **OBJ-CISO-01 (BLOQUEANTE_PROPUESTO)**, OBJ-CISO-03 | — | — | NO_CUMPLE parcial (AUD-16) → A-04, A-20 |
| CTX-007 | DOC-007 §8 | Veto del CISO y mínimos de gobierno | DOC-008 Anexo E | — | — | — | OBJ-CISO-05 (sin procedimiento de escalamiento) | — | — | PARCIAL |
| CTX-007 | DOC-007 §8 | People plan mínimo | DOC-008 Anexo F, table:24–26 | Ajusta AP-CEO-05 | — | — | — | OBJ-CHRO-01 a OBJ-CHRO-03 | Adopta OBJ-CHRO-02 | PARCIAL |
| CTX-007 | DOC-007 §5.3 | Notas del orador en cada slide | DOC-010 (PDF) | — | — | — | — | — | — | NO_VERIFICABLE (AUD-20) |
| CTX-007 | DOC-007 §10 | Supuestos a validar, con quién los valida | DOC-008 / DOC-009 | — | — | — | — | — | — | NO_EVALUADO específicamente; AUD-05 cubre el origen → A-06 |
| CTX-007 | DOC-007 §3 vs. proyecto | Ejemplo "1.500 técnicos (40% propios / 60% tercerizados)" | El proyecto usa 1.000 de domicilio (400/600) + 500 de red | — | — | — | — | — | — | CONFLICTO registrado; se usa el proyecto (AUD-01) |
| CTX-007 | DOC-007 §11 | Documentos aludidos (`fieldops_contexto_caso.md`, banco de ideas, PDF de ejemplo) | No aportados | — | — | — | — | — | — | NO_VERIFICABLE (RT-09) → A-28 |

## Efecto en las conclusiones

- **Bajan la recomendación a "condicionada":** los requisitos de contexto con estado `NO_CUMPLE` o `PARCIAL` en finanzas (CTX-001 §5, CTX-006 Anexo A) y privacidad (CTX-007 §7.8). El segundo origina el único `BLOQUEANTE_PROPUESTO`.
- **No afectan la viabilidad del caso, pero sí la nota de la entrega académica:** los `NO_CUMPLE` de formato (CTX-006 §2 y §6). Van al Bloque I del plan de acción.
- **No cambian ningún voto:** los conflictos entre fuentes de contexto (escala de madurez, audiencia, ejemplo de dotación).
