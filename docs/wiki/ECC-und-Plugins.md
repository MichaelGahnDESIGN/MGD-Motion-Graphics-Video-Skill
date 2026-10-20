# ECC, Zusatzskills und Plugins kombinieren

## Verbindliche Werkzeugwahl

FFmpeg und Remotion sind die vorgesehenen Videowerkzeuge. Andere lokale
Video-Skills vor Auswahl oder Aufruf namentlich vorschlagen und ausdrücklich
nach Zustimmung fragen. Installiert bedeutet nicht freigegeben. Bereits
getroffene passende Entscheidungen übernehmen. Ein Videoauftrag allein ist
keine Erlaubnis, beliebige lokale Zusatzskills oder externe Dienste zu starten.

Der Hauptskill und seine 14 Aufrufvarianten funktionieren ohne Zusatzprofile.
Optionale Profile installieren nur die ausdrücklich ausgewählten ECC-Dateien:

| Profil | Ergänzung | Voraussetzung |
|---|---|---|
| `core` | ECC video-editing | Vorher Skill und Zweck nennen und Zustimmung einholen |
| `ads` | ECC Markenfindung und Markensprache | Ausdrücklich gewählte Ergänzung |
| `remotion` | ECC Remotion | Zusatzskill nur nach Zustimmung verwenden |
| `math` | ECC Manim | Anderes lokales Videowerkzeug, vorher fragen |
| `react-ui` | ECC Motion-Reihe | Passende Webaufgabe; Videoeinsatz vorher klären |
| `cloud-media` | ECC fal.ai, Tasteforge, VideoDB | Anbieter, Upload und Kosten gesondert freigeben |
| `blender` | ECC Blender Motion State Inspection | Anderes lokales Videowerkzeug, vorher fragen |

Profile können kombiniert werden, etwa `--profile core --profile remotion`.
Das frühere `youtube`-Zusatzprofil entfällt; `/MGD-YouTube` bleibt verfügbar.
Die Motion-Reihe betrifft vorwiegend Web-/React-Oberflächen, nicht jede Videotimeline.

## Ein Skill ist kein Connector

Ein Plugin muss verfügbar und gegebenenfalls ein Konto verbunden sein; die
konkrete Funktion muss tatsächlich existieren. Kopierte Skill-Dateien richten
keinen MCP-Server und keine Zugangsdaten ein. Keine kontoabhängigen Plugin-IDs
als allgemeingültigen Installationsweg veröffentlichen.

Higgsfield oder fal.ai können nach gesonderter Wahl Medienbausteine liefern.
Adobe, Canva oder Figma erschließen Designs, Voice-Anbieter vertonen Texte.
Vorher Datenübertragung, Kosten, Rechte und Exportqualität klären. Der lokale
Schnitt bleibt im Projekt; keine stillen Anbieterwechsel.

Upstream-Dateien unverändert zu installieren belegt keine Kompatibilität aller
Claude-Funktionen mit Codex. Toolnamen, Plattform und aktuelle Dokumentation prüfen;
Benutzer- und Projektregeln bleiben maßgeblich.
