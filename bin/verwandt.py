#!/usr/bin/env python3
"""Setzt die „Gehört zu"-Bloecke in die Datenstuecke.

  verwandt.py            zeigt, was gesetzt wuerde (nichts wird geschrieben)
  verwandt.py --setzen   schreibt die Bloecke in die index.html

Quelle der Zuordnung ist bin/verwandt.json, von Hand gepflegt. Der Block wird
zwischen Markern gesetzt und bei jedem Lauf vollstaendig ersetzt, damit sich
nichts doppelt.
"""
import json, os, re, sys, io, glob

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START = "<!-- VERWANDT:START -->"
ENDE = "<!-- VERWANDT:ENDE -->"
# Ankerpunkte in absteigender Vorzugsreihenfolge; die Stuecke haben teils eigene Layouts.
ANKER = ['<div class="article-footer">', '<div class="finale-footer">',
         '<div class="sources">', '<div class="meta">']

CSS = """<style>
.verwandt{margin-top:3rem;padding-top:1.6rem;border-top:1px solid var(--border)}
.verwandt-label{font-family:'JetBrains Mono',monospace;font-size:.7rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--text-tertiary);margin-bottom:.9rem}
.verwandt-liste{display:flex;flex-direction:column;gap:.55rem}
.verwandt-liste a{display:flex;gap:.6rem;align-items:baseline;text-decoration:none;
  color:var(--text-secondary);font-size:.9rem;line-height:1.45}
.verwandt-liste a:hover{color:var(--accent)}
.verwandt-nr{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--text-tertiary);
  flex-shrink:0;min-width:2.1rem}
</style>"""


def stuecke():
    aus = {}
    for p in glob.glob(os.path.join(WURZEL, "*/index.html")):
        d = os.path.basename(os.path.dirname(p))
        h = io.open(p, encoding="utf-8").read()
        m = re.search(r"Datenstück #(\d+)", h)
        if not m:
            continue
        t = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        roh = re.sub(r"<br\s*/?>", " ", t.group(1)) if t else d
        titel = re.sub(r"<[^>]+>", "", roh)
        titel = re.sub(r"\s+", " ", titel).strip()
        aus[d] = {"nr": int(m.group(1)), "titel": titel, "pfad": p}
    return aus


def nachbarn(alle, spuren):
    """Je Stueck die verwandten, nach Spur gruppiert, ohne Dubletten."""
    aus = {}
    for d in alle:
        gefunden, gesehen = [], {d}
        for sid, s in spuren.items():
            if d not in s["stuecke"]:
                continue
            for anderes in s["stuecke"]:
                if anderes in gesehen or anderes not in alle:
                    continue
                gesehen.add(anderes)
                gefunden.append((s["titel"], anderes))
        if gefunden:
            aus[d] = gefunden[:3]
    return aus


def block(eintraege, alle):
    zeilen = []
    for spur, ziel in eintraege:
        s = alle[ziel]
        zeilen.append(
            f'<a href="../{ziel}/"><span class="verwandt-nr">#{s["nr"]}</span>'
            f'<span>{s["titel"]}</span></a>')
    spuren = sorted({s for s, _ in eintraege})
    label = "Gehört zu: " + " · ".join(spuren)
    return (f'{START}\n<div class="verwandt">\n  <div class="verwandt-label">{label}</div>\n'
            f'  <div class="verwandt-liste">\n    ' + "\n    ".join(zeilen) +
            f'\n  </div>\n</div>\n{ENDE}')


def main():
    setzen = "--setzen" in sys.argv
    konf = json.load(io.open(os.path.join(WURZEL, "bin", "verwandt.json"), encoding="utf-8"))
    alle = stuecke()
    unbekannt = {s for v in konf["spuren"].values() for s in v["stuecke"]} - set(alle)
    if unbekannt:
        print("Unbekannte Stücke in verwandt.json:", sorted(unbekannt))
        return 1
    nb = nachbarn(alle, konf["spuren"])
    ohne = sorted(set(alle) - set(nb), key=lambda d: alle[d]["nr"])
    for d in sorted(nb, key=lambda x: -alle[x]["nr"]):
        print(f'#{alle[d]["nr"]:<3} {alle[d]["titel"][:38]:<38} -> ' +
              ", ".join(f'#{alle[z]["nr"]}' for _, z in nb[d]))
    if ohne:
        print("\nOhne Spur (bekommen keinen Block):")
        for d in ohne:
            print(f'   #{alle[d]["nr"]:<3} {d}')
        print("   Kandidaten vorschlagen lassen:  bin/aehnlich.py --fehlend")
    if not setzen:
        print("\nProbelauf. Mit --setzen schreiben.")
        return 0

    uebersprungen = []
    geschrieben = 0
    for d, eintraege in nb.items():
        p = alle[d]["pfad"]
        h = io.open(p, encoding="utf-8").read()
        neu = block(eintraege, alle)
        if START in h:
            h = re.sub(re.escape(START) + r".*?" + re.escape(ENDE), neu, h, flags=re.S)
        else:
            anker = next((a for a in ANKER if a in h), None)
            if anker is None:
                print(f"   {d}: kein Anker gefunden, übersprungen")
                uebersprungen.append(d)
                continue
            h = h.replace(anker, neu + "\n\n" + anker, 1)
        if "verwandt-label" not in h.split("</head>")[0] and ".verwandt{" not in h:
            h = h.replace("</head>", CSS + "\n</head>", 1)
        io.open(p, "w", encoding="utf-8").write(h)
        geschrieben += 1
    print(f"\n{geschrieben} von {len(nb)} Datenstücken geschrieben"
          + (f", übersprungen: {uebersprungen}" if uebersprungen else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
