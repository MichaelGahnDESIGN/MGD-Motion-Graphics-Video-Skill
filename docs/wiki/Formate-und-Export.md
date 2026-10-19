# Seitenverhältnisse, Qualität und Export

## Das Motiv für das Format komponieren

9:16 eignet sich oft für Reels und Shorts, 16:9 für klassische YouTube-Videos und
1:1 für bestimmte Feed- oder Displayeinsätze. Der Auftrag entscheidet. Der
Starter bietet `reel` mit 1080×1920, `youtube` mit 1920×1080 und `square` mit
1080×1080. Das sind Arbeitsvorgaben, keine vollständige Liste aktueller
Plattformgrenzen. Uploadgrenzen vor der Veröffentlichung offiziell prüfen.

Texte neu umbrechen, Motive passend positionieren und Gruppen vollständig zeigen.
Wichtige Aussagen nicht an die äußersten Bildränder legen. Bedienelemente können
je nach App, Ansicht und Gerät andere Flächen belegen; eine pauschale Prozentzahl
ersetzt keine Zielvorschau.

## Hohe Qualität sinnvoll erreichen

Verwende geeignete Originalauflösung, lokale Schriften und saubere Ableitungen.
Behalte eine passende Bildrate bei. 4K-Upscaling ersetzt keine fehlenden Details.
Ein geeignetes SDR-Lieferformat ist häufig MP4 mit H.264 und yuv420p; bei
hochwertiger lokaler Ausgabe kann CRF 14–18 ein Ausgangspunkt sein. Dateigröße
und echte Bildqualität prüfen. Farbkonvertierung und Farbraummarkierung bewusst
behandeln; HDR nicht lediglich als SDR kennzeichnen.

Der Starter nutzt feste Paketversionen, 30 fps und eine zentrale Zeitkonfiguration.
Ein optionales ProRes-Master oder ein Alpha-Export braucht einen konkreten
Weiterverarbeitungszweck und ausreichend Speicher. Es ist nicht für jede kleine
Revision nötig.

## Neue Version exportieren

```bash
python3 /PFAD/ZUM/SKILL/scripts/run_pipeline.py /PFAD/PROJEKT render --output exports/film-v002.mp4
```

Ein vorhandener Name wird abgelehnt. Das Render-Skript nutzt die lokale Engine
und lädt nicht durch `npx` ungefragt eine neue Version. Es erzwingt nicht jedes
projektspezifische Lieferprofil. Danach [Export prüfen](Qualitaet.md), die echte
Datei ansehen und erst dann als fertig übergeben.
