#!/usr/bin/env python3
"""Installiert den MGD-Skill und ausgewählte, fest versionierte Zusatzskills.

Standardmäßig wird ausschließlich ein Plan ausgegeben. Downloads werden als
Daten geprüft und nie ausgeführt. Bestehende Installationen werden weder gelöscht
noch überschrieben; eine spätere Aktualisierung ist eine separate Entscheidung.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import urllib.request
import sys
sys.dont_write_bytecode = True
from command_catalog import load_catalog, render_command, render_skill, render_ui

SKILL = Path(__file__).resolve().parents[1]
ALLOWLIST = {'affaan-m/ecc'}
MAX_FILE = 4 * 1024 * 1024
MAX_TOTAL = 64 * 1024 * 1024


def safe_relative(value):
    """Prüft auch Windows-Trenner, damit Sperrdateien plattformneutral bleiben."""
    path = PurePosixPath(value)
    if not value or '\\' in value or path.is_absolute() or '..' in path.parts or ':' in value:
        raise ValueError('Unsicherer relativer Pfad: ' + value)
    return path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def select_packages(lock, profiles):
    chosen = {}
    for profile in profiles:
        if profile not in lock['profiles']:
            raise ValueError('Unbekanntes Profil: ' + profile)
        for source, names in lock['profiles'][profile].items():
            chosen.setdefault(source, set()).update(names)
    result = []
    for source_id, names in sorted(chosen.items()):
        source = lock['sources'][source_id]
        if source['repository'] not in ALLOWLIST or not re.fullmatch('[0-9a-f]{40}', source['revision']):
            raise ValueError('Nicht freigegebene Quelle oder Revision')
        licenses = [f for f in source['files'] if f['path'] in ('LICENSE', 'LICENSE.md', 'LICENSE.txt')]
        if not licenses:
            raise ValueError('Upstream-Lizenz fehlt')
        for name in sorted(names):
            if not re.fullmatch('[a-z0-9-]+', name):
                raise ValueError('Ungültiger Skill-Name')
            prefix = 'skills/' + name + '/'
            files = [f for f in source['files'] if f['path'].startswith(prefix)]
            if not any(f['path'] == prefix + 'SKILL.md' for f in files):
                raise ValueError('Skill-Einstieg fehlt: ' + name)
            result.append((name, source_id, source, prefix, files, licenses[0]))
    if len({p[0] for p in result}) != len(result):
        raise ValueError('Namenskollision zwischen Quellen')
    return result


def checked_data(source_id, source, entry, cache=None):
    relative = safe_relative(entry['path'])
    if not 0 <= entry['size'] <= MAX_FILE or not re.fullmatch('[a-f0-9]{64}', entry['sha256']):
        raise ValueError('Ungültiger Größen- oder Hash-Eintrag')
    if cache:
        path = cache / source_id / str(relative)
        if path.is_symlink() or not path.resolve().is_relative_to(cache.resolve()):
            raise ValueError('Cache-Pfad verlässt den Cache')
        with path.open('rb') as handle:
            data = handle.read(MAX_FILE + 1)
    else:
        url = f"https://raw.githubusercontent.com/{source['repository']}/{source['revision']}/{relative}"
        req = urllib.request.Request(url, headers={'User-Agent': 'MGD-Motion-Graphics/0.1'})
        with urllib.request.urlopen(req, timeout=45) as response:
            if not response.url.startswith('https://raw.githubusercontent.com/'):
                raise ValueError('Unerwartete Download-Weiterleitung')
            data = response.read(MAX_FILE + 1)
    if len(data) != entry['size'] or digest(data) != entry['sha256']:
        raise ValueError('Prüfsumme oder Größe falsch: ' + entry['path'])
    return data


def same_tree(a, b):
    """Nur exakt gleiche Installationen gelten als bereits vorhanden."""
    if a.is_symlink() or not a.is_dir():
        return False
    if any(p.is_symlink() for p in a.rglob('*')):
        return False
    left = {p.relative_to(a).as_posix(): p for p in managed_files(a)}
    right = {p.relative_to(b).as_posix(): p for p in managed_files(b)}
    return (left.keys() == right.keys() and
            all(not p.is_symlink() and digest(p.read_bytes()) == digest(right[n].read_bytes())
                for n, p in left.items()))


def managed_files(root):
    return [p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts
            and p.suffix != '.pyc' and p.name != '.DS_Store']


def preview_conflicts(target, catalog, command_root):
    """Vergleicht lokale Ziele ohne Staging, Downloads oder Schreiboperationen."""
    expected = {SKILL.name: {p.relative_to(SKILL).as_posix(): p.read_bytes() for p in managed_files(SKILL)}}
    license_data = (SKILL / 'LICENSE').read_bytes()
    for item in catalog:
        expected[item['skill']] = {'SKILL.md': render_skill(item).encode('utf-8'),
                                  'agents/openai.yaml': render_ui(item).encode('utf-8'),
                                  'LICENSE': license_data}
    conflicts = []
    for name, files in expected.items():
        current = target / name
        if not current.exists() and not current.is_symlink(): continue
        if current.is_symlink() or not current.is_dir() or any(p.is_symlink() for p in current.rglob('*')):
            conflicts.append(name); continue
        actual = {p.relative_to(current).as_posix(): p.read_bytes() for p in managed_files(current)}
        if actual != files: conflicts.append(name)
    if command_root:
        for item in catalog:
            path = command_root / (item['command'] + '.md')
            if path.exists() or path.is_symlink():
                if path.is_symlink() or not path.is_file() or path.read_bytes() != render_command(item).encode('utf-8'):
                    conflicts.append('/' + item['command'])
    return conflicts


def install(target, profiles, apply=False, cache=None, allow_global=False, lock=None, aliases=False, commands_target=None):
    target = Path(target).expanduser().absolute()
    if '..' in target.parts:
        raise ValueError('Zielpfad muss ohne .. angegeben werden')
    # Ein vorhandener Symlink im Zielpfad darf nicht heimlich das Schreibziel ändern.
    if any(p.is_symlink() for p in (target, *target.parents)):
        raise ValueError('Installationsziel enthält einen Symlink')
    global_roots = [Path.home() / name for name in ('.codex', '.agents', '.claude')]
    if any(target.is_relative_to(p) for p in global_roots) and not allow_global:
        raise ValueError('Globale Installation braucht zusätzlich --global und einen Benutzerauftrag')
    command_root = None
    if commands_target is not None:
        if not aliases:
            raise ValueError('--commands-target braucht --aliases')
        command_root = Path(commands_target).expanduser().absolute()
        if '..' in command_root.parts or any(p.is_symlink() for p in (command_root, *command_root.parents)):
            raise ValueError('Unsicheres Befehlsziel')
        if command_root.name != 'commands' or target != command_root.parent / 'skills':
            raise ValueError('Claude-Befehle brauchen skills und commands im selben Elternordner')
        if any(command_root.is_relative_to(p) for p in global_roots) and not allow_global:
            raise ValueError('Globale Befehle brauchen --global')
    catalog = load_catalog()['commands'] if aliases else []
    lock = lock or json.loads((SKILL / 'dependencies.lock.json').read_text(encoding='utf-8'))
    packages = select_packages(lock, profiles)
    total = sum(sum(f['size'] for f in p[4]) + p[5]['size'] for p in packages)
    if total > MAX_TOTAL:
        raise ValueError('Download-Gesamtbudget überschritten')
    names = [SKILL.name] + [item['skill'] for item in catalog] + [p[0] for p in packages]
    if len(set(names)) != len(names):
        raise ValueError('Namenskollision zwischen Hauptskill, Aufrufen oder Zusatzskills')
    conflicts = preview_conflicts(target, catalog, command_root)
    print(json.dumps({'mode': 'apply' if apply else 'dry-run', 'target': str(target),
                      'skills': names, 'conflicts': conflicts, 'commands_target': str(command_root) if command_root else None,
                      'commands': [item['command'] for item in catalog] if command_root else [], 'download_bytes_max': total}, ensure_ascii=False, indent=2))
    if not apply:
        return names
    if conflicts:
        raise FileExistsError('Bestehende lokale Änderungen bleiben unangetastet: ' + ', '.join(conflicts))
    target.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.mgd-install-', dir=target))
    created = []
    created_commands = []
    try:
        own = stage / SKILL.name
        # Dateien aus fremden Installationen und Python-Caches gehören nicht ins Paket.
        shutil.copytree(SKILL, own, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'), symlinks=True)
        if any(p.is_symlink() for p in own.rglob('*')):
            raise ValueError('MGD-Paket enthält einen Symlink')
        for item in catalog:
            alias = stage / item['skill']
            (alias / 'agents').mkdir(parents=True)
            (alias / 'SKILL.md').write_text(render_skill(item), encoding='utf-8')
            (alias / 'agents/openai.yaml').write_text(render_ui(item), encoding='utf-8')
            shutil.copyfile(SKILL / 'LICENSE', alias / 'LICENSE')
        command_files = {}
        if command_root:
            for item in catalog:
                destination = command_root / (item['command'] + '.md')
                data = render_command(item).encode('utf-8')
                if destination.exists() or destination.is_symlink():
                    if destination.is_symlink() or not destination.is_file() or destination.read_bytes() != data:
                        raise FileExistsError('Bestehender Befehl bleibt unangetastet: ' + item['command'])
                else:
                    command_files[destination] = data
        for name, source_id, source, prefix, files, license_entry in packages:
            destination = stage / name
            destination.mkdir()
            for entry in files:
                rel = safe_relative(entry['path'][len(prefix):])
                out = destination / str(rel)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(checked_data(source_id, source, entry, cache))
            (destination / 'LICENSE.upstream').write_bytes(checked_data(source_id, source, license_entry, cache))
            receipt = {'repository': source['repository'], 'revision': source['revision'],
                       'license': source['license'], 'files': files}
            (destination / 'MGD-SOURCE.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
        # Alle Konflikte prüfen, bevor die erste fertige Installation sichtbar wird.
        pending = []
        for name in names:
            existing = target / name
            if existing.exists() or existing.is_symlink():
                if not same_tree(existing, stage / name):
                    raise FileExistsError('Bestehender Skill bleibt unangetastet: ' + name)
            else:
                pending.append(name)
        for name in pending:
            destination = target / name
            # Exklusiv reservieren: kein fremdes, inzwischen angelegtes Ziel ersetzen.
            destination.mkdir()
            created.append(destination)
            for item in (stage / name).iterdir():
                os.rename(item, destination / item.name)
            (stage / name).rmdir()
        if command_root:
            command_root.mkdir(parents=True, exist_ok=True)
            for destination, data in command_files.items():
                # Exklusive Anlage: Ein zwischenzeitlich erstellter Befehl bleibt erhalten.
                with destination.open('xb') as handle:
                    created_commands.append(destination)
                    handle.write(data)
        return names
    except Exception:
        # Ausschließlich in diesem Aufruf neu angelegte Verzeichnisse zurücknehmen.
        for command in reversed(created_commands):
            command.unlink()
        for directory in reversed(created):
            shutil.rmtree(directory)
        raise
    finally:
        shutil.rmtree(stage)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path, help='z. B. PROJEKT/.agents/skills')
    parser.add_argument('--profile', action='append', default=[], help='core, youtube, ads, remotion, math, react-ui, cloud-media, blender')
    parser.add_argument('--apply', action='store_true', help='Plan tatsächlich ausführen')
    parser.add_argument('--aliases', action='store_true', help='Alle 14 spezialisierten Skill-Aufrufe installieren')
    parser.add_argument('--commands-target', type=Path, help='Optional: passende .claude/commands für Slash-Befehle')
    parser.add_argument('--cache', type=Path, help='Ausschließlich lokale, geprüfte Quellen verwenden')
    parser.add_argument('--global', dest='allow_global', action='store_true', help='Bewusst beauftragte globale Zielablage erlauben')
    args = parser.parse_args()
    try:
        install(args.target, args.profile, args.apply, args.cache, args.allow_global, aliases=args.aliases, commands_target=args.commands_target)
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')

if __name__ == '__main__':
    main()
