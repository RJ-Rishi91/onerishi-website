# OneRishi — onerishi.in

Personal brand site for Rushal S. — Marketing × Technology × Creativity.
Editorial-magazine aesthetic, warm and approachable, not corporate.

This repo/handoff covers 9 pages + 2 dynamic templates (11 builds total).
Design source: Google Stitch exports, refined in this handoff for accuracy.

See also: `SITEMAP.md` (page tree + full linking map), `DESIGN-TOKENS.md`
(colors, fonts, motion), `CONTENT-GUIDELINES.md` (non-negotiable content rules).

---

## Site identity

- **Domain:** onerishi.in
- **Brand:** OneRishi
- **Displayed name:** Rushal S. (not "Rushal Suthar" — confirmed choice)
- **Hero positioning line:** "I build, market and execute — bringing technology, creativity and communication together to turn ideas into real-world projects."
- **Site purpose:** personal brand / thought leadership, for recruiters, potential clients/collaborators, and the marketing × tech community

## Navigation

- **Primary (header, all pages, identical):** Home · Work · Writing · About · Labs, plus a "Say Hello" CTA button (visually distinct from nav links) → Contact
- **Secondary (footer, all pages):** Philosophy · Impact · Collaborate · Contact
- Secondary pages are also reached via contextual inline links from relevant primary pages (see `SITEMAP.md` for exact link sources) — this is intentional, not a missing dropdown. No folding/hamburger "more" menu — rejected on purpose, see prior design discussion if it resurfaces.

## Pages (11 builds)

| # | Page | Type | Nav |
|---|---|---|---|
| 1 | Home | static | primary |
| 2 | Work | index | primary |
| 3 | Writing | index | primary |
| 4 | About | static | primary |
| 5 | Labs | static | primary |
| 6 | Philosophy | static | secondary/footer |
| 7 | Impact | static | secondary/footer |
| 8 | Collaborate | static | secondary/footer |
| 9 | Contact | static | secondary/footer + CTA target |
| 10 | Case study (template) | dynamic, under Work | — |
| 11 | Blog post (template) | dynamic, under Writing | — |

## Build order (recommended)

1. Home — sets the visual language everything else follows
2. Work + Case study template together (interdependent)
3. Writing + Blog post template together (interdependent)
4. About
5. Contact
6. Philosophy, Impact, Collaborate, Labs (secondary tier)

## Design system quick reference

Full detail in `DESIGN-TOKENS.md`. Summary:
- Colors: `#F7F4EF` bg · `#1B1B18` ink · `#C1592B` terracotta accent · `#1F3A3D` teal accent — **exactly these 4 hex values, no generated tonal/Material palette**
- Fonts: **Fraunces** (headlines/serif), **Inter** (body/UI/sans)
- Motion: subtle only — fade-up on scroll, hover lift + border color shift on cards, no bounce/parallax/auto-play

## Content rules (non-negotiable)

Full detail in `CONTENT-GUIDELINES.md`. The short version: no fabricated statistics, no invented projects/achievements, no AI-generated faces, no unrelated stock photography. Real content only, placeholders left visibly as placeholders until real material is supplied.

## Open decisions — resolve before final launch

- [ ] **Home tagline:** current draft says "Creative Technologist & Strategist" under the photo — not yet confirmed against the agreed positioning ("Marketing × Technology × Creativity"). Keep or revert.
- [ ] **Writing page:** two conflicting design exports exist from the Stitch phase — confirm final layout before implementing.
- [ ] **Veer Gatha / Ministry of Defence recognition:** unconfirmed. Impact page currently shows a "details pending confirmation" placeholder — do not fill in specifics until verified.
- [ ] **Labs entries:** currently 2 real entries (Gazette Collective publishing tooling, DevFest ops runbooks). Add more only if genuinely real and in progress.
- [ ] **Collaborate discoverability:** currently reached via footer + About/Work links only. Consider adding a small secondary link near the "Say Hello" CTA on Home if conversion tracking shows it's under-found.

## Known implementation bugs from the Stitch phase (verify fixed)

- Labs page: STACK/pkg metadata row was overlapping/wrapping incorrectly in the last export — check responsive behavior on long stack lists.
