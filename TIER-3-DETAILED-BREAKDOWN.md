# Tier 3 Detailed Breakdown: LIMITS

**Phase:** 0 (Foundations)
**Tier:** 3 (Lessons 33-48)
**Theme:** "Pushing Against the Ceiling"
**Pedagogical Goal:** Deliberately attempt impossible techniques to viscerally demonstrate BASIC limitations

---

## Tier 3 Philosophy

**Unlike Tier 2 where limits emerge naturally, Tier 3 deliberately attempts impossible things.**

Students will:
- Try to implement professional techniques in BASIC
- See flickering, unstable timing, and performance failures
- Experience visceral frustration that creates *need* for assembly
- Understand *why* assembly exists, not just *how* it works

**Key "Honest Failure" Lessons:**
- **L36**: Attempting sprite multiplexing → Visible flickering
- **L42**: Mid-screen color changes → Unstable raster bars
- **L46**: Real-time animation → Jerky, inconsistent frame timing

These aren't "you did something wrong" failures. They're "BASIC cannot do this" failures.

---

## Section 1: Sprite Mastery (Lessons 33-37)

**Arc:** From simple multi-color sprites through impossible multiplexing

### Lesson 33: Multi-Colour Sprites
**Concept:** Sprite multi-color mode (more colors, lower resolution)
**WOW Moment:** Four-color sprite graphics
**Hardware:** 53276 (sprite multi-color enable), 53285-53286 (shared colors)

**Technical Details:**
- Multi-color mode trades X resolution for colors (12x21 vs 24x21)
- Each pixel uses 2 bits → 4 colors possible
- Colors: transparent, sprite color, shared color 1, shared color 2
- Bit pattern: `00`=transparent, `01`=sprite color, `10`=shared1, `11`=shared2

**Code Examples:**
1. Simple multi-color sprite (4-color spaceship)
2. Multiple multi-color sprites with different individual colors but shared palette

**Game Context:** Better-looking sprites in arcade games (Pac-Man ghosts, detailed characters)

**Progression Notes:**
- Builds on L17-22 single-color sprites
- Prepares for L36 multiplexing (where resolution matters)

---

### Lesson 34: Sprite Priorities & Collisions
**Concept:** Display order, sprite-sprite and sprite-background collision detection
**WOW Moment:** Detecting when sprites overlap
**Hardware:** 53275 (priority), 53279 (sprite-sprite), 53278 (sprite-background)

**Technical Details:**
- Priority bit: sprite-behind-background vs sprite-in-front
- Collision registers are READ-ONLY status flags
- Reading collision register clears it (must read before next frame!)
- Bit mask: bit N = 1 means sprite N collided

**Code Examples:**
1. Sprite priority demo (spaceship behind cloud, in front of ground)
2. Collision detection game loop (bullet hits enemy → explosion)

**Game Context:** Essential for any action game (hit detection)

**Common Mistakes to Address:**
- Reading collision register multiple times per frame
- Not clearing collision register between frames
- Assuming background collision works without setting priority bit

**Progression Notes:**
- Builds collision foundation for L35-37 game mechanics
- Collision detection becomes critical in L36 multiplexing test

---

### Lesson 35: Sprite Expansion
**Concept:** Double-width and double-height sprites
**WOW Moment:** Giant sprites without more data
**Hardware:** 53277 (Y expansion), 53278 (X expansion)

**Technical Details:**
- Each pixel rendered twice (2x2 for both directions)
- 24x21 becomes 48x42 (or 12x21→24x42 for multi-color)
- No memory cost, just register POKE
- Can expand X and Y independently

**Code Examples:**
1. Boss enemy that grows larger as it approaches
2. Zoom effect (sprite grows from small to 2x size)

**Game Context:** End-level bosses, power-up effects, simple scaling

**Visual Considerations:**
- Expanded sprites look blocky (pixel doubling visible)
- Multi-color + expansion = very chunky appearance
- Best for intentional "large" objects, not smooth scaling

**Progression Notes:**
- Final sprite hardware feature before L36 limit-test
- Sets up "we need more sprites" desire for multiplexing lesson

---

### Lesson 36: Attempting Multiplexing ⚡ (HONEST FAILURE)
**Concept:** Try to show >8 sprites using manual repositioning
**WOW Moment:** It (barely) works... then it doesn't
**Reality Check:** Visible flickering, missed updates, broken collision detection

