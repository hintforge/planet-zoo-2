# Planet Zoo 2 -- interactive tools

Self-contained HTML tools that read this guide's files. Open the file in any browser; nothing is installed, nothing phones home. Two pages live here:

- `accreditation_tree.html` -- which animals each Accreditation tier adds, and the research levels for each animal.
- `reserve_ecosystems.html` -- which ecosystems to set up first in each Wildlife Reserve.

Both pages have gaps the guide has not read yet, marked on the page. A player who has the game can close a gap with screenshots (see "Adding ..." under each page below); the guide's companion types the screenshots into the guide and reruns two scripts.

## Accreditation tree -- `accreditation_tree.html`

Which animals each Accreditation tier adds, in Career and in Franchise, as a ladder from the first tier to the last, with the number of animals per tier. Search by name, filter to Deluxe-only or to animals with a release group, and tap an animal for its tier in both modes, how to get it, other gates, release group and research levels. Career tier gates are described by medal counts only; where a research gate names a Wildlife Reserve beyond the first chapter, the name sits behind a "Show which one" button.

Research levels are filled in for the animals the guide has documented (the page shows the count, "Research documented for N of 136 species"). Every other animal shows an empty slot with the level structure the guide does know.

### Adding an animal's research levels (screenshots first)

1. A player who has the game opens that animal's research screen and takes screenshots: every level, with what each asks for and unlocks, and any Observation Network gate marker. One capture per level if the game shows one at a time.
2. The player gives the screenshots to their Hintforge companion (reader or builder session). The companion transcribes them into a row in `items/research_tree.md` using the template block "Fill-in target" there, with a `_source: player screenshot <date> ...` metadata line.
3. The companion reruns the two scripts below. The animal's research tree now shows on the page.

Fallback, no companion: edit `items/research_tree.md` by hand. Copy the template row under "Fill-in target", fill the four columns (species name exactly as in `animals/accreditation.md`; number of levels; `L1 ...; L2 ...` entries separated by `; `; gate as `none` or `Before L4: an Observation Network (Observation Platform) in <reserve> and the species released there`), put it in the table that matches the species' spoiler tier, add the metadata line under the table, then rerun the scripts.

### Rebuild

```
python -I artifacts/extract.py
python -I artifacts/build.py
```

`build.py` runs `extract.py` itself, so the second line alone is enough. Python 3, standard library only. `extract.py` reads `animals/accreditation.md`, `items/research_tree.md`, `sections/career_progression.md`, `mechanics.md` and `research_briefs/source_register.md`, writes `data/*.json`, and prints a WARNING for an unknown species name, a repeated row, a level count that does not match its entries, or per-tier counts that differ from the totals stated in the guide. `build.py` swaps the data into `accreditation_tree.html`; the page's layout and script are left alone.

## Reserve ecosystem order -- `reserve_ecosystems.html`

Which ecosystems to set up in each Wildlife Reserve, and in what order, which the game leaves unclear.

- **Plan a reserve.** Pick a reserve for a numbered list of steps. Each step shows what the ecosystem needs to become Established (terrain, extra needs, nature objects, with a source link), the roles that make it Flourishing and which of the reserve's animals can fill them, which animals the step releases, and what it opens up next (for example "Lion needs Flourishing Savannah").
- **The order is the guide's own reasoning.** Every reserve opens with a banner saying so, with the five rules the order follows (smallest set, fewest requirements first, release as soon as possible, prerequisites first, predators last). The requirements inside each step are documented facts; the order is not.
- **Find an animal.** Type an animal's name (all 58 animals that any reserve can release) to see its documented release requirements, the ecosystems whose pages list it, and, per reserve, its step and what must come first.
- **Spoilers.** The first chapter's reserve (Great Rift Valley) shows straight away, because the guide marks the first chapter as free of spoilers. The three reserves from chapters 2-3 and the two from chapter 4 sit behind two separate "Show these reserves" buttons; their names are not readable in the page source until pressed. Which chapter a reserve belongs to, and how spoilery that chapter is, is read from the guide's own career table and tags each time the page is built, so a change in the guide moves a reserve between the groups on the next rebuild. The animal lookup shows only a count of the hidden reserves until the matching button is pressed.
- **Gaps are shown, never guessed.** Marked "Not documented yet" with the in-game screen a player can capture: which ecosystems a reserve offers and whether any start Established (guessed from the biome), release requirements for the animals not yet read (documented for 9 of 58), who fills the Medium Prey and Small Prey roles, and each ecosystem's area requirement.

### Closing a gap on the reserve page (screenshots first)

1. A player who has the game takes the screenshots the gap names: a reserve's Ecosystems panel (Ecosystem Brush list, with one ecosystem selected to show its Area requirement), an animal's Release Group requirements screen, or a prey animal's Release Group screen with its Roles shown.
2. The player gives them to their Hintforge companion (reader or builder session). The companion transcribes them into the tables under "Fill template" at the end of `animals/reserve_ecosystems.md` (Table A1 or A2 for a reserve's Ecosystems panel, Table B for release requirements, Table C for role fill lists), with a metadata line `source: player screenshot <date> · capture: screenshot` under each table.
3. The companion reruns the two scripts below. The matching "Not documented yet" notes close and the screenshot's values show, marked as from a player's screenshot.

Fallback, no companion: type the same rows into those tables by hand (ecosystem and animal names exactly as in the guide's tables; one row per thing seen; the capture date in the last column), then rerun the scripts.

If a reserve's Ecosystems panel does not list an ecosystem the suggested order uses, the page flags that step. The order is not redone automatically: change the guide's order text in `animals/reserve_ecosystems.md` and rerun.

### Rebuild the reserve page

```
python -I artifacts/extract_ecosystems.py
python -I artifacts/build_ecosystems.py
```

`build_ecosystems.py` runs `extract_ecosystems.py` itself, so the second line alone is enough. Python 3, standard library only. `extract_ecosystems.py` reads `animals/reserve_ecosystems.md`, `animals/reserve_releases.md`, `sections/career_progression.md` (each reserve's chapter and that chapter's spoiler tier) and `animals/accreditation.md` (read only), writes `data/ecosystems.json`, and prints a WARNING for a problem that does not stop the build (a requirement count that differs from the guide's, an ecosystem out of fewest-requirements order, an unrecognised name in the fill tables, a reserve whose chapter tier is missing from the career table) and an ERROR, writing nothing, when a reserve's steps do not cover its releasable list exactly once or a step names an ecosystem outside the reserve's biome. `build_ecosystems.py` swaps the data into the page, refuses to finish if a hidden reserve's name is readable in the page source or a local path is on the page, and checks that the lookup covers every releasable animal.

## Screenshots

`shots/` holds screenshots of both pages (the accreditation tree at phone and desktop width; the reserve page's opening screen and a reserve open).
