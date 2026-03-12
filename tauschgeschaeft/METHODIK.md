# Methodik — Es ist ein Tauschgeschäft

**Datenstück #4** | Datenstand: März 2026 | Autor: Thomas Körting

---

## Quellen

| Datenpunkt | Quelle | URL | Abrufdatum |
|-----------|--------|-----|-----------|
| Nettovermögen nach Alter | Deutsche Bundesbank — Panel on Household Finances (PHF) 2023 | https://www.bundesbank.de/de/bundesbank/forschung/panel-on-household-finances | März 2026 |
| Gini-Koeffizient Vermögen | IW Köln — Vermögensverteilung 2025 | https://www.iwkoeln.de/studien/judith-niehues-maximilian-stockhausen-ein-vermoegensvergleich-nach-altersgruppen.html | März 2026 |
| Wohneigentumsquote | Destatis / SOEP (Sozio-oekonomisches Panel) | https://www.diw.de/soep | März 2026 |
| Hochschulreife-Quote | Destatis — Bildungsstand der Bevölkerung | https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bildung-Forschung-Kultur/Bildungsstand/_inhalt.html | März 2026 |
| Ausbildungsquote | BIBB — Bundesinstitut für Berufsbildung | https://www.bibb.de/de/214719.php | März 2026 |
| Azubi-Ratio (historisch) | Autorengruppe Bildungsberichterstattung / Bildungsbericht 2024 | https://www.bildungsbericht.de/ | März 2026 |
| Gen Z & Millennial Survey | Deloitte Gen Z & Millennial Survey 2025 (Deutschland) | https://www.deloitte.com/de/de/services/consulting/research/genz-millennial-survey.html | März 2026 |
| Depressionstage | DAK Psychreport 2025 | https://www.dak.de/dak/unternehmen/reporte-forschung/psychreport-2025_91766 | März 2026 |
| Krankenstand Gen Z | DAK Gesundheitsreport 2025 | https://www.dak.de/dak/unternehmen/reporte-forschung/gesundheitsreport-2025_142376 | März 2026 |
| Jugend-Hospitalisierung | DAK Kinder- und Jugendreport 2023 | https://www.dak.de/dak/unternehmen/reporte-forschung/dak-kinder-und-jugendreport-2023_45524 | März 2026 |
| Nachrichtenquellen | Reuters Institute Digital News Report 2024 (Deutschland) | https://leibniz-hbi.de/hbi-publications/reuters-institute-digital-news-report-2024-ergebnisse-fuer-deutschland/ | März 2026 |
| Social Media Nutzung | ARD/ZDF-Medienstudie 2024 | https://www.ard-zdf-onlinestudie.de/ | März 2026 |
| Reallöhne | Destatis — Reallöhne und Nettoverdienste | https://www.destatis.de/DE/Themen/Arbeit/Verdienste/Realloehne-Nettoverdienste/_inhalt.html | März 2026 |
| Wahlbeteiligung | Bundeswahlleiter — Repräsentative Wahlstatistik BTW 2025 | https://www.bundeswahlleiterin.de/info/presse/mitteilungen/bundestagswahl-2025/30_25_ergebnisse-rws.html | März 2026 |

## Berechnungen

### Vermögenslücke (14x)
```
gap_factor = median_55_64 / median_unter_35
= 241.100 / 17.300
= 13,9 ≈ 14x
```
Medianwerte (nicht Durchschnitt!) aus PHF 2023. Der Median ist robuster gegen Ausreißer (einzelne Superreiche verzerren den Durchschnitt).

### Gini-Koeffizient
- 0 = perfekte Gleichheit, 1 = maximale Ungleichheit
- Unter 35: 0,83 → extreme Spreizung (einige erben viel, viele haben fast nichts)
- 55-64: 0,63 → immer noch hoch, aber deutlich gleichmäßiger
- Quelle: IW Köln, basierend auf PHF-Mikrodaten

### Wohneigentumsquote
- Anteil der Haushalte mit Wohneigentum (Selbstnutzer)
- "Junge Eigentümer = 15% aller Eigentümer" berechnet als:
```
anteil = (eigentümer_unter_45 / eigentümer_gesamt) × 100
```
- Rückgang von 31% (2000) auf 15% (2024) zeigt: Die Leiter wurde hochgezogen

