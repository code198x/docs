# Bits and shifts: learner tasks

This trial has not been run with a learner. Keep predictions before observations;
do not open the assessor notes. Use the lessons when needed and record help.
There is no time target. Stop if a tool or instruction is unclear.

Start from Foundations, BASIC or assembly according to your experience. Neither
system route requires the other language. Counting in Twos supports unfamiliar
binary/hex notation; Decisions supports conditions. You may consult them without
having completed a course first.

## Predict and explain

1. Read Working the Bits unit 1. Starting with `11001010`, predict the result of
   AND with `00001111`, OR with `00001111` and XOR with `00001111`. Mark which
   positions can change and which must stay the same. Predict XOR with that mask twice.
2. Explain how many inputs BITNOT needs and why its answer depends on the width.
   Predict the eight-bit complement of `00001111`.
3. Before entering commands, predict Spectrum BASIC's `PRINT 202 AND 15` and
   `PRINT 9 OR 2`. Use the lesson if needed. Run them through the BASIC keyboard
   controls, then explain why their names do not establish bit-mask behaviour.
4. Use unit 2's eight-bit unsigned zero-fill rules. Predict the result bits and
   numeric values for 5 shifted left once, 200 shifted left once and 5 shifted
   right once. What leaves the stored byte in each case?
5. Start with `10000000`. Predict a zero-fill right shift and a right shift that
   preserves the old top bit. Read the results as signed two's-complement bytes.

## Change and check

6. Follow unit 1's optional byte-and-pixels link. Find the source drawer and
   choose “Change the pattern”. If a saved draft is offered, record what you
   choose; download work you want to keep before reverting.

   Set the pattern to `%11001010`. Insert `and %00001111` between the existing
   read and write, so these three lines appear in order:

   ```text
   ld a,(pattern)
   and %00001111
   ld ($4000),a
   ```

   Here `and` combines the bits in register A with the mask and leaves the result
   in A. `%` means binary. Predict the eight pixels, assemble and run, then compare
   the real memory reading and picture with your prediction. Use browser Back to
   return and explain how the shared lesson helped.

## Find a fault and create

7. Someone replaces a calculation of 200 × 2 with one left shift stored in a byte
   and expects 400. Find the missing assumption. Does saying “a shift is always
   fastest” resolve the problem? Explain what evidence a speed claim needs.
8. Choose a byte pattern of your own. Design a mask that turns on one chosen bit
   without changing the others. Then design a mask that flips two chosen bits.
   Predict both results and, if using the assembly editor, test them by replacing
   `and` with `or` or `xor` as appropriate. Explain what a second application does.

Keep your first answer, later changes, actual output and explanation separately.
The observer may clarify a task, but should not coach the answer.
