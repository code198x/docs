# Full Game Outline: ZX Spectrum Shatter (128 Units)

**Game:** Shatter (Game 2)
**Platform:** Sinclair ZX Spectrum
**Units:** 128 (8 phases × 16 units)
**Prerequisite:** Skyfire (Game 1) - screen memory, attributes, keyboard, beeper
**Target Quality:** Polished breakout clone (Arkanoid / Batty quality)

---

## What Carries Over from Game 1

Learners already know:
- Screen memory layout ($4000-$57FF)
- Attribute memory ($5800-$5AFF)
- Keyboard input via ROM routines
- Beeper sound effects
- Basic collision detection
- Game loop structure

**What's NEW in this game:**
- Sub-cell (pixel-precise) movement
- Ball physics (velocity, angles, reflection)
- Paddle control (horizontal only)
- Brick grid and destruction
- Power-up systems
- Frame-rate independent movement

---

## Design Philosophy

- **Ball moving from Unit 1** — the defining mechanic
- **Playable breakout by Unit 8** — complete core loop early
- **Physics feel right** — angles, speed, spin
- **Debugging inline** — ball physics bugs are common
- **Polish by Unit 128** — smooth, satisfying, complete

---

## Phase 1: Core Ball Physics (Units 1-16)

**Goal:** Ball bounces around screen, paddle can hit it, bricks can be broken.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Ball on screen (pixel position) | See the ball |
| 2 | Ball moves (velocity) | Ball in motion |
| 3 | Ball bounces off walls | Contained |
| 4 | Paddle on screen | Player element |
| 5 | Paddle moves (keyboard) | **Control** |
| 6 | Ball bounces off paddle | **Interaction** |
| 7 | Brick row on screen | Targets |
| 8 | Ball destroys brick | **Core loop complete** |
| 9 | Multiple brick rows | Full playfield |
| 10 | Brick colours | Visual variety |
| 11 | Miss ball = lose life | Stakes |
| 12 | Lives display | Feedback |
| 13 | All bricks = level complete | Win condition |
| 14 | Score display | Progress |
| 15 | Brick = points | Reward |
| 16 | Integration + feel | Solid foundation |

**Spectrum-Specific Unit 1:**
```z80
; Sub-pixel ball position using fixed-point
; High byte = screen position, low byte = fraction

ball_x:      defw 0      ; 8.8 fixed point
ball_y:      defw 0      ; 8.8 fixed point
ball_vel_x:  defw 0      ; Velocity X (signed)
ball_vel_y:  defw 0      ; Velocity Y (signed)

update_ball:
    ; Add velocity to position (16-bit add)
    ld hl,(ball_x)
    ld de,(ball_vel_x)
    add hl,de
    ld (ball_x),hl

    ld hl,(ball_y)
    ld de,(ball_vel_y)
    add hl,de
    ld (ball_y),hl

    ; Screen position is high byte
    ld a,(ball_x+1)     ; X screen position
    ld b,a
    ld a,(ball_y+1)     ; Y screen position
    ld c,a
    ; Now B=X, C=Y for drawing
    ret
```

**If it doesn't work (Phase 1):**
- **Ball moves wrong direction?** Check sign of velocity values
- **Ball too fast/slow?** Adjust velocity magnitude (remember: 8.8 fixed point)
- **Ball passes through paddle?** Test collision BEFORE moving, or use swept collision
- **Paddle jittery?** Use consistent keyboard polling rate
- **Bricks don't break?** Check collision detection bounds match brick size

**End of Phase 1:** Playable breakout. Ball, paddle, bricks, lives, score.

---

## Phase 2: Physics Refinement (Units 17-32)

**Goal:** Ball physics feel satisfying and controllable.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Paddle position affects angle | Skill expression |
| 18 | Centre = straight, edge = angled | Predictable |
| 19 | Ball speed increases over time | Tension |
| 20 | Speed cap | Fair |
| 21 | Steeper angles possible | Variety |
| 22 | Angle limits (not too steep) | Playable |
| 23 | Ball spin concept | Advanced control |
| 24 | Spin affects bounce | Depth |
| 25 | Brick collision from side | Correct physics |
| 26 | Brick collision from below | Consistency |
| 27 | Multiple brick hits per frame | Fast ball handling |
| 28 | Corner collision handling | Polish |
| 29 | Ball launch control | Player agency |
| 30 | Serve angle choice | Strategy |
| 31 | Speed display (optional) | Feedback |
| 32 | Integration + feel | Physics feel right |

