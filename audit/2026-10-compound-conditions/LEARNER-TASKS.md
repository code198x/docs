# Compound-condition learner tasks

Use the proposed Decisions unit 4. We use teaching notation on paper; nothing
needs installing. A comparison makes a TRUE/FALSE answer. AND needs both answers,
OR accepts either or both, and brackets choose which answers belong together.
Assume input has already supplied an ordinary numeric value. We are not parsing
words or deciding how a machine handles invalid text.

Try these before revealing the lesson answers or reading the assessor notes.
Use words, a table or a trace. There is no score, time target or required course.

1. Predict which values pass `guess >= 1 AND guess <= 10`: 0, 1, 1.5, 10 and
   10.5. Does the condition promise that accepted values are whole numbers?
   Explain what each comparison checks.
2. Compare `guess > 0` with `guess >= 1`. Find one value that distinguishes them.
   Would your answer change if a separate rule guaranteed whole-number input?
3. A program should accept numbers between 2 and 8, including both ends. Its
   author wrote `guess >= 2 OR guess <= 8`. Predict what happens for 0, 5 and 9.
   Repair the condition and explain how these three cases distinguish the repair.
4. The intended rule is: the player must be alive and have ammo or grenades.
   Compare `alive AND ammo > 0 OR grenades > 0` with
   `alive AND (ammo > 0 OR grenades > 0)`. Choose current values that make the
   results differ. Explain which version expresses the intended rule.
5. Modify the range rule to reject values below 2 or above 8. Give both an
   accepting condition and a rejecting condition. Check their answers at 2,
   8 and a fraction inside the interval. Does reversing the two messages as
   well as reversing the condition preserve the behaviour?
6. Create a rule for a door that opens only when power is on and either a key
   is present or an override is on. Give all eight TRUE/FALSE input combinations,
   identify the passing rows, and supply a wrong grouping with a counterexample.

Optional machine connection: follow the lesson's Keep guessing link. Find the
separate range and whole-number checks. Explain why rejecting 6.5 differs from
changing it into 6. Read the local explanation; running the preceding game is
optional. Return to the Foundations lesson afterwards.

Tell the observer where a word, symbol or instruction left you guessing. Record
help separately from your answer. A corrected prediction with an explanation is
useful; copying the revealed answer does not establish independent understanding.
