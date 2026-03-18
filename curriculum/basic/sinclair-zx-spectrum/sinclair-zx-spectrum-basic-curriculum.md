# Sinclair ZX Spectrum BASIC Curriculum (v6.0 DRAFT)

**Platform:** Sinclair ZX Spectrum 48K
**Language:** Sinclair BASIC
**Games:** 16
**Total Units:** 336

---

## Overview

This curriculum teaches game design through 16 complete games. The Sinclair BASIC language and the ZX Spectrum hardware are the tools — but the real subject is the craft of making games. Every concept taught here transfers to any platform, any language, any era.

Each game teaches two things in parallel:

- **A game design concept** — a universal principle that applies whether you're building on a Spectrum, a C64, a modern console, or a game engine. Feedback, tension, pattern, physics, AI — the ideas that make games work as games.
- **A programming implementation** — the specific Sinclair BASIC commands and Spectrum hardware techniques that bring the design concept to life on this machine.

A learner who completes this curriculum can make games. Not just Spectrum games — games. The BASIC and the hardware are the first workshop. The craft is portable.

**See also:** `sinclair-zx-spectrum-basic-visual-progression.md` — the visual design philosophy that drives how each game looks and feels.

---

## Design and Programming Progression

Each game introduces one primary game design concept alongside its programming implementation:

| Game | Design concept | What the learner understands |
|------|---------------|------------------------------|
| 1 Lucky Number | **Feedback** — the game communicates without words | Colour, sound, and display responding to player actions |
| 2 Wire Panic | **Tension** — time pressure creates engagement | Countdowns, escalation, the feeling of urgency |
| 3 Bright Spark | **Pattern** — recognise, reproduce, extend | Sequences, difficulty through length and speed |
| 4 Hot and Cold | **The game loop** — input → update → draw, forever | Continuous real-time response |
| 5 Letter Soup | **Content vs logic** — change the data, not the code | Separating what varies from what's fixed |
| 6 Quiz Master | **Structure** — reusable pieces, organised code | Building larger programs from smaller parts |
| 7 Tail Chase | **Timing** — the game runs whether you act or not | Frame-rate independence, consistent speed |
| 8 Minefield | **Information design** — the screen holds meaning | Colour as data, deduction from visual clues |
| 9 Brick Bash | **Physics** — objects obey rules that feel right | Collision, angles, momentum |
| 10 Night Patrol | **Opponent behaviour** — simple rules, emergent challenge | AI that chases, flees, patrols |
| 11 Tarmac | **Visual identity** — a world built from designed pieces | Tile sets, consistent aesthetic, authored feel |
| 12 Ink Spill | **Mechanics as meaning** — the rules ARE the experience | When the game system is the game |
| 13 Rooftops | **Character** — a sprite that feels alive | Animation, weight, personality through movement |
| 14 Blockstorm | **Performance** — when design exceeds hardware, optimise | The bridge to lower-level thinking |
| 15 Dungeons of Dorin | **Procedural generation** — the computer as co-creator | Systems that produce surprise |
| 16 Thornwood Manor | **Living worlds** — agents, atmosphere, narrative | Autonomous characters, emergent story |

These design concepts are universal. A learner doing the C64 assembly track or a future Amiga AMOS track would encounter the same concepts, implemented with different tools. Repetition across tracks is reinforcement, not redundancy.

---

## Graphics from Day One

PLOT and DRAW are available from Game 1. They appear in the starter program's visual subroutines — the digit renderer, title screen effects, and temperature bar use pixel-level drawing, not character-cell tricks. The learner types PLOT and DRAW commands in Unit 1 before understanding them, just as they type FOR/NEXT and GO SUB.

PLOT and DRAW are formally taught in Game 2 (Wire Panic), where the learner uses them to draw the countdown display and the burning fuse. By Game 9 (Brick Bash), PLOT/DRAW are old friends — the new concepts there are POINT (reading pixels back), CIRCLE, and trigonometry for angle-based physics.

This means the learner's first program uses real pixel graphics, not "block-pixel" character-cell workarounds. The Spectrum can draw. We teach that from the start.

---

## Structure

