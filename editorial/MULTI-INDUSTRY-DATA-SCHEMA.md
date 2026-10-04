# Multi-industry data schema (proposal)

**Status: PROPOSAL ONLY.**
- `book-data.json` has not been changed.
- No schema has been implemented.
- The design choices here need author approval: D-09 (industry IDs), D-10 (codes), D-16 (data placement).

## 1. Constraints from the current system

| Current fact | Consequence for the design |
|---|---|
| `book-data.json` is a **top-level array of 5 level objects**. `index.html`, `build_print.py`, `book.py` (`items()`), the proof tools and the consistency audit all iterate over it as levels. | Adding industry objects to that array, or changing it to an object, would break or change every consumer. |
| `apply_corrections.py --check` verifies that `book-data.json` equals **baseline `61c769f` + logged corrections**, and refuses unknown correction phases. | New content written straight into `book-data.json` would make the check fail. Industry content needs its own baseline and correction phases. |
| Each unit stores content as HTML in `objectives_html`, `body_html` and `practice_html`, with IDs like `CE-L02-M01-L01`. | Reusing this unit shape lets the existing renderers (website lesson view, print HTML builder) show industry lessons with little change. |
| The code pattern `\b(V\|PAT\|GIC\|CF\|TL\|MIS\|TIP\|P)-\d{3,4}\b` is used in the index builder, the website and the print builder. | New codes must not be matched by mistake. Tested: `IND-IT-V-0001` **is** matched as `V-0001`; `V-IT-0001` is not. |
| Progress is a per-unit flag in browser storage, keyed by unit ID (`hea-book-reviewed`). | New unit IDs must be globally unique and stable. |
| The core book's publication gates (proofread and native review not performed; approval NO) are tied to its current files. | Industry content must not reopen the core's files. |

## 2. Placement options

| Option | Description | Effect on core | Website/PDF | Lazy loading | Correction log |
|---|---|---|---|---|---|
| A. Inside `book-data.json` | Change the top level to `{levels: [...], industries: [...]}`, or add industry keys to the levels | **Breaks** every consumer and the baseline check; reopens the core | Every renderer changes | No | The core baseline must be redefined |
| B. One sidecar file | `industry-data.json` alongside `book-data.json` | None | New loader; existing unit renderer reused | No (one file grows to all industries) | Own baseline and phases |
| C. Registry + per-industry files | `industry-data/registry.json` + `industry-data/IT.json`, `industry-data/BFS.json`, … | None | New loader; existing unit renderer reused | **Yes**: load only the chosen industry | Own baseline per file |

**Proposed design: option C.**
- It keeps the core untouched (R-11).
- It lets the website load one industry at a time (R-13).
- It lets each industry be versioned, reviewed and published separately, which fits Model D and publishing option 5.

Option B is the simpler alternative if only a few industries are planned. The choice is decision D-16.

## 3. Identifier conventions

| Entity | Pattern | Example | Note |
|---|---|---|---|
| Industry | Uppercase token, 2–4 letters, never equal to a code type (V, P, PAT, GIC, CF, TL, MIS, TIP) | `IT`, `BFS`, `HOSP` | List in the registry (D-09) |
| Band | `E` / `P` / `L` | `P` | Entry / Professional / Leadership |
| Skill | `SK-nn` | `SK-02` | Registry; links to core lessons |
| Domain | `D1`…`D9` | `D3` | Registry |
| Role | `ROLE-<IND>-<slug>` | `ROLE-IT-support-exec` | Tier `E`/`M`/`S`/`L` stored as a field |
| Situation | `SIT-<IND>-<nnn>` | `SIT-IT-014` | |
| Industry module | `CE-IND-<IND>-<band>-M<nn>` | `CE-IND-IT-P-M01` | Parallels `CE-L03-M01` |
| Industry lesson | `CE-IND-<IND>-<band>-M<nn>-L<nn>` | `CE-IND-IT-P-M01-L03` | Parallels `CE-L03-M01-L03`; unique across both files |
| Assessment | `CE-IND-<IND>-<band>-ASSESSMENT` / `-DIAGNOSTIC` | `CE-IND-BFS-E-ASSESSMENT` | |
| Capstone | `CE-IND-<IND>-<band>-CAPSTONE` | `CE-IND-HLTH-P-CAPSTONE` | |
| Industry code | `<TYPE>-<IND>-<nnnn>` | `V-IT-0001`, `PAT-BFS-0003`, `MIS-HLTH-0007` | Option 3 (D-10); not matched by current tools |
| New universal code | `<TYPE>-<nnnn>` continuing above the current maximum | `V-0793` | Never reuse gap or retired numbers |
| Claim | `CLM-<nnn>` | `CLM-004` | |

