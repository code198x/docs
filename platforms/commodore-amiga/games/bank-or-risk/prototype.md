# Bank or risk native prototype status

The current teaching endpoint is `stages/arcade/styled-board.amos` in
code-samples. The [score-chase record](../../../../audit/2026-10-amos-bank-or-risk-replay-value/REPORT.md)
checks all five rounds, in-program best, five awards, one rescue and feedback.
The [arcade record](../../../../audit/2026-10-amos-bank-or-risk-arcade/REPORT.md)
checks the following palette, layout and animated-roll stages. The
[complete-frame record](../../../../audit/2026-10-amos-bank-or-risk-complete-frames/REPORT.md)
checks the visible-redraw fix, ROM text and custom title/score lettering. Game
checks pass. The [storage follow-up](../../../../audit/2026-10-amos-storage-follow-up/REPORT.md)
verifies native Save, cold Load and execution of that larger endpoint on the
fixed emulator revision. The original pre-fix failure remains recorded;
version 0.34.2 alone does not establish that the disk-change fix is present.
The earlier prototype and presentation sources below retain their early endings
and their own evidence; the [current brief](brief.md) owns the extended rules.
The user played the rescue endpoint and reported that it works well, then
requested colour, spacing and an animated roll. Acceptance of the new
presentation, explicit listening preference and learner outcomes remain pending.

**Native rules, input and save/reopen checks pass on the recorded Emu198x setup.**
The user accepted the browser trial's simple scope: one six-sided die, limit 10,
at most five rounds and target 30. The prototype now runs in AMOS
Professional 2.00 with an outlined die matching the stored roll and grouped
round/session values. Short result cues have native PCM evidence. Listening
acceptance and remaining lesson sources still need work.

## Source and execution

