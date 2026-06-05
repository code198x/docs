# Primer — "Meet BASIC" (outline)

> **Status:** Approved to build, 2026-06-05 (read and signed off by Steve; open
> questions resolved — see *Open for the author*). The BASIC track's opening artefact, per
> [`front-of-curriculum-architecture.md`](../../../../decisions/front-of-curriculum-architecture.md)
> (Layer 2a). Sits *ahead* of Story Builder and the rest of Volume 1, and *after*
> the General Programming primer (Foundations, Layer 1). "meet-basic" is the working
> slug; a real name can wait. This is a design outline (beats + intent), not authored
> unit prose.
>
> **Working beat list (live numbering carried by the authored units):**
> 1 The Keyboard Types Words · 2 The Line Number Is an Address · 3 PRINT, Properly ·
> 4 LET, and What You May Name · 5 INPUT — the Program Listens · 6 IF / THEN the
> Spectrum Way · 7 FOR / NEXT Counts For You · 8 GO TO, GO SUB, and the Game Loop ·
> 9 The Screen Is a Grid (PRINT AT) · 10 Colour, and Text in Many Colours · 11 The
> Machine Can Sing (BEEP) · 12 Drawing With Light (PLOT/DRAW/CIRCLE) · 13 Making It
> Move (animation) · 14 Keeping Your Work (SAVE/LOAD) · 15 When It's Wrong (the
> report line).
>
> Fifteen is the working count, not a target — the no-fixed-unit-counts rule holds.
> Several beats could merge or split at build time (see *Open for the author*).

## What the Primer is

The bridge from *the ideas* to *one real language on one real machine*. General
Programming taught what a variable, a loop, a decision and a subroutine **are**, in
pseudocode, illustrated lightly in Sinclair BASIC. *Meet BASIC* now sits the learner
at the Spectrum and teaches them to **write and run Sinclair BASIC for real** — its
syntax, its quirks, and the expressive surfaces General Programming skipped on
purpose: the screen, colour, sound, and pixel graphics that games are made of.

It is **not a game** — there is no win condition. Its single job: by the end the
learner can type, run, edit, save, and debug a Sinclair BASIC program, and has met
every language feature and machine surface the Volume 1 games assume — so the games
open on *building a thing*, not on "here is what PRINT does."

**This primer absorbs the language-primer work currently inside Story Builder
unit-01** ("Hello, Spectrum" — keyword entry, line numbers, PRINT/CLS, the report
line, numbering in tens). Once Meet BASIC ships, Story Builder re-scopes to open on
the game (architecture step 3, tracked separately).

**Floor:** the learner has met sequence, variables, input, decisions, loops,
subroutines and the debugging mindset — in General Programming, or any language. The
*ideas* are assumed. The concept beats (3–8) are therefore **fast**: they map a known
idea onto Sinclair syntax and name the quirk that bites, nothing more. The weight sits
where the material is genuinely new — the editor (1–2) and the Spectrum's own surfaces
(9–13).

**Signpost (recommend, never gate)** — opens the Primer:
> *New to programming entirely? Start with [General Programming](/foundations/general-programming);
> it teaches the ideas this primer writes in Sinclair BASIC. Met variables, loops and
> decisions before, in any language? You're ready.*

## The one rule the author must trust

**"Feels easy" is correct on the concept beats.** The learner has seen the idea; here
the lesson is "*this* is how the Spectrum spells it, and *this* is the quirk that will
catch you." A PRINT beat that maps a known concept to one line of Sinclair BASIC and
names one gotcha is doing its whole job. The instinct to re-teach the concept (it was
taught in General Programming) is the over-extraction risk — resist it.

The surface beats (9–13) carry the delight. Colour, sound, a drawn frame, and finally
motion are where the Spectrum stops being a text terminal and becomes the machine the
learner wanted. Let those beats show off.

## Toolchain / runtime (established in Beat 1, reused throughout)

