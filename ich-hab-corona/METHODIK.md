# Methodik — Ich hab Corona.

**Datenstück #5** | Datenstand: März 2026 | Autor: Thomas Körting | Standalone (kein Blogpost)

---

## Quellen

| Datenpunkt | Quelle | URL | Abrufdatum |
|-----------|--------|-----|-----------|
| ICU-Zeitreihe | DIVI Intensivregister — COVID-19 Tagesberichte | https://www.divi.de/register/tagesreport | März 2026 |
| SARI-Surveillance | RKI — GrippeWeb / ICOSARI | https://grippeweb.rki.de/ | März 2026 |
| COVID-Todesfälle | RKI Lagebericht / Destatis Sterbefallstatistik | https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Todesursachen/_inhalt.html | März 2026 |
| Krankmeldungs-Ranking | DAK Gesundheitsreport 2024/2025 | https://www.dak.de/dak/unternehmen/reporte-forschung/gesundheitsreport-2025_142376 | März 2026 |
| AU-Tage COVID | DAK / TK Gesundheitsreport | https://www.tk.de/firmenkunden/service/gesund-arbeiten/gesundheitsreport | März 2026 |
| Ende COVID-Maßnahmen | WHO Policy Tracker / Our World in Data | https://ourworldindata.org/policy-responses-covid | März 2026 |
| Dänemark Hospitalisierung | Statens Serum Institut (SSI) | https://www.ssi.dk/ | März 2026 |
| USA Hospitalisierung | CDC RESP-NET / FluView | https://www.cdc.gov/respiratory-viruses/data-research/ | März 2026 |
| Medienberichterstattung | PMG Presse-Monitor / Media Tenor | https://www.presse-monitor.de/ | März 2026 |
| TV-Nachrichtenanteil | Media Tenor International | https://www.mediatenor.com/ | März 2026 |
| Drosten-Podcast | NDR Coronavirus-Update Archiv | https://www.ndr.de/nachrichten/info/Coronavirus-Update-Alle-Folgen,podcastcoronavirus100.html | März 2026 |
| Lauterbach Talkshows | Talkshow-Tracker / Medienanalyse | — | März 2026 |
| Lauterbach Zustimmung | Infratest dimap | https://www.infratest-dimap.de/ | März 2026 |
| Medienvertrauen | Uni Mainz — Medienvertrauen Langzeitstudie | https://medienvertrauen.uni-mainz.de/ | März 2026 |
| Masken Deutschland | BMG Beschaffungsdaten / Bundesrechnungshof | https://www.bundesrechnungshof.de/ | März 2026 |
| Masken Gewicht/Maße | PNAS — Environmental challenges of COVID-19 PPE | https://www.pnas.org/doi/10.1073/pnas.2108799118 | März 2026 |
| PCR-Tests Gesamtzahl | ALM e.V. — Datenerhebung SARS-CoV-2 | https://www.alm-ev.de/ | März 2026 |
| Schnelltests | BMG / Statista | https://de.statista.com/ | März 2026 |
| Impfdosen | RKI Impfquotenmonitoring | https://www.rki.de/DE/Content/Infekt/Impfen/ImpfungenAZ/COVID-19/Covid-19.html | März 2026 |
| Spahn Maskenbeschaffung | Bundesrechnungshof — Sonderbericht | https://www.bundesrechnungshof.de/ | März 2026 |
| Masken im Meer | OceansAsia — COVID-19 Facemasks in Oceans | https://oceansasia.org/covid-19-facemasks/ | März 2026 |
| Zersetzungszeit | PNAS / Environmental Science & Technology | https://pubs.acs.org/journal/esthag | März 2026 |
| Testkosten gesamt | Bundesrechnungshof | https://www.bundesrechnungshof.de/ | März 2026 |
| Long COVID | BMG / BMAS / DAK | https://www.bundesgesundheitsministerium.de/ | März 2026 |
| Volkswirtschaftl. Kosten | IW Köln / ifo Institut | https://www.iwkoeln.de/ | März 2026 |

## Berechnungen

### ICU-Rückgang
```
rückgang_pct = (1 - aktuell / peak) × 100
= (1 - 30 / 5700) × 100
= 99,5%
```

### Erdumrundungen (Masken)
```
erdumrundungen = (17.000.000.000 × 0,17 m) / 40.075.000 m
= 2.890.000.000 m / 40.075.000 m
= 72,1
```
17 Mrd. Masken × 17 cm (Standard-OP-Maske Länge) ÷ Erdumfang (40.075 km)

