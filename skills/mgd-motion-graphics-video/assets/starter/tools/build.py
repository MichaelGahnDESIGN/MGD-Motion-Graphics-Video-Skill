#!/usr/bin/env python3
"""Eine Zeitquelle für Timeline, Bildformat, Lesedauer und Export-Sollwerte."""
import html
import json
import math
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]

def derive(config):
    for name in ('width', 'height', 'fps'):
        if type(config[name]) is not int or config[name] <= 0:
            raise ValueError('Positive Ganzzahl erwartet: ' + name)
    if config['width'] % 2 or config['height'] % 2:
        raise ValueError('H.264 braucht gerade Bildabmessungen')
    for name in ('intro_duration', 'middle_duration', 'end_entrance', 'end_hold', 'end_fade'):
        value = config[name]
        if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
            raise ValueError('Positive Zeit erwartet: ' + name)
    end_start = config['intro_duration'] + config['middle_duration']
    readable = end_start + config['end_entrance']
    duration = readable + config['end_hold'] + config['end_fade']
    frames = round(duration * config['fps'])
    if abs(frames / config['fps'] - duration) > 1e-7:
        raise ValueError('Gesamtdauer liegt nicht auf einer Frame-Grenze')
    return {**config, 'end_start':end_start, 'readable_from':readable, 'duration':duration, 'frames':frames}

def build(root=ROOT):
    config = derive(json.loads((root/'project.json').read_text(encoding='utf-8')))
    gsap = root/'node_modules/gsap/dist/gsap.min.js'
    if not gsap.is_file(): raise FileNotFoundError('Zuerst npm ci --ignore-scripts ausführen.')
    (root/'assets').mkdir(exist_ok=True)
    shutil.copyfile(gsap, root/'assets/gsap.min.js')
    template = (root/'template.html').read_text(encoding='utf-8')
    template = template.replace('{{composition_id}}', 'data-composition-id="main"')
    for name in ('width','height','fps','duration','headline','message','brand','tagline'):
        template = template.replace('{{'+name+'}}',html.escape(str(config[name]),quote=True))
    (root/'index.html').write_text(template,encoding='utf-8')
    (root/'runtime-config.js').write_text('window.MGD_CONFIG = '+json.dumps(config,ensure_ascii=True)+';\n',encoding='utf-8')
    (root/'.tmp').mkdir(exist_ok=True)
    (root/'.tmp/expected-export.json').write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:config[k] for k in ('width','height','duration','frames','readable_from')},indent=2))
    return config

if __name__=='__main__': build()
