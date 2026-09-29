# Spectrum BASIC games: polish audit against the 1982 to 1983 bar

Read-only audit, 2026-09-29, against the bar in [PROJECT.md](../../PROJECT.md#what-makes-a-finished-game). It reads code; nothing was played, and period comparisons are not sourced here. Evidence is the final program each course ends with, read in full. Paths are relative to `Code198x/code-samples/sinclair-zx-spectrum/basic/`. Endpoints were confirmed from the last unit in each `units/…/<game>.yaml` and the last `CodeFromFile` in that unit's MDX.

Key: ✓ present, ~ partial, ✗ missing, – genre does not call for it. For item 9, ✓ means no visible rough edge found, ~ minor, ✗ a player would notice.

## Headline

1. **Sound is the biggest gap.** 13 of 15 games contain no `BEEP` at all. Only Bright Spark (panel tones, failure buzz) and Touchdown (landing and crash only) make any sound.
2. **Progression is thin.** Most action games are one screen, one speed and one attempt: Volley, Touchdown, Tail Chase, Brick Bash, Drift, Quickstep and Night Patrol have no levels, speed-up or lives. The Caverns is fully deterministic, so every replay is the same game.
3. **No game keeps a best result**, apart from the session tallies in Three in a Row (W/L/D) and Cipher (won/lost). Five games already count a `steps` variable that is never displayed (Tail Chase, Brick Bash, Drift, Quickstep, Night Patrol): the hook for a best score is there and unused.
4. **Title screens are text only.** Every game has one, and all share one template: the name in one INK colour on the same line size as the instructions, then "S starts. Q quits." There is no large title, logo, attract mode or demo. Bright Spark and Volley do not even colour the name.
5. **Game over and replay are solid everywhere.** Every game offers R to replay without reloading. This item passes across the board.
6. **No loading screens.** No endpoint uses `SCREEN$`.

## Per game

### Bright Spark
`bright-spark/opening/unit-07/steps/step-02.bas` (122 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ~ | "BRIGHT SPARK" in plain white at 0,0 (l.50, 2140); no styling |
| 2 | Instructions | ✓ | l.2000–2060 |
| 3 | Sound | ✓ | per-panel note (920), fail buzz (1810); no success sound at 1850 |
| 4 | Feedback | ✓ | "Rounds completed", WATCH/YOUR TURN, "Challenge complete." |
| 5 | Progression | ✓ | sequence grows each round to cap 16 (287, 1170) |
| 6 | Replay | ✓ | r replay (2250, 2270) |
| 7 | Best | ✗ | rounds shown, never kept |
| 8 | Colour | ~ | four coloured panels flashing BRIGHT (670–690); no UDGs |
| 9 | Rough edges | ✓ | none found |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) keep best rounds for the session; (2) a styled title; (3) a completion jingle at 1850.

### Volley
`volley/prototype/steps/step-08.bas` (43 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ~ | "VOLLEY" plain at 3,3 on the instruction screen (l.15) |
| 2 | Instructions | ✓ | l.15 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | "Returns:" (30, 620); "Miss." (700) |
| 5 | Progression | ✗ | constant ball speed (PAUSE 2 at 110), no rounds |
| 6 | Replay | ✓ | R returns to title (750) |
| 7 | Best | ✗ | |
| 8 | Colour | ~ | blue court, cyan walls, yellow bat by PAPER (35–50, 500); ball is letter "o"; no UDGs |
| 9 | Rough edges | ✓ | none found |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) bat and wall sounds; (2) speed-up as returns climb; (3) best-returns record; (4) a UDG ball. The smallest program in the set (43 lines) and the thinnest game.

### Touchdown
`touchdown/teaching/unit-11/steps/step-02.bas` (66 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "TOUCHDOWN" (50), text only |
| 2 | Instructions | ✓ | l.60–100 |
| 3 | Sound | ~ | landing two-note and crash tone (750–760); no thrust sound |
| 4 | Feedback | ✓ | FUEL, SPEED, MAX 12 (150, 370); three outcome messages (710–730) |
| 5 | Progression | ✗ | one terrain (DATA 9000), fixed fuel 45 |
| 6 | Replay | ✓ | R (797) |
| 7 | Best | ✗ | |
| 8 | Colour | ✓ | UDG lander and flame frame (40, 380), green terrain, yellow pad (600–640) |
| 9 | Rough edges | ✓ | none found |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) further landscapes or less fuel per landing; (2) thrust sound; (3) score or best (fuel left).

### Sonar
`sonar/teaching/unit-08/steps/step-01.bas` (105 lines; the last unit, 09, uses unit-08's file)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "SONAR - BANDS" (5010) |
| 2 | Instructions | ✓ | l.5020–5080 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | probe count (2510), N/M/F clue line (260–280) |
| 5 | Progression | ~ | "No probe limit" (5070): no way to lose, no rounds |
| 6 | Replay | ✓ | R (6030) |
| 7 | Best | ✗ | fewest probes is the natural record, not kept |
| 8 | Colour | ~ | BORDER 1, checkerboard PAPER 1/5 (2010–2020); letters as markers; no UDGs |
| 9 | Rough edges | ✗ | leftover `LET stage=6` (l.10, never used); all input via `INPUT` + ENTER (3010, 6000); full board redraw if input exceeds 16 chars (3015, 6010) as a scroll workaround |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) replace INPUT with single-key row/column entry; (2) a probe limit or par to give it stakes; (3) best probes; (4) ping sounds whose pitch tracks distance.

### Crates
`crates/teaching/unit-10/steps/step-01.bas` (174 lines; unit 11 uses unit-10's file)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "CRATES" (5010) |
| 2 | Instructions | ✓ | l.5020–5080 |
| 3 | Sound | ✗ | no BEEP; wall bump (700) silent |
| 4 | Feedback | ✓ | STEPS, GOALS n/t (2500–2505), "Delivered!" (2510–2520) |
| 5 | Progression | ~ | three rooms (8000–8270) but 1, 1 and 2 crates; wraps to room 1 (810) |
| 6 | Replay | ✓ | R restart room, N new game (130, 800) |
| 7 | Best | ✗ | fewest steps per room would suit |
| 8 | Colour | ✓ | 2x2 UDG tiles for wall, target, crate, player (7000–7390) |
| 9 | Rough edges | ✓ | none found |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) more and harder rooms; (2) push and delivery sounds; (3) best steps per room.

### Locksmith
`locksmith/teaching/finished/locksmith.bas` (82 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "L O C K S M I T H" with ASCII lock (20–50) |
| 2 | Instructions | ✓ | l.60–110 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | full try history with EXACT/OTHER (4000–4020); OPEN/LOCKED plus code reveal (5000–5210) |
| 5 | Progression | – | fixed 10 tries fits the genre |
| 6 | Replay | ✓ | R (5260) |
| 7 | Best | ✗ | codes cracked or fewest tries not kept |
| 8 | Colour | ~ | INK colours, PAPER 1 digits; no UDGs |
| 9 | Rough edges | ✓ | none found |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) sounds for key entry, check and open; (2) session record; (3) a UDG lock on the title.

### Three in a Row
`three-in-a-row/teaching/finished/three.bas` (100 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "T H R E E  I N  A  R O W" (30) |
| 2 | Instructions | ✓ | l.40–90 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | W/L/D (1020), O's reason (630), win line drawn (6000–6040) |
| 5 | Progression | – | alternates first player (5110); no difficulty levels |
| 6 | Replay | ✓ | R (5110) |
| 7 | Best | ✓ | session W/L/D tally |
| 8 | Colour | ~ | PLOT/DRAW grid and marks; grid is INK 1 on black (1030), low contrast |
| 9 | Rough edges | ~ | draw routines change permanent INK (2050, 2100, 6040) |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) move and result sounds; (2) a brighter grid; (3) optional difficulty.

### Cipher
`cipher/teaching/finished/cipher.bas` (90 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "C I P H E R" (30) |
| 2 | Instructions | ✓ | l.40–80 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | mistakes as O/. row (2520–2570), untried letters, word revealed (710–730) |
| 5 | Progression | – | 24 fixed words, no difficulty |
| 6 | Replay | ✓ | SPACE next, R reset (770–780) |
| 7 | Best | ~ | won/lost tally (2020), no best run |
| 8 | Colour | ~ | text only; no UDGs or picture |
| 9 | Rough edges | ~ | Q quits with bare STOP and no message (100, 660, 760) |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) sounds for hit, miss, win and loss; (2) a visual for mistakes (the genre's gallows or equivalent); (3) a best streak.

### Tail Chase
`tail-chase/teaching/unit-09/steps/step-01.bas` (86 lines; unit 10 uses unit-09's file)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "TAIL CHASE" (5010) |
| 2 | Instructions | ✓ | l.5020–5080 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | FOOD n/8, LENGTH (2500); outcome messages (290, 310, 440) |
| 5 | Progression | ✗ | fixed 18-frame step (260), ends at 8 snacks (440) |
| 6 | Replay | ✓ | R (4050) |
| 7 | Best | ✗ | `steps` counted (400), never shown |
| 8 | Colour | ✓ | UDG wall, directional head, body, food (7200–7260) |
| 9 | Rough edges | ✓ | none found beyond unused `steps` |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) eat and crash sounds; (2) speed-up per snack or further rounds; (3) best length or time.

### Brick Bash
`brick-bash/teaching/unit-09/brick-bash.bas` (85 lines; unit 10 uses unit-09's file)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "BRICK BASH" (5010) |
| 2 | Instructions | ✓ | l.5020–5080 |
| 3 | Sound | ✗ | no BEEP, even on bat and brick hits |
| 4 | Feedback | ✓ | BRICKS count (1010, 2510); "Missed!" / "Wall cleared!" |
| 5 | Progression | ✗ | one wall of 18, one ball, no lives (400 ends on first miss), no speed-up |
| 6 | Replay | ✓ | R (4050) |
| 7 | Best | ✗ | no score; `steps` counted (500), never shown |
| 8 | Colour | ✓ | UDG bricks in three colours and paddle (1040–1070, 7200) |
| 9 | Rough edges | ✗ | serve prints "Clear every brick." (l.300, 18 chars) over "SPACE serves. O/P move." (l.1020, 23 chars) without clearing, so row 1 reads "Clear every brick.move." during play |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) bat, brick and wall sounds; (2) lives (three balls) and a score; (3) fix the row-1 overlap; (4) a second wall or speed-up. Captures `brick-bash/teaching/ready.png` and `complete.png` show the pre-serve and win states; neither shows the overlap state, which is inferred from code.

### Drift
`drift/teaching/finished/drift.bas` (76 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "DRIFT" (5010) |
| 2 | Instructions | ✓ | l.5020–5090 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | SPEED, DOCK OK/TOO FAST, E/W N/S drift (6000–6090) |
| 5 | Progression | ✗ | one start, one dock |
| 6 | Replay | ✓ | R (4050) |
| 7 | Best | ✗ | `steps` counted (340), never shown |
| 8 | Colour | ~ | vector ship by PLOT/DRAW OVER 1, outline dock; little colour |
| 9 | Rough edges | ~ | ship XOR-erased (230) and redrawn (350) every loop even when still, so it flickers |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) thrust, dock and crash sounds; (2) successive docks with different positions or less fuel; (3) best time (the unused `steps`); (4) redraw only on change.

### Quickstep
`quickstep/teaching/finished/quickstep.bas` (107 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "QUICKSTEP" (5010) |
| 2 | Instructions | ✓ | l.5020–5090 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ~ | outcome message only (4000); no score, lives or progress readout |
| 5 | Progression | ✗ | one crossing ends the game (460) |
| 6 | Replay | ✓ | R (4050) |
| 7 | Best | ✗ | `steps` counted (440), never shown |
| 8 | Colour | ✓ | 2x2 UDG vehicles and player, blue verges, green exit (7200–7320, 1040–1070) |
| 9 | Rough edges | ✓ | none found beyond unused `steps` |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) repeated crossings with faster lanes and lives, which is the genre's shape; (2) hop and hit sounds; (3) score and best.

### The Caverns
`the-caverns/teaching/finished/caverns.bas` (93 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "THE CAVERNS" (20) |
| 2 | Instructions | ✓ | l.30–90 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | TREASURE n/3, TURNS (1020), signs per exit (1120–1150), three endings (5000–5060) |
| 5 | Progression | ✗ | fixed map, pit fixed at room 7 (250), treasures fixed (240), creature route fixed (9800); every replay is identical |
| 6 | Replay | ✓ | R (5110) |
| 7 | Best | ✗ | fewest turns not kept |
| 8 | Colour | ~ | INK colours, one PLOT rule; no UDGs |
| 9 | Rough edges | ~ | full CLS and redraw every move (270 → 1000), a visible flash per turn |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) randomise pit, treasures and creature start so replays differ; (2) sounds for treasure, creature near, death; (3) best turns.

### Yearfall
`yearfall/teaching/finished/yearfall.bas` (173 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "YEARFALL" (20) |
| 2 | Instructions | ✓ | l.30–100 |
| 3 | Sound | ✗ | no BEEP |
| 4 | Feedback | ✓ | full plan and harvest accounts (2100–2240, 4000–4150), decade verdict (5070–5110) |
| 5 | Progression | ✓ | random yields, traveller events (7000), ten-year reviews with continue (540, 5165) |
| 6 | Replay | ✓ | R new settlement (5160) |
| 7 | Best | ~ | end-of-decade summary; nothing kept across settlements |
| 8 | Colour | ~ | INK colours only; no graphics |
| 9 | Rough edges | ~ | Q quits with bare STOP and no message (120, 310, 510, 5150, 7180); full CLS on each plan edit (270 → 2090) |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) sounds for harvest, famine, travellers; (2) best settlement kept for the session; (3) a clean quit message.

### Night Patrol
`night-patrol/teaching/finished/night-patrol.bas` (183 lines)

| # | Item | | Evidence |
|---|---|---|---|
| 1 | Title | ✓ | "NIGHT PATROL" with UDG legend (5010–5100) |
| 2 | Instructions | ✓ | l.5020–5100 |
| 3 | Sound | ✗ | no BEEP, even when spotted |
| 4 | Feedback | ✓ | objective line (2500–2510), SPOTTED/RECOVERED (4010–4020) |
| 5 | Progression | ✗ | one map, one guard route (8200–8900) |
| 6 | Replay | ✓ | R (4050) |
| 7 | Best | ✗ | `steps` counted (350), never shown |
| 8 | Colour | ✓ | UDG player, wall, file, exit (7500–7540); amber sight cone by attribute POKE (3020) |
| 9 | Rough edges | ✓ | none found beyond unused `steps` |
| 10 | SCREEN$ | ✗ | |

Gaps: (1) alarm and pickup sounds; (2) a second floor or faster guard; (3) best time.

## Summary table

| Game | 1 Title | 2 Instr | 3 Sound | 4 Feedback | 5 Progress | 6 Replay | 7 Best | 8 Colour | 9 Rough | 10 SCREEN$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Bright Spark | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ~ | ✓ | ✗ |
| Volley | ~ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ~ | ✓ | ✗ |
| Touchdown | ✓ | ✓ | ~ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ |
| Sonar | ✓ | ✓ | ✗ | ✓ | ~ | ✓ | ✗ | ~ | ✗ | ✗ |
| Crates | ✓ | ✓ | ✗ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ✗ |
| Locksmith | ✓ | ✓ | ✗ | ✓ | – | ✓ | ✗ | ~ | ✓ | ✗ |
| Three in a Row | ✓ | ✓ | ✗ | ✓ | – | ✓ | ✓ | ~ | ~ | ✗ |
| Cipher | ✓ | ✓ | ✗ | ✓ | – | ✓ | ~ | ~ | ~ | ✗ |
| Tail Chase | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ |
| Brick Bash | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ |
| Drift | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ~ | ~ | ✗ |
| Quickstep | ✓ | ✓ | ✗ | ~ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ |
| The Caverns | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ~ | ~ | ✗ |
| Yearfall | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ~ | ~ | ~ | ✗ |
| Night Patrol | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ |

## Cross-cutting gaps

- **Sound:** 13 of 15 have none. Bright Spark and Touchdown are the only games with a `BEEP`, and Touchdown's is end-of-game only.
- **Progression in action games:** seven of the eight real-time games (all but Bright Spark) end after one screen at one speed. Brick Bash has no lives; a single miss ends it.
- **Best result:** only Three in a Row keeps a real session record. Five games increment an unused `steps` variable (Tail Chase 400, Brick Bash 500, Drift 340, Quickstep 440, Night Patrol 350); it reads as a dropped feature and is the cheapest route to a best score.
- **Title screens:** all text, all one template, none with a large or drawn title. Bright Spark and Volley print the name unstyled.
- **Quit:** every game ends on `STOP`, leaving the ROM's "STOP statement" report; Cipher and Yearfall do it without printing any closing message. 1982 to 1983 releases rarely had a quit key at all, so this is a design choice to revisit rather than a bug.
- **UDGs:** 6 of 15 use them (Touchdown, Crates, Tail Chase, Brick Bash, Quickstep, Night Patrol); Drift and Three in a Row draw with PLOT/DRAW instead. The puzzle and text games (Sonar, Locksmith, Cipher, Caverns, Yearfall, Volley, Bright Spark) have no custom graphics.
- **Loading screens:** none.
- **Replay without reloading:** passes in all 15.

## Captures available

`website/public/images/sinclair-zx-spectrum/basic/<game>/`: most games have 7 to 9 images; Volley has one (`court.png`), Night Patrol two (`teaching/archive.png`, `candidate-fan.svg`), Drift three and Brick Bash five under `teaching/`. No gameplay videos under `website/public/videos/…/basic/` for these games. I viewed `brick-bash/teaching/ready.png` and `complete.png`; they match the endpoint code (title row, BRICKS counter, three brick colours, "R plays again / Q quits" footer).
