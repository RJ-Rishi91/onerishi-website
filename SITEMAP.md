# Sitemap & linking map — OneRishi

## Page tree (text form)

```
OneRishi (Home)
│
├── Work                              [primary nav]
│   └── Case study (template)         [dynamic — one page per project]
│       ├── Google DevFest Udaipur 2024
│       ├── Gazette Collective
│       └── Web & Digital Projects
│
├── Writing                           [primary nav]
│   └── Blog post (template)          [dynamic — one page per post]
│       categories: Marketing Experiments · Marketing × Tech ·
│                   Building on the Internet · Projects & Behind-the-Scenes ·
│                   Career & Learning
│
├── About                             [primary nav]
├── Labs                              [primary nav]
│
├── Philosophy                        [footer nav, linked from About]
├── Impact                            [footer nav, linked from Home/Work]
├── Collaborate                       [footer nav, linked from About/Work]
└── Contact                           [footer nav, "Say Hello" CTA target]
```

## Full linking map

Every internal link, by source page. "Nav" links (present identically on
every page) are listed once at the top and not repeated per page below.

**On every page (header + footer, all 11 builds):**
- Header → Home, Work, Writing, About, Labs, Say Hello (→ Contact)
- Footer → same 5, plus Philosophy, Impact, Collaborate, Contact, social links (GitHub, LinkedIn, YouTube)

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
| Case study template | "Back to Work" | Work | text link |
| Case study template | "Next project" | Case study template (next item) | arrow nav |
| Blog post template | Related posts (×2-3) | Blog post template (other posts) | card click |
| Blog post template | Author bio | About (optional) | text link |

## Notes for implementation

- Work and Writing are the only two "index → template" relationships on the site. Every other page is standalone.
- Philosophy, Impact, and Collaborate are deliberately absent from primary nav — this was a considered IA decision (see README open-decisions log if it needs re-litigating), not an oversight to fix.
- Contact is the single conversion endpoint — every "Say Hello," "Collaborate," and card CTA across the site should resolve there, optionally passing an inquiry-type tag from Collaborate.
