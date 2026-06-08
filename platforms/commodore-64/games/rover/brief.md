# Rover — Brief

**Title (working):** Rover
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 7 of 8
**Headline concept:** Control — real-time, responsive movement
**Embedded concept:** Collision — the world pushes back
**Topics:** 7 topics, ~9–12 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that a program can run a continuous loop, read the joystick at control port 2 with `PEEK(56320)` on every pass, and move a character by the erase-move-draw technique — and that `PEEK`-ing the cell the rover is *about to enter* tells you what it would hit before it gets there, so the learner arrives at Dropzone with a live input loop and collision detection already in hand.

---

## 2. Classic Ancestors

- **Maze and chase type-ins** — the character-graphics action game that filled *Compute!'s Gazette* listings from 1983 on: a player block, a screenful of walls drawn in PETSCII, dots to collect, all moving in a `GOTO` loop. Short enough to type in over an evening, fast enough to feel alive.
- **The joystick-reading "move the man" listing** — the magazine staple that first showed a reader their stick could steer something on screen. `PEEK(56320)`, an `AND` to pick the bit, a POKE to move. The whole point was that *you* were driving.

---

## 3. Core Experience

Steer a rover around a screen of walls and pickups. It moves while you hold the stick; it stops dead at walls; it scores when it rolls over a pickup. The screen is the world and the rover lives in it — the first time in the volume that the machine answers you in real time.

---

## 4. Visual Direction

- A character-graphics world: a solid border and inner walls drawn in one colour into screen RAM at 1024, with the matching cells in colour RAM at 55296. The rover is a single bright block — a filled square or a distinct PETSCII shape — in a colour that reads distinctly against the walls.
- Colour carries state, not decoration. Walls are one steady colour; pickups are a second, brighter colour so they read as "go here"; the rover is a third so the eye tracks it instantly. When a pickup is collected the cell clears to background — the world visibly changes as you play.
- The score sits on the top or bottom row, POKEd into screen + colour RAM so it never scrolls the playfield.
- Magazine-screenshot test: a *Compute!'s Gazette*-style screenshot — a boxed maze of walls, scattered bright pickups, the rover mid-corridor, and a score line reading `SCORE 30`. A reader recognises it as a game they could type in and play.

---

## 5. Audio Direction

- **A step blip on movement.** A short tone POKEd into the SID at 54272 (single voice) each time the rover moves a cell — a soft motor tick that gives the movement weight without becoming a drone.
- **A pickup tone.** A brighter, higher blip the moment a pickup is collected — distinct from the step so the ear knows a point was scored without watching the number.
- **A bump tone.** A low, blunt tone when the rover is pushed into a wall and stops — the audio half of the collision; the world answering back.
- Deliberately silent: no title music, no continuous engine hum. The SID speaks only on events, so each one stays legible.

---

## 6. Anti-goals

- No physics — the rover moves a whole cell per step at a constant rate. Velocity, acceleration and gravity are Dropzone's job, the capstone.
- No enemies and no AI — nothing chases the rover, nothing else moves. Live opponents are a later, bigger game.
- No win-by-survival and no timer pressure — the goal is to collect, not to outlast. Tension from the clock belongs to other games.
- No sprites, no custom characters, no smooth pixel scrolling — this is stock character graphics on screen + colour RAM. Sprites are a later volume.
- Keep it small — a complete, readable program a learner is proud to keep, not a sprawling engine.

---

## 7. Topic Progression

1. **Place the rover.** POKE a single bright block into screen RAM and its colour into colour RAM at a chosen row and column, using `1024 + R*40 + C` and `55296 + R*40 + C` from the primer. Hold the rover's position in two variables, `R` and `C`. Nothing moves yet — the lesson is that the rover is just two numbers and two POKEs. **New:** the rover as position variables `R`,`C` driving paired screen + colour POKEs. **Program:** ~10 lines. **Polish beat:** pick the rover's colour and shape so it reads instantly against the background — try a few before settling.

