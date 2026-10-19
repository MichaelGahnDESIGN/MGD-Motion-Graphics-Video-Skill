# Aufrufe und gezielter Einstieg

`assets/commands.json` ist die gemeinsame Quelle für alle 14 Aufrufe. Mit
`scripts/commands.py list` lassen sie sich lesen, mit `show AUFRUF` als kopierfertiger
Prompt ausgeben. Die Ausgabe startet keine Generierung.

| Gewünschter Aufruf / Claude-Datei | Codex-Skill | Schwerpunkt |
|---|---|---|
| `/MGD-Motion` | `$mgd-motion` | Einrichtung, fehlenden Ordner und erstes Thema erfragen |
| `/reel` | `$reel` | Vertikaler Social-Kurzaufruf |
| `/MGD-Video` | `$mgd-video` | Freie Videos |
| `/MGD-Reel` | `$mgd-reel` | Instagram, Facebook, TikTok, Shorts |
| `/MGD-Trailer` | `$mgd-trailer` | Teaser und Spannung |
| `/MGD-Erklärvideo` | `$mgd-erklaervideo` | Verständliche Vermittlung |
| `/MGD-Motion-Graphic-Animation` | `$mgd-motion-graphic-animation` | Typografie, Formen und Compositing |
| `/MGD-Anime` | `$mgd-anime` | Konsistente Anime-Szenen, Animatics und Animation |
| `/MGD-Werbefilm` | `$mgd-werbefilm` | Nutzen und Handlung |
| `/MGD-Produktvideo` | `$mgd-produktvideo` | Korrekte Produkt-/Funktionsdarstellung |
| `/MGD-YouTube` | `$mgd-youtube` | Kapitel und längere Formate |
| `/MGD-Logo-Animation` | `$mgd-logo-animation` | Markenenthüllung und Abschluss |
| `/MGD-Loop` | `$mgd-loop` | Nahtlose Wiederholung |
| `/MGD-Video-Optimieren` | `$mgd-video-optimieren` | Bestehende Videos gezielt verbessern |

Codex verwendet Skills; veraltete Custom-Prompts nicht als neue Integration
installieren. Claude Code kann die mitgelieferten Befehlsdateien nutzen; Plugins
können einen eigenen Namensraum voranstellen. Behaupte keine live geprüfte
Composer-Funktion allein aufgrund einer kopierten Datei.

Bei einem neuen Einstieg fehlenden Zielordner und erstes Thema gemeinsam erfragen.
Vorhandene Angaben übernehmen. Für eine Korrektur aus Datei und bestehendem
Projekt arbeiten, ohne unnötig ein neues Thema oder Gesamtbriefing abzufragen.
Stil und Formatvorschläge bleiben durch ausdrückliche Benutzerwünsche änderbar.
