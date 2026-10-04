# Role content QA specification

Every generated or written piece of role-engine content must pass these checks before it can be APPROVED or used in a public claim.

**Constraint recorded from the author** (3 October 2026): no separate human proofreader or native-language reviewer is available.
- Checks that need those people are recorded as **NOT_PERFORMED** when not done. **They are never marked PASS by default.**
- **D-R09 (approved 4 October 2026, with strict gates).** Content whose required human, specialist or native-language review is NOT_PERFORMED **is not APPROVED**. It cannot be compiled, published or counted toward any claim tier (sections 3 and 6).

## 1. The 11 checks

| # | Check | What it verifies | Automated part | Human owner | Blocking? |
|---|---|---|---|---|---|
| 1 | English | Grammar, naturalness, spelling (UK), punctuation | Spelling, repetition, a/an, quotes, house style (existing proof tools adapted) | Editor / proofreader | Yes |
| 2 | CEFR | Language within the target level | Sentence length, word-frequency band, grammar-pattern estimate | CEFR-aware editor | Yes |
| 3 | Role realism | The role would really say and do this, at this responsibility level (Seniority §9 qualities) | Function-to-layer consistency | Practitioner of the role | Yes |
| 4 | Industry realism | Situations, terms, processes and constraints are true to the industry, and differ from other industries at situation level | Detects "noun-swap" by comparing situations across instances of the same role | Industry practitioner / specialist | Yes |
| 5 | Job knowledge | Items accurate, within boundaries, used by the content, with a disclaimer where required | Every assumed JKN is taught or referenced | Practitioner; **specialist** where flagged | Yes |
| 6 | Conversation | All 19 elements; function coverage; turn rules; consistency | Schema, function coverage, turn counts | Editor | Yes |
| 7 | Vocabulary | De-duplication; correct scope; codes; definitions; tags | Duplicate search against core and engine; code-format and collision test | Editor | Yes |
| 8 | Professional tone | Tone fits the relationship and the PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION logic | — | Editor | Yes |
| 9 | Cultural | Respectful; no stereotypes; regionally plausible | Name and setting variety report | Cultural reviewer / editor | Yes |
| 10 | Assessment | Items match objectives; answer keys correct; rubric weights total 100; pass marks set | Answer-count and numbering checks (as in the core audit); weight totals | Assessment editor | Yes |
| 11 | Consistency | Names, facts, numbers and characters consistent across units, the role instance and the registry; links resolve | Reference resolution; character registry check | Editor | Yes |

**Plus localisation checks** where Bengali/Hindi appears:
- **Bengali QA** and **Hindi QA** by named native reviewers;
- otherwise NOT_PERFORMED;
- registers modelled on the existing `editorial/proof/NATIVE-LANGUAGE-REVIEW.csv`.

## 2. Specialist review (regulated or safety-sensitive)

| Industry or area | Specialist | Triggers |
|---|---|---|
| Healthcare | Healthcare administration and clinician | Any patient-facing content; any clinical term; privacy |
| Banking & finance | Banking compliance | KYC/AML, disclosures, complaints, product statements |
| Aviation | Airline / airport operations | Any safety or announcement language; regulated scope |
| Manufacturing | EHS / quality | Safety, PPE, lockout, quality-system terms |
| Pharmaceuticals (if added) | Regulatory / quality | GMP, recalls, medical representative content |
| Education, sports academies | Safeguarding | Anything involving minors |
| BPO / contact centre | Data protection | Call recording, verification, customer data |
| HR (all industries) | HR practitioner | Employment-law-adjacent statements (kept generic) |
| Logistics | Logistics specialist | Customs, dangerous goods (out of scope unless reviewed) |

A role instance in a flagged industry **cannot be APPROVED** without a specialist PASS. A specialist NOT_PERFORMED leaves it unapproved: not for compilation or publication.

## 3. Status workflow (D-R09, approved 4 October 2026)

