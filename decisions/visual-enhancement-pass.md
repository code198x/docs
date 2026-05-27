# Decision: Visual Enhancement Pass — Spectrum BASIC Games 1-15

**Status:** Active
**Date:** 2026-05-27

## The decision

Every Spectrum BASIC game (1-15) gets a visual enhancement pass using the machine's full BASIC visual vocabulary — PRINT AT, INVERSE, BRIGHT, FLASH, block graphics (CHR$ 128-143), PLOT, DRAW, CIRCLE, and UDGs. Two games (Hi-Lo, Touchdown) gain one new unit each for substantial visual systems. All other games gain visual quality within their existing unit structure.

The visual pass does not change game logic, teaching progression, or the dual-subject curriculum model. It changes what the output looks like.

## Why

Two independent reviews (Claude + Codex) and a screenshot capture pass revealed that the programs' visual output — particularly games 1-3 — looked like terminal text, not Spectrum programs. The Usborne bar requires output that a learner wants to show someone. Dark themes, illustrated title screens, UDG sprites, DRAW shapes, and animation moments are all standard in period Spectrum BASIC programs — including the examples in the Spectrum manual itself.

## Principle

Use the Spectrum's visual vocabulary (PRINT AT, INVERSE, BRIGHT, FLASH, block graphics, PLOT/DRAW) from the start — as recipes before they're formally taught, as reinforcement after. No new game logic. No new teaching units. The same programs, looking like they belong on the machine.

Commands are available as recipes from any unit; formally taught where noted.

| Command | First recipe use | Formally taught |
|---------|-----------------|-----------------|
| BORDER, PAPER, INK | Game 1 unit 2 | Game 1 unit 8 |
| PRINT AT | Game 1 unit 7 (title) | Game 5 unit 5 |
| BRIGHT | Game 1 unit 7 | Game 6 unit 3 |
| INVERSE | Game 2 unit 1 | (never — recipe only) |
| FLASH | Game 3 unit 6 | (never — recipe only) |
| PLOT, DRAW | Game 4 unit 4 | Game 4 unit 4 |
| Block graphics (CHR$) | Game 3 unit 8 | (never — recipe only) |
| FOR/NEXT drawing | Game 4 unit 4 | Game 5 unit 2 |
| GO SUB | Game 6 unit 2 | Game 6 unit 2 |
| UDG (POKE USR) | Game 7 "The Cards" | (recipe — "8 numbers = 8 rows of pixels") |

## Three layers of visual improvement

### Layer 1: Theme and colour (all games)
Dark theme from the start. INVERSE title bars. BRIGHT emphasis. Colour palettes per game. This is the baseline — one or two lines per unit, no new concepts.

### Layer 2: Block graphics and screen composition (all games)
CHR$ 128-143 for dividers, frames, borders. Consistent layout zones: INVERSE header (row 0), play area (rows 2-18), status/input (rows 20-21). Replaces ad-hoc text scrolling with designed screens.

### Layer 3: UDGs and DRAW (games 4+)
Custom 8×8 pixel characters for game-specific sprites and symbols. DRAW for vector shapes (grid lines, terrain). This is where the output stops looking like text and starts looking like a Spectrum game.

### Layer 4: Title screen illustrations and animation moments

**Title screen DRAW art.** Each game gets a simple illustration on its title screen — 5-10 DRAW/PLOT/CIRCLE commands, not detailed art. The illustration anchors the game's identity visually. Examples:

