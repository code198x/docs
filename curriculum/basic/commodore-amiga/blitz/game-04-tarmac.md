# Blitz Game 04: Tarmac

**Track:** Blitz Basic 2
**Genre:** Top-down racing game
**Units:** 64 (4 phases × 16 units)
**Language:** Blitz Basic 2
**Max lines:** ~500

---

## Premise

Top-down racing on bitmap tracks. Your car slides, drifts, and skids around corners. AI opponents jostle for position. The track scrolls beneath you as the bitmap world whips past. Oil slicks slow you down, boost pads launch you forward, and one wrong corner sends you into the gravel.

This is the Micro Machines / Super Cars lineage — top-down racing where the track is a bitmap and the car is a rotating shape. It contrasts directly with the assembly track's Redline (pseudo-3D Copper rendering): same sport, completely different perspective and technique. Redline uses per-scanline Copper tricks for depth. Tarmac uses bitmap collision and rotation maths for overhead action.

Blitz's compiled speed is essential: smooth car rotation, multiple AI opponents, per-pixel track collision, and scrolling — all at 50fps.

---

## Core Mechanics

### The Track

Each track is a bitmap. The road is one colour, grass is another, gravel is a third, walls are a fourth. The car reads the pixel colour beneath it to determine surface:

| Surface | Colour | Effect |
|---------|--------|--------|
| Tarmac | Dark grey | Full speed, full grip |
| Kerb | Red/white | Slight speed reduction |
| Grass | Green | Major speed reduction, sliding |
| Gravel | Yellow | Speed reduction, poor grip |
| Wall | White | Stop dead, damage |
| Oil slick | Blue | Zero grip for 1 second |
| Boost pad | Cyan | Speed burst for 0.5 seconds |
| Checkpoint | Magenta | Lap progress marker |

Surface detection: `ReadPixel(car_x, car_y)` returns the colour. The bitmap IS the physics.

### Car Physics

The car has:
- **Position**: x, y (floating point for sub-pixel accuracy)
- **Angle**: 0-359 degrees (rotation)
- **Speed**: current forward velocity
- **Grip**: how well the car holds the road (surface-dependent)

Each frame:
```
If accelerating: speed += acceleration × grip
If braking: speed -= braking_force
speed × = surface_friction
vx = speed × COS(angle)
vy = speed × SIN(angle)
x += vx : y += vy
```

Steering rotates the angle. At high speed with low grip, the car drifts — the angle changes but the velocity vector lags behind. This creates satisfying sliding around corners.

### Rotation

The car sprite is pre-rendered at 16 or 32 angles (one shape per angle). Steering selects the nearest pre-rendered angle. With 32 angles, rotation is smooth enough to feel continuous.

Pre-computed SIN/COS tables (from Flashpoint/Craterfall experience) drive the physics.

### Scrolling

The viewport follows the player's car. The track bitmap is larger than the screen; the viewport is a window into it. Blitz's bitmap offset or blit-based scrolling keeps the car centred.

For a 500-line game, the simplest approach: draw the visible portion of the track bitmap each frame using BitMapBlit or similar. Blitz's compiled speed makes this feasible.

### AI Opponents

3 AI cars follow the racing line (a series of waypoints around the track). They accelerate on straights, brake before corners, and have slight random variation to prevent robotic uniformity. They obey the same physics as the player — oil slicks affect them too.

AI cars are shapes drawn at their current rotation angle, same as the player.

### Laps and Checkpoints

Each track has 4-6 checkpoint zones. The car must pass through all checkpoints in order to complete a lap. This prevents shortcutting. 3 laps per race.

---

## Track Design

### Scale

6 tracks, increasing in difficulty.

| Track | Theme | Difficulty | Features |
|-------|-------|-----------|----------|
| 1 | Oval | Easy | Wide road, gentle curves. Learn controls. |
| 2 | Figure-8 | Easy | Crossover point, tighter curves |
| 3 | Coastal | Medium | Narrow sections, chicanes, first oil slicks |
| 4 | Mountain | Medium | Hairpins, elevation markers (visual only), gravel traps |
| 5 | City | Hard | Right angles, narrow streets, boost pads |
| 6 | Circuit | Hard | All features combined. The championship finale. |

### Track Bitmaps