| Phase | Games | Units each | Total | Purpose |
|-------|-------|------------|-------|---------|
| Foundations | 1-6 | 8 | 48 | Learn the language and core design patterns |
| Skills | 7-10 | 16 | 64 | Build real-time games with hardware access |
| Projects | 11-14 | 32 | 128 | Ambitious, visually distinctive software |
| Advanced | 15 | 32 | 32 | Complex systems |
| Capstone | 16 | 64 | 64 | A living world |
| **Total** | **16** | | **336** | |

Each unit is 60-90 minutes and produces a working, runnable result.

---

## Foundations (Games 1-6, 8 units each)

These six games teach the Sinclair BASIC language and the foundational concepts of game design. Each game is small enough to understand in 8 units. A learner can finish all six in a week.

Every Foundations game looks and sounds like a real game from unit 1. Game 1 uses a starter program with visual subroutines (PLOT/DRAW graphics, colour, sound) that the learner types in before they understand them — a deliberate echo of the magazine type-in culture. These subroutines become understandable as each subsequent game formally introduces the concepts behind them.

---

### Game 1: Lucky Number

**Units:** 8
**Design concept:** Feedback — the game communicates without words
**Genre:** Number guessing game
**Final size:** ~100 lines (starter program); ~20 lines of game logic understood by end

The computer picks a number between 1 and 100. The player guesses. The computer says higher or lower. Simple, ancient, and a perfect first program.

The learner's first experience isn't `10 PRINT "Hello"` on a blank screen — it's typing in a complete, visually impressive game. A title screen drawn with PLOT and DRAW. Digits rendered as pixel art. A temperature bar. Sound effects. Victory celebrations. The learner types in the full program in Unit 1 before they understand any of it — just as millions of children typed in magazine listings in the 1980s. Over the following units, they take the game logic apart and learn how it works.

**Game design — Feedback:**

The temperature bar is a *proximity indicator* — a design pattern used in everything from children's games to modern radar systems. The border colour shift is *ambient feedback* — information delivered through the environment rather than text. The victory celebration is *reward framing* — making the player feel their achievement. The directional BEEP (ascending for "guess higher", descending for "guess lower") is *audio feedback* — sound carrying meaning. None of this is explained as theory. The learner plays the game and feels it working.

**New BASIC concepts (understood by end of game):**
| Concept | What the learner discovers |
|---------|---------------------------|
| What a program is | Numbered lines, executed in order |
| The Spectrum keyboard | K-mode (keywords), L-mode (letters), how to enter a program |
| `PRINT` | Putting text on screen |
| Strings | Text in quotation marks |
| `RUN` | Executing the program |
| `LET` | Storing a value in a variable |
| Numeric variables | `g`, `n` — names that hold numbers |
| `INPUT` | Asking the player to type something |
| `IF`/`THEN` | Making a decision based on a condition |
| `=`, `<`, `>` | Comparing two values |
| `GO TO` | Jumping to a different line |
| `REM` | Comments — notes for the programmer |
| `RND` | Random numbers (introduced late, after the game works with a fixed number) |
| `RANDOMIZE` | Seeding the random number generator — different game each time |
| `INT` | Rounding to a whole number (`INT(RND*100)+1`) |
| `LIST` / `NEW` / `RUN` | Editor commands — managing and running programs |
| `STOP` / `CONTINUE` | Debugging tools — pause mid-program and resume |

**Present in the starter program but NOT formally taught yet:** PLOT/DRAW (Game 2), FOR/NEXT (Game 3), INK/PAPER/BORDER/BRIGHT/BEEP (Games 2-3), PRINT AT (Game 2), DATA/READ/RESTORE (Game 5), GO SUB/RETURN (Game 6). These are black boxes — magic that works. Each is formally introduced in the game listed.

**Milestone:** The learner has typed in, run, and partially understood a complete interactive program. They've experienced feedback as a design concept — even if they can't name it yet.

---

### Game 2: Wire Panic

**Units:** 8
**Design concept:** Tension — time pressure creates engagement
**Genre:** Bomb defusal
**Final size:** ~25 lines

