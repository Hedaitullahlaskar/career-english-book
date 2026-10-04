# Career English: multi-industry expansion architecture

**Phase 1: architecture and gap analysis only.**
- Nothing in the book has been changed: `book-data.json`, lessons, codes, the PDF, covers, indexes and publication gates are untouched.
- Nothing has been committed or pushed.
- Every design choice below that needs the author's approval is listed in [MULTI-INDUSTRY-AUTHOR-DECISIONS.md](MULTI-INDUSTRY-AUTHOR-DECISIONS.md). Where this document says "proposed design", it means a proposal awaiting that approval.

Companion files:

| File | Content |
|---|---|
| [MULTI-INDUSTRY-BASELINE-AUDIT.md](MULTI-INDUSTRY-BASELINE-AUDIT.md) | Forensic baseline: findings A–J |
| [MULTI-INDUSTRY-COVERAGE-MATRIX.csv](MULTI-INDUSTRY-COVERAGE-MATRIX.csv) | 50 module/assessment/capstone rows × 14 industries |
| [MULTI-INDUSTRY-DATA-SCHEMA.md](MULTI-INDUSTRY-DATA-SCHEMA.md) | Proposed data model |
| [INDUSTRY-COVERAGE-AUDIT.md](INDUSTRY-COVERAGE-AUDIT.md) | Earlier 74-sector audit |

---

## 1. Executive summary

- **The current book is a complete universal professional-English core, told through one hotel role.**
  - Its 40 modules teach 25 universal workplace skills, from self-introduction to leading change.
  - Its dialogues and capstones are set in one hotel front office.
  - Other industries appear only as one-line "industry overlay" examples. The most frequent are IT (88 items), banking (73), retail (58) and healthcare (47).
- **No industry other than hospitality reaches "application" level**, and hospitality covers one role (front office), not the industry.
- **The expansion therefore needs new *application* content, not new universal teaching.** Every universal skill in the brief is already taught in the core.
- **Proposed design: Model D, hybrid.**
  - The existing 5-level book stays unchanged as the **Universal Core**.
  - New **Industry Application Modules** apply core skills to industry situations. They are organised by industry and by three bands aligned to core Levels 1–2, 3–4 and 5.
  - A **Role layer** lets a learner filter situations by job role.
  - Content lives in a separate data file that references core skills by stable IDs. The core book's data file and its verification remain untouched.
- **Claim control is part of the design.** "Covers industry X" may be said only when a defined coverage tier is met (section 23). Today only these claims are supported:
  - "workplace English useful across industries";
  - "includes examples from IT, banking, retail and healthcare";
  - "set in a hotel workplace".
- **Scale.** A full track is about 168 print pages per industry; an industry module (one band) about 63 pages.
  - 14 full tracks would add about 2,350 pages to the current 1,104.
  - That supports keeping the core book as one volume and publishing industries as separate supplements and/or digital tracks.
  - The choice of publishing option is an author decision.

## 2. Current-state findings

These are from the baseline audit.

| Finding | Evidence |
|---|---|
| Size | 5 levels, 40 modules, 186 lessons, 5 assessments, 5 capstones (196 units); 4,510 estimated minutes; 1,104 PDF pages |
| Codes | 926 indexed codes (V 540, MIS 180, PAT 133, CF 25, GIC 18, TL 14, TIP 8, P 8); numbers have gaps (V up to V-0792) |
| Framework | PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION (from L1 M7) |
| Learning cycle in brief | "Learn → … → Improve" is **not** present in the book; proposed here as a design principle only |
| Setting | Arif, hotel front office; hotel terms in 171/196 units; hospitality reaches APPLICATION in 39 of 50 matrix rows, including all 5 capstones |
| Overlays | 155 sections; IT 88, banking 73, retail 58, hotel 58, healthcare 47 labelled items |
| Assessments | 5 level assessments are sector-neutral; 5 capstones are hotel-set |
| Audio | None ("Audio is not available yet, so this part is read, not heard") |
| Bengali/Hindi | Script in 31 units (27 in Level 1); 40 English-language "Bengali/Hindi support" notes |
| Data | One file, `book-data.json`, an array of levels whose units store HTML. It is verified as baseline `61c769f` + logged corrections. |
| Code parsing | Website, index builder and print builder all match `\b(V\|PAT\|GIC\|CF\|TL\|MIS\|TIP\|P)-\d{3,4}\b` |
| Publication status | Core book: human proofread NOT PERFORMED; native-language review NOT PERFORMED; publication approval NO |

## 3. Current book architecture

```
Level 1 Foundation (7 modules) ──► Level 2 Workplace English (8) ──► Level 3 Professional English (9)
        ──► Level 4 Advanced Professional English (8) ──► Level 5 Leadership English (8)
Each level: modules → lessons → level assessment → capstone (Arif's story)
Each lesson (flexible): Lesson Opening · Key Workplace Lesson · Listen & Read dialogue · Key Expressions ·
  Vocabulary (V codes) · Grammar in Context · Common Mistake (MIS) · Professional Tone · Industry Overlays ·
  Bengali/Hindi support · Self-Check · Motivation · Exercises · Answer Key
```

This architecture is preserved unchanged. Arif's story, the level and lesson numbering, and all codes stay as they are.

## 4. Industry coverage baseline

The highest coverage level reached, using the brief's scale (1 MENTION · 2 OVERLAY · 3 APPLICATION · 4 DEDICATED MODULE · 5 FULL TRACK):

| Industry | Level reached | Note |
|---|---|---|
| Hospitality & Hotels | **3** | Throughout the book, but one role (front office). Not 4 or 5: no hotel-specific vocabulary domains, documents or assessments are taught as such. |
| IT & Technology | 2 | 33 matrix rows with overlay; hotel IT counterparts in Level 4 |
| Banking & Finance | 2 | 31 rows |
| Retail | 2 | 30 rows |
| Corporate / Office | 2 | 26 rows (generic) |
| Healthcare & Hospitals | 2 | 23 rows (mainly administration) |
| Logistics & Supply Chain | 2 | 19 rows; many are the hotel's own suppliers |
| Professional Services | 2 | 10 rows |
| Education | 2 | 7 rows |
| Tourism & Travel | 2 | 4 rows; other travel words are hotel-guest context |
| BPO & Contact Centre | 2 | 2 "phone/chat support" lines only |
| Aviation | 1 | Guests' flights only |
| Sports & Sports Management | 1 | 3 passing mentions; cricket 0 |
| Manufacturing | — | None |

## 5. Problems with the current multi-industry claim

1. **"Covers" is not supported for any industry except hospitality.** One-line overlays do not give the learner practice in that industry's situations, documents or vocabulary.
2. **Several sectors in the proposed marketing line are absent:** BPO/call centres, aviation and sports, with cricket at zero. Education and tourism are too thin to claim.
3. **Hospitality itself is one role.** Housekeeping, F&B and events appear only from the front office's point of view.
4. **Assessment does not test industry performance.** The level assessments are sector-neutral and the capstones are hotel-set.
5. **No audio.** "Listening practice" cannot be claimed for any track until audio exists.
6. **Bengali/Hindi support is front-loaded** (27 of 31 script units are in Level 1), and the native-language review of the current book has not been performed.

## 6. Proposed multi-industry architecture

### 6.1 The layered model

```
CAREER ENGLISH
  └─ UNIVERSAL PROFESSIONAL CORE ........ the existing 5 levels, unchanged; skills SK-01…SK-25
       └─ INDUSTRY APPLICATION ........... per industry (HOSP, IT, BFS …); 3 bands: Entry / Professional / Leadership
            └─ ROLE TRACK ................ a filter over situations: entry → mid → senior → leadership roles
                 └─ WORKPLACE SITUATION .. a concrete event in that role (e.g. "P1 production incident")
                      └─ COMMUNICATION ... the language functions and frames the situation needs
                           └─ PERFORMANCE  what the learner says, writes or does
                                └─ ASSESSMENT  how performance is checked (rubric, task, capstone)
```

| Layer | What it holds | Where it comes from | Changes per industry? |
|---|---|---|---|
| Universal Core | The skill, its structure, its formula (CF/PAT), its grammar and tone | Existing core lessons | **No** |
| Industry Application | The industry's setting, vocabulary domains, documents, norms and constraints (regulation, safety) | New | Yes |
| Role Track | Who the learner is in the situation and whom they speak to; the role's seniority sets the band | New, per industry | Yes |
| Workplace Situation | One concrete event with participants, stakes and the information available | New | Yes |
| Communication | Target functions, frames ("Could you give me an update on ___?") and slot vocabulary | Frame from the core, slots from the industry | Frames no, slots yes |
| Performance | Spoken, written or interactive output (role-play, email, report, briefing) | New task, using a core output type | Partly |
| Assessment | Rubric criteria: universal (tone, structure, accuracy) + industry (correct terms, policy-safe content, document format) | Universal rubric + industry criteria | Partly |

**Worked example (from the brief):**

| Layer | IT example |
|---|---|
| Universal skill | Giving a professional work update. Core: L2 M1, done/doing/blocked structure. |
| Industry | IT & Technology |
| Role | Software Support Executive (entry) |
| Situation | Updating a manager about a production issue |
| Communication | problem + current status + action + expected resolution ("The payment service has been failing since 10:15. We've rolled back the release and errors are down to 2%. I'll confirm full recovery by 11:00.") |
| Performance | Speak the update in a stand-up; write it as a ticket comment and an email |
| Assessment | Role-play (rubric: structure, clarity, accurate status, tone) + email (format, completeness) + comprehension of an incident log |

**The same universal skill (work update) across industries:**

| Industry | Role | Situation | Update content (problem → status → action → expected outcome) |
|---|---|---|---|
| Hospitality | Front-desk agent | Room not ready for a VIP arrival | Room 305 still being cleaned → housekeeping 15 min away → guest offered lounge → room ready 14:30 |
| Banking | Customer service officer | Account opening held | KYC documents incomplete → customer contacted → new upload requested → account active tomorrow |
| Healthcare | Patient-service executive | Clinic running late | Doctor delayed in surgery → patients informed → rescheduling offered → clinic resumes 16:00 |
| Retail | Floor supervisor | Stock discrepancy | 5 units short on item #2214 → recount done → loss-prevention informed → report by close |
| BPO | Support associate → team leader | Call spike after outage | Queue at 140 calls → callback script live → overflow team added → service level back by 13:00 |
| Aviation | Gate agent | Delayed departure | Aircraft change → passengers informed → meal vouchers issued → new boarding 18:40 |
| Education | Academic coordinator | Exam timetable clash | Two papers on one day → HoDs consulted → revised timetable drafted → circular Friday |
| Logistics | Dispatch coordinator | Shipment held at hub | Consignment missed linehaul → next truck 06:00 → customer notified → delivery Thursday |
| Manufacturing | Line supervisor | Line stoppage | Conveyor fault on line 2 → maintenance on site → output moved to line 3 → restart 15:00 |
| Corporate / Office | Admin executive | Office move | Movers delayed → IT relocation done → desks ready Monday → floor plan circulated |
| Professional services | Consultant | Deliverable slipping | Client data late → analysis 60% done → interim findings Friday → final report next Wednesday |
| Sports management | Event coordinator | Tournament schedule | Rain delay at ground 2 → matches moved to ground 1 → teams and sponsor informed → finals unchanged |
| Tourism | Tour coordinator | Excursion cancelled | Ferry cancelled → alternative city tour booked → guests informed at breakfast → refund difference processed |
| IT | Support executive | Production issue | (worked example above) |

**What the table shows:** the structure, formula, tone and grammar are taught once in the core. The role, the situation, the content slots and some constraints are new for each industry.

### 6.2 Learning cycle (proposed principle, not an existing feature)

For industry lessons: **Learn** (core reference) → **Understand** (situation and constraints) → **Observe** (model dialogue or document) → **Practice** (guided tasks) → **Perform** (role-play, writing) → **Reflect** (self-check against rubric) → **Improve** (redo with feedback).
- The PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION framework stays the planning tool inside "Perform".
- Adopting the cycle as house methodology is an author decision (D-14).

### 6.3 Architecture comparison

**Model A: industry modules inside every existing level**

| Criterion | Assessment |
|---|---|
| Structural impact | High. Changes the content of every level; new modules must be numbered after the existing ones to avoid renumbering. |
| Page-count impact | Grows the single volume at every level |
| Editorial complexity | High. Every level edited; the core's verified state is reopened. |
| Learner usability | Good for in-level practice; noisy for learners outside the chosen industry |
| Scalability | Poor. Each new industry touches 5 levels. |
| Website/app | Possible; the tree gets crowded |
| Future expansion | Each addition reopens the core |
| Assessment | Level assessments must change for every industry |
| Publishing | One ever-growing volume; the core can't be printed stably |
| Code/data | Inside `book-data.json`; breaks the baseline+corrections check unless that model is extended |
| Duplication risk | High (universal teaching repeated next to applications) |

**Model B: separate Part VI "Industry English" after Level 5**

| Criterion | Assessment |
|---|---|
| Structural impact | Medium. The core is unchanged but the book gains a Part VI. |
| Page-count impact | One large appendix-style part |
| Editorial complexity | Medium |
| Learner usability | Weak alignment. A Level 1 learner must jump to the end, and Part VI mixes levels unless banded internally. |
| Scalability | Medium. Part VI grows without limit. |
| Website/app | Simple (one more branch) |
| Future expansion | Adds pages to the same volume |
| Assessment | Separate industry assessments are possible |
| Publishing | One volume, or Part VI split later |
| Code/data | Can be a separate file or a new top-level structure |
| Duplication risk | Medium |

**Model C: core unchanged plus separate Industry Application Tracks**

