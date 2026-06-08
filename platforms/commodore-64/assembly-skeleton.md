# Commodore 64 Track — Lightweight Skeleton

**STATUS: Opening committed (2026-06-03); the deeper track stays lightweight.** The precondition this skeleton was waiting on — *Spectrum validating the gentle-ramp methodology* — is met: Meet the Machine and a complete Gloaming have shipped. Per the [October 2026 launch spec](../../decisions/october-2026-launch-spec.md) (2026-06-03 amendment), C64 is now the **second platform brought to the finishable bar**, and its launch opening is committed: a C64 **Primer** + **Starfield** as the first complete game (see § Committed opening). Everything *beyond the opening* — the flagship (Cadence), V2–V4, the full ~16-game lineup, per-game scope, naming lock-in, tech-tree — stays **lightweight / no-commit**, as before. North Star, volume themes, and the candidate lineup remain working-draft.

Captured 2026-05-19 alongside [nes-track-skeleton.md](nes-track-skeleton.md) and [amiga-track-skeleton.md](amiga-track-skeleton.md) for cross-platform methodology check.

## North Star

The C64 teaches the *commercial 8-bit game in its fullest form*. Where Spectrum taught what you can do with bytes, attribute clash, and a beeper, **C64 teaches what you can do when the hardware is *generous***: 8 hardware sprites, true multi-color graphics, a 3-voice SID synthesiser with filters and envelopes, raster interrupts for split-screen tricks, and 64K to spend. The same legends crossed both platforms (Crow, Braybrook at Hewson; later Smith, Galway, Hubbard) but C64's design vocabulary is *different*. Hardware sprites change masking and Y-sort. SID is a completely different audio paradigm from beeper or AY. Multi-color graphics change pixel-art constraints. Disk loading replaces tape conventions.

Cadence is the canonical demonstration — the **flagship**, concept locked. Under the gentle ramp it sits where Shadowkeep does on the Spectrum: the ambitious showcase, *off* the finishable-opening critical path and deferred. The game a learner actually *finishes* first is the smaller **Starfield**, reached via the Primer — see § Committed opening.

## Committed opening — the finishable bar (2026-06-03)

Validated on the Spectrum, applied here. The C64 launch opening is two artefacts, both at the full Definition-of-Done bar:

1. **The C64 Primer ("Meet the Machine")** — machine literacy, not a game: the 6502, the C64 memory map, and the character screen with its colour RAM — one idea at a time, before you build a thing. Hardware sprites and SID are deliberately held back for Starfield, exactly as the Spectrum primer leaves sprites and sound to its games. New authoring; C64 has had no on-ramp until now.
2. **Starfield — the first complete game you finish.** The single-screen hardware-sprite shooter already started (~16 real units, "Ship on Screen" → "Screen Edges", with code samples). Re-scoped to exactly those units — the 112 auto-generated stub units dropped from the catalogue — finished to the bar and marked `complete`. This is the C64's Gloaming.

The bar is **Primer → Starfield**: "a real game you finish" on a second machine. The flagship (Cadence) and the rest of the lineup below follow afterwards, exactly as Shadowkeep's later arcs do on the Spectrum.

### Meet the Machine (C64 Primer) — committed shape (decided 2026-06-03, a *flexible* lock)

The C64 on-ramp. Same name as the Spectrum primer on purpose: **"Meet the Machine" is the universal on-ramp across every platform** — a teaching module (not a game), so exempt from the inspired-by game-naming rule. The content shares nothing with the Z80 version; the name is the signpost.

**15 units, 4 phases, mirroring the Spectrum primer beat-for-beat**, with the C64's own concepts where the machine diverges:

