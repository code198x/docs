# Sinclair ZX Spectrum BASIC Curriculum (v5.0 DRAFT)

**Platform:** Sinclair ZX Spectrum 48K
**Language:** Sinclair BASIC
**Games:** 16
**Total Units:** 336

---

## Overview

The Sinclair BASIC curriculum teaches programming from absolute zero through 16 complete games. A learner who has never written a line of code can start at Game 1 and finish at Game 16 having built a graphical adventure with autonomous NPCs.

The games grow in ambition as the learner's skills grow. Early games are tiny (8 units, under 30 lines) and exist purely to teach language fundamentals. Later games are substantial (32-64 units, hundreds of lines) and feel like real software.

Every concept is introduced before it's needed. No game assumes knowledge that hasn't been taught by a previous game. The curriculum document below lists every new concept alongside the game that introduces it.

BASIC is not a prerequisite for the assembly track. The two tracks are independent — but a learner who completes the BASIC track arrives at assembly with real hardware knowledge. By Game 14, they're writing machine code in DATA statements. By Game 16, they've built an illustrated adventure with autonomous NPCs. The assembly track isn't a scary new world — it's the thing they've been reaching for every time BASIC wasn't fast enough.

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
| `INT` | Rounding to a whole number (`INT(RND*100)+1`) |

**Present in the starter program but NOT formally taught yet:** FOR/NEXT (Game 3), INK/PAPER/BORDER/BRIGHT/BEEP (Games 2-3), PRINT AT (Game 4), DATA/READ/RESTORE (Game 5), GO SUB/RETURN (Game 6). These are black boxes — magic that works. Each is formally introduced in the game listed.

**Why this game:** Every concept has an immediate, visible purpose. `INPUT` is how the player guesses. `IF/THEN` is how the computer responds. `GO TO` is what keeps the game running. Nothing is abstract. And the learner's very first Spectrum program looks like something worth showing to a friend.

**Milestone:** The learner has typed in, run, and partially understood a complete interactive program.

---

### Game 2: Countdown

**Units:** 8
**Genre:** Reaction timer
**Final size:** ~25 lines

A word appears on screen. Press a key as fast as you can. The program measures your reaction time. Compete against yourself or a friend.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `CLS` | Clearing the screen |
| `INKEY$` | Checking the keyboard without waiting |
| The empty string `""` | What `INKEY$` returns when no key is pressed |
| Loops with `GO TO` | Spinning until something happens |
| `PAUSE` | Waiting for a set time |
| `BEEP` | Making sound (duration and pitch) |
| String variables | `a$` — names that hold text |
| The difference between `INPUT` and `INKEY$` | Blocking vs non-blocking input |

**Why this game:** `INKEY$` is the foundation of every action game on the Spectrum. Understanding the difference between "wait for the player" (`INPUT`) and "check right now" (`INKEY$`) is fundamental. The reaction timer makes this visceral — you feel the difference.

**Milestone:** The learner understands two models of input and can make sounds.

---

### Game 3: Colour Flood

**Units:** 8
**Genre:** Visual toy / screen-filling patterns
**Final size:** ~25 lines

Fill the screen with colour patterns. Stripes, checkerboards, random splashes. Each pattern is a few lines of code. The learner experiments with loops and colour to create visual effects.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `FOR`/`NEXT` | Counted loops — do something N times |
| `BORDER` | The screen border colour |
| `PAPER` | The background colour |
| `INK` | The text/foreground colour |
| The 8 colours (0-7) | Black, blue, red, magenta, green, cyan, yellow, white |
| `BRIGHT` | Brighter versions of the colours |
| Nested loops | A `FOR` inside a `FOR` |
| The screen as a grid | 24 rows, 32 columns, each cell has INK and PAPER |

**Why this game:** This is the first game where the result is primarily visual rather than textual. The learner sees the direct relationship between code and what appears on screen. Loops stop being abstract (repeat N times) and become concrete (draw a row of red squares).

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
| `PRINT AT` | Placing text at a specific row and column |
| The coordinate grid | Row 0-23, column 0-31 |
| Using variables for position | `r` for row, `c` for column |
| Updating position | `LET r = r - 1` (move up) |
| `<>`, `<=`, `>=` | More comparison operators |
| `ABS` | Distance without caring about direction |
| The game loop | Read input → update state → draw |

