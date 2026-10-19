# Befehle und komplette Prompt-Bibliothek

Alle Aufrufe verwenden denselben Hauptskill und wechseln nur den Arbeitsmodus.
In Codex den Eintrag mit `$skill-name` oder über die Skill-Auswahl wählen. Die
Schreibweise `/MGD-Reel` ist die gewünschte Kurzbezeichnung; ein frei definierter
nativer Codex-Slash-Befehl wird damit nicht versprochen. In Claude Code erzeugen
die optional installierten Befehlsdateien die unten genannten Slash-Aufrufe.
Bei Plugin-Installation können Aufrufe zusätzlich den Plugin-Namensraum tragen.

`/MGD-Video-Optimieren` ist der endgültige Name für die Verbesserung bestehender
Videos. Der frühere Entwurf `/MGD-Optimieren` wird nicht installiert.

| Gewünschter Aufruf / Claude-Befehl | Codex-Skill | Zweck |
|---|---|---|
| `/MGD-Motion` | `$mgd-motion` | Einstieg und Werkzeugwahl |
| `/reel` | `$reel` | Reel-Kurzaufruf |
| `/MGD-Video` | `$mgd-video` | Videos allgemein |
| `/MGD-Reel` | `$mgd-reel` | Reels und Shorts |
| `/MGD-Trailer` | `$mgd-trailer` | Trailer und Teaser |
| `/MGD-Erklärvideo` | `$mgd-erklaervideo` | Erklärvideo |
| `/MGD-Motion-Graphic-Animation` | `$mgd-motion-graphic-animation` | Motion Graphics und Animation |
| `/MGD-Anime` | `$mgd-anime` | Anime-Szenen und Trailer |
| `/MGD-Werbefilm` | `$mgd-werbefilm` | Werbefilm |
| `/MGD-Produktvideo` | `$mgd-produktvideo` | Produktvideo |
| `/MGD-YouTube` | `$mgd-youtube` | YouTube mit Kapiteln |
| `/MGD-Logo-Animation` | `$mgd-logo-animation` | Logo-Animation |
| `/MGD-Loop` | `$mgd-loop` | Nahtlose Animation |
| `/MGD-Video-Optimieren` | `$mgd-video-optimieren` | Vorhandenes Video verbessern |

## So verwendest du die Vorlagen

Eckige Platzhalter durch eigene Angaben ersetzen. Sind Thema oder Projektordner
noch unbekannt, den Agenten danach fragen lassen. Bereits bekannte Angaben
müssen nicht wiederholt werden. Ein Formatvorschlag darf ausdrücklich geändert
werden. Originale, bisherige Freigaben und bestehende Entscheidungen bleiben
maßgeblich.

## /MGD-Motion

Einrichtung und Einstieg in eine neue Videozusammenarbeit.

> Nutze den MGD Motion Graphics Video Skill. Richte den Video-Workflow für dieses Projekt ein. Prüfe vorhandene Werkzeuge und Skills, ohne ungefragt globale Einstellungen zu ändern. Frage mich zuerst, wo unsere Videoprojekte liegen sollen und welches Thema beziehungsweise welche Videoart wir beginnen. Vorhandene Angaben übernehmen.

## /reel

Kurzer alternativer Einstieg für vertikale Social-Videos.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein dynamisches Reel über [Thema] für [Plattform]. Nutze die Materialien aus [Projektordner], einen starken Einstieg, abwechslungsreiche Schnitte und gezielt bewegte Schrift. Komponiere in 9:16, schütze wichtige Inhalte vor Plattformbedienelementen und halte die Schlussbotschaft nach dem Texteinlauf ausreichend lange lesbar.

## /MGD-Video

Freie Videoformate und Mischformen ohne spezielleren Workflow.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein hochwertiges Video über [Thema] aus den Materialien in [Projektordner]. Zielgruppe: [Zielgruppe], Format: [Format], ungefähre Dauer: [Dauer]. Entwickle Dramaturgie, Bildsprache und Ton passend zum Ziel. Liefere die geprüfte Videodatei mit bearbeitbaren Quellen.

## /MGD-Reel

Instagram, Facebook, TikTok und vertikale YouTube Shorts.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein dynamisches Reel über [Thema] für [Plattform]. Verwende die Materialien aus [Projektordner]. Beginne mit einem starken Bild oder einer klaren Aussage, entwickle eine kleine Geschichte und schließe mit [gewünschte Handlung oder Änderung]. Nutze 9:16, gut lesbare Einblendungen und passende Bewegung. Berücksichtige die aktuelle Plattformvorschau.

## /MGD-Trailer

YouTube-Trailer, Buch-, Spiel- und Projektteaser.

> Nutze den MGD Motion Graphics Video Skill. Erstelle einen spannenden Trailer für [Thema] aus [Projektordner]. Baue Atmosphäre, Neugier und eine deutliche Steigerung auf. Nutze starke Enthüllungen, präzise Schnitte und einen wirkungsvollen Abschluss mit Logo und [gewünschte Handlung oder Änderung]. Format: [Format], Dauer: [Dauer]. Vermeide unnötige Wiederholungen und wichtige Spoiler.

## /MGD-Erklärvideo

Sachverhalte, Anleitungen, Schulung und Wissensvermittlung.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein verständliches Erklärvideo über [Thema] für [Zielgruppe]. Verwende Materialien aus [Projektordner], einen klaren Ablauf, anschauliche Beispiele und passende Animationen. Stimme Sprechtext, Untertitel und Bilder aufeinander ab. Prüfe fachliche Aussagen und beschrifte wichtige Zusammenhänge gut lesbar.

