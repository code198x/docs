# Decision: General Programming is taught in pseudocode alone

## The decision

**General Programming drops Sinclair BASIC.** Every idea is taught in one neutral
pseudocode and nothing else. The `.bas` examples, the screenshots, and the
Spectrum-specific material move to *Meet BASIC*, where they open the track.

The pseudocode is a **fixed grammar**, written down below, rather than prose invented
per unit. Units author to it.

## Why

[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md) already
decides this; the track had drifted from it. That record says General Programming is

> the one universal step … **Language-neutral, so it serves a learner whose machine has
> no BASIC at all.**

and, in "Where a concept belongs":

> **A language's expression of a concept** — syntax, idiom, the gotchas — belongs in
> that language's `Meet <language>`.

Measured against that rule, most of the BASIC in the track was misplaced. An audit of
all eleven units found the concrete language carrying: the single-letter `$` rule for
text variables, line numbers setting execution order, `GO TO` standing in for a
loop-until, `GO SUB 100` standing in for a name, and the Spectrum's report lines. Each
one is Sinclair BASIC's *expression* of an idea, which the architecture record places
downstream.

The cost fell hardest on the learner the record was written to protect. A learner
heading for assembly runs General Programming → Meet the Machine → Numbers & Bits →
Meet Assembly and never meets a BASIC. Until now, that learner was taught a 1982
string-naming rule on the way past.

**Concreteness is not abandoned, it changes form.** What the BASIC listing was standing
in for — a thing to look at, so nothing stays abstract — is better served by the
diagrams and trace tables the track has been gaining: a flow diagram shows the shape a
listing hides, and a trace table shows a value changing over time. The failure mode to
avoid is the one
[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md) names for itself,
going pure-abstract with nothing to look at. Diagrams and traces are the answer to it
here.

## The pseudocode

One grammar, used by every unit. Keywords are chosen to read plainly; several are
borrowed from BASIC where BASIC was already clear.

```text
LET score = 0                       assignment
LET score = score + 10              a box updated from its own value

SHOW "Score: ", score               output; comma joins
ASK "Your name? " INTO name         input

IF guess = 7 THEN SHOW "Correct!"   one-line form, no second path
IF guess = 7 THEN … END             block form
IF … THEN … ELSE … END              two paths
IF … THEN … ELSE IF … THEN … END    a chain, closed once

FOR i = 1 TO 10 … END               counted loop
WHILE lives > 0 DO … END            test at the top
REPEAT … UNTIL guess = 7            test at the bottom

DEFINE divider … END                a job with a name
CALL divider

+ - * /       = < >       AND OR
```

Notes on the choices:

- **`LET` keeps `=` as assignment**, so `LET score = score + 10` still teaches that `=`
  means *put this in the box*, not *equals* — and `IF guess = 7` still teaches the same
  symbol doing a second job as a question. Both lessons survive the move intact; they
  were never Sinclair's.
- **Three loops, three shapes.** `FOR` when you know how many, `REPEAT … UNTIL` when you
  do not, `WHILE … DO` when the test belongs before the first pass. The course currently
  teaches the first two; `WHILE` exists in the grammar and is not yet taught.
- **No type sigils and no naming rules.** Names are names. The `n$` single-letter trap
  disappears rather than being restated.
- **`ELSE`, and `ELSE IF` as a chain.** `ELSE IF` introduces no new keyword — it is
  `ELSE` followed by another test — and the whole chain closes with a single `END`
  rather than nesting one per branch. This matters more than it looks: the course's
  central example is three-way (too low, correct, too high), and without a chain it can
  only be written as three separate unrelated tests, which is what the track does today
  and which hides that the three cases are one decision.
- **`END` closes `FOR`, `WHILE`, `DEFINE` and the block `IF`.** `UNTIL` closes `REPEAT`.

The grammar is fixed now, before the units are rewritten, so that the rewrite happens
once. It is also deliberately small and non-general: it runs this course's examples and
is not a language anyone writes programs in. If it ever grows past that, the growth
needs its own record.

## What moves to Meet BASIC

Not deleted — relocated to the track that owns it. It gives *Meet BASIC* a first
chapter built from material that already exists and is already verified:

| From | What |
|---|---|
| Units 1–11 | The `.bas` step files and their 21 verified screenshots |
| Unit 2 | Line numbers set execution order, not typing order |
| Units 4, 5 | The `$` sigil and the single-letter rule for text variables |
| Unit 9 | Building a loop-until from a test and `GO TO` |
| Unit 10 | `GO SUB` / `RETURN` identifying a block by line number |
| Unit 11 | The Spectrum's report lines, read as real diagnostics |