**Why this game:** `PRINT AT` unlocks the Spectrum's screen. The learner moves from sequential text output to placing things where they want them. This is the fundamental skill for every game from here on.

**Milestone:** The learner can position text on screen and build a game loop.

---

### Game 5: Word Scramble

**Units:** 8
**Genre:** Word puzzle
**Final size:** ~30 lines

A scrambled word appears. Type the correct word to score a point. Ten rounds, then your score. Words get harder.

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
| Score tracking | A variable that counts correct answers |
| Animated letter reveal | Characters appear one at a time with ascending BEEP |

**Why this game:** Strings are essential for the text adventure later. This game makes string manipulation tangible — you can see the letters being scrambled and unscrambled. `DATA`/`READ` provides a natural way to store the word list. The animated letter reveal — characters appearing one at a time with ascending BEEP — builds anticipation and shows how loops and timing create drama.

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
| `AND` / `OR` | Combining conditions |
| Simple arrays | `DIM s(4)` — a row of numbered boxes |
| Array access | `LET s(p) = s(p) + 1` — updating a specific element |
| Line numbering conventions | Organising code into sections (100s, 200s, etc.) |
| Multiple colons | Several commands on one line |
| Structured screen layout | GO SUB draws formatted question cards with coloured borders |

**Why this game:** GO SUB is the first step toward structured code — the quiz naturally needs reusable drawing routines for question cards and score panels. Arrays are the gateway to real data structures. A quiz game makes them natural — you need somewhere to store four players' scores. `RESTORE` completes the `DATA`/`READ` toolkit. And the learner starts thinking about code organisation for the first time.

**Milestone:** The learner has the full BASIC toolkit for simple programs: variables, strings, arrays, loops, decisions, input, colour, sound, data, and reusable subroutines.

---

## Skills (Games 7-10, 16 units each)

These four games build real gameplay skills. The learner already knows the language; now they learn to use it. Each game is a recognisable type — the kind of thing that appeared in magazine type-in listings.

---

### Game 7: Treasure Hunt

**Units:** 16
**Genre:** Grid collection game
**Final size:** ~60 lines
**Inspired by:** Magazine type-in listings

A character moves around a grid collecting coins while avoiding hazards. PRINT AT for all display. INKEY$ for real-time control. A timer counts down. Clear each level to progress.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| The game loop (formal) | Input → update → draw, running continuously |
| `INKEY$` in a game loop | Polling every frame, not blocking |
| Moving a character | Erase old position, draw new position |
| Collision detection | Same cell = hit |
| Game states | Playing, game over, level complete |
| Lives | Lose a life, reset position, continue |
| Level progression | Harder each time (more hazards, less time) |
| `PEEK` 23672 (frames counter) | Consistent game speed regardless of what's on screen |
| Attribute-file POKE (22528+) | Screen transitions — fade to black row by row before redrawing |
| `FLASH` for items | Coins glitter, hazards pulse with alternating INK |

**Why this game:** This is the learner's first real-time game, and the first time they touch the hardware directly. PEEK 23672 gives consistent frame-rate timing — movement is smooth because it's *timed*, not just fast. Attribute-file POKEs create atmospheric screen transitions between levels: colour drains away row by row before the new level appears. The game *feels* different from anything before because the learner controls *when* things happen, not just *what* happens.

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

### Game 9: Word Worm

**Units:** 16
**Genre:** Typing challenge
**Final size:** ~80 lines
**Inspired by:** Typing of the Dead, word games

Words fall from the top of the screen. Type them before they reach the bottom. Speed increases as you progress. Miss three and it's game over.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| String arrays | `DIM w$(50)` — a list of strings |
| `CHR$` / `CODE` | Character codes, converting between numbers and characters |
| `CHR$` 128-143 | Block graphic characters for screen framing and borders |
| String building | Assembling input character by character |
| Increasing difficulty | Speed controlled by a variable that changes |
| Multiple objects on screen | Tracking several words simultaneously |
| `GOSUB` dispatch | Using a variable to choose which subroutine to call |
| Screen framing | Box-drawing characters, arrows, and symbols create a polished game frame |

**Why this game:** String arrays and character-level string handling are essential for the text adventure's parser. CHR$ 128-143 unlocks the Spectrum's built-in block graphic characters — box-drawing, arrows, symbols — transforming the game from text on a black screen to a polished application with proper framing. The pressure of falling words forces the learner to think about strings as sequences of characters, not opaque blocks.

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
| Flicker-free movement | OVER 1 combined with PEEK timing for the smoothest movement yet |

