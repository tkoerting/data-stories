# Methodik — Nicht fauler. Führungsloser.

**Datenstück #3** | Datenstand: März 2026 | Autor: Thomas Körting

---

## Quellen

| Datenpunkt | Quelle | URL | Abrufdatum |
|-----------|--------|-----|-----------|
| Arbeitsstunden pro Land | OECD Employment Outlook 2024 | https://data.oecd.org/emp/hours-worked.htm | März 2026 |
| Produktivität pro Stunde | OECD Productivity Statistics | https://data.oecd.org/lprdty/gdp-per-hour-worked.htm | März 2026 |
| Pencavel-Kurve | John Pencavel, Stanford — "The Productivity of Working Hours", IZA DP No. 8129 (2014) | https://docs.iza.org/dp8129.pdf | März 2026 |
| Stundenproduktivität DE | Destatis — Volkswirtschaftliche Gesamtrechnungen | https://www.destatis.de/DE/Themen/Wirtschaft/Volkswirtschaftliche-Gesamtrechnungen-Inlandsprodukt/_inhalt.html | März 2026 |
| BIP-Wachstum | ifo Institut / Destatis | https://www.ifo.de/ | März 2026 |
| Krankheitstage | DAK Gesundheitsreport 2025 / TK Gesundheitsreport | https://www.dak.de/dak/unternehmen/reporte-forschung/gesundheitsreport-2025_142376 | März 2026 |
| eAU-Einführung | GKV-Spitzenverband | https://www.gkv-spitzenverband.de/ | März 2026 |
| Lohnfortzahlung | Institut der deutschen Wirtschaft (IW) | https://www.iwkoeln.de/ | März 2026 |
| Mitarbeiter-Engagement | Gallup State of the Global Workplace 2024 | https://www.gallup.com/workplace/349484/state-of-the-global-workplace.aspx | März 2026 |
| KI-Produktivitätsstudie | Harvard Business School / BCG — "Navigating the Jagged Technological Frontier" (2023) | https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7571.pdf | März 2026 |
| Fachkräftemangel | DIHK Fachkräftereport 2024 | https://www.dihk.de/ | März 2026 |
| Boomer-Renteneintritt | Destatis Bevölkerungsvorausberechnung | https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/_inhalt.html | März 2026 |
| Dänemark Flexicurity | OECD / Danmarks Statistik / Eurofound | https://www.eurofound.europa.eu/ | März 2026 |

## Berechnungen

### OECD-Vergleich
- Arbeitsstunden: Tatsächlich geleistete Jahresarbeitsstunden pro Erwerbstätigen (OECD-Definition)
- Produktivität: GDP per hour worked in USD (aktuelle Kaufkraftparitäten)
- Keine eigene Berechnung — Werte direkt aus OECD.Stat übernommen

### Pencavel-Kurve
- Originaldaten basieren auf britischen Munitionsarbeiterinnen im 1. Weltkrieg
- Pencavel hat die Produktivitäts-Output-Kurve aus historischen Daten rekonstruiert
- Die Kurve in `data.json` ist eine indexierte Darstellung (Peak = 100 bei 48h)
- Die Zwischenwerte sind interpoliert auf Basis der publizierten Kurve aus dem Paper
- **Kernaussage direkt aus dem Paper:** "Output at 70 hours differs little from output at 56 hours"

### Stundenproduktivität Deutschland
```
veraenderung_pct = ((produktivitaet_jahr_n / produktivitaet_jahr_n-1) - 1) × 100
```
Werte direkt aus Destatis VGR (preisbereinigt, verkettet)

### Krankheitstage & eAU-Effekt
- Durchschnittliche Krankheitstage: DAK-Versicherte (ca. 5,5 Mio.)
- **eAU-Erklärung:** Vor 2023 mussten Arbeitnehmer die Arbeitsunfähigkeitsbescheinigung (AU) selbst beim Arbeitgeber einreichen. Viele kurze Krankmeldungen (1-3 Tage) wurden nie eingereicht. Seit 01.01.2023 meldet der Arzt elektronisch direkt an die Krankenkasse → vorher unsichtbare Kurzkrankmeldungen tauchen erstmals in der Statistik auf
- Der Sprung 2022→2023→2024 ist daher teilweise ein **statistischer Artefakt**, nicht nur ein realer Anstieg
- Lohnfortzahlung 82 Mrd €: IW-Schätzung für 2024, basierend auf durchschnittlichen Bruttolöhnen × Krankheitstage

### Gallup Engagement
- Definitionen nach Gallup Q12-Methodik:
  - **Engaged** (12%): Emotional gebunden, intrinsisch motiviert
  - **Not Engaged** (43%): Dienst nach Vorschrift
  - **Actively Disengaged** (45%): Innerlich gekündigt, potenziell destruktiv
- 167 Mrd € Produktivitätsverlust: Gallup-eigene Hochrechnung basierend auf Fehlzeiten, Fluktuation, Qualitätsmängeln
- Repräsentative Befragung, n ≈ 1.500 Arbeitnehmer in Deutschland

### Harvard/BCG KI-Studie
- 758 BCG-Consultants, randomisiert in Gruppen mit/ohne GPT-4-Zugang
- +12% mehr Aufgaben, +25% schneller, +40% höhere Qualität: Differenz zwischen KI-Gruppe und Kontrollgruppe
- +43% Verbesserung bei Below-Average: Performancegewinn der unteren 50% mit KI vs. ohne
- Wichtig: Die Studie zeigt auch eine "Jagged Frontier" — bei bestimmten Aufgabentypen war KI-Nutzung kontraproduktiv

### 12,9 Mio. Boomer
```
boomer_generation = Geburtsjahrgänge 1954–1968
renteneintritt_bis_2036 = ca. 12,9 Mio. Personen
```
Basierend auf Destatis Bevölkerungsvorausberechnung (14. koordinierte), mittlere Variante

## Einschränkungen

- OECD-Produktivität ist ein Makro-Indikator — sagt nichts über einzelne Branchen
- Die Pencavel-Kurve basiert auf historischen Daten (Munitionsproduktion 1914-1918) — Übertragbarkeit auf Wissensarbeit ist diskutabel, aber die Grundtendenz wurde in modernen Studien bestätigt
- Gallup Q12 ist ein proprietärer Fragebogen — Methodik nicht vollständig offengelegt
- Harvard/BCG-Studie: Nur Consultants getestet, nur GPT-4, nur bestimmte Aufgabentypen
- eAU-Effekt: Exakte Größe des statistischen Artefakts ist nicht quantifiziert — Schätzungen liegen bei 2-4 Tagen des Anstiegs

## Datenverarbeitung

Alle Werte manuell aus den Primärquellen extrahiert. OECD-Daten über OECD.Stat (CSV-Export). Pencavel-Kurve aus dem Originalpaper digitalisiert und auf Index 100 normiert. Gallup- und Harvard/BCG-Daten aus den jeweiligen Studienberichten. Keine algorithmische Transformation oder Modellierung.
