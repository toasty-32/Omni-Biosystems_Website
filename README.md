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
