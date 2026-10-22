# Embedded BASIC latency: first-session greeting

Fifteen live timed runs completed successfully: five fresh-context cold starts,
five unchanged runs on the same page, and five edited greetings. Observed
click-to-result ranges were **3.43–3.74 seconds cold**, **3.31–3.44 seconds warm
unchanged**, and **3.23–3.37 seconds warm edited**. These are measurements of a
specified desktop task and observation method, not a performance rating or a
promise for other learners, browsers or networks. No optimisation is proposed.

This addresses [website #748](https://github.com/code198x/website/issues/748)
under umbrella #124, after
approved [website #750](https://github.com/code198x/website/pull/750) and
[docs #81](https://github.com/code198x/docs/pull/81) merged. The
[preceding browser qualification](../2026-10-embedded-basic/REPORT.md) established
stored-value/error recovery. This pass measures a different, named first-session
route rather than reusing that earlier run as timing evidence.

## Task and exact boundaries

We used the published [Make the Spectrum answer](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-01-make-the-spectrum-answer/)
editable listing—the same greeting activity linked from the first-session pack.
The maintained three-line program prints Welcome, to you, from the Spectrum.
Each trial has these sequential stages:

1. **Cold startup:** a new browser context navigates to the lesson with browser
   HTTP cache cleared and disabled. The timer starts at a capturing click listener
   on Run this code, before the product's run handler. It includes tape preparation,
   WASM initialisation, machine creation, tape loading and program execution.
2. **Warm unchanged:** return to the listing and choose Run again on the same
   page with identical source. The fetched/initialised module remains available;
   the product creates a new machine. HTTP cache remains disabled.
3. **Warm edited:** replace Welcome with Hello again plus the trial number, then
   choose Run. Click-to-result uses the same boundary as above. A separate
   input-to-result value begins at the source field's input event from that complete
   replacement. It includes the automation's edit-to-submit gap, not human typing time.

All three timers end only after the complete expected three-line output and
`0 OK, 20:1` are observed, two animation-frame callbacks have occurred, and
readback confirms a nonblank text region on the visible machine canvas. A fresh
incomplete transcript transition is required before success, preventing an
unchanged warm run from passing on its predecessor's output. Edited markers differ
per trial. Canvas fingerprints match for the two unchanged programs and differ
for each edited result.

We measure the **application-observed complete-result endpoint**. This is not
first-pixel latency or physical display response. The product updates screen text
every ten runner callbacks, not continuously. Event-loop work and the two later
callbacks can delay observation; there is no fixed millisecond error bound.
The recorded final match-to-end interval ranges from about 30 to 151 ms, and
canvas readback contributes about 0.1 to 9.3 ms. Those costs are included, not
subtracted to invent a faster result. Page navigation is recorded separately
and excluded from the Run timer; the method also excludes time spent reading,
scrolling to the listing and deciding what to change.

The browser's [performance.now clock](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now)
provides all action/result timestamps within the same document. Network/cache
observations use [Playwright CDP sessions](https://playwright.dev/docs/api/class-cdpsession)
and the [Chrome Network protocol](https://chromedevtools.github.io/devtools-protocol/tot/Network/).
No Chrome DevTools MCP trace tool was available; the installed Playwright/CDP
path supplied the needed task and network observations. We did not collect a
main-thread trace, Core Web Vitals audit or accessibility audit in this bounded pass.

## Configuration and identity

[Raw results](results.json) identify Chrome **155.0.8059.40**, Playwright
**1.62.1**, Node **24.22.0**, macOS **27 arm64**, Apple **M2 Max**, 12 logical
CPUs and 32 GiB host RAM. Viewport: **1440 × 1000**, device scale factor 1;
headless Chrome, sound off, sequential trials, CPU throttle rate 1. Network:
**unthrottled host connection**, with no bandwidth or RTT shaping. This is not a
mobile-network simulation, and available bandwidth was not independently measured.
Other host workloads were not controlled.

“Cold” means a new nonpersistent context and document, empty browser session
storage, and cleared/disabled browser HTTP cache. Service workers were blocked.
It does not mean a cold CDN, DNS resolver, TLS connection pool, operating system,
CPU or browser-process compilation cache. All five contexts shared one Chrome
process. “Warm” means same-page module reuse, not a warm-cache page reload.
These labels do not qualify every possible cold/warm configuration.

The network records show one HTTP 200 WASM response per trial during cold startup,
with no disk-cache or service-worker delivery, and **no recorded same-origin network responses in the
warm stages**. Cross-origin background requests were not retained in that log. The five WASM payload hashes agree. Each trial retains twelve
JavaScript/WASM response hashes, read after its cold timed endpoint so hashing
does not run inside that measurement. CDP event logging and passive DOM observation
remain instrumentation costs. We did not measure an uninstrumented control.

[Source identities](identities.json) bind the inspected website baseline
`97f306dc7bbd3b8190c06498eb5eccfca7e0cb43`, docs baseline
`dc585af6160ea6e1ec9c2043c9a1a86d62f7c40b`, samples
`163e74e18e9536fb555ef7319fa08bbc1836542b`, lesson, components, runner and
package files. The original live listing matches the maintained unit 1 step 4
sample. Raw results retain the executing verifier's hash, HTML hashes and live
served asset identities. The inspected browser package is 0.4.3; the browser ROM
fingerprint remains uncaptured. [Deployment metadata](deployment-metadata.json)
names the successful deployment of the website baseline. It supplements actual
execution/response evidence; it does not prove source-to-binary provenance alone.

## Individual observations

Values below are milliseconds rounded for reading. Full precision is retained in
JSON; displayed digits are not a claim of measurement accuracy.

| Trial | Cold Run → result | Warm unchanged Run → result | Warm edited Run → result | Edited input event → result |
| --- | ---: | ---: | ---: | ---: |
| 1 | 3742.3 | 3409.1 | 3316.2 | 3341.9 |
| 2 | 3432.5 | 3444.3 | 3311.3 | 3347.5 |
| 3 | 3632.8 | 3408.6 | 3229.2 | 3249.8 |
| 4 | 3550.5 | 3359.0 | 3259.3 | 3295.1 |
| 5 | 3445.6 | 3306.1 | 3367.8 | 3405.5 |

| Measure | n | Minimum (ms) | Median (ms) | Maximum (ms) |
| --- | ---: | ---: | ---: | ---: |
| Cold click-to-result | 5 | 3432.5 | 3550.5 | 3742.3 |
| Warm unchanged click-to-result | 5 | 3306.1 | 3408.6 | 3444.3 |
| Warm edited click-to-result | 5 | 3229.2 | 3311.3 | 3367.8 |
| Edited input-to-result | 5 | 3249.8 | 3341.9 | 3405.5 |

The cold and unchanged warm ranges overlap; trial 2's warm run is slightly slower
than its cold run. These samples do not isolate network, compilation, machine
boot or tape costs, and do not support a general speedup claim. The edited program
also has a different string/tape payload, so its timing is not a controlled test
of a code optimisation. Five trials on one machine do not establish a population
percentile, deadline, SLA or learner tolerance.

The last trial's [cold](cold.png), [warm unchanged](warm.png) and
[edited](edited.png) canvas screenshots were visually inspected. The first two
show Welcome; the third shows Hello again 5, with the other two greeting lines
and successful completion. Every timed stage separately retains actual text rows,
canvas fingerprints and incomplete/complete observation timestamps.

## Failure controls, verification and next step

All fifteen positive stages passed on the first measurement attempt; no failed
positive sample was dropped. An additional **missing-result control** asks for
text that the program cannot print. It uses a deliberate two-second observation
deadline, returns failed with a null end timestamp and no latency value, and is
excluded from successful timing statistics. That short control deadline is not a
performance budget or evidence that the real program failed to boot. Empty/stale
or incorrect output cannot satisfy the normal complete-result condition.

Run `scripts/verification/embedded-latency.mjs` from the website checkout with
installed Chrome and the existing dependencies:

```sh
node scripts/verification/embedded-latency.mjs https://code198x.com /path/to/evidence 5
```

Node syntax and explicit-semicolon checks pass. The
[evidence verifier](verify-evidence.py) independently recomputes counts/statistics,
checks all timing boundaries against actual complete/fresh outputs and canvas
changes, validates cache/asset/source identities, and rejects missing or altered
observations. [Validation](validation.json) records the outcome;
[artefact hashes](artifacts.json) identify the retained raw results and screenshots.

Website #748 can close when this reproducible baseline is accepted. We have no
agreed performance budget or learner evidence that these waits are acceptable or
unacceptable, so we propose no optimisation from this sample. Further attribution
would need a separate targeted profile, preserving the same user-visible outcome.
Next qualify the broader first-session browser/input/assistive-technology matrix
under [website #749](https://github.com/code198x/website/issues/749). Umbrella #124
remains open. Physical mobile, touch, Safari/WebKit, assistive technology, slower
networks and learner outcomes remain unqualified by this desktop baseline.
