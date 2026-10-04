# Career English: Universal Role-Based Professional English Engine

> **Update (4 October 2026):** extended and, where they differ, superseded by [CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md](CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md). The superseded parts are the role-instance definition, the 48-role and 15-industry lists, the pilot options and any page ceiling. D-R01, D-R07 and D-R09 remain approved.

**Architecture specification only.**
- No content is generated here, and the existing book is untouched.
- Nothing is committed or pushed.
- Every design choice that needs the author's approval is listed in section 12.

This document is the entry point. The detail lives in 13 companion files:

| File | Covers |
|---|---|
| [SENIORITY-PROGRESSION-ARCHITECTURE.md](SENIORITY-PROGRESSION-ARCHITECTURE.md) | The two axes (English level × responsibility); responsibility levels; designations; Manager, GM/Director, MD/Entrepreneur layers; teacher ladder |
| [COMMUNICATION-FUNCTION-LIBRARY.md](COMMUNICATION-FUNCTION-LIBRARY.md) | The reusable communication functions (CFN), linked to existing core lessons |
| [CONVERSATION-ENGINE-SPEC.md](CONVERSATION-ENGINE-SPEC.md) | The conversation record: the central learning object |
| [JOB-KNOWLEDGE-LAYER.md](JOB-KNOWLEDGE-LAYER.md) | The contextual job knowledge that makes the English meaningful |
| [ROLE-VOCABULARY-ARCHITECTURE.md](ROLE-VOCABULARY-ARCHITECTURE.md) | The six vocabulary layers, codes and de-duplication |
| [ROLE-CONTENT-BLUEPRINT.md](ROLE-CONTENT-BLUEPRINT.md) | What one role curriculum contains and how it is sequenced |
| [INDUSTRY-ADDITION-BLUEPRINT.md](INDUSTRY-ADDITION-BLUEPRINT.md) | Procedure: add an industry with no architecture change |
| [ROLE-ADDITION-BLUEPRINT.md](ROLE-ADDITION-BLUEPRINT.md) | Procedure: add a role with no architecture change |
| [CONTENT-DATA-SCHEMA.md](CONTENT-DATA-SCHEMA.md) | Every entity, its fields and stable IDs; repository layout |
| [CHATGPT-CONTENT-ENGINE-SPEC.md](CHATGPT-CONTENT-ENGINE-SPEC.md) | The exact input/output contract between the content generator and the repository |
| [ROLE-QA-SPEC.md](ROLE-QA-SPEC.md) | The 11 QA checks, specialist review and status workflow |
| [ROLE-INDUSTRY-MATRIX.csv](ROLE-INDUSTRY-MATRIX.csv) | 48 roles × 15 industries |
| [ROLE-DEPARTMENT-MATRIX.csv](ROLE-DEPARTMENT-MATRIX.csv) | 48 roles × 22 departments, including industry-dependent placements |

## 1. Inspection results that shape this design

| Repository fact (inspected 4 October 2026) | Design consequence |
|---|---|
| `book-data.json` is the single source for the core book: 5 levels, 40 modules, 196 units, an array of levels with HTML fields. It is verified as baseline `61c769f` + logged corrections. | The core is **referenced, never modified**. Engine content lives in separate files. |
| `reference-index.json` has 926 codes in 8 types. The website, index builder and print builder recognise codes with `\b(V\|PAT\|GIC\|CF\|TL\|MIS\|TIP\|P)-\d{3,4}\b`. | New codes use `<TYPE>-<SCOPE>-<nnnn>`. All 40 proposed scope codes × 8 types were tested: none is mistaken for a core code. (`IND-IT-V-0001`-style codes would collide and are rejected.) |
| **The deploy workflow uploads the whole repository root to the public website**, excluding only `.git*`, `.github/**`, `README.md`, `.gitignore` and `editorial/**`. | A top-level `/curriculum` folder **would be published to the live site** on the next deploy. Unreviewed DRAFT source must live under `editorial/` (section 7). Only built, approved output belongs at the root. |
| The website (`index.html`) loads JSON at runtime and stores progress per unit ID in browser storage. | The engine publishes compiled JSON. Unit IDs must be stable and globally unique. |
| The earlier architecture (`MULTI-INDUSTRY-EXPANSION-ARCHITECTURE.md`, not yet approved) organised content **industry first**. | **This specification replaces that organising principle with role first.** Its claim-control tiers, QA gates, page-scale model and skill registry (SK-01…SK-25) are kept. Where the two differ (organisation, IDs, file layout), this specification prevails if approved (D-R01). |
| Author's earlier statement: no separate human proofreader or native-language reviewer will be available. | The QA workflow records those checks as **NOT PERFORMED** rather than passing them. Claims depending on them stay blocked (ROLE-QA-SPEC). |

