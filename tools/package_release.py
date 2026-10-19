#!/usr/bin/env python3
"""Paketiert ausschließlich versionierte öffentliche Dateien und deren Hashes.

Ein sauberer Git-Stand und übereinstimmende Versionsmetadaten sind Voraussetzung.
Temporäre Daten, lokale Installationen und persönliche Dateien werden nicht erfasst.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT=Path(__file__).resolve().parents[1]


def main():
    if subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip():
        raise ValueError('Zuerst einen geprüften, sauberen Git-Stand herstellen')
    version=json.loads((ROOT/'plugin.json').read_text())['version']
    for name in ('.codex-plugin/plugin.json','.claude-plugin/plugin.json','skills/mgd-motion-graphics-video/assets/commands.json'):
        if json.loads((ROOT/name).read_text())['version']!=version:raise ValueError('Versionsmetadaten weichen ab')
    files=[Path(p) for p in subprocess.check_output(['git','ls-files','-z'],cwd=ROOT,text=True).split('\0') if p]
    patterns=(r'/Users/',r'/Volumes/',r'ghp_[A-Za-z0-9]{20,}',r'sk-proj-[A-Za-z0-9]{20,}',r'AKIA[0-9A-Z]{16}')
    for relative in files:
        path=ROOT/relative
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):raise ValueError('Umgeleitete Paketdatei')
        if path.suffix not in ('.jpg','.png'):
            text=path.read_text(encoding='utf-8')
            # Die Muster stehen nur hier als Prüfdefinition, nicht als reale Daten.
            if relative==Path('tools/package_release.py'):continue
            if any(re.search(pattern,text) for pattern in patterns):raise ValueError('Unerwartetes privates Muster: '+str(relative))
    destination=ROOT/'.tmp/release'/version;destination.mkdir(parents=True,exist_ok=True)
    bundles={
      'mgd-motion-graphics-video-'+version+'.zip':[(p,Path(*p.parts[1:])) for p in files if p.parts[:2]==('skills','mgd-motion-graphics-video')],
      'mgd-motion-graphics-video-wiki-'+version+'.zip':[(p,Path('wiki')/p.name) for p in files if p.parts[:2]==('docs','wiki')]}
    hashes=[]
    for name,entries in bundles.items():
        path=destination/name
        with zipfile.ZipFile(path,'x',compression=zipfile.ZIP_DEFLATED) as archive:
            for source,target in entries:archive.write(ROOT/source,target.as_posix())
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None:raise ValueError('ZIP-Prüfung fehlgeschlagen')
        hashes.append(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+name)
    (destination/'SHA256SUMS.txt').write_text('\n'.join(hashes)+'\n',encoding='utf-8')
    print(json.dumps({'version':version,'files_checked':len(files),'packages':list(bundles),'directory':str(destination)},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
