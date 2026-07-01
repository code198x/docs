# Gloaming — prototype discovery log (validate-and-repair pass)

The endpoint-first discovery log (✦ convention in
[decisions/endpoint-first-authoring.md](../../../../decisions/endpoint-first-authoring.md)),
kept for the 2026-07 validate-and-repair pass. The shipped game (unit 21, `step-01.asm`)
is the starting point; the reshape contract is brief §10.

## 2026-07-01 — baseline: gate re-run + first human playtest

**Gate re-run (machine):** both checked-in scripts (`step-01-won`, `step-01-sting`) run
green on the current Emu198x release build (rebuilt from 2026-07-01 HEAD; screenshots
byte-identical to the 9 Jun binary — the ULA timing fix was Pentagon-class only). Win
reaches THE NIGHT IS HELD + fanfare; loss reaches NIGHT FALLS + sting.

**Human playtest (Steve), shipped build — findings:**

| # | Sheet question | Finding | Disposition |
|---|---|---|---|
| 1 | Held-key movement | **WAY TOO FAST** — one cell/frame at 50 Hz confirmed as wall-magnet | Repair: repeat-gate (step on press, then every N frames held); tune N by feel |
| 2 | The draught | "Just bouncing — not very *menacing*" | Reshape (brief §10): seek-the-nearest-light replaces the bounce |
| 3 | Three phrases | Didn't register as distinct musical beats | Watch: re-ask after the speed fix slows the game down; may need nothing |
| 4 | `LOCK 25` | Player never noticed it | **Pass** — an input lock is working precisely when it's invisible |
| 5 | Unassisted win | **Won first time** | Reachability confirmed ✓ — but zero challenge; confirms the missing curve (brief §10 "the night deepens") |
| 6 | Win-screen walls | Magenta flood — **bug**, not a glow | Repair: win recolour should be the warm-yellow vocabulary of §6 |

**Reading:** findings 1+5 compound — the player is 8× faster than the draught *and* the
draught doesn't hunt, so the shipped game cannot threaten anyone. The reshape isn't
gold-plating; the baseline proves the game has no antagonist in practice.

**Order of work from here:** prototype workspace forks unit-21's `step-01.asm`
(never edit shipped units in place — "never regress the launch"). Commit-sized
teachable increments; win + loss scripts re-run after each. Repairs first
(speed gate, magenta), then the reshape (seek rule → dusk table → best-night pips),
then re-playtest.
