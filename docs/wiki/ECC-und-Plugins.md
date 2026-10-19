# ECC, Zusatzskills und Plugins kombinieren

## Nach tatsächlichem Bedarf auswählen

Der Hauptskill koordiniert; Zusatzskills liefern spezifisches Wissen. Die
Installation unterstützt folgende Profile:

| Profil | Inhalt | Typischer Einsatz |
|---|---|---|
| `core` | HyperFrames-Basis und ECC video-editing | Lokale Schnitt-/Motion-Pipeline |
| `youtube` | Erklärvideo, Untertitel und Talking-Head-Workflows | Redaktionelle Videos |
| `ads` | Produktvideo, Markenfindung und Markensprache | Werbe- und Produktfilme |
| `remotion` | ECC Remotion | Bewusst gewählte React-Videoprojekte |
| `math` | ECC Manim | Mathematische Erklärungen |
| `react-ui` | ECC Motion-Reihe | Weboberflächen und passende React-Aufgaben |
| `cloud-media` | fal.ai, Tasteforge und VideoDB | Gewählte externe Medienverarbeitung |
| `blender` | Blender-Motion-State-Inspection | Bestehende Blender-Szenen |

Profile lassen sich wiederholen: `--profile core --profile youtube`. Bereits
vorhandene `ecc-*`-Varianten können verwendet werden. Installiere nicht vorsorglich
alle Profile, nur weil ein neues Video entsteht. Die Motion-Reihe behandelt
vorwiegend Web-/React-UI und schreibt einem GSAP-Projekt nicht `motion/react` vor.

## Ein Skill ist kein Connector

Ein Plugin muss verfügbar sein, gegebenenfalls ein Konto verbunden werden und
die konkrete Funktion tatsächlich zugänglich sein. Ein kopierter Skill stellt
keinen MCP-Server und keine Zugangsdaten bereit. Nutze die in der Umgebung
vorhandene Plugin-Suche und die jeweiligen Einrichtungsanweisungen. Keine
kontoabhängigen Plugin-IDs als allgemeingültigen Installationsweg veröffentlichen.

Higgsfield oder fal.ai können gewählte Medienbausteine liefern. Adobe, Canva oder
Figma können vorhandene Designs erschließen. Ein Voice-Anbieter kann freigegebenen
Sprechtext vertonen. Vor der Verwendung Datenübertragung, Kosten, Rechte und
Exportqualität prüfen. Der lokale Schnitt bleibt die gemeinsame Projektgrundlage.

Upstream-Skills unverändert zu installieren bedeutet nicht, dass jede darin
beschriebene Claude-Funktion in Codex vorhanden ist. Toolnamen und Befehle prüfen;
höherrangige Benutzer- und Projektregeln bleiben maßgeblich.
