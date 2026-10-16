/** Verify the complete authored Foundations publication surface, not comprehension. */
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import path from 'node:path';
const [website, sourcePath, out, mode = 'actual'] = process.argv.slice(2);
assert(website && sourcePath && out && ['actual', 'wrong-count'].includes(mode), 'Expected website, source, output and actual/wrong-count');
const require = createRequire(path.resolve(website, 'package.json'));
const {chromium} = require('@playwright/test');
const sourceBytes = await fs.readFile(sourcePath);
const source = JSON.parse(sourceBytes);
assert(source.pages.length === 49 && new Set(source.pages.map(item => item.route)).size === 49, 'Incomplete source surface');
const base = 'https://code198x.com';
await fs.mkdir(out, {recursive: true});
const browser = await chromium.launch({channel: 'chrome', headless: true});
const context = await browser.newContext();
const page = await context.newPage();
page.setDefaultTimeout(15000);
const report = {status: 'running', date: new Date().toISOString(), base, mode, browser: browser.version(),
  sourceSha256: createHash('sha256').update(sourceBytes).digest('hex'), cases: [], links: [], errors: []};
const links = new Map();
page.on('pageerror', error => report.errors.push({route: page.url(), error: String(error)}));
const normal = text => text.replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, ' ').trim();
async function open(details) {
  assert.equal(await details.getAttribute('open'), null, 'Authored answer unexpectedly open');
  const summary = details.locator(':scope > summary');
  await summary.focus();
  await page.keyboard.press('Enter');
  assert.notEqual(await details.getAttribute('open'), null, 'Answer did not open from keyboard');
  assert((await details.innerText()).trim().length > (await summary.innerText()).trim().length, 'Answer has no content');
}
try {
  for (const width of [1440, 390]) {
    await page.setViewportSize({width, height: 900});
    for (const item of source.pages) {
      const response = await page.goto(base + item.route, {timeout: 30000});
      assert(response?.ok(), `HTTP ${response?.status()} ${item.route}`);
      await page.locator('main h1, h1').first().waitFor();
      await page.evaluate(async () => { await document.fonts.ready; });
      assert.equal(await page.locator('h1').count(), 1, 'Expected one page heading');
      assert((await page.locator('main').innerText()).length > 100, 'Main content missing');
      const questions = page.locator('main .question');
      const expectedQuestions = item.questions + (mode === 'wrong-count' && report.cases.length === 0 ? 1 : 0);
      assert.equal(await questions.count(), expectedQuestions, `Question count ${item.route}`);
      const record = {route: item.route, kind: item.kind, width, height: 900, http: response.status(), finalUrl: page.url(),
        responseSha256: createHash('sha256').update(await response.body()).digest('hex'), questionCount: await questions.count(), opened: []};
      for (let index = 0; index < item.questions; index++) {
        const question = questions.nth(index);
        assert((await question.locator('.question-prompt').innerText()).trim().length > 0, 'Empty prediction');
        await open(question.locator(':scope > details'));
        record.opened.push({kind: 'Question', index});
      }
      const details = page.locator('main details');
      const labels = await details.locator(':scope > summary').allInnerTexts();
      for (const label of item.summaries) {
        const matches = labels.map((value, index) => normal(value) === normal(label) ? index : -1).filter(index => index >= 0);
        assert.equal(matches.length, 1, `Missing/ambiguous authored disclosure: ${label}`);
        await open(details.nth(matches[0]));
        record.opened.push({kind: 'details', summary: label});
      }
      record.dimensions = await page.evaluate(() => ({width: innerWidth, document: document.documentElement.scrollWidth}));
      assert(record.dimensions.document <= width, `Document overflow: ${item.route} at ${width}`);
      const hrefs = await page.locator('main a[href]').evaluateAll(items => items.map(item => item.getAttribute('href')));
      for (const href of hrefs) {
        if (!href || (!href.startsWith('/') && !href.startsWith('#')) || href.startsWith('//')) { continue; }
        const url = new URL(href, base + item.route);
        if (!links.has(url.href)) { links.set(url.href, new Set()); }
        links.get(url.href).add(item.route);
      }
      report.cases.push(record);
      console.log(`${report.cases.length}/98 ${width} ${item.route} ${record.opened.length} answers`);
    }
  }
  assert.equal(report.cases.length, 98, 'Incomplete viewport matrix');
  for (const width of [1440, 390]) {
    assert.equal(report.cases.filter(item => item.width === width).length, 49);
  }
  const entries = [...links.entries()];
  assert(entries.length > 49, 'Internal-link collection empty or incomplete');
  // Fetch each target body once; fragments on that body share the response.
  const responses = new Map();
  const targetUrls = [...new Set(entries.map(([href]) => { const url = new URL(href); url.hash = ''; return url.href; }))];
  for (let offset = 0; offset < targetUrls.length; offset += 4) {
    const batch = targetUrls.slice(offset, offset + 4);
    const results = await Promise.allSettled(batch.map(async url => {
      const response = await context.request.get(url, {timeout: 20000});
      const body = await response.body();
      return {http: response.status(), finalUrl: response.url(), contentType: response.headers()['content-type'] || '',
        responseSha256: createHash('sha256').update(body).digest('hex'), body: body.toString('utf8')};
    }));
    results.forEach((result, index) => responses.set(batch[index], result.status === 'fulfilled' ? result.value : {error: String(result.reason)}));
  }
  for (const [href, from] of entries) {
    const url = new URL(href), fragment = decodeURIComponent(url.hash.slice(1));
    url.hash = '';
    const target = responses.get(url.href);
    const record = {href, from: [...from], http: target.http, finalUrl: target.finalUrl,
      responseSha256: target.responseSha256, error: target.error, fragment, fragmentFound: null};
    if (fragment && target.body && target.contentType.includes('text/html')) {
      record.fragmentFound = await page.evaluate(({html, fragment}) => {
        const doc = new DOMParser().parseFromString(html, 'text/html');
        return !!doc.getElementById(fragment) || Array.from(doc.querySelectorAll('a[name]')).some(item => item.getAttribute('name') === fragment);
      }, {html: target.body, fragment});
    }
    record.passed = !record.error && record.http >= 200 && record.http < 300 && record.fragmentFound !== false;
    report.links.push(record);
  }
  assert(report.links.length === entries.length && report.links.every(item => item.passed), 'Broken internal links or missing fragments; inspect results');
  assert.deepEqual(report.errors, [], 'Uncaught page errors');
  report.status = 'passed';
  console.log(`PASS 98 page/viewport cases, ${report.cases.reduce((sum, item) => sum + item.opened.length, 0)} keyboard answer opens, ${report.links.length} internal links`);
} catch (error) {
  report.status = 'failed';
  report.failure = String(error);
  await page.screenshot({path: `${out}/failure.png`, fullPage: true});
  throw error;
} finally {
  await fs.writeFile(`${out}/results.json`, JSON.stringify(report, null, 2) + '\n');
  await browser.close();
}
