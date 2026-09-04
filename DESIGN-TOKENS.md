# Design Tokens — OneRishi

Strict design token definitions for onerishi.in.
Reference: onerishi_build_spec.md & warm_editorial_craft design system.

## 1. Palette (Exactly these 4 hex values, no generated tonal/Material palette)

| Role | Hex | Name | Purpose |
|---|---|---|---|
| Background | `#F7F4EF` | Warm off-white | Base paper canvas, eliminates clinical digital harshness |
| Text / Ink | `#1B1B18` | Warm near-black | Soot ink, high legibility, humanist contrast |
| Primary Accent | `#C1592B` | Terracotta | Focus anchors, active states, reading progress, signature highlights |
| Secondary Accent | `#1F3A3D` | Muted Teal | Intellectual counterweight, tags, editorial indicators, deep contrast |

**Card Face & Surfaces:**
- Card Face / Elevation: `#FFFFFF` (Pure Bone)
- Hairlines & Borders: `#E6E1D8` / `rgba(27, 27, 24, 0.12)`

## 2. Typography

- **Headlines & Display:** **Fraunces** (Serif, variable optical sizing)
  - Display XL: 56px / 64px line-height (desktop), 38px / 46px (mobile)
  - Headline LG: 40px / 48px (desktop), 30px / 38px (mobile)
  - Headline MD: 28px / 36px
  - Headline SM: 22px / 30px
- **Body, UI & Navigation:** **Inter** (Humanist Sans)
  - Body LG: 18px / 30px line-height
  - Body MD: 16px / 26px line-height
  - Body SM: 14px / 22px line-height
  - Label MD: 13px / 18px line-height (nav, buttons)
  - Label SM: 11px / 16px line-height, letter-spacing 0.08em uppercase (chips, metadata)
- **Code & Specs:** JetBrains Mono / SF Mono / monospace

## 3. Spacing & Grid

- Container Max Width: `1200px`
- Editorial Measure: `720px` (body prose 65–75 characters per line)
- Gutter: `16px` (`1rem`) on mobile, `32px` (`2rem`) on desktop
- Vertical Rhythm: Multiples of `1.5rem` (`24px`) and `3rem` (`48px`)

## 4. Animation & Interactions

- **Speed:** Subtle 200–300ms ease-out.
- **Hover Lift:** `translateY(-2px)` to `-3px` max, soft diffuse shadow `0 12px 28px -6px rgba(27, 27, 24, 0.08)`, border shifts to `#C1592B`.
- **Motion Restraint:** No bounce, no spring easing, no auto-playing carousels, no scroll-jacking.
- **Accessibility:** Immediate static fallback on `@media (prefers-reduced-motion: reduce)`.
