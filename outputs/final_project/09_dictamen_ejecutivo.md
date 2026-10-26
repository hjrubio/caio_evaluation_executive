# Dictamen ejecutivo simulado — `final_project` (FieldOps IA · Austral Conecta S.A.)

> Evaluación generada por un comité de agentes, no constituye aprobación corporativa real. Austral Conecta S.A. es una organización ficticia (DOC-006 §4). El comité no tiene autoridad legal ni institucional y no afirma que el plan se haya ejecutado.

- **Versión / fecha / documentación revisada:** entrega "vf" del equipo, revisada el 26/10/2026 en modo `completo` (R0–R6). Se revisaron el deck de 10 slides (DOC-010, SHA256 92a56a7c…), los anexos A–I (DOC-008, fb297c19…) y el modelo financiero de 10 hojas (DOC-009, 6b032ca9…). El contexto del curso son DOC-001 a DOC-007, hashes verificados contra AUX-001. Detalle en `00_inventario_evidencias.md`.
- **Resultado recomendado:** **`APROBADO_CON_CONDICIONES`**. Se recomienda aprobar el plan y **solo la parte Q1 del tramo 1 (USD 1,35 M)**, sujeta a condiciones precedentes. Sin esas condiciones, la recomendación pasa a `REFORMULAR` (ver §Condiciones).
- **Síntesis de negocio:**
  - El problema está cuantificado y es material: una pérdida de USD 25,6 M/año por visitas evitables, visitas repetidas y reinstalaciones (DOC-009 Diagnóstico; DOC-010 page:2).
  - La estructura del pedido es buena: tramos, gate en Q2, contingencia separada, certificación del ahorro fuera del CAIO y grupo de control (DOC-008 paragraph:41, paragraph:112–116, paragraph:158–164).
  - La arquitectura es defendible: el LLM no ejecuta, la salida es tipada, las reglas pueden anular y hay un respaldo determinístico (DOC-008 paragraph:76–97).
  - El modelo es íntegro y la aritmética se verificó: VAN 21,0 / 13,4 M y TIR 276% / 175% antes y después de impuestos (CAL-01 a CAL-10).
- **Incertidumbres que deciden:**
  1. Que el ahorro se cobre en la factura de las contratistas. El 96% del bruto depende de eso y no hay ninguna cláusula documentada.
  2. Que los supuestos de cada palanca tengan origen. Hoy es circular, con doble conteo estimado en ≈ 1,9 M/año de bruto.
  3. Que la promesa de privacidad, "solo viaja el estado del caso", sea compatible con los componentes de texto libre, voz e imagen.
  4. Que el camino pesimista real (el que sigue la decisión del gate) no tenga el VAN ≈ 0 que estima el comité.
- **Alternativas consideradas por el comité** (RT-02; ninguna cuantificada por falta de datos):
  - **A (sin IA):** plantillas de aviso, optimización clásica de agenda, checklist con foto y contrato por orden resuelta.
  - **B (IA acotada):** ML + reglas como decisor y LLM solo para captura.
  - **C:** desdoblar el tramo 1.

  La recomendación incorpora B y C como condiciones y exige comparar contra A.
- **Cobertura de puntajes:** 100% (6/6 roles evaluables). **Total ponderado: 3,00 / 5**, en la banda "condicionado" (≥ 3,0 y < 4,0) de `protocols/scoring-and-veto.md`. El puntaje no decide solo.

## Votos y justificación

