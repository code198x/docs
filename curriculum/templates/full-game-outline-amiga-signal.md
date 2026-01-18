# Full Game Outline: Amiga Signal (128 Units)

**Game:** Signal (Game 2)
**Platform:** Commodore Amiga
**Units:** 128 (8 phases × 16 units)
**Prerequisite:** Blast Zone (Game 1) - sprites, BOBs, Copper, Paula, bootable ADF
**Target Quality:** Polished lane-crossing game (Frogger / Crossy Road quality)

---

## What Carries Over from Game 1

Learners already know:
- 68000 assembly fundamentals
- Hardware sprites (player)
- BOBs via Blitter (moving objects)
- Copper list basics
- Paula sample playback
- Bootable ADF creation
- Collision detection basics

**What's NEW in this game:**
- Timing-based gameplay (not reflex-based)
- Lane/grid movement (discrete, not continuous)
- Multiple object types moving independently
- Riding moving objects
- Different gameplay rhythm (patience vs. action)
- More complex Copper backgrounds

---

## Design Philosophy

- **Movement from Unit 1** — hop immediately
- **Danger by Unit 4** — cars that kill
- **Complete loop by Unit 12** — cross all lanes, win
- **Timing over reflexes** — different skill than shooter
- **Debugging inline** — lane timing bugs addressed
- **Polish by Unit 128** — satisfying, complete game

---

## Phase 1: Core Mechanics (Units 1-16)

**Goal:** Frog can hop, cars move, frog can die, frog can win.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Frog sprite at bottom | See your frog |
| 2 | Joystick moves frog (grid hop) | **Control** |
| 3 | Hop animation | Feel |
| 4 | Road lane with car (BOB) | Danger exists |
| 5 | Car moves across screen | Traffic |
| 6 | Car wraps around | Continuous |
| 7 | Frog hit by car = death | **Stakes** |
| 8 | Death animation + sound | Feedback |
| 9 | Multiple cars in lane | Density |
| 10 | Safe zone (median) | Breathing room |
| 11 | River lane with log | New mechanic |
| 12 | Frog rides log | **Carried along** |
| 13 | Fall in water = death | Water danger |
| 14 | Home at top | Goal |
| 15 | Reach home = score | **Win condition** |
| 16 | Integration + feel | Core complete |

**Amiga-Specific Unit 1:**
```asm
; Frog as hardware sprite (16 pixels wide)
; Grid-based movement: hop in 16-pixel increments

GRID_SIZE = 16
MOVE_SPEED = 4      ; Pixels per frame during hop

frog_x:     dc.w 160        ; Centre of screen
frog_y:     dc.w 240        ; Bottom
frog_target_x: dc.w 160     ; Where hopping to
frog_target_y: dc.w 240
hopping:    dc.w 0          ; 0=stationary, 1=hopping

update_frog:
    tst.w hopping
    beq .check_input
    bsr .animate_hop
    rts

.check_input:
    move.b $bfe001,d0       ; Read joystick
    btst #0,d0              ; Up
    beq .hop_up
    btst #1,d0              ; Down
    beq .hop_down
    ; ... etc
    rts

.hop_up:
    move.w frog_y,d0
    sub.w #GRID_SIZE,d0
    move.w d0,frog_target_y
    move.w #1,hopping
    rts

.animate_hop:
    ; Smoothly move toward target
    move.w frog_y,d0
    cmp.w frog_target_y,d0
    beq .hop_done
    ; ... interpolate toward target
    rts
.hop_done:
    clr.w hopping
    rts
```

**If it doesn't work (Phase 1):**
- **Frog doesn't hop?** Check joystick reading (active low signals)
- **Hop feels instant?** Add smooth interpolation between grid positions
- **Car collision wrong?** Check hitbox alignment with sprite visuals
- **Log doesn't carry frog?** Add log velocity to frog position each frame
- **Frog slides off log?** Update frog position AFTER log position

**End of Phase 1:** Complete Frogger core. Roads, river, logs, lives.

---

## Phase 2: Level Structure (Units 17-32)

**Goal:** Full playfield with multiple lanes and variety.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Multiple road lanes | Full road |
| 18 | Different car speeds | Variety |
| 19 | Different car sizes | Visual interest |
| 20 | Multiple river lanes | Full river |
| 21 | Different log sizes | Variety |
| 22 | Different log speeds | Challenge |
| 23 | Turtle lane | New object |
| 24 | Turtles dive (disappear) | Timing |
| 25 | Turtle dive warning | Fairness |
| 26 | Multiple home slots | Goals |
| 27 | Fill home = points | Progress |
| 28 | All homes = level complete | Round end |
| 29 | Level 2 (faster) | Progression |
| 30 | Level 3 (harder patterns) | Challenge |
| 31 | Level display | Progress |
| 32 | Integration + balance | 3 levels |

