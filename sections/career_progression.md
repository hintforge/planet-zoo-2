# Planet Zoo 2 -- Career progression (sites, unlock edges, Accreditation)

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19
**mode:** Career (offline). Franchise and Sandbox rules are in `../mechanics.md`.

**Role split (zipper 2026-10-19, accepted as design):** this file owns the progression graph (unlock rules, medal edges, Accreditation, Hub); the four `chapter_*.md` files own the per-level objectives and repeat an unlock rule only as a reader convenience. Where the two differ, this file's table is the primary claim. Which species each Accreditation tier adds is owned by `../animals/accreditation.md` (zipper 2026-10-19, role split); this file owns the medal gates.

Nav-skip corpus (no `nav/`): the zone graph for this game lives here. A "zone" is a site: a Career level (zoo or Wildlife Reserve). Movement between sites is a menu action through the Planet Hub, not travel. Per-level objectives are in `chapter_1_wild_at_heart.md` .. `chapter_4_fentastic_opportunity.md`.

## Chapters and levels (4 chapters, 18 levels: 12 zoos + 6 Wildlife Reserves)

Each level has a scenario title (canonical) and a location name (alias; the Hub and the in-game "Travel to X via the Hub" prompts use the location).

| Order | zone-id | Scenario title | Location | Type | Chapter | Unlock rule | Starting money |
|---|---|---|---|---|---|---|---|
| 1 | c1_grv | Earning Your Stripes | Great Rift Valley Reserve | Wildlife Reserve | 1 | Available from start | Unlimited |
| 2 | c1_eaf | Spreading Your Wings | East Africa | Zoo | 1 | Bronze in Great Rift Valley Reserve | $20,000 |
| 3 | c2_nfj | All A-Fjord | Nordic Fjords | Zoo (aquarium-led) | 2 | Silver in Great Rift Valley Reserve; Accreditation Tier 2 | $25,000 |
| 4 | c2_sew | Otterly Lush | South East Wales | Zoo | 2 | Bronze in Nordic Fjords | $30,000 |
| 5 | c2_neng | Grizzly Details | New England | Zoo | 2 | Bronze in South East Wales | -$2,000 (plus a $10,000 "Nest Eggs" loan) |
| 6 | c2_sco | Deer, Oh Deer | Scottish Highlands | Wildlife Reserve | 2 | Bronze in South East Wales | Unlimited |
| 7 | c2_saf | A Penny Learned | South Africa | Zoo | 2 | Bronze in South East Wales | $20,000 |
| 8 | c3_sum | Mine Your Business | Sumatra Reserve | Wildlife Reserve | 3 | 7 Bronze career medals; Accreditation Tier 3 | Unlimited |
| 9 | c3_java | Creature Comforts | Java | Zoo | 3 | Bronze in Sumatra Reserve | $10,000 |
| 10 | c3_fra | Trot To Go | Rural France | Zoo | 3 | Bronze in Sumatra Reserve | $10,000 |
| 11 | c3_mtf | Parakeet Paradise | Mountain Forests | Zoo | 3 | Bronze in Sumatra Reserve | $10,000 |
| 12 | c3_swe | Howls It Going? | Sweden Reserve | Wildlife Reserve | 3 | Silver in Sumatra Reserve AND 11 Bronze career medals | Unlimited |
_source: P1 result 2026-10-19 [refs 2, 9-20 (wikily.gg/planet-zoo-2/career and per-level pages)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_
`[Single source -- verify · class:community-wiki]` Chapter 1 rows are spoiler `none`, chapter 2 and 3 level titles are `progression`; the table is gated at the higher of the two (puzzle-tier 1). The six chapter-4 levels are in their own table below, at puzzle-tier 2.

### Chapter 4 levels (late-game, puzzle-tier 2)

| Order | zone-id | Scenario title | Location | Type | Chapter | Unlock rule | Starting money |
|---|---|---|---|---|---|---|---|
| 13 | c4_mal | Mola Money, Mola Problems | Maluku Islands | Zoo (aquarium-led) | 4 | Bronze in Sweden Reserve; Accreditation Tier 4 | $15,000 |
| 14 | c4_pol | No Ifs, No Putts | Poland Reserve | Wildlife Reserve | 4 | Bronze in Maluku Islands | Unlimited |
| 15 | c4_tan | Take Pride | Tanzania Reserve | Wildlife Reserve | 4 | Bronze in Maluku Islands | Unlimited |
| 16 | c4_chi | Not Much To Sea | Channel Islands | Zoo | 4 | Bronze in Maluku Islands | $45,000 |
| 17 | c4_swi | From A To Ski | Swiss Alps | Zoo (two sites split by a ski slope) | 4 | Bronze in Maluku Islands | $45,000 |
| 18 | c4_sgp | Dragon, Ball, Zoo | Singapore | Zoo | 4 | Bronze in Maluku Islands | $45,000 (P2) |

_source: P1 result 2026-10-19 [refs 2, 21-25 (wikily.gg/planet-zoo-2/career and per-level pages)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_
`[Single source -- verify · class:community-wiki]` (chapter-4 name and locations also seen in a search excerpt of a second guide, not opened).

Row 18's location-to-title pairing was inferred by elimination at P1 (page unreadable twice) and **confirmed at P2**, which read the Singapore page (P2 refs 16, 30): location Singapore, title "Dragon, Ball, Zoo", Bronze in Maluku Islands, $45,000.
_source: P2 result 2026-10-19 [Wikily P2 ref 16; Whisper of the House P2 ref 30] · capture: browser_fetch (P2 ref 16) / web_fetch (P2 ref 30) · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

Order inside a chapter is the wiki's list order; after the chapter opener the levels of one chapter unlock in parallel, so it is not a forced sequence.
_source: P1 result 2026-10-19 [refs 2, 9-25] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

## Chapter-to-zone mapping
- Chapter 1 Wild At Heart: c1_grv, c1_eaf.
  _source: P1 result 2026-10-19 [ref 2] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Chapter 2 Paws on the Path: c2_nfj, c2_sew, c2_neng, c2_sco, c2_saf.
  _source: P1 result 2026-10-19 [ref 2] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`
- Chapter 3 Claws and Effect: c3_sum, c3_java, c3_fra, c3_mtf, c3_swe.
  _source: P1 result 2026-10-19 [ref 2] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

### Chapter 4 zone mapping (late-game, puzzle-tier 2)
- Chapter 4 FENtastic Opportunity: c4_mal, c4_pol, c4_tan, c4_chi, c4_swi, c4_sgp.
  _source: P1 result 2026-10-19 [ref 2] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

## Unlock edges (medal in source -> target)

```
c1_grv --Bronze--> c1_eaf
c1_grv --Silver--> c2_nfj            (also needs Accreditation Tier 2)
c2_nfj --Bronze--> c2_sew
c2_sew --Bronze--> c2_neng, c2_sco, c2_saf
(7 Bronze total) --> c3_sum          (Accreditation Tier 3)
c3_sum --Bronze--> c3_java, c3_fra, c3_mtf
c3_sum --Silver--> c3_swe            (also needs 11 Bronze total)
```

_source: P1 result 2026-10-19 [refs 9-20] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

Level objective lists end with "Travel to X via the Hub to continue", which adds a total-medal condition (2 medals for East Africa, 5 for South East Wales) [refs 9, 11].
_source: P1 result 2026-10-19 [refs 9, 11] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

Chapter 4 unlock edges (late-game, puzzle-tier 2):

```
c3_swe --Bronze--> c4_mal            (Accreditation Tier 4)
c4_mal --Bronze--> c4_pol, c4_tan, c4_chi, c4_swi, c4_sgp
```

_source: P1 result 2026-10-19 [refs 20-25] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

**Medal-count unlocks were unreliable before 14 Oct 2026:** Update 1.0.4 fixed later save slots sharing save slot 1's medal total and unlocking levels early [ref 27].
_source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes, 14 Oct 2026)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

**Tier 4 versus Maluku (late-game, puzzle-tier 2).** The Career Accreditation table says Tier 4 needs "12 Bronze, 2 Silver" and unlocks Maluku Islands; the Maluku page names only "Bronze medal in Sweden Reserve" plus "Unlocks at Accreditation Tier 4". Both conditions probably apply, but no source states it.
_source: P1 result 2026-10-19 [refs 2, 21] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Contradicted across sources -- see notes]`

## Career Accreditation (gate structure)

| Tier | Career medals needed | Unlocks |
|---|---|---|
| 1 | Starting tier | 33 species in trading |
| 2 | 2 Bronze, 1 Silver | 38 species in trading; All A-Fjord (Nordic Fjords) |
| 3 | 7 Bronze, 1 Silver | 35 species in trading; Mine Your Business (Sumatra Reserve) |
| 4 | 12 Bronze, 2 Silver | 30 species in trading; the first chapter-4 level (named in the late-game line below the table); +50 animal storage slots |
| 5 | 18 Bronze, 2 Silver | +50 animal storage slots |

_source: P1 result 2026-10-19 [ref 2 (wikily.gg/planet-zoo-2/career)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `dependencies.md` DEP-024: each Accreditation tier adds species to Animal Trading, and a species is buyable only once its tier is unlocked.

Accreditation Tier 4 unlocks the chapter-4 level Mola Money, Mola Problems (Maluku Islands) (late-game, puzzle-tier 2).
_source: P1 result 2026-10-19 [ref 2 (wikily.gg/planet-zoo-2/career)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

The page says higher tiers bring improved marketing and new research network types, without per-tier detail.
_source: P1 result 2026-10-19 [ref 2 (wikily.gg/planet-zoo-2/career)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `dependencies.md` DEP-026: Accreditation tiers hand out the Research Network pieces.

The "species in trading" figures fall from 38 to 30, so they are probably species ADDED per tier, not a running total.
_source: P1 result 2026-10-19 [ref 2 (wikily.gg/planet-zoo-2/career)] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`

## Career mode rules that change how a level plays
- Difficulty (Easy / Medium / Hard) is chosen when each Career level starts. A zoo records every difficulty it was played on; the completion screen shows the lowest; the game records the difficulty each medal was earned on, and changing difficulty "can affect whether achievements can be earned" [ref 6]. missable: yes (latest safe point: before lowering difficulty on a level where an achievement is being pursued).
  _source: P1 result 2026-10-19 [ref 6] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` SEQ-002: lowering difficulty can affect whether achievements can be earned.

- **Exception to "one rule set per map":** many level-start settings switch on as medals progress (East Africa starts with ageing/breeding, death and escapes OFF and turns them ON at Silver; Great Rift Valley turns on ageing, old-age death, death and wild territory migration at Gold) [refs 9, 10].
  _source: P1 result 2026-10-19 [refs 9, 10] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-010: breeding switches on at a medal tier in the first Career zoo, and the first-baby achievement waits for it.

> **Cross-system dependency** -- see `../dependencies.md` DEP-011: ageing and old-age death switch on at medal tiers, and the 15-year achievement waits for ageing.

- Staff hiring is often locked or limited to one staff type during Bronze (East Africa: "Later in Bronze: keepers only, then not allowed"; Nordic Fjords: vets only) [refs 10, 11].
  _source: P1 result 2026-10-19 [refs 10, 11] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`
- The Career doubles as the tutorial: the German review called it "ein etwas bemühtes 'Bitte hier klicken'-Tutorial" (a rather forced "click here" tutorial) [ref 34, translated from: German]; the French review praised tutorials built into missions and noted **three profiles** that adapt the aids and tools to the player's familiarity with the series [ref 35, translated from: French].
  _source: P1 result 2026-10-19 [refs 34, 35] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`

## Hub and site switching (all modes)
- Movement between sites is through the **Planet Hub**, a global menu reachable in every mode. It also holds shared research, animal storage and animal exchange across a player's zoos and reserves [ref 36, translated from: Russian].
  _source: P1 result 2026-10-19 [ref 36 (securitylab.ru blog review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`
- **Name clash:** Wikily's wiki page titled "Planet Hub" [ref 7] is a rotating globe listing species by wild region (land: Asia 47, Africa 44, Europe 22, North America 17, South America 14, Oceania 8, Arctic 1; ocean: Pacific 28, Indian 26, Atlantic 5, Arctic Ocean 1, Southern Ocean 1), not the in-game travel menu.
  _source: P1 result 2026-10-19 [ref 7 (wikily.gg/planet-zoo-2/planet-hub)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Update 1.0.4 fixed crashes from entering and leaving the Hub quickly, Career scenario data not clearing when switching hubs, and custom keybindings resetting when opening the Hub [ref 27].
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- "Credit Where It's Due" refers to "any non-Sandbox **hub**" [ref 3]: each mode (Career, Franchise) seems to keep its own hub with its own Accreditation (wording-based inference).
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

## Optional content registry
| Item | Parent site / mode | Unlock / access | Failure mode |
|---|---|---|---|
| Silver and Gold objectives on every Career level | each Career level | Bronze completion | always-available: earlier levels stay available and can be revisited for higher medals (P2 refs 26, 28, 30, 34) `[Single source -- verify · class:editorial-en]` (P1 recorded this as a hypothesis; P2 superseded it) |
| Weekly conservation projects (10 at capture) | zoos, offered by FEN | weekly rotation | possibly time-limited because they rotate weekly [ref 8]; whether a missed project returns is unknown `[Hypothesis -- unverified]` |
| Community Challenges | Franchise only | online, run by Frontier | time-windowed, online-only [refs 5, 32] |
| Career-completion avatar costumes | Avatar Editor | complete the Career | always-available [ref 27] |
| Field-research levels for 58 species | Wildlife Reserves | Observation Network built in a reserve AND the species released there [ref 4] | always-available |

_source: P1 result 2026-10-19 · capture: browser_fetch · confidence: medium (Hypothesis rows: low) · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_

> **Cross-system dependency** -- see `../dependencies.md` DEP-012: later research levels for 58 species need an Observation Network in a reserve plus a release of the species there.

> **Cross-system dependency** -- see `../dependencies.md` SEQ-001: weekly conservation projects rotate; whether a missed one returns is unknown.

## Not captured after P1 and P2
Silver and Gold objective lists: captured by P2 only for chapter 4 (all six levels), Sumatra and part of Great Rift Valley; not captured for East Africa, Nordic Fjords, South East Wales, New England, Scottish Highlands, South Africa, Java, Rural France, Mountain Forests, Sweden Reserve, or Great Rift Valley Gold `[location inventory incomplete]`. Medal rewards beyond those listed as given during Bronze. (Resolved at P2: finished levels can be revisited to earn higher medals; the chapter-4 level whose page was unreadable at P1 was read.)
_source: P2 result 2026-10-19 [Wikily level pages P2 refs 2-19; Whisper of the House P2 refs 26-30; absence statement for the lists not captured] · capture: browser_fetch (Wikily) / web_fetch (Whisper) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[location inventory incomplete]`

## P2 additions (P2 result 2026-10-19; "P2 ref N" numbers are in `../research_briefs/source_register.md`)
P2 corroborates the P1 unlock edges above with independent guides (Whisper of the House, planetzoo-2.wiki, Prima); every edge agrees.
_source: P2 result 2026-10-19 [planetzoo-2.wiki P2 ref 25; Whisper of the House P2 refs 26-30; Prima P2 refs 31-32] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
Because the game is days old and Update 1.0.4 changed medal-unlock behaviour, confidence stays medium and no fact reaches the 5-source `[Confirmed]` floor.

### Branching shape
Strictly linear through chapter 1 and Nordic Fjords / South East Wales; a three-way branch after South East Wales (New England, Scottish Highlands, South Africa); a three-way branch after Sumatra (Java, Rural France, Mountain Forests) that rejoins at Sumatra Silver. Only Great Rift Valley and Sumatra need a return trip for a Silver to progress. (P2 refs 25, 26, 27, 29, 30; below floor.) vector: nav.
_source: P2 result 2026-10-19 [planetzoo-2.wiki P2 ref 25; Whisper of the House P2 refs 26, 27, 29, 30] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

Earlier levels stay available: "free return to earlier levels to earn higher medals" (P2 refs 26, 28, 30, 34).
_source: P2 result 2026-10-19 [Whisper of the House P2 refs 26, 28, 30; Power Up Gaming P2 ref 34] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

Chapter 4 branching (late-game, puzzle-tier 2): a five-way branch after Maluku Islands.
_source: P2 result 2026-10-19 [planetzoo-2.wiki P2 ref 25; Whisper of the House P2 ref 30] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:editorial-en]`

### Medal-arithmetic hypothesis
The counts fit "every level's Bronze": chapters 1-2 hold exactly 7 levels (7 Bronze = the Tier 3 gate to Sumatra); chapters 1-3 minus Sweden hold 11 (the Sweden gate); chapters 1-3 hold 12 (Tier 4 = 12 Bronze); all 18 levels = 18 Bronze (Tier 5). The 1-2 Silver gates match Great Rift Valley Silver (Tier 2) and Sumatra Silver (Sweden, Tier 4). model analysis (P2 result) 2026-10-19
_source: P2 result 2026-10-19 [model analysis in the P2 result over Wikily accreditation P2 ref 20 and career pages P2 refs 1-19] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`

Cross-check by this ingestion (model analysis, 2026-10-19): the Career species-in-trading figures 33 + 38 + 35 + 30 sum to 136, the full roster, which supports the P1 reading that those figures are species ADDED per tier; also still `[Hypothesis -- unverified]` for Career (the P2 Franchise table, 32 + 33 + 31 + 30 + 10 = 136, is the same pattern).
_source: model analysis, ingestion 2026-10-19 [Wikily accreditation P2 ref 20; P1 ref 2] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`

### Rules with documented exceptions
- "Bronze here opens the next level" has exceptions: Nordic Fjords needs Silver at Great Rift Valley and Tier 2; South East Wales needs 5 medals; Sumatra needs 7 Bronze; Sweden needs Sumatra Silver and 11 Bronze. (P2 refs 1, 4, 9, 13, 26, 29.)
  _source: P2 result 2026-10-19 [Wikily P2 refs 1, 4, 9, 13; Whisper of the House P2 refs 26, 29] · capture: browser_fetch (Wikily) / web_fetch (Whisper) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`
- Chapter 4 exception (late-game, puzzle-tier 2): Maluku needs Sweden Bronze and Tier 4. (P2 refs 14, 30.)
  _source: P2 result 2026-10-19 [Wikily P2 ref 14; Whisper of the House P2 ref 30] · capture: browser_fetch (Wikily) / web_fetch (Whisper) · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`
- "Inspections are on in Career" is false at several starts: Great Rift Valley, Scottish Highlands, Sumatra and Sweden have inspections Off; East Africa, New England, South Africa and Java start Off and turn on at Silver (Nordic Fjords at Gold); South East Wales is On from the start. (P2 refs 2-13.)
  _source: P2 result 2026-10-19 [Wikily level pages P2 refs 2-13] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`
- Chapter 4 inspections (late-game, puzzle-tier 2): Poland and Tanzania have inspections Off. (P2 refs 17, 19.)
  _source: P2 result 2026-10-19 [Wikily level pages P2 refs 17, 19] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`
- Wikily's level pages print only the Bronze tab as text; the page objective totals sum to 385 (14+38+26+35+19+15+29+20+43+26+24+11+13+18+16+9+13+16); Silver and Gold lists come from Whisper of the House where printed.
  _source: P2 result 2026-10-19 [Wikily level pages P2 refs 2-19; Whisper of the House P2 refs 26-30] · capture: browser_fetch (Wikily) / web_fetch (Whisper) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

### Unlock conflicts
- **South East Wales (C1):** the level page says "Bronze medal in Nordic Fjords"; Nordic Fjords' own objective list says "Travel to South East Wales via the Hub to continue - Have at least 5 Career medals"; guides say Nordic Bronze alone can leave the Hub on "Progress Blocked" until 5 Career medals. Medals counted so far (Bronze + Silver Great Rift Valley, Bronze East Africa, Bronze Nordic) are only 4 if each tier counts as a medal, so the counting rule is unresolved. This ingestion (P1 + P2) agrees with the 2-medal and 5-medal conditions P1 recorded.
  _source: P2 result 2026-10-19 [Wikily P2 refs 4, 5; Whisper of the House P2 refs 26, 28] · capture: browser_fetch (Wikily) / web_fetch (Whisper) · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Contradicted across sources -- see notes]`
- **East Africa (C2):** Great Rift Valley's objective list says "Travel to East Africa via the Hub ... Have at least 2 Career medals", but East Africa's unlock rule is Bronze in Great Rift Valley (1 medal); the line is not on the East Africa page in English, Japanese or Brazilian Portuguese.
  _source: P2 result 2026-10-19 [Wikily P2 refs 2, 3, 44, 45] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Contradicted across sources -- see notes]`
- **Maluku vs Tier 4 (late-game, puzzle-tier 2):** unchanged from P1 (both conditions probably apply).
  _source: P2 result 2026-10-19 [Wikily P2 refs 14, 20] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Contradicted across sources -- see notes]`

### Franchise and Sandbox gate structure
Moved to `../mechanics.md` ("Franchise accreditation gates (P2)").

### Support topology (Planet Hub, saves)
- Site switching goes through the Planet Hub: in Career "open Planet Hub and travel to East Africa"; the Hub shows locked destinations and their medal requirement ("Progress Blocked" for South East Wales until 5 medals) (P2 refs 25, 26, 27, 28, 35). (Five English sources, derivative families, below the independence floor.)
  _source: P2 result 2026-10-19 [planetzoo-2.wiki P2 ref 25; Whisper of the House P2 refs 26, 27, 28; GamerBlurb P2 ref 35] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Shared across sites via the Hub: Research and Conservation Projects; in Franchise all research and animal storage are shared, so animals can move between zoos (P2 refs 31, 35).
  _source: P2 result 2026-10-19 [Prima P2 ref 31; GamerBlurb P2 ref 35] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-008: in Franchise, research is shared across zoos through the Planet Hub.

- Career medal totals and Accreditation are per save slot: Update 1.0.4 fixed later save slots sharing save slot 1's medal total and unlocking levels early (P2 refs 36, 37). A Career save slot is the unit that holds medals.
  _source: P2 result 2026-10-19 [Insider Gaming P2 ref 36; games.gg P2 ref 37] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Scenario data is per site: 1.0.4 fixed "scenario data was not being cleared when entering and exiting a different hub" (the patch note's word "hub"; it may mean a different site) (P2 ref 36). Evidence of reset-on-switch behaviour; mechanism not described.
  _source: P2 result 2026-10-19 [Insider Gaming P2 ref 36] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Animals move between sites only as Release Groups (zoo to reserve); "Animals committed to a Release Group cannot return to the zoo". Zoo-to-zoo transfers go through Animal Storage in Franchise (P2 refs 27, 31).
  _source: P2 result 2026-10-19 [Whisper of the House P2 ref 27; Prima P2 ref 31] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

> **Cross-system dependency** -- see `../dependencies.md` PON-001: animals committed to a release cannot return to the zoo.

> **Cross-system dependency** -- see `../dependencies.md` DEP-016: a reserve takes a Release Group only while that species' release requirements are met.

- Blueprints carrying across Career saves is a search-summary claim only.
  _source: P2 result 2026-10-19 [search-summary excerpt; no page opened] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`
- **What the Hub resets on a site switch is not documented anywhere readable.**
  _source: P2 result 2026-10-19 [absence statement over P2 refs 25-28, 35, 36; no source states it] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]` `[location inventory incomplete]`
- **Hub access from any site: not documented** (`Hub access: unknown`). Indirect evidence: patch notes mention custom keybindings resetting "when opening the Hub, Animal Trading, or Animal Storage", so the Hub opens by a rebindable key or menu entry (P2 ref 36). The pause-menu path and key name were not found. Official Planet Zoo 2 player guides were not found readable (the help-centre path returned 404; the one at planetzoogame.com/help-centre is the first game's).
  _source: P2 result 2026-10-19 [Insider Gaming P2 ref 36; absence statement for the pause-menu path and key name] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Fast-travel equivalents: None within a site (driving the Research Vehicle in a reserve is real travel); between sites the Hub is a load transition, not a teleport.
  _source: P2 result 2026-10-19 [no per-claim reference in the P2 result; the support-topology sources P2 refs 25-28, 31, 35, 36 apply] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Saves, Career: multiple Career save slots exist; "save and quit before completing" a scenario could lose the next-scenario unlock (fixed in 1.0.4; assume the fix applies going forward only, which is not stated). A reload of an existing save re-opens a scenario; a full restart loses progress; the menu path is not stated. Medals are cumulative per level. No fail-state text was found (no bankruptcy rule, no objective-timer failure); seasonal conditions such as "no protesters for N seasons" reset their counter rather than failing the level. What a failed scenario loses: `unknown`. (P2 refs 26, 30, 36, 37, 38.)
  _source: P2 result 2026-10-19 [Whisper of the House P2 refs 26, 30; Insider Gaming P2 ref 36; games.gg P2 ref 37; dtgre.com P2 ref 38] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Saves, Franchise / Sandbox: Franchise is online; an "offline" state blocked many players at launch; save-slot behaviour not found; planned maintenance 15 Oct. Sandbox: Career and Franchise zoos can be exported as Sandbox maps; Sandbox save behaviour not found. (P2 refs 35, 36, 40.)
  _source: P2 result 2026-10-19 [GamerBlurb P2 ref 35; Insider Gaming P2 ref 36; Reddit launch-day thread P2 ref 40] · capture: web_fetch (P2 refs 35, 36) / browser_fetch (P2 ref 40) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Autosave / manual save / quicksave: one low-reliability source (planet-zoo2.wiki, P2 ref 46, which contradicts others on Franchise) claims an autosave slot, a manual slot, saves every 5 minutes, quicksave F5 and a ten-save cap; treat as unverified. Save-point names and menu paths: `unknown`.
  _source: P2 result 2026-10-19 [planet-zoo2.wiki P2 ref 46] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`
- A launch-day Reddit post confirms a saving progress bar appears when exiting to the main menu (P2 ref 40).
  _source: P2 result 2026-10-19 [Reddit launch-day thread P2 ref 40] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:forum]`

### Locks-and-keys (Career)
| # | Lock | Key | Key source | Visible before key? | Notes |
|---|---|---|---|---|---|
| 1 | East Africa | Bronze in Great Rift Valley Reserve | Great Rift Valley Reserve | page shows the condition; Hub display not described | see C2 |
| 2 | Nordic Fjords | Silver in Great Rift Valley Reserve + Accreditation Tier 2 | Great Rift Valley (the Silver needs the East Africa-prepared giraffe group) | Hub shows the requirement | |
| 3 | South East Wales | Bronze in Nordic Fjords; plus "at least 5 Career medals" | Nordic Fjords; medals from earlier levels | yes ("Progress Blocked") | see C1 `[Contradicted across sources -- see notes]` |
| 4 | New England / Scottish Highlands / South Africa | Bronze in South East Wales | South East Wales | yes | |
| 5 | Sumatra Reserve | 7 Bronze Career medals; Tier 3 (7 Bronze + 1 Silver) | any 7 Bronzes (chapters 1-2, hypothesis) | yes (Hub) | |
| 6 | Java / Rural France / Mountain Forests | Bronze in Sumatra Reserve | Sumatra Reserve | yes | |
| 7 | Sweden Reserve | Silver in Sumatra Reserve AND 11 Bronze | Sumatra Silver (6 Camera Traps, 8 Release Groups, Tapir/Siamang/Sun Bear releases) | yes | spoiler: story |
| 11 | Great Rift Valley Gold | key: unknown (Gold list not captured) | key: unknown | key: unknown | gap |
| 12 | Wildlife Reserve release group | the species' release requirements met (ecosystems Established, roles) | reserve ecosystem work | blocked groups show their missing requirement | |
| 13 | Research-level objectives (e.g. Hawksbill Turtle level 4) | research levels | Hub research | n/a | pointer only; see `../items/upgrades.md` |

_source: P2 result 2026-10-19 [P2 refs 3-20, 25-30, 36] · capture: browser_fetch / web_fetch · confidence: medium (rows 3 and 5-7: medium or low as flagged) · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`. Keys are taken only from the matching source rows; none derived from lock names.

Locks-and-keys, late-game rows (puzzle-tier 2):

| # | Lock | Key | Key source | Visible before key? | Notes |
|---|---|---|---|---|---|
| 8 | Maluku Islands | Bronze in Sweden Reserve AND Tier 4 (12 Bronze + 2 Silver) | Sweden Bronze; 2nd Silver (Sumatra, hypothesis) | yes | spoiler: late-game |
| 9 | Channel Islands / Singapore / Poland / Swiss Alps / Tanzania | Bronze in Maluku Islands | Maluku Islands | yes | spoiler: late-game |
| 10 | Career Accreditation Tier 5 | 18 Bronze + 2 Silver | all 18 levels (hypothesis) | yes (Accreditation tab) | spoiler: late-game |

_source: P2 result 2026-10-19 [P2 refs 14-20, 25-30, 36] · capture: browser_fetch / web_fetch · confidence: medium (rows 8-10: medium or low as flagged) · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`

## Achievement-bound claims
- Bronze in all 18 Career scenarios completes "Good Start…".
  _source: P1 result 2026-10-19 [refs 2, 3] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: good_start · achievement-hidden: yes · trigger_type: collection_
- Gold in all Career scenarios completes "Excellent Finish" (Gold lists not captured for most levels).
  _source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: excellent_finish · achievement-hidden: yes · trigger_type: collection_
- Reaching Career Accreditation Tier 5 (18 Bronze, 2 Silver) is the Career route to "Credit Where It's Due" (highest Accreditation in any non-Sandbox hub).
  _source: P1 result 2026-10-19 [refs 2, 3] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression · achievement: credit_where_its_due · achievement-hidden: yes · trigger_type: progression_
Aggregated in `../achievements.md`.

> **Cross-system dependency** -- see `../dependencies.md` DEP-017.

> **Cross-system dependency** -- see `../dependencies.md` DEP-018.

> **Cross-system dependency** -- see `../dependencies.md` DEP-019.