## /MGD-Motion-Graphic-Animation

Gestaltete Animationen aus Schrift, Grafik, Formen und Compositing.

> Nutze den MGD Motion Graphics Video Skill. Erstelle eine eigenständige Motion-Graphics-Animation über [Thema] für [Marke]. Nutze bewegte Typografie, Formen, Masken, räumliche Ebenen und motivierte Übergänge. Entwickle eine zusammenhängende Bewegungssprache im Stil [Stil]. Format: [Format], Dauer: [Dauer]. Texte bleiben trotz Dynamik gut lesbar.

## /MGD-Anime

Anime-Erzählung, Stilentwicklung, Szenen und animierte Figuren.

> Nutze den MGD Motion Graphics Video Skill. Entwickle ein Anime-Video über [Thema] mit konsistenten Figuren, ausdrucksstarken Einstellungen und einer zusammenhängenden Bildsprache. Nutze Charaktervorlagen aus [Projektordner]. Unterscheide echte Figurenanimation von Kamerafahrten auf Standbildern. Prüfe benötigte Werkzeuge; vor externer Generierung Kosten und Referenzupload klären.

## /MGD-Werbefilm

Werbung, Angebote und Kampagnen mit konkreter Handlung.

> Nutze den MGD Motion Graphics Video Skill. Erstelle einen Werbefilm für [Produkt oder Angebot]. Zeige den wichtigsten Nutzen für [Zielgruppe], halte die Markenrichtlinien aus [Projektordner] ein und führe zu [gewünschte Handlung oder Änderung]. Verwende belegbare Aussagen und erstelle passende Fassungen für [Plattform] in [Format]. Veröffentliche den Film nur auf gesonderten Auftrag.

## /MGD-Produktvideo

Produktvorstellung, Funktionsdarstellung und Anwendung.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein hochwertiges Produktvideo für [Produkt oder Angebot] aus [Projektordner]. Zeige Details, Anwendung und Vorteile mit passenden Nahaufnahmen, Animationen und kurzen Beschriftungen. Stelle Produkt und Funktionen korrekt dar. Nutze vorhandene Produktmedien und Designvorlagen. Format: [Format], Dauer: [Dauer].

## /MGD-YouTube

Längere Videos, Kapitel, Interviews und redaktionelle Formate.

> Nutze den MGD Motion Graphics Video Skill. Erstelle ein YouTube-Video über [Thema] in 16:9 mit ungefähr [Dauer]. Nutze Materialien aus [Projektordner]. Plane einen starken Einstieg, verständliche Kapitel, passende Einblendungen und abwechslungsreiche Bilder. Ergänze bei Bedarf Untertitel sowie einen Titelvorschlag und eine Idee für das Vorschaubild.

## /MGD-Logo-Animation

Markenenthüllung, Intro, Outro und animierter Logoabschluss.

> Nutze den MGD Motion Graphics Video Skill. Erstelle eine hochwertige Logo-Animation für [Marke] aus den Dateien in [Projektordner]. Der Stil soll [Stil] wirken. Bewahre Form und Proportionen des Logos. Plane eine passende Enthüllung und eine ruhige, gut erkennbare Schlussphase. Format: [Format], Dauer: [Dauer].

## /MGD-Loop

Nahtlose Wiederholungen für Displays, Hintergründe und Social Media.

> Nutze den MGD Motion Graphics Video Skill. Erstelle eine nahtlos wiederholbare Animation über [Thema] für [gewünschte Handlung oder Änderung]. Anfang und Ende sollen ohne sichtbaren Sprung ineinander übergehen. Prüfe den Übergang über mehrere Wiederholungen, einschließlich Partikeln, Kamera und gegebenenfalls Ton. Format: [Format], Dauer: [Dauer].

## /MGD-Video-Optimieren

Gezielte Verbesserung vorhandener Videos und bestehender Quellprojekte.

> Nutze den MGD Motion Graphics Video Skill. Analysiere das vorhandene Video [Dateipfad] und verbessere gezielt [gewünschte Handlung oder Änderung]. Erhalte bereits gelungene Teile und berücksichtige bisherige Entscheidungen. Nutze nach Möglichkeit das zugehörige Quellprojekt, schütze Originale und speichere eine neue Version. Prüfe die tatsächlich exportierte Datei auf die gewünschten Verbesserungen.

## Prompt ohne Agenten vorbereiten

Vom Repository-Hauptordner aus:

```bash
python3 skills/mgd-motion-graphics-video/scripts/commands.py list
python3 skills/mgd-motion-graphics-video/scripts/commands.py show /MGD-Reel --thema "Eine fantastische Reise" --ordner "/PFAD/ZUM/PROJEKT" --plattform "Instagram"
python3 skills/mgd-motion-graphics-video/scripts/commands.py show /MGD-Video-Optimieren --datei "/PFAD/ZUM/PROJEKT/exports/film-v001.mp4" --ziel "ruhigere Schrift und längere Schlusskarte"
```

Diese Befehle geben Texte aus. Sie installieren nichts und starten keine
Videogenerierung. Alle Platzhalter können als gleichnamige Parameter übergeben
werden, etwa `--dauer`, `--format` oder `--zielgruppe`.

Weiter: [Installation](Installation.md) · [Projektstart](Projektstart.md) ·
[Videoarten](Videoarten.md) · [Problemlösung](Probleme-und-FAQ.md)