2. **Move it by joystick.** Open the loop. Each pass, read control port 2 with `J = PEEK(56320)`. The bits are active-low — a held direction *clears* its bit — so test with `AND`: up is `(J AND 1) = 0`, down is `2`, left is `4`, right is `8`. Adjust `R`/`C`, then erase the old cell, draw the new one — the erase-move-draw technique. The rover follows the stick. **New:** `PEEK(56320)` in a live loop; decoding direction bits with `AND`; erase-move-draw. **Program:** ~22 lines. **Polish beat:** how fast does it move? A short delay or a tighter loop sets the feel — too fast is uncontrollable, too slow is sluggish.

3. **Keep it on screen.** Without limits the rover walks off the edge and POKEs into memory it shouldn't. Before applying a move, check the new `R`/`C` against the bounds (0–24 rows, 0–39 columns) and refuse the step if it would leave the screen. The playfield now has edges. **New:** bounds-checking a move before committing it. **Program:** ~28 lines. **Polish beat:** does the rover stop cleanly at the edge, or stutter? The check should feel like a wall, not a glitch.

4. **Draw walls and stop at them.** POKE a border and a few inner walls into screen + colour RAM before the loop starts. Now collision: before moving, `PEEK` the cell the rover is *about to enter*. If it holds a wall character, cancel the step — the rover stops. This is the embedded concept made real: the world pushes back. **New:** `PEEK`-the-target-cell collision; reading a character code back from screen RAM. **Program:** ~38 lines. **Polish beat:** play a bump tone on a blocked move so a wall feels solid, not just unresponsive.

5. **Scatter pickups and score.** POKE a handful of pickups in a second bright colour. Extend the look-ahead `PEEK`: if the target cell holds a pickup, let the rover move in, clear the pickup to background, and add to `SC`. POKE the score onto a status row. The world now rewards exploration. **New:** distinguishing wall / pickup / empty by the PEEKed code; collecting and scoring; a POKEd score display. **Program:** ~48 lines. **Polish beat:** a bright pickup tone on collection — the score should be heard as well as seen.

6. **A goal and a finish.** Count the pickups at the start; count them down as they're collected. When the last one is taken, break the loop and show a "ALL CLEAR" finish with the final score. The session now has a shape: enter, clear the screen, done. **New:** a remaining-count variable; an end condition that exits the loop; a finish state. **Program:** ~56 lines. **Polish beat:** the finish should land — a colour change, a tone, the score held on screen. Make clearing the board feel earned.

7. **Make it yours.** Add a title screen with the rover's name and a "press fire to start" prompt — read fire with `(J AND 16) = 0`. Lay out a wall pattern the learner designs themselves, place the pickups deliberately, and tune the colours, the move rate and the tones until the whole thing feels like a game you'd type in from a magazine. **New:** reading fire to start; hand-designed playfield layout; final tuning pass. **Program:** ~65 lines. **Polish beat:** show someone. Watch them drive. The rover is a toy you built that another person can pick up and play.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] The joystick loop is responsive — no perceptible lag between moving the stick and the rover moving
- [ ] Joystick bits are read from port 2 (`PEEK(56320)`) and decoded active-low with `AND` (up=1, down=2, left=4, right=8, fire=16)
- [ ] The rover stops cleanly at walls and at the screen edge — collision reads the target cell *before* moving, never POKEs past the playfield
- [ ] Pickups are collected and scored reliably; the score display updates without disturbing the playfield
- [ ] Gradual progression — a reader can follow from topic 1 to final topic without gaps
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **input** — `PEEK(56320)` joystick polling in a live loop, decoded active-low with `AND` (up=1, down=2, left=4, right=8, fire=16). The C64's real-time input read — the foundation of every action game on the platform.
- **rendering** — erase-move-draw on screen + colour RAM: clear the old cell, POKE the new one. The character-graphics movement technique reused wherever something moves a cell at a time.
- **basic** — look-ahead collision: `PEEK` the cell a mover is about to enter and branch on the character code (wall / pickup / empty). Test the world before committing the move — the core of collision on a memory-mapped screen.

---

## 10. Vault Tie-ins

- **Maze and chase type-ins** — the *Compute!'s Gazette* character-graphics action tradition; the joystick-driven game a reader could type in and play.
- C64 control port 2 at `PEEK(56320)` — the active-low joystick register the assembly track revisits at machine speed.
- C64 screen RAM (1024) + colour RAM (55296) — the memory-mapped playfield the rover lives in, the same surface every C64 BASIC game in the volume writes to.
