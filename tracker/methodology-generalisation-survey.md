# Methodology Generalisation Survey

**STATUS: Methodology-check only. No-commit.** No skeleton specs, no candidate lineups, no design work — just the question *does the Spectrum methodology generalise to this system?*

The Spectrum methodology being tested (per [`decisions/spectrum-assembly-track.md`](../decisions/spectrum-assembly-track.md)):

1. **Three-axis design pattern** — player-facing headline + design concept + technique (mapped separately)
2. **Trunk + Branches tech tree** — shared foundations + genre-conditional specialisations
3. **Three cross-cutting axes** — Embedded Design Concepts (cross-platform) + Engineering Practices (CPU-specific) + Production Craft (platform-specific)
4. **Layer model** — L0 native + L+1 audio/memory enhancement + L+3 demoscene polish + L+4 modern variants
5. **Inspired-by-not-clones naming convention**
6. **Tier hierarchy** per platform
7. **Per-game scope honesty** — canon dictates size, not aesthetic uniformity

Captured 2026-05-19 after C64 / NES / Amiga skeletons surfaced no major framework cracks. This survey extends the check to a wider set: Apple 8-bit, Atari 8-bit, Game Boy, SNES, Sega Master System, Mega Drive / Genesis, BBC Micro, Dragon.

## The survey

### Apple II (1977-1993)

6502 CPU; speaker (single-bit, beeper-like); hi-res mode with NTSC colour artifacts (a *unique design vocabulary*); 5.25" floppy (Disk II) defining; canon = Ultima series, Wizardry, Karateka, Prince of Persia, Lode Runner, Bards Tale.

**Methodology generalises: Yes.** Engineering Practices ≈ 6502 family (similar to C64 / NES). Branch G content is *speaker-as-beeper* (closer to Spectrum than to SID / AY / SPC). Production Craft includes 5.25"-floppy authoring + Disk II conventions. **Unique design vocabulary: hi-res colour artifacting** — Apple II hi-res mode achieved 6 distinct colours from monochrome bit patterns interpreted by NTSC chrominance. That's a Branch C-equivalent (graphics-trick) Apple-only addition. The RPG tradition is heavier here than anywhere else (Wizardry, Ultima, Bards Tale) — Branch A would be unusually dominant.

### Atari 8-bit (400/800/XL/XE, 1979-1992)

6502 CPU; **ANTIC display-list processor** (essentially a programmable Copper-equivalent, predates Amiga); CTIA/GTIA graphics; POKEY 4-channel sound chip; player-missile graphics (8 hardware sprites); canon = Star Raiders, M.U.L.E., Eastern Front, Alternate Reality, Archon, Necromancer.

**Methodology generalises: Yes.** Engineering Practices ≈ 6502 family. Branch G = POKEY (4-channel audio, distinct from SID / AY but in the same conceptual position). **Unique: ANTIC display lists** — running display-list-modification code is a Copper-style technique on 8-bit hardware, well ahead of its time. Could be its own branch or cross-cutting axis ("hardware co-processor programming"). Player-missile graphics are similar to NES sprites — Trunk Layer 2 generalises with player-missile specifics. Methodology fits cleanly.

### Game Boy / Game Boy Color (1989 / 1998)

**Modified Z80 (LR35902)** — *very* close to Spectrum's Z80; 4-shade greyscale on DMG, 32K-palette + 56-on-screen on CGB; tile-based graphics + 40 hardware sprites; 4-channel sound (2 pulse + wave + noise); cartridge with mappers (MBC1-7); battery-backed saves; canon = Tetris, Super Mario Land, Pokémon, Metroid II, Link's Awakening, Wario Land, Donkey Kong '94.

