#!/usr/bin/env python3
"""Verwendet die installierte Projekt-Laufzeit, ohne npx-Nachinstallationen.

Check und Snapshot sind gezielte Prüfschritte; Render schreibt erst temporär
und veröffentlicht nur einen erfolgreichen, neuen Exportnamen.
"""
import argparse
import os
from pathlib import Path
import subprocess
import uuid


def run(project, action, output=None, at='1,4,8'):
    project=Path(project).resolve()
    cli=project/'node_modules/hyperframes/dist/cli.js'
    if not cli.is_file(): raise FileNotFoundError('Lokale HyperFrames-Laufzeit fehlt')
    scratch=project/'.tmp/pipeline'
    scratch.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    env['TMPDIR']=str(scratch)
    env['HYPERFRAMES_NO_TELEMETRY']='1'
    # Ein vorhandener Chrome-Cache bleibt nutzbar; wir versprechen keine globale
    # Cache-Isolation. Browserprofil und Arbeitsausgaben liegen im Projekt.
    command=['node',str(cli),action,'.']
    if action=='snapshot': command += ['--at',at]
    if action=='render':
        if output is None: raise ValueError('Render braucht --output')
        output=(project/output).resolve() if not output.is_absolute() else output.resolve()
        if not output.is_relative_to(project): raise ValueError('Export muss im Videoprojekt liegen')
        if output.exists(): raise FileExistsError('Exportname existiert bereits')
        output.parent.mkdir(parents=True,exist_ok=True)
        temporary=scratch/(uuid.uuid4().hex+'.mp4')
        command += ['--format','mp4','--quality','delivery','--fps',str(__import__('json').loads((project/'project.json').read_text())['fps']), '--crf','15','--workers','2','--output',str(temporary)]
    subprocess.run(command,cwd=project,env=env,check=True)
    if action=='render':
        # Exklusives Anlegen verhindert versehentliches Ersetzen bei Parallelstarts.
        try:
            with output.open('xb') as dst, temporary.open('rb') as src:
                __import__('shutil').copyfileobj(src,dst)
        except FileExistsError:
            raise
        except Exception:
            if output.exists(): output.unlink()
            raise
        temporary.unlink()
        print(output)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',type=Path)
    parser.add_argument('action',choices=['check','snapshot','render'])
    parser.add_argument('--output',type=Path)
    parser.add_argument('--at',default='1,4,8')
    args=parser.parse_args()
    try: run(args.project,args.action,args.output,args.at)
    except (ValueError,OSError,subprocess.CalledProcessError) as error: parser.exit(1,str(error)+'\n')

if __name__=='__main__': main()
