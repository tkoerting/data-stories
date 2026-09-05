# Methodik — „84.400 ohne Platz."

Stand: 04.09.2026. Alle Zahlen aus amtlichen Primärquellen, jede Prozentangabe selbst
nachgerechnet und nicht aus Fließtext oder Pressemitteilung übernommen.

## Quellen

| Reihe | Quelle | Tabelle |
|---|---|---|
| Angebot, Nachfrage, eANR 2011–2025 | BIBB, Datenreport zum Berufsbildungsbericht 2026 | A1.1.1-1 |
| Neu abgeschlossene Verträge 2011–2025 | dito | A1.2-1 |
| Neu abgeschlossene Verträge 2002–2010 | BIBB, Datenreport 2021 | A1.2-1 |
| Ausbildungsbetriebsquote 2007 / 2024 | BIBB/Bundesagentur für Arbeit, Datenreport 2026 | A7.1-1 |
| Unbesetzte Stellen, unversorgte junge Menschen 2025 | BIBB, „Der Ausbildungsmarkt im Jahr 2025" | — |
| Erwerbspersonen nach Alter 2024 | Statistisches Bundesamt, PM Nr. 048/2025, Mikrozensus 2024 | — |

## Verkettung der Langreihe

Die Reihe 2002–2025 stammt aus zwei Ausgaben des Datenreports. Der Datenreport 2026 weist
Verträge erst ab 2011 aus, der Datenreport 2021 deckt 2002–2020 ab.

**Gegenprobe:** In allen zehn Überlappungsjahren (2011–2020) sind die Werte beider Ausgaben
**identisch**. Erst dieser Abgleich macht die Verkettung zulässig. Ohne ihn wären zwei
Reihen aneinandergeklebt und nicht geprüft worden.

Startjahr 2002 statt 1977: Die Erhebung läuft seit 1977, vor 1990 aber nur für
Westdeutschland. Ein Rückgang bis dorthin würde einen Wiedervereinigungsbruch in die Kurve
holen, ohne die Aussage zu verbessern. 2002 ist durchgehend Gesamtdeutschland.

## Rundung auf Vielfache von drei

Fußnote des BIBB unter Tabelle A1.2-1, wörtlich:

> „Absolutwerte werden aus Datenschutzgründen jeweils auf ein Vielfaches von 3 gerundet;
> der Gesamtwert kann deshalb von der Summe der Einzelwerte abweichen."

Abweichungen von ±3 zwischen eigenen Rechnungen und den ausgewiesenen Differenzen sind
dadurch erklärt und kein Fehler. Beispiel: Nachfrage 2025 minus 2024 ergibt aus den
gerundeten Werten 3.660, die Tabelle weist 3.663 aus.

## Aufgefüllte Lücke in der Zahl für 2025

Fußnote 1 zu Tabelle A1.2-1: Meldeausfall für die Ärztekammer Westfalen-Lippe
(Nordrhein-Westfalen, Freie Berufe); verwendet wurden die Daten aus 2024. Das größte
Bundesland der Tabelle (102.009 Verträge, ausgewiesen mit −4,5 %) trägt damit teilweise
Vorjahreswerte. Korrekt gekennzeichnet, methodisch vertretbar — im Datenstück als
Einschränkung ausgewiesen.

## Eigene Rechnungen

- Verträge 2025 zu 2024: 475.950 − 486.261 = −10.311 → −2,12 % (Tabelle: −10.311 / −2,1 %)
- Verträge seit Höchststand: 475.950 − 625.884 = −149.934 → −24,0 %
- Angebot 2025: 530.334 − 555.666 = −25.332 → −4,56 %
- Nachfrage 2011 → 2025: 560.307 / 641.796 − 1 = −12,7 %
- Ausbildungsbetriebe 2007 → 2024: 396.817 − 489.890 = −93.073 → −19,0 %
- Betriebe 2007 → 2024: 2.116.533 − 2.035.511 = +81.022 → +4,0 %
- Erwerbspersonen 55–64 (2024): 5,6 + 4,4 = 10,0 Mio gegen 9,0 Mio bei 25–34

## Was bewusst nicht behauptet wird

Es gibt keine amtliche Statistik, die den Rückgang von Ausbildungsplätzen mit dem Einsatz
von KI verknüpft. Das Datenstück stellt die zeitliche Entwicklung dar und benennt
ausdrücklich, dass daraus keine Ursache abgeleitet werden kann. Die Langreihe ab 2002 ist
genau deshalb enthalten: Sie zeigt, dass der Abstieg 2007 beginnt.

## Reproduzierbar

`data.json` enthält alle verwendeten Reihen. Die CSV-Zwischenstände und der Rechenweg
liegen im Blog-Repository unter `datenstuecke/daten-20/`.

Fehler gefunden? ich@der-koerting.de
