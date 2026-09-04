# OneRishi — Full Build Spec
**onerishi.in · Rushal S. · Marketing × Technology × Creativity**

Working checklist for everything going into Stitch today. 9 pages + 2 dynamic templates = 11 builds.

---

## Design system (applies to every page)

**Colors**
| Role | Hex |
|---|---|
| Background | `#F7F4EF` (warm off-white) |
| Text/ink | `#1B1B18` (warm near-black) |
| Primary accent | `#C1592B` (terracotta) |
| Secondary accent | `#1F3A3D` (muted teal) |

**Fonts**
- Headlines: **Fraunces** (serif)
- Body/UI: **Inter** (sans)

**Animation principles** — editorial, not flashy:
- Fade-up on scroll for section reveals (200-300ms, subtle, no bounce/spring easing)
- Link/button hover: color shift to terracotta + underline reveal (no scale/zoom effects)
- Case study & post cards: slight lift (2-4px translateY) + border-color shift on hover, nothing else
- Page transitions: simple crossfade, no slide/wipe gimmicks
- No parallax, no auto-playing carousels, no scroll-jacking
- Reduced-motion: everything above must have a static fallback (no motion-dependent info)

**Imagery rule (all pages):** real photos or clean typographic placeholders only. No AI-generated faces, no unrelated stock photography (business people, motorcycles, etc.), no fabricated data/stat visuals.

**Navigation**
- Primary (header): Home · Work · Writing · About · Labs + "Say Hello" CTA button
- Secondary (footer + contextual links): Philosophy · Impact · Collaborate · Contact

---

## 1. Home
**Purpose:** first impression + entry point to everything else.

**Content:**
- Hero headline (Fraunces): "I build, market and execute — bringing technology, creativity and communication together to turn ideas into real-world projects."
- Short manifesto paragraph (2-3 sentences, first person)
- Credibility strip: Google DevFest Udaipur 2024, Gazette Collective, 94K+ YouTube audience, Web/dev projects
- Latest Writing: 3 post preview cards
- Footer: nav, social links

**Images needed:**
- 1 hero photo placeholder (real photo of Rushal — not AI-generated)
- No other imagery required; credibility strip is text + icon, not photos

**Animation:**
- Hero text fades up on load (once, not on every scroll)
- Credibility strip items fade up staggered (80ms delay each) on scroll into view
- Post cards: hover lift + terracotta border

---

## 2. Work
**Purpose:** portfolio proof.

**Content:**
- Page header + one-line intro
- 3 case-study cards: DevFest 2024, Gazette Collective, Web & Digital Projects
- YouTube audience-growth highlight (separate smaller feature, not a stats dashboard)
- Closing CTA → Collaborate

**Images needed:**
- 1 representative image per case study (event photo for DevFest, publication/screenshot for Gazette, project screenshot for Web work) — real, not stock
- YouTube highlight: channel screenshot or thumbnail grid, not a fabricated graph

**Animation:**
- Case-study cards: hover lift + image slight zoom (1.03x max, no more)
- Fade-up on scroll for each card

---

## 3. Writing (blog index)
**Purpose:** SEO engine + thought leadership.

**Content:**
- Page header + intro line
- Category filter pills: Marketing Experiments, Marketing × Tech, Building on the Internet, Projects & Behind-the-Scenes, Career & Learning
- Post grid — one featured (larger) + standard cards
- Pagination / load more

**Images needed:**
- 1 cover image per post (varies in size for featured vs. standard cards)
- Category icons: optional, simple line-style only if used

**Animation:**
- Filter pills: active state = terracotta fill, smooth 150ms transition on switch
- Post grid re-flows with a simple fade (no flip/masonry animation)

---

## 4. About
**Purpose:** where recruiters/clients actually decide.

**Content:**
- Header + photo
- Opening narrative (how Rushal ended up at the marketing/tech intersection)
- "What I do" (Demand Generation Specialist work)
- "What I build outside that" (events, Gazette Collective, independent projects)
- "How I work" (tone/values)
- CTA → Work / Collaborate
- Contextual links to Philosophy and Collaborate

