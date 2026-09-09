# Sitemap & linking map — OneRishi

## Page tree (text form)

```
OneRishi.in (Home) ────────────────────────────── [/]
│
├── Work                                        [/work/]
│   └── Case Studies (Dynamic Collections)
│       ├── Google DevFest Udaipur 2024         [/work/google-devfest-udaipur-2024/]
│       ├── Gazette Collective                  [/work/gazette-collective/]
│       └── Web & Digital Systems               [/work/web-digital-projects/]
│
├── Writing                                     [/writing/]
│   └── Field Dispatches (Dynamic Collections)
│       ├── Distribution Before Destination     [/writing/distribution-before-destination/]
│       ├── What Building Gazette Collective... [/writing/community-journalism-gazette-collective/]
│       ├── Why Engineering Empathy...          [/writing/engineering-empathy-growth-marketer/]
│       ├── The Architecture of High-Converting [/writing/the-architecture-of-high-converting-b2b-web-experiences/]
│       ├── Operational Lessons from Directing  [/writing/operational-lessons-directing-tech-events/]
│       ├── Learning to Build in Public...      [/writing/learning-to-build-in-public-without-burning-out/]
│       └── Cultivating Taste: The Unspoken...  [/writing/cultivating-taste-unspoken-lever/]
│
├── About                                       [/about/]
├── Labs                                        [/labs/]
├── Philosophy                                  [/philosophy/]
├── Impact                                      [/impact/]
├── Collaborate                                 [/collaborate/]
├── Contact                                     [/contact/]
│
├── Admin CMS (Restricted / Private)
│   ├── Author Authentication Screen            [/admin/login]
│   ├── Posts Dashboard (All / Published / Scheduled / Drafts) [/admin]
│   ├── Editorial Calendar (Timed Schedule Grid) [/admin/calendar]
│   └── Monograph Editor & Publishing Terminal  [/admin/editor]
│
├── Cloud API Endpoints (FastAPI Backend @ Render)
│   ├── Health Check                            [GET  /api/health]
│   ├── Published Monograph Feed                [GET  /api/posts]
│   ├── Single Post Query by Slug               [GET  /api/posts/{slug}]
│   ├── Admin Master Key Authentication         [POST /api/admin/login]
│   ├── Admin Posts Directory (incl. Drafts)    [GET  /api/admin/posts]
│   ├── Create Monograph (incl. Scheduling)     [POST /api/admin/posts]
│   ├── Bulk CSV Post Import                    [POST /api/admin/posts/bulk-import]
│   ├── Get Post by ID                          [GET  /api/admin/posts/{id}]
│   ├── Update Monograph & SEO Overrides        [PUT  /api/admin/posts/{id}]
│   ├── Delete Monograph                        [DELETE /api/admin/posts/{id}]
│   ├── System Media Upload (Cover / OG)        [POST /api/admin/upload]
│   └── Interactive API Docs (Swagger UI)       [GET  /docs]
│
└── Feeds & Endpoints
    ├── RSS 2.0 Feed                            [/rss.xml]
    ├── XML Search Engine Sitemap               [/sitemap.xml]
    └── Robots Directives                       [/robots.txt]
```

## Full linking map

Every internal link, by source page. "Nav" links (present identically on
every page) are listed once at the top and not repeated per page below.

**On every page (header + footer, all builds):**
- Header → Home, Work, Writing, About, Labs, Say Hello (→ Contact)
- Footer → same 5, plus Philosophy, Impact, Collaborate, Contact, social links (GitHub, LinkedIn, YouTube), and **Admin Login** button (in Explore column and colophon bar)

| From | Link | To | Type |
|---|---|---|---|
| Home | "See my work" CTA | Work | button |
| Home | Latest Writing cards (×3) | Blog post template | card click |
| Home | "Read all writing" | Writing | text link |
| Home | "Start a Conversation" CTA | Contact (or Collaborate) | button |
| Home | "More About Rushal" | About | text link |
| Work | Case study cards (×3) | Case study template | card click |
| Work | Closing CTA | Collaborate | button |
| Writing | Post cards | Blog post template | card click |
| Writing | Filter pills | Writing (filtered view) | in-page state |
| About | "Read the full philosophy →" | Philosophy | text link |
| About | Closing CTA | Collaborate | button |
| About | "See my work" | Work | text link |
| Philosophy | Closing line | About or Work | text link |
| Impact | Closing CTA | Collaborate | button |
| Collaborate | "Hire Me" card | Contact (tagged: hire) | button |
| Collaborate | "Media & Community Projects" card | Contact (tagged: media) | button |
| Collaborate | "Junior Journalist/Mentorship" card | Contact (tagged: mentorship) | button |
| Footer | "Admin Login" (pill + list link) | Admin Login (`/admin/login`) | button & link |
| Case study template | "Back to Work" | Work | text link |
| Case study template | "Next project" | Case study template (next item) | arrow nav |
| Blog post template | Related posts (×2-3) | Blog post template (other posts) | card click |
| Blog post template | Author bio | About (optional) | text link |
| Admin Login | "Log In" | Posts Dashboard (`/admin`) | form submit |
| Admin Login | "Return to onerishi.in" | Home (`/`) | text link |
| Admin Dashboard | "+ New Post" | Post Editor (`/admin/editor`) | button |
| Admin Dashboard | Post table row edit | Post Editor (`/admin/editor?id={id}`) | row click |
| Admin Dashboard | "Log Out" | Admin Login (`/admin/login`) | button |
| Admin Editor | "Save Draft" / "Publish" | API Backend → GitHub Actions | button |
| Admin Editor | "Back to Posts" | Posts Dashboard (`/admin`) | button |

## Notes for implementation

- Work and Writing are the two "index → template" dynamic collection relationships on the public site.
- Admin CMS routes (`/admin`, `/admin/editor`, `/admin/login`) are excluded from search indexing via `public/robots.txt` (`Disallow: /admin`).
- The XML Sitemap (`/sitemap.xml`) and RSS 2.0 Feed (`/rss.xml`) dynamically query the live cloud API backend (`https://onerishi-website.onrender.com/api/posts`) with automatic fallback to local markdown collections.
- Philosophy, Impact, and Collaborate are deliberately absent from primary header nav — this was a considered IA decision, reached via footer and contextual inline cross-links.
- Contact is the single conversion endpoint — every "Say Hello," "Collaborate," and card CTA across the site resolves there.
- Publishing from the CMS triggers an automated GitHub Actions `repository_dispatch` (`cms_post_published`) to rebuild and deploy `onerishi.in` live.