Digits count down on screen, drawn with PLOT — reusing Game 1's renderer in a new context. A burning fuse drawn with DRAW creeps across the display. Four coloured wires wait to be cut. The border shifts from safe green through warning yellow to danger red as time runs out. Cut the right wire and you're a hero. Cut the wrong one and the screen strobes with an explosion.

**Game design — Tension:**

The countdown creates *time pressure* — the most fundamental source of tension in games. The fuse is a *visual countdown* — the same information as the digits, delivered spatially rather than numerically. The border colour shift is *environmental escalation* — the world itself tells you things are getting worse. The tick sound is *rhythmic tension* — a heartbeat that speeds up or stays constant while everything else changes. The explosion is *consequence* — tension means nothing without stakes.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLS` | Clearing the screen |
| `PRINT AT` | Placing text at a specific row and column |
| `PLOT` | Drawing a single pixel at x,y coordinates |
| `DRAW` | Drawing a line from the current position |
| `INKEY$` | Checking the keyboard without waiting |
| The empty string `""` | What `INKEY$` returns when no key is pressed |
| `PAUSE` | Waiting for a set time |
| `BEEP` | Making sound (duration and pitch) |
| String variables | `a$` — names that hold text |
| The difference between `INPUT` and `INKEY$` | Blocking vs non-blocking input |

**Why this game:** `INKEY$` is the foundation of every action game. Understanding the difference between "wait for the player" (`INPUT`) and "check right now" (`INKEY$`) is fundamental. The bomb makes this visceral — you feel the pressure of real-time input. PLOT and DRAW move from black boxes to understood tools — the digit renderer and fuse become the teaching examples.

**Milestone:** The learner understands two models of input, can draw pixels on screen, and can create tension through time pressure.

---

### Game 3: Bright Spark

**Units:** 8
**Design concept:** Pattern — recognise, reproduce, extend
**Genre:** Memory game (Simon Says)
**Final size:** ~25 lines

Four chunky colour panels dominate the screen. Simon plays a sequence — each panel flashes with BRIGHT, accompanied by a distinct BEEP tone. The learner watches, then repeats. Sequences grow longer, stored in strings. The learner experiments with all 15 colours (8 base + BRIGHT) and discovers colour as a system, not a decoration.

**Game design — Pattern:**

Pattern recognition and reproduction is one of the oldest game mechanics. *Sequence length* is the difficulty curve — each round adds one element. *Distinct signals* (colour + sound for each panel) make patterns memorable through multiple senses. *Immediate feedback* on each step (right/wrong) tells the player whether their mental model matches reality. The game teaches the player to build and maintain a *mental model* — the most transferable skill in all of game design.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `FOR`/`NEXT` | Counted loops — do something N times |
| `BORDER` | The screen border colour |
| `PAPER` | The background colour |
| `INK` | The text/foreground colour |
| The 8 colours (0-7) | Black, blue, red, magenta, green, cyan, yellow, white |
| `BRIGHT` | Brighter versions of the colours |
| `STEP` | `FOR n=7 TO 0 STEP -1` — counting backwards, counting by twos |
| Nested loops | A `FOR` inside a `FOR` |
| The screen as a grid | 24 rows, 32 columns, each cell has INK and PAPER |

**Milestone:** The learner understands loops, the Spectrum's colour model, and how pattern length creates difficulty.

---

### Game 4: Hot and Cold

**Units:** 8
**Design concept:** The game loop — input → update → draw, forever
**Genre:** Grid search game
**Final size:** ~30 lines

A treasure is hidden at a random position on screen. The player moves a cursor around with keys. The border colour changes to indicate distance: blue (cold) through red (warm) to white (hot). Find the treasure.

**Game design — The game loop:**

Every real-time game runs the same cycle: read input, update state, draw the result. This is the *game loop* — the universal heartbeat of interactive software. Hot and Cold makes it explicit: each frame, the program checks the keyboard, moves the cursor, calculates the distance, and updates the border. The loop runs whether the player acts or not. This is the structural difference between a quiz (turn-based, event-driven) and a game (continuous, loop-driven).

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Using variables for position | `r` for row, `c` for column |
| The coordinate grid | Row 0-23, column 0-31 |
| Updating position | `LET r = r - 1` (move up) |
| `<>`, `<=`, `>=` | More comparison operators |
| `ABS` | Distance without caring about direction |
| `SQR` | Square root — true distance: `SQR(dx^2 + dy^2)` |
| `^` (power) | Exponentiation — `dx^2` is cleaner than `dx*dx` |
| The game loop | Read input → update state → draw |

**Milestone:** The learner can build a game loop with continuous movement and understands the universal structure of real-time games.

---

### Game 5: Letter Soup

**Units:** 8
**Design concept:** Content vs logic — change the data, not the code
**Genre:** Word puzzle
**Final size:** ~30 lines

A scrambled word appears. Type the correct word to score a point. Ten rounds, then your score. Words get harder. Characters appear one at a time with ascending BEEP, building anticipation.

**Game design — Content vs logic:**

The most powerful insight in game development: *separate what varies from what's fixed*. The game logic (scramble, check, score) never changes. The content (the word list) is pure data. Edit the DATA lines and you have a different game — different words, different difficulty — without touching a line of code. This is the principle behind every level editor, mod tool, and content pipeline in modern game development.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| String variables | Using `w$`, `g$` for words |
| `LEN` | How many characters in a string |
| String slicing | `a$(2 TO 4)` — extracting part of a string |
| String concatenation | `a$ + b$` — joining strings |
| String comparison | `IF g$ = w$ THEN ...` |
| `DATA` | Storing a list of words in the program |
| `READ` | Pulling the next value from `DATA` |
| `STR$` | Number to string — `"Score: " + STR$ s` builds display text |
| `VAL` | String to number — converting typed input to a numeric value |
| Score tracking | A variable that counts correct answers |

**Milestone:** The learner can manipulate strings, store data in the program, and understands that separating content from logic makes games flexible.

---

### Game 6: Quiz Master

**Units:** 8
**Design concept:** Structure — reusable pieces, organised code
**Genre:** Quiz game with categories
**Final size:** ~35 lines

A multiple-choice quiz. Questions from `DATA` statements, shuffled options, score at the end. The learner creates their own questions.

**Game design — Structure:**

As programs grow, organisation becomes design. *Subroutines* (GO SUB) let you name a piece of code and call it from anywhere — the quiz's question-card drawing routine is written once and used for every question. *Arrays* give you indexed storage — four players' scores in one structure instead of four separate variables. This is the first game where the learner thinks about *how the code is organised*, not just what it does. Structure is the difference between a program that works and a program you can change.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `GO SUB` / `RETURN` | Reusable subroutines — code you can call from anywhere |
| `RESTORE` | Rewinding `DATA` to read it again |
| `AND` / `OR` / `NOT` | Combining and negating conditions — `IF NOT found THEN` |
| Simple arrays | `DIM s(4)` — a row of numbered boxes |
| Array access | `LET s(p) = s(p) + 1` — updating a specific element |
| Line numbering conventions | Organising code into sections (100s, 200s, etc.) |
| Multiple colons | Several commands on one line |
| `TAB` | Horizontal formatting — `PRINT TAB 10; "Score"` |

**Milestone:** The learner has the full BASIC toolkit for simple programs and understands that code organisation is a design decision.

---

## Skills (Games 7-10, 16 units each)

These four games build real gameplay skills. The learner already knows the language; now they learn to use it for games that move, think, and fight back.

---

### Game 7: Tail Chase

**Units:** 16
**Design concept:** Timing — the game runs whether you act or not
**Genre:** Snake game
**Final size:** ~60 lines
**Inspired by:** Classic Snake, magazine type-in listings

A snake moves continuously across the screen. The learner steers — left, right, up, down — but the snake never stops. Each pickup makes the body grow, trailing behind in an array. Hit a wall or your own tail and it's game over.

**Game design — Timing:**

The game loop from Hot and Cold ran continuously, but at BASIC's natural speed — inconsistent and dependent on what's happening on screen. Tail Chase introduces *frame-rate timing*: the game waits for the Spectrum's hardware frame counter (PEEK 23672) before each update, ensuring consistent speed. This is the universal principle of *delta time* — making game behaviour independent of execution speed. Every modern game engine solves this same problem.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `PEEK` 23672 (frames counter) | Consistent game speed regardless of what's on screen |
| Continuous movement | The snake moves whether the player presses a key or not |
| Collision detection | Same cell = hit (walls, self, pickups) |
| Game states | Playing, game over, level complete |
| Level progression | Harder each time (more hazards, faster speed) |
| Attribute-file POKE (22528+) | Screen transitions — fade to black row by row |
| `SGN` | Direction of movement — `LET dx = SGN(target - current)` |
| `FLASH` for items | Pickups glitter, hazards pulse |

---

### Game 8: Minefield

**Units:** 16
**Design concept:** Information design — the screen holds meaning
**Genre:** Grid logic game (Minesweeper-style)
**Final size:** ~80 lines
**Inspired by:** Minesweeper, logic puzzles

Navigate a grid. Hidden mines surround you. Each revealed cell shows how many adjacent mines exist. Use logic to find a safe path to the exit.

**Game design — Information design:**

Every pixel on screen is a communication from the game to the player. In Minefield, *colour is data* — the ATTR function reads the colour of any cell, turning the display into a queryable database. The distinction between *game state* (the array) and *display* (what's on screen) is fundamental: the player sees the display, the code reads the state. Cascading reveal animations aren't decoration — they're *information delivery*, showing the player what's safe in a way that builds understanding cell by cell.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| 2D arrays | `DIM m(10,10)` — a grid of data |
| Array initialisation | Filling arrays with starting values |
| Flags | 0/1 values meaning hidden/revealed/flagged |
| Reading neighbours | Checking all 8 adjacent cells |
| `ATTR` | Reading the colour of a character cell — the screen is data |
| Separating data from display | The grid array vs what's on screen |

---

### Game 9: Brick Bash

**Units:** 16
**Design concept:** Physics — objects obey rules that feel right
**Genre:** Breakout-style action game
**Final size:** ~80 lines
**Inspired by:** Breakout, Arkanoid, magazine type-in bat-and-ball games

Bricks built from CHR$ block characters fill the top of the screen. A ball bounces around the play area, drawn with CIRCLE, checked with POINT for pixel-level collision. The bat moves smoothly along the bottom. Where the ball hits the bat determines the reflection angle.

**Game design — Physics:**

The ball obeys rules — angle of incidence, reflection, momentum. These rules create *emergent gameplay*: the player doesn't control the ball directly, they control the bat, and the physics determines what happens. Simple bouncing (reverse dx or dy) works but feels mechanical. *Angle-based deflection* from the bat position makes the game *controllable* — skilled players can aim. The maths (SIN/COS/ATN) earns its place by making the game feel better. Physics in games isn't about accuracy — it's about *feel*.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CHR$` 128-143 | Block graphic characters — bricks, borders, frame elements |
| `CHR$` / `CODE` | Character codes, converting between numbers and characters |
| `CIRCLE` | Drawing a circle |
| `POINT` | Reading whether a pixel is set |
| `SIN` / `COS` | Converting an angle to dx/dy velocity components |
| `ATN` | Calculating the deflection angle from bat impact position |
| `TAN` | The ratio of SIN to COS — completes the trigonometry family |
| `ASN` / `ACS` | Inverse functions — velocity components back to angle |
| `PI` | The constant needed for angle calculations |

