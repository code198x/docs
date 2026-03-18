# Sinclair ZX Spectrum BASIC Curriculum (v5.3 DRAFT)

**Platform:** Sinclair ZX Spectrum 48K
**Language:** Sinclair BASIC
**Games:** 16
**Total Units:** 336

---

## Overview

The Sinclair BASIC curriculum teaches programming from absolute zero through 16 complete games. A learner who has never written a line of code can start at Game 1 and finish at Game 16 having built a top-down adventure with connected screens, autonomous NPCs, and atmospheric lighting.

The games grow in ambition as the learner's skills grow. Early games are tiny (8 units, under 30 lines) and exist purely to teach language fundamentals. Later games are substantial (32-64 units, hundreds of lines) and feel like real software.

Every concept is introduced before it's needed. No game assumes knowledge that hasn't been taught by a previous game. The curriculum document below lists every new concept alongside the game that introduces it.

BASIC is not a prerequisite for the assembly track. The two tracks are independent — but a learner who completes the BASIC track arrives at assembly with real hardware knowledge. By Game 14, they're writing machine code in DATA statements. By Game 16, they've built a top-down adventure with autonomous NPCs. The assembly track isn't a scary new world — it's the thing they've been reaching for every time BASIC wasn't fast enough.

**See also:** `sinclair-zx-spectrum-basic-visual-progression.md` — the visual design philosophy that drives how each game looks and feels.

---

## Structure

| Phase | Games | Units each | Total | Purpose |
|-------|-------|------------|-------|---------|
| Foundations | 1-6 | 8 | 48 | Learn the language |
| Skills | 7-10 | 16 | 64 | Build real games |
| Projects | 11-14 | 32 | 128 | Ambitious, complete software |
| Advanced | 15 | 32 | 32 | Complex systems |
| Capstone | 16 | 64 | 64 | The Hobbit-scale adventure |
| **Total** | **16** | | **336** | |

Each unit is 60-90 minutes and produces a working, runnable result.

---

## Foundations (Games 1-6, 8 units each)

These six games teach the Sinclair BASIC language. Each game is small enough to understand in 8 units, and exists to introduce a handful of concepts through a complete, satisfying experience. A learner can finish all six in a week.

Every Foundations game looks and sounds like a real game from unit 1. Game 1 uses a starter program with visual subroutines (colour, sound, block-pixel graphics) that the learner types in before they understand them — a deliberate echo of the magazine type-in culture. These subroutines become understandable as each subsequent game formally introduces the concepts behind them.

---

### Game 1: Lucky Number

**Units:** 8
**Genre:** Number guessing game
**Final size:** ~100 lines (starter program); ~20 lines of game logic understood by end

The computer picks a number between 1 and 100. The player guesses. The computer says higher or lower. Simple, ancient, and a perfect first program.

The learner's first experience isn't `10 PRINT "Hello"` on a blank screen — it's typing in a complete, visually impressive game. A rainbow title screen. Big block-pixel letters. A temperature bar. Sound effects. Victory celebrations. The learner types in the full program in Unit 1 before they understand any of it — just as millions of children typed in magazine listings in the 1980s. Over the following units, they take the game logic apart and learn how it works. The visual subroutines remain black boxes, understood later as each technique is formally introduced in subsequent games.

**New concepts introduced (understood by end of game):**
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

**Present in the starter program but NOT formally taught yet:** FOR/NEXT (Game 3), INK/PAPER/BORDER/BRIGHT/BEEP (Games 2-3), PRINT AT (Game 2), DATA/READ/RESTORE (Game 5), GO SUB/RETURN (Game 6). These are black boxes — magic that works. Each is formally introduced in the game listed.

**Why this game:** Every concept has an immediate, visible purpose. `INPUT` is how the player guesses. `IF/THEN` is how the computer responds. `GO TO` is what keeps the game running. Nothing is abstract. And the learner's very first Spectrum program looks like something worth showing to a friend.

