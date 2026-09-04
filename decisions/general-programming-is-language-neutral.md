# Decision: General Programming is taught in pseudocode alone

## The decision

**General Programming drops Sinclair BASIC.** Every idea is taught in one neutral
pseudocode and nothing else. The Spectrum-specific material is **retired rather than
relocated**: *Meet BASIC* already teaches every piece of it, unit by unit.

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
# a comment runs to the end of the line

LET score = 0                        assignment
LET score = score + 10               a box updated from its own value

SHOW "Score: ", score                output; the comma joins and adds nothing
ASK "Your name? " INTO name          input

IF guess = 7 THEN SHOW "Correct!"    one-line form, no second path
IF guess = 7 THEN … END              block form
IF … THEN … ELSE … END               two paths
IF … THEN … ELSE IF … THEN … END     a chain, closed once

FOR i = 1 TO 10 … END                counted loop
FOR EACH score IN scores … END       over a list
WHILE lives > 0 DO … END             test at the top
REPEAT … UNTIL guess = 7             test at the bottom

DEFINE divider … END                 a job with a name
DEFINE double(n) … RETURN n * 2 … END a job given a value, giving one back
CALL divider                         do the job
CALL draw(10, 5)                     do the job, with values
LET x = double(5)                    use what it hands back

LET scores = [10, 20, 30]            a list
LET first = scores[1]                one item, counting from 1
LET scores[2] = 99                   change one item
APPEND 40 TO scores                  grow it
LENGTH(scores)                       how many

+ - * /        = <> < > <= >=        AND OR NOT
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
  A bare `END` is enough at this course's nesting depth — the deepest construct is an
  `ELSE IF` chain inside a `REPEAT`, where `UNTIL` closes the outer one and only a single
  `END` is ever in view. `END IF` / `END FOR` is the fallback if that stops being true.
- **A condition takes a connector; a range does not.** `IF … THEN`, `WHILE … DO`: where a
  condition could run on, a word marks where the body starts. `FOR i = 1 TO 10` is
  self-delimiting, so it takes none. The asymmetry is the rule, not an oversight.
- **The comma joins and adds nothing.** `SHOW "Hello, ", name` prints `Hello, Ada`;
  `SHOW "Hello,", name` prints `Hello,Ada`. This is deliberate: two of the course's
  debugging bullets teach that the space belongs inside the quotes, and an auto-spacing
  comma would silently delete both lessons. Every language makes a learner think about
  this once.
- **`#` for comments.** Unit 3 already annotates its pseudocode in a trailing column with
  no marker, which is fine as decoration and breaks the moment anything parses it. `#` is
  quiet, collides with nothing else here, and is not a marker anyone has to unlearn.
- **Two shapes of job, and the difference is the point.** `CALL divider` does a job;
  `LET x = double(5)` uses one that hands a value back. Keeping them visibly different
  teaches the distinction rather than hiding it. `CALL` takes no empty parentheses when
  there is nothing to pass — `CALL divider`, not `CALL divider()`.
- **Lists count from 1.** The first item is item 1, because for an absolute beginner the
  alternative is a stumbling block that is not the lesson. Where indexing starts is a
  language's own convention — which the architecture record places downstream — and the
  course already primes the learner for it, in unit 8's bullet on deciding "whether you're
  counting *things* or counting *from zero*". This is the most arguable call in the
  grammar; it is written here so it can be argued with.
- **`RETURN` here is not BASIC's `RETURN`.** Ours hands a value back. Sinclair BASIC's
  ends a `GO SUB` and hands back nothing — closer to our `END`. Meet BASIC inherits that
  collision and should name it, since the learner meets the same word twice meaning
  different things.

The grammar is fixed now, before the units are rewritten, so that the rewrite happens
once. It is also deliberately small and non-general: it runs this course's examples and
is not a language anyone writes programs in. If it ever grows past that, the growth
needs its own record.

## What happens to the BASIC

