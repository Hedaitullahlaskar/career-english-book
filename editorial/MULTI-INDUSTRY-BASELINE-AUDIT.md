# Multi-industry baseline audit

**Purpose:** establish, from the current book only, what a multi-industry expansion would build on.

This is Phase 1 (architecture only). Nothing in the book was changed. Audit date: 3 October 2026; branch `editorial-audit-2026-10` at `5685b52`.

Companion files:
- [MULTI-INDUSTRY-COVERAGE-MATRIX.csv](MULTI-INDUSTRY-COVERAGE-MATRIX.csv): 50 rows (40 modules, 5 assessments, 5 capstones) × 14 candidate industries, with each module's universal skill area and transfer category.
- [INDUSTRY-COVERAGE-AUDIT.md](INDUSTRY-COVERAGE-AUDIT.md): the earlier sector-by-sector audit of 74 sectors, whose evidence this file reuses.

## 1. What was inspected

| Source | Finding used here |
|---|---|
| `book-data.json` | **Single source of truth.** 5 levels, 40 modules, 186 lessons, 5 level assessments and 5 capstones (196 units). Total estimated study time 4,510 minutes. Content is stored as three HTML fields per unit: `objectives_html`, `body_html`, `practice_html`. |
| `reference-index.json` | 926 indexed codes in 8 types: V 540, MIS 180, PAT 133, CF 25, GIC 18, TL 14, TIP 8, P 8. Numbers have gaps (V reaches V-0792) because codes were retired or recycled. |
| `index.html` | Website. Loads `book-data.json` and `reference-index.json`. It has a level tree, search (including code search), and a "reviewed" progress flag per lesson in browser storage (`hea-book-reviewed`). |
| `editorial/tools/build_print.py`, `editorial/print/render_pdf.js`, `editorial/print/pages.json` | Print edition: 1,104 pages. Measured sizes: lesson mean 5.0 pages (range 4–8); assessments 5–8; capstones 8–14; module opener about 1 page; Reference Index 34 pages for 926 codes. |
| `editorial/tools/build_reference_index.py`, `index.html`, `build_print.py` | All three recognise codes with the pattern `\b(V\|PAT\|GIC\|CF\|TL\|MIS\|TIP\|P)-\d{3,4}\b`. This matters for any new code scheme (section 5). |
| `editorial/tools/apply_corrections.py` | `book-data.json` is verified as "baseline `61c769f` + logged corrections". Adding new content directly to it would fail this check unless the correction model is extended (see the data schema). |
| `editorial/INDUSTRY-COVERAGE-*` | Earlier coverage audit (74 sectors). |
| Editorial and proof files | `QA-REPORT.md` and `proof/PROOF-CHECKLIST.md`, for current gate status: human proofread and native-language review NOT PERFORMED; publication approval NO. |

**Two items from the brief that are not in the book:**
- **Level 1's title** is "Level 1 — Foundation", not "Workplace Foundations".
- **The "Learn → Understand → Observe → Practice → Perform → Reflect → Improve" cycle** does not appear in `book-data.json`, `index.html` or the print builder.
  - "Improve" occurs 0 times; "Learn" and "Observe" once each, not as a cycle.
  - The framework the book does teach is **PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION**, introduced in Level 1 Module 7 and reused afterwards.
  - The architecture below treats the cycle as a *proposed* design principle, not an existing feature.

**Other baseline facts that affect the design:**
- **No audio exists.** Listening sections state "Audio is not available yet, so this part is read, not heard."
- **Bengali/Hindi script appears in 31 units, 27 of them in Level 1.** Later levels have English-language "Bengali support / Hindi support" notes (40 sections in all) but almost no script.
- **Lesson anatomy.** Typical sections, by how many units use them:

| Section | Units |
|---|---|
| Lesson Opening | 186 |
| Key Workplace Lesson | 186 |
| Exercises | 196 |
| Answer Key | 196 |
| Motivation | 186 |
| Self-Check | 191 |
| Industry Overlays | 155 |
| Vocabulary | 152 |
| Key Expressions | 152 |
| Professional Tone | 149 |
| Common Mistake | 170 |
| Grammar in Context | 61 |
| Listen & Read dialogue boxes | 213 boxes |

- **Exercises:** 709 in total.
  - The most common types are Role-Play 164, Guided Practice 137, Recognition 108, Rewriting 106 and Multiple Choice 67.
  - Writing tasks labelled as such: 12. Comprehension: 13.

## 2. Coverage scale used

Definitions from the brief, applied consistently:

| Level | Name | Meaning |
|---|---|---|
| 1 | MENTION | The industry appears incidentally. |
| 2 | OVERLAY | A universal lesson gives a few example lines from the industry. |
| 3 | APPLICATION | The learner practises the skill in a meaningful industry-specific situation. |
| 4 | DEDICATED INDUSTRY MODULE | Several connected lessons with vocabulary, dialogues, situations, role-play, writing, listening, speaking, problem solving, documents and assessment. |
| 5 | FULL INDUSTRY TRACK | A structured sequence for that industry from entry level to leadership. |

