# Career English: editorial audit and QA report

Branch: `editorial-audit-2026-10` · Date: 1 October 2026 · Nothing has been deployed or pushed.

## Summary

- All 186 lessons, 5 level assessments and 5 capstones (196 units) were read and corrected. No lesson was removed or merged.
- **968 corrections** are logged in [`correction-log.csv`](correction-log.csv) and [`CORRECTION-LOG.md`](CORRECTION-LOG.md): 846 from the editorial audit, 95 from the PDF proof pass and 27 author decisions (3 October 2026). Each entry records level, module, lesson, original, replacement, reason and source; rows 1–941 are frozen.
- Every correction is a script in [`corrections/`](corrections/), applied to the original text (commit `61c769f`) by `tools/apply_corrections.py`. Running `python editorial/tools/apply_corrections.py --check` confirms that `book-data.json` matches the original plus the logged corrections, so nothing changed without a log entry.
- The website was updated and checked in headless Chrome at desktop and phone widths: 0 console errors, 0 layout overflow, 0 duplicate IDs, 0 broken internal links (3,699 checked).
- A master PDF was generated from the corrected text: A4, 1,104 pages, contents and index with real page numbers, bookmarks for every level, module, lesson and assessment, and running heads.

**Status: NOT READY FOR PUBLICATION.** The editorial audit, the website checks and an editorial read of the complete rendered PDF (all 1,104 pages, in five batches) are done, and the registers for the human stage are ready (see "Final human QA and author decision gate"). Still needed:
- a human proofread of the PDF;
- a native-speaker review of the Bengali/Hindi text;
- a corrected back-cover image (the author has supplied the text; the designer must supply 300 ppi artwork);
- a final regeneration and final PDF QA.

The author decisions and house-style choices were made and applied on 3 October 2026. No unit is marked approved.

## Corrections by type (editorial audit, 846)

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
## PDF proof pass

The whole rendered PDF was reviewed in five batches: front matter and Level 1 (pp. 1–175), Level 2 (176–347), Level 3 (348–614), Level 4 (615–860), and Level 5, the index and the back cover (861–1104). The PDF was rebuilt after each batch.

- **Three kinds of check, kept separate:**
  - *Automated* (`proof/auto_checks.py` on the PDF text): layout flags (near-empty pages, headings stranded at the foot of a page, text outside the margins) and text flags (repeated words, stray spaces, a/an, unbalanced quotes or brackets, leftover markers, British spelling). Every flag was reviewed; the 18 still raised are confirmed false positives (numbered "1) 2)" answers, multi-paragraph quotations, "checked in in", the deliberate "really really").
  - *Editorial review* (Claude): every page's text read in full for grammar, instructional accuracy, examples, answer keys, scoring, continuity and typography, with flagged and changed pages rendered and checked visually.
  - *Human and native-speaker review*: not done yet, and recorded as pending for every unit.
- **95 corrections** (each in the correction log with source "PDF proof, batch N"):
  - story continuity: 26;
  - natural professional English: 21;
  - typography and consistency: 20;
  - exercise and answer-key alignment: 8;
  - production language: 6;
  - assessment scoring: 6;
  - factual accuracy: 3;
  - reference codes: 3;
  - grammar: 2.
- **Layout fixes in the build** (`tools/build_print.py`): contents headings no longer stranded at the foot of a page; reference codes in table cells no longer split across lines; a duplicated sentence in How to Use removed.
- **Index fixes** (`tools/build_reference_index.py`, which also feeds the website): tips and patterns that were labelled with their own code now show their names, V-0754 shows the right term, quoted patterns lose their stray quotation marks, and long labels break at a word.
- **Outputs:**
  - [`proof/PROOF-CHECKLIST.md`](proof/PROOF-CHECKLIST.md): one row per unit, with PDF pages, automated flags, the editorial-review batch, the number of proof fixes, and human, native-speaker and approval status.
  - [`proof/PROOF-ISSUES.csv`](proof/PROOF-ISSUES.csv): all 123 issues, each with unit, PDF page, original, correction, reason and status.
- **Final build:** 1,104 pages, 243 of 243 bookmarks matched; `apply_corrections.py --check` passes.

## Final human QA and author decision gate

This stage prepares the book for people to check and approve. It changed no lesson text. Publication status: **NOT READY FOR PUBLICATION** (gate dashboard at the top of [`proof/PROOF-CHECKLIST.md`](proof/PROOF-CHECKLIST.md)).

