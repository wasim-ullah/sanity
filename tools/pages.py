# Content for the SanityAI inner pages. Copy rules: no em dashes, no single-sentence paragraphs,
# no invented numbers. The only figures used are the real ones: $1M+, 60% across four GCC markets, 13 years.

ARR = '<svg class="arr" width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"></path><path d="M8 7h9v9"></path></svg>'
GO = '<span class="go" aria-hidden="true"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg></span>'
CHECK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"></path></svg>'
WA = 'https://wa.me/971585785819'

SOLUTIONS = [
    {'slug': 'websites', 'name': 'Websites', 'short': 'Fast, phone-first sites people trust.', 'url': '/solutions/websites',
     'icon': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><path d="M7 6.5h.01"/>'},
    {'slug': 'paid-ads', 'name': 'Paid ads', 'short': 'Campaigns judged on bookings.', 'url': '/solutions/paid-ads',
     'icon': '<path d="M3 17l6-6 4 4 8-8"/><path d="M14 7h7v7"/>'},
    {'slug': 'search-and-ai', 'name': 'Search and AI', 'short': 'Found on Google and in AI answers.', 'url': '/solutions/search-and-ai',
     'icon': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>'},
    {'slug': 'automation', 'name': 'Automation', 'short': 'Every lead followed up.', 'url': '/solutions/automation',
     'icon': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'},
]
INDUSTRIES = [
    {'slug': 'clinics', 'name': 'Clinics and health', 'short': 'Full diaries from search, ads and WhatsApp.', 'url': '/industries/clinics',
     'icon': '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>'},
    {'slug': 'real-estate', 'name': 'Real estate', 'short': 'Viewings booked by serious buyers.', 'url': '/industries/real-estate',
     'icon': '<path d="M4 21V9l8-6 8 6v12"/><path d="M9 21v-6h6v6"/>'},
    {'slug': 'interior-design', 'name': 'Interior design', 'short': 'Enquiries from clients with real budgets.', 'url': '/industries/interior-design',
     'icon': '<path d="M5 11V8a2 2 0 012-2h10a2 2 0 012 2v3"/><path d="M3 11h18v5H3z"/><path d="M6 16v3M18 16v3"/>'},
    {'slug': 'law-firms', 'name': 'Law firms', 'short': 'Consultations from people ready to act.', 'url': '/industries/law-firms',
     'icon': '<path d="M12 4v16M7 20h10"/><path d="M5 7h14"/><path d="M5 7l-3 6h6zM19 7l-3 6h6z"/>'},
]
BY = {i['slug']: i for i in SOLUTIONS + INDUSTRIES}

# ---------- building blocks ----------
def chip(text):
    return '<div class="chip"><i></i>' + text + '</div>'

def crumb(parent, parent_url, name):
    return '<div class="chip rise"><i></i><a href="' + parent_url + '">' + parent + '</a><span class="sep">/</span>' + name + '</div>'

def hero(parent, parent_url, name, h1, side, img, panel, panel_pos, wa_text):
    return ('<section class="wrap ph">\n' + crumb(parent, parent_url, name) + '\n'
        '<div class="ph-grid">\n<h1 class="rise d1">' + h1 + '</h1>\n'
        '<div class="ph-side rise d2"><p>' + side + '</p>\n<div class="row"><a class="btn dark" href="#start">Book a call ' + ARR + '</a>'
        '<a class="btn" href="' + WA + '?text=' + wa_text + '">WhatsApp</a></div></div>\n</div>\n</section>\n'
        '<div class="wrap"><div class="band grow"><img src="/assets/photos/' + img + '" alt="" class="px">\n'
        '<div class="panel" style="' + panel_pos + '">' + panel + '</div></div></div>\n')

def panel_list(title, items, right=''):
    rows = ''.join('<div style="display:flex;gap:8px;align-items:center;font-size:12px;color:#111111"><span style="width:18px;height:18px;border-radius:4px;background:#111111;color:#ffffff;display:inline-flex;align-items:center;justify-content:center;flex:none">' + CHECK + '</span>' + t + '</div>' for t in items)
    return ('<div style="display:flex;justify-content:space-between;color:#55565a"><span>' + title + '</span><span>' + right + '</span></div>' + rows)

def tiles(ch, h2, intro, items):
    cells = ''.join('<div><span class="n">%02d</span><h3>%s</h3><p>%s</p></div>' % (k + 1, t, d) for k, (t, d) in enumerate(items))
    return ('<section class="wrap sec">\n' + chip(ch) + '\n<h2 class="sv">' + h2 + '</h2>\n<p class="intro sv">' + intro + '</p>\n'
        '<div class="tgrid sv">' + cells + '</div>\n</section>\n')

def steps(ch, h2, intro, items):
    cells = ''.join('<div class="sv"><div class="k"><b>%s</b><span>%s</span></div><h3>%s</h3><p>%s</p></div>' % i for i in items)
    return ('<section class="wrap sec">\n' + chip(ch) + '\n<h2 class="sv">' + h2 + '</h2>\n<p class="intro sv">' + intro + '</p>\n'
        '<div class="steps">' + cells + '</div>\n</section>\n')

def rows(ch, h2, intro, items):
    r = ''.join('<div class="sv"><b>%s</b><p>%s</p></div>' % i for i in items)
    return ('<section class="wrap sec"><div class="sp2">\n<div>' + chip(ch) + '\n<h2 class="sv">' + h2 + '</h2>\n<p class="intro sv">' + intro + '</p></div>\n'
        '<div class="rows">' + r + '</div>\n</div></section>\n')

def cards(ch, h2, intro, items):
    c = ''.join('<div class="sv"><span class="tag">%s</span><h3>%s</h3><p>%s</p><div class="fix"><b>What we do</b>%s</div></div>' % i for i in items)
    return ('<section class="wrap sec">\n' + chip(ch) + '\n<h2 class="sv">' + h2 + '</h2>\n<p class="intro sv">' + intro + '</p>\n'
        '<div class="cards">' + c + '</div>\n</section>\n')

def links(ch, h2, intro, items):
    l = ''.join('<a class="sv" href="%s"><b>%s</b><span>%s</span>%s</a>' % (BY[s]['url'], BY[s]['name'], t, GO) for s, t in items)
    return ('<section class="wrap sec">\n' + chip(ch) + '\n<h2 class="sv">' + h2 + '</h2>\n' + ('<p class="intro sv">' + intro + '</p>\n' if intro else '') +
        '<div class="links">' + l + '</div>\n</section>\n')

def faq(items):
    q = ''.join('<details><summary>%s <span class="plus" aria-hidden="true">+</span></summary><p>%s</p></details>' % i for i in items)
    return ('<section class="wrap sec"><div class="sp2">\n<div>' + chip('Questions') + '\n<h2 class="sv">Questions we <span class="focus">often get.</span></h2></div>\n'
        '<div class="faq sv">' + q + '</div>\n</div></section>\n')

CLOSE_LEAD = 'Book a free 20-minute call and we will look at your site, ads and enquiries with you. You leave with the first three fixes, whether or not we work together.'

# ---------- Solutions: Websites ----------
websites = (
    hero('Solutions', '/#services', 'Websites',
         'Websites that turn visits into <span class="focus">booked calls.</span>',
         'We plan, write and build fast, phone-first websites for service businesses in the GCC. Every page answers the questions buyers ask and makes it easy to call, book or message on WhatsApp.',
         's-websites.jpg',
         panel_list('Launch checklist', ['Speed tested on a mid-range phone', 'Every form sends to WhatsApp and email', 'Lead source saved with each enquiry', 'Pages written around real searches'], '4 of 4'),
         'left:24px;top:40px;width:min(290px,calc(100% - 48px))',
         'Hi%20Wasim%2C%20I%27d%20like%20to%20talk%20about%20a%20website.')
    + tiles('What you get',
            'Everything a website needs to <span class="focus">bring in enquiries.</span>',
            'A good-looking site is the starting point, not the goal. Each part below exists to turn a visitor into a conversation with your team.',
            [('Plan and copy', 'We start with your best clients and the questions they ask before buying. Then we write every page in plain language, so visitors know what you do and why to pick you.'),
             ('Design and build', 'Clean, fast pages built for phones first, with your brand applied properly. Your team can change text and images without a developer.'),
             ('Booking and WhatsApp', 'Call, WhatsApp and booking buttons sit where people look for them. Each enquiry reaches your inbox or CRM with the page it came from.'),
             ('Tracking from day one', 'Analytics and conversion tracking go in before launch, not after. You see which pages and channels bring enquiries from the first week.')])
    + steps('How it works',
            'From first call to <span class="focus">live site.</span>',
            'The timeline depends on the number of pages and how quickly content is approved. You get a fixed scope, price and dates before any work starts.',
            [('1.0', 'Discover', 'Plan the pages', 'We review your current site, your competitors and the searches your buyers make. You get a page plan and a list of what each page must answer.'),
             ('2.0', 'Write', 'Copy, then design', 'Words come first, so the design fits the message. You review real pages with real content, not empty templates.'),
             ('3.0', 'Build', 'Build and test', 'We build the site, connect forms and tracking, and test on phones and slow connections. Nothing goes live until every enquiry route works.'),
             ('4.0', 'Improve', 'Launch and learn', 'After launch we watch which pages bring enquiries and where people drop off. Fixes go in based on the numbers, not on opinions.')])
    + rows('Measured on enquiries',
           'Numbers you can <span class="focus">act on.</span>',
           'We report on what brings in business, not on visits alone. Each month you get a short summary in plain language with the next fixes.',
           [('Enquiries by page', 'Which pages start calls, WhatsApp chats and form fills. This shows where to add content and what to cut.'),
            ('Source of each lead', 'Search, ads, social or direct, saved with every enquiry. You can see which channel deserves more budget.'),
            ('Booking rate', 'How many enquiries turn into a call or visit booked. This is the number that pays for the site.'),
            ('Speed and errors', 'Load time on phones, plus any broken forms or links. Problems get fixed before they cost you leads.')])
    + links('Works well with',
            'Pair it with <span class="focus">the rest of the system.</span>', '',
            [('paid-ads', 'Send paid traffic to pages built to convert it, and judge campaigns on bookings.'),
             ('search-and-ai', 'Get the new pages found on Google and named in AI answers for your field.'),
             ('automation', 'Reply to every website enquiry in seconds, day or night, and follow up for you.')])
    + faq([('Who owns the website?', 'You do. The domain, content and design files sit in your name, and you get every login at handover.'),
           ('What do you need from us?', 'A kick-off call, plus access to your current site and analytics if you have them. After that, mostly quick approvals on the page plan, copy and design.'),
           ('Can you redesign our current site instead?', 'Yes, and it is often the better route. We first check what already brings enquiries, so we keep what works and rebuild what does not.'),
           ('What happens after launch?', 'We can keep improving the site each month, or hand it over fully to your team. Either way, your team can update text and images without a developer.')])
)

# ---------- Industries: Clinics and health ----------
clinic_panel = ('<div style="display:flex;justify-content:space-between;color:#55565a"><span>Clinic dashboard</span><span>This week</span></div>'
    '<div style="color:#6e6f74;display:flex;align-items:center;gap:6px"><span class="live-dot" aria-hidden="true"></span>Just now</div>'
    '<div style="display:flex;gap:8px"><span aria-hidden="true">•</span>Missed calls now get a WhatsApp reply</div>'
    '<div style="display:flex;gap:8px"><span aria-hidden="true">•</span>Whitening ads bring most bookings</div>'
    '<div style="display:flex;gap:8px"><span aria-hidden="true">•</span>Review request sent after each visit</div>')

clinics = (
    hero('Industries', '/#industries', 'Clinics and health',
         'Marketing for clinics that keeps <span class="focus">the diary full.</span>',
         'Patients compare clinics on their phone, often late in the evening, and book with whoever replies first. We connect your ads, search and WhatsApp so every enquiry gets an answer and every booking is traced to its source.',
         'hero-2.jpg', clinic_panel, 'right:24px;bottom:32px;width:min(280px,calc(100% - 48px))',
         'Hi%20Wasim%2C%20I%27d%20like%20to%20talk%20about%20marketing%20for%20our%20clinic.')
    + cards('Where clinics lose patients',
            'Most clinics don\'t need more traffic. <span class="focus">They need fewer leaks.</span>',
            'Before spending more on ads, we look at what happens to the enquiries you already get. These three gaps come up again and again.',
            [('After hours', 'Missed calls and slow replies', 'Many enquiries arrive after reception closes or during the busiest hours. By the next morning, the patient has often booked somewhere else.',
              'An instant WhatsApp reply offers booking times straight away. If the patient goes quiet, a polite follow-up goes out the next day.'),
             ('Paid ads', 'Ads judged on clicks', 'Clicks and impressions look good in reports but do not fill appointments. Without booking data, budget keeps flowing to the wrong treatments.',
              'We trace each booking back to the campaign that brought it. Budget then moves to the treatments that actually book.'),
             ('Reputation', 'Reviews nobody asks for', 'Happy patients rarely leave a review unless asked at the right moment. Meanwhile, clinics with more reviews win the map results.',
              'A review request goes out after each visit, timed and worded to feel personal. Unhappy feedback comes to you first, so you can resolve it.')])
    + links('What we set up',
            'One system, <span class="focus">four parts.</span>',
            'Each part works on its own, but they work best together. You get one team and one report instead of four suppliers.',
            [('websites', 'Treatment pages that answer patient questions, with booking and WhatsApp on every page.'),
             ('paid-ads', 'Google and Meta campaigns per treatment, reported on bookings rather than clicks.'),
             ('search-and-ai', 'Found on Google Maps, in search, and when patients ask AI assistants for a clinic nearby.'),
             ('automation', 'Instant replies, appointment reminders and review requests that run day and night.')])
    + steps('Your first 90 days',
            'A clear plan for <span class="focus">the first quarter.</span>',
            'We fix the leaks first, because that recovers patients you are already paying for. Growth work comes next, once tracking shows what is worth scaling.',
            [('1.0', 'Weeks 1 to 2', 'Audit', 'We check reply times, tracking, ads and your Google profile. You get a written plan with weekly numbers to watch.'),
             ('2.0', 'Weeks 3 to 4', 'Fix the leaks', 'Instant WhatsApp replies, call tracking and booking data go live. From here, every enquiry has a source and an owner.'),
             ('3.0', 'Month 2', 'Grow what works', 'Campaigns are rebuilt around the treatments that book. Treatment pages and reviews start lifting search visibility.'),
             ('4.0', 'Month 3', 'Scale and report', 'Budget moves to the channels with the lowest cost per booking. You get a clear view of what to do in the next quarter.')])
    + faq([('Can you help with health advertising approvals?', 'In the UAE, medical ads usually need approval from the relevant health authority before they run. We prepare ads and landing pages with that process in mind and work with your team on the submission.'),
           ('Do you work with single clinics or groups?', 'Both. For groups, we set up reporting per branch and per treatment, so each manager sees their own numbers.'),
           ('Will you handle patient records?', 'No. Enquiries go to systems you control, such as your inbox, CRM or booking software, and we set up access on your accounts.'),
           ('How soon will we see more bookings?', 'Fixing reply times and tracking recovers enquiries you already get, so it is the fastest win. New campaigns and search work build on that over the following months.')])
)

# ---------- Privacy ----------
privacy = '''<section class="wrap ph">
<div class="chip rise"><i></i>Legal</div>
<div class="ph-grid"><h1 class="rise d1">Privacy <span class="focus">policy.</span></h1>
<div class="ph-side rise d2"><p>Last updated 5 November 2026. This page explains what we collect through this website, why we collect it and what you can ask us to do with it.</p></div></div>
</section>
<section class="wrap" style="padding-top:64px"><div class="doc">
<h2>Who we are</h2>
<p>SanityAI is a marketing business of Safia Saif LLC, based in Dubai, United Arab Emirates. For anything about your data, email <a href="mailto:work@sanity.ai">work@sanity.ai</a> and a person will reply.</p>
<h2>What we collect</h2>
<p>We only collect what you choose to send us through the forms on this site or by contacting us directly. We do not use advertising trackers or analytics cookies on this website.</p>
<ul>
<li>Callback request: your phone number, whether you prefer WhatsApp or a call, and the page you were on.</li>
<li>Free guide: your work email address and the page you were on.</li>
<li>Newsletter: your email address.</li>
<li>Messages you send us by email or WhatsApp, including anything you choose to share in them.</li>
</ul>
<h2>How we use it</h2>
<p>We use your details to reply to you, send the guide you asked for, and send the newsletter if you subscribed. We do not sell your details or share them with other businesses for their own marketing.</p>
<h2>Services that help us run the site</h2>
<p>A small number of providers process data on our behalf so the site can work. Each one only receives what it needs for its task.</p>
<ul>
<li>Vercel hosts the website and keeps standard server logs, such as IP address and browser type, for security and reliability.</li>
<li>Resend delivers the emails that our forms send, including the guide.</li>
<li>Google Fonts serves the typefaces on this site, which means your browser connects to Google when a page loads.</li>
<li>WhatsApp, run by Meta, handles any chat you start with us through a WhatsApp link.</li>
</ul>
<h2>Storage on your device</h2>
<p>The site saves a few small settings in your browser's local storage, such as whether you closed or filled in a popup and when it may show again. These settings stay on your device, are not sent to us and can be cleared in your browser at any time.</p>
<h2>How long we keep it</h2>
<p>We keep enquiry emails for as long as they are useful for our conversation with you, and delete them on request. Newsletter addresses are kept until you unsubscribe or ask us to remove them.</p>
<h2>Your choices</h2>
<p>You can ask to see the details we hold about you, correct them or have them deleted. Email <a href="mailto:work@sanity.ai">work@sanity.ai</a> from the address you used, or tell us the phone number you gave, and we will act on it.</p>
<h2>Changes to this policy</h2>
<p>If we change how we handle data, we will update this page and the date at the top. Significant changes will also be mentioned in the newsletter.</p>
</div></section>
'''

PAGES = [
    {'file': 'solutions/websites.html', 'path': '/solutions/websites',
     'title': 'Websites | SanityAI', 'desc': 'Fast, phone-first websites for GCC service businesses, built to turn visits into calls, WhatsApp chats and bookings.',
     'body': websites, 'close': {'h2': 'Let\'s plan a website that <span class="focus">gets you booked.</span>', 'lead': CLOSE_LEAD, 'img': 'proof.jpg',
     'wa': 'Hi%20Wasim%2C%20I%27d%20like%20to%20book%20a%20call%20about%20a%20website.'}},
    {'file': 'industries/clinics.html', 'path': '/industries/clinics',
     'title': 'Marketing for clinics in Dubai | SanityAI', 'desc': 'Ads, search, websites and WhatsApp automation for clinics, measured on bookings rather than clicks.',
     'body': clinics, 'close': {'h2': 'Let\'s find where your clinic <span class="focus">loses bookings.</span>', 'lead': CLOSE_LEAD, 'img': 'night-fog.jpg',
     'wa': 'Hi%20Wasim%2C%20I%27d%20like%20to%20book%20a%20call%20about%20our%20clinic.'}},
    {'file': 'privacy.html', 'path': '/privacy',
     'title': 'Privacy policy | SanityAI', 'desc': 'How SanityAI handles the details you share through this website.',
     'body': privacy, 'close': {'h2': 'Questions about <span class="focus">your data?</span>', 'lead': 'Email work@sanity.ai and a person will reply. We can show, correct or delete the details we hold about you.', 'img': 'dunes.jpg',
     'wa': 'Hi%2C%20I%20have%20a%20question%20about%20my%20data.'}},
]

# =================== Remaining Solutions ===================
def wa(t):
    from urllib.parse import quote
    return quote(t)

def close(h2, img, topic):
    return {'h2': h2, 'lead': CLOSE_LEAD, 'img': img, 'wa': wa("Hi Wasim, I'd like to book a call about " + topic + ".")}

chat_panel = ('<div style="display:flex;justify-content:space-between;color:#55565a"><span>WhatsApp</span><span>11:42 pm</span></div>'
    '<div style="align-self:flex-start;max-width:85%;padding:8px 10px;border-radius:8px 8px 8px 2px;background:#f0f0ee;color:#33343a;line-height:1.45">Hi, do you have anything available this week?</div>'
    '<div style="align-self:flex-end;max-width:85%;padding:8px 10px;border-radius:8px 8px 2px 8px;background:#111111;color:#ffffff;line-height:1.45">Thanks for reaching out. Here are the next free times, tap one to book.</div>'
    '<div style="color:#6e6f74;display:flex;align-items:center;gap:6px"><span class="live-dot" aria-hidden="true"></span>Lead saved with its source</div>')

ask_panel = ('<div style="color:#55565a">Asked in an AI assistant</div>'
    '<div style="padding:9px 10px;border-radius:6px;background:#f3f2f8;color:#33343a;line-height:1.45">Which interior studio in Dubai handles full villa renovations?</div>'
    '<div style="display:flex;gap:8px;align-items:center;color:#111111"><span class="live-dot" aria-hidden="true"></span>Goal: your business named in the answer</div>')

report_panel = ('<div style="color:#55565a">Prepare a report for <span style="padding:2px 6px;border-radius:4px;background:#ece9f6;color:#4b3f8f">off-plan launch</span></div>'
    '<div style="padding:9px 10px;border-radius:6px;background:#f3f2f8;color:#33343a;line-height:1.45">Enquiries by source, cost per viewing booked and which ads to scale next week.</div>')

paid_ads = (
    hero('Solutions', '/#services', 'Paid ads', 'Paid ads judged on <span class="focus">bookings, not clicks.</span>',
         'We run Google, Meta, LinkedIn and TikTok campaigns for service businesses in the GCC. Every campaign is tracked to the enquiries and sales it brings, so budget goes where it pays.',
         's-paid-ads.jpg', panel_list('Weekly ads review', ['Bookings traced to each campaign', 'Budget moved to the best cost per lead', 'Wasted search terms removed', 'New ad versions tested'], 'Monday'),
         'left:24px;top:40px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about our ads."))
    + tiles('What you get', 'Campaigns built around <span class="focus">what you sell.</span>',
            "We start from your offer and your margins, not from the platform's suggestions. The four parts below are included in every account we run.",
            [('Tracking that holds up', 'Calls, WhatsApp chats and forms are tracked as conversions before we spend. Sales data goes back to Google and Meta, so they learn from real buyers.'),
             ('Clear campaign structure', "Campaigns are split by service, area and intent, so you can see what each one returns. Broad campaigns get firm limits so they don't eat the budget."),
             ('Ads and landing pages', 'We write and design the ads and the pages they lead to. Each version is tested, and the weaker one is switched off.'),
             ('Weekly management', 'Bids, budgets, search terms and audiences are checked every week. You get a short note on what changed and why.')])
    + steps('How it works', 'How we take over <span class="focus">an account.</span>',
            "Most businesses come to us with ads already running. We keep what works, fix tracking first and rebuild in stages, so results don't drop while things change.",
            [('1.0', 'Audit', 'Review the account', 'We go through your campaigns, tracking and recent spend line by line. You get a written list of what to keep, fix and stop.'),
             ('2.0', 'Track', 'Fix the tracking', 'Conversions are set up for calls, chats and forms, then checked against real enquiries. From here on, every number in the report means something.'),
             ('3.0', 'Rebuild', 'Restructure', 'Campaigns are rebuilt around your services and the searches that bring buyers. Budget shifts gradually toward what the data supports.'),
             ('4.0', 'Grow', 'Scale what works', 'Once cost per lead is steady, budget rises on the best campaigns and new channels are tested. Spend only grows when the numbers justify it.')])
    + rows('Measured on enquiries', 'A report you can <span class="focus">read in five minutes.</span>',
           'Platform dashboards show hundreds of numbers. We send the few that matter, in plain language, with the next steps.',
           [('Cost per enquiry', 'What you pay for each call, chat or form, by campaign. This is the main number we manage to.'),
            ('Cost per booking', 'What each booked call, visit or sale costs once enquiries are followed up. This shows which campaigns actually pay.'),
            ('Spend by intent', 'How much goes to people ready to buy versus people still browsing. Both have a place, but the split should be deliberate.'),
            ('Wasted spend', 'Search terms, placements and audiences that cost money without results. These are cut every week.')])
    + links('Works well with', 'Pair it with <span class="focus">the rest of the system.</span>', '',
            [('websites', 'Landing pages built for each campaign, so paid traffic turns into enquiries.'),
             ('automation', 'Instant replies to ad enquiries, which matters most for leads that arrive at night.'),
             ('search-and-ai', 'Visibility in search that lowers how much you depend on paid clicks over time.')])
    + faq([('What budget do we need to start?', 'It depends on your market and what a new client is worth to you. On the first call we look at your numbers and suggest a test budget that can show results without risking too much.'),
           ('Which platforms do you run?', 'Google, Meta, LinkedIn and TikTok, chosen by where your buyers spend their time. Most service businesses start with Google search and one social channel, then expand.'),
           ('Who owns the ad accounts?', 'You do. We work inside accounts in your name, so the history and data stay with you.'),
           ('How long before we see results?', 'Fixing tracking and wasted spend can improve the numbers within the first weeks. Rebuilt campaigns need a few weeks of data before costs settle.')])
)

search_ai = (
    hero('Solutions', '/#services', 'Search and AI', 'Found on Google and <span class="focus">named in AI answers.</span>',
         'More buyers now ask ChatGPT, Gemini and Perplexity who to hire, alongside searching on Google. We make sure your business shows up in both, with pages and facts these tools can trust.',
         's-search.jpg', ask_panel, 'right:24px;bottom:32px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about search and AI visibility."))
    + tiles('What you get', 'Visibility that <span class="focus">builds over time.</span>',
            'Paid ads stop the day the budget stops. Search work keeps paying back, because pages, reviews and mentions build on each other.',
            [('Technical health', 'Fast pages, clean structure and no errors blocking search engines. This comes first, because everything else depends on it.'),
             ('Pages for real searches', 'One clear page for each service and area, written around the questions buyers ask. Each page is useful enough to earn the click.'),
             ('Google Business Profile', 'Complete details, photos, services and a steady flow of reviews. This is what wins the map results for local searches.'),
             ('Mentions and facts', 'Consistent business details across directories and sites your industry respects. AI assistants build their answers from sources like these.')])
    + steps('How it works', 'How the work <span class="focus">runs each month.</span>',
            'Search is steady work rather than a one-off project. Each month follows the same rhythm, so you always know what was done and what comes next.',
            [('1.0', 'Check', 'Find the gaps', 'We check rankings, your map listing and how AI assistants answer questions in your field. Gaps against competitors become the priorities.'),
             ('2.0', 'Fix', 'Fix the basics', 'Technical issues, missing pages and wrong business details are corrected. Small fixes here often unlock more than new content.'),
             ('3.0', 'Write', 'Publish and improve', 'New pages are written and weak ones improved, based on what buyers search for. Every page ends with a clear way to enquire.'),
             ('4.0', 'Earn', 'Build trust', 'Reviews, mentions and listings grow steadily on sites that matter. This is what makes Google and AI assistants confident to recommend you.')])
    + rows('Measured on enquiries', 'Tracked to <span class="focus">enquiries.</span>',
           "Rankings are useful, but they don't pay the bills on their own. We report on the visits and enquiries that search actually brings.",
           [('Enquiries from search', 'Calls, chats and forms from Google search and maps, tracked apart from ads. This is the number search work is judged on.'),
            ('Rankings that matter', 'Positions for the searches that bring buyers, not hundreds of vanity terms. You see movement on the ones tied to revenue.'),
            ('AI answer checks', 'Each month we ask the main AI assistants the questions your buyers ask. You see who gets named and how that changes.'),
            ('Map performance', 'Views, calls and direction requests from your Google Business Profile. For local businesses, this is often the biggest source of enquiries.')])
    + links('Works well with', 'Pair it with <span class="focus">the rest of the system.</span>', '',
            [('websites', 'A fast, well-structured site gives search work a solid base to build on.'),
             ('paid-ads', 'Ads cover the searches you cannot rank for yet, while search builds up.'),
             ('automation', 'Instant replies make sure the new enquiries from search are never missed.')])
    + faq([('How long does search take to work?', 'Fixes to a site and map listing can show within weeks. Competitive searches usually take several months of steady work, which is why we report on progress every month.'),
           ('Can you guarantee first place on Google?', 'No, and it is worth being careful with anyone who does. We can promise the work, the reporting and a clear view of what is moving.'),
           ('How does a business get into AI answers?', 'AI assistants lean on clear pages, consistent business details and mentions on sites they trust. We work on those same signals and check the answers each month.'),
           ('Do you write the content?', 'Yes. We write pages and articles based on what your buyers ask, and you approve everything before it goes live.')])
)

automation = (
    hero('Solutions', '/#services', 'Automation', 'Every enquiry answered, <span class="focus">day or night.</span>',
         'Most leads go cold because nobody replied in time. We set up WhatsApp, email and CRM automations that answer in seconds, follow up for you and keep every enquiry in one place.',
         's-automation.jpg', chat_panel, 'left:24px;top:40px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about automation."))
    + tiles('What you get', 'Systems that do the <span class="focus">follow-up for you.</span>',
            'Automation here means simple, reliable steps that save your team time. Each one is built around how your business already sells.',
            [('Instant replies', 'Every WhatsApp message, form and missed call gets an answer within seconds. The reply offers a clear next step, such as booking a time.'),
             ('Follow-up sequences', 'Enquiries that go quiet get polite reminders on a set schedule. Your team only steps in when a person replies.'),
             ('CRM and lead tracking', "Every enquiry lands in your CRM with its source, notes and status. Nothing lives only in someone's phone."),
             ('Reminders and reviews', 'Reminders go out before each appointment, and review requests after it. Both run without anyone having to remember.')])
    + steps('How it works', 'From busy inbox to <span class="focus">clear pipeline.</span>',
            'We map how enquiries move today before building anything. That way the automation fits your team, instead of your team fitting the software.',
            [('1.0', 'Map', 'Map the journey', 'We follow an enquiry from first message to booked client and note every delay. You see exactly where leads are lost today.'),
             ('2.0', 'Write', 'Write the messages', 'Replies and follow-ups are written in your tone of voice. You approve every message before anything goes live.'),
             ('3.0', 'Build', 'Connect the tools', 'WhatsApp Business, website forms, CRM and calendar are linked together. Everything is tested with real enquiries before launch.'),
             ('4.0', 'Tune', 'Watch and adjust', 'We watch reply rates and drop-off points in the first weeks. Messages and timings are adjusted until the flow runs smoothly.')])
    + rows('Measured on enquiries', 'Proof that it <span class="focus">works.</span>',
           'Automation should show its value in plain numbers. These are the ones we track and share with you.',
           [('Time to first reply', 'How long an enquiry waits before getting an answer, day and night. This is the first number we fix.'),
            ('Leads followed up', 'The share of enquiries that receive every planned follow-up. It shows whether anything is slipping through.'),
            ('Booked by automation', 'Calls and visits booked straight from automated messages. This is the work your system does while the team is busy.'),
            ('Source per lead', 'Where each enquiry came from, saved automatically. Your ads and search reports then reflect real outcomes.')])
    + links('Works well with', 'Pair it with <span class="focus">the rest of the system.</span>', '',
            [('websites', 'Forms and WhatsApp buttons on every page feed straight into your automations.'),
             ('paid-ads', 'Ad leads get an instant reply, and booking data goes back to improve the campaigns.'),
             ('search-and-ai', 'Review requests from your automations help lift your map and search visibility.')])
    + faq([('Which tools do you work with?', 'We work with WhatsApp Business, common CRMs and booking tools, and most website builders. If you already use a system, we build around it rather than replace it.'),
           ('Will customers know replies are automated?', 'The aim is a quick, useful answer, not pretending to be a person. Replies hand over to your team as soon as someone needs a human.'),
           ('What if a lead needs a person?', 'Any message that needs judgement goes to your team straight away, with the full conversation attached. Nothing is left waiting in the system.'),
           ('Do we need new software?', 'Usually not. We start with the tools you already pay for and only suggest new ones when they clearly save time or money.')])
)

# =================== Remaining Industries ===================
def plan90(intro, items):
    return steps('Your first 90 days', 'A clear plan for <span class="focus">the first quarter.</span>', intro, items)

def system(items):
    return links('What we set up', 'One system, <span class="focus">four parts.</span>',
                 'Each part works on its own, but they work best together. You get one team and one report instead of four suppliers.', items)

real_estate = (
    hero('Industries', '/#industries', 'Real estate', 'Real estate marketing that <span class="focus">books the viewing.</span>',
         'Buyers and tenants send enquiries to several agents at once and go with whoever responds best. We connect your listings, ads and WhatsApp so every lead gets a fast reply and every viewing is traced to its source.',
         'sector.jpg', report_panel, 'right:24px;bottom:32px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about real estate marketing."))
    + cards('Where agencies lose buyers', 'Leads are expensive. <span class="focus">Losing them is worse.</span>',
            'Before raising budgets, we look at what happens after an enquiry arrives. These three gaps cost agencies the most.',
            [('Response time', 'Slow first replies', 'Portal and ad leads often contact several agents within minutes. The first useful reply has the best chance of winning the viewing.',
              'An instant WhatsApp reply shares the listing details and viewing times. The right agent is notified at the same moment.'),
             ('Lead quality', 'Budget spent on browsers', 'Broad campaigns bring plenty of enquiries from people who are years away from buying. Agents then spend their days on calls that go nowhere.',
              'Ads and forms qualify on budget, timing and area before an agent calls. Deal data goes back to the platforms so they find more real buyers.'),
             ('Attribution', 'No idea which source sells', 'Leads come from portals, ads, social and referrals, but deals are rarely traced back. Budget decisions end up based on gut feel.',
              'Every lead is saved with its source and followed through to viewing and deal. You see which channels actually close.')])
    + system([('websites', 'Project and area pages that answer buyer questions, with WhatsApp and viewing requests built in.'),
              ('paid-ads', 'Campaigns per project and buyer type, reported on viewings booked rather than leads alone.'),
              ('search-and-ai', 'Found when buyers search for areas and projects, and when they ask AI assistants for an agent.'),
              ('automation', 'Instant replies, lead routing to the right agent and follow-ups that keep buyers warm.')])
    + plan90('We fix lead handling first, because that recovers buyers you are already paying for. Then we grow the channels that bring viewings.',
             [('1.0', 'Weeks 1 to 2', 'Audit', 'We review your campaigns, portal leads, reply times and tracking. You get a written plan with weekly numbers to watch.'),
              ('2.0', 'Weeks 3 to 4', 'Fix lead handling', 'Instant replies, lead routing and source tracking go live. Every lead now has an owner and a next step.'),
              ('3.0', 'Month 2', 'Rebuild campaigns', 'Campaigns are rebuilt around the projects and buyer types that convert. Weak audiences and placements are cut.'),
              ('4.0', 'Month 3', 'Scale and report', 'Budget moves to the sources with the lowest cost per viewing. You get a clear plan for the next launch or quarter.')])
    + faq([('Do you work with developers or brokerages?', 'Both. Developers usually need launch campaigns per project, while brokerages need a steady flow of leads across listings, so we plan for each differently.'),
           ('Can you run campaigns for off-plan launches?', 'Yes. We plan launches with landing pages, lead qualification and reporting by cost per viewing, so you can adjust while the launch is live.'),
           ('What about advertising permits?', 'Property ads in Dubai usually need an advertising permit through the Dubai Land Department. We work with the permits your team holds and show permit details on ads where required.'),
           ('Will this work alongside the portals?', 'Yes. Portals stay part of the mix, and we add channels you control, so you depend less on any single source of leads.')])
)

interior = (
    hero('Industries', '/#industries', 'Interior design', 'Interior design marketing that wins <span class="focus">the right projects.</span>',
         'Clients for interior projects take their time, compare portfolios and look for proof of taste and reliability. We help you show your best work, reach people with real budgets and turn enquiries into consultations.',
         'mono-facade.jpg', panel_list('New enquiry', ['Villa renovation, Dubai Hills', 'Budget and timeline shared on the form', 'Portfolio viewed before enquiring', 'Consultation offered on WhatsApp'], 'Just now'),
         'left:24px;top:40px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about marketing for our design studio."))
    + cards('Where studios lose projects', 'Great work is not enough. <span class="focus">It has to be found.</span>',
            'Many studios have a strong portfolio and an unpredictable flow of enquiries. These three gaps often explain why.',
            [('Portfolio', 'A portfolio without a story', "Beautiful photos alone don't tell a client what you did, for whom and at what scale. Visitors leave without knowing if you suit their project.",
              'Each project page explains the brief, the approach and the result. A clear next step invites a consultation.'),
             ('Lead quality', 'Enquiries without budgets', 'Open forms attract people looking for free ideas or very small jobs. Your team spends hours on calls that never become projects.',
              'Forms and ads ask about project type, size and budget up front. Your team spends its time on the enquiries worth it.'),
             ('Long decisions', 'Leads that go quiet', 'Interior clients often take weeks or months to decide. Without follow-up, they forget which studio impressed them first.',
              'Gentle follow-ups share relevant projects over the following weeks. When the client is ready, your studio is still front of mind.')])
    + system([('websites', 'Portfolio and service pages that show your work properly and invite a consultation.'),
              ('paid-ads', 'Meta and Google campaigns aimed at homeowners and businesses with real budgets.'),
              ('search-and-ai', 'Found when people search for designers in their area, and when they ask AI assistants for a recommendation.'),
              ('automation', 'Qualifying questions, consultation booking and follow-ups that keep long decisions moving.')])
    + plan90('We start with how your work is presented and how enquiries are handled. Then we bring in more of the right people.',
             [('1.0', 'Weeks 1 to 2', 'Audit', 'We review your site, portfolio, social channels and enquiry handling. You get a written plan with weekly numbers to watch.'),
              ('2.0', 'Weeks 3 to 4', 'Fix the basics', 'Enquiry forms, WhatsApp replies and tracking are set up properly. Your best projects are rewritten to show the brief and the result.'),
              ('3.0', 'Month 2', 'Reach the right clients', 'Campaigns and content reach homeowners and businesses that match your typical project. Unsuitable enquiries are filtered out early.'),
              ('4.0', 'Month 3', 'Scale and report', 'Budget moves to the channels bringing consultations. You get a clear plan for the next quarter.')])
    + faq([('Do you work with residential or commercial studios?', 'Both. Homeowners and business clients search and decide in different ways, so we plan the channels for each accordingly.'),
           ("We don't have professional photos of every project. Is that a problem?", 'Not at the start. We begin with your strongest projects and plan how to capture new ones properly as they finish.'),
           ('Can you also manage our Instagram?', 'Our focus is the content and campaigns that bring enquiries. We can talk through what your social channels need on the first call.'),
           ('How do you filter out small jobs?', 'Forms, ads and replies ask about project type, size and budget early. Enquiries outside your range get a polite reply, and your team focuses on the rest.')])
)

law = (
    hero('Industries', '/#industries', 'Law firms', 'Marketing for law firms that brings <span class="focus">the right cases.</span>',
         'People looking for a lawyer are often stressed, short on time and comparing several firms. We help you appear when they search, answer them quickly and show why your firm is the safe choice.',
         'hero-1.jpg', panel_list('Consultation requests', ['Employment matter, replied to at once', 'Source saved: Google search', 'Matched to the right lawyer', 'Consultation booked for Thursday'], 'Today'),
         'right:24px;bottom:32px;width:min(290px,calc(100% - 48px))', wa("Hi Wasim, I'd like to talk about marketing for our firm."))
    + cards('Where firms lose clients', 'Clients choose quickly. <span class="focus">Firms often reply slowly.</span>',
            'Legal clients rarely browse for long once they decide to act. These three gaps decide whether they call you or the next firm.',
            [('Response', 'Enquiries waiting for a reply', 'Messages sent in the evening or at weekends often wait until the next working day. By then, the client may have spoken to another firm.',
              'An instant reply confirms receipt and offers consultation times. Urgent matters are flagged to the right lawyer straight away.'),
             ('Trust', "Pages that don't build confidence", "Generic practice pages make every firm look the same. Clients can't tell who handles matters like theirs.",
              'Clear practice area pages explain the process, the likely steps and who will handle the case. Clients arrive at the call already informed.'),
             ('Lead quality', "Calls about matters you don't take", 'Broad ads and vague pages bring enquiries outside your practice areas. Lawyers then lose billable time screening them.',
              'Ads, pages and forms focus on the matters you want. Enquiries are sorted by practice area before anyone calls back.')])
    + system([('websites', 'Practice area pages that explain the process clearly and make booking a consultation easy.'),
              ('paid-ads', 'Search campaigns per practice area, reported on consultations booked rather than clicks.'),
              ('search-and-ai', 'Found when people search for legal help, and when they ask AI assistants which firm to call.'),
              ('automation', 'Instant replies, intake questions and consultation booking that work outside office hours.')])
    + plan90('We fix intake first, because it recovers enquiries you already receive. Then we grow visibility for the practice areas that matter most to you.',
             [('1.0', 'Weeks 1 to 2', 'Audit', 'We review your site, campaigns, listings and how enquiries are handled today. You get a written plan with weekly numbers to watch.'),
              ('2.0', 'Weeks 3 to 4', 'Fix intake', 'Instant replies, intake questions and source tracking go live. Each enquiry reaches the right lawyer with the details they need.'),
              ('3.0', 'Month 2', 'Grow priority areas', 'Pages and campaigns are built around your priority practice areas. Searches that bring the wrong matters are excluded.'),
              ('4.0', 'Month 3', 'Scale and report', 'Budget moves to the channels with the lowest cost per consultation. You get a clear plan for the next quarter.')])
    + faq([('Do you follow the rules on legal advertising?', 'Rules on how firms can advertise vary by jurisdiction and regulator. We keep claims factual, avoid promises about outcomes and have your team approve all content before it goes live.'),
           ('Which practice areas does this suit?', 'The approach works for most practice areas, from corporate and employment to family and property law. What changes is how clients in each area search and decide.'),
           ('How are enquiries kept confidential?', 'Enquiries go only to systems your firm controls, such as your inbox or case management tool. We set up access on your accounts and keep message content out of reports.'),
           ('Can you help an individual lawyer as well as a firm?', 'Yes. For individual practitioners, the focus is usually a strong profile, clear practice pages and steady reviews.')])
)

PAGES += [
    {'file': 'solutions/paid-ads.html', 'path': '/solutions/paid-ads', 'title': 'Paid ads | SanityAI',
     'desc': 'Google, Meta, LinkedIn and TikTok campaigns for GCC service businesses, judged on bookings rather than clicks.',
     'body': paid_ads, 'close': close("Let's see where your <span class=\"focus\">ad budget goes.</span>", 'hero-3.jpg', 'our ads')},
    {'file': 'solutions/search-and-ai.html', 'path': '/solutions/search-and-ai', 'title': 'Search and AI visibility | SanityAI',
     'desc': 'SEO, Google Business Profile and visibility in ChatGPT, Gemini and Perplexity answers, tracked to enquiries.',
     'body': search_ai, 'close': close("Let's check how buyers <span class=\"focus\">find you today.</span>", 'sector.jpg', 'search and AI visibility')},
    {'file': 'solutions/automation.html', 'path': '/solutions/automation', 'title': 'WhatsApp and CRM automation | SanityAI',
     'desc': 'Instant WhatsApp replies, follow-ups, reminders and CRM tracking so every enquiry gets an answer, day or night.',
     'body': automation, 'close': close("Let's make sure no lead <span class=\"focus\">waits for a reply.</span>", 'proof.jpg', 'automation')},
    {'file': 'industries/real-estate.html', 'path': '/industries/real-estate', 'title': 'Real estate marketing in Dubai | SanityAI',
     'desc': 'Ads, websites, search and WhatsApp automation for developers and brokerages, measured on viewings booked.',
     'body': real_estate, 'close': close("Let's find where your agency <span class=\"focus\">loses buyers.</span>", 'dunes.jpg', 'real estate marketing')},
    {'file': 'industries/interior-design.html', 'path': '/industries/interior-design', 'title': 'Marketing for interior designers | SanityAI',
     'desc': 'Portfolio sites, campaigns and follow-up for interior design studios, aimed at clients with real budgets.',
     'body': interior, 'close': close("Let's bring your studio <span class=\"focus\">the right projects.</span>", 'hero-1.jpg', 'marketing for our studio')},
    {'file': 'industries/law-firms.html', 'path': '/industries/law-firms', 'title': 'Marketing for law firms | SanityAI',
     'desc': 'Search, ads, practice area pages and intake automation for law firms, measured on consultations booked.',
     'body': law, 'close': close("Let's find where your firm <span class=\"focus\">loses enquiries.</span>", 'night-fog.jpg', 'marketing for our firm')},
]

# =================== Careers ===================
careers = (
    '<section class="wrap ph">\n<div class="chip rise"><i></i>Careers</div>\n'
    '<div class="ph-grid">\n<h1 class="rise d1">Do the best work of your career, <span class="focus">without the agency noise.</span></h1>\n'
    '<div class="ph-side rise d2"><p>SanityAI is a small team in Dubai working on websites, ads, search and automation for service businesses across the GCC. We hire slowly, and only when there is real work for someone good to own.</p>\n'
    '<div class="row"><a class="btn dark" href="mailto:work@sanity.ai?subject=Careers">Send us your work ' + ARR + '</a></div></div>\n</div>\n</section>\n'
    '<div class="wrap"><div class="band grow" style="height:clamp(300px,38vw,520px)"><img src="/assets/photos/glass-roof.jpg" alt="" class="px"></div></div>\n'
    + tiles('How we work', 'What working here <span class="focus">feels like.</span>',
            'We would rather do fewer things properly than many things loudly. These are the habits we look for and try to protect.',
            [('Outcomes over output', 'We judge work by the enquiries and sales it brings, not by hours or slide counts. You will always know which number your work moves.'),
             ('Plain words', 'We write the way we talk to clients, without jargon or filler. If an idea cannot be explained simply, it usually is not ready.'),
             ('Honest numbers', 'We report what happened, including when something did not work. Nobody here gets in trouble for bad news shared early.'),
             ('Ownership', 'You own your accounts and projects from start to finish. That comes with real trust and a direct line to the founder.')])
    + rows('Who we want to hear from', 'Skills we are <span class="focus">always open to.</span>',
           'We do not always have an open role. If your work is strong in one of these areas, we still want to see it, and we keep good people in mind.',
           [('Paid media', 'Google and Meta specialists who can show results measured on bookings or sales. LinkedIn and TikTok experience is a plus.'),
            ('Search and content', 'Writers and SEO people who can explain a complex service in simple language. You care about readers first and rankings second.'),
            ('Automation', 'Builders who know WhatsApp Business, CRMs and booking tools. You like making messy processes simple and reliable.'),
            ('Design and web', 'Designers and developers who build fast, clean sites that work on a phone first. Taste matters, and so does the conversion rate.')])
    + steps('How to apply', 'Three steps, <span class="focus">no cover letter.</span>',
            'We care more about your work than your CV. The process is short, and you will hear back either way.',
            [('1.0', 'Email', 'Send your work', 'Email work@sanity.ai with "Careers" and your area in the subject line. Include two or three pieces of work you are proud of and what you personally did on each.'),
             ('2.0', 'Talk', 'A real conversation', 'If there is a fit, we will set up a call to talk through your work. Expect questions about how you think, not trick questions.'),
             ('3.0', 'Try', 'A small paid task', 'For serious candidates, we agree a short, paid piece of work close to the real job. It shows both sides what working together is like.'),
             ('4.0', 'Decide', 'A clear answer', 'We make a decision quickly and tell you why. If it is not a fit now, we will say so honestly.')])
)

PAGES.append({'file': 'careers.html', 'path': '/careers', 'title': 'Careers | SanityAI',
    'desc': 'Work with SanityAI in Dubai on websites, ads, search and automation for GCC service businesses.',
    'body': careers,
    'close': {'h2': 'Think you would fit? <span class="focus">Show us your work.</span>',
              'lead': 'Email two or three pieces of work you are proud of to work@sanity.ai. Tell us what you did on each one, and what you would do differently now.',
              'img': 'hero-2.jpg',
              'btns': '<a class="btn light" href="mailto:work@sanity.ai?subject=Careers">Email work@sanity.ai ' + ARR + '</a>',
              'chip': 'Careers at SanityAI', 'stats': False}})
