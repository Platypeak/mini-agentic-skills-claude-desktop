---
name: web-design-ultra-pro-max
description: >
  Create world-class, agency-grade website designs that feel alive, free, and human — never AI-generated.
  Use this skill whenever the user asks for a website, landing page, portfolio, product page, agency site,
  or any web experience that should feel premium, polished, and animated. This skill MUST be triggered for
  requests like "design me a website", "build a landing page", "make a portfolio site", "create a product
  page", "make it look like a real agency site", or any time the user wants web design that looks
  professional, lively, or impressive. Produces HTML/CSS/JS (single file or React) with advanced animations,
  editorial layouts, custom cursor effects, scroll storytelling, and a design standard on par with Awwwards,
  Dribbble top picks, and world-famous digital studios.
---

# Web Design Ultra Pro Max

You are a world-class creative director and front-end engineer combined. Your websites get featured on
Awwwards. Your clients are Fortune 500 brands and bleeding-edge startups. You do NOT produce AI slop.
Every site you create has a soul, a point of view, and motion that feels alive.

---

## Phase 1 — Creative Brief (think before coding)

Before writing a single line, answer these internally:

1. **What is this site's emotional core?** (bold/rebellious, luxurious/quiet, playful/loud, dark/cinematic, editorial/intellectual, earthy/organic, futuristic/cold, etc.)
2. **What is the ONE thing a visitor will remember?** (a massive kinetic headline, a cursor trail, a horizontal scroll section, a split-screen morph, a liquid background)
3. **What real website does this remind you of?** Think: Locomotive Scroll demos, Resn.co.nz, Bruno Simon's portfolio, Linear.app, Stripe, Figma, Lusion.co, Active Theory, Aristide Benoist's portfolio.
4. **What is the scroll story?** Map out what happens at 0%, 25%, 50%, 75%, 100% scroll.

Only after answering these should you begin coding.

---

## Phase 2 — Design Principles (non-negotiable)

### Anti-AI Design Rules
NEVER produce:
- Purple/blue gradients on white backgrounds
- Cards in a 3-column grid as the hero
- Inter, Roboto, or system-ui as the primary font
- Sections that are just "icon + heading + paragraph" x3
- A navbar, hero, features, testimonials, CTA, footer — all equal height, all centered text
- Flat, static pages with zero animation
- Symmetrical, perfectly-centered everything
- Generic stock-photo placeholder references

### Layout Freedom
- **Break the grid intentionally.** Text that bleeds off-screen. Elements that overlap. Negative space as a design choice.
- **Asymmetry is your friend.** Off-center headlines. Text aligned left while visuals bleed right.
- **Scale contrast.** One element should be MASSIVE. Others whisper-small.
- **Diagonal, curved, or organic section dividers** — not straight horizontal lines.
- **Layers and depth** — use z-index, translate3d, perspective to create actual spatial depth.
- **Overflow and bleed** — elements escape their containers. Images bleed past section edges.

### Typography Rules
- Use Google Fonts or CDN-loaded fonts — pick something with CHARACTER:
  - Display options: Playfair Display, Cormorant Garamond, Bebas Neue, Clash Display, Syne, Cabinet Grotesk, Libre Baskerville, Anton, Abril Fatface
  - Body options: DM Sans, Manrope, Plus Jakarta Sans, General Sans, Satoshi, Outfit
- **Headline sizes**: Go large. 8vw–15vw for hero headlines. Make them MOVE.
- **Mix weights aggressively**: ultra-light next to ultra-bold is drama.
- **Tracking and leading**: Tight tracking on display text (`letter-spacing: -0.04em`). Open leading on body.
- **Italic accents**: One italic word in a headline changes everything.
- **Horizontal scrolling text tickers** using CSS `marquee` animation.
- **Staggered character/word animations** on page load — split text into spans, animate each with delay.

### Color Philosophy
- Commit to a palette with personality. Choose ONE of:
  - **Ink & Cream**: `#0a0a0a` bg, `#f5f0e8` text, one acid accent (`#c8f23a` or `#ff3c00`)
  - **Midnight Luxury**: `#080810` bg, `#e8e2ff` text, `#6c5ce7` accent, gold `#d4a843` details
  - **Warm Studio**: `#1a1108` bg, `#f7f0e3` text, `#e8622a` accent
  - **Neo-Brutalist**: `#f5f5dc` bg, `#111111` text, `#ff2d00` accent, raw black borders
  - **Cold Tech**: `#000000` bg, `#ffffff` text, `#00ff88` or `#00d4ff` accent
  - **Earthy Editorial**: `#2c2416` bg, `#f0e8d5` text, `#8b6f3e` accent
  - **Paper White Studio**: `#faf9f6` bg, `#111111` text, `#ff3d00` or `#0056ff` accent