- **No assembler.** BASIC is typed and `RUN` directly — no build step (a contrast the
  assembly primer's Beat 1 draws the other way).
- **Runtime:** Emu198x (Fuse as the present learner runtime). The teaching surface is
  the screen itself — text, colour, a drawn line, a beep — not a register view.
- **The distinctive Spectrum thing:** the **keyword-entry keyboard**. `P` types the
  whole word `PRINT`. Beat 1 makes this the first "aha"; every later beat assumes it.
- **Capture:** the BASIC capture pipeline (`code-samples/_capture/capture.py`,
  `load_basic_program` → run → screenshot; `save_audio_capture` for BEEP),
  manifest-driven, cold-boot, saved scripts — per the v3.0 bar.

## The recurring artefact (the title card — adopted)

A **title card** that grows across the surface beats into the kind of splash screen
every game opens with. It starts (Beat 3) as a plain `PRINT` greeting; gains a chosen
position (Beat 9, `PRINT AT`); colour, a border, and a rainbow pass (Beat 10); a
fanfare (Beat 11, `BEEP`); a drawn frame (Beat 12, `DRAW`); and finally **motion**
(Beat 13) — it animates in, or a star tracks across it. By the end the learner has
built a small, **moving, multicolour Spectrum splash screen**, exercising every surface
and producing a vivid capstone — and has felt the flicker that opens the door to the
assembly track. Discrete beats otherwise (like the assembly primer); the title card is
a light motif the surface beats converge on, not a forced single program.

## Each beat's shape

Title (the feature) · the one idea · the felt "aha" · the task + what the screen shows
· the General-Programming callback (concept → Sinclair syntax) · the code primitive(s)
· the quirk that bites · "Try this" · what it unlocks.

---

## The beats

### 1 — The Keyboard Types Words *(keyword entry + the run-it loop)*
- **Idea:** on the Spectrum, a keypress types a whole BASIC word — `P` gives `PRINT`.
  You type a numbered line, `RUN` it, and read the report the machine prints back.
- **Aha:** "the keyboard is a BASIC instrument — whole keywords arrive from one key,
  and the machine tells me, in a report line, that it finished."
- **Task:** enter `10 PRINT "Hello"`; `RUN`; see `Hello` and the report `0 OK, 10:1`
  (it ran line 10 and stopped happily). Change the word; run again.
- **Callback:** General Programming's `SHOW "Hello"` → here `10 PRINT "Hello"`, typed
  on a real keyboard that speaks in keywords.
- **Primitive:** `PRINT`; `RUN`; reading the report line.
- **Quirk:** `PRINT` comes from one keypress in keyword mode, not typed letter by
  letter; a missing closing quote gives `Nonsense in BASIC`.
- **Try this:** print a different word; print your name.
- **Unlocks:** the type-run loop repeated all primer; the report line as feedback.

### 2 — The Line Number Is an Address *(the editor)*
- **Idea:** every line has a number; the number is its *address*. Reuse a number to
  replace that line; pick a free number to add one; type a number alone to delete it.
  `LIST` shows the program in number order. Number in **tens** to leave gaps.
- **Aha:** "I edit by line number, and the gaps in the numbering are room to slip
  lines in later."
- **Task:** grow a three-line program; replace line 10 by retyping it; insert line 25
  between 20 and 30; delete a line; `LIST` to read the order.
- **Callback:** the program is General Programming's ordered instructions — here the
  order is the *line numbers*, not the typing order.
- **Primitive:** line numbers; `LIST`; replace / insert / delete by number.
- **Quirk:** the program runs in **number order**, not the order you typed; reusing a
  number silently overwrites the line that was there.
- **Try this:** predict where line 35 lands before running; change a line in a gap.
- **Unlocks:** every later beat edits a multi-line program with confidence.

### 3 — PRINT, Properly *(output syntax + the title card begins)*
- **Idea:** `PRINT` has punctuation. `;` joins items, `,` jumps to the next column
  zone, `'` starts a new line; you can print fixed text, a value, or both joined.
  `CLS` clears the screen first.
- **Aha:** "the semicolon and comma place things — PRINT is how the program lays text
  out, not just dumps it."
- **Task:** `PRINT "Score: "; n`; a comma-separated pair in two columns; `CLS` then a
  two-line greeting (the title card, plain for now).
- **Callback:** General Programming unit 3 (output) — here the Sinclair punctuation.
- **Primitive:** `PRINT` with `;` `,` `'`; `CLS`.
- **Quirk:** `;` joins with no gap, `,` tabs to a zone — mixing them up misaligns
  output; a trailing `;` suppresses the newline.
- **Try this:** print three numbers in a row two ways (`;` vs `,`); see the spacing.
- **Unlocks:** every beat's on-screen result; the title card's text.

### 4 — LET, and What You May Name *(variables + the naming rules)*
- **Idea:** `LET a = 5` stores a value in a named box. Numeric names may be long
  (`score`); **text variables must be a single letter plus `$`** (`n$`). `=` here is
  *assignment*, not a question.
- **Aha:** "the idea is the box I already know; the Spectrum's rule is that string
  names are single-letter — and `name$` will not work."
- **Task:** `LET score = 0`; `LET n$ = "Sam"`; print both. Then try `LET name$ = "Sam"`
  and meet `Variable not found` — the rule, shown failing.
- **Callback:** General Programming unit 4 (variables) flagged this rule; here it is
  the binding Sinclair rule, with the error on screen.
- **Primitive:** `LET`; numeric vs `$` (string) variables.
- **Quirk:** string variables are **single letter + `$`** (`n$`, not `name$`); a
  keyword can't be a variable name; `=` in `LET` assigns (it asks a question only
  inside `IF`).
