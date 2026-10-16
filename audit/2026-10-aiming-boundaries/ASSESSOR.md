# Aiming boundary assessor notes

Keep these explanations separate from the learner sheet. Use the existing
[first-session observation sheet](../../guides/first-session/session-observations.md)
to record predictions, explanations, help and revisions. Do not explain the
answer before the learner has had a chance to reason about it.

1. Each endpoint is √27.25 ≈ 5.22015 units from the centre, so an endpoint-only
   test misses. Halfway along, at (1.5,0), the distance is exactly 5; the declared
   inclusive rule counts contact. Look for a distinction between sampled
   position and travelled segment, rather than accepting only the word “hit”.
2. The infinite horizontal line reaches the target, but this finite segment
   stops at X=3. Its closest point is (3,0), 6 units away, so there is no hit
   this tick. A case beyond the finish, before the start or a zero-length move
   can distinguish a correct finite-segment rule from an unbounded line test.
3. Stored velocity is −1, decoded velocity −0.25 units/tick. Four additions
   produce stored position −4, decoded −1. The original unquantised velocity
   would reach −0.5. Retaining fractional position preserves the chosen encoded
   velocity; it cannot recover error already introduced during encoding.
   JavaScript Math.round(−0.5) gives negative zero, so it does not implement the
   stated signed tie rule. The maintained model uses its own signed rounding.

The geometry fixtures are not selectable targets in the published controls.
Task 3 uses a deliberately small diagnostic velocity, not the experiment's
fixed speed 3. Do not present these as observed browser shots or retro-machine
execution. The actual exports are checked by the retained model verifier.
No learner outcomes are recorded.
