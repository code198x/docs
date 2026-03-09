# Full Game Outline: Amiga Horizons (512 Units)

**Game:** Horizons (Game 4 — Capstone)
**Units:** 512 (16 phases × 32 units)
**Genre:** Scrolling action game bridging OCS to AGA
**Inspired by:** Team17 releases, Psygnosis titles, Bitmap Brothers aesthetic
**Target Quality:** Cross-generation showcase (1992–94 era)

---

## Premise

The world is a chain of floating islands — remnants of a shattered continent, drifting in a luminous void. Each island is a self-contained realm: forests grow on one, machinery grinds on another, crystal formations light a third, ruins of a lost civilisation crumble on a fourth, and the final island — the Horizon — hangs at the edge of the void where the light originates.

You leap between islands, fight the creatures that infest them, and gather the shards needed to reconnect the chain. The game scrolls horizontally through each island, with vertical sections for climbing and descending between them. On an A500, the world is vivid OCS — 32 colours, Copper gradients, Blitter BOBs. On an A1200, the same world ignites with AGA: 256 colours, enhanced sprites, HAM8 title screens, smoother animation.

One game. Two presentations. The Amiga's full history in one cartridge — from the machine's birth to its final flowering.

---

## Why This Is the Capstone

Horizons requires everything from Games 1-3 and adds the production craft that bridges the Amiga's two eras:

| From Game | Technique | Use in Horizons |
|-----------|-----------|----------------|
| Exodus | Blitter operations, bitmap manipulation | BOB rendering, terrain effects, particle debris |
| Exodus | Copper basics, display setup | Display pipeline, screen splits, gradient sky |
| Exodus | Paula samples | Sound effects, environmental audio |
| Duskfall | Dual playfield parallax | Multi-layer island backgrounds |
| Duskfall | Blitter BOB cookie-cut, save/restore | All game sprites |
| Duskfall | Copper per-line effects | Atmospheric gradients, water, haze |
| Duskfall | MOD playback | Per-island music themes |
| Redline | Copper per-scanline rendering | Sky effects, distance fog, lighting |
| Redline | Perspective maths | Scaling scenery in vertical sections |
| Redline | Split-screen Copper | HUD panel, cutscene framing |

**New in Horizons:**
- **Chipset detection** — OCS/ECS/AGA via DENISEID or VPOSR register probe
- **AGA registers** — BPLCON3 (bank select), BPLCON4 (sprite XOR), FMODE (fetch width), 256-entry 24-bit palette via LOCT
- **8-bitplane display** — AGA 256-colour mode for enhanced island visuals
- **HAM8 mode** — Hold and Modify with 8 bitplanes (262,144 colours) for title and cutscene screens
- **Dual code paths** — OCS baseline, AGA conditional enhancements
- **Custom disk loading** — bypass AmigaDOS for speed, trackloader for boot disk
- **Multi-disk support** — if content exceeds a single ADF
- **Startup-sequence launcher** — hard disk install compatibility
- **Cross-model testing** — A500, A500+, A600, A1200, A4000

---

## The Five Islands

| Island | Theme | Scroll | OCS Palette | AGA Enhancement |
|--------|-------|--------|-------------|-----------------|
| 1: Verdance | Living forest, rivers, canopy | Horizontal | 32 colours, Copper gradients | 128 colours, smooth gradients, leaf particles |
| 2: Ironworks | Mechanical, gears, steam, pipes | Horizontal + vertical (ascend) | 32 colours, metallic palette | 256 colours, metal sheen, animated machinery tiles |
| 3: Crystalline | Crystal formations, light refractions | Horizontal | 32 colours, Copper rainbow | 256 colours, translucent crystal overlay, light bloom |
| 4: Remnant | Ancient ruins, weathered stone, glyphs | Horizontal + vertical (descend) | 32 colours, earthy palette | 128 colours, detailed stonework, parallax depth layers |
| 5: Horizon | The edge, luminous void, pure light | All directions | 32 colours, Copper full spectrum | 256 colours, HAM8 cutscenes, full palette glow |

Each island: 3 scrolling stages + boss. 15 stages + 5 bosses total.

---

## Core Mechanics

### Player

A swift, agile character — jumps, wall-clings, dashes, and strikes with a light-blade. Movement inherited from Duskfall's platforming engine, refined for speed and fluidity.

### Combat

Light-blade (melee, fast), light-bolt (ranged, costs energy), charged blast (hold → release, powerful). Energy regenerates from crystal shards dropped by enemies.

