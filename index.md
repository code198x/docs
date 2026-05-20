# Wiki Index

## Platforms
- [Commodore 64](platforms/c64.md) — ACME assembler, Docker toolchain, ROM symlinks from ~/Projects/Reference/
- [ZX Spectrum](platforms/spectrum.md) — pasmonext assembler, no ROMs needed, Emu198x for screenshots
- [Commodore Amiga](platforms/amiga.md) — vasm 68000, Kickstart ROM required (not distributable)
- [NES](platforms/nes.md) — ca65 + ld65 two-step build, linker config required

## Curriculum
- [Content model](curriculum/content-model.md) — platform → track → game → unit hierarchy, Astro collections, computed fields
- [Writing voice](curriculum/writing-voice.md) — warm/technical, British English, quality criteria, anti-patterns
- [Code samples](curriculum/code-samples.md) — CodeFromFile component, naming conventions, language detection
- [Revamp tracker](curriculum/revamp.md) — live status of the four-Game-1 commercial-bar revamp (Cadence, Nightshade, Exodus, Shadowkeep)
- [Lesson references](curriculum/lesson-references.md) — live catalogue of vault and pattern links from curriculum units; drives vault completeness work
- [Shadowkeep Phase 1 design](curriculum/shadowkeep-phase-1-design.md) — full design doc for the Spectrum priority-1 game: setting, 16-unit spine, cell vocabulary, room data format
- [Shadowkeep beeper spec](curriculum/shadowkeep-beeper-spec.md) — composition spec for the Spectrum title theme (1-voice beeper, ~30-60s loop)
- [Shadowkeep Unit 3 plan](curriculum/shadowkeep-unit-3-plan.md) — *The Hero Arrives*. Four-stage authoring plan: bitmap basics → stone-textured walls → hooded-thief sprite → cell preservation. Ready for a fresh session to execute.
- [C64 track skeleton](curriculum/c64-track-skeleton.md) — lightweight skeleton: North Star, 4 volume themes, ~16 candidate games. No per-game commit. Post-October. Awaits Spectrum methodology validation.
- [NES track skeleton](curriculum/nes-track-skeleton.md) — lightweight skeleton: North Star, 4 volume themes, ~16 candidate games. Post-October. NES needs most adaptation of Trunk Layers (no software-sprite era).
- [Amiga track skeleton](curriculum/amiga-track-skeleton.md) — lightweight skeleton: North Star, 4 volume themes, ~16 candidate games. Post-October. Amiga needs most reworking of methodology (68000 + custom chips fundamentally different from 8-bit).
- [Methodology generalisation survey](curriculum/methodology-generalisation-survey.md) — does the Spectrum methodology generalise to Apple II, Atari 8-bit, Game Boy, SNES, SMS, Mega Drive, BBC Micro, Dragon? Result: yes, across all 11 systems surveyed. No-commit pressure-test; not a roadmap.

## Infrastructure
- [Docker toolchains](infrastructure/docker-toolchains.md) — per-platform images, volume mount gotcha
- [Media capture pipeline](infrastructure/media-capture-pipeline.md) — screenshot / video / audio capture across the four platforms; current Spectrum SNA-based flow, legacy pipelines for the other three
- [Astro site](infrastructure/astro-site.md) — dev/build commands, content routing, collection gotchas

## Decisions
- [October 2026 launch spec](decisions/october-2026-launch-spec.md) — Spectrum-only, four artefacts at full bar, cut hierarchy, drift triggers
- [British English](decisions/british-english.md) — colour not color, exception for "program"
- [Seven repos](decisions/seven-repos.md) — why separate repos, git status gotcha
- [Commercial-bar revamp](decisions/commercial-bar-revamp.md) — Game 1s rewritten to "shippable in the era" bar, Phase 1 only
- [Real retro games (multi-disciplinary commitment)](decisions/real-retro-games.md) — code/visuals/audio/level/polish co-equal, mid-tier full-price target, drift triggers
- [Phase boundaries](decisions/phase-boundaries.md) — pedagogy sets sequence within a phase, commercial bar gates phase-end output
- [Constraint position](decisions/constraint-position.md) — three-tier taxonomy (period-faithful / period-possible / modern scene), declared per game, optionally per phase
- [Spiral and incremental](decisions/spiral-and-incremental.md) — incremental scaffold within phases, spiral progression across phases; Bruner's spiral applied to retro game dev
- [Curriculum structure](decisions/curriculum-structure.md) — 4 platforms × 4 games × 256 units; mid-tier full-price target; acceleration assumption load-bearing
- [Pattern Library](decisions/pattern-library.md) — populated from curriculum, technique-categorised; polish content decomposes into existing categories
- [Shadowkeep 32-unit commitment](decisions/shadowkeep-32-unit-commitment.md) — Arc 1+2 / 32 units for October; vertical-slice framing retired; three engine commitments. Extended by shadowkeep-four-arc-framing.
- [Shadowkeep four-arc framing](decisions/shadowkeep-four-arc-framing.md) — Arcs 3-4 post-October (Beyond the Walls / Heroes and Stories); per-unit refinements to Arcs 1-2; October scope unchanged
- [Spectrum BASIC 32-game lineup (v6.4)](decisions/spectrum-basic-32-games.md) — 32 games × 4 volumes × 8 per volume; v6.4 names applied
- [Spectrum BASIC v6.4 renames](decisions/spectrum-basic-v6.4-renames.md) — 11 BASIC games renamed under inspired-by-not-clones convention
- [Spectrum Assembly track structure](decisions/spectrum-assembly-track.md) — 44 entries across 6 volumes; three-axis design pattern; layer model (L0 + L+1 + L+3 + L+4a + L+4b); tech-tree with branches A-G; three cross-cutting axes
- [Spectrum Assembly per-game scope](decisions/spectrum-assembly-per-game-scope.md) — first-draft unit estimates for all 44 entries; total 2,396 units; cut hierarchy refined with scope; multi-decade shipping timeline
- [Inspired-by, not clones — naming convention](decisions/inspired-by-not-clones-naming.md) — every curriculum game is inspired by canon, not a clone; 10-principle convention; applies cross-track
