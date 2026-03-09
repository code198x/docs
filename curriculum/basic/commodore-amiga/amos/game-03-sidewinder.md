# AMOS Game 03: Sidewinder

**Track:** AMOS
**Genre:** Side-scrolling action game
**Units:** 64 (4 phases × 16 units)
**Language:** AMOS Professional
**Max lines:** ~500

---

## Premise

A side-scrolling action game where the background moves and enemies appear from the right. The player navigates, dodges, and shoots through a scrolling landscape. AMOS's Screen Offset command provides hardware scrolling — the same scroll registers the assembly track programs directly. The learner sees the connection between AMOS commands and hardware behaviour.

---

## Core Mechanics

### Hardware Scrolling

AMOS's `Screen Offset` writes to Agnus's scroll registers. The background bitmap is wider than the visible screen; shifting the offset slides the viewport. This is real hardware scrolling — the same technique Shadow of the Beast uses — wrapped in a friendlier API.

### Tile-Based World

The world is a strip of tiles extending to the right. As the viewport scrolls, new tile columns are drawn at the leading edge (off-screen, before they scroll into view). The learner builds a level streaming system.

### The Player

A BOB that moves in 8 directions. Joystick controlled. Can fire projectiles right. The player stays on screen while the world scrolls beneath.

### Enemies

BOBs that enter from the right edge. Types:
- **Drifter**: floats across, no threat unless player collides
- **Swooper**: dives toward player, then exits
- **Turret**: fixed position in the world, fires left
- **Boss**: large, multi-hit, end-of-level

### Parallax

Two background layers scrolling at different speeds. AMOS Dual Screen or layered Screen Offset. The mountains move slowly; the foreground scrolls fast. This is the parallax effect that defines Amiga visuals.

---

## Phase Breakdown

### Phase 1: Scrolling World (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Wide Screen | Screen Open with a bitmap wider than 320 pixels. Screen Offset shifts the view. The world moves. | Screen Open, Screen Offset, bitmap width |
| 2 | Smooth Scroll | Increment Screen Offset each frame. Smooth, continuous rightward scroll. Wait Vbl for sync. | Frame-based scrolling, Wait Vbl |
| 3 | Tile Data | Level as an array of tile codes. Each column is a vertical strip of tiles. | Array-based level data |
| 4 | Drawing Tiles | Draw tiles at the leading edge of the scroll (just off-screen right). As the viewport advances, they scroll into view. | Tile streaming, edge drawing |
| 5 | Level from DATA | Read tile columns from DATA statements. A full level in data. | DATA-driven level |
| 6 | Terrain Variety | Multiple tile types: sky, ground, platforms, walls. Different images per tile. | Tile variety, sprite sheet |
| 7 | The Player | A BOB that moves in 8 directions. Stays within screen bounds while the world scrolls. | Player BOB, bounded movement |
| 8 | Joystick Control | Joy(1) for movement. Smooth, responsive. Player moves relative to the screen, not the world. | Joystick, screen-relative positioning |
| 9 | Ground Collision | Player can't move below the ground tiles. Check tile data at player position. | Tile collision, world-space lookup |
| 10 | Parallax Layer | A second screen at half scroll speed. Mountains or clouds behind the action. Dual screen or layered offset. | Parallax via dual Screen Offset |
| 11 | Scroll Speed | Variable scroll speed. Slow sections for exploration, fast for action. | Speed as parameter |
| 12 | Level End | The level has a defined length. Reaching the end = level complete. | Level length, completion |
| 13 | Three Levels | Three level DATA sets with different terrain and scroll speeds. | Multiple levels |
| 14 | Level Transition | Fade between levels (palette manipulation). Brief title card: "LEVEL 2: THE CANYON". | Palette fade, inter-level pacing |
| 15 | Background Decoration | Clouds, stars, or particles in the parallax layer. Moving elements that aren't gameplay-relevant. | Decorative elements, visual depth |
| 16 | Scrolling Polish | Smooth, tear-free scrolling with parallax. The world feels large and continuous. | Integration, polish |

**Milestone:** A smoothly scrolling world with parallax, tile-based terrain, and player movement. Three levels. Looks like a real Amiga side-scroller.

### Phase 2: Action (Units 17-32)

