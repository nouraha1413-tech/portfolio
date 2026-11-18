# يولّد سلايدات البوست (1080x1350) كـ HTML ثم يحولها لصور PNG
# ضع صور الشاشات في screens/01.png ... والشعار في logo.png ثم شغّل: python3 build.py
import os, json, subprocess, base64, pathlib
HERE = pathlib.Path(__file__).parent
BLUE, DARK = "#1538dc", "#0e289f"

SITES = [
 dict(n="01", acc="#1ff79a", ink="#06331f", lay="bottom", name="Alfont", url="alfont.com", tag="مجاني",
      desc="آلاف الخطوط العربية، تكتب النص اللي تبيه وتشوف معاينته بكل الخطوط قبل التحميل.", fonts=[]),
 dict(n="02", acc="#e0458f", ink="#fff", lay="top", name="Arbfonts", url="arbfonts.com", tag="مجاني",
      desc="عرب فونتس، من أكبر مواقع الخطوط العربية، فيه أكثر من 12 ألف خط مقسّمة: رقعة، ثلث، ديواني وكوفي.", fonts=[]),
 dict(n="03", acc="#ffffff", ink="#111", lay="bottom", name="1001 Free Fonts", url="1001freefonts.com", tag="مجاني",
      desc="موقع خطوط عالمي فيه قسم كامل للخطوط العربية. انتبه لرخصة كل خط قبل الاستخدام التجاري.", fonts=[]),
 dict(n="04", acc="#ff4b55", ink="#fff", lay="bottom", name="29LT", url="29lt.com", tag="احترافي",
      desc="مسبك خطوط عربي احترافي، خطوطه مصممة بعناية ومعها خط لاتيني متناسق.", fonts=[]),
 dict(n="05", acc="#ff3b2f", ink="#fff", lay="top", name="Adobe Fonts", url="fonts.adobe.com", tag="مع الاشتراك",
      desc="متاح مع اشتراك أدوبي، يتفعّل الخط مباشرة داخل فوتوشوب وإليستريتور.", fonts=[]),
 dict(n="06", acc="#7fb2ff", ink="#08245c", lay="bottom", name="MyFonts", url="myfonts.com", tag="مدفوع",
      desc="من أكبر أسواق الخطوط بالعالم، فيه أكثر من 400 ألف خط منها خطوط عربية احترافية.", fonts=[]),
]
SAMPLE = "تصميم مميز"

ALL_FONTS = ["Tajawal","Readex Pro"]
gf = "https://fonts.googleapis.com/css2?" + "&".join(
    "family="+f.replace(" ","+")+(":wght@400;700;800" if f in ("Tajawal",) else "") for f in ALL_FONTS) + "&display=block"

def img64(p):
    p = HERE/p
    if not p.exists(): return None
    ext = p.suffix[1:].replace("jpg","jpeg")
    return f"data:image/{ext};base64,"+base64.b64encode(p.read_bytes()).decode()

def find(base):
    for e in ("png","jpg","jpeg","webp"):
        if (HERE/f"{base}.{e}").exists(): return img64(f"{base}.{e}")
