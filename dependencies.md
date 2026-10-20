# Dependencies -- Planet Zoo 2
<!-- hintforge · stitch pass · last run: 2026-10-19 -->
<!-- Every stitch run re-audits ALL existing edges + adds new ones. The per-edge convergence audit (open each cited source, verify the specific value) applies to every row in this file on every run, not just new candidates. A game patch, DLC, or new ingestion phase can change facts that existing edges cite -- only a full re-audit catches that. See `stitch_and_zipper.md` Phase B "Re-run scope: always full." Inconsistencies (cited source contradicts edge text) land in the `## Corpus inconsistencies` section; the edge row stays in place. -->

**status:** research-integrated

Rows are grouped into tables by the highest spoiler tier any row names. Each table carries its own metadata line directly under it; a reader gated below that tier does not see that table. Inline cross-references in the corpus files point here by DEP ID and name nothing above the tier of the block they sit in.

## Cross-system edges

### Tier 0 (puzzle-tier 0, spoiler none)

| Edge ID | System A | System B | Dependency description | Confidence | Source files | Related DEP(s) |
|---------|----------|----------|------------------------|------------|--------------|----------------|
| DEP-001 | Species research (research trees) | Thriving welfare state | A species has to be researched before it can reach the Thriving welfare state; 100% welfare does not stand in for the research. Research also reveals that species' thriving requirements. | medium | items/upgrades.md, animals/welfare_breeding_release.md, achievements.md, items/builds.md, items/research_tree.md | DEP-002 |
| DEP-002 | Thriving welfare state | The achievement for 3 species Thriving at once in one zoo | The 3-species Thriving achievement rests on DEP-001: each of the three species has to be researched first. | medium | achievements.md, items/upgrades.md, animals/welfare_breeding_release.md | DEP-001 |
| DEP-003 | Research Centre staffing (Vets) | Species research progress | Species research is done by Vets working in a powered, path-connected Research Centre (Small: 1 researcher, Large: 6); the achievement for fully researching one species lists a Research Centre with a Vet as a prerequisite. | medium | items/upgrades.md, achievements.md, items/research_tree.md | |
| DEP-004 | Aquarium Water Filter | Power Generator and the Filtration Rate achievement | A Water Filter needs power: an unpowered filter shows a "Not Powered" warning, an early aquarium objective asks for a filter and a generator together, and the Filtration Rate achievement (5,000 in one network) lists filters and power as prerequisites. The "generator in radius" detail is a search-excerpt lead only. | medium | animals/aquariums_and_aviaries.md, sections/chapter_2_paws_on_the_path.md, achievements.md | |
| DEP-005 | Aquarium Staff Gate | Path network | An aquarium is built around a Staff Gate that has to be connected to the path network (an early aquarium objective asks for exactly this); the general habitat pattern is a staff gate on a staff path. | medium | animals/aquariums_and_aviaries.md, sections/chapter_2_paws_on_the_path.md, items/builds.md | |
| DEP-006 | Nests | Bird and egg-laying reptile breeding; an early bird-habitat objective | Flying birds, flightless birds and egg-laying reptiles need a nest per breeding pair and cannot conceive until the pair has claimed one; an early Career bird-habitat objective requires a suitable nest, and its guide note says the roof and the nest are separate requirements. | medium | animals/welfare_breeding_release.md, sections/chapter_1_wild_at_heart.md, sections/chapter_3_claws_and_effect.md (a gifted bird group "needs nesting"), mechanics.md (patch fix for juvenile birds stuck in nests) | |
| DEP-007 | Species research | Education topics | Each species' research adds its fact sheet as an education topic, so research progress decides which topics a zoo can show; the make-every-topic-available achievement lists species research as its prerequisite. | medium | items/upgrades.md, achievements.md, items/research_tree.md | |
| DEP-008 | Franchise shared research (Planet Hub) | The 80-species full-research threshold | In Franchise research is shared across zoos through the Planet Hub, so the 80-species full-research threshold can be met by splitting research across several zoos. | medium | mechanics.md, achievements.md, sections/career_progression.md | DEP-013 |
| DEP-023 | Species research level | Release Groups | A species' release groups are enabled at a research level: Level 3 on the species pages read (the eight predators read, and the 4-, 5- and 6-level patterns), with two exceptions: Wild Boar's release groups need no research, and the Aardvark release group is available without research. Wikily counts research-enabled release groups for 109 species and none for 27 (a count that conflicts with its 104 release groups, an unresolved conflict recorded in `items/research_tree.md`). | medium | items/research_tree.md, items/upgrades.md, animals/reserve_ecosystems.md, animals/accreditation.md | DEP-012, DEP-016 |
| DEP-024 | Accreditation tier | Species in Animal Trading | Each Accreditation tier adds species to Animal Trading on top of the earlier tiers (additions, not running totals), and a species is buyable only once its tier is unlocked, its edition includes it and, in Franchise, the player market lists one. Career tiers are gated by medals (`sections/career_progression.md`); Franchise tiers by zoo and reserve star counts (`mechanics.md`). | medium | animals/accreditation.md, sections/career_progression.md, mechanics.md, items/upgrades.md | DEP-026 |
| DEP-025 | Trade Centre (connected by path) | Adopting species from Animal Trading | Every species is adopted through Animal Trading, which needs a working Trade Centre in the zoo; an early Career objective that moves two animals "from the Trade Centre" notes the Trade Centre needs a connected path and that staff deliver the animals after a wait. | medium | animals/accreditation.md, sections/chapter_1_wild_at_heart.md | DEP-024 |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply) · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Tier 1 (puzzle-tier 1, spoiler progression)

