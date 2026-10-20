# Planet Zoo 2 -- Achievements

**status:** research-integrated <!-- scaffold | research-integrated | live-observed | reconciled -->
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19 (cross-checked against P2 2026-10-19)
**stub_source:** Steam (names via a vgtimes.ru mirror; re-checked 2026-10-19 against the us.gamesplanet.com Steam-key community achievements page, a Steam list mirror; the canonical Steam stats page for Planet Zoo 2 was not found at ingestion: the Steam stats URL returned by search was the first game's, app 703080; the doctor run 2026-10-19 found it at steamcommunity.com/stats/3219030/achievements, where 26 of the 39 names loaded and all 26 match this file, the other 13 did not load)
**stub_fetched:** 2026-10-19
**stub_count:** 39
**coverage:** 39 of 39 names match the live-list mirror (receipt: `research_briefs/achievement_completeness_check.md`). Trigger resolution: 33 resolved, 6 deferred (4 mastery entries without a strategy claim, 2 collection entries whose set members are not all captured), 0 unreachable. Coverage line is `verified against a live list mirror, not the canonical Steam stats page`.
**hidden flags:** no read source states a hidden flag for any entry, so every entry is `hidden: yes` (the spoiler-safe value that gates the name), set by the doctor run 2026-10-19; see `limitations.md` "Achievement hidden flags". Steam's own achievement list (app 3219030) shows 26 of the 39 entries with names and full descriptions and no hidden marker, but it never says "not hidden", so it does not set any entry to `no`.

The reader treats this file as authoritative for trigger conditions, point-of-no-return windows and missability. No read source names a missable achievement window. The one general window: difficulty changes can affect whether achievements can be earned (see `sections/career_progression.md`). Triggers below are paraphrased; developer descriptions are publisher IP.

> **Cross-system dependency** -- see `dependencies.md` SEQ-002: lowering difficulty can affect whether achievements can be earned.

Accepted as design (zipper 2026-10-19): each trigger appears here and again as an `achievement:` overlay claim in the topic file that owns its mechanic; this file is the aggregate, the topic file is the primary claim, and neither is a duplicate to remove.

Each entry ends with its own `_source:` line (sources, capture, confidence, tiers); the names are cross-checked against Wikily (ref 3), Insider Gaming (ref 28) and Destructoid (ref 29). Genre overlays: none apply. Branch section omitted (no mutually exclusive achievements found).

## Progression

### The Future is Bright
- **id:** the_future_is_bright
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** first baby born in your zoo; needs ageing/breeding on (off in early Career levels until Silver) [refs 3, 9, 10]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** ageing/breeding switched on
- **vector-binding:** `animals/welfare_breeding_release.md`; `sections/chapter_1_wild_at_heart.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 9, 10] · capture: browser_fetch (refs 3, 9, 10) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 3, 9, 10 are all Wikily pages, counted as one source)

### Let's Get Started
- **id:** lets_get_started
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** adopt your first animal; first reached in East Africa Bronze [refs 3, 10]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/welfare_breeding_release.md`; `sections/chapter_1_wild_at_heart.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 10] · capture: browser_fetch (refs 3, 10) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 3, 10 are both Wikily pages, counted as one source)

### Earth, Wind and Water
- **id:** earth_wind_and_water
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** adopt an aquatic, an avian and a terrestrial animal [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Student
- **id:** student
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** fully research one species; some species need reserve field research for later levels [refs 3, 4]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a Research Centre with a Vet; for field-research species, an Observation Network in a reserve and the species released there
- **vector-binding:** `items/upgrades.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 4] · capture: browser_fetch (refs 3, 4) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 3, 4 are both Wikily pages, counted as one source)

