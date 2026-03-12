# Methodik — Wie man seine Stadt schön träumt

**Datenstück #2** | Datenstand: März 2026 | Autor: Thomas Körting

---

## Quellen

| Datenpunkt | Quelle | URL | Abrufdatum |
|-----------|--------|-----|-----------|
| Stadtdaten Fürth | Stadt Fürth / Bayerisches Landesamt für Statistik | https://www.statistik.bayern.de/ | März 2026 |
| Pendlerströme | Bundesagentur für Arbeit — Pendleratlas | https://statistik.arbeitsagentur.de/DE/Navigation/Statistiken/Interaktive-Statistiken/Pendleratlas/Pendleratlas-Nav.html | März 2026 |
| Pro-Kopf-Verschuldung | Stadt Fürth Haushaltsbericht / Bayerischer Rechnungshof | https://www.fuerth.de/ | März 2026 |
| Open Data Datensätze | GovData.de + jeweilige kommunale Portale | https://www.govdata.de/ | März 2026 |
| Open Data Moers | Offene Daten Moers / OKNRW | https://www.offenesdatenportal.de/organization/moers | März 2026 |
| Smart City Index | IMD Smart City Index 2024 | https://www.imd.org/smart-city-observatory/home/ | März 2026 |
| Bitkom Smart City | Bitkom Smart City Index 2024 | https://www.bitkom.org/Smart-City-Index | März 2026 |
| EU Open Data Maturity | EU Open Data Maturity Report 2024 | https://data.europa.eu/en/publications/open-data-maturity | März 2026 |

## Berechnungen

### Datasets pro 100.000 Einwohner
```
datasets_pro_100k = (anzahl_datasets / einwohner) × 100.000
```
Beispiel Moers: `(800 / 103.000) × 100.000 = 777`
Beispiel Fürth: `(0 / 132.600) × 100.000 = 0`

### Auspendlerquote
```
auspendlerquote = (auspendler / sozialversicherungspflichtig_beschaeftigte_wohnort) × 100
```
Quelle: Bundesagentur für Arbeit, Stichtag 30.06.2024

### Pro-Kopf-Verschuldung
```
pro_kopf = schuldenstand_kernhaushalt / einwohner
```
Zeitreihe 2005–2024, jeweils Jahresende. Bayern-Durchschnitt (1.050 €) aus Bayerischem Rechnungshof.

### Schuldenabbau seit 2005
```
abbau_prozent = ((2005_wert - 2024_wert) / 2005_wert) × 100
= ((2.800 - 1.174) / 2.800) × 100 = 58%
```

### Open Data Readiness Score
Eigene Bewertungsmethodik mit 6 Dimensionen, max. 100 Punkte:

| Dimension | Max | Methode |
|-----------|-----|---------|
| Datensätze (Anzahl) | 20 | Logarithmische Skala, 0 Datasets = 0 Punkte |
| Maschinenlesbarkeit | 15 | Anteil CSV/JSON/API vs. PDF/HTML |
| Echtzeit-APIs | 15 | Verfügbarkeit von Live-Daten-Schnittstellen |
| Bürgerbeteiligung | 20 | Feedback-Mechanismen, Hackathons, Community |
| Verwaltung digital | 15 | Online-Services, OZG-Umsetzungsgrad |
| Strategie & Governance | 15 | Existenz einer Open-Data-Strategie, CDO, Budget |

**Wichtig:** Der Readiness Score ist eine eigene Einschätzung, kein offizieller Index. Die Gewichtung orientiert sich an der EU Open Data Maturity Methodik, ist aber vereinfacht und auf kommunale Ebene angepasst. Best-Practice-Werte basieren auf den jeweils besten Kommunen in der jeweiligen Dimension.

## Einschränkungen

- Open Data Datensatz-Zahlen schwanken: Portale ändern sich, Datasets werden zusammengelegt oder aufgeteilt
- Pendlerdaten sind Stichtagswerte (30.06.), unterjährige Schwankungen nicht abgebildet
- Der Readiness Score ist subjektiv — andere Gewichtungen führen zu anderen Ergebnissen
- Fürth hat einzelne Datensätze über das Bayerische Open Data Portal, aber kein eigenes kommunales Portal
- Schulden: Nur Kernhaushalt, keine Eigenbetriebe/Beteiligungen

## Datenverarbeitung

Alle Werte manuell recherchiert und in `data.json` strukturiert. Keine automatisierte Datenerhebung. Wo Zeitreihen aus unterschiedlichen Quellen stammen, ist die Quelle im JSON pro Sektion angegeben.
