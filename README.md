# SanityAI website

Static site for sanity.ai (the "Haze" design). No build step.

- `index.html`: the whole page (layout, styles, carousel and tile scripts)
- `assets/haze/`: background images, founder photo and the PP Altera Sans logo font
- `assets/social/og-image.png`: link preview image

Deploy on Vercel: import this repository, framework preset "Other", no build command, output directory `.`.

## Newsletter sign-ups

The footer form posts to `api/subscribe.js`, which emails each new subscriber to work@sanity.ai through Resend.
Add `RESEND_API_KEY` in Vercel (Project Settings > Environment Variables), then redeploy.
Optional: `SUBSCRIBE_TO` to send sign-ups to a different inbox.

## Popups and lead emails

- Callback popup (bottom left, after 10 seconds): `api/lead.js` emails the number and preferred channel to work@sanity.ai.
- Exit popup (when a visitor is leaving without contacting us): `api/guide.js` emails the AI in Marketing PDF (`assets/guide/`) to the visitor's work email, with replies going to work@sanity.ai, and notifies work@sanity.ai.
- Preview them any time with `?popup=callback` or `?popup=guide` at the end of the URL.
- All emails need `RESEND_API_KEY` in Vercel. They send from the verified reach.sanity.ai domain.

## Adding pages and posts

All inner pages are generated. Run `python3 tools/build.py` after any change.

- Solutions, industries, careers and privacy content: `tools/pages.py`
- Blog posts: `tools/posts.py` (add an entry to `POSTS`, it appears on /blog and in the sitemap)
- Styles: `tools/base.css` and `tools/site-extra.css` (compiled to `assets/site.css`)
- Logo: `tools/make_logo.py` builds `assets/brand/sanityai-logo.svg` from Altera Sans

Every page gets share previews automatically (Facebook, WhatsApp, LinkedIn, X and others):
`tools/og.py` renders a 1200x630 image at `assets/og/<page>.jpg` with the page photo, its
headline and the logo, and writes the Open Graph and Twitter tags. Only changed pages are
re-rendered. The build needs Python Playwright and Pillow.