### Credit Where It's Due
- **id:** credit_where_its_due
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** reach the highest Accreditation in any non-Sandbox hub; in Career that is Tier 5 (18 Bronze, 2 Silver) [refs 2, 3]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** Career medals; Franchise has its own Accreditation track
- **vector-binding:** `sections/career_progression.md`
- **spoiler:** progression (the tier requirement)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 2, 3] · capture: browser_fetch (refs 2, 3) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]` (refs 2, 3 are both Wikily pages, counted as one source)

### Mola Mola Likes You
- **id:** mola_mola_likes_you
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** 100% welfare on an Ocean Sunfish; the Maluku Islands Bronze objective asks the same [refs 3, 21]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** an aquarium; Ocean Sunfish adopted
- **vector-binding:** `sections/chapter_4_fentastic_opportunity.md`; `animals/aquariums_and_aviaries.md`
- **spoiler:** late-game (the Career level link)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 21] · capture: browser_fetch (refs 3, 21) · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]` (refs 3, 21 are both Wikily pages, counted as one source)

### Budding Conservationist
- **id:** budding_conservationist
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** complete one conservation project [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `items/upgrades.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Show-Pony
- **id:** show_pony
- **hidden:** yes
- **trigger_type:** progression
- **trigger:** start a Gold Tier (Level 3) marketing campaign for an animal [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** marketing tiers unlocked through Accreditation
- **vector-binding:** `mechanics.md` (Economy and guests)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `dependencies.md` DEP-003: species research is done by Vets working in a powered, path-connected Research Centre.

> **Cross-system dependency** -- see `dependencies.md` DEP-010.

> **Cross-system dependency** -- see `dependencies.md` DEP-012.

> **Cross-system dependency** -- see `dependencies.md` DEP-013.

> **Cross-system dependency** -- see `dependencies.md` DEP-017.

> **Cross-system dependency** -- see `dependencies.md` DEP-020.

## Mastery

### Lessons Learned
- **id:** lessons_learned
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** 5-star Education Rating in a non-Sandbox zoo; Destructoid adds "research all educational facilities" `[Hypothesis -- unverified]` [refs 3, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** education boards, speakers, talk points, educators; not Sandbox
- **vector-binding:** `items/builds.md` (hybrid education pattern)
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** no strategy claim beyond the Chapter 3 education pattern; P3 was skipped at setup, so this stays open until a doctor pass
_source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Unbothered. Focused. Thriving.
- **id:** unbothered_focused_thriving
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** 3 species Thriving at once in a zoo; thriving needs the species researched first [refs 3, 26]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** species research
- **vector-binding:** `animals/welfare_breeding_release.md`; `items/upgrades.md`
- **notes:** strategy: research each species before chasing 100% welfare
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 26] · capture: browser_fetch (refs 3, 26) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Snap!
- **id:** snap
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** a photo scoring 10,000 in any Wildlife Reserve; rare animals and close shots score higher [refs 3, 29, 35]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a Wildlife Reserve; Research Photo tool
- **vector-binding:** `mechanics.md` (Wildlife Reserves)
- **notes:** strategy: close, rare, behaviour-rich subjects; crouching to approach quietly [ref 35]
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 29, 35] · capture: browser_fetch (ref 3) / web_fetch (refs 29, 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

### Shared Accommodation
- **id:** shared_accommodation
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** 5 species in one terrestrial habitat that all share a "Thriving relationship" [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** cohabitation lists (updated in 1.0.4)
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** no strategy claim (which species combinations work); P3 skipped at setup
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Paradise
- **id:** paradise
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** 5-star rating in a Wildlife Reserve [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a reserve
- **vector-binding:** `mechanics.md` (Wildlife Reserves)
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** rating inputs for the 5-star target not captured; P3 skipped at setup
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Goodwin Park
- **id:** goodwin_park
- **hidden:** yes
- **trigger_type:** mastery
- **trigger:** 5-star reputation in a zoo; an achievement name, not a site [refs 3, 28, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a zoo
- **vector-binding:** `mechanics.md` (Economy and guests)
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** reputation inputs for the 5-star target not captured; P3 skipped at setup
_source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `dependencies.md` DEP-001: a species has to be researched before it can reach the Thriving welfare state.

> **Cross-system dependency** -- see `dependencies.md` DEP-002: the 3-species Thriving achievement depends on each species being researched first.

## Collection

### Ultimate Conservationist
- **id:** ultimate_conservationist
- **hidden:** yes
- **trigger_type:** collection
- **trigger:** complete one project of every type (6 types: Animal Reintroduction, Research, Habitat Restoration, Habitat Connectivity, Outreach, Wildlife Care); weekly rotation may limit availability `[Hypothesis -- unverified]` [refs 3, 8]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** projects of each type offered
- **vector-binding:** `items/upgrades.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 8] · capture: browser_fetch (refs 3, 8) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 3, 8 are both Wikily pages, counted as one source)

