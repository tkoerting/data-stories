# Methodik — Schneller als du denkst.

## Datenstück #8 — Die Beschleunigung der KI

### Was dieses Datenstück zeigt

Die Beschleunigung des KI-Fortschritts anhand von fünf Dimensionen: Meilenstein-Abstände, Rechenleistung, Kosten, Adoption und Benchmark-Konvergenz. Alle Daten beziehen sich auf den Stand März 2026.

### Datenquellen

| Sektion | Primärquelle | Sekundärquelle |
|---------|-------------|----------------|
| Meilensteine | Stanford HAI AI Index 2025 | Epoch AI |
| Training Compute | Epoch AI Compute Trends Post-2010 | Epoch AI Training Compute Dataset |
| Kostenverfall | Stanford HAI AI Index 2025 (MMLU-Performance-Kosten) | — |
| Modell-Effizienz | Stanford HAI AI Index 2025 (Phi-3-mini vs. PaLM) | Microsoft Research |
| Adoption (100M Nutzer) | Visual Capitalist | Epoch AI |
| Enterprise Adoption | McKinsey State of AI 2025 | — |
| VC-Investitionen | OECD VC Report | Stanford HAI Economy Chapter |
| Corporate AI Investment | Stanford HAI AI Index 2025 | CNBC |
| Benchmark-Performance | Stanford HAI AI Index 2025 (MMLU, HumanEval) | — |
| Modell-Konvergenz | Stanford HAI AI Index 2025 | — |
| KI-Paper | Stanford HAI R&D Chapter | Our World in Data |
| KI-Patente | Our World in Data | PatentPC |

### Methodik im Detail

**Meilenstein-Abstände:**
Die Zeitspannen zwischen KI-Meilensteinen sind kalendarische Abstände zwischen öffentlich dokumentierten Ereignissen (Deep Blue Match 1997, Watson Jeopardy 2011, AlphaGo vs. Lee Sedol 2016, GPT-3 Paper 2020, ChatGPT Release Nov 2022, GPT-4 Release März 2023). Die Auswahl der Meilensteine folgt der gängigen Literatur und ist naturgemäß subjektiv — andere Meilensteine (z.B. BERT 2018, DALL-E 2021) hätten die Reihe verändert, aber nicht den Trend.

**Training Compute:**
FLOP-Werte (Floating Point Operations) stammen aus dem Epoch AI Training Compute Dataset. Die Werte sind geschätzt, da nicht alle Unternehmen exakte Trainingsdaten veröffentlichen. Für GPT-4 wird der Epoch-AI-Schätzwert >10^25 FLOP verwendet. Die logarithmische Darstellung ist notwendig, da die Werte über 8 Größenordnungen streuen.

**Kostenverfall:**
Die Kosten pro Million Tokens beziehen sich auf MMLU-Performance auf GPT-3.5-Niveau (ca. 70% MMLU-Score). Die Reduktion von $20 auf $0,07 ergibt den Faktor 285x. Quelle: Stanford HAI AI Index 2025, basierend auf öffentlichen API-Preisen.

**Modell-Effizienz (142x):**
Microsoft Phi-3-mini (3,8 Mrd. Parameter) erreicht 2024 ca. 60% auf dem MMLU-Benchmark — ein Wert, den 2022 nur PaLM mit 540 Mrd. Parametern erreichte. Das ergibt einen Faktor von ~142x in der Parameterreduktion für gleiche Leistung. Achtung: Die Architektur ist nicht identisch, der Vergleich zeigt den Effizienzgewinn, nicht eine direkte 1:1-Reduktion.

**Adoption (100 Millionen Nutzer):**
Die Zeitangaben für historische Technologien sind Schätzwerte und variieren je nach Quelle und Marktdefinition. Für ChatGPT ist der Zeitraum Nov 2022 bis Jan 2023 dokumentiert (UBS-Studie). Die 700 Mio. wöchentlich aktive Nutzer sind OpenAI-Angaben (Stand Ende 2025).

**Enterprise Adoption:**
McKinsey State of AI Report, basierend auf globaler Befragung (N>1.000 Unternehmen). Der Sprung von ~50% auf 72% (2024) korreliert mit dem ChatGPT-Launch, ist aber auch durch erweiterte KI-Definitionen in der Umfrage beeinflusst.

**Benchmark-Konvergenz:**
Der Abstand zwischen dem besten und zweitbesten Modell auf MMLU schrumpfte von 4,9 Prozentpunkten (2023) auf 0,7 Prozentpunkte (2024). Dies zeigt Konvergenz an der Frontier, nicht Stillstand. Gleichzeitig wechseln Forscher auf härtere Benchmarks (MMLU-Pro, GPQA, HLE, MMMU).

### Einschränkungen

- **Meilenstein-Auswahl ist subjektiv.** Andere Forscher würden andere Meilensteine wählen. Der Trend der Beschleunigung bleibt davon unberührt.
- **Training-Compute-Schätzungen.** Nicht alle Unternehmen veröffentlichen exakte Werte. Epoch AI verwendet eine anerkannte Schätzmethodik, aber Unsicherheiten bleiben.
- **Kosten-Benchmark-Kopplung.** Der 285x-Faktor gilt für ein spezifisches Leistungsniveau (GPT-3.5-äquivalent auf MMLU). Für andere Leistungsniveaus oder Aufgaben wäre der Faktor anders.
- **Adoption ≠ Nutzung.** 72% der Unternehmen "nutzen KI" sagt nichts über die Tiefe der Nutzung. 74% schaffen es nicht über Pilotprojekte hinaus.
- **Benchmark-Sättigung.** Hohe MMLU-Scores (>88%) bedeuten nicht, dass Modelle "alles können". Sie bedeuten, dass der Benchmark zu einfach geworden ist.

### Tools & Erstellung

- Recherche und Datenaufbereitung: Claude (Anthropic)
- Visualisierung: ECharts 5
- Alle Daten, Quellen und der vollständige Code sind öffentlich auf GitHub: [tkoerting/data-stories](https://github.com/tkoerting/data-stories)

### Kontakt

Fehler gefunden? Bessere Quelle? → ich@der-koerting.de