| Game | Title illustration | Commands |
|------|-------------------|----------|
| 1 Story Builder | Quill/pen — angled line with a flourish | 3-4 DRAW |
| 2 Lucky Number | Question mark — CIRCLE head + DRAW curve + PLOT dot | CIRCLE + 2 DRAW + PLOT |
| 3 Oracle Stone | Crystal ball — CIRCLE on a DRAW base | CIRCLE + 3 DRAW |
| 4 Reflex | Lightning bolt — zigzag DRAW | 5 DRAW |
| 5 Dice Roller | Die face — DRAW rectangle + 6 PLOT dots | DRAW 4 + PLOT 6 |
| 6 Bright Spark | (Panels are the illustration — no need) | — |
| 7 Hi-Lo | (Cards are the illustration — no need) | — |
| 8 Touchdown | Rocket silhouette — DRAW triangle + legs | 6 DRAW |
| 9 Cipher | Lock/keyhole — DRAW rectangle + CIRCLE | DRAW 4 + CIRCLE |
| 10 Quiz Master | Mortarboard hat — DRAW rectangle + diamond top | 5 DRAW |
| 11 Locksmith | Padlock — DRAW body + CIRCLE shackle | DRAW 3 + CIRCLE |
| 12 Sonar | Radar circles — 3 concentric CIRCLE + DRAW sweep line | 3 CIRCLE + DRAW |
| 13 Three in a Row | (Board is the illustration — no need) | — |
| 14 The Caverns | Torch flame — DRAW handle + flame outline in INK 6 | 6 DRAW |
| 15 Yearfall | Castle silhouette — DRAW rectangles + triangles for towers | 8 DRAW |

~5-10 extra lines per game title screen. The learner runs the program and sees an image, not just text.

**Animation moments.** Small, specific animations at key points — not continuous animation, just a beat of visual life:

| Game | Moment | Animation | Lines |
|------|--------|-----------|-------|
| 3 Oracle Stone | Pondering | Dots appear one by one (`. . .`) with PAUSE between each, while BEEP descends | ~3 |
| 8 Touchdown | Crash | Explosion UDGs appear one at a time at random offsets from landing point, each with a BEEP | ~4 |
| 8 Touchdown | Thrust | Exhaust UDG appears below lander when SPACE held, disappears when released (already proposed — confirmed) | ~2 |
| 9 Cipher | Letter found | BRIGHT 1 flash on the revealed letter for 10 frames, then BRIGHT 0 | ~2 |
| 12 Sonar | Probe | BORDER flashes the distance colour for 5 frames, then resets — a "ping" effect | ~2 |
| 15 Yearfall | Starvation | Brief BORDER 2 (red) flash when people die, like an alarm | ~1 |

**UDG budget** (21 slots available, shared per-game — each game defines its own at startup):

| Game | UDGs | Characters |
|------|------|-----------|
| 7 Hi-Lo | 4 | ♠ ♥ ♦ ♣ card suits |
| 8 Touchdown | 3 | Lander, exhaust flame, explosion |
| 9 Cipher | 1 | Heart (lives) |
| 11 Locksmith | 2 | Bull peg, cow peg |
| **Total** | **10 of 21** | |

**Three in a Row uses DRAW instead of UDGs.** X is two crossed DRAW lines; O is a CIRCLE. Each piece fills a full grid cell (~24×24 pixels) — much larger and bolder than an 8×8 UDG character. The grid itself is also DRAW lines. At most 9 pieces per game, so the speed cost is trivial.

**DRAW vs UDG rule of thumb:** DRAW for large symbols drawn rarely (board game pieces, grid lines, terrain, title illustrations). UDGs for small symbols that move or repeat frequently (lander sprite, lives, pegs, card suits).

Each UDG costs 8 lines of DATA + a FOR/READ/POKE loop (~3 lines shared). The pixel grid diagrams in the prose connect code to visual output: "Each number is a row of pixels. Eight rows make a character."

---

## Volume 1 — First Programs

### Game 1: Story Builder (8 units)

**Current:** Grey screen → black + cyan at unit 8.
**Proposed:**
- **Unit 2 onwards:** Dark theme (`BORDER 0: PAPER 0: INK 7: CLS`). One-line recipe. Prose: "This sets the screen to black with white text. We'll explore what each part does in unit 8."
- **Unit 7 (title):** Centre with PRINT AT. BRIGHT 1 on the title line. DRAW a quill/pen illustration — an angled line with a small flourish at the top. ~4 DRAW commands. The title screen has an image.
- **Unit 8 (polish):** Already has colours. Add block-graphic divider between title and questions: a row of `CHR$ 131` (lower-half block) as a visual separator.

