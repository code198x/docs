# Full Game Outline: Amiga Redline (512 Units)

**Game:** Redline (Game 3)
**Units:** 512 (16 phases × 32 units)
**Genre:** Pseudo-3D racing
**Inspired by:** Lotus Turbo Challenge, Outrun, Super Hang-On
**Target Quality:** Commercial-grade racing game (1990–92 era)

---

## Premise

Five circuits. One championship. The Redline Grand Prix crosses the continent: coastal roads, mountain passes, desert highways, forest tracks, and the night circuit through the city. Your car slides, drifts, and screams through corners at 200 mph. The road stretches to the horizon. Other cars jostle for position. Split-screen two-player doubles the chaos.

The Copper renders the road: every scanline is a different colour, a different horizontal position, a different road width. The road curves because the Copper says it curves. The hills rise because the Copper shifts the scanline positions. This is the Amiga at its most technically distinctive — per-scanline effects that no other home computer could match.

---

## Why This Game

Lotus Turbo Challenge defined Amiga racing. Magnetic Fields used the Copper to render a pseudo-3D road with per-scanline colour changes, creating the illusion of depth, curves, and hills. The technique is pure Amiga: no other platform has a coprocessor that can change display parameters on every scanline in parallel with the CPU.

Redline teaches:
- **Copper per-scanline rendering** — the road is painted by the Copper, not the CPU
- **Perspective projection** — 3D world-space road segments mapped to 2D screen lines
- **Road geometry** — curves (horizontal offset per line), hills (vertical displacement), width variation
- **Sprite scaling** — pre-drawn sprites at multiple sizes for depth simulation
- **Split-screen two-player** — Copper splits the screen into two viewports
- **Paula audio** — engine sound synthesis, MOD music, gear changes
- **Blitter** — scenery rendering, car sprites, HUD elements

---

## 68000 Progression

| Phase | 68000/Amiga Focus |
|-------|------------------|
| 1-2 | Road rendering: Copper per-scanline colour, perspective maths, road segments |
| 3-4 | Car physics: steering, acceleration, braking, surface friction, curves |
| 5-6 | Scenery and sprites: roadside objects, other cars, pre-scaled sprites |
| 7-8 | Two-player: Copper screen split, dual viewports, independent game state |
| 9-10 | 5 circuits, championship mode, AI opponents |
| 11-12 | Audio: engine synthesis, MOD music, gear sounds |
| 13-14 | Visual effects: weather, time-of-day, tunnels |
| 15-16 | Production: title, high scores, difficulty, ADF distribution |

---

## Phase 1-2: The Road (Units 1–64)

**Phase 1 (Units 1-32): Copper-Rendered Road**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 1-4 | Display setup, Copper list with many colour changes | Copper WAIT/MOVE, colour register writes per scanline | Multicolour display |
| 5-8 | Road colours per scanline | Bottom scanlines: wide road (grey). Top scanlines: narrow road (grey). Grass (green) on sides. | **Road shape visible** |
| 9-12 | Perspective width | Road width narrows toward the horizon. Width per scanline = perspective function of distance. | Depth illusion |
| 13-16 | Road/grass boundary | Copper changes colour at the road edge per scanline. Road colour, kerb colour, grass colour. | **Road with edges** |
| 17-20 | Road segments | Road defined as segments: each has a curvature and elevation. Segments map to scanline ranges. | Road geometry data |
| 21-24 | Curves | Horizontal offset per scanline. A curve shifts the road centre left or right. Gentle curves → sharp bends. | **The road curves** |
| 25-28 | Hills | Vertical displacement per segment. Uphill: scanlines compress (road rises). Downhill: scanlines spread. | **The road has hills** |
| 29-32 | Scrolling road | The player's Z-position advances each frame. Road segments scroll toward the viewer. New segments appear at the horizon. | **Road moves** |

**Key Teaching Moment (Units 5-8):**
The road is NOT drawn by the CPU. The Copper writes colour registers on every scanline. Each scanline represents a horizontal strip of road at a specific distance from the viewer. The Copper decides: at scanline N, the road is X pixels from the left edge, Y pixels wide, and coloured Z. The CPU computes the road geometry; the Copper paints it. This division of labour is what makes the Amiga unique.

```asm
; Copper list for one frame's road
; Each scanline: WAIT, set road colour, set grass colour, position road
; (Simplified — real implementation uses bitplane tricks or colour splits)

copper_road:
    ; Scanline 200 (nearest): wide road
    dc.w    $C801,$FFFE         ; WAIT line $C8
    dc.w    COLOR01,$0888       ; Road: grey
    dc.w    COLOR02,$0080       ; Grass: green

    ; Scanline 150 (mid-distance): narrower road
    dc.w    $9601,$FFFE
    dc.w    COLOR01,$0888
    dc.w    COLOR02,$0070       ; Slightly darker grass (distance)

    ; Scanline 100 (horizon): very narrow road
    dc.w    $6401,$FFFE
    dc.w    COLOR01,$0666       ; Darker road (distance)
    dc.w    COLOR02,$0060

    ; ... one entry per scanline for smooth rendering
```

