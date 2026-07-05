# Flock — Design-Stress Pass (2026-07-05)

Adversarial refutation of the **shipped** Amiga assembly first game. Target build:
`code-samples/commodore-amiga/assembly/flock/unit-18/flock.asm` (the cumulative
final program, 2076 lines, which assembles `flock.adf`). Stance: the player who
wants to win cheaply, the reviewer with a deadline, the kid mashing buttons —
never the designer's friend. Every finding is a falsifiable scenario checked
against shipped code, not the brief.

**Bottom line:** Flock **clears** the jeopardy bar and — unlike Starfield —
carries genuine, forceable, fairly-telegraphed jeopardy under optimal play. No
BREAKS. But it has a serious tension leak: **the river inversion, the entire
Arc 2 signature mechanic, is bypassable** — you can win every level touching the
water exactly once, on the bridge, then walking sideways on dry land. And the
**winnability gate is only half-proven**: Flock uniquely ships with *no capture
manifests* (no `capture/`, no `.script.json` anywhere under the Amiga games), so
its loss path has never been driven by a repeatable scripted run. The loss is
*reachable and forceable from code analysis*; it is *not demonstrated by
artifact*. The missing loss-script is a gate item.

---

## Lead verdicts (the two priorities)

### Ghost hearts (named specimen) — **CLOSED**

The design-stress methodology and the winnability gate both cite "ghost hearts in
the pens — a reset that doesn't reset every plane" as the house specimen. In the
**shipped** unit-18 code it is **closed, cleanly**, and the fix is deliberate.

The residents (penned-sheep glyphs) live in **plane 2**; the farm-wide clear
touches only **plane 1**:

- `startgame` (lines 814–842) clears plane 1 rows 0–239 via `rectclear`
  (`lea plane,a0`, lines 831–835), then calls **`clearfold`** (line 836) which
  clears plane 2 rows 16–23 — exactly the 8 rows `penglyph` writes at `PEN_ROW=16`
  (`clearfold`, lines 1347–1355; loop count `8*ROW_BYTES/4-1` = 79 → 80 longwords
  = 320 bytes = 8 rows, no off-by-one).
- `nextlevel` (lines 878–900) does the same pair (`rectclear` + `clearfold`, lines
  889–894) on level-up.
- The HUD "hearts" (life-sheep icons, plane 1 row 244, *below* the row-0–239
  clear) are cleared by `drawflock`'s own `rectclear` before redraw
  (lines 1446–1450).

Both reset paths clear **both planes**; the icon strip clears itself. The
`clearfold` comment even names the trap: *"the farm-wide clear never touches them.
New level, empty pens, BOTH planes."* This is the *fixed* form of the specimen —
report it CLOSED with evidence. (See the related BLEEDS-3: other state is *not*
reset, so the reset is not total — but the pen residents, the named case, are.)

### Loss reachability — **REACHABLE, FORCEABLE, FAIR** (but unproven by script)

A loss is **deterministically forceable**, several ways:

- **Drown (cleanest deterministic loss).** Hop up into the stream rows (44–76,
  `checkstream` gate lines 666–669) at any column that is neither the footbridge
  (sheep-centre 144–176, lines 672–675) nor under a ferry → three contactless wet
  frames → `losesheep` (`.drowned`, lines 701–708). From a cold boot the field
  edge (e.g. x=0) is open water; hop up, dead in ~3 frames. Repeat 5× → `lives=0`
  → `gameover` (`losesheep`, lines 715–724). No RNG, no timing skill required.
- **Squash.** Bit 9 (tractor **or** cow, position-independent) kills on contact
  wherever she stands (`checksquash`, lines 630–632). Hop into an oncoming lane.

The bolt fail-behaviour is **reachable and fairly telegraphed**: `fret`
(lines 527–560) builds `nerve` only when `sheepy < ROW_FIELD` (176) and she is
idle; at `NERVE_EDGE` (150 = 3 s) she trembles (walk-on-spot, `showframe`
lines 1180–1184) *and* plays one worried baa; at `nervebolt` (250 → 160 by level 4)
she bolts (`PANIC_HOPS` = 3 involuntary up-hops, lines 550–554). That is a ~2 s
visual+audio warning before control is taken. Fair.

