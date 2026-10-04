# Role content blueprint

What a **role-instance curriculum** contains, how it is assembled from the registry, and how it is sequenced. The examples are outlines (situation titles); no lessons are generated.

## 1. Inputs

| Input | From |
|---|---|
| Role core: responsibilities, stakeholders, functions by layer, documents, meetings, speaking situations | `roles/ROL-…` |
| Industry context: added or removed situations, stakeholders, documents, processes, risks, priorities | `role-instances/RIN-…` |
| Responsibility level, and therefore layer | `responsibility-levels` |
| Target CEFR | Learner / product choice |
| Communication functions and core links | `communication-functions` |
| Job knowledge (role, industry and instance scopes) | `job-knowledge` |

## 2. Assembly rule

```
situations(instance) = roleCore.situations ∪ industryContext.situationsAdded − industryContext.situationsRemoved
functions(instance)  = functions typical of the instance's layer (Seniority §11) ∩ functions its situations need
units                = situations grouped into a sequence (section 4), each unit = 1 main situation
```

## 3. Coverage targets for one role-instance curriculum

These are the minimum the instance needs to reach the **"role curriculum" tier** (ROLE-QA-SPEC §6). The numbers come from situation categories, not from a fixed lesson count.

| Layer of the instance | Situation categories that must each have at least one unit | Typical unit count |
|---|---|---|
| Operational | Daily work; customer/client; internal; manager communication; email; problem; complaint; escalation; training (receiving); feedback (receiving) | 10–12 |
| Supervisory | The operational set + team communication (briefing); meeting; report; conflict; performance (shift); crisis (shift response) | 14–16 |
| Managerial | Team; meeting (chair); report; presentation; problem; escalation (upward); conflict; crisis; negotiation; feedback; performance; training (delivering or arranging); decision; change; stakeholder | 16–18 |
| Executive (GM / Director) | Meeting (leadership); presentation (business review); stakeholder (owners / board); decision; change; crisis; negotiation; performance (department heads); report; leadership | 12–14 |
| Enterprise / Founder | Stakeholder (investors / partners / public); presentation (company / pitch); negotiation; decision; change; crisis; leadership; team building | 10–12 |

**Plus, for every instance:**
- one **capstone** (CAPSTONE engine, as in the earlier architecture §14, with role-instance inputs);
- one **performance assessment**;
- a **diagnostic** if the instance is offered stand-alone.

## 4. Sequencing

1. **Orientation unit:** the role, its stakeholders and its key job knowledge (short).
2. **Frequency first:** the situations the role meets daily come before rare ones.
3. **Stakes rise:** routine → problem → complaint / escalation → conflict / crisis.
4. **Modes interleave:** each 3–4 units include speaking, writing, a meeting or presentation, and reading.
5. **Integration unit** before the capstone.
6. **Capstone.**

## 5. Unit (lesson) template

Same 20 elements as the earlier architecture's industry lesson template, now keyed to the role instance. Required in every unit:
- objective;
- situation;
- role and stakeholder;
- communication goal (CFN);
- job-knowledge items (only those used);
- vocabulary (new and review);
- expressions;
- conversation (CNV);
- professional tone;
- speaking task;
- writing task;
- role-play;
- reflection;
- performance task;
- answer key.

Conditional (included when the unit needs them): grammar in context (cite core GIC), pronunciation/delivery, reading, listening (only if audio exists), problem solving, assessment items.

**Length:** core lessons average 5.0 print pages. Role units are planned at 4–6 pages.

## 6. Outlines for representative instances (situation titles only)

| Instance | Units (outline) |
|---|---|
| Front Office Executive · HOSP · B1 | Greeting and check-in; explaining services; phone reservations; routine requests; room not ready (complaint); billing question; handover note; asking the supervisor for approval; email confirmation to a guest; escalating an unhappy guest; receiving feedback; capstone: a difficult arrival |
| Restaurant Manager · HOSP · B2 | Pre-shift briefing; table and staffing plan; handling an escalated complaint; service-standards feedback; inventory and wastage discussion with the chef; weekly report to the F&B Manager; department meeting; training a new captain; cost discussion; conflict between service and kitchen; capstone: a full-house evening goes wrong |
| HR Manager · TECH · B2 | Recruitment priorities with an engineering head; interviewing for technical skills; offer negotiation; onboarding remote hires; performance calibration; grievance meeting; attrition report; change announcement (hybrid policy); capstone: hiring freeze communication |
| HR Manager · BPO · B2 | High-volume hiring plan; batch training schedule with operations; attrition review; shift-allowance grievance; quality-team staffing; capstone: an attrition spike before a client audit |
| Operations Manager · BPO · B2 | Daily metrics huddle; service-quality review with team leaders; client governance call; staffing escalation; underperformance conversation; process change; capstone: SLA breach month |
| School Teacher · EDU · B1 | Classroom instructions; explaining a concept; checking understanding; correcting mistakes; student feedback; parent meeting on progress; staff meeting contribution; progress-report comments; school event coordination; capstone: parent concern about a grade |
| General Manager · HOSP · C1 | Monthly performance to ownership; department-heads meeting; budget variance; guest-experience strategy; major incident leadership; staff address; partner negotiation; capstone: a difficult quarter review |
| Managing Director · GEN · C1 | Organisational change address; leadership-team meeting; board update; partner proposal; media statement (basic); culture conversation; capstone: restructuring communication |
| Entrepreneur · SMB · B2 | 30-second explanation; problem/solution pitch to a partner; customer conversation; first hire interview; partnership negotiation; investor update email; company presentation; capstone: partner pitch with Q&A |

## 7. Teacher as a full role

The Teacher ladder (Seniority §10) uses the G12 teaching and training functions:
- classroom instructions;
- explaining and checking understanding;
- correcting errors;
- learner feedback;
- parent progress reports.

All of these are new in the engine. They combine with the general functions (meetings, emails, difficult conversations). Senior teaching roles add the coordination, leadership and stakeholder functions of their layer.