**Milestone:** The learner has typed in, run, and partially understood a complete interactive program.

---

### Game 2: Wire Panic

**Units:** 8
**Genre:** Bomb defusal
**Final size:** ~25 lines

Big block-pixel digits count down on screen — reusing Game 1's digit renderer in a new context. A burning fuse creeps across the display with a red spark. Four coloured wires wait to be cut. The border shifts from safe green through warning yellow to danger red as time runs out. Cut the right wire and you're a hero. Cut the wrong one and the screen strobes with an explosion.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLS` | Clearing the screen |
| `PRINT AT` | Placing text at a specific row and column |
| `INKEY$` | Checking the keyboard without waiting |
| The empty string `""` | What `INKEY$` returns when no key is pressed |
| Loops with `GO TO` | Spinning until something happens |
| `PAUSE` | Waiting for a set time |
| `BEEP` | Making sound (duration and pitch) |
| String variables | `a$` — names that hold text |
| The difference between `INPUT` and `INKEY$` | Blocking vs non-blocking input |

**Why this game:** `INKEY$` is the foundation of every action game on the Spectrum. Understanding the difference between "wait for the player" (`INPUT`) and "check right now" (`INKEY$`) is fundamental. The bomb makes this visceral — you feel the pressure of real-time input. And the digit renderer from Game 1 reappears in a new context, showing how subroutines travel between programs.

**Milestone:** The learner understands two models of input, can position text on screen, and can make sounds.

---

### Game 3: Bright Spark

**Units:** 8
**Genre:** Memory game (Simon Says)
**Final size:** ~25 lines

Four chunky colour panels (7×8 blocks each) dominate the screen. Simon plays a sequence — each panel flashes with BRIGHT, accompanied by a distinct BEEP tone. The learner watches, then repeats. Sequences grow longer, stored in strings. The learner experiments with all 15 colours (8 base + BRIGHT) and discovers colour as a system, not a decoration.

**New concepts introduced:**
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

**Why this game:** The entire screen becomes a canvas. Colour carries meaning — each panel is identified by its colour alone. The learner sees the direct relationship between code and what appears on screen. Loops stop being abstract (repeat N times) and become concrete (fill a panel with red squares). GO SUB appears from the starter program to draw and redraw panels cleanly — a preview of formal subroutines in Game 6.

**Milestone:** The learner understands loops and the Spectrum's colour model.

---

### Game 4: Hot and Cold

**Units:** 8
**Genre:** Grid search game
**Final size:** ~30 lines

A treasure is hidden at a random position on screen. The player moves a cursor around with keys. The border colour changes to indicate distance: blue (cold) through red (warm) to white (hot). Find the treasure.

**New concepts introduced:**
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

**Why this game:** This is the first game with a proper game loop. The screen updates continuously, not in response to a single keypress. Every frame: erase the old position, draw the new one, check the distance, update the border. The learner already knows `PRINT AT` from Game 2 — now they use it for something that moves.

**Milestone:** The learner can build a game loop with continuous movement.

---

### Game 5: Letter Soup

**Units:** 8
**Genre:** Word puzzle
**Final size:** ~30 lines

A scrambled word appears. Type the correct word to score a point. Ten rounds, then your score. Words get harder. Characters appear one at a time with ascending BEEP, building anticipation.

**New concepts introduced:**
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
| Animated letter reveal | Characters appear one at a time with ascending BEEP |

**Why this game:** Strings are essential for data-driven games later. This game makes string manipulation tangible — you can see the letters being scrambled and unscrambled. `DATA`/`READ` provides a natural way to store the word list. The animated letter reveal — characters appearing one at a time with ascending BEEP — builds anticipation and shows how loops and timing create drama. The learner discovers they can change the game's content by editing DATA lines without touching the code.

**Milestone:** The learner can manipulate strings and store data in the program.

---

### Game 6: Quiz Master

**Units:** 8
**Genre:** Quiz game with categories
**Final size:** ~35 lines

A multiple-choice quiz. Questions from `DATA` statements, shuffled options, score at the end. The learner creates their own questions.

**New concepts introduced:**
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
| Structured screen layout | GO SUB draws formatted question cards with coloured borders |

**Why this game:** GO SUB is the first step toward structured code — the quiz naturally needs reusable drawing routines for question cards and score panels. Arrays are the gateway to real data structures. A quiz game makes them natural — you need somewhere to store four players' scores. `RESTORE` completes the `DATA`/`READ` toolkit. And the learner starts thinking about code organisation for the first time.

**Milestone:** The learner has the full BASIC toolkit for simple programs: variables, strings, arrays, loops, decisions, input, colour, sound, data, and reusable subroutines.

---

## Skills (Games 7-10, 16 units each)

These four games build real gameplay skills. The learner already knows the language; now they learn to use it. Each game is a recognisable type — the kind of thing that appeared in magazine type-in listings.

---

### Game 7: Tail Chase

**Units:** 16
**Genre:** Snake game
**Final size:** ~60 lines
**Inspired by:** Classic Snake, magazine type-in listings

A snake moves continuously across the screen. The learner steers — left, right, up, down — but the snake never stops. Each pickup makes the body grow, trailing behind in an array. Hit a wall or your own tail and it's game over. Each level adds more hazards and faster movement.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| The game loop (formal) | Input → update → draw, running continuously |
| `INKEY$` in a game loop | Polling every frame, not blocking |
| Moving a character | Erase old position, draw new position |
| Continuous movement | The snake moves whether the player presses a key or not |
| Collision detection | Same cell = hit (walls, self, pickups) |
| Game states | Playing, game over, level complete |
| Lives | Lose a life, reset position, continue |
| Level progression | Harder each time (more hazards, faster speed) |
| `PEEK` 23672 (frames counter) | Consistent game speed regardless of what's on screen |
| Attribute-file POKE (22528+) | Screen transitions — fade to black row by row before redrawing |
| `SGN` | Direction of movement — `LET dx = SGN(target - current)` gives -1, 0, or 1 |
| `FLASH` for items | Pickups glitter, hazards pulse with alternating INK |

**Why this game:** This is the learner's first real-time game, and the first time they touch the hardware directly. PEEK 23672 gives consistent frame-rate timing — movement is smooth because it's *timed*, not just fast. The body trailing in an array is a natural, visual use of data structures. Attribute-file POKEs create atmospheric screen transitions between levels: colour drains away row by row before the new level appears. The game *feels* different from anything before because the learner controls *when* things happen, not just *what* happens.

---

### Game 8: Minefield

**Units:** 16
**Genre:** Grid logic game (Minesweeper-style)
**Final size:** ~80 lines
**Inspired by:** Minesweeper, logic puzzles

Navigate a grid. Hidden mines surround you. Each revealed cell shows how many adjacent mines exist. Use logic to find a safe path to the exit.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| 2D arrays | `DIM m(10,10)` — a grid of data |
| Array initialisation | Filling arrays with starting values |
| Flags | 0/1 values meaning hidden/revealed/flagged |
| Reading neighbours | Checking all 8 adjacent cells |
| `GO SUB` architecture | Multiple subroutines, organised by purpose |
| Separating data from display | The grid array vs what's on screen |
| `ATTR` | Reading the colour of a character cell — the screen is data |
| Cascading visual effects | Reveal animations ripple outward, changing PAPER cell by cell |

**Why this game:** 2D arrays are the fundamental data structure for grids, boards, maps, and rooms. ATTR lets the learner *read* the screen — the display isn't just output, it's queryable data. Reveal animations cascade outward from each uncovered cell, changing PAPER colours with a rippling BEEP. Mine detonation is a visual event: FLASH, descending tone, border strobe, chain reaction. The distinction between game state (the array) and display (what's on screen) is a crucial insight.

---

### Game 9: Brick Bash

**Units:** 16
**Genre:** Breakout-style action game
**Final size:** ~80 lines
**Inspired by:** Breakout, Arkanoid, magazine type-in bat-and-ball games

Bricks built from CHR$ block characters fill the top of the screen. A ball bounces around the play area — drawn with PLOT/DRAW and CIRCLE, checked with POINT for pixel-level collision. The bat moves smoothly along the bottom. Block-graphic borders frame the play area. Bricks shatter row by row with colour changes and descending tones.

The game evolves: early units use simple dx/dy reversal for bouncing. Later units introduce angle-based deflection — where the ball hits the bat determines the reflection angle, calculated with SIN, COS, and ATN. Hitting the bat's edge sends the ball at a steep angle; hitting the centre sends it straight back up.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CHR$` 128-143 | Block graphic characters — bricks, borders, frame elements |
| `CHR$` / `CODE` | Character codes, converting between numbers and characters |
| `PLOT` | Drawing a single pixel |
| `DRAW` | Drawing a line from the current position |
| `CIRCLE` | Drawing a circle — the ball, drawn properly |
| `POINT` | Reading whether a pixel is set |
| Pixel coordinates | 256×176 pixel grid vs 32×22 character grid |
| Ball physics | Simple dx/dy reversal first, then angle-based deflection |
| `SIN` / `COS` | Converting an angle to dx/dy velocity components |
| `ATN` | Calculating the deflection angle from bat impact position |
| `TAN` | The ratio of SIN to COS — completes the trigonometry family |
| `ASN` / `ACS` | Inverse functions — velocity components back to angle |
| `PI` | The constant needed for angle calculations |
| Character-pixel hybrid | Bricks are characters, the ball lives in pixels |
| Screen framing | Block-graphic borders create a polished game frame |

