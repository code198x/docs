# Bank or risk teaching map

**Opening, session and presentation checkpoints now have complete sources; authored replacement lessons remain pending.**
The [native text prototype](prototype.md) has rules, input and persistence
evidence on a named Emu198x setup. The [drawing audit](../../../../audit/2026-10-amos-bank-or-risk-die/REPORT.md)
checks the fixed picture and supplied faces 1–6. The
[board audit](../../../../audit/2026-10-amos-bank-or-risk-board/REPORT.md)
checks supplied one-round/challenge snapshots and the live grouped display.
The [sound record](../../../../audit/2026-10-amos-bank-or-risk-sound/REPORT.md)
checks pitch/volume/fade variations, event counts, muting and named input windows;
it does not establish human listening preference. The
[opening record](../../../../audit/2026-10-amos-bank-or-risk-opening/REPORT.md)
checks the message/edit/save, colour variation, roll, total, comparisons and
input route through one round. The
[session record](../../../../audit/2026-10-amos-bank-or-risk-session/REPORT.md)
checks the next-round, score, completed-count, ending and replay sources.
The [presentation record](../../../../audit/2026-10-amos-bank-or-risk-presentation/REPORT.md)
checks the continuous route into a shared display, grouped board, event cues
and ready screen. It adapts the old current-round display to the completed
counter, preserving the session loops. The [game brief](brief.md) owns the rules; this map explains
how we could teach them without importing an unexplained game framework.
The user agreed that drawing, colour and sound should develop through the game.
The initial text prototype checked the proposed rules; the current presentation
has graphics and sound. The user played the rescue endpoint and reported that
it works well; explicit listening preference and learner outcomes remain pending.

The user accepted the browser playtest's simple scope and 10/5/30 tuning. Keep
that basis while implementing this progression. Native checks may change exact
edits or checkpoint boundaries; they do not require adding more game mechanics.

Show the complete game's purpose early: bank points towards 30, or risk another
roll while staying at or below 10. Five rounds give us a limited opportunity to
reach the target. Use native demonstrations only for the checked prototype and drawing fragments;
later variations need their own execution evidence. The
first exercises below are runnable fragments of that game, not finished games.

## From a message to one round

Each row describes a checkpoint, not a promised lesson count. The fixed-die and
supplied-face [sources](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages)
and supplied board snapshots are implemented. Short-tone and separate
bank/bust/success sources are also available. The
[opening guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/opening)
now supplies the earlier steps through one round with exact edits and answers.
The [session guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/session)
supplies the later scoring, completed-count, ending and replay steps. It
separates a supplied lifetime trace, input extraction and continuation before
live scoring. The [presentation guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/presentation)
continues with separate display extraction, board, bank/bust/success cues and
ready-screen steps. It keeps completed rounds throughout. The older For-based
prototype and top-level cue sources are alternative implementations, not an
unexplained next step in this route.
The [arcade guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/arcade)
continues the score-chase endpoint through three separate checkpoints: colour
roles with the old geometry, a spaced board with a relative die origin, then a
slowing reveal. Predict which fields change with a palette entry; repair a slot
position while preserving five awards; explain why preview faces never change
the accepted roll. Compare motion and static sources with the same supplied
rolls. These are complete sources with a [native record](../../../../audit/2026-10-amos-bank-or-risk-arcade/REPORT.md);
authored lesson boundaries and learner understanding remain unverified.

Split a row further if its implementation needs another unfamiliar idea. Keep a complete source for each checkpoint in code-samples, with exact
editing instructions and expected output in the lesson.

| Checkpoint | New understanding | Expected result and learner investigation |
| --- | --- | --- |
| Display the challenge | Instructions execute in order; quoted text is displayed | Change the welcome text, run it, stop and return to editing. Repair a deliberately misspelt Print command. The checked Merge ASCII route repairs a missing closing quote automatically. |
| Keep the changed program | Source, filename and saved output are different things | Save, leave the editor session, reopen and run the changed words. A screenshot or emulator snapshot does not satisfy this check. |
| Draw a die | Pixel coordinates place shapes | Draw an outline and one central pip using explained fixed coordinates. Change one position and predict which shape moves. Distinguish pixel positions from text rows and columns. |
| Choose its colours | A palette entry and the colour selected for drawing have different jobs | Change a small palette deliberately, then change which entry a shape uses. Keep the pip, die and text distinguishable; explain the colour notation locally. |
| Show one die result | A random choice has a defined range | Explain the die expression after checking it against the original manual and runtime. Investigate how the smallest and largest generated values become 1 and 6. |
| Store a running total | Assignment uses an old value to produce a new one | First use prescribed values 4 then 3. Show old total, roll and new total separately; predict 7 before running. Mark this as a test setup, not random play. |
| Decide what a total means | Comparisons choose a path | Separate runs with supplied totals 9, 10 and 11 show active, perfect and bust. Ask which comparison admits exactly 10. |
| Match picture to roll | Decisions select a representation of stored data | Draw the corresponding pip pattern for each supplied value 1 through 6. Keep the printed number beside it and explain every branch before introducing random faces. Clear the old face without erasing the labels. |
| Read one choice | A key becomes a value the program can inspect | Read and report R, B or Q once, then stop. An unrelated key changes no score. This stage does not yet run a repeated game. |
| Ask again | A loop returns to a decision | Repeat the prompt, accept Q to leave, and keep the total unchanged while waiting. Explain the loop's entry and exit before adding repeated rolls. |
| Accept a fresh press | A held key and a new choice are different | Teach and check the required release/buffer handling in a small example before the game depends on it. Holding R produces one accepted action; release and press again produces another. |
| Play one round | The choice changes whether the round continues | Connect the explained input and limit decisions. R adds one roll, B after a roll banks, exact 10 ends automatically, and a bust awards zero. Show a result before returning to the editor. |

