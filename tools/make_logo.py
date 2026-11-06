#!/usr/bin/env python3
"""Builds the SanityAI wordmark as SVG paths from Altera Sans (no live text, no font needed).
Writes assets/brand/sanityai-logo.svg (uses currentColor, black when opened alone)
and assets/brand/sanityai-logo-white.svg. Spacing matches the site: letter-spacing 0.28em,
a thin bar with 0.34em before and 0.62em after it."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
font = TTFont(os.path.join(ROOT, 'assets/haze/AlteraSans-Regular.otf'))
gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font['head'].unitsPerEm
cap = getattr(font['OS/2'], 'sCapHeight', 0) or int(upm * 0.7)
LS, BAR_L, BAR_R, BAR_W, BAR_H = 0.28 * upm, 0.34 * upm, 0.62 * upm, 0.075 * upm, 1.3 * upm

def word(text, x, pen_list):
    for i, ch in enumerate(text):
        g = gs[cmap[ord(ch)]]
        sp = SVGPathPen(gs)
        g.draw(TransformPen(sp, (1, 0, 0, -1, x, 0)))  # flip y, baseline at 0
        pen_list.append(sp.getCommands())
        x += g.width + (LS if i < len(text) - 1 else 0)
    return x

paths = []
x = word('SANITY', 0, paths)
x += LS + BAR_L
mid = -cap / 2
bar = (x, mid - BAR_H / 2, BAR_W, BAR_H)
x += BAR_W + BAR_R
x = word('AI', x, paths)
# tight horizontal bounds from the first glyph's left side bearing
bp = BoundsPen(gs); gs[cmap[ord('S')]].draw(bp); lsb = bp.bounds[0]
bp = BoundsPen(gs); gs[cmap[ord('I')]].draw(bp); rsb = gs[cmap[ord('I')]].width - bp.bounds[2]
x0, x1 = lsb - 20, x - rsb + 40
y0, y1 = bar[1], bar[1] + bar[3]
vb = '%g %g %g %g' % (round(x0), round(y0), round(x1 - x0), round(y1 - y0))
d = ''.join(paths)
rect = '<rect x="%g" y="%g" width="%g" height="%g"/>' % tuple(round(v, 1) for v in bar)

def svg(fill):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="SanityAI">'
            '<title>SanityAI</title><g id="mark" fill="%s"><path d="%s"/>%s</g></svg>\n') % (vb, fill, d, rect)

open(os.path.join(ROOT, 'assets/brand/sanityai-logo.svg'), 'w').write(svg('currentColor'))
open(os.path.join(ROOT, 'assets/brand/sanityai-logo-white.svg'), 'w').write(svg('#ffffff'))
w, h = round(x1 - x0), round(y1 - y0)
open(os.path.join(ROOT, 'tools/logo_vb.txt'), 'w').write('%s|%.4f' % (vb, w / h))
print('viewBox', vb, 'ratio', round(w / h, 4))

# Favicon: S | A drawn as paths, white on a black rounded square.
def glyph_path(ch, x, y, s):
    g = gs[cmap[ord(ch)]]; sp = SVGPathPen(gs)
    g.draw(TransformPen(sp, (s, 0, 0, -s, x, y))); return sp.getCommands(), g.width * s
s = 26 / upm
ps, ws = glyph_path('S', 0, 0, s); pa, wa = glyph_path('A', 0, 0, s)
ys = 32 + cap * s / 2
ps, _ = glyph_path('S', 19 - ws / 2, ys, s); pa, _ = glyph_path('A', 45 - wa / 2, ys, s)
fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#111111"/>'
       '<path fill="#ffffff" d="%s%s"/><rect x="31.2" y="17" width="1.6" height="30" fill="#ffffff"/></svg>\n') % (ps, pa)
open(os.path.join(ROOT, 'favicon.svg'), 'w').write(fav)
print('favicon written')
