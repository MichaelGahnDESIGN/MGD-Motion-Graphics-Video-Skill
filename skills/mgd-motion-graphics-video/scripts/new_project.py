#!/usr/bin/env python3
"""Legt einen neutralen, vollständig lokalen Motion-Graphics-Startpunkt an."""
import argparse
import json
from pathlib import Path
import shutil

PRESETS = {'reel': (1080, 1920), 'youtube': (1920, 1080), 'square': (1080, 1080)}


def create_project(destination, preset='reel', hold=4.0):
    if preset not in PRESETS or not 2 <= hold <= 60:
        raise ValueError('Format unbekannt oder Schluss-Haltezeit außerhalb 2–60 Sekunden')
    destination = Path(destination).expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Ziel existiert bereits; keine Dateien überschrieben')
    if any(p.is_symlink() for p in destination.parents):
        raise ValueError('Zielpfad enthält einen Symlink')
    source = Path(__file__).resolve().parents[1] / 'assets' / 'starter'
    # Exklusives mkdir außerhalb des Rollbacks: ein parallel erzeugtes fremdes
    # Ziel gehört uns nicht und darf bei FileExistsError nicht entfernt werden.
    destination.mkdir(parents=True)
    try:
        shutil.copytree(source, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        config = json.loads((destination / 'project.json').read_text(encoding='utf-8'))
        config.update(width=PRESETS[preset][0], height=PRESETS[preset][1], end_hold=hold)
        (destination / 'project.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        for folder in ('.tmp', 'exports', 'assets', 'docs/arbeitsberichte'):
            (destination / folder).mkdir(parents=True, exist_ok=True)
    except Exception:
        if destination.exists(): shutil.rmtree(destination)
        raise
    print(str(destination))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--preset', choices=PRESETS, default='reel')
    parser.add_argument('--end-hold', type=float, default=4)
    args = parser.parse_args()
    try: create_project(args.destination, args.preset, args.end_hold)
    except (OSError, ValueError) as error: parser.exit(1, str(error) + '\n')

if __name__ == '__main__': main()
