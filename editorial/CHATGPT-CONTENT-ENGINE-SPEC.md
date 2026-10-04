# Content engine specification (ChatGPT ↔ GitHub contract)

This spec defines the exact contract between the **content generator** and the **repository**. The brief names ChatGPT. The contract is model-agnostic, so the same packets work with any capable model; the choice is decision D-R08.

## 1. Division of responsibility

| Repository (system of record) | Content generator (ChatGPT) | People |
|---|---|---|
| Registries, IDs, schemas, codes | Proposes content inside the provided context | Approve or reject |
| Assembles the context pack for each request | Generates lessons, conversations, vocabulary proposals, job knowledge, practice, assessments, capstones | Specialist and native review where required |
| Validates every response; assigns final IDs and codes | Reviews content when asked (review mode) | Publication approval |
| Stores provenance, versions, review results | Never assigns final IDs; never marks anything approved | — |
| Compiles only APPROVED content for publication | — | — |

**Non-negotiable rules:**
1. **Generated content enters as `GENERATED`.** It can never become APPROVED without the required human checks (ROLE-QA-SPEC).
2. **A model review is recorded as `reviewer: "model"`.** It never satisfies a human, specialist or native-language check.

## 2. Request packet (`REQ-000001`), repository → generator

```jsonc
{
  "requestId": "REQ-000123",
  "contractVersion": "1.0",
  "mode": "generate",                       // generate | revise | review
  "outputType": "unit",                     // unit | conversation | vocabulary | job_knowledge | document |
                                            // meeting | presentation | tasks | assessment | capstone
  "spec": {
    "industry":   { "id": "IND-0002", "scope": "TECH", "name": "IT & Technology" },
    "department": { "id": "DEP-0005", "name": "Human Resources", "localName": null },
    "role":       { "id": "ROL-0013", "name": "HR Manager", "family": "HR" },
    "roleInstance": "RIN-000031",
    "responsibilityLevel": { "id": "SEN-0008", "name": "Manager", "layer": "managerial" },
    "cefr": "B2",
    "workplace": "Mid-size software company, Bengaluru office, hybrid teams",
    "situation": { "id": "SIT-000210", "category": "SCT-04",
                   "title": "Discussing recruitment priorities with the engineering head" },
    "functions": ["CFN-0035", "CFN-0044", "CFN-0062", "CFN-0074"]
  },
  "context": {
    "roleCore": { "responsibilities": ["…"], "stakeholders": ["…"] },
    "industryContext": { "stakeholders": ["…"], "processes": ["…"], "risks": ["…"], "priorities": ["…"] },
    "jobKnowledge": [ { "id": "JKN-000412", "title": "Technical skill assessment", "body": "…" } ],
    "existingVocabulary": [ { "code": "V-HR-0007", "term": "attrition" }, { "code": "V-0251", "term": "on track" } ],
    "functions": [ { "id": "CFN-0062", "structure": "…", "exponents": { "B2": ["…"] } } ],
    "coreLinks": [ { "unit": "CE-L04-M01-L02", "title": "Opening a Negotiation and Anchoring", "codes": ["TL-0009"] } ],
    "characters": [ { "name": "…", "role": "Engineering Head", "relationship": "peer-senior" } ],
    "constraints": ["no legal advice on employment law", "no real company names"]
  },
  "style": {
    "spelling": "UK", "dateFormat": "UK", "register": "professional",
    "englishFirst": true, "l1SupportTriggers": ["difficult-concept", "false-friend", "cultural", "learner-error",
                                                  "pronunciation", "industry-term"],
    "cefrRules": "CEF-B2.generationRules",
    "unitTemplate": "ROLE-CONTENT-BLUEPRINT §5",
    "conversationRules": "CONVERSATION-ENGINE-SPEC §3"
  },
  "limits": { "maxNewVocabulary": 10, "conversationTurns": [10, 18], "unitPages": [4, 6] },
  "outputSchema": "schemas/unit.schema.json"
}
```

**How the context pack is built.** The repository resolves every ID into the records the generator needs. The generator never has to guess a registry value or invent a role, stakeholder or function.

## 3. Response packet, generator → repository

