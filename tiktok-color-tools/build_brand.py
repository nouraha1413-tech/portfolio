"""Brand version of the TikTok slides (NOURAH blue), with each site's logo.

Usage: python3 build_brand.py && node render.js slides-brand
"""
from build import TOOLS, BASE_CSS, ROOT

OUT = ROOT / "slides-brand"
OUT.mkdir(exist_ok=True)

BLUE, NAVY, SUN, WHITE = "#102ECF", "#0A1B7E", "#FFC83D", "#FFFFFF"

# Logo per tool, cropped from the screenshots, shown on its native background.
LOGOS = {
    "01-adobe-color": ("adobe.png", "#F8F8F8", 110),
    "02-coolors": ("coolors.png", "#FFFFFF", 130),
    "03-huemint": ("huemint.png", "#72BCD5", 120),
    "04-color-hunt": ("colorhunt.png", "#FFFFFF", 160),
    "05-paletton": ("paletton-wheel.png", "#2A2A2A", 180),
}

CSS = BASE_CSS + f"""
body {{ background:{BLUE}; color:{WHITE}; }}
.ring {{ position:absolute; border-radius:50%; border:3px solid rgba(255,255,255,.14); }}
.tag {{ position:absolute; top:150px; right:80px; font-size:30px; font-weight:800; padding:10px 28px; border-radius:999px; background:{WHITE}; color:{BLUE}; }}
.count {{ position:absolute; top:158px; left:84px; font-size:34px; font-weight:800; color:rgba(255,255,255,.75); }}
"""

RINGS = ('<div class="ring" style="width:900px;height:900px;left:-420px;top:980px"></div>'
         '<div class="ring" style="width:600px;height:600px;right:-300px;top:-200px"></div>')


def tool_html(t, i, total):
    _, sbg, _ = LOGOS[t["slug"]]  # screenshot's own background, used for the phone status bar
    chips = "".join(f'<span class="chip">{c}</span>' for c in t["chips"])
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>{t['name']}</title><style>{CSS}
.head {{ position:absolute; top:250px; right:80px; left:80px; }}
.row {{ display:flex; justify-content:space-between; align-items:flex-end; }}
.num {{ font-size:140px; line-height:1; font-weight:900; color:transparent; -webkit-text-stroke:4px {SUN}; }}
.name {{ font-size:112px; font-weight:900; line-height:1; letter-spacing:-3px; text-align:right; }}
.url {{ font-size:30px; font-weight:600; color:{SUN}; margin-top:12px; text-align:right; }}
.line {{ font-size:52px; font-weight:900; line-height:1.35; margin-top:24px; }}
.desc {{ font-size:35px; font-weight:500; line-height:1.6; margin-top:10px; color:rgba(255,255,255,.82); }}
.chips {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:24px; }}
.chip {{ font-size:29px; font-weight:800; padding:8px 26px; border-radius:999px; background:{WHITE}; color:{BLUE}; }}
.phone {{ position:absolute; left:50%; top:880px; width:560px; height:1100px; margin-left:-280px; background:#0B0B12;
  border-radius:70px; padding:16px; box-shadow:0 40px 90px rgba(5,12,70,.55); transform:rotate(-3deg); }}
