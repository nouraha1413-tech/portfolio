"""Generate TikTok slides (1080x1920) for 5 color tools, then render them to PNG.

Usage: python3 build.py && node render.js
Outputs: slides/*.html and slides/*.png
"""
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "slides"
OUT.mkdir(exist_ok=True)

TOOLS = [
    {
        "slug": "01-adobe-color",
        "name": "Adobe Color",
        "url": "color.adobe.com",
        "img": "adobe-color.jpg",
        "line": "لإنشاء لوحات لونية وفق قواعد تناغم الألوان.",
        "desc": "اختاروا لونًا أساسيًا، طبّقوا قاعدة تناغم، وتطلع لكم لوحة متوازنة فورًا.",
        "chips": ["عجلة الألوان", "ألوان من صورة", "فحص التباين"],
        "tip": "ارفعوا صورة من تبويب Image وخذوا ألوانها مباشرة",
        "accent": "#E5402B", "bg": "#FBF1EC", "ink": "#2A0F0A",
        "swatches": ["#BFDA4B", "#8C8A2E", "#3F8F2F", "#8A2216", "#6E2A7E"],
    },
    {
        "slug": "02-coolors",
        "name": "Coolors",
        "url": "coolors.co",
        "img": "coolors.jpg",
        "line": "لتوليد مجموعات لونية متناسقة بسرعة.",
        "desc": "كل ضغطة تعطيكم لوحة جديدة، ثبّتوا اللون اللي يعجبكم وكمّلوا التوليد.",
        "chips": ["توليد سريع", "تثبيت الألوان", "+10M لوحة"],
        "tip": "اضغطوا زر المسافة (Space) لتوليد لوحة جديدة",
        "accent": "#3B63E3", "bg": "#EEF2FD", "ink": "#0B1640",
        "swatches": ["#0B24C9", "#4C95F5", "#A8D3FB", "#F7EE4E", "#F3C343"],
    },
    {
        "slug": "03-huemint",
        "name": "Huemint",
        "url": "huemint.com",
        "img": "huemint.jpg",
        "line": "لاقتراح الألوان ومعاينتها على التصاميم.",
        "desc": "يقترح ألوانًا بالذكاء الاصطناعي ويعرضها على تصميم حقيقي قبل ما تعتمدونها.",
        "chips": ["ذكاء اصطناعي", "معاينة مباشرة", "شعار وموقع"],
        "tip": "اضغطوا Generate وشوفوا الألوان على التصميم مباشرة",
        "accent": "#3E6DAE", "bg": "#E9F4F8", "ink": "#2B0C0D",
        "swatches": ["#70BCD5", "#2B0C0D", "#3E6DAE", "#C1D0E0", "#FFFFFF"],
    },
    {
        "slug": "04-color-hunt",
        "name": "Color Hunt",
        "url": "colorhunt.co",
        "img": "color-hunt.jpg",
        "line": "لاستكشاف مجموعات لونية جاهزة.",
        "desc": "آلاف اللوحات الجاهزة من مصممين، فرّزوها بالأحدث أو الأشهر واحفظوا المفضّلة.",
        "chips": ["الأحدث", "الأشهر", "عشوائي", "مجموعتي"],
        "tip": "اضغطوا على أي لون لنسخ كوده فورًا",
        "accent": "#6F8A2E", "bg": "#FBF6E4", "ink": "#2C3312",
        "swatches": ["#EAC054", "#E8D975", "#7C9637", "#5F7434", "#EC6838"],
    },
    {
        "slug": "05-paletton",
        "name": "Paletton",
        "url": "paletton.com",
        "img": "paletton.jpg",
        "line": "لتنسيق الألوان باستخدام عجلة الألوان.",
        "desc": "حرّكوا النقطة على العجلة واختاروا نوع التنسيق، ويعطيكم درجات كل لون.",
        "chips": ["أحادي", "متجاور", "ثلاثي", "رباعي"],
        "tip": "اكتبوا كود لونكم في خانة Base RGB وابدأوا منه",
        "accent": "#C9A23F", "bg": "#1E1E1E", "ink": "#F4EEDF", "dark": True,
        "swatches": ["#AA3939", "#E8432E", "#F2C53D", "#5BC236", "#3A2DB0"],
    },
]

FONT = (ROOT / "fonts" / "cairo-arabic.woff2").resolve().as_uri()

BASE_CSS = f"""
@font-face {{ font-family: 'Cairo'; src: url('{FONT}') format('woff2'); font-weight: 200 1000; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; }}
body {{ font-family: 'Cairo', 'Inter', sans-serif; direction: rtl; position: relative; }}
.latin {{ font-family: 'Inter Display', 'Inter', sans-serif; direction: ltr; unicode-bidi: isolate; }}
"""


