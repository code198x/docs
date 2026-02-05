# Full Game Outline: C64 Platform Panic (128 Units)

**Game:** Platform Panic (Game 2)
**Platform:** Commodore 64
**Units:** 128 (8 phases × 16 units)
**Prerequisite:** Starfield (Game 1) - sprites, joystick, collision, SID basics
**Target Quality:** Polished single-screen platformer (Miner 2049er / Jumpman quality)

---

## What Carries Over from Game 1

Learners already know:
- Hardware sprites (enabling, positioning, colours)
- Joystick reading via CIA
- Sprite-to-sprite collision basics
- SID sound effects
- Game loop structure
- Score display

**What's NEW in this game:**
- Gravity and acceleration
- Jump physics (impulse, arc, landing)
- Tile-based collision (character graphics as platforms)
- Animation state machines
- Level data structures
- Multiple levels with progression

---

## Design Philosophy

- **Gravity from Unit 1** — the defining new mechanic
- **Jumping by Unit 4** — playable platformer early
- **One new concept per unit** — building complexity gradually
- **Debugging inline** — gravity bugs are common, address them
- **Polish by Unit 128** — a game worth showing off

---

## Phase 1: Basic Platforming (Units 1-16)

**Goal:** Player can run, jump, and land on platforms. Minimal but complete.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Player sprite + gravity | Falls to bottom of screen |
| 2 | Floor collision (ground) | Stops falling, stands |
| 3 | Left/right movement | Walk on ground |
| 4 | Jump (impulse) | **Can jump!** |
| 5 | Jump arc (gravity during jump) | Natural arc |
| 6 | Landing detection | Smooth landing |
| 7 | Platform tiles (characters) | Something to jump onto |
| 8 | Platform collision | **Land on platforms** |
| 9 | Walk off platform = fall | Feels right |
| 10 | Jump sound effect | Feedback |
| 11 | Land sound effect | Polish |
| 12 | Simple level layout | One complete screen |
| 13 | Exit/goal tile | Something to reach |
| 14 | Reach goal = level complete | **Playable game** |
| 15 | Level complete fanfare | Satisfaction |
| 16 | Integration + edge cases | Solid foundation |

**C64-Specific Unit 1:**
```asm
; Gravity - the foundation of platforming
; Player Y position increases each frame (falls down)

GRAVITY = 1         ; Pixels per frame (can be fractional later)

update_player:
    ; Apply gravity to velocity
    lda player_vel_y
    clc
    adc #GRAVITY
    sta player_vel_y

    ; Apply velocity to position
    lda player_y
    clc
    adc player_vel_y
    sta player_y

    ; Update sprite position
    sta $d001       ; Sprite 0 Y
    rts
```

**If it doesn't work (Phase 1):**
- **Player falls through floor?** Check collision detection order - test BEFORE moving
- **Jumps feel wrong?** Adjust GRAVITY and JUMP_IMPULSE constants
- **Stuck on platforms?** Ensure you're testing the player's FEET, not centre
- **Jittery landing?** Snap to platform top when landing, zero velocity

**End of Phase 1:** Basic platforming works. Jump, land, reach goal.

---

## Phase 2: Level Design (Units 17-32)

**Goal:** Multiple distinct levels with increasing challenge.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Level data format | Structured levels |
| 18 | Load level from data | Data-driven |
| 19 | Level 2 | Variety |
| 20 | Level 3 | Progression |
| 21 | Level transition | Flow |
| 22 | Lives system | Stakes |
| 23 | Fall off screen = death | Consequence |
| 24 | Death animation | Feedback |
| 25 | Respawn at level start | Try again |
| 26 | Game over screen | End state |
| 27 | Level 4 (harder jumps) | Challenge |
| 28 | Level 5 (precision required) | Skill test |
| 29 | Level counter display | Progress |
| 30 | Score display | Competition |
| 31 | Points for completing levels | Reward |
| 32 | Integration + balance | 5 solid levels |

**C64-Specific:**
- Levels stored as 40×25 character data (1000 bytes each)
- Use custom character set for platform tiles
- Screen RAM at $0400, character set at $2000
- Colour RAM for platform colours

**If it doesn't work (Phase 2):**
- **Level data corrupted?** Check address calculations, ensure data doesn't cross page boundaries
- **Character graphics wrong?** Verify character set address in $D018
- **Colours wrong?** Remember colour RAM is separate from screen RAM

