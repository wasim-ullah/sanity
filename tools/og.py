"""Share preview images (Open Graph / Twitter) for every page.

Each page gets a 1200x630 JPG: its own photo, a dark overlay, the page headline in the
site fonts, a small label and the SanityAI logo. Images are cached by content, so only
changed pages are re-rendered. Used by tools/build.py for all current and future pages."""
import os, re, json, hashlib, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'og')
CACHE = os.path.join(OUT, 'cache.json')
VERSION = 'og-v2'
FONTS = os.path.join(ROOT, 'tools', 'fonts')

def _logo_white():
    s = open(os.path.join(ROOT, 'assets/brand/sanityai-logo.svg')).read()
    return s.replace('currentColor', '#ffffff')

def _clean_headline(h):
    # keep the serif accent span, drop other markup
    h = re.sub(r'<span class="focus">', '\x00', h)
    h = re.sub(r'</span>', '\x01', h)
    h = re.sub(r'<[^>]+>', '', h)
    h = H.escape(H.unescape(h))
    return h.replace('\x00', '<span class="focus">').replace('\x01', '</span>').strip()

def template(headline, eyebrow, photo):
    return '''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:G;font-weight:400;src:url("file://%(f)s/geist-sans-latin-400-normal.woff2")}
@font-face{font-family:G;font-weight:500;src:url("file://%(f)s/geist-sans-latin-500-normal.woff2")}
@font-face{font-family:P;font-weight:400;src:url("file://%(f)s/ibm-plex-serif-latin-400-normal.woff2")}
html,body{margin:0;width:1200px;height:630px;overflow:hidden;background:#111}
.bg{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover}
.ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,10,12,.86) 0%%,rgba(10,10,12,.62) 52%%,rgba(10,10,12,.28) 100%%),linear-gradient(180deg,rgba(10,10,12,.35) 0%%,rgba(10,10,12,0) 30%%,rgba(10,10,12,.55) 100%%)}
.logo{position:absolute;left:72px;top:64px;width:236px;height:auto;display:block}
.logo svg{width:236px;height:auto;display:block}
.txt{position:absolute;left:72px;right:200px;bottom:72px;color:#fff;font-family:G}
.eb{display:flex;align-items:center;gap:12px;font-size:19px;color:rgba(255,255,255,.82);letter-spacing:.01em}
.eb i{width:16px;height:16px;border-radius:3px;background:rgba(255,255,255,.28);display:inline-block}
h1{margin:22px 0 0;font-weight:400;letter-spacing:-0.045em;line-height:1.05;max-width:960px}
.focus{font-family:P;font-weight:400;letter-spacing:-0.05em}
.url{position:absolute;right:72px;bottom:74px;font-family:G;font-size:19px;color:rgba(255,255,255,.75)}
</style></head><body>
<img class="bg" src="file://%(photo)s">
<div class="ov"></div>
<div class="logo">%(logo)s</div>
<div class="txt"><div class="eb"><i></i>%(eb)s</div><h1 id="h">%(h)s</h1></div>
<div class="url">sanity.ai</div>
</body></html>''' % {'f': FONTS, 'photo': photo, 'logo': _logo_white(), 'eb': H.escape(eyebrow), 'h': _clean_headline(headline)}

def render_all(items):
    """items: list of dicts with key, headline (html), eyebrow, img (filename in assets/photos).
    Returns {key: '/assets/og/<key>.jpg?v=<hash>'}."""
    os.makedirs(OUT, exist_ok=True)
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo, urls = [], {}
    for it in items:
        photo = os.path.join(ROOT, 'assets/photos', it['img'])
        sig = hashlib.md5((VERSION + it['headline'] + it['eyebrow'] + it['img'] + str(os.path.getsize(photo)) + _logo_white()).encode()).hexdigest()[:10]
        path = os.path.join(OUT, it['key'] + '.jpg')
        if cache.get(it['key']) != sig or not os.path.exists(path):
            todo.append((it, photo, path, sig))
        urls[it['key']] = '/assets/og/%s.jpg?v=%s' % (it['key'], sig)
    if todo:
        from playwright.sync_api import sync_playwright
        from PIL import Image
        tmp = os.path.join(OUT, '_tmp.html')
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
            for it, photo, path, sig in todo:
                open(tmp, 'w').write(template(it['headline'], it['eyebrow'], photo))
                pg.goto('file://' + tmp); pg.wait_for_timeout(250)
                pg.evaluate('''async () => { await document.fonts.ready;
                    const h = document.getElementById('h'); let s = 78; h.style.fontSize = s + 'px';
                    while (h.getBoundingClientRect().height > s * 1.05 * 3 + 4 && s > 40) { s -= 2; h.style.fontSize = s + 'px'; } }''')
                pg.wait_for_timeout(80)
                png = path[:-4] + '.png'; pg.screenshot(path=png)
                Image.open(png).convert('RGB').save(path, quality=82, optimize=True, progressive=True); os.remove(png)
                cache[it['key']] = sig
                print('og image', it['key'], os.path.getsize(path) // 1024, 'KB')
            b.close()
        os.remove(tmp)
    json.dump(cache, open(CACHE, 'w'), indent=1, sort_keys=True)
    return urls

def meta_tags(url, title, desc, image_path, alt, kind='website', published=None):
    img = 'https://sanity.ai' + image_path
    t, d, a = H.escape(title), H.escape(desc), H.escape(alt)
    tags = [
        '<meta property="og:site_name" content="SanityAI">',
        '<meta property="og:locale" content="en_US">',
        '<meta property="og:type" content="%s">' % kind,
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:title" content="%s">' % t,
        '<meta property="og:description" content="%s">' % d,
        '<meta property="og:image" content="%s">' % img,
        '<meta property="og:image:secure_url" content="%s">' % img,
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="%s">' % a,
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % t,
        '<meta name="twitter:description" content="%s">' % d,
        '<meta name="twitter:image" content="%s">' % img,
        '<meta name="twitter:image:alt" content="%s">' % a,
    ]
    if kind == 'article' and published:
        tags += ['<meta property="article:published_time" content="%s">' % published, '<meta property="article:author" content="Wasim Ullah">']
    return '\n'.join(tags) + '\n'
