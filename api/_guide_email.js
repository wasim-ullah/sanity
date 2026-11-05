// Branded HTML email for the AI in marketing guide. Table layout and inline styles for Gmail, Outlook and Apple Mail.
module.exports = function guideEmail(base) {
  const pdf = base + '/assets/guide/sanityai-ai-in-marketing-guide.pdf';
  const wa = 'https://wa.me/971585785819?text=' + encodeURIComponent('Hi Wasim, I read the AI in marketing guide and would like to book the free 20-minute call.');
  const F = "'Altera Sans','Helvetica Neue',Helvetica,Arial,sans-serif";
  const B = "'Helvetica Neue',Helvetica,Arial,sans-serif";
  const H = "'Geist','Helvetica Neue',Helvetica,Arial,sans-serif";
  const S = "'IBM Plex Serif',Georgia,'Times New Roman',serif";
  const item = (n, t) => '<tr><td width="34" valign="top" style="padding:12px 0;border-top:1px solid #e6e6e2;font:500 12px/20px ' + B + ';color:#8a8b90">' + n + '</td><td valign="top" style="padding:12px 0;border-top:1px solid #e6e6e2;font:400 15px/20px ' + B + ';color:#111111">' + t + '</td></tr>';
  const html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><title>Your guide: AI in marketing, without the hype</title>' +
  '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400&family=IBM+Plex+Serif:wght@400&display=swap" rel="stylesheet">' +
  '<style>@font-face{font-family:"Altera Sans";src:url("' + base + '/assets/haze/AlteraSans-Regular.otf") format("opentype");font-weight:400}' +
  'a{color:#111111}@media (max-width:620px){.card{padding:28px 22px !important}.h1{font-size:28px !important;line-height:32px !important}.pad{padding-left:16px !important;padding-right:16px !important}}</style></head>' +
  '<body style="margin:0;padding:0;background:#f3f3f1;-webkit-text-size-adjust:100%">' +
  '<div style="display:none;max-height:0;overflow:hidden;opacity:0">Your copy is attached. Four practical sections and a 30-day plan you can start this week.</div>' +
  '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f3f3f1"><tr><td align="center" class="pad" style="padding:40px 24px">' +
  '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px">' +
  // header
  '<tr><td style="padding:0 4px 22px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>' +
  '<td style="font:400 13px/16px ' + F + ';letter-spacing:4px;text-transform:uppercase;color:#111111">SANITY<span style="display:inline-block;width:1px;height:16px;background:#111111;margin:0 9px 0 5px;vertical-align:-3px"></span>AI</td>' +
  '<td align="right" style="font:400 12px/16px ' + B + ';color:#8a8b90">Free guide</td></tr></table></td></tr>' +
  // cover
  '<tr><td><a href="' + pdf + '"><img src="' + base + '/assets/email/guide-banner.jpg" width="600" alt="AI in marketing, without the hype" style="display:block;width:100%;height:auto;border:0;border-radius:6px 6px 0 0"></a></td></tr>' +
  // card
  '<tr><td class="card" style="background:#ffffff;border-radius:0 0 6px 6px;padding:40px 44px">' +
  '<p style="margin:0 0 12px;font:500 12px/16px ' + B + ';letter-spacing:1.5px;text-transform:uppercase;color:#8a8b90">Your guide</p>' +
  '<h1 class="h1" style="margin:0 0 20px;font:400 36px/40px ' + H + ';letter-spacing:-1.5px;color:#111111">AI in marketing, <span style="font-family:' + S + ';font-weight:400;letter-spacing:-1.6px">without the hype</span></h1>' +
  '<p style="margin:0 0 28px;font:400 16px/25px ' + B + ';color:#3a3b3f">Thank you for requesting the guide. Your copy is attached to this email as a PDF, and you can open it any time with the button below.</p>' +
  '<table role="presentation" cellpadding="0" cellspacing="0"><tr><td bgcolor="#111111" style="border-radius:6px"><a href="' + pdf + '" style="display:inline-block;padding:15px 26px;font:500 15px/18px ' + B + ';color:#ffffff;text-decoration:none;border-radius:6px">Open the guide&nbsp;&nbsp;&#8599;</a></td></tr></table>' +
  '<p style="margin:40px 0 4px;font:500 12px/16px ' + B + ';letter-spacing:1.5px;text-transform:uppercase;color:#8a8b90">What is inside</p>' +
  '<table role="presentation" width="100%" cellpadding="0" cellspacing="0">' +
  item('01', 'Replying to every lead in seconds, day or night') +
  item('02', 'Getting your business recommended in AI answers') +
  item('03', 'Using AI for content that still sounds like you') +
  item('04', 'A 30-day plan you can start straight away') +
  '</table>' +
  '<div style="margin:36px 0 0;padding:24px;background:#f6f6f4;border-radius:6px">' +
  '<p style="margin:0 0 6px;font:500 16px/22px ' + B + ';color:#111111">Want a second opinion on your marketing?</p>' +
  '<p style="margin:0 0 18px;font:400 15px/23px ' + B + ';color:#3a3b3f">Reply to this email or message us on WhatsApp to book a free 20-minute call. We will look at your ads, website and enquiry handling together and point out what to fix first.</p>' +
  '<table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="border:1px solid #111111;border-radius:6px"><a href="' + wa + '" style="display:inline-block;padding:11px 18px;font:500 14px/18px ' + B + ';color:#111111;text-decoration:none">WhatsApp +971 58 578 5819</a></td></tr></table>' +
  '</div>' +
  // signature
  '<table role="presentation" cellpadding="0" cellspacing="0" style="margin-top:36px"><tr>' +
  '<td valign="middle" style="padding-right:14px"><img src="' + base + '/assets/haze/founder.jpg" width="44" height="44" alt="Wasim Ullah" style="display:block;border-radius:50%;object-fit:cover"></td>' +
  '<td valign="middle" style="font:400 14px/20px ' + B + ';color:#111111">Wasim Ullah<br><span style="color:#8a8b90">Founder, SanityAI</span></td></tr></table>' +
  '</td></tr>' +
  // footer
  '<tr><td style="padding:24px 4px 0;font:400 12px/18px ' + B + ';color:#8a8b90">' +
  '<a href="' + base + '" style="color:#55565a;text-decoration:none">sanity.ai</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="mailto:work@sanity.ai" style="color:#55565a;text-decoration:none">work@sanity.ai</a><br><br>' +
  'SanityAI is a business of Safia Saif LLC, Wasl Village, Dubai, United Arab Emirates. You received this email because you requested the guide on sanity.ai.</td></tr>' +
  '</table></td></tr></table></body></html>';
  const text = 'AI in marketing, without the hype\n\nThank you for requesting the guide. Your copy is attached to this email as a PDF, and you can open it any time here:\n' + pdf +
    '\n\nWhat is inside\n01 Replying to every lead in seconds, day or night\n02 Getting your business recommended in AI answers\n03 Using AI for content that still sounds like you\n04 A 30-day plan you can start straight away' +
    '\n\nWant a second opinion on your marketing? Reply to this email or WhatsApp +971 58 578 5819 to book a free 20-minute call. We will look at your ads, website and enquiry handling together and point out what to fix first.' +
    '\n\nWasim Ullah\nFounder, SanityAI\nsanity.ai\n\nSanityAI is a business of Safia Saif LLC, Wasl Village, Dubai, United Arab Emirates.';
  return { html, text, pdf };
};
