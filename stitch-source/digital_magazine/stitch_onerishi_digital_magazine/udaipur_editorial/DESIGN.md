# Design System Strategy: The Technical Curator

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Technical Curator."** 

This system rejects the "standard dashboard" aesthetic in favor of a high-fashion editorial experience merged with the cold precision of laboratory documentation. We are balancing the romanticism of *Vogue* (large-scale serif, dramatic white space) with the data-driven rigor of *Wired* (monospaced accents, brutalist corners, technical blue). 

The goal is to move beyond templates. We achieve this through **intentional asymmetry**, where heavy headlines are offset by small, technical captions, and **brutalist structure**, where the 0px border radius creates a feeling of architectural permanence and authority.

---

## 2. Colors & Surface Logic
The palette is built on high-contrast neutrals with a single, high-energy technical "pulse"—Udaipur Blue.

### The "No-Line" Rule
Traditional 1px borders are strictly prohibited for sectioning. They clutter the visual field and feel "templated." Boundaries must be defined through:
- **Tonal Shifts:** Transitioning from `surface` (#f9f9f9) to `surface-container-low` (#f3f3f3).
- **Negative Space:** Using a rigorous 8px-based spacing scale to let "nothing" define the "something."

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. We do not use shadows to create depth; we use **Tonal Layering**.
- **Base Layer:** `surface` (#f9f9f9) for the overall canvas.
- **Content Blocks:** `surface-container-lowest` (#ffffff) to make articles "pop" against the background.
- **Technical Insets:** `surface-container-high` (#e8e8e8) for code snippets, data tables, or sidebars.

### Signature Textures
To add "soul" to the technical precision, use a subtle gradient for primary action states:
- **The Udaipur Pulse:** A linear gradient (135°) from `primary` (#006184) to `primary-container` (#007ba7). This gives depth to buttons and interactive data points without breaking the minimalist aesthetic.

---

## 3. Typography: The Editorial Dialectic
The system uses a "Dialectic" approach—two opposing forces creating a new whole.

- **The Philosophy (Newsreader):** Use for `display` and `headline` scales. It represents the human, the editorial, and the philosophical. Letter-spacing should be slightly tightened (-2%) for large displays to create a "tight" fashion-spread feel.
- **The Data (Space Grotesk):** Use for `title`, `body`, and `label` scales. This is the "Wired" influence. It is precise, legible, and technical. 
- **The Logic (Monospace):** For metadata, timestamps, and coordinates, use a monospace font (fallback: System Mono) in `label-sm` to emphasize the "precision" aspect of the brand.

---

## 4. Elevation & Depth
We reject the Material Design "Shadow" default. Our elevation is "Architectural."

- **The Layering Principle:** Use `surface-container` tiers to stack information. A technical sidebar should be `surface-container-highest`, while the main reading pane is `surface-container-lowest`. 
- **Ambient Shadows (The Float):** Only use shadows for floating elements (e.g., Modals). Use a hyper-diffused shadow: `box-shadow: 0 20px 80px rgba(26, 28, 28, 0.08);`. This mimics natural light through a gallery window rather than a digital glow.
- **The "Ghost Border" Fallback:** If a separation is required for accessibility in forms, use `outline-variant` at 15% opacity. Never use a 100% opaque border.
- **Glassmorphism:** For navigation bars, use `surface` at 80% opacity with a `backdrop-filter: blur(20px)`. This allows the high-fashion imagery to bleed through the UI, integrating the content with the system.

---

## 5. Components

### Buttons: The "Solid State"
- **Primary:** Rectangle (0px radius), background `primary`, text `on-primary` (Space Grotesk, All Caps). 
- **Secondary:** Rectangle (0px radius), background `transparent`, 1px "Ghost Border" (`outline-variant` at 20%), text `primary`.
- **Interaction:** On hover, the primary button should shift to the Udaipur Pulse gradient.

### Input Fields: The "Data Entry"
- **Styling:** Underline-only (2px `outline-variant`) or subtle `surface-container-low` fills. 
- **Labeling:** Use `label-sm` (Space Grotesk) always in All Caps to mimic technical blueprints.

### Cards: The "Editorial Plate"
- **Constraint:** No borders. No shadows. 
- **Structure:** Use `surface-container-lowest` as the card base. The headline (Newsreader) should be dramatically larger than the body text to create an editorial "anchor."

### Data Visualization (Specific to OneRishi)
- **Technical Accents:** Use Udaipur Blue (#007BA7) for all data lines and active states. Use `tertiary` (#834d00) sparingly as a warning or "alert" accent to provide a warm counter-point to the cool blues.

---

## 6. Do's and Don'ts

### Do:
- **Do** embrace extreme white space. If a section feels "full," it is likely over-designed.
- **Do** use 0px border radius for everything. The system's character comes from its sharp, uncompromising corners.
- **Do** use Newsreader for emotional hooks and Space Grotesk for factual information.

### Don't:
- **Don't** use dividers or lines to separate list items. Use 16px or 24px of vertical white space instead.
- **Don't** use standard "Blue" links. Use Udaipur Blue with a custom underline (offset 4px) for a bespoke feel.
- **Don't** use "Grey." Use the `secondary` and `surface` tokens which are slightly "warm" or "cool" to ensure the interface doesn't feel like a generic wireframe.
- **Don't** use animations that "bounce." All transitions should be linear or ease-out, mimicking the mechanical shutter of a camera or the slide of a high-end drawer.