# Sinclair ZX Spectrum BASIC Curriculum

**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Games:** 4
**Total Units:** 256 (4 × 64)

---

## Overview

The Sinclair BASIC curriculum teaches programming fundamentals through four complete games. Each game is completable in under 500 lines of Sinclair BASIC. The track follows the Spectrum's BASIC culture: type-in listings from magazines, text adventures, PRINT AT games, and UDG-based action.

Sinclair BASIC is more capable than most home computer BASICs — built-in graphics commands (PLOT, DRAW, CIRCLE), attribute control (INK, PAPER, BRIGHT), and user-defined graphics (UDGs) make it possible to create visually distinctive games without leaving BASIC. The curriculum exploits these capabilities, progressing from text to screen positioning to pixel graphics to custom characters.

BASIC is not a prerequisite for the assembly track. The two tracks are independent. A learner starting at assembly Game 1 should not feel they have missed something by skipping BASIC.

---

## Structure

| Game | Units | Role |
|------|-------|------|
| 1 | 64 | First program — text adventure (the Spectrum BASIC tradition) |
| 2 | 64 | Screen interaction — chase game using PRINT AT |
| 3 | 64 | Graphics — drawing/puzzle game using PLOT, DRAW, ATTR |
| 4 | 64 | Custom graphics — action game with user-defined graphics |
| **Total** | **256** | |

Each game has 4 phases of 16 units. Each unit is 60-120 minutes and produces a working result.

---

## Game Sequence

### Game 1: Text Adventure

**Units:** 64 (4 phases × 16 units)
**Genre:** Text adventure
**Inspired by:** The Hobbit, Level 9 games, The Quill

**Concept:** A text adventure in the Spectrum tradition. The player types commands ("GO NORTH", "GET LAMP", "USE KEY"), explores rooms, collects items, solves puzzles. Text adventures were the Spectrum's first killer genre — The Hobbit shipped with every Spectrum+ — and they teach programming fundamentals through narrative.

**Skills taught:**
- Sinclair BASIC environment and keyword entry system
- Variables, strings, and data types
- INPUT and PRINT statements
- IF/THEN/ELSE logic
- GOTO and GOSUB for program flow
- DATA and READ for room descriptions and connections
- Arrays for inventory and room state
- String handling (LEFT$, RIGHT$, MID$, INKEY$)
- Two-word command parser ("verb noun")
- Game state management (visited rooms, collected items, locked doors)
- Atmospheric text output (PAUSE, INVERSE, colour changes)
- Save/load via SAVE/LOAD (tape persistence)

**Why first:** This is how Spectrum owners started. Text adventures require no graphics knowledge — just strings, logic, and imagination. The game is immediately engaging (explore a world, solve puzzles) while teaching every fundamental programming concept. By the end, the learner has built a real game with 20+ rooms, inventory, and puzzles.

---

### Game 2: Chase Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Top-down chase game
**Inspired by:** Magazine type-ins from Crash, Sinclair User, Your Sinclair

**Concept:** A top-down grid-based game using PRINT AT for all display. The player moves through a maze, collects items, avoids enemies. Enemies chase the player using simple AI. The game looks and feels like the type-in listings that filled 1980s Spectrum magazines — the kind of game someone would type in from a printed listing over a Saturday afternoon.

**Skills taught:**
- PRINT AT for screen positioning (row, column)
- Keyboard scanning (INKEY$)
- Game loop structure (read input, update state, draw)
- Grid-based movement (character cell coordinates)
- Simple AI (enemies move toward player, random patrol)
- Maze data using string arrays
- Collision detection via screen coordinates
- Score tracking and display
- Difficulty progression (faster enemies, more complex mazes)
- Multiple levels with different layouts
- Lives and game-over logic
- Timing control (PAUSE, loop delays)

**Why here:** PRINT AT is the Spectrum's unique BASIC strength — position text anywhere on screen instantly. This game teaches real-time interaction (game loop, keyboard scanning, enemy movement) while staying within the text-mode world the learner already understands from Game 1. The jump from text adventure to action game is where BASIC starts to feel like a real development tool.

---

### Game 3: Drawing/Puzzle Game

**Units:** 64 (4 phases × 16 units)
**Genre:** Graphical puzzle game
**Inspired by:** Type-in graphical games, simple puzzle games

**Concept:** A puzzle game using Sinclair BASIC's graphics commands for rendering. PLOT draws points, DRAW connects them with lines, CIRCLE creates shapes. The attribute system (INK, PAPER, BRIGHT) provides colour. Collision detection reads attribute values — if the pixel is a certain INK colour, it's a wall; another colour, it's a collectible. The game looks distinctly Spectrum: blocky colour, clean geometry, functional beauty.

**Skills taught:**
- PLOT, DRAW, and CIRCLE commands
- INK, PAPER, BRIGHT, FLASH for colour control
- POINT and ATTR functions for reading screen state
- Pixel-level collision detection via colour values
- Coordinate systems (pixel vs. character cell)
- Arrays for game state (board, pieces, positions)
- Mathematical functions (SIN, COS for circular motion, ABS for distance)
- Timer mechanics and score systems
- Level design stored in DATA statements
- Screen clearing and redraw strategies
- BORDER for visual feedback
- Combining graphics and text (PRINT AT for HUD, PLOT/DRAW for game area)

**Why here:** Sinclair BASIC's graphics commands are genuinely capable — PLOT, DRAW, and CIRCLE produce clean vector-style visuals that look good within the attribute system. This game transitions the learner from character-cell thinking (PRINT AT) to pixel thinking (coordinates, angles, distance). Reading ATTR values for collision is also the exact technique used in the assembly curriculum's Game 1, creating a natural bridge.

---

### Game 4: Action Game with UDGs

**Units:** 64 (4 phases × 16 units)
**Genre:** Action game with custom graphics
**Inspired by:** Magazine type-in action games, simple arcade conversions

**Concept:** An action game using user-defined graphics (UDGs) for custom characters — a spaceship, enemies, projectiles, terrain. The player moves and shoots in real time. UDGs replace the built-in character set with 8×8 pixel designs, creating the illusion of sprites. The game pushes BASIC to its performance limits: integer variables for speed, minimal string operations, tight game loops. By the end, the learner understands both what BASIC can achieve and exactly why assembly exists.

**Skills taught:**
- User-defined graphics (USR, BIN for defining 8×8 pixel characters)
- UDG design workflow (graph paper → binary → BASIC code)
- PRINT AT with UDG characters for sprite-like display
- Animation via UDG cycling (multiple frames)
- Speed optimisation in Sinclair BASIC:
  - Integer variables (avoiding floating point)
  - Minimal string operations
  - Short variable names (interpreter lookup speed)
  - GOSUB placement (early in program = faster lookup)
- Real-time action (shooting, dodging, collecting)
- Bullet management (limited pool, recycling)
- Enemy patterns (dive, patrol, chase)
- Scrolling effect via PRINT AT (character-cell scroll)
- Sound via BEEP (pitch and duration for effects)
- High score table with name entry
- The limits of BASIC: frame rate ceiling, why assembly is the next step

**Why last:** This is the BASIC track's peak. UDGs make the game look like something you'd buy — custom graphics, animation, themed visuals. The speed optimisation teaches how interpreters work (why short variable names matter, why GOSUBs early in the program run faster). And hitting BASIC's performance ceiling is the honest conclusion: the learner sees exactly what 500 lines of BASIC can achieve, and understands viscerally why the assembly track exists.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 8 to 4 games. Standardised to 64 units per game (256 total). Each game targets under 500 lines. Previous 8-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 8-game curriculum.