**Why this game:** OVER 1 (XOR mode) is the big unlock — the player and enemies move across the maze without destroying it. No more erase-and-redraw flicker. Combined with PEEK timing from Game 7, movement is the smoothest yet. This is the most complex game so far — a complete arcade-style experience with AI, levels, and real tension. It consolidates every skill from the previous nine games. The learner who finishes Night Patrol is ready for the projects phase.

---

## Projects (Games 11-14, 32 units each)

These are real software projects. Each takes sustained effort over 32 units and produces something the learner can be genuinely proud of. The code is substantial (200-400 lines) and requires planning and organisation.

---

### Game 11: Draughts

**Units:** 32
**Genre:** Two-player board game
**Final size:** ~300 lines
**Inspired by:** Classic board game conversions

A full implementation of draughts (checkers). Two-player, legal move validation, mandatory captures, king promotion, win detection. Clean board display using PRINT AT and colour.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Custom character set | POKE 23606/23607 (CHARS) replaces the entire font |
| Character design | Hand-designed 8×8 pixel graphics for pieces, borders, board |
| Complex move validation | Legal vs illegal, mandatory captures |
| Turn-based game flow | Alternating players, state transitions |
| Board display | Custom-designed pieces, not default characters |
| Search patterns | Checking all possible moves for a piece |
| Rule encoding | Translating real-world rules into IF/THEN chains |
| Input validation | Parsing coordinate input (e.g. "A3 B4") |
| Code at scale | 300 lines that must work together |
| Visual identity | The game looks nothing like standard Spectrum text |

**Why this game:** The custom character set is the visual centrepiece. POKE to the CHARS system variable (23606/23607) installs a bespoke font — board pieces aren't letters, they're hand-designed 8×8 pixel graphics. The entire game has its own typeface: custom alphabet, custom numbers, custom border characters. Draughts is also a test of logical thinking — the rules are simple but encoding them precisely requires careful, systematic programming.

---

### Game 12: Battleships

**Units:** 32
**Genre:** Two-player strategy game
**Final size:** ~300 lines
**Inspired by:** Battleship (board game), magazine type-in versions

Two players take turns calling coordinates to find and sink each other's fleet. Each player has a 10×10 grid — one showing their own ships and incoming hits, one tracking their shots against the opponent. Ships of different lengths, hit/miss/sunk detection, and a "pass the keyboard" two-player mode.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Parallel state | Two grids per player — your ships, your guesses |
| Hidden information | One player's grid must not be visible to the other |
| Ship placement | Validating that ships fit on the grid and don't overlap |
| Coordinate parsing | "B7" → row 1, column 6 (building on Draughts) |
| Hit/miss/sunk logic | Tracking damage per ship, detecting when all cells are hit |
| Screen management | `CLS` between turns to hide information |
| Formatted display | Drawing two grids side by side with labels |
| `FLASH` / `INVERSE` | Visual feedback for hits and misses — information, not decoration |
| Direct attribute POKE (22528+) | Fast colour effects — hit ripples, sunk ship colour drain |
| Dramatic visual events | Every hit and miss is an event: flash ripple, colour drain, descending tone |

**Why this game:** Direct POKE to the attribute file (22528+) gives speed that PRINT AT can't match — hit ripples flash across a ship's cells, sunk ships drain to black cell by cell with a descending tone. FLASH and INVERSE carry information, not decoration. Battleships extends the board game skills from Draughts into hidden information and parallel state. The learner manages four 2D arrays simultaneously and builds ship placement validation more complex than Draughts' move rules.

---

### Game 13: Lattice

**Units:** 32
**Genre:** Graphical puzzle
**Final size:** ~300 lines
**Inspired by:** Graphical puzzle games, geometric design

A puzzle game using Sinclair BASIC's graphics commands. PLOT draws points, DRAW connects them, CIRCLE creates shapes. Collision detection reads attribute values. The game has a distinct Spectrum aesthetic: clean geometry and blocky colour.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| `PLOT` | Drawing a single pixel |
| `DRAW` | Drawing a line from the current position |
| `CIRCLE` | Drawing a circle |
| `POINT` | Reading whether a pixel is set |
| `ATTR` | Reading the attribute (colour) of a character cell |
| Pixel coordinates | 256×176 pixel grid vs 32×22 character grid |
| Collision via colour | If the pixel under the player is red, it's a wall |
| `SIN`, `COS` | Circular motion and angles |
| Combining graphics and text | PLOT/DRAW for the game, PRINT AT for the HUD |

