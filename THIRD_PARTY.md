# Drittanbieter und Herkunft

Dieses Repository enthält eigene Anleitungen, Hilfsskripte und einen neutralen
Vektor-Demo. Es bündelt keine privaten Projektmedien und keine heruntergeladenen
Fremdskills oder npm-Pakete. Manifest und Paket-Sperrdatei verweisen auf Quellen.

| Bestandteil | Quelle | Umgang |
|---|---|---|
| Optionale ECC-Skills | [affaan-m/ecc](https://github.com/affaan-m/ecc) | MIT am gepinnten Stand; Original-Lizenz und Herkunft werden beigelegt |
| Remotion, Bundler, Renderer 4.0.537 | [Remotion](https://www.remotion.dev/docs/license) | Projektlokal installiert; aktuelle einsatzabhängige Lizenz prüfen |
| React und React DOM 19.3.1 | [React](https://github.com/facebook/react/blob/main/LICENSE) | MIT; transitive Paketlizenzen separat beachten |
| FFmpeg | [FFmpeg](https://ffmpeg.org/legal.html) | Lizenz hängt vom konkreten Build und eingebundenen Komponenten ab |
| Weitere lokale Skills und Plugins | Jeweilige offizielle Dokumentation | Erst nach ausdrücklicher Auswahl; eigene Bedingungen gelten |

`dependencies.lock.json` hält ECC-Dateihashes und feste Git-Revisionen fest.
Die Paket-Sperrdatei wurde eigenständig aus öffentlichen npm-Quellen erzeugt.
Kein privates Projekt-Lockfile wurde übernommen. Frühere Laufzeitabhängigkeiten
sind im aktuellen Paket nicht enthalten; historische Versionen bleiben Git-Historie.

Bilder, Marken, Stimmen, Musik und Schriften separat auf Nutzungsrechte prüfen.
Ein vorhandener Ordner ist kein Beleg einer kommerziellen Nutzungserlaubnis.
