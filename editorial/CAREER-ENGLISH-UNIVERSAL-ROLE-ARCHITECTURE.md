# Career English: universal role architecture

**Status: ARCHITECTURE PRINCIPLES APPROVED by the author (4 October 2026), with clarifications on audio, Bengali/Hindi, pilot U-1, counts and book size. Open decisions remain** (see [ROLE-ENGINE-DECISIONS.md](ROLE-ENGINE-DECISIONS.md)). Architecture only.
- No curriculum content has been generated.
- `book-data.json`, the lessons, the PDF, the covers and the publication gates are unchanged.
- Nothing is committed or pushed. HEAD is `5685b52`.

**Goal (author, 4 October 2026):**

> "Any working person, from almost any legitimate field, should be able to open Career English and find English directly relevant to their own work."

**Relation to earlier documents:**
- This document **supersedes** `ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE.md` and its companions wherever they differ: the role-instance definition, registry sizes, the pilot, and any page ceiling.
- Everything approved there still holds:
  - **D-R01**: role first;
  - **D-R07**: source under `editorial/curriculum/`;
  - **D-R09**: the strict review gates.
- Decision status is in [ROLE-ENGINE-DECISIONS.md](ROLE-ENGINE-DECISIONS.md).

**Registries** (generated, validated, proposed):

| File | Content |
|---|---|
| [ROLE-UNIVERSE.csv](ROLE-UNIVERSE.csv) | 402 roles (seed; open-ended) |
| [ROLE-FAMILY-REGISTRY.csv](ROLE-FAMILY-REGISTRY.csv) | 62 role families in 11 groups, with core modules |
| [INDUSTRY-REGISTRY.csv](INDUSTRY-REGISTRY.csv) | 27 sectors → 122 industries |
| [DEPARTMENT-REGISTRY.csv](DEPARTMENT-REGISTRY.csv) | 50 departments / functions |
| [SITUATION-LIBRARY.csv](SITUATION-LIBRARY.csv) | 156 situation templates in 25 categories |
| [COMMUNICATION-FUNCTION-LIBRARY.csv](COMMUNICATION-FUNCTION-LIBRARY.csv) | 113 functions in 16 groups |
| [ROLE-INDUSTRY-MATRIX.csv](ROLE-INDUSTRY-MATRIX.csv) | 402 roles × 26 sectors (10,452 cells): every sector except `GEN` (see §3.1) |

---

## 1. Final architecture

```
CAREER ENGLISH (digital-first; no page ceiling)
├── UNIVERSAL PROFESSIONAL CORE ......... existing 5-level book, unchanged; linked, never copied
└── UNIVERSAL ROLE ENGINE
      REGISTRIES (data, open-ended)
        sectors → industries → (segments as tags)        departments / functions
        role-family groups → role families → roles → specialised roles (inherit) → designations / aliases
        responsibility levels (ranked) · employment settings · CEFR levels · stakeholder types
        situation categories → situation templates      function groups → communication functions
        core modules (reusable role-core building blocks)
      CONTENT LAYERS (inherit top-down; each layer stores only what is new)
        L0 function exponents (per CEFR) ............ universal language for a function
        L1 situation template content .................. universal model for a situation
        L2 core-module content ........................ e.g. CM-03 Selling: needs → explain → objections → close
        L3 role-core content .......................... what the role does in that situation
        L4 context overlay ............................ industry / department / specialisation / employment setting
        L5 seniority overlay .......................... responsibility, audience, accountability
        L6 CEFR variant ............................... language and scaffolding
      LEARNING OBJECT = ROLE INSTANCE (composed at compile time from L0–L6)
        industry + department + role + specialisation + seniority + CEFR + situation + stakeholder + function
```

### Terminology change (requested by the author)

| Term | Meaning now | Meaning in the earlier documents |
|---|---|---|
| **Role Profile** (`RPF`) | Industry + department + role + specialisation + seniority (+ employment setting). The reusable context bundle. | This was called "role instance" (`RIN`) |
| **Role Instance** (`RIN`) | **The fundamental learning object:** Role Profile + CEFR + workplace situation + stakeholder + communication function | — |

