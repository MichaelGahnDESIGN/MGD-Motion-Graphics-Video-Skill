# Charaktere: Sheet, LoRA und bewusste Werkzeugwahl

## Wann dieser Ablauf gilt

Bei Figuren, Charakteren, Avataren oder wiederkehrenden Maskottchen gehören ein
**Charakter-Sheet und ein echtes LoRA** zur Standardproduktion. Das gilt für alle
MGD-Videoarten, nicht nur Anime oder Fantasy. Ein LoRA ist ein trainierter Adapter
für ein bestimmtes Bildmodell. Ein Referenzbild, JSON-Steckbrief oder wiederholter
Prompt ist kein LoRA. Das Verfahren erhöht Wiedererkennbarkeit; es garantiert
keine perfekte Identität in jedem Bild.

Vor neuen Figurenbildern diesen Ablauf durchführen. Vorhandene freigegebene
Ressourcen prüfen und wiederverwenden. Bei unveränderter Figur und einem reinen
Schnitt-, Text- oder Tonfix weder das Interview noch das Training wiederholen.
Ein Video ohne Figuren benötigt diesen Zusatzablauf nicht.

## Gebündelt fragen, bevor Bilder oder Training starten

Den Dialog kurz und an vorhandenen Quellen ausrichten. Fehlende Angaben lassen
sich in drei Fragen zusammenfassen:

1. **Verbindliche Figur:** Welche Version und Referenzen gelten? Gibt es bereits
   ein freigegebenes Charakter-Sheet? Erkennbare Varianten nicht mischen; bei
   Menschen Darstellungseinwilligung und zulässige Nutzung klären.
2. **Vorhandenes LoRA:** Gibt es bereits eines? Nach vollständigem Dateipfad oder
   eindeutigem Anbieter-Modellverweis, Basismodell/Version, Triggerwort und
   Nutzungsrechten fragen. Wenn nicht, neues LoRA einplanen. Den Benutzer nicht
   erneut nach einem bereits eindeutig angegebenen Pfad fragen.
3. **Werkzeuge und Rahmen:** Womit sollen Sheet und Bilder entstehen:
   ChatGPT/OpenAI, lokale Bildgenerierung, Higgsfield oder anderer Anbieter?
   Welcher kompatible Trainer soll gegebenenfalls das LoRA erstellen? Welche
   Referenzen dürfen wohin übertragen werden und wie hoch ist der Kostenrahmen?

Beispiel für den dritten Teil: „Für Sheet und Bilder: OpenAI-Imagegen in der
Cloud, ein lokales Modell, Higgsfield oder ein anderer Anbieter? Ein echtes LoRA
braucht zusätzlich einen kompatiblen Trainer. Soll dieser lokal laufen oder darf
ein konkret benannter Cloud-Dienst die freigegebenen Trainingsbilder erhalten?
Welches Budget gilt dafür?“

Sind Antworten unklar, daran abhängige Generierung pausieren; unabhängig davon
Kanon und bereits freigegebene Projektinformationen auswerten und den Schnittplan
vorbereiten. Nicht aufgrund verstrichener Zeit einen Anbieter oder Upload wählen.
Passende Entscheidungen und Freigaben gelten weiter, solange Figur, Daten,
Anbieter, Zweck und Kostenrahmen dazu passen.

## Bildanbieter und LoRA-Trainer sind zwei Entscheidungen

| Gewünschter Weg | Was vorher zu prüfen und offenzulegen ist |
|---|---|
| ChatGPT/OpenAI-Bildwerkzeug | Cloud-Verarbeitung, auch bei Aufruf aus einer lokalen App. Verfügbare Bild-/Referenzfunktionen prüfen; das integrierte Imagegen-Werkzeug bietet in diesem Workflow kein eigenes LoRA-Training und keinen zugesagten Import fremder LoRA-Gewichte. Für das LoRA einen separat unterstützten Trainer und für dessen Verwendung ein kompatibles Bildmodell wählen. |
| Lokale Generierung | Konkretes Modell und laufende Werkzeuge, z. B. ComfyUI oder Diffusers, sowie unterstütztes Adapterformat prüfen. Generierung ist nicht automatisch Training; ein passender Trainer kann zusätzlich nötig sein. Hardware, Speicher, Modelllizenzen und erforderliche Downloads vorher prüfen. |
| Higgsfield | Cloud-Dienst. Installiertes Plugin, verbundenes Konto und tatsächliche aktuelle Modellfunktionen prüfen. Charakterreferenz, proprietärer Charakterdienst und exportierbares LoRA sind verschiedene Fähigkeiten. Training oder Import/Export nicht aus einem Produktnamen ableiten. |
| Anderer Anbieter | Name, Modell, Datenempfänger, mögliche Unterauftragnehmer, Rechte, Speicherung, Trainings-/Exportfunktion und Credits vor dem Job klären. |
| Vorhandenes LoRA | Datei zunächst nur lesend prüfen. Adapter und Zielmodell müssen zusammenpassen; ein SDXL-Adapter lässt sich beispielsweise nicht allein wegen der Dateiendung in jedes andere Modell laden. |

