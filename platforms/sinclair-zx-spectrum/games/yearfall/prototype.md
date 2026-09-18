# Yearfall — prototype record

**Status:** The user accepted the extended native game: “Yep, that'll do”.
Samples commit `03afc02` is the accepted endpoint. Replacement lessons remain
to be planned and authored. The [brief](brief.md) defines the rules;
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
not an implemented change. The subsequent extended game is accepted.

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

## Continued play and travellers

The user accepted the clearer land controls and authorised continuing beyond
ten years plus one occasional traveller offer. Decade summaries offer C to
continue with the same resources and history. Empty settlements cannot continue.
The first offer comes in year 3–5 and later offers are 3–5 years apart. Each
welcomed person costs six grain, then joins the current year's food and worker
counts. Declining costs nothing. The cost, grain balance and total food need
are shown before deciding. Acceptance is blocked unless welcome and food are
affordable. The harvest report includes welcome costs and admitted people.

The host model retains the old ten-year no-event comparisons above as a baseline.
Two thousand additional thirty-year trials compare always declining with welcoming
when affordable, using the same expansion policy. Declining completed 811 runs;
welcoming completed 644. Median final populations were 231 and 291 respectively.
These policy outcomes suggest a cost to rapid growth; they do not rate human
difficulty or establish that every crisis can be recovered. Fifteen host model
check groups pass.

## Native verification

Forty-three native execution groups pass on stock 48K PAL, with forty observed
year ledgers and seven traveller offers. The seeded thirty-year run ends with
284 people, 7,106 grain, 542 acres and no deaths. It declines the first offer
and welcomes later affordable offers. Reviews at years ten and twenty preserve
resources, deaths, traveller history and the next scheduled visit when continued.

A separate legal playthrough sells all land and spends the remaining grain on
food, reaching a year-three offer that cannot be afforded. Y and invalid keys
leave that offer and its resources unchanged. Restart clears history and returns
to the original settlement; quit works at the offer. Empty settlements cannot
continue. Held acceptance and continuation keys trigger only one action.

The final listing was entered into a fresh ROM using keyword keys and saved
with `SAVE "yearfall" LINE 10`. Checks load the tape in a separate process; game
input is through keys and memory observations are read-only. The reproducible
fixture uses ROM `RANDOMIZE 17` and `RUN 200`. The executable reports Emu198x
0.24.0, built from `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3`; its identity is
recorded in the evidence. Source/target, stored-token, tape-checksum and evidence
identity audits pass. No incomplete-snapshot retries were needed in this run.

Original traveller offer, unaffordable offer and decade-summary captures were
visually inspected. The updated TAP was launched in the native emulator for
playtesting. The user accepted this extended version. The allocation editor currently
accepts four digits; this is a practical limit on very long runs. The trial does
not establish indefinite play at arbitrarily large populations. No replacement
lessons or website change are published.