| Criterion | Assessment |
|---|---|
| Structural impact | Low. The core is unchanged. |
| Page-count impact | Each track is its own product (about 168 pages) |
| Editorial complexity | Medium. Each track is independent. |
| Learner usability | Clear. Choose an industry; each track is banded to core levels. |
| Scalability | High (add tracks) |
| Website/app | Good (industry as a top-level choice) |
| Future expansion | Easy |
| Assessment | Track-level assessments and capstones |
| Publishing | Supplements or digital tracks |
| Code/data | Separate file; core data untouched |
| Duplication risk | Medium. Tracks may re-teach universal skills unless they reference the core. |

**Model D: hybrid (core + Industry Application Modules + Role Tracks)**

| Criterion | Assessment |
|---|---|
| Structural impact | Low. The core is unchanged; modules sit beside it by band. |
| Page-count impact | Same as C (modules per band); the role layer adds data, not pages |
| Editorial complexity | Medium–high. A skill registry (SK IDs) and role taxonomy must be maintained. |
| Learner usability | Clear in both print and digital: core level → band module; digital adds a role filter |
| Scalability | High (add industry modules, roles and situations independently) |
| Website/app | Strong (level → industry → role → situation filters) |
| Future expansion | Easy; industries can start at one band (a module) and grow to a full track |
| Assessment | Universal rubric + industry criteria; reusable capstone engine |
| Publishing | Supports core volume + supplements + digital from one data source |
| Code/data | Separate file + skill registry + role and situation tables |
| Duplication risk | Lowest. Modules must reference core skills, not re-teach them. |

**Trade-offs.**
- A and B keep everything in one place, but they reopen or enlarge the verified core and grow one volume.
- C keeps the core stable but has no role dimension and invites tracks to re-teach universal skills.
- D carries the most design overhead (skill registry, role taxonomy). In return it keeps the core untouched, lets an industry start small (one band) and grow, supports the level → industry → role → situation navigation the brief asks for, and avoids duplication by design.

**Proposed design: Model D (hybrid).** It is the only one of the four that meets all four constraints of the brief at once:
- the core is preserved unchanged;
- coverage claims can be controlled tier by tier;
- it scales to 14 industries;
- it supports print and app from one data source.

Adoption needs author approval (D-01).

## 7. Core vs industry layer

### 7.1 What transfers and what must be taught specifically

| Element | Universal (taught once in the core) | Industry-specific (taught in the application layer) |
|---|---|---|
| Structure | done/doing/blocked; FEAAR report framework; complaint formula; negotiation stages | Industry document formats (BEO, bug report, NCR, PIR, QA form) |
| Formulas (CF/PAT) | Existing CF and PAT codes | Industry frames only where the core has no formula (e.g. read-back protocol) |
| Tone | PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION | Industry norms: clinical neutrality, banking disclosure language, aviation SOP scripts |
| Grammar | Core GIC | None new; industry lessons cite core GIC |
| Vocabulary | Core V (universal workplace) | Domain terms (ticket priority, KYC, admission, POS, consignment) |
| Constraints | — | What staff may say or offer: policy, regulation, safety, privacy |
| Situations | Hotel examples | New industry situations |
| Roles | Arif's front-office path | Industry role taxonomies |

### 7.2 Frame + slot examples

**Frame: "Could you give me an update on ___?"**

| Industry | Slot |
|---|---|
| Universal | this |
| IT | the production incident |
| Hospitality | Room 305 |
| Banking | the customer's KYC verification |
| Healthcare | the patient's registration |
| Retail | today's stock discrepancy |
| BPO | the escalated ticket for this caller |
| Aviation | the replacement aircraft |
| Education | the revised exam timetable |
| Logistics | the consignment held at the hub |
| Manufacturing | line 2's restart |
| Corporate / Office | the office move |
| Professional services | the client's data request |
| Sports management | the ground 2 pitch inspection |
| Tourism | the ferry replacement |

**Frame: "I'm sorry for ___. What I can do right now is ___."**
The structure is universal (core L2 M5, L3 M5). The second slot is industry-constrained:

| Industry | What the second slot can offer |
|---|---|
| Hotel | upgrade |
| Banking | review within policy; never a promise of reversal |
| Healthcare | earliest available appointment; no clinical promise |
| Aviation | rebooking per policy |
| Retail | exchange per returns policy |
| BPO | callback within SLA |

**Frame: "Just to confirm, you'd like me to ___ by ___."**
Universal clarification (L1 M4–M5) becomes **mandatory read-back** in safety-critical settings: a medication-round request in healthcare, a gate change in aviation, lockout before maintenance in manufacturing. There, accuracy is assessed, not tone (assessment category J).

**Frame: "I need to escalate this to ___ because ___."**
Universal (L3 1.5, L4 M6). The industry layer supplies the escalation path:

| Industry | Escalation path |
|---|---|
| IT | P1 bridge |
| BPO | escalation matrix |
| Banking | compliance / grievance officer |
| Healthcare | duty doctor / patient relations |
| Manufacturing | EHS |
| Hotel | duty manager |

**Rule:** an industry lesson never re-teaches a frame. It cites the core lesson and code, and teaches the slot vocabulary, the constraints and the situation.

## 8. Industry Track Framework

The fields are those required by the brief. The roles are curriculum-oriented: those a learner can realistically practise, not complete organisation charts. Industry IDs are proposed (D-09).

**Review flags:**
- **SME** = specialist subject-matter review required.
- **REG** = regulatory or safety-sensitive content.

### HOSP — Hospitality & Hotels

| Field | Definition |
|---|---|
| Purpose | Extend the existing front-office base to the other hotel and F&B roles, so that hospitality becomes a full track rather than one role |
| Target learners | Hotel, resort, restaurant and catering staff; hospitality students |
| Entry roles | Front-desk agent; reservations agent; housekeeping attendant; F&B server; concierge / bell desk |
| Mid roles | Front-office supervisor; housekeeping supervisor; restaurant supervisor / captain; sales & events coordinator |
| Leadership roles | Front-office manager; executive housekeeper; F&B manager; events manager; general manager |
| Core situations | Arrival and check-in/out; guest requests; room readiness; restaurant service; banquet events; group bookings; complaints; shift handover; system outage |
| Vocabulary domains | Room types and status; reservations and rate codes; housekeeping (par, room status); F&B service; banqueting; service recovery; occupancy and ADR basics |
| Communication functions | Welcome; explain services and policy; upsell; apologise and recover; coordinate departments; hand over |
| Document types | Shift log / handover note; guest incident report; banquet event order; rooming list; review response |
| Meeting types | Daily briefing; department-heads meeting; event pre-meeting |
| Customer/client | Walk-in, VIP, group and corporate guests; event clients |
| Internal | Front office ↔ housekeeping ↔ F&B ↔ engineering ↔ sales |
| Conflict/escalation | Overbooking; noise; billing dispute → duty manager |
| Crisis | System outage (core L4 M6); fire alarm and evacuation (SOP language); guest medical emergency (handoff only) |
| Reporting | Daily ops summary; satisfaction report; incident report |
| Presentation | Monthly guest-satisfaction review; proposal to corporate client |
| Negotiation | Corporate and group rates; supplier contracts (core L4 M1) |
| Leadership | Shift leadership; briefing; coaching new staff |
| Assessment | Guest role-plays; handover note and banquet event order; incident report |
| Capstone | Guest complaint → coordinate departments → update supervisor → communicate resolution → document incident |
| Review flags | Light SME; food-safety and evacuation wording to SOP |

### IT — IT & Technology

| Field | Definition |
|---|---|
| Purpose | English for people who build, support and run technology services |
| Target learners | IT support, software development, QA and IT-services staff; IT graduates |
| Entry roles | IT support / helpdesk executive; technical support executive; junior developer; QA executive |
| Mid roles | Team lead; project coordinator; business analyst; service-delivery coordinator |
| Leadership roles | Project manager; engineering manager; head of IT / delivery head |
| Core situations | Ticket handling; user support call; stand-up; bug report; release; production incident; requirements call; code-review feedback |
| Vocabulary domains | Tickets and priority (P1–P4, SLA); environments and releases; defects and testing; incident management; agile ceremonies; requirements |
| Communication functions | Explain technical issues to non-technical users; status; estimate; push back on scope; incident updates |
| Document types | Ticket update; bug report; release note; incident report / post-incident review; requirements email; status report |
| Meeting types | Stand-up; sprint planning, review and retrospective; incident bridge; client requirements call |
| Customer/client | End users; internal business users; external clients |
| Internal | Development ↔ QA ↔ operations ↔ product; onsite ↔ offshore |
| Conflict/escalation | Scope creep; missed SLA; blame after incidents → incident manager |
| Crisis | Production outage; security incident (communication and handoff only, no security advice) |
| Reporting | SLA and ticket metrics; sprint report |
| Presentation | Product demo; project status to stakeholders |
| Negotiation | Scope and timeline trade-offs; vendor SLA |
| Leadership | Delegating; review culture; one-to-ones |
| Assessment | Support-call role-play; bug report and ticket; incident email |
| Capstone | Simulated production incident → investigate information → update manager → write incident email → join escalation meeting → present resolution |
| Review flags | Practitioner review; security content as handoff only |

### BFS — Banking & Finance

| Field | Definition |
|---|---|
| Purpose | English for branch, operations and customer-facing finance roles |
| Target learners | Bank, microfinance and finance-office staff; commerce graduates |
| Entry roles | Customer service officer / teller; account-opening executive; operations executive; collections executive |
| Mid roles | Relationship manager; branch operations manager; credit officer; team lead |
| Leadership roles | Branch manager; area / regional manager; operations head |
| Core situations | Account opening and KYC; explaining fees and charges; transaction disputes; loan enquiries; fraud alerts; complaints within policy; audit requests |
| Vocabulary domains | Accounts and products; KYC/AML (generic); transactions and charges; loans and EMI; grievance redressal; audit and compliance |
| Communication functions | Explain policy and fees clearly; verify identity; decline within policy; disclose accurately; escalate to compliance |
| Document types | Customer letter/email; complaint response; internal memo; audit response; branch report |
| Meeting types | Branch huddle; review with regional manager; audit closing meeting |
| Customer/client | Retail customers; business clients; elderly and vulnerable customers |
| Internal | Branch ↔ operations ↔ compliance ↔ credit |
| Conflict/escalation | Fee reversal; disputed transaction; refused loan → grievance officer / compliance |
| Crisis | Branch system downtime; suspected fraud; cash discrepancy |
| Reporting | Branch performance; discrepancy report |
| Presentation | Branch metrics to regional director |
| Negotiation | Business-client terms within limits |
| Leadership | Team briefings; ethical sales-target conversations |
| Assessment | Disputed-transaction role-play; complaint reply; policy-safe wording check |
| Capstone | Customer transaction dispute → verify → explain policy → escalate → written resolution → branch report |
| Review flags | **SME + REG**: compliance review; jurisdiction-neutral wording (Indian and Bangladeshi rules differ); no financial advice |

### HLTH — Healthcare & Hospitals

The proposed scope is **non-clinical** communication. Clinical content would need clinician authorship (D-07).

| Field | Definition |
|---|---|
| Purpose | English for front-line and administrative healthcare communication |
| Target learners | Hospital and clinic front office, patient services, billing, administration, ward support |
| Entry roles | Patient-service executive / receptionist; admissions or billing executive; ward assistant; medical-records assistant |
| Mid roles | Patient-relations officer; scheduling coordinator; department coordinator; nursing supervisor (communication only) |
| Leadership roles | Department head; hospital administrator; patient-experience manager |
| Core situations | Registration and appointments; waiting times; billing and insurance (TPA) queries; patient and family complaints; handover; confidentiality; discharge paperwork |
| Vocabulary domains | Departments and roles; appointment, admission and discharge; billing and insurance claims; patient privacy; non-clinical safety |
| Communication functions | Empathetic explanation; confidentiality-safe answers; read-back; escalation to clinical staff |
| Document types | Appointment message; complaint response; non-clinical incident report; handover note |
| Meeting types | Department huddle; quality meeting (participant); scheduling meeting |
| Customer/client | Patients; families; insurers / TPAs |
| Internal | Front office ↔ wards ↔ billing ↔ doctors |
| Conflict/escalation | Long waits; billing dispute; visitor rules → patient relations / duty doctor |
| Crisis | Emergency arrival at the front desk (handoff); system outage; major-incident communication (refer to protocol only) |
| Reporting | Incident reporting; patient-feedback summary |
| Presentation | Scheduling-change proposal (an overlay exists, L4 5.1) |
| Negotiation | Limited: insurer queries; service vendors |
| Leadership | Rostering; feedback; change (scheduling system) |
| Assessment | Patient-complaint role-play; read-back accuracy; confidentiality scenario; written response |
| Capstone | Patient-service complaint → non-clinical investigation → coordinate department → reply to family → incident documentation |
| Review flags | **SME + REG**: healthcare-administration and clinician review; no medical advice; privacy wording generic |

### RTL — Retail

| Field | Definition |
|---|---|
| Purpose | English for store and customer-facing retail roles |
| Target learners | Shop-floor, cashier, stock and store-management staff |
| Entry roles | Sales associate; cashier; stock associate; customer-service desk associate |
| Mid roles | Floor / department supervisor; visual merchandiser; store operations coordinator |
| Leadership roles | Store manager; area manager |
| Core situations | Helping shoppers; product questions; returns, refunds and exchanges; stock discrepancies; promotions; shift briefings; shoplifting (handoff to security) |
| Vocabulary domains | Product, size and fit; point of sale and payments; returns policy; stock and inventory; promotions; store operations |
| Communication functions | Assist; recommend; explain policy; refuse politely; brief the team |
| Document types | Stock-discrepancy report; shift handover; customer email; incident report |
| Meeting types | Store huddle; district review |
| Customer/client | Shoppers; online-order customers |
| Internal | Floor ↔ stockroom ↔ cash office ↔ area manager |
| Conflict/escalation | Refund dispute; price match; queues → store manager |
| Crisis | Point-of-sale outage; safety incident; stock-out at peak |
| Reporting | Daily sales and stock report |
| Presentation | Monthly store review |
| Negotiation | Supplier and price discussions (store level) |
| Leadership | Rota; briefing; coaching |
| Assessment | Refund role-play; discrepancy report; team briefing |
| Capstone | Customer refund dispute → policy check → offer → escalate to manager → document → team briefing |
| Review flags | Light SME; consumer-law statements generic |

