# Aiming: finite movement and rounding boundaries

The selected aiming-model boundaries agree with the published lessons. A point
can touch a target between recorded positions, but extending its movement into
an infinite line can invent contact beyond this tick. Signed rounding and
fractional position also follow the stated contracts. No lesson or model
correction is proposed from these results.

We found one documentation discrepancy: the sample README still calls the
approved, published sequence an unpublished draft.
[Samples #94](https://github.com/code198x/code-samples/issues/94) owns the bounded
status correction. It changes no arithmetic, controls or curriculum prose.
The [plan](../../plans/2026-10-16-aiming-boundaries.md) records this investigation
under [umbrella #114](https://github.com/stevehill1981/198x/issues/114).
Approved [docs #91](https://github.com/code198x/docs/pull/91) merged first at
`6131fce9dfe227f08fa47bc868a642663e5881c4`.

## Scope and source ownership

We read all six authored aiming units, the maths specification, maintained
model, controls, standalone teaching copy and original five model tests.
[Identities](identities.json) retain the website revision
`405c0594d30af56ecdfdc1ee4b6c119dead20ab7`, samples baseline
`163e74e18e9536fb555ef7319fa08bbc1836542b` and source hashes.
All six unit hashes still match the earlier
[objective/prerequisite map](../2026-10-probability-pilot/OBJECTIVES.md).
That map remains current for these units; we do not duplicate it.

The public units teach coordinates/displacement, distance/direction ratios,
signed components, radians, inverse aiming and fixed-point movement. Their local
explanations support independent entry from probability. Within the sequence,
later examples use the earlier geometric vocabulary. This is an editorial
observation, not evidence that a beginner understands those explanations.

MDX owns the public teaching prose. `AimingExperiment.astro` selects the focused
experiment; the website's experiment route serves maintained samples.
`model.mjs` owns geometry, signed rounding and simulation. `lessons.mjs` owns
controls, drawing and presentation. Standalone sample prose is not another set
of public curriculum units. Earlier
[release/browser evidence](../../specifications/experiments/aiming.md) retains
its original scope; this run adds no browser, device, audio or timing claim.

## Expected and observed boundaries

We wrote the [expected fixtures](EXPECTED.md) before running the model. The
verifier imports the actual maintained module; it does not replace the
production distance function with a test implementation.

[Fresh results](model.json), using Node 24.22.0, cover:

- **Ten finite-segment fixtures:** interior tangency, just inside/outside,
  endpoints, travel reversal, vertical travel and zero movement. The diagnostic
  movement from (0,0) to (3,0), with target centre (1.5,5), touches at distance 5
  even though both endpoints are about 5.22015 away. With centre (9,0), its
  nearest distance is 6, so it misses. The contact comparison is inclusive;
  the verifier's numerical comparison tolerance does not change that rule.
- **Nine signed rounding cases:** half ties on both sides of zero and neighbours
  of −0.5. The custom rule rounds −0.5 to −1; JavaScript Math.round gives negative
  zero. Keeping the encoded fractional position cannot undo earlier velocity
  quantisation.
- **Nine direction cases:** all axes/quadrants and null at the origin. This
  checks the exported direction function; it does not exercise each control.
- **10,800 velocity combinations:** all 3,600 tenths-of-a-degree values on the
  declared input grid at scales 4, 16 and 256. Components are integral, within
  half a stored unit of the scaled reference, and within signed 16-bit range.
  The largest absolute stored component is 768. This grid is not every possible
  JavaScript value or every angle that control code can assign.
- **Eighteen selected shots:** the six authored target directions at three
  scales. Both axes retain tick × stored velocity at every recorded position;
  the largest absolute stored position is 61,440, within signed 32-bit range.
  All reference shots and all scale-256 shots hit. These repeat selected
  accepted representation cases with explicit two-axis/whole-trace checks;
  they do not prove every aiming angle hits or that precision improves every shot.

The [existing five model tests](existing-model-tests.txt) also pass. The new
geometry fixtures distinguish policies not distinguished by the old two
segment-distance examples. They are diagnostic fixtures, not additional targets
exposed by the public interface. No native target or overflow emulation ran.

## Controls and unsuccessful attempt

Two deliberately wrong geometry policies are rejected with nonzero exits:
[endpoint-only](wrong-endpoints.json) misses the interior tangent; an
[infinite-line policy](wrong-line.json) invents contact beyond the segment.
[Actual error output](negative-controls.json) preserves both failures.

The [initial verification attempt](initial-signed-zero-check.json) failed with
`Fractional position lost` because strict equality distinguished `0` from `-0`
at tick zero. Those values represent the same numeric position. We corrected
that assertion to numerical equality and retained the failed attempt separately.
This was a verifier error, not a lost-fraction defect in the model.

## Learner work and remaining limits

The [learner sheet](LEARNER-TASKS.md) has three independent prediction/debugging
tasks; the [assessor notes](ASSESSOR.md) separate answers and observation guidance.
They distinguish recorded endpoints from movement, a finite segment from a line,
and retained encoded state from original unquantised motion. No new public
exercise is added before a learner has tried the existing material.

No learner is available. Difficulty, understanding, retention and unaided
transfer remain unknown. #114/#115/#124 stay open. VoiceOver and physical touch
retain their separate outstanding status in website #749. This model run cannot
qualify rendering, controls, assistive technology or arbitrary inputs. No machine
performance, hardware or historical claim follows from host arithmetic.

Next, use a learner observation or a reproduced discrepancy to guide the next
correction. This investigation supplies additional numerical/geometry evidence
for existing lessons, rather than a reason to expand the sequence.

## Reproduction and evidence checks

Run `node audit/2026-10-aiming-boundaries/verify-model.mjs SAMPLES_PATH OUTPUT_JSON`
from docs. Optional third arguments `endpoints` and `line` deliberately fail.
[Evidence validation](validation.json) checks the complete positive case counts,
input identities, two failed controls and retained local links.
[SHA256SUMS](SHA256SUMS) preserves evidence integrity. No dependency was added.
