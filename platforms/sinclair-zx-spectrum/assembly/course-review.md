# Spectrum Z80 assembly — opening review

**Status:** The user read and approved the review and replacement direction.
Existing games, engine, sequence and lessons have no protected place in the new
course. Meteor Storm is selected for the first native trial. Approval does not authorise
immediate deletion of published material or establish a later lineup.

Apply [the charter](../../../PROJECT.md) and
[curriculum design](../../../specifications/curriculum.md).

## Recommendation

Replace the compulsory **Meet the Machine → Gloaming → The Long Night →
Shadowkeep** progression. Design a fresh independent assembly opening and first
game. Retain selected experiments, routines, assets and design investigations as
candidates, with no obligation to retain the game names, source structure or
unit numbering. This is a teaching and architecture recommendation, not a claim
that the existing games cannot run.

Do not start by rewriting every existing lesson. Agree the new opening's purpose,
prototype its first game, assess it through native play, then derive teaching
stages. The game must earn its place before we invest in a replacement sequence.

## Evidence and limits

Reviewed the published module catalogue and landing page, inventories of all
65 authored units, representative lesson bodies across the opening and each
game, retained briefs and design investigations, final sources and capture
manifests. This is a curriculum/architecture review with targeted technical
checks, not an exhaustive line-by-line audit of every lesson or instruction.

| Module | Authored units | Referenced assembly sources | CodeDiff components |
|---|---:|---:|---:|
| Meet the Machine | 16 | 22 | 6 |
| Gloaming | 20 | 63 | 43 |
| The Long Night | 10 | 31 | 21 |
| Shadowkeep | 19 | 43 | 24 |

All **159 unique assembly sources referenced by those unit pages** build as
snapshots using Asm198x v0.0.58 with explicit `--cpu z80`. All literal image/video
`src` and poster paths checked in those unit pages exist locally. This check does
not establish external-link health, embedded-player behaviour or teaching accuracy.

Fresh 48K emulator smoke runs loaded snapshots rebuilt from the three game
endpoints, reached titles and entered play through keyboard input. The resulting
screens were inspected. These runs did not load tapes, complete the games,
measure responsiveness or validate sound. The Long Night needed a longer title
wait and key hold than the initial short smoke script; no responsiveness verdict
is inferred from that. Earlier design logs report more extensive playtests, but
those historical observations are not new human acceptance of these endpoints.

Build identities and results are in [the evidence record](verification/opening-review.json).
The website revision reviewed is `52c68f1f`; samples revision is `e0b4f464`.
The emulator binary is identified by its hash in the record, not assumed to equal
the current checkout. Sources and checked-in manifests are retained unchanged.

## Findings that change the teaching plan

### 1. Independent entry is promised by the landing page, contradicted by lessons

The assembly landing says BASIC is not required and invites readers to choose a
game. Meet the Machine unit 01 assumes variables, loops and subroutines, sends
new programmers to Foundations, and explains assembly through what the reader
previously did in BASIC. Unit 02 is titled “LD Is Not LET”; units 07 and 11 also
use BASIC as their starting explanation.

Comparisons can help readers who know BASIC. They must not supply essential
meaning for a reader who does not. Retain the concrete register, memory, branch
and stack experiments, but explain the concepts locally and make language
comparisons optional.

Shadowkeep unit 01 says the reader wrote the whole preceding engine, carries it
forward wholesale and could almost reproduce it from memory. Some routine
contracts are usefully summarised, but that is not an independent entry route.
A replacement game needs explicit starting files, explained contracts and a
route to understanding reused implementation, not assumed attendance.

Evidence: `meet-the-machine/unit-01`, `unit-02`, `unit-07`, `unit-11`;
`shadowkeep/unit-01`; assembly landing page.

### 2. Display attributes remain rules well beyond a small introductory experiment

Gloaming's final `wall_at` calls `attr_addr_cr` and tests `WALL_BIT` in display
memory. Lamp state lives in attributes, including the saved-under attribute while
a character covers a lamp. The Long Night extends that model into target
selection, light pools and terrain. Shadowkeep has room-state data, but its final
collision routine still tests the displayed attribute's BRIGHT bit.

Shadowkeep unit 03 explicitly defers separating collision from appearance to a
later game. Unit 13 makes a torch solid because it is bright. These are deliberate
choices, not incidental implementation details. They conflict with the current
direction established during BASIC: rules should survive a change in colour or
presentation.

An attribute-driven toy can show a machine-specific shortcut and its limits.
It should not be the architecture inherited across the opening games. Use an
explicit map or entity state, draw from it, and teach collision from that state.
The extra representation needs teaching; it does not require a general engine.

Evidence: `gloaming/unit-09`, `unit-12`, `unit-14`; `the-long-night/unit-01`;
`shadowkeep/unit-03`, `unit-13`; all three final `wall_at` routines.

### 3. The current handoff rolls back fixes

Gloaming unit 20 teaches step 03 to correct win/loss precedence and a collision
case involving the wisp's saved background. The Long Night unit 01 says its step
00 is the exact finished Gloaming. Freshly assembled snapshots show otherwise:
its step 00 is byte-identical to Gloaming step 02, and differs from step 03.

This establishes a continuity defect, not a claim that every later Long Night
checkpoint retains both bugs. A replacement sequence should have mechanically
checked handoffs and narrative descriptions tied to the actual starting source.
If the existing sequence remains public during review, this is a bounded repair
candidate independently of whether its curriculum is ultimately retained.

### 4. Progression follows an inherited engine and development history

