import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const [base,out]=process.argv.slice(2);
if(!base||!out)throw Error('Expected base and output path');
const browser=await chromium.launch({channel:'chrome',headless:true});
try {
 const context=await browser.newContext({viewport:{width:390,height:900}});const page=await context.newPage();
 await page.goto(base+'/foundations/repeating/unit-02/');
 const rows=[];
 for(const line of [2,3]) {
  const nodes=page.locator(line===2?'[data-label="Code, listing 2 of 3"] .ll-line:nth-child(2) > .ll-text':'[data-label="Code, listing 3 of 3"] .ll-line:nth-child(3) > .ll-text');
  for(const node of await nodes.all()) {
   await node.scrollIntoViewIfNeeded();
   const scroller=node.locator('xpath=ancestor::*[@data-ll-scroll]');
   for(const position of ['left','right']) {
    await scroller.evaluate((e,p)=>{e.scrollLeft=p==='left'?0:e.scrollWidth;},position);
    const sample=await node.evaluate(n=>{let p=n,background='rgba(0, 0, 0, 0)';while(p&&background==='rgba(0, 0, 0, 0)'){background=getComputedStyle(p).backgroundColor;p=p.parentElement;}return {text:n.textContent,foreground:getComputedStyle(n).color,background,scrollLeft:n.closest('[data-ll-scroll]').scrollLeft};});
    rows.push({line,position,...sample});
   }
  }
 }
 const lum=s=>{const c=s.match(/[\d.]+/g).map(Number);if(c.length!==3)throw Error('Expected opaque RGB');const v=c.map(n=>n/255).map(n=>n<=.04045?n/12.92:((n+.055)/1.055)**2.4);return .2126*v[0]+.7152*v[1]+.0722*v[2];};
 for(const r of rows){const a=lum(r.foreground),b=lum(r.background);r.ratio=Number(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(4));if(r.ratio<4.5)throw Error('Contrast below 4.5');}
 if(rows.length!==4||!rows.some(r=>r.scrollLeft>0))throw Error('Expected two source lines and actual horizontal scroll');
 await fs.writeFile(out,JSON.stringify({status:'passed',scope:'Two axe-incomplete source lines at 390, rendered colours against inherited listing background, left/right horizontal scroll. Not a general accessibility pass.',rows},null,2)+'\n');
 console.log(JSON.stringify({samples:rows.length,minimum:Math.min(...rows.map(r=>r.ratio))}));
} finally {await browser.close();}
