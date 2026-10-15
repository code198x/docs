import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
const [base,out]=process.argv.slice(2);
if(!base||!out)throw Error('Expected base and output path');
const browser=await chromium.launch({channel:'chrome',headless:true});
try {
 const context=await browser.newContext({viewport:{width:390,height:900}});const page=await context.newPage();await page.goto(base+'/foundations/basics/unit-05/');
 const node=page.locator('.ll-line:nth-child(1) > .ll-text');if(await node.count()!==1)throw Error('Expected one source line');await node.scrollIntoViewIfNeeded();const scroller=node.locator('xpath=ancestor::*[@data-ll-scroll]');const rows=[];
 for(const position of ['left','right']) {
  await scroller.evaluate((e,p)=>{e.scrollLeft=p==='left'?0:e.scrollWidth;},position);
  rows.push(await node.evaluate(n=>{let p=n,background='rgba(0, 0, 0, 0)';while(p&&background==='rgba(0, 0, 0, 0)'){background=getComputedStyle(p).backgroundColor;p=p.parentElement;}return {text:n.textContent,foreground:getComputedStyle(n).color,background,scrollLeft:n.closest('[data-ll-scroll]').scrollLeft};}));
 }
 const lum=s=>{const c=s.match(/[\d.]+/g).map(Number);if(c.length!==3)throw Error('Expected opaque RGB');const v=c.map(n=>n/255).map(n=>n<=.04045?n/12.92:((n+.055)/1.055)**2.4);return .2126*v[0]+.7152*v[1]+.0722*v[2];};
 for(const row of rows){const a=lum(row.foreground),b=lum(row.background);row.ratio=Number(((Math.max(a,b)+.05)/(Math.min(a,b)+.05)).toFixed(4));if(row.ratio<4.5)throw Error('Low text contrast');}
 if(rows.length!==2||!rows.some(r=>r.scrollLeft>0))throw Error('Horizontal scroll not observed');await fs.writeFile(out,JSON.stringify({status:'passed',scope:'One axe-incomplete source line at 390, rendered text colour against inherited listing background, both horizontal scroll endpoints. Not a general accessibility assessment.',rows},null,2)+'\n');console.log(JSON.stringify({samples:rows.length,minimum:Math.min(...rows.map(r=>r.ratio))}));
} finally {await browser.close();}