Verfügbarkeit anhand der aktuellen Werkzeuge und offiziellen Dokumentation
prüfen, statt Funktionslisten zu erfinden. Ein nicht exportierbarer proprietärer
Charakterbezug wird nicht als gelieferte LoRA-Datei bezeichnet. Bei einem
zulässigen verwalteten Adapter die Modell-ID, Basis und tatsächliche Nutzbarkeit
belegen und diese Lieferform vorher mit dem Benutzer vereinbaren.

**Keine stille Ersatzlösung:** Unterstützt der gewählte Weg kein echtes LoRA,
die konkrete Grenze nennen. Dann einen unterstützten Trainings-/Generierungsweg
klären. Möchte der Benutzer ausdrücklich nur Referenzbilder ohne LoRA, diese
Abweichung als `deferred_by_user` festhalten. Ohne diese Entscheidung bleibt das
LoRA `blocked`; nicht als fertig melden oder ungefragt zu einem anderen Anbieter
wechseln. Dieses Skill-Update selbst startet keinen Trainingsjob.

## Charakter-Sheet erstellen oder validieren

- Verbindliche Merkmale aus freigegebenem Kanon und Referenzen festhalten:
  Gesicht, Körperbau, Proportionen, Haut/Fell, Augen, Haare, Flügel/Hörner,
  Kleidung, Rüstung, markante Gegenstände und Farbpalette. Spoiler auslassen.
- Sheet mit zweckmäßigen Ansichten erstellen: vorn, Seite, hinten und Dreiviertel,
  ergänzt um Gesichtsdetails, typische Mimik und wichtige Gegenstände. Ansichten
  müssen dieselbe Figur zeigen; keine beliebige Sammlung ähnlicher Personen.
- Perspektiven, Anzahl von Gliedmaßen, Kleidung und Wiedererkennbarkeit prüfen.
  Aussehen bestätigen lassen, wenn keine bereits verbindliche Vorlage vorliegt.
- Freigegebene Version speichern. Bei neuen Bildern das Sheet und erlaubte
  Einzelreferenzen benutzen. Ein LoRA-Prompt ohne geladenen Adapter gilt nicht
  als Nutzung des LoRAs.

Das Sheet dient der Abstimmung. Für das Training saubere hochauflösende
Einzelbilder mit sinnvoller Varianz und passenden Captions vorbereiten. Nicht
ein einziges Sheet mehrfach zerschneiden und damit vermeintlich unterschiedliche
Trainingsdaten behaupten. Identität, Outfit und Stil bewusst auseinanderhalten;
keine widersprüchlichen Varianten, verdeckte Gesichter, Duplikate oder Wasserzeichen
ungeprüft übernehmen. Synthetische Trainingsbilder auf dieselbe Figur prüfen.

## Vorhandenes LoRA prüfen oder ein neues trainieren

**Vorhanden:** Pfad/Modell-ID, Herkunft, Lizenz, Basismodell und Revision,
Triggerwörter sowie empfohlene Stärke ermitteln. Quelle nicht überschreiben.
Unbekannte Pickle-/Checkpoint-Dateien nicht als Programm laden; sichere Formate
wie Safetensors bevorzugen und keinen fremden Trainingscode ungeprüft ausführen.
Die Endung oder SHA-256 allein beweist weder Herkunft noch Bildqualität.

**Neu:** Nach bewusster Werkzeug-, Daten- und Kostenwahl den passenden Trainer
bereitstellen. Größere Modell-Downloads oder globale Installationen separat
beauftragen lassen, soweit sie nicht bereits ausdrücklich abgedeckt sind.
Trainingsdatensatz, Captions, Basisrevision, Trainer-Version, Seed,
Auflösung, Lernrate, Rank/Alpha und Schritte begründet konfigurieren. Parameter
nach Modell, Hardware und Material wählen, keine universelle Trainingsdauer oder
Qualität versprechen. Trainingsauftrag und tatsächlichen Abschluss dokumentieren.
Keine automatische öffentliche Modellveröffentlichung, keine ungefragten Hub-
Uploads und keine Bild-/Prompt-Übertragung an externe Experiment-Tracker.
Dokumentationsbeispiele mit `--push_to_hub` oder Cloud-Tracking nicht blind kopieren.

