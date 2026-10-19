#!/usr/bin/env python3
"""Prüft echte Exportbytes und erzeugt Bilder zur anschließenden Sichtkontrolle.

Ein grüner Bericht belegt technische Prüfpunkte, niemals Gestaltung, Rechte oder
Abnahme auf Instagram. Bilder und Audiomessungen müssen passend bewertet werden.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess


def sha256(path):
    value=hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda:handle.read(4*1024*1024),b''): value.update(block)
    return value.hexdigest()


def inspect(video, expected, require_audio=False):
    data=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)],text=True))
    streams=data['streams']
    image=next((s for s in streams if s['codec_type']=='video'),None)
    if image is None: raise ValueError('Videospur fehlt')
    for key in ('width','height'):
        if image[key]!=expected[key]: raise ValueError('Falsches '+key)
    fps=float(Fraction(image['avg_frame_rate']))
    if abs(fps-expected['fps'])>0.001: raise ValueError('Falsche Bildrate')
    duration=float(image.get('duration',data['format']['duration']))
    if abs(duration-expected['duration'])>1/expected['fps']+0.001: raise ValueError('Falsche Dauer')
    count=image.get('nb_frames')
    if count and count!='N/A' and int(count)!=expected['frames']: raise ValueError('Falsche Frame-Anzahl')
    audio=next((s for s in streams if s['codec_type']=='audio'),None)
    if require_audio and not audio: raise ValueError('Erwartete Audiospur fehlt')
    subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(video),'-map','0:v:0','-map','0:a?','-f','null','-'],check=True,stdout=subprocess.DEVNULL)
    result={'technical_checks_passed':True,'width':image['width'],'height':image['height'],
            'fps':fps,'duration':duration,'frames_metadata':count,'codec':image['codec_name'],
            'pixel_format':image.get('pix_fmt'),'color':{k:image.get(k,'unspecified') for k in ('color_space','color_transfer','color_primaries')},
            'audio_present':audio is not None,'sha256':sha256(video),'visual_review':'REQUIRED'}
    if audio:
        measure=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-vn','-af','ebur128=peak=true','-f','null','-'],text=True,capture_output=True,check=True)
        result['audio_summary']=measure.stderr.rsplit('Summary:',1)[-1].strip()
    return result


def verify_sources(manifest):
    entries=json.loads(Path(manifest).read_text(encoding='utf-8'))
    for entry in entries:
        path=Path(entry['source'])
        if not path.is_absolute(): path=Path(manifest).parent/path
        if sha256(path)!=entry['source_sha256']:
            raise ValueError('Original-Prüfsumme abweichend: '+path.name)
    return len(entries)


def make_evidence(video, expected, destination):
    destination=Path(destination)
    if destination.exists(): raise FileExistsError('QC-Ziel existiert bereits')
    destination.mkdir(parents=True)
    duration=expected['duration']
    times=[min(duration-1/expected['fps'],t) for t in (0.5,duration*0.35,duration*0.6,expected.get('readable_from',duration*0.75)+0.2,duration-expected.get('end_fade',0.5)-0.1)]
    for index,at in enumerate(times):
        subprocess.run(['ffmpeg','-v','error','-n','-ss',str(at),'-i',str(video),'-frames:v','1',str(destination/f'frame-{index:02d}.png')],check=True)
    subprocess.run(['ffmpeg','-v','error','-n','-i',str(destination/'frame-%02d.png'),'-vf','scale=216:-1,tile=5x1','-frames:v','1',str(destination/'contact-sheet.jpg')],check=True)
    return times


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video',type=Path)
    parser.add_argument('--expected',required=True,type=Path)
    parser.add_argument('--report',required=True,type=Path)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--source-manifest',type=Path)
    parser.add_argument('--require-audio',action='store_true')
    args=parser.parse_args()
    if args.report.exists(): parser.exit(1,'Bericht existiert bereits\n')
    try:
        expected=json.loads(args.expected.read_text(encoding='utf-8'))
        report=inspect(args.video,expected,args.require_audio)
        if args.source_manifest: report['unchanged_sources']=verify_sources(args.source_manifest)
        if args.evidence: report['evidence_times']=make_evidence(args.video,expected,args.evidence)
        args.report.parent.mkdir(parents=True,exist_ok=True)
        with args.report.open('x',encoding='utf-8') as handle: json.dump(report,handle,ensure_ascii=False,indent=2)
        print(json.dumps(report,ensure_ascii=False,indent=2))
    except (ValueError,OSError,subprocess.CalledProcessError) as error: parser.exit(1,str(error)+'\n')

if __name__=='__main__': main()
