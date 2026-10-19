# Ton, Qualität und Lieferung

## Ton

Nutze belegbar freigegebene Musik, Aufnahmen oder ausdrücklich gewählte Generatoren.
Lokales Rendern verursacht keine automatisch hinzukommende Medien-API-Gebühr,
verbraucht aber Rechenzeit; Abonnement, Strom, Lizenzen und Cloud-Guthaben sind
getrennte Kosten. Keine pauschale Zusage „kostenlos“ für jeden Workflow.

Schneide Musik musikalisch, verwende saubere Ein-/Ausläufe, vermeide abrupte
Phasensprünge. Sprache verständlich halten, Musik bei Bedarf absenken. SFX sparsam
und passend einsetzen; Whooshes sind keine Pflicht. Einen als störend abgelehnten
Effekt nicht in jeder Überarbeitung erneut einbauen.

-14 LUFS mit etwas True-Peak-Reserve kann für ein Musik-Reel ein Ausgangspunkt
sein, ist keine universelle Plattformpflicht. Sprache, Dynamik, Format und
Lieferanforderungen entscheiden. Miss die tatsächlich codierte Audiospur: Ein
geprüftes WAV beweist nicht, dass AAC im MP4 unverzerrt und richtig synchron ist.

## Ausgabeprofile als Ausgangspunkt

| Ziel | Sinnvolle Ausgangswerte |
|---|---|
| Social/YouTube SDR | MP4, H.264 High, yuv420p, Quellen-/Zielfps, Faststart |
| Hochwertige lokale Lieferung | CRF etwa 14–18, visuell und auf Dateigröße prüfen |
| Ton | AAC, 48 kHz, angemessene Bitrate; bei Stereo z. B. 256–320 kbit/s |
| Master | ProRes bzw. verlustarmes Format nur bei echtem Weiterverarbeitungsbedarf |
| Transparenz | Eigenes alpha-fähiges Lieferformat, Kompatibilität vorher prüfen |

Farbmanagement bewusst planen: SDR-Quellen korrekt nach Rec.709 verarbeiten und
markieren; HDR nicht einfach als SDR umetikettieren. Farbraum-, Transfer- und
Matrixangaben sowie die Darstellung im Zielplayer prüfen. Das mitgelieferte
Render-Skript übernimmt die Ausgabe der Engine; es erzwingt nicht sämtliche
Lieferprofile oder garantiert automatisch korrekte Farbmetadaten.

Ein erneutes Bild-Encoding nur für Musikmux oder Metadatenkorrektur vermeiden,
wenn die vorhandene Videospur passend ist. Kein 4K-Versprechen allein durch
Hochskalieren kleiner Bilder. Systemschrift kann für den neutralen Test ausreichen;
für reproduzierbare Produktion lizenzierte Schriften lokal mitgeben.

## Übergabe

Neuer Name je abgenommener Revision, etwa `projekt-reel-v003.mp4`. Dazu Format,
Dauer, Prüfbericht, Vorschau und bearbeitbare Quellen liefern. Keine Rohquellen
oder großen Master automatisch in ein öffentliches Git-Repository laden. Ein
lokal gutes Video ist noch keine bestätigte Instagram-/YouTube-Veröffentlichung.