---

### Game 10: Night Patrol

**Units:** 16
**Design concept:** Opponent behaviour — simple rules, emergent challenge
**Genre:** Top-down maze chase
**Final size:** ~100 lines
**Inspired by:** Magazine chase games, Pac-Man

Move through a maze collecting items while enemies chase you. Enemies use simple AI to pursue. Multiple levels with different maze layouts.

**Game design — Opponent behaviour:**

The enemies in Night Patrol follow simple rules: move toward the player, avoid walls. Two rules. But the emergent behaviour — cornering, flanking, blocking escape routes — feels *intelligent*. This is the core insight of game AI: *complex-looking behaviour from simple rules*. The enemies don't plan or think. They react. The player's brain fills in the rest, attributing intention where there is only algorithm. Understanding this changes how you think about every game with opponents.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Map data | String arrays as maze layouts |
| Simple AI | Enemies move toward the player |
| Multiple enemies | Arrays for enemy positions |
| `RESTORE` to specific line | Loading a particular level's data |
| `OVER 1` | XOR mode — move without destroying the background |
| `SCREEN$` | Reading the character at a screen position |
| String arrays | `DIM m$(20)` — a list of strings for level data |

---

## Projects (Games 11-14, 32 units each)

These are real software projects. Each takes sustained effort over 32 units and produces something the learner can be genuinely proud of.

