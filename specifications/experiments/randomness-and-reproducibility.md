# Randomness and reproducibility

**Status:** Source-audited progression with local lesson/pattern edits. Bright Spark 06 has a repeated-choice prediction exercise; Flock 15's repeatability claims and the LFSR pattern's mapping/cost claims are clarified. No generator, game sequence, replay recorder or native fixture has been added. Scope: Spectrum, C64, NES and Amiga.

Build on [diagnosis](testing-and-diagnosis.md), [lifecycle](state-lifecycle-and-recovery.md), [timing](timing-and-interrupts.md), [data](data-memory-tools.md) and [feedback](timing-and-player-feedback.md). Probability belongs with the existing Maths for Games Dice Roller sequence; game-specific choices stay in their games. No new standalone randomness module is required.

## Existing material and verified details

| Inspected source | Existing coverage | Gap / action |
|---|---|---|
| Spectrum Bright Spark 06 and Sonar 08 | `INT (RND*n)+1`, repeated results allowed, fixed choices for debugging; Sonar seeds once and continues the sequence on retry | Local Bright Spark exercise contrasts unrestricted and no-immediate-repeat rules. Later fixed-seed trials need explicit reset/call timing, not repeated reseeding. |
| Maths for Games 03, Dice Roller “Compare shares” | Counts versus proportions, rounded display versus exact tally, short samples do not prove fairness | Reuse the tally mechanism for a mapping comparison; do not infer uniformity from a pleasing histogram. |
| C64 Starfield 17 `steps/step-04.asm`, `advance_rng` and `spawn_enemy` | Left-shift 8-bit LFSR, feedback `$1D`, non-zero raster-derived start; spawn maps byte b to `b + floor(b/8) + 24`, stored with a high bit | Source arithmetic and host enumeration show a 255-state cycle and 255 distinct positions from 25 through 310. It does not choose every integer in the advertised 24–310 span. Follow-on lesson must distinguish coverage of the field from uniform choice of every coordinate. |
| Amiga Flock 15 `flock.asm`, `rnd`/`newsheep` | 16-bit xorshift (7,9,8), XOR with `framecnt` on each call, zero replaced by `$ACE1`, low three bits select sheep type | Fixed seed alone cannot repeat a run with different frame-counter values. Local text corrects “same moments” and inevitable-difference claims; the exact mixed distribution is not established. “One in eight” is a design target, not a proof from the mask. |
| NES Dash 10/14 | Authored coin positions and collection state; no random source identified in the inspected Dash samples | Preserve those deterministic levels. A later bounded experiment can select among already validated pickup layouts; it is proposed, not existing Dash behaviour. Thunder Run is a later home only when its agreed mechanic needs it. |
| Cross-platform LFSR pattern | Right-shift 8-bit `$B4` implementation on 6502/Z80/68000, one-byte state, seed examples | Enumerated all 255 non-zero states. Local correction: low-nibble zero occurs 15 times; 1–15 each 16. Removed unsupported universal cycle estimate and “avoid when needing zero” advice. |

Verification in this pass was source reading and exhaustive host enumeration of the two specified 8-bit transitions and Starfield mapping, not native CPU execution or statistical certification. The exact byte mask and shift direction matter; `$1D` left-shift and `$B4` right-shift are not interchangeable code snippets. Source claims come from the actual routines; enumeration establishes these small mathematical state spaces without guessing a polynomial convention.

## Progression through the games