**What Students Attempt:**
```basic
100 REM Try to show 16 sprites
110 FOR I=0 TO 7: POKE 53248+I*2,X(I): POKE 53249+I*2,Y(I): NEXT
120 FOR I=8 TO 15: POKE 53248+(I-8)*2,X(I): POKE 53249+(I-8)*2,Y(I): NEXT
130 REM Wait for screen to draw...
140 FOR D=1 TO 10: NEXT D
150 GOTO 110
```

**Why It Fails:**
1. **Timing inconsistency**: FOR loops take variable time
2. **Visible flicker**: Eye sees repositioning happen
3. **Collision breaks**: Can't check collisions for "virtual" sprites
4. **No raster synchronization**: Updates happen whenever BASIC gets there

**The Learning Moment:**
Students see 16 sprites... but they flicker wildly. Moving them makes it worse. Checking collisions breaks completely. This isn't "you need to optimize your code" — **BASIC fundamentally cannot time this precisely**.

**Code Examples:**
1. "Working" 12-sprite display (mostly stable when not moving)
2. 16-sprite game attempt (bullet hell) → unplayable flickering

**Assembly Teaser:**
"In assembly, you can trigger this update during vertical blank using IRQ. That's lesson 58."

**Progression Notes:**
- First explicit "BASIC can't do this" moment
- Creates visceral desire for timing control
- References forward to Tier 4 IRQ lesson

---

### Lesson 37: Sprite Animation Patterns
**Concept:** Frame animation, movement patterns, practical sprite techniques within limits
**WOW Moment:** Smooth character walk cycle
**Scope:** What BASIC *can* actually do well with sprites

**Technical Details:**
- Sprite pointer animation: change 2040-2047 to switch frames
- Frame timing using FOR-NEXT delays or timer reads
- Movement patterns: circular motion (SIN/COS tables), figure-8, patrol routes
- Pre-calculated paths stored in arrays

**Code Examples:**
1. Walking character (4-frame cycle) with movement
2. Patrol enemy with directional facing (change sprite frames based on direction)
3. Circular orbiting enemies (pre-calculated SIN/COS table)

**Game Context:** This is what professional games *actually* did in BASIC before switching to assembly

**Reality Check:**
"We can animate 6-8 sprites smoothly in BASIC. That's enough for many games. Multiplexing isn't needed unless you're making bullet hell or strategy games with dozens of units."

**Progression Notes:**
- Bookend after L36 failure lesson
- Shows what students *should* do with sprites in BASIC
- Completes sprite curriculum before moving to sound

---

## Section 2: Advanced Sound (Lessons 38-40)

**Arc:** From simple multi-voice to synchronized sound+sprite, hitting timing limits

### Lesson 38: Sound Envelopes & ADSR
**Concept:** Attack-Decay-Sustain-Release envelope shaping
**WOW Moment:** Realistic instrument sounds (piano, strings, drums)
**Hardware:** 54277-54278, 54284-54285, 54291-54292 (ADSR registers per voice)

**Technical Details:**
- **Attack:** 0-15 (how fast sound reaches peak, 2ms-8sec)
- **Decay:** 0-15 (how fast sound drops to sustain level)
- **Sustain:** 0-15 (held volume level while gate=1)
- **Release:** 0-15 (how fast sound fades after gate=0)

**Envelope Register Format:**
```
54277 (Voice 1 A/D): High nibble = Attack, Low nibble = Decay
54278 (Voice 1 S/R): High nibble = Sustain, Low nibble = Release
```

**Instrument Presets:**
- Piano: Fast attack (5), medium decay (8), low sustain (3), medium release (5)
- Strings: Slow attack (10), slow decay (10), high sustain (12), slow release (10)
- Percussion: Instant attack (0), fast decay (2), zero sustain (0), fast release (1)

**Code Examples:**
1. Three instruments playing the same note (C) with different envelopes
2. Drum kit (different envelopes on noise waveform)

