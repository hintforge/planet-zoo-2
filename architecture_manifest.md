# Planet Zoo 2 -- Architecture manifest (nav skipped)

**status:** research-integrated <!-- scaffold | research-integrated | live-observed | reconciled -->
**last_reconciled:** 2026-10-19
**research_run:** P1 + P2 2026-10-19

Root manifest for a sanctioned nav-skip corpus (Stage 0 game-type signal: narrative-no-nav; localization class: none). The five spatial primitives (zone graph, chapter-zone mapping, optional content, support topology, locks and keys) are intentionally absent, not missing.

## Hintforge manifest

```
corpus-core-version: 6
game-version: "latest"
game-version-platform: "PC / Steam"
game-version-as-of: 2026-10-19
vector-extensions: animals
```

## Vector extensions

- `animals/` -- corpus-declared extension: species care, habitat needs and welfare facts, one file per species or species group, indexed by `animals/index.md`

## Zone Graph

**Game-type label:** narrative-no-nav (closest available label; the game is a zoo-management sim, see `research_briefs/stage0_priors.md`). P1 re-checked it: the structure is a hub with spokes (the Planet Hub menu opens each site as a separate level; Career sites unlock by medal count, not traversal), so no label fits well and `narrative-no-nav` is kept for routing. The zone graph lives in `sections/career_progression.md` (model recommendation, P1 result 2026-10-19).
**Localization-mechanism class:** none (kept). P1 recommended `none` for zoos and `landmark` for Wildlife Reserves (a compass to fixed buildings and player-placed Observation Platforms); P2's brief asked for no localization toolkit, so no `nav/localization.md` was written (model recommendation, P1 result 2026-10-19; open thread in `CHECKPOINT.md`).
**Source-language set:** English (developer, UK); German, French, Russian as the non-English source floor. Read at P1: Gameswelt (German), Xboxygen (French), SecurityLab.ru blog (Russian); at P2 the DE, FR, RU, JA and PT-BR pages of Wikily (the same wiki, not independent). Spanish, Italian and Japanese editorial sources were not searched.
