#!/usr/bin/env python3
"""Erstellt nach bewusster Versionswahl die Prüfsummen der optionalen Skill-Quellen.

Kein Upstream-Programm wird ausgeführt. Die Downloads dienen ausschließlich der
Quellenprüfung. Änderungen dieser Sperrdatei müssen vor einer Veröffentlichung
geprüft werden; der normale Installer aktualisiert sie niemals selbst.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / '.tmp' / 'mgd-skill'
SKILL = ROOT / 'skills' / 'mgd-motion-graphics-video'
SOURCES = {
 'hyperframes': {'repository':'heygen-com/hyperframes','revision':'7d47194e4a078b4382bf3e8597ca9520e278781c',
 'skills':['hyperframes','hyperframes-core','hyperframes-keyframes','hyperframes-animation','hyperframes-creative','hyperframes-cli','hyperframes-audio','hyperframes-registry','media-use','general-video','motion-graphics','embedded-captions','faceless-explainer','talking-head-recut','product-launch-video']},
 'ecc': {'repository':'affaan-m/ecc','revision':'6c557856af89a657f846a8ca15907cbdc1e41530',
 'skills':['video-editing','remotion-video-creation','manim-video','brand-discovery','brand-voice','motion-foundations','motion-patterns','motion-advanced','fal-ai-media','tasteforge-video','videodb','blender-motion-state-inspection']}
}

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'MGD-Motion-Graphics-Lock/0.1'})
    with urllib.request.urlopen(req,timeout=60) as response:
        data=response.read(4*1024*1024+1)
    if len(data)>4*1024*1024:
        raise ValueError('Einzeldatei zu groß: '+url)
    return data

def main():
    WORK.mkdir(parents=True,exist_ok=True)
    lock={'schema':1,'checked_on':'2026-10-20','sources':{},'profiles':{
      'core':{'hyperframes':SOURCES['hyperframes']['skills'][:11],'ecc':['video-editing']},
      'youtube':{'hyperframes':['embedded-captions','faceless-explainer','talking-head-recut']},
      'ads':{'hyperframes':['product-launch-video'],'ecc':['brand-discovery','brand-voice']},
      'remotion':{'ecc':['remotion-video-creation']},
      'math':{'ecc':['manim-video']},
      'react-ui':{'ecc':['motion-foundations','motion-patterns','motion-advanced']},
      'cloud-media':{'ecc':['fal-ai-media','tasteforge-video','videodb']},
      'blender':{'ecc':['blender-motion-state-inspection']}}}
    for key,source in SOURCES.items():
        raw=subprocess.run(['gh','api',f"repos/{source['repository']}/git/trees/{source['revision']}?recursive=1"],capture_output=True,text=True,check=True)
        tree=json.loads(raw.stdout)
        if tree.get('truncated'): raise ValueError('Unvollständiger Git-Baum')
        prefixes=tuple('skills/'+name+'/' for name in source['skills'])
        entries=[x for x in tree['tree'] if x['type']=='blob' and (x['path'].startswith(prefixes) or x['path'] in ('LICENSE','LICENSE.md','LICENSE.txt'))]
        if any(x['mode'] not in ('100644','100755') for x in entries): raise ValueError('Keine Symlinks erlaubt')
        def obtain(entry):
            rel=entry['path']
            data=fetch(f"https://raw.githubusercontent.com/{source['repository']}/{source['revision']}/{rel}")
            if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=entry['sha']:
                raise ValueError('Git-Hash stimmt nicht: '+rel)
            target=WORK/'upstream-cache'/key/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(data)
            return {'path':rel,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()}
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            files=sorted(pool.map(obtain,entries),key=lambda x:x['path'])
        lock['sources'][key]={**source,'files':files,'license':'Apache-2.0' if key == 'hyperframes' else 'MIT'}
        print(key,len(files),sum(x['size'] for x in files),flush=True)
    (SKILL/'dependencies.lock.json').write_text(json.dumps(lock,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Sperrdatei erstellt',flush=True)

if __name__=='__main__': main()
