# Messages link preview design

## Intent and goals

Make links to `https://impex.facilitiops.io/` display a clear FacilitiOps preview in Apple Messages and other link unfurlers. Use the supplied brand reference in a landscape share image and describe the site as facility management software.

## Non-goals and constraints

- Keep the page content and current page title as they are.
- Keep the static GitHub Pages deployment and avoid adding dependencies.
- The homepage and original HTML route share the same page source.
- A deployed preview can still be cached by Messages; source changes alone cannot prove the final card shown by Messages.

## Approaches

- Use the logo strip as-is: simple, but too short and wide for a readable preview.
- Add descriptive metadata only: depends on crawler extraction and provides no controlled image.
- Add Open Graph and Twitter metadata plus a landscape card (selected): provides a predictable title, description, URL, and branded image.

## Implementation

Add canonical, Open Graph, and Twitter card metadata to `ProductLedSlite.dc.html`. Store a 1200×630 share image at the site root and copy it into the GitHub Pages artifact in `.github/workflows/pages.yml`. Use the absolute image URL `https://impex.facilitiops.io/og-image.png`.

## Acceptance and proof

Review the final metadata values and workflow asset copy step, inspect the image dimensions and content, and check the exact diff for whitespace issues. Runtime acceptance requires the deployed page and image to be fetchable and Apple Messages to refresh its cached preview.
