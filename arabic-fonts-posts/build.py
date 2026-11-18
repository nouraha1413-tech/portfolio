# سلايدات بوست تيك توك (1080x1920) — شغّل: python3 build.py
import base64, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
BLUE, DARK = "#1538dc", "#0e289f"
W, H = 1080, 1920

SITES = [
 dict(n="01", name="Alfont", url="alfont.com", tag="مجاني",
      desc="آلاف الخطوط العربية، تكتب النص اللي تبيه وتشوف معاينته بكل الخطوط قبل التحميل."),
 dict(n="02", name="Arbfonts", url="arbfonts.com", tag="مجاني",
      desc="عرب فونتس، من أكبر مواقع الخطوط العربية، فيه أكثر من 12 ألف خط مقسّمة: رقعة، ثلث، ديواني وكوفي."),
 dict(n="03", name="1001 Free Fonts", url="1001freefonts.com", tag="مجاني",
      desc="موقع خطوط عالمي فيه قسم كامل للخطوط العربية. انتبه لرخصة كل خط قبل الاستخدام التجاري."),
 dict(n="04", name="29LT", url="29lt.com", tag="احترافي",
      desc="مسبك خطوط عربي احترافي، خطوطه مصممة بعناية ومعها خط لاتيني متناسق."),
 dict(n="05", name="Adobe Fonts", url="fonts.adobe.com", tag="مع الاشتراك",
      desc="متاح مع اشتراك أدوبي، يتفعّل الخط مباشرة داخل فوتوشوب وإليستريتور."),
 dict(n="06", name="MyFonts", url="myfonts.com", tag="مدفوع",
      desc="من أكبر أسواق الخطوط بالعالم، فيه أكثر من 400 ألف خط منها خطوط عربية احترافية."),
]
TITLE = "أفضل مواقع<br>لتحميل الخطوط<br>العربية"
DECO_FONTS = ["Reem Kufi","Amiri","Aref Ruqaa","Lalezar","El Messiri","Marhey","Rakkas","Changa","Lemonada","Katibeh","Mirza","Jomhuria"]
FONTS = ["Tajawal:wght@400;700;800","Readex Pro:wght@400;600;700"] + DECO_FONTS
GF = "https://fonts.googleapis.com/css2?" + "&".join("family="+f.replace(" ","+") for f in FONTS) + "&display=block"

def img64(rel):
    for e in ("png","jpg","jpeg","webp"):
        p = HERE/f"{rel}.{e}"
        if p.exists(): return f"data:image/{e.replace('jpg','jpeg')};base64,"+base64.b64encode(p.read_bytes()).decode()

