# Career English: editorial audit and QA report

Branch: `editorial-audit-2026-10` · Date: 1 October 2026 · Nothing has been deployed or pushed.

## Summary

- All 186 lessons, 5 level assessments and 5 capstones (196 units) were read and corrected. No lesson was removed or merged.
- **846 corrections** are logged in [`correction-log.csv`](correction-log.csv) and [`CORRECTION-LOG.md`](CORRECTION-LOG.md). Each entry records level, module, lesson, original, replacement and reason.
- Every correction is a script in [`corrections/`](corrections/), applied to the original text (commit `61c769f`) by `tools/apply_corrections.py`. Running `python editorial/tools/apply_corrections.py --check` confirms that `book-data.json` matches the original plus the logged corrections, so nothing changed without a log entry.
- The website was updated and checked in headless Chrome at desktop and phone widths: 0 console errors, 0 layout overflow, 0 duplicate IDs, 0 broken internal links (3,699 checked).
- A master PDF was generated from the corrected text: A4, 1,104 pages, contents and index with real page numbers, bookmarks for every level, module, lesson and assessment, and running heads.

**Status: not yet publication-ready.** The editorial audit and website checks are complete. The PDF has only been spot-checked; it still needs a full human proofread, and the open items below need a decision.

## Corrections by type

| Type | Count |
|---|---|
| Production language / unfinished material (template answers, internal notes, theme tags, curriculum-map references, activity codes) | 226 |
| Story continuity (names, roles, timelines, numbers) | 140 |
| Assessment instructions and scoring | 134 |
| Reference codes and links | 67 |
| Exercise and answer-key alignment | 65 |
| Natural professional English | 42 |
| Grammar and usage explanations | 38 |
| Factual and content accuracy | 31 |
| Headings and structure | 29 |
| Typography and consistency | 29 |
| Honest audio labelling | 18 |
| Pronunciation and word stress | 15 |
| Bengali/Hindi support | 12 |

By level: Level 1: 212 · Level 2: 107 · Level 3: 159 · Level 4: 145 · Level 5: 189 · book-wide rules: 34 (each rule may change many lessons).

## QA findings from the reference PDF

| Finding | Where | Resolution |
|---|---|---|
| "punctual" stress | Level 1, Lesson 1.1 | Now PUNCtual (first syllable). |
| "background" stress | Level 1, Lesson 1.2 | Now BACKground. |
| "become professional": adjective vs noun | Level 1, Lesson 1.1 (MIS-0002) | Explanation rewritten: *more professional* (adjective) vs *a professional* (noun). |
| "respectful" answer key | Level 1, Lesson 1.1, Exercise 2 | Key now accepts *respectful* and explains why (an adjective after *being*). |
| Present perfect | Level 3, Lesson 7.1 | Rule and examples corrected; finished-time expressions use the past simple. |
| Passive voice changing the facts | Level 3, Lesson 7.3 (and Level 2, Lesson 2.4) | Model answers now keep the original facts and agent. |
| Backshift presented as compulsory | Level 3, Lesson 7.3 | Now optional when the reported fact is still true. |
| Prepositions by meaning (arrive at/in; agree with/on/to) | Level 3, Lesson 7.4 | Rewritten by meaning, with correct examples. |
| which/that; defining vs non-defining clauses | Level 3, Lesson 7.5 | Explanation, commas and examples corrected. |
| Visible stress marking; unanswerable matching exercise | Level 3, Lesson 8.1 | Stress shown in capitals/bold; the matching exercise now has a full set of options and a key. |
| Assessments: criteria not applicable, scoring unexplained | All 5 Level Assessments, all 5 capstones, every module assessment | Each part has criteria that fit it (written vs spoken), a 0–3 or 0–4 scale and a pass mark (70%). Capstones keep the weighted rubric with a 0–4 scale and a 70/100 completion mark. |
| Duplicated headings (PDF pp. 469, 495) | Print layout | The new PDF prints each module heading once, on its own module title page. |
| Unfinished model answers, theme tags, curriculum-map references, internal notes | Throughout | Removed or replaced with sample answers. A scan of the corrected book (`tools/scan.py`) finds none left. |
| Final capstone: pilot-launch timeline, participants, staffing | Level 5 capstone, "The Handover" | Timeline fixed (first week of the handover, no pilot "results" before launch). The staffing decision is now made once, in the Step 5 meeting, and correctly described. Roster ownership stays with Hasan; Farhan briefs staff and gets the decision with its reasoning. |

## Other significant fixes

- **Continuity.**
  - Arif's hotel is Riverside Hotel; other "Riverside" businesses were renamed.
  - The Level 4 vendor "Mr. Hossain" no longer shares a name with Arif's Level 1 supervisor.
  - The Meridian Partners relationship is no longer called "three years old" after one year.
  - Farhan's role (front office), Rima's history and Priyanka's length of service are now consistent.
  - The Level 4 lobby kiosk is acknowledged when Level 5 extends self-check-in.
  - In Lesson 4.7.4, the developer Alex was described as consistently direct, which contradicted the evidence in Lesson 4.7.1; the description now matches what Alex did there.
