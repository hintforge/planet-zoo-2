# -*- coding: utf-8 -*-
"""Parse the Planet Zoo 2 guide into data/*.json for the Accreditation tree.

Run from anywhere (standard library only):

    python -I extract.py

Reads, relative to this file's parent (the guide folder):
    animals/accreditation.md        one row per species (tiers, release, gates)
    items/research_tree.md          per-species research rows (any table whose
                                    header is Species | Levels | Level-by-level
                                    unlocks | Research gate), level spread, gates
    sections/career_progression.md  Career medal counts per tier; level chapters
    mechanics.md                    Franchise tier gates (zoos / reserves / stars)
    research_briefs/source_register.md  resolves "P2 ref N" numbers to URLs

Writes data/accreditation.json, data/research.json, data/gates.json.
Problems that do not stop the build are printed as WARNING lines.
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.dirname(HERE)
OUT = os.path.join(HERE, "data")

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    sys.stderr.write("WARNING: %s\n" % msg)


def read_lines(rel):
    path = os.path.join(GUIDE, *rel.split("/"))
    with io.open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


# ---------------------------------------------------------------- markdown

def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_row(line):
    s = line.strip()
    return len(s) > 1 and s.startswith("|") and s.endswith("|")


def find_tables(lines):
    """Yield dicts: header, rows, start, end (index of last row), heading."""
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{1,6}\s", line):
            heading = line.lstrip("#").strip()
        if is_row(line) and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = split_row(line)
            j = i + 2
            rows = []
            while j < len(lines) and is_row(lines[j]):
                rows.append(split_row(lines[j]))
                j += 1
            yield {"header": header, "rows": rows, "start": i, "end": j - 1, "heading": heading}
            i = j
            continue
        i += 1


def source_after(lines, idx):
    """First _source: line after line idx, stopping at a heading or table."""
    j = idx + 1
    while j < len(lines):
        s = lines[j].strip()
        if s.startswith("_source:"):
            return s
        if s and (s.startswith("#") or is_row(s)):
            return ""
        j += 1
    return ""


URL_RE = re.compile(r"https?://[^\s;,\)\]\`\"']+")


def urls_in(text):
    seen = []
    for u in URL_RE.findall(text):
        u = u.rstrip(".:")
        if u not in seen:
            seen.append(u)
    return seen


def host(url):
    m = re.match(r"https?://(?:www\.)?([^/]+)", url)
    return m.group(1) if m else url


def link(url, label=None):
    if not label:
        label = host(url)
        if label == "wikily.gg":  # many different pages; name the page
            label += "/" + url.rstrip("/").split("/")[-1]
    return {"label": label, "url": url}


def spoiler_of(src):
    m = re.search(r"spoiler:\s*([a-z-]+)", src)
    return m.group(1) if m else "none"


def para_after_start(lines, start):
    """(text, source line) for the paragraph line that starts with `start`."""
    for i, line in enumerate(lines):
        if line.startswith(start):
            return line.strip(), source_after(lines, i)
    return "", ""


def slugify(name):
    s = name.lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


# ----------------------------------------------------------- accreditation

def parse_accreditation():
    lines = read_lines("animals/accreditation.md")
    species = []
    seen = set()
    for t in find_tables(lines):
        h = t["header"]
        if not (h and h[0] == "Species" and "Career tier" in h and "Franchise tier" in h):
            continue
        ci, fi = h.index("Career tier"), h.index("Franchise tier")
        oi = h.index("Obtained")
        ri = [k for k, c in enumerate(h) if c.startswith("Release group")][0]
        gi = h.index("Other gates")
        src = source_after(lines, t["end"])
        spoil = spoiler_of(src)
        all_urls = urls_in(src)
        tier_links = [link(u) for u in all_urls
                      if "release-groups" not in u and "zoopedia" not in u][:4]
        release_links = [link(u) for u in all_urls if "release-groups" in u][:1]
        deluxe_links = [link(u) for u in all_urls if "zoopedia" in u][:1]
        for r in t["rows"]:
            name = r[0]
            if name in seen:
                warn("duplicate species row: %s" % name)
                continue
            seen.add(name)
            try:
                career, franchise = int(r[ci]), int(r[fi])
            except ValueError:
                warn("non-numeric tier for %s: %r / %r" % (name, r[ci], r[fi]))
                continue
            rel_raw = r[ri]
            if rel_raw.startswith("yes (reserve"):
                rel = "reserve"
            elif rel_raw.startswith("yes"):
                rel = "yes"
            elif rel_raw.startswith("no group"):
                rel = "none"
            else:
                rel = "unknown"
            other = r[gi]
            other = "" if other in ("--", "") else other
            m = re.search(r"release group needs research level (\d+)", other)
            rel_level = int(m.group(1)) if m else None
            rel_no_research = "needs no research" in other
            species.append({
                "name": name,
                "slug": slugify(name),
                "career": career,
                "franchise": franchise,
                "obtained": r[oi],
                "release": rel,
                "release_raw": rel_raw,
                "other": other,
                "deluxe": "Deluxe Edition" in other,
                "release_research_level": rel_level,
                "release_no_research": rel_no_research,
                "spoiler": spoil,
                "src": {"tier": tier_links, "release": release_links, "deluxe": deluxe_links},
            })
    # guide-declared counts, for cross-checking
    text = "\n".join(lines)
    exp_f = re.search(r"\((\d+) / (\d+) / (\d+) / (\d+) / (\d+) = 136", text)
    exp_c = re.search(r"by tier (\d+) of \d+ \(tier 1\), (\d+) of \d+ \(tier 2\), "
                      r"(\d+) of \d+ \(tier 3\), (\d+) of \d+ \(tier 4\)", text)
    expected = {
        "franchise": [int(x) for x in exp_f.groups()] if exp_f else None,
        "career": ([int(x) for x in exp_c.groups()] + [0]) if exp_c else None,
    }
    counts = {"career": [0] * 5, "franchise": [0] * 5}
    for s in species:
        for mode in ("career", "franchise"):
            tier = s[mode]
            if 1 <= tier <= 5:
                counts[mode][tier - 1] += 1
            else:
                warn("%s has %s tier %d outside 1-5" % (s["name"], mode, tier))
    for mode in ("career", "franchise"):
        if expected[mode] and expected[mode] != counts[mode]:
            warn("%s per-tier counts %s differ from the guide's stated %s"
                 % (mode, counts[mode], expected[mode]))
    if len(species) != 136:
        warn("expected 136 species, parsed %d" % len(species))

    how_text, how_src = para_after_start(lines, "Every species is obtained by adopting")
    how = how_text.split("tier lock.")[0] + "tier lock." if "tier lock." in how_text else how_text
    other_text, other_src = para_after_start(lines, '"Other gates" lists')
    rel_text, rel_src = para_after_start(lines, 'The "Release group" column says')
    mode_text, mode_src = para_after_start(lines, "Career and Franchise keep separate")
    add_text, add_src = para_after_start(lines, "Each tier adds species to")
    return {
        "species": species,
        "counts": counts,
        "expected_counts": expected,
        "how_obtained": how,
        "how_src": [link(u) for u in urls_in(how_src)][:3],
        "other_gates_src": [link(u) for u in urls_in(other_src) if "release-groups" not in u][:3],
        "release_src": [link(u) for u in urls_in(rel_src)][:2],
        "mode_src": [link(u) for u in urls_in(mode_src)][:3],
        "adds_src": [link(u) for u in urls_in(add_src)][:3],
    }


# --------------------------------------------------------- source register

def parse_register():
    reg = {"P1": {}, "P2": {}}
    try:
        lines = read_lines("research_briefs/source_register.md")
    except IOError:
        warn("source_register.md not found; gate source links will be missing")
        return reg
    cur = None
    for line in lines:
        if line.startswith("## P1 references"):
            cur = "P1"
        elif line.startswith("## P2 references"):
            cur = "P2"
        elif line.startswith("## "):
            cur = None
        elif cur:
            m = re.match(r"^(\d+)\.\s+(https?://\S+)", line)
            if m:
                reg[cur][int(m.group(1))] = m.group(2)
    return reg


# ------------------------------------------------------------------- gates

def parse_chapters():
    """Map level location -> chapter number, for spoiler handling."""
    lines = read_lines("sections/career_progression.md")
    out = {}
    for t in find_tables(lines):
        h = t["header"]
        if "Location" in h and "Chapter" in h and "Type" in h:
            li, ci, ti = h.index("Location"), h.index("Chapter"), h.index("Type")
            for r in t["rows"]:
                try:
                    out[r[li]] = {"chapter": int(r[ci]), "type": r[ti]}
                except ValueError:
                    pass
    return out


def parse_gates(reg, species_total):
    gates = {"career": {}, "franchise": {}}
    # Career: "Career Accreditation (gate structure)" table
    c_lines = read_lines("sections/career_progression.md")
    for t in find_tables(c_lines):
        h = t["header"]
        if h[:2] == ["Tier", "Career medals needed"]:
            src = source_after(c_lines, t["end"])
            srcs = []
            for m in re.finditer(r"\bref (\d+)", src):
                u = reg["P1"].get(int(m.group(1)))
                if u and link(u) not in srcs:
                    srcs.append(link(u))
            for r in t["rows"]:
                n = int(r[0])
                med = re.match(r"(\d+) Bronze, (\d+) Silver", r[1])
                if med:
                    b, s = int(med.group(1)), int(med.group(2))
                    gate = "Earn at least %d Bronze and %d Silver Career medals." % (b, s)
                    medals = {"bronze": b, "silver": s}
                else:
                    gate = "You start here." if "Starting" in r[1] else r[1]
                    medals = None
                extras = []
                level_opens = False
                for part in [p.strip() for p in r[2].split(";")]:
                    if re.search(r"species in trading", part):
                        continue
                    if re.search(r"storage", part, re.I):
                        extras.append(part.lstrip("+").strip() and
                                      ("+50 animal storage slots" if "50" in part else part))
                    elif part:
                        level_opens = True
                if level_opens:
                    extras.insert(0, "a new Career level (reach it through the Planet Hub)")
                gates["career"][n] = {"n": n, "gate": gate, "medals": medals,
                                      "extras": extras, "sources": srcs[:2]}
    # Franchise: gate rows F2-F7 in mechanics.md
    m_lines = read_lines("mechanics.md")
    for t in find_tables(m_lines):
        h = t["header"]
        if h[:3] != ["#", "Gate", "Detail"]:
            continue
        src = source_after(m_lines, t["end"])
        for r in t["rows"]:
            mm = re.match(r"Tier (\d)$", r[1])
            if not mm:
                continue
            n = int(mm.group(1))
            detail = re.sub(r"\(P2 refs?[^)]*\)", "", r[2])
            detail = re.sub(r"\(spoiler[^)]*\)", "", detail).strip()
            req, _, rest = detail.partition(":")
            req = re.sub(r"(\d+ (?:Reputation|Biodiversity))(?! stars)", r"\1 stars", req.strip())
            rest = re.sub(r"^\s*\+\d+ species( including [^,]+)?,?\s*", "", rest).strip()
            rest = re.sub(r"(\+\d+ \w+), (\+\d+ \w+) marketing( slots?)?",
                          r"\1 and \2 marketing slots", rest)
            extras = [x.strip() for x in rest.split(",") if x.strip()]
            refs = [int(x) for x in re.findall(r"P2 refs? ([\d, ]+)", r[2])
                    for x in re.split(r"[, ]+", x) if x]
            if not refs:
                # no refs on the row: use the two guides the table's source line names
                mc = re.search(r"corroborated by two guides: P2 refs (\d+), (\d+)", src)
                if mc:
                    refs = [int(mc.group(1)), int(mc.group(2))]
                else:
                    refs = [int(x) for x in re.findall(r"P2 ref (\d+)", src)]
            srcs = []
            for ref in refs:
                u = reg["P2"].get(ref)
                if u and link(u) not in srcs:
                    srcs.append(link(u))
            gates["franchise"][n] = {
                "n": n,
                "gate": "Have " + req.replace(" AND ", " and ") + ".",
                "extras": extras, "sources": srcs[:2], "_src_line": src}
    # Franchise tier 1 and the tier rows missing from the table
    f_start = None
    for line in m_lines:
        m = re.search(r"First zoo starts at Tier 1", line)
        if m:
            f_start = line
    gates["franchise"].setdefault(1, {"n": 1, "gate": "You start here.", "extras": [], "sources": []})
    if f_start:
        refs = [int(x) for x in re.findall(r"\b(\d{2})\b", re.findall(r"\(P2 refs?([^)]*)\)", f_start)[0])] \
            if re.findall(r"\(P2 refs?([^)]*)\)", f_start) else []
        srcs = [link(reg["P2"][x]) for x in refs if x in reg["P2"]]
        gates["franchise"][1]["sources"] = srcs[:2]
    # Research network pieces handed out by tier (items/research_tree.md)
    r_lines = read_lines("items/research_tree.md")
    r_text = "\n".join(r_lines)
    mnet = re.search(r"(Observation Platform) at tier 1, (Camera Trap) at tier 2, (Acoustic Monitor) at tier 3", r_text)
    mcar = re.search(r"Career: (Camera Trap) at tier 2 and (Acoustic Monitor) at tier 3", r_text)
    nets = {"franchise": {}, "career": {}}
    if mnet:
        nets["franchise"] = {1: mnet.group(1), 2: mnet.group(2), 3: mnet.group(3)}
    if mcar:
        nets["career"] = {2: mcar.group(1), 3: mcar.group(2)}
    for mode in ("franchise", "career"):
        for n, piece in nets[mode].items():
            g = gates[mode].get(n)
            if not g:
                continue
            g["extras"] = [e for e in g["extras"] if e.lower() != piece.lower()]
            g["extras"].append("Research network piece: %s" % piece)
    for mode in gates:
        for g in gates[mode].values():
            g.pop("_src_line", None)
    return gates


# ---------------------------------------------------------------- research

def split_levels(text):
    """'L1 ...; L2 ...' -> (steps, trailing note)."""
    note = ""
    parts = re.split(r";\s*(?=L\d\b)", text.strip())
    steps = []
    for k, part in enumerate(parts):
        m = re.match(r"L(\d)\s+(.*)$", part, re.S)
        if not m:
            warn("could not read level text: %r" % part[:60])
            continue
        body = m.group(2).strip()
        if k == len(parts) - 1:
            mm = re.search(r"\.\s+(?=[A-Z])", body)
            if mm:
                note = body[mm.end():].strip()
                body = body[:mm.start()].strip()
        body = body.rstrip(".")
        shown = re.sub(r"\bTR(\d)\b", r"Thriving Requirement \1", body)
        shown = shown.replace("Fert 1", "Fertility 1 (+15%)").replace("Fert 2", "Fertility 2 (+30%)")
        tags = []
        if "Fert" in body:
            tags.append("fertility")
        if "fact sheet" in body:
            tags.append("factsheet")
        if "release group" in body:
            tags.append("release")
        if re.search(r"\bTR\d", body):
            tags.append("thriving")
        steps.append({"n": int(m.group(1)), "raw": body, "text": shown, "tags": tags})
    return steps, note


def parse_research(species_names, chapters):
    lines = read_lines("items/research_tree.md")
    text = "\n".join(lines)
    known = set(species_names)
    docs = {}
    for t in find_tables(lines):
        h = t["header"]
        if h[:4] != ["Species", "Levels", "Level-by-level unlocks", "Research gate"]:
            continue
        src = source_after(lines, t["end"])
        spoil = spoiler_of(src)
        src_text = src
        all_urls = urls_in(src)
        base = next((u for u in all_urls if "/research/" in u or u.endswith("/research")), "")
        for r in t["rows"]:
            name = r[0].strip()
            if not name or name.startswith("(") or name.startswith("<") or name.lower().startswith("species name"):
                continue  # blank template row
            if name not in known:
                warn("research row for unknown species %r (check the name against animals/accreditation.md)" % name)
                continue
            if name in docs:
                warn("research row repeated for %s; the later one wins" % name)
            try:
                nlev = int(r[1])
            except ValueError:
                warn("Levels for %s is not a number: %r" % (name, r[1]))
                continue
            steps, note = split_levels(r[2])
            if len(steps) != nlev:
                warn("%s: Levels says %d but %d level entries were read" % (name, nlev, len(steps)))
            slug = slugify(name)
            page = None
            if re.search(r"(?<![a-z0-9-])%s(?![a-z0-9-])" % re.escape(slug), src_text):
                page = "https://wikily.gg/planet-zoo-2/research/%s" % slug
            srcs = [link(page, "Research page")] if page else []
            if not srcs and all_urls:
                srcs = [link(all_urls[0])]
            gate = None
            graw = r[3].strip()
            if graw and graw.lower() not in ("none", "--", "-"):
                mm = re.match(r"Before L(\d): (.*?) in (.+?) and the species released there", graw)
                if mm:
                    reserve = mm.group(3)
                    info = None
                    for loc, v in chapters.items():
                        if loc == reserve or loc.startswith(reserve):
                            info = v
                    gate = {"raw": graw, "before_level": int(mm.group(1)),
                            "reserve": reserve,
                            "reserve_chapter": info["chapter"] if info else None}
                else:
                    gate = {"raw": graw, "before_level": None, "reserve": None,
                            "reserve_chapter": None}
            docs[name] = {"levels": nlev, "steps": steps, "note": note,
                          "gate": gate, "spoiler": spoil, "src": srcs}
    # framework facts
    dist = {}
    m = re.search(r"3 levels for (\d+) species, 4 levels for (\d+), 5 for (\d+), 6 for (\d+)", text)
    if m:
        dist = {"3": int(m.group(1)), "4": int(m.group(2)), "5": int(m.group(3)), "6": int(m.group(4))}
    else:
        warn("level spread (3/4/5/6 levels) not found in research_tree.md")
    gated = re.search(r"(\d+) species open their later levels only after", text)
    grv = []
    mg = re.search(r"Great Rift Valley list \(\d+\) is named on the Wikily species page: ([^.]+)\.", text)
    if mg:
        grv = [x.strip() for x in mg.group(1).split(",")]
        for x in grv:
            if x not in known:
                warn("Great Rift Valley list name not a known species: %s" % x)
    rel_no = re.search(r"need no research for (\d+) species", text)
    framework_src = []
    for i, line in enumerate(lines):
        if line.startswith("58 species open their later levels"):
            framework_src = [link(u) for u in urls_in(source_after(lines, i)) if "/research" in u][:2]
    return {
        "documented": docs,
        "spread": dist,
        "gated_total": int(gated.group(1)) if gated else None,
        "grv_gated": grv,
        "release_no_research": int(rel_no.group(1)) if rel_no else None,
        "framework_src": framework_src,
    }


def write(name, obj):
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write("\n")


def main():
    acc = parse_accreditation()
    names = [s["name"] for s in acc["species"]]
    reg = parse_register()
    chapters = parse_chapters()
    gates = parse_gates(reg, len(names))
    research = parse_research(names, chapters)
    for mode in ("career", "franchise"):
        for n in range(1, 6):
            if n not in gates[mode]:
                warn("no %s gate text found for tier %d" % (mode, n))
    gates_out = {mode: [gates[mode][n] for n in sorted(gates[mode])] for mode in gates}
    write("accreditation.json", acc)
    write("research.json", research)
    write("gates.json", gates_out)
    print("species: %d | career per tier %s | franchise per tier %s"
          % (len(acc["species"]), acc["counts"]["career"], acc["counts"]["franchise"]))
    print("research documented: %d of %d species" % (len(research["documented"]), len(names)))
    print("warnings: %d" % len(WARNINGS))


if __name__ == "__main__":
    main()