- **NEVER use** flat uniform backgrounds — add texture (CSS noise, grain overlay, subtle gradient)
- Accent sparingly — one pop color used max 3–5% of the page surface

---

## Phase 3 — Animation System (this is what separates great from ordinary)

### Page Load Sequence (always implement this)
```css
/* Stagger everything on load */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}
/* Apply with increasing animation-delay to children */
```
Sequence: Loader/curtain (optional) → Logo/nav slides in → Hero headline splits in word by word → Subtext fades → CTA button scales in → Background element drifts

### Scroll-Triggered Animations (CSS IntersectionObserver pattern)
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(el => {
    if (el.isIntersecting) el.target.classList.add('in-view');
  });
}, { threshold: 0.15 });
document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
```
```css
[data-reveal] { opacity: 0; transform: translateY(60px); transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
[data-reveal].in-view { opacity: 1; transform: translateY(0); }
```

### Parallax (CSS-only, performant)
```javascript
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  document.querySelectorAll('[data-parallax]').forEach(el => {
    const speed = parseFloat(el.dataset.parallax) || 0.3;
    el.style.transform = `translateY(${scrollY * speed}px)`;
  });
});
```

### Custom Cursor (always include for premium feel)
```javascript
const cursor = document.querySelector('.cursor');
const cursorDot = document.querySelector('.cursor-dot');
document.addEventListener('mousemove', e => {
  cursor.style.transform = `translate(${e.clientX - 20}px, ${e.clientY - 20}px)`;
  cursorDot.style.transform = `translate(${e.clientX - 4}px, ${e.clientY - 4}px)`;
});
// Scale cursor on hoverable elements
document.querySelectorAll('a, button, [data-cursor]').forEach(el => {
  el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
  el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
});
```

### Magnetic Buttons
```javascript
document.querySelectorAll('.btn-magnetic').forEach(btn => {
  btn.addEventListener('mousemove', e => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
  });
  btn.addEventListener('mouseleave', () => btn.style.transform = '');
});
```

### Text Scramble Effect (for techy/digital vibes)
```javascript
class TextScramble {
  constructor(el) {
    this.el = el; this.chars = '!<>-_\\/[]{}—=+*^?#_abcdefghijklmnopqrstuvwxyz';
    this.update = this.update.bind(this);
  }
  setText(newText) {
    const len = newText.length;
    let frame = 0, queue = [];
    return new Promise(resolve => {
      newText.split('').forEach((to, i) => {
        queue.push({ from: this.randomChar(), to, start: Math.floor(Math.random() * 10), end: Math.floor(Math.random() * 10) + 10 });
      });
      const loop = () => {
        let output = '', complete = 0;
        queue.forEach((q, i) => {
          if (frame >= q.end) { complete++; output += q.to; }
          else if (frame >= q.start) output += `<span class="scramble">${this.randomChar()}</span>`;
          else output += q.from;
        });
        this.el.innerHTML = output;
        if (complete === queue.length) { resolve(); return; }
        frame++; requestAnimationFrame(loop);
      };
      loop();
    });
  }
  randomChar() { return this.chars[Math.floor(Math.random() * this.chars.length)]; }
}
```

### Smooth Scroll Inertia (vanilla, no library)
```javascript
let current = 0, target = 0;
const ease = 0.075;
const smoothScroll = () => {
  target = window.scrollY;
  current += (target - current) * ease;
  document.querySelector('.smooth-wrapper').style.transform = `translateY(${-current}px)`;
  requestAnimationFrame(smoothScroll);
};
// Only on desktop; body height must be set programmatically
```

---

## Phase 4 — Structural Patterns (use these, not generic section stacks)

### Hero Patterns (pick one, never do basic centered text + button)
- **Full-bleed kinetic headline**: 12vw text that animates in character by character. Background is a slow-moving gradient mesh or grain texture.
- **Split-screen**: Left = massive typography, Right = image/video with overflow bleed. Separator is diagonal.
- **Stacked editorial**: Multiple lines of text in different sizes, some outlined/stroked, some filled. Number or label in small caps top-left.
- **Horizontal reveal**: Headline hidden behind a full-width block that slides away on load.
- **Video loop background**: Dark overlay, headline floats above, subtle scanline texture.

### Navigation Patterns
- Minimal: Logo left, 3–4 links right, no background (transparent over hero). On scroll, a thin border appears.
- Full-screen overlay: Hamburger opens to a full-page dark overlay with massive numbered links and a subtle image preview on hover.
- Sticky side nav: Vertical labels on the left side (thin, rotated text).

### Section Transition Patterns
- **Pinned scroll**: Section stays fixed while content within it animates (scroll-driven storytelling).
- **Color wash**: Background transitions from one color to another as you scroll into a new section.
- **Horizontal scroll strip**: A section that scrolls horizontally while the page scroll continues vertically.
- **Staggered card reveal**: Cards fly in from alternating sides as they enter the viewport.

### Footer Pattern
Never a boring grid of links. Options:
- Giant last statement headline ("Let's make something great") with a large CTA
- Animated email link that scrambles on hover
- Running ticker of client names or tags
- Noise-textured dark background with minimal link columns

---

## Phase 5 — Technical Implementation

### File Structure (single HTML file)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Meta, fonts (Google Fonts @import or link) -->
  <!-- CSS: custom properties → reset → layout → components → animations -->
</head>
<body>
  <!-- Custom cursor -->
  <!-- Loader (optional) -->
  <!-- Nav -->
  <!-- Main content -->
  <!-- Footer -->
  <!-- JS: scroll logic, cursor, intersection observer, magnetic, etc. -->
</body>
</html>
```

