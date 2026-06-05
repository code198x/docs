# Brief: General Programming primer  *(working title — name TBD)*

**Kind:** `teaching` · **Scope:** cross-platform · **Layer:** 1 (the front of
everything) · **Status:** approved to build 2026-06-05.

The universal first step. Teaches the **ideas every language is built from**, before
any specific language or machine. It is the prerequisite for the BASIC primer *and*
(via Foundations) for *Meet the Machine* — so a learner targeting a machine with no
BASIC (the NES) reaches assembly through this, never needing BASIC. Architecture:
[`decisions/front-of-curriculum-architecture.md`](../../../decisions/front-of-curriculum-architecture.md).
Built native to the v3.0 bar
([`decisions/incremental-construction-units.md`](../../../decisions/incremental-construction-units.md)).

## The teaching contract

Every concept is shown **twice**:

1. **Pseudocode** — the idea, in a tiny language-neutral notation (below). This is
   the thing being taught; it is true in every language.
2. **Spectrum BASIC, running** — the same idea on a real machine, captured as a
   result, so the concept is *concrete*, never dry (the over-extraction risk the
   architecture doc flags). Framed explicitly as *an example*: "here in BASIC; the
   same idea everywhere — Python says `print`, C says `printf`."

A learner bound for NES assembly reads the BASIC as illustration and moves on; a
learner bound for the BASIC track meets it again in earnest in the BASIC primer
(concept here → syntax there → application in the games).

### The pseudocode notation

```
SHOW "Hello"                          output a value
ASK "Name?" INTO name                 read input into a variable
SET total TO price + tax              assignment / compute
IF score = 7 THEN SHOW "You win"      a decision
REPEAT 5 TIMES … END                  counted loop
REPEAT UNTIL guess = answer … END     loop with a condition
DEFINE greet … END   /   CALL greet   a named, reusable block
```

BASIC mapping: `SHOW`→`PRINT`, `ASK…INTO`→`INPUT`, `SET…TO`→`LET`,
`REPEAT n TIMES`→`FOR/NEXT`, `REPEAT UNTIL`→`GO TO` loop guarded by `IF`,
`DEFINE/CALL`→`GO SUB/RETURN`.

### The recurring thread

Discrete concept beats (like *Meet the Machine*), warmed by a light recurring
example — a **guess-the-number** toy that surfaces as the payoff in unit 7
(decisions) and unit 9 (the game loop), so "decision" and "repeat until" land in
something that already feels like a game. Not a forced single cumulative program;
each unit has its own minimal illustration, and the thread reappears where it earns
its place.

## The beats (11 units)

Counts are markers, not contracts. Each unit is one concept with a runnable BASIC
result; most have 2–3 milestones.

1. **A program is instructions.** A program is a list of instructions; the computer
   follows them in order and does *exactly* what each says.
   *The honest version (per the caveat):* "exactly" is not "perfectly." The machine
   was built by people, and people make mistakes — a few famous bugs are baked into
   the silicon and ROM (the 6502's indirect-`JMP` page-boundary bug, buggy disk
   ROMs, Z80 quirks). Those are rare and documented. In your first months a
   misbehaving program is almost never one of them — it is the instruction you
   wrote. So suspect your own code first: the discipline holds *because* real machine
   bugs are rare and known, not because the machine is perfect.
   *Pseudo:* `SHOW "Hello"` → *BASIC:* `10 PRINT "Hello"`. *Milestone:* one
   instruction runs (and the report line — the machine telling you it finished).

2. **Sequence.** Order is the program — instructions run top to bottom; the order
   you put them in *is* the logic. *BASIC:* three `PRINT`s; reorder, output
   reorders. *Milestone:* same lines, two orders, two results.

3. **Output.** How a program talks: fixed text, a value, and the two joined.
   *Pseudo:* `SHOW`. *BASIC:* a word; a number; `PRINT "Score: "; n`. *Milestones:*
   text → number → joined.

4. **Variables.** A named box that remembers a value; set it, use it, change it —
   the single most important idea in the course. *Pseudo:* `SET n TO …`. *BASIC:*
   `LET`, string vs numeric names. *Milestones:* store→use; change→see it change.

5. **Input.** The program responds to *you*: read a typed value into a variable.
   *Pseudo:* `ASK … INTO n`. *BASIC:* `INPUT`. *Milestone:* ask a name, greet it.
   (First interactive payoff. Capture injects the typed answer — see Capture.)

