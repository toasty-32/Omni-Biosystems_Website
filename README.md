# Omni Biosystems Website

A full-stack web application for managing biological samples and analysis results.

**Stack:** React (Vite + TypeScript) · FastAPI · Supabase (PostgreSQL + Auth)

---

## Folder Structure

```
.
├── frontend/                   # React + TypeScript SPA
│   ├── src/
│   │   ├── components/
│   │   │   ├── auth/           # AuthForm
│   │   │   ├── dashboard/      # StatCard
│   │   │   └── ui/             # Navbar
│   │   ├── hooks/              # useAuth
│   │   ├── lib/                # supabase.ts, api.ts (axios)
│   │   ├── pages/              # LoginPage, RegisterPage, DashboardPage, ProfilePage
│   │   └── types/              # Shared TypeScript interfaces
│   ├── .env.example
│   ├── Dockerfile
│   └── package.json
│
├── backend/                    # FastAPI
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── endpoints/      # users, samples, analysis, dashboard
│   │   │   └── router.py
│   │   ├── core/
│   │   │   ├── config.py       # Pydantic settings
│   │   │   └── security.py     # JWT validation
│   │   ├── db/
│   │   │   └── supabase_client.py
│   │   ├── schemas/            # Pydantic models
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   ├── Dockerfile
│   └── requirements.txt
│
├── supabase/
│   └── migrations/
│       └── 001_initial_schema.sql
│
└── docker-compose.yml
```

---

## API Endpoints

All endpoints are prefixed with `/api/v1`. Authentication uses a Supabase JWT passed as `Authorization: Bearer <token>`.

### Health

| Method | Path      | Auth | Description        |
|--------|-----------|------|--------------------|
| GET    | `/health` | No   | Liveness check     |

### Users

| Method | Path          | Auth | Description              |
|--------|---------------|------|--------------------------|
| GET    | `/users/me`   | Yes  | Get own profile          |
| PATCH  | `/users/me`   | Yes  | Update full_name / org   |

### Samples

| Method | Path                   | Auth | Description              |
|--------|------------------------|------|--------------------------|
| GET    | `/samples/`            | Yes  | List own samples         |
| POST   | `/samples/`            | Yes  | Create a new sample      |
| GET    | `/samples/{id}`        | Yes  | Get single sample        |
| PATCH  | `/samples/{id}`        | Yes  | Update sample fields     |
| DELETE | `/samples/{id}`        | Yes  | Delete sample            |

### Analysis Results

| Method | Path                                     | Auth | Description                     |
|--------|------------------------------------------|------|---------------------------------|
| GET    | `/analysis/samples/{sample_id}/results`  | Yes  | List results for a sample       |
| POST   | `/analysis/samples/{sample_id}/results`  | Yes  | Add a result to a sample        |

### Dashboard

| Method | Path               | Auth | Description                     |
|--------|--------------------|------|---------------------------------|
| GET    | `/dashboard/stats` | Yes  | Aggregated stats for the user   |

Interactive docs are available at `/api/docs` (Swagger) and `/api/redoc`.

---

## Data Models

### `profiles`

| Column         | Type        | Notes                              |
|----------------|-------------|------------------------------------|
| `id`           | uuid (PK)   | References `auth.users`            |
| `email`        | text        |                                    |
| `full_name`    | text        | Nullable                           |
| `role`         | text        | `admin` \| `researcher` \| `viewer` |
| `organization` | text        | Nullable                           |
| `created_at`   | timestamptz |                                    |

### `samples`

| Column         | Type        | Notes                                          |
|----------------|-------------|------------------------------------------------|
| `id`           | uuid (PK)   |                                                |
| `name`         | text        |                                                |
| `type`         | text        | e.g. `blood`, `tissue`, `fluid`                |
| `status`       | text        | `pending` \| `processing` \| `completed` \| `failed` |
| `collected_at` | timestamptz |                                                |
| `processed_at` | timestamptz | Nullable                                       |
| `owner_id`     | uuid (FK)   | References `auth.users`                        |
| `metadata`     | jsonb       | Arbitrary key-value data                       |
| `created_at`   | timestamptz |                                                |