**Spectrum-Specific:**
- Angle calculation: use lookup tables, not trig functions
- 8-16 discrete angles is enough for smooth movement
- Paddle zones: divide paddle into 5-7 regions for angle mapping

**If it doesn't work (Phase 2):**
- **Ball gets stuck bouncing horizontally?** Ensure minimum vertical velocity
- **Angles feel random?** Debug paddle zone calculation
- **Ball passes through bricks?** Handle multiple collisions per frame

**End of Phase 2:** Ball physics feel professional. Angles are predictable but varied.

---

## Phase 3: Level Design (Units 33-48)

**Goal:** Multiple levels with distinct brick patterns.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Level data format | Structured levels |
| 34 | Load level from data | Data-driven |
| 35 | Level 2 (different pattern) | Variety |
| 36 | Level 3 (harder) | Progression |
| 37 | Harder bricks (2 hits) | Challenge |
| 38 | Hard brick colour change | Visual feedback |
| 39 | Unbreakable bricks | Strategy |
| 40 | Unbreakable = metal colour | Clarity |
| 41 | Level 4-6 | Content |
| 42 | Level transition effect | Polish |
| 43 | Level display | Progress |
| 44 | Bonus points for clear | Incentive |
| 45 | Time bonus (optional) | Speed reward |
| 46 | Brick patterns (shapes) | Visual interest |
| 47 | Levels 7-10 | Mid-game content |
| 48 | Integration + balance | Fair progression |

**Spectrum-Specific:**
- Brick data: 1 byte per brick (colour + hit count)
- Level data: 12×8 = 96 bytes per level (compressed if needed)
- Use attribute colours for brick types

**End of Phase 3:** 10 distinct levels with varied brick types and patterns.

---

## Phase 4: Power-Ups (Units 49-64)

**Goal:** Items that change gameplay temporarily or permanently.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Power-up drops from brick | System exists |
| 50 | Power-up falls down | Catch it |
| 51 | Catch power-up | Activation |
| 52 | Extend paddle | Easier |
| 53 | Shrink paddle (bad) | Risk |
| 54 | Paddle size display | Clarity |
| 55 | Multi-ball (2 balls) | Chaos |
| 56 | Multi-ball handling | Technical |
| 57 | Slow ball | Breathing room |
| 58 | Fast ball (bad) | Challenge |
| 59 | Laser paddle | Alternative |
| 60 | Laser fires | Shoot bricks |
| 61 | Catch ball | Strategic pause |
| 62 | Release caught ball | Control |
| 63 | Power-up sounds | Feedback |
| 64 | Integration + balance | Fair variety |

**Spectrum-Specific:**
- Power-ups: single character falling, different colours = different types
- Multi-ball: array of ball structures, iterate through active balls
- Laser: simple projectile, reuse collision code

**If it doesn't work (Phase 4):**
- **Multi-ball causes glitches?** Ensure ball array is properly bounded
- **Power-ups fall through paddle?** Same collision as ball, but different response
- **Laser doesn't hit bricks?** Check vertical collision detection

**End of Phase 4:** Power-up system adds variety and strategy.

---

## Phase 5: Audio Polish (Units 65-80)

**Goal:** Rich beeper audio that enhances gameplay.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Paddle hit sound (pitch varies) | Position feedback |
| 66 | Wall bounce sound | Spatial awareness |
| 67 | Brick break sound | Satisfaction |
| 68 | Different sound per brick type | Variety |
| 69 | Power-up collect sound | Reward |
| 70 | Bad power-up sound | Warning |
| 71 | Life lost sound | Impact |
| 72 | Level complete fanfare | Celebration |
| 73 | Game over sound | Finality |
| 74 | Title screen music | Atmosphere |
| 75 | In-game music (simple) | Energy |
| 76 | Music + SFX balance | Coexistence |
| 77 | High score entry sounds | Polish |
| 78 | Multi-ball chaos sounds | Fun |
| 79 | Laser sound | Power |
| 80 | Integration + mix | Cohesive audio |

**Spectrum-Specific:**
- Beeper: use pitch for feedback (higher = paddle edge, lower = centre)
- Music: simple arpeggios between game updates, or use interrupt-driven
- 48K beeper only - no AY chip assumed (128K enhancement possible later)

**End of Phase 5:** Complete audio experience using beeper.

---

## Phase 6: Visual Polish (Units 81-96)

