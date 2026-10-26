#!/usr/bin/env python3
"""Genera paquetes de fuentes y plantillas. No llama modelos IA."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROLES = ['CEO', 'CTO', 'CTIO', 'CISO', 'CHRO', 'CFO']
EXTS = {'.md', '.txt', '.csv', '.json', '.yaml', '.yml', '.pdf', '.docx', '.pptx', '.xlsx'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, help='Identificador seguro del proyecto')
    parser.add_argument('--docs', required=True, type=Path, help='Directorio con documentos')
    parser.add_argument('--output', default=Path('outputs'), type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}', args.project):
        parser.error('project debe ser un identificador alfanumérico con - o _')
    docs = args.docs.resolve()
    if not docs.is_dir():
        parser.error(f'No existe directorio: {docs}')
    files = sorted(p for p in docs.rglob('*') if p.is_file() and p.suffix.lower() in EXTS)
    if not files:
        parser.error('No se encontraron documentos admitidos')
    out = args.output / args.project
    out.mkdir(parents=True, exist_ok=True)
    sources = []
    for idx, path in enumerate(files, 1):
        relative = path.relative_to(docs).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        sources.append({'id': f'DOC-{idx:03d}', 'path': str(path), 'relative_path': relative,
                        'size_bytes': path.stat().st_size, 'sha256': digest, 'format': path.suffix.lower(),
                        'extraction_status': 'pendiente_lectura_semantica'})
    manifest = {'project_id': args.project, 'created_utc': datetime.now(timezone.utc).isoformat(),
                'docs_directory': str(docs), 'sources': sources,
                'note': 'Inventario automático sin evaluación ni extracción semántica'}
    (out / 'document_inventory.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'evaluation_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Índice de fuentes', '', 'No equivale a validación del contenido.', '',
             '| ID | Archivo | Formato | SHA256 |', '|---|---|---|---|']
    for s in sources:
        lines.append(f"| {s['id']} | `{s['relative_path'].replace('|','/')}` | {s['format']} | `{s['sha256'][:16]}…` |")
    (out / 'source_index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    template = Path(__file__).resolve().parents[1] / 'templates' / 'individual-review.md'
    for i, role in enumerate(ROLES, 1):
        name = f'{i:02d}_{role}.md'
        path = out / name
        if not path.exists():
            path.write_text(template.read_text(encoding='utf-8').replace('<ROL>', role).replace('<PROYECTO>', args.project), encoding='utf-8')
    for name, header in [('00_inventario_evidencias.md', '# Inventario y evidencia'),
                         ('07_matriz_objeciones.md', '# Matriz de objeciones'),
                         ('08_debate_cruzado.md', '# Debate cruzado'),
                         ('10_plan_de_accion.md', '# Plan de acción'),
                         ('11_trazabilidad_fuentes.md', '# Trazabilidad de fuentes')]:
        path = out / name
        if not path.exists():
            path.write_text(header + '\n\n> Pendiente de completar por el Swarm MoE.\n', encoding='utf-8')
    final = out / '09_dictamen_ejecutivo.md'
    if not final.exists():
        contents = (Path(__file__).resolve().parents[1] / 'templates' / 'final-resolution.md').read_text(encoding='utf-8')
        final.write_text(contents.replace('<PROYECTO>', args.project), encoding='utf-8')
    print(f'Inventario de {len(sources)} documento(s) en {out}. Requiere evaluación con agente Cursor.')

if __name__ == '__main__':
    main()