| Experto | Peso | Inicial (R1) | Puntaje R4 | Posición final | Razón principal | Disenso |
|---|---:|---|---:|---|---|---|
| CEO | 20% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES | Oportunidad real y pedido bien estructurado; la captura del valor en la factura de terceros no tiene prueba. Sube a 4 con un dictamen contractual favorable y baja a 2 si hay mínimos que posterguen el ahorro más allá de 2028 | Contra reformular antes de cualquier desembolso; contra liberar los 3,29 M completos sin dictamen contractual; RT-02 no es un descuento a priori |
| CTO | 15% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES | Diseño en capas juzgable, sin métricas offline de ningún modelo. Jev no está justificado frente a ML + reglas. OBJ-CTO-05 sube a alta | La convergencia de C-4 no equivale a mitigación; el aviso de Q1 puede avanzar si no envía datos personales a terceros |
| CTIO | 15% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES | Hay camino de degradación y salida humana, pero no SLO, runbooks, kill switch técnico, dimensionamiento del despacho (≈ 5.800 aprobaciones por día hábil, ESTIMACIÓN) ni prueba de conmutación | El bloqueante no congela todo Q1; C-4 no está cerrada |
| CISO | 20% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES · **BLOQUEANTE_PROPUESTO** en OBJ-CISO-01 | Guardrails estructurales documentados; contradicción de privacidad demostrada en los propios documentos, autenticación débil y contratos de proveedores en beta sin cláusula de "sin retención" | Firmar la evaluación de impacto no basta por sí solo; un piloto en sombra con datos reales es procesamiento real |
| CHRO | 10% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES | People plan real (Anexo F), pero el acuerdo gremial no tiene plan B, las 7 visitas por día son una meta fija y no hay plan para ~175 equivalentes de contratistas ("sin doble estándar" se contradice con el anexo) | "Sin despidos propios" no alcanza como historia de personas; no se propone bloqueante de personas |
| CFO | 20% | APOYA_CON_CONDICIONES (3) | 3 | APOYA_CON_CONDICIONES (**pasa a OBJETA** si el dictamen contractual no es previo al primer desembolso) | El VAN base resiste ajustes (≈ 12–16 M, ESTIMACIÓN) y el piso no está demostrado (≈ 0 en el camino pesimista real, exposición ≈ 4 M). Agrega OBJ-CFO-06 y OBJ-CFO-07 | Contra usar los 0,7 M/mes y el VAN esperado de 19,0 como argumentos; contra exigir más transformación dentro de los 12 meses |

**Cálculo:** (3×20 + 3×15 + 3×15 + 3×20 + 3×10 + 3×20) / 100 = **3,00**.

**Unanimidad y anclaje.** Los seis roles coinciden en 3 / APOYA_CON_CONDICIONES desde R1, y ningún voto cambió en R4. El red team lo marcó como posible anclaje (RT-01). En R4 cada rol justificó su número con hallazgos propios que no estaban en el inventario del auditor y declaró qué evidencia lo movería. Aun así, la coincidencia se reporta como **limitación**: todos partieron del mismo inventario y el proponente no participó.

**Reconciliación de condiciones CEO–CFO.** El CEO pide el dictamen contractual "antes del tramo 1" (§b de su R4) y, al desdoblarlo, lo ata a Q2 (§c). El CFO lo exige antes del primer desembolso y, si no, vota OBJETA. **El comité adopta la lectura más estricta, antes del primer desembolso de Q1**, por tres motivos:

- es compatible con los dos disensos registrados por el CEO;
- conserva el voto condicionado del CFO;
- el propio CEO califica esa verificación como "barata y rápida".

## Bloqueantes y riesgos residuales

| ID | Tipo | Estado | Alcance | Escalamiento recomendado |
|---|---|---|---|---|
| OBJ-CISO-01 | `BLOQUEANTE_PROPUESTO` (riesgo crítico pendiente de comprobación; **no** es un incumplimiento legal verificado) | **No resuelto** | Impide procesar datos reales de clientes con proveedores externos, **incluido el triage en modo sombra de Q1** y cualquier aviso que use un proveedor externo. No impide aprobar el plan ni comprometer el tramo 1 para actividades sin esos datos | A la autoridad humana de privacidad o protección de datos y a Legales, con el diagrama de flujo de datos. No existe veto real del agente |
| OBJ-CEO-01 / OBJ-CFO-01 | Riesgo crítico: hipótesis financiera esencial **no probada** (tampoco refutada) | ABIERTA | Que el ahorro se realice en la factura de las contratistas | Condición precedente CP-1 |

Como hay un bloqueante no resuelto, no se recomienda `APROBADO`. No se recomienda `RECHAZADO` porque ninguna hipótesis esencial quedó refutada y no hay un incumplimiento legal verificado.

**Riesgos residuales principales** (todos `ABIERTA`, 32 objeciones en total, detalle en `07_matriz_objeciones.md`):

- Doble conteo y supuestos de origen circular (OBJ-CFO-02, OBJ-CEO-02).
- Gates no medibles; el gate de Q2 no mide la cobertura del triage (OBJ-CTO-02, OBJ-CFO-03).
- Proveedores en acceso anticipado o beta sin conmutación ensayada (OBJ-CTIO-04, OBJ-CISO-03).
- Copiloto sin métrica de fundamentación sosteniendo 3,68 M/año (OBJ-CTO-03, RT-08).
- Efecto mezcla sobre el FTF y las 7 visitas por día (RT-06, C-3): si la planta propia baja a 6,5 visitas por día, el ahorro cae ≈ 1,63 M/año (ESTIMACIÓN verificada por el CFO).
- Costos recurrentes incompletos (OBJ-CFO-04).
- Autenticación débil frente al catálogo de acciones (OBJ-CISO-02).
- Acuerdo gremial sin plan B (OBJ-CHRO-01).

## Controversias y debates no resueltos