A Role Instance is **composed** from the layers. It is never authored from scratch, so the number of possible instances can be huge without duplicate content.

## 2. Role hierarchy

```
family group (11) → role family (62) → role (402 seeded) → specialised role (inherits; e.g. Car Sales Executive ← Sales Executive)
                                                       → designations / local titles / aliases (search only)
```

- **Roles are open-ended records.** The 402 seeded roles are a starting registry, not a limit.
  - 48 role IDs from the earlier proposal are kept unchanged (`ROL-0001`…`ROL-0048`).
  - New roles start at `ROL-0049`.
- **Inheritance:** a specialised role names a parent and inherits its role core, then adds its own situations, vocabulary and job knowledge. Examples:
  - Medical Representative ← Field Sales Executive ← Sales Executive;
  - Vegetable Seller ← Street Vendor;
  - Optical Store Manager ← Store Manager.
- **The 11 family groups:**
  1. Frontline commerce & customer service
  2. Field, mobile & delivery work
  3. Operations, trades & production
  4. Hospitality, food & travel
  5. Health & care
  6. Education & training
  7. Public, community & safety services
  8. Business functions
  9. Technology & data
  10. Media, marketing & creative
  11. Management, leadership & ownership

## 3. Industry hierarchy

```
sector (27, incl. GEN = industry-neutral) → industry (122) → segment (tag, e.g. "wedding catering", "fibre installation")
```

### 3.1 Count reconciliation (verified from the files, 4 October 2026)

| Item | Count | IDs |
|---|---|---|
| Sector records in INDUSTRY-REGISTRY.csv | **27** | SEC-01 … SEC-27 |
| Sectors that contain industries | **26** | SEC-01 … SEC-26 |
| Industry records | **122** | IND-0001 … IND-0122, each with a parent among SEC-01 … SEC-26 |
| Sector columns in ROLE-INDUSTRY-MATRIX.csv | **26** | the scope codes of SEC-01 … SEC-26 |
| Scope codes (sectors 27 + industries 122 + role families 62) | **211** | — |

**Why the matrix has 26 sector columns, not 27:**
- SEC-27 `GEN` ("industry-neutral") is a sector record with **no industries**. It is the context for content that belongs to no particular industry, for example a Managing Director addressing staff in a generic organisation.
- Every role is usable in `GEN` by definition, so a `GEN` column would hold the same value in all 402 rows. The matrix generator therefore excludes it **by design**. This is not a data loss.

**Same taxonomy:**
- All 26 matrix column codes equal the scope codes of registry sectors SEC-01 … SEC-26. There are none extra and none missing.
- Every sector code used in ROLE-UNIVERSE.csv exists in the registry.

Neither number was changed.

**Rule for future registries:** the matrix covers every sector that contains industries; `GEN` applicability is implicit for every role.


**Each sector and industry has a unique scope code** (2–5 letters). Industries, sectors and role families share one namespace: 211 codes in all. Checks run on all 211:
- all are unique;
- none equals a code type;
- none is mistaken for a core code by the live code pattern.

**Sectors added beyond the brief's list.** The brief asked which sectors were missing; these were added:
- Energy & Utilities;
- Domestic & Personal Services (domestic workers, caregivers, private drivers);
- Environment, Sanitation & Waste;
- Technical Trades & Field Services (as a sector of its own);
- Mobile & electronics repair; Printing & publishing; Jewellery retail;
- Police & public safety (public-interaction scope only);
- Citizen service centres; Public distribution (ration);
- Banking correspondents and payment agents.

**Candidates noted but not yet added:** mining & quarrying, defence (civilian interaction roles), religious and cultural institutions, legal-aid clinics, shipping crews.

## 4. Department hierarchy

```
function group (Customer-facing · Operations · Support function · Professional/domain · Public service · Leadership · Self-employed)
  → department / function (50) → local name per industry (e.g. "Rooms Division", "Polling station")
```