Each track is drawn as a bitmap. Road is painted dark grey, grass green, walls white, etc. The bitmap is the track AND the physics — no separate collision map needed.

Tracks can be hand-drawn in Deluxe Paint (or equivalent) and loaded, or generated procedurally from DATA (waypoints → road painting). For 500 lines, hand-drawn bitmaps loaded from disk are more practical.

---

## Game Modes

### Quick Race
Pick a track, pick difficulty (number of AI cars: 1, 2, or 3), race 3 laps.

### Championship
Race all 6 tracks in order. Points per race based on finishing position. Cumulative championship standings. The player who wins the most races across all 6 tracks is champion.

### Time Trial
Solo, no AI. Race against your own best time. Ghost car shows your previous best lap.

---

## Phase Breakdown

### Phase 1: Car and Track (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Track Bitmap | Load a track bitmap (or draw a simple oval with Blitz drawing commands). Display it. | BitMap loading, display setup |
| 2 | The Car | A small shape (pre-drawn car top-down). Place it on the track. | Shape loading, initial position |
| 3 | SIN/COS Tables | Pre-compute rotation tables (reuse from Flashpoint/Craterfall). 32 angles. | Lookup tables, trigonometry |
| 4 | Rotation | Left/right keys rotate the car. Select the nearest pre-rendered angle. The car turns smoothly. | Angle-based sprite selection |
| 5 | Acceleration | Fire button (or up key) accelerates. Speed increases, car moves forward in its facing direction. | Velocity, forward vector |
| 6 | Braking | Down key brakes. Speed decreases. Car slows to a stop. | Deceleration |
| 7 | Surface Detection | ReadPixel beneath the car. Green = grass (slow). Grey = tarmac (fast). White = wall (stop). | ReadPixel, surface-based physics |
| 8 | Friction | Different surfaces apply different friction. Grass saps speed. Tarmac is smooth. | Surface-dependent friction |
| 9 | Drifting | At high speed, the car's movement direction lags behind its facing direction. Corners produce satisfying slides. | Velocity vector vs facing angle |
| 10 | Wall Collision | Hitting a wall (white pixel): speed drops to zero, small bounce-back. | Collision response |
| 11 | Viewport Scrolling | The screen follows the car. The track bitmap is larger than the display. Viewport centres on the car. | Viewport offset, camera |
| 12 | Smooth Scrolling | Double-buffered rendering of the visible track area. No tearing, no flicker. | Double buffer with scrolling |
| 13 | Checkpoint System | Invisible checkpoint zones on the track. Pass through them in order. Track progress around the lap. | Zone detection, ordered progression |
| 14 | Lap Counter | Complete all checkpoints → lap. 3 laps → race complete. Lap counter in HUD. | Lap tracking, race completion |
| 15 | HUD | Speed, lap, position, lap time. Rendered on top of the track. | HUD overlay |
| 16 | One Track Playable | The oval track, solo, 3 laps. Car physics feel good. Drifting is satisfying. | Integration |

**Milestone:** A single-track racing game with rotation, surface physics, drifting, scrolling, and lap counting. The car feels like a car.

