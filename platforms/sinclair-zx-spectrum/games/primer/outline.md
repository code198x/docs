# Primer — "Meet the Machine" (outline)

> **Status:** Draft outline, 2026-05-29. The assembly track's opening artefact, per
> [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> Sits *ahead* of the tiny first game and Shadowkeep. "primer" is a working slug; a real name
> can wait. This is a design outline (beats + intent), not authored unit prose.

## What the Primer is

A bridge sequence that moves a **programming-literate** learner from a high-level mental model
into the Z80/Spectrum machine model. It is **not a game** — there is no win condition, no
sprite, no loop-driven play. Its single job is to make the machine stop feeling like magic.

**Floor:** the reader has met variables, loops, conditionals and subroutines *somewhere* — our
BASIC course, or any other language. The spine is language-agnostic and demonstrated concretely
in the emulator; references to a prior language are **optional asides**, never load-bearing.

**Signpost (recommend, never gate)** — opens the Primer:
> *New to programming entirely? You'll have a smoother time starting with the BASIC course; this
> track assumes you've met variables, loops and subroutines before.*

## The one rule the author must trust

**"Feels easy" is correct here.** Every beat is one idea on a trivial task. The teaching is the
*conceptual rewiring* — unlearning a high-level abstraction — not task difficulty. The instinct
to "make a beat earn its place" by piling on mechanics is exactly how the old cliff was built.
Resist it. A beat that takes three lines of source and produces one visible change on screen is
doing its whole job.

Per the technique budget: **one idea per beat**, one beat ≈ one unit (~11 units; the
per-game-scope floor for the Primer is ~8–12).

## Toolchain (established in Beat 1, reused throughout)

- **Assembler:** `pasmonext --sna` (Docker image `ghcr.io/code198x/sinclair-zx-spectrum:latest`).
- **Runtime:** Emu198x (Fuse as the present learner runtime), with the register and memory views
  open — those views *are* the Primer's teaching surface. Seeing `A` change is the lesson.

## Each beat's shape

Title (the design concept) · the one idea · the felt "aha" · the trivial task + what the emulator
shows · the optional prior-language aside · the code primitive(s) · "Try this" · what it unlocks.

---

## The beats

### 1 — Assemble and Run *(toolchain)*
- **Idea:** source text → assembler → a program the Spectrum runs. There's a build step now.
- **Aha:** "I wrote text, a tool turned it into a program, the machine ran it." No magic.
- **Task:** assemble a 3-line given program that sets the border colour; load the `.sna` in
  Emu198x; see the border change. Edit the value, re-assemble, see it change again.
- **Aside:** in BASIC you typed `RUN`; here there's an assemble step between writing and running.
- **Primitive:** `OUT ($FE), A` (border = low 3 bits of A); the build-run cycle.
- **Try this:** make the border a different colour; make it black.
- **Unlocks:** the assemble-run loop repeated all course; instant visible feedback.

### 2 — LD Is Not LET *(registers)*
- **Idea:** a register is a *physical, finite, 8-bit* store named `A B C D E H L` — not an
  unlimited pool of named variables.
- **Aha:** there are only a handful, they live inside the CPU, and they hold 0–255.
- **Task:** `LD A, 5`; watch `A` in the register view. Try `LD A, 300` — see it won't fit
  (the assembler complains / the value wraps). Move a value between two registers.
- **Aside:** `LET a = 5` gave you unlimited named variables; the CPU gives you seven 8-bit slots.
- **Primitive:** `LD A, n` · `LD B, A`.
- **Try this:** copy a value through three registers; predict each before you look.
- **Unlocks:** the idea that you *orchestrate a few registers*, not declare variables.

### 3 — Everything Is a Number *(bytes have no type)*
- **Idea:** `65`, `"A"` and the pixel pattern `%01000001` are the *same byte* seen three ways.
  Hex (`$41`) is just a friendlier way to read a byte.
- **Aha:** type is interpretation, not storage. Nothing in the machine "knows" a byte is a letter.
- **Task:** `LD A, 65`, then `LD A, $41`, then `LD A, 'A'` — see identical register contents each time.
- **Aside:** BASIC kept strings and numbers apart; the machine doesn't — meaning is whatever you
  decide to *do* with the byte.
- **Primitive:** decimal / hex / character literals; reading the register view in hex.
- **Try this:** find the byte for `"Z"` and for a space; predict, then check.
- **Unlocks:** reading hex; the screen-is-bytes revelation next.

### 4 — A Street of Numbered Boxes *(memory)*
- **Idea:** memory is one flat addressable space; each address holds one byte; you own all of it.
- **Aha:** an address is just a number; storing is moving a byte to an address; reading is the reverse.
- **Task:** `LD A, n` then `LD (address), A` to poke a byte into RAM; read it back into a different
  register; watch both the register and the memory view.
- **Aside:** you met this as `POKE`/`PEEK` in BASIC — here it's your *primary* tool, not an escape hatch.
- **Primitive:** `LD (nn), A` · `LD A, (nn)`.
- **Try this:** store two different bytes at two addresses; read them back swapped.
- **Unlocks:** the screen is just a region of this street (next).

### 5 — The Screen Is Memory *(the showpiece)*
- **Idea:** the framebuffer at `$4000` is *just memory* — writing bytes lights pixels.
- **Aha:** `PLOT` was writing bytes here all along. The screen isn't special; it's mapped memory.
- **Task:** poke `$FF` to `$4000` — eight pixels appear, top-left. Poke a pattern like `%10101010`
  and see the dots. Poke a few more addresses along the top.
- **Aside:** BASIC's `PLOT`/`PRINT` hid this; now you write the screen directly, byte by byte.
- **Primitive:** `LD HL, $4000` · `LD (HL), $FF`.
- **Try this:** draw a short dashed line along the very top row.
- **Deliberate cliff-hanger (do NOT resolve here):** "Why did the byte *below* the first one
  appear far down the screen, not on the next line?" The Spectrum's thirds/interleaved screen
  layout is **the tiny game's / Shadowkeep's** territory — name the mystery, leave it open. Budget
  discipline: this beat teaches *screen = memory*, nothing more.
- **Unlocks:** the confidence that drawing is just writing bytes.

### 6 — Colour Is a Separate Map *(attributes)*
- **Idea:** colour lives in its *own* region (`$5800`), one byte per 8×8 cell
  (INK / PAPER / BRIGHT / FLASH packed in one byte).
- **Aha:** pixels and colour are stored *separately* — the root of "attribute clash."
- **Task:** poke an attribute byte at `$5800`; watch one 8×8 cell change colour without touching
  a single pixel. Change INK vs PAPER bits and see the effect.
- **Aside:** BASIC's `INK`/`PAPER` were setting these bytes for you.
- **Primitive:** `LD ($5800), A` with a packed attribute byte; the INK/PAPER/BRIGHT/FLASH bit layout.
- **Try this:** colour a 2×2 block of cells; make one BRIGHT.
- **Unlocks:** the cell-based mental model the tiny game and Shadowkeep both use.

### 7 — Test, Then Jump *(decisions)*
- **Idea:** there's no `IF` block. The CPU *compares*, sets flags, and *jumps* on a flag.
- **Aha:** control flow is assembled from "test, then jump" primitives — you build the `IF` yourself.
- **Task:** `CP n` then `JR Z, label` / `JR NZ, label` to set the border one colour or another
  depending on a value you put in `A`. Change the value, re-run, watch the path change.
- **Aside:** `IF x = 5 THEN …` becomes `CP 5` / `JR Z, …`.
- **Primitive:** `CP n` · `JR Z,e` · `JR NZ,e` · the zero flag.
- **Try this:** branch three ways (less / equal / more) using a second compare.
- **Unlocks:** all conditional logic; pairs with input next.

### 8 — The Machine Can Hear You *(input)*
- **Idea:** a key is read by reading a port; you test one bit to see if it's down. (A pressed key
  reads as **0**, not 1 — the bit is *cleared*.)
