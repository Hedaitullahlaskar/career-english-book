# Back cover: replacement brief

**Status: DESIGNER ACTION REQUIRED**

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
| Helpline (phone icon) | `Helpline: 6290 05 6461` | No problem found; matches the number in the logo (`6290056461`). Author to confirm it is current. |

## 2. Exact website correction

- Replace `www.HedayatEnglishAcademy.com` with the website on the front cover: **hidayetenglishacademy.com**.
- The author should choose how it appears, keeping the current typeface and spacing:
  - Option A, as on the front cover: `hidayetenglishacademy.com`.
  - Option B, keeping the current style: `www.HidayetEnglishAcademy.com`.
- Domains are not case-sensitive, so both open the same site.

## 3. Email requiring confirmation

- The current address, `info@HedayatEnglishAcademy.com`, uses the misspelt domain.
- **The author must supply the correct email address.** This brief does not propose one; nobody has confirmed which mailbox exists on the correct domain.
- Before the artwork is signed off, send a test email to the confirmed address and check that it arrives.

## 4. Mission-line issue

- The mission paragraph currently reads: "To help Bengali learners worldwide grow from where they are today, build confidence in English and move forward in their personal and professional lives."
- The book supports both Bengali and Hindi speakers: vocabulary tables give both languages, and the Bengali/Hindi notes address both.
- **Author decision:**
  - (a) keep "Bengali learners";
  - (b) change to wording that covers both, for example "Bengali and Hindi speakers" or "Bengali- and Hindi-speaking learners";
  - (c) use other wording the author supplies.
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
- **Front cover.** `front-cover.jpg` has the same size and shape (1024 × 1536 px, about 131 ppi on A4). Its text is correct, but it needs the same resolution and shape decision before print.
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
| Email address supplied by the author | PENDING (author) |
| Email address corrected in the artwork | PENDING (designer, after the author confirms) |
| Mission line decision | PENDING (author) |
| Visual elements preserved (section 5) | PENDING (designer) |
| Print resolution and A4 shape (section 6) | PENDING (designer) |
| Front-cover resolution decision | PENDING (author and designer) |
| Replacement file committed and PDF rebuilt | PENDING |
| Final visual check of PDF p. 1104 | PENDING |
| **Designer approval** | **DESIGNER ACTION REQUIRED** |
