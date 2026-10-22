# Messages Link Preview Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Show a branded, readable rich preview when the site URL is shared.

**Architecture:** Add crawler metadata to the single page source used by both homepage and original route. Publish a landscape image as a static root asset through the existing Pages workflow.

**Tech Stack:** Static HTML, GitHub Pages Actions, PNG image asset.

**Spec:** `docs/superpowers/specs/2026-10-22-messages-link-preview-design.md`

## Global Constraints

- Preserve the existing page content and title.
- Do not add dependencies or change the static hosting model.
- Use `https://impex.facilitiops.io/og-image.png` as the absolute share image URL.
- Report deployment and Apple Messages cache acceptance separately from source validation.

## Review Focus

- Root and original page routes must expose the same metadata: they are both produced from `ProductLedSlite.dc.html`.
- The metadata image URL must match the deployed asset location and filename.
- GitHub Pages must copy the image into `_site` for both routes.
- The image must fit standard share-card proportions and retain readable brand text.
- Crawler metadata must be present in the static HTML head without relying on JavaScript.

---

### Task 1: Add and publish share preview metadata

**Files:**
- Modify: `ProductLedSlite.dc.html`
- Create: `og-image.png`
- Modify: `.github/workflows/pages.yml`

**Interfaces:**
- Produces metadata for canonical URL `https://impex.facilitiops.io/` and image `https://impex.facilitiops.io/og-image.png`.
- Produces `_site/og-image.png` in the existing GitHub Pages build.

- [x] Copy the generated brand card into the task worktree as `og-image.png`, crop/resize it to 1200×630, and inspect the result for legible, correctly spelled logo and copy.
- [x] Add a canonical link plus `og:title`, `og:description`, `og:type`, `og:url`, `og:image`, image dimensions, and matching Twitter summary-large-image tags in the document head.
- [x] Add `og-image.png` to the workflow's static asset copy command.
- [x] Review the changed head, workflow, image dimensions, and exact diff; run `git diff --check`.
- [x] Commit only the page, image, workflow, and approved design/plan documents with a Conventional Commit message.
