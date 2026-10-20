# -*- coding: utf-8 -*-
"""Rebuild accreditation_tree.html from the Planet Zoo 2 guide.

Run after the guide changes (standard library only):

    python -I build.py

It runs extract.py, merges data/accreditation.json, data/research.json and
data/gates.json, and swaps the result into the JSON data block inside
accreditation_tree.html. The page's markup, styling and script are left alone.
The finished file is self-contained: no network, no external libraries.
"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "accreditation_tree.html")
DATA = os.path.join(HERE, "data")
ISLAND = "tree-data"


def load(name):
    with io.open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


def merge():
    acc, res, gates = load("accreditation.json"), load("research.json"), load("gates.json")
    documented = res["documented"]
    species = []
    for s in acc["species"]:
        rec = dict(s)
        rec["research"] = documented.get(s["name"])
        species.append(rec)
    species.sort(key=lambda r: r["name"])
    return {
        "species": species,
        "modes": {
            "career": {"label": "Career", "tiers": gates["career"]},
            "franchise": {"label": "Franchise", "tiers": gates["franchise"]},
        },
        "coverage": {"documented": len(documented), "total": len(species)},
        "research": {
            "spread": res["spread"],
            "gated_total": res["gated_total"],
            "grv_gated": res["grv_gated"],
            "framework_src": res["framework_src"],
        },
        "how_obtained": acc["how_obtained"],
        "how_src": acc["how_src"],
        "other_gates_src": acc["other_gates_src"],
        "mode_src": acc["mode_src"],
    }


def main():
    result = subprocess.call([sys.executable, "-I", os.path.join(HERE, "extract.py")])
    if result != 0:
        sys.exit("extract.py failed with exit code %d" % result)
    payload = merge()
    compact = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    safe = compact.replace("</", "<\\/")
    with io.open(PAGE, encoding="utf-8") as fh:
        html = fh.read()
    pattern = re.compile(r'(<script id="%s" type="application/json">)(.*?)(</script>)' % ISLAND, re.S)
    if not pattern.search(html):
        sys.exit("data block '%s' not found in accreditation_tree.html" % ISLAND)
    html = pattern.sub(lambda m: m.group(1) + safe + m.group(3), html, count=1)
    with io.open(PAGE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print("embedded %d species (%d with research) into %s (%.0f KB)"
          % (len(payload["species"]), payload["coverage"]["documented"], os.path.basename(PAGE),
             len(html.encode("utf-8")) / 1024.0))


if __name__ == "__main__":
    main()
