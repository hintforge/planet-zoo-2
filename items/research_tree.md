# Planet Zoo 2 -- Research tree (topics, levels, unlocks, prerequisites)

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** doctor Branch C 2026-10-19

Built for an interactive research-planner tool. The overview of the four trees and of conservation projects is in `upgrades.md`; this file holds the topic-level data. Every claim carries its own `_source:` line. Spoiler layout: tree structure and the topic lists are tier 0; rows that name a chapter 1-3 reserve are tier 1; rows that name a chapter 4 reserve are in the last table at tier 2.

**Coverage (located vs total, 217 topics in 4 trees).** Topic names: Disease 52 of 52, Enrichment 22 of 22, Education 7 of 7, Species 100 of 136 read on the index (page 1 of 2; the other 36 names are on page 2, not read; the species topics are one per species, so the species list in `../animals/accreditation.md` is the candidate list). That is 181 of 217 names read directly. Level counts: known for all 217 (Species 3 to 6 levels with a distribution for all 136, Disease 3, Enrichment 1, Education 1). Level-by-level unlock text read on the topic's own page for 22 of 217 topics: 20 species, 1 disease (Amoebiasis; the level effect is stated once for all 52), 1 enrichment topic (Aquatic Toy Enrichments); 0 of 7 education topics. Prerequisite (research gate) data: read on the 20 species pages; for the other 116 species only the count (58 gated) and, for the Great Rift Valley, the 19 names.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research (217 topics); .../research/species; .../research/disease; .../research/enrichment; .../research/education (all under https://wikily.gg/planet-zoo-2/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## How the trees work

All four trees are researched by Vets at a Research Centre (Small: 1 researcher; Large: 6); species research happens at a habitat or exhibit that holds the species plus a Research Centre (the topic pages say "Habitat or exhibit and Research Centre"). The Research Centre needs power and a path; staff put feeding and treatment first. Totals: 217 topics, 425 thriving requirements, up to +30% fertility, up to +75% immunity.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research; https://wikily.gg/planet-zoo-2/research/wild-boar; https://wikily.gg/planet-zoo-2/research/aquatic-toy-enrichments; https://wikily.gg/planet-zoo-2/research/amoebiasis] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

| Tree | Topics | Levels per topic | What a level unlocks |
|---|---|---|---|
| Species Research | 136 (one per species) | 3 to 6: 3 levels for 8 species, 4 levels for 43, 5 for 33, 6 for 52 | thriving requirements, fertility +15% then +30%, the species fact sheet (an education topic), release groups |
| Disease Research | 52 | 3 | Level 1 Advanced Diagnosis (+25% immunity, lower lethality); Level 2 Advanced Treatment (+50%); Level 3 Advanced Pharmacology (+75%); applies to every species that can catch the disease |
| Enrichment Research | 22 (12 toys, 10 feeders) | 1 | a set of toys or feeders: 84 enrichment items in total |
| Education Research | 7 | 1 | education topics or stations: 37 topics and 8 stations across the 7 topics |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research; .../research/species; .../research/disease (all three levels); .../research/enrichment; .../research/education; https://wikily.gg/planet-zoo-2/research/amoebiasis (level names)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

Levels are listed in order on each page; no source says whether a level needs the previous one, so "level N needs level N-1" is `unknown`.
_source: doctor Branch C 2026-10-19 [Wikily species, disease and enrichment research pages] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

## Species Research: level patterns (read on 20 species pages)

