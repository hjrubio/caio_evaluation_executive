# 08 · Red team, debate cruzado y derecho a réplica (R2–R3) — `final_project`

> Evaluación simulada. Conducen el Orquestador (sin voto) y el Red Team (sin voto). **No se fabrican respuestas del proponente:** el equipo de FieldOps IA no participó en esta sesión. Donde un rol "responde" a otro, la respuesta se construye **solo** con el contenido de su propio dictamen de R1 y con documentos citados. Ningún argumento se presenta como evidencia nueva.

## 1. Verificación del auditor sobre los dictámenes de R1

| Control | Resultado |
|---|---|
| Seis dictámenes presentes y separados | Sí: `01_CEO.md` … `06_CFO.md`, redactados por subagentes aislados en paralelo |
| Citas con DOC-ID y locador | Sí. Muestreo de 8 citas contrastadas con la fuente (DOC-008 paragraph:127, paragraph:172, table:25/row:4; DOC-009 KPIs!A16, Supuestos!B33, Escenarios!A2; DOC-010 page:7, page:10): las 8 coinciden. El resto de las citas no se contrastó una por una |
| Cifras propias etiquetadas | Sí. CFO (EST-01 a EST-07), CTIO (≈ 5.800 aprobaciones/día) y CHRO (≈ 5.600 visitas por formación) están marcadas como ESTIMACIÓN del comité, con fórmula |
| Verificación de un hallazgo nuevo del CFO | El gate de Q2 exige "resuelve sin visita ≥ 20% de los reclamos que **atiende**" (DOC-008 paragraph:159; DOC-009 KPIs!A16) y no mide la cobertura del 50% (Supuestos!B26). **Confirmado** |
| Verificación de un hallazgo nuevo del CISO | DOC-008 table:22/row:5 dice "sin entrenamiento con datos de Austral Conecta por contrato"; no menciona retención. DOC-007 §7.8 pide "sin retención ni entrenamiento". **Confirmado** |
| Verificación de un hallazgo nuevo del CHRO | DOC-010 page:7 dice "Mismos pilotos, herramientas, formación y criterios de calidad: sin doble estándar"; DOC-008 table:24/row:4 da a los contratistas "acceso a la app y al copiloto desde 2028". **Confirmado** |
| Normas citadas | Ningún rol afirmó la aplicabilidad de normas no citadas por el proyecto. Las citadas (Ley 25.326; Convenio 108+ / Ley 27.699) quedan como afirmaciones del proponente, no verificadas |

## 2. Red team: desafíos al conjunto (RT)

