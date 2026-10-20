# Planet Zoo 2 -- Limitations & Blocked Sources

Sources I found that look useful but couldn't fully fetch -- paywalls, Cloudflare, age gates, video-only content, etc. URLs preserved so the player (or another contributor) can open them in a real browser.

## How to read this file
- Each entry: topic, URL, block type, what I could glean, best alternative I did get to.
- Each per-topic file (in `puzzles/`, `[areas]/`, `items/`, `sections/`) also lists its own blocked sources at the bottom -- the player rarely needs to come hunting here.
- This file is the catch-all for sources that didn't fit a specific topic.

## Block types
- **paywall** -- content gated behind a subscription or article limit
- **cloudflare** -- Cloudflare bot challenge / 403 / 503 from WebFetch
- **video-only** -- YouTube or other video where the answer is shown visually; no readable text equivalent
- **age-gate** -- content blocked behind age verification
- **cookie-wall** -- popup or consent flow that broke the fetch
- **search-snippet-only** -- search engine returned a snippet but the page itself wasn't reachable
- **dead-link** -- URL was in another source but no longer resolves

- **robots-restriction** -- the external research runtime reports a robots access restriction
- **terms-restriction** -- a stated retrieval restriction was reported; preserve the actual evidence
- **javascript-dependent** -- useful content requires page execution the available tool did not perform
- **login-required** -- a signed-in session is required
- **access-not-checked** -- no content/access check was performed; never call this robots-blocked

## Companion tools

For every useful map, tracker, database or completion tool supplied, recalled or found:

- Name and URL if verified (otherwise mark unknown/unverified)
- Apparent coverage, evidence for it, and uncertainty; unread coverage is not confirmed game data
- Reason not read, access-check result, policy evidence if available, and check date
- How a person could use it, best readable alternative, and wider-spoiler warning where relevant

Merge repeated URLs with dated evidence retained. Read tools can also be recorded here when they offer a useful location fallback. Record an honest empty statement when no candidates were found; do not imply exhaustive discovery.

- No Planet Zoo 2 interactive map or collectible tracker was found by one combined search on 2026-10-19 ("Planet Zoo 2 interactive map collectible tracker"), by four searches at P1, or by P2. This is not proof none exists; the game launched 2026-10-13 and has no world map and no collectible-hunting loop in scope. Access status: not checked for the setup search.
- **Wikily Planet Zoo 2 Wiki** -- https://wikily.gg/planet-zoo-2 -- Zoopedia mirror (136 species, housing filters), a **Barrier planner** tool, Career level tables, research trees, achievements, an "Ask Wikily" beta, Planet Hub region globe; languages EN, DE, FR, RU, JA, PT-BR (PL seen only as a search snippet). Evidence: navigation counts on every page. Access 2026-10-19: WebFetch 403; read through a headless browser (P1) and camoufox-fetch (P2). Use: Career objectives, unlock tables, research. Caveat: level pages render only the Bronze objective tab as text; Silver and Gold tabs need a click in a browser. Wiki counts were edited after launch.
- **TheGamesWiki Planet Zoo 2** -- https://thegameswiki.com/planet-zoo-2/wiki/ -- Animals and Welfare page read (updated 18 Oct 2026); dated Zoopedia catalogue; "Track in playthrough" feature; its game-modes page is marked incomplete and was not read. Access: WebFetch 429; headless browser ok. Pages say they are drafted with AI assistance and editorially reviewed.
- **Whisper of the House Planet Zoo 2 guides** -- https://www.whisperofthehouse.com/planet-zoo-2 -- hub and chapter 1-4 walkthroughs read (P2), including Silver and Gold goals for some levels; an interactive "All 39 Achievements Checklist" exists, not read (name only). Use: chapter walkthroughs, achievement checklist.
- **planetzoo-2.wiki** -- https://planetzoo-2.wiki/guide/walkthrough/ -- fan wiki, one walkthrough page read (P2), consistent with other sources. **planet-zoo2.wiki** -- one page read, low reliability (see `mechanics.md` source cautions).
- **Official Zoopedia** on the Planet Zoo website -- published before launch per TheGamesWiki -- not read; URL not captured.
- **PlatPursuit trophy page** -- https://platpursuit.com/games/402959/ -- seen in search, not read; apparent coverage: trophies.
- **Frontier Issue Tracker / official forms** (app.formcrafts.com/planetzoo2) -- referenced in the Reddit launch thread; not read. **Steam Workshop for blueprints/zoos** -- not read. **Nexus "QuickSave" mod** -- first game only.
- First-game fan planning spreadsheet thread on the Frontier forums -- supplied by the brief; not read; first game only.

