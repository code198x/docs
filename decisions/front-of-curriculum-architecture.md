# Decision: the front-of-curriculum architecture

**Status:** ACCEPTED — 2026-06-05 (proposed and accepted the same day). Designed in
one pass per the "rethink the whole front" call; all load-bearing decisions resolved,
leaving only naming and one grouping choice for build time. **Supersedes** the two
seeds [`number-systems-primer.md`](number-systems-primer.md) and
[`cross-system-foundations.md`](cross-system-foundations.md), and amends the front
of [`curriculum-structure.md`](curriculum-structure.md). Built natively to the
raised bar ([`incremental-construction-units.md`](incremental-construction-units.md)).
The General Programming primer (Foundations) is built; the rest is the architecture
to build against.

## The problem it fixes

Three faults, one root:

1. **The BASIC games teach the language, not games.** Volume-1 "First Programs"
   skills are bare keywords — Story Builder = `PRINT`/`CLS`/`INPUT`/strings;
   Lucky Number = `LET`/`IF`/`GO TO`/`RND`. Each game's unit-01 re-teaches
   first-principles (typing, `RUN`, line numbers, the dark-screen setup) before
   the game proper. There is no primer, so the language is taught game-by-game,
   and every game opens with a discontinuity (Story Builder u1 ends on a throwaway
   welcome demo; u2 starts a fresh program with an unexplained
   `BORDER 0: PAPER 0: INK 7: CLS`).

2. **"General programming" was conflated with BASIC.** *Meet the Machine* assumes
   "variables, loops, conditionals, subroutines — our BASIC course." But that
   makes BASIC a prerequisite for assembly.

3. **Not every target machine has BASIC.** The NES has no built-in BASIC or HLL.
   A learner targeting NES assembly has nowhere on-platform to learn to program —
   so a BASIC-keyed on-ramp strands them.

The root: the front of the curriculum had no clean separation between *learning
to program* (universal), *learning a language* (BASIC, per-platform), and
*learning a machine* (per-system).

## The decision — the front layers

**Refined 2026-06-05** to separate *learning the machine* from *learning a
language*. "Meet the Machine" becomes a per-system **briefing** (what the machine
was, its era, the constraints it imposed — colours, sound, memory); the language
on-ramps become the **"Meet \<language\>"** family (Meet BASIC, Meet Assembly, and
later Meet C, Meet FORTH), so a machine is approached through whatever language
*fits* it. One machine briefing then feeds every language path for that machine.

```
General Programming primer   (language-neutral, universal — every learner)
        |
        v
Meet the Machine — per-system briefing
        |   what it was · its era · its constraints (colours, sound, memory),
        |   shown concretely — the "why it's limited" lives here
        v
   +----+----------------------+---------------------------+
   v                           v                           v
Meet BASIC                Foundations                 Meet C · Meet FORTH
   (where BASIC exists)    (Number Systems + Bit        (machines those fit —
   |                        Logic; the asm bridge)       e.g. C on Amiga/ST,
   v                       v                             FORTH on the Jupiter Ace)
BASIC games           Meet Assembly                     |
(game-dev ideas)          |                             v
                          v                          their games
                     assembly games -> flagship
```

Every box except General Programming is per-language and/or per-machine; the
General Programming primer is the one universal, cross-platform base. The "Meet
\<language\>" family is open-ended — a machine gets on-ramps for the languages
that actually shipped on it.

### The machine/language split (refinement, 2026-06-05)

The original *Meet the Machine* taught the Z80 **through** assembly — you learned
the screen by writing bytes to it. That conflated two jobs. The split:

- **Meet the Machine — the machine, not a language.** A per-system briefing: what
  this machine was, when it sat, who used it, and the **specific constraints it
  imposed** — the colour limits, the sound hardware, the memory, the quirks. This
  is the concrete home for the display/sound/memory limits that earlier had no
  natural place (the CRT/sound question): "15 colours with attribute clash, a
  one-bit beeper, 48K" belongs *here*, shown running on the machine, not lectured
  abstractly upstream. It must **stay concrete** — show the constraints live — or it
  trips the same over-extraction wire one level up. It teaches you *about* the
  machine; it stops short of teaching you to write a language for it.
- **Meet \<language\> — the language, on that machine.** Meet BASIC, Meet Assembly,
  and later Meet C, Meet FORTH. Each teaches a language's toolkit, assuming the
  General Programming concepts and the machine briefing. A machine gets the
  on-ramps for the languages that fit it: **the Jupiter Ace's native ROM language
  was FORTH** — Meet FORTH is its only honest on-ramp; **C is how most people
  shipped on the Amiga / ST** — Meet C belongs there. One *Meet the Machine:
  Spectrum* briefing feeds *both* Meet BASIC and Meet Assembly for the Spectrum,
  with the hardware taught once.

**Consequence — real rework.** The just-converted *Meet the Machine* (15 units,
the v3.0 conversion) re-splits: the machine-orientation parts (what the screen is,
the colour map, the constraints) become the **briefing**; the Z80/assembly toolkit
(LD, compare-and-jump as `IF`, loops, subroutines, the build-run loop, debugging)
becomes **Meet Assembly**. The conversion work isn't lost — it's re-cut along this
seam. Budget it as a known cost of adopting the split.

