# NAS und lokale Renderarbeit

Große Abhängigkeiten, Browserprofile, Hardlinks und viele kleine npm-Dateien
können auf SMB/NAS langsam sein oder fehlschlagen. Stelle zuerst den eigentlichen
Projektpfad fest. Nutze dann eine vom Benutzer erlaubte, auf dieses Projekt
begrenzte SSD-Arbeitskopie. Nur benötigte Quellen übernehmen; keine pauschale
Spiegelung von Git-Verwaltung, fremden Projekten oder großen Modellbeständen.

Wenn eine lokale Umgebung einen geprüften Transferhelfer vorgibt, dessen
`begin`/`finish`-Ablauf benutzen. Er darf Originale erst nach Konfliktprüfung
ersetzen und die lokale Kopie erst nach erfolgreichem SHA-256-Abgleich entfernen.
Keine fremden Aufgabenordner leeren oder globale Dateischutzregeln abschalten.

SMB-Zeitstempel können nach dem ersten Lesen normalisiert werden und einen
Metadaten-Stabilitätstest irritieren. Lese-/Stat-Ergebnis prüfen, benötigte eigene
Dateien stabil einlesen und den vorgesehenen Helfer erneut versuchen. Wenn das
nicht reicht, Ursache dokumentieren und einen projektspezifischen, überprüfbaren
Transfer mit echter Inhalts- und Konfliktprüfung vorbereiten. Keinen Fehler
pauschal ignorieren und niemals unverifizierte lokale Dateien löschen.

npm-Abhängigkeiten und Laufzeitcaches sind keine finalen Produktionsdateien.
Zurück gehören Quellen, Lockfile, finale Exporte und die relevanten Nachweise.
Kein „fertig“, solange ein erforderlicher Rücktransfer offen ist. Entferne
anschließend ausschließlich den erfolgreich abgeglichenen Aufgabenordner.
