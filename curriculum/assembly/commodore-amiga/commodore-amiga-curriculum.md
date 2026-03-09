# Commodore Amiga Curriculum

**Platform:** Commodore Amiga
**Killer Feature:** Custom chipset — Agnus, Denise, and Paula working in concert
**Assembly Games:** 4
**Total Units:** 1,408

---

## Overview

The Amiga curriculum teaches 68000 assembly programming through four complete games. The sequence begins with the custom chipset — Agnus (DMA, Copper, Blitter), Denise (video output), and Paula (audio, interrupts) — and progresses through dual playfield parallax, Copper per-scanline effects, and AGA enhanced graphics until learners can produce commercial-quality games spanning the A500 to A1200.

The Amiga was not about one killer feature. It was about the custom chips working in harmony: the Blitter accelerating graphics, the Copper synchronising effects to the display beam, Paula playing four channels of sampled audio — all while the 68000 orchestrated the action. This curriculum teaches learners to conduct that orchestra.

By the final game, learners will have skills matching professional Amiga developers of the early 1990s — equivalent to teams at Team17, Psygnosis, or Magnetic Fields.

---

## Assembly Track

### Structure

| Game | Units | Phases | Units/Phase | Role |
|------|-------|--------|-------------|------|
| 1 | 128 | 8 | 16 | Accessible entry — Blitter as game mechanic |
| 2 | 256 | 8 | 32 | Signature technique — dual playfield parallax |
| 3 | 512 | 16 | 32 | Ambitious — Copper per-scanline racing, perspective maths |
| 4 | 512 | 16 | 32 | Capstone — OCS/ECS/AGA, chipset detection, professional distribution |
| **Total** | **1,408** | | | |

---

### Game 1: Terrain Puzzle

**Units:** 128 (8 phases)
**Genre:** Terrain puzzle
**Inspired by:** Lemmings, Clonk, Worms (terrain modification)
**Working title:** TBD

**Concept:** Creatures walk across a bitmap landscape. The player modifies the terrain to guide them to safety: digging tunnels, building bridges, redirecting paths. Every game action is a Blitter operation — clearing bits digs, setting bits builds, copying bits constructs. The Copper paints gradient skies above. Paula plays satisfying terrain sounds. The game boots from a custom ADF disk from unit 1.

**Skills taught:**
- 68000 assembly fundamentals (data/address registers, addressing modes, supervisor/user mode)
- Amiga hardware architecture (chip RAM, custom registers, DMA channels)
- Display setup (bitplanes, display window, DIWSTRT/DIWSTOP, DDFSTRT/DDFSTOP)
- Copper list basics (WAIT, MOVE, colour changes, screen splits)
- Copper gradient backgrounds (sky, ground, water)
- Bitplane graphics and bitmap terrain representation
- Blitter operations as game mechanics:
  - BLTCON0/BLTCON1 configuration
  - Copy (A→D for building), clear (D=0 for digging), fill, line draw
  - Cookie-cut masking (A=source, B=mask, C=background, D=destination)
- Paula sample playback (loading and triggering sound effects)
- Terrain collision detection against bitmap data
- Creature AI (walking, turning at edges, falling, climbing)
- Player input for assigning creature abilities
- UI panel with Copper screen split
- Level data structures (bitmap terrain + creature spawn points)
- Bootable ADF creation (executable on disk from unit 1)
- Level progression with increasing difficulty

**Why first:** Lemmings makes the Blitter a game mechanic. Digging a tunnel is `BLTCON0 = $0100` (clear destination). Building a bridge is a Blitter copy. The learner doesn't learn the Blitter in theory and then apply it — every game action IS a Blitter operation. The Copper splits the screen for the UI panel and paints gradients, Paula plays terrain sounds, and the 68000 orchestrates the creatures. It's a small-scale demonstration of the full chipset orchestra.

---

### Game 2: Parallax Showcase

**Units:** 256 (8 phases × 32 units)
**Genre:** Parallax showcase (side-scrolling action)
**Inspired by:** Shadow of the Beast, Agony, Lionheart
**Working title:** TBD

**Concept:** A side-scrolling action game where the visuals are the headline. Multiple background layers scroll at different speeds — distant mountains barely move, mid-ground trees drift past, foreground details rush by. The player runs, jumps, and fights through a world that looks impossibly deep. Shadow of the Beast made people buy Amigas; this game teaches how it worked.

**Skills taught:**
- Dual playfield mode (DBLPF in BPLCON0)
  - Two independent 3-bitplane playfields
  - Separate scroll registers per playfield
  - Priority control (playfield 1 vs. 2, sprites between layers)
- Multi-layer parallax (4+ speed layers via scroll register manipulation)
- Hardware scroll registers (BPLCON1 fine scroll, BPLxPT coarse scroll)
- Bitplane DMA timing (fetch start/stop, modulos for scrolled displays)
- Copper per-line colour effects (gradient skies, water reflections, atmospheric haze)
- Colour cycling and palette animation
- Blitter-based BOB (Blitter Object) rendering
  - Cookie-cut sprite drawing
  - Background save and restore
  - BOB animation frames
- Hardware sprite usage alongside BOBs
- Player movement and combat (run, jump, attack, duck)
- Enemy AI variety (ground patrol, flying, ranged, boss)
- Parallax-aware level design (foreground obstacles vs. background decoration)
- Paula MOD music playback (ProTracker format)
- Paula SFX mixing (playing effects without interrupting music)
- Level streaming (loading new background columns during scroll)
- 5 themed stages with distinct parallax configurations
- Boss encounters