**So Flock has a real loss and real jeopardy — it passes `a-game-needs-jeopardy.md`
on substance.** The gap is *procedural*: the winnability gate wants the loss path
"exercised the same way" by a checked-in script in the game's `capture/` directory
(commercial-bar-revamp.md, lines 104–109). Flock has **no `capture/` and no
scripts at all** — the playtest sheet header concedes the four first games are
"script-verified to their **win** states." Flock's loss half is therefore
**unproven by artifact**, even though it is provable. That is a gate item (see
end).

---

## Findings (severity-ordered)

### BREAKS — none

No unwinnable level, no soft-lock, no whole-game dominant strategy, no immortality
farm. Difficulty plateaus at `MAXLEVEL=4` and the table repeats (`applylevel`,
lines 904–906), so no runaway-to-impossible. There is **no risk-free way to
score**: `ROAD_POINTS` fire only past `ROW_BANK_TOP=88` (lines 488–494) and
`PEN_POINTS` only at a pen (lines 1318–1321), both of which require a road
crossing where bit-9 contact kills. Worth stating plainly: this is a materially
healthier game than its C64 sibling.

### BLEEDS 1 — The bridge-and-shuffle bypasses the entire river inversion

**Scenario:** Every sheep spawns at `SHEEP_X=152` → centre 160, which sits inside
the footbridge span `BRIDGE_MINX..MAXX` = 144–176 (lines 137–138, 745). Go
*straight up* from spawn: you cross the stream on dry planks (`checkstream` bridge
check, lines 672–675) — **no ferry, no ride-mode collision, ever**. Now the trick:
row 40 (`ROW_HEDGE`) sits *above* `STREAM_TOP=44`, so `checkstream` does not judge
it (lines 666–669) — it is dry land. Nothing is drawn there but a background colour
band (the "hedgerow" is a `COLOR00` change, not a sprite, so it has no collision).
So: cross once on the bridge, stop at row 40, and **walk sideways to any pen
column** (sheepx clamps 0–304, pen centres span 8–311, lines 1373–1387), then hop
up into the pen. Each sideways hop also resets `nerve` (line 476), so the shuffle
never frets or bolts.

**Consequence:** the bale, the duck, ride-mode collision, the diving-duck timing
layer — the whole of Arc 2's headline mechanic and its "two meanings from one
`CLXDAT` read" teaching payoff — become **optional scenery you never touch to
win**. The player faces 5 road crossings (real jeopardy) and 0 river crossings.

**Current answer:** none — geometry permits it directly.
**Severity:** BLEEDS (not BREAKS: the road half still supplies genuine, losable
jeopardy 5× per level, so the game is not trivialised — one of its two mechanics
is).
**Suggested direction (level-data, pedagogy-safe):** make the stream span the full
approach so only the *centre* pen is bridge-reachable and the other four force a
ferry crossing; or add a hedgerow the player cannot cross horizontally above the
water. Note the wall option needs playfield-vs-sprite collision, a technique Flock
deliberately avoids (sprite-only collision) — so prefer the geometry fix over a
new collision type.

### BLEEDS 2 — The black-sheep "gamble" has no downside

**Scenario:** The brief and Ship Test promise "a real risk/reward" — "risk it or
play safe." In code, a black sheep differs only in `hopgap = SKITTISH (4)` vs
`COOLDOWN (6)` (lines 62–63, 757/764) and pays `+BLACK_BONUS` (100) on top of
`PEN_POINTS` (25) — 125 vs 25 (lines 1318–1321). But movement is **input-driven**:
a *shorter* cooldown means her hops register *sooner*, i.e. she is **more**
responsive and easier to steer, not harder. `nerve`/`nervebolt` are per-frame and
level-based, untouched by her coat, so she carries no extra bolt risk either. The
gamble is **all upside**: easier to control *and* worth 5×. There is nothing to
"dare."

