# Aktualisieren, Sichern und Wiederherstellen

## Versionen auseinanderhalten

Skill-Version, Zusatzskill-Revisionen, Videolaufzeit und Filmexport sind getrennte
Stände. Version 0.2.0 des Skills bedeutet nicht, dass HyperFrames oder GSAP
aktualisiert wurden. Der Starter verwendet weiterhin seine geprüfte Sperrdatei.
Ein neuer Filmexport bekommt eine eigene Versionsnummer.

## Skill aktualisieren

Prüfe zuerst das lokale Git-Projekt und eigene Änderungen. Hole einen gewünschten
neuen Stand aus GitHub und sieh dessen Änderungen an. Ein einfaches `--apply`
überschreibt absichtlich keine abweichende Installation. Sichere eine vorhandene
Installation und vergleiche eigene Anpassungen, bevor du sie bewusst durch die
neue ersetzt. Verwende die Projektregeln für Ablage und Sicherung. Keine globale
Massenlöschung als Updateverfahren.

Wenn die Installation bereits exakt identisch ist, ist ein erneuter Aufruf
unschädlich. Ein abweichender einzelner Befehl blockiert den neuen Installationslauf,
damit persönliche Anpassungen erhalten bleiben. Die Aufrufdateien und der
Hauptskill sollten aus derselben Paketversion stammen.

## Abhängigkeiten bewusst ändern

Die Zusatzskills sind an Git-Revisionen mit Dateihashes gebunden. Der Maintainer
aktualisiert `dependencies.lock.json` ausdrücklich, prüft Lizenzen und führt
Tests aus. Für geänderte Video-Engines zusätzlich einen echten Browsercheck und
Testexport durchführen. Kein routinemäßiges `latest` bei jeder kleinen Korrektur.

## Einen Film zurücksetzen

Behalte den letzten brauchbaren Export und zugehörigen Quellstand. Bei Problemen
eine neue Reparaturversion erstellen oder bewusst zum gesicherten Stand
zurückkehren. Quellmedien bleiben unverändert. Nach einem NAS-Konflikt beide
Änderungsstände erhalten und den Konflikt lösen, bevor etwas gelöscht wird.