### BPO — BPO & Contact Centre

| Field | Definition |
|---|---|
| Purpose | Voice, chat and email customer support in outsourced and in-house contact centres |
| Target learners | Contact-centre agents and applicants; team leaders |
| Entry roles | Customer support associate (voice / chat / email); telecaller; technical support associate |
| Mid roles | Team leader; quality analyst; process trainer; real-time / workforce analyst |
| Leadership roles | Operations manager; process head |
| Core situations | Inbound call opening and verification; troubleshooting; hold and transfer; de-escalation; outbound calls; chat and email tickets; quality feedback; client governance call |
| Vocabulary domains | Call flow; verification; AHT, FCR, CSAT, quality; escalation matrix; SOP; adherence |
| Communication functions | Natural opening and closing; empathy statements; accurate information; compliance disclosures; clarity of speech |
| Document types | Ticket notes; chat and email replies; quality feedback form; escalation email; client performance report |
| Meeting types | Team huddle; calibration session; client governance call |
| Customer/client | End customers on behalf of a client; the client process owner |
| Internal | Agent ↔ team leader ↔ quality ↔ client |
| Conflict/escalation | Angry and repeat callers; quality-score disputes → team leader / escalation desk |
| Crisis | Outage-driven call spike; data-protection breach (handoff) |
| Reporting | Daily metrics; client report |
| Presentation | Monthly business review to the client |
| Negotiation | Targets and staffing with the client |
| Leadership | Floor management; coaching from call recordings |
| Assessment | Recorded-call role-play against a quality rubric (**needs audio** for listening); chat/email replies |
| Capstone | Escalated customer interaction → de-escalate → resolve or escalate → ticket and escalation note → quality feedback session |
| Review flags | SME; data-protection and call-recording compliance. Overlaps with core L2 M3, L2 M7 and L3 M5, which must be cited, not repeated. |

### AVN — Aviation (ground and cabin service)

**Scope boundary:** pilot and air-traffic radiotelephony is regulated (ICAO language-proficiency requirements). It is **excluded**, and no regulatory or proficiency claim may be made.

| Field | Definition |
|---|---|
| Purpose | Passenger-service English for airport and airline service roles |
| Target learners | Airport customer-service, ground-handling and cabin-crew applicants and staff |
| Entry roles | Check-in / customer-service agent; gate agent; baggage-services agent; cabin crew (service communication) |
| Mid roles | Duty officer; customer-service supervisor; senior cabin crew (service communication) |
| Leadership roles | Station / airport-services manager; customer-experience manager |
| Core situations | Check-in and baggage; delay and cancellation; boarding; special assistance; mishandled baggage; onboard service; disruptive passenger (service level) |
| Vocabulary domains | Flight status; baggage; boarding; rebooking; special assistance; announcements (scripted to SOP) |
| Communication functions | Inform; announce; reassure; rebook; refuse within policy; read back |
| Document types | Baggage irregularity report; incident report; passenger email; shift handover |
| Meeting types | Pre-shift / pre-flight briefing; debrief |
| Customer/client | Passengers; passengers needing assistance; groups |
| Internal | Check-in ↔ gate ↔ ramp ↔ operations control ↔ cabin |
| Conflict/escalation | Denied boarding; excess baggage; disruption anger → duty officer |
| Crisis | Irregular operations; onboard medical event (handoff); evacuation communication (SOP only) |
| Reporting | Shift report; irregularity report |
| Presentation | On-time performance and service review |
| Negotiation | Minimal (ground-handling coordination) |
| Leadership | Shift briefing; coaching agents |
| Assessment | Disruption role-play; announcement delivery (**needs audio**); irregularity report |
| Capstone | Passenger service disruption → announce → rebook and assist → handle complaint → incident report → debrief |
| Review flags | **SME + REG**; safety scripts must come from official SOP; no certification claim |

### EDU — Education

| Field | Definition |
|---|---|
| Purpose | English for teachers', school administrators' and education-services communication |
| Target learners | School and college staff; coaching and edtech support staff |
| Entry roles | Teaching assistant; admin / coordinator executive; admissions counsellor; edtech student-support executive |
| Mid roles | Teacher / subject lead; academic coordinator; admissions manager |
| Leadership roles | Principal / head; academic director |
| Core situations | Parent communication; student issues; admissions enquiries; cover and timetable changes; grading delays; parent-teacher meetings |
| Vocabulary domains | Curriculum and assessment; admissions; attendance; parent communication; safeguarding (generic) |
| Communication functions | Explain; reassure; set boundaries; report concerns; chair meetings |
| Document types | Parent letter/email; report-card comment; circular; minutes; concern referral (handoff) |
| Meeting types | Staff meeting; parent-teacher meeting; academic council |
| Customer/client | Parents; students; applicants |
| Internal | Teachers ↔ coordinators ↔ administration ↔ principal |
| Conflict/escalation | Grade disputes; parent complaints → coordinator / principal |
| Crisis | Student safety incident (protocol handoff); exam disruption |
| Reporting | Attendance and results summaries |
| Presentation | Parent orientation; results review |
| Negotiation | Timetabling; resources |
| Leadership | Staff feedback; change (new curriculum) |
| Assessment | Parent-meeting role-play; parent email; circular |
| Capstone | Parent/student complaint → listen → investigate → meeting → written follow-up → staff briefing |
| Review flags | SME; **REG** for child-safeguarding content |

### TRV — Tourism & Travel

| Field | Definition |
|---|---|
| Purpose | English for travel agencies, tour operations and guiding |
| Target learners | Travel consultants, tour guides and reservations staff |
| Entry roles | Travel consultant; tour guide; reservations executive; travel-desk executive |
| Mid roles | Tour-operations coordinator; corporate travel account manager; team lead |
| Leadership roles | Operations manager; agency / branch head |
| Core situations | Enquiries and itineraries; bookings and changes; document reminders (no visa advice); guiding groups; disruption and rebooking; complaints; supplier coordination |
| Vocabulary domains | Itineraries and packages; inclusions and exclusions; cancellation policy; documentation; group handling |
| Communication functions | Advise; describe; confirm; manage expectations; apologise and rebook |
| Document types | Itinerary; quotation; booking confirmation; complaint reply; supplier email |
| Meeting types | Tour briefing; supplier review |
| Customer/client | Leisure travellers; corporate travellers; groups |
| Internal | Sales ↔ operations ↔ guides ↔ suppliers |
| Conflict/escalation | Overbooking; service failures → operations manager |
| Crisis | Weather or strike disruption; lost traveller or documents; medical event (handoff) |
| Reporting | Tour report; supplier performance |
| Presentation | Package proposal to a corporate client |
| Negotiation | Supplier rates; group terms |
| Leadership | Guide briefing; seasonal staffing |
| Assessment | Itinerary consultation role-play; quotation and itinerary writing |
| Capstone | Tour disruption → inform group → rebook with suppliers → handle complaint → written follow-up → supplier review |
| Review flags | Light SME; visa and immigration statements generic. Overlaps with HOSP and AVN. |

### LOG — Logistics & Supply Chain

| Field | Definition |
|---|---|
| Purpose | English for logistics, warehousing and procurement operations |
| Target learners | Logistics, warehouse, transport and procurement staff |
| Entry roles | Dispatch / logistics coordinator; warehouse associate; shipment-tracking customer service; procurement assistant |
| Mid roles | Warehouse supervisor; transport planner; buyer / procurement executive; supply-chain analyst |
| Leadership roles | Warehouse / operations manager; supply-chain manager; procurement head |
| Core situations | Tracking enquiries; delays; dispatch coordination; inventory discrepancies; supplier follow-up; purchase orders; customs paperwork (generic) |
| Vocabulary domains | Shipment and consignment; proof of delivery, ETA/ETD; stock terms; purchase order, goods-received note, invoice; incoterms (introduction only) |
| Communication functions | Inform about status; chase; negotiate dates; report discrepancies |
| Document types | Delay notification; purchase-order follow-up; discrepancy report; carrier claim |
| Meeting types | Daily operations call; supplier review; sales and operations planning (participant) |
| Customer/client | B2B customers; consignees |
| Internal | Warehouse ↔ transport ↔ procurement ↔ sales |
| Conflict/escalation | Missed delivery; short shipment → operations manager |
| Crisis | Major disruption; warehouse safety incident (handoff) |
| Reporting | On-time-in-full metrics; root-cause report |
| Presentation | Supplier performance review |
| Negotiation | Freight rates; supplier lead times (core L4 M1 transfers) |
| Leadership | Shift planning; safety briefing |
| Assessment | Delay-call role-play; delay email; discrepancy report |
| Capstone | Delayed shipment → investigate status → inform customer → coordinate carrier/supplier → written update → root-cause report |
| Review flags | SME; dangerous goods and customs out of scope unless a specialist reviews |

### MFG — Manufacturing

| Field | Definition |
|---|---|
| Purpose | English for production, quality and maintenance communication |
| Target learners | Shop-floor supervisors, quality and maintenance staff, engineers |
| Entry roles | Production operator (communication); quality inspector; maintenance technician; materials assistant |
| Mid roles | Shift / line supervisor; quality engineer; production planner; EHS officer |
| Leadership roles | Plant / production manager; quality manager; operations head |
| Core situations | Shift handover; safety briefing; defects; breakdown reporting; production targets; customer quality complaints; audits |
| Vocabulary domains | Lines and shifts; defects and non-conformance; maintenance and breakdown; safety and PPE; quality systems (generic) |
| Communication functions | Report accurately; read back; brief on safety; escalate; explain root cause |
| Document types | Shift log; non-conformance / defect report; maintenance request; corrective-action summary; safety observation |
| Meeting types | Start-of-shift meeting; quality review; audit opening and closing |
| Customer/client | B2B customers' quality teams; auditors |
| Internal | Production ↔ quality ↔ maintenance ↔ planning ↔ EHS |
| Conflict/escalation | Target versus quality; shift blame → plant manager |
| Crisis | Safety incident (protocol); line stoppage; recall (internal communication) |
| Reporting | Daily production report; quality report |
| Presentation | Monthly quality review to customer |
| Negotiation | Delivery schedules; supplier quality terms |
| Leadership | Toolbox talks; coaching operators |
| Assessment | Handover role-play with read-back; non-conformance report; safety briefing |
| Capstone | Production-quality issue → report defect → contain and escalate → customer communication → corrective-action report → team briefing |
| Review flags | **SME + REG**; EHS review mandatory for safety content |

### CORP — Corporate / Office

| Field | Definition |
|---|---|
| Purpose | Office-function roles (administration, HR, finance office, operations). The core already serves the general office context, so the risk of duplication is highest here. |
| Target learners | Office staff in any sector |
| Entry roles | Admin / office executive; HR executive; accounts executive; executive assistant |
| Mid roles | Office manager; HR generalist / recruiter; project coordinator |
| Leadership roles | Department head; HR, finance or operations manager |
| Core situations | Scheduling; internal requests; HR and policy queries; expense and invoice queries; onboarding; policy change |
| Vocabulary domains | Office administration; HR processes (generic); expenses and invoices; facilities |
| Communication functions | Coordinate; inform; explain policy; chase |
| Document types | Memo; minutes; policy notice; HR letter (generic); expense query |
| Meeting types | Team meeting; all-hands; interview panel |
| Customer/client | Internal customers; visitors |
| Internal | Cross-department |
| Conflict/escalation | Policy disputes; resource conflicts |
| Crisis | Office closure; IT outage (user side) |
| Reporting | Monthly function report |
| Presentation | Policy briefing |
| Negotiation | Vendors; budgets (overlay exists: internal budget) |
| Leadership | Core L5 applies directly |
| Assessment | Policy-announcement task; memo; HR query role-play |
| Capstone | Office policy change → plan communication → announce → handle questions and resistance → follow-up report |
| Review flags | Generic HR and legal wording; may be best served as a **role layer** rather than a full track (D-04) |

### PROF — Professional Services

| Field | Definition |
|---|---|
| Purpose | English for consulting, audit/accounting firms, legal support and agencies |
| Target learners | Analysts, associates, account and project staff |
| Entry roles | Analyst / associate; client-service executive; legal assistant (communication); audit associate |
| Mid roles | Consultant / senior associate; account manager; project manager |
| Leadership roles | Engagement manager / partner; practice head |
| Core situations | Client kickoff; requirements; status reporting; scope change; deliverable review; billing queries; proposals |
| Vocabulary domains | Engagements and statements of work; deliverables; billing; proposals; governance |
| Communication functions | Clarify scope; report status; push back; recommend; present findings |
| Document types | Proposal; statement-of-work summary; status report; executive summary; minutes |
| Meeting types | Kickoff; steering committee; deliverable review |
| Customer/client | B2B clients and stakeholders |
| Internal | Engagement team ↔ partners ↔ specialists |
| Conflict/escalation | Scope creep; fee disputes → engagement manager |
| Crisis | Missed deadline; data error in a deliverable |
| Reporting | Status and executive reports |
| Presentation | Findings to a steering committee (core L5 M6 transfers) |
| Negotiation | Scope and fees (core L4 M1) |
| Leadership | Staffing; feedback |
| Assessment | Steering-committee presentation; executive summary; scope-change negotiation |
| Capstone | Client scope-change dispute → meeting → negotiate → written change summary → executive presentation |
| Review flags | SME for legal-support and audit wording |