**Images needed:**
- 1 real photo of Rushal (header)
- Optional: 1-2 candid/work-in-progress photos alongside narrative sections

**Animation:**
- Sections fade up sequentially on scroll
- Photo: subtle static presentation, no ken-burns/zoom effect

---

## 5. Labs
**Purpose:** honest work-in-progress space.

**Content:**
- Header + subtitle explaining "not everything here is finished"
- Status-tagged entries (Draft / In Progress / Shipped / Archived) — expect only 1-3 real entries at launch

**Images needed:**
- None required — text/status-card driven page

**Animation:**
- Status tag color is the only "animation-adjacent" element — keep static, no pulsing/blinking badges (reads as broken, not lively)
- Cards fade up on scroll

---

## 6. Philosophy
**Purpose:** narrative depth, linked from About.

**Content:**
- Header + subtitle
- Long-form first-person sections on why Rushal builds the way he does
- "What I believe" — 4-5 short principle statements
- One large pull-quote

**Images needed:**
- None required, or one editorial-style photo if available — text-led page, imagery is optional

**Animation:**
- Pull-quote fades in distinctly (slightly slower, 400ms) as a visual pause point
- Otherwise same fade-up-on-scroll as other long-form pages

---

## 7. Impact
**Purpose:** credibility markers, linked from Home/Work.

**Content:**
- Header
- Recognition section — **placeholder pending Veer Gatha/Ministry of Defence confirmation**
- Social-impact section — Gazette Collective's community journalism work
- Collaborations section — DevFest, Gazette Collective
- CTA → Collaborate

**Images needed:**
- Recognition section: hold empty/placeholder until confirmed — do not fill with a stock award image
- Social-impact section: real photos from Gazette Collective work if available

**Animation:**
- Standard fade-up on scroll, nothing page-specific

---

## 8. Collaborate
**Purpose:** conversion page for partners, linked from About/Work.

**Content:**
- Header
- 3 collaboration-type cards: Hire Me, Media & Community Projects, Junior Journalist/Mentorship
- Each links to Contact, optionally pre-tagging inquiry type

**Images needed:**
- None required — text/card driven

**Animation:**
- Card hover: same lift + terracotta border treatment as Work cards, for visual consistency

---

## 9. Contact
**Purpose:** the "Say Hello" CTA destination.

**Content:**
- Header: "Say Hello"
- Form: Name, Email, Message
- Direct email + social links (GitHub, LinkedIn, YouTube)

**Images needed:**
- None

**Animation:**
- Form field focus: border color shifts to terracotta, no other motion
- Submit button: standard hover state only, no loading spinner gimmicks — a simple text change ("Sending…" → "Sent") is enough

---

## 10. Single blog post (template)
**Purpose:** houses every Writing entry.

**Content:**
- Category tag, title, date, read time, byline
- Long-form body with support for pull-quotes and image blocks
- "Written from experience" callout option
- Footer: author bio, 2-3 related posts, share links

**Images needed:**
- 1 cover image per post (reused from Writing index)
- Inline images as needed per post — real screenshots/photos relevant to the content, no generic stock

**Animation:**
- Optional: thin reading-progress bar at top of viewport (subtle, 2px, terracotta) — nice-to-have, not required
- Related-post cards: same hover treatment as index cards

---

## 11. Single case study (template)
**Purpose:** houses every Work entry.

**Content:**
- Title, role/category tag, timeframe
- Problem / Approach / Outcome structure
- Optional image gallery
- Real-language outcomes (no invented metrics)
- Footer: back to Work, "Next project" nav

**Images needed:**
- 1 hero image + optional gallery (2-4 images) per case study — real project/event photos only

**Animation:**
- Gallery: simple fade between images if more than one, no auto-advancing carousel
- "Next project" link: standard hover underline

---

## Build order (recommended)
1. Home — sets the visual language everything else follows
2. Work + case study template together — they're interdependent
3. Writing + blog post template together — same reason
4. About
5. Contact (fast, low-risk, good to lock early)
6. Philosophy, Impact, Collaborate, Labs — the secondary tier, once the core visual system is proven

Send me pages as you generate them and I'll check each against this spec.