**Why this game:** The learner bridges character space and pixel space for the first time. Bricks are built from CHR$ block characters — the Spectrum's built-in graphic set of half-blocks, quarter-blocks, and stripes. The ball lives in pixel space, drawn with CIRCLE, its position checked with POINT. The trigonometry isn't abstract maths — it solves a problem the learner can feel. Simple bouncing (reverse dx or dy) works, but the ball always goes the same way. Angle-based deflection from the bat position makes the game *controllable* — skilled players can aim. SIN and COS convert the angle to velocity; ATN calculates the angle from where the ball hit the bat. The maths earns its place by making the game better.

---

### Game 10: Night Patrol

**Units:** 16
**Genre:** Top-down maze chase
**Final size:** ~100 lines
**Inspired by:** Magazine chase games, Pac-Man

Move through a maze collecting items while enemies chase you. Enemies use simple AI to pursue. Multiple levels with different maze layouts stored in DATA statements.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Map data | String arrays as maze layouts |
| Drawing a map from data | Reading strings, plotting walls and paths |
| Simple AI | Enemies move toward the player |
| Multiple enemies | Arrays for enemy positions |
| Level data in `DATA` | Different mazes for different levels |
| `RESTORE` to specific line | Loading a particular level's data |
| `OVER 1` | XOR mode — move sprites without destroying the background |
| `SCREEN$` | Reading the character at a screen position |
| String arrays | `DIM m$(20)` — a list of strings for level data |
| Flicker-free movement | OVER 1 combined with PEEK timing for the smoothest movement yet |

