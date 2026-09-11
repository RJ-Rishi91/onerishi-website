# OneRishi — onerishi.in

Personal brand site for Rushal Sharma — Marketing × Technology × Creativity.
Editorial-magazine aesthetic, warm and approachable, not corporate.

This repo/handoff covers 9 pages + 2 dynamic templates (11 builds total).
Design source: Google Stitch exports, refined in this handoff for accuracy.

See also: `SITEMAP.md` (page tree + full linking map), `DESIGN-TOKENS.md`
(colors, fonts, motion), `CONTENT-GUIDELINES.md` (non-negotiable content rules).

---

## Site identity

- **Domain:** onerishi.in
- **Brand:** OneRishi
- **Displayed name:** Rushal Sharma (general carried name; national award officially recorded under legal name Rushal Suthar)
- **Hero positioning line:** "I build, market and execute — bringing technology, creativity and communication together to turn ideas into real-world projects."
- **Site purpose:** personal brand / thought leadership, for recruiters, potential clients/collaborators, and the marketing × tech community

## Navigation

- **Primary (header, all pages, identical):** Home · Work · Writing · About · Labs, plus a "Say Hello" CTA button (visually distinct from nav links) → Contact
- **Secondary (footer, all pages):** Philosophy · Impact · Collaborate · Contact
- Secondary pages are also reached via contextual inline links from relevant primary pages (see `SITEMAP.md` for exact link sources) — this is intentional, not a missing dropdown. No folding/hamburger "more" menu — rejected on purpose, see prior design discussion if it resurfaces.

## Pages & Architecture

| # | Route | Type | Purpose / Description |
|---|---|---|---|
| 1 | `/` | Home | Visual anchor, positioning, featured works & latest writing |
| 2 | `/work` | Index | Curated case studies and design engineering catalog |
| 3 | `/work/[slug]` | Dynamic | In-depth case study template with deliverables & artifacts |
| 4 | `/writing` | Index | Filterable monograph directory with category pills & read times |
| 5 | `/writing/[slug]` | Dynamic | Editorial monograph template with Fraunces drop-caps & meta tags |
| 6 | `/about` | Static | Personal biography, operating philosophy, and official portrait |
| 7 | `/labs` | Static | R&D experiments, prototypes, and open tools |
| 8 | `/philosophy` | Static | Guiding principles on craft, speed, agency, and distribution |
| 9 | `/impact` | Static | Track record, metrics, community stewardship, and numbers |
| 10 | `/collaborate` | Static | Partnership pathways, advisory, and engagement terms |
| 11 | `/contact` | Static | Central inquiry endpoint with intent tagging |
| 12 | `/admin/login` | Private CMS | Single-admin master password authentication terminal |
| 13 | `/admin` | Private CMS | Posts dashboard, status filtering (All/Published/Drafts), deletion |
| 14 | `/admin/editor` | Private CMS | Monograph writer, SEO overrides, custom slugs, image upload |
| 15 | `/rss.xml` | Dynamic Feed | RSS 2.0 feed populated from live posts |
| 16 | `/sitemap.xml` | Dynamic Feed | XML Sitemap with priority weighting & dynamic post timestamps |
| 17 | `/robots.txt` | Directives | Search engine crawl directives (disallowing `/admin`) |

---

## Technical Stack

* **Frontend**: Astro v4 (Static Site Generation), Tailwind CSS, Fraunces serif + Inter typography
* **Analytics**: Google Tag Manager (`GTM-KGP8QDFC`) installed in `<head>` and `<noscript>` in `<body>`
* **Hosting (Frontend)**: GitHub Pages with custom domain `onerishi.in` via automated GitHub Actions (`deploy.yml`)
* **Backend API**: FastAPI (Python 3.11.9) hosted on Render at `https://onerishi-website.onrender.com`
* **Database**: SQLite with SQLAlchemy ORM (auto-seeded with 7 writing monographs)
* **Auth**: Single-admin master key with bcrypt password verification and JWT bearer tokens
* **Continuous Delivery**: Publishing from the CMS triggers automated GitHub Actions rebuilds via `repository_dispatch`

---

## Local Development & Operations

### 1. Frontend
```bash
npm install
npm run dev        # Runs on http://localhost:4321
npm run build      # Static production build into dist/
```

### 2. Backend (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Interactive Swagger API docs: `http://localhost:8000/docs` (Local) or `https://onerishi-website.onrender.com/docs` (Live Cloud).

### 3. CMS Administration
* **Live Admin CMS**: [`https://onerishi.in/admin/login`](https://onerishi.in/admin/login)
* **Local Admin CMS**: [`http://localhost:4321/admin/login`](http://localhost:4321/admin/login)
* Enter master password (`onerishi2024`) to create, preview, edit SEO fields, and publish articles.

---

## Design system quick reference

Full detail in `DESIGN-TOKENS.md`. Summary:
- Colors: `#F7F4EF` bg · `#1B1B18` ink · `#C1592B` terracotta accent · `#1F3A3D` teal accent
- Fonts: **Fraunces** (headlines/serif), **Inter** (body/UI/sans)
- Motion: subtle only — fade-up on scroll, hover lift + border color shift on cards