- The department is **optional for the self-employed.** `DEP-0048` "Not applicable — own business / self-employed" and `DEP-0049` "Household (domestic employer)" exist so that vendors, drivers and domestic workers are first-class records.
- A role has one **primary** department. Placements in other departments are allowed per industry (as in the earlier role × department matrix).

## 5. Situation hierarchy

```
situation category (25) → situation template (156) → contextualised situation (role-core / overlay content) → role instance
```

**Frontline relevance.** 130 of the 156 templates are marked frontline-relevant. The categories include:
- selling and products;
- orders and payment;
- delivery and pickup;
- field visits, surveys and inspections;
- public-service procedures;
- technical work and repair;
- instructions and safety;
- health and care (non-clinical).

**Everything the brief lists is covered:** greeting; questions; directions; products and services; orders; payment; price; bargaining; complaints; refunds; appointments; calls; WhatsApp; email; meetings; field visits; surveys; inspections; site visits; delivery; pickup; late delivery; document checks; reporting; instructions; shift handover; sales; follow-up; after-sales; team briefing; feedback; conflict; escalation; problem solving.

## 6. Communication-function hierarchy

```
function group (16) → function (113) → exponents per CEFR level
```

- **CFN-0001…0084 are unchanged** from the earlier library.
- **29 new functions** (CFN-0085…0113) cover frontline, field and trades work:
  - price; quantity and measures; bargaining; orders; payment and change; payment problems; comparing products; promotions;
  - directions; addresses; arrival and purpose; permission; identity and documents; neutral survey questions; consent; explaining public procedures; refusals; assisting people with disabilities; announcements;
  - problem descriptions; explaining faults; estimates; safety warnings; hazard reports; aftercare;
  - time and dates; appointments; asking for leave.
- **45 of the 113 functions are new in the engine,** meaning the core book does not teach them. The other 68 link to the core lesson where they are taught.
- **Mapping of the brief's list:**

| Brief's function | Library ID(s) |
|---|---|
| greeting | 0001 |
| introducing | 0002 |
| clarifying | 0013 |
| confirming | 0014 |
| requesting | 0019 |
| offering | 0026 |
| explaining | 0012 |
| describing / comparing | 0091 |
| recommending | 0023 |
| persuading | 0059 |
| negotiating | 0062 / 0087 |
| apologising | 0007 |
| refusing politely | 0020 |
| reporting | 0028 |
| updating | 0027 |
| checking | 0015 |
| verifying | 0098 |
| instructing | 0025 |
| coaching | 0071 |
| giving feedback | 0067 |
| receiving feedback | 0068 |
| handling disagreement | 0052 / 0072 |
| problem solving | 0043 / 0044 |
| escalation | 0024 |
| closing | 0005 / 0041 |
| follow-up | 0022 |

## 7. Role core model

**A role core is composed from Core Modules**: 15 reusable building blocks. This is how "the Sales core" is shared by a car salesperson and a vegetable seller without duplication.

| Core module | Content (situation categories / functions) |
|---|---|
| CM-01 Workplace basics | Greetings, introductions, instructions, clarification, time, permission, leave (every role) |
| CM-02 Customer service | Welcome, needs, information, complaints, apology, closing |
| CM-03 Selling | Greeting, needs discovery, questioning, explaining, recommending, objections, negotiation, closing, follow-up, complaints |
| CM-04 Transactions & payment | Price, quantity, orders, payment, change, payment problems |
| CM-05 Field & public interaction | Arrival and purpose, permission, verification, surveys, consent, refusals |
| CM-06 Delivery & mobility | Pickup, address, arrival, delays, missing items, proof of delivery |
| CM-07 Technical work & safety | Problem descriptions, faults, estimates, safety, hazards, aftercare |
| CM-08 Operations & reporting | Updates, problems, incident reports, handover |
| CM-09 Office & digital communication | Email, messaging, calls, meetings, documents |
| CM-10 Team supervision | Briefing, allocating, on-the-spot feedback, shift reports, conflicts |
| CM-11 Management | Delegation, performance, resources, upward reporting, change, crisis |
| CM-12 Executive & ownership | Business reviews, boards and owners, strategy, investors and partners, public representation |
| CM-13 Teaching & training | Instructions, explaining, checking understanding, correction, learner feedback, parents |
| CM-14 Care & patient communication (non-clinical) | Registration, next steps, privacy, families, read-back |
| CM-15 Public procedures | Eligibility, documents, counters, announcements, decisions (neutral, procedure-accurate) |