It is retired from General Programming rather than migrated, because *Meet BASIC*
already teaches every piece of it — at more length, and without apologising for the
language:

| General Programming taught | Meet BASIC unit that already owns it |
|---|---|
| Line numbers set execution order | 2 — "The Line Number Is an Address" |
| `PRINT`, and joining text to a value | 3 — "PRINT, Properly" |
| The `$` sigil, the single-letter rule, the C64's first-two-letters | 4 — "LET, and What You May Name" |
| `INPUT` | 5 — "INPUT — the Program Listens" |
| `IF` / `THEN` | 6 — "IF / THEN, the Spectrum Way" |
| `FOR` / `NEXT` | 7 — "FOR / NEXT Counts For You" |
| `GO TO` as a loop, `GO SUB` by line number | 8 — "GO TO, GO SUB, and the Game Loop" |
| The report lines, read as real diagnostics | 15 — "When It's Wrong" |

**That table is the strongest evidence for this decision.** The material was misplaced
by the architecture record's rule, and duplicated besides: General Programming has been
teaching a compressed,
apologetic version of a fifteen-unit track that already exists downstream and does the
job properly. What General Programming unit 4 covers in a parenthesis, Meet BASIC unit 4
covers as its subject. What General Programming unit 11 lists in three bullets, Meet
BASIC unit 15 is about.

So nothing needs writing to receive it, and this record mandates no migration. The
`.bas` step files and their 21 verified screenshots stay where they are; whether a Meet
BASIC unit wants any of them is that track's call.

Unit 11's debugging *method* — observe, localise, read the line, do not guess — is
language-neutral and stays in General Programming. What leaves is the catalogue of
Spectrum reports, which Meet BASIC unit 15 already carries. The lesson that travels is
that a learner's tools write them a message naming a problem and a place; each
`Meet <language>` shows its own, since an assembly learner meets an assembler error and
never `2 Variable not found`.

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

- **Unit 10 loses `STOP`.** A `DEFINE` block is a declaration, so the main program cannot
  fall into one. That deletes the `STOP` line, the `9 STOP statement` report, and the
  "put a stop above the block or it runs twice" debugging bullet — all of them
  consequences of BASIC identifying a block by line number rather than holding it apart.
- **Unit 8 stops writing a cheque it cannot cash.** Its prose already says a counted loop
  is how you "fill a row, draw a grid, **step through a list**, or lay out a level", in a
  course with no list. `FOR EACH … IN` makes that true.

## The syllabus grows, deliberately

`ELSE`, parameters with `RETURN`, and lists are three universal ideas the track did not
teach. Adding them is a **narrow, deliberate amendment** to
[front-of-curriculum-architecture.md](front-of-curriculum-architecture.md), which
enumerates General Programming as "what a program is; sequence, variables, input and
output, conditionals, loops, subroutines". Lists and parameters are not in that list.
They are added here on the same grounds the record uses throughout: they are true in
every language, so by its own placement rule — "a concept true in every language …
belongs in General Programming, taught once" — they belong here rather than being met
separately in each `Meet <language>`. The amendment follows the precedent of
[foundations-logic-and-gates.md](foundations-logic-and-gates.md), which amends the same
record explicitly and narrowly rather than quietly widening it.

By one-concept-per-unit this is three new units, not three additions to existing ones.
Unit 7 already carries `IF`, the comparison operators and `AND`/`OR`; unit 10 already
carries call, return and reuse. The unit count is not fixed
([curriculum-structure.md](curriculum-structure.md)), so the track grows rather than
displacing anything.

Sequence matters for two of them. Lists are useless before loops, so they follow unit 9;
parameters need a plain named job first, so they follow unit 10. Debugging stays last.
The content pass settles the exact placement and numbering.

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
- A `SHOW` relies on the comma to supply a space. → the comma joins and adds nothing; put
  the space inside the quotes.
- A list is indexed from 0. → count from 1, per the grammar; where indexing starts is a
  downstream language's business.
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
