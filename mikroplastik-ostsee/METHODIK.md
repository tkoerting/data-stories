# Methodik — Was unter der klaren Ostsee liegt

**Datenstück #1** | Datenstand: März 2026 | Autor: Thomas Körting

---

## Quellen

| Datenpunkt | Quelle | URL | Abrufdatum |
|-----------|--------|-----|-----------|
| Mikroplastik-Konzentrationen | Leibniz-Institut für Ostseeforschung Warnemünde (IOW) | https://www.io-warnemuende.de/ | März 2026 |
| Munitionsaltlasten | HELCOM Thematic Assessment 2023 | https://helcom.fi/action-areas/marine-litter-and-noise/munitions/ | März 2026 |
| Dorschbestände | ICES Advice 2024 (Western Baltic Cod) | https://www.ices.dk/advice/Pages/Latest-Advice.aspx | März 2026 |
| Schweinswale Ostsee | SAMBAH-Studie / ASCOBANS | https://www.ascobans.org/ | März 2026 |
| Nährstoffeinträge | Umweltbundesamt (UBA) | https://www.umweltbundesamt.de/themen/wasser/gewaesser/meere/nutzung-belastungen/naehrstoffeintraege | März 2026 |
| Temperaturentwicklung | BSH (Bundesamt für Seeschifffahrt und Hydrographie) | https://www.bsh.de/ | März 2026 |
| Fangquoten | EU-Kommission / Bundesanstalt für Landwirtschaft und Ernährung | https://www.ble.de/ | März 2026 |
| Tourismus Ostsee | Statistisches Amt Mecklenburg-Vorpommern | https://www.statistik-mv.de/ | März 2026 |

## Berechnungen

### Mikroplastik-Dichte
- Partikel pro Kubikmeter: direkt aus IOW-Messdaten übernommen
- Vergleichswerte (Nordsee, Mittelmeer): Literaturvergleich, jeweils aktuellste verfügbare Studien

### Munitionsaltlasten
- 1,6 Mio. Tonnen konventionelle Munition in der gesamten Ostsee (HELCOM-Schätzung)
- Lokalisierung der Hauptgebiete aus HELCOM-Kartenmaterial

### Dorsch-Bestandsentwicklung
- Zeitreihe aus ICES Stock Assessment: Spawning Stock Biomass (SSB) in Tonnen
- Referenzpunkte (Blim, MSY Btrigger) aus ICES Advice Sheets

### 491 Schweinswale
- Population der zentralen Ostsee-Population (Belt Sea nicht mitgezählt)
- SAMBAH-Studie (Static Acoustic Monitoring of the Baltic Harbour Porpoise)
- 95%-Konfidenzintervall: 80–1.091 Tiere

## Einschränkungen

- Mikroplastik-Messungen variieren stark je nach Methodik (Partikelgröße, Beprobungstiefe)
- Munitionsmengen sind Schätzungen — exakte Kartierung existiert nicht
- Dorsch-Bestandsschätzungen haben Unsicherheitsmargen von ±20-30%
- Schweinswal-Zählung basiert auf akustischem Monitoring, nicht auf Sichtungen

## Datenverarbeitung

Alle Rohdaten wurden manuell aus den genannten Quellen extrahiert und in `data.json` strukturiert. Keine algorithmische Transformation. Zeitreihen wurden 1:1 übernommen, Vergleichswerte auf gleiche Einheiten normiert.