| ID | Desafío | Evidencia | Pedido |
|---|---|---|---|
| RT-01 | **Convergencia sospechosa de puntajes.** Los seis roles dieron 3/5 de forma independiente. Puede ser un juicio genuino ("viable con condiciones"), pero también un efecto de anclaje: los seis recibieron el mismo inventario del auditor, con 20 hallazgos priorizados. El riesgo es que el comité refleje la agenda del auditor y no seis lentes distintas | Los seis dictámenes citan AUD-xx; sin embargo, cada rol aportó al menos un hallazgo que no estaba en el inventario (ver §1) | En R4, cada rol debe justificar su voto con su propia evidencia y explicitar si coincide con la mayoría por razones propias |
| RT-02 | **Sesgo pro-IA y alternativas sin IA.** De las cinco palancas, al menos dos pueden capturarse en parte sin IA generativa. **Alternativa A (sin IA):** aviso proactivo con plantillas, confirmación de turno y franja corta mediante optimización clásica de agenda (palanca 2); checklist de instalación con foto obligatoria y auditoría muestral humana (palanca 4); reglas de telemetría para reinicio remoto (parte de la palanca 1); contrato por orden resuelta desde ya. **Alternativa B (IA acotada):** LLM solo para captura, ML + reglas como decisor principal y Jev solo como contendiente en modo sombra. El plan no compara ninguna de las dos | DOC-010 page:4; DOC-008 paragraph:83, paragraph:97, table:25 | Para cada palanca: costo, efecto y porción del beneficio atribuible a la IA frente a la Alternativa A. El comité **no cuantifica** esas alternativas por falta de datos (SIN_EVIDENCIA) |
| RT-03 | **Doble conteo.** Con los solapamientos estimados (palanca 2 sobre visitas remanentes, palanca 3 no derivada y grupo de control no visible), el bruto baja ≈ 1,9 M/año | AUD-02 a AUD-04; `06_CFO.md` EST-02 | Modelo v2 |
| RT-04 | **Definiciones inconsistentes de "costo de campo".** La métrica norte (40,3) incluye el opex de IA, pero el "costo de campo por mes" de la slide 5 (3,94 M = (57,0 − 9,7)/12) lo excluye. Son dos bases distintas en la misma tabla | DOC-010 page:5; DOC-008 paragraph:36 | Unificar la definición o aclararla en la tabla |
| RT-05 | **Probabilidades sin fundamento usadas como presión.** El 25/50/25 no tiene método; con él se calcula un "costo de esperar" que sirve de argumento de urgencia en tres slides | DOC-009 Supuestos!B53:B57; DOC-010 page:1, page:3, page:10 | Explicar el criterio de las probabilidades; ver OBJ-CFO-05 |
| RT-06 | **Efecto mezcla no modelado.** Si el triage retira los casos fáciles (reinicios, configuración), las visitas que quedan son más difíciles. Entonces el FTF de base de esas visitas baja (la meta de 82% se vuelve más exigente) y la duración por visita sube (las 7 visitas por día de la planta propia se vuelven menos sostenibles). Afecta a la vez a las palancas 1 y 3 y al mecanismo de ahorro | Señalado por separado en `06_CFO.md` (OBJ-CFO-02, opinión) y `05_CHRO.md` (OBJ-CHRO-02) | Medir FTF y duración por tipo de falla en el piloto de Q2, contra control |
| RT-07 | **Seguir el instructivo no prueba idoneidad.** La elección de Jev como decisor principal y de la Decisions API como respaldo coincide con lo prescripto en DOC-007 §7.4, un instructivo del propio curso o equipo para un asistente de IA. Que el contexto lo recomiende no demuestra que sea la mejor opción para un sistema crítico | DOC-007 §7.4; DOC-008 paragraph:82 | Criterios de selección de proveedor (DOC-006 §6 Anexo C) independientes del instructivo |
| RT-08 | **Riesgo de alucinación con impacto económico.** El copiloto con manuales sostiene la palanca de mayor valor (3,68 M) y no tiene métrica de fundamentación; la revisión es semanal y muestral | DOC-008 paragraph:148; `02_CTO.md` OBJ-CTO-03 | Umbral de calidad del copiloto como condición de gate, no solo de adopción |
| RT-09 | **Afirmaciones de lectura.** Revisé si algún artefacto afirma haber leído la ChatGPT Library: ninguno lo hace. Los documentos aludidos en DOC-007 §11 (`fieldops_contexto_caso.md`, banco de ideas, PDF de ejemplo) **no fueron aportados**; los anexos funcionan como fuente de verdad del caso. No se detectan documentos del proyecto omitidos | `context_review.json` access_note; DOC-007 §11 | Si existe `fieldops_contexto_caso.md`, aportarlo; podría contener el origen de los supuestos |
| RT-10 | **Narrativa "sin despidos" vs. impacto real.** El titular "sin despidos propios" es veraz, pero el plan retira el equivalente a 175 puestos de terceros. Ante un board, la omisión de ese costo social puede leerse como encubrimiento | DOC-010 page:1, page:7; DOC-008 paragraph:133 | Declarar el impacto en terceros en la slide 7 y el plan para esas personas |

## 3. Controversias entre roles

### C-1 · CISO vs. CTIO y CEO: alcance del bloqueante y calendario de Q1

- **Planteo (Orquestador):** el CISO propone que no se procesen datos reales de clientes con proveedores externos, **incluido el modo sombra de Q1**, hasta cerrar OBJ-CISO-01. El CTIO ya considera comprimido el calendario de Q1 (OBJ-CTIO-03). El CEO depende del quick win del aviso proactivo en Q1 (DOC-008 table:4/row:4). ¿El bloqueante hace inviable el gate de Q1?
- **Posición CISO (de `04_CISO.md`):** el bloqueante no agrega una condición nueva. El plan ya exige una evaluación de impacto firmada antes de cada salida a producción (DOC-008 paragraph:169) y la programa para las semanas 3–4 (table:31/row:8). Lo único que pide es que esa evaluación contenga el diagrama de flujo de datos y una afirmación de privacidad verdadera.
- **Posición CTIO (de `03_CTIO.md`):** el problema de calendario es anterior al bloqueante. Integración de FSM y CRM, gateway, registro, MLOps, aviso y sombra en un trimestre, con equipo contratado en diciembre y enero (table:5, table:27/row:2).
- **Posición CEO:** su dictamen de R1 no trata el calendario de Q1 ni el bloqueante, así que no se le atribuye una posición. Dato registrado por el Orquestador: el beneficio bruto de Q1 es 0,10 M (DOC-009 Beneficios!B27). El costo de caja de una demora en Q1 es bajo; el costo se concentra en el corrimiento de la rampa.
- **Lectura del Orquestador:** el desacuerdo es real pero acotado. El aviso proactivo puede no requerir un LLM externo (plantillas y datos de agenda), lo que permitiría avanzar en Q1 sin tocar el bloqueante. El modo sombra del triage sí requiere procesar conversaciones reales. **Pregunta abierta al proponente:** ¿qué componentes de Q1 envían datos personales a terceros?
- **Estado:** ABIERTA. Disenso preservado: el CISO mantiene el alcance; el CTIO pide un plan de integración y reconoce que el bloqueante no es la causa principal del riesgo de calendario.

### C-2 · CFO vs. CEO: urgencia y estructura del tramo 1

