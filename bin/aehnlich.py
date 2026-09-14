#!/usr/bin/env python3
"""Schlaegt verwandte Datenstuecke vor. Entscheidet nichts.

TF-IDF ueber den Fliesstext, Kosinus-Aehnlichkeit, ohne Fremdbibliothek.

  aehnlich.py <slug>     Kandidaten fuer ein Stueck, mit Spurzugehoerigkeit
  aehnlich.py --fehlend  alle Stuecke ohne Spur, samt Vorschlag
  aehnlich.py --abgleich Guete der Rechnung gegen die Handarbeit
  aehnlich.py            Top-3 fuer alle

WARUM NUR VORSCHLAG: Der Abgleich am 14.09.2026 ergab 40 Prozent Deckung mit
der handgepflegten Zuordnung. Wo das Vokabular das Thema traegt (KI-Block),
trifft die Rechnung 3 von 3. Wo das Thema im Gegenstand steckt und nicht in
den Woertern, liegt sie komplett daneben - „Prost. Oder auch nicht." bekam
Fuerth, Hotels und Ausbildungsmarkt vorgeschlagen, weil alle von Betrieben,
Rueckgang und Prozent handeln. Die Datenstuecke aehneln sich sprachlich, weil
sie gleich geschrieben sind. Deshalb vorschlagen, nicht setzen.
"""
import glob, io, json, math, os, re, sys
from collections import Counter

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KONF = os.path.join(WURZEL, "bin", "verwandt.json")

STOPP = set("""
der die das den dem des ein eine einer eines einem einen und oder aber doch denn
ist sind war waren wird werden wurde wurden hat haben hatte hatten kann koennen
nicht nur auch noch schon mehr sehr mit ohne fuer gegen durch ueber unter vor nach
bei aus auf in im am an als zum zur vom beim dass wenn weil wie wo was wer
ich du er sie es wir ihr man sich mein dein sein ihre unser diese dieser dieses
hier dort dann jetzt heute jahr jahre jahren prozent seit bis pro etwa rund
sowie dabei damit dafuer daran darauf davon dazu jedoch zwar ja nein
koerting datenstueck datenstuecke blog quelle quellen daten methodik chart
""".split())


def text(pfad):
    h = io.open(pfad, encoding="utf-8").read()
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    h = h.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return [w for w in re.findall(r"[a-z]{4,}", h) if w not in STOPP]


def stuecke():
    aus = {}
    for p in glob.glob(os.path.join(WURZEL, "*/index.html")):
        d = os.path.basename(os.path.dirname(p))
        h = io.open(p, encoding="utf-8").read()
        m = re.search(r"Datenstück #(\d+)", h)
        t = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        if not m:
            continue
        roh = re.sub(r"<br\s*/?>", " ", t.group(1)) if t else d
        aus[d] = {"nr": int(m.group(1)),
                  "titel": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", roh)).strip(),
                  "worte": text(p)}
    return aus


def vektoren(alle):
    n = len(alle)
    df = Counter()
    for d in alle:
        df.update(set(alle[d]["worte"]))
    vek = {}
    for d in alle:
        tf = Counter(alle[d]["worte"])
        gesamt = sum(tf.values()) or 1
        v = {w: (c / gesamt) * math.log(n / df[w]) for w, c in tf.items() if df[w] > 1}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vek[d] = {w: x / norm for w, x in v.items()}
    return vek


def cos(a, b):
    klein, gross = (a, b) if len(a) < len(b) else (b, a)
    return sum(x * gross.get(w, 0) for w, x in klein.items())


def spuren_von(konf):
    zu = {}
    for sid, s in konf["spuren"].items():
        for d in s["stuecke"]:
            zu.setdefault(d, []).append(s["titel"])
    return zu


def kandidaten(d, alle, vek, k=4):
    return sorted(((cos(vek[d], vek[o]), o) for o in alle if o != d), reverse=True)[:k]


def zeige(d, alle, vek, zu):
    print(f'\n#{alle[d]["nr"]} {alle[d]["titel"]}')
    eigene = zu.get(d)
    print(f'   Spuren bisher: {", ".join(eigene) if eigene else "— keine —"}')
    print("   Kandidaten (Rechnung, nicht Entscheidung):")
    for s, o in kandidaten(d, alle, vek):
        sp = ", ".join(zu.get(o, [])) or "—"
        print(f'     {s:.2f}  #{alle[o]["nr"]:<3} {alle[o]["titel"][:34]:<34} [{sp}]')
    print("   Danach die passende Spur in bin/verwandt.json ergaenzen und")
    print("   bin/verwandt.py --setzen laufen lassen.")


def main():
    alle = stuecke()
    vek = vektoren(alle)
    konf = json.load(io.open(KONF, encoding="utf-8"))
    zu = spuren_von(konf)
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if arg == "--fehlend":
        ohne = [d for d in alle if d not in zu]
        if not ohne:
            print("Jedes Datenstück steht in mindestens einer Spur.")
            return 0
        print(f"{len(ohne)} Stück(e) ohne Spur:")
        for d in sorted(ohne, key=lambda x: -alle[x]["nr"]):
            zeige(d, alle, vek, zu)
        return 0

    if arg == "--abgleich":
        hand = {}
        for s in konf["spuren"].values():
            for a in s["stuecke"]:
                hand.setdefault(a, set()).update(x for x in s["stuecke"] if x != a)
        treffer = gesamt = 0
        for d in sorted(alle, key=lambda x: -alle[x]["nr"]):
            h = hand.get(d, set())
            if not h:
                continue
            auto = {o for _, o in kandidaten(d, alle, vek, 3)}
            treffer += len(auto & h)
            gesamt += 3
            print(f'  #{alle[d]["nr"]:<3} {d[:28]:<28} {len(auto & h)}/3')
        print(f"\n  Deckung mit der Handarbeit: {treffer}/{gesamt} = {treffer/gesamt*100:.0f} %")
        print("  Darum Vorschlag statt Automatik.")
        return 0

    if arg and not arg.startswith("--"):
        if arg not in alle:
            print(f"Unbekannt: {arg}")
            print("Bekannt:", ", ".join(sorted(alle)))
            return 1
        zeige(arg, alle, vek, zu)
        return 0

    for d in sorted(alle, key=lambda x: -alle[x]["nr"]):
        z = ", ".join(f'#{alle[o]["nr"]} ({s:.2f})' for s, o in kandidaten(d, alle, vek, 3))
        print(f'#{alle[d]["nr"]:<3} {alle[d]["titel"][:30]:<30} -> {z}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