**Amiga-Specific:**
- Cars/logs as BOBs: Blitter handles any size
- Multiple lanes: array of lane structures with speed, direction, object type
- Turtles: animated BOBs with dive timer
- Copper gradient for water effect

**Lane Data Structure:**
```asm
; Each lane: type, y-position, speed, objects...
lane_data:
    dc.w LANE_ROAD      ; Type
    dc.w 200            ; Y position
    dc.w 2              ; Speed (pixels/frame, signed = direction)
    dc.w 3              ; Number of objects
    dc.l car_bob        ; BOB pointer
    ; ... object positions

LANE_ROAD = 0
LANE_WATER = 1
LANE_SAFE = 2
```

**If it doesn't work (Phase 2):**
- **Objects bunch up?** Initialise with proper spacing
- **Turtles don't sync?** Use global timer for dive cycle
- **Lane collision wrong?** Check Y coordinate for lane detection

**End of Phase 2:** Full Frogger playfield with variety.

---

## Phase 3: Polish and Feel (Units 33-48)

**Goal:** The game feels good to play.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Hop sound effect | Feedback |
| 34 | Car engine sounds | Atmosphere |
| 35 | Splash sound (water death) | Distinction |
| 36 | Squish sound (car death) | Impact |
| 37 | Home reached jingle | Reward |
| 38 | Frog spawn animation | Polish |
| 39 | Death animation variety | Interest |
| 40 | Score bonus for speed | Incentive |
| 41 | Timer display | Urgency |
| 42 | Timer running out | Pressure |
| 43 | Timer warning sound | Alert |
| 44 | Smooth hop animation | Feel |
| 45 | Anticipation frame | Juice |
| 46 | Landing squash | Weight |
| 47 | Screen shake on death | Impact |
| 48 | Integration + feel | Satisfying |

**Amiga-Specific:**
- Multiple Paula samples: preload splat, splash, hop, engine
- Animation: multiple sprite frames, swap during hop
- Screen shake: offset Copper display start briefly

**Sample Code:**
```asm
play_hop_sound:
    move.l #hop_sample,$dff0a0   ; AUD0 pointer
    move.w #hop_length,$dff0a4   ; Length
    move.w #hop_period,$dff0a6   ; Period (pitch)
    move.w #64,$dff0a8           ; Volume
    move.w #$8201,$dff096        ; Enable DMA
    rts
```

**End of Phase 3:** Game feels polished and satisfying.

---

## Phase 4: Visual Enhancement (Units 49-64)

**Goal:** Make it look distinctly Amiga.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Copper gradient sky | Depth |
| 50 | Copper gradient water | Liquid feel |
| 51 | Road texture (bitplane) | Detail |
| 52 | Animated water | Life |
| 53 | Car variety (sprites) | Interest |
| 54 | Truck (long vehicle) | Variety |
| 55 | Log detail | Polish |
| 56 | Lily pad homes | Theme |
| 57 | Riverside scenery | Context |
| 58 | Parallax elements | Depth |
| 59 | Frog detail (multicolour) | Character |
| 60 | Death effects (splat sprite) | Impact |
| 61 | Score popup animation | Feedback |
| 62 | UI design | Clean |
| 63 | Theme cohesion | Professional |
| 64 | Integration | Visually complete |

**Amiga-Specific:**
- Copper gradients: change COLOR registers per scanline for smooth sky/water
- Animated water: cycle palette entries, or use Copper for wave effect
- Parallax: move background elements slower than game objects

**Copper Gradient Example:**
```asm
; Water gradient via Copper list
water_copper:
    dc.w $8001,$fffe    ; Wait for line $80
    dc.w $0180,$0048    ; COLOR0 = dark blue
    dc.w $8101,$fffe
    dc.w $0180,$004a    ; Slightly lighter
    dc.w $8201,$fffe
    dc.w $0180,$004c    ; Continue gradient...
    ; ... etc
```

**End of Phase 4:** Distinctly Amiga visual quality.

---

## Phase 5: Audio Enhancement (Units 65-80)

**Goal:** Full Amiga audio experience.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Title music (MOD) | Atmosphere |
| 66 | MOD player integration | System |
| 67 | In-game music | Energy |
| 68 | Music tempo with level | Escalation |
| 69 | SFX channel priority | Balance |
| 70 | Varied car sounds | Interest |
| 71 | Ambient river sounds | Atmosphere |
| 72 | Level complete music | Celebration |
| 73 | Game over music | Finality |
| 74 | High score music | Achievement |
| 75 | Bonus round music | Variety |
| 76 | Sound mixing | Professional |
| 77 | Volume balance | Polish |
| 78 | Stereo positioning | Immersion |
| 79 | Audio options | Accessibility |
| 80 | Integration | Complete audio |