```jsonc
{
  "requestId": "REQ-000123",
  "contractVersion": "1.0",
  "outputs": [
    { "tempId": "tmp:unit-1", "type": "unit", "record": { /* conforms to outputSchema; references use real IDs or tempIds */ } },
    { "tempId": "tmp:cnv-1",  "type": "conversation", "record": { } }
  ],
  "proposedCodes": [
    { "tempId": "tmp:v-1", "type": "V", "term": "headcount plan", "suggestedScope": "HR",
      "definition": "…", "reasonNotExisting": "not in existingVocabulary or core index" }
  ],
  "selfCheck": [
    { "check": "functionCoverage", "result": "met", "notes": "CFN-0062 in turns 7 and 9" },
    { "check": "cefrFit", "result": "uncertain", "notes": "turn 12 may be C1" }
  ],
  "assumptions": ["Engineering head prefers fast hiring over cost"],
  "flags": [ { "type": "specialistReview", "reason": "mentions notice-period rules" } ],
  "questions": []
}
```

**Rules for the generator:**
- **Output JSON only**, conforming to `outputSchema`. No prose outside the packet.
- **New items use `tempId`s.** The generator never invents final IDs or codes. Existing items are referenced by their real ID or code from the context pack.
- **Report honestly** in `selfCheck`, `assumptions` and `flags`. "Uncertain" is acceptable; claiming a check passed when it has not is not.
- **Never state** that content is approved, certified, CEFR-validated or compliant with any regulation.
- **No real companies, real people, or real regulations cited as fact.** Regulated content is kept generic and flagged for specialist review.
- **No medical, legal, financial or safety advice.** Job knowledge stays within JOB-KNOWLEDGE-LAYER §1.
- **Characters** come from the context pack. New characters are proposed with a `tempId`.

## 4. Repository processing pipeline

1. **Receive and store** the raw response (`requests/REQ-…` + response file), for audit.
2. **Schema validation.** Failure → status `REJECTED` with reasons, and an optional automatic `revise` request.
3. **Reference resolution.** Every real ID or code exists; every `tempId` is defined in the response.
4. **De-duplication** of `proposedCodes` (ROLE-VOCABULARY-ARCHITECTURE §4): existing terms are replaced by their codes.
5. **ID and code assignment.** `tempId`s are mapped to final IDs and codes, and the mapping is stored.
6. **Automated checks:**
   - house style (UK spelling and dates);
   - CEFR estimate (sentence length, word-frequency bands);
   - function coverage;
   - answer-key completeness;
   - rubric totals.
7. **Store** as `GENERATED`, with `provenance { source: "generated", generator: "<model name and version>", requestId, date }`.
8. **Review stages** (D-R09): AI_QA → EDITORIAL_REVIEW → SPECIALIST_REVIEW (where required) → NATIVE_REVIEW (where required) → APPROVED (ROLE-QA-SPEC §3). A required review that is NOT_PERFORMED stops the record before APPROVED.
9. **Compile** only APPROVED records to `curriculum-data/` (status COMPILED). Publishing is a separate author decision (status PUBLISHED).

## 5. Review mode

The repository sends `mode: "review"` with:
- the target records;
- the checks requested (any of the 11);
- the same context pack.

The generator returns a **review report**:

```jsonc
{ "requestId": "REQ-000140", "target": "CNV-000210",
  "findings": [ { "check": "industryRealism", "location": "turn 5", "severity": "major",
                  "issue": "…", "suggestion": "…" } ],
  "summary": { "industryRealism": "fail", "english": "pass" } }
```

It is stored as `REV-…` with `reviewer: "model"`. Model reviews **inform** human reviewers; they never replace them.

## 6. Revise mode

`mode: "revise"` sends:
- the record;
- the findings to fix;
- the instruction to change **only** those points.

The response returns the full revised record and increments `version`. The previous version is kept.

## 7. Prompt envelope

Fixed text, versioned with the contract:
- **System:** role (content generator for Career English); the rules in §3; output JSON only.
- **User:** the request packet.
- **Attachments:**
  - the output JSON Schema;
  - the unit template;
  - the conversation rules;
  - the CEFR generation rules for the level;
  - the house style.

The prompt envelope's version is stored with each request, so any output can be traced and reproduced.

## 8. The brief's eight example requests

Each example becomes one `REQ` with `outputType: "unit"`, built from the spec table in ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE §6. All of them resolve to registry IDs; none needs a schema change. No requests have been sent: generation starts only after approval and Phase 1 (registry and schemas).
