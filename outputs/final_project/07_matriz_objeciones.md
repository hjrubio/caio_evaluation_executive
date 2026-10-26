# 07 · Matriz de objeciones — `final_project` (FieldOps IA)

> Evaluación simulada. Consolidado por el Orquestador y el Relator (sin voto) a partir de los seis dictámenes de R1 (`01_CEO.md` … `06_CFO.md`) y del red team (`08_debate_cruzado.md`). No se fusionan objeciones en un único texto: cada rol conserva la suya y se agrupan por tema.
>
> **Estado R3:** el proponente **no aportó réplicas ni evidencia nueva** en esta sesión. Por eso ninguna objeción figura como respondida o mitigada. El estado es `ABIERTA` salvo indicación expresa.

## 1. Resumen por severidad

| Severidad | Cantidad | IDs |
|---|---:|---|
| crítica | 3 | OBJ-CEO-01, OBJ-CFO-01, OBJ-CISO-01 (`BLOQUEANTE_PROPUESTO`, de alcance acotado) |
| alta | 18 | OBJ-CEO-02, OBJ-CEO-03, OBJ-CTO-01, OBJ-CTO-02, OBJ-CTO-03, OBJ-CTO-05 (sube en R4), OBJ-CTIO-01, OBJ-CTIO-02, OBJ-CTIO-03, OBJ-CTIO-04, OBJ-CISO-02, OBJ-CISO-03, OBJ-CHRO-01, OBJ-CHRO-02, OBJ-CHRO-03, OBJ-CFO-02, OBJ-CFO-03, OBJ-CFO-04 |
| media | 10 | OBJ-CEO-04, OBJ-CEO-05, OBJ-CTO-04, OBJ-CTIO-05, OBJ-CISO-04, OBJ-CISO-05, OBJ-CHRO-04, OBJ-CHRO-05, OBJ-CFO-05, OBJ-CFO-06 (nueva en R4) |
| baja | 1 | OBJ-CFO-07 (nueva en R4) |

**Cambios en R4** (cada rol revisó su dictamen después de leer esta matriz y `08`): OBJ-CTO-05 sube de media a alta, porque la afirmación "solo viaja el estado del caso" es incompatible con los componentes de texto libre, voz y visión, y esa definición es condición previa del modo sombra. El CFO agrega OBJ-CFO-06 (adopta RT-02) y OBJ-CFO-07 (adopta RT-04). No se retiró ninguna objeción. Total: 32, todas `ABIERTA`.

## 2. Matriz por tema

### T1 · Realizabilidad del ahorro en la factura de terceros

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CFO-01 | CFO | crítica | El 96% del beneficio bruto depende de que cada visita evitada deje de facturarse a USD 32 desde Q1 2027. No constan mínimos, preaviso ni penalidades, y el contrato por orden resuelta (desde mediados de 2028, "compensa en parte el menor volumen") no está modelado | DOC-008 table:25, paragraph:144; DOC-009 Supuestos!B14; AUD-07 | Informe de Legales y Compras sobre los contratos vigentes; hoja de realizabilidad (desfase, mínimos, precio por orden desde Q3 2028); conciliación de la factura de Q1 2027 | COO + Compras + Legales; valida Control de Gestión | ABIERTA |
| OBJ-CEO-01 | CEO | crítica | Mismo mecanismo, desde la estrategia: sin respaldo contractual, el payback de Q1 2028 queda en duda. Concentrar la baja (−29%) en contratistas puede llevar a que suban tarifas, degraden calidad o se retiren, y no hay plan de capacidad para picos | DOC-008 paragraph:57, table:25; AUD-07 | Dictamen contractual antes del tramo 1; plan de capacidad mínima de terceros para picos | COO + Compras | ABIERTA |

### T2 · Origen y cálculo de los supuestos del beneficio

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CFO-02 | CFO | alta | Origen circular de los supuestos ("Anexo B" ↔ modelo). Además: palanca 3 cargada a mano; el factor 0,9 del grupo de control no aparece en fórmulas; la palanca 2 se calcula sobre visitas ya eliminadas por otras palancas; la palanca 1 toma el 10% de todas las órdenes y no solo de las de reparación. Estimación del comité: neto a régimen 6,84 y VAN ≈ 15,2 | DOC-009 Supuestos!D5:D59, B33, Beneficios!C4:C6; AUD-02 a AUD-06 | Modelo v2 con origen tipificado, fórmula para la palanca 3, factor de control explícito y palanca 2 calculada sobre las visitas remanentes | CAIO + Data Lead; valida Control de Gestión | ABIERTA |
| OBJ-CEO-02 | CEO | alta | La evidencia de la oportunidad es débil: no hay benchmarks ni resultados de los 9 pilotos, y la muestra de cierres no tiene tamaño ni método | DOC-008 paragraph:17, paragraph:19, paragraph:30, paragraph:190–193 | Clasificar cada supuesto; documentar la muestra; publicar los resultados de los pilotos o declarar que no existen | CAIO | ABIERTA |