Teach random play and prescribed test values as separate versions with explicit
edits. Do not introduce DATA, a test generator or a hidden die routine just to
make an early example deterministic. Native acceptance probes are authoring
tools; learners need only the small test setup explained at that checkpoint.

The single round shows the controls and scoring. Explain that it lacks
the full challenge's reason to take risks: banking a safe total can be repeated
without trying to meet a session target. Do not present it as evidence that the
finished game is compelling.

## From one round to a challenge

| Checkpoint | New understanding | Expected result and learner investigation |
| --- | --- | --- |
| Keep secured points | Values can survive a round | Bank 4, then reset the current total for another round while preserving the secured 4. Introduce the next-round continuation separately from scoring. |
| Award the result once | Showing a result and changing a score are different actions | Finish a round, then wait and press an invalid key. The secured score does not change. Trace where the one award happens. |
| Hear a bank or bust | A sound belongs to an event, not every redraw | First teach one short sound's pitch, duration and volume through an explained example. Then give banking and busting distinct cues in separate edits at the once-only result transition. Listen while waiting, redrawing and holding a key: the cue must not repeat. |
| Count completed rounds | A counter records finished work | Increment once after a round, not after a roll or a display refresh. After two rounds, three of the five opportunities remain. |
| Lay out the challenge | A board groups values with different meanings | Place the die/current total, secured score, round/remaining rounds and target in labelled regions. Reuse the taught drawing and colour facilities. Keep the bust total visible beside its zero award and preserve the layout across rounds. |
| Recognise success | A session decision uses the secured score | Three perfect rounds reach 30. Hold the result; another roll cannot change it. Include target equality in the check. |
| Hear success | Reuse an explained cue at a different event | Add a distinct short success cue once at the session ending. Decide explicitly whether it replaces the final bank cue or follows it; check for overlap and confirm the visual result alone explains success. |
| Recognise impossibility | Remaining opportunities bound what can still happen | Explain secured points plus 10 times the remaining rounds. Three opening busts leave at most 20, so end without offering a fourth round. |
| Start again | Reset follows the lifetimes of all stored values | Replay restores score, completed rounds, current total and input readiness. Compare a fresh challenge with the original start. |
| Review the finished presentation | Drawing and sound must agree with the rules | Run all six faces, bank, bust, success, failure and replay. Check readable labels, stable results, once-only cues and play with sound off. Change the wording or palette and repeat the same rule checks. |

The prototype's title screen, routines and final input handling are an endpoint
to investigate, not starter code to copy wholesale. Introduce a routine when
repeated work gives it a purpose. Explain its inputs, changed values and return
before callers depend on it. Recheck every affected checkpoint after moving code.

## Give the completed game a reason to replay

The user approved the [score-chase extension](brief.md): finish all five rounds,
keep an in-program personal best, show the five awards and offer one rescue.
The [replay-value guide](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/replay-value)
develops these in five complete stages after the presentation bridge. Its final
`feedback.amos` is the extended teaching endpoint. Earlier sources keep their
early endings as an explained working stage; the extension changes that design
after its replay limitation becomes visible.

| Stage | Idea | Investigation |
| --- | --- | --- |
| Five rounds | A target and a stopping rule need not be identical | Reach 30 in round 3, then continue. Also continue when 30 becomes impossible. |
| Personal best | A value can outlive one replay | Complete higher, lower and tied scores; record only a strict improvement after round 5. |
| Five awards | An indexed table stores repeated values | Distinguish completed zero, current question mark and future dash; reconcile the completed entries with secured score. |
| One rescue | A limited resource adds a pending decision | Undo to the pre-roll state or accept zero while saving rescue. Neither pending nor invalid input completes a round. |
| Feedback | A reveal and a result event have different jobs | A short preview changes no score; first reaching 30 produces one acknowledgement, with readable muted outcomes. |

The [native record](../../../../audit/2026-10-amos-bank-or-risk-replay-value/REPORT.md)
qualifies the named source versions and cases. Personal best is memory-only;
disk records, additional mechanics and beginner learning claims are outside it.

## Use AMOS without increasing the rules load