- **Try this:** store and print a long numeric name; break it with a long string name.
- **Unlocks:** variables for every later beat; the naming rule that bites in INPUT.

### 5 — INPUT — the Program Listens *(input syntax)*
- **Idea:** `INPUT n` reads a number the player types; `INPUT n$` reads text. The
  program pauses with a cursor until Enter.
- **Aha:** "the program waits for *me* now — and what I type lands in a variable."
- **Task:** `INPUT "Your name? "; n$` then greet them; `INPUT a` then double it. (The
  capture injects the typed answer after the prompt appears — per the pipeline.)
- **Callback:** General Programming unit 5 (input) — here `INPUT`, with the
  single-letter `$` rule from Beat 4 applied.
- **Primitive:** `INPUT` (numeric and string); the input prompt.
- **Quirk:** a string answer needs a single-letter `$` variable; typing letters into a
  numeric `INPUT` gives an error, not a silent zero.
- **Try this:** ask two numbers and print their sum; ask a name and a number together.
- **Unlocks:** interactive programs; the first beat the player drives.

### 6 — IF / THEN the Spectrum Way *(decisions)*
- **Idea:** `IF a = 7 THEN PRINT "Yes"` acts only when the condition holds. Compare
  with `=`, `<`, `>`, `<=`, `>=`, and **`<>` for not-equal**. Combine with `AND` /
  `OR` (logical, not bitwise). `THEN` is followed by a statement.
- **Aha:** "the decision I know, spelled with `<>` and a `THEN` that runs a statement —
  and there is no `ELSE` to lean on."
- **Task:** a guess check — `IF g = 7 THEN PRINT "Correct"`; a range check
  `IF n > 0 AND n < 10 THEN ...`; the "too low / too high" pair written as two IFs
  (because there is no `ELSE`).
- **Callback:** General Programming unit 7 (decisions) — here the Sinclair operators.
- **Primitive:** `IF ... THEN`; `=` `<` `>` `<=` `>=` `<>`; `AND` `OR`.
- **Quirk:** not-equal is **`<>`** (not `!=`); `AND`/`OR` are **logical**, not bitwise;
  classic Sinclair BASIC has **no `ELSE`** — write a second `IF`.
- **Try this:** branch three ways (low / equal / high) with two IFs.
- **Unlocks:** all conditional logic; the guard for the game loop.

### 7 — FOR / NEXT Counts For You *(counted loop)*
- **Idea:** `FOR i = 1 TO 10 ... NEXT i` repeats a known number of times; `STEP`
  changes the stride; `i` is a real numeric variable you can use inside the loop.
- **Aha:** "the counted loop I know — and the counter is just a variable I can read."
- **Task:** count 1–10 on screen; a times-table line with the counter; a `STEP 2` run.
- **Callback:** General Programming unit 8 (counted repetition) — here `FOR`/`NEXT`.
- **Primitive:** `FOR ... TO ... [STEP]`; `NEXT`.
- **Quirk:** `NEXT i` must name the same variable; an empty range still runs once in
  some dialects — keep ranges sensible.
- **Try this:** count down with `STEP -1`; nest a short delay loop for a visible pause.
- **Unlocks:** repetition without copying lines; rising-beep runs in Beat 11.

### 8 — GO TO, GO SUB, and the Game Loop *(jumps + the loop)*
- **Idea:** `GO TO` and `GO SUB` are **two words**. `GO TO n` jumps to a line; a
  `GO TO` back to the top, guarded by an `IF`, is the **game loop**. `GO SUB n` calls a
  block and `RETURN` comes back — but the call is to a **line number**, not a name.
- **Aha:** "the game loop and the reusable block I met as ideas — here they jump to
  *line numbers*, because Sinclair BASIC has no named subroutines."