**Why this game:** The Spectrum's graphics commands are surprisingly capable. This game shows that BASIC can produce visuals beyond character cells. The ATTR-based collision technique is exactly what the assembly curriculum uses, creating a bridge between the two tracks.

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
| `USR` | Defining user-defined graphic characters |
| `BIN` | Binary notation for pixel rows |
| UDG design | Graph paper → binary → POKE |
| `PRINT AT` with UDGs | Custom graphics positioned on screen |
| Animation | Cycling between UDG frame definitions |
| Bullet pool | Fixed array of projectiles, recycled on hit/miss |
| Enemy patterns | Dive, patrol, chase behaviours |
| Speed optimisation | Short variable names, GOSUB placement, integer tricks |
| `PEEK` | Reading memory (for timing) |
| Machine code helpers | Small Z80 routines in DATA, POKEd into RAM, called via `RANDOMIZE USR` |
| `IN` 31 (Kempston joystick) | Arcade-feel input for action games |
| High score table | Name entry, sorting, display |
| The limits of BASIC — and how to break through | Frame rate ceiling, then machine code punches through it |

**Why this game:** UDGs transform the Spectrum's appearance — suddenly the game looks *authored*, not like text. Every visual element is hand-designed. And the big unlock: small machine code routines stored in DATA, POKEd into RAM, called via RANDOMIZE USR. A fast screen clear. A smooth scroll. A sound effect richer than BEEP. The game runs faster than BASIC should allow. The learner hits the performance ceiling — and then punches through it. They've written their first assembly, embedded in BASIC. They understand why it's faster. They know what every byte does. This is the bridge to the assembly track.

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
| `SAVE` / `LOAD` | Saving game state to tape — the game outlasts a single session |
| Multiple interacting systems | Combat + inventory + movement + generation |
| `OUT` 254 (border port) | Screen shake via rapid border changes during combat |
| Machine code helpers | Fast room redraws and richer sound effects via DATA/POKE/USR |
| Atmospheric depth | Deeper floors get darker PAPER, lower BRIGHT — the dungeon *feels* dangerous |

**Why this game:** Procedural generation is the wonder moment — the learner sees something on screen that *they didn't design*. The code generated it. OUT 254 adds physical impact to combat: screen shake from rapid border writes, richer than anything BASIC's BEEP can produce. Machine code helpers handle fast room redraws. Deeper floors get darker, lower BRIGHT — the dungeon *feels* dangerous. Save/load teaches persistence. The RPG structure (stats, combat, equipment) translates directly to the NPC systems in Game 16.

---

## Capstone (Game 16, 64 units)

### Game 16: The Cursed Manor

**Units:** 64
**Genre:** Graphical text adventure with autonomous NPCs
**Final size:** ~500 lines
**Inspired by:** The Hobbit (Melbourne House, 1982)

The learner's magnum opus. Thornbury Manor stands frozen — every guest mid-gesture, mid-laugh, mid-step. The player explores the manor, solves puzzles, and breaks the curse room by room. As each part of the curse lifts, the guests unfreeze and begin acting on their own — moving through rooms, talking to each other, helping or hindering the player.

Location illustrations drawn with PLOT/DRAW. A rich parser that understands prepositions and indirect commands ("say to butler open the cellar"). NPCs with goals and relationships. Events that happen whether the player is present or not. The manor comes alive around you.

This is what 500 lines of Sinclair BASIC can achieve when the programmer knows what they're doing.

**New concepts introduced:**
| Concept | What the learner discovers |
|---------|---------------------------|
| Location illustrations | PLOT/DRAW pictures for each room — real illustrations, not character art |
| Custom character set | Gothic, manor-appropriate typeface via POKE CHARS |
| Attribute-based mood | Frozen rooms are blue/cyan; as the curse lifts, rooms warm to yellow/white |
| The command loop | `INPUT` → parse → dispatch → display |
| Parser design | Splitting strings, verb lookup, synonym handling |
| Room model | Number, name, description, exits as DATA |
| Item model | Location tracking (in room, carried, used) |
| Inventory | Array of carried items, GET/DROP/EXAMINE |
| Puzzle state | Boolean flags for progress (key found, door unlocked) |
| Autonomous NPCs | Characters that move and act on their own |
| NPC decision-making | Simple goal-driven behaviour |
| Event system | Things happen independently of the player |
| Advanced parser | Prepositions, indirect objects, SAY TO [character] |
| NPC interaction | Talking to characters, giving orders |
| Multiple solutions | Puzzles solvable in different ways |
| Machine code helpers | Fast redraws and atmospheric sound via DATA/POKE/USR |
| The final visual moment | The curse breaks — colour floods back room by room via cascading attribute POKE |
| The complete picture | Everything from 15 games, brought together |

