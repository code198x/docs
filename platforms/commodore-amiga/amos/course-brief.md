# AMOS course brief

**Status: course proposal; first game awaiting agreement.** We want a complete
beginner to make and understand small games in AMOS, then grow towards more
substantial Amiga games. An experienced programmer should be able to enter
later without missing AMOS-specific explanations.

The [opening comparison](opening-candidates.md) recommends a small take-away
game for discussion: two players remove one or two counters from a pile, and
whoever takes the last wins. Its scope makes player choice and changing state
visible before moving graphics, arrays or an opponent become necessary.

Apply the [charter](../../../PROJECT.md),
[curriculum specification](../../../specifications/curriculum.md) and
[unit guidance](../../../specifications/unit.md). The
[tooling brief](../tooling-feasibility.md) identifies the facilities this course
would need. AMOS remains a full language track; assembly is an optional direction.

## Audience and outcomes

Assume the reader can enter text and use a keyboard. Explain the editor,
program, variable, decision, loop and routine where each becomes useful.
Foundations supplies optional depth, not missing prerequisites. Include the
keyboard mapping and exact recovery steps for the named emulator.

By the end of the opening, the reader should be able to:

- Enter, run, stop, edit, save and reopen a small AMOS program.
- Explain how a player's choice changes a stored value and the visible result.
- Predict a short sequence of decisions and repeated turns.
- Repair a small fault using an expected result and a reduced example.
- Make a modest variation with hints available, then explain and check it.

These are authoring outcomes to investigate with learners, not examination gates.
Parents and teachers should have prompts, explanatory answers and a record of
what help was needed. No learner trial is currently available.

## Progression through the full track

The opening should establish confidence through small playable programs and
careful explanations. Subsequent games can combine movement, input, graphics,
sound, collections and routines as each experience needs them. Later projects
can explore richer behaviour, connected worlds, asset workflows, storage,
presentation and measured performance, towards games as substantial as AMOS and
the chosen machine configuration reasonably allow.

This is a direction for growth, not a selected lineup, fixed set of tiers or
requirement to teach every facility before making a game. A small first game
sets the starting teaching load; it does not set the track's eventual ambition.
Choose each next game for the experience and understanding it adds.

Games should be distinct across tracks and systems by default. The
[comparison](opening-candidates.md) rules out a falling-object catcher and
paddle game as default openings because their play overlaps existing material.
A point-and-click adventure introduces too many interacting responsibilities for
the current opening brief. Keep short drawing experiments where they help
explain the actual game.

## Proposed first game

One pile begins with seven counters. Two local players alternate taking one or
two, and the player who takes the last wins. There is no timer. The program shows
whose turn it is, what was taken and how many remain. An invalid choice or a take
larger than the pile leaves both the count and active player unchanged. After a
win, the result remains visible until replay or exit.

A reader working alone can enter both players' choices while building and
investigating the game. A computer opponent is a possible later addition, not
an unexplained dependency of the first game. The prototype review must check
whether two-player play is a suitable opening for the intended audience.

Start with text output and deliberate choice entry. The exact AMOS input method
must be checked for invalid text and recovery before lesson development. A
single-key route may be preferable to numeric entry if it gives a clearer,
trustworthy explanation. Add a repeated picture of the counters once the game
creates a reason to learn counted drawing.

## Proposed opening stages

These are teaching stages, not executed programs or a fixed lesson count. Split
any stage whose teaching load is too large. Each needs maintained complete source
in code-samples and exact editing instructions.

| Stage | Result and purpose | New idea explained locally | Observable check |
| --- | --- | --- | --- |
| State the game | Run a tiny program showing the rules and starting pile; change the wording | Instructions, execution order and editor controls | The edited words appear on the next run; an intentional syntax error can be repaired. |
| Keep your work | Save, leave the session and reopen the edited program | Source files, filenames and storage | The reopened version contains the edit and runs; the reader can find the saved file. |
| Change the pile | Store the count and carry out one named take | Assignment and subtraction | Predict seven minus two, then explain why printing the old count earlier does not change it retrospectively. |
| Accept one choice | Let the player choose one or two and update the count | Input and decisions, introduced separately | Valid choices change the count as expected; invalid input can be rejected and retried. |
| Continue playing | Repeat valid choices while counters remain; prevent an unavailable take | Repetition and boundary decisions, introduced separately | With one counter left, a request for two changes nothing; zero ends the game without another move. |
| Take turns | Identify two players, switch after accepted moves and announce the last taker | A turn value and update order | An invalid move preserves the active player; the winner is the player who acted, not the next one. |
| Show the counters | Draw one mark per remaining counter beside the numeric count | Counted repetition and coordinates, introduced separately | The displayed marks agree with the count from seven through zero. Old marks disappear after a move. |
| Finish a round | Add instructions, readable result feedback, replay and exit | Initialisation and reset | Replay restores seven and the stated first player; repeated rounds preserve no stale winner or input. |
| Explain and vary | Trace a whole game, repair a fault and change the starting count within a stated display range | Integration and an independent change with hints | The new range, picture, legal choices and result remain consistent. |

