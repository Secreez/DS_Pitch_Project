# Regelbuch für Benchmark Test: Docker vs. Manuelle Einrichtung

## Ziel des Benchmarks

Dieser Benchmark zielt darauf ab, die Effizienz und Zeitersparnis des Docker-Setups im Vergleich zur manuellen Einrichtung einer WordPress-Umgebung im kleinen Rahmen zu messen. Wir vergleichen die Dauer der Einrichtung bei verschiedenen Teilnehmern mit unterschiedlichen Kenntnisstufen. Dies würde mir helfen, für den Pitch sowie auch eine Messlatte für die weitere Entwicklung zu haben, gerade in Bezug zur Verständlichkeit und Benutzerfreundlichkeit der Doku.

## Teilnehmer

### Teilnehmer 1 und 2: 
Erfahrene Entwickler im PHP und WordPress Bereich, haben teilweise bereits Erfahrung mit Docker.

### Teilnehmer 3 und 4:
Praktikanten, die noch keine Erfahrung mit Docker und WordPress haben.

### Durchführung

Jeder Teilnehmer führt vier Versuche jeweils durch für:

- Manuelles Setup
- Automatisches Setup mittels Docker

### Szenario:
- Stellt euch vor, ihr möchtet bevor Launch eines Kundenprojekts eine lokale WordPress-Umgebung einrichten, um das Projekt zu testen und zu entwickeln. Jedesmal wenn ein neues Projekt ansteht, müsst ihr eine neue WordPress-Umgebung einrichten...

## Regeln

1. Zeitmessung: Verwendet eine Stoppuhr oder eine andere Zeitmess-App. Startet die Zeitmessung bei Beginn des Setups und stoppt die Zeit, sobald ihr fertig seid. Wichtig ist mir hierbei, dass ihr bitte es in diesem Format dokumentiert:

- `Teilnehmer`: Name des Teilnehmers (Werde ich Zensieren).
- `Versuch`: Gibt an, ob es sich um ein manuelles Setup oder ein Docker-Setup handelt.
- `Startzeit`: Die Zeit, zu der der Teilnehmer mit dem Setup begonnen hat.- `Endzeit`: Die Zeit, zu der der Teilnehmer das Setup abgeschlossen hat.
- `Dauer`: Die Gesamtdauer des Setups (kann berechnet werden als Differenz zwischen Endzeit und Startzeit in Minuten).
- `Datum`: Das Datum, an dem der Versuch durchgeführt wurde.

**Bspw.:**

| Teilnehmer | Versuch | Startzeit | Endzeit | Dauer | Datum |
| --- | --- | --- | --- | --- | --- |
| A | 1 | 10:00 | 10:30 | 00:30 | dd.mm.yyyy |
| A | 2 | 10:00 | 10:30 | 00:30 | dd.mm.yyyy |

- Die Dauer kann entweder manuell oder durch eine Formel in der CSV-Datei oder in einem Tabellenkalkulationsprogramm wie Excel berechnet werden.
- Es ist mir wichtig, dass alle Teilnehmer die Zeitmessung konsistent durchführen, um vergleichbare Ergebnisse zu erhalten.
- Seht zu, dass **ihr apache2 schon vorher installiert habt,** da es sonst zu einer Verzerrung der Ergebnisse kommen kann. Am besten ihr verwendet eine VM oder einen Server wenn einer frei ist (**Verwendet bitte Ubuntu LTS 22.04**). Also wirklich ab dem Punkt anfangen, wo ihr auch mit Docker anfangen würdet.

2. Vorgegebene Aufgaben: Jedes Setup (manuell und Docker) muss folgende Elemente umfassen (beide auf localhost/wordpress):


2.1 Installation von WordPress (`6.4`)
2.2 Installation des Haus eigenen Plugins
2.3 Einrichtung von XDebug (`xdebug-3.1.5`)
2.4 Verbindung zu PHPStorm mit XDebug und PHP (`8.1`)
2.5 Verbindung zu MySQL (`8.0`)
2.6 PHPUnit miteinbauen (`phpunit-9.6.16.phar`)
2.7 (Docker Only) Einrichtung von docker-compose.yml auf (`3.8`)

Ergo: **LAMP Stack**. (Linux, Apache, MySQL, PHP) mit XDebug und PHPUnit wie auch in Production.

3. Unabhängigkeit: Jeder Versuch sollte unabhängig von vorherigen Versuchen durchgeführt werden, um zumindest etwas Bias zu vermeiden.

4. Keine externe Hilfe beim Docker Setup: Außer den bereitgestellten Anleitungen dürfen keine zusätzlichen Ressourcen oder Hilfe verwendet werden. (Dies gilt **nur** für das Docker-Setup, nicht für das manuelle Setup!) Solltet ihr schwierigikeiten oder unverständlichkeit haben. Bitte schreibt es euch auf!

## Hinweise zur Datenerfassung

- Stellt sicher, dass alle Daten akkurat und zeitnah erfasst werden
- Führt eine separate Datei für die Datenerfassung, um die Übersichtlichkeit zu gewährleisten.


## Ethik und Transparenz

- Dieser Benchmark zielt darauf ab, reale Daten zu erfassen. Es ist wichtig, dass alle Teilnehmer ehrlich über ihre Erfahrungen berichten und keine Daten manipuliert werden.
- Die Ergebnisse sollen dazu dienen, eine faire und transparente Vergleichsbasis zu schaffen.

Abgabedeadline: 22.01.2024 !

**Vielen Dank für eure Teilnahme!**