### Eiffeltürme (Maskengewicht)
```
eiffeltürme = masken_gewicht_t / eiffelturm_gewicht_t
= 68.000 / 10.100
= 6,7
```
Gewicht Eiffelturm: 10.100 Tonnen (Stahlkonstruktion)

### Maskengewicht
```
masken_gewicht_t = 17.000.000.000 × 4 g / 1.000.000
= 68.000 t
```

### Olympische Schwimmbecken
```
schwimmbecken = masken_volumen_m3 / becken_volumen_m3
= 255.000 / 2.500
= 102
```
Volumen eines Olympischen Schwimmbeckens: 2.500 m³ (50m × 25m × 2m)

### Spahn-Masken Gesamtkosten
```
gesamtkosten = bestellkosten + vernichtungskosten
= 5.900.000.000 + 500.000.000
= 6.400.000.000 € (6,4 Mrd.)
```

### Todesfälle-Rückgang 2021→2023
```
rückgang_pct = (1 - 25.768 / 71.331) × 100 = 63,9% ≈ 64%
```

### Medienvertrauen-Verlust
```
verlust_pp = 63% - 43% = 20 Prozentpunkte
```
In Prozentpunkten (pp), nicht Prozent.

## Datenbilder — Methodik

Die "Datenbilder" sind bewusst gewählte Vergleichsgrößen, die große Zahlen greifbar machen:
- **72 Erdumrundungen**: 17 Mrd. Masken × 17 cm ÷ 40.075 km
- **6,7 Eiffeltürme**: 68.000 t ÷ 10.100 t
- **102 Olympische Schwimmbecken**: 255.000 m³ ÷ 2.500 m³
- **450 Jahre Zersetzung**: PNAS-Studie zu Polypropylen-Degradation in mariner Umgebung

Alle Berechnungen sind bewusst konservativ. Die tatsächlichen Zahlen könnten höher liegen (z.B. durch nicht erfasste privat gekaufte Masken).

## Einschränkungen

- **Todesfälle 2024/2025**: Schätzwerte, da offizielle Daten noch nicht konsolidiert sind. Basierend auf RKI-Trends und SARI-Surveillance.
- **Maskenverbrauch**: 17 Mrd. ist eine Schätzung auf Basis von BMG-Beschaffungsdaten + geschätztem privatem Verbrauch. Die echte Zahl könnte höher liegen.
- **PCR-Testmüll**: 37,27 g pro Test ist ein Durchschnittswert aus der PNAS-Studie, variiert je nach Testkit.
- **Schnelltests**: 10 g pro Test ist ein konservativer Durchschnitt (Plastikkassette + Verpackung).
- **Ländervergleich**: "Ende aller Maßnahmen" ist nicht eindeutig definiert. Manche Länder hoben Maßnahmen stufenweise auf. Das angegebene Datum bezieht sich auf den letzten wesentlichen Maßnahmen-Schritt.
- **Medienberichterstattung**: PMG-Daten erfassen nur deutschsprachige Printmedien und Online-Auftritte. TV-Berichterstattung separat über Media Tenor.
- **Medienvertrauen**: Die Mainzer Langzeitstudie misst "generelles Medienvertrauen", nicht spezifisch COVID-bezogen. Der Rückgang korreliert mit der Pandemie, ist aber nicht kausal nur darauf zurückzuführen.
- **Long COVID**: Die 1,5 Mio. Betroffenen sind eine Schätzung. Diagnosekriterien und Erfassung variieren.
- **Volkswirtschaftliche Kosten**: Die 250 Mrd. € sind eine Gesamtschätzung (IW Köln), die direkte und indirekte Kosten umfasst.
- **Standalone-Format**: Dieses Datenstück hat keinen zugehörigen Blogpost. Die Daten sprechen für sich.

## Datenverarbeitung

Alle Werte manuell aus den Primärquellen extrahiert. Zeitreihen aus DIVI, RKI und Destatis als CSV/JSON heruntergeladen und auf relevante Datenpunkte verdichtet. Datenbilder-Berechnungen mit Standardwerten (Erdumfang, Eiffelturm-Gewicht, Schwimmbecken-Volumen) aus allgemein anerkannten Quellen. Alle Prozentwerte auf eine Nachkommastelle gerundet.
