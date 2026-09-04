# Design System: The Technical Editorial

## 1. Overview & Creative North Star: "The Digital Curator"
This design system is a sophisticated collision of high-fashion editorial and "Tech-Noir" precision. It rejects the generic, rounded-corner "app" aesthetic in favor of the **"Digital Curator"** North Star: a visual language where every pixel is intentional, every image is a centerpiece, and the interface serves as a rigid, technical frame for fluid, artistic content.

The system breaks the "template" look by utilizing extreme typographic contrast—pairing the romantic, high-contrast serif with the cold, clinical precision of monospace. It embraces **Intentional Asymmetry**, where large-scale editorial imagery is anchored by technical data points, creating a layout that feels both airy and structurally sound.

---

## 2. Colors & Tonal Depth
The palette is built on high-contrast foundations, utilizing **Udaipur Blue** (`primary`) as a surgical strike of color against a monochromatic world of **Stark White** (`surface`) and **Deep Charcoal** (`on-surface`).

### The Palette (Material 3 Mapping)
*   **Primary (Udaipur Blue):** `#006184` – The digital pulse. Use for key actions and technical accents.
*   **Surface (Stark White):** `#fcf9f8` – The gallery wall. 
*   **On-Surface (Deep Charcoal):** `#1c1b1b` – The ink.
*   **Secondary (Technical Grey):** `#5f5e5e` – Used for metadata and monospaced annotations.

### The "No-Line" Rule vs. The Technical Grid
While standard UI relies on borders, this system uses a dual approach:
1.  **Editorial Flow:** Prohibit 1px solid borders for sectioning content. Boundaries must be defined by **background color shifts** (e.g., a `surface-container-low` section sitting on a `surface` background).
2.  **Technical Framing:** Traditional borders are replaced by "Technical Grids." Use the `outline-variant` (`#bfc8cf`) only when creating a "Wired-style" data block or technical inset.

### Surface Hierarchy & Nesting
Treat the UI as stacked sheets of vellum. 
*   **Base:** `surface` (#fcf9f8).
*   **Level 1 (The Inset):** `surface-container-low` (#f6f3f2).
*   **Level 2 (The Card):** `surface-container-lowest` (#ffffff) to create a sharp, "popped" white effect against the off-white base.

### The "Glass & Technical Noir" Rule
For floating elements (modals, dropdowns), use **Glassmorphism**. Apply a semi-transparent `surface` color with a `24px` backdrop blur. This softens the tech-noir edge, ensuring the UI feels premium rather than aggressive.

---

## 3. Typography
The typography is the backbone of the "Vogue meets Wired" aesthetic.

*   **Display & Headline (Newsreader/Playfair Display):** These are the "Vogue" elements. Use `display-lg` (3.5rem) for hero titles. They should feel massive, authoritative, and elegant.
*   **Labels & UI Details (Space Grotesk/Monospace):** These are the "Wired" elements. All buttons, timestamps, and data points must use `label-md` or `label-sm`. This creates a "blueprint" feel.
*   **Body Content (Inter):** Clean, high-legibility sans-serif. Use `body-lg` (1rem) with generous line-height (1.6) to maintain the "Airy" requirement.

---

## 4. Elevation & Depth
In this system, **Roundedness is strictly 0px.** Sharp corners communicate precision and architectural intent.

*   **The Layering Principle:** Depth is achieved through tonal stacking. A `surface-container-highest` navigation bar sits atop a `surface` header without a shadow, using only the color shift to define its edge.
*   **Ambient Shadows:** If a floating effect is required (e.g., a floating image), use an ultra-diffused shadow: `box-shadow: 0 20px 50px rgba(28, 27, 27, 0.05)`.
*   **The Ghost Border:** For input fields and technical containers, use the "Ghost Border"—the `outline-variant` token at 20% opacity. It should be felt, not seen.

---

## 5. Components

### Buttons (Technical Accents)
*   **Primary:** Sharp 0px corners. `primary` background, `on-primary` text. Typography: `label-md` (Monospace). All caps.
*   **Secondary:** Ghost Border (`outline-variant` at 20%). No background.
*   **Hover State:** A subtle shift to `primary-container`. No "glow" effects.

### Cards & Editorial Modules
*   **Rule:** Forbid divider lines.
*   **Structure:** Use vertical white space (64px+) and subtle background shifts (`surface-container-low`) to separate stories. Images should be full-bleed within their containers to emphasize the "Editorial" scale.

### Input Fields (Tech-Noir)
*   **Style:** A single bottom border (1px) using `outline`. Label in `label-sm` (Monospace) positioned above the field. 
*   **Focus:** The bottom border transforms into `primary` (Udaipur Blue).

### The "Data-Ticker" (Custom Component)
A signature component for this system: A scrolling or static horizontal bar using `surface-container-high` featuring real-time metadata (date, article word count, technical coordinates) in `label-sm` monospace.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use extreme scale. A 3.5rem headline next to a 0.6875rem monospace label creates the desired "Curator" tension.
*   **Do** allow imagery to break the grid. Let a high-fashion photo overlap a technical container.
*   **Do** use Udaipur Blue sparingly—it is a laser, not a paint bucket.

### Don’t:
*   **Don’t** use border-radius. Ever. 0px is the law.
*   **Don’t** use standard "drop shadows." They muddy the crisp, tech-noir aesthetic.
*   **Don’t** use centered text for body copy. Keep it left-aligned (flush left, ragged right) for a classic magazine feel.
*   **Don't** use 1px dividers to separate content. Use the Spacing Scale (64px, 80px, 120px) to let the layout breathe.