**Code cost:** ~8 extra lines across 7 units. No new game logic.

### Game 2: Lucky Number (10 units)

**Current:** Grey screen, border colour feedback from unit 7.
**Proposed:**
- **Unit 1 onwards:** Dark theme. INVERSE title bar: `INVERSE 1: PRINT AT 2, 0; "  *** LUCKY NUMBER ***          ": INVERSE 0`. The full-width white bar immediately looks professional.
- **Unit 1 (title):** DRAW question mark — `CIRCLE 128, 110, 8` for the head, a DRAW curve below, PLOT dot at the bottom. ~4 commands. The title screen asks a visual question.
- **Unit 3 onwards (INPUT):** Centre the guess prompt with PRINT AT instead of scrolling text.
- **Unit 7 (border colours):** Already good — border feedback is the game's visual signature. No change.
- **Unit 10 (ratings):** Ratings text centred with PRINT AT, BRIGHT 1 on the rating name.

**Code cost:** ~10 extra lines. Title bar + question mark illustration.

### Game 3: Oracle Stone (9 units)

**Current:** Grey until unit 9 (blue chamber). Equals-sign framing on the reveal.
**Proposed:**
- **Unit 1 onwards:** Blue theme (`BORDER 1: PAPER 1: INK 7: CLS`). The mystical atmosphere starts immediately.
- **Unit 5 (ceremony):** Pondering dots — `FOR i = 1 TO 3: PRINT ".  ";: BEEP 0.3, 20-i*5: PAUSE 25: NEXT i`. Three dots appear one by one with descending tones. The learner watches the Oracle "think." ~2 lines replace the current block of BEEP/PAUSE.
- **Unit 6 (reveal):** Add `FLASH 1` on the Oracle's answer line. The answer blinks — mystical and arresting. One command.
- **Unit 8 (framing):** Replace equals-sign decoration with block graphics: rows of `CHR$ 143` (solid blocks) in INK 5 (cyan) above and below the answer — a jewelled frame.
- **Title screen:** DRAW crystal ball — `CIRCLE 128, 100, 20` with a `DRAW` base beneath it. The Oracle has a face before you ask the question. ~5 lines.

**Code cost:** ~10 extra lines. The blue theme + pondering animation + flashing answer + crystal ball title transforms the game's presence.

### Game 4: Reflex (9 units)

**Current:** Black screen, PLOT/DRAW telegraph bar, red PAPER flash. Already strong.
**Proposed:**
- **Unit 6 (title):** BRIGHT 1 on title. PRINT AT centred.
- **Unit 8 (bar outline):** DRAW a proper rectangle around the bar area — `PLOT 26, 85: DRAW 204, 0: DRAW 0, 6: DRAW -204, 0: DRAW 0, -6`. The bar fills inside a drawn frame, like a meter. This reinforces DRAW (taught 4 units ago) in a practical context.
- **Unit 9 (sound + rating):** BRIGHT on the rating text.

**Code cost:** ~5 extra lines. The DRAW frame turns the telegraph line into a proper meter.

### Game 5: Dice Roller (8 units)

**Current:** Black screen, PRINT AT dashboard, asterisk bar charts in 6 colours.
**Proposed:**
- **Unit 7 (bar chart):** Replace `PRINT "*"` bars with `PRINT CHR$ 143` (solid block character). The bars become solid coloured blocks instead of asterisks — denser, chunkier, more like a real data visualisation. Same code structure, one character change.
- **Unit 6 (title):** INVERSE title bar across the top, centred with PRINT AT.
- **Unit 8 (colour):** The coloured solid blocks look significantly better than coloured asterisks. No code change beyond the CHR$ swap.