### Island Shards

Each island has a core shard protected by the boss. Collecting all 5 reconnects the island chain. Within islands, smaller crystal fragments serve as collectibles (100 per island, used for scoring and completion percentage).

### The Void

Between islands: brief transition sequences. On OCS: a starfield scroll. On AGA: a HAM8 image of the void with animated light effects. Same gameplay, different visual presentations.

---

## Phase Breakdown

### Phases 1-4: The OCS Game (Units 1–128)

**Phase 1 (Units 1-32): Scrolling Action Core**

Build on Duskfall's engine: horizontal scrolling with Copper parallax, Blitter BOBs for player and enemies.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 1-8 | Display engine from Duskfall foundations | Dual playfield, hardware scroll, Copper gradient | Parallax display |
| 9-16 | Player: run, jump, wall-cling, dash, light-blade | BOB animation, physics, combat hitbox | Full moveset |
| 17-24 | Verdance Stage 1 | Forest tileset, platforms, enemies, crystal fragments | First stage |
| 25-32 | Stage 1 complete | Boss area, Blitter particle effects (leaves), stage clear | **Playable island stage** |

**Phase 2 (Units 33-64): OCS Island 1 Complete**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 33-40 | Verdance Stages 2-3 | Varied terrain, river section (Copper water effect), canopy sections | Three forest stages |
| 41-48 | Verdance boss: The Rootbind | Multi-BOB tree entity. Vine attacks. Weak to charged blast on exposed core. | First boss |
| 49-56 | Ranged combat and energy system | Light-bolt projectile, energy bar, crystal energy drops | Full combat |
| 57-64 | MOD music, SFX, audio integration | Per-island theme, combat SFX, ambient forest sounds | Audio |

**Phase 3 (Units 65-96): Islands 2-3 (OCS)**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 65-80 | Ironworks (3 stages + boss) | Mechanical tileset, vertical ascent sections, gear platforms, steam hazards. Boss: The Furnace. | Second island |
| 81-96 | Crystalline (3 stages + boss) | Crystal tileset, light-beam puzzles (redirect with blade), prismatic effects via Copper. Boss: The Prism. | Third island |

**Phase 4 (Units 97-128): Islands 4-5 (OCS) — Game Complete**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 97-112 | Remnant (3 stages + boss) | Ruin tileset, vertical descent, crumbling platforms, glyph puzzles. Boss: The Guardian. | Fourth island |
| 113-128 | Horizon (3 stages + final boss) | Luminous void, floating platforms, all enemy types, The Eclipse (final boss). Island chain restored. | **OCS game complete** |

**End of Phase 4:** The complete game running on OCS hardware (A500). 5 islands, 15 stages, 5 bosses, 32-colour visuals with Copper effects, MOD music. A full Amiga game.

---

### Phases 5-8: AGA Enhancement (Units 129–256)

**Phase 5 (Units 129-160): Chipset Detection and AGA Basics**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 129-132 | Chipset detection | Read DENISEID ($DFF07C) or probe VPOSR. Identify OCS, ECS, or AGA. | **Hardware detection** |
| 133-136 | Conditional code paths | If AGA: branch to enhanced setup. If OCS: standard setup. One codebase, two presentations. | Dual-path architecture |
| 137-140 | AGA palette setup | 256-entry palette. BPLCON3 bank select. Write 24-bit RGB via colour registers + LOCT for low bits. | **256-colour palette** |
| 141-144 | 8-bitplane display | BPLCON0 for 8 bitplanes (256 colours). FMODE for wider fetch. More DMA bandwidth needed. | 256-colour display |
| 145-148 | AGA palette for Verdance | 256 shades of green, brown, blue. Smooth gradients that OCS approximated with Copper. | **Visual upgrade** |
| 149-152 | AGA sprite enhancements | Wider sprites (FMODE), more colours per sprite. Enhanced player and enemy BOBs. | Sprite upgrade |
| 153-156 | AGA vs OCS comparison | Same stage, side by side. OCS: 32 colours, Copper tricks. AGA: 256 smooth colours. | The difference |
| 157-160 | Performance on AGA | A1200: 14MHz 68EC020, faster chip RAM. The game runs with headroom. Profile both chipsets. | Cross-platform performance |

