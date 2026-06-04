# Starfield — DoD-Finishing Pass (plan)

**Status:** Not started. This is the deferred Definition-of-Done pass named in
[`assembly-skeleton.md`](../../assembly-skeleton.md) § *Starfield — committed shape*.
Completing it closes the second half of the C64 finishable bar (Primer ✅ +
Starfield) per the [Oct-2026 launch spec](../../../../decisions/october-2026-launch-spec.md).

Cross-repo: edits land in **website** (MDX, images, `units.yaml`) and
**code-samples** (per-unit `.asm` dirs). Commit per repo, like the primer.

## What we found (sizing, 2026-06-04)

Two findings drive this pass — see the session analysis for evidence:

1. **The order has one real break, and the reorder fixes it.** The shooter
   build-up (ship → move → shoot → … → starfield → title) flows; each unit's
   "What's Next" chains to the next. The exception: **Screen Edges** sits dead
   last (u16, *after* Title Screen) — a finale followed by a leftover technical
   unit, dangling into deferred Phase-2 content. Moving it to **3** restores the
   motivation (move the ship → it can only reach half the screen → clamp it),
   and makes Title Screen the true finale. The reorder is validated by flow.

2. **Starfield does not come off the back of the Primer** (the bigger gap).
   It was authored before the Primer existed: **0 of 16 units reference it**, the
   opening re-teaches `LDA`/`STA` + the BASIC stub from scratch, and several
   units present Primer material as "new." The techniques the Primer *promised*
   (the whole joystick; the computed/indirect pointer) are delivered but never
   cashed in as those payoffs. The author already does callbacks well *within*
   Starfield (u3 "you already know `$DC00`", u5 "just like `bullet_y`"), so the
   fix is to aim some of them at the Primer — same move, same voice.

**These overlap.** The heaviest continuity work (u1–u3) is the same front of the
game the reorder seams touch. So this is **one pass on the opening + the
mechanical renumber + a handful of targeted touches deeper in** — not a
mechanical reorder followed by separate continuity work.

## Target order + permutation map

The single source of truth for all renumbering. **Not a blind `+1`** — units 1–2
fixed, Screen Edges jumps 16→3, everything between shifts +1.

| New | Title | Old |
|----:|-------|----:|
| 1 | Ship on Screen | 1 |
| 2 | Joystick Movement | 2 |
| **3** | **Screen Edges** | **16** |
| 4 | Fire Button Shoots | 3 |
| 5 | Laser Sound | 4 |
| 6 | Enemy Appears | 5 |
| 7 | Direct Hit | 6 |
| 8 | Explosion | 7 |
| 9 | Scoring Points | 8 |
| 10 | Enemy Waves | 9 |
| 11 | Player Death | 10 |
| 12 | Game Over | 11 |
| 13 | Three Lives | 12 |
| 14 | Life Lost Flash | 13 |
| 15 | Starfield | 14 |
| 16 | Title Screen | 15 |

Forward map (old→new) for remapping references: `1→1, 2→2, 3→4, 4→5, 5→6, 6→7,
7→8, 8→9, 9→10, 10→11, 11→12, 12→13, 13→14, 14→15, 15→16, 16→3`.

## Job A — Mechanical renumber (map-driven, verifiable)

Everything keyed by `unit-NN`. Surface: **16 MDX** (website) + **16 code-sample
dirs** (code-samples) + **16 image dirs** (website) + 16 frontmatter `unit:` +
**53 `CodeFromFile src=` paths** + `units.yaml` order + 5 hard links + numeric
"Unit N" prose refs.

**Collision-safe ordering** (a 3→4→5… shift clobbers in place): rename every
old→new through a temp namespace first (`unit-NN` → `tmp-MM`), then strip the
prefix (`tmp-MM` → `unit-MM`). Use `git mv` to preserve history. Apply to all
three trees (MDX, code-samples dirs, image dirs).

Per file, apply the map to: (a) filename, (b) frontmatter `unit:`, (c) its own
`CodeFromFile src=…/unit-NN/…` segments, (d) image `…/unit-NN/screenshot.png`
segments, (e) numeric `Unit N` prose references (by number — relational
"next/previous" is Job B). Then fix `units.yaml` order to match.

**Verify Job A in isolation:** `npm run build` (catches broken `src=` /
frontmatter), link-check (broken `/unit-NN` links), `git status` (16+16+16 clean
renames). A green build here means the structure is sound before any prose
judgment.

## Job B — Continuity + seam rewrites (authoring)

### B1. The reorder seams (narrative, not numeric)

Inserting Screen Edges between Joystick and Fire Button breaks three transitions:

- **u2 Joystick → "What's Next"**: currently leads to bullets (Fire Button). Must
  hand off to **Screen Edges** (the ship can fly off the edge → keep it on screen).
- **u3 Screen Edges** (was u16): intro assumes it follows the finished game; "What's
  Next" dangles into Phase 2. Rewrite so it **follows Joystick** (ship reaches
  only half the screen) and **leads into Fire Button**.
- **u4 Fire Button** (was u3): intro assumes it follows Joystick. Now it **follows
  Screen Edges** — adjust the "the ship moves, now make it shoot" framing.

### B2. Primer continuity (stop re-teaching; cash in the payoffs)

From the re-teaching audit:

