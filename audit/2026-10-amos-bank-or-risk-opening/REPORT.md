# AMOS opening: a message through one playable round

This bounded pass supplies ten complete beginner checkpoints before the full
bank-or-risk session. The maintained game is unchanged. The sources separate
message/edit/save, a palette variation, one roll, assignment, limit decisions,
one key, repeated input, a fresh physical press and one round. Existing fixed
and supplied die drawings fit between these steps.

The [source guide](https://github.com/code198x/code-samples/tree/696c429ad225bbdbc17e582115bb61d0e8371a7a/commodore-amiga/amos/bank-or-risk/stages/opening)
explains commands, exact edits, expected output, prediction/repair answers and
where the incomplete round differs from the full challenge. These are checked
authoring sources, not published replacement lessons or learner-trial findings.
Later session-scoring, round-count, ending and replay teaching sources remain
separate work. The existing endpoint's execution does not qualify them.

## Configuration and provenance

[inputs.json](inputs.json) pins source hashes, firmware/media and tools. The
configuration remains AMOS Professional 2.00, Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock 2 MiB chip RAM
and no fast RAM. Build198x at `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`
masters and validates OFS disks. Both tools build offline from existing locked
dependencies; no runtime, language implementation or dependency is added.

The qualified [sound media helper](../2026-10-amos-bank-or-risk-sound/prepare.py)
reconstructs a valid boot filesystem preserving all 78 runtime file contents.
Our ASCII files occupy separate data disks. The native editor imports each
into a blank project, with a retained listing checkpoint before F2 and F1.
No licensed media, tokenised programs, ROMs or emulator snapshots are published.
Original input media remains unchanged.

The [Maths chapter](https://amospromanual.dev/05-03-maths.html#rnd) defines the
inclusive Rnd bound. The small roll example displays one observation, plus
explicitly supplied endpoint variants. This does not prove the generator's
range, distribution or fairness; umbrella #173 remains a separate investigation.
The [Keyboard chapter](https://amospromanual.dev/10-01-using-the-keyboard.html)
defines blocking character input, polling, scan codes and buffer control.
The fresh-choice policy follows the previously qualified endpoint, now exposed
in a small inline example before the game uses it.

## Native findings that changed the guide

The planned missing-quote repair does not fail on this Merge ASCII route: the
editor supplies the closing quote and F2 reports No errors. The listing and
check are retained. A misspelt Print provides a separate deliberate fault;
the repaired message is a separate positive check. We do not present a missing
quote in a host text file as evidence of a native syntax failure.

The first message uses the runtime's existing white text on an orange text
background, with black elsewhere. An attempted Paper 0 / Pen 1 selection made
the glyphs orange because entry 1 is not white in that default palette. We
returned to the small original message source, keeping explicit palette setup
at the drawing checkpoint where it is explained. The selected-colour attempt
is retained in diagnostics. The running-total heading became generic so a
changed supplied roll cannot leave a contradictory quoted heading. Affected
sources are reimported and checked; initial data-image hashes are retained.

The first round display cleared pixels without resetting the text position.
Prompts drifted after unchanged input, and the empty-round image comparison
failed. Locate 0,0 before active and result printing corrects that source fault.
The manual's [screen](https://amospromanual.dev/06-01-setting-up-screens.html)
and [text](https://amospromanual.dev/05-06-text.html) chapters distinguish screen
clearing from text positioning. The rejected round source and captures remain
in [diagnostics/](diagnostics/). All affected round cases are imported and run
again. No emulator defect is inferred from this program error.

The first edits-disk reconstruction used a different file allocation order.
All five file contents agreed. The helper now retains the recorded order so
both relevant data disks and the runtime boot disk reproduce byte for byte.
This was a reproduction detail, not an AMOS or emulator defect.

## Observed checks

| Checkpoint | Native observation | Evidence |
| --- | --- | --- |
| Message and edit | The title is unchanged; the second line becomes the question about securing 30. | [message](captures/message-start.png), [edit](captures/edited-message-start.png) |
| Syntax repair | Prit fails F2; restoring Print passes. Merge ASCII supplies a missing final quote. | [fault](captures/misspelt-print-syntax.png), [repair](captures/message-syntax.png), [quote](captures/missing-quote-syntax.png) |
| Drawing colour | Orange pip with white outline/text; Ink 1 makes the pip white; changing entry 2 makes it cyan. | [orange](captures/die-colours-start.png), [white](captures/white-pip-start.png), [cyan](captures/cyan-pip-start.png) |
| One roll | The random source produces one displayed roll; supplied 1 and 6 display those values. | [ordinary](captures/one-roll-result.png), [one](captures/roll-one-result.png), [six](captures/roll-six-result.png) |
| Assignment | Supplied old total 4 plus roll 3 displays 7; changing the roll to 6 displays 10. | [seven](captures/running-total-start.png), [ten](captures/sum-ten-start.png) |
| Limit decisions | 9 remains at risk, 10 is perfect, 11 is a bust. | [nine](captures/total-meaning-start.png), [ten](captures/total-10-start.png), [eleven](captures/total-11-start.png) |
| One choice | R/B/Q report their request; X reports only the key and no score change. | [R](captures/choice-R.png), [B](captures/choice-B.png), [Q](captures/choice-Q.png), [X](captures/choice-X.png) |
| Naive repetition | Holding R for 90 frames produces repeated received characters. Q and then Return reach the editor. | [held](captures/ask-again-held.png), [editor](captures/ask-again-editor.png) |
| Fresh press | The same hold counts one; a new press counts two; X leaves two. Q and Return reach the editor. | [one](captures/fresh-held.png), [two](captures/fresh-second.png), [invalid](captures/fresh-invalid.png), [editor](captures/fresh-editor.png) |
| One round | B/X at zero leave the view unchanged. A supplied 4 banks 4; two fives bank exactly 10; two sixes preserve total 12 with award 0. A held roll does not act twice. Results remain stable while waiting and a fresh key can finish. | [bank](captures/round-bank-stable.png), [perfect](captures/round-perfect-stable.png), [bust](captures/round-bust-stable.png) |
| Ordinary round and quit | The random source also rolls, banks and returns to the editor. Q from its opening returns without a roll. | [bank](captures/random-round-bank-stable.png), [quit](captures/round-quit-editor.png) |
| Save the edit | Native Save As creates welcome.amos; a separate cold boot loads it and displays the edited question. | [saved](captures/message-saved.png), [loaded](captures/message-reopened-listing.png), [run](captures/message-reopened-title.png) |

The edited native program is 108 bytes and both saved-file and disk hashes are
recorded. All 78 runtime files are preserved. Ctrl+C from the message and a
further key from the single-choice experiment also return to the editor.

Negative controls reject a changed source, a missing required image, an earlier
count substituted for the unchanged count, a valid filesystem without the saved
program and an attempt to prepare into a populated run directory. All three
relevant disks reproduce byte for byte in an independent final rebuild.

The automated verifier checks source identities and each explicit variant edit,
validated media, required nonempty PNGs, unchanged views after B/X at zero,
unchanged fresh-press count after X, stable result images and native saved-file
presence with all runtime files preserved. Screen wording, numbers, pips,
colour and syntax banners are inspected separately; hashes alone do not read
those meanings. [verification.json](verification.json) retains measured checks.

## Reproduction and limits

Build the pinned emulator with `--release --offline --locked
--no-default-features` and Build198x with `--release --offline --locked`.
Run `prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
with lawful matching inputs and an empty run folder. SAMPLES is the bank-or-risk
folder containing `prototype/` and `stages/`. Source identities are checked
before preparation. The inherited helper refuses existing output, preserving
previous runs.

Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN`. Use [sequence.json](sequence.json) for the complete dependency order, beginning
with `work-boot-1000` and `work-editor`. Each source has
an `-import` phase followed by `-run`; inspect its listing and syntax/result
captures. The deliberately faulty program is syntax-checked without running.
The roll endpoints, changed sum and pip-colour edits have their own phases.
Scripts, not tool exit codes, specify the keyboard actions and observation
windows. Each native subprocess has a 50-second limit.

The remaining action phases test single choices, repeated/fresh input, round
bank/perfect/bust/quit and edited-message persistence. The message is saved as
`welcome.amos`, exported to a new sidecar disk and loaded through native Load
after an independent cold boot. Restoring the edited session is not the
persistence check. Intermediate snapshots only divide each booted route into
bounded commands.

[reports/](reports/) retains native observations with local run paths replaced
by `${RUN}`. [artifact-hashes.json](artifact-hashes.json) binds unedited native
screenshots. For the two message displays, a retained pointer-motion phase moves the mouse
away from the first characters before capture. It does not edit the program
or image. Temporary QA contact sheets are excluded. This named configuration
is not a minimum hardware claim. Human understanding, listening acceptance and
the later uncoached learner trial remain unverified.
