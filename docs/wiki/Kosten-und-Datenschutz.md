# Kosten, Datenübertragung und vertrauliche Inhalte

## Welche Kosten entstehen können

Der Skill ist ein Anweisungspaket. Lokales Rendern braucht Rechenleistung und
Speicher, startet aber nicht automatisch einen kostenpflichtigen Medien-API-Aufruf.
Agentenabonnement, Strom, Softwarelizenzen, Musikrechte und optionale Generatoren
sind verschiedene Kostenarten. Eine pauschale Zusage „alles kostenlos“ wäre falsch.

Vor externer Generierung Anbieter, Modell, Anzahl, mögliche Credits und erlaubte
Referenzen festhalten. Ein Konto mit Guthaben ist kein Freibrief für beliebige
Jobs. Aktuelle Lizenzbedingungen separat prüfen, etwa bei Remotion. Eine unklare
Kostenanzeige nicht als null Euro interpretieren.

## Private Quellen lokal halten

Manuskripte, interne Produktangaben, unveröffentlichte Figuren, Gesichter und
Stimmvorlagen nur entsprechend dem Auftrag verarbeiten. Ein Stilwunsch allein
berechtigt nicht zu einem Referenzupload. Secrets gehören in geeignete lokale
Verwaltung und niemals in Git, Beispielkonfigurationen, Clientcode oder Berichte.

## Unerwartete Schriftabrufe

Die getestete HyperFrames-Version kann bestimmte benannte Systemschriften durch
Webfonts ersetzen und dazu aus dem Dokument gewonnene Schriftzeichen übertragen.
Vor Browserchecks vertraulicher Texte lokale lizenzierte `@font-face`-Dateien
bereitstellen und kompilierte Quellen beziehungsweise Logs prüfen. Der neutrale
Starter verwendet generisches `serif`/`sans-serif`, das im dokumentierten Test
keinen solchen Abruf auslöste. Abgeschaltete Telemetrie allein verhindert nicht
jeden Netzwerkzugriff eines Werkzeugs.

## Veröffentlichung ist ein eigener Auftrag

Ein exportiertes Video ist noch kein veröffentlichter Beitrag. Plattformkonto,
Begleittext, Rechte, Ziel und Zeitpunkt vor einem Upload beachten. Private
Rohquellen oder sensible Testlogs nicht automatisch zusammen mit einem Skill
oder einer Release-Datei veröffentlichen.

## Cloud, lokale Bilder und Assistentenkontext unterscheiden

OpenAI-/ChatGPT-Imagegen ist ein Cloud-Bilddienst, auch wenn der Aufruf in einer
lokalen App erfolgt. Beim Cloud-Assistenten können bereits gelesene Projekttexte
und betrachtete Referenzbilder Teil der Serververarbeitung sein. Lokales FFmpeg-
Rendern ist davon getrennt. Ein Speicherort auf dem NAS garantiert keine Offline-
Verarbeitung. Den Datenfluss vor neuen Generierungs-/Trainingsjobs offenlegen.

Bei Figuren den [Charakter-Workflow](Charaktere-und-LoRA.md) verwenden. Bildanbieter
und LoRA-Trainer können verschieden sein; die Freigabe für einen Dienst gilt
nicht automatisch für den anderen. Gewichte, Trainingsbilder und private Sheets
werden nicht zusammen mit dem öffentlichen Skill veröffentlicht.

## Tokenzahlen und Geldbeträge nicht verwechseln

Wenn ein Benutzer nach Kosten fragt, den konkreten Auftrag zeitlich abgrenzen
und verfügbare Sitzungszähler davor/danach vergleichen. Eingabetokens, darin
enthaltene Cache-Tokens und Ausgabetokens getrennt berichten; Cache nicht nochmals
zum Input addieren, Reasoning nicht doppelt zum Output zählen. Wiederholt
mitgesendeter Gesprächskontext erklärt große kumulierte Tokenzahlen. Bei
Kontextkürzungen und Resets die Konsistenz der Zähler prüfen und Grenzen nennen.
Keine Tokenzahl aus Dateigröße oder sichtbarer Antwortlänge erfinden.

Eine API-Vergleichsrechnung anhand aktueller offizieller Modellpreise ist keine
Abo-Rechnung. Cachetarife, Kontextlängenstaffeln und gegebenenfalls Dienststufen
beachten. Bild-/Video-/Sprachgenerierung kann zusätzlich berechnet werden und
ist ohne gemeldete Nutzungs-/Preisdaten nicht exakt zurechenbar. Abo-Kontingente,
Zusatzcredits, tatsächlich abgebuchte Beträge, Strom und Renderzeit getrennt
benennen; unbekannte Werte nicht als null Euro ausgeben. Vorher genehmigte
Budgets gelten weiter, solange der konkrete Job abgedeckt ist.
