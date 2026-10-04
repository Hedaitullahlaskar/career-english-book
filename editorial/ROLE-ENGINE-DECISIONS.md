# Role engine: decision record

The decisions from [ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE.md](ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE.md) §12, updated for [CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md](CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md).

**Approval scope.** The architecture is approved **only** as stated below. **No implementation has started**, and none will until the pending decisions are answered.

## Decisions recorded (4 October 2026)

| # | Decision | Author's ruling | Effect on the specifications |
|---|---|---|---|
| D-R01 | Role-first organisation | **APPROVED.** ROLE is the central reusable unit, not HR and not industry. The system supports industry + department/function + role + seniority + workplace situation + communication function. The same role is reusable across industries. | Role-first organisation adopted. It supersedes the industry-first organisation of `MULTI-INDUSTRY-EXPANSION-ARCHITECTURE.md`; that document's claim tiers, QA gates, page-scale model and skill registry remain in use. |
| D-R07 | Source location | **APPROVED.** Source and draft curriculum content stays under `editorial/curriculum/`. Never in a top-level `/curriculum`, because the deploy workflow would publish it. Only validated, approved, compiled output may be published. | CONTENT-DATA-SCHEMA §2 |
| D-R09 | Review policy | **APPROVED WITH STRICT GATES.** GENERATED → AI QA → Editorial Review → Specialist Review (where required) → Native Review (where required) → APPROVED → COMPILED → PUBLISHED. If a required human, specialist or native review is NOT_PERFORMED, the content is not APPROVED. NOT_PERFORMED is never treated as PASS. | ROLE-QA-SPEC §1, §3, §6; CONTENT-DATA-SCHEMA §3 and rules 7–8; CHATGPT-CONTENT-ENGINE-SPEC §4. Status values are aligned to this sequence. |
| D-R12 | Pilot | **PRINCIPLE APPROVED; options A–D SUPERSEDED by D-U13.** Pilot role instances, not entire industries. The pilot must test (1) a reusable cross-industry role and (2) an industry-specific role. The final selection waits for the author's review of the options below. | No pilot chosen; nothing implemented |

## Superseded decisions (author's update, 4 October 2026)

The author clarified the final vision: universal coverage, frontline workers as a first-class requirement, digital-first, and no page ceiling. As a result, the pending decisions below are **SUPERSEDED**. They are replaced by D-U01…D-U16 in [CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md](CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md) §20. **The author does not need to answer them.**

| # | Earlier decision | Status | Replaced by |
|---|---|---|---|
| D-R02 | Role model (role instance = role + industry + department + level) | **SUPERSEDED** | D-U01 (Role Profile vs Role Instance; layered model), D-U02 (hierarchies), D-U03 (core modules) |
| D-R03 | Responsibility levels and ranks | **SUPERSEDED** | D-U05 (adds ownership-track scale and employment setting) |
| D-R04 | CEFR range | **SUPERSEDED** | D-U04 (Pre-A1…C2 including plus levels) |
| D-R05 | Scope codes | **SUPERSEDED** | D-U07 (211 codes: sectors, industries, families) |
| D-R06 | Industry list | **SUPERSEDED** | D-U02 (27 sectors → 122 industries) |
| D-R08 | Content generator | **SUPERSEDED** | D-U10 (adds budget rules) |
| D-R10 | Job-knowledge boundaries | **SUPERSEDED** | D-U11 (adds public-procedure and safety policies) |
| D-R11 | Characters | **SUPERSEDED** | D-U12 |
| D-R12 options A–D and Parts 2–5 | Pilot selection | **SUPERSEDED** (the pilot *principle* stays approved) | D-U13 (Pilot U-1 / Minimal / Extended) |

## Author approval: universal role architecture (4 October 2026, second ruling)