### SPRT — Sports & Sports Management

Cricket is a **context pack** within this industry (section 8.1).

| Field | Definition |
|---|---|
| Purpose | English for sports administration, events, academies and club operations |
| Target learners | Sports-event, club, academy and sponsorship staff |
| Entry roles | Event coordinator; club / academy administrator; ticketing and fan-service executive; junior coach (communication) |
| Mid roles | Team / club manager; event manager; sponsorship executive; academy head coach |
| Leadership roles | Sports-operations manager; club / academy director |
| Core situations | Fixtures and scheduling; sponsor communication; player and parent communication (academies); basic media requests; venue coordination; fan complaints |
| Vocabulary domains | Fixtures and venues; registration; sponsorship deliverables; match-day operations; the cricket context pack (nets, selection, match officials, rain rules: generic) |
| Communication functions | Schedule; inform; negotiate; handle complaints; brief teams |
| Document types | Event brief; sponsor report; schedule notice; incident report |
| Meeting types | Match-day briefing; sponsor review; club committee |
| Customer/client | Sponsors; fans; parents; players |
| Internal | Operations ↔ coaching ↔ commercial ↔ venue |
| Conflict/escalation | Selection disputes (academy); sponsor-visibility disputes |
| Crisis | Weather postponement; injury (handoff); security incident (handoff) |
| Reporting | Sponsor activation report; event report |
| Presentation | Sponsorship proposal |
| Negotiation | Sponsorship terms; venue hire |
| Leadership | Volunteer and staff briefings |
| Assessment | Sponsor-call role-play; sponsor report; match-day briefing |
| Capstone | Sponsor/event communication problem → assess → inform stakeholders → negotiate remedy → written sponsor report → present |
| Review flags | SME; **REG** for safeguarding in academies with minors |

### 8.1 Cricket

**Cricket is not proposed as an independent industry.**
- The book has no cricket content (0 occurrences).
- Cricket workplace communication (academy administration, club operations, match-day operations, sponsorship) uses the same communicative functions, documents and roles as sports management. Only the vocabulary and settings differ.
- **Proposed design:** a **cricket context pack** inside SPRT. These are situation and vocabulary variants (e.g. "rain delay at a club fixture", "academy selection feedback to a parent") that reuse SPRT lessons.
- Promoting cricket to its own track would need evidence of distinct communicative events. Not doing so is an author decision (D-08).

### 8.2 Factual classification of industries (no ranking)

| Industry | Current evidence | Current coverage | Expansion required | Content complexity | Role diversity | Document complexity | Scenario diversity | Review category |
|---|---|---|---|---|---|---|---|---|
| HOSP | Existing strong base | Level 3 (one role) | Other roles; documents; assessment | Moderate | High | Moderate | High | Light SME |
| IT | Existing overlay base | Level 2 | Substantial new content | High (technical) | High | High | High | Practitioner review |
| BFS | Existing overlay base | Level 2 | Substantial new content | High | Moderate | High | Moderate | Specialist consultation + regulatory review |
| HLTH | Existing overlay base | Level 2 | Substantial new content | High | High | Moderate | High | Specialist consultation + regulatory/safety review |
| RTL | Existing overlay base | Level 2 | Substantial new content | Moderate | Moderate | Low | Moderate | Light SME |
| CORP | Existing overlay base (generic) | Level 2 | Moderate (much transfers from core) | Low | Moderate | Moderate | Moderate | Light |
| LOG | Limited overlay base | Level 2 | Substantial new content | Moderate | Moderate | Moderate | Moderate | Specialist consultation |
| PROF | Limited overlay base | Level 2 | Substantial new content | Moderate | Moderate | High | Moderate | Specialist consultation |
| EDU | Limited overlay base | Level 2 | Substantial new content | Moderate | Moderate | Moderate | Moderate | Safeguarding review |
| TRV | Limited overlay base | Level 2 | Substantial new content | Moderate | Moderate | Moderate | High | Light SME |
| BPO | Effectively no base | Level 2 (2 lines) | Substantial new content; audio needed | Moderate | Moderate | Moderate | Moderate | Specialist consultation (data protection) |
| AVN | No base | Level 1 | Substantial new content; audio needed | High | Moderate | Moderate | Moderate | Specialist consultation + regulatory/safety review |
| SPRT | No base | Level 1 | Substantial new content | Moderate | Moderate | Low | Moderate | Safeguarding review (academies) |
| MFG | No base | — | Substantial new content | High | Moderate | High | Moderate | Specialist consultation + regulatory/safety review |

## 9. Role framework

### 9.1 Tiers and bands

| Tier | Meaning | Industry band | Aligned core levels | Proposed CEFR band (section 18) |
|---|---|---|---|---|
| **E** Entry | Front-line role; follows procedures; serves customers; reports upward | Entry band | L1–L2 | A2+ → B1 |
| **M** Mid | Supervises a shift or function; coordinates; writes reports; handles escalations | Professional band | L3–L4 | B1+ → B2 |
| **S** Senior | Manages a unit; negotiates; presents to management; owns incidents | Professional (upper) / Leadership band | L4–L5 | B2 → C1 |
| **L** Leadership | Leads people and change; sets direction; represents the organisation | Leadership band | L5 | C1 |

Rules:
- A role belongs to one tier.
- Situations are tagged with the tiers that meet them; a complaint, for example, is met at E, M and S.
- The role layer is a **filter**: selecting a role shows the situations tagged for that role. It does not create separate lessons for every role.
- This keeps the taxonomy curriculum-sized. Each industry has 3–5 roles per tier, chosen because each has distinct communicative events.

### 9.2 Role taxonomy (all 14 industries)

| Industry | E — Entry | M — Mid | S — Senior | L — Leadership |
|---|---|---|---|---|
| HOSP | Front-desk agent; reservations agent; housekeeping attendant; F&B server; concierge | Front-office supervisor; housekeeping supervisor; restaurant supervisor; events coordinator | Front-office manager; executive housekeeper; F&B manager; events manager | General manager |
| IT | IT support executive; technical support executive; junior developer; QA executive | Team lead; project coordinator; business analyst | Project manager; engineering manager; department head | Technology manager; head of IT |
| BFS | Customer service officer / teller; account-opening executive; operations executive; collections executive | Relationship manager; credit officer; team lead | Branch manager; branch operations manager | Area / regional manager; operations head |
| HLTH | Patient-service executive; admissions/billing executive; ward assistant; records assistant | Patient-relations officer; scheduling coordinator; department coordinator | Department head; nursing supervisor (communication) | Hospital administrator; patient-experience manager |
| RTL | Sales associate; cashier; stock associate; customer-service desk | Floor supervisor; visual merchandiser; operations coordinator | Store manager | Area manager |
| BPO | Support associate (voice/chat/email); telecaller; technical support associate | Team leader; quality analyst; trainer; real-time analyst | Operations manager | Process head |
| AVN | Check-in agent; gate agent; baggage-services agent; cabin crew (service) | Duty officer; customer-service supervisor; senior cabin crew | Station / airport-services manager | Customer-experience manager |
| EDU | Teaching assistant; admin coordinator; admissions counsellor; student-support executive | Teacher / subject lead; academic coordinator | Admissions manager; vice-principal | Principal; academic director |
| TRV | Travel consultant; tour guide; reservations executive | Tour-operations coordinator; corporate travel account manager | Operations manager | Agency / branch head |
| LOG | Dispatch coordinator; warehouse associate; tracking customer service; procurement assistant | Warehouse supervisor; transport planner; buyer | Warehouse / operations manager | Supply-chain manager; procurement head |
| MFG | Operator (communication); quality inspector; maintenance technician; materials assistant | Line supervisor; quality engineer; planner; EHS officer | Production manager; quality manager | Plant manager; operations head |
| CORP | Admin executive; HR executive; accounts executive; executive assistant | Office manager; HR generalist / recruiter; project coordinator | Department head | Function head (HR / finance / operations) |
| PROF | Analyst / associate; client-service executive; legal assistant; audit associate | Consultant; account manager | Project manager; engagement manager | Partner; practice head |
| SPRT | Event coordinator; club administrator; fan-service executive; junior coach | Team / club manager; event manager; sponsorship executive | Head coach / academy head; operations manager | Club / academy director |

### 9.3 Characters

Arif stays the core protagonist and is not changed. How industry modules present characters is author decision D-05. The options are:
- (a) a new protagonist per industry;
- (b) an ensemble of colleagues connected to Arif's world (e.g. the hotel's IT vendor, a guest who is a bank manager);
- (c) no fixed protagonist: the learner takes the role.

## 10. Universal skill matrix

The **skill registry**: each universal skill gets a stable ID (SK-nn) that industry content links to. The links point to existing core lessons and never change them.

**Domains:**
- D1 Self, role and orientation
- D2 Instructions, requests and clarification
- D3 Updates, problems and spoken reporting
- D4 Customer / client / service-user interaction and complaints
- D5 Escalation, incidents and crisis
- D6 Workplace writing and documents
- D7 Meetings and presentations
- D8 Negotiation, persuasion and disagreement
- D9 People leadership

**Bands:**
- E = Entry (core L1–L2)
- P = Professional (core L3–L4)
- L = Leadership (core L5)

**Transfer categories** (G/H/I/J) are as in the baseline audit.

| ID | Universal skill | Domain | Band | Core location (existing) | Transfer | Industry layer must add |
|---|---|---|---|---|---|---|
| SK-01 | Introducing yourself | D1 | E | L1 M1 (1.3), L1 M2 | H | Role descriptions, workplace setting |
| SK-02 | Giving a work update | D3 | E–P | L2 M1 | H | Status vocabulary (ticket, account, patient, consignment) |
| SK-03 | Asking for clarification | D2 | E | L1 M5; L1 4.4 | G (J where safety-critical) | Read-back protocol in HLTH, AVN, MFG |
| SK-04 | Giving instructions | D2/D9 | P–L | L5 M1 | G (J where safety-critical) | Procedure and safety language |
| SK-05 | Making requests | D2 | E | L1 7.2; L2 M2 | G | Situations only |
| SK-06 | Making suggestions | D7 | P | L3 3.3; L4 4.2 | G | Situations only |
| SK-07 | Handling a customer | D4 | E | L2 M7 | I | Customer type, service norms |
| SK-08 | Handling a complaint | D4 | E–P | L2 7.4; L3 M5; L3 1.4 | I | Remedies allowed by policy or regulation |
| SK-09 | Apologising professionally | D4 | E | L2 M5 | G | Liability-safe wording (BFS, HLTH, AVN) |
| SK-10 | Explaining a problem | D3 | E–P | L2 1.2; L4 4.1 | H | Problem types |
| SK-11 | Escalating an issue | D5 | P | L3 1.5; L3 5.4; L4 M6 | J | Escalation paths and matrices |
| SK-12 | Writing an email | D6 | P | L3 M1 | H | Content; compliance language |
| SK-13 | Writing a report | D6 | P | L3 M2 | J | Industry document formats |
| SK-14 | Joining a meeting | D7 | P | L3 3.3–3.4 | G | Meeting types |
| SK-15 | Leading a meeting | D7 | L | L3 3.2, 3.5; L5 M5 | G | Meeting types |
| SK-16 | Giving a presentation | D7 | P–L | L3 M4; L4 M5; L5 M6 | H/G | Industry metrics |
| SK-17 | Negotiating | D8 | P | L4 M1 | H | Terms (SLA, rate, scope, tariff) |
| SK-18 | Handling disagreement | D8 | P | L3 3.3; L4 M2 | G | Situations only |
| SK-19 | Giving feedback | D9 | P–L | L4 2.2; L5 M2 | G | Performance norms (quality scores, KPIs) |
| SK-20 | Receiving feedback | D9 | P | L4 2.3 | G | Situations only |
| SK-21 | Delegating | D9 | L | L5 M1 | G | Situations only |
| SK-22 | Coaching | D9 | L | L5 M3 | G | Situations only |
| SK-23 | Managing conflict | D9 | P–L | L4 2.5–2.6 | G | Situations only |
| SK-24 | Handling a crisis | D5 | P–L | L4 M6 | J | Protocols; regulated and safety communication |
| SK-25 | Communicating decisions | D9 | L | L4 4.3; L5 5.3 | G | Situations only |

## 11. Industry application matrix

**Layout:** for each universal skill, the *language function* and *output* are universal and stated once. The table then gives each industry's **role** and **workplace situation**. The output column states only industry-specific outputs; where it is blank, the universal output applies.

### SK-01 Introducing yourself
**Function:** state name, role, background and what you can help with.
**Output:** spoken self-introduction and written intro message.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Housekeeping attendant | First briefing with the housekeeping team |
| IT | Junior developer | Joining a sprint team's stand-up |
| BFS | Customer service officer | Meeting the branch team on day one |
| HLTH | Patient-service executive | Introducing yourself to the ward coordinator |
| RTL | Sales associate | Store huddle on the first shift |
| BPO | Support associate | First day on the floor with the team leader |
| AVN | Check-in agent | Pre-shift briefing at the counter |
| EDU | Teaching assistant | Introduction at the staff meeting |
| TRV | Tour guide | Introducing yourself to a tour group |
| LOG | Dispatch coordinator | First call with a carrier's control room |
| MFG | Quality inspector | Start-of-shift meeting on the line |
| CORP | HR executive | New-joiner email to department heads |
| PROF | Analyst | Client kickoff meeting |
| SPRT | Event coordinator | Venue walk-through with the ground staff |

