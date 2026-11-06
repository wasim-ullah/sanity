#!/usr/bin/env python3
"""Builds the SanityAI inner pages and keeps the shared header and footer in sync.

Run from the repo root:  python3 tools/build.py
- Writes assets/site.css (base styles from the home page plus tools/site-extra.css)
- Writes solutions/*.html, industries/*.html and privacy.html from tools/pages.py
- Replaces the header and footer blocks in index.html between their markers
"""
import os, re, html, sys, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from pages import SOLUTIONS, INDUSTRIES, PAGES
from blog import blog_pages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARR = '<svg class="arr" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"></path><path d="M8 7h9v9"></path></svg>'
ARR_R = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>'
WA = 'https://wa.me/971585785819'
MARK = '<span class="mark">Sanity<span class="bar"></span>AI</span>'

def icon(paths):
    return '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>'

def dd(label, key, items, foot):
    links = ''.join('<a href="%s"><span class="ic">%s</span><span><b>%s</b><small>%s</small></span></a>' % (i['url'], icon(i['icon']), i['name'], i['short']) for i in items)
    return ('<div class="dd"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-%s">%s <span class="plus" aria-hidden="true">+</span></button>'
            '<div class="dd-panel" id="dd-%s">%s<div class="dd-foot"><span>%s</span><a href="#start">Book a call %s</a></div></div></div>') % (key, label, key, links, foot, ARR)

def msub(label, items):
    links = ''.join('<a href="%s">%s<small>%s</small></a>' % (i['url'], i['name'], i['short']) for i in items)
    return ('<li><button type="button" class="macc" aria-expanded="false">%s <span class="plus" aria-hidden="true">+</span></button>'
            '<div class="msub"><div><div>%s</div></div></div></li>') % (label, links)

def header():
    return ('<!-- HEADER:START -->\n<header class="sh">\n<div class="hd">\n'
        '<a class="hd-logo" href="/" aria-label="SanityAI home">' + MARK.replace('class="mark"', 'class="mark" aria-hidden="true"') + '</a>\n'
        '<nav class="navlinks" aria-label="Main">\n'
        '<a href="/#services">About</a>\n'
        + dd('Solutions', 'sol', SOLUTIONS, 'One team for all four, measured on enquiries.') + '\n'
        '<a href="/#start">Pricing</a>\n'
        + dd('Industries', 'ind', INDUSTRIES, 'Not listed? We work across most service businesses.') + '\n'
        '</nav>\n'
        '<div class="hd-cta">\n'
        '<a class="btn navwa" href="' + WA + '">WhatsApp</a>\n'
        '<a class="btn dark" href="#start">Book a call ' + ARR + '</a>\n'
        '<button type="button" class="burger" aria-expanded="false" aria-controls="mnav" aria-label="Open menu"><span></span><span></span></button>\n'
        '</div>\n</div>\n</header>\n'
        '<div class="mnav" id="mnav" aria-hidden="true"><div class="mnav-in">\n<ul class="mnav-list">\n'
        '<li><a href="/#services">About</a></li>\n'
        + msub('Solutions', SOLUTIONS) + '\n'
        '<li><a href="/#start">Pricing</a></li>\n'
        + msub('Industries', INDUSTRIES) + '\n'
        '</ul>\n'
        '<div class="mnav-cta"><a class="btn" href="' + WA + '">WhatsApp</a><a class="btn dark" href="#start">Book a call ' + ARR + '</a></div>\n'
        '<div class="mnav-meta"><a href="mailto:work@sanity.ai">work@sanity.ai</a><span>Dubai, UAE</span></div>\n'
        '</div></div>\n<!-- HEADER:END -->')

def footer_cols():
    sol = ''.join('<a href="%s">%s</a>' % (i['url'], i['name']) for i in SOLUTIONS)
    ind = ''.join('<a href="%s">%s</a>' % (i['url'], i['name']) for i in INDUSTRIES)
    return ('<!-- FOOTCOLS:START -->\n<div class="wrap ft-cols">\n'
        '<div><h4>Solutions</h4>' + sol + '</div>\n'
        '<div><h4>Industries</h4>' + ind + '</div>\n'
        '<div><h4>Company</h4><a href="/#start">Pricing</a><a href="/blog">Blog</a><a href="/careers">Careers</a><a href="/privacy">Privacy policy</a></div>\n'
        '<div><h4>Contact</h4><a href="mailto:work@sanity.ai">work@sanity.ai</a><a href="' + WA + '">WhatsApp</a><a href="https://www.instagram.com/_sanityhq/">Instagram</a></div>\n'
        '</div>\n'
        '<div class="wrap ft-base"><span>© 2026 SanityAI, a business of Safia Saif LLC, Dubai</span><a href="/privacy">Privacy policy</a></div>\n'
        '<!-- FOOTCOLS:END -->')