How the matrix assigns a level per module:
- **APPLICATION** needs industry terms inside the module's dialogue or scenario sections, with the learner in an industry role.
- **OVERLAY** needs a match in an "Industry overlays" section.
- **MENTION** needs a match anywhere else.

Every pattern was checked by reading the matches in the earlier audit. This rule is conservative: a hotel-set module whose dialogues happen not to use hotel words (for example L2 M6 Following Up, built around a hotel maintenance request) shows as OVERLAY or MENTION, not APPLICATION.

## 3. Findings A–J

### A. Existing universal professional skills

All 40 modules teach a universal workplace skill; no module or lesson title names an industry. The 25 universal skills in the brief map onto the existing core as follows (lesson numbers are Level.Module.Lesson):

| Universal skill | Where the core teaches it now |
|---|---|
| Introducing yourself | L1 M1 (1.3), L1 M2 |
| Giving a work update | L2 M1 (1.1–1.4) |
| Asking for clarification | L1 M5; L1 M4 (4.4) |
| Giving instructions | L5 M1 (1.1–1.2); receiving instructions: L1 M4 |
| Making requests | L1 M7 (7.2); L2 M2 |
| Making suggestions | L3 M3 (3.3); L4 M4 (4.2) |
| Handling a customer | L2 M7 |
| Handling a complaint | L2 M7 (7.4); L3 M5; L3 M1 (1.4) |
| Apologising professionally | L2 M5 |
| Explaining a problem | L2 M1 (1.2); L4 M4 (4.1) |
| Escalating an issue | L3 M1 (1.5); L3 M5 (5.4); L4 M6 |
| Writing an email | L3 M1 |
| Writing a report | L3 M2 |
| Joining a meeting | L3 M3 (3.3–3.4) |
| Leading a meeting | L3 M3 (3.2, 3.5); L5 M5 |
| Giving a presentation | L3 M4; L4 M5; L5 M6 |
| Negotiating | L4 M1 |
| Handling disagreement | L3 M3 (3.3); L4 M2 |
| Giving feedback | L4 M2 (2.2); L5 M2 |
| Receiving feedback | L4 M2 (2.3) |
| Delegating | L5 M1 |
| Coaching | L5 M3 |
| Managing conflict | L4 M2 (2.5–2.6) |
| Handling a crisis | L4 M6 |
| Communicating decisions | L4 M4 (4.3); L5 M5 (5.3) |

Every one of the 25 skills already has core instruction. **The expansion does not need new universal teaching. It needs industry *application* of skills the core already teaches.**

### B. Existing hospitality-specific skills

These are taught through the hotel and are specific to it:
- Front-desk greeting and phone opening ("Good afternoon, Front Desk, this is Arif speaking", L2 3.5).
- Explaining hotel jargon to guests ("F&B", L2 7.2).
- Guest complaint recovery with hotel remedies: upgrade, late checkout, goodwill gestures (L3 M5; L3 1.6).
- Room-inventory and storeroom counts; housekeeping requests; maintenance requests (L2).
- Corporate event and conference accounts (L3 M6; L3 capstone).
- Linen supplier contract negotiation (L4 M1; L4 M8; L4 capstone).
- Property-management-system outage (L4 M6).
- Online check-in and kiosk rollout (L3 3.6; L5 6.3–6.4).
- Front-office shift handover and team leadership (L5; L5 capstone).

### C. Existing industry overlays

There are 155 "Industry overlays" sections; 127 have labelled items and 28 are general "applies across industries" notes. Labelled items by sector:

| Sector | Labelled items | Units |
|---|---|---|
| IT | 88 | 87 |
| Banking | 73 | 73 |
| Retail | 58 | 58 |
| Hotel | 58 | 56 |
| Healthcare | 47 | 47 |
| Client account / B2B (no industry named) | 23 | — |
| Office | 17 | — |
| Sales | 13 | — |
| Supply chain / supplier | 8 | — |
| Education | 5 | — |
| Internal budget | 5 | — |
| Tourism | 3 | — |
| Phone/chat support | 2 | — |
| Facilities | 1 | — |

### D. Industries with only examples

On the 14 candidate industries, counted across the 50 module/assessment/capstone rows of the matrix:

| Industry | OVERLAY rows | MENTION rows |
|---|---|---|
| IT & Technology | 33 | 2 |
| Banking & Finance | 31 | 10 |
| Retail | 30 | 1 |
| Corporate / Office | 26 | 14 |
| Healthcare & Hospitals | 23 | 5 |
| Logistics & Supply Chain | 19 | 15 |
| Professional Services | 10 | 3 |
| Education | 7 | 7 |
| Tourism & Travel | 4 | 12 |
| BPO & Contact Centre | 2 | 0 |

None of these reaches APPLICATION in any row. The learner never acts in a non-hotel role in a dialogue, scenario or capstone.

### E. Industries with meaningful instructional coverage