```
GENERATED → AI_QA → EDITORIAL_REVIEW → SPECIALIST_REVIEW (where required) → NATIVE_REVIEW (where required)
          → APPROVED → COMPILED → PUBLISHED                                         RETIRED (never deleted)
```

| Status | Entered when | Who |
|---|---|---|
| GENERATED | The response passes schema validation and reference resolution, and final IDs are assigned (CHATGPT-CONTENT-ENGINE-SPEC §4). Human-written content enters at the same point, with `provenance.source = "human"`. | Repository |
| AI_QA | Automated checks and the model review have run and their results are recorded. They cover checks 6, 7, 10 and 11, plus automated estimates for 1 and 2. | Repository + model |
| EDITORIAL_REVIEW | A named editor has recorded PASS for every blocking human check (1–11 as owned by an editor or practitioner) | Editor |
| SPECIALIST_REVIEW | Required only when the industry, role or content triggers section 2. A named specialist has recorded PASS. | Specialist |
| NATIVE_REVIEW | Required only when Bengali/Hindi appears. Named native reviewers have recorded PASS for Bengali and Hindi. | Native reviewers |
| APPROVED | Every required review is PASS. Author/editor sign-off is recorded. | Author / editor |
| COMPILED | The compiler has built the record into `curriculum-data/` (only APPROVED records are eligible) | Repository |
| PUBLISHED | Released on the website or in print by an explicit publication decision | Author |

**Gate rules:**
- **A review that is not required** is recorded as NOT_REQUIRED, and its stage is skipped.
- **A review that is required but not done** is recorded as **NOT_PERFORMED**. The record **stops at its current stage**: it cannot become APPROVED, and therefore cannot be COMPILED or PUBLISHED.
- **NOT_PERFORMED is never treated as PASS**, by any tool, dashboard or person.
- **Any FAIL** sends the record back to EDITORIAL_REVIEW (after a fix), or to a `revise` request to the generator.
- **A model review** (`reviewer: "model"`) belongs to AI_QA only. It never satisfies editorial, specialist or native-language review.

## 4. Evidence

- **Every check result is a `REV-…` record:** target, check, reviewer (named person or "model"), result (PASS / FAIL / NOT_PERFORMED), findings, date.
- **Gate dashboard.** A per-instance dashboard is generated the same way the current `PROOF-CHECKLIST.md` is. It refuses to show PASS when the evidence is missing; this is the existing pattern in `build_proof_reports.py`.

## 5. Sampling for large volumes

**Automated checks run on 100% of records.**

| Content type | Human review |
|---|---|
| Conversations, job knowledge and assessments for a role instance's **first** release | 100% |
| Later batches of the same instance type | At least 20% sample + every flagged item, escalating to 100% if the sample FAIL rate exceeds 5% |
| Specialist and localisation reviews | 100% where triggered |

## 6. Claim tiers for roles and role instances

| Tier | Claim allowed | Requires |
|---|---|---|
| R0 | "Workplace English for every role" | The universal core (exists) |
| R1 | "Includes examples for [role]" | At least 3 APPROVED units for the role |
| R2 | "[Role] English: [industry]: [CEFR]" | The role instance's coverage targets met (ROLE-CONTENT-BLUEPRINT §3), capstone and performance assessment APPROVED, all blocking checks PASS (specialist PASS where flagged) |
| R3 | "[Role] English across industries" | R2 in at least 3 industries where the role is Common or Specialization required |
| R4 | "[Role] career track" | R2 across at least 3 consecutive responsibility levels of the role's ladder |

**Effect of NOT_PERFORMED checks (D-R09):**
- Every tier counts **APPROVED** content only.
- Content with any required review NOT_PERFORMED is not APPROVED, so it supports **no tier and no claim**, including R1.

Industry tiers from the earlier architecture (T0–T4) continue to apply to industry-level claims.

**Current state (4 October 2026):** no role-engine content exists, so every role claim is NOT SUPPORTED. Only R0 is supported, by the existing core.