**Naming.** The "Meet \<language\>" family is settled in spirit (Meet BASIC, Meet
Assembly, Meet C, Meet FORTH); *Meet the Machine* keeps its name in its new
briefing role. The **General Programming primer**'s name is still open — it sits
*outside* the Meet-a-language family (it's language-neutral), so "Meet Programming"
is tempting but may mislead; TBD.

### Layer 1 — General Programming primer (language-neutral, universal)

A short primer teaching the concepts that are true in *every* language: what a
program is; sequence; variables; input/output; conditionals; loops; subroutines.
**Language-neutral**, so it serves every learner — including those whose target
machine (NES) has no BASIC. It is the universal first step and the new prerequisite
for everything downstream.

- `kind: teaching` module, **cross-platform** (lives outside any one system).
- Replaces "our BASIC course" as the stated prerequisite of every *Meet the
  Machine* and of the BASIC primer.
- **Concreteness — DECIDED (2026-06-05): pseudocode + a single concrete vehicle.**
  [`cross-system-foundations.md`](cross-system-foundations.md) warns that
  pure-abstract primers go dry, and a language-neutral primer is the sharpest case.
  Resolution: each concept is stated in neutral pseudocode and shown running in
  *one* concrete vehicle — **Spectrum BASIC**, as the gentlest — with the prose
  framing it as "here in BASIC; the same idea everywhere." Concrete enough to avoid
  dry, honest that the concept transcends the vehicle. A NES learner reads the BASIC
  illustration as an *example*, not a track they must complete.

### Layer 2a — Meet BASIC (per-platform language primer)

*(Named "Meet BASIC" per the machine/language split above; described as "the BASIC
primer" throughout this section.)*

Teaches **Sinclair BASIC the language** — the *fat* primer: the full toolkit as
standalone one-concept beats, the way *Meet the Machine* teaches the Z80 toolkit.
It **assumes** the General Programming primer (the learner already knows what a
loop or a conditional *is*), so it teaches BASIC's *expression* of each — syntax,
idiom, the Spectrum's keyword-entry, the gotchas — not the underlying concept.

Illustrative beats (count is a marker, not a contract —
[`curriculum-structure.md`](curriculum-structure.md)):

- Type a line, `RUN`, the report line — the build-run loop on a live machine.
- Line numbers as addresses; editing, replacing, `LIST`, deleting.
- Several lines in order; `CLS`; numbering in tens (the reserved-gap habit —
  [`incremental-code-samples.md`](incremental-code-samples.md) rule 7).
- The dark-screen canvas — `BORDER`/`PAPER`/`INK` (the setup every game opens on,
  finally taught where it belongs, not smuggled into a game's u1).
- `INPUT` and a variable; string vs numeric variables; `LET` and arithmetic.
- `IF`/`THEN`; `FOR`/`NEXT`; `GO TO`; `GO SUB`/`RETURN`; `RND`/`INT`.
- When it's wrong, see why — read the program's state and the report line (the
  debugging spine the bar requires).

Per-platform: a **C64 BASIC primer** and **Amiga AMOS primer** are parallels of
the same shape, built when those tracks are. The Spectrum one is canonical (launch
platform). The **AMOS primer is expected to be slightly more involved** — AMOS is
an in-emulator environment (you work inside the Amiga, not just type lines), so its
primer carries more setup than a built-in-BASIC primer does.

### Layer 2b — Foundations (cross-platform, the bridge to low-level)

Machine-independent primers that sit between general programming and *Meet the
Machine* — the foundation the assembly on-ramp stands on. The BASIC track barely
needs them; assembly needs them constantly.

- **Promote (Tier 1) — the whole of Foundations:** **Number Systems**
  (decimal/binary/hex, place value, bits/nibbles/bytes, two's complement) and
  **Bit Logic** (AND/OR/XOR/NOT, masking, shifting). Pass all three of the seed's
  tests; likely one combined primer or two small ones.
- **Display / Sound — DECIDED (2026-06-05): not promoted; cover lightly,
  just-in-time, concretely.** Tempting as Tier 2, but rejected. CRT *physics*
  (scanlines, phosphor) isn't worth a foundation — it only matters for advanced
  per-machine beam-racing, taught when a game needs it. What modern (LCD/LED-raised)
  learners actually lack is simpler and lands best *concretely*: that the screen
  **is** memory you write to, that there's a fixed refresh you **sync** to, and
  **why** the colours and sound are so limited. Those are felt — the byte becoming
  a pixel, the one-bit beeper heard — far better than lectured upstream. So the
  display and sound models stay **in *Meet the Machine* and the games**, covered
  with a light "here's why it's this limited" touch at the point of first use. No
  upstream display/sound primer.
- **Keep concrete (Tier 3):** the CPU model, memory model, game loop, 2D space —
  stay in *Meet the Machine*, where you see the byte become a pixel. (Same logic
  as display/sound: concrete beats abstract for everything machine-shaped.)

### Layer 3 — Meet the Machine (briefing) + Meet \<language\> + games (per-system)

Reshaped by the machine/language split above. The assembly decisions still hold,
re-cut along the seam:

- *Meet the Machine* is now the per-system **briefing** (the machine + its
  constraints), not the assembly course; **Meet Assembly** carries the Z80/assembly
  toolkit. The current converted *Meet the Machine* re-splits into the two.
- Its prerequisite line changes from "our BASIC course" to **the General
  Programming primer** (so BASIC-less learners qualify).
- *Meet Assembly* may **assume** number/bit literacy once Foundations exists,
  letting units like "Everything Is a Number" / "Working With Bits" lean out (the
  seed's "strengthens the existing primers" point) — or drop, now that the machine
  briefing covers what the machine *is* and Foundations covers number systems.

## How the BASIC games re-scope

With the language taught in the BASIC primer, the **First Programs** games stop
being keyword-delivery vehicles and become **game-dev-idea** vehicles, each using
the toolkit the learner already has:

- **Story Builder** — building output from user input (the mad-lib shape, screen
  layout, a title) — not "here is `INPUT`".
- **Lucky Number** — chance as a design material, feedback loops, a guess-until-win
  loop — not "here is `IF`/`RND`".
- ... and so on through Volume 1.

Each game opens as a real program (the dark canvas and typing are primer'd), and
each unit's diff stays within the ~5–8 line budget
([`incremental-code-samples.md`](incremental-code-samples.md)) — the discontinuity
that started this is designed out at the root, not patched per game.

The later phases (*Patterns of State*, *Worlds and Rules*, *Stories and Systems*)
already teach game-dev ideas (arrays, AI, physics, parsers) and need far less
re-scoping than Volume 1.

## Sequencing and build order

The architecture is built **top-down**, native to the v3.0 bar, before the
existing games are converted — because converting the games first would rework
every game intro twice (the thing the "rethink the front" call avoids):

1. **General Programming primer** — greenfield, native-to-bar; unblocks everything.
2. **Spectrum BASIC primer** — the language; lets the games re-scope cleanly.
3. **Re-scope + convert the Volume-1 BASIC games** — now game-dev-idea vehicles,
   each at the v3.0 bar, in the agreed order (Story Builder → rest of Volume 1).
4. **Foundations (Number Systems + Bit Logic)** — greenfield; bridges to assembly.
   Buildable in parallel; not on the BASIC critical path.
5. Volume 2+ BASIC games and the per-system primers follow.

**October interaction — CONFIRMED fits (2026-06-05).** The launch content is
Spectrum-only and includes the BASIC games; this adds two new build items (the
General Programming primer and the Spectrum BASIC primer) ahead of them. With the
runway from June, this fits the window — no scope concern. The guiding stance still
holds if anything slips: per
[`october-2026-launch-spec.md`](october-2026-launch-spec.md), ship fewer
fully-formed games behind a real primer rather than more games at the old bar.

## Relationship to the raised bar

Everything here is **new content built native to the bar** (incremental milestones,
multi-media honest captures, debugging spine, accessibility) — not conversion. It
**completes the foundation** of the on-ramp; per the depth-before-breadth stance it
is foundation-completion, not the breadth the bar gates, so it is welcomed by the
bar rather than blocked by it.

## Resolved (2026-06-05)

- **General Programming primer concreteness** — pseudocode + a single concrete
  vehicle (Spectrum BASIC), framed as universal. (Layer 1.)
- **Display / Sound** — *not* a Foundations primer; covered lightly and concretely
  at the point of first use in *Meet the Machine* and the games. Foundations is
  Number Systems + Bit Logic only. (Layer 2b.)
- **October** — the two-primers-first ordering fits the launch window.
- **C64 BASIC / AMOS primers** — per-platform parallels of the Spectrum primer;
  AMOS slightly more involved (in-emulator). (Layer 2a.)

## Open questions (decide before/at build)

1. **Naming** — the General Programming primer and the Foundations primer(s) (the
   seed floated "Meet the Numbers" / "How Computers Count"). Deferred — name at build.
2. **Number Systems + Bit Logic** — one combined primer or two small ones.

## Drift triggers

- A BASIC game's unit-01 re-teaches typing/`RUN`/line-numbers/the dark canvas —
  that belongs in the BASIC primer; the game opens as a real program.
- A "First Programs" game's stated skill is a bare keyword (`IF/THEN`, `FOR/NEXT`)
  rather than a game-dev idea — the keyword is the primer's job now.
- *Meet the Machine* (any system) names "the BASIC course" as its prerequisite
  instead of the General Programming primer.
- The General Programming primer reads as dry abstraction with no concrete
  illustration — the over-extraction failure the seed warned about.
- A general-programming concept (what a loop *is*) is taught in Foundations or
  *Meet the Machine* — it belongs in Layer 1, once.
- Foundations grows a per-chip specific (a SID register, a ULA quirk) — that
  belongs in *Meet the Machine*.