| Edge ID | System A | System B | Dependency description | Confidence | Source files | Related DEP(s) |
|---------|----------|----------|------------------------|------------|--------------|----------------|
| DEP-009 | Career Bronze rewards | Species research levels | Two Career levels hand out research levels as rewards given during Bronze; one of them also has an objective to research two of its species to L3 while its reward lists L2 for the same species, so the objective sits one level above the reward. | medium | items/upgrades.md, sections/chapter_2_paws_on_the_path.md, sections/chapter_3_claws_and_effect.md | |
| DEP-010 | Zoo level setting: ageing and breeding (switched on at a medal tier) | The first-baby-born-in-a-zoo achievement | In the first Career zoo, ageing and breeding start Off and switch on at Silver; the first-baby achievement needs breeding switched on, so it cannot be earned in that zoo before that medal tier. | medium | sections/chapter_1_wild_at_heart.md, sections/career_progression.md, achievements.md, animals/welfare_breeding_release.md | DEP-011 |
| DEP-011 | Level setting: ageing and animal death | The zoo-born-animal-reaches-15-years achievement | That achievement needs ageing switched on and the animal kept alive; the first Career zoo turns ageing on at Silver while death from old age, disease and fights stay Off there, and the first reserve level turns ageing and old-age death on only at Gold. | medium | sections/chapter_1_wild_at_heart.md, sections/career_progression.md, achievements.md | DEP-010 |
| DEP-012 | Reserve Observation Network | Later research levels for 58 species | For 58 species the later research levels open only after an Observation Network is built in a Wildlife Reserve and the species is released there; an early reserve objective builds that network from three non-overlapping Observation Platforms. | medium | items/upgrades.md, sections/career_progression.md, achievements.md, sections/chapter_2_paws_on_the_path.md, items/research_tree.md | DEP-013, DEP-023, DEP-026 |
| DEP-013 | Field research (DEP-012) | The full-research achievements (1 species; 80 species) | Fully researching a species, or 80 species, can require reserve play and not only zoo research, because the field-research species stop at their early levels until the DEP-012 conditions are met. | medium | achievements.md, items/upgrades.md, items/research_tree.md | DEP-012, DEP-008 |
| DEP-014 | Aviary Staff Gate connection | Aviary habitat registration | An aviary can read "No Habitat Selected" until its Staff Gate is connected to a path, and an early bird-habitat guide note says the connection has to be a staff path, not a guest path. | medium | sections/chapter_1_wild_at_heart.md, sections/chapter_3_claws_and_effect.md, items/builds.md | DEP-005 |
| DEP-015 | Planet Hub conservation projects | A Chapter 3 level objective | One Chapter 3 level objective requires completing a Career-only conservation project, and its guide note says the project is completed in the Planet Hub, where conservation decisions are made. | medium | sections/chapter_3_claws_and_effect.md, items/upgrades.md, mechanics.md | |
| DEP-016 | Reserve ecosystem state and species roles | Release Groups | A reserve takes a Release Group only once the species' release requirements are met (an Established ecosystem, required roles); an early reserve guide warns a release can stay blocked even after an ecosystem shows Established because a plant requirement can drop below its threshold again. | medium | mechanics.md, sections/career_progression.md, sections/chapter_2_paws_on_the_path.md, animals/reserve_ecosystems.md | DEP-022, DEP-023, DEP-027 |
| DEP-026 | Accreditation tiers 2 and 3 | Research Network pieces (Camera Trap, Acoustic Monitor) | The Camera Trap comes with Accreditation tier 2 and the Acoustic Monitor with tier 3 (Franchise: two guides agree; Career: one guide, Gamerant, via `items/research_tree.md`), and the Observation Platform with Franchise tier 1; the Career gate page says only that higher tiers bring new research network types. The pieces make up the Research Network that "opens Research Gates"; the species gates read name the Observation Platform only. | medium | items/research_tree.md, mechanics.md, sections/career_progression.md | DEP-012, DEP-024 |
| DEP-027 | Prey roles filled by earlier releases | A predator's release group | A predator's release group waits for the prey roles it requires to be filled by animals already released: every predator read needs a Medium Prey role (the Grey Wolf also Small Prey), and a Sweden Reserve tip says to release the Red Deer and Wild Boar before the Grey Wolf. Which species fill the prey roles was not read (the fill lists are `unknown`). | medium | animals/reserve_ecosystems.md, sections/chapter_3_claws_and_effect.md | DEP-016 |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply) · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_

