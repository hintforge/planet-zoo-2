# -*- coding: utf-8 -*-
"""Parse the Planet Zoo 2 guide into data/ecosystems.json for the Reserve ecosystem planner.

Run from anywhere (standard library only):

    python -I extract_ecosystems.py

Reads, relative to this file's parent (the guide folder):
    animals/reserve_ecosystems.md   ecosystem requirements, Flourishing roles, role-fill lists,
                                    species release rows, suggested setup orders, and the
                                    "Fill template" tables a player's screenshots are typed into
    animals/reserve_releases.md     releasable species per reserve (authoritative list)
    animals/accreditation.md        read only: the Deluxe Edition species names
    sections/career_progression.md  read only: each Wildlife Reserve's chapter, and the spoiler
                                    tier the guide gives each chapter's level names

Writes data/ecosystems.json with three parts:
    open    tier 0 data (ecosystems, roles, species rows, rules, species index) plus
            reserves0, the reserves whose level names are tier 0 in the guide
    tier1   reserves whose level names are puzzle-tier 1 in the guide, and their orders
    tier2   reserves whose level names are puzzle-tier 2 in the guide, and their orders
A reserve's tier comes from its chapter row in sections/career_progression.md and the tier
that file tags that chapter with (no reserve list is written into this script).
The page shows reserves0 straight away and keeps tier1 / tier2 out of sight until the
reader asks for them.

Problems that do not stop the build are printed as WARNING lines; a structural problem
(a reserve's steps not covering its releasable list, an unknown ecosystem) exits non-zero.
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
ERRORS = []


def warn(msg):
    WARNINGS.append(msg)
    sys.stderr.write("WARNING: %s\n" % msg)


def err(msg):
    ERRORS.append(msg)
    sys.stderr.write("ERROR: %s\n" % msg)


def read_lines(rel):
    path = os.path.join(GUIDE, *rel.split("/"))
    with io.open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


# ---------------------------------------------------------------- markdown helpers

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


def table_after(lines, start):
    """First markdown table at or after index `start`: (header, rows, index_after)."""
    i = start
    while i < len(lines) and not is_row(lines[i]):
        i += 1
    if i >= len(lines):
        return None, [], i
    header = split_row(lines[i])
    i += 1
    if i < len(lines) and re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[i]):
        i += 1
    rows = []
    while i < len(lines) and is_row(lines[i]):
        rows.append(split_row(lines[i]))
        i += 1
    return header, rows, i


def next_source(lines, start, limit=6):
    """The first `_source:` line within `limit` lines after `start`."""
    for j in range(start, min(len(lines), start + limit)):
        if lines[j].startswith("_source:"):
            return lines[j]
        if lines[j].startswith("#"):
            break
    return ""


def parse_source(line):
    """Return {text, urls, capture, confidence, puzzle_tier, label, label_plain}."""
    out = {"text": "", "urls": [], "capture": "", "confidence": "", "puzzle_tier": None,
           "label": "", "label_plain": ""}
    if not line:
        return out
    out["text"] = line
    out["urls"] = re.findall(r"https?://[^\s;,\]\)`]+", line)
    m = re.search(r"capture:\s*(.*?)\s*·", line)
    if m:
        out["capture"] = m.group(1)
    m = re.search(r"confidence:\s*(\w+)", line)
    if m:
        out["confidence"] = m.group(1)
    m = re.search(r"puzzle-tier:\s*(\d)", line)
    if m:
        out["puzzle_tier"] = int(m.group(1))
    k = line.rfind("`[")
    if k >= 0:
        lab = line[k + 2:line.rfind("]`")] if line.rfind("]`") > k else line[k + 2:]
        out["label"] = lab
        out["label_plain"] = plain_label(lab)
    return out


def plain_label(lab):
    low = lab.lower()
    m = re.match(r"corroborated:\s*(\d+) sources", low)
    if m:
        return "%s sources agree" % m.group(1)
    if low.startswith("single source"):
        return "one source, not yet cross-checked"
    if low.startswith("contradicted"):
        return "sources disagree"
    if low.startswith("hypothesis"):
        return "unverified guess"
    if low.startswith("derived"):
        return "the guide's own reasoning"
    return lab


def slugify(name):
    s = name.lower()
    s = re.sub(r"[()]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def split_list(text):
    return [x.strip() for x in re.split(r",\s*", text) if x.strip()]


def to_int(txt):
    return int(txt.replace(",", ""))


# ---------------------------------------------------------------- parsers

def parse_nature(text):
    """'Bushes at least 125; Trees 75 to 400' -> list of {item, min, max, text}."""
    out = []
    if not text or text.lower().startswith("none listed"):
        return out
    for part in text.split(";"):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(.*?)\s+at least\s+([\d,]+)$", part)
        if m:
            out.append({"item": m.group(1), "min": to_int(m.group(2)), "max": None, "text": part})
            continue
        m = re.match(r"^(.*?)\s+([\d,]+)\s+to\s+([\d,]+)$", part)
        if m:
            out.append({"item": m.group(1), "min": to_int(m.group(2)), "max": to_int(m.group(3)), "text": part})
            continue
        m = re.match(r"^(.*?)\s+([\d,]+)$", part)
        if m:
            out.append({"item": m.group(1), "min": to_int(m.group(2)), "max": to_int(m.group(2)), "text": part})
            continue
        warn("nature object not understood: %r" % part)
        out.append({"item": part, "min": None, "max": None, "text": part})
    return out


def parse_req(raw):
    """'Either Rocky Hills or Riverine; Flourishing Savannah' -> rows of alternatives."""
    rows, notes = [], []
    for part in raw.split(";"):
        part = part.strip()
        if not part:
            continue
        if part.lower().startswith("also "):
            notes.append(part[5:].strip())
            continue
        body = part
        if body.lower().startswith("either "):
            body = body[7:]
        opts = []
        for o in re.split(r"\s+or\s+", body):
            o = o.strip()
            fl = False
            if o.lower().startswith("flourishing "):
                fl = True
                o = o[12:].strip()
            opts.append({"eco": o, "flourishing": fl})
        rows.append({"either": len(opts) > 1, "options": opts})
    return rows, notes


def parse_ecosystems(lines, warns):
    """The four biome tables -> {name: record}."""
    ecos = {}
    i = 0
    while i < len(lines):
        m = re.match(r"^### (\w+) biome \((\d+) ecosystems\)", lines[i])
        if not m:
            i += 1
            continue
        biome, count = m.group(1), int(m.group(2))
        header, rows, j = table_after(lines, i + 1)
        srcline = next_source(lines, j)
        src = parse_source(srcline)
        base = ""
        mb = re.search(r"\(all under (https?://[^)]+)\)", srcline)
        if mb:
            base = mb.group(1)
        got = 0
        for r in rows:
            if len(r) < 6:
                continue
            name, terrain, also, nature, roles, listed = r[:6]
            slug = slugify(name)
            if slug not in srcline:
                warns("ecosystem %s: page %r not named in its source line" % (name, slug))
            nat = parse_nature(nature)
            extras = [] if also in ("--", "") else [also]
            rows_n = len(nat) + len(extras)
            listed_by = [] if listed.lower().startswith("none") else split_list(listed)
            ecos[name] = {
                "name": name, "slug": slug, "biome": biome,
                "terrain": split_list(terrain),
                "also": extras[0] if extras else "",
                "nature": nat,
                "natureNote": "The game lists no nature objects for this one." if (not nat and nature) else "",
                "rows": rows_n,
                "roles": [x.strip() for x in roles.split(";") if x.strip()],
                "listedBy": listed_by,
                "url": (base.rstrip("/") + "/" + slug) if base else "",
                "label": src["label_plain"],
                "cap": src["confidence"],
            }
            got += 1
        if got != count:
            warns("%s biome: heading says %d ecosystems, table has %d" % (biome, count, got))
        i = j
    return ecos


def parse_roles(lines):
    """Role-fill table and the list of roles whose fill lists were not read."""
    roles = {}
    url = ""
    for i, ln in enumerate(lines):
        if ln.startswith("## Role-fill lists"):
            header, rows, j = table_after(lines, i)
            src = parse_source(next_source(lines, j))
            url = "https://wikily.gg/planet-zoo-2/ecosystems/"
            for r in rows:
                if len(r) >= 2:
                    roles[r[0]] = {"fillers": split_list(r[1]), "complete": True, "known": 0,
                                   "url": url, "label": src["label_plain"], "from": "wiki"}
            break
    unread = {}
    for ln in lines:
        if ln.startswith("Roles that exist on species pages but whose fill lists were not read"):
            body = ln.split("were not read:", 1)[1]
            body = body.split(". These are")[0]
            for m in re.finditer(r"(?:^|[:,])\s*([A-Z][A-Za-z ]+?) \((\d+)", body):
                unread[m.group(1).strip()] = int(m.group(2))
    for name, n in unread.items():
        roles[name] = {"fillers": [], "complete": False, "known": n,
                       "url": "https://wikily.gg/planet-zoo-2/release-groups", "label": "one source, not yet cross-checked",
                       "from": "wiki"}
    return roles, unread


def parse_species_rows(lines):
    """The nine species read on the species side."""
    out = {}
    for i, ln in enumerate(lines):
        if ln.startswith("## Species release requirements"):
            header, rows, j = table_after(lines, i)
            srcline = next_source(lines, j)
            src = parse_source(srcline)
            for r in rows:
                if len(r) < 5:
                    continue
                sp = r[0]
                slug = slugify(sp)
                if slug not in srcline:
                    warn("species %s: page %r not named in its source line" % (sp, slug))
                out[sp] = species_record(sp, r[1], r[2], r[3], r[4],
                                         "https://wikily.gg/planet-zoo-2/release-groups/" + slug,
                                         src["label_plain"], "wiki", "")
            break
    return out


def species_record(sp, ereq, rreq, unlock, fills, url, label, origin, date):
    rows, notes = parse_req(ereq)
    roles_req = [] if rreq.lower().startswith("none") else split_list(rreq)
    return {"species": sp, "raw": ereq, "rows": rows, "notes": notes, "rolesRequired": roles_req,
            "unlock": unlock, "fills": split_list(fills) if fills and fills.lower() != "none" else [],
            "url": url, "label": label, "origin": origin, "date": date}


def parse_rules(lines):
    rules = []
    for i, ln in enumerate(lines):
        if ln.startswith("### Rules used for every suggested order"):
            for j in range(i + 1, len(lines)):
                m = re.match(r"^(\d)\. (.*)$", lines[j])
                if m:
                    rules.append(m.group(2))
                elif lines[j].startswith("_source:"):
                    break
            srcline = next_source(lines, i + 1, limit=20)
            return rules, parse_source(srcline)
    return rules, parse_source("")


def parse_releases(lines):
    """reserve_releases.md -> {name: [species]} (Sweden/Tanzania resolved from their sentence)."""
    raw = {}
    for ln in lines:
        if is_row(ln):
            c = split_row(ln)
            if len(c) == 2 and re.search(r"\d+", c[1]) and c[0] not in ("Reserve", "---"):
                raw[c[0]] = c[1]
    lists = {}
    for name, txt in raw.items():
        m = re.match(r"^(\d+):\s*(.*)$", txt)
        if not m:
            continue
        count, body = int(m.group(1)), m.group(2)
        if " list plus " in body:
            lists[name] = ("derived", count, body)
        elif body.startswith("as Great Rift Valley minus"):
            lists[name] = ("derived", count, body)
        else:
            lists[name] = ("plain", count, split_list(body))
    out = {}
    for name, (kind, count, body) in lists.items():
        if kind == "plain":
            out[name] = body
    # Sweden = Scottish Highlands + named additions
    if "Sweden" in lists:
        body = lists["Sweden"][2]
        add = split_list(body.split(" list plus ", 1)[1])
        out["Sweden"] = list(out["Scottish Highlands"]) + add
    if "Tanzania" in lists:
        body = lists["Tanzania"][2]
        m = re.match(r"as Great Rift Valley minus (.*?), plus (.*)$", body)
        minus = split_list(m.group(1))
        plus = [x.strip() for x in re.split(r",\s*| and ", m.group(2)) if x.strip()]
        out["Tanzania"] = [s for s in out["Great Rift Valley"] if s not in minus] + plus
    for name, (kind, count, body) in lists.items():
        if len(out.get(name, [])) != count:
            warn("releases: %s says %d species, parsed %d" % (name, count, len(out.get(name, []))))
    url = ""
    for ln in lines:
        m = re.search(r"insider-gaming\.com/[^\s,;)\]]+", ln)
        if m:
            url = "https://" + m.group(0)
            break
    return out, url


# ---------------------------------------------------------------- reserve sections

def parse_reserves(lines, ecos, releases):
    reserves = []
    heads = [i for i, ln in enumerate(lines) if re.match(r"^### .* Reserve \(\w+ biome|^### Scottish Highlands \(", ln)]
    for k, h in enumerate(heads):
        end = len(lines)
        for j in range(h + 1, len(lines)):
            if lines[j].startswith("## ") or (lines[j].startswith("### ") and j in heads):
                end = j
                break
        sec = lines[h:end]
        m = re.match(r"^### (.*?) \((\w+) biome", lines[h])
        full, biome = m.group(1), m.group(2)
        short = re.sub(r" Reserve$", "", full)
        # order block
        oi = next((x for x, ln in enumerate(sec) if ln.startswith("**Suggested setup order")), None)
        steps_raw, inline, srcline, conf = [], "", "", ""
        if oi is not None:
            mc = re.search(r"\(confidence (\w+)\):?\s*(.*)$", sec[oi])
            conf = mc.group(1) if mc else ""
            inline = (mc.group(2) if mc else "").strip()
            x = oi + 1
            while x < len(sec) and re.match(r"^\d+\. ", sec[x]):
                steps_raw.append(re.sub(r"^\d+\. ", "", sec[x]))
                x += 1
            for y in range(x, min(len(sec), x + 3)):
                if sec[y].startswith("_source:"):
                    srcline = sec[y]
                    break
            if not srcline and inline:
                for y in range(oi + 1, min(len(sec), oi + 4)):
                    if sec[y].startswith("_source:"):
                        srcline = sec[y]
                        break
        src = parse_source(srcline)
        reserves.append({"full": full, "short": short, "biome": biome, "stepsRaw": steps_raw,
                         "inline": inline, "confidence": conf, "src": src,
                         "tier": src["puzzle_tier"]})
    return reserves


SPOILER_TIER = {"none": 0, "progression": 1, "late-game": 2, "story": 3}


def parse_chapter_tiers(lines):
    """sections/career_progression.md -> ({reserve location: chapter}, {chapter: puzzle-tier}).

    The chapter of each Wildlife Reserve comes from the level tables. The tier of each chapter
    comes from the guide's own wording: a sentence "Chapter 1 rows are spoiler `none`, chapter 2
    and 3 level titles are `progression`", and a heading "Chapter 4 levels (late-game, puzzle-tier 2)".
    """
    where = {}
    for ln in lines:
        if not is_row(ln):
            continue
        c = split_row(ln)
        if len(c) >= 6 and re.match(r"^\d+$", c[0]) and c[5].isdigit() and c[4].startswith("Wildlife Reserve"):
            where[c[3]] = int(c[5])
    tiers = {}
    text = "\n".join(lines)
    pat = r"[Cc]hapters? ((?:\d+(?:,\s*| and )?)+)(?: rows| level titles| level names)? (?:are|is)(?: spoiler)? `([\w-]+)`"
    for m in re.finditer(pat, text):
        t = SPOILER_TIER.get(m.group(2))
        if t is not None:
            for n in re.findall(r"\d+", m.group(1)):
                tiers[int(n)] = t
    for m in re.finditer(r"^#{2,4} Chapter (\d+) levels \([^)]*puzzle-tier (\d)\)", text, re.M):
        tiers[int(m.group(1))] = int(m.group(2))
    return where, tiers


def chapter_label(chapters):
    """[2, 3] -> 'chapters 2-3'; [1] -> 'chapter 1'; [2, 4] -> 'chapters 2 and 4'."""
    ch = sorted(set(chapters))
    if not ch:
        return ""
    if len(ch) == 1:
        return "chapter %d" % ch[0]
    if ch == list(range(ch[0], ch[-1] + 1)):
        return "chapters %d-%d" % (ch[0], ch[-1])
    return "chapters " + ", ".join(str(n) for n in ch[:-1]) + " and %d" % ch[-1]


def eco_names_sorted(ecos):
    return sorted(ecos.keys(), key=lambda n: -len(n))


def parse_steps(res, ecos, releasable):
    """Numbered steps of a reserve -> structured steps. Variants (Sweden, Tanzania) return None."""
    names = eco_names_sorted(ecos)
    steps = []
    rel = set(releasable)

    def species_in(text):
        found = []
        for sp in releasable:
            idx = text.find(sp)
            if idx >= 0:
                found.append((idx, sp))
        found.sort()
        return [s for _, s in found]

    for raw in res["stepsRaw"]:
        n = len(steps) + 1
        m = re.match(r"^Make (.*?) Flourishing\b", raw)
        if m:
            eco = m.group(1)
            if eco not in ecos:
                err("%s step %d: unknown ecosystem %r" % (res["short"], n, eco))
            steps.append({"n": n, "kind": "flourish", "eco": eco, "releases": [], "why": "", "rules": [4]})
            continue
        if raw.startswith("Predators last:"):
            sp = species_in(raw)
            steps.append({"n": n, "kind": "predators", "eco": "", "releases": sp, "why": "", "rules": [5, 4]})
            continue
        hit = next((nm for nm in names if raw.startswith(nm + " (") or raw.startswith(nm + ".")), None)
        if hit:
            mp = re.match(r"^" + re.escape(hit) + r" \((.*?)\)\.\s*(.*)$", raw)
            paren = mp.group(1) if mp else ""
            rest = mp.group(2) if mp else raw[len(hit) + 1:]
            mr = re.match(r"^(\d+) rows(.*)$", paren)
            rows_stated = int(mr.group(1)) if mr else None
            extra = mr.group(2).lstrip(",; ").strip() if mr else paren
            if re.match(r"^(elevation|water)", extra):
                extra = ""
            rel_sp = species_in(rest.replace("Release", "", 1)) if rest.startswith("Release") else []
            if rows_stated is not None and rows_stated != ecos[hit]["rows"]:
                if not (hit == "Lowland Marsh" and False):
                    warn("%s step %d: %s rows stated %d, counted %d" % (res["short"], n, hit, rows_stated, ecos[hit]["rows"]))
            steps.append({"n": n, "kind": "establish", "eco": hit, "releases": rel_sp, "why": extra,
                          "rules": [2, 3]})
            continue
        sp0 = next((s for s in releasable if raw.startswith(s)), None)
        if sp0:
            mp = re.match(r"^" + re.escape(sp0) + r"( last)? \((.*)\)\.?\s*$", raw)
            steps.append({"n": n, "kind": "release", "eco": "", "releases": [sp0],
                          "why": mp.group(2) if mp else "", "rules": [4, 5]})
            continue
        err("%s step %d not understood: %s" % (res["short"], n, raw[:80]))
    # a "Montane Forest" step that ends with Lynx text: handled below via description
    return steps


VARIANT_NOTES = {
    # Neutral wording: names no other reserve, so a revealed tier never leaks another tier's name.
    "Sweden": "This reserve has the same animals as another taiga reserve plus the Eurasian Brown Bear. "
              "Its order is that reserve's order with two changes: the lake is made Flourishing straight "
              "after step 1, and the Eurasian Brown Bear is released last.",
    "Tanzania": "This order is the one for a grassland reserve with a nearly identical animal list, with two "
                "changes: Common Ostrich and Thomson's Gazelle are released at step 1, and there is no "
                "Meerkat on this list.",
}


def merge_why(msgs):
    """'Release X (fills A)' + 'Release X (fills B)' -> 'Release X (fills A and B)'."""
    out, fills = [], {}
    for m in msgs:
        mm = re.match(r"^Release (.*) \(fills (.*)\)$", m)
        if mm:
            if mm.group(1) not in fills:
                fills[mm.group(1)] = []
                out.append(("rel", mm.group(1)))
            fills[mm.group(1)].append(mm.group(2))
        elif m not in [o[1] for o in out]:
            out.append(("txt", m))
    return "; ".join("Release %s (fills %s)" % (o[1], " and ".join(fills[o[1]])) if o[0] == "rel" else o[1] for o in out)


def variant_steps(res, base, ecos, releasable_full, md_text):
    """Sweden and Tanzania are written as 'as X with these changes'. Apply the stated changes."""
    steps = [dict(s) for s in base]
    for s in steps:
        s["releases"] = list(s["releases"])
    if res["short"] == "Sweden":
        need = ["Flourishing Lake", "Brown Bear last", "Eurasian Brown Bear last"]
        if "Eurasian Brown Bear last" not in md_text or "make the lake Flourishing" not in md_text:
            warn("Sweden: the variant sentence changed; re-check how its order is derived")
        lake = next(s for s in steps if s["kind"] == "establish" and s["eco"].startswith("Lake"))
        flo = {"n": 0, "kind": "flourish", "eco": lake["eco"], "releases": [],
               "why": "Both of its roles can already be filled by animals released in step 1", "rules": [4]}
        steps.insert(steps.index(lake) + 1, flo)
        steps.append({"n": 0, "kind": "release", "eco": "", "releases": ["Eurasian Brown Bear"],
                      "why": "Moorland plus Flourishing Lake; no prey role listed", "rules": [4, 5]})
    elif res["short"] == "Tanzania":
        if "Common Ostrich and Thomson's Gazelle released at step 1" not in md_text:
            warn("Tanzania: the variant sentence changed; re-check how its order is derived")
        first = next(s for s in steps if s["kind"] == "establish")
        for sp in ("Common Ostrich", "Thomson's Gazelle"):
            if sp not in first["releases"]:
                first["releases"].append(sp)
        for s in steps:
            if "Meerkat" in s["releases"]:
                s["releases"].remove("Meerkat")
    for i, s in enumerate(steps):
        s["n"] = i + 1
    return steps


# ---------------------------------------------------------------- fill template

FILL_HEAD = "## Fill template"


def parse_fill(lines, warns):
    """Rows typed in from a player's screenshots. Returns dict of lists."""
    out = {"reserves": [], "species": [], "roles": []}
    start = next((i for i, ln in enumerate(lines) if ln.startswith(FILL_HEAD)), None)
    if start is None:
        warns("no fill template section found")
        return out
    i = start + 1
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^### Table ([A-Z]\d?) ", ln)
        if m:
            tid = m.group(1)
            header, rows, j = table_after(lines, i + 1)
            for r in rows:
                if not any(c.strip() for c in r) or r[0].startswith("<"):
                    continue
                if tid in ("A1", "A2"):
                    out["reserves"].append((tid, r))
                elif tid == "B":
                    out["species"].append(r)
                elif tid == "C":
                    out["roles"].append(r)
            i = j
            continue
        i += 1
    return out


