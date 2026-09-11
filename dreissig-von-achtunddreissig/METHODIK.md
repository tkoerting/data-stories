# Methodik — „Dreißig von achtunddreißig."

Stand: 11.09.2026. Alle Anteile selbst berechnet, keine Prozentangabe aus einem Fließtext
übernommen.

## Wichtiger Hinweis zur Quelle

Grundlage sind die **Wahl-O-Mat-Datensätze der Bundeszentrale für politische Bildung**.
Die bpb erlaubt die Analyse dieser Daten zu wissenschaftlichen oder journalistischen Zwecken
und die Veröffentlichung der Ergebnisse. Sie verlangt dabei ausdrücklich, dass erkennbar
bleibt, dass sie nicht Urheberin der Analyse ist.

**Diese Auswertung stammt nicht von der Bundeszentrale für politische Bildung.**

Aus demselben Grund enthält `data.json` nur berechnete Werte — Anteile, Zählungen, die Titel
einzelner Thesen. Der Datensatz selbst wird hier nicht weiterveröffentlicht, die
Begründungstexte der Parteien ebenfalls nicht.

## Was gemessen wird

Der Wahl-O-Mat legt jeder antretenden Partei dieselben 38 Thesen vor. Jede Partei antwortet
mit **„Stimme zu"**, **„Neutral"** oder **„Stimme nicht zu"**.

Die hier verwendete Kennzahl ist denkbar einfach: Bei wie vielen der 38 Thesen haben zwei
Parteien **dieselbe Antwort** gegeben?

Mehr steckt nicht dahinter. Kein Gewichtungsmodell, keine Skalierung, keine Faktorenanalyse.
Das ist Absicht — jeder kann es nachzählen.

## Quellen

| Reihe | Quelle |
|---|---|
| Positionen zu 21 Wahlen 2021–2026 | bpb, Wahl-O-Mat-Datensätze, Sammelausgabe Stand 30.03.2026 |
| Positionen Sachsen-Anhalt 2026 | bpb, Wahl-O-Mat Sachsen-Anhalt 2026, Datensatz v1.01 vom 14.08.2026 |
| Ergebnisse Bundestagswahl 2021, 2025 | Die Bundeswahlleiterin, amtliches Endergebnis |
| Ergebnis Europawahl 2024 | Die Bundeswahlleiterin, amtliches Endergebnis |
| Ergebnisse Landtagswahlen | Landeswahlleitungen der Länder, amtliche Endergebnisse |

## Grenzen der Messung

Diese Einschränkungen sind keine Fußnote. Sie bestimmen, was die Zahlen aussagen dürfen.

### Die Thesen sind zwischen den Wahlen nicht dieselben

Für jede Wahl stellt ein eigenes Redaktionsteam der bpb aus rund 80 vorgelegten Thesen
38 zusammen. Die Auswahl unterscheidet sich also von Wahl zu Wahl.

**Folge:** Die Prozentwerte zweier Wahlen sind nicht streng vergleichbar. Was verglichen
werden darf, sind Größenordnung und Rangfolge — nicht der Abstand zweier Einzelwerte auf
den Punkt. Der Vergleich Sachsen-Anhalt 2021 (50 %) gegen 2026 (47 %) ist deshalb
**schwächer, als er aussieht**. Drei Punkte bei wechselnder Thesenauswahl sind kein Beleg
für eine Bewegung.

Belastbarer ist das Muster über viele Wahlen hinweg, weil sich die Auswahleffekte dort
teilweise herausmitteln.

### Die Thesen sind absichtlich die strittigen

Die bpb wählt aus den 80 Thesen jene aus, die von den Parteien **kontrovers** beantwortet
wurden. Gemessen wird also die Übereinstimmung auf dem Feld, das am meisten trennt.

**Folge:** Die tatsächliche programmatische Übereinstimmung liegt höher als hier gemessen,
nicht niedriger. Die Verzerrung geht zulasten der These, nicht zu ihren Gunsten.

### Gleiche Position heißt nicht gleiche Begründung

Bei der These „Sonntagsöffnung" lehnen in Sachsen-Anhalt alle sechs Landtagsparteien ab —
mit sehr verschiedenen Argumenten. Der Datensatz enthält die Begründungen, diese Auswertung
nutzt sie nicht.

**Folge:** Übereinstimmung in der Position ist ein schwächerer Befund als Übereinstimmung in
der Haltung. Wer aus den Zahlen inhaltliche Nähe liest, liest mehr hinein als drinsteht.

### Das Parteienfeld verändert sich

Ab 2024 tritt das BSW an. Das verändert beide Messgrößen der Isolationsrechnung
gleichzeitig: Es kommt eine Partei hinzu, die der AfD in Teilen nahesteht und den übrigen
fern.

**Folge:** Dass der Abstand der AfD zu den anderen von 8 auf 12 Punkte gewachsen ist, lässt
sich mit diesen Daten **nicht** eindeutig der AfD zurechnen. Es kann am veränderten Feld
liegen. Diese Zahl ist als Beobachtung gekennzeichnet, nicht als Befund.

### Die Korrelation ist schwach

Zwischen dem Stimmenanteil der AfD und der Programmnähe von CDU und AfD liegt über 22 Wahlen
**r = −0,33**. Das Vorzeichen ist stabil, die Erklärungskraft gering — rund elf Prozent der
Streuung.

**Folge:** „Wo die AfD stark ist, steht ihr die CDU ferner" ist ein Trend, keine Regel. Die
Ausreißer sind größer als der Zusammenhang. Berlin 2023 hat den höchsten Nähewert bei fast
schwächstem AfD-Ergebnis.

### Ost und West

Der Unterschied der Mediane — 51 % gegenüber 63 % — beruht auf sechs östlichen gegenüber
dreizehn westlichen Landtagswahlen. Bei dieser Größenordnung ist das eine **Beobachtung**.
Ein Signifikanztest ist bei sechs Beobachtungen nicht sinnvoll, und er wird hier deshalb
auch nicht behauptet.

## Was diese Auswertung nicht zeigt

- **Kein Abstimmungsverhalten.** Gemessen sind Wahlkampfpositionen, nicht Entscheidungen in
  Parlamenten. Ob CDU und AfD in Sachsen-Anhalt tatsächlich gleich abstimmen, steht in
  Plenarprotokollen und nicht hier.
- **Keine Koalitionsaussage.** Programmatische Nähe sagt nichts darüber, wer mit wem
  regieren will oder kann.
- **Keine Entwicklung einzelner Parteien.** Dafür wären identische Thesen über die Zeit
  nötig. Die gibt es nicht.
- **Nichts über Ursachen.** Warum die Werte streuen, ist mit diesen Daten nicht zu
  beantworten.

## Nachrechnen

Wer die Zahlen prüfen will, braucht zwei Dinge: die Wahl-O-Mat-Datensätze von der bpb und
eine Zählung identischer Antworten je Parteienpaar. Die Kennzahl ist bewusst so gewählt,
dass dafür eine Tabellenkalkulation reicht.
