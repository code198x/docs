# Full Game Outline: C64 Sidereal (512 Units)

**Game:** Sidereal (Game 4 — Capstone)
**Units:** 512 (16 phases × 32 units)
**Genre:** Action-platformer with demo-scene polish
**Inspired by:** Creatures, Mayhem in Monsterland, Thalamus releases, demo-scene productions
**Target Quality:** Late-era showcase (1992–93 era)

---

## Premise

The stars are shifting. Ancient constellations have broken apart, scattering fragments of celestial light across five realms. Each realm reflects a different sky: the Verdant (emerald canopy beneath green stars), the Azure (frozen coast under blue constellations), the Gilded (desert ruins under golden suns), the Crimson (volcanic peaks beneath red giants), and the Sidereal (the void between stars, where the constellations must be restored).

You are a starkeeper — quick, agile, bright against the darkness. Collect the light fragments, restore the constellations, and return the sky to order. Each realm is a side-scrolling platformer with puzzles, secrets, and a guardian constellation gone wrong.

The game itself is a love letter to the C64. Demo-scene effects in the title sequence and transitions. A Chris Hülsbeck-style SID soundtrack. Raster tricks that make the borders disappear. A fast loader that plays music while loading. Direct 1541 drive programming. 6581/8580 SID detection. PAL/NTSC adaptation. Dual distribution on D64 and tape. Everything the C64 can do, in one game.

---

## Why This Is the Capstone

Sidereal requires every technique from Games 1-3 plus the production craft that separates a game from a product:

| From Game | Technique | Use in Sidereal |
|-----------|-----------|----------------|
| Nova Storm | Sprites, SID basics, raster IRQs | Player sprites, sound effects, stable timing |
| Nova Storm | Sprite multiplexing (introduced) | Background particles, collectible fragments |
| Coldframe | Hardware scrolling, colour RAM sync | Side-scrolling realms |
| Coldframe | Large sprite animation | Starkeeper walk/jump/collect animations |
| Coldframe | SID atmosphere | Per-realm ambient soundscapes |
| Warfront | 8-way scrolling, tile streaming | Realm world data, vertical sections |
| Warfront | Full sprite multiplexing | 20+ objects during boss encounters |
| Warfront | Advanced SID, multi-speed music | Full soundtrack with digi-drums |
| Warfront | Boss state machines | Constellation guardians |

**New in Sidereal:**
- **Demo-scene effects:** FLD (Flexible Line Distance), DYCP (Different Y Character Positions), AGSP (Any Given Screen Position), raster bars, tech-tech, open borders
- **Fast loader with music:** IRQ-driven loading routine that plays SID music while data transfers from disk
- **Direct 1541 drive programming:** Send custom code to the drive's 6502 for maximum transfer speed
- **6581/8580 SID detection:** Detect which SID revision is installed, adjust filter and combined waveform behaviour
- **PAL/NTSC detection and adaptation:** CIA timer comparison, speed calibration
- **Loading screen:** Displayed during tape/disk load — the first thing the player sees
- **Dual distribution:** Same game on D64 (disk) and tape with turbo loader
- **Open borders:** Remove the top/bottom border for full-screen display in title sequence

---

## The Five Realms

| Realm | Setting | Palette | Scroll | Signature effect |
|-------|---------|---------|--------|-----------------|
| 1: Verdant | Forest canopy, mossy ruins, streams | Green/brown | Horizontal | Parallax tree layers, leaf particles |
| 2: Azure | Frozen coast, ice caves, aurora | Blue/white/cyan | Horizontal + vertical (ice slides) | Colour-cycling aurora in border area |
| 3: Gilded | Desert ruins, sandstorms, oasis | Yellow/orange/brown | Horizontal | Heat shimmer (raster wobble effect) |
| 4: Crimson | Volcanic peaks, lava rivers, ember rain | Red/orange/black | Horizontal + vertical (climbing) | Lava glow (colour RAM cycling) |
| 5: Sidereal | The void, floating platforms, starfields | Black/white/all colours | All directions | Open borders, full-screen star parallax |

Each realm: 3 scrolling stages + guardian boss. Realm 5 (Sidereal) uses every visual technique as a finale.

---

## Core Mechanics

### Platforming

The starkeeper runs, jumps, and wall-kicks through scrolling landscapes. Movement is fast and fluid — closer to Mayhem in Monsterland than Turrican. The focus is on momentum: running builds speed, jumps carry forward, wall-kicks redirect. The player feels like light.

### Collection

