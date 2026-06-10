# Documentation Index

Project documentation lives entirely in `docs/`. This is the navigation map.

> **Source of truth for state:** what is shipped / in-progress / planned is read from the
> website module **catalogues** (`website/src/content/modules/<platform>/<track>.yaml`
> `status:`), `units.yaml`, the shipped files, and git — **not** from these prose docs.
> Planning prose is history and intent, not a live status claim. See
> [State lives in the catalogues](decisions/state-lives-in-catalogues.md).

## Top-level layout

- `decisions/` — binding policy records
- `specifications/` — formal specs (cross-cutting format/structure rules)
- `platforms/` — per-system reference + curriculum + games (16 systems)
- `tracker/` — plans, research, and design sketches (not live status — see banner above)
- `infrastructure/` — Docker, capture pipeline, Astro
- `emulators/` — emulator references
- `vault/` — encyclopedia of people, companies, games, techniques
- `log.md` — append-only event log

## Decisions (binding)

### Cross-cutting

- [October 2026 launch spec](decisions/october-2026-launch-spec.md) — all four core platforms, complete on-ramps at full bar (2026-06-09 amendment)
- [Real retro games](decisions/real-retro-games.md) — multi-disciplinary commitment (code/visuals/audio/level/polish co-equal)
- [Commercial-bar revamp](decisions/commercial-bar-revamp.md) — Game 1s rewritten to commercially-shippable bar
- [Curriculum structure](decisions/curriculum-structure.md) — 4 platforms × 4 games × 256 units (direction-of-travel)
- [Phase boundaries](decisions/phase-boundaries.md) — pedagogy sequences within, commercial bar gates phase ends
- [Constraint position](decisions/constraint-position.md) — period-faithful / period-possible / modern scene
- [Spiral and incremental](decisions/spiral-and-incremental.md) — incremental within phases, spiral across phases
- [Pattern library](decisions/pattern-library.md) — populated from curriculum, technique-categorised
- [Inspired-by, not clones (naming)](decisions/inspired-by-not-clones-naming.md) — 10-principle naming convention
- [British English](decisions/british-english.md) — colour, learnt, centre (exception: program)
- [Seven repos](decisions/seven-repos.md) — repo layout, git status gotcha
- [State lives in the catalogues](decisions/state-lives-in-catalogues.md) — `modules/*.yaml` + git are authoritative for status; prose carries why/intent, not state

### Website / IA

