# Loops and repetition: learner tasks

Draft prompts for a future trial. Choose one route; BASIC and assembly do not
require each other. Predict before running code or revealing an answer. Tell the
observer when the difficulty is finding a control, reading syntax or reasoning
about the program.

## Foundations

Find [Repeating](https://code198x.com/foundations/repeating/) from Start Here and
read the relevant lessons. Use the proposed preview for the revised random-choice
explanation until it is published. Pseudocode is notation to trace, not code to
type into a Spectrum.

1. For `FOR i = 1 TO 3`, predict the values shown by `SHOW i`. What changes with
   `1 TO 1`, and with `1 TO 0`? Explain whether both endpoints count.
2. In [Checking Before You Start](https://code198x.com/foundations/repeating/unit-03/),
   start with zero lives. Which instructions run? Compare that with a `REPEAT`
   block: when is its condition first checked?
3. In [Until You Get It](https://code198x.com/foundations/repeating/unit-02/),
   suppose the chosen secret is 7 and the guesses are 4, 9, 7. How many times
   does `ASK` run, and how many times does the assignment to `secret` run?
4. The previous round chose 7. Can the next round choose 7 too? Predict before
   opening the answer. Would a repeated value alone establish a fault?
5. Someone moves `LET secret = RANDOM 1 TO 10` inside the guess loop. Explain
   what rule changes and how that affects the earlier clues. Restore one fixed
   answer per round, without claiming that each round must have a unique value.
6. Create a short guessing example with your own range and messages. Mark which
   work happens once per round and which happens once per guess. Choose a sample
   secret and a sequence of guesses, then trace the route to termination.

## BASIC

Read [Keep guessing](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-06-keep-guessing/)
and [Choose a new secret](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-07-choose-a-new-secret/).
Use the opening's entry/keyboard guidance as needed. The complete listings let
you join without assembly or Foundations. Target keyboard entry needs a physical
keyboard; do not assume these lessons have an editable browser listing.

1. With the known secret restored to 7, predict the messages and guess count for
   4, 9, 7. Explain why `GO TO 30` does not run the secret assignment or reset the
   attempt counter.
2. Change the loop destination to line 15, where the counter is initialised.
   Predict what happens to the count. Test, explain and restore line 30.
3. In lesson 7, use the supplied fixed seed experiment: `5 RANDOMIZE 1`. Run and
   guess 1, then run again and guess 1. Explain why the repeated answer is useful
   for testing and why it is not evidence of a broken generator.
4. Restore normal seeding. Give a new round a fresh choice while keeping that
   choice fixed during the guesses. Explain which lines enforce each part of
   that requirement. A short in-range sample does not prove equal likelihood.
5. Choose a different example range. Identify all the range, validation and
   prompt changes before editing. Test the two endpoints with deliberately fixed
   secrets first, then restore random selection. Keep a copy of work to retain.

## Assembly

Read [Draw with a counted loop](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meet-assembly/unit-04/).
Earlier assembly lessons explain the editor, memory and register operations;
BASIC is not required. Keep the drawing experiments within the lesson's 1–8
range. Do not run an unsafe zero-count drawing experiment.

1. Predict the eight destination addresses before using the recorded-write
   replay. Does advancing DE after the final write mean the loop also wrote at
   the advanced address? Compare with the actual captured writes.
2. Predict and test `ld b,4`. What happens to rows that are never written? Does a
   shorter loop clear them automatically?
3. Explain why initial B=0 would not skip this body. Use the lesson's decrement
   rule and byte wraparound; do not test it against the eight-byte drawing table.
   Compare with Foundations' empty `FOR 1 TO 0` range. Are those constructs
   interchangeable merely because both are called counted loops?
4. Remove `inc d`, predict the destination addresses and final first-row value,
   then test. Explain why repeated writes do not preserve every previous pattern.
5. Restore the pointer step, choose your own eight-row artwork and transfer it
   from the preceding lesson in the same tab. Predict the first and last writes,
   run, inspect and download the current source.

## Optional connection and return

[LFSR Random Numbers](https://code198x.com/patterns/cross-platform/framework/lfsr-random/)
is an intermediate optional pattern. It explicitly labels its code illustrative
and has no execution record for the listing. Find what it says about using the
same seed. Explain why it is not the Spectrum ROM's `RND` implementation, then
return to your lesson. You do not need to implement it or accept an untested
listing as verified to complete this pilot.
