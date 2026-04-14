# Datenstück-Template — Open Data Minded

> Wiederverwendbare Struktur für neue Datenstücke auf opendataminded.de.
> Reference-Implementierung: `/zwei-tode/index.html` und `/du-dumme-gans/index.html`.

## Ordnerstruktur pro Datenstück

```
<slug>/
├── index.html          # Hauptseite
├── data.json           # (optional) Rohdaten, wenn externe Quellen
├── research.md         # Recherche, Quellen, belegte Zahlen
└── METHODIK.md         # (optional) Methodik, wenn Berechnungen komplex
```

## Narrativer Bogen (4-Klang)

Jedes Datenstück folgt dem gleichen dramaturgischen Aufbau:

1. **Hook / Anlass** — Warum jetzt? Persönlicher oder aktueller Einstieg.
2. **Daten / Befund** — Was sagen die Zahlen? KPIs + 2–4 Charts.
3. **Kontext / Einordnung** — Wie ist das im Vergleich zu bedenken?
4. **Closer / Frage** — Was bleibt offen? Keine Urteile, sondern Fragen.

## Pflicht-Elemente

- **Category-Tag** + **Snapshot-Datum** oben
- **Headline** (Instrument Serif) + **Subtitle** (kursiv, grau)
- **Lead-Absatz** im Intro (größere Schrift, grau)
- **KPI-Grid** (3 Karten) mit den Kern-Zahlen
- **Section-Nav** (Pills) als klickbarer Anker
- **Quellen-Abschnitt** am Ende mit vollständigen Links
- **Transparenz-Disclaimer:** "Fehler gefunden? ich@der-koerting.de"
- **Footer mit Feedback-Block** ("Mehr davon?" → Google Sheets)
- **GA4-Consent-Banner** (nur laden nach Zustimmung, G-Q50MESBRQS)

## Optional

- **Podcast-Player** (NotebookLM-Audio, wenn vorhanden)
- **Interaktive Elemente:** Quiz, Race, Dilemma (siehe `du-dumme-gans`)
- **Laut-gedacht-Element:** persönlicher Gedanke in eigener Box (Instrument Serif, italic)
- **Data-Box:** Hervorgehobene Einzelbeobachtung mit Zahl

## Meta / SEO / GEO (Pflicht)

- `<title>` mit Format: `<Titel> — Datenstück | Der Körting`
- `<meta name="description">` ca. 155 Zeichen
- OpenGraph (`og:title`, `og:description`, `og:url`, `og:site_name`)
- `twitter:card` als `summary`
- `<link rel="canonical">` auf opendataminded.de-URL
- JSON-LD `Article` Schema mit author, datePublished, url, inLanguage
- `@font-face` für Instrument Serif + Space Grotesk (oder Google Fonts preconnect)

## Design-Variablen (Slate & Tonic)

**Dark:**
- bg #111318, text #E5E7EB, accent #14B8A6, accent-2 #FACC15

**Light:**
- bg #F4F6F7, text #1E293B, accent #0D9488, accent-2 #EAB308

## Technik

- **Charts:** ECharts 5 via CDN (`cdn.jsdelivr.net/npm/echarts@5`)
- **Fonts:** Instrument Serif (Headlines) + Space Grotesk (Body) + JetBrains Mono (Zahlen)
- **Theme-Toggle:** `data-theme="light|dark"` auf `<html>`, localStorage
- **Max-Width:** 760px Content
- **Mobile:** header-nav ab 768px ausblenden
- **GA4:** Only-after-consent, Measurement ID `G-Q50MESBRQS`

## Quick Start — Neues Datenstück

1. `cp -r zwei-tode <neuer-slug>`
2. `index.html` — alle Meta/Schema-Felder auf neue URL/Titel/Datum ändern
3. `research.md` — Quellen und belegte Zahlen zuerst festhalten, **vor** jeder Visualisierung
4. Datenstück nach 4-Klang gliedern
5. KPI-Grid + 2–4 Charts bauen, auf echte Zahlen verweisen
6. Closer als Frage formulieren, nicht als Urteil
7. Quellen komplett angeben, jede Zahl muss rückverfolgbar sein
8. Auf opendataminded.de Landing Page (`/index.html`) verlinken
9. Im Blogpost Rückverlinkung setzen
10. Commit, push, LinkedIn-Post nach Live-Gang

## Anti-Patterns (NICHT machen)

- Zahlen ohne Quelle
- KI-generierte "Schätzungen" als Fakten darstellen
- Narrative Brücken mit erfundenen Zitaten realer Personen
- Framing aus Angreifer-Perspektive (bei sicherheitsrelevanten Themen)
- Urteile im Closer statt Fragen
- Fehlende Transparenz-Hinweise (Fehler-Mail, KI-Unterstützung)