**End of Phase 2:** 5 distinct levels, lives, death, game over.

---

## Phase 3: Hazards and Enemies (Units 33-48)

**Goal:** Things that kill you besides falling.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Static hazard (spikes) | Danger zones |
| 34 | Touch hazard = death | Consequence |
| 35 | Hazard graphics | Visual clarity |
| 36 | Moving platform (horizontal) | Dynamic |
| 37 | Ride moving platform | New mechanic |
| 38 | Moving platform (vertical) | Variety |
| 39 | Enemy sprite (patroller) | Active threat |
| 40 | Enemy movement (back/forth) | Predictable |
| 41 | Touch enemy = death | Danger |
| 42 | Enemy death sound | Feedback |
| 43 | Crumbling platform | Timing element |
| 44 | Crumble animation | Visual feedback |
| 45 | Crumble sound | Audio feedback |
| 46 | Level 6-8 with new hazards | Application |
| 47 | Hazard combinations | Complexity |
| 48 | Integration + balance | Fair challenge |

**C64-Specific:**
- Enemies as sprites (use multiplexing if needed later)
- Moving platforms can be sprites OR character animation
- Crumbling uses character animation (swap characters over time)

**If it doesn't work (Phase 3):**
- **Player clips through moving platform?** Update platform position BEFORE player collision
- **Enemy movement jerky?** Use velocity, not direct position changes
- **Crumble timing off?** Use frame counter, not random timing

**End of Phase 3:** 8 levels with hazards, enemies, dynamic platforms.

---

## Phase 4: Player Abilities (Units 49-64)

**Goal:** Expand what the player can do.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Walk animation (2 frames) | Life |
| 50 | Walk animation (4 frames) | Smooth |
| 51 | Jump animation | Polish |
| 52 | Fall animation | Distinction |
| 53 | Direction facing | Responsiveness |
| 54 | Collectible items | Goals within levels |
| 55 | Collect = points | Reward |
| 56 | Collect sound | Feedback |
| 57 | All items = bonus | Incentive |
| 58 | Ladder tile | New traversal |
| 59 | Climb ladder | Vertical movement |
| 60 | Ladder animation | Polish |
| 61 | Variable jump height | Skill expression |
| 62 | Jump control (release = stop rising) | Precision |
| 63 | Levels 9-12 with new abilities | Application |
| 64 | Integration + feel | Responsive controls |

**C64-Specific:**
```asm
; Variable jump height - release button to cut jump short
check_jump_release:
    lda $dc00           ; Read joystick
    and #$10            ; Fire button (active low)
    bne .released       ; Button released
    rts
.released:
    lda player_vel_y
    bpl .done           ; Already falling, don't interfere
    lsr                 ; Cut upward velocity in half
    sta player_vel_y
.done:
    rts
```

**If it doesn't work (Phase 4):**
- **Animation stutters?** Ensure frame counter increments consistently
- **Ladder movement weird?** Disable gravity while on ladder
- **Variable jump feels wrong?** Tune the velocity cut amount

**End of Phase 4:** 12 levels, animated player, ladders, collectibles, tight controls.

---

## Phase 5: Audio Polish (Units 65-80)

**Goal:** Full SID soundtrack and rich sound design.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Title music | Atmosphere |
| 66 | In-game music (simple) | Energy |
| 67 | Music doesn't interfere with SFX | Balance |
| 68 | Death jingle | Punctuation |
| 69 | Level complete jingle | Celebration |
| 70 | Game over music | Finality |
| 71 | Varied jump sounds | Interest |
| 72 | Enemy sounds | Presence |
| 73 | Hazard warning sounds | Fairness |
| 74 | Collectible jingles | Reward |
| 75 | Low lives warning | Tension |
| 76 | Bonus round music | Variety |
| 77 | Music tempo increases with level | Urgency |
| 78 | Sound options (music on/off) | Accessibility |
| 79 | Audio mixing balance | Professional |
| 80 | Integration + consistency | Cohesive |

**C64-Specific:**
- SID has 3 voices - typically 2 for music, 1 for SFX
- Or: music uses all 3, SFX briefly steals voice 3
- Use ADSR envelopes for punchy sound effects
- Filter for bass sounds in music

**End of Phase 5:** Complete audio experience, music and SFX.

---

## Phase 6: Visual Polish (Units 81-96)