Celestial fragments are scattered through each realm. Collect enough to restore the realm's constellation (displayed as a connect-the-dots pattern that fills in as fragments are collected). Collecting all fragments in a realm unlocks a bonus stage.

### Puzzle Elements

Some fragments are behind environmental puzzles: push a block to bridge a gap, activate a switch to open a path, redirect a beam of light to unlock a door. Puzzles are brief — 30 seconds to a minute — and never halt the game's momentum.

### Guardians

Each realm's guardian is a corrupted constellation: a multi-sprite boss built from star patterns. The Verdant guardian is a tree-constellation that drops root attacks. The Azure guardian is an ice-bird constellation that swoops. Each has learnable patterns and a weak point.

---

## Phase Breakdown

### Phases 1-4: The Game (Units 1–128)

**Phase 1 (Units 1-32): Scrolling Platformer**
Side-scrolling platformer with the starkeeper. Smooth horizontal scroll (from Coldframe/Warfront techniques). Tile-based terrain. Gravity, jumping, wall-kick. Fragment collection. One complete realm (Verdant) with 3 stages.

**Phase 2 (Units 33-64): Enemies and Combat**
Realm-specific enemies. The starkeeper attacks with a short-range light burst (not a projectile — contact range). Enemy variety per realm. Fragment collection gates progression. Two more realms (Azure, Gilded) with stages and guardians.

**Phase 3 (Units 65-96): Advanced Mechanics**
Wall-kick mastery. Vertical scrolling sections (ice slides in Azure, climbing in Crimson). Environmental puzzles. Realm 4 (Crimson) complete. Advanced enemy patterns.

**Phase 4 (Units 97-128): The Sidereal**
Realm 5: multi-directional scrolling through the void. Floating platforms in starfield. All techniques combined. Final guardian. The constellation restoration ending. Game content complete.

**End of Phase 4:** 5 realms, 15 stages, 5 guardians. A complete action-platformer. 48K playable.

---

### Phases 5-8: Sound and Visuals (Units 129–256)

**Phase 5 (Units 129-160): SID Soundtrack**
Multi-speed music engine (from Warfront). Per-realm themes reflecting each palette:
- Verdant: flowing, organic, major key
- Azure: crystalline, sparse, ethereal
- Gilded: rhythmic, percussive, ancient
- Crimson: driving, intense, minor key
- Sidereal: ambient building to triumphant

Digi-drums for percussion. Filter automation synced to gameplay events.

**Phase 6 (Units 161-192): SID Polish**
6581/8580 detection: the two SID revisions have different filter characteristics and combined waveform behaviour. Detect at startup, adjust filter cutoff curves and waveform tables accordingly. Both models sound their best.

Sound effect library refined: fragment collection (ascending chime, different pitch per fragment count), wall-kick (sharp percussive), guardian damage (deep resonant hit), death (descending filter sweep), realm-clear (triumphant three-voice chord).

**Phase 7 (Units 193-224): Raster Visual Effects**
- Parallax scrolling via raster splits (background layer at half scroll speed)
- Colour-cycling aurora for Azure realm (palette rotation in the border area)
- Heat shimmer for Gilded realm (horizontal raster wobble — $D016 fine scroll varies per scanline)
- Lava glow for Crimson realm (colour RAM red-channel cycling)
- Full-screen starfield for Sidereal realm (open top/bottom borders via $D011 timing trick)

**Phase 8 (Units 225-256): Visual Polish**
Player animation refined (8+ frames per action, smooth transitions). Enemy animation. Guardian multi-sprite assembly. Explosion particles. Screen shake. Constellation display (connect-the-dots overlay). Realm transition effects (palette fade, colour wipe).

**End of Phase 8:** Full soundtrack, per-realm visual effects, polished animation. The game looks and sounds like a late-era Thalamus release.

---

### Phases 9-12: Demo-Scene Craft (Units 257–384)

**Phase 9 (Units 257-288): Title Sequence**
The title sequence is a demo-scene production:
- Open top/bottom borders (full-screen display) via $D011 timing
- Raster bars: horizontal colour stripes that flow down the screen, each a different $D020/$D021 write per scanline
- DYCP (Different Y Character Positions): each character in "SIDEREAL" bobs independently using FLD (Flexible Line Distance)
- Tech-tech: two overlapping sine-wave text scrollers using AGSP
- Starfield parallax behind everything

This isn't gratuitous — it demonstrates mastery of VIC-II timing at a level that commands respect. The demo-scene IS the C64 community, and the title sequence speaks its language.