**Phase 2 (Units 33-64): Road Rendering Engine**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 33-36 | Perspective maths | Distance-to-scanline mapping. Near = bottom of screen. Far = horizon. Projection formula. | 3D-to-2D mapping |
| 37-40 | Road segment data | Array of segments: curvature (signed), elevation (signed), length. Defines the entire track. | Track data format |
| 41-44 | Dynamic Copper list | CPU builds the Copper list each frame based on player Z-position, curvature, and elevation. | Dynamic Copper generation |
| 45-48 | Rumble strips | Alternating red/white kerb colours. Cycle pattern per distance to create a rolling effect. | Kerb animation |
| 49-52 | Road markings | Centre line dashes. Visible as colour changes at the road centre. Dash spacing creates speed illusion. | Speed indication |
| 53-56 | Sky gradient | Top portion of screen: Copper gradient for sky. Blends into the road at the horizon. | Complete scene |
| 57-60 | Ground colour variation | Grass alternates between two greens per segment. Creates a striped pattern that enhances speed perception. | Speed stripes |
| 61-64 | Road at 50fps | Complete road rendering at 50fps. Profile: Copper list generation + segment processing per frame. | **Road engine complete** |

**End of Phase 2:** A road that curves, rises, falls, and scrolls toward the viewer at 50fps. The Copper paints every scanline. The engine is ready for gameplay.

---

## Phase 3-4: Driving (Units 65–128)

**Phase 3 (Units 65-96): Car Physics**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 65-68 | Player car sprite | BOB at bottom-centre of screen. Drawn via Blitter. Steering tilts the sprite (pre-drawn angles). | Car visible |
| 69-72 | Acceleration and braking | Speed increases with throttle, decreases with brake. Max speed. | Speed control |
| 73-76 | Steering | Left/right shifts the car's lateral position. At speed, steering moves the road offset (illusion of turning). | **Steering works** |
| 77-80 | Speed-dependent steering | At high speed: less responsive steering. At low speed: more responsive. Feels like a real car. | Realistic feel |
| 81-84 | Curve physics | In a curve: the car drifts outward (centrifugal force simulation). Player must counter-steer. | Curve challenge |
| 85-88 | Off-road penalty | Car position beyond road edge: speed drops sharply, handling degrades. Grass slows you down. | Stay on the road |
| 89-92 | Gear system | 4 gears. Each gear has a speed range. Higher gear = higher top speed, slower acceleration. Manual shift. | Gear management |
| 93-96 | Speed display | Speedometer in HUD panel. Gear indicator. Lap timer. | Dashboard |

**Phase 4 (Units 97-128): Scenery and Objects**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 97-100 | Roadside scenery | Trees, signs, barriers placed at road edges. BOBs at positions defined by road segments. | Populated road |
| 101-104 | Scaled scenery sprites | Each scenery object has 4-6 pre-drawn sizes. Size selected by distance. Near = large. Far = small. | Depth scaling |
| 105-108 | Scenery streaming | Objects appear at the horizon and grow as they approach. Remove when past the player. | Dynamic objects |
| 109-112 | Other cars | AI car BOBs on the road. Scaled by distance like scenery. Multiple visible simultaneously. | Traffic |
| 113-116 | Car collision | Hit another car: speed drops, slight lateral push. Not instant death — just a penalty. | Racing contact |
| 117-120 | Lap structure | Track loops. Cross the start/finish line: lap count increments. 3 laps per race. | Race structure |
| 121-124 | Lap timer | Per-lap timing. Best lap displayed. Total race time. | Time tracking |
| 125-128 | One circuit playable | Complete track with curves, hills, scenery, AI cars, lap counting, timer. A racing game. | **First circuit** |

**End of Phase 4:** Driving on a pseudo-3D road with AI opponents, scenery, gear shifting, and lap timing. One circuit complete.

---

## Phase 5-6: Two-Player (Units 129–192)

**Phase 5 (Units 129-160): Split Screen**

