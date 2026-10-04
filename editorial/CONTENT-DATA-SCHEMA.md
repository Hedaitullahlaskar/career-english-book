# Content data schema (role engine)

> **Update (4 October 2026):** what this schema calls a "role instance" (`RIN`: role + industry + department + level) is now the **Role Profile** (`RPF`). **Role Instance** (`RIN`) now means the learning object: profile + CEFR + situation + stakeholder + function. Layered composition (L0–L6), core modules, sectors and employment settings are added by [CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md](CAREER-ENGLISH-UNIVERSAL-ROLE-ARCHITECTURE.md) (pending D-U01–D-U05).

**Status: PROPOSAL.**
- Nothing is implemented.
- `book-data.json` and every other existing file are unchanged.

If approved (D-R01), this schema **supersedes** the industry-first schema in `MULTI-INDUSTRY-DATA-SCHEMA.md` for organisation, IDs and layout. It keeps that document's principles:
- the core book is never modified;
- new data lives in separate files;
- code formats are collision-tested.

## 1. Principles

1. **Stable IDs are primary keys.** Names, titles and slugs are editable attributes; nothing references a record by name.
2. **One record per file** in the authoring source (small diffs, parallel work, per-record validation). A compiler builds the published bundles.
3. **Structured content, compiled to HTML.**
   - Conversations, documents and tasks are stored as structured JSON, so they can be generated and validated.
   - The compiler renders them into the core book's HTML conventions (`dialogue-box`, `exercise`, `vocab-table`, `bn` / `hi` spans), so the existing website and print styling apply.
4. **Everything extensible is data.** Industries, departments, role families, roles, designations, responsibility levels, CEFR levels, situation categories and communication functions are registry records. No code holds a fixed list.
5. **The core book is referenced, never copied.** Links go to `book-data.json` unit IDs (e.g. `CE-L03-M01-L05`) and to existing codes (`CF-0023`, `V-0251`).

## 2. Repository layout

Proposed. Location is decision D-R07.

```
editorial/curriculum/            ← authoring source (D-R07 approved; excluded from deploy; unapproved content allowed)
  registry/
    industries/IND-0001.json …          departments/DEP-0001.json …
    industry-departments/IDP-000001.json role-families/RFM-0001.json …
    responsibility-levels/SEN-0001.json  designations/DES-0001.json …
    cefr-levels/CEF-B1.json …            scope-codes.json
    situation-categories/SCT-01.json …   communication-functions/CFN-0001.json …
    skills/SK-01.json …                  stakeholder-types/STK-0001.json …
  roles/ROL-0001.json …
  role-instances/RIN-000001.json …
  responsibilities/JFN-000001.json …
  situations/SIT-000001.json …
  job-knowledge/JKN-000001.json …
  vocabulary/<SCOPE>/V-<SCOPE>-0001.json …     (and PAT-/MIS- items the same way)
  conversations/CNV-000001.json …      documents/DOC-000001.json …
  meetings/MTG-000001.json …           presentations/PRS-000001.json …
  tasks/TSK-000001.json …              assessments/ASM-000001.json …
  capstones/CAP-000001.json …          units/CE-RI-000001-U01.json …
  requests/REQ-000001.json …           reviews/REV-000001.json …
  claims/CLM-0001.json …
  schemas/<entity>.schema.json
curriculum-data/                 ← FUTURE compiled output at site root: APPROVED/PUBLISHED records only
  registry.json  roles.json  industries/<SCOPE>.json  units/<RIN>.json  search-index.json
```

## 3. Common envelope (every record)

```jsonc
{
  "id": "RIN-000014",              // immutable
  "type": "role_instance",
  "schemaVersion": "1.0",
  "name": "HR Manager — IT — Human Resources",   // editable display name
  "status": "GENERATED",           // GENERATED | AI_QA | EDITORIAL_REVIEW | SPECIALIST_REVIEW | NATIVE_REVIEW | APPROVED | COMPILED | PUBLISHED | RETIRED (D-R09)
  "version": 3,
  "createdAt": "2026-10-04", "updatedAt": "2026-10-04",
  "provenance": { "source": "human|generated", "generator": null, "requestId": null },
  "review": { "english": "PENDING", "cefr": "PENDING", "roleRealism": "PENDING", "industry": "PENDING",
              "specialist": "NOT_REQUIRED|PENDING|PASS|NOT_PERFORMED", "bengali": "…", "hindi": "…" },
  "tags": []
}
```

