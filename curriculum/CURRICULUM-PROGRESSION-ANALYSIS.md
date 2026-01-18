# Curriculum Progression Analysis

**Purpose:** Analyse skill progression after restructuring Game 1 to shooters across all platforms.

**Problem:** The former Game 1s (SID Symphony, Ink War, Neon Nexus, Signal) may not fit as Game 2 because:
1. Some skills are now redundant (already taught in shooter)
2. Some games feel like a step backward in complexity
3. Some are actually more advanced than they appeared

---

## Skill Pillars by Platform

### Commodore 64

| Pillar | When Introduced |
|--------|-----------------|
| Sprites & collision | Game 1 (Starfield) ✓ |
| Joystick input | Game 1 ✓ |
| SID basics (effects) | Game 1 ✓ |
| SID deep dive (music, ADSR) | Later |
| Character graphics / tiles | Needed |
| Platforming physics | Needed |
| Horizontal scrolling | Needed |
| Vertical scrolling | Needed |
| Raster effects | Needed |
| Sprite multiplexing | Needed |
| Disk I/O | Needed |

**Recommended Game 2:** Platforming (jump physics, gravity, tile collision) - introduces major new concepts.

**Where does SID Symphony fit?**
- Rhythm games require timing precision, multi-voice orchestration, keyboard matrix reading
- These are intermediate-to-advanced skills
- **Recommendation:** Move to Game 6-8 range, positioned as a "change of pace" between action games

---

### ZX Spectrum

| Pillar | When Introduced |
|--------|-----------------|
| Screen memory layout | Game 1 (Skyfire) ✓ |
| Attribute system | Game 1 ✓ |
| Keyboard input | Game 1 ✓ |
| Beeper basics | Game 1 ✓ |
| Sprite masking | Game 1 ✓ |
| Custom fonts | Needed |
| Smooth sub-cell movement | Needed |
| Ball/physics simulation | Needed |
| Scrolling techniques | Needed |
| Tape/disk I/O | Needed |

**Recommended Game 2:** Breakout (Shatter) - introduces ball physics, reflection angles, sub-cell movement.

**Where does Ink War fit?**
- Turn-based strategic gameplay is a different paradigm
- AI decision-making is a valuable skill but not urgent
- **Recommendation:** Move to Game 5-6 range, after learners have more action game experience

---

### Nintendo NES

| Pillar | When Introduced |
|--------|-----------------|
| PPU setup | Game 1 (Stellar Barrage) ✓ |
| Nametables/backgrounds | Game 1 ✓ |
| Sprites/OAM | Game 1 ✓ |
| Controller input | Game 1 ✓ |
| Collision detection | Game 1 ✓ |
| APU basics | Game 1 ✓ |
| Sprite limit management | Game 1 ✓ |
| Gravity/platforming | Needed |
| Tile-based collision | Needed (partial in shooter) |
| Hardware scrolling | Needed |
| Mappers | Needed |

**Recommended Game 2:** Platformer (Crate Escape) - introduces gravity, jump physics, platform collision.

**Where does Neon Nexus fit?**
- Fixed-screen collect-em-up with simpler mechanics
- Many skills now redundant with shooter
- **Recommendation:** Either merge into another game OR move much later as a "puzzle-action" variant OR remove entirely

---

### Commodore Amiga

| Pillar | When Introduced |
|--------|-----------------|
| 68000 basics | Game 1 (Blast Zone) ✓ |
| Display/Copper basics | Game 1 ✓ |
| Hardware sprites | Game 1 ✓ |
| BOBs/Blitter basics | Game 1 ✓ |
| Paula samples | Game 1 ✓ |
| Bootable ADF | Game 1 ✓ |
| Collision detection | Game 1 ✓ |
| Deeper Blitter work | Needed |
| Copper effects | Needed (basics in G1) |
| Platforming physics | Needed |
| Scrolling | Needed |
| Dual playfield | Needed |
| MOD music playback | Needed |

**Recommended Game 2:** Platformer or Frogger-style (Signal) - introduces timing-based gameplay, different movement model.

**Where does Signal fit?**
- Frogger-style lane-crossing is legitimately different from shooter
- Teaches timing, patience, different collision model
- **Recommendation:** Could stay as Game 2 (it works), OR move to Game 3 if we want platforming sooner

---

## Proposed Reordering

### C64 Revised Sequence (Games 1-10)