| Stage / placement | Prerequisites and smallest experiment | Observable outcome |
|---|---|---|
| 1. Choose an item: Bright Spark 06; Sonar 08 | Fractions, integer range and stored state. Trace a value through multiplication, INT and offset; inspect legal endpoints. | Every chosen panel/coordinate is valid; repeats are allowed. Random does not mean “different from last time”. |
| 2. Decide what variety means: Bright Spark 06; Dice Roller 03 | Lists and counting. **Local:** trace six candidate panel choices with/without rejecting immediate repeats; describe the changed challenge. | Separate unpredictability, marginal frequencies, legal placement and enjoyment. A no-repeat rule creates dependence on the previous choice. |
| 3. Seeds and repeatability: Sonar companion, Starfield 17 | Initialisation and a known generator call. Reset a fixed seed once per test run; retain the same state/input/update schedule and count calls. | Reproduce a chosen failure and show that changing one unrelated call can shift the later sequence. Never reseed every draw as a generic improvement. |
| 4. Range mappings and bias: Dice Roller → Starfield/LFSR | Byte limits, remainder/masks and sample size. Enumerate a small source domain before sampling; compare mask/remainder/rejection or an authored lookup. | Distinguish correct range from equal frequencies, and equal frequencies from independence. Explain the extra work/storage and call-count changes. |
| 5. Constraints and fairness: Tail Chase snack placement, Sonar, proposed Dash layout experiment | Occupied/legal cells, boundaries and intended difficulty. Compare unrestricted proposals with a list of legal choices; explicitly handle no choices. | Never spawn in an impossible location; explain whether excluding recent choices, weighting or a bag serves the mechanic. None is universally fair. |
| 6. Divergence diagnosis: Flock 15; Starfield 17 | State traces, reproducible input and clock domains. Log call ordinal, purpose, state before/after, mixed input and selected result. Compare two runs at the first mismatch. | Explain whether a difference came from reset, input timing, update order, seed mixing or mapping; logging must not consume new random values. |
| 7. Deterministic scenarios: existing Meteor Storm verification; later Dash/Flock companions | Known event schedules and targeted assertions. Supply fixed spawn/layout data for one boundary case, then add a small set of seeds as supplemental coverage. | A deterministic case exercises a precise failure regardless of chance. A lucky random run is not a substitute for empty/full/boundary tests. |
| 8. Recording/replay, only when useful | Stable update/input contract, initialisation and versioned data. First record a bounded sequence of logical inputs at named guest updates for one game. | Reproduce a rare failure and detect first state divergence; do not claim replay portability across changed builds or machines. No general recorder is required for earlier lessons. |

Tail Chase's placement is a follow-on opportunity from its snack/occupancy lessons, not an assertion that its current selection algorithm has been audited here. Link Foundations representations and decisions for support; retain local explanations for independent entry routes. Vault random-number history gives context, not proof of the game generator's quality.

## Four controlled experiments

### A. Fixed seed, fixed failure — Starfield 17

Proposed isolated companion after the current lifecycle reset fixture. In the experiment only, replace the raster-derived start with non-zero `$01`; reset all game state and use a fixed logical input schedule. Introduce a labelled missing-high-bit fault in the position consumer, keeping the generator unchanged. Log the first spawn whose expected full position exceeds 255. Predict why its displayed/compared position disagrees before repairing it. Repeat from the same setup after repair, then check both sides of the boundary.

The original source already preserves the high bit. Do not ship a fault in its working checkpoint or claim the fixture exists. The expected mapped positions can be checked independently from the routine; that model does not establish VIC timing or collision implementation correctness.

### B. Compare distributions — Dice Roller and the LFSR pattern

For an ideal uniform byte 0–255, remainder 6 gives outcomes 0–3 43 source values each and 4–5 42 each. Rejecting 252–255 first gives 42 per outcome, with variable draws. The existing non-zero LFSR is a different source: subtract one to make 0–254, accept 0–251 and then take remainder 6 if demonstrating equal counts over the accepted domain. State the source assumptions before using either recipe.

First enumerate every source value, then compare several short samples with the existing tally idea. Expected counts over a complete finite cycle are not a claim that successive draws are independent. Rejection reduces mapping bias under the stated model; it does not remove generator correlations. Bound real-time work or prepare ahead of time when a retry loop could exceed the game's budget.

### C. Change call order — Starfield or a small logical fixture

From the same seed, label consecutive values “spawn”, “colour”, “spawn”. In a second run remove the colour draw, or put it before the first spawn. Predict which raw sequence values become positions; compare logs. A diagnostic that calls random again has changed the experiment.

Only when cosmetic additions repeatedly disturb important tests consider separate gameplay/cosmetic state streams. That is a design boundary, not a proof of statistical independence: nearby seeds of a tiny LFSR may merely be phase shifts of the same cycle. Each stream has reset/storage costs and its own call-order contract.

### D. Why matching seeds diverge — Flock 15

The existing routine mixes a 16-bit frame counter into state before its word-width shifts, then substitutes `$ACE1` for a zero result. Keep seed fixed and vary only one recorded `framecnt` input in a host arithmetic trace; predict divergence at that call. Then repeat with both seed and the counter-input sequence fixed. For a later native fixture, reset the rest of the game and reproduce the same logical input schedule too.

Removing the stir in an isolated copy can produce a repeatable colour sequence with the same call order. It does not fix spawn times unless gameplay timing matches. Log masked colour, raw state and call time separately. Do not promise an exact one-eighth probability for the mixed routine without analysing its actual input/state distribution.

## Numeric limits, cost and game design

