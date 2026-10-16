# Compound-condition assessor notes

No learner trial has taken place. These notes prepare an observation; expert
model/native checks do not establish that the tasks are understandable or that
learning transfers. Use the matching proposed lesson and keep this sheet apart
from the prompts. Record predictions before revealing explanations, help given,
repairs and the learner's reasoning. Do not coach a first attempt.

1. 0 fails, 1 passes, 1.5 passes, 10 passes, 10.5 fails. The interval includes its
   endpoints and fractions between them. Neither comparison tests whole-number
   validity. Watch for rejecting 1.5 because the earlier secret-number game used
   whole numbers: that game has an extra rule.
2. 0.5 is greater than zero but is not at least one. For whole-number input,
   both lower-bound tests agree. Ask for a reason or a new distinguishing value,
   rather than accepting a memorised example alone.
3. The wrong OR accepts all three: each number meets at least one broad bound.
   `guess >= 2 AND guess <= 8` rejects 0/9 and accepts 5. Testing only 5 would
   not expose the wrong joining word. Preserve both endpoint inclusions.
4. With alive FALSE, ammo 0 and grenades 1, the ungrouped expression is TRUE and
   the grouped expression FALSE. AND binds before OR in this notation. Brackets
   keep being alive necessary for either resource. Ammo 1 with those other
   values also distinguishes them; do not require one particular example.
5. Accept with `guess >= 2 AND guess <= 8`; reject with
   `guess < 2 OR guess > 8`. The accepting test is TRUE and rejecting test FALSE
   at 2, 8 and an interior fraction such as 3.5. Swapping both the condition and
   its branch messages preserves these outcomes. Swapping only the condition
   reverses them. A whole-number rule would be an additional condition.
6. `power AND (key OR override)` passes only these rows:
   TRUE/FALSE/TRUE, TRUE/TRUE/FALSE and TRUE/TRUE/TRUE, in power/key/override
   order. The other five fail. The wrong `power AND key OR override` also passes
   FALSE/FALSE/TRUE and FALSE/TRUE/TRUE. Look for a complete eight-row table and
   an explanation of the unintended unpowered opening.

The optional BASIC connection rejects out-of-range values and then checks
whether a value equals its INT result. Changing the value first would turn a
fraction into a different guess. These are checks on a numeric value; BASIC's
input-expression syntax and errors remain separate. Do not paste Foundations
notation into the Spectrum or infer another language's numeric truth rules.

After the first attempt, offer a hint if wanted: trace each comparison separately,
then combine the two answers. For grouping, calculate the bracketed part first.
Record any hint before asking for another example. A useful transfer observation
is a new boundary or a new wrong guard explained without copying the lesson.