### SK-02 Giving a work update
**Function:** problem / status → action → expected outcome.
**Output:** spoken update plus written update (email, ticket or chat).

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-desk agent | Room not ready for a VIP arrival |
| IT | Support executive | Production issue update to the manager |
| BFS | Account-opening executive | KYC-held account update |
| HLTH | Scheduling coordinator | Clinic running late |
| RTL | Floor supervisor | Stock discrepancy before close |
| BPO | Team leader | Queue spike after an outage |
| AVN | Gate agent | Aircraft change and new boarding time |
| EDU | Academic coordinator | Exam timetable clash |
| TRV | Tour coordinator | Excursion cancelled, alternative booked |
| LOG | Dispatch coordinator | Consignment held at the hub |
| MFG | Line supervisor | Line stoppage and restart time |
| CORP | Admin executive | Office move progress |
| PROF | Consultant | Deliverable slipping because of late client data |
| SPRT | Event coordinator | Rain delay and moved fixtures |

### SK-03 Asking for clarification
**Function:** check meaning, numbers and responsibility; read back critical details.
**Output:** clarification question and read-back.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Reservations agent | Group booking with unclear room split |
| IT | QA executive | Ambiguous acceptance criteria |
| BFS | Operations executive | Unclear transfer instruction from a branch |
| HLTH | Ward assistant | Read back a non-clinical instruction (bed transfer time) |
| RTL | Stock associate | Unclear restock priority |
| BPO | Support associate | Caller's account details unclear |
| AVN | Gate agent | Read back a gate or stand change from operations |
| EDU | Teaching assistant | Unclear cover instructions |
| TRV | Travel consultant | Client's dates and flexibility unclear |
| LOG | Warehouse associate | Pick list with conflicting quantities |
| MFG | Maintenance technician | Read back the isolation/lockout step before work |
| CORP | Executive assistant | Ambiguous meeting request |
| PROF | Associate | Scope of a client data request |
| SPRT | Club administrator | Unclear registration deadline |

### SK-04 Giving instructions
**Function:** clear steps, sequence and checkpoints; confirm understanding.
**Output:** spoken briefing plus written checklist.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Housekeeping supervisor | Allocating rooms for a group checkout |
| IT | Team lead | Instructions for a release window |
| BFS | Branch operations manager | New cash-handling step |
| HLTH | Department coordinator | New appointment-booking procedure |
| RTL | Store manager | Promotion setup for the weekend |
| BPO | Trainer | New process update to agents |
| AVN | Duty officer | Disruption handling steps for agents |
| EDU | Academic coordinator | Exam invigilation instructions |
| TRV | Operations manager | Guide briefing for a new route |
| LOG | Warehouse supervisor | Peak-day picking plan |
| MFG | Line supervisor | Toolbox talk on a changeover |
| CORP | Office manager | Visitor-registration procedure |
| PROF | Project manager | Work allocation for a client deliverable |
| SPRT | Event manager | Match-day steward briefing |

### SK-05 Making requests
**Function:** polite, specific request with reason and deadline.
**Output:** spoken request plus message or email.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-desk agent | Ask housekeeping to prioritise a room |
| IT | Developer | Ask for test data from QA |
| BFS | Relationship manager | Ask operations to expedite a client request |
| HLTH | Patient-service executive | Ask billing for an estimate |
| RTL | Sales associate | Ask the stockroom for a size |
| BPO | Agent | Ask the team leader for an approval |
| AVN | Check-in agent | Ask ramp for baggage status |
| EDU | Teacher | Ask the coordinator for a room change |
| TRV | Consultant | Ask a hotel supplier for a late checkout |
| LOG | Buyer | Ask a supplier for an earlier dispatch |
| MFG | Planner | Ask maintenance for a slot |
| CORP | Accounts executive | Ask a manager to approve expenses |
| PROF | Associate | Ask the client for documents |
| SPRT | Sponsorship executive | Ask the venue for branding access |

### SK-06 Making suggestions
**Function:** propose an option with reason and trade-off.
**Output:** spoken suggestion in a meeting plus short proposal.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Restaurant supervisor | Suggest a breakfast queue change |
| IT | Business analyst | Suggest splitting a requirement |
| BFS | Team lead | Suggest an appointment slot system |
| HLTH | Scheduling coordinator | Suggest an SMS reminder to cut no-shows |
| RTL | Visual merchandiser | Suggest a display move |
| BPO | Quality analyst | Suggest a script change |
| AVN | Customer-service supervisor | Suggest pre-boarding announcements |
| EDU | Subject lead | Suggest a revision timetable |
| TRV | Coordinator | Suggest a rain-day alternative |
| LOG | Transport planner | Suggest consolidating loads |
| MFG | Quality engineer | Suggest an inspection checkpoint |
| CORP | Office manager | Suggest a hot-desk rota |
| PROF | Consultant | Suggest a phased delivery |
| SPRT | Event manager | Suggest staggered gate opening |

### SK-07 Handling a customer
**Function:** welcome, identify the need, inform, confirm, close.
**Output:** service interaction role-play; written reply.

| Industry | Role | Situation | Industry-specific output |
|---|---|---|---|
| HOSP | Front-desk agent | Walk-in guest asking about rates | |
| IT | Support executive | User cannot log in | Ticket note |
| BFS | Customer service officer | Customer asking about charges | |
| HLTH | Patient-service executive | Patient booking a follow-up | |
| RTL | Sales associate | Shopper choosing a product | |
| BPO | Support associate | Inbound billing query | Ticket notes |
| AVN | Check-in agent | Passenger with excess baggage | |
| EDU | Admissions counsellor | Parent enquiry about admission | |
| TRV | Travel consultant | Couple planning a holiday | Itinerary |
| LOG | Tracking customer service | Customer asking where a parcel is | |
| MFG | Customer quality contact | Customer asking about order status | |
| CORP | Admin executive | Visitor at reception | |
| PROF | Client-service executive | Client billing question | |
| SPRT | Fan-service executive | Ticket enquiry | |

### SK-08 Handling a complaint
**Function:** listen → acknowledge → own → offer what policy allows → confirm → follow up.
**Output:** complaint role-play plus written response.

| Industry | Role | Situation (remedy constraint) |
|---|---|---|
| HOSP | Front-office supervisor | Billing error (refund / goodwill allowed) |
| IT | Service-delivery coordinator | Missed SLA on a client ticket (service credit per contract) |
| BFS | Customer service officer | Transaction dispute (no promise of reversal; grievance process) |
| HLTH | Patient-relations officer | Long wait and rude-staff complaint (no clinical judgement) |
| RTL | Customer-service desk | Refund outside the return window (policy exception via manager) |
| BPO | Support associate | Repeat caller angry about an unresolved issue (escalation matrix) |
| AVN | Customer-service agent | Missed connection (rebooking per policy) |
| EDU | Coordinator | Parent disputes a grade (review process) |
| TRV | Consultant | Hotel not as described (supplier claim) |
| LOG | Customer service | Damaged delivery (claim process) |
| MFG | Quality engineer | Customer reports a defective batch (corrective-action process) |
| CORP | HR executive | Employee complaint about a payroll error |
| PROF | Account manager | Client unhappy with deliverable quality |
| SPRT | Fan-service executive | Fan complaint about seating |

### SK-09 Apologising professionally
**Function:** specific apology + responsibility + repair + prevention, using liability-safe wording where required.
**Output:** spoken and written apology.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-desk agent | Wrong room number sent to the airport driver |
| IT | Developer | Your change broke the build |
| BFS | Operations executive | Delayed processing of a request |
| HLTH | Receptionist | Appointment double-booked |
| RTL | Cashier | Wrong change given |
| BPO | Agent | Wrong information given on an earlier call |
| AVN | Gate agent | Boarding announcement error |
| EDU | Teacher | Delay returning marked work |
| TRV | Consultant | Itinerary sent with wrong dates |
| LOG | Coordinator | Missed pickup |
| MFG | Line supervisor | Shipped quantity short |
| CORP | Executive assistant | Calendar clash for an executive |
| PROF | Associate | Error in client report figures |
| SPRT | Event coordinator | Sponsor logo missing from a banner |

### SK-10 Explaining a problem
**Function:** what happened → impact → cause (known/unknown) → next step.
**Output:** spoken explanation plus a short written summary.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-office supervisor | Keycard encoder failing |
| IT | Support executive | Intermittent payment errors |
| BFS | Teller | Cash counter discrepancy |
| HLTH | Billing executive | Insurance pre-authorisation delayed |
| RTL | Store operations coordinator | Point-of-sale terminal faults |
| BPO | Technical support associate | Customer's router fault diagnosis |
| AVN | Baggage agent | Bag missed a connection |
| EDU | Edtech support | Student cannot submit an assignment |
| TRV | Coordinator | Supplier overbooked rooms |
| LOG | Transport planner | Truck breakdown en route |
| MFG | Maintenance technician | Recurring machine fault |
| CORP | Admin executive | Meeting-room booking system down |
| PROF | Consultant | Client data inconsistent |
| SPRT | Club manager | Pitch unfit for play |

### SK-11 Escalating an issue
**Function:** why now, to whom, what you have done, what you need.
**Output:** escalation message plus call.

| Industry | Role | Situation (escalation path) |
|---|---|---|
| HOSP | Front-desk agent | Guest threatens a review over noise (duty manager) |
| IT | Support executive | P1 outage (incident bridge) |
| BFS | Customer service officer | Suspected fraud (fraud / compliance team) |
| HLTH | Receptionist | Patient deteriorating in the waiting area (clinical staff immediately) |
| RTL | Sales associate | Suspected shoplifting (security / manager) |
| BPO | Agent | Legal threat from a caller (escalation matrix) |
| AVN | Check-in agent | Passenger documents in doubt (duty officer) |
| EDU | Teacher | Student welfare concern (safeguarding lead) |
| TRV | Guide | Traveller lost passport (operations / embassy procedure) |
| LOG | Coordinator | Customer's critical delivery at risk (operations manager) |
| MFG | Operator | Safety hazard on the line (supervisor / EHS: stop work) |
| CORP | HR executive | Grievance beyond your authority (HR manager) |
| PROF | Associate | Client requests out-of-scope work (engagement manager) |
| SPRT | Event coordinator | Crowd-safety concern (safety officer) |

### SK-12 Writing an email
**Function:** subject, purpose, details, action, close.
**Output:** email.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Events coordinator | Confirming conference details |
| IT | Business analyst | Requirement clarification |
| BFS | Relationship manager | Document checklist for a business loan |
| HLTH | Billing executive | Insurance claim follow-up |
| RTL | Store manager | Supplier delivery issue |
| BPO | Team leader | Escalation summary to the client |
| AVN | Customer-service agent | Delayed-baggage follow-up |
| EDU | Coordinator | Parent-meeting invitation |
| TRV | Consultant | Itinerary and payment terms |
| LOG | Buyer | Purchase-order follow-up |
| MFG | Quality engineer | Containment update to the customer |
| CORP | Office manager | Policy reminder |
| PROF | Project manager | Weekly status to the client |
| SPRT | Sponsorship executive | Activation plan to the sponsor |

### SK-13 Writing a report
**Function:** facts → evidence → analysis → action → recommendation (core FEAAR).
**Output:** industry document.

| Industry | Role | Situation | Document |
|---|---|---|---|
| HOSP | Front-office supervisor | Guest incident | Incident report |
| IT | Engineering manager | After an outage | Post-incident review |
| BFS | Branch manager | Cash discrepancy | Discrepancy report |
| HLTH | Department coordinator | Patient fall in the waiting area | Non-clinical incident report |
| RTL | Floor supervisor | Weekly stock variance | Stock report |
| BPO | Quality analyst | Monthly quality findings | Quality report |
| AVN | Duty officer | Disruption | Irregularity report |
| EDU | Academic coordinator | Term results | Results report |
| TRV | Operations manager | End of season | Tour report |
| LOG | Warehouse supervisor | Late delivery | Root-cause report |
| MFG | Quality engineer | Defect | Non-conformance report |
| CORP | Office manager | Facilities | Monthly facilities report |
| PROF | Consultant | Engagement findings | Executive summary |
| SPRT | Event manager | Sponsor campaign | Activation report |

### SK-14 Joining a meeting
**Function:** contribute, ask, agree or disagree, summarise.
**Output:** meeting role-play.

| Industry | Role | Meeting |
|---|---|---|
| HOSP | Front-desk agent | Daily briefing |
| IT | Developer | Sprint planning |
| BFS | Officer | Branch huddle |
| HLTH | Coordinator | Quality meeting |
| RTL | Associate | Store huddle |
| BPO | Agent | Calibration session |
| AVN | Agent | Pre-shift briefing |
| EDU | Teacher | Staff meeting |
| TRV | Guide | Tour briefing |
| LOG | Planner | Daily operations call |
| MFG | Supervisor | Start-of-shift meeting |
| CORP | Executive | Team meeting |
| PROF | Associate | Steering committee (supporting) |
| SPRT | Coordinator | Match-day briefing |

### SK-15 Leading a meeting
**Function:** open, agenda, manage time, decide, assign actions, close.
**Output:** chaired meeting plus minutes.

| Industry | Role | Meeting |
|---|---|---|
| HOSP | Front-office manager | Department-heads meeting |
| IT | Engineering manager | Incident review |
| BFS | Branch manager | Monthly branch review |
| HLTH | Department head | Rota-change meeting |
| RTL | Store manager | Weekly operations meeting |
| BPO | Operations manager | Client governance call |
| AVN | Station manager | Disruption debrief |
| EDU | Principal | Academic council |
| TRV | Operations manager | Season-planning meeting |
| LOG | Operations manager | Supplier review |
| MFG | Plant manager | Quality review |
| CORP | Function head | All-hands |
| PROF | Engagement manager | Steering committee |
| SPRT | Club director | Committee meeting |