- **Task:** a loop that keeps asking until the guess matches the computer's secret
  number (the game loop); `GO SUB` a divider-drawing block, called from two places,
  with `RETURN`.
- **Aside — the computer picks (`RND`):** for the guess loop to be a *game*, the
  computer needs a secret number — `LET secret = INT(RND * 100) + 1` gives a whole
  number 1–100. `RND` is a fresh fraction (0–1) each time; `INT(RND * n) + 1` is the
  idiom for "a whole number from 1 to n." Introduced here because the game loop is
  where an unpredictable value first earns its place; the chance games lean on it. (Per
  the lean: an aside, not its own beat.)
- **Callback:** General Programming units 9 (loop-until / the game loop) and 10 (named
  blocks) — here `GO TO` and `GO SUB`, by line number; the guess thread completes.
- **Primitive:** `GO TO n`; `GO SUB n` / `RETURN`; `STOP`; `RND`, `INT(RND * n) + 1`.
- **Quirk:** **two words** (`GO TO`, not `GOTO`); you jump to a **number**, so leaving
  numbering gaps matters; a `GO SUB` with no `RETURN` (or vice-versa) corrupts the flow.
- **Try this:** move the subroutine; loop the divider call inside a `FOR`; narrow the
  range to 1–10 and count the guesses it takes.
- **Unlocks:** the game-loop shape every Volume 1 game runs on; `RND` for the chance
  games.

### 9 — The Screen Is a Grid *(PRINT AT)*
- **Idea:** `PRINT AT row, col;` places text anywhere on a **32 wide × 24 tall**
  character grid; the origin is **top-left** (row 0 at the top).
- **Aha:** "I can put text *where I want* — the screen is a grid I address."
- **Task:** centre the title-card greeting with `PRINT AT`; place a label in a corner.
- **Callback:** the first surface General Programming skipped — position.
- **Primitive:** `PRINT AT row, col;`.
- **Quirk:** rows run **0–21** for the print area (the lowest two lines are the editing
  area); `AT` is **row then column** (y, x) — easy to swap.
- **Try this:** place the same word at three positions; predict each before running.
- **Unlocks:** laid-out screens; the title card finds its place.

### 10 — Colour, and Text in Many Colours *(INK / PAPER / BORDER / BRIGHT / FLASH + multicolour text)*
- **Idea:** eight colours (0–7). `INK` is the foreground, `PAPER` the background,
  `BORDER` the frame; `BRIGHT` and `FLASH` modify a cell. Colour is stored **per 8×8
  cell**, separately from the pixels — so a `FOR` loop that changes `INK` before each
  letter gives **multicolour text**: a rainbow title, one colour per cell.
- **Aha:** "two bytes' worth of choices turn a grey screen into a Spectrum screen — and
  a loop over `INK` makes the title itself a rainbow."
- **Task:** give the title card an `INK`/`PAPER` scheme and a `BORDER`; make one line
  `BRIGHT`; make a word `FLASH`; then a `FOR` loop printing the title a letter at a
  time, `INK` set to the loop counter — a rainbow.
- **Callback:** the showpiece surface — what makes it *look* like a Spectrum; the
  rainbow reuses the `FOR` loop from Beat 7.
- **Primitive:** `INK` · `PAPER` · `BORDER` · `BRIGHT` · `FLASH` (0–7 / 0–1); `INK` set
  from a loop counter for per-cell colour.
- **Quirk:** colour is **per 8×8 cell** — two colours can't share a cell, the seed of
  *attribute clash* (named here, managed in the games). "Multicolour" here means
  **per-cell**, not per-pixel; the clash-breaking tricks belong to the assembly track.
  See [[emu198x:zx-spectrum-attribute-clash-and-pixel-symbols]] in the KB.
- **Try this:** clash two colours in one cell on purpose and watch the cell; embed
  colour control codes inside one `PRINT` string (`CHR$` INK codes) for multicolour
  text from a single statement.
- **Unlocks:** every coloured screen the games draw; the title card's rainbow palette.

### 11 — The Machine Can Sing *(sound)*
- **Idea:** `BEEP duration, pitch` plays one tone — `duration` in seconds, `pitch` in
  semitones from middle C. One line is one note; a `FOR` loop is a tune.
- **Aha:** "sound is one line — and a loop turns it into a fanfare."
- **Task:** a single `BEEP`; then a rising run of beeps with a `FOR` (the title-card
  fanfare). Capture the audio per the pipeline.
