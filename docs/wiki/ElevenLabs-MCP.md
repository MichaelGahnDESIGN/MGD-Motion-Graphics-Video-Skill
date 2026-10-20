# ElevenLabs-MCP: natürliche Sprecherstimmen

ElevenLabs ist eine optionale Ergänzung für Sprecherfassungen. Du kannst zum
Beispiel eine natürliche männliche deutsche Stimme für ein Erklär-Reel wählen.
Musik, Schnitt und Schlusskarte werden anschließend mit FFmpeg oder Remotion
zusammengeführt. Das Video muss dafür nicht beim Sprachdienst hochgeladen werden.

## Einmal verbinden

Beauftrage die Verbindung ausdrücklich, wenn Codex dafür seine globale
Konfiguration ändern soll. Der aktuelle offizielle Server nutzt OAuth: Du meldest
dich im Browser bei ElevenLabs an und prüfst die angefragten Berechtigungen.
Ein API-Schlüssel im Chat oder im Video-Projekt ist dafür nicht nötig.

```bash
codex mcp add elevenlabs --url https://api.elevenlabs.io/v1/mcp
codex mcp login elevenlabs
```

Am 20.10.2026 gab es beim Standard-Endpunkt einen OAuth-Adresskonflikt. Die vom
offiziellen Dienst ausgewiesene kanonische Adresse
`https://api.us.elevenlabs.io/v1/mcp` funktionierte. Vor Anwendung dieses datierten
Hinweises die aktuellen Metadaten prüfen; keine Sicherheitsprüfung abschalten.
Die ausführliche [Einrichtungsanleitung](../../skills/mgd-motion-graphics-video/references/elevenlabs-mcp.md)
erklärt den Fehler und die getrennten Residency-Workspaces.

Eine erfolgreiche Anmeldung ist erst der Anfang: Der Assistent prüft die
verfügbaren Werkzeuge und den Zugriff. Je nach Client muss die Verbindung
neu geladen oder eine neue Sitzung geöffnet werden.

## Beispielauftrag

> Erstelle eine zusätzliche Sprecherfassung meines vorhandenen Reels mit einer
> natürlichen männlichen deutschen ElevenLabs-Bibliotheksstimme. Ruhig, freundlich
> und verständlich. Nutze das vorhandene freigegebene Kontingent und prüfe die
> Credit-Kosten vorab. Erzeuge eine einzige Version. Musik leiser; die vollständig
> lesbare Schlusskarte fünf Sekunden stehen lassen. Originalfassung erhalten.

Der Assistent sucht eine verfügbare passende Stimme, erzeugt die freigegebene
Fassung genau einmal und prüft ihren Status. Wiederholtes Starten erzeugt weitere
kostenpflichtige Fassungen; eine laufende Generierung wird deshalb nur abgefragt.
Stimme, Modell, Text und Herkunft bleiben in der jeweiligen Produktion nachvollziehbar.

## Rechte, Kosten und Abnahme

Ein bezahlter Tarif und die geltenden Bedingungen entscheiden über kommerzielle
Verwendung. Alte Screenshots nicht als aktuellen Kontostand behandeln. Keine
Stimme von Simon, Michael oder anderen Personen ohne gesonderte Freigabe klonen.
Anmeldung und Lizenz sind keine pauschale Freigabe für beliebige Käufe oder Uploads.

Nach der Erzeugung werden Aussprache, Pausen, Musikbalance und der tatsächlich
codierte Ton kontrolliert. Credit-Schätzung und echte Abrechnung unterscheiden;
keine erfundenen Token-/Eurokosten nennen. Die fertige Datei erhält eine neue
Version. Nichts wird allein durch die MCP-Verbindung veröffentlicht.

[Audio und Untertitel](Audio-und-Untertitel.md) ·
[Kosten und Datenschutz](Kosten-und-Datenschutz.md) ·
[Offizielle ElevenLabs-Dokumentation](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)