# ---------------------------------------------------------------- main assembly

def resolve_eco(name, species, biome_ecos, ecos):
    """Map a requirement name ('Lake') onto an ecosystem of the reserve's biome."""
    if name in biome_ecos:
        return [name]
    var = [e for e in biome_ecos if e.startswith(name + " (")]
    if len(var) > 1:
        narrowed = [e for e in var if species in ecos[e]["listedBy"]]
        if narrowed:
            return narrowed
    return var


def main():
    lines = read_lines("animals/reserve_ecosystems.md")
    rel_lines = read_lines("animals/reserve_releases.md")
    acc_lines = read_lines("animals/accreditation.md")
    md_text = "\n".join(lines)

    ecos = parse_ecosystems(lines, warn)
    if len(ecos) != 32:
        warn("expected 32 ecosystems, found %d" % len(ecos))
    roles, unread = parse_roles(lines)
    species = parse_species_rows(lines)
    rules, rules_src = parse_rules(lines)
    if len(rules) != 5:
        warn("expected 5 order rules, found %d" % len(rules))
    releases, insider_url = parse_releases(rel_lines)

    # Roles a released animal is documented to fill (from the species side)
    for sp, rec in species.items():
        for role in rec["fills"]:
            r = roles.setdefault(role, {"fillers": [], "complete": False, "known": 0,
                                        "url": "https://wikily.gg/planet-zoo-2/release-groups",
                                        "label": "one source, not yet cross-checked", "from": "wiki"})
            if sp not in r["fillers"] and not r.get("complete"):
                r["fillers"].append(sp)

    # Deluxe Edition species (accreditation.md, read only)
    deluxe, deluxe_url = [], ""
    for k, ln in enumerate(acc_lines):
        m = re.search(r"six Deluxe Edition species:\s*(.*?)(?:;|\))", ln)
        if m:
            deluxe = split_list(m.group(1))
            mu = re.search(r"https://insider-gaming\.com/planet-zoo-2-all-animals-complete-zoopedia/",
                           next_source(acc_lines, k + 1, limit=3))
            deluxe_url = mu.group(0) if mu else ""
            break
    if "Golden Eagle" not in deluxe or len(deluxe) != 6:
        warn("Deluxe species list not parsed from accreditation.md")

    # Player-screenshot rows
    fill = parse_fill(lines, warn)
    fills_log = {"reserves": 0, "species": 0, "roles": 0}
    for r in fill["species"]:
        if len(r) < 5:
            warn("fill table B row too short: %r" % r)
            continue
        date = r[5] if len(r) > 5 else ""
        rec = species_record(r[0], r[1], r[2], r[3], r[4], "", "from a player's screenshot", "player", date)
        species[r[0]] = rec
        for role in rec["fills"]:
            rr = roles.setdefault(role, {"fillers": [], "complete": False, "known": 0, "url": "",
                                         "label": "from a player's screenshot", "from": "player"})
            if r[0] not in rr["fillers"]:
                rr["fillers"].append(r[0])
        fills_log["species"] += 1
    for r in fill["roles"]:
        if len(r) < 2:
            continue
        date = r[2] if len(r) > 2 else ""
        fl = split_list(r[1])
        old = roles.get(r[0], {"known": 0})
        roles[r[0]] = {"fillers": fl, "complete": True, "known": len(fl), "url": "",
                       "label": "from a player's screenshot", "from": "player", "date": date}
        fills_log["roles"] += 1

    # Reserves
    res_list = parse_reserves(lines, ecos, releases)
    where, chapter_tier = parse_chapter_tiers(read_lines("sections/career_progression.md"))
    for res in res_list:
        ch = where.get(res["full"])
        res["chapter"] = ch
        if ch is not None and chapter_tier.get(ch) in (0, 1, 2):
            res["tier"] = chapter_tier[ch]
        elif res["tier"] in (0, 1, 2):
            warn("%s: chapter tier not found in career_progression.md; using the reserve's own tag (tier %d)"
                 % (res["full"], res["tier"]))
        else:
            err("%s: no spoiler tier found" % res["full"])
    by_short = {r["short"]: r for r in res_list}
    base_steps = {}
    reserve_out = []
    for res in res_list:
        short = res["short"]
        if short not in releases:
            err("no releasable list for %s" % short)
            continue
        releasable = releases[short]
        for sp in releasable:
            pass
        biome_ecos = [e for e in ecos if ecos[e]["biome"] == res["biome"]]
        if res["stepsRaw"]:
            steps = parse_steps(res, ecos, releasable)
            base_steps[short] = steps
        else:
            base = base_steps.get("Scottish Highlands" if short == "Sweden" else "Great Rift Valley")
            steps = variant_steps(res, base, ecos, releasable, res["inline"])
        # coverage check: every releasable species released exactly once
        released = [s for st in steps for s in st["releases"]]
        miss = [s for s in releasable if s not in released]
        extra = [s for s in released if s not in releasable]
        dup = sorted(set(s for s in released if released.count(s) > 1))
        if miss or extra or dup:
            err("%s: order vs releasable list: missing %s extra %s duplicated %s" % (short, miss, extra, dup))
        for st in steps:
            if st["kind"] in ("establish", "flourish") and st["eco"] not in biome_ecos:
                err("%s: step %d ecosystem %s is not in the %s biome" % (short, st["n"], st["eco"], res["biome"]))
        est_rows = [ecos[st["eco"]]["rows"] for st in steps if st["kind"] == "establish"]
        if est_rows != sorted(est_rows):
            warn("%s: ecosystems are not in order of fewest requirements first: %s" % (short, est_rows))
        res["steps"] = steps
        res["releasable"] = releasable
        res["biome_ecos"] = biome_ecos

    if ERRORS:
        print("%d error(s); data not written" % len(ERRORS))
        return 1

    # Table A: reserve ecosystems panel rows
    avail = {}
    for tid, r in fill["reserves"]:
        if len(r) < 2:
            continue
        key = re.sub(r" Reserve$", "", r[0])
        if key not in by_short:
            warn("fill table A: reserve %r not recognised" % r[0])
            continue
        offered = split_list(r[1])
        for e in offered:
            if e not in ecos:
                warn("fill table A: ecosystem %r not recognised" % e)
        pre = split_list(r[2]) if len(r) > 2 and r[2] and r[2].lower() not in ("none", "-", "--") else []
        area = {}
        if len(r) > 3 and r[3]:
            for part in r[3].split(";"):
                if ":" in part:
                    a, b = part.split(":", 1)
                    area[a.strip()] = b.strip()
        date = r[4] if len(r) > 4 else ""
        avail[key] = {"offered": offered, "pre": pre, "area": area, "date": date}
        fills_log["reserves"] += 1

    # ---- derive per-step details and per-species routes
    def release_step(res, sp):
        for st in res["steps"]:
            if sp in st["releases"]:
                return st["n"]
        return None

    def eco_step(res, eco, kind):
        for st in res["steps"]:
            if st["kind"] == kind and st["eco"] == eco:
                return st["n"]
        return None

    def species_deps(res, sp):
        """Steps that must precede the release of `sp`: list of (n, why)."""
        n_rel = release_step(res, sp)
        deps = {}
        rec = species.get(sp)
        if rec and rec["rows"]:
            for row in rec["rows"]:
                chosen = None
                for opt in row["options"]:
                    for eco in resolve_eco(opt["eco"], sp, res["biome_ecos"], ecos):
                        est = eco_step(res, eco, "establish")
                        if est is None:
                            continue
                        flo = eco_step(res, eco, "flourish") if opt["flourishing"] else None
                        if opt["flourishing"] and flo is None:
                            continue
                        chosen = (eco, est, flo)
                        break
                    if chosen:
                        break
                if chosen:
                    eco, est, flo = chosen
                    deps.setdefault(est, []).append("Set up %s" % eco)
                    if flo:
                        deps.setdefault(flo, []).append("Make %s Flourishing" % eco)
                else:
                    # no ecosystem of the row is in the order: record as unresolved
                    pass
        else:
            for st in res["steps"]:
                if st["kind"] == "establish" and sp in st["releases"]:
                    deps.setdefault(st["n"], []).append("Set up %s" % st["eco"])
        return n_rel, deps

    def role_ready(res, role, before):
        """Earliest release step (< before) of a releasable animal known to fill the role."""
        best = None
        for sp in roles.get(role, {}).get("fillers", []):
            n = release_step(res, sp)
            if n is not None and n < before and (best is None or n < best[0]):
                best = (n, sp)
        return best

    def closure(res, n_target, deps):
        """Add what the Flourishing steps in `deps` themselves need."""
        out = {k: list(v) for k, v in deps.items()}
        changed = True
        while changed:
            changed = False
            for n, why in list(out.items()):
                st = res["steps"][n - 1]
                if st["kind"] == "flourish":
                    est = eco_step(res, st["eco"], "establish")
                    msg = "Set up %s" % st["eco"]
                    if est is not None and msg not in out.get(est, []):
                        out.setdefault(est, []).append(msg)
                        changed = True
                    for role in ecos[st["eco"]]["roles"]:
                        rr = role_ready(res, role, n)
                        if rr:
                            msg = "Release %s (fills %s)" % (rr[1], role)
                            if msg not in out.get(rr[0], []):
                                out.setdefault(rr[0], []).append(msg)
                                changed = True
        return out

    tier_out = {0: [], 1: [], 2: []}
    index = {}
    for res in res_list:
        if "steps" not in res:
            continue
        short = res["short"]
        tier = res["tier"]
        a = avail.get(short)
        steps_out = []
        known_cnt = sum(1 for sp in res["releasable"] if sp in species and species[sp]["rows"])
        for st in res["steps"]:
            o = {"n": st["n"], "kind": st["kind"], "eco": st["eco"], "releases": st["releases"],
                 "why": st["why"], "rules": st["rules"]}
            n = st["n"]
            if st["kind"] in ("establish", "flourish"):
                eco = st["eco"]
                # roles and who on this reserve can fill them
                rf = []
                for role in ecos[eco]["roles"]:
                    info = roles.get(role, {"fillers": [], "complete": False, "known": 0})
                    here = []
                    for sp in info["fillers"]:
                        rn = release_step(res, sp)
                        if rn is not None:
                            here.append({"sp": sp, "step": rn})
                    here.sort(key=lambda x: (x["step"], x["sp"]))
                    rf.append({"role": role, "here": here, "complete": info.get("complete", True)})
                o["roleFill"] = rf
                o["flourishStep"] = eco_step(res, eco, "flourish") if st["kind"] == "establish" else None
                o["establishStep"] = eco_step(res, eco, "establish")
                # which later species are gated by this ecosystem
                unlocks = []
                for sp in res["releasable"]:
                    rn, deps = species_deps(res, sp)
                    if rn is None or rn <= n or not species.get(sp, {}).get("rows"):
                        continue
                    if n in closure(res, rn, deps):
                        # only list the direct dependants (not every filler chain)
                        direct = n in deps
                        if direct:
                            unlocks.append({"sp": sp, "step": rn, "raw": species[sp]["raw"]})
                o["unlocks"] = unlocks
                if st["kind"] == "establish":
                    others = []
                    for sp in ecos[eco]["listedBy"]:
                        if sp in res["releasable"] and sp not in st["releases"]:
                            others.append({"sp": sp, "step": release_step(res, sp)})
                    o["alsoNamedBy"] = others
            # species routes for every species released in this step
            for sp in st["releases"]:
                rn, deps = species_deps(res, sp)
                ent = index.setdefault(sp, {"tiers": {0: [], 1: [], 2: []}})
                ent["tiers"][tier].append({"reserve": short, "step": rn})
            steps_out.append(o)
        # per-species route info for the gated data
        routes = {}
        for sp in res["releasable"]:
            rn, deps = species_deps(res, sp)
            full = closure(res, rn, deps)
            must = [{"n": k, "why": merge_why(v)} for k, v in sorted(full.items()) if k < rn]
            st = res["steps"][rn - 1]
            routes[sp] = {"step": rn, "via": st["eco"] or "", "kind": st["kind"], "must": must,
                          "known": bool(species.get(sp, {}).get("rows")),
                          "prey": (species.get(sp, {}).get("rolesRequired") or [])}
        rec = {
            "id": slugify(short),
            "name": short,
            "full": res["full"],
            "tier": tier,
            "biome": res["biome"],
            "releasable": res["releasable"],
            "releaseUrl": insider_url,
            "steps": steps_out,
            "routes": routes,
            "orderLabel": res["src"]["label_plain"],
            "orderLabelRaw": res["src"]["label"],
            "orderConfidence": res["confidence"] or res["src"]["confidence"],
            "variantNote": VARIANT_NOTES.get(short, ""),
            "knownReq": known_cnt,
            "avail": a,
        }
        tier_out[tier].append(rec)

    # species lookup index (open data): every releasable species
    all_sp = []
    for lst in releases.values():
        for sp in lst:
            if sp not in all_sp:
                all_sp.append(sp)
    all_sp.sort()
    sp_index = {}
    for sp in all_sp:
        listed = [e for e in ecos if sp in ecos[e]["listedBy"]]
        rec = species.get(sp)
        sp_index[sp] = {
            "listed": listed,
            "req": None,
            "deluxe": sp in deluxe,
            "t1": len(index.get(sp, {"tiers": {1: [], 2: []}})["tiers"][1]),
            "t2": len(index.get(sp, {"tiers": {1: [], 2: []}})["tiers"][2]),
        }
        if rec:
            sp_index[sp]["req"] = {"raw": rec["raw"], "rows": rec["rows"], "notes": rec["notes"],
                                   "roles": rec["rolesRequired"], "unlock": rec["unlock"],
                                   "fills": rec["fills"], "url": rec["url"], "label": rec["label"],
                                   "origin": rec["origin"], "date": rec["date"]}
        if not listed:
            warn("species %s is releasable but no ecosystem lists it" % sp)

    open_data = {
        "ecosystems": ecos,
        "biomes": ["Grassland", "Temperate", "Taiga", "Tropical"],
        "roles": roles,
        "unreadRoles": unread,
        "rules": rules,
        "rulesLabel": rules_src["label_plain"],
        "species": sp_index,
        "filled": fills_log,
        "reserveCounts": {"0": len(tier_out[0]), "1": len(tier_out[1]), "2": len(tier_out[2])},
        "tierLabels": {str(t): chapter_label([r["chapter"] for r in res_list if r.get("tier") == t])
                       for t in (0, 1, 2)},
        "deluxeUrl": deluxe_url,
        "counts": {"ecosystems": len(ecos), "releasableSpecies": len(all_sp),
                   "speciesReqKnown": sum(1 for s in all_sp if sp_index[s]["req"])},
    }
    for t in (0, 1, 2):
        tier_out[t].sort(key=lambda r: r["name"])
    open_data["reserves0"] = tier_out[0]
    payload = {"open": open_data, "tier1": tier_out[1], "tier2": tier_out[2]}

    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    path = os.path.join(OUT, "ecosystems.json")
    with io.open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")

    print("ecosystems: %d, releasable species in lookup: %d, with release rows documented: %d"
          % (len(ecos), len(all_sp), open_data["counts"]["speciesReqKnown"]))
    for t in (0, 1, 2):
        for r in tier_out[t]:
            print("tier %d: %-18s %2d steps, %2d releasable, release rows documented for %d"
                  % (t, r["name"], len(r["steps"]), len(r["releasable"]), r["knownReq"]))
    print("fill rows read: %s" % fills_log)
    print("%d warning(s), %d error(s)" % (len(WARNINGS), len(ERRORS)))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