## 2. Master architecture

```
CAREER ENGLISH
├── UNIVERSAL PROFESSIONAL CORE ........ existing book (book-data.json), unchanged
│     skills SK-01…SK-25 and communication functions CFN-* point INTO core lessons
│
└── PROFESSIONAL ROLE ENGINE
      ├── INDUSTRY ............... context: terminology, stakeholders, risks, processes, documents
      ├── DEPARTMENT / FUNCTION .. where the role sits in that industry's organisation
      ├── ROLE FAMILY ............ the kind of work (HR, Finance, Front Office, Teaching …)
      ├── ROLE / DESIGNATION ..... the reusable job (HR Manager, Teacher, Restaurant Captain …)
      ├── SENIORITY .............. responsibility level (axis B); designations map onto it
      ├── ROLE INSTANCE .......... role + industry + department + responsibility level (+ local title)
      │     ├── RESPONSIBILITIES . job functions the instance performs
      │     ├── STAKEHOLDERS ..... whom the instance talks to
      │     ├── JOB KNOWLEDGE .... the contextual knowledge needed to communicate
      │     └── SITUATIONS ....... the instance's situation library (22 categories)
      │           └── COMMUNICATION FUNCTIONS (CFN) ... what the speaker is doing with language
      │                 └── CONVERSATION (central object) + EMAIL/DOCUMENT + MEETING + PRESENTATION
      │                       ├── VOCABULARY (6 layers) · EXPRESSIONS · GRAMMAR IN CONTEXT (core GIC)
      │                       └── PRACTICE → ROLE-PLAY → PERFORMANCE TASK → ASSESSMENT / CAPSTONE
      └── ENGLISH LEVEL (CEFR A1–C2) ....... axis A, independent of seniority
```

**The design principle in one line:** the **role** says *what* must be communicated; the **industry** says *in what world*; **seniority** says *with what responsibility*; **CEFR** says *in what language*. Each is a separate, data-driven dimension, so none is hard-coded.

## 3. Entity model

```
industry 1─* department_in_industry *─1 department
role_family 1─* role *─* department      (default + industry-specific placements)
role 1─* role_instance *─1 industry
role_instance *─1 department ; role_instance *─1 responsibility_level
designation *─1 responsibility_level      (designation = title; may be industry-specific)
role 1─* responsibility (job_function)
role_instance 1─* situation *─* communication_function
situation 1─* conversation | document | meeting | presentation
job_knowledge  attaches to role (core) | industry (context) | role_instance (specific)
vocabulary     scoped to core | industry | role_family ; tagged with department, role, situation
assessment / capstone  attach to role_instance (+ CEFR target)
content_variant  = (any content object) × CEFR level
```

**Key separation (brief §3–5):**
- A **role core** holds the role's universal communication requirements, on the `role` record.
- An **industry context** holds the modifications for that industry, on the `industry` record and its industry-specific overlays.
- A **role instance** combines the two and is where content is generated.

Content changes **at the situation level**:
- an IT HR Manager's situations (technical-skills hiring, remote teams) are different situations from a BPO HR Manager's (high-volume batches, attrition);
- they are not the same situation with different nouns.

## 4. The two independent axes

- **Axis A: English level.** A1 → C2. It controls the *language*: range, accuracy demands, text length, scaffolding, speed.
- **Axis B: Professional responsibility.** Trainee → … → MD / Founder. It controls the *content*: what is communicated, to whom, with what accountability, time horizon and evidence.

Every content object stores both. Any combination is allowed. A B1 Front Office Manager receives managerial content in B1 language with scaffolds; a C1 Front Office Executive receives executive-level content in C1 language. Rules are in SENIORITY-PROGRESSION-ARCHITECTURE §5.

## 5. Leadership layers

These are distinct function sets, not harder words.

