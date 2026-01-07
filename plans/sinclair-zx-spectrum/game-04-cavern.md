# Cavern: 64-Unit Outline

**Game:** 4 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer in the Manic Miner tradition. Platforms, hazards, collectibles, air supply.

---

## Why This Game Fourth?

Cavern introduces platformer physics - gravity, jumping, and platform collision. The Spectrum was home to legendary platformers (Manic Miner, Jet Set Willy), and this game teaches the fundamentals:

1. **Gravity** - Constant downward force
2. **Jump physics** - Velocity, arc, landing
3. **Platform collision** - Standing on, bumping into
4. **Tile-based levels** - Efficient level design
5. **Hazards** - Enemies and dangers to avoid

This is the foundation for scrolling platformers later in the curriculum.

---

## Skills Applied from Previous Games

| Skill | From | Application in Cavern |
|-------|------|---------------------|
| Screen memory | Ink War | Level graphics |
| Attributes | Ink War | Platform colours |
| Software sprites | Shatter | Player character |
| Pixel movement | Shatter | Smooth player motion |
| Collision detection | Shatter/Skyfire | Platform and hazard collision |
| Object arrays | Skyfire | Enemy management |
| Frame timing | Shatter | Consistent physics |
| Sound effects | Shatter/Skyfire | Jump, collect, death sounds |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Gravity simulation | 1 | Constant downward velocity |
| Jump physics | 2 | Variable height jumping |
| Platform collision | 2 | Standing on surfaces |
| Tile-based levels | 1 | Efficient level storage |
| Player animation | 2 | Walk cycle, jump frame |
| Hazard collision | 3 | Deadly objects |
| Collectibles | 3 | Items to gather |
| Air supply | 3 | Time pressure mechanic |

---

## Phase 1: Level Foundation (Units 1-16)
*Tile-based level display.*

### Units 1-4: Tile System
- **Unit 1:** Tile concept - 8×8 character cells as level building blocks
- **Unit 2:** Tile types - empty, solid, platform, hazard, collectible
- **Unit 3:** Level data format - byte array representing tile grid
- **Unit 4:** Tile graphics - designing tile appearance

### Units 5-8: Level Display
- **Unit 5:** Level rendering - draw tiles to screen
- **Unit 6:** Tile type lookup - identify tile at position
- **Unit 7:** Multiple tile graphics - variety in appearance
- **Unit 8:** Attribute colouring - coloured platforms and walls

### Units 9-12: Player Character
- **Unit 9:** Player sprite design - miner character
- **Unit 10:** Walk animation frames - 4-frame walk cycle
- **Unit 11:** Standing and jumping frames - additional poses
- **Unit 12:** Direction facing - left/right sprite flip

### Units 13-16: Basic Level
- **Unit 13:** First level design - platforms, walls, collectibles
- **Unit 14:** Level boundary - walls on edges
- **Unit 15:** Complete level display - all tiles visible
- **Unit 16:** Player positioned - starting location

**Phase Goal:** Display a complete platformer level with animated player.

---

## Phase 2: Movement and Physics (Units 17-32)
*Gravity, jumping, and platform collision.*

### Units 17-20: Horizontal Movement
- **Unit 17:** Left/right input - keyboard reading
- **Unit 18:** Horizontal velocity - smooth acceleration
- **Unit 19:** Wall collision - stop at solid tiles
- **Unit 20:** Walk animation triggering - animate while moving

### Units 21-24: Gravity
- **Unit 21:** Gravity constant - downward acceleration
- **Unit 22:** Falling state - apply gravity when not on ground
- **Unit 23:** Terminal velocity - maximum fall speed
- **Unit 24:** Ground detection - check tile below player

### Units 25-28: Jumping
- **Unit 25:** Jump input - fire button or up
- **Unit 26:** Jump velocity - initial upward speed
- **Unit 27:** Jump arc - gravity reduces upward velocity
- **Unit 28:** Variable jump height - tap vs hold for height

### Units 29-32: Platform Collision
- **Unit 29:** Landing on platforms - stop falling, stand on surface
- **Unit 30:** Head collision - bump ceiling, stop rising
- **Unit 31:** One-way platforms - can jump through from below
- **Unit 32:** Complete physics - smooth platforming feel

