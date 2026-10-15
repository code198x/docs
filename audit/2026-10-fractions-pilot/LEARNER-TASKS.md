# Fractions: learner tasks

No learner has completed this trial. Keep first predictions before observations;
do not open the assessor sheet. Use the lessons as needed and record help.
There is no time target. Stop if a tool or instruction is unclear.

Choose Foundations, BASIC or assembly according to prior experience. Neither
system language requires the other. Binary place values and unsigned byte pairs
support these tasks; consult Counting in Twos if unfamiliar. Read Working the
Bits units 4–5 for the shared explanations.

## Predict and explain

1. Can a finite binary floating-point format hold a half exactly? A tenth?
   Explain why a screen showing 0.5 does or does not prove the stored value is exact.
2. Before running Spectrum BASIC, predict `PRINT (10000000000+1)-10000000000`.
   Observe it, then explain what the result says about precision. Does it prove
   every operation introduces an error?
3. At scale 256, decode the stored integer 384. Split its two bytes into whole
   units and 256ths. Predict what remains if you keep only the high byte.
4. Store 1.5 and 0.5 at the same scale 256. Add the stored integers, then decode
   the answer. Explain why the scales must agree.

## Change and check

5. At scale 256, represent 0.1 by rounding to the nearest integer. Write the stored
   integer and decoded value before using BASIC to check the division. Choose
   scale 10 instead: can it represent a tenth exactly?
6. Follow the optional BASIC link from unit 5 and find the fraction-to-secret
   table. Explain what INT does to its nonnegative values. Return with browser
   Back and explain why removing the fractional part is different from reading
   the full fixed-point value. The table can be read without playing the game.
7. If using BASIC, compare `LET x=1/2` and `LET x=0.5`, printing x after each.
   Can those printed answers alone settle whether their stored bytes match?
   Record what you can observe and what would require another tool.

## Find a fault and create

8. Someone reads stored 384 at scale 256 by shifting it right eight bits and
   expects 1.5. Diagnose the mistake. Someone else adds values stored at scales
   256 and 10 directly: what information must be reconciled first?
9. Choose a width and scale for a nonnegative game position that needs half-pixel
   steps and reaches at least 100 pixels. Show a position and a half-pixel move,
   their stored integers and their sum. Check both precision and range. Explain
   what extra evidence you need before calling your choice fast enough.

Keep first answers, edits, output and later explanations separate. The observer
may clarify the task but should not supply a missing concept.
