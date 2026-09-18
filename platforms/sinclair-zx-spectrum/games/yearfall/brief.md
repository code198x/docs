# Yearfall — BASIC prototype brief

**Status:** The user accepted the native BASIC prototype, including separate
buy/sell controls, decade continuation and traveller offers. The accepted source
is samples commit `03afc02`. The user authorised the [teaching progression](lesson-brief.md); the approved replacement
lessons are [published in Hidden worlds](lessons.md).

## Experience and scope

Manage one settlement, reviewing the results every ten years. Each year, inspect people, grain, land and
the offered land price. Edit a combined plan for trading land, feeding people
and planting, then commit it. The recurring choice is how much grain to retain
against a poor harvest and how much to invest in productive land. Selling land
can bridge a shortage but reduces subsequent growing capacity.

The first trial starts with 60 people, 360 grain and 100 acres. Each person
needs three grain and each fed person can work two acres. Each planted acre
costs one grain and yields two to five grain, selected at harvest. Land costs
six to ten grain per acre, with one price for buying and selling in that year.
The year has no deadline and the player sees the combined budget before
committing it. Food supports whole people: partial rations do not count as an
extra person. A starvation warning is explicit. Unfed people do not supply
planting labour. Food above the requirement is allowed but buys no extra growth.

A year resolves as trade and expenditure, food-supported population, harvest,
then newcomers. When everyone is fed, newcomers equal five per cent of the
opening population, rounded down. Otherwise none arrive. Newcomers join after
the harvest and cannot work that year. Grain, land and people persist.

Every ten years the report shows remaining resources, cumulative deaths and
travellers welcomed. C continues ruling the same settlement; R starts again.
An empty settlement ends the run and cannot continue. Summary text describes
actual outcomes; it does not award an unreachable population rating. Restart is available from
the plan, report and ending. The title is a separate first-entry screen.

The user authorised one occasional traveller event before planning. The first
visit occurs in year 3–5, then visits are spaced 3–5 years apart. Each offers
3–6 people for six grain each. Acceptance immediately spends the welcome cost
and adds those people; they require food and can work in the same year. The
screen shows the cost, remaining grain and total food need. Y welcomes them only
if the stock covers both welcome and food; N declines with no resource change.
The harvest report accounts for welcome costs separately from food and seed.
Restart and quit remain available at the offer.

No combat, upgrades, additional event catalogue, saved campaigns or assembly
helper belong to this trial. Harvest, market and traveller variation are random. There
is no claim that every random sequence can be rescued. A session's duration
and enjoyment require native play, not a forecast from source size.

## Target, controls and presentation

Stock PAL 48K ZX Spectrum, Sinclair BASIC, keyboard and a self-starting TAP.
Sources live in `code-samples/sinclair-zx-spectrum/basic/yearfall/prototype/`.
Emu198x enters the maintained listing through ROM keyword keys, saves it, then
loads that tape in a fresh process for execution checks. The development host
also runs a separate Python economy model. Neither adds runtime capability to
the Spectrum.

S starts. B buys land and S sells land, each taking a positive number of acres.
Zero clears the land plan; choosing one action replaces the other planned land
action. F/P edit food and planting. Digits enter a new amount; Enter accepts;
Delete erases and X cancels an edit. Space
commits a valid plan or continues a report. R restarts and Q quits outside the
number editor. Held keys count once. Blank entry leaves the previous plan.

The screen is a compact ledger with aligned quantities and costs. It shows
remaining grain, food requirements, land after trading and fed-worker capacity.
Buying and selling have separate visible rows. The plan states how much grain
will be spent or received, and the report labels land purchases and sales.
A valid plan includes its possible post-harvest grain range. The report accounts
for opening grain, trade, food, seed and harvest before showing the balance.
Text carries each meaning; colour separates headings and totals. The game is
deliberately silent. All visual content is BASIC text, with no external assets.

## Learning and possible development

The distinct subject is constrained allocation with consequences across turns.
Programming relationships include a draft plan versus committed state, integer
limits, validation, a common year-resolution routine and a report that explains
changes. Maths includes a resource ledger, bounded randomness and rounded
population growth. The Caverns offers a useful contrast: state there describes
an unseen place, while here it limits future decisions.

The authorised [thirteen-lesson progression](lesson-brief.md) begins with a
settlement ledger, adds feeding and seed constraints, resolves one harvest, then
introduces editable plans, retained years, land trading, travellers and decade
reviews. Eleven runnable checkpoints preserve the accepted game as their
endpoint. The approved replacement pages are published in Hidden worlds.

## Verification and design risks

Check combined costs, negative trades, land and fed-worker limits, partial
rations, excess feeding, reset, empty settlement, ten-year reviews, continued state and traveller acceptance/refusal.
The editor must reject expressions and unwanted characters, bound input length,
handle deletion and cancellation, and avoid repeated actions from held keys.
Check every resource delta against the model during legal tape-driven play.
Inspect the planning, invalid-plan, harvest and final screens at native scale.

Host comparisons use simple policies with deterministic Python seeds. They can
show attainable outcomes and accounting invariants; they do not measure player
success, mirror Spectrum random sequences or prove an optimal strategy. Native
play should establish whether the plan is readable and whether expansion,
reserves and recovery offer interesting choices. If allocating becomes rote,
revise the economy or information before adding more systems.