**Goal:** Make it look like a commercial Spectrum game.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Custom font | Unique look |
| 82 | Title screen design | Presentation |
| 83 | Brick graphics (UDG) | Detail |
| 84 | Ball trail effect | Speed feel |
| 85 | Paddle design | Character |
| 86 | Background pattern | Depth |
| 87 | Border colour effects | Flair |
| 88 | Brick destruction effect | Impact |
| 89 | Power-up graphics | Clarity |
| 90 | Score/lives UI design | Clean |
| 91 | Level intro screen | Anticipation |
| 92 | Colour themes per level | Variety |
| 93 | BRIGHT/FLASH effects | Polish |
| 94 | Smooth ball rendering | Professional |
| 95 | Attribute clash minimisation | Clean |
| 96 | Integration + consistency | Cohesive |

**Spectrum-Specific:**
- UDG (User Defined Graphics) for custom characters
- Ball: single character or 2×2 for larger ball
- Attribute clash: plan layouts to minimise, or embrace it stylistically
- BRIGHT 1 for active elements, BRIGHT 0 for background

**End of Phase 6:** Looks professional, manages colour clash well.

---

## Phase 7: Advanced Features (Units 97-112)

**Goal:** Features that make it a complete product.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | High score table | Competition |
| 98 | Initials entry | Ownership |
| 99 | Score persistence (tape optional) | Memory |
| 100 | Attract mode | Showcase |
| 101 | Demo playback | Instruction |
| 102 | Difficulty settings | Accessibility |
| 103 | Level select (earned) | Convenience |
| 104 | Bonus level (all gold bricks) | Reward |
| 105 | Hidden power-ups | Discovery |
| 106 | Paddle skins (visual only) | Customisation |
| 107 | Two-player alternating | Multiplayer |
| 108 | Score competition | Rivalry |
| 109 | Warp levels | Speedrun |
| 110 | Boss brick (moves) | Variety |
| 111 | Boss pattern | Challenge |
| 112 | Integration + balance | Feature complete |

**Spectrum-Specific:**
- High scores: 10 entries, stored in memory
- Tape save: optional, use standard ROM routines
- Two-player: alternate on life loss

**End of Phase 7:** Full-featured breakout with high scores, difficulty, multiplayer.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Ship-ready quality.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | Levels 11-15 | More content |
| 114 | Levels 16-20 | Full game |
| 115 | Level balance pass | Fair curve |
| 116 | Physics fine-tuning | Responsive |
| 117 | Bug hunting | Stable |
| 118 | Edge case handling | Robust |
| 119 | Loading screen | Presentation |
| 120 | Credits screen | Attribution |
| 121 | Ending sequence | Reward |
| 122 | TAP file creation | Distribution |
| 123 | TZX file (turbo) | Fast loading |
| 124 | 128K enhancements (optional) | Bonus |
| 125 | Manual/instructions | Documentation |
| 126 | Final testing | Quality |
| 127 | Performance optimisation | Smooth |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A breakout game worthy of commercial release.

---

## Shatter Debugging Guide

**Ball Physics Issues:**
- Ball moves diagonally only → Check velocity components are independent
- Ball speed inconsistent → Use fixed-point math, not integer
- Ball gets stuck → Add minimum velocity in each axis
- Ball tunnels through objects → Use swept collision or smaller time steps

**Collision Issues:**
- Ball bounces wrong direction → Check which surface was hit (top/bottom/side)
- Multiple bounces per frame → Set flag to prevent re-collision
- Corner hits cause glitches → Determine primary collision surface

**Fixed-Point Issues:**
- Movement too fast → Reduce velocity values (remember: low byte is fraction)
- Movement too slow → Increase velocity or reduce precision
- Overflow → Use signed 16-bit carefully, check bounds

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Levels | 1 brick pattern | 20 varied levels |
| Physics | Basic bounce | Angles, spin, feel |
| Bricks | One type | Hard, unbreakable, boss |
| Power-ups | None | 8+ types |
| Audio | Basic sounds | Music + varied SFX |
| Visuals | Functional | Polished, themed |
| Features | Lives + score | High scores, multiplayer, difficulty |

---

## The Physics Game Difference

Where the shooter was about patterns and reflexes, the physics game is about:
- **Prediction** — where will the ball go?
- **Control** — influencing trajectory through paddle position
- **Risk** — aggressive angles vs. safe returns
- **Chaos management** — multi-ball, fast ball, power-ups

This teaches learners that physics simulation requires different thinking than discrete movement.

---

**Version:** 1.0
**Last Updated:** 2026-01-18
