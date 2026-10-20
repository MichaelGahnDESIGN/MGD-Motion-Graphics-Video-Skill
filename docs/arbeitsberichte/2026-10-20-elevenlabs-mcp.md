# ElevenLabs-MCP im Video-Skill

## Änderung

Optionale ElevenLabs-Sprecherfassungen werden aus dem Skill, der README und
dem Handbuch erschlossen. Eine eigene Referenz erklärt OAuth, die tatsächliche
Stimmenwahl, Schätzung und einmaligen Start, Statusabfrage, Lizenzprüfung und
FFmpeg-Mischung. Die neue Wiki-Seite ist in Home, Seitenleiste und Audio-Kapitel
verlinkt. Kein automatischer Installer und keine Zugangsdaten im Paket.

## Verifikation

`python3 tools/check.py`: 40 Tests bestanden; 58 Katalogdateien geprüft.
Lokale Markdown-Verweise gültig, Python-/JSON-Prüfung erfolgreich. Die Prüfung
lief in einer mit dem vorgeschriebenen Helfer angelegten lokalen NAS-Arbeitskopie.
Auf dem NAS selbst scheiterte zuvor genau der Wiederholungs-Installationstest
an `FileExistsError` beim Umlaut-Dateinamen des Erklärvideo-Befehls. Die identischen
Quellen bestehen lokal. Kein Installer- oder Laufzeitcode wurde geändert.

## Verbindung und Grenzen

Der offizielle Server wurde am 20.10.2026 per OAuth verbunden. Bei der
Standard-URL trat ein Ressourcen-Metadatenkonflikt auf; der vom offiziellen
Dienst ausgewiesene kanonische US-Endpunkt funktionierte. Die Dokumentation
kennzeichnet das als datierten Befund. Stimmenliste, eine einzelne Spracherzeugung
und Statusabfragen wurden tatsächlich geprüft. Private Texte, Kontodaten,
Voice-IDs, Generationen und Projektmedien wurden nicht in dieses öffentliche
Repository übernommen. Ein neuer Video-Render war für diese Dokumentationsänderung
nicht erforderlich. Keine Veröffentlichung eines Kundenfilms.

Die GitHub-Wiki-Veröffentlichung erfolgt mit dem vorhandenen Sync-Helfer und
seinem Konfliktschutz. Normales Git stellt den vorherigen Stand wieder her;
OAuth kann unabhängig im Client/Konto widerrufen werden. Kein neuer Release
und keine globale Skill-Neuinstallation in diesem Auftrag.
