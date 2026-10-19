# AMOS score chase, five awards and one rescue

Five complete teaching stages extend the game with full five-round sessions,
a personal best, a visible scorecard, one rescue and short roll/result feedback.
The new endpoint is [feedback.amos](https://github.com/code198x/code-samples/blob/da45d25c0bed7dd3e251b098bec65f8e762aa3fd/commodore-amiga/amos/bank-or-risk/stages/replay-value/feedback.amos). The game still uses one
die, limit 10 and target 30. It now continues after the target is reached or
becomes unreachable. These are deliberate design changes approved by the user,
not corrections to the earlier endpoint's stopping rules.

## Configuration and inputs

[inputs.json](inputs.json) identifies all five sources, lawful original inputs
and the tools: AMOS Professional 2.00, Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200 with stock 2 MiB chip RAM
and no fast RAM; Build198x at `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0`.
Both tools build offline from locked existing dependencies. Neither tool's code
nor any dependency changes. This is a named execution profile, not a minimum
machine claim.

[prepare.py](prepare.py) reuses the qualified runtime filesystem builder,
preserving all 78 original file contents. It puts the sources and seven
constant-roll copies on `value.adf`. One separate `varied.adf` supplies 4,5,6,1
through Read/Data, restored at challenge reset. That authoring-only case makes
the pre-bust and bust faces different. Its import therefore cannot conceal a
broken face restoration behind repeated sixes. The source/variant hashes and
exact transformation checks identify what each native run imported.

All earlier prototype, opening, session and presentation sources remain
unchanged. Their older early-ending checks retain their own revisions. The
current [game brief](../../platforms/commodore-amiga/games/bank-or-risk/brief.md)
owns the extension's rules; the new guide explains its five stages and edits.
No public lesson changes.

## Teaching and state boundaries

`five-rounds` retains the original one-round rules but ends the challenge only
after five completed rounds or Q. Target reachability becomes a message.
`personal-best` keeps Best outside the replay reset and updates it only on a
strictly greater completed five-round score. It is memory-only; running the
program again starts at zero. A partial challenge never sets a record.

`scorecard` introduces one indexed table separately. Completed entries contain
awards, including zero. The renderer uses the completed count to distinguish
zero from a future dash and the current question mark. The five completed
entries agree with secured points. The slot counter cannot advance game rounds.

`rescue` separates a pending bust from a completed round. U spends rescue and
restores pre-roll total/face; B records zero and keeps rescue. Invalid keys
leave the decision pending. A spent-token bust finishes immediately. Q cannot
fall through into scoring. Replay restores the rescue and clears the card,
while preserving Best and the previous scan code's input handover.

`feedback` briefly draws 2,4,6 before committing the already chosen actual face
and adding it once. The six Wait Vbl instructions are an intentional short
reveal, not a reaction timer. The captured preview shows a six while total and
printed accepted roll remain zero; the settled view shows the supplied five
and total five. These are preview pictures, not extra random choices. Decisions
afterwards remain untimed. The fresh-key reader is unchanged and does not queue
choices tapped during the reveal. The native checks qualify named windows,
not every possible input arrival time or every host keyboard.

The result shows its positive contribution alongside the updated secured score
and scorecard. A zero bust shows +0. A per-challenge reached flag and one-event
cue flag acknowledge the first crossing of 30. That high cue replaces the bank
cue at that event; later rounds above 30 use the normal result cue. A final
new-best message has priority over target acknowledgement on their shared text
row. Semicolons on bottom-row messages prevent a line feed from scrolling the
board. Muted play retains all essential information.

## Observed native outcomes

| Check | Observed result | Evidence |
| --- | --- | --- |
| F2/F1 | All five sources and eight variants import, pass syntax and reach the ready screen. | [captures](captures/), [reports](reports/) |
| Five-round target | Five banks of 6 reach 30 at completed 5. Earlier completions remain playable. | [fifth](captures/five-result-5.png) |
| Early goal | Perfect rounds reach 30 at completed 3; Space continues through 40 and 50. | [30](captures/live-result-3.png), [50](captures/live-result-5.png) |
| Impossible goal | One bank of 4 followed by busts continues through five rounds, retaining the 4 and recording four zeros. | [unreachable but playable](captures/card-result-3.png), [final](captures/card-result-5.png) |
| Best higher/lower/tie | Completed 50 sets Best; completed 25 preserves 50; another 50 is not labelled new. A later 30 replaces an existing Best of 6. | [lower](captures/lower-result-5.png), [tie](captures/tie-result-5.png), [higher](captures/higher-result-5.png) |
| Scorecard | Completed zero differs from current ? and future -. Its completed awards sum to secured points; replay clears the awards and retains Best. | [zero](captures/card-result-2.png), [replay](captures/live-reset.png) |
| Pending bust | Total 12 leaves completed/secured at zero and the first slot pending. X/R/Space do not change it or make a result cue. | [pending](captures/risk-pending.png), [held](captures/risk-pending-stable.png) |
| Spend rescue | U restores 6, keeps the round active, spends rescue; repeated/held U does not undo again. B then secures 6 once. | [restored](captures/risk-restored.png), [bank](captures/risk-result-1.png) |
| Restore distinct face | Supplied 4,5,6 reaches total 15 with face 6. U restores total 9 and face 5; another supplied 1 banks perfect 10. | [bust](captures/varied-bust.png), [restored](captures/varied-restored.png), [perfect](captures/varied-perfect.png) |
| Accept zero | Pending B records zero and leaves rescue available. The next round can still spend it. | [accepted](captures/accept-result-1.png), [later use](captures/accept-restored-2.png) |
| Spent/reset token | Later busts immediately award zero. Even when 30 is out of reach, play reaches round 5. Replay restores token 1 and clears the card while keeping Best 6. | [later bust](captures/risk-result-2.png), [reset](captures/risk-reset.png) |
| Once-only target sound | The perfect game has bank, bank, high target, bank, bank: first reaching 30 sounds once. Pending/reveal/undo/invalid/terminal windows are silent. | [audio](audio/), [measurements](verification.json) |
| Muted agreement | Each perfect-run roll/result picture agrees with the audible source; the muted recordings are silent. | [muted final](captures/muted-result-5.png) |
| Feedback and stability | A transient face does not award points; the committed roll agrees with ordinary play. Waiting, held controls and invalid terminal choices do not add a result or cue. | [preview](captures/reveal-preview.png), [committed](captures/reveal-committed.png) |
| Exit | Q returns to the editor from title, active, pending bust, between rounds and final result. Partial rounds do not pass the scoring boundary. | [pending exit](captures/pending-editor.png) |
| Ordinary random source | The maintained new endpoint rolls, banks, begins another round and exits. | [bank](captures/random-bank.png), [next](captures/random-next.png) |
| Native storage | A verified exported filesystem independently cold-boots and loads the native saved program, then rolls/banks, continues and exits. | [loaded](captures/replay-value-reopened-listing.png), [reopened bank](captures/reopened-bank.png) |

The verifier checks identities, routine bodies, state-update locations, explicit
variant transformations, every required phase/capture/recording, stable and
muted picture pairs, cue counts/pitch/duration, native saved-program format and
all original runtime contents. Labels, numbers, pip meanings and F2 banners
are inspected directly; picture hashes do not interpret them. Programmatic
source contracts and host-side models do not replace those native observations.

## Balance and its limits

[balance.json](balance.json) records the exact ideal independent fair-die model
from [replay_value_check.py](../../platforms/commodore-amiga/games/bank-or-risk/replay_value_check.py).
The no-rescue score distributions agree with an independent round-distribution
convolution and the earlier target-probability implementation. Rescue cannot
increase the per-round cap or the maximum score of 50. Equality in the remaining
capacity bound remains reachable. These cross-checks can reject inconsistent
results instead of accepting a model's own constants as proof.

Banking at 6, with the first bust undone, raises reaching 30 from about 86.84%
to 96.90% and mean score from 34.99 to 36.54. Banking at 7 with that rescue policy
has a lower goal probability (90.32%) and a higher mean score (38.02). An optimal
target policy and an optimal score policy maximise different objectives; their
reported maxima are not one combined policy or human win rates.

Thirty stays a welcoming goal. The score chase supplies the longer-lived
challenge. Rescue principally adds forgiveness and changes the risk of rolling
before it is spent; the sampled best-score rescue decisions favour undo, so
we do not claim every bust question is a difficult resource-allocation puzzle.
Neither these calculations nor native correctness establishes fun. Further
human play should judge whether the extra choice and feedback earn their cost.

## Reproduction and remaining acceptance

Build the pinned emulator with `--release --offline --locked
--no-default-features` and Build198x with `--release --offline --locked`.
Run `prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
with matching lawful inputs and an empty run folder. SAMPLES is bank-or-risk,
containing prototype and stages. Populated output is refused.

Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` in [sequence.json](sequence.json) order. Each native subprocess
has a 50-second bound. Snapshots split the longer checks; their restores are not
called native Load. After `replay-value-export-requests.json`, require
`TOOL verify RUN/replay-value-settled.save.adf` before cold boot. The guest-write
waits are configuration-specific; preserve the edited session if an export
fails validation rather than trusting a closed Save As requester.

Run `verify.py RUN --disk-tool TOOL --samples SAMPLES` and inspect the frames,
including syntax and the transient reveal. [verification.json](verification.json)
records 166 required captures, 17 identical-picture pairs and 22 PCM checks.
The saved native program is 8,326 bytes. Seven negative controls reject a
missing required capture, a wrong pending picture, silent bank audio, a valid
disk missing the saved program, changed source, populated preparation output
and an inconsistent independent target probability. [media-checks.json](media-checks.json) records independent
byte-identical media reconstruction and failure controls. [artifact-hashes.json](artifact-hashes.json)
binds unedited captures and PCM. Reports replace local run roots with `${RUN}`.
ROMs, licensed runtime contents, ADFs, native programs and snapshots are excluded.
Original input hashes remain unchanged.

Human play/listening acceptance, authored replacement lessons and the uncoached
learner trial remain pending. Earlier browser acceptance does not qualify the
new rescue rule. The separate random-range/angle investigation remains outside
this work. The extension does not publish or replace lessons.
