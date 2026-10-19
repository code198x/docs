# AMOS session checkpoints

Eight complete sources develop the checked one-round opening into the accepted
10/5/30 challenge: a supplied score-lifetime trace, input routine extraction,
next-round practice, once-only awards, completed rounds, success, impossibility
and replay. The maintained presentation/sound endpoint is unchanged. These are
authoring checkpoints with editing instructions and explanatory answers, not
published replacement lessons or evidence of beginner understanding.

## Configuration and source identity

[inputs.json](inputs.json) pins the eight sources, lawful firmware/media and
tools. Execution uses AMOS Professional 2.00 through Emu198x 0.34.2 at
`6cc5d5f9e7fe6507a079f237bc44da0dc95fe25c`, PAL A1200, stock 2 MiB chip RAM,
no fast RAM. Build198x at `f7016398deb1fff9dc1efb6713dfab8c7bacf2d0` masters
and verifies OFS media. Both tools build offline with locked existing
dependencies. No runtime, language implementation or dependency is added.

The qualified [sound-audit builder](../2026-10-amos-bank-or-risk-sound/prepare.py)
reconstructs a valid boot filesystem preserving all 78 original runtime file
contents. Our eight sources and eleven authoring variants occupy a separate
source disk. Each import starts in the blank editor; its listing is retained
before F2/F1. The source and variant hashes identify what was supplied.

The constant-roll variants replace exactly one supplier assignment. Learners
can make that edit without DATA or an acceptance-test generator. The retained
baseline is the previously checked one-round source with supplied roll 4.
Its game images are compared with the extracted-input version using identical
accepted controls. This checks the named windows; it does not prove equal
latency for every possible arrival time.

## Native syntax correction

