# MGD Motion Graphics Video Skill

Ein deutsch dokumentierter Skill für **Reels, YouTube-Videos, Werbefilme,
Motion Graphics und Animationen**. Er verbindet Projektmaterial, Dramaturgie,
bewegte Typografie, Compositing, Schnitt, Ton und überprüfbare Videoexporte.

Lokale Werkzeuge bilden den Kern. Passende ECC-Skills und Medien-Plugins können
gezielt ergänzt werden. Der Aufbau orientiert sich am
[Video Composer Skill](https://github.com/MichaelGahnDESIGN/ChatGPT-Video-Composer-Skill)
und der MGD-Skill-Struktur. Version **0.1.0**.

## Was enthalten ist

- Ein kompakter [Skill-Einstieg](skills/mgd-motion-graphics-video/SKILL.md) mit
  vertiefenden Anleitungen für Gestaltung, Formate, Ton, Qualität und Fehlersuche.
- Ein Installer mit Vorschau, festen Upstream-Versionen, SHA-256-Prüfung,
  wählbaren Profilen und Schutz bestehender Skill-Installationen.
- Ein neutraler lokaler Demo-Baukasten: **9:16, 16:9 und 1:1**, räumliche
  Vektorwelt, bewegte Schrift, Lichtpartikel und konfigurierbare Schluss-Haltezeit.
- Umgebungsprüfung, projektlokales Toolsetup, Renderhilfe und Exportprüfung.
- [Versionierte Wiki-Dokumentation](docs/wiki/Home.md), Tests und
  [Prüfnachweise](docs/arbeitsberichte/).

Erfahrungen aus realen Iterationen sind als allgemeine Fehlerhilfen enthalten:
sichtbare Nebelkanten, abgeschnittene Gruppen, strichartige Partikel, zu kurze
Schlussbilder, fehlende Timeline-Bindungen und NAS-Probleme. Private Medien,
Projektpfade und Inhalte gehören nicht zum öffentlichen Paket.

![Neutraler, lokal erzeugter Demo-Baukasten in 9:16](docs/media/demo-reel.jpg)

## Schnellstart

Voraussetzungen: Python ≥3.9. Für Videos zusätzlich Node.js ≥22 mit npm,
FFmpeg/ffprobe und kompatibles Chrome/Chromium. Der Installer selbst braucht
weder npm noch GitHub-Anmeldung.

```bash
git clone https://github.com/MichaelGahnDESIGN/MGD-Motion-Graphics-Video-Skill.git
cd MGD-Motion-Graphics-Video-Skill
python3 skills/mgd-motion-graphics-video/scripts/doctor.py
```

Installationsplan für ein gewähltes Projekt ansehen:

```bash
python3 skills/mgd-motion-graphics-video/scripts/install.py --target /PFAD/PROJEKT/.agents/skills --profile core
```

Nach Prüfung mit `--apply` ausführen. Ohne Profil wird ausschließlich der
MGD-Skill installiert. `core` ergänzt die HyperFrames-Basis und ECC video-editing.
Weitere Profile und die bewusst getrennte globale Installation stehen in der
[Installationsanleitung](skills/mgd-motion-graphics-video/references/installation.md).
Keine bestehende abweichende Skill-Installation wird überschrieben.

Ein eigenes Demo-Projekt erzeugen:

```bash
python3 skills/mgd-motion-graphics-video/scripts/new_project.py /PFAD/PROJEKT/mein-reel --preset reel --end-hold 4
python3 skills/mgd-motion-graphics-video/scripts/setup_tools.py /PFAD/PROJEKT/mein-reel --apply
cd /PFAD/PROJEKT/mein-reel
python3 tools/build.py
```

Ersetze die Platzhalter durch echte absolute Pfade. Für Querformat `--preset youtube`,
für Quadrat `--preset square`. Danach checken, ansehen und rendern wie in der
[Anleitung](skills/mgd-motion-graphics-video/references/installation.md).
Auf NAS-Systemen Abhängigkeiten und Renderarbeit in einer erlaubten lokalen
Arbeitskopie ausführen; Quellen und Ergebnisse anschließend geprüft zurückgeben.

## Verwendung im Agenten

Nach der Installation den Skill beispielsweise so aufrufen:

> Nutze $mgd-motion-graphics-video. Erstelle aus den Materialien dieses Projekts
> ein dynamisches Fantasy-Reel in 9:16. Runde magische Lichtpartikel, Regen hinter
> dem Motiv, keine zusätzlichen Whooshes. Halte den vollständig lesbaren Schluss
> sechs Sekunden und liefere einen hochwertigen MP4-Export mit Prüfbericht.

Oder:

> Nutze $mgd-motion-graphics-video für einen erklärenden YouTube-Film in 16:9 mit
> Kapiteln und Untertiteln. Verwende die vorhandene CI und die freigegebenen Medien.

Der Stil wird pro Projekt gewählt. Fantasy ist ein Beispiel, keine feste Vorgabe.
Ein vorhandenes Projekt wird gezielt weiterbearbeitet, ohne unnötigen Neustart.

## Grenzen, Kosten und Rechte

Der Skill selbst ist MIT-lizenziert. Zusatzskills behalten ihre jeweilige Lizenz.
Werkzeuge, Schriftarten, Musik, Medien und Generatoren haben eigene Bedingungen;
[Remotion](https://www.remotion.dev/docs/license) nicht pauschal als kostenlos
für jeden Einsatz behandeln. Details: [Drittanbieter](THIRD_PARTY.md).

Keine automatische Cloudgenerierung, Kontoverbindung oder Veröffentlichung.
Lokales Rendern benötigt Rechenleistung; externe Dienste können Credits oder
Gebühren verursachen. Ein kopierter Skill installiert keinen MCP-Server.
Plugins werden nur verwendet, wenn ihre Funktion tatsächlich verfügbar und der
betreffende Zugriff autorisiert ist.

Die technische Exportprüfung ersetzt keine Sicht-/Hörkontrolle und keine echte
Abnahme auf Instagram oder YouTube. Der Demo ist stumm; private Projektdaten
müssen für seine Nutzung nicht hochgeladen werden.

## Entwicklung und Prüfung

```bash
python3 tools/check.py
```

Die Standardprüfungen laufen ohne Netzwerk und ohne zusätzliche Python-Pakete.
Der tatsächliche Browser- und Render-Test ist gesondert im
[Prüfbericht](docs/arbeitsberichte/0.1.0-pruefung.md) dokumentiert.
Änderungen an Upstream-Versionen erfolgen bewusst über
`tools/update_dependency_lock.py`, mit anschließender Prüfung und Testexport.

[MIT-Lizenz](LICENSE) · [Wiki](docs/wiki/Home.md) ·
[Skill-Anleitung](skills/mgd-motion-graphics-video/SKILL.md)