---

### Game 11: Tarmac

**Units:** 32
**Design concept:** Visual identity — a world built from designed pieces
**Genre:** Top-down racing game
**Final size:** ~300 lines
**Inspired by:** Super Sprint, magazine type-in racers

A top-down racer where the track scrolls toward the player. Track tiles, kerbs, grass, barriers, and the player's car are all hand-designed 8×8 pixel graphics that replace the standard character set.

**Game design — Visual identity:**

A custom character set transforms the Spectrum from a text machine into a visual world. Every tile is *designed*, not default. The game has its own *visual language* — road looks different from grass, kerbs look different from barriers, and the player reads the world instinctively. This is *environmental storytelling through graphics*: the visuals communicate the rules without text. Every commercial game creates its own visual identity. This is where the learner creates theirs.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Custom character set | POKE 23606/23607 (CHARS) replaces the entire font |
| Character design | Hand-designed 8×8 pixel graphics |
| Tile-based level design | The track is built from repeating character tiles |
| Vertical scrolling | The track moves toward the player |

---

### Game 12: Ink Spill

**Units:** 32
**Design concept:** Mechanics as meaning — the rules ARE the experience
**Genre:** Colour flood puzzle
**Final size:** ~300 lines
**Inspired by:** Flood-It, colour flood puzzles

