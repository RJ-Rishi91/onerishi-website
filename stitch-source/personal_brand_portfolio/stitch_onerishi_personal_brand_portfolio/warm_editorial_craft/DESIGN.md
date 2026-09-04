---
name: Warm Editorial Craft
colors:
  surface: '#fcf9f3'
  surface-dim: '#dcdad4'
  surface-bright: '#fcf9f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ee'
  surface-container: '#f0ede8'
  surface-container-high: '#ebe8e2'
  surface-container-highest: '#e5e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#56423b'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0eb'
  outline: '#8a7269'
  outline-variant: '#ddc0b6'
  surface-tint: '#a04114'
  primary: '#9d3e11'
  on-primary: '#ffffff'
  primary-container: '#bd5628'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb599'
  secondary: '#486366'
  on-secondary: '#ffffff'
  secondary-container: '#c8e5e9'
  on-secondary-container: '#4c676a'
  tertiary: '#00647f'
  on-tertiary: '#ffffff'
  tertiary-container: '#007fa0'
  on-tertiary-container: '#fbfdff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#ffb599'
  on-primary-fixed: '#370e00'
  on-primary-fixed-variant: '#7f2b00'
  secondary-fixed: '#cbe8eb'
  secondary-fixed-dim: '#afcccf'
  on-secondary-fixed: '#021f22'
  on-secondary-fixed-variant: '#304b4e'
  tertiary-fixed: '#bbe9ff'
  tertiary-fixed-dim: '#75d2f7'
  on-tertiary-fixed: '#001f29'
  on-tertiary-fixed-variant: '#004d63'
  background: '#fcf9f3'
  on-background: '#1c1c19'
  surface-variant: '#e5e2dd'
typography:
  display-xl:
    fontFamily: Libre Caslon Text
    fontSize: 56px
    fontWeight: '400'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 38px
    fontWeight: '400'
    lineHeight: 46px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 30px
    fontWeight: '400'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Libre Caslon Text
    fontSize: 22px
    fontWeight: '400'
    lineHeight: 30px
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 30px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-2xs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4.5rem
  space-4xl: 6rem
  gutter-mobile: 1rem
  gutter-desktop: 2rem
  max-width-editorial: 720px
  max-width-container: 1200px
---

## Brand & Style
The design system channels an intentional, literary editorial sensibility tailored for an independent creator and practitioner. It bridges classical magazine art direction with modern digital product restraint. The emotional tone is grounded, literate, human, and quietly confident.

Key aesthetic anchors:
- **Literary Materiality:** Drawing inspiration from print journals, broadsheets, and curated monographs. Every layout feels typeset rather than assembled.
- **Quiet Dignity:** Absence of performative visual noise, hyper-saturated gradients, or trendy glass effects. White space functions as room for contemplation.
- **Physical Restraint:** Transitions are deliberate and cinematic with gentle decelerations. Interactions mimic physical paper and book craft rather than bouncy software springs.

## Colors
The palette evokes archival paper stock, mineral pigments, and rich printing inks.

- **Primary Accent (`#C1592B` - Terracotta):** Used selectively for focal anchors, key interactive states, reading progress, and signature editorial highlights. It represents warmth and human touch.
- **Secondary Accent (`#1F3A3D` - Muted Teal):** Provides deep, intellectual counterweight. Used for contextual tags, thematic sub-sections, dark editorial surfaces, and balanced contrast against terracotta.
- **Base Canvas (`#F7F4EF` - Warm Off-White):** The foundational paper tone. Avoid pure `#FFFFFF` across primary layouts to eliminate clinical digital harshness.
- **Ink / Text (`#1B1B18` - Warm Near-Black):** Deep soot ink with organic warmth. Ensures high-legibility typographic hierarchy without the severe contrast of digital black.
- **Borders & Rules (`#E6E1D8` - Warm Graystone):** Delicate hairline borders that establish structural grid definition without visual clutter.
- **Surface Elevation (`#FFFFFF` - Pure Bone):** Used sparingly for card faces to separate them cleanly from the `#F7F4EF` canvas.

## Typography
Typographic pairings embody classical editorial contrast:
- **Headlines (Libre Caslon Text / Fraunces):** Expressive, high-character serif style applied to essay headers, display quotes, and sectional anchors. It introduces literary gravitas and warmth. Italic variants should be used selectively for emphasis, book titles, and editorial subheads.
- **Body, UI & Metadata (Inter):** Neutral, humanist sans-serif. Highly legible at small sizes, handling UI scaffolding, body prose, navigational nodes, and technical captions with clarity.
- **Editorial Proportions:** Longform body copy must stay within 65–75 characters per line to maintain rhythm and avoid cognitive fatigue.