- **Spectrum BASIC:** retain the already cited Sinclair manual's RND/range model. A fixed-seed companion should verify `RANDOMIZE` syntax/range against chapter 11 and the selected ROM before publication; this plan adds no unverified seed command. Interpreted retries and string/list updates have costs; do not make an unbounded placement loop the beginner default.
- **C64:** the inspected generator state is an 8-bit non-zero byte. The mapped position needs nine bits; the conditional feedback path costs differently. Count the actual branch, call and mapping work rather than saying every random value has one universal cycle cost.
- **NES:** a later implementation can use an explicitly verified byte generator, but must not borrow C64-specific timing, ROM or device assumptions. Keep authored Dash layouts as a control and choose among a small validated set before proposing arbitrary procedural levels.
- **Amiga:** word operations in the inspected Flock routine truncate to 16 bits. The shifts and per-call frame-counter mixing must both be reproduced by any host model. Do not infer the mixed stream's period from the unmixed xorshift's name.

An equal chance of all cells may include unreachable or unfair placements. A valid placement may still be too close to the player to react. A no-repeat rule reduces one kind of streak while making the next choice more predictable. A shuffled bag limits long absences but adds memory and changes dependence. A weighted table can deliberately favour easier options; label that design instead of calling it a broken fair die.

For independent ideal four-way draws, an adjacent repeat has probability one quarter. That model explains why repeats are ordinary; it is not a proof that a particular finite PRNG produces independent draws. Compare playable outcomes as well as frequency tables. Game PRNGs described here are predictable and unsuitable for security-sensitive randomness.

## Reproduction and replay boundaries

A seed is only one field in a reproduction record. Include program/assets identity, machine/region and relevant emulator configuration, initial game state, generator algorithm/state, input sampling convention, update order and random-call order. External timing or entropy must be fixed or recorded. A wall-clock key recording does not automatically reproduce guest-update input.

Begin with saved test scenarios and a few bounded input steps. When a rare gameplay failure justifies a recorder, store normalised input by simulation update plus a versioned initial-state description; check state at selected boundaries. Recording physical input separately tests the reader, not the same contract. If the implementation changes random-call order, an old seed/input replay may diverge legitimately: retain the old build or migrate the scenario explicitly. Recording outcomes can preserve an authored scenario, but that tests a different boundary from replaying the generator.

Cap record length/storage, mark truncation, and give reset/stop instructions. Use the existing supported sample scripting and guest state reads from the profiling audit; no general replay tool, cross-machine synchronisation or debugger facility is assumed. Keep replay out of the introductory choice lesson.

## Next implementation and remaining gaps

1. **Local edits complete:** Bright Spark 06 repeated-choice prediction; Flock 15 reproducibility qualifications; LFSR range/bias/cost explanations. Game sources unchanged. Native listening/game execution was not part of this pass.
2. **Next randomness companion:** extend Dice Roller's existing tally experiment with one finite-domain mapping comparison and predictions. The host enumeration here supports expected counts; a learner-facing runnable companion remains to implement. Preserve the existing Bright Spark native-work priority.
3. Attach Starfield fixed-seed/high-bit and call-order fixtures to its later diagnosis work. Correct its broad spawn-range prose with the enumerated mapping, and review Flock's remaining exact-frequency wording before publishing a distribution lesson.
4. NES legal-layout selection and bounded replay follow an agreed project need. The input, reset and timing contracts must be taught first. No procedural generation module or replay engine is commissioned by this plan.


## Spawn mapping and sheep frequency checks

C03d is locally authored, ready for review. Inspected code:
`code-samples/commodore-64/assembly/starfield/unit-17/steps/step-04.asm`,
`spawn_enemy`/`advance_rng`, and
`code-samples/commodore-amiga/assembly/flock/unit-15/flock.asm`, `newsheep`/`rnd`.
Lesson prose, narrow shared-reference qualifications and Flock’s displayed odds comments change. Removing comments line by line confirms identical instruction/data text in `flock.asm` and its `01-newsheep-and-rnd.asm` excerpt.

Exhaustive Python arithmetic checks on 22 September 2026:

- Starfield left-shifting eight-bit Galois LFSR, feedback $1D: starting at 1
  returns to 1 after visiting all 255 non-zero bytes. Mapping each through
  `24 + b + (b >> 3)` produces 255 distinct positions, minimum 25, maximum 310.
  The 32 absent positions within 24–310 are 24 and `32 + 9*k` for k=0…30.
  The source comment's 24–310 range describes arbitrary bytes including zero;
  it does not describe the generator's reachable set. Drift and collision
  coverage must be considered separately from spawn positions.
- Flock word-truncated xorshift (7,9,8), with frame mixing removed: starting
  at $ACE1 visits all 65,535 non-zero words and returns to $ACE1. Zero low bits
  occur 16,383 times for mask 3; 8,191 for mask 7; 4,095 for mask 15. These are
  counts over the unmixed full cycle, not independent probabilities per call.