- **Aha:** input is just another read-and-branch; no `INKEY$` waiting for you.
- **Task:** read the half-row holding a single key (e.g. SPACE), test its bit, and branch — set the
  border while the key is held. Keep it to **one key, one bit**; the full keyboard is deferred.
- **Aside:** `IF INKEY$ = " "` becomes "read this half-row, test this bit."
- **Primitive:** `LD BC, $7FFE` · `IN A,(C)` · `BIT 0, A` · `JR Z/NZ`.
- **Deliberate cliff-hanger (do NOT resolve here):** the full 8-half-row keyboard matrix, and
  reading several movement keys at once, is **the tiny game's** territory (where movement motivates
  it). This beat reads *one* key. Budget discipline.
- **Try this:** use a different key; invert the logic (border changes when *not* held).
- **Unlocks:** reacting to the player — the seed of control.

### 9 — Counting Toward Zero *(repetition)*
- **Idea:** a loop is a register counted *down* and a conditional jump. `DJNZ` is the idiom; the
  CPU counts toward zero because that's what the zero flag makes cheap.
- **Aha:** `FOR`/`NEXT` is a counter plus a branch you assemble yourself.
- **Task:** a `DJNZ` loop that pokes the same byte across a row of screen memory, or repeats a
  visible action N times. Watch `B` count down in the register view.