- [Systems, not platforms](decisions/systems-not-platforms.md) — "system" is the structural term (nav, URLs, collections, components); prose may use "platform"
- [System URL structure](decisions/system-url-structure.md) — system-rooted URLs, explicit track segment, no `/curriculum//learn/` prefix
- [System readiness lives in `tier`](decisions/system-readiness-lives-in-tier.md) — one field drives the fleet wall, homepage band, active/coming-soon and routing; no parallel `status`/`curriculumStatus`
- [Website design zoning](decisions/website-design-zoning.md) — character in the margins, legibility in the column; resolves "two winners" page types via template-vs-view
- [Visual direction: synthesise, don't pivot](decisions/visual-direction-synthesis.md) — production's bones + the fanzine's soul as one language; re-role Inter/Mono/Caveat, no new fonts

### Game lineups (per-track, 2026 replan)

- [Spectrum assembly — gentle ramp](decisions/spectrum-assembly-gentle-ramp.md) — governing record: the rendering ladder, technique budget, Shadowkeep re-scope
- [Spectrum BASIC 32-game lineup](decisions/spectrum-basic-32-games.md) — 32 games × 4 volumes; UDGs foundational; trig at Drift
- [C64 assembly lineup](decisions/c64-assembly-lineup.md) — VIC-II/6502 hardware ladder
- [C64 BASIC Volumes 2–4](decisions/c64-basic-volumes-2-4.md) — twin concept + POKE-the-hardware ladders
- [NES assembly lineup](decisions/nes-assembly-lineup.md) — PPU/6502 ladder; Dash re-scope; mappers late
- [Amiga assembly lineup](decisions/amiga-assembly-lineup.md) — custom-chip ladder; Exodus re-scope
- [Amiga AMOS + Blitz lineups](decisions/amiga-basic-amos-and-blitz.md) — peer-path BASIC fork

### Spectrum-specific

- [Shadowkeep 32-unit commitment](decisions/shadowkeep-32-unit-commitment.md) — Arc 1+2 / 32 units for October
- [Shadowkeep four-arc framing](decisions/shadowkeep-four-arc-framing.md) — Arcs 3-4 post-October
- [Spectrum BASIC v6.4 renames](decisions/spectrum-basic-v6.4-renames.md) — 11 BASIC games renamed under inspired-by-not-clones

## Specifications (formats and structures)

- [Curriculum](specifications/curriculum.md) — games model, unit structure, pedagogical approach
- [Unit](specifications/unit.md) — technical formatting for unit files
- [Brief](specifications/brief.md) — per-game brief format
- [Vault](specifications/vault.md) — encyclopedia structure
- [Pattern library](specifications/pattern-library.md) — reusable code patterns
- [Information architecture](specifications/information-architecture.md) — site URL structure
- [Content creation workflow](specifications/content-creation-workflow.md) — end-to-end process
- [Writing voice](specifications/writing-voice.md) — magazine-class, British English, anti-patterns
- [Content model](specifications/content-model.md) — Astro collections, computed fields
- [Code samples](specifications/code-samples.md) — CodeFromFile component, naming
- [Skill progression](specifications/skill-progression.md) — per-platform skill dependency maps
- [Graphics and audio coverage](specifications/graphics-and-audio.md) — per-platform A/V capability
- [BASIC languages overview](specifications/basic-languages-overview.md) — cross-BASIC reference

## Platforms

### Core platforms (live on-ramp + recorded lineup)

State is the website catalogue (`website/src/content/modules/<platform>/<track>.yaml`); each track's lineup + rationale is the per-track record under § Game lineups above.

- [Sinclair ZX Spectrum](platforms/sinclair-zx-spectrum/) — [reference](platforms/sinclair-zx-spectrum/reference.md), [games/](platforms/sinclair-zx-spectrum/games/) · Z80 assembly + Sinclair BASIC
- [Commodore 64](platforms/commodore-64/) — [reference](platforms/commodore-64/reference.md) · 6510 assembly + BASIC V2
- [Commodore Amiga](platforms/commodore-amiga/) — [reference](platforms/commodore-amiga/reference.md) · 68000 assembly + AMOS / Blitz BASIC
- [Nintendo NES](platforms/nintendo-entertainment-system/) — [reference](platforms/nintendo-entertainment-system/reference.md) · 6502 assembly

### Far-future drafts

Pre-methodology sketches for platforms outside the current 4. Awaits Spectrum methodology validation before any methodology investment.

- [Acorn Archimedes](platforms/acorn-archimedes/)
- [Amstrad CPC](platforms/amstrad-cpc/) — assembly + BASIC sketches
- [Atari 8-bit](platforms/atari-8-bit/)
- [Atari ST](platforms/atari-st/) — assembly + BASIC sketches
- [BBC Micro](platforms/bbc-micro/) — assembly + BASIC sketches
- [Game Boy](platforms/game-boy/)
- [MSX](platforms/msx/) — assembly + BASIC sketches
- [Sega Master System](platforms/sega-master-system/)
- [Sega Mega Drive](platforms/sega-mega-drive/)
- [SNES](platforms/snes/)
- [TurboGrafx-16](platforms/turbografx-16/)
- [Vectrex](platforms/vectrex/)

## Tracker (live state / plans)

- [Lesson references](tracker/lesson-references.md) — vault/pattern links from curriculum units; drives vault completeness work
- [Methodology generalisation survey](tracker/methodology-generalisation-survey.md) — does the Spectrum methodology generalise to 11+ systems?
- [Future expansion tracks](tracker/future-expansion-tracks.md) — post-capstone (MEGA65, ZX Next, AGA)

## Infrastructure

- [Docker toolchains](infrastructure/docker-toolchains.md) — per-platform images, volume mount gotcha
- [Media capture pipeline](infrastructure/media-capture-pipeline.md) — screenshot / video / audio
- [Astro site](infrastructure/astro-site.md) — dev/build commands, content routing, collection gotchas
- [Site testing](infrastructure/site-testing.md) — Playwright e2e, axe a11y + baseline, Lighthouse budgets
- [Emu198x HALT investigation brief](infrastructure/emu198x-halt-investigation-brief.md) — emulator bug investigation
