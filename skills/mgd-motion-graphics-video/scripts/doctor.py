#!/usr/bin/env python3
"""Liest die Umgebung, ohne Pakete nachzuladen oder Einstellungen zu ändern."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess


def inspect_environment(skill_root=None):
    results = {'tools': {}, 'skills': {}}
    for name, args in {'python3':['--version'], 'node':['--version'], 'npm':['--version'],
                       'ffmpeg':['-version'], 'ffprobe':['-version'], 'git':['--version']}.items():
        executable = shutil.which(name)
        if not executable:
            results['tools'][name] = {'available': False}
            continue
        try:
            run = subprocess.run([executable, *args], capture_output=True, text=True, timeout=15)
            results['tools'][name] = {'available': run.returncode == 0,
                                     'version': (run.stdout or run.stderr).splitlines()[0]}
        except (OSError, subprocess.TimeoutExpired) as error:
            results['tools'][name] = {'available': False, 'error': type(error).__name__}
    if skill_root:
        for name in ('hyperframes', 'hyperframes-core', 'video-editing', 'remotion-video-creation'):
            results['skills'][name] = [alias for alias in (name, 'ecc-' + name)
                                      if (skill_root / alias / 'SKILL.md').is_file()]
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skills', type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect_environment(args.skills), ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