**Code cost:** ~2 extra lines (title bar). The CHR$ swap is a character change, not new code.

### Game 6: Bright Spark (10 units)

**Current:** Four coloured panels with BRIGHT flash. Already the strongest visual in V1.
**Proposed:**
- **Minimal changes.** The game already looks striking.
- **Unit 8 (title):** INVERSE score display at the top. BRIGHT 1 on the title.
- **Unit 9 (ratings):** BRIGHT on the rating text.

**Code cost:** ~2 extra lines. Don't fix what works.

### Game 7: Hi-Lo (10 → 11 units)

**Current:** White text dashboard — Number, Streak, Best. Plain.
**Proposed — playing cards with suits:**

The range is 1-13 and the prose already says "like a suit of playing cards." Show actual cards.

**Card display:**
- Each card is a PAPER 7 (white) rectangle drawn with PRINT AT (7 rows × 9 columns).
- Value at top-left and bottom-right corners: A, 2-9, 10, J, Q, K.
- Suit symbol in the centre: ♠ ♥ ♦ ♣ as UDGs, printed in the suit's colour.

**Suit UDGs** — four 8×8 pixel characters defined with DATA/READ/POKE at game start:

```
 ♥ heart          ♦ diamond        ♣ club           ♠ spade
 . . . . . . . .  . . . # . . . .  . # . . . # . .  . . . # . . . .
 . # # . # # . .  . . # # # . . .  # # # . # # # .  . . # # # . . .
 # # # # # # # .  . # # # # # . .  # # # # # # # .  . # # # # # . .
 # # # # # # # .  # # # # # # # .  . # # # # # . .  # # # # # # # .
 # # # # # # # .  . # # # # # . .  . . # # # . . .  # # # # # # # .
 . # # # # # . .  . . # # # . . .  . . . # . . . .  # # # # # # # .
 . . # # # . . .  . . . # . . . .  . . # # # . . .  . # # # # # . .
 . . . # . . . .  . . . . . . . .  . . . . . . . .  . . . # . . . .
```

Definition code (~12 lines using DATA + nested FOR/READ/POKE loop). Each suit maps to a UDG character (CHR$ 144-147). Hearts and diamonds print in INK 2 (red); spades and clubs print in INK 0 (black) against the white card.

**Card layout on screen:**

```
 *** HI-LO ***               Streak: 3  Best: 5

   ┌───────┐         ┌───────┐
   │ 7     │         │       │
   │   ♠   │         │  ???  │
   │     7 │         │       │
   └───────┘         └───────┘

   Higher or lower (H/L)?
```

Two card positions: current (revealed with value + suit) and next (face-down). Player guesses H or L, next card flips to reveal. Old card slides to the "current" position. Each card gets a random suit — the suit doesn't affect gameplay but makes each card feel like a real draw.

**Unit changes:**
- **Units 1-4:** Existing game logic, no visual change (numbers display as before — the card system arrives as its own unit).
- **New unit (inserted after current unit 5 "The Display"):** "The Cards" — replaces the number display with card visuals. Defines the four suit UDGs, writes the card-drawing subroutine, and replaces the inline number display. This is the unit's sole focus: turning data into a visual representation. The prose connects pixels to code: "Each number in the DATA is a row of 8 pixels. Eight rows make a character. You just taught the Spectrum what a heart looks like."
- **Unit 5 (display):** INVERSE header bar with "*** HI-LO ***" + streak + best.
- **Unit 9 (title):** Title screen with two face-down cards as decoration.

**Code cost:** ~30 extra lines (UDG definitions + card subroutine + suit assignment + face conversion). Uses GO SUB (taught in Game 6), PRINT AT (Game 5), PAPER/INK (recipe), DATA/READ (taught in Game 5 for dice counts, formally in Game 9 but used here as recipe for pixel data), POKE (recipe — "type this to define the character").

