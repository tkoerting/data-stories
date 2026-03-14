# Datenstücke

**Open Data, interaktiv visualisiert. Zu jedem Blogpost die Zahlen dahinter.**

Von [Thomas Körting](https://der-koerting.de) — Der Nerd. Der Spinner. Der, der was draus macht.

---

## Was sind Datenstücke?

Datenstücke nehmen ein Thema aus dem [Blog](https://der-koerting.de) und gehen tiefer — mit offenen Daten, interaktiven Charts und allen Quellen. Kein akademisches Paper, kein Dashboard. Eher: Was passiert, wenn jemand Zahlen nimmt, sie dreht, wendet, hinterfragt — und dann eine Geschichte erzählt, die man sonst nicht sieht.

**Live:** [opendataminded.de](https://opendataminded.de/)

---

## Datenstücke

| # | Titel | Thema | Charts | Quellen |
|---|-------|-------|--------|---------|
| 7 | [Du dumme Gans.](https://opendataminded.de/du-dumme-gans/) | Tier-Schimpfwörter, Neuronen, Jagderfolg, Ratten-Empathie, Alpha-Mythos, Sprachgeschichte | 6 | 14 |
| 6 | [1 Gramm, 23 Millionen](https://opendataminded.de/was-socke-hinterlaesst/) | Hundekot, Bakterien, Bußgelder, Plastik-Paradox, DNA-Tracking, Hundesteuer | 6 | 16 |
| 5 | [Ich hab Corona.](https://opendataminded.de/ich-hab-corona/) | COVID-Normalisierung, ICU, Medien, Müllberge, Ländervergleich | 5 | 25 |
| 4 | [Es ist ein Tauschgeschäft](https://opendataminded.de/tauschgeschaeft/) | Generationenvertrag, Vermögen, Bildungsinflation, Mental Health | 7 | 12 |
| 3 | [Nicht fauler. Führungsloser.](https://opendataminded.de/nicht-fauler-fuehrungsloser/) | OECD-Produktivität, Gallup-Engagement, Pencavel-Kurve | 6 | 8 |
| 2 | [Wie man seine Stadt schön träumt](https://opendataminded.de/fuerth-wissenschaftsstadt/) | Fürth als Wissenschaftsstadt, Open Data, Pendlerströme | 6 | 9 |
| 1 | [Was unter der klaren Ostsee liegt](https://opendataminded.de/mikroplastik-ostsee/) | Mikroplastik, Munition, Dorsch-Kollaps, Schweinswale | 9 | 19 |

---

## Technik

- **Visualisierung:** [Apache ECharts 5](https://echarts.apache.org/) — interaktiv, responsive, Dark/Light Mode
- **Design:** Slate & Tonic — Instrument Serif, Space Grotesk, JetBrains Mono
- **Daten:** Jedes Datenstück hat eine eigene `data.json` mit allen Zahlen und Quellenangaben
- **Hosting:** GitHub Pages
- **Kein Framework.** Kein Build-Step. Kein npm. Pures HTML, CSS, JavaScript.

## Struktur

```
data-stories/
├── index.html                          # Landing Page
├── mikroplastik-ostsee/
│   ├── index.html                      # Datenstück #1
│   ├── data.json                       # Daten + Quellen
│   └── METHODIK.md                     # Quellen-URLs, Berechnungen, Einschränkungen
├── fuerth-wissenschaftsstadt/
│   ├── index.html                      # Datenstück #2
│   ├── data.json
│   └── METHODIK.md
├── nicht-fauler-fuehrungsloser/
│   ├── index.html                      # Datenstück #3
│   ├── data.json
│   └── METHODIK.md
├── tauschgeschaeft/
│   ├── index.html                      # Datenstück #4
│   ├── data.json
│   └── METHODIK.md
├── ich-hab-corona/
│   ├── index.html                      # Datenstück #5 (Standalone)
│   ├── data.json
│   └── METHODIK.md
├── was-socke-hinterlaesst/
│   ├── index.html                      # Datenstück #6
│   ├── data.json
│   └── METHODIK.md
└── du-dumme-gans/
    ├── index.html                      # Datenstück #7
    ├── data.json
    └── METHODIK.md
```

Jedes Datenstück ist selbstständig — eine HTML-Datei, eine JSON-Datei, eine Methodik-Dokumentation. Keine Abhängigkeiten untereinander.

## Transparenz

Jedes Datenstück hat drei Ebenen der Nachvollziehbarkeit:

1. **`data.json`** — Alle Zahlen, die in den Charts stecken. Maschinenlesbar, mit Quellenangabe pro Datenpunkt.
2. **`METHODIK.md`** — Wie gerechnet wurde, woher die Daten kommen (mit direkten URLs), welche Annahmen getroffen wurden, was die Einschränkungen sind.
3. **Quellen-Sektion** am Ende jedes Datenstücks — für Leser, die nicht ins Repo schauen.

Wer eine Zahl anzweifelt, findet hier den Weg zur Primärquelle.

## Datenquellen

Alle Daten stammen aus öffentlich zugänglichen Quellen: OECD, Destatis, Bundesagentur für Arbeit, DAK Gesundheitsreport, Gallup, Harvard Business School, HELCOM, UBA, Bundesbank, Deloitte, Reuters Institute, und weitere. Die vollständige Quellenliste mit URLs findet sich in der jeweiligen `METHODIK.md`.

## Lizenz

Die Visualisierungen und Texte sind urheberrechtlich geschützt. Die zugrunde liegenden Daten sind Open Data und frei verfügbar über die jeweils angegebenen Quellen.

---

*Teil von [der-koerting.de](https://der-koerting.de) — Neugierig. Technisch. Vernetzt.*