| Layer | Responsibility levels | What changes | Spec |
|---|---|---|---|
| Operational | Trainee → Senior Executive / Specialist / Coordinator | Serve, report, request, follow procedure | Seniority §3 |
| Supervisory | Supervisor, Team Leader, Captain | Coordinate a shift, brief, handle escalations, support staff | Seniority §4 |
| **Manager English** | Assistant Manager → Senior Manager / Department Head | Delegate, manage performance, allocate resources, report upward, coordinate across departments, lead change | Seniority §6 |
| **GM / Director English** | Director, General Manager | Business reviews, budgets, risk, cross-functional decisions, board and owner communication | Seniority §7 |
| **MD / Entrepreneur English** | Managing Director, Founder, Entrepreneur | Vision, strategy, investment, partnerships, culture, pitching, public representation, kept as professional English, not business school | Seniority §8 |

## 6. How the eight example requests resolve

Each request becomes a **generation spec**: industry + department + role + responsibility level + CEFR + situation + communication functions. Each is resolved to stable IDs before any content is generated (see the ChatGPT engine spec).

| # | CEFR | Industry | Department | Role (family) | Responsibility | Situation category | Main functions |
|---|---|---|---|---|---|---|---|
| 1 | B1 | HOSP | Front Office | Front Office Executive (FO) | Executive | Complaint | Acknowledge, apologise, offer remedy within authority, confirm, escalate |
| 2 | B2 | HOSP | Food & Beverage | Restaurant Manager (FNB) | Manager | Team communication / Meeting | Brief a team, allocate, set standards, motivate |
| 3 | B2 | TECH | Human Resources | HR Manager (HR) | Manager | Manager communication | Discuss priorities, negotiate trade-offs, recommend |
| 4 | B2 | BPO | Operations | Operations Manager (OPS) | Manager | Performance | Present metrics, diagnose, agree actions |
| 5 | B1 | EDU | Academic | School Teacher (TEACH) | Executive-equivalent | Stakeholder (parent) | Report progress, give balanced feedback, agree next steps |
| 6 | C1 | HOSP | Management | General Manager (MGMT) | General Manager | Presentation / stakeholder | Business review to ownership, explain variance, recommend |
| 7 | C1 | GEN (corporate) | Executive Office | Managing Director (LEAD) | Managing Director | Change | Explain why, what changes, what stays, address concern |
| 8 | B2 | SMB | Founder's Office | Entrepreneur / Founder (ENTR) | Founder | Stakeholder / negotiation | Pitch problem → solution → value → ask |

All eight are expressible with the entities above. None needs a schema change.

## 7. Repository layout (proposed)

```
/ (repository root = published website; unchanged)
  book-data.json, reference-index.json, index.html, covers ...    ← core, untouched
  curriculum-data/            ← FUTURE build output only: approved, compiled JSON for the website
                                 (created by a build step after approval; nothing DRAFT here)
editorial/                    ← excluded from deploy
  curriculum/                 ← AUTHORING SOURCE (proposed)
    registry/                 industries, departments, role_families, responsibility_levels,
                              designations, cefr_levels, scope_codes, situation_categories,
                              communication_functions, skills (SK), stakeholders_types
    roles/                    one JSON file per role             (ROL-xxxx.json)
    role-instances/           one file per instance              (RIN-xxxxxx.json)
    situations/               per instance folder                (SIT-xxxxxx.json)
    job-knowledge/            JKN items by scope
    vocabulary/               by scope code (core refs, industry, role family)
    conversations/            CNV-xxxxxx.json (+ CEFR variants)
    documents/  meetings/  presentations/
    assessments/  capstones/
    requests/                 generation requests sent to the content engine (audit trail)
    reviews/                  QA and review reports
    schemas/                  JSON Schemas for all of the above
  tools/                      existing tools; future validator/compiler would live here
```

**Why not `/curriculum` at the root, as in the brief's example?** The deploy workflow would publish it, including DRAFT and unreviewed content.

| Option | What it means |
|---|---|
| (a) **Proposed** | Source under `editorial/curriculum/` (already excluded from deploy); compiled, approved output in `curriculum-data/` |
| (b) | Root `/curriculum` plus a new deploy exclusion. Requires changing `deploy.yml`, which earlier instructions put off-limits without explicit approval. |

Decision D-R07.

**One file per record:**
- small diffs;
- parallel authoring without merge conflicts;
- generated content enters through reviewable pull requests or local commits;
- the compiler can validate each record independently.

## 8. Extensibility guarantees