def tool_html(t, i, total):
    dark = t.get("dark", False)
    muted = "rgba(244,238,223,.72)" if dark else "rgba(0,0,0,.62)"
    card = "#2B2B2B" if dark else "#FFFFFF"
    line_border = "rgba(255,255,255,.12)" if dark else "rgba(0,0,0,.08)"
    chips = "".join(f'<span class="chip">{c}</span>' for c in t["chips"])
    sw = "".join(f'<i style="background:{c}"></i>' for c in t["swatches"])
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8">
<title>{t['name']}</title><style>{BASE_CSS}
body {{ background: {t['bg']}; color: {t['ink']}; }}
.blob {{ position:absolute; border-radius:50%; filter: blur(2px); }}
.b1 {{ width:760px; height:760px; left:-260px; top:1020px; background:{t['accent']}; opacity:{.22 if dark else .16}; }}
.b2 {{ width:420px; height:420px; right:-160px; top:-120px; background:{t['swatches'][0]}; opacity:{.25 if dark else .35}; }}
.top {{ position:absolute; top:150px; right:80px; left:80px; display:flex; justify-content:space-between; align-items:center; }}
.tag {{ font-size:30px; font-weight:700; padding:10px 28px; border-radius:999px; background:{t['ink']}; color:{t['bg']}; }}
.count {{ font-size:34px; font-weight:800; color:{muted}; }}
.head {{ position:absolute; top:250px; right:80px; left:80px; }}
.num {{ font-size:150px; line-height:1; font-weight:900; color:transparent; -webkit-text-stroke:4px {t['accent']}; }}
.name {{ font-size:118px; font-weight:900; line-height:1; letter-spacing:-3px; margin-top:-10px; text-align:right; }}
.url {{ font-size:32px; font-weight:600; color:{t['accent']}; margin-top:14px; text-align:right; }}
.line {{ font-size:54px; font-weight:900; line-height:1.35; margin-top:26px; }}
.desc {{ font-size:36px; font-weight:500; line-height:1.6; margin-top:12px; color:{muted}; max-width:900px; }}
.chips {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:26px; }}
.chip {{ font-size:30px; font-weight:700; padding:8px 26px; border-radius:999px; border:3px solid {t['accent']}; color:{t['ink']}; background:{card}; }}
.phone {{ position:absolute; left:50%; top:850px; width:560px; height:1100px; margin-left:-280px;
  background:#0E0E10; border-radius:72px; padding:16px; box-shadow: 0 40px 90px rgba(0,0,0,.35), 0 0 0 2px {line_border}; transform: rotate(-3deg); }}
.screen {{ width:100%; height:100%; border-radius:58px; overflow:hidden; background:#fff; position:relative; }}
.screen img {{ width:100%; height:100%; object-fit:cover; object-position:top; display:block; }}
.notch {{ position:absolute; top:14px; left:50%; width:150px; height:38px; margin-left:-75px; background:#0E0E10; border-radius:20px; z-index:2; }}
.sw {{ position:absolute; left:70px; top:930px; display:flex; flex-direction:column; gap:16px; }}
.sw i {{ width:74px; height:74px; border-radius:50%; display:block; box-shadow:0 8px 20px rgba(0,0,0,.18), inset 0 0 0 3px rgba(255,255,255,.55); }}
.tip {{ position:absolute; right:80px; top:1300px; width:480px; background:{t['accent']}; color:#fff; border-radius:34px; padding:26px 32px;
  font-size:31px; font-weight:700; line-height:1.5; box-shadow:0 24px 50px rgba(0,0,0,.25); transform: rotate(2deg); }}
.tip b {{ display:block; font-size:26px; font-weight:900; opacity:.85; margin-bottom:4px; }}
</style></head><body>
<div class="blob b1"></div><div class="blob b2"></div>
<div class="top"><span class="tag">أدوات الألوان للمصممين</span><span class="count latin">{i}/{total}</span></div>
<div class="head">
  <div style="display:flex; justify-content:space-between; align-items:flex-end;">
    <div><div class="name latin">{t['name']}</div><div class="url latin">{t['url']}</div></div>
    <div class="num latin">0{i}</div>
  </div>
  <div class="line">{t['line']}</div>
  <div class="desc">{t['desc']}</div>
  <div class="chips">{chips}</div>
</div>
<div class="sw">{sw}</div>
<div class="phone"><div class="notch"></div><div class="screen"><img src="../screens/{t['img']}"></div></div>
<div class="tip"><b>نصيحة</b>{t['tip']}</div>
</body></html>"""


RAINBOW = ["#E5402B", "#F3C343", "#7C9637", "#70BCD5", "#3B63E3", "#6E2A7E"]


def cover_html():
    bars = "".join(f'<i style="background:{c}"></i>' for c in RAINBOW)
    names = "".join(
        f'<li><span class="n latin">0{k+1}</span><span class="latin">{t["name"]}</span><em style="background:{t["accent"]}"></em></li>'
        for k, t in enumerate(TOOLS))
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Cover</title><style>{BASE_CSS}
body {{ background:#F7F2EA; color:#141414; }}
.bars {{ position:absolute; top:0; left:0; right:0; height:1920px; display:flex; opacity:.95; }}
.bars i {{ flex:1; display:block; }}
.card {{ position:absolute; top:230px; left:70px; right:70px; bottom:250px; background:#F7F2EA; border-radius:64px; padding:80px 70px; box-shadow:0 40px 100px rgba(0,0,0,.25); }}
.kick {{ display:inline-block; font-size:34px; font-weight:800; background:#141414; color:#F7F2EA; padding:10px 30px; border-radius:999px; }}
h1 {{ font-size:118px; font-weight:900; line-height:1.15; margin-top:40px; }}
h1 span {{ background: linear-gradient(90deg,#3B63E3,#6E2A7E,#E5402B,#F3C343); -webkit-background-clip:text; color:transparent; }}
p {{ font-size:44px; font-weight:600; color:rgba(0,0,0,.6); margin-top:24px; line-height:1.5; }}
ul {{ list-style:none; margin-top:50px; display:flex; flex-direction:column; gap:20px; }}
li {{ display:flex; align-items:center; gap:26px; font-size:52px; font-weight:800; direction:ltr; justify-content:flex-end; }}
li .n {{ font-size:34px; color:rgba(0,0,0,.4); font-weight:700; }}
li em {{ width:58px; height:58px; border-radius:50%; display:block; }}
.save {{ position:absolute; bottom:120px; left:0; right:0; text-align:center; font-size:40px; font-weight:800; color:#fff; text-shadow:0 2px 12px rgba(0,0,0,.35); }}
</style></head><body>
<div class="bars">{bars}</div>
<div class="card">
  <span class="kick">للمصممين والمبتدئين</span>
  <h1>٥ مواقع <span>للألوان</span><br>لازم تعرفونها</h1>
  <p>من اختيار اللون الأساسي… إلى لوحة جاهزة لتصميمك</p>
  <ul>{names}</ul>
</div>
<div class="save">احفظوا المنشور قبل لا يضيع ←</div>
</body></html>"""


def outro_html():
    rows = "".join(
        f'<div class="row"><span class="dot" style="background:{t["accent"]}"></span>'
        f'<span class="nm latin">{t["name"]}</span><span class="what">{t["line"].rstrip(".")}</span></div>'
        for t in TOOLS)
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Outro</title><style>{BASE_CSS}
body {{ background:#141414; color:#F7F2EA; }}
.wrap {{ position:absolute; top:170px; right:80px; left:80px; }}
h2 {{ font-size:96px; font-weight:900; line-height:1.2; }}
h2 span {{ color:#F3C343; }}
.sub {{ font-size:40px; color:rgba(247,242,234,.65); margin-top:16px; font-weight:600; }}
.list {{ margin-top:50px; display:flex; flex-direction:column; gap:22px; }}
.row {{ background:#1F1F1F; border-radius:36px; padding:24px 36px; display:grid; grid-template-columns:56px 1fr; grid-template-rows:auto auto; column-gap:24px; align-items:center; }}
.dot {{ width:56px; height:56px; border-radius:50%; grid-row:1 / span 2; }}
.nm {{ font-size:50px; font-weight:800; text-align:right; }}
.what {{ font-size:32px; color:rgba(247,242,234,.7); font-weight:600; }}
.cta {{ position:absolute; bottom:220px; right:80px; left:80px; text-align:center; font-size:52px; font-weight:900; background:linear-gradient(90deg,#3B63E3,#6E2A7E,#E5402B,#F3C343); border-radius:999px; padding:26px; }}
</style></head><body>
<div class="wrap">
  <h2>أي موقع بتجربونه <span>أول؟</span></h2>
  <div class="sub">قولوا لي في التعليقات 👇</div>
  <div class="list">{rows}</div>
</div>
<div class="cta">تابعوني لأدوات تصميم أكثر</div>
</body></html>"""


def main():
    pages = [("00-cover", cover_html())]
    pages += [(t["slug"], tool_html(t, i + 1, len(TOOLS))) for i, t in enumerate(TOOLS)]
    pages.append(("06-outro", outro_html()))
    for slug, html in pages:
        (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print('HTML written; run: node render.js')

if __name__ == "__main__":
    main()