### T3 · Escenarios, gates y exposición

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CFO-03 | CFO | alta | El pesimista gasta todo el plan, contra la decisión preacordada; la exposición está mal expresada ("hasta 2,11 M"); el gate de Q2 no mide cobertura (con 5% de contención igual se aprueba); un gate de Q1 fallido no tiene consecuencias sobre los 1,94 M de Q2. Estimación del comité: en el camino pesimista real el VAN queda entre −1,3 y +1,3 y la exposición ronda USD 4 M | DOC-009 Escenarios!A2, KPIs!A16; DOC-008 paragraph:172, image:1, table:21; AUD-09 | Pesimista con el árbol real; exposición máxima en la slide 10; condición de cobertura en el gate de Q2; desdoblar el tramo 1 (Q2 atado al gate de Q1) | CAIO + analista de valor; valida CFO | ABIERTA |
| OBJ-CEO-03 | CEO | alta | No hay escenario de cancelación ni distinción reversible/irreversible para las decisiones del board (acuerdo de no despidos, contratos, proveedor, registro inmutable) | DOC-001 §1 bloque 4; DOC-008 paragraph:99; AUD-14 | Criterio explícito de "detener"; tabla de decisiones reversibles e irreversibles con tratamiento diferenciado | CAIO + CEO | ABIERTA |
| OBJ-CFO-05 | CFO | media | El "costo de esperar" (0,7 M/mes) está sobredimensionado. Si todo el proyecto se corre un mes, se pierden ≈ 0,26 M de VAN | DOC-009 Escenarios!B17:B19 | Reexpresar el costo de esperar como pérdida de VAN por desplazamiento, o justificar el horizonte truncado | CAIO + CFO | ABIERTA |

### T4 · Datos personales y proveedores externos

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CISO-01 | CISO | crítica · `BLOQUEANTE_PROPUESTO` | "Solo viaja el estado del caso" es incompatible con un LLM por WhatsApp y voz, voz a texto, visión por foto y copiloto. No se dice dónde corren ni cómo se enmascara texto libre, audio o imagen. **Alcance:** impide procesar datos reales de clientes con proveedores externos (incluido el modo sombra) hasta el cierre; no bloquea la aprobación del plan ni del tramo 1 | DOC-010 page:6–7; DOC-008 paragraph:80, paragraph:111, table:16, table:22/row:5, table:23/row:6; AUD-16 | Diagrama de flujo de datos por componente; afirmación del deck corregida; enmascaramiento verificado sobre ≥ 500 payloads; evaluación de impacto firmada | Data Lead (R), CISO (A), Legales (C) | ABIERTA (bloqueante no resuelto) |
| OBJ-CTO-05 | CTO | alta (media en R1) | Falta definir dónde se alojan los componentes que tocan datos personales y quién opera la plataforma desde 2028 | DOC-008 table:16, table:22/row:5 | Diagrama de despliegue y dueño del run | CTO/CIO + CAIO | ABIERTA |
| OBJ-CISO-03 | CISO | alta | Proveedores en acceso anticipado y beta. Solo "sin entrenamiento", no "sin retención" (DOC-007 §7.8). Sin due diligence, ubicación ni SLA. La conmutación duplica la superficie de datos | DOC-008 paragraph:82, table:22/row:5, table:31/row:6; DOC-007 §7.4, §7.8 | Due diligence y contratos con no retención, ubicación, subencargados y auditoría antes de datos reales; plan de salida probado | CTO/CIO (R), Legales y CISO | ABIERTA |
| OBJ-CISO-02 | CISO | alta | Autenticación del cliente ("número de línea más un dato del contrato") vulnerable a suplantación en un canal que propone acciones remotas de red y reprograma visitas. Riesgo hipotético, no demostrado | DOC-008 paragraph:127, table:19/row:2–3 | Autenticación escalonada según la opción elegida; casos de suplantación en el red teaming del gate de Q1 | Conversational designer + PM técnico; A: CISO | ABIERTA |
| OBJ-CISO-04 | CISO | media | El registro inmutable de 3 años choca con el derecho de supresión; falta la retención de conversaciones, audios, fotos y desvíos | DOC-008 paragraph:89–90, table:17, table:23/row:7 | Contenido personal fuera de la cadena (borrado criptográfico); tabla de retención; prueba de supresión de punta a punta | Data Lead; A: CISO; C: Legales | ABIERTA |
| OBJ-CISO-05 | CISO | media | El red teaming no tiene criterio de salida; falta definir "incidente grave", el plan de respuesta, el presupuesto de seguridad y el procedimiento del veto | DOC-008 paragraph:131, paragraph:163, table:23/row:9; DOC-009 Inversión!A4:A12 | Criterio "0 hallazgos críticos/altos abiertos" en el gate de Q1; matriz de severidad; simulacro; línea de presupuesto; reglamento del veto | CISO; CAIO | ABIERTA |

