# -*- coding: utf-8 -*-
"""Rebuild reserve_ecosystems.html from the Planet Zoo 2 guide.

Run after the guide changes (or after typing player screenshots into the fill template):

    python -I build_ecosystems.py

It runs extract_ecosystems.py, then swaps the data into the three data blocks inside
reserve_ecosystems.html. The page's markup, styling and script are left untouched.
Reserves whose level names are tier 0 in the guide (chapter 1) go in the open data and show
at once. The tier 1 and tier 2 reserves (chapters 2-3 and chapter 4; the extractor reads
the tiers from the guide) go in as encoded text, so no such reserve name sits in the page
source in readable form until the reader asks for them.
Standard library only.
"""
import base64
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "reserve_ecosystems.html")
DATA = os.path.join(HERE, "data", "ecosystems.json")


def run(script):
    path = os.path.join(HERE, script)
    code = subprocess.call([sys.executable, "-I", path])
    if code != 0:
        sys.exit("%s failed with exit code %d" % (script, code))


def embed(html, block_id, mime, payload):
    pattern = re.compile(r'(<script id="%s" type="%s">)(.*?)(</script>)' % (block_id, re.escape(mime)), re.S)
    if not pattern.search(html):
        sys.exit("data block '%s' not found in reserve_ecosystems.html" % block_id)
    safe = payload.replace("</", "<\\/")
    return pattern.sub(lambda m: m.group(1) + safe + m.group(3), html, count=1)


def compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def main():
    run("extract_ecosystems.py")
    with io.open(DATA, encoding="utf-8") as fh:
        data = json.load(fh)
    html = io.open(PAGE, encoding="utf-8").read()

    html = embed(html, "data-open", "application/json", compact(data["open"]))
    for key, block in (("tier1", "data-t1"), ("tier2", "data-t2")):
        enc = base64.b64encode(compact(data[key]).encode("utf-8")).decode("ascii")
        html = embed(html, block, "text/plain", enc)

    # Checks on the finished page.
    for key, want in (("tier1", 1), ("tier2", 2)):
        for r in data[key]:
            if r["tier"] != want:
                sys.exit("%s is in %s but carries tier %s" % (r["name"], key, r["tier"]))
    for r in data["open"]["reserves0"]:
        if r["tier"] != 0:
            sys.exit("%s is shown by default but carries tier %s" % (r["name"], r["tier"]))
    names =[r["name"] for r in data["tier1"] + data["tier2"]] + [r["full"] for r in data["tier1"] + data["tier2"]]
    visible = re.sub(r'(<script id="data-t[12]" type="text/plain">)(.*?)(</script>)', r"\1\3", html, flags=re.S)
    leaked = [n for n in names if re.search(r"\b%s\b" % re.escape(n), visible)]
    if leaked:
        sys.exit("reserve names readable in the page source: %s" % leaked)
    if re.search(r"[A-Za-z]:\\|[A-Za-z0-9_/]+\.md\b|/Guides/", html):
        sys.exit("a local path or file name is on the page")

    with io.open(PAGE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)

    # Coverage report.
    species = data["open"]["species"]
    every = data["open"]["reserves0"] + data["tier1"] + data["tier2"]
    steps = {r["name"]: len(r["steps"]) for r in every}
    print("species in lookup: %d; with release rows documented: %d" % (len(species), data["open"]["counts"]["speciesReqKnown"]))
    for r in every:
        covered = sum(1 for sp in r["releasable"] if sp in species and sp in r["routes"])
        print("  tier %d %-18s %d steps, lookup route found for %d of %d releasable species"
              % (r["tier"], r["name"], steps[r["name"]], covered, len(r["releasable"])))
        if covered != len(r["releasable"]):
            sys.exit("lookup does not cover every releasable species of %s" % r["name"])
    print("wrote reserve_ecosystems.html (%d bytes)" % os.path.getsize(PAGE))


if __name__ == "__main__":
    main()
