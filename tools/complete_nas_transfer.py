#!/usr/bin/env python3
"""Bereitet einen durch instabile SMB-Zeitstempel blockierten Rücktransfer vor.

Nur dieses Repository ist Ziel. Der normale JARVIS-Helfer bleibt unverändert und
führt anschließend den Abschlussabgleich aus. Statt unzuverlässiger Zeitstempel
werden Inhalt, Dateityp, Größe und Identität wiederholt geprüft. Echte Inhalts-
oder Baselinekonflikte brechen ab; ersetzte Quelldateien erhalten eine Sicherung.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat

ROOT=Path(__file__).resolve().parents[1]


def stable_hash(path):
    before=path.lstat()
    if not stat.S_ISREG(before.st_mode) or before.st_nlink!=1:
        raise ValueError('Nur reguläre, unverknüpfte Dateien erlaubt')
    def read_hash():
        digest=hashlib.sha256()
        with path.open('rb') as handle:
            for block in iter(lambda:handle.read(4*1024*1024),b''):digest.update(block)
        return digest.hexdigest()
    first=read_hash();second=read_hash();after=path.lstat()
    if first!=second or (before.st_ino,before.st_size)!=(after.st_ino,after.st_size):
        raise ValueError('Dateiinhalt oder Identität ändert sich: '+str(path))
    return first


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('task',type=Path)
    args=parser.parse_args();task=args.task.absolute()
    if task.is_symlink() or task.resolve()!=task:raise ValueError('Umgeleitete Aufgabe')
    state=json.loads((task/'jarvis-status.json').read_text())
    if state.get('project')!=str(ROOT) or state.get('task')!=str(task) or state.get('status') not in ('working','blocked'):
        raise ValueError('Aufgabe gehört nicht zu diesem Repository oder ist nicht übertragungsbereit')
    if not os.path.ismount(Path('/Volumes')/ROOT.parts[2]):raise ValueError('Originalvolume ist nicht verbunden')
    work=task/'worktree';files={}
    for path in work.rglob('*'):
        if path.is_symlink():raise ValueError('Symlink in Aufgabe')
        if path.is_file():
            relative=path.relative_to(work)
            if '.git' in relative.parts:raise ValueError('Git-Verwaltung nicht übertragen')
            files[relative]=stable_hash(path)
    if set(state['baseline'])-set(map(str,files)):raise ValueError('Ursprüngliche Quellen fehlen lokal')
    current={}
    for relative,expected in files.items():
        target=ROOT/relative
        if any(p.is_symlink() for p in (target,*target.parents)):raise ValueError('Umgeleitetes Ziel')
        old=stable_hash(target) if target.exists() else None
        if old!=state['baseline'].get(str(relative)) and old!=expected:
            raise ValueError('Parallele Inhaltsänderung: '+str(relative))
        current[relative]=old
    backup=ROOT/'.tmp/nas-transfer-backup'/task.name
    staging=ROOT/'.tmp/nas-transfer-staging'/task.name
    for relative,expected in files.items():
        target=ROOT/relative;source=work/relative;old=current[relative]
        if old==expected:continue
        if old is not None:
            saved=backup/relative;saved.parent.mkdir(parents=True,exist_ok=True)
            if saved.exists():
                if stable_hash(saved)!=old:raise ValueError('Vorhandene Sicherung weicht ab')
            else:
                with saved.open('xb') as dst,target.open('rb') as src:shutil.copyfileobj(src,dst)
                if stable_hash(saved)!=old:raise ValueError('Sicherung stimmt nicht')
        part=staging/relative;part.parent.mkdir(parents=True,exist_ok=True)
        # Ein früherer Teilstand ist nur wiederverwendbar, wenn er exakt passt.
        if part.exists():
            if stable_hash(part)!=expected:raise ValueError('Vorhandene Teilkopie weicht ab')
        else:
            with part.open('xb') as dst,source.open('rb') as src:
                shutil.copyfileobj(src,dst);dst.flush();os.fsync(dst.fileno())
        if stable_hash(part)!=expected or stable_hash(source)!=expected:raise ValueError('Kopierprüfung fehlgeschlagen')
        if (stable_hash(target) if target.exists() else None)!=old:raise ValueError('Ziel inzwischen geändert')
        target.parent.mkdir(parents=True,exist_ok=True);os.replace(part,target)
    for relative,expected in files.items():
        if stable_hash(ROOT/relative)!=expected:raise ValueError('Abschlussvergleich fehlgeschlagen')
    print(json.dumps({'prepared':True,'files':len(files),'next':'Normalen JARVIS finish erneut ausführen'},ensure_ascii=False))

if __name__=='__main__':main()
