# Installation und Voraussetzungen

Die Installation verändert ausschließlich das angegebene Skill-Ziel. Ohne
`--apply` entstehen weder Dateien noch Netzwerkzugriffe. Eine leere Profilauswahl
installiert nur den MGD-Skill; Zusatzskills werden ausdrücklich ausgewählt.

Vom Repository-Hauptordner aus:

```bash
python3 skills/mgd-motion-graphics-video/scripts/doctor.py
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.agents/skills --profile core
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.agents/skills --profile core --apply
```

`/PFAD/PROJEKT` ist ein bewusst gewählter absoluter Projektpfad. Bereits
abweichende Skill-Ordner führen zum Abbruch; exakt gleiche werden übersprungen.
Updates sind bewusst vorzubereiten, nicht mit einem erzwungenen Überschreiben.
Vorhandene lokale ECC-Varianten können stattdessen direkt verwendet werden;
dann das entsprechende Installationsprofil weglassen.

| Profil | Ergänzung | Wann sinnvoll |
|---|---|---|
| `core` | HyperFrames-Basis, Medien, Audio, Motion Graphics; ECC video-editing | Neue lokale Videopipeline |
| `youtube` | Erklärvideo, eingebettete Untertitel, Talking Head | Interview/Erklärvideo |
| `ads` | Produktvideo, Markenfindung und Markensprache | Werbefilm |
| `remotion` | ECC Remotion | Gewähltes React-Videoprojekt |
| `math` | ECC Manim | Mathematische Visualisierung |
| `react-ui` | ECC Motion-Reihe | Weboberfläche, nicht pauschal ein MP4 |
| `cloud-media` | ECC fal.ai, Tasteforge, VideoDB | Bewusst gewählte externe Medienverarbeitung |
| `blender` | ECC Blender Motion State Inspection | Passendes Blender-Projekt |

Profile können wiederholt werden, z. B. `--profile core --profile youtube`.
Jede Fremddatei wird an einer festen Git-Revision und ihrem SHA-256 geprüft.
Es werden keine Upstream-Installationsskripte ausgeführt. Herkunft und Original-Lizenz (HyperFrames: Apache-2.0; ECC: MIT)
liegen anschließend in `MGD-SOURCE.json` und `LICENSE.upstream` des Zusatzskills.
Der Installer lädt nur ausgewählte Dateien, keine großen Repository-Archive.
Ein manipulationssicherer Transport ersetzt keine Vertrauensprüfung der Inhalte.

Eine **globale** Installation braucht einen entsprechenden Benutzerauftrag.
Erst dann beispielsweise `--target "$HOME/.codex/skills" --global --apply`
verwenden. Projektinstallation ist der Standard. Der Skill selbst ändert keine
Agent-Konfiguration, aktiviert keine Hooks und installiert keine Plugins.

## Lokale Videowerkzeuge

**Schriftabrufe vor vertraulichen Inhalten prüfen:** Die getestete Engine kann
Namen wie Georgia oder Arial automatisch Webfonts zuordnen und dafür Anfragen
mit aus dem Dokument gewonnenen Schriftzeichen an Google Fonts schicken.
Verwende lokal eingebundene, lizenzierte `@font-face`-Dateien und kontrolliere
die kompilierten Quellen/Logs auf externe Abrufe. Der neutrale Starter verwendet
ausschließlich generisches `serif`/`sans-serif`, die im Test keinen solchen Abruf
auslösten. Telemetrie-Abschaltung allein verhindert Schriftabrufe nicht.


Benötigt: Python ≥3.9, Node.js ≥22 mit npm sowie FFmpeg/ffprobe. Das geprüfte
Demo verwendet HyperFrames 0.8.177 und GSAP 3.15.0 mit einer Paket-Sperrdatei.
Keine pauschale Aktualisierung auf `latest` bei einer laufenden Produktion.

Fehlt FFmpeg auf macOS, kann es nach bewusst gewählter Toolinstallation mit
`brew install ffmpeg` installiert werden. Homebrew verwaltet sein eigenes Prefix;
ein frei gewählter Projektordner ist kein Homebrew-Installationsziel. Andere
Plattformen: passende Paketverwaltung bzw. [offizielle Downloads](https://ffmpeg.org/download.html).
Systeminstallationen werden nicht vom MGD-Installer gestartet.

```bash
python3 skills/mgd-motion-graphics-video/scripts/new_project.py /PFAD/PROJEKT/film --preset reel --end-hold 4
python3 skills/mgd-motion-graphics-video/scripts/setup_tools.py /PFAD/PROJEKT/film
python3 skills/mgd-motion-graphics-video/scripts/setup_tools.py /PFAD/PROJEKT/film --apply
```

Das Toolsetup führt projektlokal `npm ci --ignore-scripts --no-audit --no-fund`
aus. Installation benötigt Netzwerk; Videobilder und Texte bleiben lokal. Ein
kompatibler Chrome/Chromium ist zusätzlich nötig. Zuerst den vorhandenen Browser
verwenden und die aktuelle CLI-Hilfe lesen. Ein erstmaliger Browserdownload ist
als zusätzlicher Werkzeugdownload zu behandeln, kein stiller Fallback.

```bash
cd /PFAD/PROJEKT/film
python3 tools/build.py
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . check
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . snapshot --at 1,4,8,10.5
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py . render --output exports/film-v001.mp4
python3 /PFAD/ZUM/SKILL/scripts/verify_export.py exports/film-v001.mp4 --expected .tmp/expected-export.json --report docs/arbeitsberichte/export-v001.json --evidence .tmp/qc-v001
```

Ersetze `/PFAD/ZUM/SKILL` durch den installierten Skill-Ordner. Für einen
bestehenden Videobaukasten dessen Werkzeugkette respektieren. Manche Werkzeuge
schreiben betriebliche Caches in ihre Standardablagen; das ist keine Garantie
vollständiger Prozess- oder Netzwerkisolation.