### SK-16 Giving a presentation
**Function:** purpose, structure, data, recommendation, Q&A.
**Output:** presentation plus slides outline.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-office manager | Guest-satisfaction trends to the GM |
| IT | Project manager | Release status to stakeholders |
| BFS | Branch manager | Branch metrics to the regional director |
| HLTH | Department head | Scheduling-change results |
| RTL | Store manager | Quarterly store review |
| BPO | Operations manager | Monthly business review to the client |
| AVN | Customer-experience manager | On-time-performance review |
| EDU | Principal | Parent orientation |
| TRV | Account manager | Corporate travel proposal |
| LOG | Supply-chain manager | Supplier performance |
| MFG | Quality manager | Customer quality review |
| CORP | HR manager | Policy rollout |
| PROF | Consultant | Findings to the client |
| SPRT | Sponsorship executive | Sponsorship proposal |

### SK-17 Negotiating
**Function:** prepare (best alternative, limits), anchor, trade concessions, close and confirm (core L4 M1).
**Output:** negotiation role-play plus confirmation email.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Sales manager | Corporate rate contract |
| IT | Project manager | Scope versus deadline with a client |
| BFS | Relationship manager | Business-client fee terms (within limits) |
| HLTH | Department head | Service-vendor contract |
| RTL | Store manager | Local supplier terms |
| BPO | Operations manager | Staffing and targets with the client |
| AVN | Station manager | Ground-handling service levels |
| EDU | Principal | Transport-vendor contract |
| TRV | Operations manager | Hotel allotment rates |
| LOG | Buyer | Freight rates and lead times |
| MFG | Production manager | Delivery schedule with a customer |
| CORP | Office manager | Facilities contract |
| PROF | Engagement manager | Scope-change fee |
| SPRT | Sponsorship executive | Sponsorship package |

### SK-18 Handling disagreement
**Function:** acknowledge, state your view with reason, find common ground.
**Output:** discussion role-play.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Supervisor | Housekeeping versus front office on room-release times |
| IT | Developer | Code-review disagreement |
| BFS | Credit officer | Disagreement with an RM on a loan file |
| HLTH | Coordinator | Ward versus admissions on bed allocation |
| RTL | Supervisor | Rota disagreement |
| BPO | Quality analyst | Agent disputes a quality score |
| AVN | Duty officer | Gate versus ramp on boarding start |
| EDU | Teacher | Disagreement on a grading rubric |
| TRV | Coordinator | Guide versus operations on the route |
| LOG | Planner | Sales versus warehouse on priority |
| MFG | Quality engineer | Production versus quality on releasing a batch |
| CORP | HR | Manager wants to skip a policy step |
| PROF | Consultant | Client disputes a finding |
| SPRT | Team manager | Coach versus administration on training slots |

### SK-19 Giving feedback
**Function:** specific behaviour → impact → request (core L4 2.2, L5 M2).
**Output:** feedback conversation.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-office manager | Agent rushing check-ins |
| IT | Team lead | Developer skipping tests |
| BFS | Branch manager | Officer's documentation errors |
| HLTH | Department head | Receptionist's tone with families |
| RTL | Store manager | Associate ignoring the queue |
| BPO | Team leader | Agent's call-closing quality |
| AVN | Supervisor | Agent's announcement clarity |
| EDU | Coordinator | Teacher's late reports |
| TRV | Operations manager | Guide's time-keeping |
| LOG | Supervisor | Picking accuracy |
| MFG | Line supervisor | PPE compliance |
| CORP | Office manager | Assistant's follow-up |
| PROF | Engagement manager | Associate's report quality |
| SPRT | Academy head | Junior coach's communication with parents |

### SK-20 Receiving feedback
**Function:** listen, clarify, acknowledge, commit (core L4 2.3).
**Output:** response role-play.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-desk agent | Manager on guest complaints |
| IT | Junior developer | Code-review comments |
| BFS | Officer | Audit observation |
| HLTH | Executive | Patient-feedback findings |
| RTL | Associate | Mystery-shopper results |
| BPO | Agent | Quality-score feedback |
| AVN | Agent | Supervisor on a disruption-handling lapse |
| EDU | Teacher | Lesson observation |
| TRV | Guide | Traveller reviews |
| LOG | Associate | Accuracy audit |
| MFG | Operator | Safety observation |
| CORP | Executive | Manager's appraisal |
| PROF | Analyst | Partner's review |
| SPRT | Coordinator | Event debrief |

### SK-21 Delegating
**Function:** outcome, ownership, deadline, check-ins (core L5 M1).
**Output:** delegation conversation plus message.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-office manager | VIP arrival preparation |
| IT | Engineering manager | Owning a bug fix to release |
| BFS | Branch manager | Audit preparation |
| HLTH | Department head | Rota redesign |
| RTL | Store manager | Promotion launch |
| BPO | Operations manager | New-process rollout |
| AVN | Station manager | Peak-day staffing plan |
| EDU | Principal | Annual-day event |
| TRV | Operations manager | New-route launch |
| LOG | Warehouse manager | Stock-take |
| MFG | Production manager | Changeover improvement |
| CORP | HR manager | Onboarding redesign |
| PROF | Engagement manager | Client workshop |
| SPRT | Club director | Tournament hosting |

### SK-22 Coaching
**Function:** open questions; the learner owns the solution (core L5 M3).
**Output:** coaching conversation.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Supervisor | New agent handling difficult guests |
| IT | Team lead | Junior stuck on a bug |
| BFS | Branch manager | RM building client relationships |
| HLTH | Department head | Coordinator managing workload |
| RTL | Store manager | Supervisor planning rotas |
| BPO | Team leader | Agent reducing hold time |
| AVN | Supervisor | Agent handling angry passengers |
| EDU | Coordinator | New teacher's classroom routines |
| TRV | Operations manager | Guide handling group dynamics |
| LOG | Supervisor | Planner prioritising loads |
| MFG | Supervisor | Operator reducing defects |
| CORP | Function head | Assistant's prioritisation |
| PROF | Engagement manager | Associate's client communication |
| SPRT | Head coach | Junior coach's feedback to players |

### SK-23 Managing conflict
**Function:** separate the people from the problem, state interests, agree next steps (core L4 2.5–2.6).
**Output:** mediation role-play.

| Industry | Role | Situation |
|---|---|---|
| HOSP | Front-office manager | Shift-swap dispute between agents |
| IT | Team lead | Developer versus QA blame |
| BFS | Branch manager | Teller versus operations friction |
| HLTH | Department head | Day versus night shift handover friction |
| RTL | Store manager | Weekend-rota fairness |
| BPO | Team leader | Agents competing for incentives |
| AVN | Duty officer | Check-in versus gate staff |
| EDU | Principal | Two departments sharing labs |
| TRV | Operations manager | Guides' allocation of routes |
| LOG | Warehouse manager | Shift-handover blame |
| MFG | Production manager | Production versus maintenance |
| CORP | HR manager | Two teams sharing an assistant |
| PROF | Engagement manager | Consultants' credit for work |
| SPRT | Club manager | Coaches competing for ground time |

### SK-24 Handling a crisis
**Function:** calm statement → facts known/unknown → actions → next update time (core L4 M6). Safety and regulatory protocols take precedence.
**Output:** crisis update (spoken plus written).

| Industry | Role | Situation |
|---|---|---|
| HOSP | Duty manager | Booking-system outage at peak (exists in the core) |
| IT | Incident manager | Company-wide outage |
| BFS | Branch manager | Core-banking downtime at month end |
| HLTH | Administrator | Hospital IT outage affecting appointments (non-clinical) |
| RTL | Store manager | POS outage on a sale day |
| BPO | Operations manager | Site outage; calls rerouted |
| AVN | Station manager | Weather disruption with mass rebooking |
| EDU | Principal | School closure announcement |
| TRV | Operations manager | Strike stranding a tour group |
| LOG | Operations manager | Port closure |
| MFG | Plant manager | Line shutdown after a safety incident |
| CORP | Function head | Office closure (flood) |
| PROF | Engagement manager | Data error found in a published client report |
| SPRT | Event manager | Tournament day postponed |

### SK-25 Communicating decisions
**Function:** decision, reasoning, what changes, what doesn't, acknowledging disagreement (core L4 4.3, L5 5.3).
**Output:** announcement plus message.

| Industry | Role | Situation |
|---|---|---|
| HOSP | General manager | New breakfast hours |
| IT | Engineering manager | Release postponed |
| BFS | Branch manager | New appointment-only service hours |
| HLTH | Department head | New scheduling system |
| RTL | Store manager | Rotating weekend schedule |
| BPO | Process head | New quality rubric |
| AVN | Station manager | New check-in cut-off |
| EDU | Principal | New assessment policy |
| TRV | Agency head | Stop selling a destination |
| LOG | Supply-chain manager | Change of carrier |
| MFG | Plant manager | Shift-pattern change |
| CORP | Function head | Hybrid-work policy |
| PROF | Partner | Engagement-team restructure |
| SPRT | Club director | Academy fee change |

## 12. Lesson architecture

### 12.1 Industry lesson template

The template is standard but flexible. **R** = required in every industry lesson. **C** = conditional (required when the lesson type needs it). **O** = optional.

| # | Element | Status | Rule |
|---|---|---|---|
| 1 | Lesson objective | R | 1–3 can-do statements, each naming the industry situation |
| 2 | Workplace situation | R | Setting, participants, stakes, the information available |
| 3 | Role | R | One role ID from the taxonomy; the band follows from it |
| 4 | Communication goal | R | The output the learner must produce |
| 5 | Key vocabulary | R | Industry and situation terms only. Universal terms are cited by core V code, not repeated. |
| 6 | Useful expressions | R | Industry slots in core frames. Cite the core CF/PAT code; don't re-teach the frame. |
| 7 | Model dialogue | R | At least one industry dialogue (or a model document in document lessons) |
| 8 | Professional tone | C | Required where industry norms differ from the core: clinical neutrality, disclosure language, SOP scripts |
| 9 | Grammar in context | O | Cite core GIC. A new GIC only if an industry document has a genuinely new pattern. |
| 10 | Pronunciation / delivery | C | Industry terms with difficult stress; announcements (AVN), calls (BPO) |
| 11 | Listening task | C | Print: "read, not heard" until audio exists. **Listening may not be claimed without audio.** |
| 12 | Speaking task | R | At least one |
| 13 | Reading task | C | Required in document lessons (read a log, ticket, policy or email) |
| 14 | Writing task | R | At least one industry text (message, email or document) |
| 15 | Role-play | R | At least one, with role cards |
| 16 | Problem-solving task | C | Required in incident/escalation lessons |
| 17 | Reflection | R | A self-check against the rubric |
| 18 | Performance task | R | An integrated task (speak + write) |
| 19 | Assessment | C | Formative items in every lesson; module-test items pooled |
| 20 | Answer key | R | For every closed item; sample answers for open tasks |

### 12.2 Lesson types

All four types use the same template with different required elements:

| Type | Purpose | Extra requirements |
|---|---|---|
| Situation lesson | One workplace event | Default type |
| Document lesson | One industry document type | Reading task + model document + writing task |
| Protocol lesson | Safety-critical or regulated communication (read-back, disclosure, announcements) | SME-supplied wording; accuracy-scored assessment |
| Integration lesson | Combines 2–3 skills before a test or capstone | — |

### 12.3 Length and links

- **Length:** the measured core lesson mean is 5.0 print pages (range 4–8). Industry lessons are planned at 4–6 pages because they cite the core instead of re-teaching it.
- **Links:** every industry lesson declares the core lessons it applies (`appliesSkills: [SK-02]`, `coreRefs: [CE-L02-M01-L01 …]`). The website can then show "Learn the skill: Level 2 · Lesson 1.1".

## 13. Assessment architecture

### 13.1 Assessment types, per industry and band

| Type | Purpose | Format | Scoring |
|---|---|---|---|
| Diagnostic | Place the learner in a band and identify gaps | 20–30 items: industry reading, situational judgement, one short writing task | Band placement; skill gaps by SK ID |
| Practice | Unscored rehearsal | Lesson exercises | Answer key and sample answers |
| Formative | Check each lesson objective | 3–6 items per lesson; self-check against the rubric | Self or peer |
| Module test | Check one band module | Situational multiple choice, rewriting, one document task, one role-play | Points + universal rubric (5 criteria) + industry criteria (3) |
| Performance assessment | Integrated real task | Role-play + document + short presentation/meeting, from role cards | Rubric; pass descriptors per band |
| Industry capstone | End-of-band or end-of-track simulation | Capstone engine (section 14) | Rubric, 100% weighting split by stage |

### 13.2 Rubric

**Universal criteria** (same for every industry): task achievement; structure; clarity and accuracy; tone and register; interaction (spoken).

**Industry criteria** (adjusted per industry):
- correct terminology;
- policy-, regulation- and safety-compliant content (**pass/fail where SME-defined**, e.g. no clinical advice, no promise of transaction reversal, exact read-back);
- correct document format.

### 13.3 Constraints

- Assessments using listening or announcements (BPO, AVN) need **audio** before they can be called listening assessments.
- No assessment result may be described as certification or external endorsement.

## 14. Capstone architecture

### 14.1 Capstone engine

One structure produces every industry's capstone. Each capstone is defined by inputs:
- industry;
- role (and therefore band);
- trigger situation;
- the constraint set (policy, regulation, safety);
- the information pack (logs, emails, data);
- the stakeholders;
- the documents required.

**Stages:**

| Stage | Name | What happens | Core skills used |
|---|---|---|---|
| 1 | Trigger | The learner receives the situation | SK-03 clarify |
| 2 | Gather | Read the information pack; ask questions | SK-03, SK-10 |
| 3 | Update up | Brief the manager or supervisor | SK-02, SK-11 |
| 4 | Act and communicate | Speak with the customer, client or stakeholder | SK-07, SK-08, SK-09 / SK-17 |
| 5 | Document | Write the industry document | SK-12, SK-13 |
| 6 | Meet / present | Escalation meeting, briefing or presentation | SK-14–SK-16 / SK-25 |
| 7 | Reflect | Self-assessment against the rubric | — |

