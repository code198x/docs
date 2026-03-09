# AMOS Game 01: Ricochet

**Track:** AMOS
**Genre:** Sprite-based action game
**Units:** 64 (4 phases × 16 units)
**Language:** AMOS Professional
**Max lines:** ~500

---

## Premise

Objects bounce around the screen — balls, projectiles, hazards. The player controls a paddle, shield, or character and must deflect, catch, or dodge them. It's Pong meets Breakout meets chaos: multiple bouncing objects with different behaviours, all rendered as smooth AMOS BOBs.

AMOS makes this immediate. `Bob 1, 100, 100, 1` — there's a sprite. Move it, bounce it off walls, detect collisions. The game comes together visually from unit 1. The learner focuses on game design and physics, not hardware registers.

---

## Core Mechanics

### Bouncing Objects

Multiple balls/objects move simultaneously, each with independent velocity (dx, dy). They bounce off screen edges (reverse dx or dy on contact). Some bounce off each other. The player's paddle/shield deflects them.

### Object Types

| Type | Behaviour | Colour | Points |
|------|-----------|--------|--------|
| Standard ball | Bounces off walls and paddle | White | 10 on catch |
| Speed ball | Faster, harder to track | Yellow | 25 |
| Splitter | Splits into two on paddle hit | Cyan | 15 each |
| Hazard | Must be dodged, not caught | Red | −1 life if hit |
| Power-up | Slow briefly, collect for bonus | Green | 50 + effect |

### The Player

A paddle or shield that moves with joystick or mouse. The player must position themselves to catch/deflect balls and avoid hazards. Mouse control is natural on the Amiga — AMOS exposes it directly.

### Scoring

Catch standard balls for points. Dodge hazards. Survive as long as possible. The game gets harder: more objects, faster speeds, more hazards. Wave-based progression.

---

## Phase Breakdown

### Phase 1: BOBs and Bounce (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | AMOS Environment | Screen Open, Flash Off, Curs Off, Cls. The AMOS editor and how to run a program. | AMOS basics, Screen Open |
| 2 | First BOB | Load a sprite bank, Bob 1, 100, 100, 1 — a sprite appears. Move it by changing coordinates. | Bob command, sprite banks |
| 3 | Movement | dx/dy variables. Each frame: x=x+dx, y=y+dy. Bob moves smoothly. Wait Vbl for sync. | Variables, frame-based movement, Wait Vbl |
| 4 | Wall Bounce | If x hits screen edge, dx=-dx. Same for y. The ball bounces endlessly. | Boundary detection, velocity reversal |
| 5 | The Paddle | A second BOB controlled by joystick (Joy(1)). Moves left/right at the bottom of the screen. | Joystick input, player control |
| 6 | Mouse Control | Alternative: X Mouse, Y Mouse position the paddle. Smoother, more Amiga-native. Support both. | Mouse input, X Mouse/Y Mouse |
| 7 | Collision Detection | Bob Col(1) checks if BOB 1 collides with another BOB. Ball hits paddle → bounce upward. | Bob Col, collision response |
| 8 | Ball Reset | Ball exits the bottom → lose a life. Ball resets to top. | Fail state, reset logic |
| 9 | Multiple Balls | Two balls bouncing simultaneously. Independent dx/dy. Both collide with the paddle. | Arrays for object state, multiple BOBs |
| 10 | Speed and Angles | Different starting angles. Some balls faster than others. Paddle hit position affects bounce angle. | Angle variation, position-based deflection |
| 11 | Score Display | Text command shows score. Locate for positioning. Update each frame. | Text display, score tracking |
| 12 | Lives Display | Three paddle icons as life indicators. Lose one when a ball escapes. | Life counter, visual feedback |
| 13 | Sound Effects | Boom for paddle hit. Shoot for wall bounce. Sample Play for custom sounds if available. | AMOS sound commands |
| 14 | Game Over | Zero lives → game over screen. High score check. Play again prompt. | End state, high score |
| 15 | Waves | Wave 1: 2 balls. Wave 2: 3 balls. Wave 3: faster. Clear a wave by catching all balls (or surviving a timer). | Wave progression, difficulty ramp |
| 16 | Polish | Ball trails (brief afterimage via second BOB at previous position). Screen shake on miss (Screen Offset briefly). | Visual effects, juice |

**Milestone:** Multiple bouncing balls, paddle control, collision, waves, score, lives. A playable game that demonstrates AMOS's immediate visual power.

### Phase 2: Chaos (Units 17-32)