**Goal:** Make it look like a commercial C64 game.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Custom character set design | Unique look |
| 82 | Multicolour characters | Richer graphics |
| 83 | Background decorations | Depth |
| 84 | Parallax scrolling (raster trick) | Wow factor |
| 85 | Animated background elements | Life |
| 86 | Player multicolour sprite | Detail |
| 87 | Enemy multicolour sprites | Variety |
| 88 | Death effect (flash/explosion) | Impact |
| 89 | Level complete effect | Celebration |
| 90 | Screen transitions | Flow |
| 91 | Score/lives UI polish | Clean |
| 92 | Border effects (optional) | Flair |
| 93 | Theme per level set | Visual variety |
| 94 | Colour palette refinement | Cohesion |
| 95 | Performance optimisation | Smooth |
| 96 | Integration + consistency | Professional |

**C64-Specific:**
- Multicolour mode: $D016 bit 4, $D022-$D023 for extra colours
- Raster interrupts for colour splits between game area and status bar
- Sprite priority: background behind platforms, player in front

**End of Phase 6:** Looks like a real C64 commercial release.

---

## Phase 7: Advanced Features (Units 97-112)

**Goal:** Features that elevate beyond basics.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | High score table | Competition |
| 98 | Initials entry | Ownership |
| 99 | Scores saved (if disk) | Persistence |
| 100 | Title screen animation | Polish |
| 101 | Attract mode (demo play) | Showcase |
| 102 | Two-player alternating | Multiplayer |
| 103 | Bonus round (timed collect) | Variety |
| 104 | Secret areas | Exploration reward |
| 105 | Warp zones | Speedrun appeal |
| 106 | Difficulty settings | Accessibility |
| 107 | Level passwords | Save progress |
| 108 | Enemy variety (new types) | Fresh challenge |
| 109 | Boss level concept | Milestone |
| 110 | Boss pattern | Skill test |
| 111 | Boss defeated = major reward | Payoff |
| 112 | Integration + balance | Feature complete |

**C64-Specific:**
- High scores: store in memory, optionally save to disk
- Passwords: encode level + score + lives into 4-6 characters
- Attract mode: record player inputs, play back

**End of Phase 7:** Full-featured platformer with high scores, passwords, boss.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Ship-ready quality.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | Levels 13-16 | Full content |
| 114 | Levels 17-20 | Complete game |
| 115 | Level balance pass | Fair difficulty |
| 116 | Control tuning | Responsive |
| 117 | Bug hunting | Stable |
| 118 | Edge case handling | Robust |
| 119 | Loading screen | Presentation |
| 120 | Credits screen | Attribution |
| 121 | Ending sequence | Reward |
| 122 | PRG file creation | Distribution |
| 123 | D64 disk image | Disk version |
| 124 | Turbo loader (optional) | Fast loading |
| 125 | Manual/instructions | Documentation |
| 126 | Final testing | Quality |
| 127 | Performance final pass | Smooth |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A platformer worthy of the C64 library.

---

## Platform Panic Debugging Guide

**Gravity Issues:**
- Player accelerates forever → Cap maximum fall velocity
- Player floats → Check gravity is being applied every frame
- Inconsistent fall speed → Use fixed-point math for sub-pixel precision

**Collision Issues:**
- Falls through thin platforms → Check collision at multiple points (feet corners)
- Stuck in walls → Separate horizontal and vertical collision passes
- Bounces on landing → Snap to platform surface, zero velocity

**Jump Issues:**
- Can't jump → Check ground detection is working
- Double jump possible → Set "jumping" flag, clear on landing
- Jump height varies → Ensure consistent frame timing

**Animation Issues:**
- Wrong frame shown → Check state machine transitions
- Animation too fast/slow → Tie to frame counter, not game speed

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Levels | 1 simple screen | 20 varied levels |
| Player | Walk + jump | Full animation, abilities |
| Hazards | None | Spikes, enemies, crumbling |
| Audio | Jump sound | Full music + SFX |
| Visuals | Basic chars | Multicolour, polished |
| Features | Reach goal | High scores, passwords, boss |

---

## The Platformer Difference

Where the shooter was about reflexes and patterns, the platformer is about:
- **Spatial reasoning** — judging distances and arcs
- **Timing** — when to jump, when to wait
- **Risk assessment** — safe path vs. fast path
- **Mastery** — the same level plays differently as skill improves

This game teaches learners that different genres require different design thinking.

---

**Version:** 1.0
**Last Updated:** 2026-01-18