The fixed die drawing comes before its random value. At that point it is an
explained picture, not a claim that the face represents a roll. Once decisions
have been taught, connect the picture to the stored result and check all six
faces. A round that has not rolled yet must show a clear empty/ready state,
not an old die face presented as its current result.

Use AMOS drawing primitives for the original die and board. A small explicit
face selection is acceptable before arrays or asset banks are useful. Do not
hide unexplained loops, data tables or routines inside a supplied renderer.
Change palette and layout in separate stages from scoring. Recheck numbers and
pictures together whenever a display change is made.

Begin sound with a short built-in tone whose parameters we explain and listen
to. Sound selection remains subject to the native trial; avoid requiring a
sample library or tracker player for these first cues. Teach timing or sound
completion controls before relying on them. Test that cues do not delay accepted
input, obscure a result or act as an unexplained pause. Every outcome remains
clear through labels and numbers with sound off and without colour distinctions.

The original AMOS Professional Manual's
[Graphics chapter](https://amospromanual.dev/06-04-graphics.html) covers drawing
coordinates, shapes, drawing colours and palettes. Its
[Music chapter](https://amospromanual.dev/08-01-music.html) covers built-in sound
effects and pitched sounds. These are source references for choosing the later
implementation, not proof that the proposed checkpoints run.

Bobs, sprites, scrolling and AMAL can enter later games when they serve the play.
The first game should make useful, explained use of AMOS graphics and sound
without adding movement, animation or new rules just to cover more commands.

## Give each value a job

Use learner-friendly labels before choosing source identifiers. The authored
names can follow the checked implementation; the distinct responsibilities must
remain visible.

| Value | When it changes | What must remain true |
| --- | --- | --- |
| Die result | Each accepted roll | It is from 1 through 6 in ordinary play. |
| Current total | A roll, or the start of a new round | It can display 11 after a bust even though the award is zero. |
| Round award | Once when the round ends | It is zero for a bust; otherwise it is the banked total. |
| Secured score | Once for a completed round, or replay | A bust preserves points from earlier rounds. |
| Completed rounds | Once when a round finishes, or replay | A roll is not a completed round. At most five rounds finish. |
| Input readiness | Accepted press, release and state transition | Holding a key cannot act twice or carry an action into the next round. |

Limit, target and maximum rounds are settings, not scores. Teach each setting
where it first affects behaviour. Do not declare all endpoint variables at the
opening and expect the reader to remember their purpose.

## Entry routes

A complete beginner follows the checkpoints in order, with essential explanations
on the page. Optional Foundations reading can deepen understanding without
supplying missing instructions.

An experienced programmer still needs the named environment's run, stop, save,
reopen and recovery route. Offer entry at the single-round and session boundaries
with a complete checked source, a short explanation of the state already present
and links to the relevant earlier explanations. Supply those sources only once
they exist and run; do not link planned samples as available material.

Use a prediction to help someone choose an entry point, with the answer available
immediately. It is advice, not an exam or an unlock condition. Familiarity with
variables does not establish familiarity with AMOS input or storage.

## Prompts and explanatory answers

**Predict:** We have secured 4 points. In the next round we roll 5, then 6.
What should the result show, and what remains for the following round?

The current total is 11, the round awards zero and the secured score stays 4.
Two rounds have finished, leaving three. Reset the next round's current total
to zero, but keep the secured score. Do not erase the bust total before the
player has had a chance to read it.

**Repair:** A perfect total of 10 is labelled a bust. Which decision should we
inspect, and what examples distinguish the intended rule from the fault?

Inspect the bust comparison: it must reject totals above the limit, not totals
equal to it. Check 9, 10 and 11; checking only 11 would leave the fault hidden.
Recheck that a perfect 10 banks once and that 11 awards zero.

**Vary:** Change the game's wording and die presentation while keeping its
rules. How can we check that this is still the same challenge?

Replay known sequences and compare totals, awards, score and endings. Keep
labels readable and outcomes understandable without colour or sound. Offer
hints before a full explanation. A later numeric variation needs a separate
look at the limit, target and remaining-round calculation together.

Parents and teachers can ask the prompt, allow time to think and record whether
the learner predicted, ran, explained or needed a hint. Reveal answers when
useful. Do not turn these suggestions into claimed learner findings: no
uncoached trial has taken place.

The [complete-frame and typography stages](https://github.com/code198x/code-samples/tree/amos-bank-or-risk-prototype/commodore-amiga/amos/bank-or-risk/stages/arcade)
follow the first animation: hidden drawing and deliberate presentation, then
ROM text with measured baselines, then an authored bitmap alphabet for title and
scores. Each has a complete source and explanatory guide. The
[native record](../../../../audit/2026-10-amos-bank-or-risk-complete-frames/REPORT.md)
separates passed game/frame checks from its pre-fix native storage failure.
The [storage follow-up](../../../../audit/2026-10-amos-storage-follow-up/REPORT.md)
verifies the larger endpoint on the fixed emulator revision. It also separates
scripted export verification from the learner's host disk-export workflow.