| File | For | What it holds |
|---|---|---|
| [`proof/HUMAN-PROOFREAD-REGISTER.csv`](proof/HUMAN-PROOFREAD-REGISTER.csv) | Human proofreader | 198 rows: all 196 units, plus front matter (pp. 1–10) and back matter (pp. 1070–1104), with PDF start and end pages. Every row is PENDING, with no reviewer and Approved = NO. |
| [`proof/NATIVE-LANGUAGE-REVIEW.csv`](proof/NATIVE-LANGUAGE-REVIEW.csv) | Native Bengali and Hindi speakers | 243 items, each with a PDF page: 209 Bengali/Hindi items in the 31 units that contain those scripts, and 34 English statements about Bengali/Hindi usage or custom in 25 further units. All are PENDING / NO. |
| [`AUTHOR-DECISIONS.md`](AUTHOR-DECISIONS.md) | Author | Decisions A (linen contract term), B (seven duplicate vocabulary codes) and C (the Level 4 kiosk pilot in Level 5 Lessons 6.3–6.4), with the affected passages, pages and options. |
| [`proof/HOUSE-STYLE-REPORT.md`](proof/HOUSE-STYLE-REPORT.md) | Author | Every date (3 US-style, 4 UK-style, 43 day-only ordinals) and the 11 teaching uses of "to hand" (a house-style / British English decision, not an error). |
| [`proof/BACK-COVER-REPLACEMENT-BRIEF.md`](proof/BACK-COVER-REPLACEMENT-BRIEF.md) | Designer and author | Website and email lines, mission line, elements to keep, and the print-resolution check. Status: DESIGNER ACTION REQUIRED. |
| [`proof/SOURCE-PDF-CONSISTENCY.md`](proof/SOURCE-PDF-CONSISTENCY.md) | Production | Source vs PDF audit, with every discrepancy assessed (`consistency-triage.json`). |

- The registers are generated by `proof/build_review_registers.py`. Re-running it keeps every value a reviewer has entered.
- New corrections are labelled by phase in the correction log. Use correction files named `96-human-proofread*.py` (label "Human proofread"), `97-native-language-review*.py` ("Native-language review") or `98-author-decision*.py` ("Author decision"). `apply_corrections.py` refuses to run if rows 1–941 of the existing log would change (`correction-log-frozen.json`).

**Source/PDF consistency (1 October 2026 PDF):**
- The source matches the 968 logged corrections; the index and print files are current; the PDF (rebuilt 3 October 2026) is newer than every input.
- All 243 structural bookmarks and all 243 contents page numbers are correct.
- All 95 PDF-proof corrections are in the PDF.
- 709 exercises have 709 answers, with no numbering or multiple-choice letter mismatches.
- Pass marks, totals and the five capstone rubrics (100% each) add up.
- Defects found by the audit, now fixed (3 October 2026):
  - **6 Reference Index labels** (PAT-0057, PAT-0061, PAT-0068, PAT-0108, MIS-0090, MIS-0095) and 42 other labels taken from nearby text: the index generator now names each pattern or mistake from its own heading. The website index and PDF index agree on all 926 codes.
  - **52 lesson bookmarks** that lost a space where a title wrapped: `render_pdf.js` now writes the exact heading text. 4 in-lesson section bookmarks still join two words (low priority).
- Still open: **both cover images** are 1024 × 1536 px, about 131 ppi on A4, and narrower than A4.

## Open items (need a decision or human review)

1. **Human proofread of the PDF.** Every page has had an editorial read, but no person has proofread the printed layout. Use `proof/HUMAN-PROOFREAD-REGISTER.csv`; 0 of 196 units are approved.
2. **Bengali and Hindi.** Text extraction cannot verify these scripts; rendered pages show correct glyphs. A native speaker needs to review every item in `proof/NATIVE-LANGUAGE-REVIEW.csv`.
3. **Back-cover image.** The author has supplied the text: website `hidayetenglishacademy.com`, email `info@hidayetenglishacademy.com`, mission line "Bengali and Hindi learners", helpline 6290 05 6461 (confirmed). The designer must now supply the artwork at 300 ppi (see `proof/BACK-COVER-REPLACEMENT-BRIEF.md`). The front cover's resolution is still to be decided.
4. **Author decisions A, B and C.** Decided and applied on 3 October 2026 (A: two-year contract; B: approved; C: cite the Level 4 pilot); see `AUTHOR-DECISIONS.md`.
5. **House style.** Decided on 3 October 2026: British/UK dates (applied) and keep "to hand" (no change); see `proof/HOUSE-STYLE-REPORT.md`.
6. **Generator fixes.** Done on 3 October 2026 (index labels and 52 bookmark titles).
7. **Audio.** The book is now honest that there are no recordings. If audio is produced later, the "read the dialogue" prompts and the How to Use note should be updated.
8. **Internal status fields.** `content_track_status` / `curriculum_status` in `book-data.json` still hold the production values (DRAFT, UNKNOWN). They are no longer shown anywhere; I changed the display, not the data.
9. **Deployment.** Not done. See `HOSTINGER-UPDATE.md`.

## How to review the changes

- **Corrections:** `editorial/CORRECTION-LOG.md` (readable) or `editorial/correction-log.csv` (filter in a spreadsheet).
- **Diff against `main`:** `git diff main...editorial-audit-2026-10 -- index.html editorial/ .github/`. The `book-data.json` diff is large; the correction log is the readable version of it.
- **Site check:** open `index.html` through a local web server, e.g. `python -m http.server`, then visit http://localhost:8000.
