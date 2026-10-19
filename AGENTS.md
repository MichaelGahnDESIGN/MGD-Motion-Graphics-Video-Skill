# Projektregeln

Dieses öffentliche Repository enthält einen projektneutralen Video-Skill.
Kommunikation, Kommentare und Dokumentation auf Deutsch. Eigene Hilfsskripte
liegen unter `tools/`, temporäre Dateien unter `.tmp/`, Nachweise unter
`docs/arbeitsberichte/`. Ausführbare Bestandteile des installierbaren Skills
gehören nach Skill-Konvention in dessen `scripts/`.

Keine privaten Medien, absoluten Benutzer-/NAS-Pfade, Tokens oder Konto-IDs
veröffentlichen. Globale Installationen, Kontoänderungen und externe Generierung
sind keine implizite Nebenwirkung eines Tests. Bestehende Quellen respektieren.

Prüfe Änderungen mit `python3 tools/check.py`. Bei Änderungen an Timeline,
Starter oder Laufzeit zusätzlich einen echten Browsercheck und Render ausführen.
Abhängigkeiten bewusst versionieren. Einen grünen technischen Test nicht als
Sichtprüfung oder tatsächliche Plattformabnahme bezeichnen.