**Approved principles** (author's numbering):
1. Role-first architecture.
2. Role Profile = industry + department + role + specialisation + seniority.
3. Role Instance = Role Profile + CEFR + situation + stakeholder + communication function.
4. The seven-layer L0–L6 content architecture.
5. Role Core + Industry Context separation.
6. 402 roles as the **initial** registry, not a maximum.
7. Open-ended role addition.
8. The 27-sector registry architecture (count reconciliation below).
9. 156 initial situation templates, expandable.
10. 113 communication functions, expandable.
11. CEFR independent of seniority.
12. Frontline / low-income / entry-level workers as first-class learners.
13. Professional, managerial and leadership communication as separate layers.
14. Teacher as a genuine professional role.
15. Booth Level Officer as a supported public-service role.
16. Optometrist / eye-care roles as supported healthcare roles.
17. Automobile sales and other field-sales roles as supported roles.
18. Digital-first, search-first navigation.
19. Layered generation and de-duplication.
20. Reuse through L0–L6 instead of rewriting complete curricula.
21. The D-R09 review sequence, unchanged.
22. NOT_PERFORMED is never PASS.
23. AI review counts only as AI QA.
24. The existing book remains unchanged.

**Clarifications recorded:**

| # | Clarification | Recorded in |
|---|---|---|
| 1 | **Audio is optional.** The curriculum is fully usable without audio. Audio is architecturally supported as an attachment, can be added later without restructuring, and is not generated now. | Architecture §11, §11.2 |
| 2 | **Bengali/Hindi is a selective support layer.** English → simple English explanation → optional Bengali/Hindi → pronunciation support where appropriate → practice. Lessons are never duplicated automatically. Native review is mandatory when Bengali/Hindi content is created and the requirement applies. Not generated now. | Architecture §11.1 |
| 3 | **Pilot U-1 approved for architecture validation, not publication.** 5 profiles, 14 units. | Architecture §19 |
| 4 | **No specialist-dependent roles in U-1.** Booth Level Officer and Optometrist stay in the registry for a later specialist batch (with Teacher and Field Survey Executive), not generated now. | Architecture §19 |
| 5 | **Count reconciliation.** 27 sectors / 122 industries vs a 26-sector matrix. | Below, and architecture §3.1 |
| 6 | **402 roles are the registry universe, not 402 chapters.** Content is generated as reusable objects and composed instances, only where required. | Architecture §16, §20 |
| 7 | **No page ceiling.** Optimise for relevance, coverage, modularity, reuse, de-duplication, navigation, search, maintainability, generation efficiency and quality. Never delete useful content to save pages. | Architecture §20 |

## Count reconciliation (verified from the files)

| Item | Count | IDs |
|---|---|---|
| Sector records | 27 | SEC-01 … SEC-27 |
| Sectors containing industries | 26 | SEC-01 … SEC-26 |
| Industry records | 122 | IND-0001 … IND-0122 |
| Matrix sector columns | 26 | the codes of SEC-01 … SEC-26 |
| Scope codes (27 + 122 + 62 families) | 211 | — |

- **Why the matrix has 26 columns:** SEC-27 `GEN` (industry-neutral) has no industries, and every role is applicable to it by definition. The matrix generator excludes it **by design**.
- **Same taxonomy:**
  - all 26 matrix column codes are registry sector codes;
  - no registry sector except `GEN` is missing;
  - every sector code used in ROLE-UNIVERSE.csv exists in the registry.
- **No number was changed.** The explanation is recorded in architecture §3.1 and in the registry table note.

## Decision status: D-U01 to D-U16

| # | Decision | Status | Detail |
|---|---|---|---|
| D-U01 | Layered model L0–L6; Role Profile (`RPF`) vs Role Instance (`RIN`) | **APPROVED** | Principles 2, 3, 4, 19, 20 |
| D-U02 | Registry hierarchies and seeded registries | **APPROVED**, with the count reconciliation recorded above (author to confirm it is acceptable) | Principles 6–10; open-ended additions (7) |
| D-U03 | Core modules CM-01…CM-15 | **APPROVED IN PRINCIPLE** (role core + context separation; shared core modules are a pilot test target). The CM list itself stays amendable after the pilot. | Principle 5; pilot test "shared core modules" |
| D-U04 | CEFR scale and first production levels | **PARTLY APPROVED.** CEFR is independent of seniority (principle 11); the pilot uses A1, A2, B1 and B2. **Open:** adopting the full scale (Pre-A1, plus levels, C1, C2) and the order of production after the pilot. | Architecture §9 |
| D-U05 | Responsibility levels, ownership-track scale, employment setting | **PARTLY APPROVED.** Professional, managerial and leadership layers are separate (13), and CEFR is independent (11). **Open:** the exact 12-level list and ranks, and employment setting as a formal attribute (both used by the pilot). | SENIORITY-PROGRESSION-ARCHITECTURE §2 |
| D-U06 | Audio | **APPROVED: optional, not a dependency** (clarification 1) | Architecture §11.2 |
| D-U07 | Scope codes and vocabulary code format `<TYPE>-<SCOPE>-<nnnn>` | **OPEN** | Needed before pilot vocabulary is coded. The pilot can use temporary IDs until then. |
| D-U08 | Bengali/Hindi | **APPROVED: selective support layer**; native review mandatory where applicable; none generated now (clarification 2) | Architecture §11.1 |
| D-U09 | Search languages | **PARTLY APPROVED.** Digital-first and search-first (18). **Open:** whether Bengali/Hindi script and transliteration search are included, and when. | Architecture §15 |
| D-U10 | Content generator and budget rules | **PARTLY APPROVED.** Layered generation and de-duplication (19). **Open:** which model (ChatGPT or another) and the budget cap per batch. | Architecture §17 |
| D-U11 | Job-knowledge, public-procedure and safety policies; disclaimer wording | **OPEN** | Needed before the specialist batch; the pilot uses generic, communication-only job knowledge |
| D-U12 | Characters | **OPEN** | Pilot default if not decided: the learner takes the role, with named stakeholders |
| D-U13 | Pilot | **APPROVED: U-1** (clarification 3). **Open sub-decision D-U13b:** who performs Editorial Review, and the HR practitioner check for P4/P5. | Architecture §19 |
| D-U14 | Pedagogical cycle | **OPEN** | The proposed cycle is used provisionally in the pilot only if the author agrees |
| D-U15 | Priority roles after the pilot | **PARTLY DEFINED.** The next specialist validation batch may include Booth Level Officer, Optometrist, Teacher and Field Survey Executive (not generated now). Pre-generation priorities are open. | Clarification 4 |
| D-U16 | Delivery surfaces and order | **PARTLY APPROVED.** Digital-first and search-first (18). **Open:** website / app / printable role packs, and their order. | Architecture §15 |

## Pilot U-1 (final definition)

| # | Role Profile | Industry | Department | Level / setting | CEFR | Units |
|---|---|---|---|---|---|---|
| P1 | Vegetable Seller (ROL-0081) | VEGM Fresh produce markets | DEP-0048 Own business | Ownership (solo); self-employed | A1 | 3: STM-0020, STM-0021, STM-0034 |
| P2 | Car Sales Executive (ROL-0050) | CARD Car dealerships | DEP-0008 Sales | Executive; formal | B1 + one A2 variant | 3 + 1: STM-0019, STM-0026, STM-0028 + STM-0019 at A2 |
| P3 | Food Delivery Executive (ROL-0157) | FDEL Food delivery | DEP-0026 Last-mile | Executive; gig | A2 | 3: STM-0042, STM-0040, STM-0043 |
| P4 | HR Manager (ROL-0013) | HOTL Hotels & resorts | DEP-0005 HR | Manager | B2 | 2: STM-0143, STM-0127 |
| P5 | HR Manager (ROL-0013) | SOFT Software & IT services | DEP-0005 HR | Manager | B1 | 2: STM-0143, STM-0127 |

**Totals:** 5 profiles, 14 units.

**Not included:**
- no capstones;
- no audio;
- no Bengali/Hindi, so native review is NOT_REQUIRED;
- no specialist-dependent roles.

**Purpose:** architecture validation, not publication. Nothing is compiled or published.

## Files that would be created or modified next (only after the author's next approval)

**Created** (all under `editorial/`, which is excluded from deploy):

| Path | Content |
|---|---|
| `editorial/curriculum/schemas/*.schema.json` | JSON Schemas: sector, industry, department, role-family, role, role-profile, situation-template, communication-function, core-module, unit, conversation, vocabulary, job-knowledge, request, review |
| `editorial/curriculum/registry/` | Registry records converted from the approved CSVs (sectors, industries, departments, families, roles, responsibility levels, CEFR levels, core modules, situation templates, functions, scope codes) |
| `editorial/curriculum/role-profiles/RPF-000001.json` … `RPF-000005.json` | The five U-1 profiles |
| `editorial/curriculum/core-modules/` | CM-03, CM-04, CM-06, CM-11 content needed by U-1 (L2) |
| `editorial/curriculum/situations/`, `conversations/`, `units/` | The 14 U-1 units and their layer objects (L0–L6), all status GENERATED → AI_QA |
| `editorial/curriculum/requests/REQ-…json`, `reviews/REV-…json` | Generation requests and AI QA / editorial review records |
| `editorial/tools/curriculum/validate.py` | Schema and reference validation, collision test, de-duplication check |
| `editorial/tools/curriculum/compose.py` | Composes Role Instances from L0–L6 for review (local preview only; not compiled for the website) |
| `editorial/tools/curriculum/search_test.py` | Runs the pilot search queries against the local data |
| `editorial/PILOT-U1-REPORT.md` | Results against the evaluation measures |

**Modified:**
- `editorial/ROLE-ENGINE-DECISIONS.md` (to record decisions);
- possibly `editorial/CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md` (pilot findings).

**Not touched:**
- `book-data.json`, `reference-index.json`, `index.html`;
- the core tools (`build_print.py`, `render_pdf.js`, `build_reference_index.py`, `apply_corrections.py`);
- the PDF, the covers, the publication gates and `deploy.yml`;
- no `curriculum-data/` at the root (nothing is compiled).

---|---|---|---|
| D-U01 | Layered content model (L0 function exponents → L6 CEFR variant); Role Profile (`RPF`) vs Role Instance (`RIN`, the learning object) | Approve / amend | Universal architecture §1, §16 |
| D-U02 | Registry hierarchies and the seeded registries (402 roles, 62 families, 27 sectors / 122 industries, 50 departments) as the starting point | Approve / amend lists | §2–§4; the CSV registries |
| D-U03 | Core modules CM-01…CM-15 as role-core building blocks | Approve / amend | §7; ROLE-FAMILY-REGISTRY.csv |
| D-U04 | CEFR scale and first production levels | (a) Pre-A1–B2 first, for frontline reach; (b) A2–C1 first, nearest to the core book; (c) other | §9 |
| D-U05 | Responsibility levels + ownership-track scale + employment setting as separate attributes | Approve / amend | §10 |
| D-U06 | Audio | (a) produce audio from the pilot onward; (b) text-only pilot, audio before frontline release; (c) no audio (then no listening claims, and frontline delivery is weaker) | §11 |
| D-U07 | Scope codes and vocabulary code format `<TYPE>-<SCOPE>-<nnnn>` | Approve / amend | §3; ROLE-VOCABULARY-ARCHITECTURE |
| D-U08 | Bengali/Hindi depth and reviewers | (a) include L1 support and source native reviewers; (b) English-only pilot (native review NOT_REQUIRED); (c) include L1 support, accepting that such units cannot be APPROVED until reviewed | §11, §18 |
| D-U09 | Search languages | (a) English + Indian-English aliases first; (b) also Bengali/Hindi script and transliteration (needs native review) | §15 |
| D-U10 | Content generator and budget | ChatGPT / other; budget cap per batch | §17 |
| D-U11 | Job-knowledge, public-procedure and safety policies, and disclaimer wording | Approve / amend | §11, §13; JOB-KNOWLEDGE-LAYER |
| D-U12 | Characters | (a) recurring characters per sector; (b) the learner as the role; (c) mixed | — |
| D-U13 | Pilot | (a) **U-1** (5 profiles, 14 units); (b) **Minimal** (3 profiles, 7 units); (c) **Extended** (U-1 + Booth Level Officer + Optometrist + capstones; needs PUB and MED specialists); plus who performs Editorial Review | §19 |
| D-U14 | Pedagogical cycle | Approve proposed cycle / amend | §20 |
| D-U15 | Priority roles for pre-generation after the pilot | List | §17 |
| D-U16 | Delivery surfaces and order | Website / app / printable role packs | §15 |

---|---|---|
| D-R02 | Role model: role = reusable job with a default level and ladder; role instance = role + industry + department + responsibility level | Architecture §3; CONTENT-DATA-SCHEMA §5 |
| D-R03 | Responsibility levels and ranks, including Founder/Entrepreneur as a separate ownership track | SENIORITY-PROGRESSION-ARCHITECTURE §2 |
| D-R04 | CEFR: support A1–C2 in data; which ranges are produced first | SENIORITY §5 |
| D-R05 | Scope codes (one shared namespace for industries and role families) | ROLE-VOCABULARY-ARCHITECTURE §2 |
| D-R06 | Industry list, including `GEN` (industry-neutral) and `SMB` (start-ups and small business) | Architecture §1, §6; ROLE-INDUSTRY-MATRIX.csv |
| D-R08 | Content generator: ChatGPT (or another model) under the contract; IDs always assigned by the repository | CHATGPT-CONTENT-ENGINE-SPEC |
| D-R10 | Job-knowledge boundaries and disclaimer wording | JOB-KNOWLEDGE-LAYER §1 |
| D-R11 | Characters for engine content | Architecture §12 |
| D-R12 | Exact pilot selection | Options below |

---

## D-R12: exact options (SUPERSEDED, 4 October 2026; kept for the record; see D-U13)

**Not selected.** Each option meets the approved principle: one cross-industry role in several industries, plus one industry-specific role. The facts below come from the proposed matrices and specifications.

### Part 1: pilot set

**Option A** (the author's example structure)

| | |
|---|---|
| Cross-industry role (instances) | HR Manager (ROL-0013, Manager) × HOSP, TECH, BPO |
| Industry-specific role | Restaurant Manager (ROL-0006, Manager) × HOSP |
| What it tests | Same role, three industries that each require specialisation (matrix: all three "Industry-specific specialization required"). Shows whether situations differ at situation level, not just in nouns. Manager layer in both roles. |
| Specialist and native review needed | HR practitioner (employment-law-adjacent statements); BPO data-protection only if call data appears. Native review only if Bengali/Hindi is used. |
| Core links | Manager layer reuses L5 (feedback, coaching, delegation) and L4 (negotiation, conflict, decisions). Restaurant Manager also connects to the core's hotel setting. |

**Option B** (entry level, service)

| | |
|---|---|
| Cross-industry role (instances) | Customer Service Executive (ROL-0022, Executive) × HOSP, BANK, BPO |
| Industry-specific role | Front Office Executive (ROL-0001) × HOSP |
| What it tests | Operational layer; the remedies allowed differ by industry (hotel goodwill vs banking policy limits vs BPO escalation matrix) |
| Specialist and native review needed | **Banking compliance specialist required** (BANK); BPO data protection |
| Core links | L2 M7, L3 M5 (customer service and complaints) |

**Option C** (operations)

| | |
|---|---|
| Cross-industry role (instances) | Operations Manager (ROL-0021, Manager) × HOSP, BPO, LOGI |
| Industry-specific role | Restaurant Captain (ROL-0004, Supervisor) × HOSP |
| What it tests | Manager layer (cross-industry) + supervisory layer (industry-specific); metrics-driven situations |
| Specialist and native review needed | Logistics specialist (LOGI); BPO data protection |
| Core links | L2 M1 (updates), L3 M2 (reports), L4 M6 (crisis) |

**Option D** (team leadership plus education)

| | |
|---|---|
| Cross-industry role (instances) | Team Leader (ROL-0023, Team Leader) × BPO, RETL, TECH |
| Industry-specific role | School Teacher (ROL-0038) × EDU |
| What it tests | Supervisory layer; new teaching functions (CFN-0082–0084) |
| Specialist and native review needed | **Safeguarding review** (EDU); BPO data protection |
| Core links | L5 M1–M2 (delegation, feedback); teaching functions are new in the engine |

### Part 2: CEFR target per instance

| Option | CEFR |
|---|---|
| (i) | B2 for all manager instances; B1 for executive/supervisor instances |
| (ii) | One CEFR level for the whole pilot (state which) |
| (iii) | Two levels for one instance (e.g. HR Manager · HOSP at B1 and B2), to test the independence of the two axes (SENIORITY §5) |

### Part 3: pilot depth per instance

| Option | Depth | Purpose |
|---|---|---|
| (a) | **Slice:** orientation unit + 3 situation units + capstone | Tests the pipeline, the role-core / industry-context split and the QA gates at the smallest useful size |
| (b) | **Full role-instance curriculum:** the coverage targets in ROLE-CONTENT-BLUEPRINT §3 (16–18 units for a manager instance, 10–12 for an executive instance) | Tests completeness and claim tier R2 |

### Part 4: content generator for the pilot

Ties to D-R08: ChatGPT under the contract, or another named model.

### Part 5: review availability for the pilot

**Under D-R09, pilot content can reach APPROVED only if the required reviews are actually performed.** Because no separate proofreader or native reviewer is available, choose one:

| Option | What it means |
|---|---|
| (x) | The author or a named editor performs editorial review |
| (y) | The pilot runs to AI_QA / EDITORIAL_REVIEW only and is never compiled or published (a pipeline test) |
| (z) | Reviewers are sourced first |

**For Option A specifically:** if Bengali/Hindi support is omitted from the pilot, native review becomes NOT_REQUIRED for it.

---

## Author final approval: U-1 pre-build decisions (4 October 2026, third ruling)

This ruling supersedes the "Decision status" table above where they differ.

| # | Ruling | How it is implemented in `editorial/curriculum/` |
|---|---|---|
| D (counts) | **APPROVED:** 27 sectors (SEC-01…27), 122 industries (IND-0001…0122), GEN without industries, 26-column matrix, 211 scope codes. Do not change. | `build_registry.py` asserts these counts; `validate.py` re-checks them |
| D-U03 | **APPROVED FOR THE PILOT;** revisable after U-1. Findings are documented, never applied silently. | `registry/core-modules.json` status "APPROVED_FOR_PILOT" |
| D-U04 | **APPROVED:** Pre-A1, A1, A2, B1, B2, C1, C2. Plus levels only as optional, justified extensions. Seniority never determines CEFR. | `registry/cefr-levels.json` (7 standard levels) |
| D-U05 | **APPROVED (principle):** responsibility ≠ proficiency; employment setting separate; the 12-level registry stays extensible; non-corporate work is representable | `responsibility-levels.json` (ranked, ownership track with scale); `employment-settings.json` |
| D-U07 | **APPROVED:** `V-<SCOPE>-<NUMBER>`; existing codes unchanged and never recycled or renumbered; automatic validation against the live reference index; reuse instead of duplicates; automatic collision rejection | `ingest.py` and `validate.py` |
| D-U09 | **APPROVED:** search-first in English (roles, industries, situations, job aliases, registered local names). Bengali/Hindi search supported later; none generated now. | `search_test.py` |
| D-U10 | **APPROVED:** ChatGPT is the curriculum-generation engine; the repository / Claude Code layer does request construction, validation, de-duplication, IDs, retrieval, composition, QA tooling, storage and version control. **Claude Code does not generate curriculum content.** Per-batch limits, size limits, usage logging, duplicate-generation detection, regeneration prevention, revise-in-place and retrieval-before-generation. **No global budget.** | `plan.py`, `ingest.py`, `config/pilot-u1.json` |
| D-U11 | **APPROVED:** job knowledge for realism only; specialist review where applicable; traceable facts; no invented safety instructions or public procedures; political neutrality | Request policies; U-1 constraints (e.g. test-drive unit excludes CFN-0108) |
| D-U12 | **APPROVED:** hybrid characters (role-specific realistic characters + reusable stakeholder archetypes); Arif untouched | `registry/stakeholder-archetypes.json`; request policy |
| D-U13b | **APPROVED:** AI QA by the pipeline; **Editorial Review by the author**; Specialist NOT_REQUIRED; Native NOT_REQUIRED; U-1 never PUBLISHED | `config/pilot-u1.json → reviewPolicy`; four separate REV records per object |
| D-U14 | **APPROVED for new role content:** Context → Notice → Understand → Guided Practice → Role Practice → Performance Task → Feedback → Review/Retrieval. Not claimed for the existing book. | `schemas/unit.schema.json` sections |
| D-U15 | Full registry kept. Next specialist-validation batch may include Booth Level Officer, Optometrist, School Teacher and Survey Enumerator (not generated in U-1). | — |
| D-U16 | **APPROVED:** digital-first. Order: structured source → web → mobile/app → search and role navigation → printable role packs → print editions if desired. The structured repository is the source of truth. | — |
| U-1 | **APPROVED FOR GENERATION** as an architecture-validation prototype: 5 profiles, 14 units; no capstones, audio or Bengali/Hindi | `config/pilot-u1.json`; build report in `editorial/PILOT-U1-REPORT.md` |

**Next step:** see `editorial/PILOT-U1-REPORT.md`: the U-1 infrastructure is built; ChatGPT generation (REQ-000001…000004 first) and the author's Editorial Review follow.
