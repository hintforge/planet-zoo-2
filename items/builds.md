# Planet Zoo 2 -- Builds (habitat and zoo design patterns)

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19

There is no combat build system; "builds" here are layout and design patterns. Mainstream guide coverage was thin six days after launch, so the patterns below come from Career objectives (which encode the designers' intended solutions) and reviews. Patterns are advice, not verified facts; the factual statements inside them carry their own tags. Every pattern carries its own `_source:` line.

- **Welfare-focused:** enclose by barrier with a staff gate on a staff path; meet each welfare component in turn (food, water, shelter, terrain/grass, enrichment) and check the welfare panel after arrival [refs 10, 31]; for stressed animals use one-way glass, "Do Not Disturb" signs and burrows [ref 19]; research the species to reveal thriving requirements before chasing 100% [refs 4, 26].
  _source: P1 result 2026-10-19 [ref 10 (wikily.gg/planet-zoo-2/career/east-africa); ref 31 (finalboss.io chapter 1 walkthrough); ref 19 (wikily.gg/planet-zoo-2/career/mountain-forests); ref 4 (wikily.gg/planet-zoo-2/research); ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch (refs 10, 19, 4, 26) / web_fetch (ref 31) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-001: a species has to be researched before it can reach the Thriving welfare state.

> **Cross-system dependency** -- see `../dependencies.md` DEP-005: a habitat or aquarium Staff Gate has to be connected to the path network.

> **Cross-system dependency** -- see `../dependencies.md` DEP-014.

- **Economy-focused (the Chapter 2 economy-recovery route; see `../sections/chapter_2_paws_on_the_path.md`):** cluster donation bins at viewing areas, add food, drink and gift shops, run a marketing campaign on a draw animal, and clear loans [ref 13].
  _source: P1 result 2026-10-19 [ref 13 (wikily.gg/planet-zoo-2/career/new-england)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` SEQ-004: repaying the starting loan before operating cash is built risks stalling.

- **Hybrid (education + donations), Rural France:** a "Free" zoo funded by donations and an adoption shop, with education boards, speakers, talk points and educators to raise guest education [ref 18]; education raises donations and is a 5-star target for the achievement "Lessons Learned" [ref 3].
  _source: P1 result 2026-10-19 [ref 18 (wikily.gg/planet-zoo-2/career/rural-france); ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`
- **Disagreement:** a Gold-medal guide (not opened) puts welfare and nutrition first; the Java level caps the zoo at 4 habitats, which runs against expanding for income [ref 17].
  _source: P1 result 2026-10-19 [ref 17 (wikily.gg/planet-zoo-2/career/java); a Gold-medal guide seen only as a search excerpt (not opened)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` SEQ-005: a habitat-count cap can make an objective unsatisfiable if more enclosures are built.

- Region-themed zoos that feed matching reserves were suggested in a guide excerpt (not opened).
  _source: P1 result 2026-10-19 [guide seen only as a search excerpt (not opened)] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`
- Build tools: plant/nature brush that fills an area; paths drawn as shapes and auto-filled; scaling and recolouring of decorations; auto-generated aviary mesh roofs [ref 36]; four new scenery themes plus five from the first game [ref 35]; blueprints praised as powerful [ref 34].
  _source: P1 result 2026-10-19 [ref 36 (securitylab.ru blog review); ref 35 (xboxygen.com review); ref 34 (gameswelt.de review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 3 languages -- below 5-source floor]`
- Reviewer gripes that guides miss: clicking an enclosure selects the landscape object before the animals; no automatic enclosure doors or sewer connections [ref 34, translated from: German]. vector: controls.
  _source: P1 result 2026-10-19 [ref 34 (gameswelt.de review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`
- Barrier planner: a Wikily tool for planning barriers (companion tool, not read in detail); see `../limitations.md`.
  _source: P1 result 2026-10-19 [ref 1 (wikily.gg/planet-zoo-2) navigation entry; the tool itself was not read] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Achievement-bound claims
Aggregated in `../achievements.md`.
- Build 25 km of barrier in total.
  _source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: long_distance_builder · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`
- 5-star Education Rating in a non-Sandbox zoo.
  _source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: lessons_learned · achievement-hidden: yes · trigger_type: mastery_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Set up an Educational Tour (sources disagree).
  _source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: follow_me · achievement-hidden: yes · trigger_type: discovery_ `[Contradicted across sources -- see notes]`
