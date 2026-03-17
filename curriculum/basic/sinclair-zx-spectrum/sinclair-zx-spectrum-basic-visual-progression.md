# Sinclair ZX Spectrum BASIC — Visual Progression

**Companion to:** sinclair-zx-spectrum-basic-curriculum.md (v5.0)

---

## Philosophy

Every game should look and feel like a game from unit 1. The learner's output should never feel like an exercise, a worksheet, or a terminal session. If a 10-year-old wouldn't want to show it to a friend, it's not good enough.

Visual polish tracks genuine skill growth. Each game looks better than the last not because we added decoration, but because the learner can do something they couldn't do before. The visual improvement *is* the learning made visible.

### The Subroutine Trick

Early games use visual subroutines the learner doesn't yet fully understand. A rainbow title screen, a block-pixel font renderer, a temperature bar — these arrive as "type this in and see what happens" before the learner has the vocabulary to explain them. This is deliberate. The subroutines create wonder first and understanding later. Each visual technique is introduced separately: here's what it does, here's how to use it, and eventually, here's how it works.

### The Hardware Arc

The progression isn't "learn commands." It's "take control of the machine."

1. **Use the language** (Foundations, Games 1–6)
2. **Understand the hardware** (Skills, Games 7–10)
3. **Control the hardware** (Projects, Games 11–14)
4. **Own the machine** (Advanced + Capstone, Games 15–16)

By Game 14, the learner is writing machine code snippets, designing custom character sets, and manipulating screen memory directly. By Game 16, they've built an illustrated text adventure with autonomous NPCs and atmospheric lighting — all in BASIC, on a machine from 1982. And they've been writing assembly in DATA statements for three games. The assembly track isn't a scary new world. It's the thing they've been reaching for every time BASIC wasn't fast enough.

---

## The Spectrum's Visual Toolkit

Everything BASIC can do, we teach. The curriculum introduces these capabilities in the order that creates the most wonder:

### Standard Commands (Foundations)

| Capability | Commands | Visual effect |
|-----------|----------|--------------|
| Colour | INK, PAPER, BORDER, BRIGHT | 15 colours (8 base + 7 bright), per-character-cell |
| Sound | BEEP | Pitch and duration, melodies, sound effects |
| Screen position | PRINT AT | Place anything at any row/column |
| Data storage | DATA, READ, RESTORE | Content separated from logic |
| Text effects | FLASH, INVERSE | Attention, emphasis, dramatic reveals |
| Code structure | GO SUB, RETURN | Reusable visual routines |

### Hardware Access (Skills)

| Capability | Technique | Visual effect |
|-----------|-----------|--------------|
| Timing | PEEK 23672/23673 (frames counter) | Consistent game speed, smooth movement |
| Screen reading | ATTR, SCREEN$ | Colour-based collision, reading the display as data |
| XOR drawing | OVER 1 | Move sprites without destroying background |
| Full character set | CHR$ 0–255 | Block graphics, arrows, lines, box drawing |

### Direct Control (Projects)

| Capability | Technique | Visual effect |
|-----------|-----------|--------------|
| Custom fonts | POKE 23606/23607 (CHARS system variable) | Entire character set replaced — the game has its own typeface |
| Fast colour | POKE 22528+ (attribute file) | Colour cycling, screen washes, fade to black, animated backgrounds |
| Pixel graphics | PLOT, DRAW, CIRCLE | Geometry beyond the character grid — curves, diagonals, circles |
| Pixel reading | POINT | Pixel-level collision detection |
| Trigonometry | SIN, COS | Circular motion, rotation, wave patterns |
| Custom sprites | USR, BIN, POKE | 8×8 hand-designed graphics for every game element |
| Animation | UDG frame cycling | Characters that move and change shape |
| Joystick | IN 31 (Kempston) | Arcade-feel input |

### Machine Code Helpers (Advanced + Capstone)

| Capability | Technique | Visual effect |
|-----------|-----------|--------------|
| Fast operations | DATA/POKE/USR | Small routines for scroll, fill, sound — faster than BASIC |
| Direct screen writes | POKE 16384+ | Pixel-level drawing faster than PLOT |
| Port I/O | OUT 254 | Fast border effects (screen shake, strobe) |
| Performance | Short variable names, GO SUB placement, integer tricks | Everything runs faster |

---

## Game-by-Game Progression

### Phase 1: Foundations (Games 1–6, 8 units each)

Each game introduces one visual dimension. By Game 6, the learner's programs look like magazine type-ins.