| Addition | What is added | Architecture change |
|---|---|---|
| Industry (e.g. Pharmaceuticals) | Industry record + scope code + departments-in-industry + role instances + context knowledge + vocabulary | None (INDUSTRY-ADDITION-BLUEPRINT) |
| Role (e.g. Procurement Manager) | Role record + role-core functions + placements + instances | None (ROLE-ADDITION-BLUEPRINT) |
| Seniority or designation level | Responsibility-level record with a sortable `rank`, or a designation record | None. Levels are data, ordered by rank, never by a hard-coded list. |
| Department or role family | Registry record + scope code | None |
| Communication function | Library record | None |
| CEFR sub-level (e.g. B1+) | `cefr_levels` record | None |

## 9. Relation to the existing core book

- **The core book is unchanged.** Arif's story, lessons, codes, PDF, covers and gates are untouched.
- **Core lessons are referenced** through `skills` (SK-01…25) and `communication_functions.coreRefs`. Every engine lesson can show "Learn the skill: Level 3 · Lesson 1.5".
- **Core vocabulary codes are reused**, never duplicated (ROLE-VOCABULARY-ARCHITECTURE).
- **The core book's own publication path** (human proofread NOT PERFORMED, native review NOT PERFORMED, approval NO) is independent of the engine.

## 10. Claims

The claim-control tiers from the earlier architecture apply, now per **role instance** as well as per industry:
- "includes HR Manager English for IT" requires the role-instance tier;
- "covers IT" requires the industry tier.

No claim may exceed what the data and QA status support. ROLE-QA-SPEC §6 sets the role-instance thresholds.

## 11. Roadmap (no work starts before approval)

| Phase | Output |
|---|---|
| 0. Approval | Decisions D-R01…D-R12 (section 12), plus still-open decisions from `MULTI-INDUSTRY-AUTHOR-DECISIONS.md` |
| 1. Registry and schemas | Registries filled (industries, departments, families, levels, CEFR, scope codes, CFN library); JSON Schemas; a validator; no learner content |
| 2. Pilot role instances | 2–3 instances across two industries sharing one role (e.g. HR Manager in HOSP and TECH), proving the role-core/industry-context split; full QA |
| 3. Generation pipeline | Request/response contract live; review reports; compiled output |
| 4. Website integration | Level → industry → department → role → seniority → situation navigation; CEFR filter |
| 5. Scale | More roles and industries by blueprint |
| 6. Publishing | Per the publishing decision; claims from the register |

## 12. Decisions needing author approval (new in this specification)

**Status (4 October 2026):** D-R01, D-R07 and D-R09 are APPROVED; D-R12 has its principle approved and its selection pending; the others are pending. See [ROLE-ENGINE-DECISIONS.md](ROLE-ENGINE-DECISIONS.md), which also gives the exact D-R12 options.

| # | Decision | Options |
|---|---|---|
| D-R01 | Adopt role-first organisation (this spec), superseding the industry-first organisation of the earlier architecture | Yes / no / hybrid |
| D-R02 | Role model: role = reusable job with a default level and ladder; instance = role + industry + department + level | Approve / alternative |
| D-R03 | Responsibility levels and ranks (Seniority §2), including whether Founder/Entrepreneur is a separate ownership track | Approve / edit |
| D-R04 | CEFR range: support A1–C2 in data, and decide which ranges are produced first (the core book's proposed range is A2+–C1) | Range and order |
| D-R05 | Scope codes for vocabulary (industries and role families share one namespace; e.g. industry `TECH`, function `ITF`) | Approve / edit |
| D-R06 | Industry list including `GEN` (industry-neutral) and `SMB` (start-ups and small business) | Approve / edit |
| D-R07 | Source location: `editorial/curriculum/` (excluded from deploy) or root `/curriculum` with a deploy-exclusion change | (a) / (b) |
| D-R08 | Content generator: ChatGPT (or another model) under the contract in CHATGPT-CONTENT-ENGINE-SPEC; IDs always assigned by the repository | Approve |
| D-R09 | Human review policy, given that no separate proofreader or native reviewer is available: which statuses may be published while marked NOT PERFORMED | Policy |
| D-R10 | Job-knowledge boundaries and the disclaimer wording ("not certification") | Approve |
| D-R11 | Characters for engine content (named recurring characters per industry, or the learner as the role) | Choice |
| D-R12 | The first pilot role instances | Choice |

**Exact next step:** the author answers D-R01…D-R12. Nothing is implemented until then.
