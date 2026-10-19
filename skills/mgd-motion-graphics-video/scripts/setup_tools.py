#!/usr/bin/env python3
"""Installiert nur die lokalen npm-Werkzeuge eines erzeugten Demo-Projekts.

Kein Homebrew, sudo oder globales npm. Das Abschalten der Installationsskripte
verhindert unbemerkte Paket-Hooks. Browser und Betriebssystem-Pakete werden nicht
nebenbei heruntergeladen; fehlende Voraussetzungen meldet der Doctor.
"""
import argparse
import json
from pathlib import Path
import subprocess


def setup(project, apply=False):
    project = Path(project).resolve()
    package = json.loads((project/'package.json').read_text(encoding='utf-8'))
    wanted = {'gsap':'3.15.0', 'hyperframes':'0.8.177'}
    if package.get('devDependencies') != wanted or package.get('dependencies') or package.get('optionalDependencies'):
        raise ValueError('Dieses Setup ist ausschließlich für den mitgelieferten Starter vorgesehen')
    if not (project/'package-lock.json').is_file():
        raise FileNotFoundError('Geprüfte Paket-Sperrdatei fehlt')
    command = ['npm', 'ci', '--ignore-scripts', '--no-audit', '--no-fund']
    print(json.dumps({'mode':'apply' if apply else 'dry-run','cwd':str(project),'command':command},indent=2))
    if apply: subprocess.run(command,cwd=project,check=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',type=Path)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    try: setup(args.project,args.apply)
    except (ValueError,OSError,subprocess.CalledProcessError) as error: parser.exit(1,str(error)+'\n')

if __name__=='__main__': main()
