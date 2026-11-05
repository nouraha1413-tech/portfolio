"""Brand version of the TikTok slides, using the NOURAH logo blue.

Usage: python3 build_brand.py && node render.js slides-brand
"""
from pathlib import Path
from build import TOOLS, BASE_CSS, ROOT

OUT = ROOT / "slides-brand"
OUT.mkdir(exist_ok=True)

# Brand palette (blue sampled from the logo)
BLUE = "#102ECF"    # primary
NAVY = "#0A1B7E"    # depth / shadows
TINT = "#EEF1FD"    # light surface
SUN = "#FFC83D"     # highlight, complements the blue
WHITE = "#FFFFFF"

LOGO = "../brand/nourah-logo.jpg"

BRAND_CSS = BASE_CSS + f"""
body {{ background:{BLUE}; color:{WHITE}; }}
.dia {{ position:absolute; width:26px; height:26px; background:{WHITE}; transform:rotate(45deg); border-radius:4px; }}
.ring {{ position:absolute; border-radius:50%; border:3px solid rgba(255,255,255,.14); }}
.logo {{ position:absolute; top:130px; left:80px; width:230px; height:158px; border-radius:26px; overflow:hidden;
  box-shadow:0 0 0 3px rgba(255,255,255,.18); }}
.logo img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.tag {{ position:absolute; top:150px; right:80px; font-size:30px; font-weight:800; padding:10px 28px; border-radius:999px;
  background:{WHITE}; color:{BLUE}; }}
.count {{ position:absolute; top:236px; right:84px; font-size:30px; font-weight:800; color:rgba(255,255,255,.7); }}
"""


def deco():
    return (f'<div class="ring" style="width:900px;height:900px;left:-420px;top:980px"></div>'
            f'<div class="ring" style="width:600px;height:600px;right:-300px;top:-200px"></div>'
            f'<div class="dia" style="left:350px;top:150px"></div>'
            f'<div class="dia" style="left:395px;top:195px;width:16px;height:16px;opacity:.6"></div>')


def tool_html(t, i, total):
    chips = "".join(f'<span class="chip">{c}</span>' for c in t["chips"])
    sw = "".join(f'<i style="background:{c}"></i>' for c in t["swatches"])
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>{t['name']}</title><style>{BRAND_CSS}
.head {{ position:absolute; top:330px; right:80px; left:80px; }}
.row {{ display:flex; justify-content:space-between; align-items:flex-end; }}
.num {{ font-size:140px; line-height:1; font-weight:900; color:transparent; -webkit-text-stroke:4px {SUN}; }}
.name {{ font-size:112px; font-weight:900; line-height:1; letter-spacing:-3px; text-align:right; }}
.url {{ font-size:30px; font-weight:600; color:{SUN}; margin-top:12px; text-align:right; }}
.line {{ font-size:52px; font-weight:900; line-height:1.35; margin-top:24px; }}
.desc {{ font-size:35px; font-weight:500; line-height:1.6; margin-top:10px; color:rgba(255,255,255,.8); }}
.chips {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:24px; }}
.chip {{ font-size:29px; font-weight:800; padding:8px 26px; border-radius:999px; background:{WHITE}; color:{BLUE}; }}
.phone {{ position:absolute; left:50%; top:930px; width:540px; height:1060px; margin-left:-270px; background:#0B0B12;
  border-radius:70px; padding:16px; box-shadow:0 40px 90px rgba(5,12,70,.55); transform:rotate(-3deg); }}