The current route asks readers to complete 16 introductory units before the first
20-unit game; another 10-unit expansion precedes the 19-unit Shadowkeep. Length
alone is not a defect. The concern is what that length buys: successive projects
stay with whole-cell movement and saved-background rendering while revisiting
lamps, darkness and related presentation.

Gloaming teaches the objective from units 11–15 and introduces its moving threat
at unit 16. Its early units contain useful drawing, input and timing work, but the
reader spends much of the first game establishing machinery before experiencing
its central decisions. The Long Night's first lesson itself argues that the
original antagonist does not contest the objective.

A small playable decision should arrive earlier and then deepen. Do not require
an entire module to rehabilitate the appeal of the first finished game. Preserve
iteration as a practice, without requiring readers to reenact every historical
prototype mistake.

Gloaming unit 10 deliberately changes and then removes a boundary clamp to
converge with the endpoint. The Long Night explicitly retells its playtest history
and postpones sound as a finish-phase concern. Some such experiments teach
valuable distinctions; the pattern should not determine every lesson. Develop
readability, controls, art and sound alongside the mechanics they explain.

### 5. The editing and setup workflow needs reconciliation

The game lessons use 88 CodeDiff components between them. Complete source is
usually available, which is valuable, but a diff is frequently the principal
instruction for a required milestone. The current unit specification calls for
explicit additions, replacements and deletions, with diffs optional.

All 16 introductory pages contain a `pasmonext` command; only the first contains
an `asm198x` command. Unit 01 demonstrates a tape build, while later examples use
snapshots. Both output formats can be useful, but the learner needs one explained
primary workflow, explicit CPU/target configuration, source acquisition, stack
and startup assumptions, and instructions for debugging with the chosen tools.
Generic references to an emulator's memory window are not a complete debugging
exercise.

Do not mistake passing builds for correct prose. For example, Meet the Machine
unit 12 groups increment/decrement with add/subtract when describing wrap and
carry. Zilog's *Z80 CPU User Manual*, UM008011-0816, “INC r”, pp. 165–166, explicitly
states that carry is unaffected. A rewrite needs instruction-specific flag
explanations, including unsigned carry versus signed overflow. Shadowkeep unit
05 also calls its two six-byte room records “eight bytes”; the listed records
occupy twelve. These examples justify a factual audit of material selected for reuse.

### 6. Later catalogue promises no longer follow current policy

The catalogue still has ten further named game proposals after the four authored
modules. These are not ten approved development obligations. Lamplight returns
to lamp collection to introduce masking; Spectral Legacy promises a commercial
capstone, 100+ screens and attendance at every earlier game. Its page presents
that ambition as currently in development.

Replace the predetermined ladder with candidate experiences and capability
coverage. Neither a commercial quality claim, historical ancestor nor a fixed
technique budget earns a game its place. Any public catalogue cleanup should
preserve useful existing URLs and distinguish proposals from work underway.

## Retain, reshape or replace

| Existing material | Recommendation | What remains useful |
|---|---|---|
| Meet the Machine | Replace the prescribed 16-unit gateway; reshape selected experiments | Build/run cycle, visible registers and memory, screen bytes, branches, loops, stack and debugging |
| Gloaming | Replace as the assumed first game; retain its premise only as a candidate | Small complete scope, readable objective, restart/state transitions, background restoration and keyboard timing |
| The Long Night | Remove from the required opening; consider a later behaviour/design study | Target selection, hunt/withdraw/rest states, territory, queues, escalation tables and measured iteration |
| Shadowkeep | Remove the inherited-engine requirement; reassess as a later independent room-based project | Room graph, persistent room state, data-driven layouts, patrols, baked shading and asset creation |
| Later named lineup | Reopen completely; no reserved slots or mandatory finale | Candidate capability questions such as smooth sprites, scrolling, larger worlds and sound |

“Retain” means reassess and verify, not copy code unchanged. A fresh first game
may make all three existing game identities unnecessary. None is protected by
sunk effort. Conversely, this review has not established that their mechanics
are intrinsically unenjoyable; a new native play review could change that judgement.

## Proposed replacement shape

Begin with short purposeful assembly experiments that lead into a complete,
compact game. Teach source → assembler → output → target, registers versus memory,
labels and branches, drawing, input and timing when the immediate result needs
them. Explain routine inputs, outputs, changed registers and storage ownership.
Introduce debugging early through a reproducible observation and an explained
register/memory view. Do not require a complete CPU survey before useful play.

The selected first project is **Meteor Storm**: pilot a ship through readable
meteor waves to reach clear space. The [brief](../games/meteor-storm/brief.md)
centres trajectory reading, gaps and crossing time. It gives input, explicit
object state, geometric contact and drawing a purpose. Salvage is optional,
after evasion itself works. Pixel movement is worth testing early; rendering
techniques should enter when the result requires them. Native play must establish
appeal and teaching suitability before lesson authoring. A driving game is a
later possibility, without a committed slot.

Then select distinct later projects by what they enable: smooth overlapping
objects, a persistent multi-room world, behavioural decisions, or a bounded
geometry/3D experiment. Do not reserve a separate full game for every rendering
upgrade. Shared Maths, Craft and AI material supplies depth, never missing local
instructions or compulsory prior attendance.

## Agreed direction and next bounded step

The replacement basis is agreed. The [opening design](opening.md) and
[Meteor Storm brief](../games/meteor-storm/brief.md) define the next step.
Build and assess a native prototype before naming a lesson count
or rewriting the public course. Review movement, readability, choices, difficulty,
retry and sound with the user. Record the exact target, build and loading path.
Then map the accepted game into understandable, independently runnable stages.

Keep current published material available during that trial. Make bounded repairs
where warranted, and replace or retire routes deliberately when a successor is
ready. No games, pages or samples were deleted by this review.
