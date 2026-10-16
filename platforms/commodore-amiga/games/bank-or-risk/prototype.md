# Bank or risk native prototype status

**Prepared source; native execution blocked before app access.** The user accepted
the trial tuning: one six-sided die, limit 10, at most five rounds and target 30.
The text-first endpoint and four fixed-roll probes are prepared in code-samples.
They have not been imported, syntax-checked, run or saved/reopened in AMOS.

## Source and verification

The proposed source is
`commodore-amiga/amos/bank-or-risk/prototype/bank-or-risk.amos` in
[samples revision c62991d](https://github.com/code198x/code-samples/tree/c62991d670568190dbd007af36fc951edd60ec6f/commodore-amiga/amos/bank-or-risk/prototype).
It is ASCII for Merge ASCII, not a tokenised AMOS project. Its README describes
the intended controls and repeatable import route. The endpoint is deliberately
silent; artwork and sound remain later teaching stages.

The [probe manifest](native-probes.json) binds the maintained source and four
generated inputs by SHA-256. The generator changes only the die supplier to
`Read FACE`, restores DATA at each new challenge and appends prescribed rolls.
All input, scoring, round transitions, endings and replay logic remain in the
generated source. Expected results are manually specified, not observations.

| Probe | Expected checkpoint | Current evidence |
| --- | --- | --- |
| Perfect success | Three rounds of 4 then 6 secure 30; exact 10 banks automatically | Generated source and hash checked; not run |
| Preserve and recover | Contributions 4, 0, 6, 10, 10; bust 11 preserves earlier 4; final-round success at 30 | Generated source and hash checked; not run |
| Range and limit | Rolls 1, 6, 2, 1 give totals 1, 7, 9, 10, then normal quit | Generated source and hash checked; not run |
| Unreachable | Three busts of 12 leave two rounds unable to reach 30 | Generated source and hash checked; not run |

The preparation checks confirm four exact transformations, matching hashes and
rejection of a nonempty output directory without overwriting it. Ruff lint and
format checks pass for the generator. These checks do not parse or execute AMOS
and cannot qualify the program's syntax, display, input or rules.

## Native access failure

Computer-use inventory failed with:

```text
Native apps: Error: Sky Computer Use native pipe startup failed
```

Resetting the computer-use session and retrying returned the same error. Neither
attempt reached an app; FS-UAE was not launched. No native screenshot, successful
play, syntax result, held-key observation or save/reopen result is claimed.

The previously approved official AMOS archive was reacquired at the pinned
revision and matched its earlier SHA-256. Test copies of the earlier firmware
and Workbench/Fonts images also matched. [Input identities](native-inputs.json)
record the public archive URL and hashes without paths or redistributing media.
Temporary copies are removed after this preparation pass; reacquire the same
inputs for the later native run.

## Source discrepancy

The [original Maths chapter](https://amospromanual.dev/05-03-maths.html#rnd)
defines an inclusive upper bound for `Rnd(n)`. The proposed die therefore uses
`Rnd(5)+1`. The quick reference instead uses an exclusive bound and `Rnd(6)+1`;
it also disagrees with the manual's default angle unit. The source contradiction
is filed as [umbrella #173](https://github.com/stevehill1981/198x/issues/173).
The prepared `random-range.amos` probe counts the results of the disputed
expression. It has not run, and a finite sample would not prove fairness.

## Resume conditions and acceptance

When native computer control is available, acquire the named inputs and follow
the [native plan](../../../../plans/2026-10-16-amos-bank-or-risk-native.md).
Import the exact maintained source and qualify the syntax before interpreting
any later result. Run the four probes and ordinary random play through actual
press/release input. Record actual observed values separately from this manifest.

Check invalid input, B at zero, held R/B/SPACE/A, waiting without action, once-only
scoring, result stability, replay, and quit at title, active round, between rounds
and final result. Save a native project, leave the editor session, reopen the
saved version and play again. Verify the fresh-key routine against the runtime;
source inspection alone cannot establish its repeat behaviour.

After correctness checks, ask for human play feedback on pace, recovery and
whether another attempt is appealing. No learner is currently available, so
educational effectiveness remains a separate pending question. Keep samples in
draft review and do not derive or publish replacement lessons from an unexecuted
endpoint. The current limitation is native access, not a reproduced AMOS failure.