**Why here:** Shadow of the Beast defined the Amiga's visual identity. Dual playfield parallax is the technique that made jaws drop — and it only exists because Agnus can drive two independent scroll positions simultaneously. This game teaches the technique through its most spectacular application. The learner also transitions from Blitter-only graphics (Game 1) to combining Blitter BOBs with hardware sprites and dual playfield backgrounds — the full display pipeline that every subsequent Amiga game requires.

---

### Game 3: Pseudo-3D Racing

**Units:** 512 (16 phases × 32 units)
**Genre:** Pseudo-3D racing
**Inspired by:** Lotus Turbo Challenge, Outrun, Super Hang-On
**Working title:** TBD

**Concept:** Drive at high speed down roads that curve, climb hills, and fork. The Copper renders the road by changing colours on every scanline — each line represents a different distance from the viewer, creating the illusion of perspective. Split-screen two-player mode doubles everything. Paula synthesises engine roar that rises and falls with speed.

This is the game that teaches Copper programming at the deepest level and introduces perspective mathematics that nothing else in the curriculum covers.

**Skills taught:**
- Perspective projection mathematics (3D world to 2D screen)
- Road geometry (curves via horizontal offset per scanline, hills via Y displacement)
- Copper per-scanline rendering:
  - Road colour changes per line (road, kerb, grass, rumble strip)
  - Horizon line positioning
  - Background colour gradients (sky, distance haze)
- Road segment data structures (curvature, elevation, width, scenery)
- Sprite scaling simulation (pre-scaled sprite sets for depth)
- Player car physics (steering, acceleration, braking, gear system)
- Curve physics (centrifugal force, drift, off-road penalties)
- Traffic system (AI cars with overtaking behaviour)
- Roadside scenery (signs, trees, buildings — sprite-based at varying depths)
- Split-screen two-player:
  - Copper screen split for two viewports
  - Independent game state per player
  - Sprite allocation across split screens
- Paula engine sound synthesis (frequency modulation for RPM)
- Paula MOD music with dynamic mixing (fade music during engine roar)
- 5 themed tracks (coastal, city, desert, forest, mountain)
- Championship mode (race across all tracks)
- Time trial with ghost replay
- Attract mode / demo replay
- Level-of-detail management (near objects detailed, far objects simplified)

**Why here:** Lotus Turbo Challenge is pure Copper programming. Every scanline of the road is a Copper MOVE — change the colour, shift the position, create the illusion of depth. No other game in the curriculum teaches perspective maths or per-scanline rendering at this depth. The split-screen two-player mode doubles the Copper workload and forces efficient resource management. And it's a genuinely fun game to play — the combination of speed, sound, and visual depth is the Amiga at its most exhilarating.

---

### Game 4: Capstone

**Units:** 512 (16 phases × 32 units)
**Genre:** Scrolling action game with chipset showcase (distinct from Games 1-3)
**Inspired by:** Team17, Psygnosis, or Bitmap Brothers releases
**Working title:** TBD

**Concept:** A scrolling action game that runs on an A500 and lights up on an A1200. The OCS/ECS version uses all techniques from Games 1-3. The AGA version adds 256-colour graphics, enhanced sprites, HAM8 title screens, and A1200-specific optimisations. The capstone bridges the Amiga's generations: one codebase, two visual presentations.

The new material is chipset detection and adaptation, AGA register programming, custom disk loading, and the production polish that characterised Amiga commercial releases.

**Skills taught:**
- All techniques from Games 1-3 at mastery level
- Chipset detection (OCS vs. ECS vs. AGA via VPOSR/DENISEID)
- AGA register programming:
  - BPLCON3/BPLCON4 (bank select, palette control, sprite XOR)
  - FMODE (fetch width for wider bitplane/sprite fetch)
  - 256-entry 24-bit palette (8-bit RGB via LOCT register)
  - 8-bitplane displays
- HAM8 mode (Hold and Modify with 8 bitplanes — 262,144 colours)
- HAM8 title screen / cutscene rendering
- Dual code paths (OCS/ECS baseline, AGA enhancements)
- Custom disk loading (bypassing AmigaDOS for speed)
- Multi-disk support (if game exceeds single ADF)
- Bootable ADF with custom trackloader
- Professional loading sequence (loading screen with progress)
- Advanced Blitter techniques (optimised for A1200's faster chip RAM)
- Copper list optimisation for complex displays
- Memory management across chip/fast RAM
- Startup-sequence compatible launcher (for hard disk installs)
- Testing across models (A500, A500+, A600, A1200, A4000)
- Credits, end sequence, attract mode

**Why last:** The capstone bridges the Amiga's two eras. Running the same game on an A500 (1987, OCS, 7 MHz) and an A1200 (1992, AGA, 14 MHz) demonstrates mastery of the full chipset family. The AGA enhancements aren't a separate game — they're conditional code paths that detect the hardware and adapt. This teaches a real-world skill that every professional Amiga developer needed: shipping a product that works everywhere while looking best on the latest hardware.

---

## AMOS Gateway

The AMOS curriculum is maintained separately. See `/docs/curriculum/basic/commodore-amiga/commodore-amiga-basic-curriculum.md`.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 16+8 AGA to 4 assembly games. No-repetition rule across primary platforms. Every game inspired by a real commercial release. AMOS gateway restructured as 4 focused games. Previous 16-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 16-game + 8 AGA enhancement curriculum.
