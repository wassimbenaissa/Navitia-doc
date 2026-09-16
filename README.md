# Navitia.io documentation

The Navitia API documentation, built with [Docusaurus](https://docusaurus.io/).
Published to <https://doc.navitia.io>.

This replaces the previous [Slate](https://github.com/slatedocs/slate) single-page
site. Content lives in `docs/` as plain Markdown — no Ruby, no Middleman, no
build step to preview a change.

## Working on the docs

```bash
npm install
npm start          # live preview on http://localhost:3000
npm run build      # production build; fails on any broken link or anchor
```

`npm run build` is the test suite. `onBrokenLinks` and `onBrokenAnchors` are both
set to `throw`, so a typo in a cross-reference fails CI rather than shipping.

## Where things are

| Path | What |
|---|---|
| `docs/` | The documentation, one folder per section |
| `static/img/` | Images |
| `static/legacy-redirects.json` | Old Slate hash → new route (generated) |
| `src/clientModules/legacyHashRedirect.ts` | Applies that map in the browser |
| `src/components/Anchor.tsx` | Inline (non-heading) link targets |
| `src/css/hove-tokens.css` | HOVE design-system tokens, vendored |
| `src/css/custom.css` | Maps those tokens onto Infima (the Docusaurus theme layer) |
| `src/prism/hovePrismTheme.ts` | Code-block syntax colours, from the same palette |
| `src/css/fonts/` | Uxum Grotesque, the brand display face |
| `tools/migrate.py` | The one-shot Slate → Docusaurus conversion |
| `tools/mdxcheck.mjs` | Compiles every page with MDX to surface all syntax errors at once |

## Theme

The site wears the **HOVE design system**: dark-teal chrome, warm-neutral
surfaces, brand cyan for selection and accents, and the system's three
families — Uxum Grotesque for display headings, Inter for UI and body, DM Mono
for section labels and code.

`src/css/hove-tokens.css` is a verbatim copy of the system's foundations
(`colors_and_type.css`), minus the parts Docusaurus owns; re-copy it to pick up
a new release of the design system. Everything site-specific — the Infima
mapping, the surfaces Infima does not expose as variables, and the notes on
where the docs deliberately diverge from the app — lives in `src/css/custom.css`.
Inter and DM Mono load from Google Fonts via `stylesheets` in the config.

## The migration

`tools/migrate.py` regenerates `docs/`, `static/img/` and
`static/legacy-redirects.json` from the untouched Slate sources in
`../Slate documentation/slate/source`. It is idempotent — re-running it
reproduces the current tree exactly.

Keep it until the cutover is signed off, then delete it along with `tools/` and
the Slate folder; after that, `docs/` is the source of truth and is edited by hand.

### What it does

1. Normalises three heading conventions (setext, ATX, raw `<hN id>`) into ATX
   with Docusaurus `{#anchor}` ids, preserving all 89 explicit anchors.
2. Makes the Markdown MDX-safe: closes 102 `<br>` tags, converts 44 `<url>`
   autolinks, escapes bare braces, rewrites block-level `<ul>/<li>` as Markdown
   lists, and turns 46 `<aside class="...">` into admonitions.
3. Splits 16 includes into 51 pages.
4. Rewrites all 317 in-page `#anchor` links into cross-page links, and emits the
   same mapping as `legacy-redirects.json`.

### Known content debt

Two links were already dead on the Slate site and are listed in `DEAD_ANCHORS`
in `tools/migrate.py`. They render as plain text until the content is fixed:

- `#additional-informations` — stop_schedules field table
- `#period-time` — disruption `time_slots` field

## Deployment

`.github/workflows/publish.yml` builds and publishes to GitHub Pages on every
push to the default branch. `static/CNAME` pins the `doc.navitia.io` domain.
