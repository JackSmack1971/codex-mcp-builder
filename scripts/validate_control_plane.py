#!/usr/bin/env python3
"""Offline structural self-check. Not MCP interoperability or policy enforcement."""
from pathlib import Path
import re
import sys
import json
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('mcp-discovery','mcp-contract-design','mcp-implementation','mcp-security-review','mcp-conformance','mcp-release')
REQUIRED = ('README.md','AGENTS.md','.codex/config.toml','docs/architecture/architecture.md','docs/contracts/server-contract.md','docs/security/threat-model.md','docs/verification/evidence.md','docs/architecture/standards-matrix.md')
errors = []
for file in REQUIRED:
    if not (ROOT / file).is_file(): errors.append(f'missing: {file}')
for name in SKILLS:
    p = ROOT / '.agents' / 'skills' / name / 'SKILL.md'
    if not p.is_file():
        errors.append(f'missing skill: {name}')
        continue
    content = p.read_text(encoding='utf-8')
    if not re.search(r'\A---\nname: '+re.escape(name)+r'\ndescription: .+\n---\n', content):
        errors.append(f'invalid skill frontmatter: {name}')
    if not (p.parent / 'references' / 'checklist.md').is_file(): errors.append(f'missing checklist: {name}')
for name in ('mcp-researcher','mcp-implementer','mcp-security','mcp-verifier'):
    if not (ROOT / '.codex' / 'agents' / f'{name}.toml').is_file(): errors.append(f'missing agent: {name}')
try:
    import tomllib
    for p in [ROOT/'.codex/config.toml', *(ROOT/'.codex/agents').glob('*.toml')]:
        if p.is_file(): tomllib.loads(p.read_text(encoding='utf-8'))
except ImportError:
    print('SKIP: TOML syntax check requires Python 3.11+')
except Exception as exc:
    errors.append(f'TOML parsing: {exc}')
manifest = ROOT / 'MANIFEST.json'
if manifest.is_file():
    try:
        recorded = json.loads(manifest.read_text(encoding='utf-8'))['files']
        actual = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in ROOT.rglob('*') if p.is_file() and p != manifest and
                  '__pycache__' not in p.relative_to(ROOT).parts}
        for path in sorted(recorded.keys() | actual.keys()):
            if path not in recorded: errors.append(f'unmanifested file: {path}')
            elif path not in actual: errors.append(f'manifested file absent: {path}')
            elif recorded[path] != actual[path]: errors.append(f'checksum mismatch: {path}')
    except Exception as exc:
        errors.append(f'manifest validation: {exc}')
if errors:
    for error in errors: print('FAIL:', error)
    sys.exit(1)
print('PASS: control-plane structural checks. MCP server behavior NOT TESTED.')