.screen {{ width:100%; height:100%; border-radius:56px; overflow:hidden; background:#fff; }}
.screen img {{ width:100%; height:100%; object-fit:cover; object-position:top; display:block; }}
.notch {{ position:absolute; top:14px; left:50%; width:150px; height:38px; margin-left:-75px; background:#0B0B12; border-radius:20px; z-index:2; }}
.sw {{ position:absolute; left:70px; top:1010px; display:flex; flex-direction:column; gap:16px; }}
.sw i {{ width:72px; height:72px; border-radius:50%; display:block; box-shadow:0 8px 20px rgba(0,0,0,.25), 0 0 0 4px {WHITE}; }}
.tip {{ position:absolute; right:80px; top:1360px; width:480px; background:{SUN}; color:{NAVY}; border-radius:34px; padding:26px 32px;
  font-size:31px; font-weight:800; line-height:1.5; box-shadow:0 24px 50px rgba(5,12,70,.4); transform:rotate(2deg); }}
.tip b {{ display:block; font-size:26px; font-weight:900; opacity:.75; margin-bottom:4px; }}
</style></head><body>
{deco()}
<div class="logo"><img src="{LOGO}"></div>
<span class="tag">أدوات الألوان للمصممين</span>
<span class="count latin">{i}/{total}</span>
<div class="head">
  <div class="row"><div><div class="name latin">{t['name']}</div><div class="url latin">{t['url']}</div></div>
  <div class="num latin">0{i}</div></div>
  <div class="line">{t['line']}</div>
  <div class="desc">{t['desc']}</div>
  <div class="chips">{chips}</div>
</div>
<div class="sw">{sw}</div>
<div class="phone"><div class="notch"></div><div class="screen"><img src="../screens/{t['img']}"></div></div>
<div class="tip"><b>نصيحة</b>{t['tip']}</div>
</body></html>"""


def cover_html():
    names = "".join(
        f'<li><span class="n latin">0{k+1}</span><span class="latin">{t["name"]}</span>'
        f'<em>{"".join(f"<i style=background:{c}></i>" for c in t["swatches"][:3])}</em></li>'
        for k, t in enumerate(TOOLS))
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Cover</title><style>{BRAND_CSS}
.kick {{ position:absolute; top:380px; right:80px; font-size:34px; font-weight:800; color:{SUN}; }}
h1 {{ position:absolute; top:440px; right:80px; left:80px; font-size:128px; font-weight:900; line-height:1.15; }}
h1 span {{ color:{SUN}; }}
.card {{ position:absolute; top:960px; left:80px; right:80px; background:{WHITE}; color:{NAVY}; border-radius:56px; padding:46px 56px;
  box-shadow:0 40px 90px rgba(5,12,70,.45); }}
ul {{ list-style:none; display:flex; flex-direction:column; gap:14px; }}
li {{ display:flex; align-items:center; gap:24px; font-size:52px; font-weight:800; direction:ltr; }}
li .n {{ font-size:32px; color:{BLUE}; font-weight:800; width:52px; }}
li em {{ margin-left:auto; display:flex; }}
li em i {{ width:46px; height:46px; border-radius:50%; display:block; margin-left:-12px; box-shadow:0 0 0 4px {WHITE}; }}
.save {{ position:absolute; top:1640px; right:80px; font-size:38px; font-weight:800; background:{SUN}; color:{NAVY}; padding:14px 34px; border-radius:999px; }}
</style></head><body>
{deco()}
<div class="logo"><img src="{LOGO}"></div>
<span class="tag">سلسلة أدوات المصمم</span>
<div class="kick">للمصممين والمبتدئين</div>
<h1>٥ مواقع <span>للألوان</span><br>لازم تعرفونها</h1>
<div class="card"><ul>{names}</ul></div>
<div class="save">احفظوا المنشور قبل لا يضيع</div>
</body></html>"""


def outro_html():
    rows = "".join(
        f'<div class="r"><span class="d" style="background:{t["swatches"][0]}"></span>'
        f'<span class="nm latin">{t["name"]}</span><span class="w">{t["line"].rstrip(".")}</span></div>'
        for t in TOOLS)
    return f"""<!doctype html><html lang="ar"><head><meta charset="utf-8"><title>Outro</title><style>{BRAND_CSS}
h2 {{ position:absolute; top:360px; right:80px; left:80px; font-size:96px; font-weight:900; line-height:1.2; }}
h2 span {{ color:{SUN}; }}
.sub {{ position:absolute; top:600px; right:80px; font-size:40px; font-weight:700; color:rgba(255,255,255,.8); }}
.list {{ position:absolute; top:700px; right:80px; left:80px; display:flex; flex-direction:column; gap:16px; }}
.r {{ background:{WHITE}; color:{NAVY}; border-radius:34px; padding:18px 34px; display:grid; grid-template-columns:52px 1fr;
  column-gap:24px; align-items:center; }}
.d {{ width:52px; height:52px; border-radius:50%; grid-row:1 / span 2; box-shadow:inset 0 0 0 3px rgba(0,0,0,.08); }}
.nm {{ font-size:46px; font-weight:800; text-align:right; }}
.w {{ font-size:30px; font-weight:600; color:rgba(10,27,126,.7); }}
.cta {{ position:absolute; top:1610px; right:80px; left:80px; text-align:center; font-size:50px; font-weight:900; background:{SUN};
  color:{NAVY}; border-radius:999px; padding:24px; }}
</style></head><body>
{deco()}
<div class="logo"><img src="{LOGO}"></div>
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
