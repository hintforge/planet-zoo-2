# Planet Zoo 2 -- Aquariums and aviaries

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** P1 2026-10-19

Every claim carries its own `_source:` line.

## Aquariums (freshwater, brackish, saltwater)
- Water types: freshwater, salt and brackish [refs 35, 36]. Built around an **Aquarium Staff Gate** connected to the path, a **Water Filter** and a **Power Generator**; temperature is set per aquarium [ref 11]. Keepers enter the tank (through airlocks, in special gear) to feed and maintain; guest tunnels and underwater decor exist [refs 35, 36].
  _source: P1 result 2026-10-19 [ref 35 (xboxygen.com review); ref 36 (securitylab.ru blog review); ref 11 (wikily.gg/planet-zoo-2/career/nordic-fjords)] · capture: web_fetch (refs 35, 36) / browser_fetch (ref 11) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 3 languages -- below 5-source floor]`
- Filtration is a network with a **Filtration Rate** (achievement "Sieve The Day": 5,000 in one network) [ref 3]; aquatic animals need a salinity requirement on top of shared needs, and every species has a temperature tolerance [ref 26].
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements); ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-004: a Water Filter needs power from a Power Generator.

> **Cross-system dependency** -- see `../dependencies.md` DEP-005: an aquarium Staff Gate has to be connected to the path network.

- Fish are kept as **Shoals** (traded as shoals; shoal welfare and social-group info added in 1.0.4) [refs 21, 27]. Fish hold a preferred position in the water column and rest by hovering [ref 26].
  _source: P1 result 2026-10-19 [ref 21 (wikily.gg/planet-zoo-2/career/maluku-islands); ref 27 (insider-gaming.com, Update 1.0.4 notes); ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch (refs 21, 26) / web_fetch (ref 27) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Leads from search excerpts only (pages not opened): salinity is set on the filtration network, not the tank; aquariums start as freshwater; water cleanliness and tank cleanliness are separate (filters vs keepers); a "Not Powered" filter needs a generator in radius.
  _source: P1 result 2026-10-19 [search excerpts only; pages not opened] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

## Aviaries and flying species
- Aviaries are built like habitats, plus posts and protective netting; birds fly freely and perch [ref 35]; mesh roofs are generated automatically once boundary and supports are set [ref 36]; roof supports come from the barrier menu and the roof tool closes the roof [ref 31].
  _source: P1 result 2026-10-19 [ref 35 (xboxygen.com review); ref 36 (securitylab.ru blog review); ref 31 (finalboss.io chapter 1 walkthrough)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 3 languages -- below 5-source floor]`
- Birds weigh the cost of flying against walking; arboreal birds prefer perching [ref 26].
  _source: P1 result 2026-10-19 [ref 26 (thegameswiki.com animals-and-welfare)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Exception: the achievement "Just In Case" asks for an aviary roof on a habitat holding a penguin or a pig, species that do not fly [ref 3].
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Aviary birds by Wikily housing (12): Eurasian Bittern, Golden Eagle, Greater Flamingo, Long-Eared Owl, Secretarybird, Shoebill, White-Backed Vulture [ref 7]; Great Hornbill, Toco Toucan, White-Tailed Sea-Eagle, Long-Tailed Parakeet and Javan Green Magpie complete 12 by roster inference `[Hypothesis -- unverified]`. African Penguin and Common Ostrich are habitat (non-flying) species [ref 7].
  _source: P1 result 2026-10-19 [ref 7 (wikily.gg/planet-zoo-2/planet-hub)] · capture: browser_fetch · confidence: medium (the five roster-inference birds: low) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`
- Walk-through exhibits exist (achievement "Metamorphose": 3 butterfly species in one) [ref 3]. Walk-through aviaries for guests: no read source describes them `[Hypothesis -- unverified]`.
  _source: P1 result 2026-10-19 [ref 3 (wikily.gg/planet-zoo-2/achievements)] · capture: browser_fetch · confidence: medium (walk-through aviaries: low) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-014.

## Achievement-bound claims
Aggregated in `../achievements.md`.
- 5 different species in one aquarium.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: full_tank · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Filtration Rate of at least 5,000 in one network.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: sieve_the_day · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- An aquarium of 25 million litres.
  _source: P1 result 2026-10-19 [refs 3, 28, 29] · capture: browser_fetch (ref 3) / web_fetch (refs 28, 29) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: a_few_more_hoses · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`
- 100% welfare on an Ocean Sunfish.
  _source: P1 result 2026-10-19 [refs 3, 21] · capture: browser_fetch (refs 3, 21) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: mola_mola_likes_you · achievement-hidden: yes · trigger_type: progression_ `[Single source -- verify · class:community-wiki]` (refs 3, 21 are both Wikily pages, counted as one source)

> **Cross-system dependency** -- see `../dependencies.md` DEP-020.

- Aviary roof on a penguin or pig habitat.
  _source: P1 result 2026-10-19 [refs 3, 28] · capture: browser_fetch (ref 3) / web_fetch (ref 28) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: just_in_case · achievement-hidden: yes · trigger_type: discovery_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
- Walk-through exhibit with 3+ butterfly species.
  _source: P1 result 2026-10-19 [refs 3, 26] · capture: browser_fetch (refs 3, 26) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none · achievement: metamorphose · achievement-hidden: yes · trigger_type: threshold_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`
