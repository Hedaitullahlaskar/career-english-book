# Curriculum store: role engine, pilot U-1

**What this is.** The structured source for the new role-based Career English layer. It currently holds **pilot U-1** only: an **architecture-validation prototype** approved by the author on 4 October 2026.
- It is **not published** and **not part of the existing book**.
- Its final state can never be COMPILED or PUBLISHED.

**Where it lives (D-R07).** Under `editorial/`, which the deploy workflow excludes. Nothing here reaches the website.

The existing book (`book-data.json`, the lessons, reference codes, PDF, covers and publication gates) is untouched.

## Who does what (D-U10)

| Step | Done by |
|---|---|
| Curriculum text (all layers L0–L6) | **ChatGPT**, the designated generation engine |
| Request construction, retrieval before generation, de-duplication, ID and code assignment, schema validation, AI QA tooling, composition, search tests, storage, version control | Repository tools (`editorial/tools/curriculum/`) |
| Editorial Review of U-1 | **The author** (D-U13b) |
| Specialist Review / Native Review for U-1 | NOT_REQUIRED (recorded with reasons; never treated as PASS) |

## Folders

| Folder | Contents |
|---|---|
| `config/pilot-u1.json` | The approved U-1 definition, per-batch limits (no global ceiling), size limits, style, policies (D-U11, D-U12, D-U14), review policy, search queries |
| `registry/` | Registries built from the approved CSVs: 27 sectors, 122 industries, 62 families, 50 departments, 402 roles, 156 situations, 113 functions, 15 core modules, 12 responsibility levels, 7 CEFR levels, 211 scope codes |
| `schemas/` | JSON Schemas for every record type |
| `role-profiles/` | RPF-000001 … RPF-000005 (the five U-1 Role Profiles) |
| `plans/` | RIN-000001 … RIN-000014 (the 14 Role Instances: layers needed, reuse, review policy) |
| `requests/` | REQ-000001 … REQ-000011 (ChatGPT request packets) + `index.json` (stable IDs) + `PROMPT-ENVELOPE-v1.md` |
| `responses/` | Put ChatGPT's JSON replies here (one file per request) |
| `content/` | *Created by ingest:* stored objects, `index.json` (key → object), `vocabulary.json` |
| `reviews/` | *Created by ingest:* REV records (AI QA; Editorial = author; Specialist and Native = NOT_REQUIRED) |
| `previews/` | *Created by compose:* readable copies of composed units for the author's Editorial Review |
| `logs/` | `plan-summary.json`, `estimates.json`, `usage.jsonl`, `compose.json`, `search-test.json` |

## Workflow

```
python editorial/tools/curriculum/build_registry.py         # registry JSON from the approved CSVs
python editorial/tools/curriculum/plan.py                   # profiles, plans, request packets (only missing layers)
#   → send each PREPARED request to ChatGPT (see requests/PROMPT-ENVELOPE-v1.md); save the reply in responses/
python editorial/tools/curriculum/ingest.py editorial/curriculum/responses/REQ-000001.json
python editorial/tools/curriculum/plan.py                   # unblocks the next batch when its dependencies are present
python editorial/tools/curriculum/compose.py                # previews for units whose layers are all present
python editorial/tools/curriculum/validate.py               # schemas, references, counts, collisions, duplicates, boundary
python editorial/tools/curriculum/search_test.py            # search/navigation queries
python editorial/tools/curriculum/tests/run_pipeline_test.py   # end-to-end test on synthetic data in a temp folder
```

**Batch order** (each batch reuses everything before it):

| Batch | Content | Requests |
|---|---|---|
| B1 | L0 function exponents | REQ-000001 |
| B2 | L1 situations | REQ-000002 |
| B3 | L2 core modules | REQ-000003 |
| B4 | L3 role cores | REQ-000004 |
| B5 | L4 context overlays + L5 seniority overlays | REQ-000005 |
| B6 | L6 units | REQ-000006 P1, 000007 P2, 000008 P2 A2 variant, 000009 P3, 000010 P4, 000011 P5 |

**Rules enforced by the tools:**
- **No regeneration.** A request that is INGESTED cannot be ingested again; revisions use `--revise`, and the previous version is kept in `content/history/`.
- **No duplicate objects.** Every layer object has one key, and an existing key is reused, never regenerated.
- **Vocabulary (D-U07):**
  - existing book codes are reused, never renumbered;
  - new terms get `V-<SCOPE>-<NUMBER>` (scope = role family if the role is used in more than one industry, otherwise the industry);
  - every code is checked against the live `reference-index.json`, and collisions are rejected.
- **Per-batch limits only** (`config/pilot-u1.json`). A request over its batch limit becomes STOPPED_BUDGET; the author may raise the limit. **Cost control never limits coverage.**
- **Statuses** follow D-R09:
  - after a clean AI QA, a record is `AI_QA`; Editorial Review is the author's;
  - **NOT_PERFORMED is never PASS**;
  - U-1 records are `prototype: true, publishable: false`, and the validator rejects COMPILED or PUBLISHED.