- **Callback:** the surface General Programming had no way to show — sound.
- **Primitive:** `BEEP duration, pitch`.
- **Quirk:** `pitch` is **semitones from middle C** (negative = lower), not a
  frequency; very long durations hang the program until the note ends.
- **Try this:** play three notes of a scale; make a "wrong answer" low buzz.
- **Unlocks:** game sound — wins, losses, ticks; the title card's fanfare.

### 12 — Drawing With Light *(PLOT / DRAW / CIRCLE)*
- **Idea:** below the character grid is a **pixel** grid, 256 wide × 176 tall. `PLOT`
  lights a point, `DRAW` draws a line from it, `CIRCLE` draws a circle.
- **Aha:** "I can draw shapes, not just place text — pixels under the letters."
- **Task:** `PLOT` a point; `DRAW` a box around the title card; a `CIRCLE` for a flourish.
- **Callback:** the last *still* surface — freehand pixel graphics.
- **Primitive:** `PLOT x, y` · `DRAW dx, dy` · `CIRCLE x, y, r`.
- **Quirk:** the pixel origin is **bottom-left** (y up) — the **opposite** of
  `PRINT AT`'s top-left. Mixing the two coordinate systems up is the classic gotcha;
  name it plainly.
- **Try this:** draw a triangle with three `DRAW`s; place a circle in each corner.
- **Unlocks:** drawn game screens; the title card's frame — the *still* splash screen
  is complete, ready to move.

### 13 — Making It Move *(animation — the surface finale)*
- **Idea:** animation is the draw-erase-redraw loop you already have the parts for: a
  `FOR` loop that `PRINT AT`s something, waits, erases it, and prints it one step over.
  Nothing new — `FOR` (Beat 7) + `PRINT AT` (Beat 9) + a delay, combined.
- **Aha:** "motion is just redrawing in a loop — and I can already do every part of it."
- **Task:** the title card comes alive — a star (or the title itself) tracks across the
  screen: `PRINT AT` it, a short delay loop, `PRINT AT` a space to erase, step the
  position, repeat. Capture it as **video** (the splash screen, moving).
- **Callback:** the payoff of the whole surface set — position, colour, and the loop
  now producing motion; the title-card thread's finale.
- **Primitive:** the draw / wait / erase / step loop; a `FOR` delay for timing. (No new
  keyword — this is *composition*, which is the lesson.)
- **Quirk — and the bridge to assembly:** in BASIC the motion **flickers and crawls** —
  the erase-and-redraw shows, and the loop is slow. That is honest, not a mistake; it is
  the exact reason the Spectrum's legends wrote games in assembly. Name it plainly:
  *"smooth, flicker-free motion is what the [assembly track](/sinclair-zx-spectrum/assembly)
  is for."* This beat is the door between the two Spectrum tracks.
- **Try this:** move two things at once; bounce the star off the screen edge with an
  `IF` (Beat 6) flipping the step direction.
- **Unlocks:** the *idea* of the game loop made visible (draw → move → redraw); the
  honest motivation for assembly; a moving splash screen to be proud of.
- **Deliberately still out of scope (do not pull forward):** player-controlled motion
  (`INKEY$`), smoothness, collision, sprites — the games' and the assembly track's
  territory. This beat is **scripted** motion on a timer, nothing more.

### 14 — Keeping Your Work *(SAVE / LOAD)*
- **Idea:** `SAVE "name"` stores the program; `LOAD "name"` brings it back. A program
  you can't keep isn't yours yet.
- **Aha:** "my program survives the machine being switched off."
- **Task:** `SAVE` the title-card program; reset; `LOAD` it back and `RUN` it.
- **Callback:** none — a machine-and-workflow beat, not a concept.
- **Primitive:** `SAVE "name"` · `LOAD "name"` (tape / snapshot in the emulator).
- **Quirk:** on real hardware this is tape (slow, audible); in the emulator it's a file
  — explain the period reality without making the learner live it.
- **Try this:** save under two names; load the older one back.
- **Unlocks:** keeping work between sessions — assumed by every game from here.

### 15 — When It's Wrong *(the report line — the debugging capstone)*
- **Idea:** the Spectrum reports every stop as a **code, text, and `line:statement`** —
  `0 OK, 10:1` when it finished, `2 Variable not found, 30:1` when it didn't. The
  report tells you *what* and *where*. Debug by reading it and `LIST`-ing the line.
