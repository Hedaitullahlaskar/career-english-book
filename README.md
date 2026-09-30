# Career English — Interactive Book

Hidayet English Academy's interactive Career English book: a single-page HTML app
(dashboard + book reader) covering 5 levels, 40 modules, 186 lessons, plus level
assessments and capstones.

## Live site

https://hidayetenglishacademy.com/career-english-book/

## Structure

This is a static site — no build step, no server, no framework.

```
career-english-book/
├── index.html        # the entire app: markup, CSS, and JS in one file
├── book-data.json     # all lesson content (fetched client-side by index.html)
├── front-cover.jpg     # book cover image (shown on the intro screen + TOC)
└── back-cover.jpg       # back cover image (author bio page)
```

All asset references inside `index.html` are **relative** (`book-data.json`,
`front-cover.jpg`, `back-cover.jpg` — no leading slash), so this repository can be
served from any subdirectory without changing a single path. The only absolute
URLs in the page are the Google Fonts stylesheet links.

## Local preview

From this directory:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000/index.html.

## Deployment

Deployed to Hostinger by GitHub Actions (`.github/workflows/deploy.yml`), which
uploads the repository root over FTPS using a dedicated FTP account restricted to
`public_html/career-english-book/`. This is separate from the main website's
Hostinger Git deployment.

- Credentials come only from the GitHub secrets `FTP_SERVER`, `FTP_USERNAME`,
  `FTP_PASSWORD`.
- Pushes to `main` deploy only when the repository variable `DEPLOY_ENABLED` is
  `true`. The workflow can also be run manually (Actions → Deploy to Hostinger →
  Run workflow); manual runs default to a dry run.
- `README.md`, `.gitignore`, `.git/` and `.github/` are not uploaded. Files are
  never deleted from the server.

Deployment target on the server: `public_html/career-english-book/` (repository
root maps directly to that folder — no nested subfolder).
