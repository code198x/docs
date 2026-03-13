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

BASIC is not a prerequisite for the assembly track. The two tracks are independent.

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

These six games teach the Sinclair BASIC language. Each game is small — under 30 lines — and exists to introduce a handful of concepts through a complete, satisfying experience. A learner can finish all six in a week.

---

### Game 1: Lucky Number

**Units:** 8
**Genre:** Number guessing game
**Final size:** ~20 lines

The computer picks a number between 1 and 100. The player guesses. The computer says higher or lower. Simple, ancient, and a perfect first program.

**New concepts introduced:**
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

**Why this game:** Every concept has an immediate, visible purpose. `INPUT` is how the player guesses. `IF/THEN` is how the computer responds. `GO TO` is what keeps the game running. Nothing is abstract.

**Milestone:** The learner has written, edited, and run a complete interactive program.

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

**Why this game:** Strings are essential for the text adventure later. This game makes string manipulation tangible — you can see the letters being scrambled and unscrambled. `DATA`/`READ` provides a natural way to store the word list.

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
| `RESTORE` | Rewinding `DATA` to read it again |
| `AND` / `OR` | Combining conditions |
| Simple arrays | `DIM s(4)` — a row of numbered boxes |
| Array access | `LET s(p) = s(p) + 1` — updating a specific element |
| Line numbering conventions | Organising code into sections (100s, 200s, etc.) |
| Multiple colons | Several commands on one line |

**Why this game:** Arrays are the gateway to real data structures. A quiz game makes them natural — you need somewhere to store four players' scores. `RESTORE` completes the `DATA`/`READ` toolkit. And the learner starts thinking about code organisation for the first time.

**Milestone:** The learner has the full BASIC toolkit for simple programs: variables, strings, arrays, loops, decisions, input, colour, sound, data.

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
| `GO SUB` / `RETURN` | Subroutines — your first code organisation |

**Why this game:** This is the learner's first real-time game. Everything happens in a loop. The character moves smoothly. Things can kill you. It feels like a game, not a quiz. `GO SUB` arrives here because the code is now complex enough to need structure.

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

**Why this game:** 2D arrays are the fundamental data structure for grids, boards, maps, and rooms. This game makes them essential — you literally cannot build Minesweeper without a 2D array. The distinction between game state (the array) and display (what's on screen) is a crucial insight.

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
| String building | Assembling input character by character |
| Increasing difficulty | Speed controlled by a variable that changes |
| Multiple objects on screen | Tracking several words simultaneously |
| `GOSUB` dispatch | Using a variable to choose which subroutine to call |

**Why this game:** String arrays and character-level string handling are essential for the text adventure's parser. This game makes them fun — the pressure of falling words forces the learner to think about strings as sequences of characters, not opaque blocks.

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

**Why this game:** This is the most complex game so far — a complete arcade-style experience with AI, levels, and real tension. It consolidates every skill from the previous nine games. The learner who finishes Night Patrol is ready for the projects phase.

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
| Complex move validation | Legal vs illegal, mandatory captures |
| Turn-based game flow | Alternating players, state transitions |
| Board display | PRINT AT with INK/PAPER for squares and pieces |
| Search patterns | Checking all possible moves for a piece |
| Rule encoding | Translating real-world rules into IF/THEN chains |
| Input validation | Parsing coordinate input (e.g. "A3 B4") |
| Code at scale | 300 lines that must work together |

**Why this game:** Draughts is a test of logical thinking. The rules are simple but encoding them precisely requires careful, systematic programming. This is the first game where the learner must think like an engineer — breaking a complex problem into small, verifiable pieces.

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
| `FLASH` / `INVERSE` | Visual feedback for hits and misses |

**Why this game:** Battleships extends the board game skills from Draughts into hidden information and parallel state. The learner manages four 2D arrays simultaneously (two grids per player) and builds ship placement validation that's more complex than Draughts' move rules. The coordinate parsing carries over directly, so the learner refines rather than relearns. It's also the last game before graphics — a send-off for character-cell display at its most polished.

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
| Animation | Cycling between UDG frames |
| Bullet pool | Fixed array of projectiles, recycled on hit/miss |
| Enemy patterns | Dive, patrol, chase behaviours |
| Speed optimisation | Short variable names, GOSUB placement, integer tricks |
| `PEEK` | Reading memory (for timing) |
| High score table | Name entry, sorting, display |
| The limits of BASIC | Frame rate ceiling, why assembly exists |

**Why this game:** UDGs transform the Spectrum's appearance — suddenly the game looks custom, not like text. The speed optimisation work teaches how the BASIC interpreter actually works: why `a` is faster than `score`, why GOSUBs early in the listing run faster, why floating point is slow. The learner hits the ceiling and understands it.

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
| `SAVE` / `LOAD` | Saving game state to tape |
| Multiple interacting systems | Combat + inventory + movement + generation |

**Why this game:** This is the proving ground for the capstone. The learner manages a complex system with many interacting parts. Procedural generation means the game is different each time — the learner has created something that surprises even them. Save/load teaches persistence. The RPG structure (stats, combat, equipment) translates directly to the NPC systems in Game 16.

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
| Location graphics | PLOT/DRAW illustrations for each room |
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
| Polish at scale | 500 lines of working, tested, atmospheric code |
| The complete picture | Everything from 15 games, brought together |

**Why last:** The learner who started with `10 PRINT "Hello"` in Game 1 finishes by building a haunted manor where frozen guests wake up and act on their own. The Hobbit was one of the most celebrated titles on the Spectrum. The Cursed Manor is the learner's own version — a graphical adventure with autonomous NPCs, built from scratch. The final act of the game is breaking the curse. The final act of the curriculum is proving you can build something this ambitious.

---

## Concept Progression Summary

### By game, when each concept group is first introduced:

| Concept group | First game | Reinforced in |
|---------------|-----------|---------------|
| PRINT, variables, INPUT | 1 | Every game |
| INKEY$, BEEP, CLS, PAUSE | 2 | 4, 7, 10, 14 |
| FOR/NEXT, colour model | 3 | 4, 7, 8, 13 |
| PRINT AT, coordinates, RND | 4 | 7, 8, 10, 12 |
| Strings, DATA/READ, LEN, slicing | 5 | 6, 9, 16 |
| Arrays, RESTORE, AND/OR | 6 | 8, 10, 12 |
| Game loop, GO SUB, lives, levels | 7 | 8, 9, 10, 14 |
| 2D arrays, flags, neighbours | 8 | 10, 11, 12, 15 |
| String arrays, CHR$/CODE | 9 | 16 |
| Map data, AI, multiple enemies | 10 | 14, 16 |
| Move validation, turn-based | 11 | 12, 15 |
| Parallel state, hidden information, FLASH/INVERSE | 12 | 16 |
| PLOT, DRAW, CIRCLE, POINT, ATTR | 13 | 16 |
| UDGs, animation, optimisation | 14 | — |
| Stats, combat, procedural gen, SAVE/LOAD | 15 | 16 |
| Parser, inventory, room model, autonomous NPCs | 16 | — |

---

## Changelog

- **v5.0 DRAFT (2026-03-13):** Complete restructure. 16 games (was 4). Graduated difficulty: 8→16→32→64 units. Every BASIC concept mapped to the game that introduces it. Teaching from absolute zero.
- **v4.0 (2026-03-09):** 4 games × 64 units (256 total).
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