Band changes the stakes and the stages used:
- **Entry band:** stages 1–5, with a short report.
- **Professional band:** all stages.
- **Leadership band:** adds leading the meeting (SK-15), deciding and announcing (SK-25), and team feedback (SK-19).

### 14.2 Core skill "handling a difficult situation" across industries

| Industry | Trigger | Constraint the learner must respect | Document |
|---|---|---|---|
| Hospitality | Guest complaint | Remedies within authority; duty-manager escalation | Incident report |
| IT | Production outage | No speculation on root cause before evidence; SLA clock | Incident email + post-incident review |
| Banking | Customer transaction dispute | No promise of reversal; grievance process | Written resolution letter |
| Healthcare | Patient-service complaint | No clinical judgement; privacy | Non-clinical incident report |
| Retail | Customer refund dispute | Returns policy; manager exception | Exception record |
| BPO | Escalated customer interaction | Escalation matrix; verification; disclosure | Ticket + escalation note |
| Education | Parent/student complaint | Review process; safeguarding referral if needed | Follow-up letter |
| Aviation | Passenger service disruption | SOP announcements; rebooking policy | Irregularity report |
| Logistics | Delayed shipment | Carrier facts only; no unconfirmed ETA | Delay notice + root-cause report |
| Manufacturing | Production-quality issue | Containment first; EHS rules | Non-conformance report + corrective action |
| Sports | Sponsor/event communication problem | Contract deliverables | Sponsor report |
| Tourism | Tour disruption | Supplier terms; traveller safety | Follow-up + supplier claim |
| Corporate / Office | Policy-change resistance | HR policy wording | Follow-up report |
| Professional services | Scope-change dispute | Contracted scope; fees | Change summary |

The architecture stays the same; only the inputs change. This is what lets one capstone design be reused across all 14 industries.

## 15. Vocabulary architecture

### 15.1 Layers

| Layer | Content | Where it lives | Coded? |
|---|---|---|---|
| Universal | Workplace terms used in any industry | Existing core V codes, unchanged | Yes: existing V |
| Industry | Domain terms (ticket, KYC, consignment, admission) | Industry vocabulary table | Yes (see 15.2) |
| Role | Which industry terms a role needs | A **tag** on industry entries | No |
| Situation | Terms tied to one situation | A **tag** on industry entries | No |

Making role and situation separate code namespaces would duplicate terms: the same "escalation matrix" would be coded once per role. Tags avoid this.

**De-duplication rule.** Before an industry term is created, search the core index and the other industries:
- the term is already a core V → cite it;
- it is needed by 3 or more industries with the same meaning → propose it as a new **universal** term (next core V number);
- it means different things in different industries (e.g. "ticket" in IT, aviation and events) → separate industry entries, each with its own definition.

### 15.2 Code options

**Constraint found in the audit:** the website, index builder and print builder all match `\b(V|PAT|GIC|CF|TL|MIS|TIP|P)-\d{3,4}\b`.

| Option | Example | Collision with current tools | Tool changes | Readability | Scalability | Notes |
|---|---|---|---|---|---|---|
| 1. Industry prefix | `IND-IT-V-0001` | **Yes.** The current pattern matches `V-0001` inside it, so the industry term would silently link to core V-0001 (*professional*). | Regex change with a negative look-behind in 3 places | Long | Good | Unsafe until every tool is changed; any tool missed causes mis-links |
| 2. Continue the global sequence | `V-0793` + metadata `industry: IT` | None | None | Industry not visible in the code | Needs reserved number blocks per industry for parallel authoring | Core and industry mixed in one index; never fill gaps below V-0792 |
| 3. Type first, industry segment | `V-IT-0001`, `PAT-BFS-0001`, `MIS-HLTH-0001` | **None.** The current pattern requires digits right after `V-`, so it ignores these codes. | Extend the pattern once: `\b(V\|PAT\|…)-(?:(HOSP\|IT\|…)-)?\d{3,4}\b` | Clear | Each industry numbers independently | Keeps type grouping; industry IDs must never equal a type name (no industry called P, TL, CF …) |
| 4. New types per industry | `ITV-0001` | None | New type per industry | Medium | Type count explodes (8 types × 14 industries) | Index sections multiply |

**Proposed design: option 3 for industry-specific items, plus the core V sequence for new universal terms.**
- New universal terms start at **V-0793**, above the current maximum. Retired and gap numbers are never reused.
- Existing V/PAT/MIS/CF/GIC/TL/TIP/P codes are not touched or renumbered.
- The choice is author decision D-10.

## 16. Data architecture (summary)

Full proposal: [MULTI-INDUSTRY-DATA-SCHEMA.md](MULTI-INDUSTRY-DATA-SCHEMA.md).

**Key points:**
- Industry content lives in a **separate file**, `industry-data.json` (proposed name), not inside `book-data.json`. Three reasons:
  - `book-data.json` is a top-level array of levels, read by the website, the print builder and the editorial tools;
  - it is verified as "baseline + logged corrections", so new content written into it would fail `apply_corrections.py --check`;
  - the core book's publication gates are tied to its current state.
- The new file uses the **same unit shape** (`objectives_html`, `body_html`, `practice_html`), so the existing renderers can be reused.
- **Linking tables:**
  - `skills` (SK-01…SK-25 → core lesson IDs);
  - `industries`;
  - `roles`;
  - `situations`;
  - `industryModules`;
  - `industryLessons`;
  - `industryVocabulary`;
  - `industryAssessments`;
  - `industryCapstones`;
  - `claims` (coverage tier per industry).
- **IDs follow the existing pattern.** Example: `CE-IND-IT-B2-M01-L01` (industry, band, module, lesson), parallel to `CE-L02-M01-L01`.

## 17. Website / app architecture

**Current site (`index.html`):**
- a fixed left dashboard with a level tree and search, including code search;
- a per-lesson "reviewed" flag stored in browser storage (`hea-book-reviewed`, keyed by lesson ID).

**Proposed navigation (concept only, not coded):**

```
CAREER ENGLISH
├─ Core course ........ Level 1 → 5 (unchanged)
└─ Industry English ... Choose level/band ─► Choose industry ─► Choose role ─► Choose situation
                         B1 (Entry)            Hospitality         Front office     Handling a guest complaint
                         B2 (Professional)     IT                  Technical support Handling a customer escalation
                         B2 (Professional)     Banking             Customer service  Explaining a transaction issue
```

**Design rules:**
- **Every industry lesson page shows "Skill from the core"**, with links to the core lessons it applies. Learners who skipped the core can learn the skill first.
- **Filters:** level/band, CEFR band (once approved), industry, role, situation, skill (SK), document type, assessment type.
- **Search:** the existing code search extends to the new code pattern (15.2). Industry vocabulary is searchable by term, industry and role.
- **Progress:** the same per-unit key model, using the new stable IDs. Progress is shown per industry module and per band. (Moving progress to an account system is a separate product decision, not needed for this architecture.)
- **Claim badges:** each industry's landing page shows its *current coverage tier* (section 23), e.g. "Examples only" or "Application module (B2)". The page can never claim more than the data supports.
- **Accessibility:** current standards are kept (WCAG AA colours, skip link, labelled search, focus outlines).

## 18. CEFR architecture

**The book currently makes no CEFR claim:** "CEFR", "A2", "B1" and similar occur 0 times. The mapping below is a **proposed, unvalidated design alignment**. It is not a certification or an endorsement, and it would need validation (D-12).

| Core level | Proposed CEFR band | Evidence in the core |
|---|---|---|
| Level 1 Foundation | A2+ → B1 | Present perfect for background (L1 1.2); polite requests; short routine exchanges |
| Level 2 Workplace English | B1 | Status updates; phone handling; short written requests; simple complaints |
| Level 3 Professional English | B1+ → B2 | Emails, reports, meetings; passive and reported speech; modals and conditionals |
| Level 4 Advanced Professional English | B2 → C1 | Negotiation, persuasion, crisis communication; senior audiences |
| Level 5 Leadership English | C1 | Executive presentation; coaching; strategic and change communication |

| Industry band | Core levels | Proposed CEFR | Skill character |
|---|---|---|---|
| Entry | L1–L2 | A2+ → B1 | **Foundational:** introductions, clarification, requests, updates, simple customer service, apology |
| Professional | L3–L4 | B1+ → B2 (upper part toward C1) | **Intermediate to advanced:** emails, reports, complaints, escalation, meetings, presentations, negotiation |
| Leadership | L5 | C1 | **Leadership:** delegation, feedback, coaching, decisions, change, executive presentation, crisis leadership |

**A1 and C2:**
- **A1** is not targeted: the core assumes basic English. A1 learners would need a pre-course (D-12).
- **C2** is not targeted: no professional role in the taxonomy requires C2 for its core communicative events.