**Teaching value:** This is the first time the learner defines a custom graphic. The pixel grid → DATA → POKE → visible character pipeline is a powerful moment. It previews UDGs without requiring formal understanding of the Spectrum's character memory layout — the recipe works, the explanation comes later (or in the assembly track). The dual-subject design concept for this unit: **Representation** — the same number (7) shown as text vs. shown as a card. The display doesn't change the data; it changes the experience.

### Game 8: Touchdown (13 → 14 units)

**Current:** Text dashboard, "V" lander character, dash ground, asterisk fuel bar, border colours.
**Proposed — graphical lander:**

Three UDGs defined at game start:

```
 Lander             Exhaust flame       Explosion
 . . # # . . . .   . . . . . . . .     . # . . . # . .
 . . # # . . . .   . . . # . . . .     . . # . # . . .
 . # # # # . . .   . . # . # . . .     # . . . . . # .
 . # # # # . . .   . . # . # . . .     . . . . . . . .
 # # # # # # . .   . # . . . # . .     # . . . . . # .
 # # # # # # . .   . # . . . # . .     . . # . # . . .
 # . # # . # . .   # . . . . . # .     . # . . . # . .
 . . # # . . . .   . . . # . . . .     . . . . . . . .
```

**Visual upgrades across units:**
- **Unit 1 (falling):** Random PLOT stars at game start — `FOR i = 1 TO 15: PLOT INT(RND*256), INT(RND*100)+60: NEXT i`. Five lines of code transforms black screen into space.
- **Unit 4 (dashboard):** INVERSE header bar spanning full width. `ALT: nn    SPD: nn    FUEL: nn` as white-on-black instrument panel.
- **Unit 6 (lander):** UDG lander (CHR$ 144) replaces `"V"`. Moved with PRINT AT — print space at old position, print UDG at new position. Same erase-then-draw logic, better sprite.
- **Unit 6 (thrust):** When SPACE is held, print the exhaust UDG (CHR$ 145) one row below the lander. When released, erase it. The player sees the thruster fire.
- **Unit 8 (ground):** DRAW terrain instead of dashes — `PLOT 0, 14: DRAW 255, 0` for a flat landing surface, or a simple terrain profile with two or three DRAW segments. INK 4 (green).
- **Unit 9 (fuel bar):** PLOT-based pixel bar instead of asterisks. Each unit of fuel is one pixel. The bar depletes smoothly. Uses PLOT (taught in Game 4).
- **New unit after unit 12 ("The View"):** Pulls the three UDG definitions and the visual setup (stars, terrain) into one focused unit. Design concept: **Polish** — the same game, visually transformed. "Nothing about the physics changed. Everything about how it feels changed."
- **Unit 11-12 (outcomes):** CRASH shows the explosion UDG (CHR$ 146) scattered around the landing point — 3-4 explosion characters at random nearby positions. PERFECT LANDING shows the lander on the ground with no exhaust, steady. BRIGHT on outcome text.

**Code cost:** ~35 extra lines across relevant units. The V1 capstone goes from "descending letter" to "rocket landing in space."

---

## Volume 2 — Patterns of State

### Game 9: Cipher (9 units)

**Current:** Black screen, underscore word display, asterisk lives, text layout.
**Proposed:**

One UDG — a heart for lives:

```
 Heart
 . . . . . . . .
 . # # . # # . .
 # # # # # # # .
 # # # # # # # .
 # # # # # # # .
 . # # # # # . .
 . . # # # . . .
 . . . # . . . .
```

- **Unit 1 (word display):** INVERSE header bar with "*** CIPHER ***" + win/loss tally.
- **Unit 2 (lives):** UDG heart (CHR$ 144) in INK 2 (red) for each remaining life. Seven hearts → six → five as lives are lost. Lives feel like lives, not punctuation.
- **Unit 5 (display):** Wider letter spacing in the word display. Each underscore/letter printed in a 2-character-wide cell using PRINT AT, centred on screen. DRAW a horizontal line below the word display to frame the play area.
- **Unit 9 (title):** BRIGHT title, FLASH on "Press any key."

