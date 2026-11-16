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
| `audio` | earshot-Skill (Audioanalyse) | Skill und Zweck nennen, Zustimmung einholen; Python-Paket separat |
| `real-sound` | earshot-Skill und real-sound-Skill | Skill und Zweck nennen, Zustimmung einholen; Python-Paket separat |

Profile können kombiniert werden, etwa `--profile core --profile remotion`.
Das frühere `youtube`-Zusatzprofil entfällt; `/MGD-YouTube` bleibt verfügbar.
Die Motion-Reihe betrifft vorwiegend Web-/React-Oberflächen, nicht jede Videotimeline.

## Audio prüfen mit earshot (optional)

earshot analysiert Ton lokal auf der CPU (beschreiben, vergleichen, Timeline und
Sync zu Schnitten, Kritik gegen Profi-Launchfilme, Soundbank). Das Audio bleibt
lokal; nur der optionale Befehl `earshot llm` lädt nach ausdrücklicher Zustimmung
Audio zu Google Gemini hoch und braucht einen eigenen API-Schlüssel. Das
Python-Paket (torch, Modelle) wird nur nach gesonderter Freigabe installiert,
nie still. `claude mcp add --scope user` ist eine globale Konfigurationsänderung
und braucht einen eigenen Benutzerauftrag. earshot misst, es hört keinen
Geschmack: Die Hörkontrolle durch Menschen bleibt nötig. `real-sound` ist ein
eigener, aufwendiger Mehr-Agenten-Ablauf für Tonspuren aus echten lizenzierten
Aufnahmen; nur bei ausdrücklichem Wunsch, Lizenzen der Tonquellen getrennt prüfen.

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
