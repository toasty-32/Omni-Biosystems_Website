# Omni Biosystems — Website

Bilingual (English + Simplified Chinese) marketing site for
[omni-biosystems.com](https://omni-biosystems.com), hosted on Firebase Hosting.
Six pages per language, generated from shared templates by a small Python build.

- **English** at `/` (e.g. `/oncomimic`)
- **中文** at `/zh/` (e.g. `/zh/oncomimic`) — parallel tree, EN/中文 toggle in the header

## Repository structure

```
omni-biosystems-web/
├── public/                     # ← DEPLOYED OUTPUT (generated; edit via build/, not by hand)
│   ├── index.html              # EN homepage
│   ├── platforms.html          # EN: Technology Platforms
│   ├── oncomimic.html          # EN: OncoMiMIC platform
│   ├── integration.html        # EN: Systems Integration
│   ├── consulting.html         # EN: Consulting
│   ├── investors.html          # EN: For Investors
│   ├── zh/                     # Simplified Chinese tree (same six pages)
│   │   ├── index.html … investors.html
│   ├── favicon.svg / *.png     # Icon family
│   ├── site.webmanifest        # PWA manifest
│   └── assets/
│       ├── css/site.css        # All styling (shared by both languages)
│       ├── js/site.js          # Nav, dropdowns, language toggle, contact form
│       ├── logo/ img/ video/   # Brand + media assets
│       └── …
├── build/                      # ← SOURCE. Run these to regenerate public/
│   ├── build_all.py            # Driver: builds EN then ZH into public/
│   ├── build_pages.py          # Shared chrome (head/nav/footer), i18n, hreflang
│   ├── pages_a.py              # index + oncomimic bodies
│   ├── pages_b.py              # integration + consulting + investors bodies
│   ├── pages_c.py              # platforms body
│   ├── translations.py         # EN→ZH string map (reviewer-editable)
│   └── cachebust.py            # Stamps ?v=<hash> on every asset URL
├── .github/workflows/deploy.yml  # Auto-deploy to Firebase on push to main
├── server/                     # Contact-form backend (Cloud Run + Mailgun)
├── firebase.json               # Hosting config (cleanUrls, cache headers)
├── .firebaserc  .gitignore  README.md
```

## Building the site

The **HTML files in `public/` are generated and not committed to git** — the GitHub
Actions workflow builds them on every push (see [Auto-deploy](#auto-deploy)). The
`build/` directory is the single source of truth for page copy and structure.

> Everything else in `public/` — `assets/` (CSS, JS, logos, images, video), the
> favicons, and `site.webmanifest` — **is** source and **is** committed. Only the
> 12 generated `.html` files are git-ignored.

To preview locally, generate them yourself:

```bash
cd build
python3 build_all.py          # writes both EN (/) and ZH (/zh/) into ../public
# normalize .html links to clean URLs in both trees:
cd ../public && for d in . zh; do \
  sed -i 's|href="\(/[a-z]*\)\.html"|href="\1"|g; s|href="\(/zh/[a-z]*\)\.html"|href="\1"|g' $d/*.html; done
cd ../build && python3 cachebust.py   # re-stamp asset hashes (also verifies them)

# serve for preview
cd ../public && python3 -m http.server 8000   # → http://localhost:8000
```

`cachebust.py` appends a content hash to every asset URL (`site.css?v=abc12345`)
so a changed file always busts the browser cache, and it **verifies** every
reference matches the file on disk (exits non-zero on mismatch — which also fails
the CI build).

### Translations

`build/translations.py` is a flat `EN → ZH` dictionary — the left side is the exact
English string, the right side its Simplified Chinese. A reviewer can edit the Chinese
in place and re-run the build; nothing else needs to change. Brand/technical tokens
(`OncoMiMIC`, `A*STAR`, `NK-92MI`, `IC50`, currency, etc.) are intentionally left in
Latin script. The three hero taglines and the 区拟 name story are transcreated, not
literal — see the comments in that file.

## Contact backend

The website form posts to a small Cloud Run service in `server/` that sends mail via
Mailgun (sending domain `mg.omni-biosystems.com`): it notifies `contact@omni-biosystems.com`
and sends the visitor a persona-specific auto-reply. Full setup, DNS, and deploy steps are
in [`server/README.md`](server/README.md). Until it's deployed and `API_ENDPOINT` is set in
`index.html`, the form falls back to opening the visitor's mail app.

## Brand assets

The favicon family is deliberately split for legibility: the **aperture** symbol is used for the small browser-tab icons (it stays recognizable at 16–32px), while the **blocks** mark (the O·N·M·I grid) is used for the larger apple-touch and PWA app icons where its detail can be seen. Logo typeface is **Causten SemiBold** (wordmark is outlined in the SVGs, so no web font is required).

## Auto-deploy

Every push to `main` triggers the GitHub Actions workflow (`.github/workflows/deploy.yml`),
which **builds** the site (`build/build_all.py` → EN + ZH into `public/`, then clean-URL
rewrite and `cachebust.py`) and deploys `public/` to Firebase Hosting. The build step fails
the deploy if any asset hash is inconsistent, so a broken build never ships. No manual
`firebase deploy` — and no need to commit generated HTML.

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
