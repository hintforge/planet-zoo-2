# Planet Zoo 2 -- Mechanics Reference

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19

Universal core file. Every claim carries its own metadata line directly beneath it. Default confidence is medium: the game launched 2026-10-13, Update 1.0.4 (14 Oct) changed many values, and most facts rest on one wiki family. No fact has reached the 5-independent-source "confirmed" floor, so no `[Confirmed: ...]` line is used. Where a fact is carried over from the first Planet Zoo (2019) it is marked as such; none are used here.

## Game modes
Career, Sandbox, Franchise (official Game Modes page, fetched 2026-10-19). Career: new Conservation Coordinator at FEN across Wildlife Reserves, zoos and scenarios; Bronze/Silver/Gold objectives (see `sections/career_progression.md`). Sandbox: free building with a selectable simulation/challenge level. Franchise: a network of interconnected zoos and Wildlife Reserves, animal trading and community conservation.
_source: Stage 0 + P1 result 2026-10-19 [official game-modes page] · capture: browser_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ (official page plus wiki and reviews agree; wording only)

### Career mode rules
See `sections/career_progression.md` (difficulty per level, settings that switch on at medals, staff-hiring limits).

### Sandbox
- Starts on Medium difficulty; has presets (named on Wikily: "Default" and "Creative") with unlimited Conservation Credits [refs 5, 8]. The full preset settings list was not read.
  _source: P1 result 2026-10-19 [ref 5 (wikily.gg/planet-zoo-2/game-modes); ref 8 (wikily.gg/planet-zoo-2/conservation-projects)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Highly configurable, including build costs and how strict ratings are ("Bewertungsstrenge") [ref 34, translated from: German].
  _source: P1 result 2026-10-19 [ref 34 (gameswelt.de review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`
- Excluded from the achievements "Credit Where It's Due" and "Lessons Learned" (both say non-Sandbox) [refs 3, 29].
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements); ref 29 (destructoid.com achievements list)] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Career and Franchise zoos can be exported as Sandbox maps; Update 1.0.4 fixed terrestrial animals being removed on export [ref 27].
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- Count of distinct Sandbox maps: not found `[location inventory incomplete]`.
  _source: P1 result 2026-10-19 [absence statement; no read source gives the count] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Franchise
| Setting | Franchise zoo | Franchise Wildlife Reserve |
|---|---|---|
| Starting cash | $45,000 | Unlimited |
| Starting Conservation Credits | 300 | 0 |
| CC per reputation star | 0 stars 0 CC; 1 star 30; 2 stars 60; 3 stars 90; 4 stars 120; 5 stars 150 (period not stated) | none |
| Guest cap | 4,000 on consoles; no cap on PC | 2,000 |
| Inspections | On, every 8 seasons | Off |
| Habitat barriers | allowed | cannot be built |

_source: P1 result 2026-10-19 [ref 5 (wikily.gg/planet-zoo-2/game-modes)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- **Platform exception:** the PC Franchise zoo has no guest cap; consoles cap at 4,000 [ref 5].
  _source: P1 result 2026-10-19 [ref 5 (wikily.gg/planet-zoo-2/game-modes)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Franchise is online: a network of zoos and reserves with Community Challenges; trading animals with other players; credits are **not shared** between Franchise and offline modes [refs 5, 8, 35].
  _source: P1 result 2026-10-19 [ref 5 (wikily.gg/planet-zoo-2/game-modes); ref 8 (wikily.gg/planet-zoo-2/conservation-projects); ref 35 (xboxygen.com review)] · capture: browser_fetch (refs 5, 8) / web_fetch (ref 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`
- Ways to earn CC in Franchise: releasing animals (Release Groups into a reserve pay well; any animal can be "quick released" but cannot then be followed); greeting VIP visitors who represent friends' or other players' avatars; Community Challenge rewards; selling animals for CC on the market (best value for endangered animals and rare albino or leucistic variants) [refs 8, 32].
  _source: P1 result 2026-10-19 [ref 8 (wikily.gg/planet-zoo-2/conservation-projects); ref 32 (primagames.com, 13 Oct 2026)] · capture: browser_fetch (ref 8) / web_fetch (ref 32) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `dependencies.md` PON-001.

- Higher-interest, prime-age, better-gene animals earn more CC on release [ref 8].
  _source: P1 result 2026-10-19 [ref 8 (wikily.gg/planet-zoo-2/conservation-projects)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Update 1.0.4: greater access to initial trading volumes; fix for listing juvenile Shoals; fix for release groups showing the wrong CC reward; PS5 fix for player info missing from Animal Trading [ref 27, web_fetch].
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- Insider Gaming notes that Franchise lets research be split across several zoos (relevant to the achievement "Professor") [ref 28].
  _source: P1 result 2026-10-19 [ref 28 (insider-gaming.com achievement list)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

> **Cross-system dependency** -- see `dependencies.md` DEP-008: in Franchise, research is shared across zoos through the Planet Hub.

## Planet Hub
New global menu available in all modes: progress, performance data, switching between sites, research and conservation decisions (official page). Shared research, storage and animal exchange across zoos and reserves; see `sections/career_progression.md` "Hub and site switching" for the Hub name clash and patch fixes.
_source: Stage 0 + P1 result 2026-10-19 [official game-modes page] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

> **Cross-system dependency** -- see `dependencies.md` DEP-015.

## Animal welfare and habitats
Species needs, habitat building, aquariums (freshwater, brackish, saltwater) and aviaries. Full coverage in `animals/welfare_breeding_release.md` and `animals/aquariums_and_aviaries.md`; species roster in `animals/roster.md`.

## Research and conservation
Research trees (217 topics), field research in Wildlife Reserves and conservation projects: `items/upgrades.md`. Conservation Credits (CC) are spent on higher-tier animals and pay project requirements (they pay for an animal; they do not unlock its Accreditation tier -- see `animals/accreditation.md`); earned from releases, quick releases and project rewards; in Franchise also from trading and Community Challenges [refs 8, 32]. Starting CC: Franchise 300; Sandbox Default and Creative presets unlimited [ref 8].
_source: P1 result 2026-10-19 [ref 8 (wikily.gg/planet-zoo-2/conservation-projects); ref 32 (primagames.com, 13 Oct 2026)] · capture: browser_fetch (ref 8) / web_fetch (ref 32) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

## Wildlife Reserves
- Rules: unlimited cash, 0 starting CC, 2,000-guest cap, inspections off, habitat barriers cannot be built [ref 5].
  _source: P1 result 2026-10-19 [ref 5 (wikily.gg/planet-zoo-2/game-modes)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- The player restores land and builds ecosystems; terrain composition, vegetation, water and altitude matter; pollution and invasive plants work against the player; each reserve has biodiversity and research indicators; monitoring tools are observation platforms, camera traps and acoustic devices [ref 35, translated from: French]. Invasive plants are removed with the bulldozer [ref 31].
  _source: P1 result 2026-10-19 [ref 35 (xboxygen.com review); ref 31 (finalboss.io chapter 1 walkthrough)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`
- Ratings used by Career objectives: Biodiversity Rating, Ecosystem Rating, ecosystems "Established". 32 ecosystems and 104 release groups exist (Wikily navigation counts) [ref 1]. Named ecosystems seen: Montane Forest, Moorland, Lowland Rainforest, Peatland, River, Fen Wetland [refs 14, 16, 23].
  _source: P1 result 2026-10-19 [ref 1 (wikily.gg/planet-zoo-2); refs 14, 16, 23 (wikily.gg/planet-zoo-2/career per-level pages)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Reserves are explored on foot or in a drivable Research Vehicle (achievement "Where Am I?": drive 10 km) [refs 3, 35]. vector: nav (local to one reserve).
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements); ref 35 (xboxygen.com review)] · capture: browser_fetch (ref 3) / web_fetch (ref 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`
- Photographing released animals earns Conservation Credits [ref 31].
  _source: P1 result 2026-10-19 [ref 31 (finalboss.io chapter 1 walkthrough)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- Which species each reserve can release: `animals/reserve_releases.md`.
- Update 1.0.4: fixed juvenile birds stuck in nests after a reserve group migrated, animals teleporting, and zoo-only blueprints appearing in the reserve object browser [ref 27].
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

> **Cross-system dependency** -- see `dependencies.md` DEP-006: birds and egg-laying reptiles need a nest per breeding pair.

- **Zoo versus reserve are different site types with different rules.** Reserves are rated on biodiversity and ecosystems, not zoo reputation [refs 20, 23].
  _source: P1 result 2026-10-19 [ref 20 (wikily.gg/planet-zoo-2/career/sweden-reserve); ref 23 (wikily.gg/planet-zoo-2/career/poland-reserve)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Economy and guests
- Income: tickets, shops, souvenirs, donations; marketing campaigns; loans [refs 34, 36]. Marketing campaigns start from the finance menu [ref 34]; tiers go up to Gold Tier (Level 3) (achievement "Show-Pony") [ref 3]. Settings reach down to ATM fees [ref 34].
  _source: P1 result 2026-10-19 [ref 34 (gameswelt.de review); ref 36 (securitylab.ru blog review); ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: web_fetch (refs 34, 36) / browser_fetch (ref 3) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 2 languages -- below 5-source floor]`
- Loans exist from the start of some levels ("Nest Eggs", $10,000, in a Chapter 2 zoo; see `sections/chapter_2_paws_on_the_path.md`); Update 1.0.4 reduced interest on low-level loans [refs 13, 27].
  _source: P1 result 2026-10-19 [ref 13 (wikily.gg/planet-zoo-2/career/new-england); ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: browser_fetch (ref 13) / web_fetch (ref 27) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `dependencies.md` SEQ-004: repaying the starting loan before operating cash is built risks stalling.

- Ticket prices are set separately for adults and children (a Chapter 2 zoo asks for $10 / $8; see `sections/chapter_2_paws_on_the_path.md`) [ref 12].
  _source: P1 result 2026-10-19 [ref 12 (wikily.gg/planet-zoo-2/career/south-east-wales)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Donation-led models: Donation Bins near viewing, Nature's Keepers (Adoption) Shop, seasonal donation targets ($5,000 in a Chapter 2 zoo; $10,000 in a Chapter 3 "Free" zoo; see the chapter files) [refs 13, 18]. Thriving animals raise donations [refs 26, 36].
  _source: P1 result 2026-10-19 [ref 13 (wikily.gg/planet-zoo-2/career/new-england); ref 18 (wikily.gg/planet-zoo-2/career/rural-france); ref 26 (thegameswiki.com animals-and-welfare); ref 36 (securitylab.ru blog review)] · capture: browser_fetch (refs 13, 18, 26) / web_fetch (ref 36) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Difficulty effects (Easy / Medium / Hard) [ref 6]: guest learning x1.75 / x1 / x0.8; happiness loss slower / standard / faster; **guests request refunds only on Hard**; spending more / standard / less; average happiness for a 5-star Guest Happiness Rating 80% / 85% / 90%; staff tire slower / standard / faster; staff move faster on Easy; animals get bored of enrichment **only on Hard**; animal stress and death-when-critical scale the same way.
  _source: P1 result 2026-10-19 [ref 6 (wikily.gg/planet-zoo-2/difficulty)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Failure states seen in sources: negative cash and loans (a Chapter 2 zoo; see `sections/chapter_2_paws_on_the_path.md`) [ref 13]; inspections with star reports [ref 22]; escapes (animals clipping through fences is a reported bug, not only a management failure) [refs 27, 35]; refunds on Hard [ref 6]. A protester-based failure state is recorded in the late-game line below.
  _source: P1 result 2026-10-19 [ref 13 (wikily.gg/planet-zoo-2/career/new-england); ref 22 (wikily.gg/planet-zoo-2/career/channel-islands); ref 27 (insider-gaming.com, Update 1.0.4 notes); ref 35 (xboxygen.com review); ref 6 (wikily.gg/planet-zoo-2/difficulty)] · capture: browser_fetch (refs 13, 22, 6) / web_fetch (refs 27, 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Failure state from a chapter-4 level (late-game, puzzle-tier 2): protesters (Channel Islands "no protesters for a season") [ref 22].
  _source: P1 result 2026-10-19 [ref 22 (wikily.gg/planet-zoo-2/career/channel-islands)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:community-wiki]`
- Staff (role split with `items/support_items.md`, zipper 2026-10-19: that file owns the staff and facility lists; this line keeps the operating rules): 6 types per Wikily [ref 1]; read sources name Keeper, Vet, Mechanic, Caretaker, Educator [refs 10, 11, 12, 18], and the French review lists vendors [ref 35]. Staff train to stars, tire, have pay and conditions; Staff Rooms carry perks (e.g. Learning Resources) [refs 12, 15, 35].
  _source: P1 result 2026-10-19 [ref 1 (wikily.gg/planet-zoo-2); refs 10, 11, 12, 15, 18 (wikily.gg career per-level pages); ref 35 (xboxygen.com review)] · capture: browser_fetch (refs 1, 10, 11, 12, 15, 18) / web_fetch (ref 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`
- Heat maps show shortages of food, rest or education; guest thoughts explain complaints [ref 36, translated from: Russian]. Economy described as largely unchanged from the first game [ref 36].
  _source: P1 result 2026-10-19 [ref 36 (securitylab.ru blog review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`

## Frontier Workshop
- Workshop opens from the build menu and is cross-platform [ref 36]; the Xbox review confirms creations download and share across platforms [ref 35].
  _source: P1 result 2026-10-19 [ref 36 (securitylab.ru blog review); ref 35 (xboxygen.com review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 2 languages -- below 5-source floor]`
- Update 1.0.4: fixed creator profiles not viewable from the object browser in Career; fixed upload thumbnails; fixed blueprints with locked enrichment items appearing before their research was done [ref 27]. So blueprint items are gated by the player's research.
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- No co-op; single-player with online Franchise and Workshop [ref 36].
  _source: P1 result 2026-10-19 [ref 36 (securitylab.ru blog review)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-non-en]`
- Franchise trading mechanics: a trading-specific guide was not found.
  _source: P1 result 2026-10-19 [absence statement; no read source covers it] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Franchise accreditation gates (P2)
Franchise and Sandbox have no authored scenarios; gating is the Accreditation ladder and Conservation Credits. Career and Franchise Accreditation are separate tracks: Career medals do not raise Franchise tier (P2 refs 20, 25, 26, 35; four sources, below the 5-source floor). "P2 ref N" numbers are in `research_briefs/source_register.md`.
_source: P2 result 2026-10-19 [Wikily P2 ref 20; planetzoo-2.wiki P2 ref 25; Whisper of the House P2 ref 26; GamerBlurb P2 ref 35] · capture: browser_fetch (P2 ref 20) / web_fetch (P2 refs 25, 26, 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

| # | Gate | Detail |
|---|---|---|
| F1 | Online requirement | Franchise is online-only; an "offline"/"can't connect to the server" state blocked many players at launch (P2 refs 21, 35, 40) `[Single source -- verify · class:forum]` |
| F2 | Start | First zoo starts at Tier 1 (32 species in trading in Franchise; 33 in Career), $45,000, 300 Conservation Credits; reserves start with unlimited cash and 0 credits (P2 refs 20, 21, 32) |
| F3 | Tier 2 | 1 zoo at 3 Reputation stars: +33 species, Camera Trap, +2 Bronze marketing slots (P2 refs 32, 33) |
| F4 | Second zoo | Opening a second zoo costs Conservation Credits; the price is unknown (P2 ref 33) |
| F5 | Tier 3 | 2 zoos at 3 Reputation stars AND 1 Wildlife Reserve at 3 Biodiversity stars: +31 species, Acoustic Monitor, +1 Bronze and +1 Silver marketing slot |
| F8 | Species total | 32+33+31+30+10 = 136, matching the roster count (P2 refs 20, 32, 33) |
| F9 | Reserve release | A reserve takes a Release Group once it meets that species' release requirements (P2 ref 21) |
| F10 | Launch shortage | Tier-1 animals were bought up at launch so players waited for Tier 2 (player report; patch 1.0.4 "greater access to initial animal trading volumes") (P2 refs 36, 40) |

_source: P2 result 2026-10-19 [P2 refs 20, 21, 31-33, 35, 36, 40 as shown in each row] · capture: browser_fetch (ref 21) / web_fetch (others) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]` (F3-F8 corroborated by two guides: P2 refs 32, 33).

> **Cross-system dependency** -- see `dependencies.md` DEP-016: a reserve takes a Release Group only while that species' release requirements are met.

> **Cross-system dependency** -- see `dependencies.md` DEP-024: each Accreditation tier adds species to Animal Trading, and a species is buyable only once its tier is unlocked.

> **Cross-system dependency** -- see `dependencies.md` DEP-026: Accreditation tiers hand out the Research Network pieces.

Late-game gates (F6, F7; puzzle-tier 2):

| # | Gate | Detail |
|---|---|---|
| F6 | Tier 4 | 2 zoos at 3 Reputation AND 2 reserves at 3 Biodiversity: +30 species, +1 Bronze, +1 Silver marketing, +50 Animal Storage (spoiler late-game) |
| F7 | Tier 5 | 2 zoos at 3 Reputation AND 3 reserves at 3 Biodiversity: +10 species including lions and elephants, +1 Silver, +1 Gold marketing (spoiler late-game) |

_source: P2 result 2026-10-19 [Primagames P2 ref 32; PowerUp Gaming (powerupgaming.co.uk) P2 ref 33; Wikily P2 ref 20] · capture: web_fetch (P2 refs 32, 33) / browser_fetch (P2 ref 20) · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`
- **Species counts per tier differ between modes:** Career lists 33 / 38 / 35 / 30 species per tier (see `sections/career_progression.md`), Franchise 32 / 33 / 31 / 30 / 10; two different totals are in circulation, both summing to 136.
  _source: P2 result 2026-10-19 [Wikily P2 ref 20; Prima P2 refs 32, 33; P1 ref 2] · capture: browser_fetch (P2 ref 20, P1 ref 2) / web_fetch (P2 refs 32, 33) · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Contradicted across sources -- see notes]`
- Expected number of Franchise sites: unknown. The only fixed reserve set is the six named reserves (P2 ref 39), and Prima says the best route is "the three European reserves" (P2 ref 32); whether Franchise can create exactly these six was not confirmed `[location inventory incomplete]`.
  _source: P2 result 2026-10-19 [Insider Gaming P2 ref 39; Prima P2 ref 32] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`
- Sandbox has no gates: no money restrictions, unlimited adoptable animals, settings (breeding/ageing off) editable; creations can be saved as Blueprints for use in other modes "assuming you have the required funds" (P2 ref 31). "Credit Where It's Due" cannot be earned in Sandbox (P2 refs 20, 22).
  _source: P2 result 2026-10-19 [Prima P2 ref 31; Wikily P2 refs 20, 22] · capture: web_fetch (P2 ref 31) / browser_fetch (P2 refs 20, 22) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

## Source cautions (P2)
- P2 found two different sites that look like "the Planet Zoo 2 wiki": planetzoo-2.wiki (a fan wiki consistent with other sources, P2 ref 25) and planet-zoo2.wiki (P2 ref 46), which calls Franchise "multiplayer co-op", cites an "official Player Guides" page nobody else found, and gives save-slot figures. Treat the second as low reliability; its numbers are hypotheses only.
  _source: P2 result 2026-10-19 [planetzoo-2.wiki P2 ref 25; planet-zoo2.wiki P2 ref 46] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Contradicted across sources -- see notes]`
- First-game (2019) pages surface in searches for "Planet Zoo 2" (Frontier CMS update notes, the first game's help centre, Steam app 703080 threads); none are used here. "Challenge Mode" existed in the first game; Planet Zoo 2 modes found are Career, Sandbox and Franchise only (a Prima page title asks the question; not read).
  _source: P2 result 2026-10-19 [search results seen during P2; pages read and discarded as wrong game (see `research_briefs/source_register.md`)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
- Patch state: P1 found Update 1.0.4 (14 Oct 2026) as the last patch with notes and a Wikily news item naming Update 1.0.5 (16 Oct 2026) whose notes were not found; P2 found no notes later than 1.0.4 (one search summary said a further update was planned for 16 Oct). Treat values as 1.0.4-era.
  _source: P1 result 2026-10-19 [ref 27 (insider-gaming.com, Update 1.0.4 notes); Wikily news item] and P2 result 2026-10-19 [P2 ref 36; games.gg P2 ref 37] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- Deluxe Edition: an edition, not DLC; no DLC found shipped by either phase; Insider Gaming speculates that new reserves "could be featured in future DLC packs" (speculation, not an announcement).
  _source: P2 result 2026-10-19 [Insider Gaming P2 ref 39; absence statement for shipped DLC] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Achievement-bound claims
Aggregated in `achievements.md`.
- A photo scoring 10,000 in any Wildlife Reserve.
  _source: P1 result 2026-10-19 [refs 3, 29, 35] · capture: browser_fetch (ref 3) / web_fetch (refs 29, 35) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: snap · achievement-hidden: yes · trigger_type: mastery_
- Plant 1,000 trees in Wildlife Reserves.
  _source: P1 result 2026-10-19 [refs 3, 29] · capture: browser_fetch (ref 3) / web_fetch (ref 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: green_thumb · achievement-hidden: yes · trigger_type: threshold_
- Drive 10 km in the Research Vehicle (reserve).
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: where_am_i · achievement-hidden: yes · trigger_type: threshold_
- Release 20 release groups (reserve release).
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: job_well_done · achievement-hidden: yes · trigger_type: threshold_
- Establish 10 ecosystems.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: naturalist · achievement-hidden: yes · trigger_type: threshold_
- 5-star rating in a Wildlife Reserve.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: paradise · achievement-hidden: yes · trigger_type: mastery_
- Earn 10,000 Conservation Credits.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: conservation_aire · achievement-hidden: yes · trigger_type: threshold_
- Start a Gold Tier (Level 3) marketing campaign for an animal.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: show_pony · achievement-hidden: yes · trigger_type: progression_
- 5-star reputation in a zoo.
  _source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: goodwin_park · achievement-hidden: yes · trigger_type: mastery_
