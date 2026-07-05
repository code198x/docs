# The Long Night — design-stress pass (2026-07-05)

Adversarial refutation of the **shipped** ZX Spectrum assembly game *The Long
Night* (catalogued `game: gloaming, pass: 2` — a separate module, own codebase).
Target: the complete final program, `code-samples/sinclair-zx-spectrum/assembly/the-long-night/unit-10/steps/step-01.asm`
(2064 lines). All findings verified against that shipped source, not the brief.
No game code or briefs were edited.

## Framing correction (read first)

The brief describes a **"timed dawn win after five watches"** and asks whether a
player can "camp a safe corner to wait out the night." **The shipped game has no
timer.** The night is not a clock. Each watch ends only when the player lights
**all eight lamps simultaneously** (`lit_count == NUM_LAMPS`, play_step:179-181);
the fifth such completion is the dawn / true win (`.thedawn`, 193-204). Nothing
advances while the player stands still — no watch counter ticks, no dawn
approaches. **The camp-the-clock dominant strategy is therefore not constructible
and is a closed hole** (see Closed holes). Every finding below is re-anchored on
the real mechanic: a lamp-lighting race against a single grudge-bearing snuffer
whose pace and board-control (tendril reach) escalate per watch.

---

## Findings (severity-ordered; propagation verdicts lead)

### PROPAGATION 1 — Death-beats-victory on the tie frame — **INHERITED (mechanism); MUTATED (exploitability)** — BLEEDS

**Verdict: INHERITED.** The Gloaming frame-ordering defect is present, structurally
identical. `play_step` (168-204) runs, in order: `player_step` → state check →
`draught_step` → state check → **then** the win check:

```
play_step:
    call    player_step
    ld      a,(game_state) / cp STATE_PLAY / ret nz   ; 171-173
    call    draught_step
    ld      a,(game_state) / cp STATE_PLAY / ret nz   ; 175-177  <-- loss resolves HERE
    ld      a,(lit_count)  / cp NUM_LAMPS / ret nz    ; 179-181  <-- win asked AFTER
```

The antagonist's catch is resolved inside `draught_step → .contact → lose_life`
(1239, 1524-1574). On the **last life**, `lose_life` sets `STATE_LOSE` and paints
NIGHT FALLS (1560-1574); the `ret nz` at 177 then returns **before the win is ever
asked**. So the constructible edge: on the frame the player steps onto the eighth
lamp (`light_pip` takes `lit_count` to 8 in `player_step`), if the draught's step
that same frame lands adjacency-contact on the player **and it is the third life**,
the frame resolves as **NIGHT FALLS, not DAWN BREAKS** — the win condition was met
but never checked. On the fifth watch this is dawn-denial: the player lit the whole
night and is told the night fell.

*Falsifiable scenario:* stand the oldest-grievance lamp one cell behind you; step
onto the last unlit lamp on your final life while the draught is one cell away and
routing through your cell toward that grievance → catch and win coincide → LOSS.

**MUTATED exploitability (why it is BLEEDS, not BREAKS):** in Gloaming the
antagonist hunts the *player*, so the tie is easy to force. Here, once **any** lamp
is lit the draught turns away from the player and hunts the **oldest lit lamp**
(`draught_step .hunt/.oldest`, 1143-1168). It only prices contact when its step
toward a *lamp* happens to land on the player. The tie is therefore rarer to
construct than Gloaming's, but the defect is the same code shape and still fires.
Non-fatal catches (lives > 0) are safe: `lose_life` respawns, state stays PLAY, and
control falls through to the win check the same frame — so only the last-life tie
denies the win.

*Suggested direction:* ask the win before pricing the antagonist's step (or, on a
fatal catch, re-ask the win once if `lit_count == NUM_LAMPS` before committing
STATE_LOSE). One re-order; no technique-budget impact.

---

### PROPAGATION 2 — Wall-hug turns lethal while the wisp phases through a wall — **INHERITED** — BLEEDS

**Verdict: INHERITED.** Same mechanism as Gloaming. The wisp's attribute clears the
wall bit, and the wisp moves onto wall cells without a wall check, so for the frames
it transits a solid-looking wall the player's veto is skipped and the hug is priced
as fatal contact.

Evidence chain:

- `DRAUGHT_ATTR equ %01000101` (line 19). Bit 3 (`WALL_BIT`) is **clear**. When
  `draw_draught` writes this over a wall cell's attribute (1880-1883), that cell's
  wall bit is clear for as long as the wisp sits there.
- The wisp moves onto wall cells **unconditionally**. `draught_step .chase/.dmove`
  has no wall test; walls simply aren't darkened (`.notake`, 1259-1270) but the
  position still commits to `dtcol/dtrow`. Interior buildings exist for it to cross
  (`bldg_data`: two 4×3 blocks at cols 5-8 and 23-26, rows 5-7, line 1431-1434).