| ID | Roles | Estado | Síntesis |
|---|---|---|---|
| C-1 | CISO vs. CTIO / CEO | ABIERTA, acotada | El bloqueante no hace inviable el gate de Q1. Sí impide la sombra con conversaciones reales. Los documentos no permiten determinar qué componentes de Q1 envían datos personales a terceros (`SIN_EVIDENCIA`, CISO R4). Pregunta al proponente |
| C-2 | CFO vs. CEO | **Convergencia**: desdoblar el tramo 1 | Ambos consideran sobredimensionado el costo de esperar. El CEO acepta aprobar solo Q1 y atar Q2 al gate. Queda un matiz: el CEO valora el costo de calendario de demorar la negociación con contratistas (preaviso de 6 meses) |
| C-3 | CHRO vs. CFO | ABIERTA | Acuerdo en el diagnóstico (las 7 visitas por día son mecanismo de ahorro y riesgo laboral), desacuerdo en el remedio. El CFO pide una guarda preventiva y recalcular el ahorro, no ajustar la carga; el CHRO pide estudio de tiempos y no usar presión individual. Se cierra solo con datos del piloto de Q2 |
| C-4 | CTO vs. CTIO (+ CISO, CEO, CFO) | Convergencia técnica, **no mitigada** | ML + reglas como decisor de línea base y Jev como contendiente en sombra. El proponente no la aceptó |
| C-5 | CEO vs. CHRO | Disenso de matiz | El CEO admite la objeción y agrega la condición C-08 (declarar el impacto en terceros en la slide 7). El CHRO no caracteriza la portada como encubrimiento: la cifra de 175 está dicha; falta el plan |

## Condiciones precedentes y próximos gates

| ID | Condición | Momento | Origen | Prueba de cierre |
|---|---|---|---|---|
| CP-1 | Dictamen de Legales y Compras sobre los contratos vigentes con contratistas: mínimos, preaviso, penalidades y posibilidad de pasar a pago por orden resuelta. Hoja de realizabilidad en el modelo | **Antes del primer desembolso** | OBJ-CFO-01, OBJ-CEO-01; voto CFO | Dictamen firmado; modelo con desfase y mínimos explícitos |
| CP-2 | Desdoblar el tramo 1: se aprueba Q1 (USD 1,35 M); Q2 (USD 1,94 M) se libera solo con el gate de Q1 cumplido y CP-1 cerrada | Hoy, en el acta | OBJ-CFO-03, OBJ-CEO-03, C-2 | Acta del board con la regla de liberación |
| CP-3 | Levantar OBJ-CISO-01 con cinco elementos: (1) diagrama de flujo de datos por componente; (2) promesa de privacidad corregida; (3) evaluación de impacto firmada (CISO y Legales); (4) contratos y due diligence de terceros con cláusula de "sin retención"; (5) enmascaramiento verificado o tratamiento como encargado | **Antes de procesar cualquier dato real de clientes con proveedores externos**, incluida la sombra | OBJ-CISO-01, OBJ-CTO-05, OBJ-CISO-03 | Los cinco artefactos revisados por la autoridad humana de privacidad |
| CP-4 | Gates medibles: definición de "acierto" con contrafactual, telemetría disponible para el gate de Q1, potencia estadística del control y **cobertura ≥ 50%** como condición del gate de Q2 | Antes de evaluar el gate de Q1 | OBJ-CTO-02, OBJ-CFO-03, OBJ-CTIO-03 | Anexo G revisado, con fórmulas |
| CP-5 | Modelo v2: supuestos con origen (dato interno, benchmark o estimación y quién los valida), sin solapamientos, grupo de control explícito, camino pesimista que siga la decisión del gate, costos recurrentes completos y comparación con la Alternativa A | Antes del gate de Q1 | OBJ-CFO-02, -04, -06; OBJ-CEO-02, -05; RT-02, RT-03 | Modelo y Anexo A revisados |
| CP-6 | Decisor de línea base ML + reglas; Jev en sombra, y lo reemplaza solo con una mejora medida. Conmutación ensayada | Antes de la producción del triage | C-4; OBJ-CTO-01, OBJ-CTIO-04 | Informe de ablación y prueba de conmutación |
| CP-7 | Modelo de operación: SLO, RTO/RPO, guardia, runbooks, kill switch técnico, dimensionamiento del despacho, regresión, canary y rollback | Antes de la producción | OBJ-CTIO-01, -02, -05 | Runbooks y game day |
| CP-8 | Umbral de calidad del copiloto (respuestas correctas y fundamentadas) dentro del gate de Q2; plan de evaluación de la visión | Antes de la zona piloto del copiloto | OBJ-CTO-03, RT-08 | Resultados de evaluación offline |
| CP-9 | Plan B si no se firma el acuerdo gremial; estudio de tiempos y guarda de carga; plan de transición para el personal de las contratistas; slide 7 consistente con el Anexo F (C-08 del CEO) | Antes del gate de Q1 (acuerdo) y del gate de Q2 (carga) | OBJ-CHRO-01, -02, -03; C-3; C-5 | Plan aprobado por RR.HH.; medición de duración y FTF por tipo de falla en Q2 |
| CP-10 | Modelo de amenazas de la autenticación del canal y prueba de suplantación; criterio de salida del red teaming; plan de incidentes | Antes de la producción del canal | OBJ-CISO-02, -05 | Informe de pruebas |