**How a role core is assembled:**

```
role core = family core modules (ROLE-FAMILY-REGISTRY) + seniority modules (SUP → CM-10; MGR → CM-10/11; DIR/MD → CM-11/12)
          + role-specific additions (situations, functions, job knowledge) + inheritance from the parent role
```

## 8. Industry context model

An **overlay** stores only what changes for a context. Overlay dimensions:
- industry (and segment);
- department;
- specialisation;
- employment setting (formal employer, self-employed, gig/platform, public service, NGO, informal, household).

| Overlay part | Example: Selling (CM-03) in a fish market | … in a car dealership |
|---|---|---|
| Situations added / removed / replaced | + bargaining over weight and freshness; + cleaning/cutting request; − quotation | + test drive; + quotation; + finance options; − bargaining at a stall |
| Stakeholders | Household buyers, restaurant buyers, regulars | Families, first-time buyers, finance executives |
| Constraints | Food safety; cash and UPI; no fixed price list | Pricing authority; finance and insurance disclosures (specialist) |
| Job knowledge | Fish varieties, freshness signs, weights, cuts | Variants, on-road price (meaning), test-drive rules, delivery process |
| Vocabulary | `V-FISHM-…` | `V-CARD-…` |
| Register | Short, oral, friendly; numbers-heavy | Polite, explanatory; documents and follow-up |

**Realism rule** (from ROLE-QA-SPEC check 4): an overlay that only replaces nouns **fails**. The overlay must change at least one situation, constraint or stakeholder.

## 9. CEFR model

- **CEFR levels are registry data:** Pre-A1, A1, A2, A2+, B1, B1+, B2, B2+, C1, C2.
  - Pre-A1 is added for frontline learners. It appears in the CEFR Companion Volume.
  - More levels can be added as records.
- **CEFR is independent of seniority.** Every combination is valid. Examples:
  - A2 Manager: managerial content with scaffolded language and fixed frames for high-stakes moves;
  - C1 Delivery Executive: operational content with richer language.
- **Recommended minimums** for a few situations (e.g. board presentations) are shown as guidance only. They never block a combination.
- **CEFR variants are separate records** (`variantOf`), so one situation can exist at several levels.
- **No CEFR claim** (alignment, certification or endorsement) is made publicly until validation, as the earlier architecture already set out.

## 10. Seniority model

- **12 ranked responsibility levels** (`SEN-0001`…`SEN-0012`, spaced ranks; extensible), as in SENIORITY-PROGRESSION-ARCHITECTURE.
- **The ownership track (`SEN-0012`)** has a `scale` attribute: solo, small team or company.
  - A vegetable seller is *solo*; a start-up founder may be *company*. Enterprise-layer modules apply only at *company* scale.
- **Employment setting is a separate attribute**, not a seniority level:
  - a self-employed electrician and a factory electrician have the same responsibility level but different settings;
  - the setting changes situations (e.g. the self-employed handle pricing and payment themselves).
- **Communication responsibilities change with level,** not just vocabulary. The seniority overlay changes purpose, audience, time horizon, evidence and accountability (SENIORITY §6–9).

## 11. Frontline / low-income worker model (first-class requirement)