def footer():
    return ('<footer class="ft">\n<div class="wrap" style="padding-top:56px;display:flex;flex-wrap:wrap;gap:40px;justify-content:space-between">\n'
        '<div style="flex:1 1 280px"><div role="img" aria-label="SanityAI" style="font-size:14px">' + MARK + '</div>'
        '<div style="margin-top:14px;font-size:22px;line-height:1.15;letter-spacing:-0.04em;max-width:10em">Your business, <span class="focus">found and chosen.</span></div>'
        '<div style="margin-top:14px;display:flex;gap:6px"><a class="btn dark sm" href="#start">Book a call ' + ARR + '</a><a class="btn sm" href="mailto:work@sanity.ai">Email us</a></div></div>\n'
        '</div>\n' + footer_cols() + '\n</footer>')

def head(title, desc, path, extra_head=''):
    url = 'https://sanity.ai' + path
    t = html.escape(title)
    d = html.escape(desc)
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<title>' + t + '</title>\n<meta name="description" content="' + d + '">\n'
        '<link rel="canonical" href="' + url + '">\n'
        '<meta property="og:type" content="website">\n<meta property="og:url" content="' + url + '">\n'
        '<meta property="og:title" content="' + t + '">\n<meta property="og:description" content="' + d + '">\n'
        '<meta property="og:image" content="https://sanity.ai/assets/social/og-image.png">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<meta name="theme-color" content="#f5f5f4">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500&family=IBM+Plex+Serif:wght@300;400&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="/assets/site.css">\n' + extra_head + '</head>\n<body>\n<div class="site">\n')

def closing(c):
    return ('<section id="start" class="close">\n<img src="/assets/photos/' + c.get('img', 'proof.jpg') + '" alt="" class="px">\n'
        '<div aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,14,16,.15) 0%,rgba(12,14,16,.25) 40%,rgba(12,14,16,.88) 100%)"></div>\n'
        '<div class="wrap">\n<div class="chip" style="color:#ffffff"><i style="background:rgba(255,255,255,.3)"></i>' + c.get('chip', '13 years of marketing across the US, LATAM, Pakistan and the GCC') + '</div>\n'
        '<h2 class="sv">' + c['h2'] + '</h2>\n<p class="lead sv">' + c['lead'] + '</p>\n'
        '<div style="margin-top:22px;display:flex;gap:8px;flex-wrap:wrap">' + c.get('btns', '<a class="btn light" href="' + WA + '?text=' + c.get('wa', 'Hi%20Wasim%2C%20I%27d%20like%20to%20book%20a%20call.') + '">Book a call on WhatsApp ' + ARR + '</a><a class="btn ghost" href="mailto:work@sanity.ai">work@sanity.ai</a>') + '</div>\n'
        + ('' if c.get('stats') is False else '<div class="stats sv"><div><div>$1M+</div><div>Revenue traced to our campaigns</div></div><div><div>60%</div><div>Lower cost per acquisition, four GCC markets</div></div><div><div>13</div><div>Years of marketing experience</div></div></div>\n') +
        '</div>\n</section>\n')

def page(p):
    return head(p['title'], p['desc'], p['path'], p.get('head', '')) + header() + '\n<main>\n' + p['body'] + closing(p['close']) + '</main>\n' + footer() + \
        '\n</div>\n<script src="/assets/site.js" defer></script>\n<script>' + REVEAL + '</script>\n' + p.get('script', '') + '</body>\n</html>\n'

# Scroll reveal fallback for browsers without scroll timelines (same as the home page).
REVEAL = ("(function(){if(!(window.CSS&&CSS.supports&&CSS.supports('animation-timeline: view()'))&&'IntersectionObserver' in window){"
    "document.documentElement.classList.add('io');var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:0.12});"
    "document.querySelectorAll('.sv,.fv,.grow').forEach(function(el){io.observe(el);});}})();")

def main():
    base = open(os.path.join(ROOT, 'tools', 'base.css')).read()
    extra = open(os.path.join(ROOT, 'tools', 'site-extra.css')).read()
    open(os.path.join(ROOT, 'assets', 'site.css'), 'w').write('/* Generated by tools/build.py. Edit tools/base.css or tools/site-extra.css. */\n' + base + '\n' + extra)
    pages = PAGES + blog_pages()
    def ver(f):
        return hashlib.md5(open(os.path.join(ROOT, 'assets', f), 'rb').read()).hexdigest()[:8]
    vcss, vjs = ver('site.css'), ver('site.js')
    def stamp(t):
        t = re.sub(r'/assets/site\.css(\?v=\w+)?', '/assets/site.css?v=' + vcss, t)
        return re.sub(r'/assets/site\.js(\?v=\w+)?', '/assets/site.js?v=' + vjs, t)
    for p in pages:
        out = os.path.join(ROOT, p['file'])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w').write(stamp(page(p)))
        print('wrote', p['file'])
    ix = os.path.join(ROOT, 'index.html')
    s = open(ix).read()
    s = re.sub(r'<!-- HEADER:START -->.*?<!-- HEADER:END -->', lambda m: header(), s, flags=re.S)
    s = re.sub(r'<!-- FOOTCOLS:START -->.*?<!-- FOOTCOLS:END -->', lambda m: footer_cols(), s, flags=re.S)
    open(ix, 'w').write(stamp(s))
    print('updated index.html')
    urls = ['/'] + [p['path'] for p in pages]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('  <url><loc>https://sanity.ai%s</loc></url>\n' % u for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    print('wrote sitemap.xml with', len(urls), 'urls')

if __name__ == '__main__':
    main()