A grid of coloured cells. Each turn, the player chooses a colour, and connected cells flood to the new choice — rippling outward with cascading attribute POKEs.

**Game design — Mechanics as meaning:**

In most games, the mechanics serve the theme: you *fight* monsters, you *drive* cars. In Ink Spill, the mechanic IS the theme. Colour isn't decoration — it's the entire game. The player's strategy is about which colour to choose, and every decision is instantly visible. This is *mechanics as meaning* — when the system itself is the experience, not a simulation of something else. Tetris, Go, and Chess work the same way.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Direct attribute POKE (22528+) | Fast colour changes without reprinting |
| Flood fill algorithm | Connected cells change colour, rippling outward |
| `FLASH` / `INVERSE` | Visual feedback — highlights, selection |

---

### Game 13: Rooftops

**Units:** 32
**Design concept:** Character — a sprite that feels alive
**Genre:** Platformer
**Final size:** ~300 lines
**Inspired by:** Manic Miner, Jet Set Willy, magazine type-in platformers

A running character leaps between rooftops. The character has animation frames — legs moving as they run. Jump physics give weight and momentum.

**Game design — Character:**

A character with two animation frames feels more alive than a static sprite with a hundred colours. *Animation communicates state*: legs cycling means running, a different pose means jumping, no animation means standing still. *Weight and momentum* from jump physics make the character feel physical — they have mass, they obey gravity, they arc through the air. Character is the player's avatar in the game world. Making them feel *right* is the difference between a tech demo and a game people want to play.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `USR` | Defining user-defined graphic characters |
| `BIN` | Binary notation for pixel rows |
| UDG design | Graph paper → binary → POKE |
| Animation | Cycling between UDG frame definitions |
| Jump physics | Gravity, momentum, arc |
| Platform collision | ATTR/SCREEN$ to check what's beneath the player |

---

### Game 14: Blockstorm

**Units:** 32
**Design concept:** Performance — when design exceeds hardware, optimise
**Genre:** UDG action shooter
**Final size:** ~400 lines
**Inspired by:** Magazine type-in shooters, arcade conversions

A vertically scrolling shooter with custom UDG sprites. Multiple enemies, bullet management, increasing difficulty. Pushes Sinclair BASIC to its speed limits — then breaks through with machine code helpers.

**Game design — Performance:**

