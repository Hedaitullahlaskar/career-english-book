# Back cover: replacement brief

**Status: DESIGNER ACTION REQUIRED**

## Text confirmed by the author (3 October 2026)

| Line | Final text |
|---|---|
| Website | `hidayetenglishacademy.com` |
| Email | `info@hidayetenglishacademy.com` |
| Helpline | `Helpline: 6290 05 6461` (confirmed current; unchanged) |
| Mission line | "To help Bengali and Hindi learners worldwide grow from where they are today, build confidence in English and move forward in their personal and professional lives." |
| Artwork | Supply at 300 ppi for the final designer rebuild (at least 2480 × 3508 px for A4) |

The designer replaces `back-cover.jpg` with artwork showing exactly this text; everything else stays as described in section 5.

| Item | Detail |
|---|---|
| File | `back-cover.jpg` (repository root), unchanged since the first commit (`b61e293`) |
| Used in | The last page of the print PDF (p. 1104). The website does not use it. |
| Current image | 1024 × 1536 px JPEG, 2:3 portrait |
| Who corrects it | The designer. The text is part of the artwork, so it cannot be fixed in the book's text, and an automatic OCR-and-replace would damage the lettering and lighting. |

## 1. Current problem

The footer of the back cover gives a website and an email address on a misspelt domain ("Hedayat"). The front cover and the academy's name use "Hidayet".

| Line on the back cover | Currently reads | Problem |
|---|---|---|
| Website (globe icon) | `www.HedayatEnglishAcademy.com` | Wrong spelling of the domain |
| Email (envelope icon) | `info@HedayatEnglishAcademy.com` | Same wrong domain; the correct address is not yet confirmed |
| Helpline (phone icon) | `Helpline: 6290 05 6461` | No problem; matches the logo (`6290056461`). Author confirmed it is current (3 Oct 2026). |

## 2. Exact website correction

- Replace `www.HedayatEnglishAcademy.com` with the website on the front cover: **hidayetenglishacademy.com**.
- **Author confirmed (3 Oct 2026):** `hidayetenglishacademy.com`, as on the front cover, in the current typeface and spacing.

## 3. Email requiring confirmation

- The current address, `info@HedayatEnglishAcademy.com`, uses the misspelt domain.
- **Author supplied (3 Oct 2026):** `info@hidayetenglishacademy.com`.
- Before the artwork is signed off, send a test email to the confirmed address and check that it arrives.

## 4. Mission-line issue

- The mission paragraph currently reads: "To help Bengali learners worldwide grow from where they are today, build confidence in English and move forward in their personal and professional lives."
- The book supports both Bengali and Hindi speakers: vocabulary tables give both languages, and the Bengali/Hindi notes address both.
- **Author decision (3 Oct 2026):** change to "Bengali and Hindi learners": "To help Bengali and Hindi learners worldwide grow from where they are today, build confidence in English and move forward in their personal and professional lives."
- The new line must fit the same three-line block without shrinking the type.

## 5. Visual elements to preserve

The replacement should change only the text in sections 2–4 above. Keep everything else exactly as it is:

- The top logo badge ("HIDAYET English Academy"), including its small line of non-Latin script and the phone number.
  - That script line should be checked by a native speaker; it is outside the scope of this brief.
- The "CAREER ENGLISH" title: white and copper lettering, serif capitals, with its glow.
- The "ABOUT THE AUTHOR" block:
  - "HEDAI TULLAH";
  - "Known as HIDAYET SIR";
  - "English teacher, author and founder of Hidayet English Academy."
- The "OUR MISSION" heading and its gold rules.
- The "EXPLORE OUR COURSES" list with its four circular icons:
  - Basic Spoken English;
  - Intermediate Spoken English;
  - Advanced Spoken English;
  - Grammar Mastery.
- "Discover more books by HEDAI TULLAH."
- The footer row: globe, envelope and phone icons, left-aligned with their text, in the same off-white serif type.
- The background photograph:
  - dark desk, window with city skyline at dusk;
  - lamp, plant, mug, open notebook with pen, laptop;
  - its warm copper lighting.
- Text colours, letter-spacing, gold rule lengths and the centring of every block.

## 6. Required final-resolution check

- **Resolution.** The current file prints on A4 at about 131 ppi (1024 px across about 198 mm), which is too low for commercial print.
  - Supply the replacement at 300 ppi or more for A4: at least 2480 × 3508 px.
  - Better still, supply the layered source or a vector/PDF export so the text stays sharp.
- **Shape.** The current image is 2:3 (1.5) while A4 is 1:1.414. The PDF fits it to the page height, leaving a dark strip about 6 mm wide on each side.
  - Either supply artwork at A4 proportions with bleed (216 × 303 mm if the printer asks for 3 mm bleed),
  - or confirm that the side strips are acceptable.
- **Front cover.** Front-cover artwork must be supplied/rebuilt at 300 ppi before final PDF regeneration. `front-cover.jpg` has the same size and shape (1024 × 1536 px, about 131 ppi on A4). Its text is correct; it needs at least 2480 × 3508 px and the same A4 shape decision. It is a separate gate (Front Cover) in `PROOF-CHECKLIST.md`.
- **Proof steps after replacement:**
  1. Rebuild the PDF (`build_print.py` and `render_pdf.js`, twice).
  2. Check the PDF at 100% and at 200% zoom.
  3. Check that the website and email lines are spelt exactly as approved, character by character.
  4. Check that no text is cropped at the page edges.
  5. Print one physical test page in colour.

## 7. Final designer approval status

| Check | Status |
|---|---|
| Website corrected to hidayetenglishacademy.com | PENDING (designer) |
| Email address supplied by the author | DONE (info@hidayetenglishacademy.com, 3 Oct 2026) |
| Email address corrected in the artwork | PENDING (designer) |
| Mission line decision | DONE ("Bengali and Hindi learners", 3 Oct 2026); artwork PENDING (designer) |
| Visual elements preserved (section 5) | PENDING (designer) |
| Print resolution and A4 shape (section 6) | PENDING (designer): author requires 300 ppi artwork in the final designer rebuild |
| Front-cover artwork at 300 ppi (at least 2480 × 3508 px), before final PDF regeneration | PENDING (designer); requirement set, text unchanged |
| Replacement file committed and PDF rebuilt | PENDING |
| Final visual check of PDF p. 1104 | PENDING |
| **Designer approval** | **DESIGNER ACTION REQUIRED** |
