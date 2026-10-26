"""Recálculo independiente del Auditor de Evidencias (no modifica la planilla fuente)."""
q_gross = [0.1, 0.6, 1.5, 2.2] + [10.06 / 4] * 4 + [10.26 / 4] * 4 + [10.47 / 4] * 4 + [10.68 / 4] * 4
q_opex = [-0.1, -0.2, -0.22, -0.28] + [-1.30 / 4] * 4 + [-1.36 / 4] * 4 + [-1.37 / 4] * 4 + [-1.48 / 4] * 4
q_inv = [-1.35, -1.94, -1.29, -0.82] + [0] * 4 + [-0.3 / 4] * 4 + [-0.3 / 4] * 4 + [-0.1 / 4] * 4
flows = [g + o + i for g, o, i in zip(q_gross, q_opex, q_inv)]
t = [(k + 0.5) / 4 for k in range(20)]


def npv(rate, fl):
    return sum(f / (1 + rate) ** tt for f, tt in zip(fl, t))


def irr_q(fl):
    lo, hi = 0.0, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        v = sum(f / (1 + mid) ** k for k, f in enumerate(fl))
        lo, hi = (mid, hi) if v > 0 else (lo, mid)
    return (1 + mid) ** 4 - 1


print('VAN base 16%:', round(npv(0.16, flows), 3))
print('TIR anual base:', round(irr_q(flows), 3))
print('Neto 24m:', round(sum(flows[:8]), 3))
print('VAN si el flujo se descuenta a fin de año (anual, t=1..5):',
      round(sum(f / 1.16 ** (k + 1) for k, f in enumerate([-1.80, 8.76, 8.60, 8.80, 9.10])), 3))

pes = [g * 0.5 + (o + i) * 1.2 for g, o, i in zip(q_gross, q_opex, q_inv)]
print('VAN pesimista (gasto completo):', round(npv(0.16, pes), 3))
# Pesimista con la decisión preacordada: sin tramo 2 (Q3-Q4 sin inversión) y beneficio limitado a triage + aviso
pes_gate = list(pes)
pes_gate[2] = q_gross[2] * 0.5 + q_opex[2] * 1.2
pes_gate[3] = q_gross[3] * 0.5 + q_opex[3] * 1.2
print('Exposición si no se libera tramo 2 (inversión tramo 1 x1.2):', round((1.35 + 1.94) * 1.2, 2))

# Solapamientos entre palancas (estimación del comité, no del proponente)
visits = 1_784_000
lev1, lev3, lev4 = 120_000, 115_000, 24_000
lev2_model = round(visits * 0.03, -2)
lev2_adj = (visits - lev1 - lev3 - lev4) * 0.03
print('Palanca 2 modelo:', lev2_model, ' ajustada por visitas remanentes:', round(lev2_adj),
      ' diferencia USD M:', round((lev2_model - lev2_adj) * 32 / 1e6, 2))
prop3 = 337_600 * (0.82 - 0.75) / (1 - 0.75)
print('Palanca 3 proporcional (7/25 de 337.600):', round(prop3), ' vs 115.000; diferencia USD M:',
      round((115_000 - prop3) * 32 / 1e6, 2))
print('Órdenes de reparación implícitas si revisitas=337.600 con FTF 75%:', round(337_600 / 0.25))
print('Efecto si el 10% de control no estuviera descontado (bruto x0,9):', round(10.064 * 0.1, 2), 'USD M/año')