The source is `commodore-amiga/amos/bank-or-risk/prototype/bank-or-risk.amos` in
[samples revision 1fa0675](https://github.com/code198x/code-samples/tree/1fa0675b809ef6a40bcf01571b75d6196cce0e0e/commodore-amiga/amos/bank-or-risk/prototype).
It is ASCII for Merge ASCII. Native Save As produces a separate tokenised AMOS
program; these two representations must not be confused.

The [execution audit](../../../../audit/2026-10-amos-bank-or-risk-emu198x/REPORT.md)
owns configuration, identities, scripts, captures, observed results and limits.
It uses Emu198x 0.34.2 at `6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL
A1200, stock 2 MiB chip RAM, no fast RAM, the recorded Kickstart 3.1 image and a
local AMOS Professional 2.00 system disk. This is distinct from the earlier
FS-UAE/official-repository installation and is not a minimum hardware claim.

The first native import exposed command-prefix collisions in our identifiers.
A reduced failing program and an isolated successful naming probe establish the
cause. Game identifiers now use `BR_`. That naming correction preserved the original
source apart from the prefixes. The later palette change adds only an explicit
black/white palette before the title; scoring and input logic are unchanged. The source is
syntax-checked and executed in AMOS, not compiled with the separate AMOS compiler.

The [palette audit](../../../../audit/2026-10-amos-bank-or-risk-palette/REPORT.md)
retains the explicit black/white title, active, bank, bust and success checks.
It repeats the perfect and recovery cases; the broader rules/input and
original save/reopen checks below belong to the earlier pre-palette source.
The endpoint persistence record below covers the current presentation and sound.

The [drawing audit](../../../../audit/2026-10-amos-bank-or-risk-die/REPORT.md)
checks the two drawing fragments and all six game faces, clearing/reset, bank,
bust, success, failure and replay. It preserves all existing scoring/input code.

The [board audit](../../../../audit/2026-10-amos-bank-or-risk-board/REPORT.md)
checks supplied round/challenge snapshots and the grouped live display, including
later/unused rounds, all result types and replay. Only the display routine
changes; scoring, input and die drawing remain identical to the drawing revision.

The [sound record](../../../../audit/2026-10-amos-bank-or-risk-sound/REPORT.md)
checks native tone parameters, bank/bust/success counts, silent controls and
named input windows. All nine audible/muted perfect-run states agree byte for
byte. Success replaces the last bank cue. Human listening acceptance remains
pending; the sound record retains raw clips and a short listening preview.

The [endpoint persistence audit](../../../../audit/2026-10-amos-bank-or-risk-persistence/REPORT.md)
repeats native Save As, disk export and independent cold-boot Load for the current
sound-enabled source. Its maintained random game rolls and banks four, then
returns to the editor. A separately saved fixed-roll copy compares the same
nine game states and bank/bank/success cues before and after saving.

The [probe manifest](native-probes.json) binds the current source and five
fixed-roll copies by SHA-256. The generator changes the die supplier to
`Read BR_FACE`, restores DATA at each challenge and appends prescribed values.
Its expectations are preparation data; actual observations live in the audit.

| Native check | Observed result |
| --- | --- |
| Perfect success | Three perfect rounds secure 30; equality banks automatically. |
| Preserve and recover | Contributions 4, 0, 6, 10, 10 reach 30 on round 5; bust 11 preserves the earlier 4. |
| Range and limit | Rolls 1, 6, 2, 1 show totals 1, 7, 9, 10; exact 10 secures 10 once. |
| Unreachable | Three busts at 12 leave the target unreachable after round 3. |
| Input boundaries | B and X at zero change no score; the tested held R/B/SPACE/A windows cause no duplicate action. Replay resets the challenge. |
| Exit | Q then Return reaches the editor from title, active, between-round and final-result states. |
| Persistence | A native saved program is exported on a verified work disk, loaded after a separate cold boot, played and exited. |

## Media and access

The former desktop-control failure does not block the emulator's script/MCP
interface. Native input and display checks use that interface; desktop-window
menu integration is not qualified by this pass.

The initial AMOS input disk fails a bitmap-bounds check, and a Save attempt
reported a write-protected boot volume. The successful persistence run uses a
fresh filesystem with all 78 original file contents preserved and an in-memory
writable mount from boot. Those setup changes were not isolated as causes of
the earlier failure. The audit records both outcomes; no confirmed emulator
defect was inferred. Original media is unchanged and excluded from the repo.
Historical FS-UAE preparation identities remain in [native-inputs.json](native-inputs.json);
the audit owns current execution identities.

## Accepted browser playtest and next work

The user played the separate
[browser version at samples revision 6e166c4](https://github.com/code198x/code-samples/tree/6e166c4eb93b60019c3eb2638ac893d5b37442f8/commodore-amiga/amos/bank-or-risk/browser)
and accepted its simple scope and 10/5/30 tuning for the first game. That is
owner play feedback on the JavaScript trial, not AMOS play approval or evidence
of beginner understanding. Keep the agreed scale while developing the native
[teaching direction](teaching-map.md), including progressive graphics and sound.

The [opening audit](../../../../audit/2026-10-amos-bank-or-risk-opening/REPORT.md)
checks ten earlier sources through one playable round, including native saving
of the edited message, a real syntax fault/repair and held-key experiments.
Those source checks do not establish how beginners learn from them. The
[session audit](../../../../audit/2026-10-amos-bank-or-risk-session/REPORT.md)
checks eight sources for value lifetime, repeated rounds, once-only awards,
completed counts, success/impossibility and replay, including saved-program
reopen. The [presentation audit](../../../../audit/2026-10-amos-bank-or-risk-presentation/REPORT.md)
checks six further sources through shared display, grouped board, separate
result cues and a ready screen, including native storage. The continuous
teaching route keeps completed rounds; its renderer adapts the older current-round
calculation. The historical For-based prototype remains an alternative with
its own source pins. The user has since played the later rescue endpoint and reported
that it works well. The following arcade pass develops the requested presentation;
its acceptance, explicit listening preference and authored replacement lessons
remain pending. Check each addition in AMOS; earlier prototype
execution does not qualify a changed teaching source.
A later uncoached beginner trial remains pending.

The [original Maths chapter](https://amospromanual.dev/05-03-maths.html#rnd)
defines the inclusive `Rnd(n)` bound used by the die. The separate reference
investigation in [umbrella #173](https://github.com/stevehill1981/198x/issues/173)
still has its own random-range and angle-mode probes; these game checks do not
complete them or prove random fairness.