**Phase Goal:** Smooth platformer movement with gravity and jumping.

---

## Phase 3: Game Elements (Units 33-48)
*Hazards, collectibles, and game rules.*

### Units 33-36: Collectibles
- **Unit 33:** Key/gem objects - items to collect
- **Unit 34:** Collection detection - player touches item
- **Unit 35:** Item removal - disappear when collected
- **Unit 36:** Collection counter - track collected items

### Units 37-40: Hazards
- **Unit 37:** Static hazards - spikes, fire, water
- **Unit 38:** Hazard collision - player death on contact
- **Unit 39:** Moving hazards - patrolling enemies
- **Unit 40:** Enemy movement patterns - back and forth

### Units 41-44: Air Supply
- **Unit 41:** Air meter - depleting resource
- **Unit 42:** Air display - visual meter bar
- **Unit 43:** Air depletion - constant drain over time
- **Unit 44:** Air death - game over when empty

### Units 45-48: Level Completion
- **Unit 45:** Exit portal - level end location
- **Unit 46:** Exit condition - all collectibles required
- **Unit 47:** Level transition - clear and load next level
- **Unit 48:** Complete game loop - play through levels

**Phase Goal:** Full game mechanics with hazards and objectives.

---

## Phase 4: Polish and Release (Units 49-64)
*Multiple levels, presentation, release.*

### Units 49-52: Multiple Levels
- **Unit 49:** Level 2 design - new layout
- **Unit 50:** Level 3 design - increased difficulty
- **Unit 51:** Level 4 design - new hazard types
- **Unit 52:** Level progression - unlocking sequence

### Units 53-56: Audio and Feedback
- **Unit 53:** Jump sound - beeper effect
- **Unit 54:** Collection sound - satisfying blip
- **Unit 55:** Death sound - descending tone
- **Unit 56:** Level complete jingle - success fanfare

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo and title
- **Unit 58:** Lives display - remaining lives shown
- **Unit 59:** Death sequence - explosion animation
- **Unit 60:** Game over screen - final message

### Units 61-64: Release
- **Unit 61:** Instructions screen - controls and rules
- **Unit 62:** Bug fixing - collision edge cases
- **Unit 63:** Level balance - difficulty tuning
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete platformer with multiple levels.

---

## Summary

**Cavern** teaches platformer fundamentals in the Manic Miner tradition:

**Phase 1 (Levels):** Tile-based display, player sprite, level structure.

**Phase 2 (Physics):** Gravity, jumping, platform collision - feels like a platformer.

**Phase 3 (Elements):** Collectibles, hazards, air supply - game has objectives.

**Phase 4 (Polish):** Multiple levels, sound, presentation - complete game.

### Skills Transferred Forward

The following skills debut in Cavern:

1. **Gravity simulation** → All platformers, physics games
2. **Jump physics** → Essential for action games
3. **Platform collision** → Exodus, Recoil, all platformers
4. **Tile-based levels** → Efficient level design throughout
5. **Player animation states** → Walk, jump, death in all games
6. **Collectible systems** → Items in many games
7. **Time pressure (air)** → Resource management games

### Classic Spectrum Heritage

Cavern pays homage to:
- **Manic Miner** (1983) - The original Spectrum platformer
- **Jet Set Willy** (1984) - Expanded exploration
- **Technician Ted** (1984) - Work-themed variation

These games defined the Spectrum platform - Cavern teaches their core techniques.

### Game Specifications

- **Screen:** Single-screen levels (no scrolling)
- **Tiles:** 32×24 grid of 8×8 tiles
- **Player:** 16×16 sprite with 4-frame walk cycle
- **Lives:** 3 per game
- **Levels:** 8 unique layouts
- **Collectibles:** 10-20 items per level (all required)
- **Hazards:** Spikes, fire, water, patrolling enemies
- **Air Supply:** 60 seconds per level (approx)
- **Controls:** Left, right, jump
- **Audio:** Beeper effects for all actions
- **Distribution:** TAP file