BASE = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;overflow:hidden;font-family:'Tajawal',sans-serif;direction:rtl;color:#fff;position:relative;
 background:linear-gradient(170deg,#2a52ff 0%,{BLUE} 38%,{DARK} 100%)}}
.clip{{position:absolute;inset:0;overflow:hidden}}
.orb{{position:absolute;border-radius:50%;filter:blur(120px)}}
.win{{border-radius:24px;overflow:hidden;background:#fff;box-shadow:0 40px 90px rgba(0,0,40,.5);border:1px solid rgba(255,255,255,.35)}}
.bar{{height:54px;background:#eef0f5;display:flex;align-items:center;gap:9px;padding:0 18px;direction:ltr}}
.dot{{width:13px;height:13px;border-radius:50%}}
.urlbox{{flex:1;margin:0 60px;height:30px;border-radius:15px;background:#fff;color:#555;font-family:'Readex Pro';font-size:19px;display:flex;align-items:center;justify-content:center}}
.win img{{width:100%;display:block}}
"""

def page(css, body):
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><link href="{GF}" rel="stylesheet">
<style>{BASE}{css}</style></head><body>{body}</body></html>"""

def window(s, extra=""):
    return f"""<div class="win" {extra}><div class="bar"><span class="dot" style="background:#ff5f57"></span><span class="dot" style="background:#febc2e"></span>
<span class="dot" style="background:#28c840"></span><div class="urlbox">{s['url']}</div></div><img src="{img64('screens/'+s['n'])}"></div>"""

# ---------- صفحات المواقع (المحتوى المهم داخل المنطقة الآمنة لتيك توك) ----------
SITE_CSS = """
.wrap{position:absolute;top:50%;transform:translateY(-50%);left:60px;right:60px;display:flex;flex-direction:column;align-items:center;text-align:center}
.tag{background:#fff;color:#1538dc;font-weight:800;font-size:34px;padding:8px 26px;border-radius:30px}
.num{font-family:'Readex Pro';font-weight:600;font-size:30px;opacity:.7;margin-top:34px;letter-spacing:4px}
h1{font-family:'Readex Pro';font-weight:700;font-size:112px;line-height:1.05;direction:ltr;margin-top:6px}
.line{width:120px;height:9px;border-radius:6px;background:#fff;margin:26px 0 24px}
.desc{font-size:40px;line-height:1.6;max-width:900px;opacity:.95}
.shot{position:relative;width:100%;margin-top:56px}
.shot:before{content:"";position:absolute;inset:10% 12%;background:#4f7dff;filter:blur(90px);opacity:.7;border-radius:50%;z-index:-1}
.url{margin-top:44px;font-family:'Readex Pro';font-size:32px;direction:ltr;background:rgba(255,255,255,.14);border:1.5px solid #fff;padding:12px 38px;border-radius:40px}
.big{position:absolute;bottom:-90px;left:40px;font-family:'Readex Pro';font-weight:700;font-size:520px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.12);direction:ltr}
"""
def site_slide(s):
    return page(SITE_CSS, f"""<div class="clip"><div class="orb" style="width:600px;height:600px;background:#3f6bff;top:-200px;right:-200px;opacity:.6"></div>
<div class="big">{s['n']}</div></div>
<div class="wrap"><span class="tag">{s['tag']}</span><div class="num">{s['n']}</div><h1>{s['name']}</h1><div class="line"></div>
<div class="desc">{s['desc']}</div><div class="shot">{window(s)}</div><div class="url">{s['url']}</div></div>""")

def outro():
    return page("""
.o{position:absolute;top:520px;left:72px;right:72px;text-align:center}
.o h1{font-weight:800;font-size:124px;line-height:1.2}
.o p{font-size:42px;margin-top:36px;opacity:.9;line-height:1.6}
.acts{display:flex;justify-content:center;gap:24px;margin-top:80px}
.acts div{background:#fff;color:#1538dc;font-weight:800;font-size:36px;padding:24px 42px;border-radius:26px}
""", """<div class="clip"><div class="orb" style="width:700px;height:700px;background:#3f6bff;top:-250px;left:-200px;opacity:.6"></div></div>
<div class="o"><h1>أي موقع<br>تستخدمه أنت؟</h1><p>شاركنا في التعليقات 👇<br>وتابع للمزيد من مصادر التصميم</p>
<div class="acts"><div>🔖 احفظ</div><div>↗ شارك</div><div>＋ تابع</div></div></div>""")

# ---------- ثلاث أفكار للغلاف ----------
def cover_a():   # حرف عملاق بالخلفية
    return page("""
.giant{position:absolute;font-family:'Aref Ruqaa';font-size:1500px;line-height:1;color:rgba(255,255,255,.1);top:120px;left:50%;transform:translateX(-50%)}
.ring{position:absolute;border:2px solid rgba(255,255,255,.18);border-radius:50%}
.t{position:absolute;top:640px;left:60px;right:60px;text-align:center}
.t .k{display:inline-block;font-size:34px;font-weight:700;border:2px solid #fff;padding:10px 30px;border-radius:40px;margin-bottom:40px}
.t h1{font-weight:800;font-size:122px;line-height:1.25;text-shadow:0 12px 40px rgba(0,0,50,.35)}
.strip{position:absolute;bottom:470px;left:0;right:0;display:flex;justify-content:center;gap:40px;font-size:90px;opacity:.9}
""", f"""<div class="clip"><div class="orb" style="width:700px;height:700px;background:#4a74ff;top:-200px;right:-200px;opacity:.7"></div>
<div class="orb" style="width:600px;height:600px;background:#081a80;bottom:-150px;left:-150px;opacity:.9"></div>
<div class="giant">خ</div><div class="ring" style="width:900px;height:900px;top:520px;left:90px"></div>
<div class="ring" style="width:1200px;height:1200px;top:370px;left:-60px;opacity:.5"></div></div>
<div class="t"><div class="k">مصادر المصمم</div><h1>{TITLE}</h1></div>
<div class="strip">""" + "".join(f'<span style="font-family:\'{f}\'">ع</span>' for f in ["Amiri","Reem Kufi","Aref Ruqaa","Lalezar","Marhey","Rakkas"]) + "</div>")

def cover_b():   # كولاج شاشات المواقع — مموّه عشان ما يكشف المحتوى
    pos = [(-140,230,-12),(560,170,9),(-80,760,7),(600,820,-8),(-160,1330,-6),(540,1400,10)]
    def blank(s):  # نافذة بدون رابط
        return f"""<div class="win"><div class="bar"><span class="dot" style="background:#ff5f57"></span><span class="dot" style="background:#febc2e"></span>
<span class="dot" style="background:#28c840"></span><div class="urlbox"></div></div><img src="{img64('screens/'+s['n'])}"></div>"""
    cards = "".join(f'<div class="card" style="left:{x}px;top:{y}px;transform:rotate({r}deg)">{blank(s)}</div>' for (x,y,r),s in zip(pos,SITES))
    return page("""
.card{position:absolute;width:680px;filter:blur(9px) saturate(.7);opacity:.75}
.tint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,56,220,.55) 0%,rgba(14,40,159,.35) 40%,rgba(14,40,159,.35) 60%,rgba(10,30,130,.75) 100%)}
.focus{position:absolute;inset:0;background:radial-gradient(70% 34% at 50% 48%,rgba(14,40,159,.96) 0%,rgba(14,40,159,.8) 50%,rgba(14,40,159,0) 100%)}
.t{position:absolute;top:50%;left:60px;right:60px;transform:translateY(-52%);text-align:center}
.t .k{display:inline-block;font-size:32px;font-weight:700;letter-spacing:1px;background:rgba(255,255,255,.14);border:1.5px solid rgba(255,255,255,.6);padding:10px 30px;border-radius:40px}
.t h1{font-weight:800;font-size:128px;line-height:1.22;margin-top:34px;text-shadow:0 14px 40px rgba(0,0,40,.45)}
.t .line{width:140px;height:9px;border-radius:6px;background:#fff;margin:40px auto 30px}
.t .sub{font-size:40px;font-weight:700;opacity:.95}
.swipe{position:absolute;bottom:470px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:16px;background:#fff;color:#1538dc;font-size:34px;font-weight:800;padding:18px 40px;border-radius:50px;box-shadow:0 20px 50px rgba(0,0,40,.35);white-space:nowrap}
""", f"""<div class="clip">{cards}<div class="tint"></div><div class="focus"></div></div>
<div class="t"><div class="k">مصادر المصمم</div><h1>{TITLE}</h1><div class="line"></div><div class="sub">٦ مواقع لازم تحفظها</div></div>
<div class="swipe">اسحب وشوفها ←</div>""")

def cover_c():   # سطور بخطوط مختلفة
    rows = "".join(f'<div class="row" style="font-family:\'{f}\';opacity:{.10 if i%2 else .2}">الخطوط العربية الخطوط العربية</div>' for i,f in enumerate(DECO_FONTS+DECO_FONTS[:3]))
    return page("""
.rows{position:absolute;inset:-40px -300px;display:flex;flex-direction:column;justify-content:space-between;transform:rotate(-8deg)}
.row{font-size:120px;line-height:1.05;white-space:nowrap;text-align:center;color:#fff}
.card{position:absolute;top:560px;left:70px;right:70px;background:#fff;color:#1538dc;border-radius:44px;padding:70px 40px 80px;text-align:center;box-shadow:0 50px 100px rgba(0,0,40,.45)}
.card h1{font-weight:800;font-size:112px;line-height:1.25}
.card .k{display:inline-block;margin-top:34px;background:#1538dc;color:#fff;font-size:34px;font-weight:700;padding:12px 34px;border-radius:40px}
""", f"""<div class="clip"><div class="rows">{rows}</div></div><div class="card"><h1>{TITLE}</h1><div class="k">مجانية واحترافية</div></div>""")

slides = {"slide-01": cover_b()}
for s in SITES: slides[f"slide-{int(s['n'])+1:02}"] = site_slide(s)
slides[f"slide-{len(SITES)+2:02}"] = outro()

out = HERE/"output"
for f in out.glob("*.png"): f.unlink()
for k, h in slides.items(): (out/f"{k}.html").write_text(h, encoding="utf-8")
(out/"_r.js").write_text(f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();
const p=await b.newPage({{viewport:{{width:{W},height:{H}}},deviceScaleFactor:2}});
for(const f of process.argv.slice(2)){{await p.goto('file://'+f,{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);
await p.waitForTimeout(400);await p.screenshot({{path:f.replace('.html','.png')}});}}await b.close();}})();""")
subprocess.run(["node", str(out/"_r.js")] + [str((out/f"{k}.html").resolve()) for k in slides], check=True)
for f in out.glob("*.html"): f.unlink()
(out/"_r.js").unlink()
print("done", len(slides))