### T5 · Arquitectura, evaluación técnica y capa de decisión

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CTO-01 | CTO | alta | No se justifica Jev (con respaldo en Decisions API) frente a una política determinística sobre el ML, aunque el propio plan acepta ML + reglas como respaldo | DOC-008 paragraph:81–83, paragraph:97; DOC-007 §7.4 | Prueba comparativa en modo sombra (Jev vs. ML + reglas) con criterios de selección; ML + reglas como línea base | CTO/CIO + PM técnico | ABIERTA |
| OBJ-CTO-02 | CTO | alta | Gate de Q1 no medible ("acierta ≥ 80%" sin definición ni contrafactual; etiquetas de cierre poco confiables; modelo evaluado sin telemetría). Gate de Q2 sin cálculo de potencia | DOC-008 paragraph:19, paragraph:81, paragraph:158, paragraph:166, table:27/row:6; AUD-18 | Definición operativa del acierto; protocolo de etiquetado; cálculo de tamaño muestral | Data Lead + analista de valor | ABIERTA |
| OBJ-CTO-03 | CTO | alta | El copiloto (RAG) y la visión no tienen protocolo de evaluación; sostienen ≈ 44% del bruto; el copiloto sale antes que la base curada | DOC-008 paragraph:148, paragraph:162, table:27; DOC-009 Beneficios!D6:D7 | Conjunto de evaluación, métricas de fundamentación y precisión, umbral de calidad en el gate de Q2 | PM técnico + curadores | ABIERTA |
| OBJ-CTO-04 | CTO | media | Sin costo por transacción ni SLO técnicos; prompts y esquemas no versionados; sin procedimiento ante un cambio del modelo del proveedor | DOC-009 Supuestos!B15, B38:B40; DOC-008 paragraph:96 | Derivación unitaria del opex; SLO de latencia; versionado de prompts y esquemas | PM técnico | ABIERTA |

### T6 · Operación, continuidad y capacidad

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CTIO-01 | CTIO | alta | No hay modelo de operación: faltan SLO, SLA de proveedores, RTO/RPO, guardia 24×7, runbooks y un mecanismo técnico para apagar el agente. Bloquea el paso a producción, no el tramo 1 | DOC-008 paragraph:96, paragraph:101, table:23/row:9 | Catálogo de SLO; RACI operativo; guardia; runbooks; apagado probado | CTO/CIO + PM técnico | ABIERTA |
| OBJ-CTIO-02 | CTIO | alta | Capacidad no dimensionada: picos, concurrencia, despachadores (≈ 5.800 aprobaciones por día, estimación), derivaciones al contact center, comportamiento al alcanzar topes de gasto | DOC-008 table:19/row:3, table:22/row:6; DOC-009 Flujo y ROI!G6 | Modelo de capacidad y dotación; prueba de carga; política al alcanzar el tope | COO + PM técnico | ABIERTA |
| OBJ-CTIO-03 | CTIO | alta | Calendario de Q1–Q2 comprimido. El gate de Q1 valida un modelo sin telemetría; no está probada la capacidad de las APIs del FSM | DOC-008 table:27, table:31, paragraph:166 | Plan de integración con hitos semanales; prueba de APIs del FSM; gate de Q1 con el modelo de producción | CTO/CIO | ABIERTA |
| OBJ-CTIO-04 | CTIO | alta | Conmutación entre proveedores no ensayada; calidad del modo degradado no medida; sin cobertura de fallas del gateway, del motor de reglas, del FSM, del CRM ni del canal | DOC-008 paragraph:82, paragraph:97, table:22/row:9; DOC-007 §7.7 | Análisis de modos de falla (FMEA); prueba de conmutación; modo sombra del respaldo | PM técnico | ABIERTA |
| OBJ-CTIO-05 | CTIO | media | Gestión de cambios y rollback incompleta para modelos y reglas | DOC-008 paragraph:95, paragraph:125 | Regresión con casos de referencia, despliegue gradual por zona, rollback < 1 h | PM técnico + COO | ABIERTA |

