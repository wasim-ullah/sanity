// Exit popup: emails the AI in Marketing guide to the visitor and notifies the SanityAI inbox.
const { send, readBody, inbox, dubaiTime } = require('./_send');
const FREE = /@(gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|icloud|me|mac|aol|proton|protonmail|gmx|mail|yandex|zoho)\./i;
module.exports = async function handler(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ ok: false }); }
  const b = readBody(req);
  if (b.company) return res.status(200).json({ ok: true });
  const email = String(b.email || '').trim().slice(0, 200);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return res.status(400).json({ ok: false, error: 'invalid_email' });
  if (FREE.test(email)) return res.status(400).json({ ok: false, error: 'work_email_required' });
  const host = req.headers['x-forwarded-host'] || req.headers.host || 'sanity.ai';
  const pdf = 'https://' + host + '/assets/guide/sanityai-ai-in-marketing-guide.pdf';
  const html = '<div style="font-family:Helvetica,Arial,sans-serif;font-size:15px;line-height:1.6;color:#111111;max-width:560px">' +
    '<p style="letter-spacing:4px;font-size:12px;color:#55565a;margin:0 0 24px">SANITY | AI</p>' +
    '<p>Hi,</p>' +
    '<p>Thanks for downloading AI in marketing, without the hype. The guide is attached as a PDF, and you can also open it here: <a href="' + pdf + '" style="color:#111111">AI in marketing guide</a>.</p>' +
    '<p>It covers replying to leads in seconds, getting recommended in AI answers, using AI for content without sounding generic, and a 30-day plan you can start straight away.</p>' +
    '<p>If you would like a second pair of eyes on your own marketing, reply to this email or WhatsApp us on +971 58 578 5819 and we can book a free 20-minute call.</p>' +
    '<p>Wasim Ullah<br>Founder, SanityAI<br><a href="https://sanity.ai" style="color:#111111">sanity.ai</a></p>' +
    '<p style="font-size:12px;color:#6e6f74;margin-top:28px">SanityAI is a business of Safia Saif LLC, Wasl Village, Dubai, United Arab Emirates. You received this because you requested the guide on sanity.ai.</p></div>';
  const r = await send({
    from: 'Wasim Ullah <work@reach.sanity.ai>',
    to: [email],
    reply_to: 'work@sanity.ai',
    subject: 'Your guide: AI in marketing, without the hype',
    html: html,
    text: 'Thanks for downloading AI in marketing, without the hype. Open the guide: ' + pdf + '\n\nReply to this email or WhatsApp +971 58 578 5819 to book a free 20-minute call.\n\nWasim Ullah\nFounder, SanityAI',
    attachments: [{ filename: 'SanityAI - AI in marketing guide.pdf', path: pdf }]
  });
  if (!r.ok) return res.status(r.error ? 500 : 502).json({ ok: false });
  await send({
    from: 'SanityAI Website <website@reach.sanity.ai>',
    to: [inbox()],
    reply_to: email,
    subject: 'Guide download: ' + email,
    text: 'Someone downloaded the AI in marketing guide.\n\nEmail: ' + email + '\nPage: ' + String(b.page || '').slice(0, 300) + '\nTime: ' + dubaiTime() + '\n\nReply to this email to write to them directly.'
  }).catch(function () {});
  return res.status(200).json({ ok: true });
};