| Design element | Rule |
|---|---|
| Entry point | "Find my job" by plain words, local aliases and pictures. No assumption of corporate vocabulary. |
| Units | **Micro-lessons**: one situation, 5–10 minutes, one main function, 5–8 words or phrases |
| Modality | **Text-first and fully usable without audio** (D-U06 approved). Phrases are short and speakable; pronunciation is shown in text (stress marks, simple respelling where useful). **Audio is an optional attachment** (`media.audio[]` on any learning object) that can be added later without restructuring. No audio is generated now. |
| Scaffolding | Sentence frames for every turn; picture/icon cues; numbers, prices and times practised explicitly; slow → natural speed; repeat-after-me |
| Literacy | Reading load kept minimal at Pre-A1/A2. Writing limited to short messages, numbers, names and addresses. |
| Bengali/Hindi support | **Selective support layer** (D-U08 approved; §11.1). Never an automatic duplicate of every lesson. **Native review is mandatory** whenever Bengali/Hindi content is created and the requirement applies (D-R09). None is generated now. |
| Topics | Greeting; introductions; price; quantity; time; location; directions; requests; permission; payment; delivery; customers; reporting problems; complaints; basic safety; instructions; follow-up |
| Dignity | Respectful tone. No "broken English" models. Realistic local settings, names and payment methods (cash, UPI). |
| Device | Mobile-first, low data, short audio; printable phrase cards per role ("role pack") |
| Safety content | Generic only, always "follow your employer's rules and local law". Safety-critical roles are specialist-reviewed (electricians, construction, drivers, delivery riders, gas cylinders, sanitation). |

### 11.1 Bengali/Hindi support layer (D-U08, approved)

**Sequence inside a learning object** (each step optional except the first and last):

**English** (target language) → **simple English explanation** → **optional Bengali/Hindi support** → **pronunciation/delivery support where appropriate** → **practice**

| Rule | Detail |
|---|---|
| Attachment, not duplication | Support is stored as an optional `l1Support` attachment on a specific element (term, phrase, instruction, cultural note), with `bn` / `hi` and a `trigger` |
| Triggers | Difficult concept; false friend; culturally important distinction; common learner error; pronunciation issue; industry term that needs explanation |
| Density | Selectively denser for frontline and lower-proficiency (Pre-A1–A2) objects; lighter at higher levels |
| Workplace terms used in English | Stay in English ("check-in", "UPI", "OTP", "KYC"); the gloss explains, never replaces |
| Both languages | When support is given, Bengali and Hindi are given together, with the same scope |
| Review | Any record with Bengali/Hindi content requires NATIVE_REVIEW; without a named native PASS it cannot be APPROVED. NOT_PERFORMED is never PASS. |
| Now | **No Bengali/Hindi content is generated** in this phase |

### 11.2 Audio (D-U06, approved as optional)

- The curriculum is **complete without audio**. Every task can be done from text.
- **Any** learning object (conversation turn, phrase, vocabulary item, announcement) may later receive `media.audio[]` entries with a voice, CEFR speed, file reference and review status.
- Adding audio changes no IDs, structures or sequences.
- **Listening claims follow audio, not the reverse.** No listening-practice claim may be made for an object without approved audio.
- **No audio is generated now.**

## 12. Professional and leadership model

- **Executive through MD and Founder** use core modules CM-09 to CM-12 plus the seniority overlay, as specified in SENIORITY-PROGRESSION-ARCHITECTURE: Manager English; GM/Director English; MD/Entrepreneur English.
- **The teacher ladder** is Teacher → Senior Teacher → Subject Coordinator → Academic Coordinator → **Vice Principal (added)** → Principal → Academic Director. It uses CM-13 plus seniority modules.

## 13. Role registry design

**One record per role**, with:
- stable ID;
- name;
- family;
- parent role;
- default responsibility level;
- primary department;
- employment settings;
- common sectors;
- sectors where specialisation is required;
- special-role flag;
- specialist-review triggers;
- search aliases;
- status.

**Rules:**
- Names are editable; IDs never change.
- **Aliases** include colloquial Indian English and transliterations (e.g. "sabzi wala", "BLO"). Transliterations are marked **pending native review**.
- **Status values:**
  - SEEDED: in the registry, no content yet;
  - PROFILED: role core and overlays defined;
  - ACTIVE: has approved content.

**Specialist-review triggers** (9 categories):
- MED: medical / clinical;
- FIN: financial regulation;
- SAFE: safety-critical;
- PUB: official public procedure and political neutrality (e.g. Booth Level Officer);
- MIN: minors / safeguarding;
- LEG: legal;
- DATA: personal data;
- FOOD: food safety;
- DRV: driving and traffic safety.