**Phase 10 (Units 289-320): Demo Effects Deep Dive**
- **FLD (Flexible Line Distance):** Manipulate $D011 to skip badlines, creating gaps in the display. Used for vertical text positioning in the title.
- **AGSP (Any Given Screen Position):** Trigger raster effects at arbitrary positions. Used for overlapping text layers.
- **Open borders:** Suppress the border blanking by changing $D011 at the exact right moment. Sprites display in the border area.
- **Colour washing:** Rapidly cycle all 16 palette entries to create a "washing" effect over existing graphics.

Each effect is taught as a standalone technique, then integrated into the title sequence.

**Phase 11 (Units 321-352): Fast Loader**
- Standard Kernal tape loader: ~1500 baud. Unacceptable for a multi-load game.
- Custom turbo tape loader: 3000-6000 baud. Halves load time.
- Custom disk loader: faster than Kernal by reading sectors directly.
- **IRQ loader:** The game continues running (SID music plays) while data loads in the background. CIA timer interrupt drives the disk read.
- Music during load: a dedicated SID routine plays independently of the game engine while the loader transfers data.

**Phase 12 (Units 353-384): Direct Drive Programming**
- The 1541 disk drive contains its own 6502 CPU and 2KB RAM.
- Send a custom fast-load routine to the drive via the serial bus.
- The drive-side routine reads data at maximum speed and sends it to the C64 in burst mode.
- This is the fastest possible transfer: ~10× the Kernal speed.
- The routine is small (~200 bytes of drive-side 6502 code) and loaded once at game start.

**End of Phase 12:** Demo-scene title sequence, fast loader with music, direct drive programming. The production craft that defines the C64's commercial peak.

---

### Phases 13-16: Production (Units 385–512)

**Phase 13 (Units 385-416): Multi-Load Architecture**
- Title + Realm 1 load first. Player plays Realm 1.
- At realm transition: fast-load Realm 2 data (tiles, enemies, music) while transition animation plays.
- The player never sees a loading screen mid-game — loading is masked by realm transitions.
- Tape version: multi-load with turbo loader. Each realm is a tape block.
- Disk version: random-access loading. Any realm loads in ~3 seconds via fast loader.

**Phase 14 (Units 417-448): Compatibility**
- PAL/NTSC detection via CIA timer comparison. Adjust frame timing, scroll speed, music tempo.
- 6581/8580 SID detection via combined waveform test. Adjust filter curves.
- Testing across configurations: PAL+6581 (European C64), PAL+8580 (C64C), NTSC+6581 (American C64), NTSC+8580 (late American C64).
- C128 compatibility check (runs in C64 mode).

**Phase 15 (Units 449-480): Distribution**
- D64 disk image: boot sector, fast-loader installer, realm data files, loading screen.
- TAP tape image: turbo-encoded blocks, multi-load structure, loading screen between blocks.
- Loading screen: hand-crafted character art displayed during initial load. Sets the mood before gameplay.
- .PRG autostart via BASIC stub (`10 SYS 2061`).
- Crunched/compressed binary for minimum load size.

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Result |
|------|---------|--------|
| 481-488 | Ending sequence: constellations restored, the sky reforms, the starkeeper ascends | Narrative climax |
| 489-492 | High scores with initials, difficulty select (3 levels) | Competition |
| 493-496 | Attract mode with demo-scene title, gameplay demo | Professional presentation |
| 497-504 | Final testing: all realms, all difficulties, PAL/NTSC, 6581/8580, disk/tape | Release quality |
| 505-508 | Inlay text, documentation, credits embedded in binary | Professional package |
| 509-512 | **Complete game** — D64, TAP, .PRG | **Ship it** |

---

## The C64 Arc

| Game | Setting | Technique | Emotion |
|------|---------|-----------|---------|
| Nova Storm | Space battle | Sprites, SID, raster basics | Action, excitement |
| Coldframe | Underground complex | Scrolling, large sprites, atmosphere | Tension, stealth |
| Warfront | Five war zones | 8-way scroll, multiplexing, advanced SID | Power, intensity |
| Sidereal | Celestial realms | Everything + demo-scene + production | Wonder, mastery |

The learner starts by putting a sprite on screen. They end by programming the disk drive's CPU, opening the borders, and shipping a game on two formats with a demo-scene title sequence. The C64 has been fully explored — from the simplest register write to the most advanced timing tricks the scene ever invented.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. C64 assembly capstone. Action-platformer combining all previous techniques with demo-scene effects, fast loader, direct drive programming, and multi-format distribution.