- **Aside:** `FOR i = 1 TO 10` → `LD B, 10` … `DJNZ loop`.
- **Primitive:** `LD B, n` · `DJNZ e` · (mention `B` as the dedicated counter).
- **Try this:** halve the count; draw a shorter run. Nest a tiny delay loop inside.
- **Unlocks:** drawing loops, timed delays.

### 10 — Call, Return, and a Stack You Can See *(subroutines)*
- **Idea:** `CALL` jumps and *remembers where*; `RET` comes back. The return address lives on the
  **stack** — real memory, which you manage and can watch.
- **Aha:** `GOSUB`/`RETURN` is `CALL`/`RET`, but the stack is visible (and breakable).
- **Task:** factor "set the border" into a subroutine; `CALL` it twice from different places; peek
  the stack in the memory view and see the return address pushed and popped.
- **Aside:** `GOSUB 9000` → `CALL set_border`; but now you can *see* the return address.
- **Primitive:** `CALL nn` · `RET` · `SP` and the stack region.
- **Try this:** call the subroutine from inside the loop of Beat 9.
- **Unlocks:** structuring code; sets up the capstone.

### 11 — The Machine Trusts You *(no safety net — the mindset capstone)*
- **Idea:** a wrong address doesn't raise an error — it *corrupts something and runs on*. You are
  responsible for every byte. Debugging is observation, not error messages.
- **Aha:** there's no "Variable not found," no bounds check, no guard rail. The machine does
  exactly what you said, even when you were wrong.
- **Task:** deliberately write to the wrong address, or unbalance the stack (a `CALL` with no
  `RET`), and watch the machine misbehave — then reset and fix it. Feel the absence of guard rails.
- **Aside:** BASIC stopped with a friendly error; the bare machine just keeps going.
- **Primitive:** (none new) — `reset` to recover; the register/memory views as the debugging surface.
- **Try this:** predict what one deliberate "off-by-one" address will corrupt, then confirm.
- **Unlocks:** the careful, *observe-the-state* discipline the whole track depends on.

---

## Exit competencies (handoff to the tiny first game)

After the Primer, the learner can, without it feeling like magic:

- Assemble a `.sna` and run it in Emu198x; read the register and memory views.
- Move bytes between registers and memory; read hex.
- Write the screen ($4000) and attributes ($5800) directly.
- Compare-and-branch; read a single key and react; loop with `DJNZ`; structure with `CALL`/`RET`.
- Debug by *observing state*, knowing the machine won't catch their mistakes.

They have **not** built a game, written a game loop, moved a sprite, or learned the screen-thirds
layout or the full keyboard matrix. Those are the **tiny first game's** job — and the Primer has
deliberately left two cliff-hangers (Beats 5 and 8) pointing straight at it.

## Deferred on purpose (budget discipline — do not pull forward)

- **Screen thirds / interleaved layout** → tiny game / Shadowkeep.
- **Full 8-half-row keyboard matrix + reading several keys at once** → tiny game (motivated by movement).
- **The game loop (input → update → draw → repeat)** → tiny game (its first major technique).
- **Sprites, masking, pre-shift, Y-sort, collision** → tiny game (simple) → rendering games (advanced).

## Open for the author

- Exact split: 11 beats ≈ 11 units is the working assumption; Beats 2–3 (registers / bytes) or
  9–10 (loops / subroutines) could merge if a unit feels too thin, but resist merging to "add
  weight" — thin is fine here.
- Whether Beat 1 sets the border via `OUT` or pokes a single screen byte as the first visible
  result. Border is one instruction and instant; the screen byte previews Beat 5. Lean: border.
- A real name for the Primer (working: "Meet the Machine").
