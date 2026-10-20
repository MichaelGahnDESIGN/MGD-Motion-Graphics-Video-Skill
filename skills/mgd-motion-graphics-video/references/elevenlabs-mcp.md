# ElevenLabs über MCP für Sprecherfassungen

Stand: 20.10.2026. Optionaler Cloud-Anbieter für künstliche Sprecherstimmen;
FFmpeg und Remotion bleiben die Videowerkzeuge. Lies diese Anleitung, wenn der
Nutzer ElevenLabs auswählt oder eine bestehende Verbindung verwenden möchte.

## Verbindung einrichten

Prüfe zuerst die verfügbaren Werkzeuge und vorhandenen MCP-Einträge. Eine
Skill-Installation stellt keine Kontoverbindung her. Globale MCP-Konfiguration
nur mit entsprechendem Auftrag ändern, vorhandene andere Server erhalten.

Der offizielle gehostete MCP verwendet OAuth. Ein API-Schlüssel muss dafür nicht
in Chat, Projektdateien oder Beispielkonfigurationen kopiert werden. In Codex:

```bash
codex mcp add elevenlabs --url https://api.elevenlabs.io/v1/mcp
codex mcp login elevenlabs
```

Der Nutzer meldet sich bei ElevenLabs an und prüft die angefragten Berechtigungen.
OAuth-Tokens bleiben im vorgesehenen Anmeldespeicher des Clients. Keine Tokens
für eigene Skripte exportieren und keine Login-Links mit temporären Parametern
in Berichten veröffentlichen. Nur benötigte Werkzeuge nutzen; die Verbindung
kann auch Agenten verwalten und Änderungen unmittelbar veröffentlichen.

### Bekannter OAuth-Adresskonflikt

Am 20.10.2026 meldete der öffentliche Standard-Endpunkt als geschützte Ressource
`https://api.us.elevenlabs.io/v1/mcp`. Codex lehnte deshalb den Login mit
`Protected resource metadata resource mismatch` ab. In diesem konkreten Fall
funktionierte die vom offiziellen Server selbst ausgewiesene Adresse:

```bash
codex mcp add elevenlabs --url https://api.us.elevenlabs.io/v1/mcp
codex mcp login elevenlabs
```

Das ist ein datierter Befund, kein pauschaler Ersatz für künftige Installationen.
Vor einer Korrektur aktuelle öffentliche OAuth-Metadaten prüfen; keine Prüfungen
abschalten und keine beliebigen fremden Ziele übernehmen. EU-/andere Residency-
Adressen gehören zu getrennten isolierten Workspaces. Eine andere URL macht ein
normales Konto nicht zu einem EU-Workspace.

Nach erfolgreichem Login Werkzeugliste und lesenden Zugriff tatsächlich prüfen.
Ein gespeicherter Eintrag allein belegt keine funktionierende Spracherzeugung.
Je nach Client ist ein Neuladen oder eine neue Sitzung nötig. Keine Zugangsdaten
als Ersatz aus Browser-Sitzungen oder dem Systemschlüsselbund auslesen.

## Stimme und einzelne Fassung erzeugen

1. Sprechertext, Sprache, gewünschtes Geschlecht, Ton und Filmzeiten aus dem
   Auftrag übernehmen. Bei vorhandener Freigabe keine erneuten Pflichtinterviews.
2. `creative_list_voices` verwenden, etwa mit `languages: ["de"]` und
   `gender: "male"`. Voice-ID aus dem tatsächlichen Ergebnis wählen, nicht aus
   Erinnerung. Natürlicher Akzent, Aussprache und Erklärstil gehen vor Werbedruck.
3. Aktuellen Tarif, kommerzielle Nutzungsrechte und verfügbares Kontingent prüfen.
   Ein alter Free-Screenshot widerlegt keinen später belegten bezahlten Tarif.
   Ein verbundenes Konto ist umgekehrt kein pauschaler Lizenznachweis.
4. `creative_generate_speech` zunächst mit `estimate_only: true` aufrufen.
   Für eine ausdrücklich einzelne Version `generations_count: 1` setzen;
   sonst können mehrere Varianten und entsprechende Kosten entstehen.
   Kostenrahmen/Freigabe aus dem laufenden Auftrag beachten, keine Zusatzpakete kaufen.
5. Eine Generierung starten und die zurückgegebenen Flow-/Session-IDs festhalten.
   Bei Verzögerungen `creative_get_flow_run_status` abfragen. Den Startaufruf
   niemals blind wiederholen: ein weiterer Start kann erneut Credits verbrauchen.
6. Fertige Audiodatei zeitnah in der zugehörigen Produktion speichern und
   SHA-256, Anbieter, Stimme, Modell, Text und tatsächlich belegte Kosten festhalten.
   Signierte kurzlebige Download-URLs nicht in öffentlichen Dateien speichern.

Die Werkzeugnamen beschreiben den geprüften aktuellen MCP. Bei Abweichungen
zuerst die tatsächlichen Tool-Schemas lesen. Keine Werkzeuge erfinden. Normale
Bibliotheksstimmen sind keine Nachahmung des Unternehmers; kein Stimmenklonen
oder Identitätsversprechen aus einem allgemeinen Sprecherauftrag ableiten.

## In das Video einbauen und prüfen

Originalaudio und bisherigen Export erhalten, Sprecherfassung neu versionieren.
Abschnitte an die Szenen anpassen, natürliche Pausen und Namen kontrollieren.
Musik unter der Stimme absenken, Ein-/Ausblenden bewahren und die gewünschte
Schluss-Haltezeit vom vollständig lesbaren Bild an messen. Bei reiner
Tonänderung die vorhandene Videospur mit FFmpeg möglichst ohne neues Encoding
übernehmen (`-c:v copy`). Keine künstliche Tonhöhenänderung als Ersatz für eine
passende männliche Stimme.

Den fertigen AAC-Ton im MP4 auf Lautheit, True Peak, Verständlichkeit und
Synchronität prüfen. Rechenprüfung, menschliche Hörabnahme und Veröffentlichung
getrennt benennen. Cloud-Credits, Abonnement und lokale Renderkosten nicht mit
exakten LLM-Tokenkosten gleichsetzen; nur tatsächlich belegte Werte angeben.

## Offizielle Quellen

- [Gehosteter MCP, OAuth und Berechtigungen](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)
- [ElevenLabs MCP](https://elevenlabs.io/mcp)
- [Kommerzielle Verwendung generierter Inhalte](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform)
