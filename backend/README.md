# OneRishi Blog API

FastAPI backend for the Writing section — lets you create/edit/delete blog
posts through an admin API, and serves published posts to the public site.

## Setup

```bash
cd onerishi-backend
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Generate your admin password hash and put it in `.env`:
```bash
python -c "from app.auth import hash_password; print(hash_password('yourpassword'))"
```
Paste the output into `ADMIN_PASSWORD_HASH` in `.env`. Also set `JWT_SECRET`
to a long random string (e.g. `python -c "import secrets; print(secrets.token_hex(32))"`).

## Run locally

```bash
uvicorn app.main:app --reload
```

API docs (auto-generated, interactive): http://localhost:8000/docs

## API reference

**Public (no auth):**
- `GET /api/posts` — all published posts. Optional `?category=Marketing%20%C3%97%20Tech`
- `GET /api/posts/{slug}` — one published post, 404 if draft or missing

**Auth:**
- `POST /api/admin/login` — body `{"password": "..."}` → returns `{"access_token": "..."}`
- Send that token on every admin request: header `Authorization: Bearer <token>`

**Admin (auth required):**
- `GET /api/admin/posts` — all posts, drafts included
- `POST /api/admin/posts` — create. Body: `title, category, excerpt, body, cover_image, status`
- `PUT /api/admin/posts/{id}` — update any subset of fields
- `DELETE /api/admin/posts/{id}` — delete

`slug` and `read_time_minutes` are computed automatically — never send them.
`category` must exactly match one of the 5 values in `app/models.py` (`CATEGORIES`).

## SEO fields

Every post has optional `meta_title`, `meta_description`, `meta_keywords`
(comma-separated), and `og_image`. Leave any of them blank in the editor —
the API response always includes resolved fallback values:

- `effective_meta_title` → `meta_title` or, if blank, `title`
- `effective_meta_description` → `meta_description` or, if blank, `excerpt`
- `effective_og_image` → `og_image` or, if blank, `cover_image`

**Always render `effective_meta_title`/`effective_meta_description`/`effective_og_image`
in the page's `<title>`, `<meta name="description">`, and Open Graph tags —
never the raw `meta_title`/`meta_description`/`og_image` fields, which are
frequently blank by design.**

**Canonical URL** isn't stored — it's always `https://onerishi.in/writing/{slug}`,
constructed by the frontend from the slug. Don't add a database field for it.

**Important — render these tags server-side.** If the frontend is a
client-rendered SPA, social crawlers (Facebook/Twitter/LinkedIn) generally
won't see JS-injected meta tags, breaking link previews. The blog post
route needs SSR or static generation at build/request time.

## Deploy

GitHub Pages cannot run this — it's static-only. Use **Render** or **Railway**
(both have a free/cheap tier, both deploy a FastAPI app directly from a
GitHub repo with almost no config):

1. Push this folder to a GitHub repo (or a subfolder of your main repo)
2. Render/Railway → "New Web Service" → point at the repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Set the same env vars from `.env` in the platform's dashboard
6. Point a subdomain at it, e.g. `api.onerishi.in`, so the frontend calls `https://api.onerishi.in/api/posts`

Default DB is SQLite (a file — fine to start, but most hosts wipe the
filesystem on redeploy). Once this is live for real, switch `DATABASE_URL`
to a hosted Postgres instance (Render/Railway both offer one) — no code
changes needed, just the env var.

## Frontend integration note

The Writing index page and the single blog post template must fetch from
this API at build/request time — they can no longer be static HTML with
content baked in by Stitch. Pass this to Antigravity:
- Writing page → `GET /api/posts` (render the returned list)
- Blog post page → `GET /api/posts/{slug}` (render the returned post)
- Category filter pills → re-fetch with `?category=`
