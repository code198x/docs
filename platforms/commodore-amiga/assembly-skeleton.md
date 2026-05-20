# Commodore Amiga Track — Lightweight Skeleton

**STATUS: Post-October work, lightweight only.** Per `docs/decisions/october-2026-launch-spec.md`, Amiga / Exodus is deferred. This skeleton is *no-commit* — North Star, volume themes, candidate game lineup only. No per-game scope, no naming lock-in, no tech-tree detail. Awaits Spectrum methodology validation before becoming a full track structure.

Captured 2026-05-19 alongside [c64-track-skeleton.md](c64-track-skeleton.md) and [nes-track-skeleton.md](nes-track-skeleton.md) for cross-platform methodology check.

## North Star

The Amiga teaches the *16-bit revolution* — what becomes possible when you cross from 8-bit constraints to 16-bit ambition. Where Spectrum / C64 / NES were 8-bit machines with 8-bit assembly (Z80 / 6502 / 6502 derivative), **Amiga is 16/32-bit Motorola 68000** — a fundamentally different CPU with a different assembly language and a different design model. Custom chips (Agnus, Denise, Paula) hardware-accelerate graphics and audio. The Copper is a programmable display-list co-processor running alongside the CPU. The Blitter is a dedicated graphics-blit chip. Sampled audio replaces synthesised. 32-color palettes (HAM mode goes to 4096) replace 16-color or 8-color. Multi-tasking Workbench OS coexists with games. Memory budgets are an order of magnitude larger.

Exodus (Game 1, concept locked per [revamp.md](revamp.md) — Lost Vikings + 3 creatures concept) is the canonical demonstration.

## Volume themes (working-draft)

| Volume | Theme | What it teaches |
|--------|-------|-----------------|
| **V1** *The Custom Chip Family* | Foundational | Blitter, Copper, Paula, hardware sprites, 32-color palette, sampled audio |
| **V2** *Bitmap Brothers and Sensi* | Action with 16-bit fidelity | Speedball II / Cannon Fodder / Sensible Soccer tradition |
| **V3** *Cinematic Adventures* | Presentation-led | Shadow of the Beast / Defender of the Crown / Another World tradition |
| **V4** *Simulators and Systems* | Deep / system | Bullfrog (Populous, Syndicate), Lemmings, Worms, F/A-18 |

## Candidate games (~16, working-draft)

| # | Working name / placeholder | Canonical tradition |
|---|----------------------------|---------------------|
| 1 | **Exodus** (concept locked — Lost Vikings + 3 creatures) | TBD per concept doc |
| 2 | [Cinematic Action] | Shadow of the Beast (Psygnosis / Reflections 1989) |
| 3 | [Brutal Sport] | Speedball II (Bitmap Brothers 1990) |
| 4 | [Top-Down Combat] | Cannon Fodder (Sensible 1993) |
| 5 | [Top-Down Football] | Sensible Soccer (Sensible 1992) |
| 6 | [Puzzle Action] | Lemmings (DMA / Psygnosis 1991) |
| 7 | [Turn-Based Artillery] | Worms (Team17 1995) |
| 8 | [Cinematic Strategy] | Defender of the Crown (Cinemaware 1986) |
| 9 | [3D Driving] | Stunt Car Racer (Crammond 1989) |
| 10 | [Pinball Sim] | Pinball Dreams / Fantasies (Digital Illusions 1992) |
| 11 | [Cinematic Action-Adventure] | Another World (Eric Chahi / Delphine 1991) |
| 12 | [Vector Flight Sim] | F/A-18 Interceptor (EA 1988) |
| 13 | [Action Platformer] | Turrican II (Trenz / Factor 5 1991) |
| 14 | [God Game] | Populous (Bullfrog 1989) |
| 15 | [Vertical Shooter] | Battle Squadron (Innerprise 1989) |
| 16 | [Point-and-Click Adventure] | Beneath a Steel Sky (Revolution 1994) |

Plus possible additions: Syndicate (Bullfrog), The Chaos Engine (Bitmap Brothers), Pinball Illusions, Megalo-Mania (Imagineer), Settlers (Bluebyte).

## Methodology generalisation check (Spectrum → Amiga)

| Spectrum element | Translates to Amiga? |
|------------------|----------------------|
| **Trunk Layers 1-4** | **Substantially different** — Amiga's foundations are Blitter + Copper + Paula, not framebuffer + ULA + beeper. 68000 assembly is a different language entirely. Trunk Layers need reframing for 16-bit + custom chips: Layer 1 might be "the custom chip family"; Layer 2 might be "Blitter operations"; etc. |
| **Branch A** (Adventure Depth) | Yes — Beneath a Steel Sky, point-and-click tradition |
| **Branch B** (Platformer) | Yes — Turrican II, Lionheart, Switchblade |
| **Branch C** (Scrolling and Density) | Hardware-supported via Copper + dual-playfield. Different teaching (parallax becomes hardware, not software) |
| **Branch D** (Real-World Sim) | **Bigger on Amiga** — sport / sim was a defining tradition (Speedball, Sensi, F/A-18, Stunt Car Racer, Pinball Dreams) |
| **Branch E** (True 3D) | Limited but real — Stunt Car Racer, F/A-18, F1GP. Less prominent than C64 in proportion. |
| **Branch F** (Cross-cutting Specials) | Different content — Workbench integration, AmigaDOS, Multi-tasking concerns |
| **Branch G** (Audio Hardware) | **Different content** — Paula 4-channel stereo samples replace synth. Sample-based composition is a different art entirely. |
| **Three cross-cutting axes** | Engineering Practices content is **most different of the four platforms** — 68000 assembly idioms, Blitter programming, Copper list authoring are not Z80/6502-style. Production Craft includes ADF disk authoring, IFF formats, AmigaDOS integration. |
| **Layer model** | Different — Amiga 500 / 600 / 1200 / 4000 variants. AGA chipset (1200+) is a real native-vs-enhanced layer like the 128K / Next split. L+1 could be AGA enhancement; L+4 could be modern Amiga scene (Vampire, MiniMig). |
| **Naming convention** | Yes — applies universally |
| **Inspired-by-not-clones** | Yes — applies universally |

**Methodology generalises conceptually but Amiga needs the most reworking of the three.** The 68000 + custom-chip foundation is genuinely different from 8-bit + framebuffer. Trunk Layers 1-4 may need full reframing rather than direct translation. Branch D is more prominent. Branch G (audio) is sampled-not-synth — different teaching model. Branch E (3D) and Branch G (audio) are where Amiga's identity lives most.

## What this skeleton does NOT commit to

(Same as C64 — see [c64-track-skeleton.md](c64-track-skeleton.md))

## Status

Skeleton — captured 2026-05-19. Post-October work. No commitment. Awaits Spectrum methodology validation before becoming a full track structure document. **Amiga will need the most adaptation work** when this skeleton becomes a full structure — flagged here as the largest expected delta from the Spectrum methodology.