Unit 11's debugging *method* — observe, localise, read the line, do not guess — is
language-neutral and stays. What moves is the specific catalogue of Spectrum reports.
The lesson that travels is that a learner's tools write them a message naming a problem
and a place; each `Meet <language>` then shows its own real ones, since an assembly
learner meets an assembler error and never `2 Variable not found`.

## What this changes in the units

Consequences worth naming, because each removes an apology the track was making:

- **Unit 9** loses "BASIC has no repeat-until, so we build one out of pieces." With
  `REPEAT … UNTIL` in the grammar the construction is gone and the idea is stated
  directly. One "What you've learnt" bullet goes with it.
- **Unit 10** loses "the BASIC we're using has no names for blocks at all." `DEFINE
  divider` / `CALL divider` is the idea the unit was reaching for through a line number.
- **Units 4, 5 and 11** lose the `n$` trap, its restatement, and its callback.
- **Unit 7** currently makes a virtue of having no second path — "there is no second
  path, just a step that is or isn't taken", in the prose and in its flow diagram's
  caption. With `ELSE` in the grammar that framing goes. The two-branch decision is a
  universal idea the course did not teach, and by one-concept-per-unit it wants its own
  unit after 7 rather than being folded into it; unit 7 is already carrying `IF`, the
  comparison operators and `AND`/`OR`. The unit count is not fixed
  ([curriculum-structure.md](curriculum-structure.md)), so this is an addition, not a
  displacement.
- **Units 7 and 9's three-way hints** become one `ELSE IF` chain instead of three
  unrelated `IF`s. The chain says what the old shape only implied: that too low, too
  high and correct are three outcomes of a single decision, exactly one of which happens.

## Relationship to other decisions

- **[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md)** — the
  governing record. This one applies its placement rule to a track that had drifted from
  it; it does not change it.
- **[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md)** — its build
  convention cites "pseudocode + one concrete vehicle (Sinclair BASIC), **exactly as
  Layer 1**", meaning General Programming. That citation is now false and is corrected
  in place. Numbers & Bits *keeps* its concrete vehicle on its own merits: it sits on the
  assembly arm, after the learner has chosen a machine, and Spectrum BASIC suits its
  subject (`BIN`, `CODE`/`CHR$`). This record does not touch it.
- **[examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md)** —
  still binding, and still governs every track with runnable examples. General
  Programming will have no runnable examples once this lands, so the record no longer
  applies to it. General Programming is not in violation of it; it is out of its scope.
- **[in-curriculum-wasm-playground.md](in-curriculum-wasm-playground.md)** — that
  playground needs a WASM assembler and an emulator, which is why it is post-launch. A
  simulator for *this* pseudocode needs neither, because the language is ours. Held open
  as a separate question, specified separately if taken.

## Drift triggers

- A General Programming unit shows Sinclair BASIC, or any named real language, as an
  example. → it belongs in that language's `Meet <language>`.
- A unit teaches a rule that is true only of one language — a naming restriction, a
  sigil, a line-number behaviour. → the same.
- A unit's pseudocode uses a keyword or form not in the grammar above. → change the unit,
  or amend the grammar here first; do not let a second dialect start.
- The track goes fully abstract with nothing to look at — no diagram, no trace, no worked
  example. → the over-extraction failure; add the concrete thing.
- The pseudocode grows features nothing in the course teaches. → it is becoming a
  language; that needs its own record.

## Open, not decided here

- **Where the two-branch decision is taught.** `ELSE` is in the grammar and the idea is
  in scope; whether it extends unit 7 or becomes a unit of its own is settled by the
  content pass, with a new unit the expected answer.
- **Whether `WHILE` gets taught.** It is in the grammar; no unit uses it.
- **A pseudocode simulator.** Stepping through a program in the page, showing the current
  line, the variable boxes and the output — with the trace table as its no-JS fallback,
  generated rather than hand-authored. Attractive and cheap relative to the WASM
  playground, but a new component and a new pattern, so it gets specified before it gets
  built.

## Status

Active. Captured 2026-09-04. Applies
[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md) to the
General Programming track; corrects the citation in
[foundations-numbers-and-bits.md](foundations-numbers-and-bits.md); takes General
Programming out of the scope of
[examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md) until a
simulator gives it runnable examples again.