**Code cost:** ~10 extra lines. The UDG hearts and DRAW frame are the key upgrades.

### Game 10: Quiz Master (10 units)

**Current:** Category colour banner via PAPER. Already has colour identity per category.
**Proposed:**
- **Unit 6 (question card):** INVERSE on the category name for a solid colour header bar. Block-graphic border around the question area — frame it like a card.
- **Unit 8 (ratings):** BRIGHT on the rating title. FLASH on "Quiz Master!" (top rating).
- **Unit 9 (breakdown):** Block-graphic bar chart for per-category scores (like Dice Roller) instead of just numbers.

**Code cost:** ~8 extra lines. The category bars in the breakdown would be a nice callback to Game 5.

### Game 11: Locksmith (9 units)

**Current:** Black screen, guess history as text columns with coloured bull/cow counts.
**Proposed:**

Two UDGs — bull peg and cow peg:

```
 Bull (filled)       Cow (ring)
 . . # # # # . .     . . # # # # . .
 . # # # # # # .     . # # # # # # .
 # # # # # # # #     # # . . . . # #
 # # # # # # # #     # # . . . . # #
 # # # # # # # #     # # . . . . # #
 # # # # # # # #     # # . . . . # #
 . # # # # # # .     . # # # # # # .
 . . # # # # . .     . . # # # # . .
```

- **Unit 1 (secret code):** INVERSE header bar.
- **Unit 3-4 (bulls/cows):** UDG bull peg (CHR$ 144) in INK 2 (red) for each bull. UDG cow peg (CHR$ 145) in INK 7 (white) for each cow. Visual Mastermind pegs instead of numbers. Each guess row shows: the 4-digit guess, then peg symbols.
- **Unit 6 (history):** DRAW a vertical separator line between the guess column and the peg column. Frame the history area with DRAW rectangle.
- **Unit 8 (title):** Show four block-graphic `?` characters in coloured cells as decoration — the hidden code visualised.

**Code cost:** ~12 extra lines. The coloured pegs and DRAW framing transform it from a text log to a Mastermind board.

### Game 12: Sonar (10 units)

**Current:** 8×8 text grid with dots, asterisks, and coloured distance numbers. Already game-like.
**Proposed:**
- **Unit 1 (grid):** DRAW grid lines — horizontal and vertical pixel lines creating an 8×8 board. Each cell is 3 characters wide × 2 rows tall. The grid uses DRAW in a FOR loop: `FOR i = 0 TO 8: PLOT x, y: DRAW grid_width, 0: NEXT i` (horizontal), same pattern for verticals. This reinforces DRAW (taught in Game 4) in a structured context. The grid looks like a proper board game.
- **Unit 6 (colour):** Already strong. The heat-map colours pop better against the drawn grid lines.
- **Unit 9 (title):** INVERSE header. DRAW a simple sonar "sweep" on the title screen — a quarter-circle arc: `PLOT 128, 88: DRAW 0, 40: PLOT 128, 88: DRAW 28, 28: PLOT 128, 88: DRAW 40, 0`. Three radial lines suggesting a radar sweep.

**Code cost:** ~12 extra lines. The DRAW grid is the main improvement — transforms dots-in-a-row into a board.

### Game 13: Three in a Row (11 units)

**Current:** 3×3 grid with text dividers (hyphens and pipes), coloured X and O.
**Proposed:**

Two UDGs — bold X and O pieces:

```
 X piece              O piece
 # # . . . . # #      . . # # # # . .
 . # # . . # # .      . # # . . # # .
 . . # # # # . .      # # . . . . # #
 . . . # # . . .      # # . . . . # #
 . . # # # # . .      # # . . . . # #
 . # # . . # # .      . # # . . # # .
 # # . . . . # #      . . # # # # . .
 . . . . . . . .      . . . . . . . .
```

