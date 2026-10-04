# Industry and sector coverage audit

**Question:** which professional industries and sectors does the current Career English book actually cover, and how far?

**Answer in one line:** the book is built on one industry, **hospitality** (a hotel front office), and it adds short example lines for **IT, banking, retail and healthcare** in most lessons. Every other sector is a passing mention or absent.

Audit date: 3 October 2026. Branch `editorial-audit-2026-10`, HEAD `5685b52`. No book content was changed.

Related files:
- [INDUSTRY-COVERAGE-MATRIX.csv](INDUSTRY-COVERAGE-MATRIX.csv): one row per sector searched, with counts, lessons, evidence and search terms.
- [INDUSTRY-COVERAGE-SUMMARY.md](INDUSTRY-COVERAGE-SUMMARY.md): one-page summary for decisions.

## 1. Source of truth

| Source | Role in this audit |
|---|---|
| `book-data.json` | **Authoritative.** It holds every unit: 186 lessons, 5 level assessments and 5 capstones (196 units). The website (`index.html`) and the print PDF both render from it. Every count below comes from this file. |
| `editorial/print/Career-English-Master.pdf` | Not searched separately. The source/PDF consistency audit (`proof/SOURCE-PDF-CONSISTENCY.md`) shows that the PDF text matches `book-data.json`. PDF page numbers are given for evidence. |
| `reference-index.json` | Checked. It is derived from the book, and its labels are almost entirely sector-neutral: "front desk" 3 times, "housekeeping" once, "IT support" once, no other sector names. It adds no coverage. |
| `editorial/corrections/` | Not used as evidence. These are edits that have already been applied to `book-data.json`, so the current text in that file is what counts. |
| Planning and marketing material in this repository | `README.md`, the How to Use page, `AUDIT-PROGRESS.md`, the front cover and the back cover were searched for industry claims (see question 21). |
| *Ultimate Hospitality English Course* and other HEA projects | **Not used.** They are not in this repository and are not evidence for Career English. |

## 2. How the book is built (why this matters for "coverage")

- **Module and lesson titles are sector-neutral.** Examples: "Telephone English Basics", "Report Writing", "Negotiation", "Coaching Through Questions". None of the 196 unit titles or 40 module titles names an industry.
- **The main teaching content is one continuous hotel story.**
  - The learner follows Arif, who studied hospitality management. He joins a hotel's front office (Level 1), handles guests, calls and complaints (Level 2), and writes reports and manages corporate event clients (Level 3). In Level 4 he negotiates the hotel's linen contract and handles a booking-system outage; in Level 5 he leads the front-office team.
  - The dialogues, worked examples, many exercises, and every capstone are set in this hotel.
- **Most lessons end with an "Industry overlays" section.** 155 of the 196 units have one. It gives one or two sentences showing the same skill in another workplace. 127 of these sections have labelled items, such as "**Banking:** …" or "**IT:** …". The other 28 contain only a short general note saying the skill applies across industries, for example "Universal across every industry — a nurse asking a doctor to repeat an instruction, a bank clerk asking a manager…" (L1 5.1).

So there are two kinds of evidence, and this audit keeps them apart:
- **Core content:** the dialogues, scenarios, exercises and answer keys, almost all set in the hotel.
- **Overlay content:** one-line examples from other sectors, appended to a lesson whose teaching is general workplace English.

## 3. Method

1. Each unit's HTML was split into sections, and each section was tagged by type:
   - objectives;
   - teaching text;
   - vocabulary;
   - dialogue or scenario (dialogue boxes, scenario cards, worked examples);
   - exercise;
   - answer key;
   - industry overlay.