**Why this game:** OVER 1 (XOR mode) is the big unlock — the player and enemies move across the maze without destroying it. No more erase-and-redraw flicker. Combined with PEEK timing from Game 7, movement is the smoothest yet. This is the most complex game so far — a complete arcade-style experience with AI, levels, and real tension. It consolidates every skill from the previous nine games. The learner who finishes Night Patrol is ready for the projects phase.

---

## Projects (Games 11-14, 32 units each)

These are real software projects. Each takes sustained effort over 32 units and produces something the learner can be genuinely proud of. The code is substantial (200-400 lines) and requires planning and organisation.

---

### Game 11: Tarmac

**Units:** 32
**Genre:** Top-down racing game
**Final size:** ~300 lines
**Inspired by:** Super Sprint, magazine type-in racers

A top-down racer where the track scrolls toward the player. Track tiles, kerbs, grass, barriers, and the player's car are all hand-designed 8×8 pixel graphics that replace the standard character set. The entire game has its own visual identity — every tile is designed, not default. Different surfaces use different character tiles, creating varied terrain from a single custom set. The track gets faster and narrower as levels progress.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Custom character set | POKE 23606/23607 (CHARS) replaces the entire font |
| Character design | Hand-designed 8×8 pixel graphics for track, car, barriers |
| Tile-based level design | The track is built from repeating character tiles |
| Vertical scrolling | The track moves toward the player, one row at a time |
| Surface types | Different tiles mean different behaviour (road, grass, kerb) |
| Speed and difficulty | The track gets faster and narrower with each level |
| Code at scale | 300 lines that must work together |
| Visual identity | The game looks nothing like standard Spectrum text |

