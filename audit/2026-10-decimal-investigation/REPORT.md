# Spectrum decimal conversion: resolved stock-ROM behaviour

The difference between `LET x=0.5` and `LET x=1/2` comes from the stock Spectrum
ROM's documented division-rounding bug. Emu198x and independently built Fuse
produce identical bytes for all seventeen tested ROM operations. The half is
exactly representable; the decimal-input routine does not always produce it.

[Docs #63](https://github.com/code198x/docs/issues/63) is resolved by this evidence.
No emulator implementation change is needed for this discrepancy. The configured
ROM and public lessons are unchanged. An altered ROM was used only as a disposable
counterfactual, not shipped as a fix. Learner effectiveness remains untested.

## Cause

The ROM's decimal parser, `DEC-TO-FP` at `$2C9B`, builds fractional digits using
successive divisions by ten. For `0.5`, its first fractional step obtains a stored
approximation to `1/10`, multiplies by 5 and adds it to the accumulated value.

The stock division routine at `$31AF` has a documented error in forming an extra
rounding bit. Its conditional jump at `$31FF` goes to `$31E2`, skipping a shift
needed to obtain the 34th quotient bit. Consequently, cases such as `1/10` are not
rounded up when they should be. In the configured ROM:

| Route | Five stored bytes, hexadecimal | Exact rational reading |
| --- | --- | --- |
| Decimal `0.1`, or calculation `1/10` | `7D 4C CC CC CC` | 858993459/8589934592, below one tenth |
| Decimal `0.5`, or calculation `(1/10)*5` | `7F 7F FF FF FF` | 4294967295/8589934592, below one half |
| Calculation `1/2` or `5/10` | `80 00 00 00 00` | 1/2 exactly |
| Exponent notation `5e-1` | `80 00 00 00 00` | 1/2 exactly |

For this particular exponent form, the ROM's `E-TO-FP` path scales 5 by dividing
it by 10 directly. It does not first form the rounded reciprocal and multiply by
5. That division is exact. The observed paths agree with the source explanation.
This does not promise that every exponent-form literal is exact.

All the half-valued interactive examples print `0.5`. Displayed digits cannot
establish the equality of stored bytes. The prior audit's numeric-byte decoder
was consistent with the documented format; its initial assumption about the
result of decimal input was too strong.

## Primary sources and the counterfactual

Ian Logan and Frank O'Hara, *The Complete Spectrum ROM Disassembly*, pp.160–161,
explains `DEC-TO-FP`; pp.162–163 explains exponent scaling; pp.184–185 explains
division. The note on p.185 explicitly identifies the misplaced jump, the lost
34th bit and failure to round `1/10` upward. This existing primary source supplies
the mechanism, rather than an inferred emulator defect.

The note's proposed hexadecimal change is verified against actual ROM bytes:
address `$3200` contains `E1`. The instruction `28 E1` at `$31FF` targets `$31E2`.
Changing only that displacement to `DA` targets `$31DB`. We use the hexadecimal
values and verified branch targets; the held text's decimal rendering beside DA
is inconsistent and is not used.

In a disposable copy, that single-byte change causes Fuse to produce:

- `0.1` and `1/10`: `7D 4C CC CC CD`, matching the correctly rounded representation
  in Sinclair Research's *ZX Spectrum BASIC Programming*, chapter 24 pp.169–170.
- `0.5`, `.5` and `(1/10)*5`: `80 00 00 00 00`, exactly one half.
- `1/2`, `3/4`, `5/10` and `5e-1`: unchanged exact results.

The counterfactual is causal evidence for the selected discrepancy, not a general
ROM repair. An initial assertion that it would make every selected representable
decimal exact failed. The full results preserve that limit: corrected conversion
of `0.25`, `0.125` and `0.0625` lands slightly above the exact values, after other
rounded operations. The final check asserts the half/tenth discriminator and
records the wider cases without claiming universally correct decimal conversion.

The BASIC manual's rounded tenth describes the representation the division should
produce; the contemporary ROM disassembly explains why this implementation can
produce the preceding value instead. Binary representability, conversion
algorithms and formatted output remain separate facts.

## Execution method and identities

The [plan](../../plans/2026-10-15-decimal-conversion-investigation.md) bounds the
investigation. Docs baseline `b9bb712878c8a739d866ef8ad96a8be7c0232fad`; samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. Unrelated README/work edits in the
normal docs checkout were excluded using an isolated worktree. No emulator source,
reference source or configured firmware was modified.

The [reproducer](verify-conversion.py) reuses the maintained ROM keyboard driver
and previous rational decoder. It generates the [fixture](conversion.asm) and
assembles a binary and auto-running tape with Asm198x. The fixture calls the real
ROM on ASCII strings; it does not inherit numeric constants converted by Emu198x.
Five further cases use the ROM calculator with integer operands. Results are
copied from the calculator stack, followed by a completion marker.

Emu198x Spectrum 0.32.5 boots independently, runs six interactive LET/PRINT cases,
then loads the fixture tape. Loaded code bytes must match the generated binary.
Fuse 1.7.0 boots separately with the same tape and ROM, using its normal tape-load
acceleration. It executes the ROM's number conversion and calculator routines on
its own Z80 implementation. No snapshot transfers, injected results or host
floating-point shortcuts supply the comparison values.

The check reads all 16,384 mapped ROM bytes in each stock-engine run and in the
counterfactual reference run. Each must match its supplied firmware. Each engine
must reach marker 165 and produce the complete result count. Missing output,
different firmware, an unloaded native fixture, disagreement, timeout or a failed
counterfactual discriminator makes the check fail.

[Results](conversion-results.json) record executable, driver, decoder, generated
code/tape and firmware hashes. The stock mapped-ROM SHA-256 is
`d55daa439b673b0e3f5897f99ac37ecb45f974d1862b4dadb85dec34af99cb42`.
The counterfactual has a separate hash and differs in exactly the selected byte.
The configured stock ROM was fingerprinted again afterwards and is unchanged.
No firmware, snapshot or third-party executable is committed.

Fuse and libspectrum 1.6.0 were built from disposable copies of existing reference
source, with the null UI and existing build libraries. The reference library was
staged only in a disposable prefix; no system package or project dependency was added.
[Build identity](reference-build-identity.json) records compiler and selected
original-source hashes. The originals remain reference-only.

## Outcomes and limits

| Check | Outcome | Qualification |
| --- | --- | --- |
| Original interactive discrepancy | Reproduced | Six LET/PRINT cases verify raw storage, complete output and normal completion. Half-valued prints agree despite differing bytes. |
| Independent stock-ROM execution | Passed | Seventeen operations, 85 numeric bytes, match between Emu198x and Fuse. Mapped ROMs and completion markers verified. |
| Direct conversion versus calculator route | Passed | Decimal 0.5 agrees byte-for-byte with `(1/10)*5`; exact division and exponent-path controls agree. |
| Documented one-byte counterfactual | Passed within stated scope | Half/tenth results change as predicted; four exact controls remain unchanged. Other decimal conversions are retained observations. |
| Installed macOS Fuse CLI attempt | Stopped setup attempt | The app opened instead of supplying CLI help; the task-owned invocation was stopped. Numeric results come from the separately built null-UI reference. |
| Initial headless debugger invocation | Failed setup | Timed out at 40 seconds with `error: Invalid debugger command: syntax error`. A trailing top-level newline was removed after inspecting the grammar. |
| Explicit-ROM automatic tape route | Failed setup | A second 40-second timeout. Bounded diagnostics showed the code was not loaded. Fuse disables autoload for a custom ROM filename, even if its bytes match the default. A default-basename copy in an owned temporary directory resolved this; mapped bytes are verified. |
| Snapshot-export probe | Refused correctly | The native writer rejected `.sna` because it writes its own state format. No misleading file or snapshot-based numeric comparison was used. |
| Broad “all binary fractions exact after patch” assertion | Failed audit assumption | Retained in [setup observations](setup-observations.json); narrowed to the actual documented discriminator. This failure is not relabelled as a pass. |
| Python and prose checks | Passed | Ruff and Vale checks, evidence hashes and patch whitespace checks. |
| Original hardware, other ROM revisions, current emulator builds beyond the named binary, and learning outcomes | Not qualified | Two independent software engines and a causal ROM experiment resolve the configured case, not every arithmetic implementation or learner task. |

The updated fractional assessor sheet points here instead of calling #63 open.
The earlier report remains a historical snapshot of what was then unresolved.
No public lesson correction is necessary: the published lesson already distinguishes
format representability from input conversion and display. Preserving the stock
ROM's behaviour is appropriate for the emulator; changing its arithmetic to hide
a ROM bug would misrepresent this machine.

## Reproduce

Use existing local reference source and installed build prerequisites. Copy it;
do not build in or edit the reference tree. For example, in a disposable workspace:

```sh
cd /path/to/disposable/libspectrum-1.6.0
./configure --prefix=/path/to/disposable/install --disable-shared
make -j4
make install
cd /path/to/disposable/fuse-1.7.0
PKG_CONFIG_PATH=/path/to/disposable/install/lib/pkgconfig ./configure --with-null-ui --without-gtk --without-sdl --disable-sdl2 --without-libgcrypt --prefix=/path/to/disposable/install
make -j4
```

From docs:

```sh
python3 audit/2026-10-decimal-investigation/verify-conversion.py --samples ../code-samples --rom /path/to/48.rom --emulator /path/to/emu198x-spectrum --assembler /path/to/asm198x --fuse /path/to/disposable/fuse-1.7.0/fuse --output /tmp/spectrum-decimal-results
```

The script creates and removes its own stock/counterfactual ROM copies beneath
the output folder. It never overwrites the supplied ROM. Keep the source, JSON
observations and [evidence hashes](evidence-sha256.json); do not publish firmware
or treat the counterfactual as the machine's original behaviour.