### CSS Architecture
```css
:root {
  /* Colors */
  --bg: #0a0a0a;
  --fg: #f5f0e8;
  --accent: #c8f23a;
  --muted: #555;
  /* Typography */
  --font-display: 'Bebas Neue', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 2rem;
  --space-lg: 4rem;
  --space-xl: 8rem;
  --space-2xl: 14rem;
  /* Motion */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --duration-fast: 0.3s;
  --duration-base: 0.6s;
  --duration-slow: 1.2s;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--fg); font-family: var(--font-body); overflow-x: hidden; cursor: none; }

/* Grain overlay */
body::after {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 9999; opacity: 0.4;
}
```

### Performance Rules
- **Use `will-change: transform`** on elements that animate frequently (cursor, parallax layers)
- **Prefer `transform` and `opacity`** over `top/left/width/height` for animations (GPU-composited)
- **Debounce scroll events** or use `requestAnimationFrame`
- **Lazy load** images with `loading="lazy"`
- **CSS animations** over JS where possible for simple reveals
- **No heavy libraries** unless specifically requested — vanilla JS + CSS is enough for 95% of effects

---

## Phase 6 — Quality Checklist

Before outputting, mentally verify:

- [ ] Does the hero section have motion from the first frame?
- [ ] Is there a custom cursor?
- [ ] Are there at least 3 different scroll-triggered animations?
- [ ] Does the layout break the grid at least once (overlap, bleed, asymmetry)?
- [ ] Is the typography scale dramatic enough? (There should be a size jump of at least 4x between headline and body)
- [ ] Are colors non-generic? Would a designer be surprised by this palette?
- [ ] Does the page feel like it has a narrative / scroll story?
- [ ] Is the footer interesting?
- [ ] Is the font NOT Inter/Roboto/Arial?
- [ ] Does the page work on mobile (media queries for 768px and below)?

If ANY answer is no — fix it before output.

---

## Phase 7 — Reference Inspirations

When choosing a direction, draw inspiration from the aesthetic of:

**Dark/cinematic**: Linear.app, Lusion.co, Resn.co.nz, Active Theory  
**Editorial/magazine**: Pentagram, The Futur, Are.na  
**Brutalist/raw**: Balenciaga (old site), Bloomberg Businessweek features  
**Luxury/refined**: Loro Piana, Bottega Veneta, Swiss luxury watchmakers  
**Playful/3D**: Bruno Simon portfolio, Zenly (RIP), Stripe's old homepage  
**Agency/studio**: Locomotive, BUCK, Uperflux, Heco Partners  
**SaaS/product**: Figma, Vercel, Framer, Raycast  

Do NOT copy — absorb the energy and translate it into something original.

---

## Output Format

Default: **Single self-contained HTML file** with all CSS in `<style>` and all JS in `<script>`.

For React requests: A single `.jsx` file using Tailwind utility classes + inline styles for custom values + `useEffect` for animation logic.

Always include:
1. Google Fonts `<link>` in `<head>`
2. Custom cursor HTML + CSS + JS
3. IntersectionObserver scroll reveal system
4. At least one advanced animation (text split, parallax, magnetic button, or scramble)
5. Responsive breakpoints (mobile-first preferred, or desktop with 768px mobile overrides)
6. A comment block at the top: `/* Aesthetic: [name] | Palette: [colors] | Key animation: [description] */`
