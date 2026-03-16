# Methodik — Datenstück #9: Erst die Hände, dann die Köpfe.

## Fragestellung

Wie hat sich die prognostizierte KI-Bedrohung am Arbeitsmarkt zwischen 2013 und 2026 verschoben? Welche Berufsgruppen sind heute exponiert — und stimmen die großen Prognosen mit der Realität überein?

## Datenquellen

### Primärquellen

1. **Frey & Osborne (2013/2017)** — "The Future of Employment: How Susceptible Are Jobs to Computerisation?"
   - Oxford Martin Programme on Technology and Employment
   - 702 Berufe analysiert, Automatisierungswahrscheinlichkeit 0–1
   - Veröffentlicht als Working Paper 2013, Journal-Publikation in Technological Forecasting and Social Change, 114, 254–280 (2017)

2. **IMF (Januar 2024)** — "AI Will Transform the Global Economy" (Georgieva)
   - KI-Exposition nach Ländergruppe: 60% fortgeschrittene, 40% Schwellenländer, 26% einkommensschwache Länder
   - AI Preparedness Index

3. **ILO (August 2023)** — "Generative AI and Jobs" (Gmyrek, Berg, Bescond)
   - Büroarbeit: 24% hochexponiert, >50% mittel exponiert
   - Frauen doppelt so stark betroffen wie Männer

4. **IAB / Dengler & Matthes (laufend seit 2013, aktualisiert 2024)** — Substituierbarkeitspotenziale von Berufen
   - IAB-Kurzbericht 9/2024
   - Daten für 2013, 2016, 2019, 2022 nach Anforderungsniveau (Helfer, Fachkraft, Spezialist, Experte)

5. **NBER / Brynjolfsson, Li & Raymond (2023)** — "Generative AI at Work", Working Paper 31161
   - 5.179 Kundensupport-Agenten, +14% Durchschnitt, +34% bei Anfängern

6. **NBER / Korinek & Suh (2024)** — "Scenarios for the Transition to AGI", Working Paper 32966
   - 40% GenAI-Nutzung, 1,4% Zeitersparnis, keine Massenentlassungen

7. **OpenAI/UPenn / Eloundou et al. (2023)** — "GPTs are GPTs"
   - 80% der US-Arbeitnehmer mit mindestens 10% betroffenen Aufgaben

8. **Goldman Sachs (März 2023)** — Briggs & Kodnani
   - 300 Mio. Jobs weltweit potenziell betroffen, Automatisierbarkeit nach Branche

9. **WEF Future of Jobs Report 2025** (Januar 2025)
   - +170 Mio. neue Jobs, –92 Mio. wegfallend = +78 Mio. netto bis 2030

10. **Brookings Institution (2019)** — "What jobs are affected by AI?"
    - Hochschulabsolventen 5x höhere KI-Exposition als Highschool-Absolventen

### Sekundärquellen

- OECD Employment Outlook 2023 — KI und Arbeitsmarkt
- OECD (2016, Arntz/Gregory/Zierahn) — Korrektur Frey/Osborne auf 9% hohes Risiko
- Pew Research Center (2023) — "Which U.S. Workers Are More Exposed to AI?"
- Accenture (2024) — GenAI-Studie, 44% Arbeitsstunden im Scope
- McKinsey Global Institute (2023) — Generative AI and the Future of Work in America
- Felten, Raj & Seamans (2021) — AI Occupational Exposure Index (AIOE)
- Stanford HAI AI Index Report 2025

## Datenaufbereitung

### Frey/Osborne Top-10 (Sektion 1)
- Direkt aus dem Paper, Tabelle A.1 (Appendix), Automatisierungswahrscheinlichkeit absteigend
- Deutsche Berufsbezeichnungen sinngemäß übersetzt (z.B. "Title Examiner" → "Versicherungsprüfer")

### Umkehrungs-Chart (Sektion 2)
- 2013-Werte: Abgeleitet aus Frey/Osborne Risikokategorien (>70%, 30–70%, <30%)
- 2024-Werte: Zusammengeführt aus Felten/AIOE-Index, OpenAI/UPenn-Studie und Brookings-Daten
- Die Exposition ist auf einer Skala 0–100 normalisiert, wobei 100 = höchste Exposition bedeutet
- **Wichtig:** Die Werte sind vergleichende Darstellungen, keine direkten Prozentwerte einer einzelnen Studie

### Ländervergleich (Sektion 3)
- IMF-Werte für Ländergruppen (60/40/26) direkt übernommen
- Einzelländer-Werte interpoliert aus IMF AI Preparedness Index + OECD 2023 + Goldman Sachs 2023
- Readiness-Ranking ist die Position im IMF AI Preparedness Index (gerundet)

### IAB-Daten Deutschland (Sektion 4)
- Substituierbarkeitspotenziale direkt aus Dengler & Matthes, IAB-Kurzbericht
- "Anteil der Beschäftigten in Berufen mit hohem Substituierbarkeitspotenzial (>70%)"
- Aufschlüsselung nach Anforderungsniveau: Helfer, Fachkraft, Spezialist, Experte
- Berufsfelder-Ranking für 2022 ebenfalls direkt aus IAB-Daten

### Alters-Paradox (Sektion 5)
- KI-Nutzung: Aggregiert aus diversen Surveys 2024–2025 (Microsoft Work Trend Index, Pew, Eurostat)
- KI-Exposition: Abgeleitet aus Brookings/Felten-Index + OECD 2023 nach Altersgruppen
- NBER +34% für Anfänger direkt aus Brynjolfsson et al. (2023)

### Realitäts-Check (Sektion 6)
- Korinek & Suh (2024): 40% GenAI-Nutzung, 1,4% Zeitersparnis — direkte Übernahme
- Konkrete Signale (Chegg, Stack Overflow etc.) aus Nachrichtenquellen und Geschäftsberichten
- WEF-Nettobilanz direkt aus Future of Jobs Report 2025

## Einschränkungen

1. **Studienvergleichbarkeit:** Die Studien verwenden unterschiedliche Methoden (Berufe vs. Aufgaben, Exposition vs. Automatisierung). Direkte Vergleiche sind Annäherungen.
2. **Zeitliche Lücken:** Die IAB-Daten enden 2022, die GenKI-Welle ab ChatGPT (Nov 2022) ist nur teilweise erfasst.
3. **Prognose vs. Realität:** Alle Zukunftsprognosen sind Modellrechnungen. Die 47% von Frey/Osborne waren ein "over the next decade or two"-Szenario, kein Soforteffekt.
4. **Alters-Daten:** KI-Nutzungsraten nach Generation stammen aus verschiedenen Surveys mit unterschiedlichen Methoden. Die Werte sind Richtwerte, keine exakten Vergleichsdaten.
5. **Länderdaten:** Einzelland-Expositionswerte sind teilweise interpoliert, da nicht alle Studien dieselben Länder abdecken.

## Reproduzierbarkeit

Alle Rohdaten und Quellen sind in `data.json` strukturiert hinterlegt. Die Visualisierungen werden clientseitig mit ECharts 5 aus dieser JSON-Datei generiert. Der vollständige Code ist im GitHub-Repository einsehbar.

---

Kontakt bei Fragen oder Korrekturen: ich@der-koerting.de