**Key Teaching Moment (Units 129-132):**
Chipset detection is reading a hardware ID register. DENISEID ($DFF07C) returns $00FC for OCS Denise, $00FC for ECS Super Denise (but with additional readable bits), and a different value for AGA Lisa. Alternatively, write a value to an AGA-only register and read it back — if it sticks, AGA is present. The game then branches: `bne.s .aga_setup` — one instruction that changes the entire visual presentation.

**Phase 6 (Units 161-192): AGA Visual Features**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 161-168 | HAM8 mode | 8-bitplane Hold and Modify: 262,144 colours. Used for title screen and inter-island cutscenes. | **HAM8 rendering** |
| 169-172 | HAM8 title screen | "HORIZONS" rendered in near-photographic quality. An image impossible on OCS. | AGA showcase title |
| 173-176 | HAM8 void transitions | Between islands: HAM8 image of the luminous void. Fades in/out via palette manipulation. | Cinematic transitions |
| 177-180 | AGA-enhanced Copper | More palette entries to change per line → smoother gradients without Copper tricks. Copper still useful for timing. | Evolved Copper use |
| 181-184 | AGA per-island palettes | Each island: full 256-colour palette designed. Verdance: 64 greens, 32 browns, 32 blues, etc. | Rich palettes |
| 185-188 | BPLCON4 sprite XOR | AGA sprite palette banking. Sprites can use different palette ranges than background. | Sprite colour independence |
| 189-192 | AGA rendering integration | All 5 islands enhanced with AGA palettes. Title and transitions in HAM8. Consistent quality. | AGA pass complete |

**Phase 7 (Units 193-224): Cross-Model Compatibility**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 193-196 | ECS support | A500+, A600: Super Denise but not AGA. Ensure OCS code path works on ECS too. | ECS validation |
| 197-200 | A1200 fast RAM | AGA machines may have fast RAM. Game code can run from fast RAM (faster); chip RAM for DMA data. | Memory model |
| 201-204 | A4000 testing | 68040 at 25MHz. Ensure timing-sensitive code doesn't break at higher clock speeds. | Speed tolerance |
| 205-208 | A500 512KB testing | Base A500: 512KB chip RAM only. Game must fit. No fast RAM assumed. | Minimum config |
| 209-212 | A500 + 512KB expansion | 1MB chip RAM total. Extra RAM for larger BOB buffers, more preloaded data. | Expanded config |
| 213-216 | A600 (ECS, 1MB chip) | Like A500+ but different timing. Gayle chip present (IDE). Ensure no conflicts. | A600 validation |
| 217-220 | Memory detection | Probe available chip RAM and fast RAM at startup. Adjust buffer sizes accordingly. | Runtime adaptation |
| 221-224 | Cross-model summary | Test matrix documented. All models verified. Known issues noted and resolved. | Compatibility |

**Phase 8 (Units 225-256): Audio and Polish**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 225-232 | Per-island MOD themes | Verdance: organic. Ironworks: industrial. Crystalline: ethereal. Remnant: ancient. Horizon: triumphant. | Musical journey |
| 233-240 | Sound effects | Blade slash, bolt fire, charged blast, crystal collect, damage, boss hit, platform crumble, void echo | Comprehensive SFX |
| 241-248 | Dynamic audio | Island themes fade between stages. Boss music replaces island theme. Victory fanfare. | Musical pacing |
| 249-256 | Visual effects polish | Particle systems (crystal debris, leaf scatter, steam, embers, void sparkle). Blitter-rendered. | Environmental effects |

**End of Phase 8:** OCS and AGA paths complete. All 5 islands with dual visual presentations. HAM8 title and transitions. Cross-model compatible. Full audio.

---

### Phases 9-12: Production (Units 257–384)

**Phase 9 (Units 257-288): Custom Disk Loading**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 257-264 | Trackdisk access | Direct hardware: CIA for disk motor, MFM encoding/decoding, DMA for disk reads | Low-level disk |
| 265-272 | Custom trackloader | Bypass AmigaDOS for faster loading. Read raw tracks, decode sectors, load data. | Fast loading |
| 273-280 | Loading masked by transitions | Island transition screen displays while next island data loads. Player never sees a loading screen mid-game. | Seamless loading |
| 281-288 | Bootable ADF | Custom boot block, trackloader in boot sector, game launches automatically | Boot disk |