2. Each of the **65 listed sectors** was searched, plus **9 additional domains** found during the audit (74 in all). Each search used the exact sector term, synonyms, occupations and workplace situations (for example, BPO: *BPO, business process outsourcing, outsourcing, offshore*; call centre: *call centre/center, contact centre, inbound/outbound call, support queue, call handling*). The full pattern for each sector is in the CSV column "Search terms".
3. Every overlay label was counted and mapped to a sector. For example, "Banking (branch operations)" maps to Banking, and "Healthcare admin (scheduling coordinator)" maps to Healthcare.
4. **Every non-zero result was read in context before it was classified.** False positives were removed and the patterns tightened. Examples:
   - "delivery" meaning a speaker's delivery;
   - "off guard";
   - "brand-new";
   - "ship" as a verb;
   - "conference room";
   - "property" meaning the hotel;
   - "book my ticket".
5. Each sector was then given one of the controlled labels:

| Label | Rule used |
|---|---|
| **DEDICATED** | The sector is the book's own setting or has whole modules or levels of its own: lessons, dialogues, capstones. |
| **SUBSTANTIAL** | Sector-specific content in the core sections (dialogue, scenario, exercise, answer key) of about 10 or more units, or a multi-lesson storyline. |
| **REPEATED OVERLAY** | Appears as a labelled industry-overlay example in 10 or more units; core content is no more than passing. |
| **LIMITED OVERLAY** | Labelled overlay examples in 2–9 units. |
| **INCIDENTAL MENTION** | A few passing mentions: a sample answer, an analogy, a background detail, or a department named in the hotel story. |
| **NOT FOUND** | No relevant occurrence after the synonym searches. |

**Limits of the method:**
- Counts are pattern matches, not a measure of teaching time.
- "Units" means units containing at least one match.
- Every classification was confirmed by reading the matches. The counts support the label but did not decide it on their own.

## 4. Overlay frequency (labelled overlay items)

