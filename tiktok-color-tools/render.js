// Renders <dir>/*.html to 1080x1920 PNGs. Usage: node render.js [slides|slides-brand]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.join(__dirname, process.argv[2] || 'slides');
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(dir, f.replace('.html', '.png')) });
    console.log('rendered', f);
  }
  await browser.close();
})();