## 14. Major-role coverage

- **402 roles** in 62 families.
- All **14 special roles** are present: Booth Level Officer, Optometrist, Car Sales Executive, Food Delivery Executive, Survey Enumerator, Newspaper Salesperson, Vegetable Seller, Fish Seller, Clothing Salesperson, Small Shop Salesperson, Shopping Mall Sales Associate, Medical Representative, Field Sales Executive and Field Service Technician.
- **Also flagged as special:** Hospital Assistant, School Administrator and Optical Sales Associate (17 in all).
- **All 51 occupations in the author's list** are matched by at least one role (checked automatically).
- **Role × sector matrix:**

| Value | Cells |
|---|---|
| Common | 827 |
| Industry-specific specialization required | 89 |
| Applicable | 1,822 |
| Not applicable | 7,714 |

## 15. Digital navigation model

**Entry paths:**
1. **Search box** (main);
2. **Find my job:** sector → role (with aliases);
3. **Browse by situation:** "I need to…";
4. **Level filter:** CEFR;
5. **Core course:** Levels 1–5.

**Search index fields:**
- role names and aliases;
- industry names and aliases;
- situation templates;
- functions;
- vocabulary terms;
- department;
- seniority;
- CEFR.

Search should tolerate typos, and support Bengali/Hindi script and transliteration once reviewed. Example queries:

| Query | Resolves to |
|---|---|
| "food delivery late order" | ROL-0157 Food Delivery Executive + STM-0042 Informing a customer about a late delivery |
| "vegetable seller English" | ROL-0081 Vegetable Seller role pack (alias "sabzi wala") |
| "car sales customer" | ROL-0050 Car Sales Executive + SC03 Selling & products (STM-0019, STM-0026) |
| "BLO field visit" | ROL-0361 Booth Level Officer + STM-0070 Door-to-door verification / STM-0059 Arriving at a household |
| "nurse patient" | ROL-0318 Staff Nurse + SC25 Health & care (non-clinical) |
| "teacher parent meeting" | ROL-0038 School Teacher + STM-0111 Parent-teacher meeting |
| "hotel check-in" | ROL-0001 Front Office Executive + STM-0050 Checking in a customer or patient at reception |
| "HR interview" | ROL-0013 HR Manager / ROL-0012 HR Executive + STM-0143 Interviewing a candidate (and STM-0142 Job interview as candidate) |

**Facets:** sector, industry, department, role family, role, seniority, employment setting, CEFR, situation category, function, mode.

**Outputs:**
- the website;
- the future app;
- **role packs:** a printable export of one Role Profile across chosen CEFR levels;
- **specialised packs** for organisations.

**Cross-links:** every unit links to its core lesson ("Learn the skill"), related roles ("Also useful for…") and related situations.

## 16. Content reuse and de-duplication model

1. **Retrieve before generating.** Before any content request, the repository searches existing objects, from the most specific layer to the most general (L6 → L0). It reuses whatever already fits.
2. **Store deltas only.** Each layer stores only what differs from the layer above it. A Role Instance is assembled at compile time.
3. **Shared objects:**
   - function exponents (L0) are shared by every role;
   - situation templates (L1) by every role that meets them;
   - core modules (L2) by every family that uses them.
4. **Vocabulary de-duplication:** as in ROLE-VOCABULARY-ARCHITECTURE §4, with scope codes at sector, industry or family level.
5. **Job knowledge** is scoped to role, industry or profile, and reused across instances.
6. **Duplicate detection:** before approval, near-duplicate situations and dialogues are flagged by a similarity check, so the same content is not stored twice under different IDs.

**Illustrative scale** (formula, not a target):
- **Fully duplicated content** would be roughly *role-sector pairs × situations × CEFR levels*. With 916 common or specialised role-sector pairs, about 25 situations each and 6 CEFR levels, that is about 137,000 separately written units.
- **Under the layered model**, what is authored is:
  - L1: 156 situation templates × CEFR levels;
  - L2: 15 core modules;
  - L3: one role core per role (402);
  - L4: overlay deltas per active Role Profile;
  - L6: CEFR variants written only where needed.
