// templates.js
// Persona-specific auto-reply emails for omni-biosystems.com
//
// Layouts (chosen per persona):
//   A "navyBanner"     -> Press, Other
//   B "lightEditorial" -> Investor, Pharma / CRO partner
//   C "apertureBadge"  -> Researcher / KOL
//
// Copy lives in TEMPLATES below — edit freely. `{firstName}` is filled at send time.
// Images must be publicly reachable; ASSET_BASE points at the deployed site.

const ASSET_BASE = (process.env.ASSET_BASE || 'https://omni-biosystems.com').replace(/\/$/, '');
const IMG = {
  lockupNavy: `${ASSET_BASE}/assets/email/lockup-navy.png`,   // white ink on navy
  lockupWhite: `${ASSET_BASE}/assets/email/lockup-white.png`, // navy ink on white
  markWhite: `${ASSET_BASE}/assets/email/mark-white.png`,     // aperture on white
};
const SITE = 'https://omni-biosystems.com';

const SIGNATURE_TEXT =
  `\n\n— The Omni Biosystems Team\n` +
  `OncoMiMIC™ · Automated, AI-powered, chip-based drug discovery\n` +
  `Singapore · omni-biosystems.com`;

const esc = (s = '') =>
  String(s).replace(/[<>&"]/g, (c) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;' }[c]));

const paras = (arr, style) =>
  arr.map((p, i) => `<p style="margin:0 0 ${i === arr.length - 1 ? 24 : 16}px;${style || ''}">${p}</p>`).join('');

const footerBlock = (bg) => `
      <div style="border-top:1px solid #E7EFF8;padding-top:18px;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.75;color:#8296B0;">
        The Omni Biosystems Team<br>
        <span style="color:#1BB3C4;font-weight:bold;">OncoMiMIC&trade;</span> &middot; Automated, AI-powered, chip-based drug discovery<br>
        Singapore &middot; <a href="${SITE}" style="color:#1BB3C4;text-decoration:none;">omni-biosystems.com</a>
      </div>`;

// ── Layout A: Navy banner (Press, Other) ──────────────────
function navyBanner(bodyParas) {
  return `<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#F4F8FC;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F4F8FC;padding:24px 0;">
<tr><td align="center">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#FFFFFF;border-radius:14px;overflow:hidden;border:1px solid #E1E9F2;">
    <tr><td align="center" style="background:#0B1B3A;padding:28px 32px 24px;">
      <img src="${IMG.lockupNavy}" width="215" alt="Omni Biosystems" style="display:block;border:0;outline:none;">
    </td></tr>
    <tr><td style="height:3px;background:#1BB3C4;font-size:0;line-height:0;">&nbsp;</td></tr>
    <tr><td style="padding:30px 34px 4px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.72;color:#2C4568;">
      ${paras(bodyParas)}
      <table role="presentation" cellpadding="0" cellspacing="0"><tr>
        <td style="background:#1BB3C4;border-radius:24px;">
          <a href="${SITE}" style="display:inline-block;padding:12px 26px;font-family:Arial,sans-serif;font-size:14px;font-weight:bold;color:#08172E;text-decoration:none;">Explore the platform&nbsp;&rarr;</a>
        </td></tr></table>
    </td></tr>
    <tr><td style="padding:26px 34px 28px;">${footerBlock()}</td></tr>
  </table>
</td></tr></table>
</body></html>`;
}

// ── Layout B: Light editorial (Investor, Pharma / CRO) ────
function lightEditorial(bodyParas) {
  return `<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#EEF3F9;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF3F9;padding:24px 0;">
<tr><td align="center">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#FFFFFF;border-radius:14px;overflow:hidden;border:1px solid #E1E9F2;">
    <tr><td style="padding:32px 36px 0;">
      <img src="${IMG.lockupWhite}" width="195" alt="Omni Biosystems" style="display:block;border:0;outline:none;">
    </td></tr>
    <tr><td style="padding:24px 36px 0;font-size:0;line-height:0;">
      <div style="height:2px;width:54px;background:#EB7B2E;"></div>
    </td></tr>
    <tr><td style="padding:24px 36px 6px;">
      <p style="margin:0 0 18px;font-family:Arial,sans-serif;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#1BB3C4;font-weight:bold;">Welcome</p>
      <div style="font-family:Georgia,'Times New Roman',serif;font-size:15.5px;line-height:1.78;color:#33455F;">
        ${paras(bodyParas)}
      </div>
      <p style="margin:0 0 6px;font-family:Arial,sans-serif;font-size:14px;">
        <a href="${SITE}" style="color:#1BB3C4;text-decoration:none;font-weight:bold;">Explore the platform&nbsp;&rarr;</a>
      </p>
    </td></tr>
    <tr><td style="padding:20px 36px 32px;">${footerBlock()}</td></tr>
  </table>
</td></tr></table>
</body></html>`;
}

// ── Layout C: Aperture badge (Researcher / KOL) ───────────
function apertureBadge(bodyParas) {
  return `<!DOCTYPE html>
<html><body style="margin:0;padding:0;background:#F4F8FC;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F4F8FC;padding:24px 0;">
<tr><td align="center">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#FFFFFF;border-radius:16px;overflow:hidden;border:1px solid #E1E9F2;">
    <tr><td style="height:5px;background:#1BB3C4;font-size:0;line-height:0;">&nbsp;</td></tr>
    <tr><td align="center" style="padding:32px 34px 0;">
      <img src="${IMG.markWhite}" width="60" alt="Omni Biosystems" style="display:block;border:0;outline:none;margin:0 auto;">
      <div style="font-family:Arial,sans-serif;font-size:17px;font-weight:bold;letter-spacing:.17em;color:#0B1B3A;padding-top:15px;">OMNI BIOSYSTEMS</div>
      <div style="font-family:Arial,sans-serif;font-size:10px;letter-spacing:.24em;color:#1BB3C4;padding-top:6px;font-weight:bold;">ONCOMIMIC&nbsp;PLATFORM</div>
    </td></tr>
    <tr><td style="padding:28px 40px 4px;font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.72;color:#2C4568;">
      ${paras(bodyParas)}
    </td></tr>
    <tr><td align="center" style="padding:0 40px 28px;">
      <table role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
        <td style="background:#0B1B3A;border-radius:24px;">
          <a href="${SITE}" style="display:inline-block;padding:12px 28px;font-family:Arial,sans-serif;font-size:14px;font-weight:bold;color:#37D6E6;text-decoration:none;">Explore the platform&nbsp;&rarr;</a>
        </td></tr></table>
    </td></tr>
    <tr><td align="center" style="background:#F7FAFD;padding:22px 34px;border-top:1px solid #EDF2F8;">
      <div style="font-family:Arial,sans-serif;font-size:12px;line-height:1.75;color:#8296B0;">
        <span style="color:#1BB3C4;font-weight:bold;">OncoMiMIC&trade;</span> &middot; The Omni Biosystems Team<br>
        Singapore &middot; <a href="${SITE}" style="color:#1BB3C4;text-decoration:none;">omni-biosystems.com</a>
      </div>
    </td></tr>
  </table>
</td></tr></table>
</body></html>`;
}

const LAYOUTS = { navyBanner, lightEditorial, apertureBadge };

// ── Persona content + layout assignment ───────────────────
const TEMPLATES = {
  Investor: {
    layout: 'lightEditorial',
    subject: 'Thanks for your interest in Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for reaching out — we're glad Omni Biosystems is on your radar.`,
      `We're building OncoMiMIC, an automated, AI-powered, chip-based platform that bridges AI-driven target discovery and clinical validation, recreating the tumor microenvironment on a chip to make preclinical data faster, cheaper, and far more predictive.`,
      `A member of our founding team will follow up personally within two business days. In the meantime, we're glad to share our investor materials and walk you through our traction, roadmap, and the current round.`,
      `We appreciate your time and look forward to speaking.`,
    ],
  },
  'Pharma / CRO partner': {
    layout: 'lightEditorial',
    subject: 'Thanks for reaching out to Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for your interest in OncoMiMIC — we'd welcome the chance to explore how it could support your programs.`,
      `Our platform runs ex-vivo immuno-oncology experiments on a microfluidic chip, delivering five or more physiologically relevant readouts per run — from immune cell recruitment and cytotoxicity to spatial dynamics and gene expression — with AI-driven analysis that sharply reduces read-out time.`,
      `A member of our team will be in touch within two business days to understand your needs and discuss a pilot or validation study. If you'd like, just reply with the indications or assay types you're focused on and we'll come prepared.`,
    ],
  },
  'Researcher / KOL': {
    layout: 'apertureBadge',
    subject: 'Thanks for connecting with Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for reaching out — collaboration with researchers and clinical leaders is central to how we build.`,
      `OncoMiMIC recreates the 3D tumor microenvironment on a chip to generate richer, more translatable immuno-oncology data than conventional 2D assays. We work closely with scientific partners on co-development, validation, and publications.`,
      `A member of our scientific team will follow up within two business days. If you have a specific model, indication, or research question in mind, feel free to reply with details — it'll help us make the first conversation a productive one.`,
    ],
  },
  Press: {
    layout: 'navyBanner',
    subject: 'Omni Biosystems — media inquiry received',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for getting in touch. We've received your media inquiry and will respond within one to two business days.`,
      `Omni Biosystems is a Singapore-based deep-tech company developing OncoMiMIC, an automated, AI-powered, chip-based drug discovery platform working toward a world beyond animal testing.`,
      `If you're on deadline, please reply with your outlet, the angle you're working on, and your timing, and we'll prioritize accordingly. We're also happy to provide background materials, executive commentary, or high-resolution assets on request.`,
    ],
  },
  Other: {
    layout: 'navyBanner',
    subject: 'Thanks for contacting Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for reaching out — we've received your message and it's on its way to the right person on our team.`,
      `Omni Biosystems is building OncoMiMIC, an automated, AI-powered, chip-based platform for drug discovery beyond animal testing. We'll get back to you within two business days.`,
      `If there's anything that would help us respond faster, just reply to this email with a little more detail.`,
    ],
  },
};

function getAutoReply(topic, firstName) {
  const name = firstName && String(firstName).trim() ? String(firstName).trim() : 'there';
  const t = TEMPLATES[topic] || TEMPLATES.Other;
  const bodyParas = t.paragraphs(name);

  // Plain-text part (always sent alongside HTML for deliverability + accessibility)
  const text = bodyParas.join('\n\n') + SIGNATURE_TEXT;

  // HTML part, escaped then bolded for the product name
  const htmlParas = bodyParas.map((p) =>
    esc(p).replace(/OncoMiMIC/g, '<strong style="color:#0B1B3A;">OncoMiMIC</strong>')
  );
  const render = LAYOUTS[t.layout] || navyBanner;
  const html = render(htmlParas);

  return { subject: t.subject, text, html, layout: t.layout };
}

module.exports = { getAutoReply, TEMPLATES, LAYOUTS };
