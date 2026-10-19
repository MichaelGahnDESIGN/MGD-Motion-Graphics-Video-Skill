# NAS, SSD-Arbeit und geprüfter Rücktransfer

NAS-Systeme eignen sich für Quellen und Archivierung. npm-Abhängigkeiten,
Browserprofile, Hardlinks und sehr viele kleine Dateien können dort langsam sein
oder fehlschlagen. Stelle deshalb zuerst die echte Projektwurzel fest und nutze
für rechenintensive Arbeit bei Bedarf eine ausdrücklich erlaubte lokale Kopie.

## Nur das benötigte Projekt übernehmen

Wähle konkrete Quellen und Unterordner. Keine pauschale Spiegelung sämtlicher
Projekte, Modelle, Git-Verwaltung oder persönlicher Daten. Nutze vorgeschriebene
Transferhelfer der jeweiligen Umgebung und führe lokale Befehle mit dem
zurückgegebenen Arbeitsverzeichnis aus.

## Änderungen konfliktfrei zurückbringen

Vor dem Rücktransfer Originale gegen die Ausgangs-Prüfsummen vergleichen. Parallel
geänderte Originale nicht einfach überschreiben. Ersetzte Dateien sichern, neue
Dateien vollständig prüfen und den Abschluss mit SHA-256 belegen. Erst danach
darf genau diese lokale Aufgabenablage entfernt werden. Bei einem getrennten
NAS die lokale Kopie behalten und den offenen Transfer klar benennen.

## Instabile Metadaten

SMB kann Zeitstempel nach dem ersten Lesen normalisieren. Ein Stabilitätstest
kann dann anschlagen, obwohl der Inhalt gleich blieb. Den Unterschied untersuchen,
gezielte Dateien stabil einlesen und den vorgesehenen Helfer erneut versuchen.
Nicht pauschal Schutzregeln abschalten. Ein projektbezogener Inhaltsvergleich muss
echte Konflikte weiterhin erkennen und Sicherungen erhalten.

Laufzeitcaches und `node_modules` sind nicht automatisch finale Produktionsdaten.
Quellen, Lockfile, Exporte und relevante Nachweise müssen zurückkehren. Ein
fertiger Render in einer vergessenen lokalen Kopie ist noch keine abgeschlossene
Projektübergabe.
