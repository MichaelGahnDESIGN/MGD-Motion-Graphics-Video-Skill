#!/usr/bin/env python3
"""Überträgt die versionierte Dokumentation in das GitHub-Wiki.

Ohne --apply nur Vorschau, ohne Netzwerk/Schreiben. Fremde Wiki-Seiten bleiben
unberührt. Ein Hash-Manifest erkennt direkte Änderungen an zuvor veröffentlichten
Seiten; dann ist zunächst eine bewusste Zusammenführung nötig.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/MichaelGahnDESIGN/MGD-Motion-Graphics-Video-Skill'
STATE='.mgd-wiki-state.json'


def sha(text):return hashlib.sha256(text.encode('utf-8')).hexdigest()


def transform(text,source):
    def replace(match):
        href=match.group(1)
        if '://' in href or href.startswith('#'):return match.group(0)
        path,sep,anchor=href.partition('#')
        target=(source.parent/path).resolve()
        wiki=ROOT/'docs/wiki'
        if target.parent==wiki and target.suffix=='.md':
            return ']('+quote(target.stem)+(('#'+anchor) if sep else '')+')'
        if not target.is_relative_to(ROOT):raise ValueError('Link verlässt das Repository')
        relative=target.relative_to(ROOT).as_posix()
        return ']('+BASE+'/blob/main/'+quote(relative,safe='/')+(('#'+anchor) if sep else '')+')'
    return re.sub(r'\]\(([^)]+)\)',replace,text)


def planned_pages():
    return {p.name:transform(p.read_text(encoding='utf-8'),p) for p in sorted((ROOT/'docs/wiki').glob('*.md'))}


def verify_remote(checkout,pages,initialize=False):
    manifest=checkout/STATE
    if manifest.is_symlink():raise ValueError('Umgeleitetes Wiki-Manifest')
    previous=json.loads(manifest.read_text())['files'] if manifest.exists() else {}
    for name,text in pages.items():
        path=checkout/name
        if path.is_symlink():raise ValueError('Umgeleitete Wiki-Seite: '+name)
        if not path.exists():continue
        current=sha(path.read_text(encoding='utf-8'))
        if current==sha(text):continue
        if name in previous:
            if current!=previous[name]:raise ValueError('Direkte Wiki-Änderung zuerst zusammenführen: '+name)
        elif not initialize:
            raise ValueError('Vorhandene Seite ohne Übernahmefreigabe: '+name+'; Erstübernahme mit --initialize')


def git(checkout,*args):
    return subprocess.run(['git','-c','core.hooksPath=/dev/null',*args],cwd=checkout,check=True,capture_output=True,text=True)


def sync(checkout,apply=False,initialize=False):
    checkout=Path(checkout).absolute()
    if '..' in checkout.parts or not checkout.is_relative_to(ROOT/'.tmp') or checkout==ROOT/'.tmp':
        raise ValueError('Wiki-Checkout muss ein Aufgabenordner unter .tmp sein')
    if any(p.is_symlink() for p in (checkout,*checkout.parents)):
        raise ValueError('Umgeleiteter Wiki-Checkout')
    pages=planned_pages()
    print(json.dumps({'mode':'publish' if apply else 'dry-run','checkout':str(checkout),'pages':len(pages),'destination':BASE+'/wiki'},indent=2))
    if not apply:return
    if not checkout.exists():
        checkout.parent.mkdir(parents=True,exist_ok=True)
        git(ROOT,'clone','--',BASE+'.wiki.git',str(checkout))
    else:
        if git(checkout,'remote','get-url','origin').stdout.strip()!=BASE+'.wiki.git':raise ValueError('Unerwartetes Wiki-Remote')
        if git(checkout,'status','--porcelain').stdout.strip():raise ValueError('Wiki-Checkout hat lokale Änderungen')
        git(checkout,'pull','--ff-only')
    verify_remote(checkout,pages,initialize)
    for name,text in pages.items():(checkout/name).write_text(text,encoding='utf-8')
    state={'schema':1,'files':{name:sha(text) for name,text in pages.items()}}
    (checkout/STATE).write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
    git(checkout,'add','--',*pages.keys(),STATE)
    diff=subprocess.run(['git','diff','--cached','--quiet'],cwd=checkout)
    if diff.returncode==0:print('Wiki unverändert');return
    if diff.returncode!=1:raise ValueError('Wiki-Diff konnte nicht geprüft werden')
    git(checkout,'diff','--cached','--check')
    git(checkout,'commit','-m','docs: veröffentliche ausführliches MGD Video-Handbuch')
    git(checkout,'push','origin','HEAD')
    print('Wiki veröffentlicht: '+git(checkout,'rev-parse','HEAD').stdout.strip())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkout',type=Path,default=ROOT/'.tmp/wiki-checkout')
    parser.add_argument('--apply',action='store_true')
    parser.add_argument('--initialize',action='store_true',help='Geprüfte vorhandene Erstseiten bewusst übernehmen')
    args=parser.parse_args()
    try:sync(args.checkout,args.apply,args.initialize)
    except (OSError,ValueError,subprocess.CalledProcessError) as error:parser.exit(1,str(error)+'\n')

if __name__=='__main__':main()