Every game hits a moment where the design wants more than the hardware can give. The shooter demands smooth scrolling, multiple enemies, fast collision detection — and BASIC can't keep up. The learner optimises: short variable names, strategic GO SUB placement, integer tricks. When optimisation isn't enough, they write their first machine code routines — small Z80 programs stored in DATA, POKEd into RAM, called via RANDOMIZE USR. *This is the bridge to assembly.* The learner understands WHY assembly exists: not because it's "proper programming", but because their game needs it.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLEAR` | `CLEAR 59999` — set RAMTOP to protect machine code |
| Machine code helpers | Small Z80 routines in DATA, called via `RANDOMIZE USR` |
| `IN` 31 (Kempston joystick) | Arcade-feel input |
| `INPUT LINE` | Read a full line without quotes |
| Speed optimisation | Short variable names, GO SUB placement, integer tricks |

---

## Advanced (Game 15, 32 units)

### Game 15: Dungeons of Dorin

**Units:** 32
**Design concept:** Procedural generation — the computer as co-creator
**Genre:** Dungeon crawl RPG
**Final size:** ~450 lines
**Inspired by:** Rogue, early CRPGs, Fighting Fantasy

A dungeon crawler with character stats, combat, equipment, and procedural level generation. Simple procedural generation creates a different dungeon each time.

**Game design — Procedural generation:**

The wonder moment: something appears on screen that *the learner didn't design*. The code generated it. Procedural generation means infinite content from finite rules. Every playthrough is different — not because of random chance, but because of *systems that create*. This is the principle behind roguelikes, Minecraft, and every game that promises "no two plays the same." The learner discovers that code can be *creative* — it can surprise even its author.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `DEF FN` / `FN` | User-defined functions — damage formulas, distance calculations |
| `LN` / `EXP` | Logarithmic and exponential functions — rarity curves |
| `SAVE` / `LOAD` / `VERIFY` | Saving game state to tape |
| `OUT` 254 (border port) | Screen shake via rapid border changes |
| `VAL$` | Evaluating a string as an expression |

---

## Capstone (Game 16, 64 units)

### Game 16: Thornwood Manor

**Units:** 64
**Design concept:** Living worlds — agents, atmosphere, narrative
**Genre:** Top-down adventure with autonomous NPCs
**Final size:** ~500 lines
**Inspired by:** The Legend of Zelda, The Hobbit (Melbourne House, 1982)

The learner's magnum opus. Connected screens form a manor and its grounds. NPCs move autonomously between rooms on their own schedules. Items, doors, and combat use everything from fifteen games.

**Game design — Living worlds:**

The manor doesn't wait for the player. NPCs move between rooms, interact with each other, react to changes in the world. The player is a participant in a system, not the centre of a script. *Autonomous agents* — characters with goals and simple decision rules — create emergent narrative: stories that the designer didn't write, emerging from the interaction of systems. The colour palette tells the story: frozen rooms are blue and cyan, warming to yellow and white as the curse lifts. *Atmosphere through systems*, not cutscenes.

**New BASIC concepts:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Connected screens | Rooms scroll into view as the player crosses boundaries |
| Autonomous NPCs | Characters that move and act on their own schedules |
| Attribute-based mood | Frozen rooms are blue/cyan; warming rooms shift to yellow/white |
| Items and inventory | GET/DROP/USE tracked in arrays |
| Multiple interacting systems | NPCs + inventory + combat + rooms + atmosphere |

---

## Concept Progression Summary

### BASIC concepts — by game, when first introduced:

