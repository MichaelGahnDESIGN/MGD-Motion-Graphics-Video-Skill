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
