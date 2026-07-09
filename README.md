# Omni Biosystems — Website

Static website for [omni-biosystems.com](https://omni-biosystems.com), built as a single-page HTML file and hosted on Firebase Hosting.

## Repository structure

```
omni-biosystems-web/
├── public/
│   ├── index.html              # The full website (single file)
│   ├── favicon.svg             # Tab icon (aperture on navy tile, scalable)
│   ├── favicon-16.png          # Tab icon fallback (standard-DPI)
│   ├── favicon-32.png          # Tab icon fallback
│   ├── apple-touch-icon.png    # iOS home screen (blocks mark, 180px)
│   ├── icon-192.png            # PWA / Android icon (maskable)
│   ├── icon-512.png            # PWA / Android icon (maskable)
│   ├── site.webmanifest        # PWA manifest
│   └── assets/
│       └── logo/
│           ├── omni-lockup-dark.svg    # Full lockup for dark backgrounds (nav, footer)
│           ├── omni-lockup-light.svg   # Full lockup for light backgrounds
│           ├── omni-blocks-dark.svg    # 2x2 grid mark, dark backgrounds
│           ├── omni-blocks-light.svg   # 2x2 grid mark, light backgrounds
│           └── omni-logo.svg           # Aperture symbol
├── .github/
│   └── workflows/
│       └── deploy.yml      # Auto-deploy to Firebase on push to main
├── server/                 # Contact-form backend (Cloud Run + Mailgun) — see server/README.md
│   ├── index.js            # POST /contact: validation, honeypot, rate limit, send
│   ├── templates.js        # The five persona auto-reply emails
│   ├── Dockerfile
│   └── package.json
├── firebase.json           # Firebase Hosting config
├── .firebaserc             # Firebase project alias
├── .gitignore
└── README.md
```

## Contact backend

The website form posts to a small Cloud Run service in `server/` that sends mail via
Mailgun (sending domain `mg.omni-biosystems.com`): it notifies `contact@omni-biosystems.com`
and sends the visitor a persona-specific auto-reply. Full setup, DNS, and deploy steps are
in [`server/README.md`](server/README.md). Until it's deployed and `API_ENDPOINT` is set in
`index.html`, the form falls back to opening the visitor's mail app.

## Brand assets

The favicon family is deliberately split for legibility: the **aperture** symbol is used for the small browser-tab icons (it stays recognizable at 16–32px), while the **blocks** mark (the O·N·M·I grid) is used for the larger apple-touch and PWA app icons where its detail can be seen. Logo typeface is **Causten SemiBold** (wordmark is outlined in the SVGs, so no web font is required).

## Auto-deploy

Every push to `main` triggers the GitHub Actions workflow, which deploys `public/` to Firebase Hosting automatically. No manual `firebase deploy` needed after initial setup.

## One-time setup (do this once)

### 1. Create the Firebase project
- Go to [console.firebase.google.com](https://console.firebase.google.com)
- Create a new project named **omni-biosystems**
- Enable Hosting

### 2. Connect GitHub Actions to Firebase
- In the Firebase console → Hosting → GitHub integration, or run locally:
  ```bash
  npm install -g firebase-tools
  firebase login
  firebase init hosting:github
  ```
- This creates a `FIREBASE_SERVICE_ACCOUNT` secret in your GitHub repo automatically.

### 3. Connect the custom domain
- In Firebase console → Hosting → Add custom domain → `omni-biosystems.com`
- Add the TXT and A records Firebase gives you to your Squarespace DNS panel (see deployment notes)

### 4. Wire up the contact form (when ready)
- Deploy your Cloud Run email API
- Open `public/index.html` and set `API_ENDPOINT` at the top of the `<script>` block:
  ```js
  var API_ENDPOINT = "https://your-cloud-run-url.a.run.app/contact";
  ```
- Push to `main` — the workflow deploys it automatically

## Local preview

```bash
npm install -g firebase-tools
firebase serve --only hosting
```

Then open [http://localhost:5000](http://localhost:5000).

## Making content updates

Edit `public/index.html`, commit, and push to `main`. The site updates within ~1 minute.
