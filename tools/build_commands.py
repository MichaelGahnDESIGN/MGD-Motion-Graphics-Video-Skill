#!/usr/bin/env python3
"""Erzeugt wiederholbare Aufrufdateien aus dem zentralen, geprüften Katalog.

Mit --check werden nur Abweichungen gemeldet. Das Wiki bleibt vollständig
versioniert; dessen Navigation und Befehlsübersicht stammen aus derselben Quelle.
"""
import argparse
from pathlib import Path
import sys
import unicodedata

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'skills/mgd-motion-graphics-video'
sys.path.insert(0,str(CORE/'scripts'))
from command_catalog import load_catalog,render_command,render_prompt,render_skill,render_ui


def equivalent_path(path):
    """NAS/APFS können denselben Umlaut als NFC oder NFD zurückgeben.

    Inhalte und logischer Name bleiben gleich. Vorhandene äquivalente Dateien
    werden verwendet, statt doppelte oder auf Linux fehlende Vorlagen zu erzeugen.
    """
    if path.exists() or not path.parent.is_dir():return path
    expected=unicodedata.normalize('NFC',path.name)
    matches=[p for p in path.parent.iterdir() if unicodedata.normalize('NFC',p.name)==expected]
    if len(matches)>1:raise ValueError('Mehrdeutige Unicode-Dateinamen: '+path.name)
    return matches[0] if matches else path


def outputs():
    result={};catalog=load_catalog()['commands']
    for item in catalog:
        folder=ROOT/'skills'/item['skill']
        result[folder/'SKILL.md']=render_skill(item)
        result[folder/'agents/openai.yaml']=render_ui(item)
        result[folder/'LICENSE']=(ROOT/'LICENSE').read_text(encoding='utf-8')
        result[equivalent_path(ROOT/'commands'/(item['command']+'.md'))]=render_command(item)
    guide='''# Befehle und komplette Prompt-Bibliothek

Alle Aufrufe verwenden denselben Hauptskill und wechseln nur den Arbeitsmodus.
In Codex den Eintrag mit `$skill-name` oder über die Skill-Auswahl wählen. Die
Schreibweise `/MGD-Reel` ist die gewünschte Kurzbezeichnung; ein frei definierter
nativer Codex-Slash-Befehl wird damit nicht versprochen. In Claude Code erzeugen
die optional installierten Befehlsdateien die unten genannten Slash-Aufrufe.
Bei Plugin-Installation können Aufrufe zusätzlich den Plugin-Namensraum tragen.

`/MGD-Video-Optimieren` ist der endgültige Name für die Verbesserung bestehender
Videos. Der frühere Entwurf `/MGD-Optimieren` wird nicht installiert.

| Gewünschter Aufruf / Claude-Befehl | Codex-Skill | Zweck |
|---|---|---|
'''
    for item in catalog:
        guide+='| `/'+item['command']+'` | `$'+item['skill']+'` | '+item['title']+' |\n'
    guide+='\n## So verwendest du die Vorlagen\n\nEckige Platzhalter durch eigene Angaben ersetzen. Sind Thema oder Projektordner\nnoch unbekannt, den Agenten danach fragen lassen. Bereits bekannte Angaben\nmüssen nicht wiederholt werden. Ein Formatvorschlag darf ausdrücklich geändert\nwerden. Originale, bisherige Freigaben und bestehende Entscheidungen bleiben\nmaßgeblich.\n\n'
    for item in catalog:
        guide+='## /'+item['command']+'\n\n'+item['description']+'\n\n> '+render_prompt(item)+'\n\n'
    guide+='''## Prompt ohne Agenten vorbereiten

Vom Repository-Hauptordner aus:

```bash
python3 skills/mgd-motion-graphics-video/scripts/commands.py list
python3 skills/mgd-motion-graphics-video/scripts/commands.py show /MGD-Reel --thema "Eine fantastische Reise" --ordner "/PFAD/ZUM/PROJEKT" --plattform "Instagram"
python3 skills/mgd-motion-graphics-video/scripts/commands.py show /MGD-Video-Optimieren --datei "/PFAD/ZUM/PROJEKT/exports/film-v001.mp4" --ziel "ruhigere Schrift und längere Schlusskarte"
```

Diese Befehle geben Texte aus. Sie installieren nichts und starten keine
Videogenerierung. Alle Platzhalter können als gleichnamige Parameter übergeben
werden, etwa `--dauer`, `--format` oder `--zielgruppe`.

Weiter: [Installation](Installation.md) · [Projektstart](Projektstart.md) ·
[Videoarten](Videoarten.md) · [Problemlösung](Probleme-und-FAQ.md)
'''
    result[ROOT/'docs/wiki/Befehle.md']=guide
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    changed=[]
    for path,text in outputs().items():
        if path.exists() and path.read_text(encoding='utf-8')==text:continue
        changed.append(str(path.relative_to(ROOT)))
        if not args.check:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')
    if args.check and changed:raise SystemExit('Veraltete Aufrufdateien: '+', '.join(changed))
    print(('Geprüft' if args.check else 'Erzeugt')+': '+str(len(outputs()))+' Katalogdateien')

if __name__=='__main__':main()