**Validation steps before any CEFR wording is used publicly:**
1. Align lesson can-do statements to CEFR descriptors (including the Companion Volume's mediation scales).
2. Have a specialist review the alignment.
3. Pilot the diagnostic with learners.

## 19. Bengali/Hindi localization architecture

**Current state:**
- Script appears in 31 units, 27 of them in Level 1.
- There are 40 English-language "Bengali/Hindi support" notes.
- **The native-language review of the current book has not been performed.**

The expansion keeps the **English-first** philosophy and does not translate sentences mechanically.

**When support appears:**

| Trigger | Support given | Example |
|---|---|---|
| Difficult concept | Short English explanation + a Bengali/Hindi gloss of the key term | "workplace culture" (existing L1 1.1 note) |
| False friend / misleading equivalent | An English note explaining the trap | Industry terms whose everyday-language equivalent differs |
| Culturally important distinction | An English note on the expectation | Directness with managers; addressing seniors; "sir/madam" in the BPO and banking registers |
| Common learner error | MIS entry + support note | Article and present-perfect errors (existing pattern) |
| Pronunciation issue | Stress/sound note for terms | Stress in "escalate" or "consignment"; sounds listed in L3 M8 |
| Industry terminology | **Rule: terms used in English at work stay English.** Script gloss only where learners need the meaning, never as a replacement term. | "check-in", "KYC", "OPD", "ticket", "dispatch" are used in English in South Asian workplaces |

**Consistency rules:**
- Bengali and Hindi always appear together, with the same scope for each.
- Support is denser in the Entry band and lighter in the Professional and Leadership bands, mirroring the core.
- Every script item becomes a native-review register item. The existing `NATIVE-LANGUAGE-REVIEW.csv` model is reused per industry.
- **No industry module's Bengali/Hindi content may be marked approved without a named native reviewer.**

## 20. QA architecture

### 20.1 Gates for every industry track

Each gate has an owner and recorded evidence. No gate may be marked PASS by automation alone where a person is named as owner.

| Gate | What it checks | Owner | Automatable part |
|---|---|---|---|
| Content QA | Template compliance; core links valid; no re-teaching of universal skills | Editor | Template and link checks |
| Language QA | Grammar, naturalness, register | Editor + proofreader | Spelling and repetition checks |
| Industry accuracy QA | Terms, procedures and documents are realistic and correct | Industry SME | — |
| Role realism QA | Roles and situations match real jobs at that tier | Industry SME | — |
| Dialogue QA | Natural turns, correct roles, consistent characters | Editor | Speaker and turn checks |
| Vocabulary QA | No duplicates with the core or other industries; code format; definitions | Editor | Duplicate and code checks |
| Assessment QA | Items match objectives; keys correct; rubric weights total 100% | Assessment editor | Answer-count and numbering checks (the core audit method) |
| CEFR QA | Can-do statements and tasks match the claimed band | CEFR specialist | — |
| Bengali QA | Script accuracy and meaning | Native Bengali reviewer | Register generation |
| Hindi QA | Script accuracy and meaning | Native Hindi reviewer | Register generation |
| Cultural QA | Respectful, non-stereotyped, region-appropriate | Editor + cultural reviewer | — |
| Copyedit QA | House style (UK dates, spelling) | Copyeditor | House-style report |
| Layout QA | Page breaks; no stranded headings | Production | `auto_checks.py` |
| PDF QA | Text, bookmarks, contents and index match the source | Production | `consistency_audit.py` (extended) |
| Accessibility QA | Contrast, headings, alt text, keyboard navigation | Production | Automated contrast and heading checks |

### 20.2 Industries needing specialist review

| Industry | Specialist | Why |
|---|---|---|
| HLTH | Healthcare administration + clinician | Patient safety, privacy, no medical advice |
| BFS | Banking compliance | KYC/AML, disclosures, complaint rules; jurisdiction differences |
| AVN | Airline/airport operations | Safety scripts must follow SOP; regulatory scope |
| MFG | EHS / quality | Safety procedures; quality-system terms |
| EDU, SPRT | Safeguarding | Communication involving minors |
| BPO | Contact-centre compliance | Data protection; call recording |
| LOG | Logistics | Customs and dangerous goods kept out of scope unless reviewed |
| IT, PROF, RTL, TRV, HOSP, CORP | Practitioner | Realism; lower regulatory risk |

## 21. Publishing architecture

**Option 1: one large book**

| Criterion | Assessment |
|---|---|
| Volume size | 2,100–3,500 pages with full tracks (section 22): beyond a practical single binding |
| Time to market | Slowest; every track must finish first |
| Update cycle | Any change reprints everything |
| Learner usability | Each learner carries 13 irrelevant industries |
| Claim granularity | One claim for the whole volume |
| Dependency on website | None |

**Option 2: core book + industry supplements (print)**

| Criterion | Assessment |
|---|---|
| Volume size | Core 1,104 pages + about 63–168 pages per industry supplement |
| Time to market | Per industry |
| Update cycle | Per supplement |
| Learner usability | Buy only your industry |
| Claim granularity | Per supplement |
| Dependency on website | None |

**Option 3: core book + digital industry tracks**

| Criterion | Assessment |
|---|---|
| Volume size | Core only in print |
| Time to market | Fastest; tracks grow band by band |
| Update cycle | Continuous |
| Learner usability | Filters by role and situation; audio possible |
| Claim granularity | Per track and per band; coverage badge |
| Dependency on website | High (needs website/app work) |

**Option 4: core book + print industry workbooks**

| Criterion | Assessment |
|---|---|
| Volume size | Thin workbooks (tasks, role cards, documents) that refer to the core for teaching |
| Time to market | Medium |
| Update cycle | Per workbook |
| Learner usability | Good for classroom use |
| Claim granularity | Per workbook; workbooks rarely meet T4 without dialogues |
| Dependency on website | None |

**Option 5: hybrid print + digital**

| Criterion | Assessment |
|---|---|
| Volume size | Core in print; industries digital first, printed as supplements once they reach T3/T4 |
| Time to market | Fast start; print follows proven content |
| Update cycle | Digital continuous; print versioned |
| Learner usability | Both |
| Claim granularity | Per band and per track, from one data source |
| Dependency on website | Medium–high |

**What the comparison shows.**
- Option 1 is ruled out by scale alone.
- Options 2 and 4 keep print simple but delay audio and role filtering.
- Option 3 depends fully on the website.
- **The proposed design is Option 5.** It matches Model D, because one data source feeds both the website and the PDF builder, which already render from data. It also lets claims follow evidence band by band.

The choice is author decision D-02.

**Core book unaffected.** The 1,104-page core keeps its own publication path, whose gates (proofread and native review not performed; approval NO) are unchanged by this architecture.

## 22. Page-scale scenarios

**Inputs measured from the current PDF:**

| Item | Pages |
|---|---|
| Lesson | 5.0 mean (range 4–8) |
| Assessment | 6.6 mean (5–8) |
| Capstone | 11.2 mean (8–14) |
| Module opener | about 1 |
| Reference Index | 34 for 926 codes, about 3.7 per 100 codes |

**Unit assumptions** (a stated planning model, not a measurement):

| Unit | Content | Pages |
|---|---|---|
| Industry module, one band, T3 | 8 lessons × 5 + opener 1 + module test 7 + capstone 11 + glossary 2 + index (about 50 codes) 2 | **≈ 63** |
| Full track, three bands, T4 | 20 lessons × 5 + 3 openers + 3 tests × 7 + 3 capstones × 11 + glossary 4 + track introduction 2 + index (about 120 codes) 4.4 | **≈ 168** |

Lesson counts come from the domain coverage in section 23: Entry 6 + Professional 8 + Leadership 6 = 20.

**Scenarios** (pages added to the 1,104-page core):

| Industries | One band each (T3) | Full tracks (T4) | Single volume with full tracks |
|---|---|---|---|
| 6 | ≈ 380 | ≈ 1,010 | ≈ 2,110 |
| 8 | ≈ 500 | ≈ 1,340 | ≈ 2,450 |
| 10 | ≈ 630 | ≈ 1,680 | ≈ 2,790 |
| 14 | ≈ 880 | ≈ 2,350 | ≈ 3,460 |

**Sensitivity:**
- At 4 pages per lesson, full tracks shrink by about 20 pages each.
- At 6 pages per lesson, they grow by about 20 pages each.
- Hospitality may need fewer new lessons for front-office situations, but its other roles still need full content.

**Reading:** even six industries at full depth would almost double the volume. The scale supports a modular core-plus-industry publication rather than one book.

## 23. Marketing claim-control system

### 23.1 Coverage tiers and minimum evidence (content depth standard)

**Why the thresholds are what they are.** A claim that a course "covers" an industry promises that a person working in that industry can:
1. rehearse the high-frequency communicative events of their role at their level;
2. produce the industry's core documents;
3. be assessed on an integrated, realistic task.

The thresholds are therefore derived from the **communication domains** (D1–D9) a role meets, per **band**. They are not round numbers:
- Entry roles meet 6 domains: D1, D2, D3, D4, D5 (recognise and escalate), D6.
- Professional roles meet 8 lesson-worthy events: D3, D4, D5, D6 (email), D6 (industry document), D7, D8, plus one integration.
- Leadership roles meet 6: D5 (crisis leadership), D7, D8, and D9 three ways (delegation; feedback and coaching; decisions and change).

The per-lesson minimums mirror the core's own density:
- the core has 213 dialogues across 196 units, about one per unit;
- it has 164 role-plays across 196 units.
- Industry lessons require one of each, because performance is their purpose.

| Tier | Claim allowed | Minimum evidence (all required) | Equivalent on the brief's scale |
|---|---|---|---|
| T0 Universal | "Workplace English useful across industries" | Universal core (met) | — |
| T1 Examples | "Includes examples from X" | At least 10 labelled examples from X spread over at least 3 levels, so the examples recur through the course rather than sit in one place | 2 OVERLAY |
| T2 Application | "Industry application lessons for X (Entry band)" | At least one application lesson in each of the 6 Entry domains. Each lesson meets the template's R items: an industry dialogue, a role-play, an industry writing task, and vocabulary closure (every term needed for its tasks is taught). | 3 APPLICATION |
| T3 Module | "English for X: [band] module" | All lessons of one band (6/8/6), plus: the band's 3 most frequent industry documents, each with a model and a writing task (identified by SME); a module test; a performance assessment; the band capstone; vocabulary closure; SME sign-off where flagged; the 15 QA gates PASS | 4 DEDICATED MODULE |
| T4 Full track | "Professional English for X" / "Full professional English track for X" | T3 met in all three bands (20 lessons), plus a track diagnostic, 3 capstones, SME sign-off, and Bengali/Hindi native review where script is used | 5 FULL TRACK |

**Separate conditions:**
- **Listening:** "listening practice" may be claimed only where audio exists.
- **CEFR:** "CEFR-aligned" may be claimed only after the validation steps in section 18.

### 23.2 Current claim register

| Claim | Status | Reason |
|---|---|---|
| "Useful across industries" / "workplace English for every career" | **SUPPORTED** | T0: universal core |
| "Industry examples included" | **SUPPORTED** only when it names IT, banking, retail and healthcare, with the hotel as the setting; **NOT SUPPORTED** if the list includes BPO, aviation, sports, education or tourism | T1 met only for IT 88, banking 73, retail 58, healthcare 47, hotel 58 |
| "Set in a hotel workplace" | **SUPPORTED** | Core setting |
| "Professional English for Hospitality" | **PARTIALLY SUPPORTED** | T2-equivalent for one role (front office); not T3/T4: no hotel-specific documents or assessment, other hotel roles absent |
| "Industry application modules" | **NOT SUPPORTED** | No T2/T3 content for any industry |
| "Full professional English track for IT" | **NOT SUPPORTED** | IT is T1 |
| "Professional English for Banking" | **NOT SUPPORTED** | T1 |
| "Professional English for Healthcare" | **NOT SUPPORTED** | T1 |
| "Covers BPO / call centres, aviation, sports, cricket" | **NOT SUPPORTED** | Below T1, or absent |
| "Listening practice" | **NOT SUPPORTED** | No audio |
| "CEFR-aligned" | **NOT SUPPORTED** | No validated mapping |

### 23.3 Control process

1. **Claims register in the data.** Proposed `claims` table in `industry-data.json`: claim text, required tier, industry, status.
2. **Computed tier.** A future check script computes each industry's tier from the data: lessons per domain and band, documents, assessments, capstones, gate status. It fails if any registered claim needs a higher tier than the computed one. This follows the same pattern as the existing gate guard in `build_proof_reports.py`, which refuses a PASS the evidence does not support.
3. **Copy review.** Every cover, back-cover, website and advertising text is checked against the register before release. A new **Claim control** publication gate is proposed.
4. **Upgrades only after evidence.** A claim's status changes only after the tier is met and the QA gates for that content PASS.

## 24. Implementation roadmap

Nothing is implemented until Phase 0 is approved.

**Phase 0: Architecture approval**

| | |
|---|---|
| Input | This document; baseline audit; matrix; schema; decisions |
| Output | Approved decisions D-01 to D-20 |
| Files | `MULTI-INDUSTRY-AUTHOR-DECISIONS.md` (decisions recorded) |
| QA | Author review |
| Dependencies | None |
| Author decisions | All of D-01 to D-20; at least the model, publishing, pilot industry, codes and data placement |

**Phase 1: Pilot industry architecture**

| | |
|---|---|
| Input | Approved decisions; one pilot industry at one band |
| Output | One T3 module: 6–8 lessons, module test, capstone, glossary; role taxonomy and situation bank for that industry; data file and schema validator; renderer support (web and PDF) for the new file; code-pattern extension |
| Files | `industry-data.json`; schema; validator; tool updates (index builder, website, print builder) |
| QA | All 15 gates on the pilot; SME review; claim check |
| Dependencies | D-01, D-02, D-03, D-05, D-09, D-10, D-16; SME available if the pilot industry is flagged |
| Author decisions | Pilot industry; characters; template sign-off |

**Phase 2: First production tracks**

| | |
|---|---|
| Input | Pilot lessons learned |
| Output | First set of industries (number per D-03) at T3; extension toward T4 |
| Files | Industry content; vocabulary; native-review registers per industry |
| QA | All gates per industry |
| Dependencies | SMEs; native reviewers (see risk R-05) |
| Author decisions | Industry order; scope boundaries (D-07) |

**Phase 3: Assessment system**

| | |
|---|---|
| Input | Production content |
| Output | Diagnostics; module tests; performance assessments; capstone engine instances; rubrics |
| Files | Assessment data |
| QA | Assessment QA; CEFR QA |
| Dependencies | D-12, D-13 |
| Author decisions | Scoring and pass marks; CEFR wording |

**Phase 4: Website/app integration**

| | |
|---|---|
| Input | Data and assessments |
| Output | Level → industry → role → situation navigation; filters; progress per industry; claim badges; extended code search |
| Files | Website code (only after approval; the deploy workflow stays gated) |
| QA | Accessibility; regression on the core site |
| Dependencies | D-11; audio decision (D-18) |
| Author decisions | Account and progress model; audio |

**Phase 5: Additional industries**

| | |
|---|---|
| Input | Proven pipeline |
| Output | Remaining industries, band by band |
| Files | As Phase 2 |
| QA | All gates |
| Dependencies | SMEs per industry |
| Author decisions | Which industries; when |

**Phase 6: Final publishing**

| | |
|---|---|
| Input | Industries at the claimed tier |
| Output | Print supplements and/or digital release; marketing copy from the claim register |
| Files | PDFs per supplement; release notes |
| QA | PDF QA; claim control; publication approval |
| Dependencies | D-02; each supplement's gates |
| Author decisions | Publication approval for each product |

## 25. Risks

| # | Risk | Effect | Mitigation in this architecture |
|---|---|---|---|
| R-01 | Claims run ahead of content | Misleading marketing | Tiers, claim register, computed-tier check, Claim control gate |
| R-02 | Duplication of universal teaching | Bloat; inconsistency with the core | Skill registry; "cite, don't re-teach" rule; Content QA check |
| R-03 | Regulated or safety content is wrong (healthcare, banking, aviation, manufacturing) | Harm; liability | Scope boundaries; SME-owned protocol lessons; pass/fail compliance criteria |
| R-04 | No SME available | Flagged industries cannot pass gates | Sequence unflagged industries first, or keep flagged ones at T1/T2 |
| R-05 | **No native-language reviewer** (the author has said no separate reviewer will be available) | Bengali/Hindi content cannot be approved; the core's native review is already NOT PERFORMED | Keep script support minimal and recorded as unreviewed, or secure reviewers before script-heavy Entry modules (D-15) |
| R-06 | Code collision | Industry terms silently link to core codes | Option 3 format, tested: `IND-IT-V-0001` collides with `V-0001`; `V-IT-0001` does not |
| R-07 | Data divergence between two files | Broken links | Validator: every `coreRef` and SK link must resolve; IDs unique across both files |
| R-08 | Scale explosion | Unfinishable programme | Band-by-band tiers; Option 5 publishing; pilot first |
| R-09 | No audio | Listening claims impossible; BPO/AVN weaker | Audio decision D-18; claims limited until then |
| R-10 | CEFR mis-claim | Credibility | Mapping marked provisional; validation before public use |
| R-11 | Core book disruption | Reopens verified content and gates | Separate data file; core untouched; core publication path independent |
| R-12 | Character and story inconsistency | Confusing for learners | D-05; continuity sheet per industry |
| R-13 | Website performance with larger data | Slow loading | Load industry data on demand, per industry |
| R-14 | Cultural stereotyping across sectors and regions | Offence; inaccuracy | Cultural QA gate; the core's L4 M7 principle (adapt without stereotyping) applies |

## 26. Open decisions requiring author approval

These are listed with options in [MULTI-INDUSTRY-AUTHOR-DECISIONS.md](MULTI-INDUSTRY-AUTHOR-DECISIONS.md):

| # | Decision |
|---|---|
| D-01 | Architecture model |
| D-02 | Publishing format |
| D-03 | Number and choice of initial industries, and the pilot |
| D-04 | Corporate/Office as a track or as a role layer |
| D-05 | Characters |
| D-06 | Hospitality's position |
| D-07 | Healthcare scope |
| D-08 | Cricket |
| D-09 | Industry IDs |
| D-10 | Vocabulary code architecture |
| D-11 | Role tracks |
| D-12 | CEFR structure |
| D-13 | Assessment structure |
| D-14 | Learning cycle |
| D-15 | Bengali/Hindi depth and reviewers |
| D-16 | Data placement |
| D-17 | Coverage tiers and claim thresholds |
| D-18 | Audio |
| D-19 | Specialist review sourcing |
| D-20 | Sequencing relative to the core book's publication |

**No decision has been made in this document.** Where a "proposed design" is stated, it is a proposal awaiting approval.
