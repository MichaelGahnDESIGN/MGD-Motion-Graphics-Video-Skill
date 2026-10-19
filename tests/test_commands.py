"""Beobachtbares Verhalten der Aufrufvarianten und ihrer Installation."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
CORE=ROOT/'skills/mgd-motion-graphics-video'
sys.path.insert(0,str(CORE/'scripts'))
from command_catalog import load_catalog,render_prompt,resolve


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

installer=load('command_install',CORE/'scripts/install.py')
wiki=load('wiki_sync',ROOT/'tools/sync_wiki.py')
generator=load('command_build',ROOT/'tools/build_commands.py')
TMP=ROOT/'.tmp/tests';TMP.mkdir(parents=True,exist_ok=True)

class CommandTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=TMP);self.root=Path(self.tmp.name)
        self.silent=contextlib.redirect_stdout(io.StringIO());self.silent.__enter__()
    def tearDown(self):self.silent.__exit__(None,None,None);self.tmp.cleanup()

    def test_requested_aliases_resolve_to_their_workflow(self):
        wanted={'/MGD-Motion':'start','/reel':'reel','/MGD-Video':'video','/MGD-Reel':'reel',
                '/MGD-Trailer':'trailer','/MGD-Erklärvideo':'explainer','/MGD-Motion-Graphic-Animation':'motion',
                '/MGD-Anime':'anime','/MGD-Werbefilm':'ad','/MGD-Produktvideo':'product','/MGD-YouTube':'youtube',
                '/MGD-Logo-Animation':'logo','/MGD-Loop':'loop','/MGD-Video-Optimieren':'optimize'}
        self.assertEqual(len(load_catalog()['commands']),len(wanted))
        for name,mode in wanted.items():
            item=resolve(name);self.assertEqual(item['mode'],mode)
            self.assertEqual(resolve('$'+item['skill'])['command'],item['command'])
        with self.assertRaises(ValueError):resolve('/MGD-Optimieren')

    def test_unicode_and_case_work_for_lookup(self):
        self.assertEqual(resolve('/mgd-Erkla\u0308rvideo')['skill'],'mgd-erklaervideo')

    def test_unicode_equivalent_template_filename_is_read_without_rewrite(self):
        existing=self.root/'MGD-Erkla\u0308rvideo.md';existing.write_text('Vorlage bleibt erhalten')
        wanted=self.root/'MGD-Erklärvideo.md'
        actual=generator.equivalent_path(wanted)
        self.assertEqual(actual.read_text(),'Vorlage bleibt erhalten')
        self.assertEqual(len(list(self.root.iterdir())),1)

    def test_prompt_interpolation_is_only_text(self):
        value='$(touch SHOULD_NOT_EXIST) {kein_python}'
        text=render_prompt(resolve('/MGD-Reel'),{'thema':value,'ordner':'/EXAMPLE/PROJEKT'})
        self.assertIn(value,text);self.assertIn('/EXAMPLE/PROJEKT',text)
        self.assertFalse((self.root/'SHOULD_NOT_EXIST').exists())

    def test_alias_dry_run_writes_neither_root(self):
        skills=self.root/'.claude/skills';commands=self.root/'.claude/commands'
        with patch.object(installer.urllib.request,'urlopen',side_effect=AssertionError('Netzwerk')):
            names=installer.install(skills,[],aliases=True,commands_target=commands)
        self.assertEqual(len(names),15);self.assertFalse(skills.exists());self.assertFalse(commands.exists())

    def test_native_command_installation_and_repeat_are_consistent(self):
        skills=self.root/'.claude/skills';commands=self.root/'.claude/commands'
        installer.install(skills,[],apply=True,aliases=True,commands_target=commands)
        first={p.name:p.read_bytes() for p in commands.glob('*.md')}
        self.assertEqual(len(first),14)
        for item in load_catalog()['commands']:
            self.assertTrue((skills/item['skill']/'SKILL.md').is_file())
            self.assertIn('../skills/mgd-motion-graphics-video/SKILL.md',(commands/(item['command']+'.md')).read_text())
        installer.install(skills,[],apply=True,aliases=True,commands_target=commands)
        self.assertEqual(first,{p.name:p.read_bytes() for p in commands.glob('*.md')})

    def test_conflicting_command_does_not_install_any_skill(self):
        skills=self.root/'.claude/skills';commands=self.root/'.claude/commands';commands.mkdir(parents=True)
        existing=commands/'MGD-Reel.md';existing.write_text('Persönliche Vorlage')
        with self.assertRaises(FileExistsError):installer.install(skills,[],apply=True,aliases=True,commands_target=commands)
        self.assertEqual(existing.read_text(),'Persönliche Vorlage')
        self.assertFalse((skills/'mgd-motion-graphics-video').exists())
        self.assertFalse(skills.exists())

    def test_preview_reports_personal_command_without_writing(self):
        skills=self.root/'.claude/skills';commands=self.root/'.claude/commands';commands.mkdir(parents=True)
        path=commands/'MGD-Reel.md';path.write_text('Persönlich')
        stream=io.StringIO()
        with contextlib.redirect_stdout(stream):installer.install(skills,[],aliases=True,commands_target=commands)
        self.assertIn('/MGD-Reel',json.loads(stream.getvalue())['conflicts'])
        self.assertFalse(skills.exists());self.assertEqual(path.read_text(),'Persönlich')

    def test_bad_command_layout_rejected_before_writing(self):
        skills=self.root/'skills'
        with self.assertRaises(ValueError):installer.install(skills,[],apply=True,aliases=True,commands_target=skills)
        with self.assertRaises(ValueError):installer.install(skills,[],commands_target=self.root/'commands')
        self.assertFalse(skills.exists())

    def test_command_failure_rolls_back_new_skills_and_commands(self):
        skills=self.root/'.claude/skills';commands=self.root/'.claude/commands'
        old_open=Path.open;writes=[]
        def fail_second(path,mode='r',*args,**kwargs):
            if path.parent==commands and mode=='xb':
                writes.append(path)
                if len(writes)==2:raise OSError('Simulierter Schreibfehler')
            return old_open(path,mode,*args,**kwargs)
        with patch.object(Path,'open',fail_second):
            with self.assertRaises(OSError):installer.install(skills,[],apply=True,aliases=True,commands_target=commands)
        self.assertEqual(list(skills.iterdir()),[]);self.assertEqual(list(commands.iterdir()),[])

    def test_wiki_links_are_correct_for_both_publications(self):
        source=ROOT/'docs/wiki/Home.md'
        text='[Start](Erste-Schritte.md) [Quelle](../../README.md) [Abschnitt](Befehle.md#beispiele)'
        changed=wiki.transform(text,source)
        self.assertIn('[Start](Erste-Schritte)',changed)
        self.assertIn('/blob/main/README.md',changed)
        self.assertIn('[Abschnitt](Befehle#beispiele)',changed)
        self.assertNotIn('../../README.md',changed)

    def test_direct_wiki_change_is_never_silently_overwritten(self):
        checkout=self.root/'wiki';checkout.mkdir();page=checkout/'Home.md';page.write_text('alter Stand')
        (checkout/wiki.STATE).write_text(json.dumps({'files':{'Home.md':wiki.sha('alter Stand')}}))
        wiki.verify_remote(checkout,{'Home.md':'neuer Stand'})
        page.write_text('direkte Änderung eines anderen Bearbeiters')
        with self.assertRaises(ValueError):wiki.verify_remote(checkout,{'Home.md':'neuer Stand'})
        self.assertEqual(page.read_text(),'direkte Änderung eines anderen Bearbeiters')

    def test_initial_wiki_adoption_is_explicit(self):
        checkout=self.root/'wiki';checkout.mkdir();(checkout/'Home.md').write_text('Startseite')
        with self.assertRaises(ValueError):wiki.verify_remote(checkout,{'Home.md':'Handbuch'})
        wiki.verify_remote(checkout,{'Home.md':'Handbuch'},initialize=True)

    def test_wiki_dry_run_does_not_access_network_or_checkout(self):
        checkout=ROOT/'.tmp/wiki-dry-run-unwritten'
        with patch.object(wiki,'git',side_effect=AssertionError('Git im Dry-Run')):
            wiki.sync(checkout)
        self.assertFalse(checkout.exists())

if __name__=='__main__':unittest.main()
