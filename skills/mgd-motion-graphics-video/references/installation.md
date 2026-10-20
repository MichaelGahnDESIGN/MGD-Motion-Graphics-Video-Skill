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

| Profil | Ergänzung | Voraussetzung |
|---|---|---|
| `core` | ECC video-editing | Vorher Skill und Zweck nennen und Zustimmung einholen |
| `ads` | ECC Markenfindung und Markensprache | Ausdrücklich gewählte Ergänzung |
| `remotion` | ECC Remotion | Zusatzskill nur nach Zustimmung verwenden |
| `math` | ECC Manim | Anderes lokales Videowerkzeug, vorher fragen |
| `react-ui` | ECC Motion-Reihe | Passende Webaufgabe; Videoeinsatz vorher klären |
| `cloud-media` | ECC fal.ai, Tasteforge, VideoDB | Anbieter, Upload und Kosten gesondert freigeben |
| `blender` | ECC Blender Motion State Inspection | Anderes lokales Videowerkzeug, vorher fragen |

Profile können wiederholt werden, z. B. `--profile core --profile remotion`.
Kein Zusatzprofil ist für FFmpeg oder den Remotion-Starter erforderlich.
Das frühere `youtube`-Zusatzprofil wurde entfernt; die MGD-YouTube-Aufrufe bleiben.
Jede Fremddatei wird an einer festen ECC-Git-Revision und SHA-256 geprüft.
Der Installer führt keine Upstream-Skripte aus und legt `MGD-SOURCE.json` sowie
`LICENSE.upstream` (ECC: MIT) bei. Installation allein autorisiert keine Nutzung.

Eine **globale** Installation braucht einen entsprechenden Benutzerauftrag.
Erst dann beispielsweise `--target "$HOME/.agents/skills" --global --apply`
verwenden. Projektinstallation ist der Standard. Der Skill selbst ändert keine
Agent-Konfiguration, aktiviert keine Hooks und installiert keine Plugins.

## Lokale Videowerkzeuge

Vorgesehen sind **FFmpeg und Remotion**. Weitere lokale Video-Skills vor Auswahl
oder Aufruf namentlich vorschlagen und ausdrücklich nach Zustimmung fragen.
Bereits erteilte passende Zustimmung übernehmen; installierte Pakete sind keine
pauschale Freigabe. Bestehende Quellen und Projekte bewahren.

Der Remotion-Starter benötigt Python ≥3.9, Node.js ≥22 mit npm und vorhandenes
Chrome/Chromium. FFmpeg/ffprobe dienen zusätzlichem Schnitt und der Exportprüfung.
Remotion, Bundler und Renderer sind auf **4.0.537**, React/React DOM auf **19.3.1**
gesperrt. Die aktuelle Remotion-Lizenz vor kommerziellem Einsatz prüfen.
Schriften und Medien lokal laden; keine Webfont-/CDN-Imports im Starter.

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

Ersetze `/PFAD/ZUM/SKILL` durch den installierten Skill-Ordner. Mit `--browser /PFAD/ZUM/CHROME` oder `MGD_BROWSER` einen vorhandenen Browser
angeben, falls er nicht erkannt wird. Ein fehlender Browser führt zum Abbruch,
nicht zu einem automatischen Download. Bei alten Projekten eine Ableitung mit
FFmpeg oder Remotion vorbereiten; andere lokale Video-Skills vorher abfragen. Manche Werkzeuge
schreiben betriebliche Caches in ihre Standardablagen; das ist keine Garantie
vollständiger Prozess- oder Netzwerkisolation.

## Alle spezialisierten Aufrufe installieren

Zusätzlich `--aliases` verwenden. Der Hauptskill erzeugt die 14 Varianten aus
seinem mitgelieferten Katalog; ein separates Repository ist dafür nicht nötig.
Codex verwendet beispielsweise `$mgd-reel` und `$mgd-video-optimieren`.

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.agents/skills --aliases --apply
```

Für eine beauftragte globale Codex-Installation ist der aktuelle benutzerweite
Ort `"$HOME/.agents/skills"`, kombiniert mit `--global`. Ältere vorhandene
Codex-Skill-Ablagen nicht ungeprüft doppeln.

Claude Code kann zusätzlich die gewünschten Slash-Befehle erhalten:

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.claude/skills --aliases --commands-target /PFAD/PROJEKT/.claude/commands --apply
```

Bei globaler Claude-Einrichtung beide Ordner unter `$HOME/.claude` wählen und
`--global` ergänzen. Auch Befehlsdateien werden bei Abweichungen nicht überschrieben.
Eine Installation startet noch keinen Film. Fehlenden Ordner und erstes Thema
beim Einstieg erfragen; bestehende Projekte gezielt fortsetzen.