**Why last:** The learner who typed in a magazine listing in Game 1 finishes by building a haunted manor where frozen guests wake up and act on their own. Every room is illustrated with PLOT/DRAW. A custom gothic character set sets the atmosphere. The colour palette tells the story: frozen rooms are blue and cyan, and as the curse lifts, rooms warm through yellow to white. The final moment — the curse breaks and colour floods back room by room — is a cascading attribute POKE that transforms the manor from cold to alive. The Hobbit was one of the most celebrated titles on the Spectrum. The Cursed Manor is the learner's own version — a graphical adventure with autonomous NPCs, built from scratch, using every technique from 15 games.

---

## Concept Progression Summary

### By game, when each concept group is first introduced:

| Concept group | First game | Reinforced in |
|---------------|-----------|---------------|
| **Language fundamentals** | | |
| PRINT, variables, INPUT | 1 | Every game |
| INKEY$, BEEP, CLS, PAUSE | 2 | 4, 7, 10, 14 |
| FOR/NEXT, colour model (INK/PAPER/BORDER/BRIGHT) | 3 | 4, 7, 8, 13 |
| PRINT AT, coordinates, game loop | 4 | 7, 8, 10, 12 |
| Strings, DATA/READ, LEN, slicing | 5 | 6, 9, 16 |
| GO SUB/RETURN, arrays, RESTORE, AND/OR | 6 | 7, 8, 10, 12 |
| **Hardware access** | | |
| PEEK 23672 (frames counter), attribute-file POKE | 7 | 10, 12, 14 |
| ATTR (reading screen as data) | 8 | 13 |
| CHR$ 128-143 (block graphic characters) | 9 | 11 |
| OVER 1 (XOR drawing), SCREEN$ | 10 | 14 |
| **Direct control** | | |
| Custom character sets (POKE CHARS 23606/23607) | 11 | 16 |
| Direct attribute POKE (22528+), FLASH/INVERSE | 12 | 15, 16 |
| PLOT, DRAW, CIRCLE, POINT, SIN, COS | 13 | 16 |
| UDGs (USR, BIN), animation, IN 31 (Kempston) | 14 | — |
| **Machine code and beyond** | | |
| Machine code helpers (DATA/POKE/RANDOMIZE USR) | 14 | 15, 16 |
| OUT 254 (border port), speed optimisation | 14-15 | 16 |
| SAVE/LOAD, procedural generation | 15 | — |
| **Game systems** | | |
| 2D arrays, flags, neighbours | 8 | 10, 11, 12, 15 |
| String arrays, CHR$/CODE | 9 | 16 |
| Map data, AI, multiple enemies | 10 | 14, 16 |
| Move validation, turn-based flow | 11 | 12, 15 |
| Parallel state, hidden information | 12 | 16 |
| Stats, combat, equipment | 15 | 16 |
| Parser, inventory, room model, autonomous NPCs | 16 | — |

---

## Changelog

- **v5.1 DRAFT (2026-03-16):** Aligned with visual progression plan. Game 1 rewritten for starter-kit approach (type-in listing, then take it apart). Added hardware/visual concepts throughout: PEEK timing (Game 7), ATTR collision (Game 8), CHR$ block graphics (Game 9), OVER 1 (Game 10), custom character sets (Game 11), direct attribute POKE (Game 12), machine code helpers (Game 14), OUT 254 (Game 15), attribute-based mood (Game 16). GO SUB moved to Game 6. Concept progression table reorganised by category.
- **v5.0 DRAFT (2026-03-13):** Complete restructure. 16 games (was 4). Graduated difficulty: 8→16→32→64 units. Every BASIC concept mapped to the game that introduces it. Teaching from absolute zero.
- **v4.0 (2026-03-09):** 4 games × 64 units (256 total).
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
