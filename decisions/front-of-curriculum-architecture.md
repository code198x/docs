# Decision: the front-of-curriculum architecture

How a learner gets from knowing nothing to writing code on a specific machine, and what each layer is called.

## The decision

One universal step, then a per-machine branch that forks by language. **Foundations is a section of the site, not a sequence every learner walks** — only General Programming is universal.

```
General Programming                    (universal — every learner)
        |
   Meet the Machine                    (per-system briefing, taught once per system)
        |
   ┌────┴──────────────────────┐
   v                           v
Meet BASIC              Numbers & Bits ──────→ Maths for Games
   |                           |
   v                           v
BASIC games            From Source to Silicon
   |                           ^        |
   └─── "why is this ──────────┘        v
         so slow?"                Meet Assembly
        (the bridge)                    |
                                        v
                                 assembly games

Game Feel — once a game of yours runs, on either arm
```

**General Programming is the one universal step.** What a program is; sequence, variables, input and output, conditionals, loops, subroutines. Language-neutral, so it serves a learner whose machine has no BASIC at all.

**A machine track opens with the briefing.** *Meet the Machine* is a per-system briefing: what this machine was, when it sat, and the specific constraints it imposed — the colour limits, the sound hardware, the memory. It teaches you *about* the machine and stops short of teaching you a language for it. One briefing feeds every language track for that system, so the hardware is taught once.

**From Source to Silicon is the assembly arm.** Numbers & Bits left it: see
[foundations-is-language-neutral.md](foundations-is-language-neutral.md), which found the
BASIC track already working around the same material with a `POKE USR` recipe.

It lives in the Foundations section because it is cross-platform — shared by four assembly tracks, so taught once rather than four times — but it is not universal. It is what an interpreter, a compiler and an assembler each are, and why *when* the translating happens decides whether an enemy chases you sixty times a second or stutters. That is a question a learner has to have earned, which is why it stays on the arm rather than joining the language-neutral shelf.

**From Source to Silicon is also the bridge back from BASIC.** A BASIC learner reaches it not as a prerequisite but as an answer, after games have made the question real — *why is this so slow?* It is written for that arrival, timing a BASIC loop that crawls while doing almost nothing. So it is offered from the BASIC games, late, rather than gating them; and because it ends by explaining what assembly buys, it is the path by which a BASIC learner becomes an assembly learner. That route matters: BASIC is the on-ramp audience, and nothing else carries them across.

**The Craft is two modules with two entry points, neither of them upfront.** *Maths for Games* — the cheap answer to sums these machines are hostile to: a lookup instead of a sine, a comparison with no square root in it — needs Numbers & Bits behind it. It stays on the assembly arm on its own merits rather than by inheritance, now that Numbers & Bits has left it: the techniques answer questions a game running too slowly raises, and a reader who has not hit that wall has nothing to hang them on. *Game Feel* — grace windows, visible feedback, ending dwells — needs a working game rather than any particular number sense, so it sits beside the games on either arm, once the first moving version runs. Neither gates a machine track.

**Then a language, named for the language.** The `Meet <language>` family — Meet BASIC, Meet Assembly, Meet C, Meet FORTH — teaches a language's toolkit on that machine. A machine gets on-ramps for the languages that shipped on it: FORTH is the Jupiter Ace's only honest on-ramp; C is how most people shipped on the Amiga and ST.

## Vocabulary

These are the terms the site, the catalogues and these records all use.

| Term | Means |
|---|---|
| **Foundations** | The cross-platform *section*: General Programming, Numbers & Bits, From Source to Silicon. A folder, not a sequence — its modules have different audiences. |
| **The Craft** | The transferable-technique section: Maths for Games (needs Numbers & Bits) and Game Feel (needs a working game). Two entry points, not one. |
| **Meet the Machine** | A per-system briefing about the hardware. Never a language course. |
| **Meet \<language\>** | A language on-ramp: Meet BASIC, Meet Assembly, Meet C, Meet FORTH. |

The name of a module says which of these it is. A module teaching a language is named for that language.

## Why the machine and the language are separate

The original *Meet the Machine* taught the Z80 **through** assembly — you learned the screen by writing bytes to it. That conflated two jobs, and the conflation caused three faults:

1. **BASIC was an accidental prerequisite for assembly.** *Meet the Machine* assumed "variables, loops, conditionals, subroutines — our BASIC course", so a learner heading for assembly was routed through BASIC to get there.
2. **Machines without BASIC stranded the learner.** The NES has no built-in BASIC or HLL. A BASIC-keyed on-ramp leaves an NES learner nowhere to start.
3. **The hardware was taught once per language.** A learner doing both BASIC and assembly on one machine met its constraints twice, and a machine with three tracks would teach them three times.

Splitting the briefing from the language fixes all three at the root: the hardware is taught once per system, and each language on-ramp assumes it.

The constraints belong in the briefing specifically because they are **felt, not lectured**. "15 colours with attribute clash, a one-bit beeper, 48K" lands when shown running on the machine. That is why there is no upstream display or sound primer in Foundations, and why the briefing must stay concrete.

## Where a concept belongs