Vor der Freigabe mit dem kompatiblen Zielmodell reale Testbilder aus mehreren
Blickwinkeln, einer Nahaufnahme und einer neuen Pose/Szene erzeugen. Gesicht,
Anatomie, Accessoires und Outfit gegen das Sheet vergleichen. Das ist eine
Identitätskontrolle, kein bloßer Nachweis, dass eine Datei existiert. Tatsächlich
verwendete Adapter, Stärke, Trigger, Seed und Modellrevision festhalten.

## Dateien, Status und Übergabe

Im jeweiligen privaten Filmprojekt beispielsweise:

```text
characters/figurenname/
  CHARACTER.md
  character-sheet-v001.png
  character.json
  training/                 freigegebener Datensatz und Captions
  lora/                     echte Gewichte und Modellinformationen
  validation/               tatsächlich erzeugte und angesehene Testbilder
```

Ein vom Benutzer angegebener vorhandener LoRA-Pfad kann außerhalb dieses Ordners
liegen und wird standardmäßig nur gelesen. Falls eine Kopie nötig ist, nur im
beauftragten Projekt anlegen und Herkunft/Prüfsumme festhalten. Bei NAS-Projekten
gelten die bestehenden Regeln für lokale Arbeit und geprüften Rücktransfer.
Keine Gewichte oder privaten Charakterbilder automatisch in öffentliche
Repositories aufnehmen. Projektbezogene Aufbewahrung und erlaubte Weitergabe
festhalten; keine automatischen Löschungen privater Trainingsdaten.

Die [neutrale Statusvorlage](../../skills/mgd-motion-graphics-video/assets/character-template.json) kann nach
`character.json` kopiert und mit echten Informationen gefüllt werden. Der
Assistent hält Sheet und LoRA getrennt fest: `required`, `existing_candidate`,
`in_progress`, `ready`, `blocked` oder `deferred_by_user`. Für ein LoRA zusätzlich
festhalten, ob es neu trainiert oder wiederverwendet wurde. `ready` erst nach
vorliegender echter Datei bzw. vereinbartem nachweisbaren Modellzugang und
geprüften Testbildern; keine leere `.safetensors`-Datei, kein ausgedachtes
Trainingsprotokoll und kein „erfolgreich“ aus einem gestarteten Job ableiten.

Lieferung: Sheet, Steckbrief, echtes LoRA bzw. vereinbarter Modellzugang,
Basis-/Triggerinformationen, Trainings- oder Herkunftsnachweis, Prüfbilder,
Kosten-/Anbieterübersicht und die damit erzeugten Filmquellen. Offene Bestandteile
klar benennen. Ohne Abschluss oder bewusste Benutzerabweichung ist der
Charakter-Workflow nicht vollständig, auch wenn bereits eine MP4 existiert.

## Datenverarbeitung transparent erklären

Lokales Rendern, lokale Bildgenerierung und lokale Assistentenverarbeitung sind
verschiedene Dinge. Ein Cloud-Assistent verarbeitet auch die ihm per Werkzeug
gezeigten Quelltexte und Bilder in seinem Kontext. „Die Datei liegt auf dem NAS“
bedeutet daher nicht, dass ihre gelesenen Inhalte offline bleiben. Bei echter
Offline-Vorgabe keinen Quellinhalt an Cloud-Modelle übergeben; die Grenze benennen
und einen vollständig lokalen Weg abstimmen.

Nur benötigte, freigegebene Aussehensinformationen übertragen, keine kompletten
Manuskripte oder Kanongeheimnisse als Trainingsprompt. Vor Cloud-Jobs den benannten
Dienst, Zweck, erlaubte Dateien und Kostenrahmen festhalten. Lokale Downloads,
Telemetrie, Cloud-Backends und Experiment-Tracker separat prüfen. Keine Daten-
oder Gebührenfreiheit aus dem bloßen Vorhandensein eines Plugins ableiten.

Primärquelle für den technischen Unterschied zwischen Referenz und trainierten
Adaptergewichten: [Diffusers: LoRA-Training](https://huggingface.co/docs/diffusers/training/lora).
Konkrete Trainer und Modellfähigkeiten zum Produktionszeitpunkt erneut prüfen.