| Concept group | First game | Reinforced in |
|---------------|-----------|---------------|
| **Language fundamentals** | | |
| PRINT, LET, variables, INPUT, IF/THEN, GO TO, REM | 1 | Every game |
| RND, INT, RANDOMIZE | 1 | 4, 7, 15 |
| LIST, NEW, RUN, STOP, CONTINUE | 1 | — (editor/debug) |
| CLS, PRINT AT, INKEY$, PAUSE, BEEP | 2 | 4, 7, 10, 14 |
| PLOT, DRAW (pixel graphics) | 2 | 3, 4, 9, 13 |
| FOR/NEXT/STEP, colour model (INK/PAPER/BORDER/BRIGHT) | 3 | 4, 7, 8, 9 |
| Position variables, game loop, ABS, SQR, ^ | 4 | 7, 8, 9, 15 |
| Strings, DATA/READ, LEN, slicing, STR$, VAL | 5 | 6, 10, 16 |
| GO SUB/RETURN, arrays, RESTORE, AND/OR/NOT, TAB | 6 | 7, 8, 10, 12 |
| **Hardware access** | | |
| PEEK 23672 (frames counter), attribute-file POKE, SGN | 7 | 10, 12, 14 |
| ATTR (reading screen as data), 2D arrays | 8 | 9, 13 |
| CHR$ 128-143 (block graphic characters), CHR$/CODE | 9 | 13 |
| CIRCLE, POINT (advanced pixel graphics) | 9 | 13 |
| SIN, COS, TAN, ATN, ASN, ACS, PI (trigonometry) | 9 | 15 |
| OVER 1 (XOR drawing), SCREEN$ | 10 | 14 |
| **Direct control** | | |
| Custom character sets (POKE CHARS 23606/23607) | 11 | 16 |
| Direct attribute POKE (22528+), FLASH/INVERSE | 12 | 15, 16 |
| UDGs (USR, BIN), animation | 13 | 14 |
| CLEAR, INPUT LINE, IN 31 (Kempston joystick) | 14 | — |
| **Machine code and beyond** | | |
| Machine code helpers (DATA/POKE/RANDOMIZE USR) | 14 | 15, 16 |
| OUT 254 (border port), speed optimisation | 14-15 | 16 |
| DEF FN/FN, LN, EXP, VAL$ | 15 | 16 |
| SAVE/LOAD/VERIFY, procedural generation | 15 | — |

### Game design concepts — by game:

| Concept | First game | Reinforced in |
|---------|-----------|---------------|
| Feedback (visual, audio, environmental) | 1 | Every game |
| Tension and time pressure | 2 | 7, 14 |
| Pattern recognition and difficulty curves | 3 | 8, 15 |
| The game loop (input → update → draw) | 4 | 7, 9, 10, 14 |
| Content vs logic (data-driven design) | 5 | 10, 15 |
| Code structure and reusability | 6 | 11, 14 |
| Frame-rate timing and consistency | 7 | 9, 10, 14 |
| Information design (screen as communication) | 8 | 12 |
| Physics and emergent gameplay | 9 | 13 |
| AI and opponent behaviour | 10 | 16 |
| Visual identity and authored feel | 11 | 13, 16 |
| Mechanics as meaning | 12 | — |
| Character and animation | 13 | 16 |
| Performance and optimisation | 14 | — |
| Procedural generation | 15 | 16 |
| Living worlds and autonomous agents | 16 | — |

---

## Excluded BASIC Keywords

The following Sinclair BASIC keywords are not taught (peripheral-specific, no stock 48K use): COPY, LPRINT, LLIST, MERGE, OPEN #, CLOSE #, FORMAT, CAT, ERASE, MOVE. Every other keyword has a game assignment.

---

## Changelog

- **v6.0 DRAFT (2026-03-18):** Dual-track curriculum: game design concepts as first-class organising principle alongside BASIC implementation. Each game now teaches a universal game design concept (feedback, tension, pattern, physics, AI, etc.) that transfers to any platform. PLOT/DRAW moved to Game 1 (black box) / Game 2 (formally taught), replacing character-cell block-pixel approach. CIRCLE/POINT/trig remain at Game 9. Game design progression table added. Overview rewritten: the curriculum teaches game design through the medium of Sinclair BASIC, not the other way around.
- **v5.3 DRAFT (2026-03-18):** Complete keyword coverage. Every teachable Sinclair BASIC keyword assigned to a game.
- **v5.2 DRAFT (2026-03-18):** Aligned game names with visual progression document.
- **v5.1 DRAFT (2026-03-16):** Visual progression alignment.
- **v5.0 DRAFT (2026-03-13):** Complete restructure. 16 games, graduated difficulty.
- **v4.0 (2026-03-09):** 4 games × 64 units.
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