**Why this game:** The custom character set is the visual centrepiece. POKE to the CHARS system variable (23606/23607) installs a bespoke font — track tiles, car sprites, and barriers are all hand-designed 8×8 pixel graphics that replace the standard character set. The entire game has its own typeface. *The game looks nothing like standard Spectrum text.* Everything on screen is designed, not default. The learner discovers that the character set isn't fixed — it's programmable, and replacing it transforms the machine's appearance completely.

---

### Game 12: Ink Spill

**Units:** 32
**Genre:** Colour flood puzzle
**Final size:** ~300 lines
**Inspired by:** Flood-It, colour flood puzzles

A grid of coloured cells. Each turn, the player chooses a colour, and all connected cells matching the player's current colour flood to the new choice — rippling outward, cell by cell, with a cascading POKE that transforms the board in real time. Capture the entire board in as few turns as possible. Colour *is* the game: the player's strategy is about which colour to choose, and the screen reflects every decision instantly.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Direct attribute POKE (22528+) | Fast colour changes without reprinting characters |
| Colour as game mechanic | The player's strategy is about which colour to choose |
| Flood fill algorithm | Connected cells change colour, rippling outward |
| Board state in attributes | The attribute file *is* the game board |
| Turn-based strategy | Plan each move to capture the most territory |
| `FLASH` / `INVERSE` | Visual feedback — highlights, selection indicators |
| Formatted display | Score panel, colour palette, turn counter |

**Why this game:** Direct POKE to the attribute file (22528+) gives speed that PRINT AT can't match. The flood fill ripples outward cell by cell — a visual effect that's only possible because attribute writes are fast. Colour isn't decoration here — it's the entire mechanic. The learner discovers that POKE to the attribute file is faster than PRINT, and uses that speed for gameplay. FLASH and INVERSE carry information, not decoration.

---

### Game 13: Rooftops

**Units:** 32
**Genre:** Platformer
**Final size:** ~300 lines
**Inspired by:** Manic Miner, Jet Set Willy, magazine type-in platformers

A running character leaps between rooftops, collecting items and avoiding hazards. The character has animation frames — legs moving as they run — designed as UDGs (user-defined graphics). Platforms, collectibles, and hazards are all hand-designed 8×8 sprites. Jump physics give weight and momentum. Platform collision uses ATTR and SCREEN$ to check what's beneath the player's feet.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `USR` | Defining user-defined graphic characters |
| `BIN` | Binary notation for pixel rows |
| UDG design | Graph paper → binary → POKE |
| `PRINT AT` with UDGs | Custom graphics positioned on screen |
| Animation | Cycling between UDG frame definitions |
| Jump physics | Gravity, momentum, arc — the character has weight |
| Platform collision | ATTR/SCREEN$ to check what's beneath the player |
| Multi-screen levels | Different screens connected by exits |

