# Expected boundaries, before the run

Contact means the minimum distance from the target centre to the **finite**
movement segment is at most 5 world units. The centre need not coincide with a
sampled position. Use squared distances for these exact rational expectations.
These fixtures are diagnostic geometry, not additional selectable browser targets.

| Case | Start → finish | Target centre | Expected squared distance | Contact |
| --- | --- | --- | --- | --- |
| Tangency between ticks | (0,0) → (3,0) | (1.5,5) | 25 | yes |
| Just outside | (0,0) → (3,0) | (1.5,5.001) | 25.010001 | no |
| Just inside | (0,0) → (3,0) | (1.5,4.999) | 24.990001 | yes |
| Beyond finish | (0,0) → (3,0) | (9,0) | 36 | no |
| Before start | (0,0) → (3,0) | (-6,0) | 36 | no |
| Endpoint tangency | (0,0) → (3,0) | (8,0) | 25 | yes |
| Vertical tangency | (0,0) → (0,3) | (-5,1.5) | 25 | yes |
| Reversed travel | (3,0) → (0,0) | (1.5,5) | 25 | yes |
| No movement | (2,3) → (2,3) | (5,7) | 25 | yes |
| No movement, outside | (2,3) → (2,3) | (8,3) | 36 | no |

The first case distinguishes segment contact from endpoint-only sampling:
each endpoint is at squared distance 27.25, outside the target. The beyond-finish
case distinguishes a segment from an infinite line: the line reaches the centre,
but this movement does not. Tangency makes the inclusive boundary observable.
No arbitrary tolerance is added to the production hit rule.

Signed rounding uses nearest integer, with half ties away from zero:
−2.5 → −3, −1.5 → −2, −0.5 → −1, 0 → 0, 0.5 → 1, 1.5 → 2,
2.5 → 3. Neighbours −0.499 and −0.501 round to 0 and −1 respectively.
JavaScript's Math.round differs at negative half ties.

Direction cases are (1,0) → 0°, (1,1) → 45°, (0,1) → 90°, (−1,1) → 135°,
(−1,0) → 180°, (−1,−1) → 225°, (0,−1) → 270°, (1,−1) → 315°.
At (0,0), the model should return null rather than invent a direction.

The angle input permits tenths from 0 to 359.9 degrees, with scales 4, 16, 256.
Check all 10,800 velocity combinations against the nearest-integer contract.
This covers that declared grid, not every JavaScript number or pointer angle.
Position-width reasoning also needs the selected shot duration; a velocity bound
alone cannot prove a position bound. The six authored targets are 220 units from
the origin, with the stated six extra updates after ceil(distance / 3).