- **Retired records are never deleted.** Their IDs are never reused.
- **`NOT_PERFORMED`** records honestly that a review did not happen. It is never equivalent to PASS (ROLE-QA-SPEC).

## 4. Registry entities

| Entity | ID | Key fields |
|---|---|---|
| industries | `IND-0001` + immutable `scope` code (e.g. `HOSP`) | `scope`, `name`, `description`, `riskFlags[]` (regulated, safety, minors), `specialistReview` (required?), `contextNotes`, `status` |
| departments | `DEP-0001` | `name`, `description`, `aliases[]` |
| industry_departments | `IDP-000001` | `industry`, `department`, `localName` (e.g. "Rooms Division"), `contextNotes`, `typicalRoles[]` |
| role_families | `RFM-0001` + immutable `scope` code (e.g. `HR`) | `scope`, `name`, `description`, `defaultDepartment` |
| responsibility_levels | `SEN-0001` | `name`, `rank` (sortable number), `layer`, `track` (main / ownership), `typicalDesignations[]` |
| designations | `DES-0001` | `title`, `responsibilityLevel`, `industry?`, `aliases[]` |
| cefr_levels | `CEF-B1` (code = level; extensible, e.g. `CEF-B1P` for B1+) | `code`, `name`, `order`, `descriptorRefs[]`, `generationRules` |
| scope_codes | file `scope-codes.json` | one namespace shared by industries and role families: `code` → `{ kind, recordId }`. Never equal to a code type (V, P, PAT, GIC, CF, TL, MIS, TIP). |
| situation_categories | `SCT-01` … `SCT-22` | `name`, `typicalFunctionGroups[]` |
| communication_functions | `CFN-0001` | `name`, `group`, `layer`, `modes[]`, `skill`, `coreRefs[]`, `coreCodes[]`, `structure`, `exponents{cefr:[…]}`, `newInEngine` |
| skills | `SK-01` | `name`, `domain`, `coreRefs[]` (from the earlier architecture) |
| stakeholder_types | `STK-0001` | `name` (guest, patient, parent, investor, owner, board, auditor …), `industries[]` |

## 5. Role entities

| Entity | ID | Key fields |
|---|---|---|
| roles | `ROL-0001` | `name`, `family`, `defaultLevel`, `allowedLevels[]`, `ladder{prev[], next[]}`, `defaultDepartment`, `roleCore{ responsibilities[], stakeholders[], functions[] (CFN by layer), documents[], meetings[], speakingSituations[] }`, `jobKnowledgeCore[]` |
| role_instances | `RIN-000001` | `role`, `industry`, `department`, `responsibilityLevel`, `designation?` (local title), `industryContext{ stakeholders[], situationsAdded[], situationsRemoved[], documents[], processes[], risks[], priorities[] }`, `jobKnowledge[]`, `situations[]`, `specialistReview`, `coverage` (computed tier) |
| responsibilities (job_functions) | `JFN-000001` | `name`, `scope` (role / instance), `description`, `functions[]` (CFN) |

**Instance rule:**
- An instance **inherits** the role core.
- The instance's `industryContext` **adds, removes or replaces** situations, stakeholders and documents.
- The difference must be visible at situation level (ROLE-QA-SPEC, industry realism check).

## 6. Situation and content entities