### Phase 2: Competition (Units 17-32)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | AI Waypoints | A series of waypoints around the track (stored as x,y pairs). The AI car steers toward the next waypoint. | Waypoint data, target steering |
| 18 | AI Steering | AI car rotates toward its target waypoint. Adjusts angle per frame. Smooth, not instant. | Angle-to-target, gradual rotation |
| 19 | AI Speed Control | AI accelerates on straights, brakes before corners (detects upcoming waypoint angle change). | Look-ahead braking |
| 20 | AI Variation | Small random offset to waypoint targets. Each AI car drives slightly differently. Not robotic. | Randomised behaviour |
| 21 | One AI Opponent | Player races against one AI car. Same physics, same surface rules. Position tracking (who's ahead). | Multi-car management, position |
| 22 | Three AI Opponents | Three AI cars with different skill levels (fast/medium/slow waypoint following). | Parameterised AI skill |
| 23 | Car-Car Collision | Cars that overlap push each other apart. Simple overlap resolution. | Inter-car collision, separation |
| 24 | Position Display | "1st / 2nd / 3rd / 4th" based on lap and checkpoint progress. Updated in HUD. | Race position calculation |
| 25 | Race Results | Race complete: finishing order, lap times, points awarded. | Results screen |
| 26 | Track 2: Figure-8 | New track bitmap with crossover. New waypoints for AI. | Second track, data for AI |
| 27 | Track 3: Coastal | Narrow sections, chicanes, oil slicks (blue pixels → zero grip). | Hazard surfaces |
| 28 | Track 4: Mountain | Hairpins requiring heavy braking. Gravel traps punish mistakes. | Technical track design |
| 29 | Track 5: City | Right angles, narrow streets, boost pads (cyan pixels → speed burst). | Boost mechanic |
| 30 | Track 6: Circuit | All features. The hardest track. Championship finale. | Capstone track |
| 31 | Championship Mode | Race all 6 tracks in order. Points: 10/6/3/1 for 1st-4th. Cumulative standings between races. | Championship state, multi-race scoring |
| 32 | Six Tracks Racing | Complete championship mode. All tracks, AI opponents, results. A real racing game. | Content-complete |

**Milestone:** Six tracks with AI opponents, championship mode, and varied surface hazards. A complete top-down racer.

### Phase 3: Polish and Production (Units 33-48)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Time Trial | Solo mode with ghost car (replay of previous best lap as a transparent shape). | Ghost replay, position recording |
| 34 | Ghost Playback | Record car position/angle each frame. Replay as a semi-transparent ghost on next attempt. | Array recording, playback |
| 35 | Difficulty Select | Easy: slow AI, wide tracks. Normal: standard. Hard: fast AI, aggressive driving. | Difficulty parameters |
| 36 | MOD Music | Menu music, in-race music (per track theme), results music. | Track Load/Play per context |
| 37 | Engine Sound | Noise channel modulated by speed. Low rumble at idle, high whine at full speed. | Speed-dependent audio |
| 38 | Skid Sound | Drifting produces a screech sound. Intensity proportional to drift angle. | Physics-based audio |
| 39 | Tyre Marks | Car leaves dark marks on the track bitmap when drifting. Permanent modification — the track shows the race's history. | Bitmap modification, persistent marks |
| 40 | Particle Gravel | Driving through gravel: small particles kick up behind the car. Compiled speed handles it. | Particles, directional spray |
| 41 | Oil Slick Animation | Oil slicks shimmer (colour cycling on the blue pixels). Visible warning before you hit them. | Localised colour cycling |
| 42 | Minimap | Small overview of the entire track in a HUD corner. Car positions shown as dots. | Scaled rendering, minimap |
| 43 | Starting Grid | Cars line up in a starting grid. Countdown: 3, 2, 1, GO! Lights (red → green). | Race start sequence |
| 44 | Title Screen | "TARMAC" with a rotating car demo (car drives around a small track loop on the title screen). | Animated title |
| 45 | High Scores | Best lap times per track. Championship records. Disk persistence. | Per-track records, file I/O |
| 46 | Edge Cases | Two cars finish simultaneously? (Use sub-pixel position for tiebreak.) Car gets stuck in wall? (Nudge out.) | Edge case handling |
| 47 | Performance | 4 cars, scrolling, particles, ghost replay. Frame time? 50fps stable? Profile and optimise. | Performance profiling |
| 48 | Balance | AI skill per difficulty. Track difficulty curve. Championship points fairness. | Full balance pass |

### Phase 4: Completion (Units 49-64)

System-friendly startup/shutdown, bootable ADF, testing across A500/A1200, the Blitz track summary.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | System Takeover | Proper Amiga startup: take over the system, restore on exit. OS-friendly. | System startup/shutdown |
| 50 | Bootable ADF | Compiled executable on a bootable ADF. Auto-starts on Amiga boot. | ADF creation |
| 51-58 | Testing across models, visual polish, sound polish, track refinement | Various | Multiple techniques |
| 59 | The Blitz Showcase | Review: this game uses compiled speed (Flashpoint), NEWTYPE structures (Gridlock), bitmap manipulation (Craterfall), and adds rotation maths, AI pathfinding, and championship structure. Everything Blitz can do. | Cumulative skill review |
| 60 | Tarmac vs Redline | Discussion: Tarmac renders the track as a bitmap read with ReadPixel. Redline (assembly Game 3) renders the road with per-scanline Copper colour changes. Same sport, opposite techniques. Both are racing games; neither could be the other. | Cross-track comparison |
| 61 | What Assembly Would Do | Discussion: assembly gives direct Blitter access for faster bitmap scrolling, copper for per-line effects, and interrupt-driven music. But for top-down racing? Blitz is genuinely close to assembly performance. The compiled code is 68000 machine code — the gap is narrow. | Honest performance comparison |
| 62 | Bug Sweep | All tracks, all modes, all difficulties. | QA |
| 63 | Line Count | Under 500 lines? Track bitmaps are loaded from disk (not in code). AI waypoints and car physics are the main code consumers. Should fit. | Scope check |
| 64 | The Finished Game | Six tracks, championship, time trial with ghost, AI opponents, surface physics, drifting, tyre marks, MOD music, bootable ADF. A complete racing game that would hold its own on an Amiga Power coverdisk. | Completion |

---

## Technical Notes

### Car Rotation

Pre-render the car at 32 angles (every 11.25°):

```blitz
; Load 32 rotation frames
For a = 0 To 31
  LoadShape a, "car_"+Str$(a)+".shape"
Next a

; Select frame based on angle
frame.w = (angle * 32 / 360) MOD 32
BBlit 0, frame, car_x - cam_x, car_y - cam_y
```

Or generate rotations at startup from a single source image using Blitz's rotation commands if available.

### Surface Physics

```blitz
; Read surface colour beneath car
surface.w = ReadPixel(Int(car_x), Int(car_y))

Select surface
  Case TARMAC_COLOUR
    grip.q = 1.0 : friction.q = 0.98
  Case GRASS_COLOUR
    grip.q = 0.4 : friction.q = 0.92
  Case GRAVEL_COLOUR
    grip.q = 0.6 : friction.q = 0.94
  Case WALL_COLOUR
    speed = 0 : ; bounce back
  Case OIL_COLOUR
    grip.q = 0.1 : friction.q = 0.99
  Case BOOST_COLOUR
    speed = speed + 3
End Select
```

### AI Waypoint Following

```blitz
; AI steers toward next waypoint
target_angle.w = ATan2(way_y(next_wp) - ai_y, way_x(next_wp) - ai_x)
angle_diff.w = target_angle - ai_angle

; Normalise to -180..180
If angle_diff > 180 Then angle_diff = angle_diff - 360
If angle_diff < -180 Then angle_diff = angle_diff + 360

; Gradual steering (not instant)
If angle_diff > 0 Then ai_angle = ai_angle + Min(angle_diff, 5)
If angle_diff < 0 Then ai_angle = ai_angle + Max(angle_diff, -5)

; Brake before sharp corners
next_diff.w = ... ; angle between current and next+1 waypoint
If Abs(next_diff) > 45 And distance_to_wp < 50
  ai_speed = ai_speed * 0.9  ; brake
End If
```

### Memory

- Track bitmaps: ~40-60 KB each (loaded one at a time)
- Car shapes (32 angles × 4 cars): ~10 KB
- Program: ~12-15 KB
- Variables, waypoints, state: ~2 KB
- MOD music: ~20-40 KB
- Total in memory: ~100-130 KB — fits in 512 KB

---

## Design Notes

### Why Top-Down Racing

Top-down racing contrasts directly with the assembly track's Redline (pseudo-3D). Both are racing games. But Tarmac reads pixels from a bitmap for physics. Redline writes Copper colour changes per scanline for depth. Same sport, opposite rendering philosophy. A learner who builds both understands that "racing game" is a design concept, not a rendering technique.

### The Bitmap as Physics

Like Craterfall's terrain, the track bitmap IS the game state. ReadPixel tells you everything: surface type, wall collision, checkpoint detection. No separate collision map. This is elegant, fast, and teaches an important principle: sometimes the simplest data structure is the one you're already drawing.

### The Blitz Arc

1. **Flashpoint**: compiled speed, many objects (arena action)
2. **Gridlock**: structured data, NEWTYPE (tower defence)
3. **Craterfall**: bitmap manipulation, physics (destructible terrain)
4. **Tarmac**: rotation, AI, surface physics, championship (racing)

Four games, four showcases of compiled BASIC's power. Each one would struggle in AMOS. Together they make the case: Blitz Basic isn't a toy language — it's a commercial development tool.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Blitz Game 4 in the restructured Amiga BASIC track. Top-down racing contrasting with the assembly track's pseudo-3D approach.
