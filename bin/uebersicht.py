#!/usr/bin/env python3
"""Erzeugt die Uebersichtstabelle in der README aus den Datenstuecken selbst.

  uebersicht.py            zeigt die Tabelle
  uebersicht.py --setzen   schreibt sie zwischen die Marker in README.md

Die Tabelle stand bis 14.09.2026 von Hand in der README und endete bei #15,
waehrend es schon 22 Stuecke gab. Handgepflegte Uebersichten driften. Diese
hier wird bei jedem Lauf vollstaendig ersetzt.
"""
import glob, io, json, os, re, sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START = "<!-- UEBERSICHT:START -->"
ENDE = "<!-- UEBERSICHT:ENDE -->"


def spuren():
    p = os.path.join(WURZEL, "bin", "verwandt.json")
    if not os.path.exists(p):
        return {}
    konf = json.load(io.open(p, encoding="utf-8"))
    zu = {}
    for s in konf["spuren"].values():
        for d in s["stuecke"]:
            zu.setdefault(d, []).append(s["titel"])
    return zu


def stuecke():
    aus = []
    for p in glob.glob(os.path.join(WURZEL, "*/index.html")):
        d = os.path.basename(os.path.dirname(p))
        h = io.open(p, encoding="utf-8").read()
        m = re.search(r"Datenstück #(\d+)", h)
        if not m:
            continue
        t = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        roh = re.sub(r"<br\s*/?>", " ", t.group(1)) if t else d
        titel = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", roh)).strip()
        desc = re.search(r'<meta name="description" content="([^"]*)"', h)
        roh_d = desc.group(1) if desc else ""
        # Satzende ist Punkt + Leerzeichen + Grossbuchstabe, nicht der Tausenderpunkt
        satz = re.split(r"(?<=[a-zäöüß])\.\s+(?=[A-ZÄÖÜ])", roh_d)[0]
        thema = satz if len(satz) <= 88 else satz[:85].rsplit(" ", 1)[0] + "…"
        aus.append({"nr": int(m.group(1)), "slug": d, "titel": titel, "thema": thema})
    return sorted(aus, key=lambda x: -x["nr"])


def tabelle():
    zu = spuren()
    z = ["| # | Titel | Thema | Spur |", "|---|-------|-------|------|"]
    for s in stuecke():
        spur = ", ".join(zu.get(s["slug"], [])) or "—"
        z.append(f'| {s["nr"]} | [{s["titel"]}](https://opendataminded.de/{s["slug"]}/) '
                 f'| {s["thema"]} | {spur} |')
    return "\n".join(z)


def main():
    tab = tabelle()
    if "--setzen" not in sys.argv:
        print(tab)
        print(f"\n{len(stuecke())} Zeilen. Mit --setzen in die README schreiben.")
        return 0
    p = os.path.join(WURZEL, "README.md")
    s = io.open(p, encoding="utf-8").read()
    neu = f"{START}\n{tab}\n{ENDE}"
    if START in s:
        s = re.sub(re.escape(START) + r".*?" + re.escape(ENDE), neu, s, flags=re.S)
    else:
        alt = re.search(r"\| # \| Titel.*?(?=\n\n|\n###|\n##)", s, re.S)
        if not alt:
            print("Keine bestehende Tabelle gefunden, Marker nicht gesetzt.")
            return 1
        s = s[:alt.start()] + neu + s[alt.end():]
    io.open(p, "w", encoding="utf-8").write(s)
    print(f"README-Tabelle ersetzt: {len(stuecke())} Zeilen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