#### Game 1: Lucky Number — *Colour and sound exist*

Rainbow cascade title screen. Big block-pixel word art ("LUCKY NUMBER") rendered from DATA strings. A temperature bar that shifts from blue through yellow to red to white. Large digit display of the current guess. Border colour changes with distance. Victory celebration with ascending tones and colour flash.

The learner types about 100 lines — many of them are subroutines they'll understand later. What matters now is the result: their first program looks like something from a magazine, not a textbook.

**Visual toolkit gained:** PAPER, INK, BORDER, BRIGHT, BEEP, block-pixel rendering from DATA.

#### Game 2: Bomb Defusal — *The screen reacts in real time*

Big block-pixel digits count down on screen — reusing Game 1's digit renderer in a new context. A burning fuse creeps across the display with a red spark. Four coloured wires wait to be cut. The border shifts from safe green through warning yellow to danger red as time runs out. INKEY$ gives instant input — no waiting for ENTER. Cut the wrong wire and the screen strobes with an explosion.

The screen isn't static text any more — it reacts in real time, moment by moment.

**Visual toolkit gained:** CLS, PRINT AT, PAUSE, BEEP, INKEY$, block-pixel digits in a new context.

#### Game 3: Colour Flood — *I can fill the screen*

Four chunky colour panels (7x8 blocks each) dominate the screen. Simon plays a sequence — each panel flashes with BRIGHT, accompanied by a distinct BEEP tone. The learner watches, then repeats. Sequences grow longer, stored in strings. GO SUB draws and redraws the panels cleanly. The learner experiments with all 15 colours (8 base + BRIGHT) and discovers colour as a system, not a decoration.

The entire screen becomes a canvas. Colour carries meaning — each panel is identified by its colour alone.

**Visual toolkit gained:** FOR/NEXT, BRIGHT, colour as a system, GO SUB for reusable drawing.

#### Game 4: Hot and Cold — *Things move*

A cursor moves continuously across the screen, erase-and-redraw in a game loop. The border pulses through a temperature gradient: cold blue → warm yellow → hot red → white-hot. The learner already knows PRINT AT from Game 2 — now they use it for something that moves. Every frame: erase the old position, draw the new one, check the distance, update the border.

This is the first game with a proper game loop. The screen updates continuously, not in response to a single keypress.

**Visual toolkit gained:** Game loop, continuous movement, erase-and-redraw, border as feedback.

#### Game 5: Word Scramble — *Content comes from data*

Words stored in DATA, read at runtime. Animated letter reveal — characters appear one at a time with ascending BEEP, building anticipation. The learner discovers they can change the game's content by editing DATA lines without touching the code.

**Visual toolkit gained:** DATA/READ for content, character-by-character animation, string display.

#### Game 6: Quiz Master — *Organised, reusable code*

GO SUB draws formatted question cards with coloured borders. Category headers in BRIGHT. Score panels update cleanly. RESTORE cycles through question banks. The visual presentation is the most polished Foundations game — because the code is structured enough to support polish.

**Visual toolkit gained:** GO SUB/RETURN, RESTORE, structured screen layout, reusable drawing routines.

**Cumulative effect after Foundations:** The learner can set colours, make sounds, position anything anywhere with PRINT AT, respond to instant input with INKEY$, run a game loop with continuous movement, store content in DATA, and organise code with GO SUB. Their programs fill the screen with colour and react in real time. They look like real Spectrum software.

---

### Phase 2: Skills (Games 7–10, 16 units each)

The leap from static displays to dynamic worlds. Characters move. Enemies chase. The screen transitions between levels. The learner's games have *life*.

#### Game 7: Treasure Hunt — *PEEK timing and screen effects*

Proper frame-rate timing via PEEK 23672 (the frames counter). Movement is smooth and consistent regardless of what's happening on screen. Screen transitions between levels: attribute wipe (POKE to the attribute file, row by row, fading to black before redrawing). Lives shown as character icons. Coins glitter with FLASH. Hazards pulse with alternating INK.

The game *feels* smooth because it *is* timed. This is the first game where the learner controls *when* things happen, not just *what* happens.

**Visual toolkit gained:** PEEK for timing, attribute-file POKE for transitions, consistent frame rate.

#### Game 8: Minefield — *ATTR collision and colour as data*

ATTR reads the colour of a character cell to determine what's there. The display grid *is* the game state — no separate array needed for what the player can see. Reveal animations ripple outward from each uncovered cell, changing PAPER colours cell by cell with a cascading BEEP. Mine detonation: FLASH, descending tone, border strobe, chain reaction through adjacent cells.