### Bildungsinflation — Azubi-Ratio
```
azubi_ratio = anzahl_auszubildende / (anzahl_studierende / 10)
```
Beispiel 1950: `971.000 Azubis / (129.000 Studenten / 10) = 75,5 Azubis pro 10 Studenten`
Beispiel 2021: `1.300.000 Azubis / (2.900.000 Studenten / 10) = 4,3 Azubis pro 10 Studenten`

### Hochschulreife-Quote
- Anteil der Schulabgänger mit allgemeiner oder fachgebundener Hochschulreife
- Historische Werte (1950-1990) aus Bildungsbericht, neuere aus Destatis Fachserie 11

### Gen Z Priorities (Deloitte)
- Repräsentative Befragung, Deutschland-Sample
- Gen Z: Geburtsjahrgänge 1995-2005 (bei Deloitte), Millennials: 1983-1994
- Werte in Prozent = "Anteil, die diesen Faktor als wichtig/sehr wichtig bei der Arbeitgeberwahl angeben"
- Mehrfachnennungen möglich → Summe > 100%

### Depression: +50% in einem Jahr
```
anstieg_pct = ((2024_wert - 2023_wert) / 2023_wert) × 100
= ((183 - 122) / 122) × 100 = 50%
```
- Einheit: AU-Tage pro 100 Versicherte mit Diagnose F32/F33 (depressive Episode / rezidivierende Depression)
- DAK-Versicherte, ca. 5,5 Mio. Personen

### Gender Gap Mental Health
- Frauen 233 vs. Männer 140 Depressionstage pro 100 Versicherte
- Mögliche Erklärungen (nicht im Datenstück, aber für Kontext):
  - Frauen suchen häufiger ärztliche Hilfe
  - Unterdiagnostizierung bei Männern
  - Doppelbelastung Care-Arbeit + Beruf

### Wahlbeteiligung Anstieg
```
anstieg_pp = beteiligung_2025 - beteiligung_2021
```
In Prozentpunkten (pp), nicht Prozent. Beispiel 21-24 Jährige: +8,3 Prozentpunkte.

### Reallöhne
```
reallohn_veraenderung = nominallohn_veraenderung - inflation
```
- 1991-2019: +60,7% nominal, -48,4% durch Inflation = +12,3% real über 28 Jahre
- Das sind ca. +0,4% pro Jahr real — deutlich unter Produktivitätswachstum

## Einschränkungen

- **Vermögen:** PHF ist eine Stichprobe (ca. 5.000 Haushalte). Sehr hohe Vermögen sind unterrepräsentiert. Das echte Gap könnte noch größer sein.
- **Wohneigentum:** Regionale Unterschiede enorm (München vs. Sachsen). Bundesdurchschnitt glättet.
- **Bildungsinflation:** "Mehr Akademiker" ist nicht per se schlecht — die Frage ist, ob das Lohnniveau mitgestiegen ist (Antwort: nein).
- **Deloitte Survey:** Selbstauskunft, möglicher Social-Desirability-Bias ("Natürlich will ich D&I").
- **Depression:** DAK-Daten bilden nur gesetzlich Versicherte ab. Privatversicherte (tendenziell höhere Einkommen) fehlen.
- **Nachrichtenquellen:** "Social Media als Nachrichtenquelle" ≠ "Informiert sich nur über Social Media". Viele nutzen mehrere Kanäle.
- **Generationen-Grenzen:** Die Jahrgangsgrenzen sind Konvention, keine wissenschaftliche Kategorie. Menschen nahe der Grenze können sich beiden Gruppen zugehörig fühlen.

## Datenverarbeitung

Alle Werte manuell aus den Primärquellen extrahiert. Keine algorithmische Datenerhebung. Zeitreihen aus Destatis/BIBB als CSV heruntergeladen und auf relevante Jahre gefiltert. Deloitte- und DAK-Daten aus den jeweiligen PDF-Studienberichten. Alle Prozentwerte auf eine Nachkommastelle gerundet.