- `wall_at` reads the **live** attribute (1758-1761): `bit WALL_BIT,(hl)`. While the
  wisp is on a wall cell, this returns "not wall."
- `player_step .pmove` (737-761): `wall_at` first (`ret nz` = harmless veto), **then**
  the mirror rule — if the target cell is the wisp's cell, `lose_life`. So when the
  wisp is transiting the wall the player is pressing into, the veto is skipped and
  the same held input that is normally a free bump is priced as a life.

The player's repeat-move timer (`PLAYER_REPEAT = 6`) re-fires a held direction every
6 frames; the wisp transits at pace 9-16. A player hugging a building wall while the
wisp slides through it loses a life to a wall that, a frame earlier, was an
inert bump. `restore_draught` restores the wall attribute after the wisp leaves
(1863-1878), so the wall bit is clear **only** during transit — exactly the bug
window. INHERITED, unmodified.

*Suggested direction:* the mirror rule should not fire against a cell whose
*restored* (under-wisp) attribute has `WALL_BIT` set — test `under_draught+8`, not
just the live cell. Or give the wisp its own wall test so it never enters walls.

> **Cross-lineage implication:** both defects are structural (frame order; sprite
> attribute vs. wall bit test), and both are inherited whole from Gloaming into the
> middle of the lineage. **Shadowkeep (pass 3) almost certainly carries both** and
> should be swept before its next build. These are the single most important output
> of this pass.

---

### F3 — No pure-play, normal-pace loss capture; the shipped win is captured against a *frozen* antagonist — **BLEEDS** (winnability-gate / verification gap)

Both shipped captures reach their end states only via **pokes**, and neither is a
cold-start playthrough:

- **Win (unit-10 `dawnphrase`, the shipped final capture)** pokes the game into an
  almost-won, hunt-disabled state, then lights one lamp by input:
  - `35332` = `lit_count` → **7** (one lamp from the win)
  - `35341` = `dusk` → **4** (fifth watch, so completion = dawn)
  - `35339` = `draught_timer` → **255** — **freezes the antagonist** for the duration
  - `22540-22546` = the PIP HUD row → `PIP_LIT`; `22628…23186` = seven lamp cells →
    `LAMP_LIT` — fakes seven lamps already lit.
  Then O/A inputs light the eighth → DAWN. **The shipped win has never been driven
  against a live draught.**
- **Loss (unit-09 `longest`, `step-01-nightfalls.png`)** pokes `35292` =
  `dusk_table[0]` → **1** (draught steps every frame — turbo hunt) and
  `35300` = `dusk_lentab[3]` → 2, then leaves the player **stationary** for 520
  frames until the accelerated draught catches three times → NIGHT FALLS.

So the fail state **is** reachable and both end screens are verified to render — but
(a) the loss is proven only by a *poke-accelerated stationary death*, not a
normal-pace played loss; (b) **unit-10, the shipped game, ships with a win capture
only** — the loss capture lives one unit back (unit-09). This is the exact gap that
gated **Flock**: the loss half of the winnability gate is not demonstrated by a
clean, input-driven run of the shipped artefact.

*Suggested direction:* add a unit-10 capture that reaches NIGHT FALLS by input at
shipped pace (walk into the wisp three times, or stand at normal watch-1 pace long
enough), with no `draught_timer`/`dusk_table` poke.

---

### F4 — Early watches lean thin: decoy-and-kite neutralises the hunt — **BLEMISH→BLEEDS (watch 1-2 only)**