### `analysis_results`

| Column            | Type        | Notes                    |
|-------------------|-------------|--------------------------|
| `id`              | uuid (PK)   |                          |
| `sample_id`       | uuid (FK)   | References `samples`     |
| `result_type`     | text        | e.g. `glucose`, `pH`     |
| `value`           | numeric     |                          |
| `unit`            | text        | e.g. `mg/dL`, `mmol/L`  |
| `reference_range` | text        | Nullable, e.g. `70-99`  |
| `flagged`         | boolean     | True if out of range     |
| `created_at`      | timestamptz |                          |

---

## Setup

### Prerequisites

- Node.js 20+, Python 3.12+
- A [Supabase](https://supabase.com) project

### 1. Supabase

Run the migration in your Supabase SQL editor:

```
supabase/migrations/001_initial_schema.sql
```

Enable **Email/Password** auth in your Supabase project settings.

### 2. Backend

```bash
cd backend
cp .env.example .env          # fill in SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, SUPABASE_JWT_SECRET
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload  # http://localhost:8000
```

### 3. Frontend

```bash
cd frontend
cp .env.example .env          # fill in VITE_SUPABASE_URL, VITE_SUPABASE_ANON_KEY
npm install
npm run dev                   # http://localhost:3000
```

### 4. Docker (optional)

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
# fill in both .env files
docker-compose up --build
```

---

## Authentication Flow

1. User registers or logs in via the React frontend using `@supabase/supabase-js`.
2. Supabase returns a signed JWT (HS256, audience `authenticated`).
3. The frontend attaches the token as `Authorization: Bearer <token>` on every API request via the Axios interceptor in `frontend/src/lib/api.ts`.
4. FastAPI's `get_current_user` dependency (`backend/app/core/security.py`) verifies the JWT using the Supabase JWT secret and extracts `sub` (the user UUID) from the payload.
5. All database queries are scoped to that `sub`, enforced by both application logic and Supabase Row-Level Security policies.

---

## Production Deployment (Firebase + omni-biosystems.com)

### Architecture

```
omni-biosystems.com        → Firebase Hosting  (React static build)
www.omni-biosystems.com    → Firebase Hosting  (redirects to apex)
omni-biosystems.com/api/** → Firebase rewrite → Cloud Run (FastAPI)
```

Firebase Hosting handles TLS, CDN, and routes `/api/**` transparently to Cloud Run — no separate API subdomain needed.

---

### One-time setup

#### 1. Create a Firebase project

1. Go to [console.firebase.google.com](https://console.firebase.google.com) → **Add project**
2. Name it **omni-biosystems** (must match `.firebaserc`)
3. Enable **Google Analytics** if desired

#### 2. Enable Cloud Run in GCP

1. In [console.cloud.google.com](https://console.cloud.google.com), select the same project
2. Enable these APIs: **Cloud Run**, **Cloud Build**, **Artifact Registry**, **Secret Manager**
3. Create an Artifact Registry repository:
   ```
   Region: us-central1  |  Format: Docker  |  Name: omni-biosystems
   ```

#### 3. Store secrets in GCP Secret Manager

```bash
# Run once with your real values
gcloud secrets create SUPABASE_URL          --data-file=- <<< "https://your-project.supabase.co"
gcloud secrets create SUPABASE_SERVICE_ROLE_KEY --data-file=- <<< "your-service-role-key"
gcloud secrets create SUPABASE_JWT_SECRET   --data-file=- <<< "your-jwt-secret"
```

#### 4. Add GitHub Actions secrets

In GitHub → repo → **Settings → Secrets and variables → Actions**, add:

| Secret | Value |
|--------|-------|
| `GCP_PROJECT_ID` | Your GCP project ID |
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload Identity Federation provider URI |
| `GCP_SERVICE_ACCOUNT` | Service account email for Cloud Build/Run |
| `FIREBASE_SERVICE_ACCOUNT` | Firebase service account JSON (from Firebase → Project Settings → Service accounts) |
| `VITE_SUPABASE_URL` | Your Supabase project URL |
| `VITE_SUPABASE_ANON_KEY` | Your Supabase anon key |

> **Workload Identity Federation** (keyless auth) is the recommended approach.
> See [google-github-actions/auth](https://github.com/google-github-actions/auth#setting-up-workload-identity-federation) for the one-time setup (~5 min).

#### 5. Connect custom domain in Firebase

1. Firebase console → **Hosting** → **Add custom domain**
2. Add `omni-biosystems.com` — Firebase shows you two A record values
3. Add `www.omni-biosystems.com` — Firebase shows a CNAME value

---

### DNS configuration in Squarespace

Go to **Squarespace Domains** → `omni-biosystems.com` → **DNS Settings** → **Custom Records**.

Add these records (replace values with what Firebase shows you):

```
Type    Host    Value / Points To               TTL
────────────────────────────────────────────────────────
A       @       151.101.1.195                   Auto
A       @       151.101.65.195                  Auto
CNAME   www     omni-biosystems.com.            Auto
```

> Squarespace uses **@** for the bare/apex domain. Firebase gives you two A record
> IPs — add both. The `www` CNAME should point to the bare domain (with trailing dot).
> DNS propagation typically takes 5–30 minutes; TLS cert issues automatically after that.

---

### Deploys

Every push to `main` triggers the `deploy.yml` workflow:
1. Builds the Docker image → pushes to Artifact Registry → deploys to Cloud Run
2. Builds the React app → deploys static files to Firebase Hosting

The CI workflow (`ci.yml`) runs on all branches and PRs independently.

### Architecture

```
omni-biosystems.com        → Render Static Site  (React build)
www.omni-biosystems.com    → Render Static Site  (redirect)
api.omni-biosystems.com    → Render Web Service  (FastAPI)
```

### 1. Connect repo to Render

1. Go to [render.com](https://render.com) → **New** → **Blueprint**
2. Connect your GitHub repo (`toasty-32/Omni-Biosystems_Website`)
3. Render reads `render.yaml` and creates both services automatically

### 2. Set secret environment variables in Render dashboard

For the **API service** (`omni-biosystems-api`):

| Key | Value |
|-----|-------|
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_SERVICE_ROLE_KEY` | From Supabase → Settings → API |
| `SUPABASE_JWT_SECRET` | From Supabase → Settings → API → JWT Secret |

For the **frontend service** (`omni-biosystems-frontend`):

| Key | Value |
|-----|-------|
| `VITE_SUPABASE_URL` | Your Supabase project URL |
| `VITE_SUPABASE_ANON_KEY` | From Supabase → Settings → API |

### 3. Add custom domains in Render

1. Open each service → **Settings** → **Custom Domains**
2. Add `omni-biosystems.com` and `www.omni-biosystems.com` to the frontend service
3. Add `api.omni-biosystems.com` to the API service
4. Render will show you the DNS values to add — typically a CNAME target

### 4. Configure DNS at your registrar

Add these records (replace `<render-target>` with the value Render gives you):

```
Type    Name    Value                          TTL
─────────────────────────────────────────────────────
A       @       216.24.57.1                    300   ← Render's apex IP
CNAME   www     omni-biosystems.com            300
CNAME   api     <api-service>.onrender.com     300
```

> **Apex domain note:** Render provides specific A record IPs for bare domains
> (`@`). Use the exact IP shown in your Render custom domain settings.
> For `www`, a CNAME pointing to the bare domain works on most registrars.

### 5. TLS

Render provisions and auto-renews Let's Encrypt certificates for all custom
domains — no action needed.

### Trigger deploys

Every push to `main` automatically redeploys both services. The CI workflow
runs first; Render only deploys on a green build if you enable **Auto-Deploy**
with a branch filter in Render settings.