**Why this game:** UDGs transform the Spectrum's appearance — suddenly the game looks *authored*, not like text. Every visual element is hand-designed: the character, the platforms, the collectibles. The animation — legs cycling as the character runs — makes the sprite feel alive. Jump physics add weight and momentum that make movement satisfying. The learner designs their own graphics for the first time, working at the pixel level with BIN notation. The game looks like something from a magazine — because it uses the same techniques magazine games used.

---

### Game 14: Blockstorm

**Units:** 32
**Genre:** UDG action shooter
**Final size:** ~400 lines
**Inspired by:** Magazine type-in shooters, arcade conversions

A vertically scrolling shooter using user-defined graphics. Custom spaceship, enemies, projectiles, explosions — all designed as 8×8 pixel UDGs. Real-time action with multiple enemies, bullet management, and increasing difficulty. Pushes Sinclair BASIC to its speed limits.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Multiple UDG sets | Different graphics for ship, enemies, bullets, explosions |
| Bullet pool | Fixed array of projectiles, recycled on hit/miss |
| Enemy patterns | Dive, patrol, chase behaviours |
| Speed optimisation | Short variable names, GOSUB placement, integer tricks |
| `CLEAR` | `CLEAR 59999` — set RAMTOP to protect machine code from BASIC |
| Machine code helpers | Small Z80 routines in DATA, POKEd into RAM, called via `RANDOMIZE USR` |
| `IN` 31 (Kempston joystick) | Arcade-feel input for action games |
| `INPUT LINE` | Read a full line without quotes — high score name entry |
| High score table | Name entry, sorting, display |
| The limits of BASIC — and how to break through | Frame rate ceiling, then machine code punches through it |

**Why this game:** The big unlock: small machine code routines stored in DATA, POKEd into RAM, called via RANDOMIZE USR. A fast screen clear. A smooth scroll. A sound effect richer than BEEP. The game runs faster than BASIC should allow. The learner hits the performance ceiling — and then punches through it. They've written their first assembly, embedded in BASIC. They understand why it's faster. They know what every byte does. This is the bridge to the assembly track.

---

## Advanced (Game 15, 32 units)

### Game 15: Dungeons of Dorin

**Units:** 32
**Genre:** Dungeon crawl RPG
**Final size:** ~450 lines
**Inspired by:** Rogue, early CRPGs, Fighting Fantasy

A dungeon crawler with character stats, random encounters, combat, equipment, and procedural level generation. The player descends through floors of a dungeon, fighting monsters, finding treasure, and trying to reach the bottom. Turn-based combat with stats. Simple procedural generation creates a different dungeon each time.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Character stats | HP, attack, defence as variables |
| Combat system | Turn-based, stat-influenced, with randomness |
| Equipment | Items that modify stats |
| Procedural generation | Random dungeon layout each play |
| Larger state management | Many variables, many flags, many arrays working together |
| `DEF FN` / `FN` | User-defined functions — `DEF FN d(a,d) = INT(a*RND - d/2)` for damage formulas |
| `LN` / `EXP` | Logarithmic and exponential functions — loot rarity curves, difficulty scaling |
| `SAVE` / `LOAD` / `VERIFY` | Saving game state to tape, verifying the save, loading it back |
| Multiple interacting systems | Combat + inventory + movement + generation |
| `OUT` 254 (border port) | Screen shake via rapid border changes during combat |
| Machine code helpers | Fast room redraws and richer sound effects via DATA/POKE/USR |
| `VAL$` | Evaluating a string as an expression — `VAL$ "2+3"` gives "5" |
| Atmospheric depth | Deeper floors get darker PAPER, lower BRIGHT — the dungeon *feels* dangerous |