| Entity | ID | Key fields |
|---|---|---|
| situations | `SIT-000001` | `roleInstances[]` (a situation may serve several instances), `category` (SCT), `title`, `context`, `stakeholders[]`, `functions[]` (CFN), `modes[]`, `stakes`, `constraints[]` (policy, regulation, safety), `jobKnowledge[]`, `cefrRange` |
| job_knowledge | `JKN-000001` | `scope` (`role:ROL-…` / `industry:IND-…` / `instance:RIN-…`), `kind` (concept, process, metric, document, stakeholder, constraint, tool), `title`, `body` (short), `sourceNote`, `specialistReview`, `disclaimerRequired` |
| vocabulary | `V-<SCOPE>-0001` (core terms stay `V-0001`…) | `term`, `pos`, `definition`, `example`, `scope`, `departments[]`, `roles[]`, `situations[]`, `technical` (bool), `cefr`, `bn?`, `hi?`, `l1Reason?`, `seeAlsoCore[]`, `home` (unit) |
| expressions / patterns | `PAT-<SCOPE>-0001`; mistakes `MIS-<SCOPE>-0001` | as the core's PAT/MIS, plus `function` (CFN) |
| conversations | `CNV-000001` | see CONVERSATION-ENGINE-SPEC |
| documents | `DOC-000001` | `docType` (email, report, handover note, agenda, minutes, incident report, proposal, performance review, memo, notice, business message), `situation`, `from` / `to` (stakeholders), `model` (structured: subject, sections[]), `functions[]`, `cefr` |
| meetings | `MTG-000001` | `meetingType` (daily briefing, department, management, leadership/strategy, staff, academic leadership, investor/partner …), `chairRole`, `participants[]`, `agenda[]`, `functions[]`, `script?` (CNV link) |
| presentations | `PRS-000001` | `speakingType` (classroom explanation, team briefing, staff address, company presentation, pitch, client presentation, training session), `audience`, `structure[]`, `functions[]` |
| tasks | `TSK-000001` | `taskType` (recognition, guided practice, rewriting, writing, role-play, performance, problem-solving, reading, listening), `prompt`, `roleCards?`, `answer` / `sampleAnswer`, `rubric?` |
| assessments | `ASM-000001` | `kind` (diagnostic, formative, module test, performance), `roleInstance`, `cefr`, `items[]` (TSK), `rubric` (universal + industry + seniority-quality criteria), `passMark` |
| capstones | `CAP-000001` | `roleInstance`, `cefr`, `trigger` (SIT), `stages[]` (trigger, gather, update-up, act, document, meet/present, reflect), `informationPack[]`, `constraints[]`, `outputs[]`, `rubricWeights` (total 100) |
| units (lessons) | `CE-RI-000001-U01` (+ CEFR variant suffix `-B1`) | `roleInstance`, `sequence`, `cefr`, `objectives[]`, ordered `blocks[]` (refs to JKN, vocabulary, expressions, CNV, DOC, MTG, PRS, TSK, core GIC refs, pronunciation notes), `answerKey` (compiled), `coreLinks[]` |

## 7. Content variants by CEFR

The same situation can have content at several CEFR levels.
- **A variant** is a separate content record with `variantOf` (the base record's ID) and its own `cefr`.
- **Unit IDs** carry the CEFR suffix (`CE-RI-000014-U03-B2`), so progress is tracked per level.
- **The base record** holds level-neutral fields (situation, stakeholders, functions). Each variant holds the language.

## 8. Operational records

| Entity | ID | Key fields |
|---|---|---|
| requests | `REQ-000001` | the generation request sent to the content engine (CHATGPT-CONTENT-ENGINE-SPEC §2), verbatim |
| reviews | `REV-000001` | `target`, `check` (one of the 11 QA checks), `reviewer` (person or "model"), `result` (PASS / FAIL / NOT_PERFORMED), `findings[]`, `date` |
| claims | `CLM-0001` | `text`, `scopeType` (industry / role / role instance), `scope`, `requiredTier`, `computedTier`, `status` (SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED) |

## 9. Consumers

| Consumer | Use |
|---|---|
| Website / app | Loads `curriculum-data/registry.json` and `roles.json`, then the chosen instance's bundle on demand. Navigation: CEFR → industry → department → role → seniority → situation; filters on any registry dimension. Progress per unit ID (+ CEFR). |
| PDF | The print builder is extended to compile a role-instance or industry bundle into a supplement. The core PDF build is unchanged. |
| Search | Terms, codes (pattern extended to `<TYPE>-<SCOPE>-<nnnn>`), roles, situations, functions. |
| Reference index | Extended to read engine vocabulary by scope. Core codes are untouched. |
| Claims | A computed coverage tier per industry, role and instance (ROLE-QA-SPEC §6). |

## 10. Validation rules (for a future validator)

1. Every reference resolves (IDs exist; `coreRefs` exist in `book-data.json`; `coreCodes` exist in `reference-index.json`).
2. IDs are unique and immutable. Retired IDs are never reused.
3. Scope codes are unique across industries and role families, and never equal a code type.
4. Engine codes match `<TYPE>-<SCOPE>-\d{4}`. New core-range codes (if any) start above the current maximum per type (V-0793, PAT-0172, MIS-0205, …).
5. Vocabulary de-duplication passes (ROLE-VOCABULARY-ARCHITECTURE §4).
6. Rubric weights total 100. Every closed task has an answer.
7. No record has `status` APPROVED, COMPILED or PUBLISHED while a required review is PENDING, FAIL or NOT_PERFORMED. NOT_PERFORMED is never treated as PASS (D-R09).
8. Only APPROVED records are compiled into `curriculum-data/` (status becomes COMPILED). PUBLISHED needs a separate publication decision.
9. A role instance whose industry has `specialistReview: required` cannot be APPROVED without a specialist PASS.
