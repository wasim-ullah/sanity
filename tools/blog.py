# Blog index and article pages, built from tools/posts.py.
import json, re
from posts import POSTS, DATE, DATE_ISO

ARR = '<svg class="arr" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"></path><path d="M8 7h9v9"></path></svg>'

def minutes(html):
    words = len(re.sub(r'<[^>]+>', ' ', html).split())
    return max(2, -(-words // 220))

def meta(p):
    return ('<div class="meta"><span class="cat">%s</span><span class="dot"></span><span>%d min read</span></div>' % (p['cat'], minutes(p['body'])))

def card(p):
    return ('<a class="pcard sv" href="/blog/%s" data-cat="%s"><div class="im"><img src="/assets/photos/%s" alt="" loading="lazy"></div>'
            '%s<h3>%s</h3><p>%s</p></a>') % (p['slug'], p['cat'], p['img'], meta(p), p['title'], p['dek'])

FILTER_JS = ('<script>(function(){var b=[].slice.call(document.querySelectorAll(".filters button")),c=[].slice.call(document.querySelectorAll("[data-cat]"));'
    'b.forEach(function(x){x.addEventListener("click",function(){var k=x.getAttribute("data-f");b.forEach(function(y){y.setAttribute("aria-pressed",y===x?"true":"false");});'
    'c.forEach(function(e){e.hidden=!(k==="all"||e.getAttribute("data-cat")===k);});});});})();</script>\n')

def index_page():
    first, rest = POSTS[0], POSTS[1:]
    cats = []
    for p in POSTS:
        if p['cat'] not in cats:
            cats.append(p['cat'])
    filters = '<button type="button" data-f="all" aria-pressed="true">All</button>' + ''.join('<button type="button" data-f="%s" aria-pressed="false">%s</button>' % (c, c) for c in cats)
    body = ('<section class="wrap ph">\n<div class="chip rise"><i></i>Blog</div>\n'
        '<div class="ph-grid">\n<h1 class="rise d1">Notes on getting <span class="focus">found and chosen.</span></h1>\n'
        '<div class="ph-side rise d2"><p>Practical writing on search, ads, automation and sales for service businesses in the GCC. Each piece covers something changing right now and what to do about it this week.</p></div>\n</div>\n'
        '<div class="filters rise d2" role="group" aria-label="Filter by topic">' + filters + '</div>\n'
        '<a class="feat sv" href="/blog/%s" data-cat="%s"><div class="im"><img src="/assets/photos/%s" alt=""></div>'
        '<div>%s<h2>%s</h2><p>%s</p><div style="margin-top:18px"><span class="btn sm">Read the article %s</span></div></div></a>\n'
        % (first['slug'], first['cat'], first['img'], meta(first), first['title'], first['dek'], ARR) +
        '<div class="pgrid">' + ''.join(card(p) for p in rest) + '</div>\n</section>\n')
    return {'file': 'blog.html', 'path': '/blog', 'title': 'Blog | SanityAI',
            'desc': 'Practical writing on search, ads, automation and sales for service businesses in the GCC.',
            'body': body, 'script': FILTER_JS,
            'close': {'h2': 'Want this applied to <span class="focus">your business?</span>',
                      'lead': 'Book a free 20-minute call and we will look at your site, ads and enquiries with you. You leave with the first three fixes, whether or not we work together.',
                      'img': 'proof.jpg'}}

def post_page(i, p):
    others = [q for q in POSTS if q is not p]
    same = [q for q in others if q['cat'] == p['cat']]
    related = (same + [q for q in others if q not in same])[:3]
    ld = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'description': p['dek'],
          'datePublished': p.get('date_iso', DATE_ISO), 'author': {'@type': 'Person', 'name': 'Wasim Ullah'},
          'publisher': {'@type': 'Organization', 'name': 'SanityAI'}, 'image': 'https://sanity.ai/assets/photos/' + p['img'],
          'mainEntityOfPage': 'https://sanity.ai/blog/' + p['slug']}
    body = ('<section class="wrap ph ph-post">\n<div class="chip rise"><i></i><a href="/blog">Blog</a><span class="sep">/</span>%s</div>\n'
        '<div class="ph-grid"><h1 class="rise d1">%s</h1></div>\n'
        '<div class="byline rise d2"><img src="/assets/haze/founder.jpg" alt=""><div><b>Wasim Ullah, Founder</b>%s &middot; %d min read</div></div>\n'
        '</section>\n<div class="wrap"><div class="band short grow"><img src="/assets/photos/%s" alt="" class="px"></div></div>\n'
        '<article class="wrap"><div class="post">%s</div>\n'
        '<div class="endnote"><p>Want a second opinion on how this applies to you? We will look at your setup on a free 20-minute call.</p><a class="btn dark" href="/contact">Book a call %s</a></div>\n</article>\n'
        '<section class="wrap sec">\n<div class="chip"><i></i>Keep reading</div>\n<h2 class="sv">More from <span class="focus">the blog.</span></h2>\n'
        '<div class="pgrid" style="margin-top:40px">%s</div>\n</section>\n'
        % (p['cat'], p['title'], p.get('date', DATE), minutes(p['body']), p['img'], p['body'].strip(), ARR, ''.join(card(q) for q in related)))
    return {'file': 'blog/%s.html' % p['slug'], 'path': '/blog/' + p['slug'], 'title': p['title'] + ' | SanityAI',
            'desc': p['dek'], 'body': body,
            'head': '<script type="application/ld+json">%s</script>\n' % json.dumps(ld),
            'published': p.get('date_iso', DATE_ISO), 'og_eyebrow': 'Blog  /  ' + p['cat'],
            'close': {'h2': 'Let\'s look at <span class="focus">your numbers.</span>',
                      'lead': 'Book a free 20-minute call and we will look at your site, ads and enquiries with you. You leave with the first three fixes, whether or not we work together.',
                      'img': ['proof.jpg', 'night-fog.jpg', 'dunes.jpg', 'hero-3.jpg', 'sector.jpg'][i % 5]}}

def blog_pages():
    return [index_page()] + [post_page(i, p) for i, p in enumerate(POSTS)]