| Overlay sector | Items | Units | Levels |
|---|---|---|---|
| IT (including IT support, software, offshore IT team) | 88 | 87 | 1–5 |
| Banking | 73 | 73 | 1–5 |
| Retail | 58 | 58 | 1–5 |
| Hotel / hospitality (restating or extending the lesson's own scenario) | 58 | 56 | 1–5 |
| Healthcare (including healthcare admin, hospital/clinic) | 47 | 47 | 1–5 |
| Client account / corporate B2B (no industry named) | 23 | 17 | 2–4 |
| Office / corporate office (generic) | 17 | 15 | 1–5 |
| Sales | 13 | 13 | 2–5 |
| Supply chain or supplier | 8 | 8 | 4 |
| Education (including education administration) | 5 | 5 | 2–5 |
| Internal budget negotiation (finance department) | 5 | 5 | 4 |
| Tourism | 3 | 3 | 3, 5 |
| Phone/chat support | 2 | 2 | 2, 5 |
| Facilities/maintenance contractor | 1 | 1 | 4 |

A typical overlay, from Level 1 Lesson 1.1 (PDF p. 13), gives one sentence each for Hotel, Healthcare, Banking, IT and Retail. For example: "**Banking:** Being professional here means double-checking details out loud before confirming a transaction."

## 5. Master table

Counts:
- **Units** = units with any match.
- **Core** = units with a match outside the overlay sections (this includes passing mentions).
- **Overlay items** = labelled overlay items for that sector.

Full lesson lists, titles and search patterns are in the CSV.

### 5.1 Dedicated and substantial

| Industry | Classification | Levels / modules | Units (core) | Evidence (short) | Type |
|---|---|---|---|---|---|
| Hospitality / Hotels | **DEDICATED** | All 5 levels; all 5 capstones; the main scenario of most modules | 171 (160); 1,601 hits | "I studied hospitality management, and I worked at a small hotel" (L1 1.5); "Arif is standing outside the hotel's staff entrance" (L1 2.1) | Core setting |
| Front Office | **DEDICATED** | All levels | 128 (125) | "Good afternoon, Front Desk, this is Arif speaking" (L2 3.5); online check-in rollout meeting (L3 3.6) | Core setting |
| Customer service (function) | **DEDICATED** | L2 M7 Basic Customer Interaction; L3 M5 Customer Service & Complaint Handling; L3 1.4 | 76 (62) | "A guest steps up to the front desk clearly upset." (L3 5.1) | Core, with hotel guests |
| Business management / leadership (function) | **DEDICATED** | Level 5 Leadership English (8 modules) | — | Delegation, feedback, coaching, change, chairing, executive presentations | Core function, not an industry |
| Housekeeping | **SUBSTANTIAL** | L1–L5; linen contract L4 M1, L4 M8, L4 capstone | 50 (46) | "A guest at the front desk asks Arif if housekeeping can send extra towels" (L2 2.4) | Core (hotel department) |
| Food & Beverage (hotel) | **SUBSTANTIAL** | L2 7.2; L3 2.1, 2.3, 2.4; L3 6.2–6.3; L3 capstone; L4 6.5 | 18 (16) | Explaining "F&B" to a guest (L2 7.2); restaurant allergy incident report (L3 2.3) | Core (hotel department) |
| Event management (hotel events) | **SUBSTANTIAL** | Meridian Partners conference: L3 M6, L3 capstone, L4 M7–M8; wedding season: L4 M6 | 35 (35) | "clients who book multi-day conferences and functions at the hotel" (L3 6.1) | Core (hotel events) |
| Sales (hotel corporate and events sales) | **SUBSTANTIAL** | L3 M6 Client Communication Basics (5 lessons) and L3 capstone; 13 overlays | 27 (9); 13 overlay items | "Ms. Cruz: It's our regional sales kickoff — around sixty attendees." (L3 6.2) | Core + overlay |
| Facilities / maintenance (hotel) | **SUBSTANTIAL** | L2 M6 Following Up (the maintenance-request storyline); L2 capstone; L4 | 19 (18) | "A three-message annotated follow-up ladder about the Room 204 maintenance request" (L2 6.3) | Core (hotel department) |
| Vendor / supplier management (function) | **SUBSTANTIAL** | L4 M1 Negotiation; L4 M8 Advanced Client & Vendor Relations; L4 capstone | — | "The hotel's linen supplier, Bengal Textile Supplies, is raising prices" (L4 1.1) | Core function (hotel buyer's side) |
| Job seeking / career communication (function) | **DEDICATED** | L5 M7 Career Growth Communication (6 lessons) | — | CV, interview, salary, resignation | Core function, not an industry |

### 5.2 Overlays

| Industry | Classification | Levels | Units (core); overlay items | Evidence (short) | Type |
|---|---|---|---|---|---|
| IT / software / IT support | **REPEATED OVERLAY**, plus a supporting role in the hotel story | 1–5 | 107 (17); 88 items | "IT: Being professional here often means responding to messages within a reasonable time" (L1 1.1). In Level 4 the hotel works with its IT team, an IT vendor and an offshore development team (L4 3.4, M6, M7, M8, capstone). | Overlay; IT people are counterparts, never the learner's role |
| Banking | **REPEATED OVERLAY** | 1–5 | 83 (7); 73 items | "Banking (relationship manager, new business client)" (L3 6.1). Outside overlays only sample answers ("I'm a teller at a bank branch", L1 1.4). | Overlay |
| Retail | **REPEATED OVERLAY** | 1–5 | 77 (7); 58 items | Stockroom discrepancy report (L3 2.3 overlay). Outside overlays only background lines ("mostly in retail"). | Overlay |
| Healthcare (mainly administration) | **REPEATED OVERLAY** | 1–5 | 54 (10); 47 items | "Healthcare: … keeping patient information confidential" (L1 1.1); insurance-claim apology (L3 1.4 overlay) | Overlay |
| Office / corporate office (generic) | **REPEATED OVERLAY** | 1–5 | 82 (72); 17 items | "Office" / "Corporate office" / "Fixed-hours office" overlay labels | Overlay + generic setting |
| Education | **LIMITED OVERLAY** | 2–5 | 14 (8); 5 items | "Education: I'm not able to take an extra class this week" (L2 2.2) | Overlay |
| Tourism | **LIMITED OVERLAY** | 1, 3, 5 | 5 (2); 3 items | "Tourism (travel consultant)" (L3 6.3); "degree in tourism management" (L1 1.2 vocabulary) | Overlay |
| Call centre / contact centre | **LIMITED OVERLAY** | 2, 5 | 3 (0); 2 items | "Phone/chat support: Thanks for calling/reaching out" (L2 7.1) | Overlay |
| Finance (as a department) | **LIMITED OVERLAY** | 4 | 42 (35); 5 items | "Internal budget negotiation" overlays; budgets and invoices as office tasks | Overlay / department |
| Supply chain / logistics | **LIMITED OVERLAY** | 4 | 51 (42); 8 items | "Supply chain (delivery disruption)" (L4 6.1) | Overlay |
| Hospitals; nursing; retail management; professional services | **LIMITED OVERLAY** | various | 3–9 units each | Ward assistant / nurse manager (L1); store manager (L1, L3–L5); "Client scope negotiation (a services company and a client)" (L4) | Overlay |

### 5.3 Incidental mentions

Each of these appears only in passing: a sample answer, a background detail, an analogy, or a hotel department named in the story.

| Industry | Units | Evidence (short) |
|---|---|---|
| Aviation / airlines | 9 | Hotel guests' flights and airport pickups only: "a missed wake-up call that made them late for a flight" (L3 1.4) |
| Travel | 17 | Guests' travel circumstances: "The guest who lost her passport…" (L3 7.5) |
| Sports | 3 | "General hobbies or sports" as a safe small-talk topic (L1 3.3); a coach/player analogy (L3 9.4); "turn professional" in sport (L1 1.1) |
| HR | 9 | Sadia Chowdhury, the HR colleague in L1 who runs orientation |
| Recruitment | 8 | Candidate side only (L5 M7); no recruiter role |
| Training / L&D | 37 | Orientation and training as workplace events |
| Kitchen / culinary | 8 | "our pastry chef is off sick" (L4 6.2 answer key) |
| Pharmacy | 3 | One sample answer: "Sample (a pharmacy)" (L2 7.1) |
| Insurance | 3 | Inside healthcare-admin overlays |
| Accounting | 4 | "I studied accounting" (L1 1.3 answer key) |
| Legal | 13 | "Compliance" in banking overlays |
| Engineering | 23 | The hotel's Engineering (maintenance) department |
| Construction | 6 | Hotel renovation |
| Procurement | 2 | The hotel's procurement team (L4 6.5) |
| Stores / warehouse | 36 | Storeroom inventory counts |
| Security | 3 | Nasir, the security guard at the gate (L1 3.1) |
| E-commerce | 1 | One answer key: "affecting online orders" (L4 6.4) |
| Consulting | 1 | "travel consultant" (L3 6.3) |
| Teaching | 3 | "school principal" in one overlay |
| Fitness | 1 | The hotel gym |
| Spa | 2 | The hotel spa |
| Transport | 2 | Arif's bus is late |
| Textiles | 6 | The supplier's name, "Bengal Textile Supplies" |

### 5.4 Not found

These were searched and found nowhere in the book:
- **BPO**;
- **cricket**;
- cruise / maritime;
- aviation ground operations;
- government / public sector;
- manufacturing;
- real estate (one "landlord" in a small-talk example only);
- media, journalism, advertising, PR;
- marketing (one "brand" meaning a product brand only);
- healthcare technology;
- startups / entrepreneurship;
- NGO / non-profit;
- sports management;
- restaurant management;
- additional searches: telecom, automotive, energy/utilities, agriculture, pharmaceutical industry.

## 6. Deep analysis

1. **What industries are genuinely covered?**
   - Hospitality only, in the sense of an industry the book teaches in: the hotel front office, with its partner departments (housekeeping, F&B, events, maintenance, hotel sales).
   - The cross-industry *functions* are also covered in depth: customer service, management/leadership, vendor relations and job seeking. These are taught through the hotel.
2. **Which industries receive the strongest coverage?**
   - Hospitality, by far: 171 of 196 units, the dialogues of at least 119 units, all five capstones.
   - Next are four overlay sectors that recur in every level: IT (88 overlay items), banking (73), retail (58) and healthcare (47).
3. **Which industries appear only as examples or overlays?**
   - Repeated: IT, banking, retail, healthcare (mostly administration), generic office.
   - Limited: education, tourism, call centre (phone/chat support), finance (internal budgets), supply chain, hospitals, nursing, retail management, professional services.
4. **Is hospitality the dominant industry context?** Yes. It is not an overlay; it is the book's setting from the first lesson to the last capstone.
5. **Is healthcare genuinely represented?**
   - Only as a repeated overlay: 47 one- or two-sentence examples in 47 units, mostly healthcare *administration* (scheduling, insurance claims, intake forms).
   - There is no healthcare dialogue, character, scenario or lesson. Outside overlays there are only a few sample answers.
6. **Is banking genuinely represented?**
   - As a repeated overlay only: 73 items in 73 units (teller, loan officer, branch manager, relationship manager).
   - There is no banking dialogue or lesson.
7. **Is IT genuinely represented?**
   - As the most frequent overlay (88 items).
   - In Level 4 IT also appears as a counterpart in the hotel story: the hotel's IT support lead, its IT vendor (NexaCore IT Solutions) and an offshore development team building the check-in module.
   - The learner is always the hotel employee dealing with IT, never an IT worker. That is not dedicated IT-industry English.
8. **Is retail genuinely represented?** As a repeated overlay only (58 items). There is no retail dialogue or lesson.
9. **Is education genuinely represented?** Barely: 5 overlay items and a few passing words (college, classroom).
10. **Is BPO genuinely represented?** No. The term and its synonyms do not occur. The "offshore team" in L4 M7 is a software-development vendor, not a BPO operation.
11. **Is call centre / contact centre genuinely represented?**
    - No, apart from 2 "Phone/chat support" overlay lines and one passing "call center".
    - Telephone English Basics (L2 M3) teaches phone handling at a hotel front desk. It has no queues, scripts, call metrics or inbound/outbound campaigns.
12. **Is aviation genuinely represented?** No. Flights and airports appear only as hotel guests' circumstances (airport pickups, a guest late for a flight). There is no airline or airport workplace.
13. **Is cruise genuinely represented?** No.
14. **Is tourism genuinely represented?** Only as a limited overlay: 3 items, plus one vocabulary sentence ("My degree is in tourism management").
15. **Is finance / accounting genuinely represented?**
    - Finance: limited overlay only (5 internal-budget overlays in L4). Budgets and invoices appear as ordinary office tasks.
    - Accounting: incidental (4 units).
    - Banking is the only finance-adjacent sector with repeated examples.
16. **Is HR genuinely represented?**
    - As a department in the story (an HR colleague in Level 1) only.
    - Performance conversations and feedback (L5 M2) are taught as a manager's skill, not as HR-practitioner English.
17. **Is sales / marketing genuinely represented?**
    - Sales: yes, as hotel B2B sales (L3 M6, 5 lessons, plus the L3 capstone), with 13 overlays.
    - Marketing: no.
18. **Is procurement / stores / logistics genuinely represented?**
    - As a function only: the hotel buys linen and manages suppliers (L4 M1, L4 M8).
    - Procurement, stores and logistics as industries are incidental or limited overlays.
19. **Is sports genuinely represented?** No: 3 passing mentions.
20. **Is cricket specifically represented?** No: zero occurrences.
21. **Are there industries in planning documents but not in the book?**
    - No planning document in this repository lists target industries.
      - The How to Use page promises only "industry examples".
      - `AUDIT-PROGRESS.md` records Arif as a hotel front-office employee.
      - The front cover's subtitle is "English for Your Professional Journey", with no sectors.
      - The back cover lists courses, not sectors.
    - The book itself names its example sectors once. The Level 1 Lesson 6.1 overlay lists Hotel, Bank, Hospital/clinic, IT company and Retail, and Lesson 6.5 speaks of "every industry this course covers". That set matches the evidence: one setting plus four overlay sectors.
    - The proposed marketing statement in section 7 is the only wider industry list found. Its BPO/call centres, aviation and sports are absent from the book, and education and tourism are barely present.
22. **Are there industries in the book that were not anticipated?** Compared with the 65-sector search list, the book adds:
    - hotel facilities/maintenance (substantial);
    - vendor/supplier management (substantial function);
    - generic corporate office (repeated overlay);
    - generic "client account / corporate B2B" overlays (23 items);
    - commuting and a textile supplier's name (incidental).

## 7. The proposed marketing statement

> "Career English covers English for hospitality, healthcare, IT, banking, retail, BPO/call centres, education, aviation, tourism, sports and other professional sectors."

**Verdict: NOT SUPPORTED as written. Only partly supported.**

| Claimed sector | Evidence | Supported? |
|---|---|---|
| Hospitality | Dedicated: the book's own setting | **Yes** |
| Healthcare | Repeated overlay (47 example lines) | Only as "examples from" |
| IT | Repeated overlay (88), plus IT counterparts in Level 4 | Only as "examples from" |
| Banking | Repeated overlay (73) | Only as "examples from" |
| Retail | Repeated overlay (58) | Only as "examples from" |
| BPO / call centres | BPO not found; call centre: 2 overlay lines | **No** |
| Education | Limited overlay (5 lines) | **No** (too thin to claim) |
| Aviation | Incidental (guests' flights only) | **No** |
| Tourism | Limited overlay (3 lines) | **No** (too thin to claim) |
| Sports | Incidental (3 passing mentions); cricket not found | **No** |
| "Other professional sectors" | Generic office and client-account overlays | Only as "transferable workplace English" |

The word "covers" overstates even the four overlay sectors. A reader would expect lessons or scenarios in those industries, and the book gives one-sentence examples.

**Narrower statements the evidence supports:**

- Precise version: *"Career English teaches the English of everyday professional life — through one continuous workplace story set in a hotel, from a new employee's first day to leading a team — with short examples from banking, retail, IT and healthcare in most lessons."*
- Short version: *"Workplace English for every career, taught through a real hotel workplace story, with examples from banking, retail, IT and healthcare."*
- Skill-based version, with no sector claim: *"Career English: five levels of workplace English — from your first day at work to leading a team."*

## 8. What should appear on the book cover?

**Recommendation:**
- **Front cover: B, a broad statement with no list of sectors (or D, no sector claim).** The current subtitle, "English for Your Professional Journey", already meets this standard and should stay as it is.
- **Back cover or blurb: C, selected industries.** Only if sectors are named at all, and only as *examples*: "with examples from banking, retail, IT and healthcare", with hospitality named as the main setting.
- **Do not use A**, a list of specific industries.

Reasons, from the evidence:
- **A (list specific industries)** is not supported. A list implies coverage, and only hospitality has it. Listing BPO, aviation, sports, education or tourism would be false. Listing healthcare, IT, banking and retail as "covered" would overstate one-sentence examples.
- **B (broad statement)** is supported:
  - every module and lesson title is a sector-neutral workplace skill;
  - 155 units carry cross-industry examples;
  - 28 overlay sections say the skill applies across industries (for example "Universal across every industry", L1 5.1).
  - The claim the book supports is "transferable workplace English", not "coverage of many industries".
- **C (selected industries)** is supported only in the narrow form above. Hospitality is the real setting; banking, retail, IT and healthcare are recurring example sectors. It belongs in the back-cover or marketing copy, where it can be worded precisely.
- **D (avoid sector claims)** is always safe. It fits the front cover, where space allows only a few words.

If the author wants the cover to name more sectors, the book would need new content first, for example dedicated scenarios or modules for those sectors. That is an editorial decision outside this audit.

## 9. Integrity statement

- This audit is read-only:
  - `book-data.json`, `reference-index.json`, the lessons, answer keys, cover artwork and publication gates were not changed;
  - nothing was committed or pushed.
- The search scripts were run from a temporary folder outside the repository.
- Publication approval remains **NO**.
