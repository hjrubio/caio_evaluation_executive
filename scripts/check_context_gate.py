#!/usr/bin/env python3
"""Verificación conservadora de cobertura documental. No sustituye la revisión semántica."""
import argparse, hashlib, json, sys
from pathlib import Path

def main():
 p=argparse.ArgumentParser(); p.add_argument('--project',required=True); p.add_argument('--docs',type=Path,required=True); p.add_argument('--review',type=Path,required=True); args=p.parse_args()
 base=Path(__file__).resolve().parents[1]; registry=json.loads((base/'context/context_sources.json').read_text(encoding='utf8'))
 issues=[]; docroot=args.docs.resolve()
 for s in registry.get('required_sources',[]):
  if not s.get('required'): continue
  loc=s.get('local_path')
  if s.get('status') not in ('AVAILABLE','VERIFIED') or not loc:
   issues.append(f"{s['id']}: fuente obligatoria no resuelta (estado={s.get('status')})"); continue
  path=(docroot/loc).resolve()
  if not path.is_relative_to(docroot) or not path.is_file(): issues.append(f"{s['id']}: archivo local no existe o fuera de docs: {loc}")
 if not args.review.is_file(): issues.append('No existe context_review.json; falta la revisión semántica'); reviews=[]
 else:
  try: reviews=json.loads(args.review.read_text(encoding='utf8'))['documents']
  except (ValueError,KeyError,TypeError): issues.append('context_review.json inválido'); reviews=[]
 for s in registry.get('required_sources',[]):
  if s.get('required') and s.get('local_path'):
   matching=[r for r in reviews if r.get('path')==s['local_path']]
   if not matching: issues.append(f"{s['id']}: no existe ficha de revisión")
   for r in matching:
    path=docroot/s['local_path']
    if path.exists() and r.get('sha256')!=hashlib.sha256(path.read_bytes()).hexdigest(): issues.append(f"{s['id']}: SHA256 no coincide")
    if r.get('read_complete') is not True or not r.get('summary') or not r.get('evidence_refs') or not r.get('used_by_roles'): issues.append(f"{s['id']}: lectura, resumen, evidencia o uso por roles incompleto")
 if not reviews: issues.append('No hay documentos con revisión documentada')
 result={'project':args.project,'status':'BLOCKED_CONTEXT_INCOMPLETE' if issues else 'READY_FOR_EXECUTIVE_REVIEW','issues':issues,'note':'La verificación automática inspecciona la consistencia documental, no certifica veracidad semántica.'}
 print(json.dumps(result,ensure_ascii=False,indent=2)); return 2 if issues else 0
if __name__=='__main__': sys.exit(main())
