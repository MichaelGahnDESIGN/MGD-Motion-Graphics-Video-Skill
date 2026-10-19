# Bewegung, Tiefe und Effekte

## Bild und Kamera

Trenne Hintergrund, Motiv und Vordergrund, wenn die Quellen das zulassen. Bei
Kamerafahrten bewegen sich nahe Ebenen stärker als ferne. Nutze Reserven außerhalb
des Bildes und prüfe die maximalen Ausschläge: kein freigelegter Rand, keine
wiederholte Textur, kein abgeschnittener Kopf. Eine starre Zoomfahrt auf jedem
Foto ist noch keine eigenständige Motion-Gestaltung.

Eine Gruppe aus einem breiten Bild darf bei 9:16 nicht unbemerkt außen Personen
verlieren. Prüfe alternative Anordnung, kleinere Gesamtdarstellung oder mehrere
Einstellungen. Bei freigestellten Figuren alle Kanten und Schatten kontrollieren;
keine Identitäten durch generative Neuzeichnung verändern, wenn das nicht gewollt ist.

## Typografie

Stelle zuerst lesbaren Satz, Zeilenumbrüche und Hierarchie her. Animiere anschließend
Blöcke, Wörter oder Buchstaben passend zur Aussage. Lesedauer beginnt erst nach
der letzten wichtigen Enthüllung. Eine einzelne statische Ruhephase am Höhepunkt
kann stärker wirken als fortwährend zitternde Schrift.

Für Schlusskarten die gesamte benötigte Zeit einplanen: Markenenthüllung,
Autoren-/Produktzeile, Handlungsaufforderung, ruhige Lesephase, Ausklang. Bei
mehreren Zeilen sind beispielsweise 6–8 Sekunden vollständig lesbare Standzeit
ein sinnvoller Startpunkt, anschließend mit der tatsächlichen Textmenge prüfen.
Der neutrale kurze Starter verwendet 4 Sekunden und ist frei konfigurierbar.

## Übergänge

Wähle eine motivierte Verbindung: Form-/Bewegungsanschluss, Tiefenfahrt,
weiche Lichtenthüllung, atmosphärische Überblendung oder harter Rhythmusschnitt.
Behalte Bildrichtung und visuelle Hierarchie im Blick. Ein schneller Schnitt
braucht nicht gleichzeitig Blitz, Shake und Soundeffekt. Stroboskopartige
Sequenzen und unlesbare Zwischenzustände vermeiden.

## Magische Partikel und Regen

Magie wirkt mit runden Lichtkernen, weichen Halos, unterschiedlichen Größen,
Helligkeiten, Drift und Lebenszeiten räumlich. Wenige kräftige Kerne, viele
zurückhaltende Tiefenpunkte. Glühen begrenzen und Haut, Typografie und Logo schützen.
Gestrichelte goldene Pfade lesen sich häufig als laufende Striche statt Lichtstaub.

Regen bildet eine separate, kühlere Ebene hinter Magie und möglichst hinter dem
Motiv. Zwei gekachelte Ebenen mit verschiedenen Geschwindigkeiten geben Tiefe.
Kachelhöhe und Bewegungsstrecke müssen genau übereinstimmen, sonst springt die
Naht. Ein stilles Regenfoto allein ist kein animierter Regen. Keine Geräusche
hinzufügen, wenn nur eine visuelle Änderung beauftragt ist.

## Deterministische Videotimelines

Für HTML/GSAP: pausierte Timeline bei `window.__timelines[compositionId]`
registrieren. Die Registrierung im HTML für den statischen Compiler sichtbar
machen. Alle Änderungen aus Videozeit ableiten, Partikel fest seeden. Kein
`requestAnimationFrame`, unkontrolliertes `Math.random`, `Date.now`, autonome
CSS-Keyframes oder nur vorwärts funktionierende Callbacks für die Exportanimation.

Bei Unterkompositionen kann HyperFrames die Root-ID durch die Host-ID ersetzen.
Verwende deshalb stabile innere Selektoren und prüfe, ob alle Glyphen existieren.
Die Laufzeit besitzt Clip-Sichtbarkeit; animiere innere Wrapper für Ein-/Ausgänge.
Globale Effekte mit eigener, passend langer Timeline einbinden und im zusammengesetzten
Video kontrollieren. Ein isoliert korrektes Szenen-HTML belegt nicht den Endexport.