## 4. Registry file (`industry-data/registry.json`)

```jsonc
{
  "schemaVersion": "1.0",
  "domains": [ { "id": "D3", "name": "Updates, problems and spoken reporting" } ],
  "bands": [
    { "id": "E", "name": "Entry",        "coreLevels": [1, 2], "cefr": "A2+–B1",  "cefrStatus": "proposed" },
    { "id": "P", "name": "Professional", "coreLevels": [3, 4], "cefr": "B1+–B2", "cefrStatus": "proposed" },
    { "id": "L", "name": "Leadership",   "coreLevels": [5],    "cefr": "C1",      "cefrStatus": "proposed" }
  ],
  "skills": [
    { "id": "SK-02", "name": "Giving a work update", "domain": "D3", "bands": ["E", "P"],
      "coreRefs": ["CE-L02-M01-L01", "CE-L02-M01-L02", "CE-L02-M01-L03", "CE-L02-M01-L04"],
      "coreCodes": ["PAT-0025", "MIS-0040"], "transfer": "H" }
  ],
  "industries": [
    { "id": "IT", "name": "IT & Technology", "file": "IT.json", "status": "planned",
      "reviewFlags": ["practitioner"], "scopeNotes": "Security incidents: communication and handoff only" }
  ],
  "tiers": [ { "id": "T3", "name": "Module", "brief": "4 DEDICATED MODULE", "requirements": "see architecture §23.1" } ],
  "claims": [
    { "id": "CLM-004", "text": "Professional English for Banking", "industry": "BFS",
      "requiredTier": "T4", "status": "NOT SUPPORTED", "checkedAt": "2026-10-03" }
  ]
}
```

## 5. Industry file (`industry-data/<IND>.json`)

```jsonc
{
  "schemaVersion": "1.0",
  "industry": "IT",
  "roles": [
    { "id": "ROLE-IT-support-exec", "name": "IT Support Executive", "tier": "E",
      "interlocutors": ["end user", "team lead", "L2 engineer"], "documents": ["ticket update", "incident email"] }
  ],
  "situations": [
    { "id": "SIT-IT-014", "name": "Updating a manager about a production issue",
      "roles": ["ROLE-IT-support-exec"], "skills": ["SK-02", "SK-11"], "domains": ["D3", "D5"],
      "bands": ["E", "P"], "constraints": ["no root-cause speculation before evidence"], "tags": ["incident"] }
  ],
  "modules": [
    { "id": "CE-IND-IT-P-M01", "band": "P", "title": "Incidents and Escalation",
      "purpose": "…", "lessons": ["CE-IND-IT-P-M01-L01", "CE-IND-IT-P-M01-L02"],
      "assessment": "CE-IND-IT-P-ASSESSMENT", "capstone": "CE-IND-IT-P-CAPSTONE", "status": "DRAFT" }
  ],
  "lessons": [
    { "id": "CE-IND-IT-P-M01-L01", "module": "CE-IND-IT-P-M01", "sequence": 1,
      "title": "Giving an Incident Update", "lessonType": "situation",
      "roles": ["ROLE-IT-support-exec"], "situations": ["SIT-IT-014"],
      "appliesSkills": ["SK-02"], "coreRefs": ["CE-L02-M01-L01"], "coreCodes": ["PAT-0025"],
      "domains": ["D3"], "band": "P", "cefr": "B1+", "estimatedMinutes": 25,
      "objectives_html": "…", "body_html": "…", "practice_html": "…",
      "media": { "audio": [] },
      "l1Support": { "bn": true, "hi": true },
      "status": "DRAFT", "review": { "sme": "PENDING", "native": "PENDING", "editor": "PENDING" } }
  ],
  "vocabulary": [
    { "code": "V-IT-0001", "term": "incident bridge", "pos": "n.", "definition": "…",
      "example": "…", "bn": null, "hi": null, "l1Reason": null,
      "roles": ["ROLE-IT-support-exec"], "situations": ["SIT-IT-014"], "home": "CE-IND-IT-P-M01-L01",
      "seeAlsoCore": [], "cefr": "B2" }
  ],
  "assessments": [
    { "id": "CE-IND-IT-P-ASSESSMENT", "kind": "module-test", "band": "P",
      "parts": [ { "type": "role-play", "rubric": "RUB-UNIVERSAL+RUB-IT" }, { "type": "document", "document": "incident email" } ],
      "objectives_html": "…", "body_html": "…", "practice_html": "…", "passMark": null }
  ],
  "capstones": [
    { "id": "CE-IND-IT-P-CAPSTONE", "band": "P", "engine": "v1",
      "trigger": "SIT-IT-014", "role": "ROLE-IT-support-exec",
      "stages": ["trigger", "gather", "update-up", "act", "document", "meet", "reflect"],
      "constraints": ["SLA clock", "evidence before root cause"],
      "informationPack": ["incident log", "monitoring summary", "customer email"],
      "documents": ["incident email", "post-incident review"],
      "rubricWeights": { "update": 20, "communication": 25, "document": 30, "meeting": 15, "reflection": 10 },
      "objectives_html": "…", "body_html": "…", "practice_html": "…" }
  ],
  "rubrics": [ { "id": "RUB-IT", "criteria": ["terminology", "policy/safety compliance", "document format"] } ]
}
```

