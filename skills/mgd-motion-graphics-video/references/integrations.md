# ECC und Medien-Plugins

## Lokale Zusatzskills

FFmpeg und Remotion sind die vorgesehenen Videowerkzeuge. Zusätzliche lokale
Video-Skills **vor Auswahl oder Aufruf namentlich vorschlagen und ausdrücklich
nach Zustimmung fragen**. Das gilt auch für bereits installierte ECC-Varianten.
Installation oder Verfügbarkeit allein ist keine Nutzungsfreigabe.

Nach Zustimmung können `video-editing`/`ecc-video-editing` FFmpeg-Wissen und
`remotion-video-creation` Remotion-Wissen ergänzen. Die Motion-Reihe behandelt
vorwiegend Web-/React-UI. Manim oder Blender sind andere lokale Produktionswege
und benötigen ebenfalls vorherige Zustimmung; sie werden nie automatisch gewählt.

Der Installer belässt Upstream-Dateien unverändert und ergänzt Herkunft/Lizenz.
Damit wird keine Kompatibilität jedes enthaltenen Befehls versprochen. Prüfe
Toolnamen, Verfügbarkeit, Plattform, aktuelle Dokumentation und Auftragsumfang.
Claude-spezifische Hooks, Agentenvorgaben oder globale Installationsschritte
werden nicht ungeprüft auf Codex übertragen. Höherrangige Anweisungen und die
aktuelle Benutzerfreigabe entscheiden, welche Aktionen möglich sind.

## Optionale Plugins und externe Dienste

| Fähigkeit | Mögliche Ergänzung | Vor Verwendung prüfen |
|---|---|---|
| Generierte Bild-/Videobausteine | Higgsfield, fal.ai oder passender Bildgenerator | Modell, Referenzupload, Credits, Nutzungsrechte |
| Vorhandene Designs und CI | Figma, Adobe, Canva | Dateizugriff, Exportqualität, lokale Ableitung |
| Sprache | Verbundener Voice-Anbieter | Stimme/Rechte, Text, Kosten und Datenübertragung |
| Medienindex oder Cloudschnitt | VideoDB oder passende Plattform | Welche Originale hochgeladen werden, Speicherung, Kosten |

Wenn Plugin-Verwaltung vorhanden ist, Fähigkeiten zunächst gezielt suchen und
prüfen, ob Plugin **installiert**, Konto **verbunden** und Funktion tatsächlich
**verfügbar** ist. Das sind drei verschiedene Zustände. Keine accountabhängigen
Plugin-IDs als universelle Installationsanweisung fest einbauen. Fehlt der
Connector, einen lokalen Weg nutzen oder die konkrete nötige Verbindung erklären.
Ein MCP-Server wird nicht durch bloßes Kopieren eines Skills eingerichtet.

Externe Generatoren liefern Bausteine; Schnitt, Branding und Abnahme verbleiben
im Projekt. Private Quellen nicht allein zur Stilfindung hochladen. API-Schlüssel
nur über geeignete Secret-Verwaltung, nie in Beispielskripten oder Git. Keine
externen Kosten, Authentifizierung oder Veröffentlichung als stiller Fallback.
Die aktuelle Remotion-Lizenz hängt vom Einsatz ab; Bedingungen vor dem Einsatz
prüfen, nicht pauschal kostenlose kommerzielle Nutzung zusagen.

Bei Figuren zuerst den [Charakter- und LoRA-Ablauf](characters-lora.md) durchführen.
Bildreferenzen, proprietäre Charakterdienste und echte trainierte Adapter nicht
gleichsetzen. Imagegen-Aufruf aus einer lokalen App ist keine Offline-Bildgenerierung.

## Audio prüfen mit earshot (optional)

[earshot](https://github.com/Leonxlnx/earshot) analysiert Ton lokal auf der CPU:
beschreiben, vergleichen, eine Film-Timeline mit Sync zu den Schnitten erstellen,
Kritik gegen professionelle Launchfilme üben und eine Soundbank bzw. Kits ordnen.
Das Audio bleibt auf dem Rechner. Einzige Ausnahme ist der optionale Befehl
`earshot llm`: Er lädt Audio zu Google Gemini hoch, braucht einen eigenen
API-Schlüssel und läuft nur nach ausdrücklicher Zustimmung zu diesem Upload.

- **Auswahl:** Die Profile `audio` (Skill `earshot`) und `real-sound` (zusätzlich
  Skill `real-sound`) nur nach ausdrücklicher Zustimmung wählen; vorher Skill und
  Zweck nennen, wie bei anderen Zusatzskills. Installation allein ist keine Freigabe.
- **Was der Installer tut:** Er legt ausschließlich die Skill-Texte an, geprüft
  gegen feste Revision und SHA-256, samt Upstream-Lizenz und Herkunft. Er führt
  nichts aus.
- **Python-Paket:** Das Paket `earshot` (torch, transformers, Modelle von Hugging
  Face beim ersten Aufruf, mehrere hundert MB bis GB, Netz nötig) wird nicht
  gebündelt und nur nach gesonderter Freigabe installiert, nie still. Der Befehl
  steht in [installation.md](installation.md).
- **Globale Konfiguration:** `claude mcp add --scope user` aus dem earshot-Skill
  ändert die globale Agent-Konfiguration und braucht einen eigenen Benutzerauftrag.
- **Grenze:** earshot misst, es hört keinen Geschmack. Es ersetzt keine
  Hörkontrolle durch Menschen; der earshot-Skill nennt das selbst unter „Limits“.
- **real-sound:** Ein eigener, aufwendiger Mehr-Agenten-Ablauf für Tonspuren aus
  echten lizenzierten Aufnahmen (Freesound, Mixkit, Bibliotheken, mit
  Lizenzprüfung). Nur bei ausdrücklichem Wunsch verwenden. Lizenzen und Herkunft
  der dabei gesuchten Tonquellen sind getrennt zu prüfen.
