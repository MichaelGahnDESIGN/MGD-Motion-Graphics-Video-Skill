---
name: mgd-motion-graphics-video
description: Erstellt und überarbeitet Reels, YouTube-Videos, Werbefilme und Motion Graphics mit Schnitt, bewegter Typografie, Compositing, Audio und geprüftem Export. Unterstützt lokale Werkzeuge sowie gezielt gewählte ECC-Skills und Medien-Plugins.
---

# MGD Motion Graphics Video Skill

Erzeuge ein verwendbares Video und ein nachvollziehbares Projekt. Arbeite vom
Material und Ziel des jeweiligen Projekts aus. Eine konkrete Korrektur setzt das
bestehende Projekt fort; beginne dabei kein neues Briefing und installiere nicht
vorsorglich die gesamte Werkzeugliste.

## Aufrufe und Start

Für `/MGD-Motion`, `/reel` und die spezialisierten Varianten lies bei Bedarf
[commands.md](references/commands.md). In Codex erfolgt die explizite Auswahl
mit `$mgd-reel` und den entsprechenden Skill-Namen; Claude Code kann die
installierten Slash-Befehle verwenden. Keine native Slash-Funktion behaupten,
wenn die Umgebung sie nicht anbietet.

Beim ersten Einstieg fehlenden Video-Projektordner und erstes Thema gemeinsam
erfragen. Sind sie bereits angegeben, direkt damit weiterarbeiten. Bei einer
Korrektur wie `/MGD-Video-Optimieren` vorhandenes Projekt fortsetzen. Ein
Installationsauftrag allein ist kein Auftrag, bereits einen Film zu erzeugen.

## Einstieg und Werkzeugwahl

1. Stelle die tatsächliche Projektwurzel, vorhandene Regeln, Git-Status und den
   letzten brauchbaren Export fest. Lies relevante Marken-, Inhalts- und
   Materialinformationen im Projekt. Private Quellen bleiben dort.
2. Kläre nur fehlende Angaben, die das Ergebnis wesentlich ändern: Zielgruppe,
   Botschaft/Handlung, Format, ungefähre Länge, Sprache, vorhandene Medien und
   gewünschter Stil. Übernimm bereits getroffene Entscheidungen.
3. Nutze passende vorhandene Werkzeuge. **FFmpeg** eignet sich für Schnitt,
   Konvertierung und Ton; **HyperFrames + GSAP** für lokale HTML-Motion-Graphics;
   **Remotion** für gewählte React-Videoprojekte; **Manim** für mathematische
   Erklärungen; **Blender** für tatsächlich benötigte 3D-Szenen. Bestehende Projekte
   haben Vorrang vor einem Framework-Wechsel.
4. Prüfe mit `scripts/doctor.py` die Umgebung. Vor einem Browsercheck vertraulicher
   Inhalte alle Schriften lokal auflösen: HyperFrames kann selbstständig
   Webfonts einschließlich Text-Subsets abrufen; siehe Installationsreferenz. Für fehlende Werkzeuge oder Skills
   lies [installation.md](references/installation.md). Installation, globale
   Konfiguration, Cloud-Upload und Veröffentlichung sind getrennte Handlungen;
   ein Videoauftrag allein autorisiert keine Kontoänderung oder bezahlte API.

## Umsetzung

- Lies [workflows.md](references/workflows.md) für das gewählte Videoformat.
  Halte ein kurzes Briefing und einen Szenenplan fest. Bei kleinen Korrekturen
  genügt die dokumentierte Änderung am bestehenden Plan.
- Wähle Bildsprache, Typografie, Farbe, Bewegungsrhythmus und Ton passend zur
  Marke. „Epischer“ wird in konkrete Entscheidungen übersetzt: stärkere Tiefe,
  Enthüllungen, präzisere Akzente, abwechslungsreiche Kamerabewegung und einen
  lesbaren Höhepunkt. Fantasy ist eine mögliche Stilrichtung, kein Standard
  für jedes Produkt.
- Lies bei Motion Graphics [motion-graphics.md](references/motion-graphics.md).
  Bewege Motiv, Vordergrund, Atmosphäre und Schrift bewusst auf getrennten
  Ebenen. Schütze Gesichter, Logos und Kernaussagen vor Effekten.
- Verarbeite Originale ausschließlich zu Ableitungen im Projekt. Halte Herkunft,
  Nutzungsrechte und bei wichtigen Quellen SHA-256 fest. Neue Exportversionen
  bekommen neue Namen. Keine Originale oder bestätigten Exporte überschreiben.
- Komponiere jedes Seitenverhältnis separat: Gruppenszenen müssen vollständig
  hineinpassen, Text neu umbrechen und wichtige Inhalte außerhalb der aktuellen
  Plattformbedienelemente liegen. Ein starrer Mittelzuschnitt reicht oft nicht.
- Verwende eine zentrale Zeit- und Formatkonfiguration. Haltezeiten beginnen,
  sobald alle benötigten Inhalte lesbar stehen. Eine Verlängerung muss auch
  Effekte, Musik, Root-Dauer und Export-Sollwerte verlängern.
- Für neue lokale Projekte kann `scripts/new_project.py` den neutralen Starter
  erzeugen. Er ist ein überprüfbarer Ausgangspunkt, keine gestalterische Vorgabe.
- Lies [audio-export.md](references/audio-export.md) für Ton und Lieferung.
  Kostenpflichtige Generierung, fremde Musik und künstliche Stimmen brauchen
  passende Rechte und die jeweilige Freigabe. Keine Whooshes als Automatismus.

## ECC und Plugins gezielt kombinieren

Lies [integrations.md](references/integrations.md), wenn Zusatzfähigkeiten nötig
sind. Lade nur passende Skills. Bereits installierte `ecc-*`-Varianten können
verwendet werden. Upstream-Annahmen über Claude, Toolnamen, Pflichtinterviews,
Uploads oder zusätzliche Bestätigungen ersetzen keine aktuellen Benutzer- und
Umgebungsregeln. Verfügbare Fähigkeiten prüfen statt Toolaufrufe erfinden.

`motion-foundations`, `motion-patterns` und `motion-advanced` behandeln vorwiegend
React-Weboberflächen. Sie werden nur für passende Web-/React-Aufgaben geladen;
ihre SSR- und `motion/react`-Regeln gelten nicht pauschal für GSAP-Videotimelines.

## Abnahme und Lieferung

Lies [quality-checks.md](references/quality-checks.md), prüfe tatsächliche Bilder,
Übergänge, Lesedauer und den fertigen Export. Ein erfolgreicher Build oder korrekte
MP4-Metadaten ersetzen keine Sicht- und Hörkontrolle. Bei einem bestimmten Fehler
lies den passenden Abschnitt in [lessons.md](references/lessons.md).

Liefer Video mit klickbarem absolutem Dateipfad bzw. nativer Vorschau, bearbeitbare
Quellen und einen kurzen Prüfbericht. Benenne Format, Dauer, geprüfte Eigenschaften
und offene Grenzen. Unterscheide lokale Prüfung von echter Plattformabnahme.
Veröffentliche oder sende das Video nur im ausdrücklich beauftragten Umfang.

Bei NAS-Projekten lies [nas-local.md](references/nas-local.md). Verfügbare lokale
Transferregeln haben Vorrang; fertige Daten müssen geprüft ins Originalprojekt
zurückkehren. Quellen und Versionsstände stehen in
[sources.md](references/sources.md).