### Tier 2 (puzzle-tier 2, spoiler late-game)

| Edge ID | System A | System B | Dependency description | Confidence | Source files | Related DEP(s) |
|---------|----------|----------|------------------------|------------|--------------|----------------|
| DEP-017 | Career Accreditation Tier 5 | The highest-Accreditation achievement | Tier 5 needs 18 Bronze and 2 Silver medals; the achievement for reaching the highest Accreditation in a non-Sandbox hub is earned through that tier in Career. | medium | sections/career_progression.md, achievements.md | DEP-018 |
| DEP-018 | A Bronze medal in every Career level (18) | The all-Bronze collection achievement | The collection achievement "Good Start..." needs Bronze in all 18 Career scenarios. Hypothesis, unverified: the 18 Bronze medals that Accreditation Tier 5 counts are taken to be the same 18 (the corpus marks "all 18 levels" for Tier 5 as a hypothesis, `sections/career_progression.md`). | medium | sections/career_progression.md, achievements.md | DEP-017, DEP-019 |
| DEP-019 | A Gold medal in every Career level | The all-Gold collection achievement | "Excellent Finish" needs Gold in all Career scenarios and lists the all-Bronze achievement as a prerequisite; Gold lists are captured for only some levels, so its set members are incomplete. | medium | sections/career_progression.md, achievements.md | DEP-018 |
| DEP-020 | The Maluku Islands Bronze objective (adopt an Ocean Sunfish, raise its welfare to 100%) | The achievement "Mola Mola Likes You" | The Bronze objective asks for the same outcome the achievement asks for (100% welfare on an Ocean Sunfish); the chapter file records the two as overlapping. | medium | sections/chapter_4_fentastic_opportunity.md, achievements.md, animals/aquariums_and_aviaries.md | |
| DEP-021 | Swiss Alps release groups | Poland Reserve release objective | The Swiss Alps Bronze asks for Eurasian Beaver and Eurasian Bittern Breeding Partners release groups, the same groups the Poland Reserve Bronze releases; the guide calls this an informal dependency for animals, not a hard unlock. | medium | sections/chapter_4_fentastic_opportunity.md, animals/reserve_releases.md | DEP-022 |
| DEP-022 | Wildlife Reserve release objectives | Each reserve's releasable-species list | Every release-group objective captured for the six Wildlife Reserve levels names species that appear on that reserve's releasable list; spot-audited for all six reserves, no mismatch found. | medium | sections/chapter_1_wild_at_heart.md, sections/chapter_2_paws_on_the_path.md, sections/chapter_3_claws_and_effect.md, sections/chapter_4_fentastic_opportunity.md, animals/reserve_releases.md, animals/reserve_ecosystems.md | DEP-021, DEP-016 |
| DEP-028 | Poland Reserve Gold objective (at least 5 Flourishing ecosystems) | Releases that fill ecosystem roles | The Poland Gold objective counts Flourishing ecosystems, and an ecosystem begins Flourishing only after all its Ecosystem Roles are filled by released animals; the Poland guide note says a Bittern release can stay blocked by missing roles (Wetland Engineers, Terrestrial Foragers). The Tanzania Gold objective asks for 9 Established ecosystems instead, which need only the Area, Terrain and Nature requirements met. | medium | sections/chapter_4_fentastic_opportunity.md, animals/reserve_ecosystems.md | DEP-016, DEP-022 |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply) · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_

### Optional cluster links

Each independently testable relationship gets its own DEP row and audit. A genuinely indivisible relationship stays one row. The `Related DEP(s)` column links facets of one cluster; every ID listed there exists in this file. A shared name alone does not justify a relationship.

## PoNR / lockout edges

### Tier 1 (puzzle-tier 1, spoiler progression)

| Edge ID | Trigger | Locked out | Notes | Source files |
|---------|---------|------------|-------|--------------|
| PON-001 | Committing animals to a release (a Release Group, or a quick release) | Returning those animals to the zoo; following a quick-released animal afterwards | Animals committed to a Release Group cannot return to the zoo; a quick-released animal cannot be followed. One-way; no timing window stated. | sections/career_progression.md, mechanics.md, animals/welfare_breeding_release.md |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply) · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_