## Entries

### Dekudeals / Digital Citizen -- release and edition details
- Source: https://www.digitalcitizen.life/planet-zoo-2-launches-october-13-with-steam-preloading-available-now/
- Block type: cloudflare (HTTP 403 from WebFetch, 2026-10-19)
- Why I think it has the answer: launch-date and edition coverage.
- What I could glean before the block: search-result snippets only (October 13, 2026 launch, Steam preloading).
- Best alternative I did get to: official site `https://www.planetzoogame.com/en-US/2/game-modes` (read via a headless browser tool).

### Planet Zoo Wiki (Fandom) -- Kai Brooks character page
- Source: https://planetzoo.fandom.com/wiki/Kai_Brooks
- Block type: javascript-dependent / fetch timeout (402 from WebFetch; 100 s timeout from headless browser, 2026-10-19)
- Why I think it has the answer: character role and personality for the persona.
- What I could glean before the block: role only (marine biologist at FEN), from a search result.
- Best alternative I did get to: `persona.md` marks Kai's voice as role-derived, not sourced.

### Exophase -- Planet Zoo 2 Steam achievements
- Source: https://www.exophase.com/game/planet-zoo-2-steam/achievements/
- Block type: cloudflare (HTTP 403, 2026-10-19)
- What I could glean before the block: nothing beyond the search snippet (39 achievements).
- Best alternative I did get to: vgtimes.ru Steam list (names), stored in `research_briefs/achievement_stubs.md`.

