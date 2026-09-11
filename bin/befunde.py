#!/usr/bin/env python3
"""Sammelt die befunde.json aller Datenstücke zu einem Index.

  befunde.py                 Überblick: Abdeckung, Warnungen
  befunde.py --index         schreibt befunde-index.json im Repo-Wurzelverzeichnis
  befunde.py --suche BEGRIFF durchsucht Behauptungen und Themen
  befunde.py --pruefen       listet Befunde, die zu lange nicht geprüft wurden

Ein Befund ist eine Tatsachenbehauptung mit Quelle, Ampel und Prüfdatum.
Die Datei BEFUNDE.md beschreibt das Format.
"""
import json, sys, glob, os, re
from datetime import date, datetime

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMPEL = {"gruen": "🟢", "gelb": "🟡", "rot": "🔴"}
VERALTET_TAGE = 365


def stuecke():
    """Alle Datenstück-Verzeichnisse, unabhängig davon ob sie Befunde haben."""
    aus = []
    for p in sorted(glob.glob(os.path.join(WURZEL, "*/"))):
        name = os.path.basename(p.rstrip("/"))
        if name in ("fonts", "bin", ".git"):
            continue
        if not os.path.exists(os.path.join(p, "index.html")):
            continue
        aus.append(name)
    return aus


def lade(name):
    p = os.path.join(WURZEL, name, "befunde.json")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def pruefe(name, d):
    """Formale Prüfung. Gibt eine Liste von Beanstandungen zurück."""
    fehler = []
    if d.get("schema") != "befunde/v1":
        fehler.append("unbekanntes Schema")
    quellen = {q["id"] for q in d.get("quellen", [])}
    for b in d.get("befunde", []):
        wo = f"{name}/{b.get('id','?')}"
        if not b.get("behauptung"):
            fehler.append(f"{wo}: keine Behauptung")
        if b.get("ampel") not in AMPEL:
            fehler.append(f"{wo}: Ampel fehlt oder unbekannt")
        if not b.get("geprueft_am"):
            fehler.append(f"{wo}: kein Prüfdatum")
        for q in b.get("quelle", []):
            if q not in quellen:
                fehler.append(f"{wo}: Quelle '{q}' nicht deklariert")
        if b.get("ampel") == "gelb" and not b.get("einschraenkung"):
            fehler.append(f"{wo}: gelb ohne Einschränkung — dann ist es grün oder rot")
    return fehler


def sammeln():
    alles, ohne, fehler = [], [], []
    for name in stuecke():
        d = lade(name)
        if d is None:
            ohne.append(name)
            continue
        fehler += pruefe(name, d)
        for b in d.get("befunde", []):
            b = dict(b)
            b["_stueck"] = d["stueck"]["id"]
            b["_titel"] = d["stueck"]["titel"]
            b["_url"] = d["stueck"].get("url", "")
            b["_thema"] = d["stueck"].get("thema", [])
            b["_quellen"] = {q["id"]: q for q in d.get("quellen", [])}
            b["_nicht_belegt"] = d.get("nicht_belegt", [])
            alles.append(b)
    return alles, ohne, fehler


def alter(b):
    try:
        return (date.today() - datetime.fromisoformat(b["geprueft_am"]).date()).days
    except Exception:
        return None


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    alles, ohne, fehler = sammeln()

    if arg == "--suche":
        if len(sys.argv) < 3:
            print("Suchbegriff fehlt"); return 1
        q = sys.argv[2].lower()
        treffer = [b for b in alles
                   if q in b["behauptung"].lower()
                   or any(q in t.lower() for t in b["_thema"])]
        print(f"{len(treffer)} Treffer für „{sys.argv[2]}“\n")
        for b in treffer:
            print(f"{AMPEL.get(b['ampel'],'?')} {b['behauptung']}")
            print(f"   aus: {b['_titel']} · geprüft {b['geprueft_am']}")
            if b.get("einschraenkung"):
                print(f"   Einschränkung: {b['einschraenkung']}")
            print()
        return 0

    if arg == "--pruefen":
        alt = [(alter(b), b) for b in alles]
        alt = [(a, b) for a, b in alt if a is not None and a > VERALTET_TAGE]
        alt.sort(reverse=True)
        if not alt:
            print(f"Kein Befund ist älter als {VERALTET_TAGE} Tage.")
            return 0
        print(f"{len(alt)} Befunde seit über {VERALTET_TAGE} Tagen nicht geprüft:\n")
        for a, b in alt:
            print(f"  {a:>4} Tage  {b['_titel']}: {b['behauptung'][:70]}")
        return 0

    if arg == "--index":
        ziel = os.path.join(WURZEL, "befunde-index.json")
        idx = {"erzeugt": date.today().isoformat(), "anzahl": len(alles),
               "stuecke_mit_befunden": len({b["_stueck"] for b in alles}),
               "stuecke_ohne_befunde": ohne, "befunde": alles}
        with open(ziel, "w", encoding="utf-8") as f:
            json.dump(idx, f, ensure_ascii=False, indent=1)
        print(f"{ziel} geschrieben: {len(alles)} Befunde aus "
              f"{idx['stuecke_mit_befunden']} Stücken")
        return 0

    # Standard: Überblick
    ges = len(stuecke())
    mit = ges - len(ohne)
    print(f"Datenstücke: {ges}   mit Befunden: {mit}   ohne: {len(ohne)}")
    print(f"Befunde gesamt: {len(alles)}")
    if alles:
        v = {}
        for b in alles:
            v[b["ampel"]] = v.get(b["ampel"], 0) + 1
        print("  " + "   ".join(f"{AMPEL.get(k,k)} {n}" for k, n in sorted(v.items())))
    if ohne:
        print(f"\nOhne befunde.json ({len(ohne)}):")
        for n in ohne:
            print(f"   {n}")
    if fehler:
        print(f"\nBeanstandungen ({len(fehler)}):")
        for f_ in fehler:
            print(f"   {f_}")
    else:
        print("\nKeine formalen Beanstandungen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