| Game | Name | New Concept | Notes |
|------|------|-------------|-------|
| 1 | Starfield | Shooter fundamentals | 128 units |
| 2 | Platform Panic | Gravity, jumping, platforms | Was Game 4 |
| 3 | Maze Raider | Tile maps, pathfinding AI | Was Game 3 |
| 4 | Brick Basher | Ball physics, angles | Was Game 5 |
| 5 | Invader Wave | Formations, shields | Was Game 6 |
| 6 | **SID Symphony** | Deep SID, rhythm timing | Was Game 1 |
| 7 | Scroll Runner | Horizontal scrolling | Was Game 7 |
| 8 | Night Raid | Scrolling + shooting | Was Game 8 |
| 9 | Sprite Storm | Multiplexing | Was Game 9 |
| 10 | Raster Rider | Pseudo-3D, raster | Was Game 10 |

**Changes:** SID Symphony moved from 1→6. Platform Panic moved from 4→2.

---

### ZX Spectrum Revised Sequence (Games 1-10)

| Game | Name | New Concept | Notes |
|------|------|-------------|-------|
| 1 | Skyfire | Shooter fundamentals | 128 units |
| 2 | Shatter | Ball physics, sub-cell | Was Game 3 |
| 3 | Cavern | Platforming, gravity | Was Game 4 |
| 4 | Byte Biter | Snake, ring buffers | Was Game 5 |
| 5 | **Ink War** | Strategy, AI decisions | Was Game 1 |
| 6 | Block Drop | Falling pieces, rotation | Was Game 6 |
| 7 | Spectrum Racer | Pseudo-3D road | Was Game 7 |
| 8 | Maze Master | Scrolling maze | Was Game 8 |
| 9 | Platform Plus | Scrolling platformer | Was Game 9 |
| 10 | Alien Assault | Run'n'gun | Was Game 10 |

**Changes:** Ink War moved from 1→5. Shatter moved from 3→2. Cavern moved from 4→3.

---

### NES Revised Sequence (Games 1-10)

| Game | Name | New Concept | Notes |
|------|------|-------------|-------|
| 1 | Stellar Barrage | Shooter fundamentals | 128 units |
| 2 | Crate Escape | Platforming, gravity | Was Game 3 |
| 3 | Fracture Point | Ball physics | Was Game 4 |
| 4 | Pellet Panic | Maze, tile collision | Was Game 5 |
| 5 | Crypt Crawler | Multi-room, exploration | Was Game 6 |
| 6 | Fangs for Memory | Snake, ring buffers | Was Game 7 |
| 7 | Gridlock | Falling blocks, rotation | Was Game 8 |
| 8 | Pixel Plains | Hardware scrolling | Was Game 9 |
| 9 | Ion Trail | Scrolling shooter | Was Game 10 |
| 10 | **(New or merged)** | TBD | |

**Changes:** Neon Nexus removed (redundant with Stellar Barrage). Crate Escape moved from 3→2. Consider adding a new Game 10 or redistributing content.

**Alternative:** Keep Neon Nexus as a shorter "bonus" or "practice" project between major games.

---

### Amiga Revised Sequence (Games 1-8)

| Game | Name | New Concept | Notes |
|------|------|-------------|-------|
| 1 | Blast Zone | Shooter fundamentals | 128 units |
| 2 | Signal | Timing, lane mechanics | Unchanged |
| 3 | Shatter Point | Ball physics | Was Game 3 |
| 4 | Jungle Leap | Platforming | Was Game 4 |
| 5 | Maze Mind | Tile maps, AI | Was Game 5 |
| 6 | Block Blitz | Falling pieces | Was Game 6 |
| 7 | Copper Chase | Racing, copper effects | Was Game 7 |
| 8 | Dungeon Delve | Multi-room adventure | Was Game 8 |

**Changes:** Signal stays at Game 2 (it works well as a different gameplay style). Sequence otherwise unchanged.

---

## Key Principles

1. **Each game introduces genuinely new concepts** - no "review" games
2. **Complexity should increase** - never feel like stepping backward
3. **Genre variety maintains interest** - alternate between action, puzzle, strategy
4. **Platform features drive ordering** - scrolling before multiplexing, tiles before scrolling
5. **Former "intro" games move to where their complexity fits** - not arbitrary placement

---

## Questions for Review

1. **NES: What replaces Neon Nexus?** Merge its content elsewhere, or create new Game 10?
2. **C64: Is Game 6 the right spot for SID Symphony?** Could be earlier (5) or later (7-8).
3. **ZX Spectrum: Is Game 5 right for Ink War?** The strategic gameplay is quite different.
4. **All platforms: Should there be "mini-games" between major titles?** Quick 16-32 unit projects to reinforce skills without major new content?

---

**Version:** 1.0
**Created:** 2026-01-18
