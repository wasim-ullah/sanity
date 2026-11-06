// Contact page form: emails the enquiry to the SanityAI inbox, with reply-to set to the visitor.
const { send, readBody, inbox, dubaiTime } = require('./_send');
const clip = (v, n) => String(v || '').replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, n);
module.exports = async function handler(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ ok: false }); }
  const b = readBody(req);
  if (b.website) return res.status(200).json({ ok: true }); // bot trap
  const name = clip(b.name, 120), email = clip(b.email, 200).toLowerCase(), phone = clip(b.phone, 40);
  const org = clip(b.org, 160), need = clip(b.need, 80), page = clip(b.page, 300);
  const message = String(b.message || '').trim().slice(0, 5000);
  if (!name) return res.status(400).json({ ok: false, error: 'name' });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return res.status(400).json({ ok: false, error: 'email' });
  if (message.length < 10) return res.status(400).json({ ok: false, error: 'message' });
  const lines = ['New enquiry from the contact page.', '', 'Name: ' + name, 'Email: ' + email,
    'Phone: ' + (phone || 'not given'), 'Company: ' + (org || 'not given'), 'Interested in: ' + (need || 'not given'),
    '', 'Message:', message, '', 'Page: ' + page, 'Time: ' + dubaiTime()];
  const r = await send({
    from: 'SanityAI Website <website@reach.sanity.ai>',
    to: [inbox()],
    reply_to: email,
    subject: 'Contact: ' + name + (org ? ' (' + org + ')' : '') + (need ? ', ' + need : ''),
    text: lines.join('\n')
  });
  return res.status(r.ok ? 200 : (r.error ? 500 : 502)).json({ ok: r.ok });
};