- **Unit 1 (board):** DRAW grid lines — two horizontal and two vertical pixel lines creating the 3×3 board. Each cell is ~8 characters wide × ~5 rows tall, centred on screen. The board dominates the play area. `PLOT 80, 40: DRAW 0, 120` etc. Clean pixel-perfect grid.
- **Unit 2 (player's move):** UDG X piece (CHR$ 144) in INK 5 (cyan). Printed 2×2 in each cell (four UDG characters forming a large, bold X). Each cell feels substantial.
- **Unit 4 (computer moves):** UDG O piece (CHR$ 145) in INK 2 (red). Same 2×2 layout. The visual contrast between cyan X and red O is immediate.
- **Unit 10 (title):** Show a sample board with a few X's and O's as decoration. BRIGHT title.
- **Unit 11 (record):** INVERSE score display: W/L/D across the top.

**Code cost:** ~20 extra lines (UDG definitions + DRAW grid subroutine + 2×2 piece printing). The DRAW grid + UDG pieces turn a text exercise into a board game.

### Game 14: The Caverns (11 units)

**Current:** Blue PAPER, white text, colour-coded sensory clues. Text adventure.
**Proposed:**
- **Minimal changes.** The darkness is the point — this game is deliberately text-based. The player imagines the caverns; the screen gives clues, not pictures.
- **Unit 1 (room):** INVERSE header bar with room number: `INVERSE 1: PRINT AT 0, 0; " Room 1                        ": INVERSE 0`. Clean navigation header.
- **Unit 4 (draft):** BRIGHT 1 on sensory clue text to make warnings more visible.
- **Unit 10 (atmosphere):** Already has the blue theme. Add a subtle compass rose using block graphics in the corner — four `CHR$` characters showing N/S/E/W with available exits highlighted.

**Code cost:** ~6 extra lines. Restraint is right here — the game's visual identity is *absence*.

### Game 15: Yearfall (10 units)

**Current:** Black screen, text dashboard with year/population/grain/land, colour-coded reports.
**Proposed:**
- **Title screen:** DRAW castle silhouette — two towers (DRAW rectangles with triangle roofs) connected by a wall (horizontal line), centred on screen. Simple but immediately says "kingdom." ~8 DRAW commands.
- **Unit 1 (kingdom):** INVERSE header bar with "*** YEARFALL ***  Year: 1". Block-graphic divider between the status display and the input area.
- **Unit 2 (feeding):** Visual population bar — a row of `CHR$ 143` blocks in INK 4 (green) proportional to population. The bar shrinks when people starve, grows when births happen. The player SEES the population, not just reads a number. Starvation triggers a brief BORDER 2 (red) flash — like an alarm. ~1 extra line for the flash.
- **Unit 7 (year-end report):** Block-graphic bars for the report metrics. Harvest as a green bar, starvation as a red bar, births as a cyan bar. Like a mini Dice Roller visualisation per year.
- **Unit 9 (atmosphere):** BRIGHT on the title. Austere palette (already there).

**Code cost:** ~20 extra lines. The castle silhouette + population bar + starvation alarm turn a spreadsheet into a kingdom.

---

## Summary

| Game | Units | UDGs | Current | Proposed | Key upgrades | Extra lines |
|------|-------|------|---------|----------|-------------|-------------|
| 1 Story Builder | 8 | — | Text on grey | Dark theme, BRIGHT title, DRAW quill | Theme + title art | ~8 |
| 2 Lucky Number | 10 | — | Text + border | INVERSE bar, DRAW question mark | Title bar + illustration | ~10 |
| 3 Oracle Stone | 9 | — | Grey → blue | Blue theme, pondering dots, FLASH answer, DRAW crystal ball | Theme + animation + title art | ~10 |
| 4 Reflex | 9 | — | PLOT bar | DRAW meter frame, DRAW lightning bolt title | DRAW shapes | ~8 |
| 5 Dice Roller | 8 | — | Asterisk bars | CHR$ 143 block bars, DRAW die face title | Block bars + title art | ~8 |
| 6 Bright Spark | 10 | — | Four panels | INVERSE score (already strong) | Light touch | ~2 |
| 7 Hi-Lo | **11** (+1) | 4 | Text numbers | **Playing cards with suit UDGs** | Card + suit system | ~30 |
| 8 Touchdown | **14** (+1) | 3 | Text + "V" | **UDG lander/exhaust/explosion, PLOT stars, DRAW terrain, pixel fuel** | Full graphical upgrade | ~35 |
| 9 Cipher | 9 | 1 | Text puzzle | UDG hearts, BRIGHT reveal flash, DRAW lock title | Hearts + animation + title art | ~12 |
| 10 Quiz Master | 10 | — | Colour banners | Framed card, DRAW mortarboard title | Question frame + title art | ~12 |
| 11 Locksmith | 9 | 2 | Text log | **UDG Mastermind pegs**, DRAW padlock title | Pegs + title art | ~15 |
| 12 Sonar | 10 | — | Dot grid | **DRAW pixel grid**, CIRCLE radar title, probe ping | Drawn board + animation | ~15 |
| 13 Three in a Row | 11 | 2 | Text grid | **UDG X/O 2×2, DRAW pixel grid** | Board game | ~20 |
| 14 The Caverns | 11 | — | Blue text | INVERSE header, DRAW torch title | Restraint + title art | ~8 |
| 15 Yearfall | 10 | — | Text dashboard | Population bar, starvation flash, **DRAW castle title** | Castle + bars + animation | ~20 |

**Total: ~213 extra lines across 15 games. 12 UDGs. Two new units. Title screen illustrations for 12 of 15 games (3 already have strong visual identity). Animation moments for 5 games.**

Four layers of visual improvement:
1. **Theme and colour** — dark themes, INVERSE bars, colour palettes (all games)
2. **Block graphics and composition** — CHR$ dividers, layout zones (all games)
3. **UDGs and DRAW** — custom sprites, vector shapes, pixel grids (games 4+)
4. **Title illustrations and animation** — DRAW art on title screens, brief animation beats (all games)

**What changes:** the visual output. Every game has a title illustration, a designed screen layout, and uses the Spectrum's full visual vocabulary.
**What doesn't change:** the game logic, the teaching progression, the unit structure (except 2 new units), the prose voice.

The visual output goes from "programs that happen to run on a Spectrum" to "programs that could only be a Spectrum game."

## Drift triggers

If you find yourself doing any of the following, stop and re-consult this decision:

- **Writing a new game or unit with grey-on-grey default colours.** Every program starts with a dark theme from its first CLS.
- **Using `PRINT "*"` for bars, lives, or indicators.** Use `CHR$ 143` (solid block) or a UDG. Asterisks are punctuation, not graphics.
- **Adding a title screen without an illustration.** Every game gets a DRAW illustration unless it already has a strong visual (Bright Spark panels, Hi-Lo cards).
- **Introducing a visual command formally before the learner needs it for game logic.** Visual commands arrive as recipes ("type this") and get taught formally when the curriculum reaches them. Use-before-understand is the model.
- **Adding visual complexity that the learner can't modify.** Every visual recipe should be something the learner can change — a different colour number, a different DRAW shape, a different UDG pattern. If it's a black box, it shouldn't be there.

## Anchored in

- [spectrum-basic-32-games.md](spectrum-basic-32-games.md) — game lineup (unit counts for Hi-Lo and Touchdown updated)
- [october-2026-launch-spec.md](october-2026-launch-spec.md) — V1 quality bar
- [commercial-bar-revamp.md](commercial-bar-revamp.md) — Usborne 1984 bar definition
- Game briefs at `platforms/sinclair-zx-spectrum/games/*/brief.md` — updated to reflect visual enhancements
