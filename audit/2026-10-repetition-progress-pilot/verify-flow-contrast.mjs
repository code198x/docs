import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const [base,out]=process.argv.slice(2);
if(!base||!out)throw Error('Expected base and output');
const browser=await chromium.launch({channel:'chrome',headless:true});
try {
 const context=await browser.newContext();const page=await context.newPage();const rows=[];
 for(const width of [1440,390])for(const unit of ['unit-02','unit-03']) {
  await page.setViewportSize({width,height:900});const response=await page.goto(base+'/foundations/repeating/'+unit+'/');if(!response?.ok())throw Error('Flow page HTTP '+response?.status());if(await page.locator('.flow-diagram-svg').count()!==1||await page.locator('.flow-diagram-svg text').count()<3)throw Error('Expected populated flow diagram');
  const samples=await page.locator('.flow-diagram-svg text').evaluateAll(nodes=>nodes.map(n=>{const shape=n.parentElement.querySelector(':scope > rect, :scope > polygon');const background=shape??n.closest('svg').querySelector(':scope > rect');if(!background)throw Error('Missing authored background');let fill=getComputedStyle(background).fill;if(fill==='rgba(0, 0, 0, 0)'){let parent=n.closest('svg');while(parent&&fill==='rgba(0, 0, 0, 0)'){fill=getComputedStyle(parent).backgroundColor;parent=parent.parentElement;}}return {text:n.textContent.trim(),foreground:getComputedStyle(n).fill,background:fill,kind:shape?'step text':'arrow label'};}));
  rows.push({width,unit,samples});
 }
 const lum=s=>{const c=s.match(/[\d.]+/g).map(Number);if(c.length!==3)throw Error('Expected opaque RGB: '+s);const v=c.map(n=>n/255).map(n=>n<=.04045?n/12.92:((n+.055)/1.055)**2.4);return .2126*v[0]+.7152*v[1]+.0722*v[2];};
 if(rows.length!==4||rows.some(row=>row.samples.length<3))throw Error('Missing flow samples');
 let failed=false;for(const row of rows)for(const sample of row.samples){const a=lum(sample.foreground),b=lum(sample.background);sample.ratio=Number(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(4));if(sample.ratio<4.5)failed=true;}
 await fs.writeFile(out,JSON.stringify({status:failed?'findings':'passed',scope:'All flow diagram text at 1440/390 against authored step fills or SVG background. Not graphical strokes or a general accessibility assessment.',rows},null,2)+'\n');console.log(JSON.stringify({samples:rows.reduce((n,r)=>n+r.samples.length,0),minimum:Math.min(...rows.flatMap(r=>r.samples.map(s=>s.ratio))),failed}));
 if(failed)throw Error('Measured flow text contrast below 4.5');
} finally {await browser.close();}