Fields named `*_html` use exactly the same conventions as `book-data.json`. That includes the existing classes: `dialogue-box`, `exercise`, `vocab-table`, `bn` and `hi` spans.

## 6. How each consumer uses the data

| Consumer | Use |
|---|---|
| Website | Loads the registry, then the selected industry file on demand. Navigation: band → industry → role → situation (filters on `roles`, `situations`, `skills`, `band`, `cefr`, `lessonType`). Each lesson shows "Skill from the core", using `coreRefs`. |
| PDF | Print builder extended to render one industry file as a supplement: industry → band → modules → lessons → assessment → capstone, plus an industry glossary and index. The core PDF build is unchanged. |
| Mobile app | Same JSON; per-industry download. |
| Search | Term, code (extended pattern), role, situation, skill. |
| Filtering | `industry`, `band`, `cefr` (once approved), `roles`, `situations`, `skills`, `domains`, `lessonType`, assessment `kind`. |
| Progress tracking | Keyed by unit ID, as now. Industry progress is aggregated by module and band. |
| CEFR | `band.cefr` + `lesson.cefr`, with `cefrStatus: "proposed"` until validated. The website must not show CEFR labels while status is `proposed` unless the author approves (D-12). |
| Assessment | `assessments` + `capstones` + `rubrics`; scores stay on the device unless an account system is approved later. |
| Claims | The `claims` table. A check script computes each industry's tier from the data and gate status, and fails when a claim needs more. |
| Reference index | `build_reference_index.py` extended to read industry files. Industry codes listed under their industry; core codes unchanged. |

## 7. Validation rules (for a future validator)

1. Every ID is unique across `book-data.json` and all industry files.
2. Every `coreRefs` entry exists in `book-data.json`. Every `appliesSkills`, `roles`, `situations` and `domains` entry exists in the registry or the industry file.
3. Industry codes match `<TYPE>-<IND>-\d{4}`, where `<IND>` is a registry industry. New universal codes are above the current maximum for their type.
4. No industry vocabulary entry duplicates a core V label with the same meaning; such terms must use `seeAlsoCore` instead.
5. Each lesson has the template's required elements (architecture §12.1): an industry dialogue, a role-play, a writing task and an answer key.
6. Rubric weights total 100.
7. No content is `status: "APPROVED"` while any of its `review` fields is `PENDING`.
8. Claims check: no claim's `requiredTier` exceeds the computed tier.

## 8. Audit trail and corrections

The existing correction engine applies to the core only. The proposal for industry files:
- each industry file gets its **own baseline commit**, once its first version is approved;
- corrections are logged with **new, registered phase labels**, for example `industry-<IND>-review`, in a separate log or a separate section of the existing log;
- the frozen-history guard (`correction-log-frozen.json`) protects rows 1–941 and is not changed.

`apply_corrections.py` currently rejects unknown phases. The new phases would need registering when implementation is approved. **No tool has been changed in this phase.**

## 9. What is not changed

- `book-data.json`, `reference-index.json`, `index.html` and the print builders.
- The PDF, the covers, the correction log and the publication gates.

All of these remain as they are until the author approves an implementation phase.