**Regla de degradación de la recomendación.** Si CP-1 no se cumple, el CFO pasa a OBJETA y la recomendación pasa a `REFORMULAR`. Si CP-3 no se cumple, el triage no sale de diseño con datos sintéticos o anonimizados.

**Próximos gates del plan** (DOC-008 Anexo G, con las correcciones de CP-4): gate de Q1 (aviso en producción, triage en sombra, acuerdo gremial firmado), gate de Q2 (liberación del tramo 2) y revisiones trimestrales.

## Confianza / limitaciones de evidencia

**Confianza global: media.**

1. **Ejecución:** los seis dictámenes de R1 los redactaron subagentes separados, en paralelo y con contexto aislado, sin acceso a los otros dictámenes. En R4, los mismos subagentes leyeron la matriz y el debate. El red team, el auditor y el Orquestador son el mismo agente principal. Ningún paso es una ejecución real del comité.
2. **ChatGPT Library:** no se accedió a la biblioteca enlazada (CTX-LIB-001). Se usó la exportación local; sus 7 hashes coinciden con el manifiesto, pero no se verificó que coincida con el contenido actual de la biblioteca.
3. **DOCX:** la conversión del DOCX a PDF no fue posible. Se extrajeron todo el texto, las 31 tablas y la única imagen (árbol de decisión, revisado visualmente), y no se encontraron cuadros de texto, comentarios ni control de cambios. **No se verificó la maquetación por página**, así que las referencias al DOCX usan paragraph/table, no página.
4. **Proponente ausente:** no hubo réplicas en R3; todas las objeciones están `ABIERTA`.
5. **Documentos aludidos y no aportados:** DOC-007 §11 menciona `fieldops_contexto_caso.md`, un banco de ideas y un PDF de ejemplo, que no se recibieron (RT-09).
6. **Estimaciones del comité:** EST-01 a EST-07 del CFO, ≈ 5.800 aprobaciones por día del CTIO, ≈ 1,63 M/año de C-3 y ≈ 1,9 M/año de doble conteo son cálculos del comité con fórmulas declaradas, no datos del proyecto.
7. **Proveedores y normas:** el comité no verificó la existencia ni la madurez de Jev (TypeSafe AI) ni de la Decisions API, ni la aplicabilidad de las normas citadas por el proyecto (Ley 25.326; Convenio 108+ / Ley 27.699).
8. **Unanimidad en 3/5:** ver RT-01.

## Fuentes citadas (DOC-ID y ubicación)

- **DOC-010** (deck): page:1 (pedido y 175 equivalentes), page:2 (pérdida), page:3–4 (palancas), page:5 (costo de campo, OBJ-CFO-07), page:6 (arquitectura y privacidad), page:7 ("sin doble estándar"), page:9 (gates), page:10 (escenarios y costo de esperar).
- **DOC-008** (anexos): paragraph:19 (códigos de cierre), :36, :41, :57, :60, :70, :76–97 (arquitectura), :99, :101, :111 (privacidad), :112–116 (control), :127 (autenticación), :133–140 (gremio), :144, :148 (copiloto), :158–164 (gates), :169, :172–173 (árbol de decisión, image:1); table:5, :14, :16, :17, :19, :21, :22/row:5, :23, :24/row:4, :25, :27, :29, :31.
- **DOC-009** (modelo): Supuestos!B10, B14, B26, B33, B38:B40, B53:B57; Beneficios!B27, D6:D7; KPIs!A16; Escenarios!A2, B17:B19; Inversión!B25:B26; 'Flujo y ROI'!G6.
- **Contexto:** DOC-001 §1–§6; DOC-005 §5–§8 y §10; DOC-006 §2, §4–§8; DOC-007 §3–§11.
- **Trabajo del comité:** `00_inventario_evidencias.md` (CAL, AUD, AF), `01`–`06` (dictámenes), `07` (matriz), `08` (debate) y `11_trazabilidad_fuentes.md`.