## Layout & Spacing
The layout leverages an architectural grid with asymmetric editorial moments:
- **Grid Architecture:** 12-column grid on desktop (`1200px` max width), 6 columns on tablet, and 4 columns on mobile. Margins set to `1.5rem` on mobile and `3rem` on desktop.
- **Editorial Measure:** Essays, reflections, and case study narratives constrain to `max-width-editorial` (`720px`), centered or offset against margin marginalia (callouts, footnotes, metadata).
- **Rhythm:** Vertical pacing relies on open multiples of `1.5rem` and `3rem`. Avoid dense UI clustering; give headers generous top breathing room (`space-3xl`) to signal thematic shifts.

## Elevation & Depth
Depth is produced through subtle surface contrasts and physical tactile resistance rather than synthetic drop shadows.

- **Surface Layering:** The primary canvas is `#F7F4EF`. Cards and inset panels rest on crisp `#FFFFFF` bone surfaces framed with `#E6E1D8` hairlines (1px solid).
- **Physical Elevation:** Rest states are flat with zero ambient blur. On interaction, items elevate subtly:
  - `transform: translateY(-2px)` to `-3px` maximum.
  - Shadow: `0 8px 24px -6px rgba(27, 27, 24, 0.07), 0 2px 6px -2px rgba(27, 27, 24, 0.04)`.
- **Border Activation:** During hover or active focus, card borders shift deliberately from `#E6E1D8` to `#C1592B` (Terracotta) with a gentle `200ms ease-out` transition.

## Shapes
Geometry is disciplined, architectural, and restrained.

- **Corner Radii:** Strict soft treatment (`roundedness: 1`). Interactive elements and cards use a modest `4px` (`0.25rem`) radius, with outer macro containers capping at `8px` (`0.5rem`).
- **Pill Exceptions:** Tags and category badges may leverage soft architectural bounding, but avoid bubble-like treatments. Never use full pill geometries on primary inputs or structural cards.
- **Dividers:** Crisp 1px rules colored `#E6E1D8` delineate horizontal narrative breaks, resembling the clean scoring of fine stationery.

## Components

### Buttons
- **Primary:** Background `#C1592B`, text `#FFFFFF`, radius `4px`, padding `10px 20px`. Hover: `#A94C23` with no scale jump. Active: slight depth press (`translateY(1px)`).
- **Secondary (Editorial Outline):** Background transparent, border `1px solid #1B1B18`, text `#1B1B18`. Hover: background `#1B1B18`, text `#F7F4EF`.
- **Tertiary (Text Link):** Understated inline serif or sans link with a subtle bottom border (`1px solid rgba(193, 89, 43, 0.4)`), expanding to full terracotta opacity on hover.

### Cards & Insets
- **Editorial Post Card:** Background `#FFFFFF`, border `1px solid #E6E1D8`, radius `4px`, padding `24px`.
- **Card Hover State:** Shifts translateY by `-3px`, box-shadow becomes warm diffuse, and the outline transitions to `#C1592B`.
- **Imagery Containers:** Clean 1:1 or 16:9 crop with a 1px inner border overlay (`rgba(27, 27, 24, 0.05)`). Apply a subtle warm sepia/amber color tint (`mix-blend-mode: multiply` at 3-5%) to all real photography placeholders for unified canvas harmony.

### Chips & Metadata Tags
- **Appearance:** Text uppercase, `11px`, `letter-spacing: 0.08em`, font Inter SemiBold.
- **Palette:** Subtle muted teal (`#1F3A3D`) background tint at 8% opacity (`rgba(31, 58, 61, 0.08)`), text `#1F3A3D`, border `1px solid rgba(31, 58, 61, 0.15)`. Radius `3px`.

### Inputs & Forms
- **Field Base:** Background `#FFFFFF`, border `1px solid #E6E1D8`, radius `4px`, padding `12px 16px`, text `#1B1B18`.
- **Focus:** Border color `#C1592B`, outline: `2px solid rgba(193, 89, 43, 0.2)` with 0 offset.

### Selection Controls (Checkboxes & Radios)
- **Base:** Hairline `#E6E1D8` borders on `#FFFFFF` base. Radius `3px` (checkbox), circle (radio).
- **Selected:** Solid `#C1592B` fill with `#FFFFFF` checkmark or center dot.

### Lists & Article Feeds
- **Feed Rows:** Minimalist list items bordered by `1px solid #E6E1D8` bottom rules. Hover reveals terracotta accent on article titles, with metadata dates remaining grounded in warm gray tones.