**Amiga-Specific:**
- MOD format: use ProTracker-compatible player
- 4 channels: typically 2 for music, 2 for SFX
- Channel stealing: SFX briefly takes music channel
- Stereo: cars pan L-R as they cross screen

**End of Phase 5:** Full audio with MOD music and rich SFX.

---

## Phase 6: Game Features (Units 81-96)

**Goal:** Complete game beyond basics.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Crocodile hazard | New danger |
| 82 | Crocodile snaps | Timing |
| 83 | Snake on median | Road hazard |
| 84 | Snake movement | Unpredictable |
| 85 | Bonus fly | Score item |
| 86 | Fly appears briefly | Timing reward |
| 87 | Bonus frog (extra life) | Rare reward |
| 88 | Lady frog escort | Bonus mode |
| 89 | Escort mechanics | Variety |
| 90 | Levels 4-6 | Content |
| 91 | Level variety | Fresh |
| 92 | Boss concept | Milestone |
| 93 | Snake boss | Challenge |
| 94 | Boss pattern | Skill test |
| 95 | Boss defeated | Achievement |
| 96 | Integration + balance | Feature complete |

**Amiga-Specific:**
- Crocodile: BOB with animation, safe to ride except when mouth open
- Snake: BOB with segmented movement
- Boss: large BOB, multiple collision zones

**End of Phase 6:** Full-featured Frogger with extras.

---

## Phase 7: Meta Features (Units 97-112)

**Goal:** Complete product features.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | High score table | Competition |
| 98 | Initials entry | Ownership |
| 99 | Scores saved to disk | Persistence |
| 100 | Title screen animation | Polish |
| 101 | Attract mode | Showcase |
| 102 | Two-player alternating | Multiplayer |
| 103 | Two-player competitive | Rivalry |
| 104 | Difficulty settings | Accessibility |
| 105 | Time attack mode | Variety |
| 106 | Endless mode | Replayability |
| 107 | Level passwords | Progress |
| 108 | Statistics tracking | Engagement |
| 109 | Tutorial mode | Onboarding |
| 110 | Options menu | Customisation |
| 111 | Pause functionality | Convenience |
| 112 | Integration | Complete |

**Amiga-Specific:**
- Save to disk: use AmigaDOS file operations
- Two-player: read second joystick port
- Pause: halt game loop, grey out display via Copper

**End of Phase 7:** Full-featured product.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Ship-ready Amiga game.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | Levels 7-10 | More content |
| 114 | Levels 11-15 | Full game |
| 115 | Difficulty curve | Fair |
| 116 | Control tuning | Responsive |
| 117 | Bug hunting | Stable |
| 118 | Edge cases | Robust |
| 119 | Memory optimisation | Efficient |
| 120 | ADF optimisation | Fast load |
| 121 | Custom boot screen | Professional |
| 122 | Disk icon + .info | Workbench polish |
| 123 | Ending sequence | Reward |
| 124 | Credits | Attribution |
| 125 | Final testing | Quality |
| 126 | PAL/NTSC handling | Compatibility |
| 127 | Performance pass | Smooth |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A complete Amiga lane-crossing game.

---

## Signal Debugging Guide

**Movement Issues:**
- Frog doesn't respond → Check joystick port, active low signals
- Hop feels laggy → Reduce hop animation duration
- Frog overshoots → Ensure grid snapping at hop end
- Can hop during hop → Check hopping flag before input

**Collision Issues:**
- Frog dies when safe → Check hitbox vs. visual alignment
- Log doesn't catch frog → Verify lane detection Y coordinates
- Crocodile always kills → Check mouth animation state

**Riding Issues:**
- Frog slides off log → Apply log velocity to frog AFTER log moves
- Frog snaps weirdly → Smooth the attachment position
- Falls off screen edge → Kill frog at screen boundaries

**Timing Issues:**
- Game too hard → Reduce speeds, increase gaps
- Turtles unpredictable → Sync to global timer
- Timer runs out unfairly → Adjust level time limits

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Lanes | 2 (road + river) | 12+ varied lanes |
| Objects | Car, log | Cars, trucks, logs, turtles, crocs |
| Hazards | Basic | Snake, croc, water, time |
| Audio | Hop sound | Full MOD music + SFX |
| Visuals | Basic | Copper gradients, animations |
| Features | Reach home | High scores, modes, boss |
| Levels | 1 | 15 varied levels |

---

## The Timing Game Difference

Where the shooter was about reflexes and the platformer about physics:
- **Patience** — wait for the right moment
- **Pattern recognition** — learn the traffic rhythm
- **Risk calculation** — dash now or wait?
- **Flow state** — the satisfying rhythm of successful crossing

This teaches learners that game feel varies by genre. Not everything needs to be fast.

---

**Version:** 1.0
**Last Updated:** 2026-01-18
