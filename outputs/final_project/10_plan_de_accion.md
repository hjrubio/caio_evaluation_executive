# 10 · Plan de acción priorizado — `final_project`

> Evaluación simulada. Las acciones tienen dos lecturas:
> - **Bloque I:** correcciones de la **entrega académica**, a cargo del equipo del TP. Fechas según DOC-006 §8: peer review el 27/10/2026, entrega final hasta el 4/11 y defensa el 10/11.
> - **Bloque II:** condiciones del **caso** (Austral Conecta, ficticia). El "responsable" es el rol que el propio plan asigna o que el comité propone, y la "prueba de cierre" es el artefacto que el proyecto debería mostrar. En el TP, cerrarlas significa **incorporar ese artefacto o su diseño al deck o los anexos**. Lo que no pueda resolverse con datos debe declararse como supuesto a validar, con quién lo valida (DOC-007 §10).
>
> Prioridad: **P0** = antes del peer review o condición precedente; **P1** = antes de la entrega final o del gate de Q1; **P2** = antes de la producción o del gate de Q2.

## Bloque I — Entrega académica

| ID | Prioridad | Acción | Origen | Responsable | Prueba de cierre | Dependencia |
|---|---|---|---|---|---|---|
| A-01 | P0 | Unir deck y anexos en **un único PDF de menos de 10 MB**, con los anexos al final. Incluir el modelo como anexo con las tablas clave, o declarar el XLSX como material complementario si la cátedra lo admite | AUD-12; DOC-006 §2 | Equipo TP | PDF único, tamaño verificado | — |
| A-02 | P0 | Agregar el **Anexo J** (referencias, benchmarks, glosario) y un **registro de objeciones con respuestas** en el Anexo I. Puede partir de `07_matriz_objeciones.md`: al menos las 3 críticas y 6 altas con su respuesta | AUD-13; DOC-006 §6; DOC-001 §4–§5 | Equipo TP | Anexos I y J presentes | A-05, A-06 aportan contenido |
| A-03 | P0 | Corregir la frase "la exposición baja hasta USD 2,11 M" (el tramo 1 es 3,29 M, o 3,95 M con +20%) y alinear el árbol ("No libera el tramo 2") con la slide 10 ("no liberar el tramo 2 completo") | AUD-09; OBJ-CEO-03 | Equipo TP | Texto consistente en DOC-008 paragraph:172, image:1 y DOC-010 page:10 | — |
| A-04 | P0 | Corregir la promesa de privacidad de la slide 6 y del Anexo E ("solo viaja el estado del caso, nunca datos personales") para que describa el flujo real de texto, voz y foto | AUD-16; OBJ-CISO-01 | Equipo TP (lente CISO) | Slide y anexo sin contradicción | Insumo de A-20 |
| A-05 | P1 | Agregar una tabla de **decisiones reversibles e irreversibles a nivel board**: acuerdo de no despidos, contrato con contratistas (preaviso de 6 meses), proveedor de decisión, registro inmutable y contratación de 11 personas, con un criterio explícito de **detener o cancelar** el programa | AUD-14; OBJ-CEO-03; DOC-001 §1 bloque 4 | Equipo TP (lente CEO) | Tabla en el Anexo H o I | — |
| A-06 | P1 | Rehacer la columna "Origen" de Supuestos: dato interno, benchmark (con cita) o estimación del equipo, más **quién lo valida**. Agregar benchmarks o referencias para FTF 75→82%, contención del 10% y fallidas 8→5% | AUD-05; OBJ-CEO-02; DOC-006 §6 Anexo A | Equipo TP (lente CFO) | Hoja Supuestos y Anexo J | A-02 |
| A-07 | P1 | Declarar en la slide 7 el impacto sobre ~175 equivalentes de contratistas y su plan de transición; corregir "sin doble estándar" frente al acceso a la app en 2028 | OBJ-CHRO-03; C-5; C-08 del CEO; RT-10 | Equipo TP (lente CHRO) | Slide 7 consistente con DOC-008 table:24/row:4 | — |
| A-08 | P1 | Quitar la urgencia basada en "0,7 M/mes" y en las probabilidades 25/50/25 sin método; expresar el costo de demora como pérdida de VAN por desplazamiento (≈ 0,26 M/mes, ESTIMACIÓN del comité, a recalcular) y mostrar el rango y la exposición máxima | OBJ-CFO-05; RT-05 | Equipo TP (lente CFO) | Slides 1, 3 y 10 y hoja Escenarios | A-11 |
| A-09 | P1 | Unificar la base del "costo de campo por mes" de la slide 5 con la métrica norte (con o sin opex de IA) | OBJ-CFO-07; RT-04 | Equipo TP | Slide 5 con una sola definición | — |
| A-15 | P1 | Correcciones editoriales: "1.500 técnicos" en la slide 1 (AUD-01); tabla de conciliación obsoleta (AUD-10); "—" frente a 5,34 en sensibilidad (AUD-11); entradas fuera de la hoja Supuestos (AUD-19); notas del orador (AUD-20, verificar que existan en el PPTX) | AUD-01, -10, -11, -19, -20 | Equipo TP | Revisión cruzada deck–anexos–modelo | — |

