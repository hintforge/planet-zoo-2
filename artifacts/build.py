# -*- coding: utf-8 -*-
"""Rebuild accreditation_tree.html from the Planet Zoo 2 guide.

Run after the guide changes (standard library only):

    python -I build.py

It runs extract.py, merges data/accreditation.json, data/research.json and
data/gates.json, and swaps the result into the JSON data block inside
accreditation_tree.html. The page's markup, styling and script are left alone.
The finished file is self-contained: no network, no external libraries.

Spoilers: a research gate that names a Wildlife Reserve from a later chapter keeps that name
out of the readable page source. The tier comes from the guide's own career table each time
the page is built (chapter 1 = tier 0, chapters 2-3 = tier 1, chapter 4 = tier 2); tier 0
names stay in the open data, every other gate's reserve name and raw text go into one
base64 block ("tree-hidden") that the page decodes only when the reader presses "Show which
one". The build refuses to finish if a hidden reserve name is still readable in the page.
"""
import base64
import importlib.util
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
HIDDEN = "tree-hidden"


def load(name):
    with io.open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


def chapter_tier(chapter):
    """Tier of a career chapter, per the guide: 1 -> 0, 2-3 -> 1, 4 -> 2. Unknown -> hidden (tier 1)."""
    if chapter == 1:
        return 0
    if chapter in (2, 3):
        return 1
    if chapter == 4:
        return 2
    return 1


def guide_chapters():
    """The extractor's own reading of sections/career_progression.md (location -> chapter, type)."""
    spec = importlib.util.spec_from_file_location("pz2_extract", os.path.join(HERE, "extract.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.parse_chapters()


def hide_gates(species):
    """Move the reserve name of every non-tier-0 gate out of the open data. Returns {species: secret}."""
    hidden = {}
    for rec in species:
        res = rec.get("research")
        gate = res and res.get("gate")
        if not gate:
            continue
        tier = chapter_tier(gate.get("reserve_chapter"))
        gate.pop("reserve_chapter", None)
        gate["tier"] = tier
        if gate.get("reserve") is not None and tier > 0:
            hidden[rec["name"]] = {"reserve": gate["reserve"], "raw": gate["raw"], "tier": tier}
            gate["reserve"] = None
            gate["raw"] = None
    return hidden


def merge():
    acc, res, gates = load("accreditation.json"), load("research.json"), load("gates.json")
    documented = res["documented"]
    species = []
    for s in acc["species"]:
        rec = dict(s)
        rec["research"] = documented.get(s["name"])
        species.append(rec)
    species.sort(key=lambda r: r["name"])
    hidden = hide_gates(species)
    payload = {
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
    return payload, hidden


def main():
    result = subprocess.call([sys.executable, "-I", os.path.join(HERE, "extract.py")])
    if result != 0:
        sys.exit("extract.py failed with exit code %d" % result)
    payload, hidden = merge()
    compact = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    safe = compact.replace("</", "<\\/")
    secret = base64.b64encode(
        json.dumps(hidden, ensure_ascii=True, separators=(",", ":"), sort_keys=True).encode("ascii")).decode("ascii")
    with io.open(PAGE, encoding="utf-8") as fh:
        html = fh.read()
    pattern = re.compile(r'(<script id="%s" type="application/json">)(.*?)(</script>)' % ISLAND, re.S)
    if not pattern.search(html):
        sys.exit("data block '%s' not found in accreditation_tree.html" % ISLAND)
    html = pattern.sub(lambda m: m.group(1) + safe + m.group(3), html, count=1)
    hpat = re.compile(r'(<script id="%s" type="text/plain">)(.*?)(</script>)' % HIDDEN, re.S)
    if not hpat.search(html):
        sys.exit("data block '%s' not found in accreditation_tree.html" % HIDDEN)
    html = hpat.sub(lambda m: m.group(1) + secret + m.group(3), html, count=1)

    # Check on the finished page: no later-chapter reserve name may be readable in the source.
    names = set()
    for loc, info in guide_chapters().items():
        if info["type"].startswith("Wildlife Reserve") and chapter_tier(info["chapter"]) > 0:
            names.add(loc)
            names.add(re.sub(r"\s+Reserve$", "", loc))
    for h in hidden.values():
        names.add(h["reserve"])
        names.add(re.sub(r"\s+Reserve$", "", h["reserve"]))
    names.discard("")
    visible = hpat.sub(lambda m: m.group(1) + m.group(3), html)
    leaked = sorted(n for n in names if re.search(r"\b%s\b" % re.escape(n), visible))
    if leaked:
        sys.exit("reserve names readable in the page source: %s" % leaked)
    print("hidden %d gate(s) behind the reveal block; %d later-chapter reserve names checked, 0 readable"
          % (len(hidden), len(names)))
    with io.open(PAGE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print("embedded %d species (%d with research) into %s (%.0f KB)"
          % (len(payload["species"]), payload["coverage"]["documented"], os.path.basename(PAGE),
             len(html.encode("utf-8")) / 1024.0))


if __name__ == "__main__":
    main()