- Units are **composed**, not separately written. The number of composed units can grow very large without the stored content growing at the same rate.

## 17. AI generation and cost-control model

| Control | Rule |
|---|---|
| Generation order | Registry data → L0/L1 shared content → L2 core modules → L3 role cores → L4/L5 overlays → L6 CEFR variants. Each step reuses the one before. |
| Demand-led | Pre-generate a priority set (author-chosen roles); generate the rest when needed. Search logs (future) show demand. |
| Batch requests | One request per role core or overlay set, with a shared context pack; never one request per unit when a batch fits |
| Context caching | The same context pack (registries, style, schemas) is reused across a batch |
| Revise, don't regenerate | Fixes use `revise` mode on the specific findings (CHATGPT-CONTENT-ENGINE-SPEC §6); the previous version is kept |
| Delta prompts | Overlay requests send the base object and ask **only for differences** |
| Budget tracking | Every request records model, prompt version, token counts and cost estimate; batches stop at a set budget |
| AI QA first | Automated and model checks before human review, so reviewer time goes to content that already passes basics |

## 18. Review architecture (D-R09, approved)

```
GENERATED → AI QA → Editorial Review → Specialist Review (where required) → Native Review (where required) → APPROVED → COMPILED → PUBLISHED
```

- **NOT_REQUIRED** may be recorded only when a review is genuinely not applicable. Whether it is required follows from the specialist triggers and the presence of Bengali/Hindi script.
- **NOT_PERFORMED is never PASS.** Content with a required review NOT_PERFORMED cannot be APPROVED.
- **AI review is AI QA only.**
- **Specialist triggers are on every role record** (section 13). For example, Booth Level Officer content triggers **PUB**: it must match official procedure, stay politically neutral, and never invent rules.

## 19. Pilot U-1 (APPROVED by the author, 4 October 2026, as an architecture-validation pilot; NOT for publication; not yet generated)

| # | Role Profile | Role ID | Industry (registry) | Department | Responsibility / setting | CEFR | Units (situation templates) |
|---|---|---|---|---|---|---|---|
| P1 | Vegetable Seller | ROL-0081 (← ROL-0080 Street Vendor) | VEGM Fresh produce markets (sector TRADE) | DEP-0048 Own business | SEN-0012 ownership track, scale *solo*; self-employed | A1 | STM-0020 Bargaining over price; STM-0021 Quantity, weight and measures; STM-0034 Taking payment |
| P2 | Car Sales Executive | ROL-0050 (← ROL-0016 Sales Executive) | CARD Car dealerships (sector AUTO) | DEP-0008 Sales | SEN-0003 Executive; formal employer | B1 + **one A2 variant** (of STM-0019) | STM-0019 Discussing price (**same template as P1**); STM-0026 Test drive; STM-0028 Quotation follow-up |
| P3 | Food Delivery Executive | ROL-0157 | FDEL Food delivery (sector MOVE) | DEP-0026 Last-mile | SEN-0003 Executive; gig / platform | A2 | STM-0042 Late delivery; STM-0040 Address-confirmation call; STM-0043 Wrong or missing item |
| P4 | HR Manager | ROL-0013 | HOTL Hotels & resorts (sector HOSP) | DEP-0005 HR | SEN-0008 Manager | B2 | STM-0143 Interviewing a candidate; STM-0127 Addressing underperformance |
| P5 | HR Manager | ROL-0013 | SOFT Software & IT services (sector TECH) | DEP-0005 HR | SEN-0008 Manager | **B1** | STM-0143; STM-0127 (same templates as P4: anti-noun-swap test) |

**Total:** 5 Role Profiles, **14 units**:
- 13 situation units (3 + 3 + 3 + 2 + 2);
- plus 1 CEFR variant (the P2 A2 version of STM-0019).

**Not included:** capstones; audio; Bengali/Hindi content.

**What the pilot must test, and where:**