**Current answer:** none — the risk half is absent.
**Severity:** BLEEDS (a promised tension the code doesn't deliver; the playtest
sheet's own probe — "Are you tempted? If never: bonus too small or risk too large"
— will misread this as a *tuning* issue when it is a *mechanics* absence).
**Suggested direction:** give the black sheep a genuine handling cost — e.g. she
overshoots (a longer `STEP`), or her faster rhythm makes the buffered-hop harder
to place — so speed cuts both ways.

### BLEEDS 3 — The reset is not total; the water grace leaks between and within attempts

**Scenario A (stale grace, within a life).** `drownarm` (the 3-frame "just landed,
CLXDAT is a frame behind" forgiveness, lines 693–700) is cleared **only** on
ferry-contact (line 680) and on drowning (line 702). Leaving the water *upward onto
dry land* exits `checkstream` at `.dry` (lines 667–669/675) **without clearing it**.
So: drift in open water 2 frames (`drownarm=2`), scramble onto the bridge or bank
before the 3rd — `drownarm` stays 2 — then step back into open water later and you
**drown after 1 frame instead of 3**. The grace window is silently inconsistent.

**Scenario B (between-attempts leak).** `startgame` (lines 814–842) resets lives,
score, pens, won, gameover, nerve/panic (via `newsheep`) — but **not** `drownarm`,
`cooldown`, `curframe`, `duckstate`/`ducktimer`, nor the **vehicle phases**
(`tractx`…`cowx`, only ever written by `drivelanes`/`applylevel`-speeds). So a
second game inherits the first game's traffic positions and a possibly-nonzero
`drownarm`. The brief's "No random hazards — lanes are deterministic loops"
holds *within a boot* but **not game-to-game**: the opening traffic you learned in
game 1 is not the traffic of game 2. (The named ghost-hearts case *is* reset;
these siblings are not.)

**Current answer:** partial — `startgame` resets the visible economy, not the
motion/grace state.
**Severity:** BLEEDS (small, but Scenario A is a real fairness inconsistency and
Scenario B undercuts a stated design promise; also matters for a loss-script,
which must boot fresh to be reproducible).
**Suggested direction:** clear `drownarm` in `newsheep`; reset vehicle phases (and
`cooldown`/`duckstate`) to their initial data values in `startgame`.

### BLEMISH 1 — No terminal victory; the game is an endless plateau

`nextlevel` only increments `level` and `applylevel` clamps to row 4 forever
(lines 878–918); there is **no game-end "whole flock safe" state**. Brief Section 9
promises "Game end: a warm 'whole flock safe' beat" — the shipped game has only
per-level fanfares and plays until you lose. Endless-with-plateau is period-honest
for a crosser, but the promised ending is absent, and level 4-onward is identical
(the playtest sheet's "plateau or grind?" question answers itself in code:
plateau). Decide whether the promise is dropped or a finish is added.

### BLEMISH 2 — Panic can pen for you (fear rewards)

`steer`'s panic path calls `trypen` when a bolt lands at the fence (lines 429–435).
So if a sheep is idled to a bolt while already lined up under an open pen, she
**pens herself hands-free** — and if she is the black sheep, banks +125 with no
input. The "fear" mechanic can pay out. Low-value (she must already have crossed
and be aligned), but it inverts the intended pressure. Route to playtest to see if
it reads as a bug.

### BLEMISH 3 — Nerve is neutralised by never standing still

Any hop in any direction resets `nerve` (line 476), and the dominant strategy hops
continuously. A confident/mobile player never sees the tremble or bolt at all; the
"held-breath" tension is entirely self-inflicted by hesitation. As designed
(pressure on the ditherer) this is defensible, but combined with BLEEDS 1 the nerve
system contributes almost nothing to optimal play. Note for tuning, not a fix.

---

## Closed holes (verified in shipped code)

- **Ghost hearts (plane-2 residents).** Both reset paths call `clearfold`; HUD
  icons self-clear in `drawflock`. Every plane the residents/hearts live in is
  reset. CLOSED (lead verdict above).
- **Buffered hop / no double-fire.** A tap during cooldown banks into `hopbuf`
  only on a *fresh* press (`sawneutral` gate, lines 421/424) and is replayed once
  when ready, consuming the cooldown via `.stepped` (lines 439–445, 474). A banked
  left/right replays raw and steers correctly. No path fires two hops inside one
  `hopgap`. CLOSED.
- **Position-disambiguated collision bits.** Bits 10/11 (cart/bale, Rover/duck)
  mean "kill" only when `sheepy >= ROW_BANK` (80) and "ride" only in stream rows
  44–76; the sheep only lands on rows ≡0 mod 8, so there is no reachable band
  between 76 and 80, and no killing sprite (cart 142, Rover 120, bale 60) reaches
  row 80. No false kill / false ride zone. CLOSED.
- **No immortality / risk-free farm.** All scoring requires crossing the bit-9
  road. Unlike Starfield's turret park, there is no static safe-and-scoring
  position. CLOSED.
- **Carried off the edge drowns.** Ferry drift off either screen end is a loss,
  not a safe wrap (`checkstream .edges`, lines 687–692). CLOSED.
- **No difficulty soft-lock.** `MAXLEVEL` clamp caps the ramp; levels stay
  solvable. CLOSED.

---

## Open questions (routed from the playtest sheet)

These need hands on a pad; the code is consistent with either reading:

- **Ride lock-on feel.** Boarding bale/duck: does the 3-frame `drownarm` grace read
  as "locked on" or as a lurch? (See BLEEDS 3 — the grace is inconsistent by
  code, so the *feel* may vary run to run.)
- **Duck-dive telegraph at level 2+.** `DUCK_WARN=50` is constant while
  `duckpaddle` drops to 130 by level 4 — proportionally *more* warning at higher
  levels. Confirm the tail-up frame reads in time.
- **Tremble vs flicker.** Does `showframe`'s two-image alternation (lines 1180–1184)
  read as fear or as a glitch? Discoverability of the whole nerve→bolt rule (does
  the *first* bolt teach cause-and-effect?) is unverified — there is no on-screen
  meter, by the author's earlier "behavioural" call.
- **The black-sheep temptation.** Per BLEEDS 2 the code offers no risk — expect
  "always take it." If the sheet reads that as "bonus fine," it will mask the
  missing-risk mechanics finding.
- **The curve / which level is the wall.** With BLEEDS 1 available, a tester using
  the bridge-shuffle will find *no* wall on the river; the wall (if any) is road
  timing only.
- **Jingle across five title visits; sting vs dwell lengths.** Sequencer only;
  code has no obvious fault.

---

## What gates a fix before the next build

- **BLEEDS 1 (bridge-and-shuffle)** — gates. It hollows out the game's headline
  second mechanic and its central teaching payoff (two-modes-from-one-`CLXDAT`).
  A level-data geometry fix is cheap and pedagogy-positive.
- **The missing loss-script — GATES (explicitly).** Flock is the only first game
  with no `capture/` directory and no scripts; its winnability gate passes on the
  **win half only**. Per commercial-bar-revamp.md (lines 104–109) and
  a-game-needs-jeopardy.md, the loss path must be exercised by a repeatable
  scripted run. The loss is forceable (drown route, above), so authoring
  `unit-18/capture/death.script.json` (and a matching win script) is
  straightforward and **must land before the build is re-marked complete**. This is
  a gate item.
- **BLEEDS 2 (fake gamble)** and **BLEEDS 3 (grace/phase leak)** — should ride the
  same build. BLEEDS 3's `drownarm` clear is a one-line fix and removes a genuine
  fairness inconsistency; BLEEDS 2 restores a promised tension.
- BLEMISHES 1–3 — batch into the tuning pass; none block, but BLEMISH 1 (no
  terminal win) needs a decide-or-drop on the brief's promise.

Ghost hearts itself does **not** gate — it is verified closed.