The split-screen is pure Copper. Midway down the screen, a Copper WAIT triggers a new road rendering section: different scroll position, different camera Z, different car position. Two complete road renders in one frame.

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 129-132 | Copper screen split | Copper divides the display: top half = Player 1, bottom half = Player 2. Divider bar between. | **Split screen** |
| 133-136 | Dual road renders | Each half gets its own perspective road. Two road Copper lists per frame. | Two viewports |
| 137-140 | Dual game state | Two player positions, speeds, gears, lap counts. Two sets of physics. | Independent players |
| 141-144 | Dual input | Joystick 1 = Player 1, Joystick 2 = Player 2. Simultaneous input reading. | Two-player input |
| 145-148 | Half-height rendering | Each viewport is half the screen height. Fewer scanlines = faster Copper list, but less road visible. | Viewport management |
| 149-152 | Scenery in split mode | Each half renders its own scenery. Fewer simultaneous BOBs per half (shared Blitter time). | Shared resources |
| 153-156 | Position markers | Each player sees the other's position as a distant car BOB (if on the same section of track). | Competitive awareness |
| 157-160 | Split-screen performance | Two road renders + two sets of scenery + dual physics. Profile: does it still run at 50fps? | Performance validation |

**Phase 6 (Units 161-192): Audio**

| Unit | You Add | 68000 Skill | Result |
|------|---------|-------------|--------|
| 161-168 | Engine sound | Paula channel: sample loop with period (pitch) modulated by engine RPM. Higher RPM = higher pitch. | **Engine sound** |
| 169-172 | Gear change | Pitch drops on gear shift (RPM drops). Brief silence then new pitch ramp. | Gear audio |
| 173-176 | Tyre screech | On heavy cornering or off-road: noise sample. Intensity proportional to slip. | Cornering audio |
| 177-180 | Collision sound | Impact sample on car contact. Proportional to speed difference. | Contact audio |
| 181-184 | MOD music | Menu/title music. In-race: engine dominates, music is background (low volume) or absent. | Musical atmosphere |
| 185-188 | Two-player audio | Engine sound for both players. Channels: P1 engine (ch 0), P2 engine (ch 1), SFX (ch 2), music (ch 3). | Channel allocation |
| 189-192 | Audio balance | Engine volume scales with speed. Music fades during intense racing. | Dynamic mix |

**End of Phase 6:** Split-screen two-player racing with engine synthesis, gear changes, and tyre screech. The Amiga's audio capabilities serve the gameplay.

---

## Phase 7-8: Championship (Units 193–256)

**Phase 7 (Units 193-224): Five Circuits**

| Circuit | Theme | Unique Feature | Palette |
|---------|-------|---------------|---------|
| 1: Coastal Road | Seaside cliffs, beach, lighthouse | Water reflection strip (Copper) | Blue/sand/white |
| 2: Mountain Pass | Switchbacks, tunnels, altitude | Tunnel sections (screen goes dark, then emerges) | Grey/green/white |
| 3: Desert Highway | Long straights, heat shimmer | Shimmer effect (Copper scanline wobble) | Orange/yellow/brown |
| 4: Forest Track | Tight corners, tree-lined | Dense scenery, dappled light (palette flicker) | Green/brown/gold |
| 5: Night City | Urban, neon lights, wet road | Night palette (dark), neon colour accents, reflections | Black/neon/chrome |

Each circuit: 15-20 road segments defining the track geometry. Different scenery object sets. Different AI difficulty.

**Phase 8 (Units 225-256): Championship Mode**

Championship: race all 5 circuits in order. Points per race (10/6/3/1 for 1st-4th). Cumulative standings. AI opponents with consistent identities (always the same 3 rivals across all circuits).

Time trial: solo, no AI. Ghost car replays the best lap. Beat your own time.

Quick race: pick a circuit, pick 1P or 2P, race 3 laps.

**End of Phase 8:** 5 circuits, championship, time trial, quick race. Content-complete.

---

## Phase 9-12: Polish and Effects (Units 257–384)

**Phase 9 (Units 257-288): Visual Effects**
- Weather: rain (particle dots falling via Blitter), spray from cars, wet road (darker, shinier palette)
- Night: headlight cone (Copper illuminates a triangular area ahead of the car)
- Tunnel: screen darkens gradually entering, brightens leaving
- Finish line: chequered flag animation, confetti particles

**Phase 10 (Units 289-320): AI Opponents**
- 3 AI cars with distinct behaviour: aggressive (blocks), defensive (consistent), erratic (fast but makes mistakes)
- AI follows the racing line (precalculated optimal path through curves)
- Rubber-banding: AI slows slightly when far ahead, speeds up when behind. Keeps races competitive.
- AI visible as scaled car BOBs. Different colours per rival.

**Phase 11 (Units 321-352): HUD and Presentation**
- Dashboard: speed, gear, position, lap, timer. Rendered in a Copper panel below the game area.
- Rear-view mirror: small rectangle showing what's behind (a simplified road render, or just car BOBs at fixed positions)
- Position indicator: "1st / 2nd / 3rd / 4th" with rival car colours
- Race results screen: finishing order, lap times, championship standings

