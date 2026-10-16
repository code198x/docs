/** Bounded independent expectations for the maintained aiming model. */
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import path from 'node:path';
const [samples, out, policy = 'actual'] = process.argv.slice(2);
assert(samples && out && ['actual', 'endpoints', 'line'].includes(policy), 'Expected samples, output and actual/endpoints/line');
const modelPath = path.resolve(samples, 'craft/maths-for-games/aiming/model.mjs');
const model = await import(pathToFileURL(modelPath));
const report = {status: 'running', date: new Date().toISOString(), node: process.version, policy,
  modelSha256: createHash('sha256').update(await fs.readFile(modelPath)).digest('hex'), geometry: [], rounding: [], directions: [], sweep: {}, shots: []};
const a = {x: 0, y: 0}, b = {x: 3, y: 0};
const fixtures = [
  ['between-tick tangent', a, b, {x: 1.5, y: 5}, 25, true],
  ['outside', a, b, {x: 1.5, y: 5.001}, 25.010001, false],
  ['inside', a, b, {x: 1.5, y: 4.999}, 24.990001, true],
  ['beyond finish', a, b, {x: 9, y: 0}, 36, false],
  ['before start', a, b, {x: -6, y: 0}, 36, false],
  ['endpoint tangent', a, b, {x: 8, y: 0}, 25, true],
  ['vertical tangent', a, {x: 0, y: 3}, {x: -5, y: 1.5}, 25, true],
  ['reverse', b, a, {x: 1.5, y: 5}, 25, true],
  ['stationary tangent', {x: 2, y: 3}, {x: 2, y: 3}, {x: 5, y: 7}, 25, true],
  ['stationary outside', {x: 2, y: 3}, {x: 2, y: 3}, {x: 8, y: 3}, 36, false]
];
try {
  assert.equal(model.HIT_RADIUS, 5);
  assert.equal(model.SPEED, 3);
  for (const [name, start, end, target, squared, hit] of fixtures) {
    let distance = model.distanceToSegment(target, start, end);
    if (policy === 'endpoints') { distance = Math.min(Math.hypot(target.x - start.x, target.y - start.y), Math.hypot(target.x - end.x, target.y - end.y)); }
    if (policy === 'line' && end.x !== start.x) { distance = Math.abs(target.y - start.y); }
    report.geometry.push({name, start, end, target, expectedSquared: squared, expectedHit: hit, distance, hit: distance <= model.HIT_RADIUS});
    assert(Math.abs(distance * distance - squared) < 1e-10, `${name}: wrong finite segment distance`);
    assert.equal(distance <= model.HIT_RADIUS, hit, `${name}: wrong contact boundary`);
  }
  for (const [input, expected] of [[-2.5,-3],[-1.5,-2],[-.5,-1],[0,0],[.5,1],[1.5,2],[2.5,3],[-.499,0],[-.501,-1]]) {
    const actual = model.roundSigned(input);
    assert(actual === expected, `Rounding ${input}`);
    report.rounding.push({input, expected, actual, mathRound: Math.round(input)});
  }
  for (const [x,y,expected] of [[1,0,0],[1,1,45],[0,1,90],[-1,1,135],[-1,0,180],[-1,-1,225],[0,-1,270],[1,-1,315],[0,0,null]]) {
    const actual = model.angleTo(x,y);
    assert.equal(actual, expected);
    report.directions.push({x,y,expected,actual});
  }
  let combinations = 0, maximum = 0;
  for (const scale of [4,16,256]) {
    for (let tenth = 0; tenth < 3600; tenth++) {
      const v = model.velocity(tenth / 10, scale);
      for (const [value, stored] of [[v.x * scale,v.ix],[v.y * scale,v.iy]]) {
        assert(Number.isInteger(stored));
        assert(Math.abs(stored - value) <= .5 + 1e-12, 'Not nearest integer');
        if (Math.abs(stored - value) === .5) { assert(Math.abs(stored) >= Math.abs(value), 'Tie rounded towards zero'); }
        assert(Math.abs(stored) <= 32767);
        maximum = Math.max(maximum, Math.abs(stored));
      }
      combinations++;
    }
  }
  assert.equal(combinations, 10800);
  report.sweep = {combinations, maximumStoredComponent: maximum, limits: 'Declared tenths-of-a-degree input grid and three scales; not arbitrary floating-point values.'};
  for (const angle of [32.8,138.4,248.6,90,318.2,180]) {
    const theta = angle * Math.PI / 180;
    const target = {x: 220 * Math.cos(theta), y: 220 * Math.sin(theta)};
    for (const scale of [4,16,256]) {
      const shot = model.simulate(angle,scale,target);
      assert(shot.exactHit);
      if (scale === 256) { assert(shot.fixedHit); }
      let maxPosition = 0;
      assert.equal(shot.fixed.length, shot.count + 1);
      for (let tick = 0; tick <= shot.count; tick++) {
        for (const [axis, velocity] of [['x',shot.velocity.ix],['y',shot.velocity.iy]]) {
          const stored = shot.fixed[tick][axis] * scale;
          assert(stored === tick * velocity, 'Fractional position lost');
          assert(Number.isSafeInteger(stored) && stored >= -2147483648 && stored <= 2147483647);
          maxPosition = Math.max(maxPosition, Math.abs(stored));
        }
      }
      report.shots.push({angle, scale, count: shot.count, referenceHit: shot.exactHit, fixedHit: shot.fixedHit,
        minimumReference: shot.minExact, minimumFixed: shot.minFixed, maximumStoredPosition: maxPosition});
    }
  }
  assert.equal(report.shots.length, 18);
  report.status = 'passed';
  console.log('PASS 10 finite-segment fixtures, 9 rounding cases, 9 directions, 10800 velocities and 18 bounded shots');
} catch (error) {
  report.status = 'failed';
  report.failure = String(error);
  throw error;
} finally {
  await fs.mkdir(path.dirname(out), {recursive: true});
  await fs.writeFile(out, JSON.stringify(report, null, 2) + '\n');
}
