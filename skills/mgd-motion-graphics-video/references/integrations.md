# ECC und Medien-Plugins

## Lokale Zusatzskills

Nutze `video-editing` bzw. eine vorhandene `ecc-video-editing`-Variante für Schnitt
und FFmpeg-Details. Für HyperFrames die Basis und nur den passenden Workflow laden.
`remotion-video-creation` ist für gewählte Remotion-Projekte; die Motion-Reihe
`motion-foundations`, `motion-patterns`, `motion-advanced` ist primär Web-/React-UI.
Keine React-Abhängigkeiten in ein GSAP-Projekt hineininstallieren, nur weil „Motion“
im Namen steht. Für Mathematik kann `manim-video`, für echte Blender-Arbeit
`blender-motion-state-inspection` passen.

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
