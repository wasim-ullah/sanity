// Shared Resend helper. Needs RESEND_API_KEY in the Vercel project settings.
module.exports.send = async function send(payload) {
  const key = process.env.RESEND_API_KEY;
  if (!key) return { ok: false, error: 'not_configured' };
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + key, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  return { ok: r.ok, status: r.status };
};
module.exports.readBody = function readBody(req) {
  let b = req.body || {};
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  return b;
};
module.exports.inbox = function inbox() { return process.env.SUBSCRIBE_TO || 'work@sanity.ai'; };
module.exports.dubaiTime = function () { return new Date().toLocaleString('en-GB', { timeZone: 'Asia/Dubai' }) + ' (Dubai)'; };
