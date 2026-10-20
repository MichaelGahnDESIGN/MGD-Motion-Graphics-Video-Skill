#!/usr/bin/env python3
"""Prüft und rendert den Remotion-Starter ohne automatische Nachinstallation.

Ein vorhandener Browser wird verwendet. Neue Exporte werden exklusiv angelegt;
Originale und vorhandene Exporte dürfen niemals ersetzt werden.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid


def browser_path(explicit=None):
    candidates = [explicit, os.environ.get('MGD_BROWSER'),
                  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                  '/Applications/Chromium.app/Contents/MacOS/Chromium']
    candidates += [shutil.which(name) for name in ('chromium', 'chromium-browser', 'google-chrome')]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(Path(candidate).resolve())
    raise FileNotFoundError('Chrome/Chromium fehlt. Vorhandenen Browser mit --browser angeben; kein automatischer Download.')


def run(project, action, output=None, at='1,4,8', browser=None):
    project = Path(project).resolve()
    if action not in ('check', 'snapshot', 'render'):
        raise ValueError('Unbekannte Aktion')
    if not (project/'node_modules/@remotion/renderer/package.json').is_file():
        raise FileNotFoundError('Projektlokale Remotion-Laufzeit fehlt; setup_tools.py bewusst ausführen')
    if action == 'render':
        if output is None: raise ValueError('Render braucht --output')
        output = (project/output).resolve()
        if not output.is_relative_to(project): raise ValueError('Export muss im Videoprojekt liegen')
        if output.exists(): raise FileExistsError('Exportname existiert bereits')
    browser = browser_path(browser)
    subprocess.run([sys.executable, 'tools/build.py'], cwd=project, check=True)
    config = json.loads((project/'runtime-config.json').read_text())
    times = at.split(',') if action == 'snapshot' else []
    for value in times:
        frame = round(float(value)*config['fps'])
        if not 0 <= frame < config['frames']: raise ValueError('Snapshot außerhalb der Timeline')
    scratch = project/'.tmp/pipeline'/uuid.uuid4().hex
    scratch.mkdir(parents=True)
    env = os.environ.copy()
    env['TMPDIR'] = str(scratch)
    subprocess.run(['node', 'tools/runtime.mjs', action, str(scratch), browser, *times],
                   cwd=project, env=env, check=True)
    if action == 'render':
        temporary = scratch/'export.mp4'
        output.parent.mkdir(parents=True, exist_ok=True)
        # Erst bei Erfolg exklusiv veröffentlichen; parallel angelegte Dateien behalten.
        created = False
        try:
            with output.open('xb') as dst:
                created = True
                with temporary.open('rb') as src: shutil.copyfileobj(src, dst)
        except Exception:
            if created: output.unlink(missing_ok=True)
            raise
        temporary.unlink()
        print(output)
    else:
        print(scratch)
    return scratch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('action', choices=['check', 'snapshot', 'render'])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--at', default='1,4,8')
    parser.add_argument('--browser', help='Pfad zu vorhandenem Chrome/Chromium')
    args = parser.parse_args()
    try: run(args.project, args.action, args.output, args.at, args.browser)
    except (ValueError, OSError, subprocess.CalledProcessError) as error: parser.exit(1, str(error)+'\n')

if __name__ == '__main__': main()
