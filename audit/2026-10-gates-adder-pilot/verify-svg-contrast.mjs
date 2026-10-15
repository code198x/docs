import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const [base,out]=process.argv.slice(2);
if(!base||!out)throw Error('Expected base and output path');
const browser=await chromium.launch({channel:'chrome',headless:true});
const rows=[];
try {
 const page=await browser.newPage();
 for(const width of [1440,390]) for(const unit of ['unit-01','unit-02','unit-03']) {
  await page.setViewportSize({width,height:900});
  await page.goto(base+'/foundations/gates-and-the-adder/'+unit+'/');
  for(const state of ['initial','all-inputs-on']) {
   if(state==='all-inputs-on') for(const pin of await page.locator('[data-input][role="button"]').all()) if(await pin.getAttribute('aria-pressed')==='false') {await pin.focus();await page.keyboard.press('Enter');}
   await page.evaluate(async()=>{await document.fonts.ready;await Promise.allSettled(document.getAnimations().map(a=>a.finished));});
   const samples=await page.locator('.logic-circuit-svg text').evaluateAll(nodes=>nodes.map(n=>{
    const style=getComputedStyle(n), svg=n.closest('svg');
    let background,kind;
    if(n.classList.contains('lc-pin-value')) {background=getComputedStyle(n.parentElement.querySelector('circle')).fill;kind='pin value on circle';}
    else if(n.classList.contains('lc-gate-name')) {background=getComputedStyle(n.parentElement.querySelector('.lc-shape')).fill;kind='gate name on shape';}
    else {let ancestor=svg;while(ancestor&&(!background||background==='rgba(0, 0, 0, 0)')) {background=getComputedStyle(ancestor).backgroundColor;ancestor=ancestor.parentElement;}kind='pin name on page';}
    return {text:n.textContent.trim(),foreground:style.fill,background,kind};
   }));
   rows.push({width,unit,state,samples});
  }
 }
 const linear=c=>{const x=c/255;return x<=0.04045?x/12.92:((x+0.055)/1.055)**2.4;};
 const lum=s=>{const c=s.match(/[\d.]+/g).map(Number);if(c.length!==3)throw Error('Expected opaque RGB: '+s);return .2126*linear(c[0])+.7152*linear(c[1])+.0722*linear(c[2]);};
 for(const row of rows) for(const sample of row.samples) {const a=lum(sample.foreground),b=lum(sample.background);sample.ratio=Number(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(4));if(sample.ratio<4.5)throw Error('Text contrast below 4.5: '+JSON.stringify(sample));}
 await fs.writeFile(out,JSON.stringify({status:'passed',scope:'Rendered SVG text fills against authored opaque circle, gate shape or inherited page background; initial and all-inputs-on states only. Does not establish all graphical-object boundaries, focus, hit areas or all combinations.',browser:browser.version(),rows},null,2)+'\n');
 console.log(JSON.stringify({cases:rows.length,samples:rows.reduce((s,r)=>s+r.samples.length,0),minimum:Math.min(...rows.flatMap(r=>r.samples.map(s=>s.ratio)))}));
} finally {await browser.close();}
