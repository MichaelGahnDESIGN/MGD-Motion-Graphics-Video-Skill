# Projektordner und Dateien

Ein eigenständiger Film braucht eine erkennbare Projektwurzel. Ein Sammelordner
mit mehreren Kunden oder Filmen ist dafür ungeeignet. Ein sinnvoller Aufbau ist:

```text
mein-film/
  BRIEF.md
  STORYBOARD.md
  project.json
  sources.json
  material/                 vorhandene, unveränderte Quellen
  assets/                   vorbereitete Ableitungen und lokale Schriften
  compositions/             bei Bedarf einzelne Szenen
  tools/                    projektspezifische Helfer
  exports/                  neue Versionen der fertigen Videos
  docs/arbeitsberichte/     beobachtete Prüfungen und Entscheidungen
  .tmp/                     temporäre Bilder, Logs und Prüfdateien
```

Das ist ein Vorschlag, kein Grund ein funktionierendes bestehendes Projekt
umzubauen. Der enthaltene Starter nutzt eine zentrale HTML-Komposition und kommt
ohne `compositions/` aus. Große Filme können getrennte Szenen erhalten.

`project.json` ist beim Starter die zentrale Quelle für Format, FPS und Zeiten.
`tools/build.py` erzeugt daraus Laufzeit und Sollwerte. Der Agent soll eine
verlängerte Schlusszeit nicht an fünf voneinander unabhängigen Stellen pflegen.

`sources.json` dokumentiert bei Bedarf `source`, Ableitung und `source_sha256`.
Relative Quellen beziehen sich bei der Prüfsoftware auf den Manifestordner.
Nutzungsrechte gehören als eigene Information dazu; eine Prüfsumme belegt nur
unveränderte Bytes.

Nutze verständliche Exportnamen, etwa `mein-film-reel-v003.mp4`. Große Rohmedien,
Modelle, Zugangsdaten und persönliche Quellen nicht automatisch ins öffentliche
Git-Repository aufnehmen. Die Aufbewahrung projektbezogen festlegen und nur
eindeutig zugeordnete temporäre Arbeitsdateien entfernen.
