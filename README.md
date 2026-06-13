# Presentation

A clean, self-contained slide deck built with plain HTML, CSS, and JavaScript — no build tools or external dependencies required.

## Getting started

```bash
# Just open index.html in any modern browser
open index.html          # macOS
xdg-open index.html      # Linux
start index.html         # Windows
```

Or serve it locally:

```bash
npx serve .
# then visit http://localhost:3000
```

## Navigation

| Action | Input |
|--------|-------|
| Next slide | `→` / `↓` arrow key or **→** button |
| Previous slide | `←` / `↑` arrow key or **←** button |

## Customisation

- **Slides** — edit or copy the `<section class="slide …">` blocks in `index.html`.
- **Colours** — change the CSS variables in the `:root` block at the top of the `<style>` tag.
- **Font** — replace the `font-family` on `body` with any web-safe or Google Font.
- **Export to PDF** — open in Chrome, press `Ctrl+P`, and choose *Save as PDF*.

## Slide layouts included

| Layout class | Purpose |
|---|---|
| `slide-title` | Full-screen title with gradient heading |
| `slide-content` | Heading + body text |
| `slide-content` + `.card-grid` | Heading + feature cards |
| `slide-content` + `.bullet-list` | Heading + bullet points |
| `slide-content` + `.code-wrap` | Heading + syntax-highlighted code block |
| `slide-thanks` | Closing thank-you slide |