Three level patterns appear on the species pages read, matching the level counts:
- **4 levels** (Golden Poison Frog, Indian Ocean Oriental Sweetlips, Lehmann's Poison Frog, Monarch, Pacific Bluefin Tuna, American Bullfrog): L1 Fertility 1 (+15%); L2 species fact sheet; L3 release groups and release to the wild; L4 Fertility 2 (+30%). No thriving requirement at any level.
- **5 levels** (Giant Grouper, Great Hammerhead, Javanese Cownose Ray, Komodo Dragon, Ocean Sunfish, Sailfin Snapper, Sand Tiger Shark, Snow Leopard, Western Lowland Gorilla): L1 Thriving Requirement 1 and the fact sheet; L2 Thriving Requirement 2 and Fertility 1; L3 Thriving Requirement 3 (Food Grade 2) and release groups; L4 Thriving Requirement 4; L5 Thriving Requirement 5 and Fertility 2.
- **6 levels** (Wild Boar, European Bison, Golden Eagle, Reticulated Giraffe, White-Backed Vulture): L1 Thriving Requirement 1; L2 Thriving Requirement 2 and the fact sheet; L3 release groups (Wild Boar: Thriving Requirement 2 instead, its release groups need no research); L4 Thriving Requirement 3 (Food Grade 2) and Fertility 1, behind a research gate; L5 Thriving Requirement 4; L6 Thriving Requirement 5 and Fertility 2.
_source: doctor Branch C 2026-10-19 [Wikily research pages read: https://wikily.gg/planet-zoo-2/research/american-bullfrog; .../golden-poison-frog; .../indian-ocean-oriental-sweetlips; .../lehmanns-poison-frog; .../monarch; .../pacific-bluefin-tuna; .../giant-grouper; .../great-hammerhead; .../javanese-cownose-ray; .../komodo-dragon; .../ocean-sunfish; .../sailfin-snapper; .../sand-tiger-shark; .../snow-leopard; .../western-lowland-gorilla; .../wild-boar; .../european-bison; .../golden-eagle; .../reticulated-giraffe; .../white-backed-vulture] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

The 425 thriving requirements equal 5 x (33 five-level + 52 six-level species) = 425, which fits "every 5- and 6-level species has 5 thriving requirements and 3- and 4-level species have none". The 3-level species were not read.
_source: model analysis, doctor Branch C 2026-10-19 [level distribution and 425 total from https://wikily.gg/planet-zoo-2/research/species; patterns above] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

## Prerequisites (research gates)

58 species open their later levels only after an Observation Network (Observation Platform) is set up in a Wildlife Reserve and the species is released there. On every 6-level page read, the gate sits before Level 4 and names the reserve; Level 4 is the first level with Fertility 1. Counts by reserve are in `upgrades.md`; the Great Rift Valley list (19) is named on the Wikily species page: Aardvark, African Leopard, African Tigerfish, African Wild Dog, Black Wildebeest, Blunthead Cichlid, Cape Buffalo, Common Warthog, Gemsbok, Greater Flamingo, Lion, Masai Giraffe, Meerkat, Nyala, Plains Zebra, Sable Antelope, Secretarybird, Shoebill, Spotted Hyena.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/species; https://wikily.gg/planet-zoo-2/research; .../research/wild-boar] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-012: later research levels for 58 species need an Observation Network in a reserve plus a release of the species there.

Research Networks in a Wildlife Reserve "open Research Gates and unlock higher levels of Species Research"; the network pieces are Observation Platforms, Camera Traps and Acoustic Monitors, which also raise the reserve's Research Rating. Franchise Accreditation hands them out: Observation Platform at tier 1, Camera Trap at tier 2, Acoustic Monitor at tier 3 (Career: Camera Trap at tier 2 and Acoustic Monitor at tier 3 per Gamerant).
_source: doctor Branch C 2026-10-19 [https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves; https://primagames.com/gaming/how-to-raise-planet-zoo-2-franchise-accreditation-level; https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/; https://gamerant.com/accreditation-planet-zoo-2/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Corroborated: 4 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-026: Accreditation tiers hand out the Research Network pieces.

Release groups are enabled by research for 109 species and need no research for 27 species (Wikily species page); Wild Boar and Aardvark are among the 27. Fertility and the fact sheet are not gated by any reserve on the pages read.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/species; .../research/wild-boar; https://wikily.gg/planet-zoo-2/release-groups/aardvark] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-023: a species' release groups unlock at a research level.

Other prerequisites (all trees): a built Research Centre with power and a path, and Vets on staff (see `support_items.md`). A species must be researched in a zoo before it can reach the Thriving welfare state (see `../dependencies.md`).
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research; existing claims in `upgrades.md`] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-003: research is done by Vets working in a powered, path-connected Research Centre.

> **Cross-system dependency** -- see `../dependencies.md` DEP-001: a species has to be researched before it can reach the Thriving welfare state.

## Disease Research: 52 topics (3 levels each)

Species that can catch each disease, as counted on Wikily's disease index (the names of the species were read for Amoebiasis only: Blackspotted Puffer, Blacktip Reef Shark, Clown Triggerfish, Dolphinfish, Galapagos Giant Tortoise, Giant Grouper, Great Hammerhead, Humphead Wrasse, Indo-Pacific Leopard Shark, Javanese Cownose Ray, Komodo Dragon, Nile Monitor, Ocean Sunfish, Ocellated Eagle Ray, Red Lionfish, Sailfin Snapper, Sand Tiger Shark).

| Disease | Species | Disease | Species | Disease | Species |
|---|---|---|---|---|---|
| Amoebiasis | 17 | Foot And Mouth Disease | 27 | Piscine Mycobacteriosis | 16 |
| Aspergillosis | 14 | Furunculosis | 15 | Q Fever | 29 |
| Avian Herpesvirus | 13 | Fusariosis | 14 | Rabbit Haemorrhagic Disease Virus | 1 |
| Avian Influenza | 63 | Glanders | 25 | Rotavirus | 49 |
| Avian Tuberculosis | 16 | Hepatitis A | 7 | Salmonellosis | 83 |
| Avipoxvirus | 13 | Isopodiasis | 14 | Simian Haemorrhagic Fever | 7 |
| Bordetellosis | 45 | Listeriosis | 50 | Staphylococcus Infection | 2 |
| Botulism Toxicosis | 50 | MRSA | 44 | Streptococcosis | 17 |
| Campylobacteriosis | 53 | Marek's Disease | 13 | Testudinid Herpesvirus | 1 |
| Candidiasis | 14 | Mpox | 7 | Tetanus | 28 |
| Canine Distemper Virus | 16 | Mycoplasmosis | 2 | Toxoplasmosis | 2 |
| Classical Swine Fever | 3 | Nematodiasis | 34 | Tularemia | 50 |
| Cowpox Virus | 49 | Newcastle Disease | 13 | Ulcerative Dermatitis | 5 |
| EEHV | 2 | Nile Crocodile Poxvirus | 2 | Ulcerative Stomatitis | 5 |
| European Brown Hare Syndrome Virus | 1 | Feather Lice | 13 | Usutu Virus | 13 |
| FIP | 5 | Velvet Disease | 14 | Vibriosis | 16 |
| Viral Erythrocytic Necrosis | 15 | Viral Papillomatosis | 1 | West Nile Virus | 15 |
| White Spot Disease | 14 | | | | |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/disease; https://wikily.gg/planet-zoo-2/research/amoebiasis (species names and level effects)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

Each disease has three levels with the same effect pattern (Advanced Diagnosis +25% immunity, Advanced Treatment +50%, Advanced Pharmacology +75%, each with lower lethality), read on the Amoebiasis page and stated for all 52 on the tree page. Prerequisites between diseases: none stated.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/amoebiasis; https://wikily.gg/planet-zoo-2/research/disease] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Enrichment Research: 22 topics (1 level each)

Toys (12): Aquatic Toy Enrichments, Auditory Toy Enrichments, Ball Toy Enrichments, Biting Toy Enrichments, Curiosity Toy Enrichments, Destructible Toy Enrichments, Manipulation Toy Enrichments, Navigational Toy Enrichments, Olfactory Toy Enrichments, Resting Toy Enrichments, Sensory Toy Enrichments, Water Feature Toy Enrichments. Feeders (10): Arboreal Food-based Enrichments, Browsing Food-based Enrichments, Carnivore Food-based Enrichments, Dexterity Food-based Enrichments, Feeder Ball Food-based Enrichments, Foraging Food-based Enrichments, Frozen Food-based Enrichments, Herbivorous Food-based Enrichments, Hunting Food-based Enrichments, Insectivore Food-based Enrichments. The toy and feeder split is read from the names and matches Wikily's counts (12 toy topics, 10 feeder topics); Aquatic Toy Enrichments is labelled Toys on its own page.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/enrichment; https://wikily.gg/planet-zoo-2/research/aquatic-toy-enrichments] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

Unlock read for 1 of 22 topics: Aquatic Toy Enrichments, Level 1 unlocks Submarine Buoy, Lattice Ball and Square Float (3 items). The other 21 topics' item lists were not read (84 items in total across the 22 topics, so 81 items are unnamed here); each topic is researched at a Research Centre.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/aquatic-toy-enrichments; https://wikily.gg/planet-zoo-2/research/enrichment] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Education Research: 7 topics (1 level each)

Activity Patterns, Animal Diets, Aquatic Ecosystem Ambiences, Conservation Threats, Human Conservation Impact, Interactive Education Stations, Terrestrial Ecosystem Ambiences. Wikily groups them as Conservation Boards 2, Education Boards 2, Interactive 1, Speakers 2; which topic is in which group, and what each topic unlocks, was not read (37 education topics and 8 stations in total, split across the seven).
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/education] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Species Research: levels read topic by topic

"TR n" = Thriving Requirement n. "Fert 1 / Fert 2" = Fertility Level 1 (+15% fertility) / Level 2 (+30%). All 20 species pages state "Researched by Vets" at "Habitat or exhibit and Research Centre". Rows for species whose research touches a chapter 4 reserve are in the last table.

### Starting-content and progression species (puzzle-tier 1)

| Species | Levels | Level-by-level unlocks | Research gate |
|---|---|---|---|
| Wild Boar | 6 | L1 TR1: at least 20 objects or plants tagged Tree Litter; L2 fact sheet; L3 TR2: Waterlogged terrain; L4 TR3: Food Grade 2, Fert 1; L5 TR4: at least 50% native plants; L6 TR5: Mud Bath, at least 3, Fert 2. Release groups available without research | Before L4: an Observation Network (Observation Platform) in Scottish Highlands and the species released there |
| American Bullfrog | 4 | L1 Fert 1; L2 fact sheet; L3 release groups and release to the wild; L4 Fert 2 | none |
| Javanese Cownose Ray | 5 | L1 TR1: Forage Tray, at least 3, and fact sheet; L2 TR2: Fine Sand terrain, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: Bubble Blower - Airstone, at least 2; L5 TR5: Large Indo-Pacific Reef animals Social Group, Fert 2 | none |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/wild-boar; .../research/american-bullfrog; .../research/javanese-cownose-ray] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

### Species at accreditation tiers 4 and 5 (late-game, puzzle-tier 2)

| Species | Levels | Level-by-level unlocks | Research gate |
|---|---|---|---|
| Giant Grouper | 5 | L1 TR1: at least 25 objects or plants tagged Rocks, and fact sheet; L2 TR2: Coarse Sand terrain, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: at least 10 tagged Coral; L5 TR5: Rough Rock terrain, Fert 2 | none |
| Golden Eagle | 6 | L1 TR1: at least 10 tagged Climbable; L2 TR2: at least 10 tagged Rocks, and fact sheet; L3 release groups; L4 TR3: Food Grade 2, Fert 1; L5 TR4: at least 50% native plants; L6 TR5: Cup Nest - Large, at least 3, Fert 2 | Before L4: an Observation Network (Observation Platform) in Sweden Reserve and the species released there |
| Golden Poison Frog | 4 | L1 Fert 1; L2 fact sheet; L3 release groups; L4 Fert 2 | none |
| Great Hammerhead | 5 | L1 TR1: Blood Scent Marker, at least 2, and fact sheet; L2 TR2: at least 5 tagged Rocks, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: Aquatic Feeder - Fish, at least 2; L5 TR5: Suspended Bait, at least 2, Fert 2 | none |
| Indian Ocean Oriental Sweetlips | 4 | L1 Fert 1; L2 fact sheet; L3 release groups; L4 Fert 2 | none |
| Komodo Dragon | 5 | L1 TR1: Restraint Feeder, at least 2, and fact sheet; L2 TR2: Soil terrain, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: at least 50% native plants; L5 TR5: Deep Water Surface Area, Fert 2 | none |
| Lehmann's Poison Frog | 4 | L1 Fert 1; L2 fact sheet; L3 release groups; L4 Fert 2 | none |
| Monarch | 4 | L1 Fert 1; L2 Monarch Butterfly fact sheet; L3 release groups; L4 Fert 2 | none |
| Ocean Sunfish | 5 | L1 TR1: Bubble Blower - Airstone, at least 2, and fact sheet; L2 TR2: Aquatic Feeder - Flakes, at least 1, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: Sand terrain; L5 TR5: Deep Water Surface Area, Fert 2 | none |
| Pacific Bluefin Tuna | 4 | L1 Fert 1; L2 fact sheet; L3 release groups; L4 Fert 2 | none |
| Sailfin Snapper | 5 | L1 TR1: at least 5 tagged Rocks, and fact sheet; L2 TR2: at least 12 tagged Coral, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: at least 50% native plants; L5 TR5: Coarse Sand terrain, Fert 2 | none |
| Sand Tiger Shark | 5 | L1 TR1: Blood Scent Marker, at least 2, and fact sheet; L2 TR2: at least 5 tagged Rocks, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: at least 5 tagged Coral; L5 TR5: Suspended Bait, at least 2, Fert 2 | none |
| Snow Leopard | 5 | L1 TR1: Ice Block, at least 3, and fact sheet; L2 TR2: at least 20 tagged Rocks, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: Scratching Post, at least 1; L5 TR5: Prey-scented Sack, at least 2, Fert 2 | none |
| Western Lowland Gorilla | 5 | L1 TR1: at least 4 tagged Climbable, and fact sheet; L2 TR2: at least 6 tagged Rocks, Fert 1; L3 TR3: Food Grade 2, release groups; L4 TR4: at least 50% native plants; L5 TR5: Water Surface Area, Fert 2 | none |

_source: doctor Branch C 2026-10-19 [Wikily research pages under https://wikily.gg/planet-zoo-2/research/: giant-grouper, golden-eagle, golden-poison-frog, great-hammerhead, indian-ocean-oriental-sweetlips, komodo-dragon, lehmanns-poison-frog, monarch, ocean-sunfish, pacific-bluefin-tuna, sailfin-snapper, sand-tiger-shark, snow-leopard, western-lowland-gorilla] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

### Species whose research gate names a chapter 4 reserve (late-game, puzzle-tier 2)

| Species | Levels | Level-by-level unlocks | Research gate |
|---|---|---|---|
| European Bison | 6 | L1 TR1: at least 8 objects or plants tagged Bushes; L2 TR2: Water Surface Area, and fact sheet; L3 release groups; L4 TR3: Food Grade 2, Fert 1; L5 TR4: at least 50% native plants; L6 TR5: Mud Bath, at least 2, Fert 2 | Before L4: an Observation Network (Observation Platform) in Poland Reserve and the species released there |
| Reticulated Giraffe | 6 | L1 TR1: at least 5 tagged Acacia Tree; L2 TR2: Smooth Rock terrain, and fact sheet; L3 release groups; L4 TR3: Food Grade 2, Fert 1; L5 TR4: at least 8 tagged Spreading Crown; L6 TR5: African Savannah Social Group, Fert 2 | Before L4: an Observation Network (Observation Platform) in Tanzania Reserve and the species released there |
| White-Backed Vulture | 6 | L1 TR1: Ribbed Feeder, at least 4; L2 TR2: at least 20 tagged Climbable, and fact sheet; L3 release groups; L4 TR3: Food Grade 2, Fert 1; L5 TR4: at least 50% native plants; L6 TR5: Canopy Platform Nest - Large, at least 8, Fert 2 | Before L4: an Observation Network (Observation Platform) in Tanzania Reserve and the species released there |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/european-bison; .../reticulated-giraffe; .../white-backed-vulture] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

## Fill-in target: one species' research levels, from a player's screenshots

For a Hintforge reader or builder session transcribing screenshots. The player only plays and captures; the session writes the row. The Accreditation tree page (`../artifacts/accreditation_tree.html`) shows a species' levels as soon as its row is here.

1. **Screen to capture:** the species' own research screen in the game, showing every level and what each level asks for and unlocks (a thriving requirement, a fertility step, the fact sheet, release groups), plus any Observation Network gate marker. If the game shows one level at a time, one capture per level. The menu path to that screen is not documented.
2. **Record per level, in the game's own wording:** the level number; the thriving requirement and its numbers (object counts, terrain, food grade, native-plant share, social group); `Fert 1` or `Fert 2` where a fertility step is shown; `fact sheet`; `release groups`. Gate: `none`, or `Before L<n>: an Observation Network (Observation Platform) in <reserve> and the species released there`.
3. **Row shape** (the columns `../artifacts/extract.py` reads; the species name must match `../animals/accreditation.md` exactly, `Levels` is a number and must equal the count of `L<n>` entries, entries are separated by `; `):

| Species | Levels | Level-by-level unlocks | Research gate |
|---|---|---|---|
| (species name) | (number of levels) | (L1 ...; L2 ...; L3 ...) | (none, or Before L<n>: ...) |

4. **Place the filled row** in the table above whose spoiler tier fits the species (Career or Franchise tier 4 or 5: the late-game table; otherwise the progression table), and add its own metadata line directly under that table, one per batch of screenshots: `_source: player screenshot <YYYY-MM-DD> [<what the screenshots show>] · capture: manual_paste · confidence: medium (low for one unclear capture) · enemy-tier: 0 · puzzle-tier: <1 or 2> · category: mainline · spoiler: <progression or late-game>`. Delete nothing from the template; a blank template row is not a claim.
5. **Rebuild:** `python -I ../artifacts/extract.py`, then `python -I ../artifacts/build.py`. The extractor prints a WARNING for an unknown species name or a level count that does not match.

## Contradictions and gaps

- **Release-group counts do not agree inside Wikily.** The species research page says 109 species have release groups by research and 27 without research (109 + 27 = 136), but the release-group index lists 104 releasable species, and the American Bullfrog's research page unlocks "release groups and release to the wild" at Level 3 although the Bullfrog is not on the 104-species index page read. So the "no group listed" entries in `../animals/accreditation.md` may be missing release groups the research pages promise. Unresolved.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/species; https://wikily.gg/planet-zoo-2/release-groups; https://wikily.gg/planet-zoo-2/research/american-bullfrog] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Contradicted across sources -- see notes]`
- **Gate versus level count.** 58 species are gated but only 52 species have 6 levels; every 6-level page read has its gate before Level 4. Where the gate sits for gated species with other level counts was not read.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/research/species and the species pages read] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`
- **Not read:** the level text for 114 species, the item lists of 21 enrichment topics, the education topic unlocks, the page-2 species names of the research index, and the species lists of 51 diseases. A Sportskeeda guide (https://www.sportskeeda.com/esports/planet-zoo-2-research-guide-all-research-types-explained) returned HTTP 405 to a plain fetch and was not opened in the browser tool; its search excerpt only repeats the 217-topic split.
_source: doctor Branch C 2026-10-19 [Sportskeeda search excerpt; Wikily pages above] · capture: n/a · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