- With the frame XOR and zero fallback included, the first 16 low-three-bit
  results for frame values 0…15 are `[7,4,7,3,6,7,4,2,4,6,7,1,7,3,6,7]`.
  Keeping every frame value zero instead gives
  `[7,5,4,2,1,6,5,1,3,4,6,2,1,4,6,0]`. These artificial call schedules illustrate
  dependence on mixed state; neither is a gameplay-frequency measurement.

Reproduce the full-cycle checks without an emulator:

```python
def lfsr(x):
    return ((x << 1) & 255) ^ (0x1d if x & 128 else 0)

def xorshift(x):
    x ^= (x << 7) & 65535
    x ^= x >> 9
    x ^= (x << 8) & 65535
    return x

for step, seed, length in [(lfsr, 1, 255), (xorshift, 0xace1, 65535)]:
    seen = set()
    x = seed
    while x not in seen:
        seen.add(x)
        x = step(x)
    assert x == seed and len(seen) == length and 0 not in seen
    if length == 255:
        positions = {24 + b + (b >> 3) for b in seen}
        assert (len(positions), min(positions), max(positions)) == (255, 25, 310)
    else:
        assert [sum((b & mask) == 0 for b in seen) for mask in (3, 7, 15)] == [16383, 8191, 4095]
```

This is source-derived integer modelling, not assembled/native execution,
statistical evidence from player sessions or proof of enjoyable fairness.
The existing LFSR pattern bias/reproducibility explanation is preserved. Narrow
Random Numbers Vault qualifications remove unconditional shuffle uniformity,
seed-only reproducibility and an unsupported sufficient-period assurance; the
rest of that page is not claimed fully audited. Learner prediction/play trials
remain pending; the game algorithms and captures are unchanged.

## Starfield fixed-seed position investigation: C07b

Unit 17 now links `code-samples/commodore-64/assembly/starfield/unit-17/position/`.
The source-hash-checked companion uses the original step-04 spawn routine, with
seed 1, enemy index 0, starting Y=80, initial `$d010=$ab` and twelve consecutive
spawn calls. Native scripts use the same BASIC RUN input timing and no gameplay
input. Initialisation, call order and the absence of intervening game updates
are explicit; this is not presented as seed-only replay.

The single fault omits `set_enemy_hibit` at the spawn handoff. Calculated X and
random bytes remain correct. Native PAL verification on 22 September 2026 found
the first divergent record at call 11: byte 232 maps to X=285, but the faulty
sprite registers select 29. Call 12 maps byte 205 to X=254, checking that the
working helper clears the high bit after setting it. All other sprite bits
survive. An independent integer calculation checks every mapped position, and
a second cold baseline reproduces all twelve records. Repair and baseline PRGs
are byte-identical. Exact identities and records live in `results.json` beside
the reproduction instructions.

The lesson provides a prediction table, two hints, folded repair and an explanation
of why changing the seed would move or hide the fault rather than repair it.
The diagnostic screen shows registers in hexadecimal, not a claimed capture of
each displayed sprite. Hardware addresses were checked against Commodore's
*Commodore 64 Programmer's Reference Guide*, sprite-position register discussion
(pp. 137–138) and Appendix G. No full playthrough, original-hardware validation,
collision or timing-equivalence claim is made. C07c below separately changes cosmetic random-call order; no new generator or
replay engine is introduced.

## Starfield consumer-order comparison: C07c

The `unit-17/call-order/` companion generates both versions from C07b's correct
baseline, retaining its source hash check, seed, fixed enemy slot and position
records. It adds one decorative border draw in both versions and moves it from
before the first spawn to after it. The ordinary game does not gain a new random
consumer. Logging records actual consumer IDs and bytes without advancing RNG.
The same RUN input schedule drives both variants and their cold repeats.

Native PAL checks on 22 September 2026 verify thirteen draws and twelve mapped
positions/register handoffs per run. Both versions produce raw bytes 2,4,8,16…;
only the first two consumers exchange places. Enemy 1 is X=28 when decoration
goes first, versus X=26 when it follows. Enemies 2–12 agree, both versions finish
at seed 135, high-bit set/clear works and unrelated sprite bits remain intact.
Both second launches reproduce their logs. Exact identities and observations
are in `call-order/results.json`; the first-three-spawn screen was inspected.

The lesson asks for predictions before a consumer table, with two graduated hints.
It distinguishes this changed choice from C07b's incorrect display handoff and
C07a's stale session state. It explicitly limits later agreement to the fixture:
a different earlier collision in a real game could change state and subsequent
calls even if generator state later matches. Restoring order, accepting a new
baseline and considering separate cosmetic state are choices with different
costs; only the first two orderings are implemented here. No new generator,
replay engine, original-hardware or timing-equivalence claim is made.