- **Exercises.**
  - "Compare these two…" and "which of these…" items that had no options now print the options.
  - Template answer keys ("[reason]", "[open response]") are replaced with sample answers.
- **Logic.**
  - Level 5 Assessment Part A told learners to give a newcomer *less* detail than an experienced colleague; it now says more.
  - Several "cost" and "rate" figures were made consistent across dialogue, worked example and answer key.
- **Audio.** No recordings exist, so prompts now say "read the dialogue (or have a partner read it aloud)". The 13 "Listening Comprehension" exercises are now labelled "Comprehension".
- **Module descriptions.** All 40 were course-design notes ("sequence logic", "project brief", "working title") and are rewritten as short summaries for learners.
- **Consistency.**
  - American spelling throughout.
  - Inline Bengali and Hindi words are now tagged with the correct language, so they get the right font and `lang` attribute.
  - The Bengali danda (।) is no longer tagged as Hindi.

## Website (`index.html`)

- Internal status pills (DRAFT, UNKNOWN, "pending review") and the "review build" notice are removed. "Mark reviewed" is now "Mark as completed".
- Pages show "Level 2 · Module 3 · Lesson 3.4" instead of internal IDs, and the sidebar shows lesson numbers.
- New **How to Use This Book** page covering:
  - the book's structure;
  - the lesson sections;
  - the audio note;
  - stress and intonation marks;
  - the reference codes;
  - scoring;
  - Bengali/Hindi support.
- New **Reference index** (`#codes`) listing all 933 reference codes (V, P, PAT, GIC, CF, TL, MIS, TIP), each with a label and a link to the lesson that introduces it. Codes in lessons link there, and the search box finds codes too (e.g. `V-0014`). The data is in `reference-index.json`, built by `tools/build_reference_index.py`.
- Accessibility:
  - skip link, landmarks, labelled search, `aria-expanded` on the contents tree and menu, a progress bar with values, and visible focus outlines;
  - light-theme text colours raised to WCAG AA (4.5:1 or better), with dark theme unchanged;
  - Bengali and Hindi fonts applied everywhere, not just in vocabulary tables.
- Loading: failed data loads now show an error message instead of a broken page. A favicon is included.
- Progress, search and the theme switch are unchanged. Progress is still stored in the reader's browser.

## Print edition and PDF

- Built by `tools/build_print.py` (HTML) and `print/render_pdf.js` (headless Chrome + pdf-lib). It takes two passes so the page numbers in the contents and index are real; the page map was stable across three passes.
- Contents of the PDF, in order:
  1. Cover.
  2. Edition page.
  3. Contents (levels, modules, lessons, assessments, capstones, index).
  4. How to Use.
  5. Each level: a level title page, a title page per module with its description and lesson list, then each lesson on a new page with its exercises and answer key.
  6. Reference index, with page numbers.
  7. Back cover.
- Fonts are embedded: Noto Sans Bengali and Noto Sans Devanagari for the Bengali and Hindi text.
- Page breaks avoid splitting dialogue turns, table rows, exercises and answer items.
- The output `editorial/print/Career-English-Master.pdf` is not committed (12.8 MB; it is in `.gitignore`). Rebuild it with the commands in `HOSTINGER-UPDATE.md`.
- Proofed pages, rendered and checked visually:
  - cover, contents, Lesson 1.1, the Lesson 1.3 vocabulary table (Bengali/Hindi), Lesson 3.8.1 (stress), the Level 5 capstone, the index and the back cover;
  - 3,699 web links checked automatically.

## Open items (need a decision or human review)

1. **Full proofread of the PDF.** About 1,100 pages were generated, but only sample pages were checked visually.
2. **Bengali and Hindi glosses.** Script and tagging are verified, and the glosses I sampled are accurate. A native-speaker review of all entries is still recommended.
3. **Cover artwork.** The back cover says "www.HedayatEnglishAcademy.com" and "info@HedayatEnglishAcademy.com", but the front cover says "hidayetenglishacademy.com". These are images, so they need the designer.
4. **Audio.** The book is now honest that there are no recordings. If audio is produced later, the "read the dialogue" prompts and the How to Use note should be updated.
5. **Internal status fields.** `content_track_status` / `curriculum_status` in `book-data.json` still hold the production values (DRAFT, UNKNOWN). They are no longer shown anywhere; I changed the display, not the data.
6. **Deployment.** Not done. See `HOSTINGER-UPDATE.md`.

## How to review the changes

- **Corrections:** `editorial/CORRECTION-LOG.md` (readable) or `editorial/correction-log.csv` (filter in a spreadsheet).
- **Diff against `main`:** `git diff main...editorial-audit-2026-10 -- index.html editorial/ .github/`. The `book-data.json` diff is large; the correction log is the readable version of it.
- **Site check:** open `index.html` through a local web server, e.g. `python -m http.server`, then visit http://localhost:8000.
