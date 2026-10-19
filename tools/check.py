#!/usr/bin/env python3
"""Netzwerkfreie Paketprüfung und Verhaltenstests mit projektlokaler Ablage."""
import ast
import json
import os
from pathlib import Path
import re
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]

def main():
    for path in ROOT.rglob('*.py'):
        if '.tmp' in path.parts or '.git' in path.parts:continue
        ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
    for path in ROOT.rglob('*.json'):
        if '.tmp' in path.parts or '.git' in path.parts:continue
        json.loads(path.read_text(encoding='utf-8'))
    for skill in (ROOT/'skills').iterdir():
        if not skill.is_dir():continue
        text=(skill/'SKILL.md').read_text(encoding='utf-8')
        if not text.startswith('---\nname: '+skill.name+'\n'):raise ValueError('Skill-Name und Verzeichnis stimmen nicht überein')
        if not re.search(r'^description: .+',text,re.M):raise ValueError('Beschreibung fehlt')
    # Lokale Markdown-Verweise prüfen; externe URLs werden nicht angefragt.
    for path in ROOT.rglob('*.md'):
        if '.tmp' in path.parts or '.git' in path.parts:continue
        for href in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if '://' in href or href.startswith('#'):continue
            target=href.split('#',1)[0]
            if target and not (path.parent/target).exists():raise ValueError('Verweis fehlt: '+str(path)+': '+target)
    import subprocess
    subprocess.run([sys.executable,str(ROOT/'tools/build_commands.py'),'--check'],check=True)
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':sys.exit(main())
