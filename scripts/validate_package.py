#!/usr/bin/env python3
"""Valida que el paquete y los contratos base estén completos (sin ejecutar IA)."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ROLES = ['ceo','cto','ctio','ciso','chro','cfo','orchestrator','evidence-auditor','red-team','rapporteur']
REQUIRED = ['AGENTS.md','README.md','protocols/evaluation-workflow.md','protocols/scoring-and-veto.md',
            'schemas/evaluation.schema.json','scripts/prepare_evaluation.py',
            '.cursor/commands/evaluar-proyecto-ia.md','.cursor/commands/reevaluar-proyecto-ia.md',
            'templates/individual-review.md','templates/final-resolution.md'] + [f'agents/{r}.md' for r in ROLES]
missing = [f for f in REQUIRED if not (ROOT / f).is_file()]
if missing:
    raise SystemExit('Faltan archivos: '+', '.join(missing))
json.loads((ROOT/'schemas/evaluation.schema.json').read_text(encoding='utf-8'))
for f in REQUIRED:
    if not (ROOT/f).read_text(encoding='utf-8').strip():
        raise SystemExit('Archivo vacío: '+f)
print(f'OK: {len(REQUIRED)} archivos requeridos y JSON Schema válido.')
