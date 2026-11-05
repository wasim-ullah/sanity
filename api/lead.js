// Callback popup: emails the visitor's number and preferred channel to the SanityAI inbox.
const { send, readBody, inbox, dubaiTime } = require('./_send');
module.exports = async function handler(req, res) {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ ok: false }); }
  const b = readBody(req);
  if (b.company) return res.status(200).json({ ok: true }); // bot trap
  const phone = String(b.phone || '').replace(/[^\d+ ]/g, '').trim().slice(0, 30);
  const channel = b.channel === 'call' ? 'Phone call' : 'WhatsApp';
  const page = String(b.page || '').slice(0, 300);
  if (phone.replace(/[^\d]/g, '').length < 7) return res.status(400).json({ ok: false, error: 'invalid_phone' });
  const wa = 'https://wa.me/' + phone.replace(/[^\d]/g, '');
  const r = await send({
    from: 'SanityAI Website <website@reach.sanity.ai>',
    to: [inbox()],
    subject: 'Contact request: ' + phone + ' (' + channel + ')',
    text: 'A visitor asked to be contacted from the website popup.\n\nNumber: ' + phone + '\nPrefers: ' + channel +
      '\nWhatsApp link: ' + wa + '\nPage: ' + page + '\nTime: ' + dubaiTime()
  });
  return res.status(r.ok ? 200 : (r.error ? 500 : 502)).json({ ok: r.ok });
};