The lamplighter steps every `PLAYER_REPEAT = 6` frames; the draught steps every
`dusk_speed` = 16 (watch 1) down to 9 (watches 4-5) — the player is ~2.6× faster
early. Combined with the grudge redirection ("light your first lamp and the hunt
turns away from you", 1143-1155) and the withdraw-home-and-rest cycle
(`WREST = 48`, draught_step 1118-1136), a player can light one decoy lamp, then
light the remaining seven while the draught fixates on, snuffs, and slowly
round-trips to re-hunt the single oldest grievance. Watch 1 (reach 3, pace 16) has
little to threaten this. The design comments own this ("Dusk 1 is gentle on
purpose", 1911-1912) and the escalation is real — tendril reach 3→6→9→13→18 and
pace to 9 restore genuine board-control pressure by watches 4-5, where 18 DARK cells
(impassable: player cannot enter DARK, `.pmove` 746-749) plus buildings can wall off
lamps mid-completion. So this is jeopardy that *arrives late*, not absent jeopardy.
Not a BREAKS. Flag only if playtest shows the decoy-kite carries all the way to
watch 5 with no real risk (see Open questions).

---

### F5 — Same-frame snuff silently voids a just-completed set — **BLEMISH**

If the player lights the eighth lamp in `player_step` and the draught snuffs any lit
lamp in the following `draught_step` (`unlight_pip`, 1289 → `lit_count` back to 7),
the win check at 179 sees 7 and the completed set evaporates with no feedback beyond
a pip cooling. Defensible as "all eight must be lit *at the check*," but it is
illegible: the player saw eight pips warm for one frame and got nothing. Minor.

---

## Closed holes (verified in code — steelmanned and dismissed)

- **Camp-the-clock / wait-out-the-night: not constructible.** No timer exists; a
  watch advances only on lighting all eight lamps (play_step 179-204). Standing in a
  safe corner produces no progress and no win. The brief's premise is void.
- **Turret-park / stand-and-win (the Starfield failure): impossible here.** Winning
  requires physically occupying eight distinct lamp cells to light them; there is no
  stationary winning play.
- **Death-beats-victory on a *survivable* catch: closed.** A non-fatal catch
  respawns and leaves `STATE_PLAY`, so control reaches the win check the same frame
  and the eighth-lamp completion still registers (only the last-life tie denies it —
  see Propagation 1).
- **Lives-across-watches ledger lie: already fixed in this codebase.** `draw_lives`
  reads carried `(lives)`, not the `LIVES` constant (1663-1678, with the fix noted in
  the source comment). Lives correctly persist across watches (init_game) and reset
  only per run (init_run, 212-217).
- **Tendril permanently walling the square off: closed.** The ring releases its
  oldest cell once `tendril_len` reaches `tendril_max` (`tendril_push`, 1305-1389),
  and released DARK heals to cobble/glow (`pooled_at`, 1480-1518). The night cannot
  hold ground beyond its reach.
- **Player stepping onto the wisp / walls / DARK on open ground:** correctly vetoed
  or priced (`.pmove`, 737-761). Only the phase-through-wall case (Propagation 2)
  leaks.
- **Frame-one catch:** `GATHER = 120` delays the draught's first step; no first-frame
  contact.

---

## Open questions (playtest-only)

1. **Does decoy-and-kite carry to watch 5?** At pace 9 / reach 18, can a practised
   player still light all eight simultaneously with zero risk, or does the tendril's
   board control force real jeopardy? Determines whether F4 is a BLEMISH or a BREAKS.
2. **Transient soft-lock by enclosure.** Can the tendril (plus buildings/edges) fully
   box the lamplighter into a cell with all four orthogonal neighbours DARK/wall?
   The player then cannot move, cannot win, and cannot die (the wisp never steps onto
   the player, `.contact` 1227-1240). The ring normally dissolves the box as the wisp
   moves, **but if the wisp snuffs and withdraws to rest (`WREST`), the box could
   persist for the rest window.** Low probability; needs a scripted stress run to
   confirm reachability. If real: BLEEDS/BREAKS.
3. **Propagation-1 hit rate in live play.** Confirm the last-life dawn-tie is
   actually reachable against the lamp-hunting AI (not just theoretically), and
   whether players can perceive it as unfair when it lands.

---

## Gate recommendations (before the next game is built)

**Fix before building the next game (Shadowkeep):**

1. **Propagation 1 (death-beats-victory) and Propagation 2 (wall-hug lethal)** — both
   BLEEDS, both inherited whole. Fix them **in the lineage**, not just here: sweep
   Shadowkeep (pass 3) for the identical frame-order and sprite-attribute-vs-wall-bit
   defects and fix all three before Shadowkeep ships further. This is the propagation
   dividend of the pass.

2. **A loss capture is a gate item — yes, exactly as it was for Flock.** The shipped
   unit-10 has a win capture only, and that win is captured against a *poke-frozen*
   antagonist (`draught_timer = 255`). Require, for unit-10: (a) an input-driven
   NIGHT FALLS capture at shipped pace with no pace/lives pokes, and (b) at minimum
   one win capture that lights the eighth lamp with the draught **live**. Until both
   exist, the winnability gate's loss half is **not** cleanly proven for the shipped
   artefact.

**Verdict on the bar as shipped:** *The Long Night* **clears the jeopardy gate** — a
reachable fail state (NIGHT FALLS on three deaths) is constitutive and escalates
genuinely through the tendril across watches. It **does not yet cleanly clear the
winnability gate**: both end states are only demonstrated via poke-assisted setups,
the loss is a poke-accelerated stationary death living in unit-09, and the shipped
win has never been driven against a live antagonist. Plus it carries **two inherited
BLEEDS-severity engine bugs** that unfairly convert a won frame into a loss and a
safe wall-hug into a death. None is a BREAKS, but the winnability-capture gap and the
two propagation bugs should be closed before the lineage advances.
