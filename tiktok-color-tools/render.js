// Renders <dir>/*.html to 9:16 PNGs (1080x1920 layout).
// Usage: node render.js [slides|slides-brand] [scale]
//   scale 1 -> 1080x1920, scale 2 -> 2160x3840 written to <dir>-hd/
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const name = process.argv[2] || 'slides';
  const scale = Number(process.argv[3] || 1);
  const dir = path.join(__dirname, name);
  const out = scale > 1 ? path.join(__dirname, name + '-hd') : dir;
  fs.mkdirSync(out, { recursive: true });
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: scale });
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
    console.log('rendered', f);
  }
  await browser.close();
})();
