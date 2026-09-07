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

## Live Cloud Deployment

* **Live Primary URL**: `https://onerishi-website.onrender.com`
* **Interactive Swagger UI Docs**: `https://onerishi-website.onrender.com/docs`
* **Health Check**: `https://onerishi-website.onrender.com/api/health`
* **Runtime**: Python 3.11.9 on Render (pinned via `.python-version`)

## API reference

**Public (no auth):**
- `GET /api/health` — service health check
- `GET /api/posts` — all published posts. Optional `?category=Marketing%20%C3%97%20Tech`
- `GET /api/posts/{slug}` — one published post, 404 if draft or missing

**Auth:**
- `POST /api/admin/login` — body `{"password": "..."}` → returns `{"access_token": "..."}`
- Send that token on every admin request: header `Authorization: Bearer <token>`

**Admin (auth required):**
- `GET /api/admin/posts` — all posts, drafts included
- `POST /api/admin/posts` — create. Body: `title, category, excerpt, body, cover_image, status, meta_title, meta_description, meta_keywords, og_image, slug`
- `GET /api/admin/posts/{id}` — fetch single post by ID (for post editor)
- `PUT /api/admin/posts/{id}` — update any subset of fields
- `DELETE /api/admin/posts/{id}` — delete post
- `POST /api/admin/upload` — multipart file upload (PNG, JPG, WebP, GIF, SVG up to 10MB) → returns `{ "url": "/uploads/..." }`

`read_time_minutes` is computed automatically from body word count.
`slug` is derived automatically from title if omitted, or can be specified as a custom URL permalink.
`category` must match one of the valid categories in `app/models.py`.

## Continuous Deployment Loop

When a post is created, updated, or deleted with `status == "published"`:
FastAPI automatically fires a background GitHub Actions `repository_dispatch` event (`cms_post_published`) to `RJ-Rishi91/onerishi-website`. GitHub Actions (`deploy.yml`) rebuilds Astro and deploys the update live to **`https://onerishi.in`** automatically.

