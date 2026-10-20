# Technische Referenz und ausführbare Beispiele

Alle Beispiele verwenden Platzhalterpfade. Ersetze sie durch die echten absoluten
Pfade. Repository-Befehle starten im Hauptordner des heruntergeladenen Skills.

| Skript | Zweck | Schreibwirkung |
|---|---|---|
| `doctor.py` | Werkzeuge und ausgewählte Skill-Namen prüfen | Keine Installation |
| `commands.py list` | Alle 14 Aufrufe anzeigen | Nur Textausgabe |
| `commands.py show AUFRUF` | Prompt mit eigenen Angaben erzeugen | Nur Textausgabe |
| `install.py` | Hauptskill, Aufrufe und gewählte Profile installieren | Erst mit `--apply` |
| `new_project.py` | Neuen neutralen Filmordner erzeugen | Neues Ziel, kein Überschreiben |
| `setup_tools.py` | Gepinnte npm-Werkzeuge im Starter installieren | Erst mit `--apply` |
| `run_pipeline.py` | Check, Snapshot oder Render | Projektbezogene Prüfdaten/Export |
| `verify_export.py` | Tatsächliche MP4-Datei und ggf. Originale prüfen | Neue Berichte und Prüfbilder |

## Einen Demo-Film erzeugen

```bash
python3 skills/mgd-motion-graphics-video/scripts/new_project.py /PFAD/PROJEKT/film --preset reel --end-hold 6
python3 skills/mgd-motion-graphics-video/scripts/setup_tools.py /PFAD/PROJEKT/film --apply
cd /PFAD/PROJEKT/film
python3 tools/build.py
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . check
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . snapshot --at 1,4,8,12
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . render --output exports/film-v001.mp4
python3 /PFAD/ZUM/SKILL/scripts/verify_export.py exports/film-v001.mp4 --expected .tmp/expected-export.json --report docs/arbeitsberichte/export-v001.json --evidence .tmp/qc-v001
```

Bei sechs Sekunden Schluss-Haltezeit dauert der sonst unveränderte Starter
13,5 Sekunden beziehungsweise 405 Frames bei 30 fps. Der Gesamtwert entsteht
aus Intro + Mittelteil + Schlusseinlauf + Haltezeit + Schluss-Fade. Bruchteile
außerhalb einer Framegrenze werden abgelehnt.

## Grenzen der Helfer

Die Pipeline ist auf den mitgelieferten Starter ausgelegt und ersetzt keine
vollständige Schnittsoftware. Vorgesehen sind FFmpeg oder Remotion. Andere
lokale Video-Skills vor Auswahl oder Aufruf ausdrücklich abfragen. Alte
Projektordner erhalten und bei Bedarf eine passende Ableitung erstellen. Die Exportprüfung belegt technische
Eigenschaften und schreibt Bilder, beurteilt deren Gestaltung aber nicht selbst.
