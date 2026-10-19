"""Verhaltensprüfungen: keine Netzwerkzugriffe oder globalen Installationen."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/mgd-motion-graphics-video'
sys.path.insert(0,str(SKILL/'scripts'))
TMP=ROOT/'.tmp/tests'
TMP.mkdir(parents=True,exist_ok=True)

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

installer=load('mgd_install',SKILL/'scripts/install.py')
generator=load('mgd_generate',SKILL/'scripts/new_project.py')
builder=load('mgd_build',SKILL/'assets/starter/tools/build.py')
setup=load('mgd_setup',SKILL/'scripts/setup_tools.py')
verify=load('mgd_verify',SKILL/'scripts/verify_export.py')

class SkillTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=TMP)
        self.root=Path(self.temp.name)
        self.output=contextlib.redirect_stdout(io.StringIO());self.output.__enter__()

    def tearDown(self):
        self.output.__exit__(None,None,None);self.temp.cleanup()

    def tiny_source(self):
        cache=self.root/'cache/ecc';files=[]
        for path,data in [('LICENSE',b'MIT test fixture'),('skills/video-editing/SKILL.md',b'---\nname: video-editing\ndescription: fixture\n---\n')]:
            p=cache/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
            files.append({'path':path,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        return {'sources':{'ecc':{'repository':'affaan-m/ecc','revision':'a'*40,'license':'MIT','files':files}},'profiles':{'test':{'ecc':['video-editing']}}}

    def test_dry_run_does_not_write_or_download(self):
        target=self.root/'missing/skills'
        with patch.object(installer.urllib.request,'urlopen',side_effect=AssertionError('Netzwerk im Dry-Run')):
            installer.install(target,['core'])
        self.assertFalse(target.exists())

    def test_install_offline_with_provenance_and_idempotence(self):
        lock=self.tiny_source();target=self.root/'skills'
        installer.install(target,['test'],True,self.root/'cache',lock=lock)
        self.assertTrue((target/'video-editing/LICENSE.upstream').is_file())
        self.assertTrue((target/'video-editing/MGD-SOURCE.json').is_file())
        before=(target/'video-editing/SKILL.md').read_bytes()
        installer.install(target,['test'],True,self.root/'cache',lock=lock)
        self.assertEqual((target/'video-editing/SKILL.md').read_bytes(),before)
        self.assertFalse(list(target.glob('.mgd-install-*')))

    def test_conflict_keeps_existing_and_installs_nothing(self):
        lock=self.tiny_source();target=self.root/'skills'
        (target/'video-editing').mkdir(parents=True)
        (target/'video-editing/SKILL.md').write_text('Persönliche Änderung')
        with self.assertRaises(FileExistsError):
            installer.install(target,['test'],True,self.root/'cache',lock=lock)
        self.assertEqual((target/'video-editing/SKILL.md').read_text(),'Persönliche Änderung')
        self.assertFalse((target/SKILL.name).exists())

    def test_bad_hash_leaves_no_skill(self):
        lock=self.tiny_source();lock['sources']['ecc']['files'][1]['sha256']='0'*64
        target=self.root/'skills'
        with self.assertRaises(ValueError):
            installer.install(target,['test'],True,self.root/'cache',lock=lock)
        self.assertEqual(list(target.iterdir()),[])

    def test_traversal_rejected(self):
        for value in ('../secret','/etc/passwd','a/../../b','C:\\temp','a\\b'):
            with self.assertRaises(ValueError,msg=value):installer.safe_relative(value)

    def test_symlink_target_rejected(self):
        real=self.root/'real';real.mkdir()
        (self.root/'link').symlink_to(real,target_is_directory=True)
        with self.assertRaises(ValueError):installer.install(self.root/'link/skills',[])
        self.assertEqual(list(real.iterdir()),[])

    def test_cache_symlink_escape_rejected(self):
        lock=self.tiny_source();entry=lock['sources']['ecc']['files'][1]
        p=self.root/'cache/ecc'/entry['path'];p.unlink()
        outside=self.root/'outside';outside.write_bytes(b'secret')
        p.symlink_to(outside)
        with self.assertRaises(ValueError):installer.checked_data('ecc',lock['sources']['ecc'],entry,self.root/'cache')

    def test_global_needs_explicit_option(self):
        with self.assertRaises(ValueError):installer.install(Path.home()/'.codex/skills',[])

    def test_parent_segments_cannot_bypass_global_guard(self):
        with self.assertRaises(ValueError):installer.install(Path.home()/'project/../.codex/skills',[])

    def test_extra_directory_symlink_is_not_identical(self):
        first=self.root/'first';second=self.root/'second';first.mkdir();second.mkdir()
        (first/'same').write_text('x');(second/'same').write_text('x')
        (first/'extra').symlink_to(second,target_is_directory=True)
        self.assertFalse(installer.same_tree(first,second))

    def test_racing_generator_target_is_preserved(self):
        destination=self.root/'racing'
        original=Path.mkdir
        def race(path,*args,**kwargs):
            if path==destination:
                original(path)
                (path/'foreign').write_text('behalten')
                raise FileExistsError('parallel angelegt')
            return original(path,*args,**kwargs)
        with patch.object(Path,'mkdir',race):
            with self.assertRaises(FileExistsError):generator.create_project(destination)
        self.assertEqual((destination/'foreign').read_text(),'behalten')

    def test_unknown_profile_rejected(self):
        with self.assertRaises(ValueError):installer.install(self.root/'skills',['not-a-profile'])

    def test_generator_all_formats_and_reading_hold(self):
        for name,size in generator.PRESETS.items():
            destination=generator.create_project(self.root/name,name,7)
            config=builder.derive(json.loads((destination/'project.json').read_text()))
            self.assertEqual((config['width'],config['height']),size)
            self.assertEqual(config['duration'],14.5)
            self.assertEqual(config['frames'],435)
            self.assertEqual(config['readable_from'],7)
            self.assertEqual(config['duration']-config['end_fade']-config['readable_from'],7)

    def test_generator_never_overwrites(self):
        destination=self.root/'exists';destination.mkdir()
        marker=destination/'marker';marker.write_text('behalten')
        with self.assertRaises(FileExistsError):generator.create_project(destination)
        self.assertEqual(marker.read_text(),'behalten')

    def test_invalid_timing_and_dimensions_rejected(self):
        config=json.loads((SKILL/'assets/starter/project.json').read_text())
        for key,value in [('end_hold',float('nan')),('end_hold',-1),('width',1081),('fps',0),('end_hold',4.001)]:
            with self.assertRaises(ValueError,msg=key):builder.derive({**config,key:value})

    def test_tool_setup_dry_run_cannot_spawn(self):
        project=generator.create_project(self.root/'film')
        with patch.object(setup.subprocess,'run',side_effect=AssertionError('Ausführung im Dry-Run')):
            setup.setup(project)

    def test_source_hash_detects_changes(self):
        source=self.root/'source.png';source.write_bytes(b'original')
        manifest=self.root/'sources.json'
        manifest.write_text(json.dumps([{'source':'source.png','source_sha256':verify.sha256(source)}]))
        self.assertEqual(verify.verify_sources(manifest),1)
        source.write_bytes(b'modified')
        with self.assertRaises(ValueError):verify.verify_sources(manifest)

    @unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'),'FFmpeg fehlt')
    def test_real_export_decode_and_wrong_delivery_rejected(self):
        video=self.root/'tiny.mp4'
        subprocess.run(['ffmpeg','-v','error','-n','-f','lavfi','-i','color=c=navy:s=64x96:r=30:d=0.3','-c:v','mpeg4','-pix_fmt','yuv420p',str(video)],check=True)
        expected={'width':64,'height':96,'fps':30,'duration':0.3,'frames':9}
        result=verify.inspect(video,expected)
        self.assertTrue(result['technical_checks_passed'])
        for change in ({'width':96},{'fps':25},{'duration':1},{'frames':10}):
            with self.assertRaises(ValueError):verify.inspect(video,{**expected,**change})
        with self.assertRaises(ValueError):verify.inspect(video,expected,require_audio=True)

    def test_manifest_profiles_have_real_skills_and_bounded_hashes(self):
        lock=json.loads((SKILL/'dependencies.lock.json').read_text())
        for profile in lock['profiles']:
            for package in installer.select_packages(lock,[profile]):
                for f in package[4]:
                    installer.safe_relative(f['path'])
                    self.assertLessEqual(f['size'],installer.MAX_FILE)
                    self.assertRegex(f['sha256'],r'^[a-f0-9]{64}$')

if __name__=='__main__':unittest.main()
