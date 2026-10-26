# Puntuación, bloqueantes y decisión

| Rol | Peso | Eje |
| --- | ---: | --- |
| CEO | 20% | Estrategia, valor, oportunidad |
| CTO | 15% | Arquitectura, IA apropiada, escalabilidad |
| CTIO | 15% | Integración, SLO, continuidad, operabilidad |
| CISO | 20% | Seguridad, privacidad, regulación, control |
| CHRO | 10% | Cambio, capacidades, ética laboral |
| CFO | 20% | ROI, TCO, escenarios, caja |

Escala: 0 = inviable o riesgo extremo demostrado; 1 = severamente deficiente; 2 = brechas mayores; 3 = viable con condiciones; 4 = sólido con mejoras; 5 = convincente y validado. `NO_EVALUABLE` cuando faltan datos críticos; **no equivale a cero**.

Promedio = SUMA(score_i × peso_i) / SUMA(pesos evaluables). Mostrar cobertura de ponderación y advertir si no cubre el 100%. Con cobertura inferior al 100%, el total es **parcial y no habilita aprobación final**.

Referencia orientativa con cobertura 100%: >= 4.0 favorable, >= 3.0 condicionado, < 3.0 reformular/rechazar según riesgos. No decidir automáticamente por puntaje.

Bloqueos: incumplimiento legal material verificado, exposición crítica de datos sin controles, imposibilidad operativa grave sin mitigación, hipótesis financiera esencial refutada o ausencia de pruebas mínimas para despliegue crítico. El CISO puede marcar `BLOQUEANTE_PROPUESTO`, pero el orquestador registra la evidencia y recomienda escalamiento a la autoridad humana correspondiente. No existe veto legal real del agente. Un bloqueante no resuelto impide recomendar `APROBADO`.

Una objeción grave basada solo en hipótesis no es automáticamente bloqueo verificado; debe quedar como riesgo crítico pendiente de comprobación.