**Methodology generalises: Yes — strongest CPU-parallel of any system.** Engineering Practices ≈ Spectrum's Z80 idioms (LR35902 has some differences — no IX/IY in same form, slightly different opcodes — but ~85% transferable). Branch G = 4-channel hardware audio (different from beeper but more like NES APU). **Unique cross-cutting: battery-backed save** (cartridge SRAM — a real production-craft concern not present on Spectrum). Mappers (MBC1-7) sit in production craft (like NES). **Unique design constraint: portability** — battery life and outdoor screen visibility become real design considerations. Could be a Branch H "Portability" if we ever did Game Boy seriously.

### Super Nintendo (SNES / Super Famicom, 1990)

**65C816** (extended 6502 with 16-bit modes); PPU with hardware sprites + multiple background layers + **Mode 7** (rotation/scaling on one layer); SPC700 audio chip + 8-channel sample-based audio; cartridge with co-processors (SuperFX, SA-1, DSP); canon = Super Mario World, A Link to the Past, Super Metroid, Final Fantasy VI, Chrono Trigger, Donkey Kong Country, F-Zero, Star Fox, Yoshi's Island.

**Methodology generalises: Yes.** Engineering Practices = 65C816 (extended 6502 — recognisable to NES/C64 developers, new 16-bit modes). Branch G = SPC700 + sample-based audio (closer to Amiga Paula than to AY/SID). **Unique design vocabulary: Mode 7** (one rotated/scaled background layer — a single specific hardware trick that defined SNES design — F-Zero / Super Mario Kart / Final Fantasy VI overworld). Could be its own Branch. **Unique production craft: cartridge co-processors** (SuperFX for Star Fox; SA-1 for Super Mario RPG; DSP for Pilotwings) — each adds a "Branch" of platform variation, like Spectrum's 128K but more dramatic.

### Sega Master System (SMS, 1985-1991)

**Z80 CPU** (same as Spectrum); VDP based on TMS9918 (tile-based, hardware sprites); PSG (3 tone + 1 noise — derived from AY-3-8910); FM sound chip (Japan only); 8K RAM; cartridge / Sega Card; canon = Alex Kidd in Miracle World, Phantasy Star, Wonder Boy, Castle of Illusion, Sonic 8-bit, R-Type SMS, Outrun.

**Methodology generalises: Yes — most Spectrum-adjacent of any 8-bit console.** Engineering Practices ≈ Spectrum directly (same Z80; same LDIR / T-state idioms). Branch G = PSG (essentially a simplified AY — Spectrum 128K-AY teaching transfers almost wholesale, with FM as a Japan-region addition). Hardware sprites + scrolling add to Trunk Layer 2-3. The SMS's structural position is *"Spectrum with hardware sprites + better audio + cartridge"* — methodology fits with mostly additive content. **No major divergence.**

### Sega Mega Drive / Genesis (1988-1997)

**Motorola 68000** (like Amiga) **+ Z80 sub-CPU** (for audio control); VDP with hardware sprites + multi-bg scrolling + palette tricks; YM2612 (FM synthesis) + PSG (Z80-controlled, AY-derivative); cartridge; canon = Sonic the Hedgehog, Streets of Rage, Phantasy Star IV, Gunstar Heroes, Strider, ToeJam & Earl, Earthworm Jim, Comix Zone.

**Methodology generalises: Yes.** Engineering Practices = 68000 (like Amiga) for main code + Z80 for audio scripts (a hybrid). Branch G = YM2612 FM synthesis (a third distinct audio paradigm — not synthesis-style like SID/AY, not sample-based like Paula, but FM operator-based). **Unique design vocabulary: FM synthesis composition** — composing for FM is genuinely a different art. Mega Drive sits structurally between SNES (16-bit console with hardware sprites) and Amiga (68000 main CPU) — methodology fits, content per axis bridges those reference points.

### BBC Micro (1981-1994)

6502 CPU; multiple graphics modes (Mode 0-7 — varying res/colours); single-bit speaker + SN76489 3-channel sound chip; **Acornsoft + BBC BASIC** as platform identity; disk drive; canon = **Elite** (original platform!), Chuckie Egg, Repton, Aviator, Revs, Frak!, Exile, Granny's Garden.