### P1 / P2 sources found but not read (2026-10-19)
Reasons: tool budget, refused at the tool-permission step, timed out, or a duplicate. None of these supplies confirmed facts. Block type for fetch failures: javascript-dependent / access-not-checked unless shown.
- https://wikily.gg/planet-zoo-2/ecosystems and /staff -- 32 ecosystems, 6 staff types (navigation counts) -- reads refused at the tool-permission step, not retried. Use: ecosystem requirements, staff roles.
- Wikily Silver/Gold tabs on the Career level pages -- tabs not rendered as text. Use: click the tabs in a browser.
- https://powerupgaming.co.uk/2026/10/14/planet-zoo-2-career-mode-guide-tips-for-gold/ -- Gold strategy (search excerpt); https://primagames.com/gaming/planet-zoo-2-which-game-mode-first and Prima "Thriving", "Franchise Accreditation", "Co-Habitable Animals" articles; https://gamerant.com/accreditation-planet-zoo-2/ ; https://gamerblurb.com/guides/planet-zoo-2-accreditation-guide ; games.gg Franchise Accreditation Explained and beginners guide -- would raise the number of independent sources for the Accreditation and Franchise gates. Use: cross-check tiers; cohabitation table.
- https://powerupgaming.co.uk/2026/10/15/planet-zoo-2-aquarium-guide-build-fix-waterlogged-terrain/ ; https://gamerblurb.com/guides/planet-zoo-2-aquarium-guide ; https://gamerblurb.com/guides/planet-zoo-2-how-to-change-water-salinity ; https://www.dtgre.com/2026/10/planet-zoo-2-water-filter-not-powered-fix.html -- aquarium salinity, filtration, power (search excerpts). Use: confirm the aquarium leads marked Hypothesis.
- https://games.gg/planet-zoo-2/guides/planet-zoo-2-beginners-guide/ ; https://insider-gaming.com/planet-zoo-2-beginners-guide/ ; https://www.itechguides.com/planet-zoo-2-beginners-guide-7-tips-to-get-started/ ; https://allthings.how/?p=267761 (and 267765, 267772, 267822; flagged low quality) -- beginner tips.
- https://www.gaming.net/planet-zoo-2-best-workshop-blueprint-types/ ; https://thegameswiki.com/planet-zoo-2/wiki/frontier-workshop -- Workshop limits.
- https://gamingbolt.com/?p=654886 ; https://games.gg/news/planet-zoo-2-update-1-0/ -- second copy of the 1.0.4 notes; the Wikily news item "Planet Zoo 2 Update 1.0.5" (16 Oct 2026) -- no URL captured, notes not found. Use: current-patch changes.
- https://www.gamestar.de/videos/planet-zoo-2,16994_138/ -- German video, no transcript tool. https://esports.ru/igrovaya-industriya/news/planet-zoo-2-vyshla-podrobnosti/ -- Russian launch news. https://www.jeuxvideo.com/jeux/jeu-2108571/ -- French page, no test found. https://wikily.gg/ja/planet-zoo-2/career%2Feast-africa and https://wikily.gg/pl/planet-zoo-2/career/sumatra-reserve -- Japanese and Polish locales of Wikily (P2 read DE, FR, RU, JA, PT-BR pages of the same wiki; they are not independent).
- Reddit r/PlanetZoo: P2 read the launch-day mega thread (80 comments, partial, via reddit-reader plus a camoufox read of the thread shell); its "Questions - Day 2 Megathread" (213 comments) and "Thanks & an update on Franchise Mode" were not read (reader rate limit). P1 found no Planet Zoo 2 thread (Steam threads returned were the first game's, app 703080).
- YouTube pages opened for titles and descriptions only, no transcript reachable: Trophygamers "<Chapter 2 level> - All Medals" (2:55:40), Leaf "Let's Beat the Career Mode" (59:34), Hazcub "Unlocking Tier 3" Part 5, GameRiot Chapter 2, MySpaceGuide "Career Mode Explained" (1:24), Bazzy (a Chapter 2 level) part 2, Trophygamers Chapter 2 (48:48). Video class (c) is NOT met for any topic.

### Unresolved research conflicts and gaps (carried from P1 + P2)
- Deluxe Edition species list: settled by the doctor pass of 2026-10-19 (Golden Eagle is Deluxe, the Rattlesnake is base; three sources, see `animals/roster.md`).
- Release rule: reserve-only vs quick release (see `animals/welfare_breeding_release.md`).
- Chapter-4 opener unlock: the last Chapter 3 level's Bronze vs Tier 4 (12 Bronze, 2 Silver) (level name in `sections/career_progression.md`, late-game block).
- Hub travel medal conditions: 2 medals for the Chapter 1 zoo and 5 for a Chapter 2 zoo vs the level pages' Bronze rules.
- Per-tier species counts: Career 33 / 38 / 35 / 30 vs Franchise 32 / 33 / 31 / 30 / 10.
- "Follow Me!" achievement trigger: Educational Tour vs "an educational tool for kids".
- Missing: per-species habitat requirements for all 130 species; Silver and Gold objectives for most levels; settings tab names; colourblind, UI-scale, subtitle options; gamepad layout; recommended remaps; number of Sandbox maps; Franchise map count and second-zoo price; Hub menu path and save menu paths; autosave interval; what a failed scenario loses; achievement hidden flags; Update 1.0.5 notes; the one unlocated base species.

### Achievement hidden flags (doctor run 2026-10-19)
- No readable source states whether any of the 39 Steam achievements is hidden. The framework's claim format and achievement entry format allow only `yes | no` and say nothing about an unknown flag, so every entry is set to `hidden: yes` (the spoiler-safe value that gates the name); the overlay claims carry `achievement-hidden: yes`.
- Checked: Steam's own achievement list (steamcommunity.com/stats/3219030/achievements; store app 3219030) loaded 26 of 39 entries with names and full descriptions and no hidden marker, but it states nothing about hidden status and the other 13 did not load; the Gamesplanet Steam-list mirror, games.gg, GamerBlurb and allthings.how list all 39 without any hidden marking; the sources read at ingestion (Wikily, Insider Gaming, Destructoid) gave no flag. Not readable: SteamHunters (Cloudflare block).
- To close the gap: a person with the game, or a source that marks Steam's hidden flag, sets each entry to `yes` or `no` (a `no` means the name no longer gates).

## Always-blocked categories

[Things no source can give us -- e.g. randomized content per save (if applicable), visual-only puzzle solutions where text guides don't exist, in-game UI elements that aren't documented anywhere. None identified yet for this game.]
