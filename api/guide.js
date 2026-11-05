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
  const mail = require('./_guide_email')('https://' + host);
  const pdf = mail.pdf;
  const r = await send({
    from: 'Wasim Ullah <work@reach.sanity.ai>',
    to: [email],
    reply_to: 'work@sanity.ai',
    subject: 'Your guide: AI in marketing, without the hype',
    html: mail.html,
    text: mail.text,
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
