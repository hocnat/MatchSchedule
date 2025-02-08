# MatchSchedule

Helferlein für Spielplangestalter eines Handballvereins

[![License](https://img.shields.io/github/license/hocnat/MatchSchedule)](https://github.com/hocnat/MatchSchedule/blob/main/LICENSE)

## Motivation

Die Idee hinter diesem Projekt ist es den Spielplangestaltern eines Handballvereins Tools zur Verfügung zu stellen, die manuelle Aufwände minimieren.
Außerdem bietet sich durch dieses Projekt die Gelegenheit ein wenig mit [ChatGPT](https://chatgpt.com/) und [Python](https://www.python.org/) zu experimentieren.

## Features

### Kennzifferoptimierung

Die Kennzifferoptimierung ermittelt für zwei Mannschaften die optimalen Kennziffern, sodass diese beiden Mannschaften möglichst viele gemeinsame Heimspieltage haben:

```shell
Die 5 besten Kennziffern-Kombinationen mit den meisten gemeinsamen Heimspieltagen:

Kennziffer 5 (Mannschaft 1) & Kennziffer 10 (Mannschaft 2) → 8 gemeinsame Heimspieltage
  Gemeinsame Heimspieltage: 14./15.09.2024, 28./29.09.2024, 02./03.11.2024, 16./17.11.2024, 14./15.12.2024, 15./16.02.2025, 15./16.03.2025, 05./06.04.2025

Kennziffer 7 (Mannschaft 1) & Kennziffer 10 (Mannschaft 2) → 8 gemeinsame Heimspieltage
  Gemeinsame Heimspieltage: 14./15.09.2024, 28./29.09.2024, 02./03.11.2024, 16./17.11.2024, 14./15.12.2024, 01./02.02.2025, 15./16.03.2025, 05./06.04.2025

Kennziffer 9 (Mannschaft 1) & Kennziffer 10 (Mannschaft 2) → 8 gemeinsame Heimspieltage
  Gemeinsame Heimspieltage: 14./15.09.2024, 02./03.11.2024, 16./17.11.2024, 14./15.12.2024, 18./19.01.2025, 01./02.02.2025, 15./16.03.2025, 05./06.04.2025

Kennziffer 11 (Mannschaft 1) & Kennziffer 10 (Mannschaft 2) → 8 gemeinsame Heimspieltage
  Gemeinsame Heimspieltage: 14./15.09.2024, 28./29.09.2024, 02./03.11.2024, 16./17.11.2024, 14./15.12.2024, 15./16.02.2025, 15./16.03.2025, 05./06.04.2025

Kennziffer 5 (Mannschaft 1) & Kennziffer 8 (Mannschaft 2) → 7 gemeinsame Heimspieltage
  Gemeinsame Heimspieltage: 14./15.09.2024, 28./29.09.2024, 02./03.11.2024, 14./15.12.2024, 15./16.02.2025, 15./16.03.2025, 05./06.04.2025
```

### ?

...

## Verwendung

## Installation von Python

Um die Tools verwenden zu können, wird Python benötigt.
Python kann von der [offiziellen Website](https://www.python.org/downloads/) heruntergeladen werden.
Bei der Installaltion wählt man am besten die Option zum Hinzufügen von Python zum PATH.

Anschließend müssen noch zwei Pakete installiert werden:

```shell
pip install pandas pyyaml
```

### Klonen des Repositories

Dieses Repository kann folgendermaßen geklont werden.

```shell
git clone https://github.com/hocnat/MatchSchedule.git
```

### Ausführung

Das Tool zur Ermittlung optimaler Kennziffern für zwei Mannschaften wird mit folgendem Befehl ausgeführt:

```shell
python .\find_best_numbers.py --seasonCalendarTeam1 SEASONCALENDARTEAM1 --rasterTeam1 RASTERTEAM1 [--fixedNumberTeam1 FIXEDNUMBERTEAM1] --seasonCalendarTeam2 SEASONCALENDARTEAM2 --rasterTeam2 RASTERTEAM2 [--fixedNumberTeam2 FIXEDNUMBERTEAM2] [--results RESULTS]
```

#### Parameter

* `--seasonCalendarTeam1`: CSV-Datei mit Saisonkalender der 1. Mannschaft
* `--rasterTeam1`: YAML-Datei mit Raster der 1. Mannschaft
* `--fixedNumberTeam1`: Feste Kennziffer für 1. Mannschaft (optional)
* `--seasonCalendarTeam2`: CSV-Datei mit Saisonkalender der 2. Mannschaft
* `--rasterTeam2`: YAML-Datei mit Raster der 2. Mannschaft
* `--fixedNumberTeam2`: Feste Kennziffer für 2. Mannschaft (optional)
* `--results`: Anzahl der auszugebenden Ergebnisse (optional, Standardwert: 3)

#### Saisonkalender

Die Saisonkalender müssen in folgendem CSV-Format vorliegen:

```csv
Datum,Spieltag
DD./DD.MM.YYYY,1
...
DD./DD.MM.YYYY,n
```

Beispiel:

```csv
Datum,Spieltag
14./15.09.2024,1
21./22.09.2024,2
...
```

> Oftmals werden Saisonkalender in Formaten zur Verfügung gestellt, die schlecht maschinenlesbar sind. Die Saisonkalender des HVS und der Regionalliga Südwest ließen sich mit ein paar einfachen Prompts durch ChatGPT in das benötigte CSV-Format umwandeln.

#### Raster

Die Raster müssen in folgendem YAML-Format vorliegen:

```yml
Kennziffer_1: kommaseparierte Liste von Heimspieltagen
...
Kennziffer_n: kommaseparierte Liste von Heimspieltagen
```

Beispiel:

```yml
1: 1,3,5,7,9,11,13,15,17,19,21
2: 2,3,5,7,9,11,12,15,17,19,21
...
```

#### Beispiel: Freie Kennzifferwahl für beide Mannschaften

Wenn für beide Mannschaften noch keine Kennziffern festgelegt wurden, können die 3 besten Kombinationen von Kennziffern wie folgt ermittelt werden:

```shell
python .\find_best_numbers.py --seasonCalendarTeam1 .\Saisonkalender\RegionalligaSüdwestFrauen2425.csv --rasterTeam1 .\Raster\12erRaster.yaml --seasonCalendarTeam2 .\Saisonkalender\OberligaSaarMänner2425.csv --rasterTeam2 .\Raster\12erRaster.yaml
```

#### Beispiel: Bereits festgelegte Kennziffer einer Mannschaft

Wenn für die 1. Mannschaft bereits die Kennziffer `2` festgelegt wurde, können die 3 besten Kennziffern für die 2. Mannschaft wie folgt ermittelt werden:

```shell
python .\find_best_numbers.py --seasonCalendarTeam1 .\Saisonkalender\RegionalligaSüdwestFrauen2425.csv --rasterTeam1 .\Raster\12erRaster.yaml --fixedNumberTeam1 2 --seasonCalendarTeam2 .\Saisonkalender\OberligaSaarMänner2425.csv --rasterTeam2 .\Raster\12erRaster.yaml
```

#### Beispiel: Ausgabe von mehr als 3 Kennzifferkombinationen

Die 5 besten Kennzifferkombinationen können wie folgt ermittelt werden:

```shell
python .\find_best_numbers.py --seasonCalendarTeam1 .\Saisonkalender\RegionalligaSüdwestFrauen2425.csv --rasterTeam1 .\Raster\12erRaster.yaml --seasonCalendarTeam2 .\Saisonkalender\OberligaSaarMänner2425.csv --rasterTeam2 .\Raster\12erRaster.yaml --results 5
```

## Verwendete Tools

* [ChatGPT](https://chatgpt.com/) - OpenAI
* [Python](https://www.python.org/) - Python Software Foundation - Python Software Foundation License

## License

[MIT License](https://github.com/hocnat/MatchSchedule/blob/main/LICENSE) Copyright 2025 © [hocnat](https://github.com/hocnat)