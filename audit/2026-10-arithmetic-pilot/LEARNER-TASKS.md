# Working It Out: learner tasks

Use the four Working It Out pages. You can read the pseudocode without choosing a
machine or learning BASIC first. Work on paper or in a plain text document. Ask
for a hint if needed; the observer should record it before helping.

1. **Predict the order.** Before calculating, group `24 / 4 * 2` and
   `24 / (4 * 2)`. Predict each result and explain which operation happens first.
   Then compare `18 - 6 - 3` with `18 - (6 - 3)`.
2. **Explain an update.** Start with `LET score = 4`. Carry out
   `LET score = score + 6` twice. Record the value before and after each line.
   What changes if `LET score = 4` runs again before the second update?
3. **Diagnose lost state.** Start with `a = 3`, `b = 8`, `c = 12`.
   A program tries to move old b into a, old c into b and old a into c by running
   `LET a = b`, `LET b = c`, `LET c = a`. Trace what happens and explain which
   old value is lost. Repair it using a spare variable.
4. **Choose the answer you need.** Thirteen tiles go in rows of four. Work out the
   full quotient, the number of complete rows, the leftover and the nearest whole
   number. Which answer tells you how many complete rows you can build? Check
   that complete rows and leftovers account for all thirteen tiles.
5. **Test boundaries.** Try totals 0, 3, 4 and 5 with group size 4. For each,
   record whole groups and leftovers. Explain why group size 0 is outside the
   rule. Would dropping the fractional digits correctly implement
   `ROUND DOWN (-9 / 2)`? Explain using a number line.
6. **Diagnose wrapping.** A 16-column display has columns 0 through 15. An update
   produces position 18. Someone tests `position REMAINDER 16 = 0` and expects
   this to supply the wrapped column. Explain the mistake and find the column.
   What happens to position 16? What extra rule would be needed for negatives?
7. **Make a small layout rule.** A line has 24 character columns. Choose a text
   length that leaves an odd number of spare columns. Write pseudocode for the
   left starting column, state the allowed text lengths, and explain which side
   gets the extra column. Change the rule so that the other side gets it.
   Say what should happen if the text is longer than the line.

Optional connections:

- In Choose a new secret, read the operation table for `INT (RND*10)+1`.
  Explain why the final addition is outside INT. There is no need to play the
  preceding game. If you do run it, record that separately.
- In Centre Text on a Character Screen, find the policy for overlong text.
  Compare it with your layout rule without needing to read the assembly.

Afterwards, say which step needed a hint and which explanation you would change.
Do not submit a child's name or personal details with the observations.
