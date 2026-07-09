// index.js — Omni Biosystems contact-form backend (Cloud Run + Mailgun)
const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const formData = require('form-data');
const Mailgun = require('mailgun.js');
const { getAutoReply } = require('./templates');

// ── Config (from environment) ─────────────────────────────
const {
  MAILGUN_API_KEY,
  MAILGUN_DOMAIN = 'mg.omni-biosystems.com',
  MAILGUN_API_BASE = 'https://api.mailgun.net', // EU accounts: https://api.eu.mailgun.net
  CONTACT_TO = 'contact@omni-biosystems.com',
  // The visitor-facing auto-reply comes FROM this identity:
  REPLY_FROM = 'Omni Biosystems <contact@omni-biosystems.com>',
  // The internal notification is sent FROM this identity (on the verified sending domain):
  NOTIFY_FROM = 'Omni Biosystems Website <postmaster@mg.omni-biosystems.com>',
  ALLOWED_ORIGINS = 'https://omni-biosystems.com,https://www.omni-biosystems.com',
  PORT = 8080,
} = process.env;

const allowList = ALLOWED_ORIGINS.split(',').map((s) => s.trim()).filter(Boolean);

// ── Mailgun client ────────────────────────────────────────
const mailgun = new Mailgun(formData);
const mg = MAILGUN_API_KEY
  ? mailgun.client({ username: 'api', key: MAILGUN_API_KEY, url: MAILGUN_API_BASE })
  : null;

// ── App ───────────────────────────────────────────────────
const app = express();
app.set('trust proxy', 1); // Cloud Run sits behind a proxy; needed for rate-limit IPs
app.use(express.json({ limit: '25kb' }));

app.use(
  cors({
    origin(origin, cb) {
      // allow same-origin / curl (no origin) and anything on the allow list
      if (!origin || allowList.includes(origin)) return cb(null, true);
      return cb(new Error('Not allowed by CORS'));
    },
    methods: ['POST', 'OPTIONS'],
  })
);

const limiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 5, // 5 submissions per IP per minute
  standardHeaders: true,
  legacyHeaders: false,
  message: { ok: false, error: 'Too many requests. Please try again shortly.' },
});

// ── Helpers ───────────────────────────────────────────────
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const esc = (s = '') =>
  String(s).replace(/[<>&]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]));
const clip = (s = '', n = 5000) => String(s).slice(0, n);

function buildNotification({ name, org, email, topic, message }) {
  const when = new Date().toISOString();
  const text =
    `New contact-form submission — omni-biosystems.com\n\n` +
    `Name:    ${name}\n` +
    `Email:   ${email}\n` +
    `Org:     ${org || '—'}\n` +
    `Type:    ${topic || '—'}\n` +
    `Time:    ${when}\n\n` +
    `Message:\n${message}\n`;
  const html =
    `<h2 style="font-family:Arial,sans-serif;color:#0B1B3A;margin:0 0 12px;">New contact-form submission</h2>` +
    `<table style="font-family:Arial,sans-serif;font-size:14px;color:#243B5E;border-collapse:collapse;">` +
    `<tr><td style="padding:4px 12px 4px 0;color:#7E97B8;">Name</td><td>${esc(name)}</td></tr>` +
    `<tr><td style="padding:4px 12px 4px 0;color:#7E97B8;">Email</td><td>${esc(email)}</td></tr>` +
    `<tr><td style="padding:4px 12px 4px 0;color:#7E97B8;">Org</td><td>${esc(org || '—')}</td></tr>` +
    `<tr><td style="padding:4px 12px 4px 0;color:#7E97B8;">Type</td><td>${esc(topic || '—')}</td></tr>` +
    `<tr><td style="padding:4px 12px 4px 0;color:#7E97B8;">Time</td><td>${when}</td></tr>` +
    `</table>` +
    `<p style="font-family:Arial,sans-serif;font-size:14px;color:#243B5E;white-space:pre-wrap;margin-top:16px;">${esc(message)}</p>`;
  return { text, html };
}

// ── Routes ────────────────────────────────────────────────
app.get('/', (_req, res) => res.status(200).send('ok'));
app.get('/health', (_req, res) => res.json({ ok: true }));

app.post('/contact', limiter, async (req, res) => {
  try {
    const b = req.body || {};

    // Honeypot: real users never fill this hidden field.
    if (b.company_website) return res.json({ ok: true }); // silently accept & drop

    const name = clip((b.name || '').trim(), 200);
    const org = clip((b.org || '').trim(), 200);
    const email = clip((b.email || '').trim(), 254);
    const topic = clip((b.topic || 'Other').trim(), 60);
    const message = clip((b.message || '').trim(), 5000);

    if (!name || !email || !message)
      return res.status(400).json({ ok: false, error: 'Missing required fields.' });
    if (!EMAIL_RE.test(email))
      return res.status(400).json({ ok: false, error: 'Invalid email address.' });

    if (!mg) {
      console.error('MAILGUN_API_KEY not configured');
      return res.status(500).json({ ok: false, error: 'Email service not configured.' });
    }

    // 1) Notify the team (delivered to the Google Group, reply goes to the visitor)
    const note = buildNotification({ name, org, email, topic, message });
    await mg.messages.create(MAILGUN_DOMAIN, {
      from: NOTIFY_FROM,
      to: [CONTACT_TO],
      subject: `New enquiry — ${topic} (${name})`,
      text: note.text,
      html: note.html,
      'h:Reply-To': `${name} <${email}>`,
    });

    // 2) Auto-reply to the visitor (FROM contact@omni-biosystems.com)
    const firstName = name.split(/\s+/)[0];
    const reply = getAutoReply(topic, firstName);
    await mg.messages.create(MAILGUN_DOMAIN, {
      from: REPLY_FROM,
      to: [`${name} <${email}>`],
      subject: reply.subject,
      text: reply.text,
      html: reply.html,
      'h:Reply-To': CONTACT_TO,
    });

    return res.json({ ok: true });
  } catch (err) {
    console.error('contact error:', err && err.message ? err.message : err);
    return res.status(502).json({ ok: false, error: 'Could not send message. Please try again.' });
  }
});

app.listen(PORT, () => console.log(`omni-contact-api listening on :${PORT}`));
