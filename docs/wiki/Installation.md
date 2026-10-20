# Installation für Codex und Claude Code

## Voraussetzungen und Umfang

Der Skill-Installer benötigt Python ab 3.9. Für den lokalen Demo-Baukasten kommen
Node.js ab 22, npm, FFmpeg/ffprobe und ein kompatibler Chrome/Chromium hinzu.
Hauptskill, Aufrufe, Zusatzskills, Videowerkzeuge und externe Plugins sind getrennte
Bestandteile. Vorhandene Werkzeuge zuerst prüfen, statt alles erneut zu installieren.

```bash
git clone https://github.com/MichaelGahnDESIGN/MGD-Motion-Graphics-Video-Skill.git
cd MGD-Motion-Graphics-Video-Skill
python3 skills/mgd-motion-graphics-video/scripts/doctor.py
```

## Codex global einrichten

Eine globale Installation gilt für deinen Benutzer und braucht einen entsprechenden
Auftrag. Die aktuelle offizielle Dokumentation nennt `~/.agents/skills` als
benutzerweiten Ort. Bereits vorhandene ältere Codex-Installationen können andere
Skill-Verzeichnisse verwenden; nicht denselben Skill ungeprüft mehrfach installieren.

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target "$HOME/.agents/skills" --aliases --global
python3 skills/mgd-motion-graphics-video/scripts/install.py --target "$HOME/.agents/skills" --aliases --global --apply
```

Danach `$mgd-motion`, `$mgd-reel` oder eine andere Variante auswählen. Codex kann
neue Skills automatisch erkennen; fehlt der Eintrag, die Sitzung neu öffnen.
Eine installierte Skill-Datei belegt noch nicht, dass der aktuelle Composer schon
neu geladen hat. Alte Custom-Prompt-Dateien sind kein neuer Standard für diese Lösung.

## Projektbezogen installieren

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.agents/skills --aliases --apply
```

Damit werden Hauptskill und Aufrufe ausschließlich in diesem Projekt abgelegt.
Ohne `--aliases` wird nur der Hauptskill installiert. Es gibt keinen automatischen
Download aller optionalen Zusatzskills.

## Claude Code mit den gewünschten Slash-Befehlen

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target "$HOME/.claude/skills" --aliases --commands-target "$HOME/.claude/commands" --global
python3 skills/mgd-motion-graphics-video/scripts/install.py --target "$HOME/.claude/skills" --aliases --commands-target "$HOME/.claude/commands" --global --apply
```

Die beiden Zielordner müssen `skills` und `commands` unter demselben Elternordner
sein. Projektbezogen entsprechend `/PFAD/PROJEKT/.claude/skills` und
`/PFAD/PROJEKT/.claude/commands` verwenden und `--global` weglassen.
Danach stehen beispielsweise `/MGD-Reel` und `/MGD-Video-Optimieren` als
Befehlsdateien bereit. Bei Plugin-Installation kann ein Namensraum vorangestellt
werden; direkte Installation und Plugin-Installation nicht verwechseln.

## ECC und Werkzeuge ergänzen

`--profile core` bietet ausschließlich fest versioniertes ECC video-editing an.
Für FFmpeg und den Remotion-Starter ist kein Zusatzprofil erforderlich. Vor
Auswahl oder Aufruf anderer lokaler Video-Skills ausdrücklich nach Zustimmung
fragen und Skill sowie Zweck nennen. Weitere Profile stehen unter [ECC und Plugins](ECC-und-Plugins.md).
Die Auswahl lädt Fremddateien mit Prüfsummen, führt aber keine Upstream-Installer
aus. Prüfe vorhandene `ecc-*`-Varianten zuerst.

FFmpeg auf macOS lässt sich über `brew install ffmpeg` installieren, wenn eine
Systeminstallation beauftragt ist. Homebrew verwaltet seinen eigenen Installationsort.
Den lokalen Starter erzeugt `new_project.py`; dessen `setup_tools.py --apply`
verwendet die gesperrten npm-Versionen und deaktiviert Paket-Installationsskripte.
Ein erstmaliger Browser- oder Modell-Download ist ein zusätzlicher Werkzeugschritt.

## Konflikte und Kontrolle

Die Vorschau zeigt Konflikte mit dem Hauptskill, seinen Aufrufen und persönlichen
Befehlsdateien bereits unter `conflicts`. Gewählte Fremdskills werden erst bei
`--apply` vollständig anhand ihrer Quellen geprüft.

Der Installer überschreibt keine abweichenden vorhandenen Skills oder Befehle.
Exakt gleiche Dateien werden als vorhanden akzeptiert. Ein Konflikt bricht die
Installation ab; eigene neue Bestandteile werden bei Fehlern zurückgenommen.
Für Updates siehe [Wiederherstellung](Updates-und-Wiederherstellung.md).

Quellen: [Codex-Skills](https://learn.chatgpt.com/docs/build-skills),
[Custom Prompts](https://learn.chatgpt.com/docs/custom-prompts),
[Claude-Code-Skills](https://code.claude.com/docs/en/skills).
