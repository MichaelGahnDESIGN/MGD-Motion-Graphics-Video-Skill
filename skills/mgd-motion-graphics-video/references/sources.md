# Quellen und gepflegte Versionsstände

Stand: 20.10.2026. Vorgesehen sind FFmpeg und Remotion. Weitere lokale Video-Skills
nur nach vorheriger Zustimmung auswählen oder aufrufen.

- [Everything Claude Code / ECC](https://github.com/affaan-m/ecc): Revision
  `6c557856af89a657f846a8ca15907cbdc1e41530` für optionale Zusatzskills.
- [FFmpeg-Dokumentation](https://ffmpeg.org/documentation.html) und
  [Homebrew-Formel](https://formulae.brew.sh/formula/ffmpeg).
- [Remotion-Dokumentation](https://www.remotion.dev/docs/) und
  [Lizenzbedingungen](https://www.remotion.dev/docs/license).
- [Remotion renderMedia](https://www.remotion.dev/docs/renderer/render-media).
- Dokumentationsvorbild:
  [ChatGPT Video Composer Skill](https://github.com/MichaelGahnDESIGN/ChatGPT-Video-Composer-Skill).

Starter: Remotion, Bundler und Renderer **4.0.537**, React/React DOM **19.3.1**.
Die Sperrdatei hält auch transitive Paketversionen und Integritätswerte fest.
Keine automatische Aktualisierung während einer laufenden Produktion.

`dependencies.lock.json` enthält ECC-Quellen, Profile, Dateigrößen und SHA-256.
`tools/update_dependency_lock.py` ist ein bewusst auszuführendes Maintainer-Tool:
Änderungen prüfen, Tests und Beispielrender ausführen. Es wird nicht bei jeder
Installation gestartet. Normale Nutzer brauchen weder `gh` noch GitHub-Token.