Each runnable checkpoint contains only explained code. Do not supply a hidden
input handler, screen framework, game loop or winner routine. A fixed starting
pile and text display are sufficient before the counter picture is introduced.
No arrays, random generation, frame-rate target or collision system are required
by the proposed opening.

## Presentation and participation

Use labels and shapes to distinguish the players and remaining counters; colour
can reinforce the information. Keep the last move visible long enough to discuss
it. Teach a short result sound only after explaining its purpose and the required
AMOS command. The winner must remain understandable with sound off, and the cue
must happen once per result rather than repeat while the game is finished.

Let readers choose wording, layout and counter artwork. Explain the limits of the
permitted starting count before inviting changes. At useful milestones, ask for
a prediction, trace or diagnosis before revealing the explanation. An example
fault is switching players before preserving the winner; an independent variation
is changing the starting count and checking the resulting complete round.

Keep checks conversational and available on paper. They support explanation and
experimentation without requiring a particular score or a win against another
player. Check keyboard operation in the actual game as well as the lesson page.

## Experienced entry

Provide a short environment route covering run, stop, save, reopen and error
recovery. At project boundaries, describe the knowledge used, show a complete
small starting state and offer a prediction or change to help readers choose
where to enter. Answers remain available and do not unlock progression.
Experience in another language does not imply knowledge of AMOS input, screen
or storage behaviour.

## Existing material and replacement checks

The current [Meet AMOS source](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-amiga/amos/meet-amos)
contains useful explanations of variables, decisions, loops, procedures,
palettes and drawing. Reuse passages where they serve the chosen program; the
existing unit order does not determine the course. Bobs, collision, AMAL and more
substantial sound work can enter later games when needed.

| Current weakness | Required replacement check |
| --- | --- |
| The overview expects earlier programming knowledge | A newcomer can follow every essential explanation locally. |
| Unit 12 promises later edge handling that unit 14 does not supply | Every promised technique has a taught, runnable stage and corresponding checks. |
| Suggested actions can repeat while input or contact remains true | Distinguish one accepted action from held input, including result sounds and replay. |
| Unit 17 treats recognising commands as readiness | Include a complete action trace, a repair and a small variation without a supplied full solution. |
| The dedicated saving lesson arrives at unit 16 | Save and independently reopen an edited program near the start. |

Use the retained [execution record](../../../audit/2026-10-amiga-unit-five/REPORT.md)
for its named configuration only: AMOS Professional 2.00, official source revision
`533b4b1f5acd604814513f78e02c7b4796cb0531`, FS-UAE 3.2.35, PAL A1200/68020,
2 MB chip and 8 MB fast memory, Kickstart and Workbench 3.1. This is a development
baseline, not a minimum requirement or qualification of the proposed game.

## First prototype and decision

After game agreement, prototype one take, validated choice, repetition, turns,
win, replay and exit in the named original runtime. Check the save/reopen route
early. Compare a text-first explanation with the later counter picture, without
turning the picture into a prerequisite for the first playable version.

Check both players winning, one and zero counters, unavailable takes, invalid
input, repeated actions and fresh rounds. Inspect the actual output and listen
to any sound. Record native behaviour and play observations separately from
learner understanding.

Reconsider the game if two-player use is unsuitable, its strategy is exhausted
before the teaching is complete, or input and setup dominate the opening.
Compare the other shortlisted candidates before adding mechanics to rescue it.
No later lineup is selected. Preserve existing public routes until checked
replacements and any necessary redirects are ready.
