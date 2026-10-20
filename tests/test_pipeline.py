"""Die neue Laufzeit schützt Exporte und lädt niemals still Werkzeuge nach."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT/'skills/mgd-motion-graphics-video'
TMP = ROOT/'.tmp/tests'
TMP.mkdir(parents=True, exist_ok=True)


def load(name):
    spec = importlib.util.spec_from_file_location(name, CORE/'scripts'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pipeline = load('run_pipeline')
setup = load('setup_tools')
installer = load('install')


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=TMP)
        self.root = Path(self.temp.name)
        (self.root/'node_modules/@remotion/renderer').mkdir(parents=True)
        (self.root/'node_modules/@remotion/renderer/package.json').write_text('{}')
        (self.root/'runtime-config.json').write_text(json.dumps({'fps':30,'frames':345}))
        self.browser = self.root/'chrome'
        self.browser.write_text('test')

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_browser_cannot_download(self):
        with patch.object(pipeline, 'browser_path', side_effect=FileNotFoundError('Browser fehlt')):
            with patch.object(pipeline.subprocess, 'run') as spawn:
                with self.assertRaises(FileNotFoundError): pipeline.run(self.root, 'check')
                spawn.assert_not_called()

    def test_existing_export_preserved_before_any_execution(self):
        output = self.root/'old.mp4'; output.write_bytes(b'original')
        with patch.object(pipeline.subprocess, 'run') as spawn:
            with self.assertRaises(FileExistsError): pipeline.run(self.root,'render',Path('old.mp4'))
            spawn.assert_not_called()
        self.assertEqual(output.read_bytes(),b'original')

    def test_symlink_cannot_export_outside_project(self):
        outside = self.root.parent/(self.root.name+'-outside')
        (self.root/'escape').symlink_to(self.root.parent, target_is_directory=True)
        with patch.object(pipeline.subprocess, 'run') as spawn:
            with self.assertRaises(ValueError): pipeline.run(self.root,'render',Path('escape')/outside.name)
            spawn.assert_not_called()
        self.assertFalse(outside.exists())

    def test_out_of_range_snapshot_never_starts_browser(self):
        with patch.object(pipeline.subprocess, 'run') as spawn:
            with self.assertRaises(ValueError): pipeline.run(self.root,'snapshot',at='12',browser=str(self.browser))
        self.assertEqual(spawn.call_count,1)  # Nur die lokale Zeitplanung wurde erneuert.

    def test_render_publishes_only_after_success_and_uses_local_runtime(self):
        def fake(args, **kwargs):
            if args[0]=='node':
                Path(args[3],'export.mp4').write_bytes(b'new video')
                self.assertEqual(args[1],'tools/runtime.mjs')
                self.assertNotIn('npx', args)
        with patch.object(pipeline.subprocess,'run',side_effect=fake):
            pipeline.run(self.root,'render',Path('exports/new.mp4'),browser=str(self.browser))
        self.assertEqual((self.root/'exports/new.mp4').read_bytes(),b'new video')

    def test_retired_dependency_source_cannot_be_selected(self):
        self.assertEqual(installer.ALLOWLIST, {'affaan-m/ecc'})
        lock=json.loads((CORE/'dependencies.lock.json').read_text())
        self.assertEqual(set(lock['sources']), {'ecc'})
        self.assertNotIn('youtube',lock['profiles'])
        package=json.loads((CORE/'assets/starter/package.json').read_text())
        self.assertEqual(set(package['dependencies']), {'remotion','@remotion/renderer','@remotion/bundler','react','react-dom'})

    def test_modified_starter_cannot_trigger_unreviewed_package_install(self):
        package=json.loads((CORE/'assets/starter/package.json').read_text())
        package['dependencies']['unreviewed-package']='1.0.0'
        (self.root/'package.json').write_text(json.dumps(package))
        with patch.object(setup.subprocess,'run') as spawn:
            with self.assertRaises(ValueError): setup.setup(self.root,True)
            spawn.assert_not_called()


if __name__ == '__main__': unittest.main()
