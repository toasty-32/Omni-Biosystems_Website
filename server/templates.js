// templates.js
// Persona-specific auto-reply emails. Keyed by the form's "topic" value.
// Edit copy freely — { firstName } is interpolated at send time.

const SIGNATURE_TEXT =
  `\n\n— The Omni Biosystems Team\n` +
  `OncoMiMIC™ · Automated, AI-powered, chip-based drug discovery\n` +
  `Singapore · omni-biosystems.com`;

// Shared, lightweight HTML wrapper so the replies look clean in an inbox.
function wrapHtml(bodyParagraphs) {
  const paras = bodyParagraphs.map((p) => `<p style="margin:0 0 16px;">${p}</p>`).join('');
  return `<!DOCTYPE html>
<html>
  <body style="margin:0;padding:0;background:#F4F8FC;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F4F8FC;padding:28px 0;">
      <tr><td align="center">
        <table role="presentation" width="560" cellpadding="0" cellspacing="0" style="max-width:560px;width:100%;background:#FFFFFF;border-radius:14px;overflow:hidden;border:1px solid #E7EFF8;">
          <tr><td style="background:#0B1B3A;padding:22px 32px;">
            <span style="font-family:'Space Grotesk',Arial,sans-serif;font-size:18px;font-weight:700;color:#FFFFFF;letter-spacing:.02em;">OMNI BIOSYSTEMS</span>
          </td></tr>
          <tr><td style="padding:30px 32px 12px;font-family:Inter,Arial,sans-serif;font-size:15px;line-height:1.65;color:#243B5E;">
            ${paras}
          </td></tr>
          <tr><td style="padding:0 32px 30px;font-family:Inter,Arial,sans-serif;font-size:13px;line-height:1.6;color:#7E97B8;border-top:1px solid #E7EFF8;padding-top:20px;">
            The Omni Biosystems Team<br>
            <span style="color:#1BB3C4;">OncoMiMIC™</span> · Automated, AI-powered, chip-based drug discovery<br>
            Singapore · <a href="https://omni-biosystems.com" style="color:#1BB3C4;text-decoration:none;">omni-biosystems.com</a>
          </td></tr>
        </table>
      </td></tr>
    </table>
  </body>
</html>`;
}

const TEMPLATES = {
  Investor: {
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
    subject: 'Thanks for reaching out to Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for your interest in OncoMiMIC — we'd welcome the chance to explore how it could support your programs.`,
      `Our platform runs ex-vivo immuno-oncology experiments on a microfluidic chip, delivering five or more physiologically relevant readouts per run — from immune cell recruitment and cytotoxicity to spatial dynamics and gene expression — with AI-driven analysis that sharply reduces read-out time.`,
      `A member of our team will be in touch within two business days to understand your needs and discuss a pilot or validation study. If you'd like, just reply with the indications or assay types you're focused on and we'll come prepared.`,
    ],
  },
  'Researcher / KOL': {
    subject: 'Thanks for connecting with Omni Biosystems',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for reaching out — collaboration with researchers and clinical leaders is central to how we build.`,
      `OncoMiMIC recreates the 3D tumor microenvironment on a chip to generate richer, more translatable immuno-oncology data than conventional 2D assays. We work closely with scientific partners on co-development, validation, and publications.`,
      `A member of our scientific team will follow up within two business days. If you have a specific model, indication, or research question in mind, feel free to reply with details — it'll help us make the first conversation a productive one.`,
    ],
  },
  Press: {
    subject: 'Omni Biosystems — media inquiry received',
    paragraphs: (n) => [
      `Hi ${n},`,
      `Thank you for getting in touch. We've received your media inquiry and will respond within one to two business days.`,
      `Omni Biosystems is a Singapore-based deep-tech company developing OncoMiMIC, an automated, AI-powered, chip-based drug discovery platform working toward a world beyond animal testing.`,
      `If you're on deadline, please reply with your outlet, the angle you're working on, and your timing, and we'll prioritize accordingly. We're also happy to provide background materials, executive commentary, or high-resolution assets on request.`,
    ],
  },
  Other: {
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
  const name = firstName && firstName.trim() ? firstName.trim() : 'there';
  const t = TEMPLATES[topic] || TEMPLATES.Other;
  const paras = t.paragraphs(name);
  const text = paras.join('\n\n') + SIGNATURE_TEXT;
  const html = wrapHtml(paras);
  return { subject: t.subject, text, html };
}

module.exports = { getAutoReply, TEMPLATES };