**Why this game:** Procedural generation is the wonder moment — the learner sees something on screen that *they didn't design*. The code generated it. DEF FN gives the learner proper functions for the first time — damage formulas, hit probability, distance calculations — cleaner than GO SUB when you need a value back. EXP drives loot rarity: `IF RND < EXP(-floor/3) THEN rare_item` — deeper floors yield rarer treasures. OUT 254 adds physical impact to combat: screen shake from rapid border writes, richer than anything BASIC's BEEP can produce. Machine code helpers handle fast room redraws. Deeper floors get darker, lower BRIGHT — the dungeon *feels* dangerous. Save/load/verify teaches persistence — the game outlasts a single session. The RPG structure (stats, combat, equipment) translates directly to the NPC systems in Game 16.

---

## Capstone (Game 16, 64 units)

### Game 16: Thornwood Manor

**Units:** 64
**Genre:** Top-down adventure with autonomous NPCs
**Final size:** ~500 lines
**Inspired by:** The Legend of Zelda, The Hobbit (Melbourne House, 1982)

The learner's magnum opus. Connected screens form a manor and its grounds, drawn with custom character tiles and UDGs. The player explores top-down, Zelda-style: rooms scroll into view as they cross screen boundaries. NPCs move autonomously between rooms on their own schedules. Items, doors, and combat use everything the learner has built across fifteen games.

Thornbury Manor stands frozen — every guest mid-gesture, mid-laugh, mid-step. The player explores the manor, solves puzzles, and breaks the curse room by room. As each part of the curse lifts, the guests unfreeze and begin acting on their own — moving through rooms, helping or hindering the player.

This is what 500 lines of Sinclair BASIC can achieve when the programmer knows what they're doing.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Connected screens | Rooms scroll into view as the player crosses boundaries |
| Top-down movement | Character moves freely in 2D space |
| Custom character tiles | Manor rooms built from designed tile sets |
| Attribute-based mood | Frozen rooms are blue/cyan; as the curse lifts, rooms warm to yellow/white |
| Autonomous NPCs | Characters that move and act on their own schedules |
| NPC interaction | Trading, conversation, help or hindrance |
| Items and inventory | GET/DROP/USE tracked in arrays |
| Puzzle state | Boolean flags for progress (key found, door unlocked) |
| Multiple interacting systems | NPCs + inventory + combat + rooms + atmosphere |
| Machine code helpers | Fast redraws and atmospheric sound via DATA/POKE/USR |
| The final visual moment | The curse breaks — colour floods back room by room via cascading attribute POKE |
| The complete picture | Everything from 15 games, brought together |

**Why last:** The learner who typed in a magazine listing in Game 1 finishes by building a top-down adventure where frozen guests wake up and act on their own. Connected screens form a living manor. Custom character tiles and UDGs create a world that looks hand-crafted. The colour palette tells the story: frozen rooms are blue and cyan, and as the curse lifts, rooms warm through yellow to white. The final moment — the curse breaks and colour floods back room by room — is a cascading attribute POKE that transforms the manor from cold to alive.

Some learners will stay here and build more adventures. Others will look at those DATA/POKE/USR routines and think: what if I wrote the whole thing in assembly? Both paths lead somewhere worth going.

---

## Concept Progression Summary

### By game, when each concept group is first introduced:

| Concept group | First game | Reinforced in |
|---------------|-----------|---------------|
| **Language fundamentals** | | |
| PRINT, LET, variables, INPUT, IF/THEN, GO TO, REM | 1 | Every game |
| RND, INT, RANDOMIZE | 1 | 4, 7, 15 |
| LIST, NEW, RUN, STOP, CONTINUE | 1 | — (editor/debug) |
| INKEY$, BEEP, CLS, PAUSE, PRINT AT | 2 | 4, 7, 10, 14 |
| FOR/NEXT/STEP, colour model (INK/PAPER/BORDER/BRIGHT) | 3 | 4, 7, 8, 9 |
| Position variables, game loop, ABS, SQR, ^ | 4 | 7, 8, 9, 15 |
| Strings, DATA/READ, LEN, slicing, STR$, VAL | 5 | 6, 10, 16 |
| GO SUB/RETURN, arrays, RESTORE, AND/OR/NOT, TAB | 6 | 7, 8, 10, 12 |
| **Hardware access** | | |
| PEEK 23672 (frames counter), attribute-file POKE, SGN | 7 | 10, 12, 14 |
| ATTR (reading screen as data), 2D arrays | 8 | 9, 13 |
| CHR$ 128-143 (block graphic characters), CHR$/CODE | 9 | 13 |
| PLOT, DRAW, CIRCLE, POINT (pixel graphics) | 9 | 13 |
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
| **Game systems** | | |
| 2D arrays, flags, neighbours | 8 | 10, 12, 15 |
| String arrays, map data, AI | 10 | 14, 16 |
| Tile design, scrolling, visual identity | 11 | 16 |
| Flood fill, colour as mechanic | 12 | — |
| Jump physics, platforming, UDG sprite design | 13 | 14 |
| Bullet pools, enemy patterns | 14 | — |
| Stats, combat, equipment, procedural generation | 15 | 16 |
| Connected screens, autonomous NPCs, top-down world | 16 | — |

---

## Changelog

- **v5.3 DRAFT (2026-03-18):** Complete keyword coverage. Added RANDOMIZE, STOP/CONTINUE, LIST/NEW/RUN (Game 1), STEP (Game 3), SQR/^ (Game 4), STR$/VAL (Game 5), NOT/TAB (Game 6), SGN (Game 7), CIRCLE/SIN/COS/TAN/ATN/ASN/ACS/PI (Game 9 — angle-based bat deflection), CLEAR/INPUT LINE (Game 14), DEF FN/LN/EXP/VAL$/VERIFY (Game 15). Dropped COPY/LPRINT/LLIST/MERGE/OPEN#/CLOSE# and Microdrive commands (peripheral-specific, no stock 48K use). Every teachable Sinclair BASIC keyword now has a game assignment.
- **v5.2 DRAFT (2026-03-18):** Aligned game names and descriptions with visual progression document. Game 2: Countdown → Wire Panic. Game 3: Colour Flood → Bright Spark. Game 5: Word Scramble → Letter Soup. Game 7: Treasure Hunt → Tail Chase (snake game). Game 9: Word Worm → Brick Bash (Breakout — moves PLOT/DRAW/POINT from Projects to Skills). Game 11: Draughts → Tarmac (racing with custom character set). Game 12: Battleships → Ink Spill (colour flood puzzle with direct attribute POKE). Game 13: Lattice → Rooftops (platformer — moves UDGs from Game 14 to Game 13). Game 16: The Cursed Manor → Thornwood Manor (top-down Zelda-style, not text parser). Concept progression table updated to match new game assignments. PRINT AT moved to Game 2 (Wire Panic).
- **v5.1 DRAFT (2026-03-16):** Aligned with visual progression plan. Game 1 rewritten for starter-kit approach (type-in listing, then take it apart). Added hardware/visual concepts throughout: PEEK timing (Game 7), ATTR collision (Game 8), CHR$ block graphics (Game 9), OVER 1 (Game 10), custom character sets (Game 11), direct attribute POKE (Game 12), machine code helpers (Game 14), OUT 254 (Game 15), attribute-based mood (Game 16). GO SUB moved to Game 6. Concept progression table reorganised by category.
- **v5.0 DRAFT (2026-03-13):** Complete restructure. 16 games (was 4). Graduated difficulty: 8→16→32→64 units. Every BASIC concept mapped to the game that introduces it. Teaching from absolute zero.
- **v4.0 (2026-03-09):** 4 games × 64 units (256 total).
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
