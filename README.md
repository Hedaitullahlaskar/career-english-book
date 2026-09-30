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

Deployed to Hostinger via Git-based deployment. Pushing to `main` updates the
live site automatically — see the repository's deployment notes / the project
owner for the current Hostinger Git deployment configuration.

Deployment target on the server: `public_html/career-english-book/` (repository
root maps directly to that folder — no nested subfolder).
