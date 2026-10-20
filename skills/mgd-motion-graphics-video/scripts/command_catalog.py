#!/usr/bin/env python3
"""Zentrale Aufrufdefinitionen für installierbare Skills, Befehle und Prompts.

Es werden ausschließlich Texte erzeugt, keine Shellbefehle oder KI-Aufträge
 ausgeführt. Der Katalog ist damit auch ohne Agenten gefahrlos einsehbar.
"""
import json
from pathlib import Path
import re
import unicodedata

SKILL=Path(__file__).resolve().parents[1]
DEFAULTS={name:'['+label+']' for name,label in {
 'thema':'Thema','ordner':'Projektordner','zielgruppe':'Zielgruppe','format':'Format',
 'dauer':'Dauer','plattform':'Plattform','ziel':'gewünschte Handlung oder Änderung',
 'stil':'Stil','datei':'Dateipfad','marke':'Marke','produkt':'Produkt oder Angebot'}.items()}


def load_catalog():
    data=json.loads((SKILL/'assets/commands.json').read_text(encoding='utf-8'))
    if data.get('schema')!=1:raise ValueError('Unbekanntes Aufrufschema')
    seen=set();skills=set()
    for item in data['commands']:
        if not re.fullmatch(r'[a-z0-9-]+',item['skill']):raise ValueError('Ungültiger Skill-Name')
        if not re.fullmatch(r'[\w-]+',item['command'],re.UNICODE):raise ValueError('Ungültiger Befehlsname')
        if item['command'].casefold() in seen or item['skill'] in skills:raise ValueError('Doppelter Aufruf')
        seen.add(item['command'].casefold());skills.add(item['skill'])
        item['prompt'].format_map(DEFAULTS)
    return data


def resolve(value):
    key=unicodedata.normalize('NFC',value.strip().lstrip('/$')).casefold()
    for item in load_catalog()['commands']:
        if key in (item['command'].casefold(),item['skill']):return item
    raise ValueError('Unbekannter Aufruf: '+value)


CHARACTER_PROMPT = (' Bei Figuren kläre vor neuen Bildern die verbindliche Darstellung und vorhandene Charakter-Sheets oder LoRAs einschließlich Dateipfad. '
                    'Frage nach ChatGPT/OpenAI (Cloud), lokaler Bildgenerierung, Higgsfield oder anderem Anbieter; kläre LoRA-Training separat. '
                    'Erstelle beziehungsweise verwende geprüft Charakter-Sheet und echtes kompatibles LoRA. Anbieter, Datenfreigabe und Kostenrahmen vor Generierung festhalten; '
                    'bestehende passende Entscheidungen übernehmen und fehlende LoRA-Fähigkeiten offen benennen.')

CHARACTER_ROUTING = ('Bei Figuren vor neuen Figurenbildern die [Charakter-Sheet-/LoRA-Anleitung](../mgd-motion-graphics-video/references/characters-lora.md) lesen. '
                     'Verbindliche Darstellung, vorhandene Sheets/LoRA-Pfade, Bildanbieter und LoRA-Trainer gemeinsam klären. '
                     'Charakter-Sheet und echtes LoRA gehören zur Standardlieferung; passende freigegebene Ressourcen wiederverwenden. '
                     'ChatGPT/OpenAI ist Cloud-Verarbeitung. Externe Datenfreigabe und Kostenrahmen beachten; keine erfundene LoRA-Erstellung. '
                     'Bereits dokumentierte passende Antworten nicht wiederholen; reine Schnittkorrekturen benötigen kein erneutes Training.')


def render_prompt(item,values=None):
    return item['prompt'].format_map({**DEFAULTS,**(values or {})}) + CHARACTER_PROMPT


def render_skill(item):
    return ('---\nname: '+item['skill']+'\ndescription: '+json.dumps(item['description'],ensure_ascii=False)+'\n---\n\n# '+item['title']+'\n\n'
            'Gewünschter Aufruf: `/'+item['command']+'`. In Codex explizit mit `$'+item['skill']+'` starten.\n\n'
            'Lies den [Hauptskill](../mgd-motion-graphics-video/SKILL.md) und nur die für diese Aufgabe nötigen Referenzen. '
            'Erhalte bestehende Entscheidungen und vorhandene Projektquellen.\n\n'+item['instructions']+'\n\n'+CHARACTER_ROUTING+'\n\n'
            'Wesentlich fehlende Angaben nur erfragen, wenn sie nicht aus Auftrag, Datei oder bestehendem Projekt ableitbar sind. '
            'Ein Formatvorschlag ist keine Einschränkung einer ausdrücklichen Benutzerwahl.\n')


def render_ui(item):
    # JSON-Strings sind gültige YAML-Strings und schützen Umlaute sowie Anführungszeichen.
    short=(item['title']+' mit dem MGD Video-Skill')[:64]
    return ('interface:\n  display_name: '+json.dumps(item['command'],ensure_ascii=False)+
            '\n  short_description: '+json.dumps(short,ensure_ascii=False)+
            '\n  default_prompt: '+json.dumps('Nutze $'+item['skill']+' für mein Videoprojekt.',ensure_ascii=False)+'\n')


def render_command(item):
    return ('---\ndescription: '+json.dumps(item['description'],ensure_ascii=False)+'\n---\n\n'
            'Nutze den [MGD-Hauptskill](../skills/mgd-motion-graphics-video/SKILL.md).\n\n'
            +item['instructions']+'\n\n'+CHARACTER_ROUTING.replace('../mgd-motion-graphics-video/references/', '../skills/mgd-motion-graphics-video/references/')+'\n\nBenutzerangaben: $ARGUMENTS\n\n'
            'Wesentlich fehlende Angaben nur erfragen, wenn sie nicht aus Auftrag, Datei oder Projekt ableitbar sind. '
            'Originale erhalten und nur beauftragte externe Aktionen ausführen.\n')
