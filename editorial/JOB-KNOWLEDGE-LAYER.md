# Job knowledge layer

**Job knowledge** is the basic contextual knowledge a learner needs so that the English is meaningful. For example, a Restaurant Captain must know what a service sequence is before discussing it.
- It is **not professional certification**, technical training or advice.
- It is the minimum needed to understand and perform the role's workplace communication.

## 1. Boundaries

| Included | Excluded |
|---|---|
| Concepts the role talks about (occupancy, SLA, attrition, KYC, service sequence) | How to do the technical job (accounting rules, clinical procedures, coding) |
| Processes at the level of "who does what, in what order" | Legal, medical, financial or safety *advice* |
| Metrics the role reports and what they mean | Formulas beyond what communication needs |
| Documents the role reads or writes, and their purpose | Jurisdiction-specific regulation detail (kept generic; specialist-reviewed) |
| Stakeholders and their expectations | Proprietary or company-specific procedures |
| Typical constraints (policy, privacy, safety) and the correct escalation | Safety instructions in place of official SOPs |

**Disclaimer rule:** units containing job knowledge carry a standard note, wording for approval under D-R10, along these lines:

> "Workplace context for language learning. Follow your organisation's procedures and qualified professionals."

Items in regulated or safety-sensitive areas also set `disclaimerRequired: true`.

## 2. Item model (`JKN-000001`)

Scope decides reuse:

| Scope | Example | Reused by |
|---|---|---|
| `role:ROL-…` (role core) | HR Manager: what onboarding involves | Every HR Manager instance in every industry |
| `industry:IND-…` (industry context) | Hospitality: what occupancy and ADR mean | Every role instance in hospitality |
| `instance:RIN-…` (specific) | HR Manager in BPO: training batches and attrition | Only that instance |

| Kind | Meaning |
|---|---|
| `concept` | A term or idea |
| `process` | Steps and owners |
| `metric` | What is measured; what good and bad look like |
| `document` | Purpose and parts |
| `stakeholder` | Who they are and what they expect |
| `constraint` | What may not be said or offered, and to whom to escalate |
| `tool` | System or equipment, named generically |

**Length:**
- 40–120 words per item, in plain English at the unit's CEFR level;
- key terms link to vocabulary codes;
- a `sourceNote` records the basis (author knowledge, SME, public reference).

## 3. Selection principle

Only knowledge that **a conversation, document, meeting or task in the curriculum actually uses** is included. A generated unit whose dialogue assumes a JKN item it does not teach or reference fails the job-knowledge check. This keeps the layer from growing into a training manual.

## 4. Example outlines (titles only; no content generated)

| Role (instance) | Job-knowledge item titles |
|---|---|
| Restaurant Captain (HOSP) | Table allocation; reservations and walk-ins; the service sequence; handling guest requests; complaint basics and when to call the manager; the bill and payment; shift handover; the pre-shift briefing |
| Restaurant Manager (HOSP) | Covers and sales; staffing and rosters; inventory and wastage; service standards; complaint patterns; cost awareness (food cost, labour); training; staff performance |
| General Manager (HOSP) | Occupancy; ADR and RevPAR (meaning only); guest satisfaction scores; staffing levels; department performance; budget and variance; owner / management-company relationship; business priorities |
| School Teacher (EDU) | Lesson structure; classroom routines; assessment types; progress records; parent communication norms; school calendar; safeguarding referral (*who to tell*, not procedure) |
| HR Manager (core) | Recruitment cycle; interviewing; onboarding; performance cycle; grievance process; training needs; employee communication |
| HR Manager (+TECH context) | Technical roles and skill assessment; remote and hybrid teams; project staffing |
| HR Manager (+BPO context) | High-volume hiring; shift staffing; attrition; training batches; quality teams |
| HR Manager (+HOSP context) | Seasonal recruitment; shift staffing; staff accommodation; guest-service training; department structure |
| Entrepreneur (SMB) | Problem and solution; customer segments; revenue model (meaning only); early metrics; partners; funding stages (meaning only) |

## 5. Review

| Content | Review required |
|---|---|
| Industry-scope items in regulated or safety industries (healthcare, banking, aviation, manufacturing safety, education safeguarding) | **Specialist review** |
| All items | Role-realism review |

If no reviewer is available, the item's review field is `NOT_PERFORMED`, and the instance cannot reach the claim tiers that require that review (ROLE-QA-SPEC §6).
