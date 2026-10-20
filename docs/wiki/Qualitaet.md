# Technische Prüfung, Sichtkontrolle und Abnahme

## Vor dem vollständigen Render

Kontrolliere Anfang, wichtige Szenen, Übergänge, maximale Kamerabewegung und die
Schlusskarte. Prüfe Schriftgröße, Umbrüche, vollständige Motive, Masken und die
Hierarchie von Effekten. Die Auswahl muss das ganze Video abdecken, nicht nur
besonders schöne Anfangsbilder. In einer suchbaren Timeline auch direkt zu
späten und früheren Zeiten springen.

Der Remotion-Check öffnet die Komposition im vorhandenen Browser und meldet
Metadaten beziehungsweise Konsolenfehler. Er erkennt nicht automatisch jede
Überlappung oder falsche Gestaltung. Kritische Frames mit `snapshot` erzeugen
und tatsächlich ansehen. FFmpeg-Filter ebenfalls am gerenderten Ergebnis prüfen.

## Tatsächlichen Export prüfen

```bash
python3 /PFAD/ZUM/SKILL/scripts/verify_export.py /PFAD/PROJEKT/exports/film-v002.mp4 --expected /PFAD/PROJEKT/.tmp/expected-export.json --report /PFAD/PROJEKT/docs/arbeitsberichte/export-v002.json --evidence /PFAD/PROJEKT/.tmp/qc-v002
```

Der Prüfer vergleicht Größe, FPS und Dauer, prüft vorhandene Frame-Metadaten und
führt einen vollständigen Decode aus. Er berichtet Codec, Pixel- und Farbraum
sowie vorhandenen Ton. `--require-audio` nur bei erwarteter Audiospur verwenden.
Ein `--source-manifest` kann wichtige Original-Prüfsummen kontrollieren.

## Bilder und Ton wirklich beurteilen

Sieh die erzeugten Bilder tatsächlich an. Prüfe feine Kanten in voller Auflösung,
lese die vollständig eingeblendete Schlusskarte und höre den Ton ab. Anzahl der
angeforderten und vorhandenen Bilder vergleichen: Ein Tool kann Zeiten ergänzen
oder auslassen. Bei einem Loop mehrere Übergänge abspielen.

Ein Bericht nennt Version, ausgeführte Prüfungen, beobachtete Gestaltung und offene
Grenzen. Keine Rechtefreigabe, Cloud-Prüfung oder echte Plattformabnahme erfinden.
Die Prüfung einer geänderten Schlusszeit muss auch Musik, FX und Gesamtdauer
umfassen; ein reiner Textfix braucht insbesondere neue Umbruch- und Lesekontrolle.