.screen {{ width:100%; height:100%; border-radius:56px; overflow:hidden; background:{sbg}; display:flex; flex-direction:column; }}
.status {{ height:72px; flex:none; position:relative; background:{sbg}; }}
.notch {{ position:absolute; top:14px; left:50%; width:150px; height:38px; margin-left:-75px; background:#0B0B12; border-radius:20px; }}
.screen img {{ width:100%; flex:1; min-height:0; object-fit:cover; object-position:top; display:block; }}
.tip {{ position:absolute; right:70px; top:1440px; width:460px; background:{SUN}; color:{NAVY}; border-radius:34px; padding:24px 30px;
  font-size:31px; font-weight:800; line-height:1.5; box-shadow:0 24px 50px rgba(5,12,70,.4); transform:rotate(2deg); }}
.tip b {{ display:block; font-size:26px; font-weight:900; opacity:.75; margin-bottom:4px; }}
</style></head><body>
{RINGS}
<span class="tag">أدوات الألوان للمصممين</span>
<span class="count latin">{i}/{total}</span>
<div class="head">
  <div class="row"><div><div class="name latin">{t['name']}</div><div class="url latin">{t['url']}</div></div>
  <div class="num latin">0{i}</div></div>
  <div class="line">{t['line']}</div>
  <div class="desc">{t['desc']}</div>
  <div class="chips">{chips}</div>
</div>
<div class="phone"><div class="screen"><div class="status"><div class="notch"></div></div>
<img src="../screens/{t['img']}"></div></div>
<div class="tip"><b>نصيحة</b>{t['tip']}</div>
</body></html>"""


def cover_html():
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Cover</title><style>{CSS}
.wrap {{ position:absolute; top:0; bottom:0; right:80px; left:80px; display:flex; flex-direction:column; justify-content:center; align-items:flex-start; }}
h1 {{ font-size:122px; font-weight:900; line-height:1.2; margin-top:10px; white-space:nowrap; }}
h1 span {{ color:{SUN}; }}
.swipe {{ position:absolute; top:1650px; right:80px; font-size:42px; font-weight:900; background:{SUN}; color:{NAVY}; padding:16px 42px; border-radius:999px; }}
</style></head><body>
{RINGS}
<span class="tag">سلسلة أدوات المصمم</span>
<div class="wrap">
<h1>5 مواقع <span>للألوان</span><br>لازم تعرفونها</h1>
</div>
<div class="swipe">اسحبوا وشوفوها ←</div>
</body></html>"""


def outro_html():
    rows = ""
    for t in TOOLS:
        logo, lbg, _ = LOGOS[t["slug"]]
        rows += (f'<div class="r"><span class="lg" style="background:{lbg}"><img src="../logos/{logo}"></span>'
                 f'<span class="tx"><span class="nm latin">{t["name"]}</span><span class="w">{t["line"].rstrip(".")}</span></span></div>')
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Outro</title><style>{CSS}
h2 {{ position:absolute; top:290px; right:80px; left:80px; font-size:96px; font-weight:900; line-height:1.2; }}
h2 span {{ color:{SUN}; }}
.sub {{ position:absolute; top:530px; right:80px; font-size:40px; font-weight:700; color:rgba(255,255,255,.8); }}
.list {{ position:absolute; top:630px; right:80px; left:80px; display:flex; flex-direction:column; gap:16px; }}
.r {{ background:{WHITE}; color:{NAVY}; border-radius:34px; padding:16px 20px 16px 30px; display:flex; align-items:center; gap:26px; }}
.lg {{ width:150px; height:96px; border-radius:22px; display:flex; align-items:center; justify-content:center; flex:none; box-shadow:inset 0 0 0 2px rgba(0,0,0,.06); }}
.lg img {{ max-width:124px; max-height:72px; display:block; }}
.tx {{ display:flex; flex-direction:column; }}
.nm {{ font-size:44px; font-weight:800; text-align:right; line-height:1.2; }}
.w {{ font-size:29px; font-weight:600; color:rgba(10,27,126,.7); }}
.cta {{ position:absolute; top:1650px; right:80px; left:80px; text-align:center; font-size:66px; font-weight:900; background:{SUN};
  color:{NAVY}; border-radius:999px; padding:38px 24px; }}
</style></head><body>
{RINGS}
<span class="tag">سلسلة أدوات المصمم</span>
<h2>أي موقع بتجربونه <span>أول؟</span></h2>
<div class="sub">قولوا لي في التعليقات 👇</div>
<div class="list">{rows}</div>
<div class="cta">تابعوني لأدوات تصميم أكثر</div>
</body></html>"""


def main():
    pages = [("00-cover", cover_html())]
    pages += [(t["slug"], tool_html(t, i + 1, len(TOOLS))) for i, t in enumerate(TOOLS)]
    pages.append(("06-outro", outro_html()))
    for slug, html in pages:
        (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print("HTML written; run: node render.js slides-brand")


if __name__ == "__main__":
    main()
