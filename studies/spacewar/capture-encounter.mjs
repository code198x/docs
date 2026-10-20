// Reproduce the reference encounter without modifying the game or emulator.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const args = process.argv.slice(2);
if (args.length !== 4 || args[0] !== '--website' || args[2] !== '--output-dir') {
  throw new Error('Usage: node studies/spacewar/capture-encounter.mjs --website ../website --output-dir /tmp/spacewar-captures');
}
const requireWebsite = createRequire(path.resolve(args[1], 'package.json'));
const { chromium } = requireWebsite('@playwright/test');
const output = path.resolve(args[3]);
fs.mkdirSync(output, { recursive: true });
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const signed = n => n & 0o400000 ? -(n ^ 0o777777) : n;
const expected = {
  'spacewar_3_1.js': 'f84be5748f3d033bbf63f94ebe93814f843052ebb4e63f9f89bec5b8920d59ec',
  'spacewar_pdp1_engine_ng.js': '01d425147f3dc18524d882992678fa477b1993259a67230064e13ec057582b58',
};
const browser = await chromium.launch();
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1050 } });
  page.setDefaultTimeout(45000);
  const errors = [];
  const responses = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => {
    if (Object.keys(expected).some(name => response.url().endsWith('/' + name))) responses.push(response);
  });
  await page.goto('https://www.masswerk.at/spacewar/', { waitUntil: 'networkidle' });
  await page.selectOption('#spacewarCodeSelect', 'spacewar3.1');
  await page.keyboard.press('Space');
  await page.waitForTimeout(100);
  await page.evaluate(() => PDP1Engine.stop());
  const identities = [];
  for (const response of responses) {
    const name = response.url().split('/').pop();
    const body = await response.body();
    if (sha(body) !== expected[name]) throw new Error('Implementation changed: ' + name);
    identities.push({ url: response.url(), bytes: body.length, sha256: sha(body) });
  }
  if (new Set(identities.map(r => r.url)).size !== 2) throw new Error('Missing implementation identity');
  const configuration = await page.evaluate(() => PDP1Engine.getConfiguration());
  if (configuration.id !== 'spacewar3.1' || configuration.sense !== '' || configuration.testword !== 0) throw new Error('Unexpected configuration');
  let memory = await page.evaluate(() => PDP1Engine.getMemory(0, 4095));
  // In 3.1 the end-loop jump leads to ml0; its third instruction is LAW mtb.
  const loop = memory[0o2051] & 0o7777;
  if ((memory[loop + 2] & 0o770000) !== 0o700000) throw new Error('Unexpected object-table setup');
  const table = memory[loop + 2] & 0o7777;
  const objects = 24; // source: nob=30, in octal
  const addresses = {
    routine: table, x: table + objects, y: table + objects * 2,
    dx: table + objects * 5, dy: table + objects * 6,
    angle: table + objects * 7 + 2, fuel: table + objects * 7 + 4,
    torpedoes: table + objects * 7 + 6,
  };
  const read = data => [0, 1].map(i => Object.fromEntries(Object.entries(addresses).map(([name, address]) => [name, name === 'routine' ? data[address + i] : signed(data[address + i])])));
  const initial = read(memory);
  if (initial.some(s => s.torpedoes !== -33 || s.fuel !== -8192)) throw new Error('Unexpected starting resources');
  const report = {
    method: 'Scripted two-sided aiming through keyboard inputs with read-only state inspection; not a human play session.',
    edition: 'Spacewar! 3.1, 24 Sep 62', browser: browser.version(),
    configuration, emulationSpeed: await page.evaluate(() => PDP1Engine.getEmulationSpeed()),
    identities, addresses, initial, events: [], captures: [], errors,
    limitation: 'Wall-clock input intervals are approximate. Positions and velocities are game storage units, not physical units. Modern phosphor rendering is not original-hardware verification.',
  };
  async function capture(filename, step) {
    const target = path.join(output, filename);
    await page.locator('#pdp1_canvas').screenshot({ path: target });
    const dimensions = await page.locator('#pdp1_canvas').evaluate(c => ({ width: c.width, height: c.height }));
    if (dimensions.width !== 512 || dimensions.height !== 512) throw new Error('Unexpected capture size');
    report.captures.push({ filename, step, ...dimensions, sha256: sha(fs.readFileSync(target)) });
  }
  await capture('opening.png', -1);
  let previousKeys = new Set();
  let destroyed = false;
  let inactive = false;
  let completed = false;
  const deadline = Date.now() + 90000;
  for (let step = 0; step < 400 && Date.now() < deadline; step++) {
    const state = read(memory);
    const keys = new Set(['w', 'i']);
    for (let i = 0; i < 2; i++) {
      const ship = state[i], target = state[1 - i];
      let desired = Math.atan2(-(target.x - ship.x), target.y - ship.y) / (2 * Math.PI) * 102944;
      if (desired < 0) desired += 102944;
      const error = ((desired - ship.angle + 154416) % 102944) - 51472;
      if (Math.abs(error) > 1000) keys.add(i === 0 ? (error > 0 ? 'j' : 'l') : (error > 0 ? 'a' : 'd'));
    }
    for (const key of previousKeys) if (!keys.has(key)) await page.keyboard.up(key);
    for (const key of keys) if (!previousKeys.has(key)) await page.keyboard.down(key);
    previousKeys = keys;
    await page.evaluate(() => PDP1Engine.resume());
    await page.waitForTimeout(100);
    await page.evaluate(() => PDP1Engine.stop());
    memory = await page.evaluate(() => PDP1Engine.getMemory(0, 4095));
    const after = read(memory);
    const scores = await page.locator('#score_player_1, #score_player_2').allTextContents();
    const event = { step, approximateInputMilliseconds: 100, heldKeys: [...keys], ships: after, scores };
    if (step === 90) { await capture('exchange.png', step); report.events.push({ kind: 'exchange', ...event }); }
    if (!destroyed && after.some((s, i) => s.routine !== initial[i].routine)) {
      destroyed = true;
      await capture('destruction.png', step);
      report.events.push({ kind: 'destruction', ...event });
    }
    if (destroyed && !inactive && after.some(s => s.routine === 0)) {
      inactive = true;
      report.events.push({ kind: 'inactive', ...event });
    }
    if (inactive && after.every((s, i) => s.routine === initial[i].routine && s.torpedoes <= -30)) {
      completed = true;
      report.events.push({ kind: 'restart-with-replenished-resources', ...event });
      break;
    }
    if (step % 50 === 0) console.log('Encounter step', step);
  }
  for (const key of previousKeys) await page.keyboard.up(key);
  report.completedEncounter = completed;
  fs.writeFileSync(path.join(output, 'capture-report.json'), JSON.stringify(report, null, 2));
  if (!completed || report.captures.length !== 3 || errors.length) throw new Error('Incomplete encounter or capture; inspect report');
  console.log('Captured three frames and verified destruction, inactive state and restart.');
} finally {
  await browser.close();
}
