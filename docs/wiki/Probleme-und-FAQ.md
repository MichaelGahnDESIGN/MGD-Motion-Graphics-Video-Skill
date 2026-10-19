# Problemlösung und häufige Fragen

## Mein Slash-Aufruf wird nicht erkannt

In Codex `$mgd-reel` oder die Skill-Auswahl verwenden. `/MGD-Reel` ist nicht
automatisch ein frei definierter nativer Codex-Befehl. In Claude Code prüfen,
ob die optionale Befehlsdatei installiert ist; nach Änderungen die Sitzung
gegebenenfalls neu öffnen. Der vollständige Name für Optimierung lautet
`/MGD-Video-Optimieren` beziehungsweise `$mgd-video-optimieren`.

## Ein vorhandener Skill blockiert die Installation

Das ist der Konfliktschutz. Dry-Run und Zielpfad prüfen, vorhandene Anpassungen
vergleichen und einen bewussten Updateweg wählen. Nicht vorschnell den kompletten
Skill-Ordner oder fremde Befehle entfernen.

## Im Nebel erscheint ein Rechteck

Filterregion oder Texturende ist sichtbar geworden. Overscan und eine weiche
Alphamaske an allen Seiten prüfen. Den kritischen Bewegungszeitpunkt ansehen.
Mehr Blur allein löst nicht jede Kante.

## Figuren passen nicht in Hochkant

Ein breites Motiv wurde wahrscheinlich zu stark mit `cover` beschnitten. Gruppe
kleiner setzen, neu anordnen oder mehrere Einstellungen verwenden. Niemand soll
unbemerkt am Rand verschwinden.

## Die Partikel sehen wie Striche aus

Runde Lichtkerne mit weichem Halo und Tiefenvariation verwenden. Animierte
Strichsegmente eignen sich eher für gezeichnete Pfade als für magischen Staub.

## Der Schluss ist zu kurz oder verliert den Ton

Die Lesedauer beginnt erst nach dem letzten Texteinlauf. Danach Gesamtdauer,
Effekte, Musik, Fade und erwartete Framezahl gemeinsam verlängern. Beim Starter
`end_hold` ändern und erneut bauen.

## Der Browsercheck meldet keine Timeline oder doppelte Root-Dateien

Die Registrierung muss für den Compiler sichtbar sein. Eine HTML-Vorlage soll
nicht als zweite fertige Komposition entdeckt werden. Der enthaltene Starter
setzt die Kompositions-ID erst beim Build. Bei Unterkompositionen stabile innere
Selektoren nutzen, weil Root-IDs beim Einhängen ersetzt werden können.

## Ist ein grüner Check die fertige Abnahme?

Nein. Technische Checks, echte Bilder, Ton und Zielplattform ergänzen sich. Ein
Build beweist weder lesbare Typografie noch passende Musik oder Nutzungsrechte.
Siehe [Qualität](Qualitaet.md).
