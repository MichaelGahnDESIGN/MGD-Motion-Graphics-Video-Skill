# Bewährte Fehlerdiagnose aus realen Video-Iterationen

| Sichtbarer Fehler | Häufige Ursache | Konkrete Korrektur |
|---|---|---|
| Rechteckige Kante im Nebel | SVG-Filterregion oder Texturende fährt ins Bild | Overscan, weiche Alphamaske an allen Seiten, kritischen Bewegungszeitpunkt ansehen |
| Figuren außen abgeschnitten | Breites Motiv mit `cover` auf Hochkant gezwungen | Gruppe passend skalieren/neu anordnen, ggf. vorhandene Gruppen trennen und sauber freistellen |
| Goldene „Ameisen“ | Animierte Striche und gestrichelte Pfade | Runde Lichtkerne mit Halo, Größen-/Tiefenvariation und weicher Drift |
| Endkarte zu kurz | Haltezeit wurde schon während des Texteinlaufs gezählt | Start nach letztem Text, dann eigenständige lesbare Haltezeit |
| Letzte Sekunden ohne Effekte/Ton | Nur Root-Dauer verlängert | Gemeinsame Konfiguration für Szenen, FX, Audio, Fade und Framezahl |
| Buchstaben fehlen | Selektoren verlieren nach Root-ID-Ersetzung ihre Treffer | Stabile innere IDs und vorhandene Glyphen im gemounteten Bild prüfen |
| Unerwartete Schrift-Netzwerkanfrage | Engine ersetzt Systemschriftnamen durch Webfonts | Lokale @font-face oder generische Familien verwenden und Compiler-/Netzwerkverhalten prüfen |
| Export anders als Vorschau | Wallclock, Zufall oder vorwärtsabhängige Callbacks | Zeitbasierte, pausierte Timeline und feste Seeds; reale Exportframes ansehen |
| Check meldet fehlende Timeline | Registrierung nur in externer JS-Datei verborgen | Explizite Registrierung im HTML, animierte Timeline anschließend zuweisen |
| Partikel bestehen Sichtbarkeitstest nicht | Gewollte geringe Deckkraft unter Testgrenze | Hellen Kern testen, weiche Hintergrundpunkte nicht als Hauptmotiv deklarieren |
| Störender Ton bei jeder Bewegung | Automatisch eingesetzte Whooshes | Effekte einzeln begründen, abgelehnte Geräusche entfernen |
| FFmpeg-Daten stimmen, Gestaltung nicht | Nur Metadaten geprüft | Echte Frames, Übergänge und vollständige Schlusskarte sichten |
| Browser-Snapshots fehlen | Werkzeug hat Zeiten ausgelassen/zusammengefasst | Anzahl vergleichen, fehlende Zeit direkt oder aus MP4 extrahieren |

Diese Befunde sind Diagnosehilfen, keine starren Stilvorgaben. Bestehende gute
Teile erhalten und die konkrete Ursache beheben. Private Beispielbilder, Texte,
Figuren oder Projektpfade sind absichtlich nicht Bestandteil dieses Pakets.
