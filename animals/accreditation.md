# Planet Zoo 2 -- Species by Accreditation tier (Career and Franchise)

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** doctor Branch C 2026-10-19

Built for an interactive species-unlock lookup. One row per species (136). Tier gate rules (medals, zoos, reserves) are in `../sections/career_progression.md` (Career) and `../mechanics.md` (Franchise); this file holds only which species each tier adds. Spoiler layout: three tables, grouped by the highest spoiler tier any column in the row implies (tier 0 starting species; tier 1 species added at tiers 2 and 3; tier 2 species touching tiers 4 and 5). Every claim carries its own `_source:` line.

**Coverage (located vs total):** Franchise 136 of 136 species assigned to a tier (32 / 33 / 31 / 30 / 10 = 136, matching the guide's recorded per-tier counts). Career 136 of 136 located, by tier 33 of 33 (tier 1), 38 of 38 (tier 2), 35 of 35 (tier 3), 30 of 30 (tier 4); Career tier 5 adds no species, so 0 of 0. The Gamerant Career table names 118 of them (its tier 3 list has 34 names and its tier 4 list 13); the other 18 species were each read on their own Wikily research page, which states the Career and Franchise tier. No species has `unknown` in either column.
_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/ (Career and Franchise tables, 2026-10-18); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ (Franchise, updated 2026-10-19); https://wikily.gg/planet-zoo-2/accreditation (Career tier 1 list, 33 names); Wikily per-species research pages for the 18 species Gamerant's Career table omits, under https://wikily.gg/planet-zoo-2/research/ (european-bison, giant-grouper, golden-eagle, golden-poison-frog, great-hammerhead, indian-ocean-oriental-sweetlips, javanese-cownose-ray, komodo-dragon, lehmanns-poison-frog, monarch, ocean-sunfish, pacific-bluefin-tuna, reticulated-giraffe, sailfin-snapper, sand-tiger-shark, snow-leopard, western-lowland-gorilla, white-backed-vulture)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

## Mode rules

Career and Franchise keep separate Accreditation records and tier lists; progress and species lists differ between the modes (a species can sit at a different tier in each mode; check which mode a tier list covers). Sandbox has no Accreditation: every animal is available from the start.
_source: doctor Branch C 2026-10-19 [https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/; https://gamerant.com/accreditation-planet-zoo-2/; https://wikily.gg/planet-zoo-2/accreditation] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

Each tier adds species to what earlier tiers gave (the lists below are species ADDED at the tier, with no repeats across tiers within a mode). The per-tier Career figures in `../sections/career_progression.md` (33 / 38 / 35 / 30) are therefore additions, not running totals; the 118 located Career names are all distinct.
_source: doctor Branch C 2026-10-19 [https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ ("Each tier adds to what you already have"); https://gamerant.com/accreditation-planet-zoo-2/ (lists disjoint across tiers)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-024: each Accreditation tier adds species to Animal Trading, and a species is buyable only once its tier is unlocked.

## How a species is obtained

Every species is obtained by adopting it in Animal Trading, which needs a working Trade Centre in the zoo. A species is only ready to buy when three things hold: the edition includes it, the tier has unlocked it, and (Franchise, an online mode) the player market has one listed for sale. Cash or Conservation Credits do not bypass a tier lock. Conservation-project rewards can also hand over animals or release groups (collected under Gifts in Animal Trading; see `../items/upgrades.md`). Releasing into a Wildlife Reserve is a separate step that needs animals already in Animal Storage: no source read describes any species that is release-only, so the "Obtained" column reads `trade` for every row.
_source: doctor Branch C 2026-10-19 [https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/; https://gamerblurb.com/guides/planet-zoo-2-accreditation-guide; https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves (release groups take animals from Animal Storage)] · capture: web_fetch (allthings.how, gamerblurb) / browser_fetch (planetzoogame.com) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-025: species are adopted from Animal Trading, which needs a connected Trade Centre.

The "Release group" column says whether Wikily's list of releasable species names the species (104 releasable species; page 1 of the index shows 100 names, alphabetical to Western Lowland Gorilla; Wild Boar, White-Tailed Sea-Eagle and White-Backed Vulture are on the reserve release lists instead; the fourth entry on the unread page 2 is not identified, so Yellow Anaconda and Yellow Tang read `unknown`). "no group listed" means the species is not in the releasable list read; it does not state that release is impossible (Wikily's own research pages and counts disagree with the index; see `../items/research_tree.md`, "Contradictions and gaps").
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/release-groups; reserve lists via `reserve_releases.md` (https://insider-gaming.com/planet-zoo-2-wildlife-reserves-releasable-animals/)] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

"Other gates" lists edition gating (six Deluxe Edition species: Axolotl, Blue and Gold Fusilier, Golden Eagle, Golden Lion Tamarin, Great Hammerhead, Longfin Batfish; owning Deluxe does not skip tiers, and reaching a tier does not give Deluxe species you do not own) and the release-group research gate where read on the species page (Aardvark: available without research; the eight predators read: research level 3). Research gating for the other species' release groups was not read.
_source: doctor Branch C 2026-10-19 [https://insider-gaming.com/planet-zoo-2-all-animals-complete-zoopedia/ (Deluxe Edition column); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ (six Deluxe species, tiers still apply); https://wikily.gg/planet-zoo-2/release-groups/aardvark and the eight predator pages listed in `reserve_ecosystems.md`] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-023: a species' release groups unlock at a research level.

## Species table: starting species (Career tier 1 and Franchise tier 1)

| Species | Career tier | Franchise tier | Obtained | Release group (Wikily) | Other gates |
|---|---|---|---|---|---|
| Aardvark | 1 | 1 | trade | yes | release group needs no research |
| Amazonian Giant Centipede | 1 | 1 | trade | no group listed | -- |
| Bluespine Unicornfish | 1 | 1 | trade | yes | -- |
| Blunthead Cichlid | 1 | 1 | trade | yes | -- |
| Cape Buffalo | 1 | 1 | trade | yes | -- |
| Cloudless Sulphur | 1 | 1 | trade | no group listed | -- |
| Clown Anemonefish | 1 | 1 | trade | yes | -- |
| Clown Loach | 1 | 1 | trade | yes | -- |
| Common Bluetongue | 1 | 1 | trade | no group listed | -- |
| Common Ostrich | 1 | 1 | trade | yes | -- |
| Common Rudd | 1 | 1 | trade | yes | -- |
| Common Warthog | 1 | 1 | trade | yes | -- |
| Galapagos Giant Tortoise | 1 | 1 | trade | yes | -- |
| Giant Forest Scorpion | 1 | 1 | trade | no group listed | -- |
| Giant Malaysian Leaf Insect | 1 | 1 | trade | no group listed | -- |
| Giant Tiger Land Snail | 1 | 1 | trade | no group listed | -- |
| Koi | 1 | 1 | trade | no group listed | -- |
| Meerkat | 1 | 1 | trade | yes | -- |
| Nyala | 1 | 1 | trade | yes | -- |
| Plains Zebra | 1 | 1 | trade | yes | -- |
| Sacred Scarab Beetle | 1 | 1 | trade | no group listed | -- |
| Schooling Bannerfish | 1 | 1 | trade | yes | -- |
| Thomson's Gazelle | 1 | 1 | trade | yes | -- |
| Toco Toucan | 1 | 1 | trade | yes | -- |
| Wild Boar | 1 | 1 | trade | yes (reserve list) | -- |
| Yellow Anaconda | 1 | 1 | trade | unknown | -- |
| Yellow Tang | 1 | 1 | trade | unknown | -- |

_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/ (Career tier 1 and Franchise tier 1 tables); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ (Franchise tier 1); https://wikily.gg/planet-zoo-2/accreditation (Career tier 1 list); release column https://wikily.gg/planet-zoo-2/release-groups] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`

## Species table: tiers 2 and 3 (progression, puzzle-tier 1)

Rows whose Career and Franchise tiers are each 1, 2 or 3 and at least one is above 1.

27 of the 32 Franchise tier-1 species also start at Career tier 1; the other five Franchise tier-1 species are Career tier 2 or 3 (Bactrian Camel, Black Wildebeest, Blue Wildebeest, Red Deer, Springbok), and the six Career tier-1 species that are not Franchise tier 1 are African Tigerfish, Lion, Masai Giraffe, Ring-Tailed Lemur, Sable Antelope, Shoebill.
_source: doctor Branch C 2026-10-19 [comparison of the two tier-1 lists in https://gamerant.com/accreditation-planet-zoo-2/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

| Species | Career tier | Franchise tier | Obtained | Release group (Wikily) | Other gates |
|---|---|---|---|---|---|
| African Leopard | 2 | 3 | trade | yes | release group needs research level 3 |
| African Penguin | 2 | 3 | trade | yes | -- |
| African Tigerfish | 1 | 3 | trade | yes | -- |
| African Wild Dog | 2 | 3 | trade | yes | release group needs research level 3 |
| American Bullfrog | 2 | 2 | trade | no group listed | -- |
| Asian Small-Clawed Otter | 2 | 2 | trade | yes | -- |
| Axolotl | 2 | 2 | trade | no group listed | Deluxe Edition |
| Bactrian Camel | 3 | 1 | trade | no group listed | -- |
| Binturong | 3 | 3 | trade | yes | -- |
| Black Wildebeest | 2 | 1 | trade | yes | -- |
| Blue and Gold Fusilier | 2 | 2 | trade | yes | Deluxe Edition |
| Blue Wildebeest | 2 | 1 | trade | yes | -- |
| Boa Constrictor | 2 | 2 | trade | no group listed | -- |
| Boeseman's Rainbowfish | 3 | 3 | trade | yes | -- |
| Brown Trout | 2 | 2 | trade | yes | -- |
| Common Hippopotamus | 3 | 3 | trade | yes | -- |
| Danube Crested Newt | 3 | 3 | trade | no group listed | -- |
| Diamondback Terrapin | 2 | 2 | trade | no group listed | -- |
| Eastern Brown Snake | 3 | 3 | trade | no group listed | -- |
| Eurasian Beaver | 2 | 2 | trade | yes | -- |
| Eurasian Bittern | 2 | 2 | trade | yes | -- |
| Eurasian Brown Bear | 3 | 3 | trade | yes | release group needs research level 3 |
| Eurasian Lynx | 2 | 2 | trade | yes | release group needs research level 3 |
| Fire Salamander | 2 | 2 | trade | no group listed | -- |
| Giant Gourami | 3 | 2 | trade | yes | -- |
| Gila Monster | 3 | 3 | trade | no group listed | -- |
| Golden Lion Tamarin | 3 | 3 | trade | yes | Deluxe Edition |
| Golden Trevally | 2 | 2 | trade | yes | -- |
| Goliath Beetle | 3 | 3 | trade | no group listed | -- |
| Great Hornbill | 3 | 2 | trade | yes | -- |
| Greater Flamingo | 2 | 2 | trade | yes | -- |
| Grey Wolf | 3 | 2 | trade | yes | release group needs research level 3 |
| Grizzly Bear | 2 | 3 | trade | yes | -- |
| Indo-Pacific Leopard Shark | 3 | 2 | trade | yes | -- |
| Indo-Pacific Sergeant | 2 | 3 | trade | yes | -- |
| Javanese Cownose Ray | 3 | 2 | trade | yes | -- |
| Long-Eared Owl | 2 | 2 | trade | yes | -- |
| Long-Tailed Parakeet | 3 | 3 | trade | yes | -- |
| Longfin Batfish | 3 | 3 | trade | yes | Deluxe Edition |
| Malayan Tapir | 3 | 3 | trade | yes | -- |
| Menelaus Blue Morpho | 3 | 3 | trade | no group listed | -- |
| Mexican Redknee | 3 | 3 | trade | no group listed | -- |
| Moon Jelly | 2 | 2 | trade | no group listed | -- |
| Mountain Hare | 2 | 2 | trade | yes | -- |
| Nile Monitor | 2 | 2 | trade | yes | -- |
| North Sulawesi Babirusa | 3 | 2 | trade | yes | -- |
| Pacific Sardine | 2 | 2 | trade | yes | -- |
| Palette Surgeonfish | 3 | 2 | trade | yes | -- |
| Przewalski's Horse | 3 | 2 | trade | yes | -- |
| Red Deer | 2 | 1 | trade | yes | -- |
| Red-Eyed Tree Frog | 2 | 2 | trade | no group listed | -- |
| Ring-Tailed Lemur | 1 | 2 | trade | yes | -- |
| Sable Antelope | 1 | 2 | trade | yes | -- |
| Saltwater Crocodile | 3 | 2 | trade | yes | -- |
| Secretarybird | 2 | 3 | trade | yes | -- |
| Siamang | 3 | 3 | trade | yes | -- |
| Spotted Hyena | 2 | 2 | trade | yes | release group needs research level 3 |
| Springbok | 2 | 1 | trade | yes | -- |
| Sri Lankan Rose | 3 | 3 | trade | no group listed | -- |
| Sunda Pangolin | 3 | 3 | trade | yes | -- |
| Threespot Damselfish | 2 | 3 | trade | yes | -- |
| Western Diamondback Rattlesnake | 3 | 3 | trade | no group listed | -- |

_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/ (Career tiers 2-3 and Franchise tiers 2-3 tables); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ (Franchise tiers 2-3); release column https://wikily.gg/planet-zoo-2/release-groups; Deluxe column https://insider-gaming.com/planet-zoo-2-all-animals-complete-zoopedia/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

## Species table: tiers 4 and 5 (late-game, puzzle-tier 2)

Rows with a Franchise or Career tier of 4 or 5. Franchise tier 4 and 5 are the "2 zoos with 3 Reputation stars and 2 or 3 reserves with 3 Biodiversity stars" tiers.

| Species | Career tier | Franchise tier | Obtained | Release group (Wikily) | Other gates |
|---|---|---|---|---|---|
| African Savannah Elephant | 4 | 5 | trade | yes | -- |
| Asian Elephant | 3 | 5 | trade | yes | -- |
| Black Rhinoceros | 4 | 4 | trade | yes | -- |
| Blackspotted Puffer | 4 | 4 | trade | yes | -- |
| Blacktip Reef Shark | 2 | 4 | trade | yes | -- |
| Clown Triggerfish | 4 | 3 | trade | yes | -- |
| Desert Horned Viper | 4 | 4 | trade | no group listed | -- |
| Dolphinfish | 4 | 3 | trade | yes | -- |
| European Bison | 4 | 2 | trade | yes | -- |
| European Peacock | 4 | 4 | trade | no group listed | -- |
| Gemsbok | 4 | 3 | trade | yes | -- |
| Gharial | 4 | 4 | trade | yes | -- |
| Giant Grouper | 4 | 4 | trade | yes | -- |
| Giant Panda | 3 | 5 | trade | yes | -- |
| Giant Slippery Frog | 4 | 4 | trade | no group listed | -- |
| Golden Eagle | 4 | 3 | trade | yes | Deluxe Edition |
| Golden Poison Frog | 4 | 4 | trade | no group listed | -- |
| Goodfellow's Tree-Kangaroo | 2 | 4 | trade | yes | -- |
| Great Hammerhead | 4 | 5 | trade | yes | Deluxe Edition |
| Hawksbill Turtle | 2 | 4 | trade | yes | -- |
| Humphead Wrasse | 2 | 4 | trade | yes | -- |
| Indian Ocean Oriental Sweetlips | 4 | 3 | trade | yes | -- |
| Javan Green Magpie | 3 | 4 | trade | yes | -- |
| Komodo Dragon | 4 | 4 | trade | yes | -- |
| Lehmann's Poison Frog | 4 | 4 | trade | no group listed | -- |
| Lion | 1 | 5 | trade | yes | release group needs research level 3 |
| Masai Giraffe | 1 | 4 | trade | yes | -- |
| Monarch | 4 | 4 | trade | no group listed | -- |
| Ocean Sunfish | 4 | 5 | trade | yes | -- |
| Ocellated Eagle Ray | 4 | 4 | trade | yes | -- |
| Old World Swallowtail | 4 | 4 | trade | no group listed | -- |
| Pacific Bluefin Tuna | 4 | 4 | trade | yes | -- |
| Red Lionfish | 4 | 4 | trade | yes | -- |
| Red Panda | 3 | 4 | trade | yes | -- |
| Reticulated Giraffe | 4 | 4 | trade | yes | -- |
| Sailfin Snapper | 4 | 2 | trade | yes | -- |
| Sand Tiger Shark | 4 | 4 | trade | yes | -- |
| Shoebill | 1 | 4 | trade | yes | -- |
| Snow Leopard | 4 | 4 | trade | yes | -- |
| Sumatran Orangutan | 3 | 5 | trade | yes | -- |
| Sumatran Tiger | 3 | 4 | trade | yes | release group needs research level 3 |
| Sun Bear | 3 | 4 | trade | yes | -- |
| West Indian Manatee | 2 | 4 | trade | yes | -- |
| Western Chimpanzee | 2 | 5 | trade | yes | -- |
| Western Lowland Gorilla | 4 | 5 | trade | yes | -- |
| White-Backed Vulture | 4 | 5 | trade | yes (reserve list) | -- |
| White-Tailed Sea-Eagle | 2 | 4 | trade | yes (reserve list) | -- |

_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/ (Career tier 4 table, Franchise tiers 4-5 tables); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/ (Franchise tiers 4-5); release column https://wikily.gg/planet-zoo-2/release-groups; Deluxe column https://insider-gaming.com/planet-zoo-2-all-animals-complete-zoopedia/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

Career tier 5 adds no species (only a Silver and a Gold marketing slot).
_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/ (tier 5 "None"); https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

## Species Gamerant's Career table omits (18), located on Wikily research pages

European Bison, Giant Grouper, Golden Eagle, Golden Poison Frog, Great Hammerhead, Indian Ocean Oriental Sweetlips, Javanese Cownose Ray, Komodo Dragon, Lehmann's Poison Frog, Monarch, Ocean Sunfish, Pacific Bluefin Tuna, Reticulated Giraffe, Sailfin Snapper, Sand Tiger Shark, Snow Leopard, Western Lowland Gorilla, White-Backed Vulture. Their pages state Career tier 4 for all except Javanese Cownose Ray (Career tier 3), which fills the one open slot in Career tier 3 (35 recorded, 34 named by Gamerant) and brings Career tier 4 to 13 + 17 = 30 as recorded. The Franchise tiers stated on those 18 pages equal the Franchise tier lists above in all 18 cases. Two spot checks on species both sources name (Wild Boar: Career 1, Franchise 1; American Bullfrog: Career 2, Franchise 2) also agree with Gamerant's tables.
_source: doctor Branch C 2026-10-19 [Wikily research pages for the 18 species (URLs in the coverage line); Wikily wild-boar and american-bullfrog research pages; https://gamerant.com/accreditation-planet-zoo-2/] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

## Contradictions and corrections found

- **Edition of Golden Eagle versus Western Diamondback Rattlesnake.** Insider Gaming's Zoopedia table marks Golden Eagle as Deluxe and the Rattlesnake as Standard; allthings.how says six Deluxe species; TheGamesWiki (cited in `roster.md`) lists the same six. Only a Wikily search excerpt (never opened) put the Rattlesnake in the Deluxe list. Three sources against one unread excerpt: Golden Eagle is Deluxe, the Rattlesnake is base. Confidence medium.
_source: doctor Branch C 2026-10-19 [https://insider-gaming.com/planet-zoo-2-all-animals-complete-zoopedia/; https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/; `roster.md` ref 26 (thegameswiki.com)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`
- **The formerly unlocated base species.** `roster.md` once recorded 129 of 130 base species; Sand Tiger Shark, which appears in both 136-name Franchise lists and in Wikily's release list, is the 130th, and `roster.md` now records 130 of 130. See `roster.md`.
_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/; https://allthings.how/planet-zoo-2-how-to-unlock-all-animals-and-accreditation-tiers/; https://wikily.gg/planet-zoo-2/release-groups] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Corroborated: 3 sources, 1 language -- below 5-source floor]`
- **Name spellings.** Gamerant's Career table spells "Humhead Wrasse" and "Longfit Batfish"; read as Humphead Wrasse and Longfin Batfish (its own Franchise table and all other sources). "Black Spotted Puffer" (Gamerant, allthings.how) is Blackspotted Puffer in Wikily and `roster.md`. Insider Gaming's table has typos ("Eurasian Bitten", "Wild Board") and only 121 of 136 species (a pre-launch list).
_source: doctor Branch C 2026-10-19 [https://gamerant.com/accreditation-planet-zoo-2/; https://insider-gaming.com/planet-zoo-2-all-animals-complete-zoopedia/; https://wikily.gg/planet-zoo-2/release-groups] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`
- **Sources that give counts but no names:** PowerUp Gaming, GamerBlurb, Prima Games, Whisper of the House, games.gg and planetzoo.net all give 32 / 33 / 31 / 30 / 10 = 136 for Franchise and no species; the Prima and GamerBlurb pages name only Lions and elephants at tier 5. Wikily's accreditation page hides its Franchise tab and tiers 2-5 behind page controls that a text fetch cannot open; only its Career tier 1 list (33 names) was read.
_source: doctor Branch C 2026-10-19 [https://powerupgaming.co.uk/2026/10/14/planet-zoo-2-franchise-mode-accreditation-guide/; https://gamerblurb.com/guides/planet-zoo-2-accreditation-guide; https://primagames.com/gaming/how-to-raise-planet-zoo-2-franchise-accreditation-level; https://www.whisperofthehouse.com/planet-zoo-2/franchise-accreditation; https://planetzoo.net/accreditation/; https://games.gg/planet-zoo-2/guides/planet-zoo-2-franchise-mode-accreditation-explained/; https://wikily.gg/planet-zoo-2/accreditation] · capture: web_fetch (all but Prima, Wikily) / browser_fetch (Prima, Wikily) · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:editorial-en]` (the seven guides repeat one set of counts, probably from the in-game panel, so they are not counted as independent)