- **A concept true in every language** — what a loop *is*, what a variable *is* — belongs in General Programming, taught once.
- **Number and bit literacy** — binary and hex, two's complement, masking, shifting — belongs in Numbers & Bits, on the assembly arm.
- **How source becomes something a machine runs** — interpreting versus assembling, and why that choice decides whether a game keeps up — belongs in From Source to Silicon. It is the last step before Meet Assembly, and the answer a BASIC learner arrives at from the other direction once their game runs out of speed.
- **A technique any game needs, in a form no chip has yet made local** — a direction as a lookup, a grace window as a timer — belongs in The Craft, taught beside the games rather than before them.
- **A machine's own constraints** — its colour map, its sound hardware, its memory — belong in that machine's briefing.
- **A language's expression of a concept** — syntax, idiom, the gotchas — belongs in that language's `Meet <language>`.

## Applying it to the four systems

The split is built for every language except assembly, and the machine briefing exists on no system in finished form. Every non-assembly track already carries a correctly named on-ramp — `meet-basic`, `meet-c64-basic`, `meet-amos`, `meet-blitz` — while all four assembly tracks still call theirs *Meet the Machine*. That is why the Spectrum currently serves two different pages under that one title, on `/machine/` and on `/assembly/`.

The work is not a file move. The seam runs through the middle of the existing units rather than between them: a single assembly unit introduces a machine fact and then teaches the instruction that exercises it, because teaching the machine *through* assembly is the conflation this record exists to end.

**The sequence is decided separately, in [splitting-the-assembly-on-ramp.md](splitting-the-assembly-on-ramp.md).** That record owns the order, the per-system scope, the `machine` pseudo-track segment, and the accepted temporary duplication. This record owns only what the layers are and what they are called.

## Drift triggers

- Reading "Foundations" as a sequence every learner walks. It is a section holding modules with different audiences: General Programming is universal, Numbers & Bits and From Source to Silicon are the assembly arm.
- Gating Meet BASIC on Numbers & Bits or From Source to Silicon, or presenting either as required before any machine route.
- A module named *Meet the Machine* that teaches a language, or a `Meet <language>` module that teaches the hardware.
- Two modules on one system sharing a display name.
- Making a Craft module a prerequisite for a machine track, or treating The Craft as one placement — Maths for Games needs Numbers & Bits behind it, Game Feel needs a game that already runs.
- Presenting From Source to Silicon to a BASIC learner as a prerequisite rather than as an answer reached after the games raise the question.
- A general-programming concept (what a loop *is*) taught in Numbers & Bits, a briefing, or a language on-ramp — it belongs in General Programming, once.
- A briefing growing a language toolkit, or a Foundations module growing a per-chip specific (a SID register, a ULA quirk) — that belongs in the briefing.
- Prose in a Foundations module naming *Meet the Machine* where it means *Meet Assembly*.
- A BASIC game's unit-01 re-teaching typing, `RUN`, line numbers or the dark canvas — that is Meet BASIC's job; the game opens as a real program.
- A "First Programs" game whose stated skill is a bare keyword (`IF`/`THEN`, `FOR`/`NEXT`) rather than a game-design idea.
- Shipping a module slug rename without redirects.

## Log

| Date | Event |
|---|---|
| 2026-06-05 | Architecture recorded and accepted the same day. Superseded the `number-systems-primer` and `cross-system-foundations` seeds. Established the machine/language split: *Meet the Machine* becomes a per-system briefing, language on-ramps become the `Meet <language>` family. Resolved General Programming's concreteness (pseudocode plus one concrete vehicle, Spectrum BASIC), and ruled out an upstream display/sound primer. |
| 2026-06-30 | Naming and grouping resolved by [foundations-numbers-and-bits.md](foundations-numbers-and-bits.md): the primer is *Numbers & Bits*, as one combined subtrack. |
| 2026-07-08 | Logic & Gates accepted as a recommended Foundations side-path that gates nothing — [foundations-logic-and-gates.md](foundations-logic-and-gates.md). |
| 2026-09-03 | Rewritten to say what is true now. From Source to Silicon and The Craft added to the record; neither appeared in it before. Foundations is named as a **section, not a sequence**: General Programming is the one universal step, while Numbers & Bits and From Source to Silicon are the assembly arm, cross-platform so they are taught once rather than per system. Checked against the content rather than the folder name — From Source to Silicon tells BASIC learners in its own text that they can skip it, and Meet BASIC's fifteen units mention bit work once. The June branch shape is therefore restored, not replaced. Two placements added that the June record predates: From Source to Silicon is also the **bridge back from BASIC**, offered after the games raise the question rather than gating them, and so the route by which the on-ramp audience reaches assembly; and The Craft is recorded as two entry points — Maths for Games behind Numbers & Bits, Game Feel behind a working game. Sequencing moved out to [splitting-the-assembly-on-ramp.md](splitting-the-assembly-on-ramp.md), accepted the same day, so this record states the architecture and that one states the order. |

## Relates to

- [splitting-the-assembly-on-ramp.md](splitting-the-assembly-on-ramp.md) — the order this split is applied in.
- [curriculum-structure.md](curriculum-structure.md) — the module spine this front feeds.
- [modules-not-games.md](modules-not-games.md) — module `kind`, bare slugs, order as catalogue data.
- [foundations-numbers-and-bits.md](foundations-numbers-and-bits.md) — the Numbers & Bits subtrack.
- [foundations-logic-and-gates.md](foundations-logic-and-gates.md) — the Logic & Gates side-path.
- [craft-and-pattern-library.md](craft-and-pattern-library.md) — what The Craft is, and how it differs from the Pattern Library.
- [october-2026-launch-spec.md](october-2026-launch-spec.md) — launch scope and the cut hierarchy.
- [website-information-architecture.md](website-information-architecture.md) — URL shape and the track segment.
