// Newsletter sign-up: emails each new subscriber to the SanityAI inbox via Resend.
// Needs the RESEND_API_KEY environment variable in Vercel. SUBSCRIBE_TO overrides the inbox.
module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false });
  }
  let body = req.body || {};
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { body = {}; }
  }
  const email = String(body.email || '').trim().slice(0, 200);
  if (body.company) return res.status(200).json({ ok: true }); // bot trap
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ ok: false, error: 'invalid_email' });
  }
  const key = process.env.RESEND_API_KEY;
  if (!key) return res.status(500).json({ ok: false, error: 'not_configured' });
  const to = process.env.SUBSCRIBE_TO || 'work@sanity.ai';
  const when = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Dubai' });
  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: 'Bearer ' + key, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'SanityAI Website <website@reach.sanity.ai>',
        to: [to],
        reply_to: email,
        subject: 'New subscriber: ' + email,
        text: 'Someone subscribed on sanity.ai.\n\nEmail: ' + email + '\nTime: ' + when + ' (Dubai)\n\nReply to this email to write to them directly.'
      })
    });
    if (!r.ok) return res.status(502).json({ ok: false, error: 'send_failed' });
    return res.status(200).json({ ok: true });
  } catch (e) {
    return res.status(502).json({ ok: false, error: 'send_failed' });
  }
};
