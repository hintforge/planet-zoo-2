# Planet Zoo 2 -- Welfare, breeding and release

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19

All modes unless noted. Every claim carries its own `_source:` line.

## Welfare mechanism
- Selecting an animal shows overall welfare % split into **Animal Status** (health), **Social** (group size and company), **Environment** (space, terrain, planting), **Enrichment**, plus an **Animal Appeal** score; the panel has direct actions (assign keeper, request vet, order clean) [ref 26]. Career objectives also name Shelter and Terrain welfare [ref 10].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare); ref 10 (wikily.gg/planet-zoo-2/career/east-africa)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Welfare inputs in the German review: food, water, space, social relationships (possibly across species), retreat areas, stress, cleanliness, climate, enrichment against boredom [ref 34, translated from: German]. Seasons, temperature and weather require shelters, heating and cooling; a habitat fine in summer may fail in winter [ref 36, translated from: Russian]. [refs 26, 34, 36]
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare); ref 34 (gameswelt.de review); ref 36 (securitylab.ru blog review)] · capture: browser_fetch (ref 26) / web_fetch (refs 34, 36) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 3 languages -- below 5-source floor]`
- "Animal brain": behaviour types Routines, Periodics, Distractions, Interruptions; moods spread (a scared zebra alerts its herd); formations for migrating, defending, fleeing; group actions are voted, weighted by how social the species is [ref 26].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Thriving needs the species to be researched first (see `../items/upgrades.md`).
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare); ref 36 (securitylab.ru blog review)] · capture: browser_fetch (ref 26) / web_fetch (ref 36) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-001: a species has to be researched before it can reach the Thriving welfare state.

> **Cross-system dependency** -- see `../dependencies.md` DEP-002: the achievement for 3 species Thriving at once depends on each species being researched first.

- Update 1.0.4 changed breeding frequency and success rate, Shoal welfare requirements and temperature calculations [ref 27]; facts about these values recorded before 14 Oct may be stale.
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

## Breeding and nesting
- New in Planet Zoo 2: flying birds, flightless birds and egg-laying reptiles need **a nest per breeding pair**, and a pair cannot conceive until it has claimed one. Eggs are incubated by male, female or both depending on species; reptiles leave eggs (some mothers guard) [ref 26].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-006: birds and egg-laying reptiles need a nest per breeding pair.

- **Exception:** fledged flying-bird juveniles do not count toward a habitat's adult population limit until sexual maturity [ref 26].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Some species have seasonal fertility; welfare feeds fertility, so poor welfare during the window **costs a whole year**; continuous breeders need housing or contraception [ref 26]. missable: yes (per-year breeding window).
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` SEQ-003: poor welfare in a species' fertility window costs a breeding year.

- Breeding is managed by partner choice and contraception [ref 34, translated from: German].
  _source: P1 result 2026-10-19 [ref 34 (gameswelt.de review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`
- Cohabitation returns; Update 1.0.4 updated cohabitation lists; aviary birds can share with other animals [refs 26, 27]. The achievement "Shared Accommodation" needs 5 species in one terrestrial habitat that all share a "Thriving relationship" [ref 3].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare); ref 27 (insider-gaming.com, Update 1.0.4 notes); ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: browser_fetch (refs 26, 3) / web_fetch (ref 27) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

## Release
- Release-group compositions seen in Career: Maternal Family Group, Solitary Male, Family Group, Mixed Group, Mating Pair, Breeding Partners, Matriarchal Sounder [refs 10, 14, 16, 23, 24].
  _source: P1 result 2026-10-19 [refs 10, 14, 16, 23, 24 (wikily.gg/planet-zoo-2/career per-level pages)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- **Contradiction:** TheGamesWiki says only species with a suitable Wildlife Reserve can be released [ref 26]; Prima says every animal can be released, but only reserve species can be followed afterwards [ref 32]; Wikily distinguishes release groups (to reserves) from "quick releasing" [ref 8]. Working reading: release groups need a reserve; quick release works for any animal.
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare); ref 32 (primagames.com, 13 Oct 2026); ref 8 (wikily.gg/planet-zoo-2/conservation-projects)] · capture: browser_fetch (refs 26, 8) / web_fetch (ref 32) · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Contradicted across sources -- see notes]`
- Releasable species per reserve: `reserve_releases.md`.

> **Cross-system dependency** -- see `../dependencies.md` DEP-010.

> **Cross-system dependency** -- see `../dependencies.md` DEP-011.

> **Cross-system dependency** -- see `../dependencies.md` DEP-016.

> **Cross-system dependency** -- see `../dependencies.md` PON-001.

## Achievement-bound claims
Aggregated in `../achievements.md`.
- First baby born in your zoo (breeding must be on).
  _source: P1 result 2026-10-19 [refs 3, 9, 10] · capture: browser_fetch (refs 3, 9, 10) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: the_future_is_bright · achievement-hidden: yes · trigger_type: progression_ `[Single source -- verify · class:community-wiki]` (refs 3, 9, 10 are all Wikily pages, counted as one source)
- Adopt your first animal.
  _source: P1 result 2026-10-19 [refs 3, 10] · capture: browser_fetch (refs 3, 10) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: lets_get_started · achievement-hidden: yes · trigger_type: progression_ `[Single source -- verify · class:community-wiki]` (refs 3, 10 are both Wikily pages, counted as one source)
- Release a group of more than 10 animals.
  _source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: they_do_move_in_herds · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Release an animal with Gold genetics.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: worth_its_weight_in_gold · achievement-hidden: yes · trigger_type: discovery_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- 5 species in one habitat sharing a Thriving relationship.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: shared_accommodation · achievement-hidden: yes · trigger_type: mastery_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- A zoo-born animal reaches 15 years old.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: they_grow_up_so_fast · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- 10 critically endangered animals born in one zoo.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: first_steps · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Release 20 release groups.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: job_well_done · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