### Did You Know?
- **id:** did_you_know
- **hidden:** yes
- **trigger_type:** collection
- **trigger:** make every education topic for one species available in a zoo; species research adds fact sheets as topics [refs 3, 4]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** species research
- **vector-binding:** `items/upgrades.md`
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** the per-species topic set is not enumerated (members are not individual claims); P3 skipped at setup
_source: P1 result 2026-10-19 [refs 3, 4] · capture: browser_fetch (refs 3, 4) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 3, 4 are both Wikily pages, counted as one source)

### Good Start…
- **id:** good_start
- **hidden:** yes
- **trigger_type:** collection
- **trigger:** Bronze in all 18 Career scenarios [refs 2, 3]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** the full Career chain
- **vector-binding:** `sections/career_progression.md`; chapter files (each level's Bronze list)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 2, 3] · capture: browser_fetch (refs 2, 3) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]` (refs 2, 3 are both Wikily pages, counted as one source)

### Excellent Finish
- **id:** excellent_finish
- **hidden:** yes
- **trigger_type:** collection
- **trigger:** Gold in all Career scenarios [refs 3, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** Good Start… ; every level's Gold objectives
- **vector-binding:** `sections/career_progression.md`
- **status:** scaffold
- **deferred-to:** P3
- **deferred-reason:** Gold objectives themselves are captured for 6 of 18 levels (chapter 4, P2) and partly for Great Rift Valley and Sumatra; not for the other levels, so the set members are not all individual claims; P3 skipped at setup
- **spoiler:** progression
_source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `dependencies.md` DEP-007: each species' research adds its fact sheet as an education topic.

> **Cross-system dependency** -- see `dependencies.md` SEQ-001: weekly conservation projects rotate; whether a missed one returns is unknown.

> **Cross-system dependency** -- see `dependencies.md` DEP-018.

> **Cross-system dependency** -- see `dependencies.md` DEP-019.

## Threshold

### Long Distance Builder
- **id:** long_distance_builder
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** build 25 km of barrier in total [refs 3, 28, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `items/builds.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

### Professor
- **id:** professor
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** fully research 80 different species; Franchise allows splitting research across zoos [refs 3, 4, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** field-research species need reserve play
- **vector-binding:** `items/upgrades.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 4, 28] · capture: browser_fetch (refs 3, 4) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]` (Wikily refs 3, 4 count as one source; ref 28 is the second)

### Bear-Able
- **id:** bear_able
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 3 different bear species in one zoo; base roster has Eurasian Brown Bear, Grizzly Bear, Sun Bear, Giant Panda [refs 3, 26]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 26] · capture: browser_fetch (refs 3, 26) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Full Tank
- **id:** full_tank
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 5 different species in one aquarium [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** an aquarium
- **vector-binding:** `animals/aquariums_and_aviaries.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Sieve The Day
- **id:** sieve_the_day
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** Filtration Rate of at least 5,000 in one filtration network [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** water filters and power
- **vector-binding:** `animals/aquariums_and_aviaries.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### They Do Move In Herds
- **id:** they_do_move_in_herds
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** release a release group of more than 10 animals [refs 3, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a reserve that accepts the species
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### A Few More Hoses
- **id:** a_few_more_hoses
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** an aquarium with 25 million litres volume [refs 3, 28, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** an aquarium
- **vector-binding:** `animals/aquariums_and_aviaries.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

### Green Thumb
- **id:** green_thumb
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** plant 1,000 trees in Wildlife Reserves; Destructoid suggests a new reserve save [refs 3, 29]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a reserve
- **vector-binding:** `mechanics.md` (Wildlife Reserves)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Where Am I?
- **id:** where_am_i
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** drive 10 km in the Research Vehicle [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** a reserve
- **vector-binding:** `mechanics.md` (Wildlife Reserves)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Conservation-aire
- **id:** conservation_aire
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** earn 10,000 Conservation Credits (Insider Gaming spells it "Coservation-aire") [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `mechanics.md` (Research and conservation)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Job Well Done
- **id:** job_well_done
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** release 20 release groups [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** reserve access
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Naturalist
- **id:** naturalist
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** establish 10 ecosystems [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** reserve access
- **vector-binding:** `mechanics.md` (Wildlife Reserves)
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### They Grow Up So Fast
- **id:** they_grow_up_so_fast
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** a zoo-born animal reaches 15 years old; needs ageing on [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** ageing switched on; a zoo-born animal kept alive
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Metamorphose
- **id:** metamorphose
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** a walk-through exhibit with 3 or more butterfly species (base roster has 6: Cloudless Sulphur, European Peacock, Menelaus Blue Morpho, Monarch, Old World Swallowtail, Sri Lankan Rose) [refs 3, 26]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** walk-through exhibit
- **vector-binding:** `animals/aquariums_and_aviaries.md`; `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 26] · capture: browser_fetch (refs 3, 26) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Cats and Dogs
- **id:** cats_and_dogs
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 2 canine and 2 feline species in a zoo (base canids: Grey Wolf, African Wild Dog; felids: Lion, African Leopard, Snow Leopard, Sumatran Tiger, Eurasian Lynx) [refs 3, 26]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 26] · capture: browser_fetch (refs 3, 26) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Jungle Beat
- **id:** jungle_beat
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 3 primate species in a zoo [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Birds of a Feather
- **id:** birds_of_a_feather
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 5 avian species in a zoo [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** none
- **vector-binding:** `animals/roster.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### First Steps
- **id:** first_steps
- **hidden:** yes
- **trigger_type:** threshold
- **trigger:** 10 critically endangered terrestrial or aquatic animals born in one zoo [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** breeding switched on; critically endangered species
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `dependencies.md` DEP-004: a Water Filter needs power from a Power Generator.

> **Cross-system dependency** -- see `dependencies.md` DEP-008: in Franchise, research is shared across zoos through the Planet Hub.

> **Cross-system dependency** -- see `dependencies.md` SEQ-003: poor welfare in a species' fertility window costs a breeding year.

> **Cross-system dependency** -- see `dependencies.md` DEP-011.

> **Cross-system dependency** -- see `dependencies.md` DEP-013.

## Discovery

### Just In Case
- **id:** just_in_case
- **hidden:** yes
- **trigger_type:** discovery
- **trigger:** put an aviary roof on a habitat holding a penguin or a pig, species that do not fly [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** aviary roof tool
- **vector-binding:** `animals/aquariums_and_aviaries.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Worth Its Weight in Gold
- **id:** worth_its_weight_in_gold
- **hidden:** yes
- **trigger_type:** discovery
- **trigger:** release an animal with Gold genetics [refs 3, 28]
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** an animal with Gold genetics (how to obtain one not captured)
- **vector-binding:** `animals/welfare_breeding_release.md`
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Follow Me!
- **id:** follow_me
- **hidden:** yes
- **trigger_type:** discovery
- **trigger:** Wikily and Insider Gaming: set up an Educational Tour [refs 3, 28]; Destructoid: "an educational tool for kids" [ref 29] `[Contradicted across sources -- see notes]`
- **missable:** no
- **ponr-window:** n/a
- **prereqs:** education facilities
- **vector-binding:** `items/builds.md`
- **confidence:** low
- **status:** research-integrated
_source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Contradicted across sources -- see notes]`

## Genre vocabulary
No `genre:` overlays used.

## Sources
- https://wikily.gg/planet-zoo-2/achievements (2026-10-19); https://insider-gaming.com/planet-zoo-2-achievement-trophy-list/; https://www.destructoid.com/all-planet-zoo-2-achievements-and-how-to-unlock-them/
- Names re-checked: https://us.gamesplanet.com/community/planet-zoo-2-steam-key--8723-1/achievements (2026-10-19); original stub list: https://vgtimes.ru/games/planet-zoo-2/achievements-and-trophies/
- PS5 has 39 trophies plus a Platinum [ref 28].
  _source: P1 result 2026-10-19 [ref 28 (insider-gaming.com achievement list)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
