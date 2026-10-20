# Entwicklung, Tests und Veröffentlichung

## Eine Quelle für alle Aufrufe

`assets/commands.json` im Hauptskill definiert Namen, Arbeitsmodus, Hinweise und
Prompt. Daraus erzeugt `tools/build_commands.py` die spezialisierten Skills,
Claude-Befehle und die Befehlsseite dieses Wikis. Der Installer kann dieselben
Varianten auch aus einem allein heruntergeladenen Hauptskill erzeugen.

```bash
python3 tools/build_commands.py
python3 tools/build_commands.py --check
python3 tools/check.py
```

Der Check soll Verhaltensfehler finden: keine Schreib-/Netzwerkaktionen im
Dry-Run, keine Änderungen bestehender Dateien, korrekte Rücknahme bei Fehlern,
richtige Aufrufauflösung, sichere Zielpfade und passende Export-Sollwerte. Eine
Überschriftenprüfung allein belegt keine funktionierende Installation.

## Wann ein neuer Render nötig ist

Ändern sich Timeline, Starter oder Laufzeit, ist ein echter Browsercheck und
Testexport erforderlich. Eine reine Dokumentations- oder Aufrufänderung braucht
keinen unveränderten Film erneut zu rendern. Ab 0.4.0 den Remotion-Starter prüfen;
historische Nachweise gelten ausschließlich für ihre damalige Laufzeit. Neue Aussagen über geänderte Anbieter oder
Plattformen müssen gesondert geprüft werden.

## Wiki und Releases

Das Wiki liegt unter `docs/wiki/` versioniert und wird zusätzlich im GitHub-Wiki
veröffentlicht. `tools/sync_wiki.py` übersetzt lokale Markdown-Verweise in passende
Wiki-Links und übernimmt keine privaten Arbeitsberichte. Direkte Wiki-Änderungen
müssen vor dem nächsten Abgleich geprüft werden, damit nichts unbemerkt verloren geht.

Versionsnummern in Plugin-Metadaten und Aufrufkatalog gemeinsam pflegen. Ein
Release kann den installierbaren Hauptskill samt Katalog, zusätzliche Vorlagen und
Prüfsummen enthalten. Nur vorgemerkte öffentliche Dateien paketieren; `.tmp`,
Zugangsdaten und private Projekte gehören nicht ins Release.