- *What the machine is* — 1 Assemble and Run (toolchain loop **+ the BASIC `SYS` stub**) · 2 LDA Is Not LET (A/X/Y are physical registers) · 3 Everything Is a Number · 4 A Street of Numbered Boxes (64K; **zero page** named here as the fast first block) · 5 The Screen Is Memory (`$0400`) · 6 Colour Is a Separate Map (`$D800` — the C64's attribute parallel).
- *What it can do* — 7 Test, Then Jump (`CMP` + `BEQ`/`BNE`/`BCC`/`BCS`) · 8 The Machine Can Hear You (read the **joystick** port `$DC00`) · 9 A Finger on the Boxes (**indexed** addressing `,X` — true indirect-indexed pointers defer to Starfield) · 10 The Counted Loop (`inx`/`cpx`/`bne` — count-up, for clarity; the leaner count-down-to-zero deferred to a later game) · 11 Call, Return, and a Stack You Can See (`JSR`/`RTS`, the page-1 stack).
- *Rounding out* — 12 Adding and Taking Away (`ADC`/`SBC` **+ the `CLC`/`SEC` carry rule**) · 13 Working With Bits · 14 Bigger Than a Byte (**16-bit by hand** — no 16-bit registers; carry chained across two bytes).
- *The mindset* — 15 The Machine Trusts You (no safety net; debugging via the VICE monitor).

**Deliberately out, mirroring the Spectrum primer's scope:** hardware sprites and SID. The Spectrum primer teaches the screen and its colour but never sprites or sound — those are game concepts. So here too, Starfield owns sprites (its Unit 1) and SID (its Unit 5).

**Where the C64 earns its keep (not transliteration):** the BASIC stub (1), the `CLC`/`SEC` carry discipline (12), and 16-bit-by-hand (14) — real 6502-isms with no Z80 equivalent.

**Flexible lock.** 15 is the committed scope, but the count flexes *at authoring time*. Phase 3 is the likeliest split point — the carry rule (12) and 16-bit-by-hand (14) carry difficulty the Z80 versions didn't. If a concept won't sit gently in one unit when written, split it then; discover the shape by writing, not by guessing. The budget is on concepts-per-unit, never on the count.

### Starfield — committed shape (decided 2026-06-03)

Scoped with the same concept-budget discipline as Gloaming — minimise the concepts introduced.

- **Concept budget: two majors, the second trimmed.** The load-bearing major is **VIC-II hardware sprites** (ship, bullet, enemies all live under it). The second is **indirect-indexed addressing** (zero-page pointers + a row lookup table), kept because it's core 6502 and the only way to move the character-stars — sprites are too scarce to spend on a starfield. The **multi-layer parallax** starfield is *kept and expanded* — **decided 2026-06-04, reversing the 2026-06-03 single-speed cut.** Target **three depth layers** (close / mid / far at full / half / quarter frame-rates, white → grey → dark-grey), with a stretch to **four** if star density supports it (the current 8 stars want bumping — 2 per layer is sparse — plus a fourth grey). It stays a *flourish, not a third major*: it introduces no new technique (a frame counter + an every-Nth-frame skip, both already known), and the depth is precisely what makes a *starfield* read as more than flat dots. No new units; the finishable bar is unaffected. Collision stays in **software** (8-bit distance compare), deliberately *not* the VIC-II hardware collision registers. SID is **SFX only** — no envelopes/filters here.
- **16 units, the "Ignition" phase.** Complete game loop: shoot, score, die, restart. The 128-unit scaffold (112 stub units + the Fleet/Firepower/Incoming/Stardust/… expansion phases) has been dropped from the catalogue.
- **Canonical order** (Title Screen last, bookending the finished game as Gloaming does): Ship on Screen → Joystick Movement → **Screen Edges** → Fire Button Shoots → Laser Sound → Enemy Appears → Direct Hit → Explosion → Scoring Points → Enemy Waves → Player Death → Game Over → Three Lives → Life Lost Flash → Starfield → Title Screen.
- **Frame-pacing:** the main loop is raster-line-paced (the Starfield equivalent of Gloaming's "Heartbeat" unit) so motion runs at a steady frame rate, not at raw CPU speed.

**Deferred expansion (sketch, for later — not committed):** The Fleet (multiple enemy types) → Firepower (power-ups) → Incoming (enemies shoot back, raster-IRQ timing) → Stardust (custom chars, multicolour sprites, raster effects) → Waveform → Command → Launch. This is the Starfield equivalent of Shadowkeep's later arcs.

## Volume themes (working-draft)

| Volume | Theme | What it teaches |
|--------|-------|-----------------|
| **V1** *The Hardware Speaks* | Foundational | Hardware sprites, SID basics, raster — what makes the C64 not-a-Spectrum |
| **V2** *Speed and Density* | Real-time arcade | Uridium / Hewson tradition — smooth scrolling, dense art |
| **V3** *The Multi-color World* | Visual mastery | IK+ / Last Ninja / Cinemaware presentation |
| **V4** *Systems and Stories* | Depth | Paradroid / Impossible Mission / RPG / strategy |

## Candidate games (~16, working-draft)

Names are stand-ins for inspired-by-not-clones renames. Canonical references named for tradition only; per-game design follows after Spectrum validates the methodology.

| # | Working name / placeholder | Canonical tradition |
|---|----------------------------|---------------------|
| 1 | **Cadence** (concept locked) | TBD per concept doc |
| 2 | [Hover-Droid Action] | Paradroid (Braybrook / Hewson 1985) |
| 3 | [Cave Physics] | Boulder Dash C64 |
| 4 | [Power-Up Shooter] | Wizball (Sensible / Hewson 1987) |
| 5 | [Smooth-Scroll Shooter] | Uridium (Braybrook / Hewson 1986) |
| 6 | [Iso Adventure-Combat] | The Last Ninja (System 3 1987) |
| 7 | [Beat-em-up] | IK+ (Maclean / System 3 1987) |
| 8 | [Cinematic Strategy] | Defender of the Crown (Cinemaware 1986) |
| 9 | [Exploration Platformer] | Impossible Mission (Epyx 1984) |
| 10 | [Action Platformer] | Turrican (Trenz / Rainbow Arts 1990) |
| 11 | [3D Strategic] | The Sentinel (Crammond 1986) |
| 12 | [Point-and-Click Adventure] | Maniac Mansion (LucasArts 1987) |
| 13 | [Single-Screen Platformer] | Pitfall II (Activision 1984) |
| 14 | [Atmospheric Horror-Action] | Forbidden Forest (Cosmi 1983) |
| 15 | [Trading / Space] | Elite C64 port (1985) |
| 16 | [Economic Sim] | M.U.L.E. (Ozark 1983) |

Plus possible additions: Pinball Construction Set (Budge), Cauldron II C64, Bruce Lee (Datasoft), Aztec Challenge (Cosmi).

## Methodology generalisation check (Spectrum → C64)

| Spectrum element | Translates to C64? |
|------------------|---------------------|
| **Trunk Layers 1-4** (foundations / sprite / world / inhabitants) | Yes, with hardware-sprite caveat — Layer 2 (The Sprite) teaches hardware sprites first, software sprites secondarily |
| **Branch A** (Adventure Depth) | Yes — Last Ninja, Impossible Mission, RPGs |
| **Branch B** (Platformer) | Yes — Turrican, Bruce Lee, Pitfall II |
| **Branch C** (Scrolling and Density) | Yes — C64 has hardware scrolling, different teaching |
| **Branch D** (Real-World Sim) | Yes — sport/sim games |
| **Branch E** (True 3D) | Yes — Elite, Sentinel, Mercenary |
| **Branch F** (Cross-cutting Specials) | Yes — parser, iso, procedural |
| **Branch G** (Audio Hardware) | **Different content** — SID replaces AY+128K. Would be a C64-specific Branch G (or "Branch G: SID"). |
| **Three cross-cutting axes** (Design / Engineering Practices / Production Craft) | Yes; Engineering Practices content is 6502-specific (different from Z80 LDIR/T-state idioms) |
| **Layer model (L0 / L+1 / L+3 / L+4)** | Different — C64 has no native-vs-128K layer split. Possible L+1 = REU expansion / cartridge variants. L+4 (Next equivalent) = C64 Reloaded / Mini, C128 variants |
| **Naming convention (inspired-by, not clones)** | Yes — applies universally |
| **Tier hierarchy** | Yes — tier per platform |

**Methodology generalises conceptually; content per axis is C64-specific.** No major framework gaps; the structure transfers. Per-platform variation lives in Branch G (audio), Engineering Practices (CPU), and layer model (no L+1 128K parallel exists).

## What this skeleton does NOT commit to

- Per-game scope / unit budget
- Final naming (the placeholders are stand-ins)
- Tech-tree per-game position
- Cross-game prerequisite seeding
- Cut hierarchy
- Build order or timeline

These remain uncommitted **for the games beyond the opening**. Spectrum's first games have now shipped and validated the methodology, so the opening (Primer + Starfield) is committed in § Committed opening above; the deeper lineup still awaits per-game design.

## Status

Captured 2026-05-19 as a no-commit skeleton. **Opening committed 2026-06-03** — the Spectrum validated the gentle-ramp (Meet the Machine + a complete Gloaming shipped), so the C64 launch opening (Primer + Starfield) is now binding per the [launch spec](../../decisions/october-2026-launch-spec.md). The deeper track (flagship Cadence, V2–V4, the full lineup, per-game scope) remains lightweight working-draft until the opening ships.
