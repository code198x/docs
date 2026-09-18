# Yearfall — prototype record

**Status:** The user authorised this bounded BASIC trial. Native play acceptance
and replacement lessons remain pending. The [brief](brief.md) defines the rules;
the [source review](review.md) records the inherited economy problems.

## Implementation

The maintained source is `code-samples/sinclair-zx-spectrum/basic/yearfall/prototype/yearfall.bas`.
It keeps a draft allocation separate from the settlement. Editing trade, food or
planting recalculates cost, food-supported workers, land and possible harvest
balances. Space resolves only valid allocations. A report accounts for every
resource change; reports wait for a separate key press before continuing.

Input is a bounded whole-number editor, not a BASIC expression prompt. Buying
and selling have separate visible controls and accept unsigned acre counts.
The selected action supplies the direction of the internal land change. A new
land action replaces the previous one; zero clears it. The plan explicitly
states grain spent or received, and the report labels each direction. Empty entry retains the
old amount; deletion, cancellation and held-key release are explicit. Invalid
plans can remain visible while the player edits another field, but cannot spend
resources or advance the year. The completed game is deliberately silent.

## Native feedback and control revision

The user found the game tough and could not understand how to recover. They
then explained that buying and selling land had not both been apparent. The
user approved separate Buy land and Sell land controls, with positive amounts
and explicit grain costs or proceeds. This revision addresses that confusion;
the economy is unchanged. Broader recovery guidance remains a possible follow-up,
not an implemented change. Further native feedback is pending.

## Economy evidence

A separate host model checks initial accounting, land ownership, planting area,
fed-worker capacity, combined costs, a poor harvest, partial food and a land
sale. It compares three simple policies across 1,000 deterministic Python seeds
each. Ten model check groups pass and all 3,000 runs preserve nonnegative
resources and consistent population changes.

| Policy | Runs with no deaths | Empty settlements | Median final grain |
|---|---:|---:|---:|
| Keep the original land; feed and plant what is affordable | 717 | 241 | 626.5 |
| Buy toward worker capacity while reserving current food; sell in shortages | 979 | 7 | 695 |
| Buy toward worker capacity from available surplus; sell in shortages | 980 | 5 | 1,035 |

These are comparisons of the stated policies, not optimal strategies, player
success rates or Spectrum random sequences. They suggest that using land trades
can matter. They do not establish that the prototype is difficult or enjoyable.

An early native managed run produced yields 2, 2, 3, 2, 3, 2, 3, 5, 4, 4.
It sold land to cover shortages and emptied in year ten. Every resource update
matched the model. `verification/evidence/poor-harvest-trial.json` retains the
trace and original source identity. The check had incorrectly required an
unseeded policy run to survive; the outcome is valid game behaviour and evidence
of a recovery spiral, not an implementation failure.

The full-run regression uses ordinary ROM `RANDOMIZE 17` and `RUN 200` commands
to make the harvest/market sequence reproducible. That fixture starts from the
same initial settlement; it does not inject resources or alter program lines.
The title, normal random start, reset and input checks remain separate. Captures
of the final run must be understood as a seeded legal playthrough.

## Native verification

Thirty-two native execution groups pass on stock 48K PAL. The final tape was
entered in a fresh ROM using keyword keys and `SAVE "yearfall" LINE 10`, then
loaded in a separate process. The executable reports Emu198x 0.24.0, locally
built from `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3`; its SHA-256 is recorded in
the evidence. Memory observations are read-only. Incomplete snapshots during
string updates are retried for at most eight frames.

Checks cover fresh tape and token identity, title/start/quit, ignored keys,
whole-number entry, deletion, cancellation, held digits, bounded input,
combined budgets, excess food, ownership and planting limits, fed labour,
buying/selling, replacement and cancellation of land plans, zero clearing,
unsigned acre entry, explicit cost/proceeds, partial rations, persistent state, all ten yearly ledgers,
retained reports, both endings, held Space, uppercase controls and restart.
The seeded ten-year run ends with 93 people, 576 grain, 178 acres and no deaths.

The final audit confirms ordered unique line numbers, literal branch targets,
source/build/model/result identities, tape checksums, auto-start line 10 and
stored token identity. Original planning, purchase, sale, editing, invalid-plan, harvest and
ending captures were visually inspected. The native emulator was launched from
the final TAP for the user's playtest.

These checks establish executed rules and readable captured output. Human
acceptance, original-hardware timing and independent learner outcomes remain
unestablished. No replacement lesson or website change is published.
