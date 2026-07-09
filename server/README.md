# Omni Biosystems — Contact API

Small Node/Express service that backs the contact form on omni-biosystems.com.
On each submission it:

1. **Notifies the team** — emails the submission to `contact@omni-biosystems.com`
   (your Google Group), with the visitor's address as `Reply-To` so a reply goes
   straight back to them.
2. **Auto-replies to the visitor** — sends a persona-specific welcome email
   *from* `Omni Biosystems <contact@omni-biosystems.com>`, chosen by the
   "I'm reaching out as" field (Investor / Pharma-CRO / Researcher-KOL / Press / Other).

Mail is sent through **Mailgun** using the sending subdomain `mg.omni-biosystems.com`.
(The Google Group can only *receive* mail, so a sending service is required — this is why we use Mailgun.)

---

## Files

```
server/
├── index.js          # Express app: POST /contact (validation, honeypot, rate limit, send)
├── templates.js      # The five auto-reply emails — edit copy here
├── package.json
├── Dockerfile
├── .dockerignore
└── .env.example      # copy to .env for local testing
```

## Endpoints

- `GET /` and `GET /health` — health checks
- `POST /contact` — body `{ name, org, email, topic, message, company_website }`
  (`company_website` is the hidden honeypot; leave empty). Returns `{ ok: true }` or an error.

---

## 1. Set up the Mailgun sending domain

1. In Mailgun → **Send → Domains → Add New Domain**, enter `mg.omni-biosystems.com`.
   Pick the region (US or EU) — note which, it decides `MAILGUN_API_BASE`.
2. Mailgun shows a set of DNS records. Add them at **Squarespace → Domains →
   omni-biosystems.com → DNS Settings**. The important ones for sending:
   - **TXT** on `mg` — SPF, value like `v=spf1 include:mailgun.org ~all`
   - **TXT** (DKIM) on the host Mailgun specifies (e.g. `smtp._domainkey.mg`) — the long `k=rsa; p=…` value
   - **CNAME** on `email.mg` → `mailgun.org` — optional, only for open/click tracking
   - (MX records Mailgun lists are only needed if you want Mailgun to *receive* mail — not required here.)
3. These all live on the **`mg` subdomain**, so they sit alongside your existing
   Google Workspace MX and Firebase records on the root domain without any conflict.
4. Back in Mailgun, click **Verify**. DNS can take up to a few hours to propagate.
5. Copy your **Sending API key** (Mailgun → API keys).

### A note on the "from" address and deliverability
The auto-reply is sent *from* `contact@omni-biosystems.com` (root domain) even though
Mailgun signs as `mg.omni-biosystems.com`. This passes DMARC via **relaxed alignment**
(a subdomain aligns with its organizational domain), so it delivers cleanly. If you later
publish a **strict** DMARC policy on the root domain, switch the auto-reply `from` to an
`@mg.omni-biosystems.com` address, or add Mailgun to the root domain's SPF.

---

## 2. Store the API key as a secret

```bash
gcloud secrets create mailgun-api-key --replication-policy=automatic
printf '%s' 'YOUR_MAILGUN_SENDING_KEY' | gcloud secrets versions add mailgun-api-key --data-file=-
```

## 3. Deploy to Cloud Run

From the `server/` folder (Singapore region shown):

```bash
gcloud run deploy omni-contact-api \
  --source . \
  --region asia-southeast1 \
  --allow-unauthenticated \
  --set-env-vars "MAILGUN_DOMAIN=mg.omni-biosystems.com,MAILGUN_API_BASE=https://api.mailgun.net,CONTACT_TO=contact@omni-biosystems.com,REPLY_FROM=Omni Biosystems <contact@omni-biosystems.com>,NOTIFY_FROM=Omni Biosystems Website <postmaster@mg.omni-biosystems.com>,ALLOWED_ORIGINS=https://omni-biosystems.com,https://www.omni-biosystems.com" \
  --set-secrets "MAILGUN_API_KEY=mailgun-api-key:latest"
```

> EU Mailgun account? Change `MAILGUN_API_BASE` to `https://api.eu.mailgun.net`.

Cloud Run prints a service URL, e.g. `https://omni-contact-api-xxxx-as.a.run.app`.

## 4. Point the website at it

In `public/index.html`, set the endpoint near the top of the `<script>` block to the
service URL **plus `/contact`**:

```js
var API_ENDPOINT = "https://omni-contact-api-xxxx-as.a.run.app/contact";
```

Commit and push — the Firebase Action redeploys the site. While `API_ENDPOINT` is empty,
the form falls back to opening the visitor's mail app (so it never looks broken).

## 5. Test

```bash
curl -i -X POST https://omni-contact-api-xxxx-as.a.run.app/contact \
  -H 'Content-Type: application/json' \
  -d '{"name":"Test User","email":"you@example.com","topic":"Investor","message":"Testing the pipeline."}'
```

You should get `{"ok":true}`, a submission in the `contact@` group inbox, and the
Investor auto-reply at the address you used.

---

## Local development

```bash
cd server
cp .env.example .env      # fill in MAILGUN_API_KEY
npm install
npm start                 # http://localhost:8080
```

## Editing the auto-replies

All copy lives in `templates.js`, one entry per persona. Change wording, timing
("two business days"), or the signature there; redeploy to publish. `{firstName}` is
filled from the submitted name (falls back to "there").

## Security notes

- **CORS** is locked to the origins in `ALLOWED_ORIGINS`.
- **Honeypot** (`company_website`) silently drops bot submissions.
- **Rate limit**: 5 requests per IP per minute.
- The Mailgun key is only ever read from the environment/Secret Manager — never commit it.