**Phase 12 (Units 353-384): Track Design Polish**
- Each circuit's road segments refined for racing feel: technical sections reward skill, fast sections reward nerve
- Scenery placement enhances corners: a tree on the apex says "corner here" without a minimap
- Circuit difficulty curve: Coastal (gentle, wide), Mountain (technical), Desert (fast), Forest (tight), City (everything)

**End of Phase 12:** Weather, AI, dashboard, rear-view, polished tracks. A complete racing experience.

---

## Phase 13-16: Production (Units 385–512)

**Phase 13 (Units 385-416): Title and Presentation**
- Title screen with Copper rainbow and car animation
- Circuit select with preview (brief road render of each circuit's opening)
- Championship standings between races
- Attract mode: AI race on Circuit 1

**Phase 14 (Units 417-448): Records and Saves**
- Best lap time per circuit (saved to disk if available)
- Championship results
- Two-player win/loss record
- Ghost lap data (position per frame, saved and replayed)

**Phase 15 (Units 449-480): ADF Distribution**
- Bootable ADF with custom loader
- 5 circuits loaded on demand (or all in memory if chip RAM allows)
- Loading masked by inter-circuit transition screens
- System-friendly startup/shutdown

**Phase 16 (Units 481-512): Ship It**

| Unit | You Add | Result |
|------|---------|--------|
| 481-488 | Championship ending: trophy ceremony, final standings, credits | Victory sequence |
| 489-492 | Difficulty select: Easy (assists, slow AI), Normal, Hard (no assists, fast AI) | Accessibility |
| 493-496 | Testing: all circuits, 1P/2P, championship, time trial, all weather/time-of-day combos | Release quality |
| 497-504 | Performance audit: 50fps in all conditions, split-screen stable | Quality assurance |
| 505-508 | ADF image: bootable, multi-circuit, saves | Distribution |
| 509-512 | **Complete game** | **Ship it** |

---

## Technical Notes

### Per-Scanline Road Rendering

The CPU builds the Copper list each frame:

```asm
; For each visible road scanline (bottom to top = near to far):
;   1. Calculate road width at this distance (perspective)
;   2. Calculate road centre X (accumulated curvature)
;   3. Calculate road colour (near = bright, far = dark)
;   4. Write Copper instructions: WAIT line, set road colour, set grass colour

build_road_copper:
    lea     copper_road_start,a0    ; Pointer into Copper list
    move.w  #199,d7                 ; Bottom scanline
    move.l  player_z,d6             ; Player position on track

.scanline_loop:
    ; Distance for this scanline
    move.w  d7,d0
    sub.w   #100,d0                 ; d0 = scanline offset from horizon
    ; perspective_width = BASE_WIDTH * NEAR_FACTOR / d0
    ; (Fixed-point division)

    ; Curvature offset
    ; road_centre = screen_centre + accumulated_curve_offset[scanline]

    ; Write Copper WAIT
    move.w  d7,d1
    lsl.w   #8,d1
    or.w    #$01,d1                 ; WAIT for scanline d7, any X
    move.w  d1,(a0)+
    move.w  #$FFFE,(a0)+

    ; Write road colour
    move.w  #COLOR01,(a0)+          ; Road colour register
    move.w  road_colour_table(pc,d7.w*2),(a0)+  ; Distance-based colour

    dbra    d7,.scanline_loop
    rts
```

### Split-Screen Copper

```asm
; Frame Copper list structure:
;   1. Player 1 road render (top half: lines 44-156)
;   2. Divider bar (line 157-159: bright colour)
;   3. Player 2 road render (bottom half: lines 160-272)
;   4. HUD panel (lines 273-312)

; The Copper handles the split automatically — no CPU intervention during the frame.
; The CPU builds both road sections during the previous frame's vertical blank.
```

### Perspective Formula

```
For scanline Y (measured from horizon, 0 = horizon, increasing = nearer):
  distance = CAMERA_HEIGHT / Y
  road_width = BASE_WIDTH × SCALE_FACTOR / distance
  road_x_offset = accumulated_curvature × SCALE_FACTOR / distance
```

All done in 16.16 fixed-point. The 68000's MULU and DIVU instructions handle the maths — no lookup table needed (unlike 8-bit platforms).

---

## The Amiga Arc

| Game | Chipset focus | Rendering | Scale |
|------|-------------|-----------|-------|
| Exodus | Blitter (terrain modification) | Single playfield, bitmap | Fixed-screen puzzle |
| Duskfall | Copper + dual playfield | Multi-layer parallax, BOBs | 5-stage side-scroller |
| Redline | Copper per-scanline | Pseudo-3D perspective road | 5-circuit racer |

Exodus: the Blitter IS the gameplay. Duskfall: the Copper paints parallax. Redline: the Copper renders 3D. Three games, three chips, three display paradigms. The Amiga's custom chipset fully explored.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 3 for the restructured Amiga assembly track. Pseudo-3D racing with Copper per-scanline rendering.
