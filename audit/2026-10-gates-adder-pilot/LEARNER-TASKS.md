# Gates and the Adder: learner tasks

Use the three units. Predict on paper before touching an input or opening an
answer. The page models settled 0/1 values; no electronics experience is needed.
Record any hint before using it.

1. **Compare rules.** Predict AND, OR and XOR for all four input pairs. Check
   each circuit using the keyboard. Which row distinguishes OR from XOR?
   Predict NOT for both of its inputs too.
2. **Read the whole answer.** For half-adder inputs 1 and 1, record sum and carry.
   Explain the numeric value of both together. Someone replaces XOR with OR for
   the sum output: find a case that reveals the fault and one that hides it.
3. **Check a contract.** For each of the full adder's eight input triples, record
   SUM and COUT, then check A+B+Cin = SUM+2×COUT. Explain what happens when all
   three inputs are 1 and why the two output bits are sufficient.
4. **Trace a different ripple.** Add three-bit binary 101 and 011 with starting
   carry zero. Make one row per column, from bit 0 upwards. Record both inputs,
   carry in, sum and carry out. Read the full result, then state what remains if
   a program keeps only the three low sum bits.
5. **Diagnose propagation.** Correctly adding 000 and 000 gives zero. Imagine a
   fault forces carry in to bit 1 to be 1, while bit 0 was correct. Trace bits 1
   and 2. Does the fault alter every higher column? Explain where it stops.
6. **Separate model from measurement.** A drawing passes every stable AND row.
   Has it measured a chip's voltage limits or the time its output takes to change?
   Name information that the four rows do not contain. What evidence would a
   physical timing claim need?
7. **Make an output policy.** Design a two-bit unsigned adding tool. Choose two
   input pairs: one whose sum fits two bits and one needing an extra bit. State
   the starting carry and whether the tool displays, saves or rejects the extra
   carry. Give expected low bits and carry for both pairs, and a check that
   reconstructs the full result. Explain what the user sees at the boundary.

Optional connections:

- In A Minus With No Minus Sign, compare the examples for carry and signed
  overflow. Explain why the interpretation of a byte matters to the question.
- In Meet Assembly's first lesson, find what the complete program changes.
  Reading its local explanation is enough; record running/editing separately.

Afterwards, record which explanation remained unclear. Do not include a child's
name or personal details in shared observations.