| Test | Where |
|---|---|
| Frontline English | P1 |
| Field / gig English | P3 |
| Sales English | P1, P2 |
| Retail English | P1 |
| Professional English | P2 |
| Management English | P4, P5 |
| Role reuse | ROL-0013 in P4 and P5 |
| Industry adaptation | P4 vs P5; P1 vs P2 (CM-03 Selling in a market vs a dealership) |
| CEFR independence | P5: manager at B1; P2: same role at B1 and A2 |
| Role / seniority separation | Manager (P4, P5) vs executive (P2, P3) vs owner-solo (P1) |
| Shared communication functions | e.g. CFN-0085 price (P1, P2); CFN-0007 apology (P3) |
| Shared core modules | CM-03 Selling (P1, P2); CM-04 Transactions (P1, P2, P3); CM-11 Management (P4, P5) |
| Genuine industry differences | Anti-noun-swap check, P4 vs P5 and P1 vs P2 |
| Deduplication | Retrieve-before-generate log; reuse ratio |
| Search / navigation | The example queries that fall within the pilot ("vegetable seller English", "car sales customer", "food delivery late order", "HR interview") resolve to pilot units |
| Generation cost control | Requests, tokens and cost per unit recorded; delta requests for P5 against P4 and for the A2 variant against B1 |

**Review plan:**
- **All units:** AI QA, then Editorial Review.
- **P4 and P5 need an HR practitioner check.** Employment-law-adjacent statements are kept generic. Who performs it is still open (D-U13b).
- **P3 driving content** stays communication-only (DRV not triggered).
- **Native review is NOT_REQUIRED for U-1,** because no Bengali/Hindi content is created. If support is added later, NATIVE_REVIEW becomes required for those records.
- **Pilot units are evaluation material.** They may reach APPROVED only through the full D-R09 sequence. Nothing is COMPILED or PUBLISHED as part of the pilot.

**Specialist roles stay out of U-1** (clarification 4). They remain in the registry for a **later specialist validation batch**, not generated now:
- Booth Level Officer (ROL-0361);
- Optometrist / Eye-care Practitioner (ROL-0323);
- School Teacher (ROL-0038);
- Survey Enumerator / Field Survey Executive (ROL-0149).

## 20. Remaining author decisions

These are listed with options in [ROLE-ENGINE-DECISIONS.md](ROLE-ENGINE-DECISIONS.md). They replace the earlier D-R02–D-R06, D-R08, D-R10, D-R11 and the D-R12 options A–D, which are now SUPERSEDED.

| # | Decision |
|---|---|
| D-U01 | Layered content model and the Role Profile / Role Instance terminology |
| D-U02 | Registry hierarchies (sector → industry → segment; family group → family → role → specialised role; departments) and the seeded registries as the starting point |
| D-U03 | Core modules (CM-01…15) as the role-core building blocks |
| D-U04 | CEFR scale (Pre-A1…C2 incl. plus levels); which levels are produced first |
| D-U05 | Responsibility levels, ownership-track scale, and employment setting as a separate attribute |
| D-U06 | Audio: **APPROVED as optional** (§11.2) |
| D-U07 | Scope codes and vocabulary code format (211 codes, collision-tested) |
| D-U08 | Bengali/Hindi: **APPROVED as a selective support layer** (§11.1) |
| D-U09 | Search languages: English, Indian-English colloquial aliases, Bengali/Hindi script and transliteration |
| D-U10 | Content generator (ChatGPT or another model) and budget rules |
| D-U11 | Job-knowledge boundaries and disclaimers, including public-procedure (PUB) and safety policies |
| D-U12 | Characters (recurring characters per sector, or the learner as the role) |
| D-U13 | Pilot: U-1, Minimal or Extended, and its review plan |
| D-U14 | Pedagogical cycle (proposed: Notice → Understand → Controlled → Guided → Freer / role-play → Perform → Review, with spaced retrieval) |
| D-U15 | Priority roles for pre-generation after the pilot |
| D-U16 | Delivery surfaces: website / app / printable role packs, and their order |

**Removed constraint (approved).** The 402 roles are the registry universe, not 402 chapters (clarification 6). No page ceiling applies (author, 4 October 2026). Page-scale figures in earlier documents are informational only.
