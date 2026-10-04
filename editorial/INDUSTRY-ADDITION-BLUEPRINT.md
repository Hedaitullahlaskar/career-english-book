# Industry addition blueprint

**Procedure** to add an industry with **no architecture change**. Every step adds data records only.

**Worked example:** Pharmaceuticals. The example is illustrative only: no records are created.

## Steps

| # | Step | Records created | Check |
|---|---|---|---|
| 1 | Register the industry | `IND-00nn` with `name`, `description`, `riskFlags` (pharma: regulated, safety), `specialistReview: required` | Name unique |
| 2 | Issue a scope code | `scope-codes.json`: e.g. `PHRM`, kind = industry | Not already used by an industry or role family; not a code type; collision test against the code pattern passes |
| 3 | Map departments | `IDP-…` records linking existing departments (Production, Quality, Sales, HR, Finance, Logistics / Warehouse, Procurement) with local names. Add a new department only if none fits, e.g. Regulatory Affairs as `DEP-00nn`. | Every department used exists |
| 4 | Map roles | Mark applicability in the role × industry matrix: Common / Applicable / Specialization required / Not applicable. Pharma examples: Quality Analyst (specialisation: GMP context); Sales Executive (specialisation: medical representative); Production Supervisor (common). | No role forced in where it does not exist |
| 5 | Add industry-specific designations | e.g. "Medical Representative" → Sales Executive role, SEN-0003, industry PHRM | Maps to an existing responsibility level |
| 6 | Create role instances | `RIN-…` for each selected role × department × level, with an `industryContext` (stakeholders, situations added/removed, documents, processes, risks, priorities) | Context differs at situation level, not just in nouns (industry realism check) |
| 7 | Industry job knowledge | `JKN-…` items with scope `industry:IND-…` (pharma: batch, GMP basics, deviation, recall (meaning only), detailing visit); **specialist review required** | Only items used by content |
| 8 | Industry stakeholders | `STK-…`, e.g. doctors (as customers of medical reps), regulators (via specialists), distributors | — |
| 9 | Industry vocabulary | `V-PHRM-nnnn`, after the de-duplication algorithm | Vocabulary check |
| 10 | Situations and content | Through the content engine contract, per role instance | All QA checks |
| 11 | Assessments and capstones | Per instance (CAPSTONE engine inputs: trigger, constraints, documents) | Assessment check |
| 12 | Claims | `CLM-…` for the industry, computed tier only | Claim control |

## What must *not* change

- Schemas;
- other industries;
- the core book;
- existing codes;
- the website and PDF code paths (they read any industry from the registry).

**If a step seems to need a schema change, stop.** Record it as an architecture issue for the author instead of patching the data.

## Minimum before any public mention of the new industry

The industry's computed tier must meet the claim (ROLE-QA-SPEC §6), with the specialist review recorded as PASS. NOT_PERFORMED does not count.
