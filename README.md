# B2 · Chosen · Slite ideas and a Works with FMX section — design reference

This is a static HTML reference mockup, originally exported from a visual
design tool. It remains a design reference, not a production application.
The content, inline style values, examples, and page layout are preserved.

## Contents

- `ProductLedSlite.dc.html` — the landing page and original source route.
- `ExampleEmail.dc.html` — the daily exception email sample, also embedded
  on the landing page.
- `PortfolioSummary.dc.html` — the portfolio summary sample, also embedded
  on the landing page.
- `site.css` — shared page defaults and embedded-example frame styling.
- `.github/workflows/pages.yml` — publishes the static files to GitHub Pages
  and makes the landing page available at `/` as well as its original route.
- `CNAME` — configures the published site for `impex.facilitiops.io`.

## Viewing

Serve the folder (e.g. `python3 -m http.server`) and open
`ProductLedSlite.dc.html` or `index.html`. The examples also work as direct
pages. Run `python3 tests/check_static_site.py` for source-level checks.

## GitHub Pages setup

After pushing the source, select **GitHub Actions** as the Pages build source
in the repository's Pages settings and set `impex.facilitiops.io` as the
custom domain. At the DNS provider, create a `CNAME` record for `impex`
pointing to `lichner.github.io`. The repository `CNAME` file documents the
site domain; custom Actions deployments use the repository Pages setting as
the domain configuration. Enable HTTPS in Pages settings once GitHub has
issued the certificate.