### T7 · Personas, gremio y contratistas

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CHRO-01 | CHRO | alta | El acuerdo gremial es condición del gate de Q1, con ~3 meses y sin plan B; RR.HH. aprueba el acuerdo pero no vota en el comité de IA | DOC-008 paragraph:136–142, table:27/row:6, paragraph:105–107 | Escenario "acuerdo no firmado al 31/03"; qué avanza sin acuerdo | RR.HH. + Change Lead | ABIERTA |
| OBJ-CHRO-02 | CHRO | alta | Intensificación de la planta propia: la meta de 7 visitas/día se mantiene fija aunque la IA retire los casos simples | DOC-008 paragraph:30, paragraph:60, paragraph:70 | Estudio de tiempos por tipo de falla; guardas de carga | RR.HH. + COO | ABIERTA |
| OBJ-CHRO-03 | CHRO | alta | El costo humano recae en ~175 técnicos equivalentes de contratistas sin plan para las personas. "Sin doble estándar" (deck) contradice el acceso a la app recién en 2028 (anexo) | DOC-010 page:7; DOC-008 table:24/row:4, table:25 | Plan para trabajadores de contratistas; corregir la inconsistencia | RR.HH. + COO + Compras | ABIERTA |
| OBJ-CHRO-04 | CHRO | media | El costo de la transición no está derivado (horas de formación, reemplazo de curadores, costos de personas desde 2028) | DOC-009 Inversión!B12:E12, B25:B26 | Presupuesto de transición derivado | RR.HH. + CFO | ABIERTA |
| OBJ-CHRO-05 | CHRO | media | La adopción se mide como uso, no como confianza; el gate cultural ("≥ 8/10") no está en el anexo G; no hay controles técnicos sobre los datos de los técnicos | DOC-010 page:7, page:9; DOC-008 paragraph:140, paragraph:153 | Instrumento de confianza con línea base; controles de acceso y agregación | Change Lead + Data Lead | ABIERTA |

### T8 · Estrategia y alternativas

| ID | Rol | Sev. | Objeción (síntesis) | Soporte | Mitigación / evidencia de cierre | Responsable propuesto | Estado |
|---|---|---|---|---|---|---|---|
| OBJ-CEO-04 | CEO | media | Eficiencia muy bien gobernada, pero con poca transformación del modelo de negocio ("transformar, no parchear") | DOC-006 §4; DOC-005 D1; DOC-010 page:3–4 | Explicitar el desacople entre crecimiento y costo, y el efecto sobre retención | CEO + CAIO | ABIERTA |
| OBJ-CEO-05 | CEO | media | No se comparan alternativas sin IA por palanca ni se dice qué se deja de financiar (9 pilotos) | DOC-008 paragraph:17; DOC-010 page:4 | Tabla de alternativas por palanca; decisión sobre los pilotos | CAIO | ABIERTA |
| OBJ-CFO-04 | CFO | alta | Costos recurrentes incompletos (personas desde 2028, canal, licencias) y sin derivación unitaria; cada USD 1 M/año omitido resta ≈ 2,6 M de VAN | DOC-009 Supuestos!B38:B40; DOC-008 table:5, paragraph:146; AUD-08 | Línea de personas y operación 2028–2031; cotizaciones | CTO/CIO + RR.HH. + CFO | ABIERTA |
| OBJ-CFO-06 | CFO (R4) | media | El grupo de control mide la IA contra el proceso actual, no contra una alternativa barata sin IA; el beneficio atribuible a la IA podría ser menor (NO_EVALUABLE) | RT-02; DOC-008 paragraph:83, paragraph:97, table:25 | Tabla por palanca con costo y efecto de la Alternativa A (sin IA) | CAIO + Control de Gestión | ABIERTA |
| OBJ-CFO-07 | CFO (R4) | baja | El "costo de campo por mes" de la slide 5 (3,94 M) excluye el opex de IA y la métrica norte de la misma tabla lo incluye (≈ 4,05 M con opex, ESTIMACIÓN) | RT-04; DOC-010 page:5; DOC-008 paragraph:36 | Unificar la base de cálculo | CAIO | ABIERTA |

## 3. Observaciones del red team (sin voto)

Se registran en `08_debate_cruzado.md` §2 (RT-01 a RT-10). No son objeciones de voto; dos de ellas generan pedidos de evidencia que se suman al plan de acción (RT-02, alternativas sin IA; RT-06, efecto mezcla).

## 4. Hallazgos del auditor sin objeción de rol

| AUD | Tema | Tratamiento |
|---|---|---|
| AUD-01 | "1.500 técnicos: en domicilio, 400 + 600" en la slide 1 | Corrección de redacción; acción A-15 |
| AUD-10 | Tabla de conciliación con una versión vieja del deck | Eliminar o actualizar; acción A-15 |
| AUD-11 | "—" vs. 5,34 en la sensibilidad | Corrección; acción A-15 |
| AUD-12, AUD-13 | Único PDF, Anexo J, registro de objeciones | Cumplimiento de consigna; acciones A-01 y A-02 |
| AUD-19, AUD-20 | Entradas fuera de la hoja Supuestos; notas del orador | Higiene; acción A-15 |
