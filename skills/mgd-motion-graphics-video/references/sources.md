# Quellen und gepflegte Versionsstände

Stand der Quellenprüfung: 20.10.2026. Der Skill bündelt eigene Anweisungen;
Fremdskills werden nur auf ausdrückliche Auswahl installiert.

- [HyperFrames und Skill-Aufbau](https://github.com/heygen-com/hyperframes):
  Revision `7d47194e4a078b4382bf3e8597ca9520e278781c` für Zusatzskills.
- [Everything Claude Code / ECC](https://github.com/affaan-m/ecc): Revision
  `6c557856af89a657f846a8ca15907cbdc1e41530` für Zusatzskills.
- [HyperFrames Skill-Anleitung](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/skills.mdx):
  Upstream-Aktualisierungsbefehle können global wirken; keine automatische
  Aktualisierung in dieser Installation.
- [FFmpeg-Dokumentation](https://ffmpeg.org/documentation.html) und
  [Homebrew-Formel](https://formulae.brew.sh/formula/ffmpeg).
- [Remotion-Dokumentation](https://www.remotion.dev/docs/) und
  [Lizenzbedingungen](https://www.remotion.dev/docs/license).
- [GSAP-Dokumentation](https://gsap.com/docs/v3/).
- Vorbild für die menschliche Dokumentation:
  [ChatGPT Video Composer Skill](https://github.com/MichaelGahnDESIGN/ChatGPT-Video-Composer-Skill).

Demo-Laufzeit: HyperFrames **0.8.177**, GSAP **3.15.0**. Zusatzskill-Revisionen und
CLI-Version sind getrennte Komponenten; eine passende Dokumentation beweist
keine Unterstützung jeder neuesten CLI-Option durch die gepinnte Version.
Prüfe bei Änderungen die lokale `--help` und führe einen echten Testexport aus.

`dependencies.lock.json` enthält Quellen, Profile, Dateigrößen und SHA-256.
`tools/update_dependency_lock.py` ist ein Maintainer-Werkzeug: Revision bewusst
setzen, Änderungen prüfen, Tests und Beispielrender ausführen. Es wird nicht
bei jeder Installation gestartet. Normale Nutzer brauchen dafür weder `gh`
noch ein GitHub-Token; öffentliche Dateien werden über HTTPS geladen.