- **Planteo:** el deck presiona con "cada mes sin decidir: −USD 0,7 M" y pide aprobar 3,29 M de una vez. El CFO estima que la pérdida real por mes de demora es ≈ 0,26 M de VAN (OBJ-CFO-05) y propone desdoblar el tramo 1 (C-CFO-02).
- **Posición CFO:** si el gate de Q1 falla, hoy no hay consecuencia sobre los 1,94 M de Q2, que ya estarían aprobados (DOC-008 table:21/row:2, paragraph:181). Desdoblar el tramo cuesta poco y protege 1,94 M.
- **Posición CEO (de `01_CEO.md`):** pide un criterio de cancelación y la distinción reversible/irreversible (OBJ-CEO-03), compatibles con el desdoblamiento. También considera que los 0,7 M/mes son "una cota alta" porque no están descontados (HS-07 y pregunta 6).
- **Lectura del Orquestador:** **convergencia.** CEO y CFO coinciden en que el costo de esperar está sobredimensionado y en que hacen falta más puntos de salida. No queda un desacuerdo de fondo entre ambos sobre este punto; queda por ver si el CEO acepta desdoblar el tramo 1 (R4).
- **Estado:** ABIERTA. Convergencia en que se desdoble el tramo 1 o se ate Q2 al gate de Q1.

### C-3 · CHRO vs. CFO: las 7 visitas por día son a la vez mecanismo de ahorro y riesgo laboral

- **Planteo:** el ahorro solo se materializa si la planta propia sostiene 7 visitas por día (DOC-008 paragraph:60, paragraph:70). El CHRO advierte que, con casos más difíciles y una ventana de 20 minutos, esa meta puede intensificar el trabajo (OBJ-CHRO-02).
- **ESTIMACIÓN del Orquestador** (ilustrativa, no del proponente): si la planta propia bajara a 6,5 visitas por día, 400 × 0,5 × 255 = 51.000 visitas por año pasarían a comprarse a terceros, ≈ USD 1,63 M/año menos de ahorro (≈ 19% del neto a régimen).
- **Posición CFO:** el control de ocupación está bien diseñado (DOC-008 paragraph:70), pero detecta el problema después de que ocurrió, no lo previene.
- **Posición CHRO:** proteger la meta con presión sobre los técnicos violaría el espíritu del acuerdo gremial (la IA no evalúa desempeño, DOC-008 paragraph:138). Hacen falta un estudio de tiempos y guardas de carga.
- **Lectura del Orquestador:** es el punto donde dos lentes convergen sobre el mismo supuesto (RT-06). Ninguno de los dos roles puede cerrarlo sin datos del piloto de Q2.
- **Estado:** ABIERTA. Se agrega al plan de acción como prueba de Q2.

### C-4 · CTO vs. CTIO: ¿qué rol tiene Jev?

- **Planteo:** el CTO cuestiona que Jev haga falta frente a ML + reglas (OBJ-CTO-01). El CTIO cuestiona que la conmutación entre proveedores no está ensayada (OBJ-CTIO-04).
- **Lectura del Orquestador:** no hay contradicción. Ambas objeciones apuntan a la misma salida: usar **ML + reglas como decisor de línea base** y a Jev como contendiente en modo sombra, que reemplaza a la línea base solo si demuestra una mejora medida. Eso reduce además la superficie de datos del CISO (OBJ-CISO-03).
- **Estado:** ABIERTA, con convergencia técnica entre CTO, CTIO y CISO.

### C-5 · CEO vs. CHRO: ¿es "sin despidos" una ventaja o un riesgo de narrativa?

- **Planteo:** el CEO usa la política de no despidos como fortaleza para el board (AP de `01_CEO.md`). El CHRO advierte que el costo humano se traslada a ~175 técnicos equivalentes de contratistas, sin plan para esas personas, y que la slide 7 contradice al anexo F (OBJ-CHRO-03; RT-10).
- **Lectura del Orquestador:** ambos tienen razón en su eje. La política protege a la planta propia y facilita el acuerdo gremial, pero la narrativa ante el board debe declarar el impacto sobre terceros para no quedar expuesta en la defensa.
- **Estado:** ABIERTA. Disenso de matiz preservado.

## 4. Derecho a réplica (R3)

| Elemento | Situación |
|---|---|
| Aclaraciones del proponente | **Ninguna** recibida en esta sesión |
| Evidencia nueva | **Ninguna** |
| Efecto | Las 30 objeciones quedan en estado `ABIERTA`. Ninguna se considera respondida por inferencia. El `BLOQUEANTE_PROPUESTO` (OBJ-CISO-01) queda **no resuelto** |
| Preguntas abiertas al proponente | Las de las secciones "Preguntas difíciles" de cada dictamen, más: (1) ¿qué componentes de Q1 envían datos personales a terceros? (C-1); (2) ¿existe `fieldops_contexto_caso.md` con el origen de los supuestos? (RT-09); (3) ¿cuánto del beneficio se obtiene sin IA? (RT-02) |