**Common Mistakes:**
- Forgetting to set ADSR → silent output or stuck notes
- Not understanding gate bit must go 0→1 to retrigger
- Trying to change ADSR during note (doesn't work, must retrigger)

**Progression Notes:**
- Builds on L23-25 basic sound
- Prepares for L39 music player with shaped notes
- ADSR timing will become issue in L40 synchronization lesson

---

### Lesson 39: Music Sequences
**Concept:** Note arrays, rhythm timing, simple music player
**WOW Moment:** Playing a recognizable melody (Public domain tune: "Westminster Chimes")
**Challenge:** Timing consistency for rhythm

**Technical Details:**
- Note frequency table (MIDI note → SID frequency value)
- Duration array (quarter note, eighth note, half note)
- Timing using TI or FOR-NEXT (both problematic)

**Data Structures:**
```basic
100 REM Note data: pitch, duration (frames)
110 DIM N(32): REM Note frequencies
120 DIM D(32): REM Durations in frames
130 DATA 4816,60,4304,60,3822,60,3405,120: REM G-E-F-C (Westminster)
```

**Code Examples:**
1. Simple melody player (Westminster Chimes, public domain)
2. Two-voice harmony (melody + bass line)

**The Timing Problem:**
Students will notice notes sometimes run together or have gaps. This is because:
- FOR-NEXT isn't frame-accurate
- TI updates only every 1/60 second but reading it takes variable time
- Playing note + waiting + stopping note = accumulated timing errors

**Foreshadowing:**
"Music timing in BASIC is approximate. Professional games used assembly with raster interrupts to get exact timing. We'll see why this matters in lesson 40."

**Progression Notes:**
- Shows what's possible (short melodies work fine)
- Sets up timing frustration for L40
- Music data structures used again in L48 synthesis game

---

### Lesson 40: Sound + Sprite Synchronization ⚡ (LIMITS EXPOSED)
**Concept:** Try to synchronize sound effects with sprite actions
**WOW Moment:** Explosion sound plays... sometimes when sprite collides
**Reality Check:** Timing drift, missed triggers, sound lags behind visuals

**The Challenge:**
```basic
100 REM Game loop with sound+sprite sync
110 X=X+VX: POKE 53248,X: POKE 53249,Y
120 IF COLLISION THEN GOSUB 500
...
500 REM Explosion effect
510 POKE 54276,129: REM Trigger sound
520 POKE 53287,2: REM Flash sprite red
530 FOR T=1 TO 10: NEXT: REM Wait
540 POKE 54276,128: REM Sound off
550 POKE 53287,14: REM Restore color
560 RETURN
```

**Why It Fails:**
1. **GOSUB overhead**: Jumping to subroutine takes time
2. **Variable timing**: Collision check happens at different times each frame
3. **Sound latency**: BASIC gets to POKE 54276 whenever it gets there
4. **No frame lock**: Game loop isn't synchronized to screen refresh

**Observable Problems:**
- Explosion sound starts after sprite has already moved
- Sometimes sound plays twice (loop iteration timing)
- Music tempo drifts if playing background music + sound effects

**The Hard Truth:**
"BASIC executes line-by-line whenever it gets there. Real games need frame-perfect timing, which requires interrupts. Assembly can trigger sounds during vertical blank, while BASIC is still processing line 120."

**Code Examples:**
1. "Working" collision sound (short delay, mostly acceptable)
2. Failing music+effects combination (tempo drifts audibly)

**Assembly Teaser:**
"Assembly IRQ can update SID registers exactly every 1/60 second while your BASIC game logic runs. That's lesson 59."

**Progression Notes:**
- Second major "BASIC can't do this" moment
- Explains why commercial games sound better
- Completes sound section, transitions to raster effects

---

## Section 3: Raster Concepts (Lessons 41-43)

**Arc:** Understanding screen drawing, then failing to control it

### Lesson 41: Understanding Rasters
**Concept:** How CRT beam draws screen, raster lines, vertical blank
**WOW Moment:** Reading raster position register
**Hardware:** 53266 (raster line register, read-only)

**Technical Details:**
- Screen draws top-to-bottom, left-to-right
- 312 total raster lines (PAL), 263 (NTSC)
- Visible area: lines ~50-250
- Vertical blank: lines 300-312 (safe time to update sprite positions)
- Raster register 53266: current line being drawn (0-255), bit 7 of 53265 for line 256+

**Reading Raster Position:**
```basic
100 R=PEEK(53266): REM Read current raster line
110 IF R>127 THEN R=R-256+256*PEEK(53265): REM Handle >255
```

**Code Examples:**
1. Raster position display (print which line is being drawn)
2. Waiting for vertical blank:
```basic
100 IF PEEK(53266)<250 THEN 100: REM Wait for vblank
110 REM Safe to update sprites now
```

**Why This Matters:**
Updating sprites mid-screen causes visible tearing (sprite appears in two places). Updating during vblank is invisible.

**The Catch:**
Waiting for vblank in BASIC means unpredictable delays (line 100 might loop 10 times or 100 times depending on when you hit it).

**Progression Notes:**
- Foundational concept for L42 raster bars
- Explains why sprite updates sometimes look wrong
- Sets up "we need timing control" for L42

---

### Lesson 42: Mid-Screen Color Changes ⚡ (HONEST FAILURE)
**Concept:** Try to change background color at specific raster lines
**WOW Moment:** Colored bars appear... shakily
**Reality Check:** Unstable bars, timing jitter, impossible to get stable

**The Technique:**
```basic
100 REM Wait for raster line 100
110 IF PEEK(53266)<>100 THEN 110
120 POKE 53280,2: REM Change border color to red
130 REM Wait for raster line 150
140 IF PEEK(53266)<>150 THEN 140
150 POKE 53280,5: REM Change to green
160 REM Wait for raster line 200
170 IF PEEK(53266)<>200 THEN 170
180 POKE 53280,6: REM Change to blue
190 GOTO 100
```

**Why It Fails Visibly:**
1. **PEEK timing**: Reading 53266 takes ~4 microseconds
2. **Comparison overhead**: `<>100` takes more time
3. **Variable loop timing**: Sometimes you catch line 100, sometimes 101
4. **POKE latency**: Writing to 53280 happens "sometime around" line 100
5. **Accumulated jitter**: Each wait point adds more timing uncertainty

**What Students See:**
- Bars appear... but they shake up and down
- Bar positions vary by 3-5 raster lines each frame
- Adding more bars makes it worse
- Bars sometimes "jump" wildly

**The Hard Truth:**
"This is a BASIC interpreter problem, not a coding problem. Each BASIC statement takes variable time. Assembly can hit exact raster lines because it controls CPU cycles. BASIC can't."

**Professional Examples:**
Show screenshots of stable raster bars in commercial games, explain they're all assembly.

**Code Examples:**
1. Two-bar attempt (unstable but visible)
2. Five-bar attempt (completely unusable)

**Assembly Teaser:**
"In assembly, you can trigger color changes using raster interrupt. The CPU will jump to your code at exactly line 100, every frame. That's lesson 60."

**Progression Notes:**
- Most visible "BASIC failure" moment in Tier 3
- Creates strong desire for precise timing control
- Often cited by students as "the moment I wanted to learn assembly"

---

### Lesson 43: Raster-Safe Update Windows
**Concept:** Practical workaround—update during safe zones only
**WOW Moment:** Stable sprite updates by timing them right
**Scope:** What you *can* do with raster awareness in BASIC

**The Technique:**
```basic
100 REM Game loop
110 GOSUB 1000: REM Update game logic
120 GOSUB 2000: REM Wait for safe zone
130 GOSUB 3000: REM Update graphics
140 GOTO 100
...
2000 REM Wait for vertical blank
2010 IF PEEK(53266)<250 THEN 2010
2020 RETURN
```

**Why This Works:**
- Game logic runs "whenever" (lines 110-990)
- Wait for vblank before graphics updates (line 2000)
- All POKEs to VIC-II happen during safe window (lines 3000+)

**Tradeoffs:**
- ✅ No visible tearing or flicker
- ✅ Stable sprite positions
- ❌ Frame rate is variable (depends on logic time)
- ❌ Slow frames cause jerky animation

**Code Examples:**
1. Sprite game with vblank sync (smooth visuals, variable speed)
2. Without vblank sync (faster but visible tearing)

**Game Context:**
"Many BASIC games use this technique. It's good enough for turn-based games, slow-moving action games, and anything where precise timing doesn't matter."

**Reality Check:**
"This solves tearing but not timing. If your logic takes 0.5 frames, you get 120fps. If it takes 1.5 frames, you get 40fps. Same code, different speeds depending on what's happening. Assembly can guarantee consistent frame time."

**Progression Notes:**
- Bookend after L42 failure lesson
- Shows practical raster awareness
- Completes raster section before optimization

---

## Section 4: Optimization (Lessons 44-47)

**Arc:** Squeezing maximum performance from BASIC before admitting defeat

### Lesson 44: Variable Speed & Lookup Tables
**Concept:** Replace calculations with pre-computed data
**WOW Moment:** 3x speed improvement from removing multiplications
**Technique:** Array lookups beat math operations

**Why Variables Are Slow:**
BASIC stores variables in a linear list. Finding `ENEMYX` requires scanning from the start of the variable table each time.

**Variable Name Timing:**
- `A` → ~0.5ms lookup
- `AA` → ~0.7ms lookup
- `ENEMYX` → ~2.0ms lookup
- `A(5)` → ~1.0ms lookup (faster than long names!)

**Array Lookups vs Math:**
```basic
REM Slow: Calculate sine every frame
100 X=X+2
110 Y=100+50*SIN(X/10): REM ~5ms

REM Fast: Lookup pre-computed values
100 X=X+1: IF X>62 THEN X=0
110 Y=100+S(X): REM ~0.8ms

1000 REM Build sine table once
1010 DIM S(62)
1020 FOR I=0 TO 62
1030 S(I)=50*SIN(I/10)
1040 NEXT
```

**Code Examples:**
1. Before/after comparison (calculated circle vs lookup table circle)
2. Movement pattern optimization (8-direction table vs IF/THEN chain)

**Technique Catalog:**
- Use short variable names (A,B,C) for hot paths
- Build lookup tables for SIN/COS, square roots, multiplication
- Use arrays instead of long variable names
- Pre-calculate constants outside loops

**Game Context:**
"Most BASIC games with smooth action use lookup tables extensively. It's the difference between 15fps and 30fps."

**Progression Notes:**
- Practical optimization students can apply immediately
- Shows thoughtful BASIC can be fast
- Sets up L45 loop optimization

---

### Lesson 45: Loop Unrolling & Batch Updates
**Concept:** Eliminate loop overhead by writing out operations
**WOW Moment:** Sprite update goes from 12ms to 4ms
**Tradeoff:** Code size vs speed

**Loop Overhead:**
```basic
REM Slow: 8 iterations of loop overhead
100 FOR S=0 TO 7
110 POKE 53248+S*2,X(S)
120 POKE 53249+S*2,Y(S)
130 NEXT S
```

Every loop iteration:
- Increments S
- Compares S to 7
- Calculates 53248+S*2 (twice!)
- Jumps back to line 110

**Unrolled Version:**
```basic
REM Fast: No loop overhead
100 POKE 53248,X(0):POKE 53249,Y(0)
110 POKE 53250,X(1):POKE 53251,Y(1)
120 POKE 53252,X(2):POKE 53253,Y(2)
130 POKE 53254,X(3):POKE 53255,Y(3)
140 POKE 53256,X(4):POKE 53257,Y(4)
150 POKE 53258,X(5):POKE 53259,Y(5)
160 POKE 53260,X(6):POKE 53261,Y(6)
170 POKE 53262,X(7):POKE 53263,Y(7)
```

**When to Unroll:**
- ✅ Small, fixed-size loops (8 sprites, 4 voices)
- ✅ Inner loops called every frame
- ❌ Large loops (don't unroll 40-column screen clear!)
- ❌ Variable iteration counts

**Code Examples:**
1. Sprite update loop unrolling (8 iterations)
2. Multi-voice sound update unrolling (3 voices)
3. Partial unrolling (process 2 items per iteration instead of 1)

**Reality Check:**
"Unrolling helps, but you're trading program memory for speed. BASIC programs are limited to ~38K. Use this technique selectively."

**Progression Notes:**
- Classic optimization technique (used in assembly too!)
- Shows diminishing returns of BASIC optimization
- Prepares for L46 profiling lesson

---

### Lesson 46: Profiling & Bottlenecks ⚡ (LIMITS EXPOSED)
**Concept:** Measure where time is spent, try to optimize critical paths
**WOW Moment:** 80% of time in 20% of code
**Reality Check:** Even fully optimized, BASIC can't hit 50fps

**Profiling Technique:**
```basic
100 T=TI: REM Start timer
110 GOSUB 1000: REM Game logic
120 L=TI-T: PRINT "LOGIC:";L
130 T=TI
140 GOSUB 2000: REM Graphics update
150 G=TI-T: PRINT "GRAPHICS:";G
160 T=TI
170 GOSUB 3000: REM Input handling
180 I=TI-T: PRINT "INPUT:";I
```

**What Students Discover:**
- Input handling: ~1 frame
- Graphics updates: ~2 frames (sprite+collision+color POKEs)
- Game logic: ~3 frames (collision checks, AI, scoring)

**Total frame time: ~6 frames (360ms) → 10fps maximum**

**After Full Optimization:**
- Lookup tables instead of calculations
- Loop unrolling for sprites
- Short variable names
- Batch updates

**Best case: ~3 frames (180ms) → 20fps**

**The Reality:**
"We optimized by 50%... but 20fps still isn't arcade-smooth. Professional games run at 50fps (PAL) or 60fps (NTSC). Even perfectly optimized BASIC can't reach that for action games."

**Why BASIC Has a Floor:**
1. **Interpreter overhead**: Every statement is parsed at runtime
2. **Variable lookup**: Linear search through name table
3. **No inline operations**: Each operation is a function call internally
4. **Memory access**: BASIC data in slow RAM, can't use CPU registers

**Code Examples:**
1. Profiled game loop showing bottlenecks
2. Before/after optimization comparison (still not fast enough)

**The "Giving Up" Moment:**
"You've done everything right. Lookup tables, unrolled loops, short variables. This is as fast as BASIC gets. And it's still not fast enough for the game you want to make. This is why assembly exists."

**Assembly Teaser:**
"The same sprite update in assembly takes 0.02 frames. The same collision check takes 0.01 frames. That's 100x faster. Not because you're a better coder in assembly—because assembly doesn't have interpreter overhead."

**Progression Notes:**
- Third major "BASIC can't do this" moment (after L36 multiplexing, L42 raster bars)
- Quantifies the problem (numbers don't lie)
- Creates readiness for assembly transition in Tier 4

---

### Lesson 47: Hybrid Programs (BASIC + Machine Code)
**Concept:** Call assembly routines from BASIC for critical sections
**WOW Moment:** BASIC game with 50fps sprite updates
**Reality Check:** You're learning assembly anyway...

**The Technique:**
```basic
100 REM Load assembly sprite routine
110 FOR I=0 TO 127
120 READ B: POKE 49152+I,B
130 NEXT
140 REM ... sprite data ...
9000 DATA 169,0,141,0,212: REM Assembly code
...
1000 REM Game loop in BASIC
1010 GOSUB 2000: REM Game logic (BASIC)
1020 SYS 49152: REM Update sprites (assembly)
1030 GOTO 1000
```

**What's Possible:**
- BASIC handles game logic, story, menus
- Assembly handles sprite updates, collision, sound
- Best of both: BASIC flexibility + assembly speed

**The Catch:**
"You're writing assembly now. The hard part isn't calling it from BASIC—it's writing the assembly. If you're going to learn assembly anyway, why not write the whole game in it?"

**Code Examples:**
1. BASIC game with assembly sprite multiplexer (16 stable sprites)
2. BASIC game with assembly raster routine (stable color bars)

**Professional Context:**
"Some commercial games did this:
- BASIC for text adventure logic, assembly for graphics
- BASIC for turn-based strategy, assembly for scrolling map
- BASIC for game editor, assembly for playback

But most action games were pure assembly because the integration overhead wasn't worth it."

**Progression Notes:**
- Shows hybrid approach is possible
- Also shows it's a stepping stone, not a destination
- Transitions naturally to "let's just learn assembly" (Tier 4)

---

## Section 5: Synthesis (Lesson 48)

### Lesson 48: "Against the Wall" — Limits Showcase Game 🔗
**Type:** Synthesis Project
**Concept:** Build a complete game that deliberately hits every BASIC limit
**Genre:** Single-screen arena shooter with escalating challenges
**WOW Moment:** Playable game that makes limits visceral

**Game Design:**
```
AGAINST THE WALL
─────────────────────────────────────────
You're a sprite bouncing in an arena. Enemies spawn at edges.
Your bullets can only travel a short distance (8 sprites max).
As waves progress, enemy count increases until...

Wave 1: 4 enemies (smooth)
Wave 2: 6 enemies (playable)
Wave 3: 8 enemies (all sprites used, no bullets!)
Wave 4: 12 enemies (flickering multiplexing attempt)
Wave 5: 16 enemies (game breaks down into slideshow)
```

**Curriculum Connections:**
This game uses EVERY technique from Tier 3:

**From Section 1 (Sprites):**
- Multi-color sprites (L33) → Better-looking enemies
- Sprite priority (L34) → Bullets in front of background
- Collision detection (L34) → Hit detection
- Sprite expansion (L35) → Boss enemies
- Failed multiplexing (L36) → Wave 4 flicker-fest
- Animation patterns (L37) → Walking enemies

**From Section 2 (Sound):**
- ADSR envelopes (L38) → Distinct shot/hit/death sounds
- Music sequences (L39) → Background music
- Sound+sprite sync (L40) → Hit sounds drift out of sync as enemies increase

**From Section 3 (Raster):**
- Raster awareness (L41) → Vblank sync for updates
- Failed color bars (L42) → Status bar at top flickers under load
- Safe update windows (L43) → Graphics update batching

**From Section 4 (Optimization):**
- Lookup tables (L44) → Pre-computed movement paths
- Loop unrolling (L45) → Optimized sprite updates
- Profiling (L46) → Visible slowdown as frame time increases
- (No hybrid code in this version)

**The Progression:**
```
Wave 1-2: "This is fun! Smooth gameplay."
Wave 3: "Okay, no bullets left, just dodging now."
Wave 4: "Whoa, sprites are flickering... is this supposed to happen?"
Wave 5: "This is a slideshow. I'm fighting the engine, not the enemies."

Game Over screen: "You hit the wall at wave 4. BASIC can't go further. Time for assembly."
```

**Technical Specifications:**

**Assets:**
- Player sprite (multi-color, 4 frames of animation)
- Enemy sprite (multi-color, 2 frames)
- Bullet sprite (single-color, small)
- Background (character graphics, simple arena)

**Game Loop Structure:**
```basic
1000 REM Main game loop
1010 GOSUB 2000: REM Input handling (CIA port reads)
1020 GOSUB 3000: REM Update player position/animation
1030 GOSUB 4000: REM Update bullets (8 max)
1040 GOSUB 5000: REM Update enemies (array-based)
1050 GOSUB 6000: REM Collision detection
1060 GOSUB 7000: REM Spawn logic
1070 GOSUB 8000: REM Wait for vblank (L43 technique)
1080 GOSUB 9000: REM Graphics update (unrolled sprite POKEs)
1090 IF WAVE>3 THEN GOSUB 10000: REM Attempt multiplexing
1100 GOSUB 11000: REM Sound updates (drifting sync)
1110 GOTO 1000
```

**Performance Target:**
- Waves 1-2: ~25fps (acceptable)
- Wave 3: ~18fps (playable but sluggish)
- Wave 4: ~10fps + flicker (frustrating)
- Wave 5: ~5fps (unplayable)

**Educational Deliverables:**

1. **Complete working game** (students type it in or load from disk)
2. **Commented source explaining which lesson each technique comes from**
3. **Performance profiling comments** showing frame time per wave
4. **Post-game analysis screen:**
```
   PERFORMANCE REPORT
   ──────────────────────────────────────
   Wave 1: 25fps ✓ SMOOTH
   Wave 2: 18fps ✓ PLAYABLE
   Wave 3: 12fps ⚠ SLUGGISH
   Wave 4: 8fps  ✗ FLICKERING
   Wave 5: 4fps  ✗ UNPLAYABLE

   BASIC LIMIT REACHED AT WAVE 4

   Assembly can handle 64+ sprites at 50fps.
   Ready to learn why?

   → Continue to Tier 4
```

**Code Example Structure:**
```basic
1000 REM ═══════════════════════════════════════════════
1010 REM AGAINST THE WALL - Main Loop
1020 REM Demonstrates BASIC limits from Tier 3
1030 REM ═══════════════════════════════════════════════
...
3000 REM Player update (L26-27: Joystick + Diagonal)
3010 J=PEEK(56320): REM Read joystick
...
6000 REM Collision detection (L34: Sprite collisions)
6010 C=PEEK(53279): REM Read collision register
...
9000 REM Graphics update (L45: Loop unrolling)
9010 POKE 53248,PX:POKE 53249,PY: REM Player sprite
...
10000 REM Multiplexing attempt (L36: Honest failure)
10010 REM Reposition sprites 0-3 for second pass
10020 FOR I=0 TO 3:POKE 53248+I*2,E(I+8):NEXT
10030 REM ↑ This causes visible flicker!
```

**Lesson Plan Flow:**

**Phase 1: Introduction (First session)**
- Explain game concept and controls
- Play through Waves 1-2 (smooth experience)
- "This is what well-optimized BASIC can do"

**Phase 2: Hitting the Wall (Second session)**
- Continue to Wave 3 (sprite limit hit)
- Wave 4 (multiplexing flicker)
- Wave 5 (slideshow)
- "Let's analyze why this happened"

**Phase 3: Code Walkthrough (Third session)**
- Walk through complete source
- Identify each Tier 3 technique by lesson number
- Show profiling data proving BASIC is the bottleneck

**Phase 4: The Transition (Fourth session)**
- "What would this look like in assembly?"
- Show demo of same game in assembly (from Tier 4 preview)
- 60fps, 24 sprites, stable music, no flicker
- "That's where we're going next. Tier 4: SYSTEMS."

**Progression Notes:**
- Capstone for all of Tier 3
- Creates visceral, undeniable need for assembly
- Not "BASIC is bad" but "BASIC has limits, and you just hit them"
- Students should feel accomplished (they built a real game!) AND frustrated (it's not as good as it could be)
- Perfect emotional state for Tier 4 transition

**Assessment Questions:**
1. Which wave did flickering start? Why?
2. Why does the music drift out of sync?
3. What's the frame time budget for 50fps? How far over are we at Wave 5?
4. If we removed the background music, how many more enemies could we handle?
5. What percentage of frame time is spent in sprite updates vs collision checks?

---

## Tier 3 Completion Checklist

**By the end of Tier 3, students should:**

**Understand:**
- ✅ Multi-color sprites and color tradeoffs
- ✅ Sprite hardware limits (8 sprites, collision detection, priorities)
- ✅ Sound envelopes and multi-voice music
- ✅ How raster scanning works and why timing matters
- ✅ Optimization techniques (lookup tables, unrolling)
- ✅ Profiling and identifying bottlenecks

**Have Experienced:**
- ✅ Visible flickering from failed multiplexing (L36)
- ✅ Unstable raster bars from timing issues (L42)
- ✅ Sound desync under high load (L40)
- ✅ Quantified performance limits via profiling (L46)
- ✅ A complete game hitting all limits (L48)

**Be Ready For:**
- ✅ Understanding *why* assembly exists (not just how)
- ✅ Motivated to learn low-level timing control
- ✅ Appreciating the design decisions of commercial games
- ✅ Tier 4: Systems (BASIC + Assembly integration)

---

## Pedagogical Notes

**Tier 3 is about FRUSTRATION → MOTIVATION**

Unlike Tier 1 (wonder) and Tier 2 (building), Tier 3 deliberately creates frustration. But it's educational frustration:

1. **You did everything right**: Not a skill issue, not a knowledge gap
2. **The tool has limits**: BASIC interpreter overhead is the problem
3. **There's a better tool**: Assembly solves these specific problems
4. **You're ready to learn it**: You understand what you need from it

**Common Student Questions (Anticipated):**

Q: "Why did you teach us BASIC if it can't do these things?"
A: "Because now you know WHAT you need from assembly (timing, speed, control). Students who start with assembly don't know what problems they're solving. You do."

Q: "Should I just give up on BASIC?"
A: "No. BASIC is still great for tools, editors, prototypes, and logic-heavy games. But action games need assembly for the real-time parts."

Q: "Can I use BASIC for my game idea?"
A: "Depends. Does it need 60fps, >8 sprites, or precise timing? Then no. Is it turn-based, menu-driven, or text-heavy? Then yes."

Q: "Is this tier just discouraging?"
A: "It should be empowering. You're not failing—you're hitting tool limits. Recognizing that is a professional skill. Now you're ready for the right tool."

---

## Transition to Tier 4

**Tier 3 ending message:**

*"You've pushed BASIC to its absolute limit. You've optimized everything that can be optimized. You've tried techniques that professionals use. And you've hit the wall.*

*The wall isn't your fault. It's the interpreter overhead. Every line of BASIC you write gets parsed, tokenized, and executed by a program running on the same C64. That overhead is unavoidable.*

*Assembly doesn't have that overhead. Your code runs directly on the CPU. No parsing, no interpreter, no variable lookups. Just instructions.*

*But assembly isn't magic. It's just a different tool—one that solves the problems you just encountered. You already know WHAT you need:*
- *Precise timing (raster interrupts)*
- *Sprite multiplexing without flicker*
- *60fps frame-locked game loops*
- *Sound effects that don't drift*

*Tier 4 teaches you HOW to do those things. Not theory—practical techniques that make your games work the way you imagined them.*

*Ready? Let's build the game you wanted to make."*

---

**End of Tier 3 Detailed Breakdown**

This document will be used to guide lesson creation for Tier 3. Each lesson should expand these outlines into full lesson content following the structure from Tier 1 lessons 7-8.
