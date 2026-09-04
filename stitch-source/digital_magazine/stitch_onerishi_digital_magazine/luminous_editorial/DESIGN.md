---
name: Luminous Editorial
colors:
  surface: '#fff8f5'
  surface-dim: '#e0d8d5'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf2ee'
  surface-container: '#f4ece8'
  surface-container-high: '#eee7e3'
  surface-container-highest: '#e9e1dd'
  on-surface: '#1e1b19'
  on-surface-variant: '#3f484e'
  inverse-surface: '#33302d'
  inverse-on-surface: '#f7efeb'
  outline: '#6f787f'
  outline-variant: '#bfc8cf'
  surface-tint: '#00658b'
  primary: '#006184'
  on-primary: '#ffffff'
  primary-container: '#007ba7'
  on-primary-container: '#f5faff'
  inverse-primary: '#7cd0ff'
  secondary: '#5d5f5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#636564'
  tertiary: '#834d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#a36410'
  on-tertiary-container: '#fff8f4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c4e7ff'
  primary-fixed-dim: '#7cd0ff'
  on-primary-fixed: '#001e2c'
  on-primary-fixed-variant: '#004c69'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c7c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdcbc'
  tertiary-fixed-dim: '#ffb86c'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#683c00'
  background: '#fff8f5'
  on-background: '#1e1b19'
  surface-variant: '#e9e1dd'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  stack-xs: 0.25rem
  stack-sm: 1rem
  stack-md: 2rem
  stack-lg: 4rem
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 5vw
---

## Brand & Style

This design system merges the authoritative weight of traditional editorial journalism with the ethereal, high-tech depth of Glassmorphism. The brand personality is intellectual yet modern—evoking the feeling of a premium digital magazine floating in a physical space. 

The aesthetic centers on transparency and refraction. By using frosted glass surfaces, we create a sense of organized complexity, where content layers overlap to suggest deep informational hierarchy. The target audience values precision, clarity, and a sophisticated reading experience that feels cutting-edge.

**Core Principles:**
- **Translucency as Hierarchy:** Depth is communicated through varying levels of background blur and opacity rather than heavy shadows.
- **Editorial Authority:** High-contrast serif typography grounds the "floating" UI, ensuring the magazine roots are never lost.
- **Precision Accents:** Use "Udaipur Blue" sparingly for functional highlights to maintain a calm, focused environment.

## Colors

The palette is anchored by "Udaipur Blue" (#007BA7), used strictly for interactive affordances, progress indicators, and key category tags. 

**Adaptive Glass Logic:**
- **Light Mode:** Uses a base of Stone 50 (#FAFAF9) with glass panels at 70% opacity white. Borders are a crisp `stone-200/40`.
- **Dark Mode:** Uses a base of Stone 950 (#0C0A09) with glass panels at 70% opacity Stone 900. Borders are a subtle `white/10`.

Backgrounds should utilize soft, organic gradients (e.g., stone-200 to white) to ensure the backdrop-blur has "texture" to distort, enhancing the glass effect.

## Typography

The typographic system relies on a high-contrast pairing: the intellectual **Newsreader** for all editorial content and the precision-engineered **Hanken Grotesk** for interface elements and body metadata.

**Usage Guidelines:**
- **Editorial Headlines:** Use Newsreader with tighter tracking and optical sizing for large displays.
- **Utility Text:** Labels, buttons, and timestamps use Hanken Grotesk to provide a clean, "app-like" contrast to the serif stories.
- **Vertical Rhythm:** Maintain generous line-heights in body copy to ensure legibility against blurred glass backgrounds.

## Layout & Spacing

This design system uses a **Fluid Editorial Grid** that emphasizes verticality and depth. 

**Layering Strategy:**
- **Overlapping Elements:** Content cards should overlap section headers by 40-80px to showcase the `backdrop-blur` effect.
- **Vertical Gutters:** Use wide gutters (24px+) to allow the background to "breathe" between glass panels.
- **Responsive Behavior:** 
    - **Desktop:** 12-column grid with asymmetric layouts (e.g., 8-column main story, 4-column glass sidebar).
    - **Mobile:** Single column with full-bleed glass panels and 16px margins.

## Elevation & Depth

Depth is achieved through **optical refraction** rather than shadows. 

1.  **Level 0 (Base):** The document background. Usually a subtle mesh gradient.
2.  **Level 1 (Panels):** `backdrop-blur-xl` (24px) with a 1px border. In light mode, use a white inner glow (top-left) to simulate a glass edge.
3.  **Level 2 (Floating/Interactive):** Increased blur (`backdrop-blur-2xl`) and a slightly higher opacity border.
4.  **Transitions:** When a user hovers over a glass panel, increase the background opacity by 5% and slightly sharpen the border to indicate focus.

Avoid traditional drop shadows; if a shadow is necessary for legibility, use a very large, ultra-low opacity (2-4%) shadow that matches the primary hue.

## Shapes

The shape language is **Refined Geometric**. While we use rounded corners to soften the "tech" feel, we keep them restrained to maintain the magazine's professional rigor.

- **Main Panels:** Use `rounded-lg` (1rem/16px) to create a soft, inviting frame for long-form text.
- **Interactive Elements:** Buttons and tags use `rounded-full` (pill) to distinguish them from structural content containers.
- **Media:** Photography should follow the panel radius (16px) or, for specific artistic layouts, be completely sharp (0px) to contrast with the glass containers.

## Components

**Glass Panels (Cards):**
The primary container. Must include `backdrop-blur-xl`, a 1px border (adaptive color), and `padding: 2rem`. For article previews, the image should be slightly inset or bleed to the top.

**Buttons:**
- **Primary:** Solid Udaipur Blue with white text. High contrast, no blur.
- **Ghost:** Transparent background with the 1px glass border style. Text in Udaipur Blue or neutral depending on context.

**Editorial Tags:**
Small, Hanken Grotesk Bold, all-caps. These sit above headlines. Use a light Udaipur Blue tint for the background (10% opacity) with 100% opacity text.

**Input Fields:**
Minimalist glass style. Bottom-border only (2px) which glows in Udaipur Blue when focused. 

**Progress Indicators:**
For long-form reading, a thin (2px) Udaipur Blue bar at the very top of the viewport, appearing to sit "above" the glass panels.