- **Aha:** "the machine already told me where it stopped and why — I read the report,
  I don't guess."
- **Task:** run a deliberately broken program (a `name$`, a missing quote, a `GO TO` to
  a line that isn't there); read each report; fix by `LIST`-ing and reading state;
  `CONTINUE` to resume after a stop.
- **Callback:** General Programming unit 11 (the debugging mindset) — here the
  Spectrum's actual error vocabulary; the gap between *meant* and *wrote*, found by
  reading what the report and the program say.
- **Primitive:** the report line; `LIST`; `CONTINUE`; the common reports
  (`Variable not found`, `Nonsense in BASIC`, `Subscript wrong`, `Number too big`).
- **Quirk:** the report's `line:statement` points at *where it stopped*, which can be
  one line past the real mistake; read the named line **and** the one before it.
- **Try this:** predict the report for three different deliberate bugs before running.
- **Unlocks:** the observe-the-state debugging spine the whole track depends on.

---

## Exit competencies (handoff to Story Builder, re-scoped)

After Meet BASIC, the learner can, without it feeling like magic:

- Enter, run, edit, and save a Sinclair BASIC program using keyword entry and line
  numbers; read the report line.
- Use `PRINT` (with `;` `,` `'`), `LET` (respecting the naming rules), `INPUT`,
  `IF/THEN`, `FOR/NEXT`, `GO TO`, and `GO SUB`/`RETURN`.
- Position text with `PRINT AT`; set colour with `INK`/`PAPER`/`BORDER`/`BRIGHT`/`FLASH`
  (including multicolour text); make sound with `BEEP`; draw with `PLOT`/`DRAW`/`CIRCLE`.
- Animate by redrawing in a loop — and know why it flickers (the bridge to assembly).
- Read a Sinclair error report and debug by observing state.

They have **not** built a game, written a real-time input loop, used arrays or canned
data, or defined custom graphics. Those are the **games'** territory.

## Deferred on purpose (budget discipline — do not pull forward)

- **Arrays (`DIM`)** → the first game that needs a list (Volume 2 data-driven games).
- **`READ` / `DATA`** → where a game needs canned data.
- **`INKEY$` real-time input** (read a key without waiting, vs `INPUT`) → the real-time
  games (Volume 3), where movement motivates it. (Decided 2026-06-05: deferred.)
- **`RANDOMIZE`** (seeding `RND` for reproducible sequences) → where a game needs a
  repeatable shuffle. `RND` itself is **in** — an aside in Beat 8 (see below).
- **Custom graphics (UDGs), full attribute-clash management, the screen-thirds layout**
  → the games and the assembly track.

## Open for the author

- **Name.** Working "Meet BASIC"; family with *Meet the Machine* / *Meet Assembly*.
- **The title-card motif — ADOPTED (2026-06-05).** The growing splash-screen thread
  runs across beats 3 + 9–13, finishing as a **moving, multicolour splash screen**
  (multicolour text folded into Beat 10; animation as the Beat 13 finale, with the
  flicker-into-assembly bridge). Was open; confirmed by Steve.
- **`RND` and `INKEY$` — DECIDED (2026-06-05).** `RND` is **in**, as an aside in Beat 8
  (the guess game's secret number; the chance games lean on it). `INKEY$` is **deferred**
  to the real-time games (Volume 3), where movement motivates it.
- **SAVE/LOAD placement — DECIDED (2026-06-05).** Its own short Beat 14 (per the lean).
- **Beat 8 weight.** `GO TO` + `GO SUB` + the loop + the `RND` aside on one "jump to a
  line" idea. Held as one beat (per the lean); if it reads heavy at authoring time,
  split into 8a (the game loop, carrying the `RND` secret) / 8b (`GO SUB`).
- **Keyword entry on the learner's runtime.** The prose teaches keyword entry as the
  real Spectrum experience (`P` → `PRINT`); the capture pipeline tokenises `.bas` via
  `load_basic_program`. Note the gap so a learner driving Fuse by hand isn't surprised.

## Downstream touch-points (note — not this primer's job)

- **Story Builder re-scope** (architecture step 3): unit-01 sheds the language-primer
  work this primer absorbs and opens on the game.
- **`meet-the-machine/index.mdx` signpost** currently points new programmers at "the
  BASIC course"; under the new architecture it should point at **General Programming**.
  That edit belongs to the "split the assembly primer" task, not this one.
- **`basic.md`** (the BASIC track curriculum doc) gains a primer ahead of Volume 1.