6. **Numbers and sums.** Computing values; the text-vs-number distinction.
   *Pseudo:* `SET total TO a + b`. *BASIC:* numeric `INPUT` + arithmetic. *Milestone:*
   ask two numbers, show their sum (and what happens if you treat text as a number).

7. **Decisions.** Act only *if* a condition holds; conditions are true/false
   questions — `=`, `<`, `>`, and combining with `AND` / `OR`. (Comparison/boolean
   folded in here, not a separate beat.) *Pseudo:* `IF … THEN`. *BASIC:* `IF/THEN`.
   *Milestones:* "if it's 7, say correct" (the guess thread begins); a range check
   `IF n > 10 AND n < 20`.

8. **Repetition — counted.** Repeat a known number of times without copying lines.
   *Pseudo:* `REPEAT 5 TIMES`. *BASIC:* `FOR/NEXT`. *Milestones:* count 1–10; a row
   of stars; a times-table line.

9. **Repetition — until.** Repeat *until* something becomes true — the shape of every
   game (keep going until win/lose/quit). Kept separate from unit 8 because this is
   the game-loop seed and earns its own beat. *Pseudo:* `REPEAT … UNTIL g = 7`.
   *BASIC:* a `GO TO` loop guarded by `IF`. *Milestone:* keep asking until the guess
   is right (the guess thread pays off as a tiny game). *Framing:* name it the **game
   loop** — "you'll meet this in every game you build, in BASIC and in assembly."

10. **Named blocks.** Package a job, name it, call it from anywhere, reuse it.
    *Pseudo:* `DEFINE/CALL`. *BASIC:* `GO SUB/RETURN`. *Milestone:* one block (draw a
    divider, or the greeting), called twice — same job, two places, written once.

11. **When it's wrong.** The debugging mindset, as the capstone. The machine did
    exactly what you said; a bug is the gap between what you *meant* and what you
    *wrote*. Find it by **reading what the program actually did** — its output and
    its variables — not by guessing. *And the maturity (per the caveat):* know the
    rare case where it genuinely is the machine or the tooling, and how you'd *prove*
    it (isolate, reproduce, check against a known-good reference) rather than blame it
    to dodge your own bug. *BASIC:* a deliberately buggy program found by observing.
    *Milestone:* spot-and-fix by reading state. This is the bar's debugging spine,
    taught here as a concept and reinforced in every unit downstream.

## Capture

Reuses the BASIC capture pipeline (`code-samples/_capture/capture.py`,
`load_basic_program` → run → screenshot), manifest-driven, saved scripts, cold-boot,
no staging — per the bar. Input units (5, 6, 9, the guess thread) inject the typed
answer with a `type` step (`type_string`, newline = Enter) after the `INPUT` prompt
appears — verified working. Results are stills (this primer produces text/number
output, not motion or sound); a unit that shows nothing observable folds into the
next that does.

## Bar / accessibility

- Cumulative `steps/step-NN.bas` per unit; `CodeDiff` between milestones; full state
  behind a `<details>`. (Steps are per-unit; the primer is discrete beats, so no
  cross-unit carry-in beyond the recurring thread's shared example.)
- Alt text on every screenshot; the concept lives in prose + pseudocode, never only
  in the BASIC illustration (a sound-off / different-target learner gets it from the
  pseudocode and prose).
- A short "When it's wrong, see why" beat in every unit (the spine), with unit 11 as
  the dedicated capstone.

## Deliberately out of scope

- **Constants.** Classic BASIC (Sinclair, C64) has no constant declaration — a "value
  you name once and never change" is just a variable held by convention. The primer
  teaches what the vehicle can *show*, and the vehicle can't show a constant, so there
  is no constants beat. Don't add one back.
- **Variable-naming rules are taught where they bite, not abstractly.** Unit 4 carries
  the honest, local rules of the vehicle: this BASIC allows long *numeric* names but
  only single-letter `$` names for *text* (`n$`, not `name$` — `name$` throws
  "Variable not found"); the C64 reads only a name's first two letters. The *idea* (a
  named box) is universal; the naming rules are local — which is the primer's thesis in
  miniature. See behavioural memory `project_sinclair_basic_variable_naming`.

## Open / deferred

- **Name.** "First Principles" / "How Programs Work" / "Meet the Ideas" / "Before the
  Language" — TBD.
- **Hosting (infra, before units go live).** The site's content model keys modules by
  `platform` + `track: assembly|basic|amos`, and the route brands by platform — a
  cross-platform module has no home yet. Needs a small IA decision (a neutral
  "foundations" section vs hosting under Spectrum with cross-platform framing).
  Tracked separately; does not block authoring the steps + captures.