Enemies, shooting, and combat.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Bullets | Fire button → bullet BOB moves right. Off-screen → deactivate. | Projectile lifecycle |
| 18 | Enemy Drifters | BOBs enter from right, drift left, exit. Collision with player = damage. | Enemy spawning, horizontal movement |
| 19 | Enemy Collision | Bullet hits enemy → explosion BOB, enemy removed, score. Bob Col for detection. | Bullet-enemy collision |
| 20 | Player Damage | Enemy hits player → flash, lose health/life. Brief invincibility after hit. | Damage, invincibility frames |
| 21 | Swoopers | Enemies that dive toward the player's Y position before exiting. More dangerous. | Tracking movement, dive patterns |
| 22 | Turrets | Fixed in the world (scroll with terrain). Fire leftward projectiles the player must dodge. | World-fixed enemies, enemy bullets |
| 23 | Spawn Timing | Enemies spawn based on scroll position (DATA defines: at column 50, spawn swooper at Y=100). | Position-triggered spawning |
| 24 | Health Bar | Player health as a bar (Ink, Bar commands). Depletes on hits. | Health display |
| 25 | Power-Ups | Dropped by enemies: speed boost, rapid fire, shield. BOBs fall downward, collect on touch. | Power-up drops, timed effects |
| 26 | Boss Fight | End of level 1: scrolling stops. Large multi-BOB boss. Pattern attacks. Must be hit 10 times. | Boss encounter, scroll pause |
| 27 | Boss Patterns | Boss moves in a pattern (sine wave, charge, retreat). Fires projectiles. Has a weak point. | Pattern AI, multi-phase boss |
| 28 | Level 1 Complete | Beat the boss → level complete. Score bonus, fanfare. | Victory sequence |
| 29 | Levels 2-3 Enemies | Different enemy types and spawn patterns per level. Level 3 boss is harder. | Per-level enemy design |
| 30 | MOD Music | Track Load, Track Play. Music during levels. Different track per level. | MOD playback |
| 31 | SFX Over Music | Sample Play for gunshots and explosions. Channel allocation so SFX don't kill the music. | Audio channel management |
| 32 | Three Levels Playable | Scrolling, shooting, enemies, bosses, music. A real side-scrolling shooter. | Integration milestone |

**Milestone:** A complete side-scrolling shooter with parallax, enemies, bosses, power-ups, and MOD music. Three levels.

### Phase 3: Depth and Phase 4: Polish (Units 33-64)

Additional levels (6 total), difficulty select, high scores, attract mode, title screen, visual effects (copper gradients, palette animation), and a level editor for creating custom levels. Testing, balance, and final line count review.

Key additions:
- 6 levels total with escalating difficulty
- Copper gradient skies per level
- Screen shake on boss hits
- Attract mode with automated player
- Difficulty select (Easy/Normal/Hard)
- High score table
- The connection between Screen Offset and hardware scroll registers (educational bridge to assembly)

---

## Technical Notes

### Screen Offset and Hardware

`Screen Offset 0, X, 0` writes to BPLxPT (bitplane pointers) and BPLCON1 (fine scroll). The learner uses one AMOS command that maps to the same registers the assembly track programs directly. This makes the assembly transition conceptually small.

### Parallax Implementation

```basic
' Two screens at different scroll speeds
Screen Open 0, 640, 256, 16, Lowres  : ' Foreground (double width)
Screen Open 1, 640, 256, 8, Lowres   : ' Background

Do
  Screen Offset 0, SCROLL_X, 0       : ' Foreground: full speed
  Screen Offset 1, SCROLL_X/2, 0     : ' Background: half speed
  Add SCROLL_X, 2
  Wait Vbl
Loop
```

### Tile Streaming

New tiles are drawn just off-screen:

```basic
' When scroll reveals a new column
If SCROLL_X Mod TILE_WIDTH = 0
  COLUMN = SCROLL_X / TILE_WIDTH + VISIBLE_COLUMNS
  Screen 0
  For ROW = 0 To GRID_HEIGHT-1
    ' Draw tile from level data at (COLUMN, ROW)
    Paste Bob COLUMN*TILE_WIDTH, ROW*TILE_HEIGHT, TILE_IMAGE(LEVEL_DATA(COLUMN, ROW))
  Next ROW
End If
```

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old AMOS games 3-7 with a focused scrolling action game teaching Screen Offset and parallax.