## Missable / sequencing dependencies

### Tier 0 (puzzle-tier 0, spoiler none)

| Edge ID | Action | Window | Consequence | Source files |
|---------|--------|--------|-------------|--------------|
| SEQ-001 | Skipping a weekly conservation project | Weekly rotation | Possibly time-limited; whether a missed project returns is unknown. The achievement that needs one project of every type may be harder to complete. Hypothesis, low confidence. | items/upgrades.md, sections/missables.md, achievements.md, sections/career_progression.md |
| SEQ-002 | Lowering difficulty on a Career level | Before lowering it on a level where an achievement is being pursued | Changing difficulty can affect whether achievements can be earned; each medal records the difficulty it was earned on and the completion screen shows the lowest. | sections/career_progression.md, sections/missables.md, achievements.md |
| SEQ-003 | Poor welfare during a species' seasonal fertility window | The per-year fertility window | Costs a whole breeding year (recoverable next year, not permanent), which delays breeding-count goals such as 10 critically endangered births in one zoo. | animals/welfare_breeding_release.md, sections/missables.md, achievements.md |
| SEQ-004 | Repaying the starting loan | Before operating cash has been built | Guide advice: repaying early risks stalling the early economy-recovery level (not a hard lock); that level's Bronze list includes paying off all loans. | sections/chapter_2_paws_on_the_path.md, mechanics.md, items/builds.md |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply) · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Tier 1 (puzzle-tier 1, spoiler progression)

| Edge ID | Action | Window | Consequence | Source files |
|---------|--------|--------|-------------|--------------|
| SEQ-005 | Building another enclosure on a level that caps the habitat count | While the level's habitat-cap objective is still open | Not a permanent lockout (guide advice, not a hard lock): building an enclosure per arrival can make the cap objective unsatisfiable until space is freed. The fix: free space by finalising release groups first. | sections/chapter_3_claws_and_effect.md, items/builds.md |

_source: stitch pass 2026-10-19 over the cited corpus files (each file's own per-claim sources apply); moved here from PON-002 by doctor Branch C 2026-10-19 · capture: corpus-synthesis · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_

## Stitch run log

| Date | Scope | Edges written | Edges proposed (pending) | Inconsistencies surfaced | Model |
|------|-------|---------------|--------------------------|--------------------------|-------|
| 2026-10-19 | full | 28 | 0 | 0 | sonnet-class (Sonnet 5.5), reasoning inline |
| 2026-10-19 (re-stitch after doctor repair #3) | full (28 existing edges re-audited; 3 new files read) | 6 | 0 | 1 | sonnet-class (Sonnet 5.5), reasoning inline |

<!-- Inconsistencies surfaced: count from the per-edge convergence audit (stitch_and_zipper.md Phase B). Counts must be derived by reading this file, not recalled. A non-zero count requires an explicit chat call-out and at least one populated row in the Corpus inconsistencies section below. -->

## Corpus inconsistencies

Stitch's per-edge convergence audit (see [`stitch_and_zipper.md`](https://github.com/hintforge/builder/blob/main/stitch_and_zipper.md) Phase B) populates this section when a candidate edge's cited sources contradict each other. Each row records the contradiction; resolving it is the user's call (or a follow-up doctor / ingestion run). Edges blocked on an unresolved entry are NOT written to the tables above until the inconsistency is closed.

| Detected | Files | Conflicting values | Suspected authoritative source | Status |
|----------|-------|--------------------|--------------------------------|--------|
| 2026-10-19 | none | The first 2026-10-19 audit found no edge whose cited sources disagree on the edge's value | n/a | none open |
| 2026-10-19 (re-stitch) | `mechanics.md` line 67; `animals/accreditation.md` "How a species is obtained" | `mechanics.md` says Conservation Credits "buy higher-tier animals"; `accreditation.md` says cash and Conservation Credits do not bypass a tier lock (allthings.how). "Higher-tier" may mean pricier animals inside already-unlocked tiers, so this may be wording rather than a conflict. DEP-024 states neither reading. | `accreditation.md` (more specific, names the guide) | resolved 2026-10-19: `mechanics.md` reworded to "spent on higher-tier animals ... they do not unlock its Accreditation tier", consistent with both sources |

<!-- Status vocabulary: open (just surfaced) | resolved (user picked authoritative value + corrected the other file) | accepted (user accepted both -- rare; usually means the claim is genuinely ambiguous in-game). When status flips to resolved, the next stitch run can re-evaluate the edge. The source conflicts that ingestion already recorded in the corpus (marked `[Contradicted across sources]` and listed in CHECKPOINT "Open threads") are not repeated here: no edge in this file depends on them. -->
