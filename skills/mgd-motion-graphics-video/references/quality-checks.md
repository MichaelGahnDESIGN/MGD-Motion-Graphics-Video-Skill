# Prüfung des tatsächlichen Ergebnisses

## Vor dem vollständigen Render

Öffne Anfang, Szenenmitten, Übergänge, maximale Kamerabewegung und Schlusskarte.
Prüfe Schrift auf dem beabsichtigten Mobilformat, vollständige Figuren, weiche
Nebelränder, Masken, Text-/Motivüberschneidung und ausreichende Lesedauer.
Prüfe auch beliebiges Anspringen und rückwärts versetzte Zeitpunkte.

Beim Remotion-Starter lädt `run_pipeline.py … check` die Komposition in einem
echten vorhandenen Browser und prüft deren Metadaten sowie Konsolenfehler.
Das ist keine automatische Layoutprüfung: Schnappschüsse aller kritischen
Zeitpunkte mit `snapshot` erzeugen und tatsächlich ansehen. Bei FFmpeg das
gefilterte Ergebnis rendern und exportierte Frames beurteilen.

## Export

`scripts/verify_export.py` prüft Dimensionen, FPS, Dauer, vorhandene Frame-Metadaten
und einen vollständigen Decode. Optional prüft es Original-SHA-256, erwartet Ton
und schreibt echte Exportbilder. Codec, Pixelformat und Farbmarkierungen werden
berichtet, sind ohne projektspezifische Bewertung aber noch keine Lieferfreigabe.

```bash
python3 /PFAD/ZUM/SKILL/scripts/verify_export.py /PFAD/PROJEKT/exports/film-v001.mp4 --expected /PFAD/PROJEKT/.tmp/expected-export.json --report /PFAD/PROJEKT/docs/arbeitsberichte/export-v001.json --evidence /PFAD/PROJEKT/.tmp/qc-v001 --require-audio
```

`--require-audio` nur setzen, wenn das Video tatsächlich Ton haben soll. Die
Demo ist bewusst stumm. Für eigene Projekte die Sollwerte aus deren zentraler
Zeitplanung erzeugen. Ein `sources.json` für `--source-manifest` ist eine Liste
mit `source` und `source_sha256`; relative Quellen beziehen sich auf dessen Ordner.

**Die ausgegebenen Bilder tatsächlich ansehen und das Video anhören.** Prüfe
mindestens eine ruhige Schlussaufnahme nach vollständigem Texteinlauf und vor
dem Fade. Erwartete Snapshot-Anzahl gegen vorhandene Dateien prüfen; ein Werkzeug
kann angeforderte Zeiten zusammenfassen oder auslassen. Die Kontaktübersicht dient
zum Navigieren, feine Kanten zusätzlich in Originalauflösung prüfen.

## Nach Änderungen

Gezielt prüfen, was sich geändert hat: Mehr Schlusszeit verlangt aktualisierte
Gesamtdauer, Musik, Effekte und Framezahl. Ein reiner Textfix verlangt korrekte
Umbrüche und Lesedauer. Bei unverändertem, bereits bestandenem Stand keine teuren
Prüfserien ohne neuen Anlass. Ergebnis und Grenzen im Arbeitsbericht festhalten.