| Unit (new #) | Edit |
|---|---|
| **1 Ship on Screen** | Open on the *new* thing — the VIC-II + hardware sprites — framed as "now use what the Primer gave you." Drop the from-scratch `LDA`/`STA` re-teach and the full BASIC-stub re-explanation (callback: "the same `10 SYS 2061` stub from the Primer"). Fix "your first machine code program" → first *game*. |
| **2 Joystick Movement** | Replace "three new concepts" — only the **game loop** is new; branches (Primer u7) and masking (Primer u8/13) are callbacks. Frame `$DC00` as the payoff: *"in the Primer you read one bit — the fire button; now the whole stick."* |
| **4 Fire Button** | `SBC`/`SEC` is **not** new (Primer u12) — make it a callback. Trim the zero-page re-introduction to a reminder. |
| **9 Scoring** | Trim the "Screen RAM `$0400`, 40×25 grid" re-teach (Primer u5) to a callback. |
| **12 Game Over** | Trim the screen-codes / PETSCII re-explanation (near-verbatim Primer u5) to a callback. |
| **15 Starfield** | Cash in the second payoff: name **"A Finger on the Boxes"** — the Primer's deferred movable pointer — as `STA ($fb),Y` arrives. |
| **3 Screen Edges** | Verify the "new instruction for toggling a bit" claim vs Primer u13 (ora/and/eor); make it a callback if so. |

Plus: a few **deliberate Primer references** at the opening so the seam between
modules actually exists (it does not today).

## Other DoD items (from the skeleton)

- **Parallax — KEEP and EXPAND (decided 2026-06-04, reverses the cut; skeleton
  updated).** u15 (old u14) already has working two-speed parallax (8 stars, split
  at index 4 via `CPX #$04`, then `frame_count AND #$01`; white close / dark-grey
  far). Expand to **three layers** — promote the existing "Three Depth Layers"
  try-this (`AND #$03`) to the main lesson: full / half / quarter frame-rates,
  white → grey → dark-grey. **Stretch to four** ("if we're brave") only with a
  bump in star count (8 → ~16; 2/layer is too sparse), a fourth grey, and accepting
  geometric speeds (1, ½, ¼, ⅛ — the slowest crawls). Touches u15 prose + the
  star code in u15/u16 `.asm`. Aim 3; decide 4 at authoring time.
- **Frame-pacing — resolved (2026-06-04), not a gap.** The `$D012` raster-wait
  sync is present in the main loop of **all 15 units (u2–u16)** and is properly
  taught in **u2** (game-loop diagram + register walkthrough; the "~50/sec" claim
  is backed by the code). Unlike Gloaming's dedicated "Heartbeat" unit, Starfield
  folds frame-pacing into the game-loop unit — a fine choice. **No new unit.**
  Only constraint: preserve u2's raster-sync explanation through its continuity
  rewrite (the game loop *is* u2's one genuinely-new idea).
- **Screenshots — the dominant task, NOT audit-only (2026-06-04).** All 16
  on-disk PNGs are **6-byte placeholders** — zero real screenshots exist. The
  convention is also inconsistent: only u2/u3 wire images (a before/after
  comparison component); u1 + u4–u16 reference none. To reach the primer's bar,
  every unit needs real captures + consistent wiring, and many are
  **interactive/timed** (ship moved by joystick, bullet mid-flight, enemy on
  screen, explosion) — exactly what the **Emu198x C64 pipeline + the joystick
  port-2 fix** now enable and VICE can't. This is the **largest sub-task of the
  pass.** **Decision needed:** visual convention — primer-style single "what
  you'll see" hero, before/after comparisons (better for an incremental game
  build), or both.

## Verification gates

- `npm run build` green (after Job A, and again after Job B).
- 0 broken internal links.
- Vale clean (0 errors / 0 warnings; advisory suggestions OK).
- **Full read-through in the new order** — the real test for Job B: does it read
  as the second module of one course, start to finish, off the back of the Primer?

## Completion

When all gates pass: flip Starfield to `status: complete` in the module
catalogue (`modules/commodore-64/assembly.yaml`) and `index.mdx`. That closes the
C64 finishable bar.

## Working checklist

- [ ] Job A — temp-namespace renames (MDX + code-samples + images), per-file map
      application (filename, `unit:`, `src=`, image paths, numeric refs), `units.yaml`
- [ ] Job A verify — build green, links clean, renames history-preserving
- [ ] B1 — rewrite the three reorder seams (u2 → u3 → u4 transitions)
- [ ] B2 — opening continuity rewrite (u1, u2, u4) + payoff callbacks (u2, u15) +
      light trims (u9, u12, u3)
- [ ] Parallax — KEEP + expand to 3 layers (promote the try-this); stretch to 4 if star count bumped (~16) + 4th grey; code+prose (u15 + u15/u16 `.asm`)
- [x] Frame-pacing — resolved: present in code (u2–u16) + explained in u2; no new unit (preserve u2's explanation in B2)
- [ ] Screenshots (**DOMINANT**) — **DECISION** (convention) → capture all 16 real (Emu198x for interactive shots) → wire consistently
- [ ] Final gates — build, links, Vale, full read-through in new order
- [ ] Mark Starfield `complete` (catalogue + index)
- [ ] Commit per repo (website, code-samples)