## Bloque II — Condiciones del caso

| ID | Prioridad | Acción | Origen | Responsable propuesto | Prueba de cierre | Dependencia |
|---|---|---|---|---|---|---|
| A-10 | **P0 · CP-1** | Dictamen contractual sobre las contratistas: mínimos, preaviso, penalidades y pago por orden resuelta. Hoja de **realizabilidad** en el modelo (desfase, mínimos, precio por orden desde Q3 2028). Plan de capacidad mínima de terceros para picos | OBJ-CFO-01; OBJ-CEO-01; AUD-07 | COO + Compras + Legales; valida Control de Gestión | Dictamen firmado; escenario con desfase de 6 meses (VAN ≈ 16,4 según EST-04 del CFO, a recalcular) | Antes del primer desembolso |
| A-11 | **P0 · CP-2** | Desdoblar el tramo 1: Q1 = USD 1,35 M hoy; Q2 = USD 1,94 M condicionado al gate de Q1 y a A-10. Rehacer el escenario pesimista **siguiendo la decisión del gate** | OBJ-CFO-03; OBJ-CEO-03; C-2; AUD-09 | CFO (A), CEO (C) | Acta con la regla de liberación; hoja Escenarios con el camino pesimista real | A-10 |
| A-12 | P1 · CP-5 | Modelo v2: derivar la palanca 3 (hoy cargada a mano en 115.000), descontar el solapamiento de la palanca 2, hacer visible el factor del grupo de control y revisar la base de reparación (≈ 1,35 M frente a 1,21 M órdenes) | AUD-02, -03, -04; OBJ-CFO-02; RT-03 | CAIO + Control de Gestión | Fórmulas trazables; bruto recalculado | A-06 |
| A-13 | P1 · CP-5 | Completar los costos recurrentes: equipo del CAIO desde 2028, curadores, despachadores supervisores, canal, licencias y derivación unitaria (volumen × costo por decisión) | AUD-08; OBJ-CFO-04; OBJ-CTO-04; OBJ-CHRO-04; OBJ-CTIO-02 | CTO/CIO + RR.HH. + CFO | Líneas de opex 2028–2031 con cotizaciones | — |
| A-14 | P1 · CP-5 | Comparar por palanca contra la Alternativa A (sin IA) y la B (ML + reglas, LLM solo de captura); decidir qué pasa con los 9 pilotos | RT-02; OBJ-CEO-05; OBJ-CFO-06 | CAIO | Tabla en el Anexo B o C | A-12 |
| A-16 | P1 · CP-4 | Gates medibles: definir "acierto" y su contrafactual en el gate de Q1, con telemetría disponible; sumar **cobertura ≥ 50%** al gate de Q2; calcular la potencia estadística del control | AUD-18; OBJ-CTO-02; OBJ-CFO-03; OBJ-CTIO-03 | CAIO + Data Lead | Anexo G con fórmulas y tamaño muestral | — |
| A-17 | P1 · CP-9 | Plan B si no se firma el acuerdo gremial antes del gate de Q1; voz de RR.HH. en el comité | OBJ-CHRO-01 | CHRO + Relaciones Laborales | Plan de contingencia | — |
| A-18 | P2 · CP-9 | Estudio de tiempos y guarda **preventiva** de carga para las 7 visitas por día; en el piloto de Q2, medir FTF y duración por tipo de falla contra control; sensibilidad del modelo a 6,5 visitas por día (≈ −1,63 M/año, ESTIMACIÓN) | OBJ-CHRO-02; RT-06; C-3 | CHRO + COO + Control de Gestión | Resultados del piloto por tipo de falla | A-16 |
| A-19 | P2 · CP-8 | Umbral de calidad del copiloto (respuestas correctas y fundamentadas) dentro del gate de Q2; protocolo de evaluación de la visión | OBJ-CTO-03; RT-08 | CTO + curadores | Evaluación offline antes de la zona piloto | — |
| A-20 | **P0 · CP-3** | Levantar el bloqueante propuesto: diagrama de flujo por componente (dato, proveedor, jurisdicción, rol, base legal, retención); evaluación de impacto firmada; contratos y due diligence con "sin retención"; enmascaramiento verificado (≥ 500 payloads) o tratamiento como encargado | OBJ-CISO-01; OBJ-CTO-05; OBJ-CISO-03; AUD-16 | Data Lead (R), CISO (A), Legales (C); escalar a la autoridad humana de privacidad | Los cinco artefactos revisados | **Antes de cualquier dato real con terceros, incluida la sombra**; A-04 |
| A-21 | P1 | Responder la pregunta de C-1: qué componentes de Q1 envían datos personales a terceros. Si el aviso proactivo puede hacerse con plantillas sobre sistemas propios, separarlo del triage en el calendario | C-1; CISO R4 | CTO/CIO + CISO | Inventario de flujos de Q1 | A-20 |
| A-22 | P2 · CP-10 | Modelo de amenazas de la autenticación ("número de línea + dato del contrato") frente al catálogo de acciones; prueba de suplantación; criterio de salida del red teaming; plan de incidentes | OBJ-CISO-02, -05 | CISO | Informe de pruebas | — |
| A-23 | P2 · CP-4 / CP-10 | Conciliar el registro inmutable de 3 años con el derecho de supresión; definir la retención de conversaciones, audios, fotos y desvíos de técnicos | AUD-17; OBJ-CISO-04; OBJ-CHRO-05 | CISO + Data Lead | Diseño de supresión (p. ej., cifrado con borrado de clave, a evaluar) | A-20 |
| A-24 | P2 · CP-6 | ML + reglas como decisor de línea base; Jev en sombra, que solo reemplaza a la línea base si mejora la ablación; conmutación ensayada; criterios de selección de proveedor independientes de DOC-007 | C-4; OBJ-CTO-01; OBJ-CTIO-04; RT-07; AUD-15 | CTO | Informe de ablación y game day de conmutación | A-16 |
| A-25 | P2 · CP-7 | Modelo de operación: SLO, RTO/RPO, guardia 24×7, runbooks, kill switch técnico, dimensionamiento del despacho (≈ 5.800 aprobaciones por día hábil, ESTIMACIÓN del CTIO), regresión, canary y rollback; dueño del run desde 2028 | OBJ-CTIO-01, -02, -05; OBJ-CTO-05 | CTO/CIO + COO | Runbooks y prueba de carga | A-13 |
| A-26 | P1 | Validar la base del diagnóstico: tamaño y método de la muestra de cierres frente a "códigos de cierre poco confiables" | AUD-06 | Data Lead | Ficha metodológica en el Anexo A | — |
| A-27 | P2 | Explicitar el desacople entre crecimiento y costo y el efecto sobre la retención (transformación, fase 2) | OBJ-CEO-04 | CEO + CAIO | Párrafo en la slide 3 o el Anexo H | — (el CFO disiente de exigirlo en 12 meses) |
| A-28 | P1 | Si existe `fieldops_contexto_caso.md` u otro documento aludido en DOC-007 §11, aportarlo o declarar que no existe | RT-09 | Equipo TP | Archivo o declaración | — |

## Secuencia mínima sugerida para el 27/10

Las acciones de una línea o un párrafo pueden hacerse en el día, y las demás pueden declararse como "en curso" en el registro de objeciones:

1. A-01: PDF único.
2. A-03 y A-04: contradicciones visibles.
3. A-15: correcciones editoriales.
4. A-02: Anexo J y registro de objeciones con las críticas y altas.
5. A-07 y A-09: slides 5 y 7.

Para la entrega final del 4/11 quedan A-05, A-06, A-08, A-10 a A-14, A-16, A-17 y A-21, y para la defensa, el resto.
