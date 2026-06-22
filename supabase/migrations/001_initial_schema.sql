-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Profiles table (extends Supabase auth.users)
create table public.profiles (
  id          uuid primary key references auth.users(id) on delete cascade,
  email       text not null,
  full_name   text,
  role        text not null default 'viewer' check (role in ('admin', 'researcher', 'viewer')),
  organization text,
  created_at  timestamptz not null default now()
);

-- Automatically create a profile row when a new user signs up
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer as $$
begin
  insert into public.profiles (id, email)
  values (new.id, new.email);
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Samples table
create table public.samples (
  id           uuid primary key default uuid_generate_v4(),
  name         text not null,
  type         text not null,
  status       text not null default 'pending' check (status in ('pending', 'processing', 'completed', 'failed')),
  collected_at timestamptz not null,
  processed_at timestamptz,
  owner_id     uuid not null references auth.users(id) on delete cascade,
  metadata     jsonb not null default '{}',
  created_at   timestamptz not null default now()
);

create index samples_owner_idx on public.samples(owner_id);

-- Analysis results table
create table public.analysis_results (
  id              uuid primary key default uuid_generate_v4(),
  sample_id       uuid not null references public.samples(id) on delete cascade,
  result_type     text not null,
  value           numeric not null,
  unit            text not null,
  reference_range text,
  flagged         boolean not null default false,
  created_at      timestamptz not null default now()
);

create index analysis_results_sample_idx on public.analysis_results(sample_id);
create index analysis_results_flagged_idx on public.analysis_results(flagged);

-- Row-level security
alter table public.profiles enable row level security;
alter table public.samples enable row level security;
alter table public.analysis_results enable row level security;

-- Profiles: users can read/update their own row
create policy "profiles_select_own" on public.profiles for select using (auth.uid() = id);
create policy "profiles_update_own" on public.profiles for update using (auth.uid() = id);

-- Samples: users can CRUD their own samples
create policy "samples_select_own" on public.samples for select using (auth.uid() = owner_id);
create policy "samples_insert_own" on public.samples for insert with check (auth.uid() = owner_id);
create policy "samples_update_own" on public.samples for update using (auth.uid() = owner_id);
create policy "samples_delete_own" on public.samples for delete using (auth.uid() = owner_id);

-- Analysis results: accessible through sample ownership
create policy "results_select_own" on public.analysis_results for select
  using (exists (select 1 from public.samples where samples.id = analysis_results.sample_id and samples.owner_id = auth.uid()));
create policy "results_insert_own" on public.analysis_results for insert
  with check (exists (select 1 from public.samples where samples.id = analysis_results.sample_id and samples.owner_id = auth.uid()));