**Hospitality only.** It reaches APPLICATION in 39 of the 50 rows, including all 5 capstones.
- It does **not** meet Level 4 or 5 as defined. Industry-specific vocabulary domains, documents and assessments are not taught *as hotel English*:
  - the vocabulary is overwhelmingly universal;
  - the 5 level assessments are sector-neutral (MENTION only).
- Functionally, the book is a de facto narrative track for **one hotel role**, the front office, from entry to team leadership. It is not a hospitality-industry track covering other hotel roles.

### F. Industries absent

- **No evidence at all:** Manufacturing.
- **Only incidental mentions:**
  - Aviation: 9 rows, all hotel guests' flights.
  - Sports & Sports Management: 3 rows.
- **Not found** (earlier audit): BPO as a term; cricket; cruise; government; media; marketing; NGO; real estate; startups.

### G. Skills that transfer directly into another industry

These are **22 rows, transfer category G**. The PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION logic, and the language, work unchanged in any industry; only the example context changes.
- Level 1: Greetings & Small Talk; Asking for Help & Clarification; Foundations of Professional Tone.
- Level 2: Making & Responding to Requests; Digital Messaging; Apologizing & Thanking; Following Up.
- Level 3: Meetings; Professional Grammar; Pronunciation; Digital & Cross-Platform Communication.
- Level 4: Difficult Conversations; Persuasion; Presentations II; Cross-Cultural Communication.
- Level 5: Delegation; Feedback & Performance; Coaching; Strategic & Change Communication; Leading Meetings & Decisions; Executive Presentation Skills; Personal Leadership Voice.

### H. Skills that need industry-specific vocabulary and context

These are **11 rows, category H**. The structure transfers, but the learner cannot perform without industry terms: status words, document names, service terms, contract terms.

| Module | What changes by industry |
|---|---|
| Starting Work | role descriptions |
| Basic Workplace Vocabulary | roles, places, tools, documents |
| Daily Work Updates | ticket / account / patient / shipment status |
| Workplace Etiquette | confidentiality rules (patient data, bank secrecy) |
| Professional Email Writing | content and compliance language |
| Presentations I | industry metrics |
| Client Communication Basics | offers and objections |
| Negotiation | rate, SLA, scope, tariff |
| Advanced Problem-Solving Communication | problem types |
| Advanced Client & Vendor Relations | contract and service terms |
| Career Growth Communication | industry CV and interview conventions |

### I. Skills that need entirely new scenarios

These are **4 rows, category I**. The situation itself changes, so the hotel scenario cannot simply be relabelled.

| Module | Why |
|---|---|
| First-Day Communication | shift handover, ward, branch, shop floor and plant are different workplaces |
| Telephone English Basics | contact-centre call flows, identity verification, triage |
| Basic Customer Interaction | the customer becomes a patient, passenger, account holder, caller or parent |
| Customer Service & Complaint Handling | complaint types and the remedies staff are *allowed* to offer differ; in regulated sectors staff cannot offer what a hotel can (an upgrade or refund) |

### J. Skills that need new assessment models

These are **13 rows, category J**: 3 modules plus all 5 assessments and 5 capstones.

| Module | Why it needs a new assessment model |
|---|---|
| Understanding Instructions | safety-critical read-back in healthcare, aviation and manufacturing must be assessed for accuracy, not tone |
| Report Writing | industry document formats: incident report, shift report, QA report, post-incident review |
| Escalation & Crisis Communication | regulated and safety-critical crisis protocols |

**Assessments and capstones:** the current ones assess universal skills in a sector-neutral or hotel context. Industry claims would need industry-specific performance tasks and scoring criteria.

## 4. Summary of the baseline

| Industry | Highest level reached | Base for expansion |
|---|---|---|
| Hospitality & Hotels | 3 APPLICATION, across the whole book, one role (front office) | Existing strong base |
| IT & Technology | 2 OVERLAY (33 rows); hotel IT counterparts in Level 4 | Existing overlay base |
| Banking & Finance | 2 OVERLAY (31) | Existing overlay base |
| Retail | 2 OVERLAY (30) | Existing overlay base |
| Healthcare & Hospitals | 2 OVERLAY (23), mainly administration | Existing overlay base |
| Corporate / Office | 2 OVERLAY (26) | Existing overlay base (generic) |
| Logistics & Supply Chain | 2 OVERLAY (19; many are the hotel's own suppliers) | Limited overlay base |
| Professional Services | 2 OVERLAY (10) | Limited overlay base |
| Education | 2 OVERLAY (7) | Limited overlay base |
| Tourism & Travel | 2 OVERLAY (4); travel mentions are hotel-guest context | Limited overlay base |
| BPO & Contact Centre | 2 OVERLAY (2 "phone/chat support" lines) | Effectively no base |
| Aviation | 1 MENTION | No base |
| Sports & Sports Management | 1 MENTION (3 passing) | No base |
| Manufacturing | none | No base |

**What the baseline shows:**
- The book is a complete **universal professional-English core** that happens to be told through one hotel role.
- Genuine multi-industry coverage would need new **application** content for every industry, including hospitality roles other than the front office.
- The transferable core does not need rewriting.
