# Conversation engine specification

**The conversation is the central learning object of the role engine.**
- Every other content type either prepares for a conversation (job knowledge, vocabulary, expressions) or follows from it (practice, role-play, performance task, assessment).
- This spec defines the record, the generation rules and the checks.
- No conversations are generated here.

## 1. Conversation record (`CNV-000001`)

The 19 elements required by the brief, mapped to fields:

| # | Element | Field | Rule |
|---|---|---|---|
| 1 | Industry | `industry` (IND) | From the role instance |
| 2 | Department | `department` (DEP) | From the role instance |
| 3 | Role | `role` (ROL) + `roleInstance` (RIN) | The learner speaks as this role |
| 4 | Seniority | `responsibilityLevel` (SEN) | Drives function choice and the qualities in Seniority §9 |
| 5 | Stakeholder | `stakeholders[]` (STK + name + relationship) | Every speaker has a stakeholder type and a relationship (senior / peer / junior / external) |
| 6 | Situation | `situation` (SIT) | One situation per conversation |
| 7 | Communication function | `functions[]` (CFN, ordered) | 1–4 functions; each must be realised in at least one learner turn |
| 8 | Objective | `objective` | One sentence: what the learner's character must achieve |
| 9 | Context | `context` | Setting, prior events, information each side knows, constraints (policy, regulation, safety) |
| 10 | Dialogue | `turns[]` | See section 2 |
| 11 | Key expressions | `expressions[]` | PAT codes (core or `PAT-<SCOPE>-…`) marked in turns |
| 12 | Vocabulary | `vocabulary[]` | V codes (core or scoped) used in turns |
| 13 | Job knowledge | `jobKnowledge[]` | JKN items the dialogue assumes; each must be taught or referenced in the unit |
| 14 | Practice | `practice[]` | TSK refs (recognition, guided practice, rewriting) |
| 15 | Role-play | `rolePlay` | Two or more role cards with goals and hidden information; based on, but not identical to, the dialogue |
| 16 | Performance task | `performance` | An integrated task (speak + write), e.g. role-play then follow-up email |
| 17 | Assessment | `assessment` | Items or rubric criteria tied to `functions[]` |
| 18 | CEFR | `cefr` (+ `variantOf`) | The language level of this variant |
| 19 | Core links | `coreRefs[]`, `coreCodes[]` | The core lessons and formulas the conversation applies |

Plus the common envelope (status, provenance, review), as in CONTENT-DATA-SCHEMA §3.

## 2. Turn structure

```jsonc
{ "n": 3, "speaker": "learnerRole",            // learnerRole | stakeholder id
  "text": "…",
  "functions": ["CFN-0037"],                    // function realised in this turn (if any)
  "expressions": ["PAT-0025"], "vocabulary": ["V-HOSP-0012"],
  "tone": "calm, specific",                     // optional delivery note
  "note": "…" }                                 // optional teaching note (shown in walkthrough)
```

## 3. Generation rules

1. **Situation first, nouns last.** A conversation for an IT HR Manager must arise from a situation that exists in IT HR, such as competing engineering hiring priorities. It must not be a hotel conversation with nouns swapped (industry realism check).
2. **The learner's role speaks the target functions.** Stakeholders create the need: questions, objections, emotion, missing information.
3. **Seniority shapes content.** The functions and the progression qualities (strategic, precise, diplomatic, analytical, persuasive, decision-oriented) must match the responsibility level (Seniority §9).
4. **CEFR shapes language only:**

   | CEFR | Learner turns | Total turns |
   |---|---|---|
   | A1–A2 | ≤ 12 words | 6–10 |
   | B1 | — | 8–14 |
   | B2–C1 | Longer turns | 10–18 (with turn length varied) |

   Grammar is limited to the level's generation rules (`cefr_levels`).
5. **Realistic constraints.** The learner never offers what the role could not offer: an upgrade a bank cannot give, a clinical opinion a receptionist must not give. Constraints come from `context.constraints` and the industry's `riskFlags`.
6. **Natural, regionally plausible names and settings.** South Asian workplaces are the default context; international stakeholders appear where the industry has them. No stereotypes (cultural check). The core's L4 M7 principle applies: adapt without stereotyping.
7. **Every vocabulary and expression code used must exist or be proposed** in the same response (with temporary IDs; the repository assigns final codes).
8. **One conversation, one situation.** Multi-situation sequences are units or capstones.
9. **House style:** UK spelling; UK date format (decided 3 October 2026, applied to the core).

## 4. Conversation types

| Type | Use | Turns |
|---|---|---|
| Model dialogue | The main example in a unit | Full |
| Contrast pair | A ❌ / ✅ version of the same moment (the core's existing technique) | 2–6 |
| Phone / chat / video | Channel variants (core L2 M3–M4, L3 M9) | Full |
| Meeting script | Linked from MTG; several stakeholders | Full |
| Role-play cards | No full script; goals plus hidden information | — |

## 5. Checks before a conversation can be APPROVED

| Check | Pass condition |
|---|---|
| Schema | All 19 elements present; references resolve |
| Function coverage | Every listed CFN is realised in a learner turn |
| Seniority fit | Functions are appropriate to the layer; the qualities rubric is met |
| CEFR fit | Turn length, vocabulary and grammar within the level's rules (automated estimate + human CEFR check) |
| Role realism | Plausible for that role (reviewer) |
| Industry realism | The situation, terms and constraints are true to the industry; specialist PASS where required |
| Job knowledge | Every assumed JKN is taught or referenced in the unit |
| Tone | Professional tone appropriate to the relationship (core PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION) |
| Cultural | No stereotyping; respectful |
| English | Grammar and naturalness (human) |
| Consistency | Names, facts and numbers consistent with the unit and the role instance |

## 6. Skeleton for the brief's example 1

Metadata only; no dialogue is generated:

```jsonc
{ "id": "CNV-(assigned)", "industry": "IND-(HOSP)", "department": "DEP-0001", "role": "ROL-0001",
  "roleInstance": "RIN-(assigned)", "responsibilityLevel": "SEN-0003", "cefr": "B1",
  "situation": "SIT-(assigned): guest complains that the room is not ready at check-in time",
  "stakeholders": [{ "type": "STK-(guest)", "relationship": "external" }, { "type": "STK-(supervisor)", "relationship": "senior" }],
  "functions": ["CFN-0038", "CFN-0007", "CFN-0039", "CFN-0024", "CFN-0041"],
  "objective": "Calm the guest, offer what the role is allowed to offer, escalate if needed, confirm next step",
  "context": { "constraints": ["executive may offer lounge access and a drink; an upgrade needs supervisor approval"] },
  "coreRefs": ["CE-L02-M07-L04", "CE-L03-M05-L01", "CE-L03-M05-L03"], "coreCodes": ["CF-0013", "CF-0008"] }
```
