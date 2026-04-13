# Datenstücke

**Open Data, interaktiv visualisiert. Zu jedem Blogpost die Zahlen dahinter.**

Von [Thomas Körting](https://der-koerting.de) — Der Nerd. Der Spinner. Der, der was draus macht.

**Live:** [opendataminded.de](https://opendataminded.de/)

---

## Was sind Datenstücke?

Datenstücke nehmen ein Thema aus dem [Blog](https://der-koerting.de) und gehen tiefer — mit offenen Daten, interaktiven Charts und allen Quellen. Kein akademisches Paper, kein Dashboard. Eher: Was passiert, wenn jemand Zahlen nimmt, sie dreht, wendet, hinterfragt — und dann eine Geschichte erzählt, die man sonst nicht sieht.

---

## Übersicht

| # | Titel | Thema | Cluster |
|---|-------|-------|---------|
| 15 | [KRIEG(e).](https://opendataminded.de/kriege/) | 61 aktive Konflikte, Medien-Blindspot, Rüstungsprofiteure, DAX-Paradox | Geopolitik |
| 14 | [Prost. Oder auch nicht.](https://opendataminded.de/prost-oder-auch-nicht/) | Kneipensterben, Gen Z, Craft Spirits, Einsamkeit | Gesellschaft |
| 13 | [347 Ergebnisse. Null Erinnerungen.](https://opendataminded.de/347-ergebnisse/) | Hotels, Personalisierungs-Paradox, Guest Journey | Hospitality |
| 12 | [Wenn Maschinen mitreden.](https://opendataminded.de/wenn-maschinen-mitreden/) | KI-Schwärme, Demokratie, 21 Propheten, Quiz | KI |
| 11 | [Zwei Tode, eine Woche.](https://opendataminded.de/zwei-tode/) | Habermas vs. Chuck Norris — in Daten | Kultur |
| 10 | [Algorithmus trifft KI.](https://opendataminded.de/algorithmus-trifft-ki/) | Was 81% verwechseln, was 10% verstehen | KI |
| 9 | [Erst die Hände, dann die Köpfe.](https://opendataminded.de/erst-die-haende/) | KI am Arbeitsmarkt, 60% der Jobs exponiert | KI/Arbeit |
| 8 | [Schneller als du denkst.](https://opendataminded.de/schneller-als-du-denkst/) | Deep Blue zu GPT-4 — Beschleunigung der KI | KI |
| 7 | [Du dumme Gans.](https://opendataminded.de/du-dumme-gans/) | Tier-Schimpfwörter, Neuronen, Jagderfolg, Sprachgeschichte | Sprache/Biologie |
| 6 | [1 Gramm, 23 Millionen](https://opendataminded.de/was-socke-hinterlaesst/) | Hundekot, Bakterien, Bußgelder, Hundesteuer | Umwelt |
| 5 | [Ich hab Corona.](https://opendataminded.de/ich-hab-corona/) | COVID-Normalisierung, Medien, Ländervergleich | Gesundheit |
| 4 | [Es ist ein Tauschgeschäft.](https://opendataminded.de/tauschgeschaeft/) | Generationenvertrag, Vermögen, Mental Health | Gesellschaft |
| 3 | [Nicht fauler. Führungsloser.](https://opendataminded.de/nicht-fauler-fuehrungsloser/) | OECD-Produktivität, Gallup-Engagement | Arbeit |
| 2 | [Wie man seine Stadt schön träumt](https://opendataminded.de/fuerth-wissenschaftsstadt/) | Fürth als Wissenschaftsstadt, Open Data | Stadt |
| 1 | [Was unter der klaren Ostsee liegt](https://opendataminded.de/mikroplastik-ostsee/) | Mikroplastik, Munition, Dorsch-Kollaps | Umwelt |

### Sidekicks & Standalones

| Titel | Thema |
|-------|-------|
| [Dieselben Zahlen. Drei Wahrheiten.](https://opendataminded.de/dieselben-zahlen/) | Wie dieselben Daten je nach Framing drei Geschichten erzählen |

---

## Technik

- **Visualisierung:** [Apache ECharts 5](https://echarts.apache.org/) — interaktiv, responsive, Dark/Light Mode
- **Design:** Slate & Tonic — Instrument Serif, Space Grotesk, JetBrains Mono
- **Fonts:** self-hosted (DSGVO-konform)
- **Tracking:** GA4 mit Cookie-Consent-Banner (nur nach Zustimmung)
- **Hosting:** GitHub Pages (Auto-Deploy bei Push auf main)
- **Kein Framework.** Kein Build-Step. Kein npm. Pures HTML, CSS, JavaScript.

## Struktur

```
data-stories/
├── index.html                   # Landing Page (alle Datenstücke)
├── README.md                    # diese Datei
├── CLAUDE.md                    # Projekt-Konventionen (EPO-Regeln)
│
├── <datenstueck-slug>/
│   ├── index.html               # Das Datenstück selbst
│   ├── data.json                # Alle Zahlen + Quellenangaben je Datenpunkt
│   └── METHODIK.md              # Quellen-URLs, Berechnungen, Einschränkungen
│
└── <research-ordner>/           # Recherche-Material (nicht deployt)
    └── RESEARCH.md              # Primärquellen, Notizen
```

Jedes Datenstück ist selbstständig — eine HTML-Datei, eine JSON-Datei, eine Methodik-Dokumentation. Keine Abhängigkeiten untereinander.

## Transparenz

Jedes Datenstück hat drei Ebenen der Nachvollziehbarkeit:

1. **`data.json`** — Alle Zahlen, die in den Charts stecken. Maschinenlesbar, mit Quellenangabe pro Datenpunkt.
2. **`METHODIK.md`** — Wie gerechnet wurde, woher die Daten kommen (mit direkten URLs), welche Annahmen getroffen wurden, was die Einschränkungen sind.
3. **Quellen-Sektion** am Ende jedes Datenstücks — für Leser, die nicht ins Repo schauen.

Bei angreifbaren Themen (z.B. #15 KRIEG(e)) wird die Quellenliste zusätzlich in **Tier 1/2/3** eingeteilt:
- **Tier 1:** Primärquellen / Regierungsdokumente (SIPRI, UCDP, CRS, UN Panels, declassifizierte CIA/State)
- **Tier 2:** Etablierte Institute / NGOs (ACLED, Brookings, HRW, PRIO)
- **Tier 3:** Etablierter Journalismus (Reuters, AP, BBC, FT)

Wer eine Zahl anzweifelt, findet hier den Weg zur Primärquelle.

## Datenquellen (Auswahl)

OECD · Destatis · Bundesagentur für Arbeit · DAK Gesundheitsreport · Gallup · Harvard Business School · HELCOM · UBA · Bundesbank · Deloitte · Reuters Institute · SIPRI · UCDP Uppsala · ACLED · UN OCHA/ICJ/ICC · CRS Reports · PRIO · National Security Archive · SeedCheck · Semantic Scholar · World Bank

Die vollständige Quellenliste mit URLs findet sich in der jeweiligen `METHODIK.md`.

## Lizenz

Die Visualisierungen und Texte sind urheberrechtlich geschützt. Die zugrunde liegenden Daten sind Open Data und frei verfügbar über die jeweils angegebenen Quellen.

Wer Fehler findet oder eine Zahl anzweifelt: **ich@der-koerting.de**

---

*Teil von [der-koerting.de](https://der-koerting.de) — Neugierig. Technisch. Vernetzt.*
