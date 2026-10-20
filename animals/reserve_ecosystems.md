# Planet Zoo 2 -- Wildlife Reserve ecosystems (requirements, species, dependencies, setup order)

**status:** research-integrated
**last_reconciled:** 2026-10-19
**research_run:** doctor Branch C 2026-10-19

Built for an interactive reserve-planner tool. Every claim carries its own `_source:` line. Spoiler layout: general ecosystem rules and the ecosystem tables name no reserve (tier 0); the four chapter 1-3 reserves are in the tier 1 section; Tanzania and Poland (chapter 4) are in the last section at tier 2. Companion file: `reserve_releases.md` (releasable species per reserve).

**Coverage (located vs total):** 32 of 32 ecosystems read (Wikily: "32 ecosystems", 4 biomes: Grassland 10, Temperate 6, Taiga 9, Tropical 7) with Established requirements and Flourishing roles. Species-to-ecosystem needs are read for all 32 ecosystems from the ecosystem side ("animals that need it") and cross-checked against the species side for 9 of 104 releasable species (Aardvark, Lion, Eurasian Brown Bear, African Leopard, African Wild Dog, Spotted Hyena, Grey Wolf, Eurasian Lynx, Sumatran Tiger). The other 95 species pages were not read, so for them the AND-versus-OR reading of a multi-ecosystem need and any "Flourishing" or prey-role requirement are `unknown`. Which species fill the Medium Prey and Small Prey roles was not read. Which of a biome's ecosystems can actually be painted in a given reserve is not stated by any source read (reserve-to-ecosystem mapping goes through the biome and is a hypothesis).
_source: doctor Branch C 2026-10-19 [wikily.gg/planet-zoo-2/ecosystems; wikily.gg/planet-zoo-2/release-groups (104 species)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## How ecosystems work

An Ecosystem is an area you paint with the Ecosystem Brush inside a Wildlife Reserve; each Ecosystem Type needs its own mix of terrain and plants, and when its Area, Terrain and Nature requirements are met it moves from Invalid to Established. Some ecosystems also need water, or a highland or lowland area.
_source: doctor Branch C 2026-10-19 [https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves (official guide, Frontier); https://wikily.gg/planet-zoo-2/ecosystems; https://www.dtgre.com/2026/10/planet-zoo-2-ecosystem-not-established-fix.html; https://primagames.com/gaming/planet-zoo-2-flourishing-ecosystem] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 4 sources, 1 language -- below 5-source floor]`

An Ecosystem can only become Flourishing after it is Established, and it needs released animals that provide the right Ecosystem Roles; each Release Group lists the roles it provides, and once all of an ecosystem's roles are filled it begins Flourishing. Flourishing is required for certain Release Groups and raises the reserve's Ecosystem Rating.
_source: doctor Branch C 2026-10-19 [https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves; https://primagames.com/gaming/planet-zoo-2-flourishing-ecosystem; https://www.dtgre.com/2026/10/planet-zoo-2-ecosystem-not-established-fix.html; https://wikily.gg/planet-zoo-2/ecosystems] · capture: browser_fetch (official, Prima, DTG, Wikily) · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 4 sources, 1 language -- below 5-source floor]`

The game shows the missing item: select the ecosystem in the Ecosystem panel, then select an unmet requirement to filter the brush or category (Nature Requirement selection filters the object browser). "Too Small" means the painted area is below the displayed size requirement; expand it before adding features. There is no universal checklist: requirements differ per ecosystem.
_source: doctor Branch C 2026-10-19 [https://www.dtgre.com/2026/10/planet-zoo-2-ecosystem-not-established-fix.html; https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

To check what a Flourishing ecosystem is missing: open the Ecosystem Brush, pick the ecosystem, select the pawprint at the top of the right-hand pop-up, read the listed Species Roles, then trade for or breed animals that provide them and release them into the reserve.
_source: doctor Branch C 2026-10-19 [https://primagames.com/gaming/planet-zoo-2-flourishing-ecosystem] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

Reserve Biodiversity Rating = Ecosystem Rating + Research Rating. Ecosystem Rating rises with Established and Flourishing ecosystems, removing Environmental Pollution and Invasive Flora, and Species Diversity (more different species released).
_source: doctor Branch C 2026-10-19 [https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

A Release Group for a species may need that species researched in a zoo first. Release Groups take only animals already in Animal Storage; once finalised the animals go to acclimatisation and cannot return to the zoo.
_source: doctor Branch C 2026-10-19 [https://www.planetzoogame.com/en-US/2/player-guides/wildlife-reserves] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:editorial-en]`

## Ecosystem requirements by biome

Established requirements are painted terrain, nature objects (minimum counts, or ranges) and, for some, water or an elevation condition. Flourishing needs released animals filling the listed roles (who can fill each role: see "Role-fill lists"). "Species that list it" are the species whose release requirements name that ecosystem (see the next section for what that means). Counts of nature objects are as published; the unit is not stated.

### Grassland biome (10 ecosystems)

| Ecosystem | Terrain | Also needs | Nature objects (Established) | Flourishing roles | Species that list it |
|---|---|---|---|---|---|
| Dense Forest | Grass, Soil, Detritus | -- | Tree Litter at least 125; Medium Rocky Cover at least 30; Spreading Crown Trees at least 300; Dense Crown Trees at least 170 | High Browsers; Terrestrial Seed Dispersers | African Leopard, Cape Buffalo, Masai Giraffe, Nyala, Reticulated Giraffe |
| Grassland | Grass, Scrub Grass | -- | Bushes at least 125; Trees 75 to 400 | Grazers; Soil Rooters | Black Rhinoceros, Black Wildebeest, Blue Wildebeest, Common Ostrich, Common Warthog, Plains Zebra, Sable Antelope, Secretarybird, Springbok, Thomson's Gazelle |
| Riverine | Grass, Soil, Wetland Sediment, Sand, Waterlogged | Water area | Small Rocky Cover at least 75; Semi-Aquatic Plants at least 200 | Wetland Engineers; Underwater Grazers | African Leopard, African Savannah Elephant, African Wild Dog, Greater Flamingo, Lion, Nile Monitor, Spotted Hyena |
| Rocky Hills | Grass, Soil, Rock | Area with elevation above 15m | Medium Rocky Cover at least 50; Large Rocky Cover at least 60 | Grazers; Low Browsers | Lion |
| Sandy Plain | Soil, Sand | Limited water area | Small Rocky Cover at least 80; Medium Rocky Cover at least 40; Bushes 150 to 400 | Scavengers; Low Browsers; Terrestrial Foragers | African Wild Dog, Spotted Hyena |
| Savannah | Grass, Scrub Grass, Detritus | Limited water area | Pyrophyte Plants at least 175; Tree Litter at least 125; Termite Mounds at least 5; Acacia Trees at least 35 | Scavengers; Low Browsers; Terrestrial Seed Dispersers | Aardvark, African Savannah Elephant, African Wild Dog, Common Ostrich, Gemsbok, Lion, Meerkat, Sable Antelope, Springbok, White-Backed Vulture |
| Shrubland | Scrub Grass, Soil, Detritus | Limited water area | Small Rocky Cover at least 100; Flowers at least 250; Bushes at least 700; Trees 20 to 250 | Low Browsers; Soil Rooters; Terrestrial Foragers | Aardvark, Common Ostrich, Common Warthog |
| Swamp | Grass, Soil, Wetland Sediment, Waterlogged | Water area | Freshwater Bed Plants at least 175; Semi-Aquatic Plants at least 450; Bushes at least 100; Semi-Aquatic Trees at least 20 | Aerial Seed Dispersers; Wetland Engineers; Underwater Grazers | African Tigerfish, Blunthead Cichlid, Common Hippopotamus, Greater Flamingo, Nile Monitor, Shoebill |
| Watering Hole | Grass, Wetland Sediment | Water area | none listed ("No entries") | Wetland Engineers | Greater Flamingo, Plains Zebra |
| Wetland | Grass, Wild Grass, Wetland Sediment, Waterlogged | Water area | Semi-Aquatic Plants at least 325 | Wetland Engineers; Underwater Grazers | African Leopard, African Savannah Elephant, Greater Flamingo, Nile Monitor |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/ecosystems/dense-forest; .../grassland; .../riverine; .../rocky-hills; .../sandy-plain; .../savannah; .../shrubland; .../swamp; .../watering-hole; .../wetland (all under https://wikily.gg/planet-zoo-2/ecosystems/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

### Temperate biome (6 ecosystems)

| Ecosystem | Terrain | Also needs | Nature objects (Established) | Flourishing roles | Species that list it |
|---|---|---|---|---|---|
| Closed Canopy Forest | Grass, Soil, Forest Floor | -- | Leaf Litter at least 200; Tree Litter at least 170; Mushrooms at least 275; Understorey Plants at least 400; Deciduous Trees at least 400 | Low Browsers; Terrestrial Seed Dispersers; Aerial Foragers | European Bison, Long-Eared Owl |
| Fen Wetland | Grass, Wild Grass, Soil, Wetland Sediment, Waterlogged | Water area | Flowers at least 450; Water Floating Plants at least 20; Semi-Aquatic Plants at least 1,350; Deciduous Trees 20 to 150; Trees 20 to 200 | Soil Rooters; Wetland Engineers | Eurasian Beaver, Eurasian Bittern |
| Lake (Temperate) | Grass, Wild Grass, Soil, Wetland Sediment | Water area | Freshwater Bed Plants at least 150; Water Floating Plants at least 50; Medium Rocky Cover at least 30; Semi-Aquatic Plants at least 450; Semi-Aquatic Trees 50 to 250 | Underwater Grazers | Brown Trout, Common Rudd, Eurasian Beaver, Golden Eagle, White-Tailed Sea-Eagle |
| Lowland Marsh | Grass, Wetland Sediment, Waterlogged | -- | Small Rocky Cover at least 120; Medium Rocky Cover at least 45; Semi-Aquatic Plants at least 400; Shrubs at least 150 | Wetland Engineers; Terrestrial Foragers | Eurasian Bittern |
| Open Canopy Forest | Grass, Wild Grass, Soil | -- | Leaf Litter at least 100; Flowers at least 600; Mushrooms at least 200; Shrubs at least 300; Fruit Bearing Bushes at least 300; Deciduous Trees 100 to 275 | Low Browsers; Terrestrial Seed Dispersers; Terrestrial Spore Dispersers | European Bison, Grey Wolf, Wild Boar |
| Pastures | Grass, Long Grass | -- | Flowers at least 800; Trees 20 to 120 | Grazers; Terrestrial Pollinators | European Bison, Red Deer |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/ecosystems/closed-canopy-forest; .../fen-wetland; .../lake-temperate; .../lowland-marsh; .../open-canopy-forest; .../pastures (all under https://wikily.gg/planet-zoo-2/ecosystems/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

### Taiga biome (9 ecosystems)

| Ecosystem | Terrain | Also needs | Nature objects (Established) | Flourishing roles | Species that list it |
|---|---|---|---|---|---|
| Flooded Grassland | Long Grass, Heavy Soil, Waterlogged | Water area | Ferns at least 250; Semi-Aquatic Plants at least 250; Trees 20 to 80 | Grazers; Wetland Engineers; Soil Rooters | none listed |
| Lake (Loch) | Grass, Soil, Scree | Water area | Small Rocky Cover at least 550 | Wetland Engineers; Underwater Grazers | none listed |
| Lake (Taiga) | Grass, Soil, Scree | Water area | Small Rocky Cover at least 250 | Wetland Engineers; Underwater Grazers | Brown Trout, Common Rudd, Eurasian Beaver, Eurasian Brown Bear, Golden Eagle, White-Tailed Sea-Eagle |
| Mixed Lowland Forest | Grass, Forest Floor, Moss | -- | Leaf Litter at least 150; Tree Litter at least 200; Mushrooms at least 250; Shrubs at least 800; Deciduous Trees at least 475; Conifers at least 500 | Low Browsers; Terrestrial Seed Dispersers; Terrestrial Spore Dispersers | Eurasian Lynx, Grey Wolf, Long-Eared Owl, Red Deer, Wild Boar |
| Montane Forest | Short Grass, Moss, Forest Floor, Rock | Area with elevation above 50m | Mossy Cover at least 300; Tree Litter at least 325; Understorey Plants at least 750; Medium Rocky Cover at least 50; Conifers at least 600; Cold Hardy Trees at least 225 | Terrestrial Seed Dispersers; Soil Rooters | Eurasian Lynx |
| Montane Forest (Boreal) | Moss, Forest Floor, Rock | -- | Mossy Cover at least 500; Understorey Plants at least 800; Tree Litter at least 450; Medium Rocky Cover at least 75; Conifers at least 800; Cold Hardy Trees at least 300 | Low Browsers; Terrestrial Seed Dispersers | none listed |
| Moorland | Grass, Wild Grass | -- | Heather at least 900; Shrubs at least 500; Trees 20 to 90 | Grazers; Terrestrial Seed Dispersers; Terrestrial Foragers | Eurasian Brown Bear, Mountain Hare |
| Rocky Peaks | Moss, Rock, Scree | -- | Small Rocky Cover at least 50; Shrubs 150 to 500; Medium Rocky Cover at least 35; Large Rocky Cover at least 75 | Low Browsers | none listed |
| Saltmarsh | Grass, Soil, Sand, Waterlogged | Water area | Tree Litter at least 100; Semi-Aquatic Plants at least 450; Trees 20 to 80 | Soil Rooters; Wetland Engineers; Terrestrial Foragers | none listed |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/ecosystems/flooded-grassland; .../lake-loch; .../lake-taiga; .../mixed-lowland-forest; .../montane-forest; .../montane-forest-boreal; .../moorland; .../rocky-peaks; .../saltmarsh (all under https://wikily.gg/planet-zoo-2/ecosystems/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

The DTG Reviews page independently gives the same Mixed Lowland Forest terrain (Grass, Forest Floor, Moss), nature categories (Leaf Litter, Tree Litter, Mushrooms, Shrubs, Deciduous Trees, Conifers) and Flourishing roles (Low Browsers, Terrestrial Seed Dispersers, Terrestrial Spore Dispersers), and the lake's Small Rocky Cover requirement; no contradiction with Wikily.
_source: doctor Branch C 2026-10-19 [https://www.dtgre.com/2026/10/planet-zoo-2-ecosystem-not-established-fix.html; https://wikily.gg/planet-zoo-2/ecosystems/mixed-lowland-forest] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

### Tropical biome (7 ecosystems)

| Ecosystem | Terrain | Also needs | Nature objects (Established) | Flourishing roles | Species that list it |
|---|---|---|---|---|---|
| Forest Swamp | Short Grass, Moss, Soil, Waterlogged | Water area | Semi-Aquatic Plants at least 200; Palm Trees 25 to 50; Semi-Aquatic Trees at least 75 | Low Browsers; Wetland Engineers; Underwater Grazers | Asian Elephant, Clown Loach, Giant Gourami, Long-Tailed Parakeet, Saltwater Crocodile |
| Grassland (Tropical) | Grass, Wild Grass | -- | Ferns at least 300 | Grazers; Soil Rooters; Terrestrial Foragers | Asian Elephant |
| Limestone Hills | Grass, Rock | Elevation range (not specified) | Large Rocky Cover at least 45; Trees 15 to 40 | Low Browsers; Aerial Foragers | Sun Bear |
| Lowland Rainforest | Wild Grass, Moss, Forest Floor | Area with elevation below 70m | Ferns at least 700; Tree Litter at least 200; Climbers at least 150; Small Rocky Cover 75 to 200; Evergreen Trees at least 320; Dense Crown Trees at least 230 | Low Browsers; Terrestrial Seed Dispersers; Terrestrial Pollinators | Binturong, Great Hornbill, Long-Tailed Parakeet, Malayan Tapir, North Sulawesi Babirusa, Siamang, Sumatran Tiger, Sun Bear, Sunda Pangolin |
| Montane Rainforest | Wild Grass, Moss, Forest Floor, Rock | Area with elevation above 95m | Climbers at least 350; Small Rocky Cover at least 120; Medium Rocky Cover 25 to 75; Evergreen Trees at least 400; Canopy Emergent Trees at least 100 | Aerial Seed Dispersers; Soil Rooters; Aerial Foragers | Great Hornbill, Siamang, Sumatran Orangutan |
| Peatland | Wild Grass, Soil, Scree, Waterlogged | -- | Ferns 125 to 225; Palm Trees at least 70 | Low Browsers; Wetland Engineers; Terrestrial Foragers | Asian Small-Clawed Otter, Sumatran Orangutan |
| River | Soil, Scree | Water area | Freshwater Bed Plants at least 250 | Underwater Grazers | Asian Small-Clawed Otter, Clown Loach, Giant Gourami, Saltwater Crocodile |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/ecosystems/forest-swamp; .../grassland-tropical; .../limestone-hills; .../lowland-rainforest; .../montane-rainforest; .../peatland; .../river (all under https://wikily.gg/planet-zoo-2/ecosystems/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

Five of the 32 ecosystems have no species listed as needing them (Flooded Grassland, Lake (Loch), Montane Forest (Boreal), Rocky Peaks, Saltmarsh). Whether they exist only to lift the Ecosystem Rating, or are used by species whose pages were not read, is unknown.
_source: doctor Branch C 2026-10-19 [the five ecosystem pages named; https://wikily.gg/planet-zoo-2/ecosystems/] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

## Role-fill lists (who can fill each Flourishing role)

Wikily publishes one list per role, identical on every ecosystem page that uses the role. The list is global (it is not filtered to a reserve): to know who can fill a role in a given reserve, intersect it with that reserve's releasable list in `reserve_releases.md`.

| Role | Species that fill it |
|---|---|
| Low Browsers | Black Rhinoceros, Cape Buffalo, North Sulawesi Babirusa, Red Deer, Sable Antelope |
| High Browsers | African Savannah Elephant, Asian Elephant, Eurasian Brown Bear, Masai Giraffe, Reticulated Giraffe |
| Grazers | Black Wildebeest, Blue Wildebeest, Common Hippopotamus, Common Ostrich, European Bison, Malayan Tapir, Mountain Hare, Nyala, Plains Zebra, Springbok, Thomson's Gazelle, Wild Boar |
| Terrestrial Seed Dispersers | African Savannah Elephant, Asian Elephant, Binturong, Black Rhinoceros, Black Wildebeest, Blue Wildebeest, Cape Buffalo, Common Ostrich, Eurasian Brown Bear, European Bison, Gemsbok, Malayan Tapir, Masai Giraffe, Mountain Hare, Nyala, Plains Zebra, Red Deer, Reticulated Giraffe, Sable Antelope, Siamang, Springbok, Sumatran Orangutan, Sun Bear |
| Terrestrial Spore Dispersers | Common Warthog, Wild Boar |
| Terrestrial Pollinators | Binturong, Eurasian Brown Bear, Red Deer, Sumatran Orangutan |
| Terrestrial Foragers | Aardvark, African Savannah Elephant, Asian Elephant, Binturong, Eurasian Beaver, Siamang, Sumatran Orangutan |
| Soil Rooters | Aardvark, Common Warthog, Meerkat, North Sulawesi Babirusa, Sun Bear, Sunda Pangolin, Wild Boar |
| Scavengers | Golden Eagle, Nile Monitor, Secretarybird, Spotted Hyena, White-Backed Vulture, White-Tailed Sea-Eagle |
| Aerial Foragers | Eurasian Bittern, Golden Eagle, Great Hornbill, Long-Eared Owl, White-Backed Vulture, White-Tailed Sea-Eagle |
| Aerial Seed Dispersers | Great Hornbill, Greater Flamingo, Long-Tailed Parakeet |
| Wetland Engineers | Asian Small-Clawed Otter, Common Hippopotamus, Eurasian Beaver |
| Underwater Grazers | Blunthead Cichlid, Common Rudd, Giant Gourami |

_source: doctor Branch C 2026-10-19 [Flourishing-requirement tables on https://wikily.gg/planet-zoo-2/ecosystems/ pages (dense-forest, fen-wetland, forest-swamp, grassland-tropical, lowland-rainforest, mixed-lowland-forest, montane-rainforest, open-canopy-forest, pastures, peatland, sandy-plain, savannah, lake-taiga)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

Roles that exist on species pages but whose fill lists were not read: Medium Prey (14 species per Wikily's release-group filter), Small Prey (9), Predators (17), Large Prey (2), Aerial Pollinators (1), Medium Underwater Prey (1), Small Underwater Prey (1), Underwater Predators (3). These are what predators' "Species Roles Required: Medium Prey / Small Prey" needs; which species fill them is `unknown` here. Seen so far: Aardvark fills Small Prey; Lion, African Leopard, African Wild Dog, Spotted Hyena, Grey Wolf, Eurasian Lynx, Sumatran Tiger and Eurasian Brown Bear fill Predators.
_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/release-groups (role filter counts); species pages named in the next section] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Species release requirements (the dependency data)

A species page lists "Ecosystems Required" as one or more rows. Observed forms: a plain ecosystem ("Moorland"), "Either X or Y", and "Flourishing X" (the ecosystem must be Flourishing, not just Established). Separate rows are separate requirements. A row may also require a role to be filled by earlier releases ("Species Roles Required: Medium Prey"). Read on the species side for 9 species:

| Species | Ecosystems Required (verbatim) | Species Roles Required | Release unlock | Roles it fills once released |
|---|---|---|---|---|
| Aardvark | Either Savannah or Shrubland; also Nature Requirements: Burrows | none | Available without research | Small Prey, Soil Rooters, Terrestrial Foragers |
| Lion | Either Rocky Hills or Riverine; Flourishing Savannah | Medium Prey | Research level 3 | Predators |
| Eurasian Brown Bear | Moorland; Flourishing Lake | none listed | Research level 3 | High Browsers, Predators, Terrestrial Pollinators, Terrestrial Seed Dispersers |
| African Leopard | Either Wetland or Riverine; Flourishing Dense Forest | Medium Prey | Research level 3 | Predators |
| African Wild Dog | Savannah; Either Sandy Plain or Riverine | Medium Prey | Research level 3 | Predators |
| Spotted Hyena | Either Sandy Plain or Riverine | Medium Prey | Research level 3 | Predators, Scavengers |
| Grey Wolf | Either Flourishing Open Canopy Forest or Flourishing Mixed Lowland Forest | Medium Prey, Small Prey | Research level 3 | Predators |
| Eurasian Lynx | Mixed Lowland Forest; Montane Forest | Medium Prey | Research level 3 | Predators |
| Sumatran Tiger | Flourishing Lowland Rainforest | Medium Prey | Research level 3 | Predators |

_source: doctor Branch C 2026-10-19 [https://wikily.gg/planet-zoo-2/release-groups/aardvark; .../lion; .../eurasian-brown-bear; .../african-leopard; .../african-wild-dog; .../spotted-hyena; .../grey-wolf; .../eurasian-lynx; .../sumatran-tiger (all under https://wikily.gg/planet-zoo-2/release-groups/)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

The ecosystem-side lists in the biome tables match the species-side rows for all 9 species read (for example the Eurasian Brown Bear appears on exactly Lake (Taiga) and Moorland, the Grey Wolf on exactly Open Canopy Forest and Mixed Lowland Forest). So "species that list it" can be read as "species whose release requirements name it"; whether a given multi-ecosystem listing means "either" or "all" is known only for these 9.
_source: doctor Branch C 2026-10-19 [species pages above compared with the 32 ecosystem pages] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Hypothesis -- unverified]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-016: a reserve takes a Release Group only while that species' release requirements are met.

> **Cross-system dependency** -- see `../dependencies.md` DEP-023: a species' release groups unlock at a research level.

> **Cross-system dependency** -- see `../dependencies.md` DEP-027.

### Dependencies between ecosystems

These chains are stated by the data above (not derived orderings):
- **Flourishing Savannah** (roles Scavengers, Low Browsers, Terrestrial Seed Dispersers) is required by the Lion. The role fillers come from other ecosystems: Scavengers are Golden Eagle, Nile Monitor, Secretarybird, Spotted Hyena, White-Backed Vulture, White-Tailed Sea-Eagle (Nile Monitor lists Riverine, Swamp or Wetland; Secretarybird lists Grassland; White-Backed Vulture lists Savannah; Spotted Hyena lists Sandy Plain or Riverine); Low Browsers are Black Rhinoceros, Cape Buffalo, Sable Antelope and others (Dense Forest, Grassland, Savannah).
- **Flourishing Dense Forest** (High Browsers, Terrestrial Seed Dispersers) is required by the African Leopard; High Browsers are elephants, giraffes and the brown bear.
- **Flourishing Lowland Rainforest** (Low Browsers, Terrestrial Seed Dispersers, Terrestrial Pollinators) is required by the Sumatran Tiger. Terrestrial Pollinators are Binturong, Eurasian Brown Bear, Red Deer, Sumatran Orangutan; the Orangutan lists Peatland or Montane Rainforest, so a second ecosystem feeds the first.
- **Flourishing Open Canopy Forest or Mixed Lowland Forest** is required by the Grey Wolf (roles Low Browsers, Terrestrial Seed Dispersers, Terrestrial Spore Dispersers; the spore dispersers are only Common Warthog and Wild Boar).
- **Flourishing Lake** is required by the Eurasian Brown Bear (alongside Moorland). The lake variant roles are Wetland Engineers (Asian Small-Clawed Otter, Common Hippopotamus, Eurasian Beaver) and Underwater Grazers (Blunthead Cichlid, Common Rudd, Giant Gourami). The page names "Flourishing Lake" without a variant; the bear's ecosystem list shows Lake (Taiga).
- **Predator prerequisites:** every predator read needs a prey role filled first (Medium Prey; the Grey Wolf also Small Prey).
- Wikily's pages do not state a "needs a neighbouring ecosystem established" rule; the only cross-ecosystem links found are the species-mediated ones above.
_source: doctor Branch C 2026-10-19 [Wikily ecosystem and release-group pages listed above; https://primagames.com/gaming/planet-zoo-2-flourishing-ecosystem (Flourishing is required for certain Release Groups)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ `[Single source -- verify · class:community-wiki]`

## Reserve to biome (chapter 1-3 reserves, tier 1)

The four chapter 1-3 reserves sit in these biomes: Great Rift Valley Reserve = Grassland; Scottish Highlands = Taiga; Sweden Reserve = Taiga; Sumatra Reserve = Tropical. The Sweden Career level page also states Biome Taiga. Which of a biome's ecosystems are paintable in a given reserve is not stated; the tables below assume all ecosystems of the reserve's biome are available.
_source: doctor Branch C 2026-10-19 [https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/ (biome per reserve); https://wikily.gg/planet-zoo-2/career/sweden-reserve (Sweden: Taiga)] · capture: web_fetch (games.gg) / browser_fetch (Wikily) · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:editorial-en]`

The reserve-to-ecosystem availability is an inference through the biome.
_source: model analysis, doctor Branch C 2026-10-19 [games.gg biome per reserve; Wikily biome per ecosystem] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Hypothesis -- unverified]`

Setup orders use two numbers per ecosystem: "rows" = nature-object rows plus one for each extra (water, elevation). Rows: Grassland 2; Riverine 3; Dense Forest 4; Savannah 5; Swamp 5; Lake (Taiga) 2; Moorland 3; Mixed Lowland Forest 6; Montane Forest 7; Peatland 2; Forest Swamp 4; Lowland Rainforest 7 (counted from the tables above).

### Rules used for every suggested order (the guide's reasoning, not a quoted guide)

1. Establish an ecosystem only if some species on the reserve's releasable list names it (or it is a stated prerequisite); choose the smallest set of ecosystems that lets every listed species be released, reading each "list it" species as satisfied by any one listed ecosystem (a lower bound; if a species really needs all its listed ecosystems the set grows).
2. Simplest first: among ecosystems with no unmet prerequisite, establish the one with the fewest rows first; ties go to the ecosystem that is a Flourishing prerequisite, then to the one releasing more species.
3. Release each species as soon as one ecosystem it names is Established.
4. Prerequisites first: before a species with a "Flourishing X" row, X is established and its roles are filled by earlier releases (roles read from the role-fill lists, restricted to the reserve's own list).
5. Predators last: a species with a prey-role requirement is released after the herbivore waves. Which species supply Medium Prey and Small Prey was not read, so that role is assumed to be satisfied by the herbivore waves (unverified).
_source: model analysis, doctor Branch C 2026-10-19 [rules applied to the tables in this file; no source states an order] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

### Great Rift Valley Reserve (Grassland biome)

Releasable list (27 per `reserve_releases.md`): Aardvark, African Leopard, African Savannah Elephant, African Tigerfish, African Wild Dog, Black Rhinoceros, Black Wildebeest, Blue Wildebeest, Blunthead Cichlid, Cape Buffalo, Common Hippopotamus, Common Warthog, Gemsbok, Greater Flamingo, Lion, Masai Giraffe, Meerkat, Nile Monitor, Nyala, Plains Zebra, Reticulated Giraffe, Sable Antelope, Secretarybird, Shoebill, Spotted Hyena, Springbok, White-Backed Vulture. Each of the 27 appears in at least one Grassland-biome ecosystem's "species that list it".
_source: doctor Branch C 2026-10-19 [reserve list from https://insider-gaming.com/planet-zoo-2-wildlife-reserves-releasable-animals/ via `reserve_releases.md`; https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/ lists 26 without a 27th named; ecosystem listings from the Wikily pages above] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Contradicted across sources -- see notes]`

Count conflict: games.gg's list for this reserve has 26 names (its own summary table says 27) and includes Meerkat; the insider-gaming list used in `reserve_releases.md` has 27. Treated as 27 here; the species-level mapping above is unaffected.
_source: doctor Branch C 2026-10-19 [https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/; https://insider-gaming.com/planet-zoo-2-wildlife-reserves-releasable-animals/] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Contradicted across sources -- see notes]`

Smallest ecosystem set for the whole list (lower bound): **Grassland, Riverine, Dense Forest, Savannah, Swamp** (5). Swamp alone serves African Tigerfish, Blunthead Cichlid, Common Hippopotamus and Shoebill; Dense Forest alone serves Cape Buffalo, Masai Giraffe, Nyala and Reticulated Giraffe; Grassland alone serves Black Rhinoceros, both wildebeests and Secretarybird; Savannah alone serves Gemsbok, Meerkat and White-Backed Vulture; the Lion's two rows force Savannah (Flourishing) plus Riverine or Rocky Hills. Fewer than 5 cannot cover the list.
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

**Suggested setup order, Great Rift Valley Reserve** (confidence low):
1. Grassland (2 rows). Release Black Rhinoceros, Black Wildebeest, Blue Wildebeest, Plains Zebra, Springbok, Common Warthog, Sable Antelope, Secretarybird.
2. Riverine (3 rows). Release Greater Flamingo, Nile Monitor, African Savannah Elephant.
3. Dense Forest (4 rows). Release Cape Buffalo, Masai Giraffe, Reticulated Giraffe, Nyala.
4. Savannah (5 rows, Flourishing prerequisite for the Lion, so it goes before Swamp on the tie). Release Aardvark, Gemsbok, Meerkat, White-Backed Vulture.
5. Swamp (5 rows). Release Common Hippopotamus, African Tigerfish, Blunthead Cichlid, Shoebill.
6. Make Savannah Flourishing: its roles are Scavengers (Secretarybird, Nile Monitor, White-Backed Vulture are already released), Low Browsers (Black Rhinoceros, Cape Buffalo, Sable Antelope) and Terrestrial Seed Dispersers (many already released).
7. Make Dense Forest Flourishing: High Browsers (African Savannah Elephant, both giraffes) and Terrestrial Seed Dispersers.
8. Predators last: Spotted Hyena (Sandy Plain or Riverine, so Riverine from step 2 serves), African Wild Dog (Savannah plus Riverine), Lion (Flourishing Savannah plus Riverine), African Leopard (Flourishing Dense Forest plus Riverine). All need Medium Prey filled.
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

### Scottish Highlands (Taiga biome)

Releasable list (11): Brown Trout, Common Rudd, Eurasian Beaver, Eurasian Lynx, Golden Eagle, Grey Wolf, Long-Eared Owl, Mountain Hare, Red Deer, White-Tailed Sea-Eagle, Wild Boar. Golden Eagle may be Deluxe-only (see `roster.md`). Lake (Loch) is a Taiga ecosystem with no species listed; its name suggests a Scottish role but no source says so.
_source: doctor Branch C 2026-10-19 [reserve list via `reserve_releases.md` (insider-gaming); Wikily ecosystem pages] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

Smallest ecosystem set (lower bound): **Lake (Taiga), Moorland, Mixed Lowland Forest, Montane Forest** (4): Lake (Taiga) serves Brown Trout, Common Rudd, Eurasian Beaver, Golden Eagle, White-Tailed Sea-Eagle; Moorland serves Mountain Hare; Mixed Lowland Forest serves Wild Boar, Red Deer, Long-Eared Owl and the Grey Wolf (Flourishing); the Lynx needs Mixed Lowland Forest and Montane Forest.
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

**Suggested setup order, Scottish Highlands** (confidence low):
1. Lake (Taiga) (2 rows). Release Brown Trout, Common Rudd, Eurasian Beaver, Golden Eagle, White-Tailed Sea-Eagle.
2. Moorland (3 rows). Release Mountain Hare.
3. Mixed Lowland Forest (6 rows). Release Wild Boar, Red Deer, Long-Eared Owl.
4. Make Mixed Lowland Forest Flourishing: Low Browsers (Red Deer), Terrestrial Seed Dispersers (Red Deer, Mountain Hare), Terrestrial Spore Dispersers (Wild Boar), all already released.
5. Grey Wolf (Flourishing Mixed Lowland Forest; Medium Prey and Small Prey filled).
6. Montane Forest (7 rows, elevation above 50m). Release Eurasian Lynx (also needs Mixed Lowland Forest and Medium Prey).
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

### Sweden Reserve (Taiga biome)

Releasable list (12): the Scottish Highlands list plus Eurasian Brown Bear. The Sweden Career level objectives (Bronze) are Red Deer x1, Wild Boar x1 and Grey Wolf x1 released, and a Biodiversity Rating of 2.5 stars.
_source: doctor Branch C 2026-10-19 [reserve list via `reserve_releases.md`; https://wikily.gg/planet-zoo-2/career/sweden-reserve (Bronze objectives)] · capture: browser_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Single source -- verify · class:community-wiki]`

Smallest ecosystem set (lower bound): the same four as the Scottish Highlands; the Brown Bear adds no new ecosystem (Moorland plus Flourishing Lake).
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

**Suggested setup order, Sweden Reserve** (confidence low): steps 1-6 as the Scottish Highlands, with these changes. After step 1 the Flourishing Lake (Taiga) is reachable: Wetland Engineers (Eurasian Beaver) and Underwater Grazers (Common Rudd, the only one of the three on this list) are both released in step 1, so make the lake Flourishing at that point; then release the Eurasian Brown Bear last (Moorland plus Flourishing Lake; no prey role listed). The Career Bronze objective (Red Deer, Wild Boar, Grey Wolf) is met after step 5.
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve; Career objectives from Wikily Sweden page] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

### Sumatra Reserve (Tropical biome)

Releasable list (15): Asian Elephant, Asian Small-Clawed Otter, Binturong, Clown Loach, Giant Gourami, Great Hornbill, Long-Tailed Parakeet, Malayan Tapir, North Sulawesi Babirusa, Saltwater Crocodile, Siamang, Sumatran Orangutan, Sumatran Tiger, Sun Bear, Sunda Pangolin.
_source: doctor Branch C 2026-10-19 [reserve list via `reserve_releases.md` (insider-gaming); https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/ gives the same 15] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Corroborated: 2 sources, 1 language -- below 5-source floor]`

Smallest ecosystem set (lower bound): **Peatland, Forest Swamp, Lowland Rainforest** (3). Lowland Rainforest serves Binturong, Great Hornbill, Malayan Tapir, North Sulawesi Babirusa, Siamang, Sun Bear, Sunda Pangolin and the Sumatran Tiger (Flourishing); Forest Swamp serves Asian Elephant, Clown Loach, Giant Gourami, Long-Tailed Parakeet and Saltwater Crocodile; Peatland serves Asian Small-Clawed Otter and Sumatran Orangutan. Fewer than 3 cannot cover the list (the Elephant needs Forest Swamp or Grassland (Tropical), the Orangutan needs Peatland or Montane Rainforest, and Lowland Rainforest is the only home of several species).
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

**Suggested setup order, Sumatra Reserve** (confidence low):
1. Peatland (2 rows). Release Sumatran Orangutan, Asian Small-Clawed Otter.
2. Forest Swamp (4 rows). Release Asian Elephant, Clown Loach, Giant Gourami, Saltwater Crocodile, Long-Tailed Parakeet.
3. Lowland Rainforest (7 rows, elevation below 70m). Release Binturong, Malayan Tapir, North Sulawesi Babirusa, Sunda Pangolin, Sun Bear, Siamang, Great Hornbill.
4. Make Lowland Rainforest Flourishing: Low Browsers (North Sulawesi Babirusa), Terrestrial Seed Dispersers (Asian Elephant, Binturong, Siamang, Sumatran Orangutan, Malayan Tapir, Sun Bear), Terrestrial Pollinators (Binturong, Sumatran Orangutan); the Orangutan from Peatland is what makes this a cross-ecosystem dependency.
5. Sumatran Tiger last (Flourishing Lowland Rainforest; Medium Prey filled).
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: progression_ `[Derived -- from requirements in this file; no source states an order]`

## Chapter 4 reserves (late-game, puzzle-tier 2)

Tanzania Reserve is in the Grassland biome and Poland Reserve in the Temperate biome (games.gg). Their sections are tier 2 throughout.
_source: doctor Branch C 2026-10-19 [https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/ (biome per reserve)] · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Single source -- verify · class:editorial-en]`

### Tanzania Reserve (Grassland biome; late-game, puzzle-tier 2)

Releasable list (28 per `reserve_releases.md`): the Great Rift Valley list minus Meerkat, plus Common Ostrich and Thomson's Gazelle. games.gg lists 27 names for this reserve (its own table says 29) and omits Meerkat as well.
_source: doctor Branch C 2026-10-19 [reserve list via `reserve_releases.md` (insider-gaming); https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Contradicted across sources -- see notes]`

Smallest ecosystem set (lower bound): the same five as the Great Rift Valley (Grassland, Riverine, Dense Forest, Savannah, Swamp); the added Common Ostrich names Grassland, Savannah or Shrubland and Thomson's Gazelle names Grassland.
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Derived -- from requirements in this file; no source states an order]`

**Suggested setup order, Tanzania Reserve** (confidence low): as the Great Rift Valley order, with Common Ostrich and Thomson's Gazelle released at step 1 (Grassland) and no Meerkat at step 4.
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Derived -- from requirements in this file; no source states an order]`

### Poland Reserve (Temperate biome; late-game, puzzle-tier 2)

Releasable list (11 per `reserve_releases.md`): Brown Trout, Common Rudd, Eurasian Beaver, Eurasian Bittern, European Bison, Golden Eagle, Grey Wolf, Long-Eared Owl, Red Deer, White-Tailed Sea-Eagle, Wild Boar. games.gg lists 10 (no Eurasian Bittern) while its own table says 11, and states that taiga-only species such as the Eurasian Lynx and Mountain Hare cannot be released here.
_source: doctor Branch C 2026-10-19 [reserve list via `reserve_releases.md` (insider-gaming); https://games.gg/planet-zoo-2/guides/planet-zoo-2-all-wildlife-reserves-and-releasable-animals/] · capture: web_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Contradicted across sources -- see notes]`

Smallest ecosystem set (lower bound): **Pastures, Closed Canopy Forest, Open Canopy Forest, Lake (Temperate), and one of Lowland Marsh or Fen Wetland** (5). In the Temperate biome the Red Deer can only use Pastures (its other listing, Mixed Lowland Forest, is Taiga), the Long-Eared Owl only Closed Canopy Forest, the Wild Boar only Open Canopy Forest, the Grey Wolf only Flourishing Open Canopy Forest, the Eurasian Bittern Fen Wetland or Lowland Marsh, and the five water species Lake (Temperate).
_source: model analysis, doctor Branch C 2026-10-19 [ecosystem tables and species rows in this file] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Derived -- from requirements in this file; no source states an order]`

> **Cross-system dependency** -- see `../dependencies.md` DEP-028: a Gold objective for Flourishing ecosystems rests on releases that fill the ecosystems' roles.

**Suggested setup order, Poland Reserve** (confidence low):
1. Pastures (2 rows). Release Red Deer, European Bison.
2. Lowland Marsh (4 rows; chosen over Fen Wetland, which has 5 rows plus water). Release Eurasian Bittern.
3. Closed Canopy Forest (5 rows). Release Long-Eared Owl.
4. Lake (Temperate) (6 rows; ties Open Canopy Forest, goes first because it releases five species). Release Brown Trout, Common Rudd, Eurasian Beaver, Golden Eagle, White-Tailed Sea-Eagle.
5. Open Canopy Forest (6 rows). Release Wild Boar.
6. Make Open Canopy Forest Flourishing: Low Browsers (Red Deer), Terrestrial Seed Dispersers (Red Deer, European Bison), Terrestrial Spore Dispersers (Wild Boar), all already released.
7. Grey Wolf last (Flourishing Open Canopy Forest; Medium Prey and Small Prey filled).
_source: model analysis, doctor Branch C 2026-10-19 [rules 1-5 above applied to this reserve] · capture: browser_fetch · confidence: low · enemy-tier: 0 · puzzle-tier: 2 · category: mainline · spoiler: late-game_ `[Derived -- from requirements in this file; no source states an order]`

## Gaps (not read)

- The 95 species release pages not read (Established versus Flourishing and "either versus all" for their ecosystem rows; the prey-role fillers).
- Per-reserve ecosystem availability (only the biome is sourced).
- Starting condition of each reserve's ecosystems (the guide has no source saying whether any ecosystem comes pre-established).
- Size (area) requirements: the game shows an area requirement ("Too Small") but no source read gave numbers.

## Fill template -- player screenshots (reader or builder session: transcribe here)

Use this section when a player who owns the game gives you screenshots. It is the only place player screenshots are typed in; the Reserve ecosystem planner (`../artifacts/reserve_ecosystems.html`) reads these tables when `../artifacts/extract_ecosystems.py` and then `../artifacts/build_ecosystems.py` are run, and the matching "Not documented yet" notes on the page close. Nothing above this heading is edited to fill a gap.

**Which screens to ask the player for** (one capture per item; a capture of the whole game window is fine):
1. **A reserve's Ecosystems panel** (the Ecosystem Brush list): which ecosystems that reserve lets you paint, which are already Established when the reserve opens, and, with one ecosystem selected, its Area requirement. Fills Table A1 or A2.
2. **A species' Release Group requirements screen** (select the species in the reserve's Release Groups list): the Ecosystems Required rows (note "Either ... or ...", "Flourishing ..."), Species Roles Required, the research unlock, and the roles it fills once released. Fills Table B.
3. **A prey animal's Release Group screen with its Roles shown**, to learn who fills Medium Prey and Small Prey. Fills Table C.

**What to record.** Copy words as the game shows them. Ecosystem names must match the names in the biome tables above exactly. Put the capture date in the last column of every row. If a screenshot contradicts a row above, keep both: add the player row here and note the conflict in the changelog; do not edit the older row.

**Claim-format metadata.** Under each table that has rows, add one line in this shape (set the date; the puzzle-tier is 1 for Table A1, 2 for Table A2, 0 for Tables B and C):

```
_source: player screenshot 2026-11-02 · capture: screenshot · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none
```

Example rows (do not copy; they are placeholders):

```
Table A1: | <Reserve name> | Grassland, Riverine, Savannah | Grassland | Savannah: 2,400 m2 | 2026-11-02 |
Table B:  | <Species> | Either Savannah or Shrubland | none | Available without research | Small Prey, Soil Rooters | 2026-11-02 |
Table C:  | Medium Prey | <Species>, <Species> | 2026-11-02 |
```

### Table A1 -- Reserve ecosystems panel, chapter 1-3 reserves (puzzle-tier 1)

| Reserve | Ecosystems offered | Already Established at start | Area requirements seen (Ecosystem: size; ...) | Shot date |
|---|---|---|---|---|

### Table A2 -- Reserve ecosystems panel, chapter 4 reserves (puzzle-tier 2)

| Reserve | Ecosystems offered | Already Established at start | Area requirements seen (Ecosystem: size; ...) | Shot date |
|---|---|---|---|---|

### Table B -- Species release-group requirements (puzzle-tier 0)

| Species | Ecosystems Required (verbatim) | Species Roles Required | Release unlock | Roles it fills once released | Shot date |
|---|---|---|---|---|---|

### Table C -- Role fill lists (puzzle-tier 0)

| Role | Species that fill it | Shot date |
|---|---|---|