LOGO = find("logo")

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:'Tajawal',sans-serif;direction:rtl;color:#fff;
 background:radial-gradient(120% 80% at 80% 0%,#2a52ff 0%,{BLUE} 40%,{DARK} 100%);position:relative}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);
 background-size:60px 60px;mask-image:linear-gradient(to bottom,#000 0%,transparent 75%)}}
.top{{position:absolute;top:56px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center}}
.logo{{height:84px;max-width:260px;object-fit:contain}}
.logo-ph{{height:84px;padding:0 26px;border:2px dashed rgba(255,255,255,.5);border-radius:18px;display:flex;align-items:center;font-size:26px;opacity:.8}}
.count{{font-family:'Readex Pro';font-size:26px;padding:10px 24px;border-radius:40px;background:rgba(255,255,255,.14);direction:ltr}}
.big{{position:absolute;font-family:'Readex Pro';font-weight:700;font-size:420px;line-height:1;left:40px;top:120px;
 color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.14);direction:ltr}}
.head{{position:absolute;top:200px;right:72px;left:72px}}
.tag{{display:inline-block;background:#fff;color:{BLUE};font-weight:800;font-size:26px;padding:8px 22px;border-radius:30px;margin-bottom:22px}}
h1{{font-family:'Readex Pro';font-weight:700;font-size:92px;line-height:1.05;direction:ltr;text-align:right}}
h2{{font-weight:700;font-size:40px;opacity:.85;margin-top:8px}}
.desc{{font-size:34px;line-height:1.6;margin-top:22px;max-width:900px;opacity:.95}}
/* browser window */
.area{{position:absolute;top:470px;bottom:140px;left:40px;right:40px;display:flex;align-items:center}}
.win{{width:100%;max-height:100%;border-radius:22px;overflow:hidden;background:#fff;display:flex;flex-direction:column;box-shadow:0 40px 90px rgba(0,0,40,.5);border:1px solid rgba(255,255,255,.35)}}
.win img.shot{{width:100%;display:block;min-height:0;object-fit:cover;object-position:top}}
.laptop{{position:absolute;left:50%;transform:translateX(-50%);bottom:150px;width:960px}}
.lid{{background:#0b0f1a;border-radius:28px 28px 0 0;padding:22px 22px 30px;box-shadow:0 40px 80px rgba(0,0,30,.45);border:2px solid #2b3245}}
.cam{{width:10px;height:10px;border-radius:50%;background:#2b3245;margin:-12px auto 10px}}
.screen{{height:520px;border-radius:6px;overflow:hidden;background:#fff;display:flex;flex-direction:column}}
.screen img.shot{{width:100%;height:100%;object-fit:cover;object-position:top}}
.base{{height:26px;background:linear-gradient(#d7dbe6,#9aa1b3);border-radius:0 0 30px 30px;margin:0 -50px;position:relative}}
.base:before{{content:"";position:absolute;top:0;left:50%;transform:translateX(-50%);width:160px;height:10px;background:#8a90a2;border-radius:0 0 12px 12px}}
.bar{{height:52px;background:#eef0f5;display:flex;align-items:center;gap:8px;padding:0 16px;direction:ltr;flex:none}}
.dot{{width:12px;height:12px;border-radius:50%}}
.urlbox{{flex:1;margin:0 60px;height:26px;border-radius:14px;background:#fff;color:#555;font-family:'Readex Pro';font-size:18px;display:flex;align-items:center;justify-content:center}}
.page{{flex:1;padding:26px 30px;color:#111;background:#fafbff}}
.ph{{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}}
.ph b{{font-family:'Readex Pro';font-size:26px;color:{BLUE};direction:ltr}}
.search{{width:380px;height:40px;border:1.5px solid #d5d9e5;border-radius:20px;font-size:18px;color:#888;display:flex;align-items:center;padding:0 14px}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.card{{background:#fff;border:1px solid #e3e6ef;border-radius:12px;padding:12px 14px;height:250px;display:flex;flex-direction:column;justify-content:space-between}}
.card small{{font-family:'Readex Pro';font-size:15px;color:#7a8099;direction:ltr;text-align:left}}
.card p{{font-size:52px;line-height:1.35;color:#111}}
.url{{position:absolute;bottom:58px;left:50%;transform:translateX(-50%);font-family:'Readex Pro';font-size:30px;direction:ltr;
 background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);padding:12px 34px;border-radius:40px;white-space:nowrap}}
"""

def shell(inner, idx, total):
    logo = f'<img class="logo" src="{LOGO}">' if LOGO else '<div></div>'
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<link href="{gf}" rel="stylesheet"><style>{CSS}{LAYOUT_CSS}</style></head><body><div class="grid"></div>
<div class="top">{logo}<div class="count">{idx} / {total}</div></div>{inner}</body></html>"""

def screen(s):
    shot = find(f"screens/{s['n']}")
    SHOT = f'<img class="shot" src="{shot}">' if shot else None
    bar = f"""<div class="bar"><span class="dot" style="background:#ff5f57"></span><span class="dot" style="background:#febc2e"></span>
<span class="dot" style="background:#28c840"></span><div class="urlbox">{s['url']}</div></div>"""
    if SHOT: return bar + SHOT
    cards = "".join(f'<div class="card"><small>{f}</small><p style="font-family:\'{f}\'">{SAMPLE}</p></div>' for f in s["fonts"])
    return bar + f"""<div class="page"><div class="ph"><b>{s['name']}</b><div class="search">ابحث عن خط...</div></div><div class="cards">{cards}</div></div>"""

LAYOUT_CSS = f"""
.L-bottom .area{{top:500px;bottom:150px;left:60px;right:60px}}
.L-bleed-r .area{{top:500px;bottom:150px;left:80px;right:-140px}}
.L-bleed-r .win{{border-radius:22px 0 0 22px}}
.L-bleed-l .area{{top:500px;bottom:150px;left:-140px;right:80px}}
.L-bleed-l .win{{border-radius:0 22px 22px 0}}
.L-top .area{{top:150px;height:640px;left:60px;right:60px;align-items:flex-end}}
.L-top .head{{top:auto;bottom:150px}}
.L-top .big{{top:auto;bottom:250px;left:40px;font-size:300px;opacity:.7}}
.L-top .url{{left:72px;transform:none}}
.L-tilt .area{{top:520px;bottom:160px;left:110px;right:110px}}
.L-tilt .win{{transform:rotate(-3deg)}}
.L-tilt .ghost{{position:absolute;inset:30px 10px;border-radius:22px;transform:rotate(4deg);opacity:.25}}
.area:before{{content:"";position:absolute;inset:10% 15%;filter:blur(90px);opacity:.55;background:var(--acc);border-radius:50%;z-index:-1}}
.area{{isolation:isolate}}
.tag{{background:var(--acc)!important;color:var(--ink)!important}}
h1:after{{content:"";display:block;width:120px;height:10px;border-radius:6px;background:var(--acc);margin:22px 0 0 auto}}
.url{{border-color:var(--acc)!important}}
"""

def site_slide(s, i, t):
    ghost = '<div class="ghost" style="background:var(--acc)"></div>' if s['lay']=="tilt" else ""
    return shell(f"""<style>body{{--acc:{s["acc"]};--ink:{s["ink"]}}}</style><div class="L-{s['lay']}" style="position:absolute;inset:0;overflow:hidden">
<div class="big">{s['n']}</div>
<div class="head"><span class="tag">{s['tag']}</span><h1>{s['name']}</h1><div class="desc">{s['desc']}</div></div>
<div class="area">{ghost}<div class="win">{screen(s)}</div></div>
<div class="url">{s['url']}</div></div>""", i, t)

def cover(t):
    names = "".join(f'<li><span>{s["n"]}</span>{s["name"]}</li>' for s in SITES)
    return shell(f"""<style>
.c{{position:absolute;top:230px;right:72px;left:72px}}
.c .k{{font-size:40px;font-weight:700;opacity:.85}}
.c h1{{font-family:'Tajawal';font-weight:800;font-size:122px;line-height:1.2;direction:rtl;text-align:right;margin-top:10px}}
.c ul{{list-style:none;margin-top:50px;display:grid;gap:22px;direction:rtl}}
.c li{{font-family:'Readex Pro';font-size:36px;display:flex;gap:18px;align-items:center;direction:ltr;justify-content:flex-end}}
.c li span{{font-size:26px;background:#fff;color:{BLUE};border-radius:50%;width:54px;height:54px;display:flex;align-items:center;justify-content:center;font-weight:700}}
.save{{position:absolute;bottom:70px;right:72px;font-size:34px;font-weight:700;display:flex;gap:14px;align-items:center}}
.swipe{{position:absolute;bottom:70px;left:72px;font-size:30px;opacity:.85}}
</style><div class="c"><div class="k">٦ مواقع لازم تعرفها</div><h1>أفضل مواقع<br>الخطوط العربية</h1><ul>{names}</ul></div>
<div class="save">🔖 احفظ البوست لشغلك الجاي</div><div class="swipe">اسحب ←</div>""", 1, t)

def outro(t):
    return shell(f"""<style>
.o{{position:absolute;top:50%;left:72px;right:72px;transform:translateY(-50%);text-align:center}}
.o h1{{font-family:'Tajawal';font-weight:800;font-size:110px;direction:rtl;text-align:center;line-height:1.2}}
.o p{{font-size:40px;margin-top:30px;opacity:.9;line-height:1.6}}
.acts{{display:flex;justify-content:center;gap:24px;margin-top:70px}}
.acts div{{background:#fff;color:{BLUE};font-weight:800;font-size:34px;padding:22px 40px;border-radius:24px}}
</style><div class="o"><h1>أي موقع<br>تستخدمه أنت؟</h1><p>شاركنا في التعليقات 👇<br>وتابع للمزيد من مصادر التصميم</p>
<div class="acts"><div>🔖 احفظ</div><div>↗ شارك</div><div>＋ تابع</div></div></div>""", t, t)

total = len(SITES)+2
slides = [cover(total)] + [site_slide(s, i+2, total) for i, s in enumerate(SITES)] + [outro(total)]
out = HERE/"output"; out.mkdir(exist_ok=True)
for i, h in enumerate(slides, 1): (out/f"slide-{i:02}.html").write_text(h, encoding="utf-8")

js = """
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
for(const f of process.argv.slice(2)){await p.goto('file://'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:f.replace('.html','.png')});}await b.close();})();"""
(out/"_r.js").write_text(js)
subprocess.run(["node", str(out/"_r.js")] + [str((out/f"slide-{i:02}.html").resolve()) for i in range(1, total+1)], check=True)
for f in out.glob("*.html"): f.unlink()
(out/"_r.js").unlink()
print("done", total)
