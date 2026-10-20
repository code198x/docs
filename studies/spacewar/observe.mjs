// Bounded external-implementation observations; no new project dependency.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
const args = process.argv.slice(2);
if (args.length !== 4 || args[0] !== '--website' || args[2] !== '--output-dir') {
  throw new Error('Usage: node studies/spacewar/observe.mjs --website ../website --output-dir /tmp/spacewar-review');
}
const requireWebsite = createRequire(path.resolve(args[1], 'package.json'));
const { chromium } = requireWebsite('@playwright/test');
const output = path.resolve(args[3]);
fs.mkdirSync(output, { recursive: true });

const hash=data=>crypto.createHash('sha256').update(data).digest('hex');
(async()=>{const b=await chromium.launch();const report={referenceEdition:'Spacewar! 3.1, 24 Sep 62',url:'https://www.masswerk.at/spacewar/',method:'Automated keyboard inputs in Chromium; browser implementation, not PDP-1 hardware or a human two-player trial.',browser:await b.version(),responses:[],cases:[]};try{
for(const scenario of ['baseline','thrust-release','rotate','fire','hyperspace']){const p=await b.newPage({viewport:{width:1440,height:1050}});p.setDefaultTimeout(45000);const errors=[];p.on('pageerror',e=>errors.push(e.message));const requests=[];p.on('response',r=>{if(/spacewar_pdp1_engine_ng\.js|spacewar_3_1\.js/.test(r.url()))requests.push(r)});await p.goto(report.url,{waitUntil:'networkidle'});await p.selectOption('#spacewarCodeSelect','spacewar3.1');await p.keyboard.press('Space');await p.waitForTimeout(100);await p.evaluate(()=>PDP1Engine.stop());const initial=await p.evaluate(()=>({configuration:PDP1Engine.getConfiguration(),parameters:PDP1Engine.getParams(),canvas:{width:document.querySelector('canvas').width,height:document.querySelector('canvas').height},memory:PDP1Engine.getMemory(0,4095)}));if(initial.configuration.id!=='spacewar3.1')throw Error('Wrong edition');const actions=[];
async function advance(ms){await p.evaluate(()=>PDP1Engine.resume());await p.waitForTimeout(ms);await p.evaluate(()=>PDP1Engine.stop())}
if(scenario==='baseline'){await advance(400);actions.push({noInputMilliseconds:400})}
else{const key={ 'thrust-release':'s',rotate:'d',fire:'w',hyperspace:'q'}[scenario];await p.keyboard.down(key);await advance(400);await p.keyboard.up(key);actions.push({held:key,approximateBrowserMilliseconds:400});await p.screenshot({path:path.join(output, `${scenario}-held.png`)});await advance(400);actions.push({released:key,approximateBrowserMilliseconds:400})}
const final=await p.evaluate(()=>({configuration:PDP1Engine.getConfiguration(),memory:PDP1Engine.getMemory(0,4095)}));const changed=initial.memory.reduce((n,v,i)=>n+(v!==final.memory[i]),0);if(changed===0)throw Error('No executed memory changes');await p.screenshot({path:path.join(output, `${scenario}-final.png`)});report.cases.push({scenario,actions,configuration:initial.configuration,parameters:initial.parameters,canvas:initial.canvas,memoryWordsChanged:changed,memoryBeforeSha256:hash(JSON.stringify(initial.memory)),memoryAfterSha256:hash(JSON.stringify(final.memory)),errors,limitations:'Wall-clock intervals are approximate. Memory changes establish execution, not a particular physical rule or player experience.'});
if(scenario==='baseline')for(const response of requests){const bytes=await response.body();report.responses.push({url:response.url(),bytes:bytes.length,sha256:hash(bytes)})}
await p.close();}
if (report.responses.length !== 2 || report.responses.some(r => r.bytes === 0)) throw Error('Missing or empty implementation response');
fs.writeFileSync(path.join(output, 'observations-raw.json'),JSON.stringify(report,null,2));console.log(report.cases.map(({scenario,memoryWordsChanged,configuration,errors})=>({scenario,memoryWordsChanged,configuration,errors})));if(report.cases.some(c=>c.errors.length))process.exitCode=1;
}finally{await b.close()}})();