The learner discovers that the screen isn't just output — it's readable data.

**Visual toolkit gained:** ATTR for collision/state, colour as information, cascading visual effects.

#### Game 9: Word Worm — *CHR$ and the full character set*

Words cascade down the screen against a frame built from graphic characters (CHR$ 128–143). Block-graphic borders, box-drawing characters, arrows, and symbols create a polished game frame that looks like a real application. Score display uses block-graphic number frames. Correct completions burst with FLASH and ascending tone. Misses crash with descending tone and colour drain.

The learner discovers the full 256-character set — far more than just letters and numbers.

**Visual toolkit gained:** CHR$ for graphic characters, screen framing with block graphics, visual polish through the full character set.

#### Game 10: Night Patrol — *OVER 1 and flicker-free movement*

OVER 1 (XOR mode) lets the player and enemies move across the maze without destroying it. No more erase-and-redraw flicker. Combined with PEEK timing, movement is the smoothest yet. Multiple enemies move with intent — simple AI that chases the player. Power-ups glow with FLASH. Different maze layouts stored in DATA create distinct-looking levels.

This is the most complex game so far: an arcade experience with AI, levels, and real tension.

**Visual toolkit gained:** OVER 1 for clean movement, AI-driven characters, DATA-driven level design.

**Cumulative effect after Skills:** The learner understands the hardware, not just the language. They know the frames counter, the attribute file, XOR drawing, and the full character set. Their games run at consistent speed with clean movement, atmospheric transitions, and AI opponents.

---

### Phase 3: Projects (Games 11–14, 32 units each)

Custom character sets, pixel graphics, UDGs, and machine code helpers. The learner's output looks like commercial Spectrum software.

#### Game 11: Draughts — *Custom character set*

POKE to the CHARS system variable (23606/23607) installs a bespoke font. Board pieces aren't letters — they're hand-designed 8×8 pixel graphics that replace the standard character set. The entire game has its own typeface: a custom alphabet, custom numbers, custom border characters. Legal moves highlighted with colour. Captured pieces animate through character designs. The board is framed with custom box-drawing characters.

*The game looks nothing like standard Spectrum text.* Everything on screen is designed, not default.

**Visual toolkit gained:** Custom character sets via POKE CHARS, character design as graphic design, visual identity.

#### Game 12: Battleships — *Attribute animation and dramatic reveals*

Direct POKE to the attribute file (22528+) for fast colour effects. Hit: a flash ripple across the ship's cells. Sunk: colour drains cell by cell as the ship fades to black, with a descending tone. The "pass the keyboard" screen uses INVERSE text and colour-cycling BORDER. Radar-style grid display with FLASH for active scanning.

Every hit and miss is a dramatic event. FLASH and INVERSE carry information, not decoration.

**Visual toolkit gained:** Direct attribute POKE for speed, FLASH/INVERSE as information design, dramatic visual events.

#### Game 13: Lattice — *Pixel graphics*

PLOT, DRAW, and CIRCLE create geometry in 256×176 pixel space. Smooth curves. Diagonal lines. Circles. Rotating shapes driven by SIN and COS. POINT-based collision — if the pixel is lit, you hit something. The game exists in pixel space, not character space. Combined with attribute colour for regions, it's visually unlike anything the learner has built before.

This is the moment the Spectrum stops looking blocky.

**Visual toolkit gained:** PLOT/DRAW/CIRCLE, POINT, SIN/COS, pixel-coordinate thinking.

#### Game 14: Blockstorm — *UDGs, animation, and machine code*

USR-defined 8×8 sprites: a custom spaceship, four enemy types, bullets, explosions, power-ups. BIN notation for pixel-row design. Animation by cycling between UDG frame definitions. The game looks *authored* — every visual element is hand-designed.

And the big unlock: small machine code routines stored in DATA, POKEd into RAM, called via RANDOMIZE USR. A fast screen clear. A smooth scroll. A sound effect richer than BEEP. The game runs faster than BASIC should allow.

The learner hits the performance ceiling — and then punches through it. They've written their first assembly, embedded in BASIC. They understand why it's faster. They know what every byte does.

**Visual toolkit gained:** UDGs, BIN, animation via frame cycling, machine code helpers, speed optimisation, the bridge to assembly.

**Cumulative effect after Projects:** Custom visuals (character sets, UDGs, pixel graphics), hardware-level effects (attribute manipulation, machine code), and designed visual identity. The learner's games look like commercial Spectrum software — because they're using the same techniques commercial developers used.

