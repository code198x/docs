# Editable BASIC in the browser — bounded trial

**Status:** The two user-approved lesson integrations are published and live-verified in website PR #445. Its emulator APIs are published in npm 0.4.0. The user authorised a
Meet BASIC and Sonar trial after reviewing the editable assembly lessons. This
is evidence for a possible shared component, not a decision to retrofit the
whole BASIC curriculum.

## Teaching slice

- Meet BASIC, **Make the Spectrum answer**: the complete three-line greeting
  after changing `Hello` to `Welcome`.
- Sonar, **Read the sonar**: the existing unit 4 checkpoint, including coordinate
  input and near/medium/far clues. Its fixed target is `(3,6)`.

Both components read the maintained `.bas` files from code-samples. The samples
and published teaching sequence are unchanged. Both playgrounds are enabled in the normal website build.

`BasicAndRun.astro` supplies syntax-highlighted source, run/restore/stop controls,
a download of the current edited source as a TAP, and a text copy of the Spectrum
screen. Source and screen panels reuse the aligned layout of the assembly trial.
The native textarea retains ordinary editing and keyboard navigation. On the
Spectrum canvas, keys are forwarded to the emulated keyboard; they are released
on blur, hiding the tab and leaving the viewport. Sonar includes touch buttons
for digits, Enter, Delete and Q. Tab remains browser navigation.

## Machine and file path

Text is converted to tokenised BASIC by Rust compiled to WASM. The additive
`basicTape(source, name)` browser export uses the existing BASIC format crate's
keyword and number definitions, plus its new text-preserving listing path, and
the shared `format198x-sinclair-zx-spectrum-tap` writer. The analysis AST path
remains unchanged: its placeholder recovery is unsuitable for user-edited text.
The listing converter orders numbered lines, rejects duplicates, checks quoted
strings and number range, and preserves expressions instead of inventing them.
It is not a full BASIC syntax validator; ROM reports remain visible in the screen.

Run installs tokenised BASIC directly into a fresh 48K Spectrum’s RAM using
the shared native loader, fixes up the BASIC system variables, and asks the
real ROM to RUN it. No tape is mounted or played. Download still produces a TAP.
Conversion, boot and execution live in a dedicated worker. The page transfers
frames and sends at most one tick at a time. Run replaces the preceding worker;
Stop and navigation release it. Download uses a separate conversion worker so
it can export the current editor contents without restarting the running program.

The installed npm 0.4.0 package includes the canvas-free constructors and BASIC
exports, including `Spectrum.runBasic(source)`. `SPECTRUM_WEB_PACKAGE` remains
an explicit local override for further API trials; ordinary builds resolve the
installed package. No generated WASM or ROM is checked into the website repository.

## Scope still to establish

The trial covers these two silent, single-file listings. It does not establish
support for every Sinclair BASIC source convention or every curriculum game.
The text route currently accepts printable ASCII and numbered lines 1–9999,
with a 36 KiB program limit. Graphics/control-code escapes and DEF FN parameter
markers need a further format check. Keyword spelling uses word boundaries;
compact, context-ambiguous spellings need their own compatibility work.
Browser audio and broader keyboard/punctuation handling are not established by
these digit/letter input checks. Initial source drafts remain recoverable with
Restore; persistence across closing the page is not implemented.

## Reproduce the review

The normal build uses the published emulator package. A local
`SPECTRUM_WEB_PACKAGE` override is needed only when testing unpublished APIs:

```sh
npm run build
```

Serve `website/dist` over loopback HTTP. The normal lesson URLs contain the trial
widgets in this build. The site scripts retain browser and native checks:

```sh
node scripts/verification/basic-wasm.mjs http://127.0.0.1:1986 /tmp/basic-wasm-checks
python3 scripts/verification/basic-tape.py --emulator /path/to/emu198x-spectrum --output /tmp/basic-wasm-checks
```

Browser verification checks a source edit during worker boot, changed output,
current-source tape download and checksums, missing-line-number feedback, a ROM
syntax report, Restore, physical and virtual Sonar probes, changed target,
restart during boot, quit, editor/keyboard focus isolation, mobile layout and
forced-colours source visibility. The browser check confirms continued UI rendering during direct boot/run,
not a cross-browser timing guarantee.

The native reload check uses the actual browser downloads and fresh ROM tape
loads, confirming the edited greeting and finding Sonar's edited target.

The original tape-loading trial’s native downloads passed fresh ROM reload and Sonar input checks. Its evidence,
including source/build hashes and inspected captures, is retained under
`website/scripts/verification/evidence/basic-wasm/`. That trial passed 35 format/browser Rust tests and scoped wasm-target Clippy.
Both normal and opt-in builds passed, with 69 active site tests and nine skips.

## Direct execution check

`verification/direct-load.mjs` in the website scripts checks the local WASM
package independently of the lesson UI. It verifies BASIC output, a ROM syntax
report, and assembly that prints via the ROM and returns to BASIC, with
`tape.loaded` and `tape.playing` both false. The assembly lesson component uses
`runCode(bytes, origin, entry)` from the published 0.4.0 package. Its tape fallback
is retained for older packages.

Direct execution passes the full greeting/Sonar browser interaction check and
all three assembly lesson checks. The wrapper and shared runtime pass 109 Rust
tests and scoped wasm-target Clippy. The full trial website build passes,
including 69 active site tests (nine existing skips). Current direct-loading
evidence is under `website/scripts/verification/evidence/direct-load/`.

## Publication verification

The production build enables both playgrounds without a trial flag. Live browser
checks pass for edited source, responsive worker boot, ROM syntax errors, restore,
physical and virtual Sonar input, target changes, restart, quit, focus isolation,
mobile geometry and forced-colours source visibility. Both live-downloaded TAPs
match the freshly native-tested tapes byte-for-byte. CI and Pages deployment pass.
