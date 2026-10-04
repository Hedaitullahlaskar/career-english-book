# Role addition blueprint

**Procedure** to add a role with **no architecture change**.

**Worked example:** Procurement Manager. It is already in the proposed registry as ROL-0031, so it is used here only to show the steps.

## Steps

| # | Step | Records | Check |
|---|---|---|---|
| 1 | Choose or create the role family | Existing `RFM` (PROC). A new family needs a scope code (shared namespace, collision-tested). | Family exists |
| 2 | Register the role | `ROL-00nn`: `name`, `family`, `defaultLevel` (SEN-0008), `allowedLevels` (SEN-0007…SEN-0009), `ladder` (prev: Procurement Executive; next: Procurement Head), `defaultDepartment` (Procurement / Purchasing) | Not a duplicate of an existing role under another name; designations are records, not roles |
| 3 | Define the role core | `roleCore`: responsibilities (sourcing, supplier evaluation, negotiation, purchase approvals, supplier performance, cost reporting); stakeholders (suppliers, finance, requesting departments, management); functions by layer (CFN: CFN-0062 negotiate, CFN-0079 vendor relationship, CFN-0030 report metrics, CFN-0074 communicate decisions …); documents (RFQ email, supplier evaluation summary, purchase approval note, monthly cost report); meetings (supplier review, department budget meeting); speaking situations (supplier negotiation, presentation of savings) | Functions exist in the library; any missing function is added there first, as a separate record |
| 4 | Role-core job knowledge | `JKN` scope `role:ROL-…`: quotation cycle, purchase order, lead time, total cost, supplier scorecard (meaning only) | Used by content |
| 5 | Role-family vocabulary | `V-PROC-nnnn` for terms that follow the role across industries | De-duplication |
| 6 | Place the role in departments | Role × department matrix: Primary = Procurement / Purchasing; alternatives (Administration in EDU and SMB) | — |
| 7 | Attach to industries | Role × industry matrix values. Create instances where needed: HOSP (food, linen, amenities: links naturally to the core's linen negotiation, L4 M1); TECH (software licences, hardware); HLTH (medical supplies: **specialisation**, specialist review); MFG (raw materials: **specialisation**); RETL (merchandise) | Each instance's context differs at situation level |
| 8 | Seniority variants | The same role at SEN-0007 and SEN-0009 changes function emphasis (Seniority §11), not just vocabulary | Seniority-fit check |
| 9 | Content | Via the content-engine contract | All QA checks |
| 10 | Claims | Role and instance claims from computed tiers | Claim control |

## Rules

- **A designation is not a new role.** "Purchase Manager", "Buyer" and "Sourcing Lead" are designation records mapped to Procurement roles.
- **A role that exists only in one industry is still a reusable role record.** It simply has instances in one industry (e.g. Restaurant Captain).
- **Never copy another role's content.** Shared material is reached through functions, core links and role-family vocabulary.
