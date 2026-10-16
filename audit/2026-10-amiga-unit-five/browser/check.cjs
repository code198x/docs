const path = require('node:path');
const website = path.resolve(process.argv[2]);
const baseUrl = process.argv[3];
const output = path.resolve(process.argv[4]);
const {createRequire} = require('node:module');
const {chromium, expect} = createRequire(path.join(website, 'package.json'))('@playwright/test');
const fs = require('node:fs');
(async () => {
 const browser = await chromium.launch({headless: true, channel: 'chrome'});
 const out = [];
 try {
  for (const viewport of [{width:390,height:844},{width:1440,height:900}]) {
   const page = await browser.newPage({viewport});
   for (const track of ['amos','blitz']) {
    const route = `/systems/commodore-amiga/${track}/meet-${track}/unit-05/`;
    await page.goto(baseUrl+route);
    await page.locator('main').waitFor();
    const questions = page.locator('[data-question]');
    await expect(questions).toHaveCount(3);
    await expect(page.locator('html')).toHaveJSProperty('scrollWidth',viewport.width);
    await page.screenshot({path:`${output}/${track}-${viewport.width}-top.png`});
    for (let i=0;i<3;i++) {
     const details=questions.nth(i).locator('details');
     const summary=details.locator('summary');
     await summary.focus();
     await page.keyboard.press('Enter');
     await expect(details).toHaveAttribute('open','');
     await expect(details.locator('.question-answer')).toBeVisible();
     await page.screenshot({path:`${output}/${track}-${viewport.width}-q${i}.png`});
     await page.keyboard.press('Enter');
     await expect(details).not.toHaveAttribute('open','');
    }
    let media = null;
    if(track==='blitz') {
     const video=page.locator('video');
     await video.scrollIntoViewIfNeeded();
     media=await video.evaluate(async el => {
      el.muted=true;
      await el.play();
      const start=el.currentTime;
      await new Promise(resolve => setTimeout(resolve,1000));
      const end=el.currentTime;
      el.pause();
      return {start,end,width:el.videoWidth,height:el.videoHeight,error:el.error?.message??null};
     });
     if(!(media.end>media.start && media.width>0 && !media.error)) throw new Error('Video did not advance');
     await page.screenshot({path:`${output}/${track}-${viewport.width}-video.png`});
    }
    out.push({route,viewport,questions:'keyboard open/close pass',horizontalOverflow:false,media});
   }
   await page.close();
  }
  fs.writeFileSync(path.join(output, 'results.json'),JSON.stringify(out,null,2)+'\n');
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
