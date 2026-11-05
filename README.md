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