---

### Phase 4: Advanced + Capstone (Games 15–16)

No new visual tricks. Instead, the learner uses everything they know to create atmosphere and living worlds.

#### Game 15: Dungeons of Dorin — *Procedural surprise*

Procedural generation means the dungeon is different every play. Room rendering uses the custom character set: wall tiles, door tiles, treasure tiles, monster tiles — all bespoke. Stats panels with custom frames. Combat has visual weight: screen shake via rapid OUT 254 (border port), health bars draining through attribute colour (POKE), damage numbers. Deeper floors get darker PAPER, lower BRIGHT — the dungeon *feels* dangerous.

The wonder here isn't a visual technique. It's the moment the learner sees something on screen that *they didn't design*. The code generated it. Procedural content is the machine being creative.

Machine code helpers handle fast room redraws and richer sound effects. SAVE/LOAD preserves the world state to tape. The learner's game has persistence — it outlasts a single session.

#### Game 16: The Cursed Manor — *A living, illustrated world*

PLOT/DRAW illustrations for each room — real pictures, not character art or UDGs. A custom character set for the text interface: gothic, manor-appropriate, atmospheric. The command parser processes natural language. NPCs move autonomously through rooms the learner illustrated.

Attribute-based mood: frozen rooms are blue and cyan. As the curse lifts, rooms warm through yellow to white. The final moment: the curse breaks and colour floods back room by room — a cascading attribute POKE that transforms the manor from cold to alive.

The learner who typed `10 PRINT "Hello"` in Game 1 has built a graphical adventure with illustrated rooms, autonomous characters, atmospheric lighting, a natural language parser, and hand-assembled machine code routines. Some learners will stay here and build more adventures. Others will look at those DATA/POKE/USR routines and think: what if I wrote the whole thing in assembly?

Both paths lead somewhere worth going.

---

## Visual Arc Summary

```
FOUNDATIONS — "It looks like a game"
  Game  1  Lucky Number ......... Colour + sound + block graphics
  Game  2  Bomb Defusal ......... Real-time countdown, INKEY$, block digits
  Game  3  Colour Flood ......... Chunky colour panels, BRIGHT, GO SUB
  Game  4  Hot and Cold ......... Game loop, continuous movement
  Game  5  Word Scramble ........ Data-driven content
  Game  6  Quiz Master .......... Structured, reusable presentation

SKILLS — "It moves, it thinks, it fights back"
  Game  7  Treasure Hunt ........ PEEK timing, smooth movement, screen transitions
  Game  8  Minefield ............ ATTR collision, colour as data, cascading reveals
  Game  9  Word Worm ............ CHR$ graphic characters, polished screen framing
  Game 10  Night Patrol ......... OVER 1 flicker-free movement, AI, level design

PROJECTS — "This is real software"
  Game 11  Draughts ............. Custom character set (POKE CHARS)
  Game 12  Battleships .......... Direct attribute POKE, dramatic reveals
  Game 13  Lattice .............. PLOT/DRAW/CIRCLE pixel graphics
  Game 14  Blockstorm ........... UDGs, animation, machine code helpers

ADVANCED + CAPSTONE — "I own the machine"
  Game 15  Dungeons of Dorin .... Procedural generation, atmosphere, persistence
  Game 16  The Cursed Manor ..... Illustrated rooms, autonomous NPCs, a living world
```

---

## Relationship to the Assembly Track

The BASIC and assembly tracks are independent — neither is a prerequisite for the other. But a learner who completes the BASIC track arrives at assembly with real advantages:

- **Hardware knowledge**: they know where screen memory lives (16384), how attributes work (22528+), what the frames counter is (23672), and how port I/O works (IN/OUT 254). The assembly track can build on this rather than teaching it from scratch.
- **Machine code exposure**: Games 14–16 include hand-assembled routines in DATA statements. The learner has already written bytes that the Z80 executes. Assembly formalises what they've been doing by hand.
- **Performance intuition**: they've hit BASIC's ceiling and understand *why* it's slow (interpreter overhead, variable lookup, floating point). Assembly isn't abstract — it's the solution to a problem they've felt.

The assembly track should acknowledge this: "If you've come from the BASIC track, you already know the Spectrum's hardware. We'll move quickly through the ground you've covered and focus on what's new: registers, addressing modes, and writing code that runs at full speed."

Learners who start directly with assembly get the same hardware introduction, just from a different angle. Neither path is lesser.

---

## Changelog

- **v1.0 (2026-03-16):** Initial visual progression document for v5.0 curriculum.
