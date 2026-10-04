# Role vocabulary architecture

## 1. The six layers (brief §21)

| Layer | Example | Coded as | Owner scope |
|---|---|---|---|
| Core professional vocabulary | "on track", "held up", "escalate" | **Existing core codes** (`V-0001`…`V-0792`, 540 indexed). Never renumbered or duplicated. | Core book |
| Industry vocabulary | "occupancy", "consignment", "KYC" | `V-<INDUSTRY>-nnnn`, e.g. `V-HOSP-0001` | Industry scope code |
| Department vocabulary | "par stock" (Housekeeping), "rooming list" (Front Office) | Industry code + **tag** `departments[]` | Industry scope (tagged) |
| Role vocabulary | "attrition", "onboarding" (HR in any industry) | `V-<FAMILY>-nnnn`, e.g. `V-HR-0001`, when used across industries; otherwise industry code + **tag** `roles[]` | Role-family scope code |
| Situation vocabulary | "no-show", "walk-in" for a reservation situation | Existing code + **tag** `situations[]` | Whichever scope owns the term |
| Technical terms | "RevPAR", "root-cause analysis", "lockout" | Any scope + flag `technical: true` (triggers specialist review where the industry requires it) | Owner scope |

**Why departments, roles and situations are tags rather than code namespaces.** A term like "escalation matrix" is used by several roles and situations. Separate namespaces would code it once per role: exactly the duplicate teaching the brief forbids. Tags give the same filtering with one entry per meaning.

## 2. Code format

```
<TYPE>-<SCOPE>-<nnnn>
TYPE  = V | PAT | MIS | CF | GIC | TL | TIP | P   (the core's existing types)
SCOPE = an industry or role-family scope code from one shared namespace
        (proposed: HOSP TECH BANK HLTH RETL BPO AVIA EDU TRVL LOGI MFG CORP PROF SPRT SMB GEN /
         ADMN HR FIN SALE MKTG OPS CSV ITF ENGR PROC TRNG QLTY TEACH HOPS FNB FO HSKP MAINT LOGF PROD HCAD MGMT LEAD ENTR)
```

**Tested** (4 October 2026) against the pattern used by the website, index builder and print builder, `\b(V|PAT|GIC|CF|TL|MIS|TIP|P)-\d{3,4}\b`:
- **0 false matches across all 40 scopes × 8 types.** No engine code can be mistaken for a core code.
- By contrast, `IND-IT-V-0001` was matched as core `V-0001`.

**Namespace rules:**
- Industries and role families share **one** namespace, so a code is never ambiguous. The IT *industry* is `TECH`; the IT *function* is `ITF`.
- No scope code equals a type name.
- Codes are immutable once issued, and retired codes are never reused.
- The **repository assigns** codes. The content generator proposes terms with temporary IDs (CHATGPT-CONTENT-ENGINE-SPEC §4).

**Tool change needed at implementation** (not now): extend the pattern in three places to `\b(V|PAT|GIC|CF|TL|MIS|TIP|P)-(?:([A-Z]{2,5})-)?\d{3,4}\b`, validated against the scope registry.

## 3. Entry model

```jsonc
{ "code": "V-HR-0007", "term": "attrition", "pos": "n.",
  "definition": "the rate at which employees leave and need replacing", "example": "…",
  "scope": "RFM-(HR)", "departments": ["DEP-0005"], "roles": ["ROL-0012", "ROL-0013"],
  "situations": [], "technical": false, "cefr": "B2",
  "senses": [],                          // separate entries for different meanings, never merged
  "bn": null, "hi": null, "l1Reason": null,   // only when a localisation trigger applies
  "seeAlsoCore": [], "home": "CE-RI-…-U02" }
```

## 4. De-duplication algorithm (run before any code is issued)

1. **Normalise** the term (lemma, case, hyphenation).
2. **Search the core index.** If the term exists with the same meaning, **cite the core code**; do not create a new one.
3. **Search all engine scopes:**
   - same meaning in a role-family scope → reuse it;
   - same meaning in another industry → if the meaning is identical, **promote** the term to the role-family scope or propose it as a core-range term (decision by editor); otherwise keep separate entries;
   - different meaning (e.g. "ticket" in TECH vs AVIA vs SPRT) → separate entries in each scope, each with a `senses` note.
4. **Choose the owner scope:**
   - core, if universal;
   - role family, if the term follows the role across industries;
   - industry, if it belongs to the industry for every role in it.
5. **Tag** departments, roles and situations.
6. **Record** the decision in the review log (vocabulary check).

**Teaching rule:**
- A term is *taught* once, in its `home` unit.
- Elsewhere it is *used* and linked, never re-taught.
- Units list "Review vocabulary" (links) separately from "New vocabulary".

## 5. Selection per unit

| CEFR | New terms per unit (guideline) |
|---|---|
| A1–A2 | 5–8 |
| B1–B2 | 6–10 |
| C1–C2 | 6–12, including collocation and nuance |

**Closure rule:** every term needed to complete the unit's tasks is either taught in the unit or linked as review.

## 6. Bengali / Hindi

`bn` / `hi` are given only when a localisation trigger applies: difficult concept, false friend, cultural distinction, common learner error, pronunciation issue, or industry term needing explanation. The trigger is recorded in `l1Reason`.

**Workplace terms used in English** (check-in, KYC, OPD, ticket, dispatch) stay English. A gloss explains them; it never replaces them. Every script entry goes to the native-review register. If no reviewer is available, it is marked NOT_PERFORMED (D-R09).