**Phase 10 (Units 289-320): Multi-Disk and Hard Disk**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 289-296 | Multi-disk structure | If content exceeds 880KB: Island data across 2 disks. "Insert Disk 2" prompt between islands 3 and 4. | Multi-disk support |
| 297-304 | Hard disk install | WHDLoad-compatible structure. Startup-sequence launcher. Run from hard disk without floppy. | HD install |
| 305-312 | Fast RAM utilisation | On machines with fast RAM: load game code to fast RAM, keep chip RAM for DMA data. Faster execution. | Memory optimisation |
| 313-320 | Save to disk | High scores and configuration saved to game disk (or HD). Read on next boot. | Persistent data |

**Phase 11 (Units 321-352): Presentation**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 321-328 | Title screen | OCS: Copper rainbow + parallax island demo. AGA: HAM8 artwork + animated sparkle. Both beautiful. | Dual presentation |
| 329-336 | Attract mode | Automated playthrough of Verdance Stage 1. Shows parallax, combat, collection. | Demo mode |
| 337-344 | High score table | Top 5 per island + overall. Initials entry. Saved to disk. | Competition |
| 345-352 | Difficulty select | Easy (more health, fewer enemies), Normal, Hard (less health, aggressive enemies, faster bosses) | Accessibility |

**Phase 12 (Units 353-384): Endings and Narrative**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 353-360 | Island chain restoration | As each boss is defeated: a brief cutscene shows the island reconnecting. The chain reforms. | Progressive narrative |
| 361-368 | Final ending | All 5 shards gathered → the Horizon blazes with light → the islands reconnect → the void recedes → dawn across the chain | Climax |
| 369-376 | AGA ending enhancement | HAM8 frames for the restoration sequence. Near-photographic quality on A1200. | AGA showcase ending |
| 377-384 | Credits | Scrolling credits over a parallax island vista. MOD theme plays. | Attribution |

---

### Phases 13-16: Final Production (Units 385–512)

**Phase 13 (Units 385-416): Balance and Content**
- Difficulty curve across 5 islands. Island 1 welcoming, Island 5 demanding.
- Enemy placement, crystal distribution, health drops, boss patterns — all three difficulty levels.
- Completion percentage: crystals + bosses + hidden areas. Displayed on save screen and ending.

**Phase 14 (Units 417-448): Testing Matrix**
- A500 (OCS, 512KB chip) — minimum spec
- A500 (OCS, 1MB chip) — common config
- A500+ (ECS, 1MB chip)
- A600 (ECS, 1MB chip + possible HD)
- A1200 (AGA, 2MB chip) — enhanced visuals
- A4000 (AGA, 68040) — fastest
- Each configuration: all 5 islands, all bosses, all difficulties, floppy and HD boot

**Phase 15 (Units 449-480): Distribution Formats**
- Bootable ADF (1 or 2 disks) for floppy users
- WHDLoad package for HD users
- AGA-optimised version detection (same disk, auto-detected)
- Loading screen (OCS or AGA, auto-selected)
- Installer script for hard disk copy

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Result |
|------|---------|--------|
| 481-488 | Final ending polish: the Horizon blazes, islands reconnect, dawn breaks. On AGA: HAM8 sunrise. | Climax |
| 489-492 | Documentation: game guide, controls, model compatibility notes | Player support |
| 493-496 | OCS final test pass | A500 release quality |
| 497-500 | AGA final test pass | A1200 release quality |
| 501-504 | Cross-model edge cases | Timing, DMA, palette, fast RAM | Bulletproof |
| 505-508 | ADF + WHDLoad packages | All distribution formats | Distribution |
| 509-512 | **Complete game** | **Ship it** |

---

## The Amiga Arc

| Game | Chipset focus | Display paradigm | Scale | Emotion |
|------|-------------|-----------------|-------|---------|
| Exodus | Blitter as gameplay | Single playfield, bitmap terrain | Fixed-screen puzzle | Discovery, creativity |
| Duskfall | Copper + dual playfield | Multi-layer parallax, BOBs | 5-stage side-scroller | Atmosphere, depth |
| Redline | Copper per-scanline | Pseudo-3D perspective road | 5-circuit racer | Speed, exhilaration |
| Horizons | Everything + AGA | OCS→AGA bridging, HAM8 | 5-island action game | Wonder, mastery |

The learner starts by setting a Copper colour. They end by detecting the chipset generation, rendering HAM8 images, and shipping a game that runs on every Amiga ever made. From the simplest register write to the most advanced display mode — the Amiga fully explored.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. Amiga assembly capstone. Scrolling action bridging OCS to AGA with chipset detection, HAM8, and cross-model compatibility.
