# Updating the live book on Hostinger

These steps publish the corrected book to the existing `career-english-book` directory, using the GitHub Actions workflow already in the repository (`.github/workflows/deploy.yml`, FTPS). They do not touch the main Hidayet English Academy site or its Hostinger Git deployment.

Nothing is deployed until you do step 4 or step 5.

## What gets uploaded

| File | Notes |
|---|---|
| `index.html` | The reader app (updated). |
| `book-data.json` | The corrected book text. |
| `reference-index.json` | **New file.** Needed for the reference index and code links (the site still works without it, but those features are hidden). |
| `front-cover.jpg`, `back-cover.jpg` | Unchanged. |

Not uploaded (excluded in the workflow): `editorial/` (scripts, logs, print edition, PDF), `.github/`, `README.md` and git files.

## 1. Back up the live directory

1. In hPanel, open **Files → File Manager** and go to the `career-english-book` directory.
2. Select all files and choose **Compress** (zip).
3. Download the zip to your computer.
4. Do not rename, move or delete anything.

## 2. Merge the branch

1. Push the branch: `git push -u origin editorial-audit-2026-10`.
2. Open a pull request into `main` and review it. Use `editorial/QA-REPORT.md` and the correction log.
3. Merge.

A merge to `main` does **not** deploy while the repository variable `DEPLOY_ENABLED` is unset.

## 3. Check the secrets

In GitHub, open **Settings → Secrets and variables → Actions** and confirm that `FTP_SERVER`, `FTP_USERNAME` and `FTP_PASSWORD` exist. The FTP account should be limited to the `career-english-book` directory: the workflow uploads to the FTP account's root (`server-dir: ./`).

## 4. Dry run (uploads nothing)

1. Open **Actions → Deploy to Hostinger → Run workflow**, choose the `main` branch, and leave **Dry run** ticked.
2. Open the run log. Confirm that it connects over FTPS and that the files listed are only those in the table above.

## 5. Real deployment

Choose one of these:

- **One-off:** run the workflow again with **Dry run** unticked.
- **Automatic from now on:** create the repository variable `DEPLOY_ENABLED` with the value `true` (**Settings → Secrets and variables → Actions → Variables**). From then on, every push to `main` deploys.

The first real run uploads every file and creates a sync-state file (`.ftp-deploy-sync-state.json`) on the server. Later runs upload only changed files. Old files on the server are not deleted (`dangerous-clean-slate: false`).

## 6. Check the live site

1. Hard-refresh the page (Ctrl+F5). If Hostinger caching is on, purge it first: **hPanel → Website → Cache Manager**.
2. Check these items:
   - The cover page shows **"Before you start"**, not "Review build", and no "Draft" pills appear on lessons.
   - Lesson pages say "Level 1 · Module 1 · Lesson 1.1".
   - **How to use this book** and **Reference index** open, and searching `V-0014` finds "team".
   - A Bengali/Hindi vocabulary table (Level 1, Lesson 1.3) shows Bengali and Hindi script, not boxes.
   - The browser console (F12) shows no errors.

## Rolling back

Either:

- upload the backup zip from step 1 through File Manager and extract it over the directory, or
- revert the merge commit on `main` and run the workflow again (not a dry run).

## Rebuilding the PDF (optional, local only)

Needs Python 3, Node.js and Google Chrome (no Python packages are required).

```
cd editorial/print
npm install puppeteer-core@23 pdf-lib@1.17.1 pdfjs-dist@4.10.38
cd ../..
python editorial/tools/apply_corrections.py
python editorial/tools/build_reference_index.py
python editorial/tools/build_print.py
node editorial/print/render_pdf.js
python editorial/tools/build_print.py
node editorial/print/render_pdf.js
```

Run the last two commands twice so the contents and index carry real page numbers. The PDF is written to `editorial/print/Career-English-Master.pdf`. It is not uploaded to the website; share it separately, or add a download link later if you decide to publish it.