More object types, power-ups, and the game becomes genuinely challenging.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Speed Balls | Yellow balls that move 50% faster. Worth more points. Harder to track. | Object variety, parameterised speed |
| 18 | Splitter Balls | On paddle hit, splits into two balls moving in different directions. More chaos. | Object spawning, array management |
| 19 | Hazard Objects | Red objects that must be dodged. Hitting one = lose a life. Different sprite image. | Collision with penalty, type checking |
| 20 | Power-Ups | Green objects: catch for slow-motion effect (all balls slow for 3 seconds). | Timed power-up, global speed modifier |
| 21 | Wider Paddle | Power-up: paddle expands for 5 seconds. Sprite image swap to wider version. | Timed sprite swap, power-up variety |
| 22 | Screen Flash | On life lost: screen flashes red (Screen Colour). On wave clear: flash green. | Screen Colour for feedback |
| 23 | Background | Simple drawn background (Ink, Box, Bar) — a playing field border. Balls bounce inside it. | AMOS drawing commands |
| 24 | Difficulty Curve | Each wave: +1 ball, +10% speed, more hazards. By wave 10, the screen is chaotic. | Escalating parameters |
| 25 | High Score Table | Top 5 scores. Name entry. Persistent during session. | Score table, string input |
| 26 | Combo System | Catch multiple balls without a miss = score multiplier. ×2, ×3, ×4. Broken by a miss. | Combo tracking, streak |
| 27 | Ball Trails | Each ball leaves a fading trail (3 previous positions drawn as smaller/dimmer BOBs). Looks dynamic. | Trail rendering, ring buffer |
| 28 | Particle Burst | On ball catch: brief particle effect (4-5 tiny BOBs scatter outward then fade). | Particle system, short-lived objects |
| 29 | Sound Variety | Different pitch per ball type. Splitter has a distinctive crack. Hazard has a warning hum. | Pitched sound effects |
| 30 | Wave Intro | "WAVE 5" title card with ball preview (what types will appear). Brief pause before chaos. | Inter-wave pacing |
| 31 | Difficulty Select | Easy (slow, few hazards), Normal, Hard (fast, many hazards, small paddle). | Difficulty parameters |
| 32 | Fifteen Waves | 15 waves of escalating chaos. Playable, balanced, satisfying. | Content-complete |

**Milestone:** 15 waves with 5 object types, power-ups, combos, particle effects, and a high score table. AMOS at its most immediate and fun.

### Phase 3: Polish (Units 33-48)

Visual refinement, attract mode, and the features that make it feel professional.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Title Screen | "RICOCHET" with bouncing ball animation on the title. BOBs work on any screen. | Title design with active sprites |
| 34 | Attract Mode | Automated demo: balls bounce without player input. Shows the game in motion. | AI paddle, attract loop |
| 35 | Copper Background | AMOS Copper commands for gradient backgrounds. Sky fading from blue to black. | AMOS Copper interface |
| 36 | Palette Animation | Cycling colours on the background. Pulsing border. Neon feel. | Colour cycling, palette manipulation |
| 37 | Instructions Screen | Controls, object types (with sprites shown), scoring. Visual instructions. | Onboarding |
| 38 | Two-Player Mode | Second paddle at top (or split-screen). Both players catch balls. Competitive or cooperative. | Two-player input, dual state |
| 39 | Smooth Transitions | Between waves: balls slow and exit screen, brief pause, new wave enters. Not instant. | Choreographed transitions |
| 40 | Frame Rate Check | Monitor frame rate. Is Wait Vbl keeping us at 50fps? With 15+ BOBs, does it slow? | Performance awareness |
| 41 | BOB Optimisation | Use hardware sprites (Sprite command) for the paddle/player, BOBs for balls. Sprites are faster. | Sprite vs BOB trade-offs |
| 42 | Screen Zones | Divide the screen into zones. Balls in certain zones are worth more. Zone colour changes. | Zone-based scoring, screen regions |
| 43 | Achievement Messages | "DOUBLE CATCH!", "SPLITTER COMBO!", "SPEED DEMON!" — brief text flashes for notable plays. | Event-triggered messages |
| 44 | Statistics Screen | Games played, best wave, total balls caught, longest combo. Session stats. | Aggregate statistics |
| 45 | Edge Cases | Two balls hit paddle simultaneously? (Both bounce.) Splitter creates ball that immediately hits hazard? (Valid.) | Edge case testing |
| 46 | Bug Sweep | All 15 waves on all difficulties. Two-player mode. Every object interaction. | QA methodology |
| 47 | Balance Final | Is wave 15 possible on Hard? Is Easy too easy? Does the combo system reward skill? | Final balance |
| 48 | Line Count | Under 500 lines? BOB management and wave data are the biggest consumers. | Code budget |

### Phase 4: Completion (Units 49-64)

Final features, the MOD preview, and the bridge to Game 2.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Menu System | Title → Instructions → Difficulty → 1P/2P → Play → Game Over → Title. Clean GOSUB flow. | Menu state machine |
| 50 | Persistent High Scores | Write high scores to disk (Open Out, Print #). Read on startup (Open In, Input #). Survive between sessions. | File I/O |
| 51-56 | Visual polish, sound design, ball physics refinement, wave balancing | Various improvements | Multiple techniques |
| 57 | MOD Music Preview | Track Load "music.mod": Track Play. Music plays during title screen. First MOD integration. | Track Load, Track Play |
| 58 | Music + SFX | Sam Play during gameplay for effects, while MOD plays. Channel allocation matters. | Audio channel management |
| 59-62 | Testing, edge cases, performance profiling | QA and optimisation | Various |
| 63 | Line Count Final | Under 500 lines. If file I/O and MOD push over, they become documented extensions. | Scope management |
| 64 | The Finished Game | 15 waves, 5 object types, power-ups, combos, particles, two-player, MOD music, high scores. A real game. | Completion |

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old AMOS Game 1 (Pixel Hunter) with a more ambitious bouncing-objects action game.