The first success/impossibility versions failed F2 with `No THEN in a structured
test.` Their terminal footer used single-line If/Then statements inside a
structured Else branch. The [original control-structure chapter](https://amospromanual.dev/05-04-control-structures.html)
prohibits that mixture. The corrected sources use a nested If/Else/End If block
with the same two messages. The failed sources, variants, syntax captures and
reports remain in [diagnostics/](diagnostics/); the initial data-image hash is
recorded separately. The two affected sources and four supplier variants are
reimported and rechecked. Other source contents are unchanged. This is a source
fault, not evidence of an emulator defect.

## Complete disk writes before trusting the export

The first Save As requester closed, but exporting after its 360-frame wait
failed validation with `corrupt ADF: bitmap references`. Its root bitmap-valid
flag was zero and the bitmap still offered allocated file blocks as free.
The attempted cold boot did not reach AMOS; the blue Workbench capture is
retained as a failure, not successful reopening.

Restoring the same saved session and running 240 more native frames, without
source edits or another Save As, produced a verified export. Only root block
880 and bitmap block 881 changed; all 79 file payloads, including the saved
program, remained byte-identical. The root flag became 0xFFFFFFFF and allocation
records agreed. [write-completion.json](diagnostics/write-completion.json) and
the [early manifest](diagnostics/early-save-manifest.json) retain this evidence.
This establishes unfinished filesystem bookkeeping at the first export; it does
not identify a language-source fault or confirmed emulator defect.
`compare_writes.py --disk-tool TOOL EARLY SETTLED` repeats the payload and block
comparison and requires rejection of the early filesystem and acceptance of the
completed one. Its assertions describe these recorded images, not all disk writes.

The passing sequence includes the additional run time, then exports to the new
`session-settled.save.adf` path and verifies it **before** cold boot. That observed
wait is configuration-specific, not a universal safe delay. The guide requires
a completed disk write and a valid exported filesystem rather than inferring
success from the requester or the tool's saved response. Original loaded media
is untouched. Licensed failed/successful ADFs and snapshots remain excluded.

## Teaching boundaries

`keep-secured` supplies a trace, not live banking. `read-fresh` only extracts
existing input. `next-round` repeats practice without accumulating session
points. `award-once` adds the session score outside the round-reset loop and
updates it once after a completed round. `count-rounds` adds a bounded completed
counter. `recognise-success` introduces the target but still permits all five
rounds if it is not reached. `recognise-impossibility` adds the strict upper-bound
test. `replay` adds the application loop and resets the session and round values
while preserving the previous scan code for a held replay key.

The [session guide](https://github.com/code198x/code-samples/blob/3d47c2f3d027782aa47b12ec45745903cb603ba5/commodore-amiga/amos/bank-or-risk/stages/session/README.md) explains these differences and the contracts of the input
and drawing routines. Native random play is kept separate from prescribed
values. The renderer reads existing values and never chooses a roll or awards
points. The ledger and reset locations are inspected as well as the pictures.

The maintained board/sound endpoint uses a one-based For counter. These sources
use an explicit completed-round counter. A future integration must explain or
remove that representation change; renaming one variable is not a valid join.
Existing board/sound and endpoint persistence evidence remains attached to its
recorded source revision. This pass does not qualify an untested integration.

## Recorded outcomes

| Check | Observed outcome | Native evidence |
| --- | --- | --- |
| Supplied lifetimes | Bank 4, reset total to 0, preserve secured 4; bust 11 awards 0 and keeps 4. | [trace](captures/keep-secured-start.png) |
| Input extraction | The same B/X at zero, held roll and bank produce identical pictures before and after extraction. | [baseline](captures/baseline-3.png), [extracted](captures/extracted-3.png) |
| Next round | A result ignores X; Space clears the total/last face without inventing a session score. | [result](captures/next-result.png), [reset](captures/next-reset.png) |
| Award once | Bank 4, wait/hold B/press X or R without another award; next round starts at 0 with secured 4. A bust at 12 contributes 0 and keeps 4. | [bank](captures/award-bank.png), [reset](captures/award-reset.png), [bust](captures/award-bust.png) |
| Count opportunities | After two banks, completed is 2 and remaining is 3. Five banks reach completed 5, secured 20, remaining 0 and offer no sixth round. A bust counts once despite its zero award. | [two](captures/count-2.png), [five](captures/count-5.png), [bust](captures/count-bust.png) |
| Success without early failure yet | Three perfect rounds reach 30 in round 3 with two unused rounds. Five banks of 4 still run to round 5 and report the missed target. | [success](captures/success-3.png), [miss](captures/missed-5.png) |
| Strict impossibility | Two opening busts leave an upper bound of 30 and still allow Space; three leave only 20 and end. | [equality](captures/failure-2.png), [unreachable](captures/failure-3.png) |
| Preserve success | The impossibility version still reaches 30 with three perfect rounds. | [result](captures/possible-success-3.png) |
| Endings hold | Wait, X, R and Space leave the terminal score, count and picture unchanged. Q returns to the editor. | [success wait](captures/success-wait.png), [failure wait](captures/failure-wait.png) |
| Replay both endings | Held A resets score, completed rounds, total and face exactly once; the first fresh roll acts once. | [win reset](captures/replay-win-reset.png), [loss reset](captures/replay-loss-reset.png), [fresh roll](captures/replay-win-first-roll.png) |
| Ordinary play and quit | The maintained random source rolls, banks, starts another round and exits. Q also exits active, between-round and terminal phases. | [bank](captures/random-bank.png), [next](captures/random-next.png), [between quit](captures/between-editor.png) |
| Native persistence | Save As exports a native session.amos; a separate cold boot loads it, rolls/banks, starts another round and exits. | [saved](captures/session-saved.png), [loaded](captures/session-reopened-listing.png), [bank](captures/reopened-bank.png) |

The verifier checks source and variant identities, exact restoration of the
pre-extraction program, unchanged input/drawing routine bodies, the isolated
award additions, nonempty required captures and byte-identical picture pairs
for extraction, ignored input, stable endings and replay reset. The native
filesystem and saved program are checked separately. Numerical labels, messages,
pips and F2 results are inspected: image hashes alone do not read their meaning.

[verification.json](verification.json) records 169 capture checks and 41
byte-identical picture pairs. The reopened native program contains 4,452 bytes.
[media-checks.json](media-checks.json) records independent byte-identical media
rebuilds and negative controls. Missing captures, a wrong reset image, changed
source, an invalid export, a valid disk missing the saved program and populated
preparation output all make their respective checks fail. All original runtime
file contents are preserved in both preparation and the saved export. Native
source execution is distinct from human play/listening acceptance or learner
outcomes. No public lessons change.

## Reproduction and limits

Build the pinned emulator with `--release --offline --locked
--no-default-features`; build Build198x with `--release --offline --locked`.
Run `prepare.py --disk-tool TOOL --amos AMOS --samples SAMPLES --run-root RUN`
with matching lawful local inputs and an empty run folder. SAMPLES is the
bank-or-risk folder containing prototype and stages. The inherited helper
refuses populated output before generating probes or copying runtime files.

After `session-export-requests.json`, run `TOOL verify
RUN/session-settled.save.adf` and require success before the cold boot.

Run `replay.py PHASE.json --emulator EMULATOR --kickstart ROM --amos AMOS
--run-root RUN` in [sequence.json](sequence.json) order. Each emulator subprocess
has a 50-second limit. Long sessions are split at native snapshots between
rounds; only the persistence cold boot starts a separate machine from its
exported disk. Restoring a running snapshot is not presented as saved-program
Load. Inspect imported listings, F2 banners and gameplay pictures: a successful
subprocess alone proves none of those outcomes.

[reports/](reports/) retains native observations with local run roots replaced
by `${RUN}`. [artifact-hashes.json](artifact-hashes.json) binds unedited native
screenshots. Licensed runtime contents, ROMs, ADFs, native saved programs and
snapshots are excluded. Source-only preparation, scripts, identities and hashes
permit a lawful rerun. The configuration is not a minimum hardware claim.

Human listening/play acceptance and the uncoached learner trial remain pending.