**Methodology generalises: Yes — and the platform has a particularly clean Spectrum parallel.** Engineering Practices = 6502 (familiar). Branch G = SN76489 + 1-bit speaker (audio is closer to Spectrum's beeper+AY than to SID's filter heritage). **Unique: graphics mode switching** — Mode 7 (teletext), Mode 0 (640×256 mono), Mode 2 (160×256 8-colour) etc. are real design choices a developer makes per game. **BBC has both a strong BASIC tradition AND a strong assembly tradition** — structurally closest to Spectrum (separate BASIC + Assembly tracks). The original Elite shipped on BBC; Geoff Crammond's foundational work was here (Aviator, Revs, Sentinel) — canon is real.

### Dragon 32 / 64 (1982-1984)

**MC6809 CPU** (different from Z80 / 6502 — more capable but smaller community); 32-64K RAM; 6847 video (similar to TRS-80 Color Computer); single-bit speaker; tape-based; small UK-focused market; canon: thin — relatively few uniquely-Dragon games, many ports, education software.

**Methodology generalises: Yes, with caveats.** Engineering Practices = 6809 (a CPU family the methodology hasn't touched yet — 6809 has more capable addressing modes than 6502 but is its own beast). The methodology *structure* fits but the **canon is thin** — there might be 6-8 candidate games rather than 16. If Dragon were ever a curriculum platform, it would probably be a smaller-scope track (12 games total maybe, not 32-44) reflecting honest canonical depth. **No major framework gap — just a quantity-of-content issue.**

## Summary table

| System | CPU | Canonical scope | Methodology fits? | Biggest divergence |
|--------|-----|-----------------|-------------------|-------------------|
| **Apple II** | 6502 | Large (RPG-heavy) | Yes | Hi-res NTSC colour artifacting (unique graphics trick); 5.25" floppy production craft; Branch A unusually dominant |
| **Atari 8-bit** | 6502 | Medium-large | Yes | ANTIC display lists (Copper-style on 8-bit); POKEY audio |
| **Game Boy / CGB** | Z80-derivative | Large | Yes (closest CPU parallel) | Portability constraints; battery saves; mappers (MBC1-7) |
| **SNES** | 65C816 | Very large | Yes | Mode 7 rotation/scaling; cartridge co-processors (SuperFX / SA-1 / DSP); SPC700 sample audio |
| **SMS** | Z80 | Medium | Yes (closest to Spectrum) | Minimal — additive only (HW sprites, PSG, cartridge) |
| **Mega Drive** | 68000 + Z80 | Large | Yes | YM2612 FM synthesis (third audio paradigm); 16-bit hybrid |
| **BBC Micro** | 6502 | Medium (Elite, Crammond, Repton) | Yes (closest *structural* parallel to Spectrum) | Graphics mode switching; BASIC + Assembly dual tradition like Spectrum |
| **Dragon 32/64** | MC6809 | **Thin** | Yes-with-caveat | Smaller canon limits scope; 6809 is methodology's first non-Z80/non-6502 CPU |

## Where the methodology stretches but doesn't break

Three patterns surfaced consistently:

1. **Branch G is platform-specific by design.** Every platform has its own audio hardware. The methodology already accommodates this (Spectrum AY+128K, C64 SID, NES APU, Amiga Paula are different content; the *axis* is the same). Adds Apple speaker, Atari POKEY, Game Boy 4-channel, SNES SPC700, Mega Drive YM2612, SMS PSG, BBC SN76489, Dragon speaker.
2. **Engineering Practices is CPU-specific.** Z80 / 6502 / 65C816 / 68000 / 6809 each have their own idioms. The *axis* is universal; the *content* per platform varies. This is fine — Engineering Practices was *always* an Assembly-track-specific axis.
3. **Trunk Layer 2 (The Sprite) varies by hardware affordance.** Spectrum: software sprites + masking + pre-shifting. NES: hardware sprites from the start, no software-sprite era. SNES / Mega Drive / SMS / Atari 8-bit / Game Boy: same — start with hardware sprites. The methodology adapts; software sprite work shifts to *demoscene / overscan / multiplexing* technique rather than foundation work on hardware-sprite platforms.

## What didn't surface as a crack

- **Naming convention** (inspired-by-not-clones) is universal — applies on every system equally.
- **Three-axis design pattern** (player-facing / design concept / technique) is platform-independent — works on any system.
- **Tier hierarchy** is per-platform — fits every system surveyed.
- **Cross-game prerequisite seeding** is intra-track concept — applies whether a platform has 6 games or 44.
- **Layer model** — every platform has its own native + enhanced layers (Spectrum: 48K/128K/Next; C64: native/REU/Reloaded; Amiga: OCS/AGA; SNES: native/co-processor variants; Mega Drive: native/32X; etc.). Layer model is universal, content per platform varies.

## The test result

The Spectrum methodology generalises across **all 11 surveyed systems** (C64, NES, Amiga + the 8 in this doc). No major framework cracks. **The pattern works.**

What varies is *content per axis*, not the axes themselves. Each platform contributes:
- Its own Branch G (audio hardware)
- Its own Engineering Practices (CPU idioms)
- Its own Production Craft (loading / saving / authoring conventions)
- Its own canonical legends and genre balance (Apple II = RPG-heavy; NES = platformer-heavy; SNES = JRPG-heavy; Amiga = sim-heavy)
- Its own unique design tricks worth their own branches or cross-cutting notes (Apple II hi-res colour, Atari ANTIC, SNES Mode 7, BBC graphics modes, Mega Drive FM)

This is a *positive* finding — methodology survives 11 systems' worth of distinct hardware, CPU families, audio paradigms, and design vocabularies without restructuring. **It's a genuine framework, not Spectrum-specific.**

## What this survey does NOT commit to

- Adding any of these systems to the Code198x platform list (project stays at 4: C64, Spectrum, Amiga, NES)
- Designing skeletons for any of them (only C64, NES, Amiga have skeletons; the 8 surveyed here are methodology-check only)
- Promising future curriculum expansion to other systems
- Locking any decisions

This is purely a *pressure-test* of the framework. Its value is methodological confidence, not roadmap.

## Pushing further — where does the methodology actually break?

The 11 systems above all fit. But that's a methodology stress-test on a comfortable population — raster-display, 8-16-bit-era, framebuffer-based home computers and consoles. The honest follow-up question: *what would break it?*

Five further systems pushed harder. Three find genuine strain. One breaks Trunk Layers 1-2. One leaves the methodology's domain entirely.

### Atari 2600 (1977) — first genuine strain on Trunk Layer 1

6507 CPU (6502 derivative); TIA (Television Interface Adaptor) generates graphics scanline-by-scanline as the beam scans; **128 bytes** of RAM total (not K); 2K-4K game ROM on cartridge; 2 player sprites + 2 missiles + ball + playfield = the entire graphics vocabulary. Canon: Adventure (1980 — shaped ARPG genre), Pitfall!, Yars' Revenge, River Raid, E.T., Combat, Asteroids 2600 port.

**The strain:** *Trunk Layer 1 (The Framebuffer as Canvas)* **doesn't translate.** There is no framebuffer. The programmer doesn't write pixels to memory; they write to TIA registers at the precise *time* the beam is at the right scanline. *"Racing the beam"* is the foundational discipline — every instruction is cycle-counted not for performance but because the CPU literally generates the image as code runs.

**What survives:** Engineering Practices (6502 family — Spectrum-adjacent at the assembly level, plus cycle-counting taken to its extreme). Production Craft (cartridge ROM authoring; bank-switching mappers). Cross-cutting Design Concepts (Atmosphere, Authorial Choice, etc.). Naming convention.

**What needs reworking:** Trunk Layer 1 becomes "The Scanline" rather than "The Framebuffer." Trunk Layer 2 (The Sprite) reworks too — TIA gives you fixed-position sprite hardware with very particular per-scanline behaviour. Branch G (audio) is 2-channel TIA tones — very limited. Branches C / E (scrolling / 3D) don't exist.

**Verdict: methodology survives with significant Trunk reframing.** First genuine strain. The 2600 is *just within* the methodology's domain, at its earliest edge.

### Vectrex (1982) — first place Trunk Layers 1-2 cannot meaningfully translate

Motorola 6809 CPU (same family as Dragon); **vector display built in** — programmer sends analog signals to deflect the beam; colour comes from physical plastic overlays placed over the screen (!); cartridge; ~30 games. Canon: Mine Storm, Berzerk, Scramble, Spike, Pole Position, Solar Quest.

**Where it breaks:** *Trunk Layer 1 (Framebuffer) and Trunk Layer 2 (The Sprite) do not exist on Vectrex.* There's no pixel array; there's no sprite concept. The programmer draws *lines* by sending start-point + end-point + intensity to the analog vector hardware. Y-sort, masking, pre-shifting, attribute clash — all the Spectrum methodology's framing for *visual rendering* is meaningless here.

**What survives:** Engineering Practices (6809 — partially covered via Dragon). Production Craft (cartridge work). Design Concepts as a category (Atmosphere, Authored Experience). Naming convention. Tier hierarchy. The three-axis pattern (player-facing / design concept / technique) still applies at the per-game level.

**What needs replacement:** Trunk Layers 1-2 entirely. The vector-display equivalent would be "Lines and Persistence" (Layer 1), "Vector Shapes" (Layer 2), "Hidden Lines and Z-order" (Layer 3 equivalent), "Movement and Inertia" (Layer 4 equivalent). Completely different framing.

**Verdict: methodology's *cross-cutting axes* survive but Trunk + Branches need replacement.** Vectrex is the **first surveyed system where the methodology's spine genuinely needs rebuilding**, not just per-axis content variation. *The pattern reaches a real boundary here.*

### Sony PlayStation (1994) and Nintendo 64 (1996) — 3D-first hardware promotes Branch E to Trunk

PSX: 32-bit MIPS R3000A + GPU + GTE (geometry coprocessor); CD-ROM streaming; 2D capabilities exist but the platform identity is 3D. N64: MIPS R4300 + RCP; cartridge; 3D-first hardware. Canon: Crash Bandicoot, Final Fantasy VII, Metal Gear Solid, Tony Hawk's Pro Skater, GoldenEye 007, Super Mario 64, Ocarina of Time.

**The strain:** On PSX/N64, **3D is the default**, not Branch E. The methodology's Branch E (True 3D — Wireframe / Solid / First-person) is the *exotic curiosity* on Spectrum / C64 / Amiga; on PSX/N64 it's the **whole platform**. Branch E gets *promoted to Trunk*. Trunk Layer 1 (Framebuffer) becomes secondary — the framebuffer exists but is mostly consumed by the GPU's output; the programmer thinks in *vertices, transforms, and texture pages* rather than pixels.

**What survives:** Engineering Practices (MIPS — a new CPU family the methodology hasn't touched, but with similar overall shape). Production Craft (CD-ROM streaming + memory-card saves are real concerns). Design Concepts. Naming convention. The Branch model — Branch E expands enormously; original Trunk shrinks. Three-axis design pattern.

**What needs reworking:** *Trunk Layers entirely.* New trunk layers: "The Vertex" (3D point), "The Polygon" (triangle), "The Texture" (image-applied-to-3D), "The Camera" (view transform), "Frame Buffer" (now an *output* not a workspace). Branch C (Scrolling) becomes minor. Branch G (audio) is sample-based + ADPCM (PSX) or sample-based + MIDI-like (N64).

**Verdict: methodology survives but Trunk fundamentally reframes.** PSX/N64 are *late-era* — beyond the natural domain of the methodology as Spectrum-rooted but still within the *console games-as-craft* tradition. The methodology applies with **a different Trunk model** for the 3D era. **Second real strain.**

### Modern mobile (2007+) and modern indie (Steam / Itch / Unity / Godot, 2010+) — methodology leaves its domain entirely

ARM CPUs (mobile) or x86-64 (desktop indie); high-level languages (Swift, Kotlin, C#, Lua); engine-mediated development (Unity, Unreal, Godot, GameMaker dominant); always-online or near-always-online; app store certification; OTA updates; touch input / mouse-keyboard / controller mix.

**Where it breaks:** The methodology's *whole premise* — hardware-constrained design where you understand the machine at the metal — doesn't apply when:
- The platform abstracts the hardware (modern OS APIs)
- The engine abstracts the platform (Unity runs on iOS / Android / Switch / PC / Mac / Linux)
- The defining concerns are *not* hardware (engagement loops, monetisation, certification, store visibility, OTA hotfix cadence)
- The Engineering Practices axis becomes irrelevant — nobody hand-optimises engine-level code in indie game development; that's the engine vendor's job

**What survives:** Naming convention. Design Concepts. Three-axis design pattern at the per-game level. Tier hierarchy concept.

**What doesn't survive:** Trunk + Branches (the engine handles graphics / audio / input — not you). Layer model (no native-vs-enhanced distinction — engine targets all platforms). Engineering Practices axis (mostly irrelevant). Production Craft axis (now means *store assets / certification / community management*, not loaders or art tools).

**Verdict: methodology breaks.** Modern mobile / indie is *outside the methodology's domain entirely*. The methodology is fundamentally about *retro / hardware-constrained game craft as taught through canonical games of the 8-16-bit era*. It is not a general games-development curriculum.

### Where the boundary actually lies

The methodology's **natural domain** is:

- **Hardware paradigm:** Raster-display, framebuffer-based, hardware-constrained, single-machine programming
- **CPU era:** 8-bit through 16-bit, possibly early 32-bit; not engine-mediated modern application development
- **Media:** Cartridge / disk / tape / early CD-ROM. Not streaming-update / always-online
- **Graphics paradigm:** Raster framebuffer with sprite hardware affordances. Not vector-only (Vectrex), not 3D-first (PSX/N64)
- **Approximate era:** 1977-1995 raster-era home computers and consoles

Outside this domain, the methodology *strains* (Atari 2600, PSX/N64) or *breaks* (Vectrex Trunk Layers, modern mobile entirely).

**This is a healthy finding.** The methodology has a *real domain*, not a *universal claim*. It applies to ~30-40 retro-era platforms cleanly; it strains at the edges (2600's race-the-beam, PSX/N64's 3D-first); it breaks completely outside the raster-era hardware-constrained-craft tradition (Vectrex on graphics paradigm; mobile on the whole development paradigm).

The methodology is **not** *"how to teach game development"* — it is **"how to teach retro raster-era hardware-craft game development through the canon."** That's a real, bounded, and defensible scope.

## Updated test result

The Spectrum methodology generalises across **all 11 systems in the first survey** (raster-era 8-16-bit home computers and consoles 1977-1995). It **strains usefully** on 2 of 5 systems in the stress-test pass (Atari 2600 at its earliest edge; PSX/N64 at its latest edge). It **breaks Trunk Layers** on Vectrex (vector display, no framebuffer or sprite concept). It **leaves its domain entirely** for modern mobile / indie.

**Conclusion: the methodology is a genuine framework with a defensible domain, not a universal claim.** That's a stronger and more honest result than "it works everywhere."

## Status

Methodology check captured 2026-05-19. Stress-test extended same day. No commitment. Result: methodology generalises across 11+ surveyed retro platforms; finds its real boundary at Vectrex (graphics paradigm) and modern mobile/indie (development paradigm); strains usefully at 2600 (earliest edge) and PSX/N64 (3D-era edge). The framework is bounded and defensible.
