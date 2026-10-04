# Seniority progression architecture

Part of the role engine ([ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE.md](ROLE-BASED-MULTI-INDUSTRY-ARCHITECTURE.md)). This is an architecture only: no lesson content is generated here. Every list below is **registry data, not hard-coded**: new levels, designations and layers are added as records.

## 1. Two independent axes

| | Axis A: English proficiency | Axis B: Professional responsibility |
|---|---|---|
| Values | A1, A2, B1, B2, C1, C2 (extensible: A2+, B1+ …) | Responsibility levels, section 2 (extensible) |
| Controls | **Language**: vocabulary range, grammar, text length and density, speed, idiom, nuance, scaffolding | **Content**: what is communicated, to whom, decision rights, accountability, time horizon, evidence, genres |
| Stored on | Every content variant (`cefr`) | Every role instance (`responsibilityLevel`) and inherited by its content |
| Learner record | Measured or self-selected English level | Current or target job level |

**Rule:**
- Seniority never implies CEFR, and CEFR never implies seniority.
- A B1 Front Office Manager and a C1 Front Office Executive are both valid targets (combination rules in section 5).

## 2. Responsibility levels (registry)

Each level is a record: `id`, `name`, `rank`, `layer`, `typicalDesignations[]`, `scope`.
- **Ranks are spaced** (10, 20 …), so a new level can be inserted (e.g. 65) without renumbering anything.
- **Order is always by `rank`.** It is never derived from a list's position.

| ID | Rank | Level | Layer | Typical designations (examples; industry titles map here) |
|---|---|---|---|---|
| SEN-0001 | 10 | Intern / Trainee | Operational | Intern, trainee, apprentice, management trainee |
| SEN-0002 | 20 | Assistant / Associate | Operational | Assistant, associate, commis, attendant, teaching assistant |
| SEN-0003 | 30 | Executive / Officer | Operational | Executive, officer, agent, associate (BPO), customer service officer |
| SEN-0004 | 35 | Specialist / Professional | Operational | Specialist, analyst, developer, trainer, **teacher**, accountant |
| SEN-0005 | 40 | Senior Executive / Senior Specialist / Coordinator | Operational (senior) | Senior executive, senior teacher, coordinator, subject coordinator |
| SEN-0006 | 50 | Supervisor / Team Leader | Supervisory | Supervisor, team leader, **restaurant captain**, shift in-charge, duty officer |
| SEN-0007 | 60 | Assistant Manager | Managerial | Assistant manager, academic coordinator (in many schools) |
| SEN-0008 | 70 | Manager | Managerial | Manager, branch manager, store manager, operations manager |
| SEN-0009 | 80 | Senior Manager / Department Head | Managerial (senior) | Senior manager, head of department, head teacher, F&B manager (department head) |
| SEN-0010 | 90 | Director / General Manager | Executive | Director (functional scope), general manager (multi-function scope), principal, academic director |
| SEN-0011 | 100 | Managing Director / CEO | Enterprise | Managing director, CEO, country head |
| SEN-0012 | — (track) | Founder / Entrepreneur | **Ownership track** | Founder, co-founder, owner, entrepreneur |

**Founder / Entrepreneur is a separate track**, not a rank (decision D-R03). A founder may be a solo trader or run a company of hundreds. The record therefore carries `scale: solo | small-team | company`. Content is chosen by scale and situation, and enterprise-layer functions apply once `scale = company`.

**Designations are separate records** (`designation` → `responsibilityLevel`, optional `industry`):
- "Restaurant Captain" (HOSP) → SEN-0006;
- "Principal" (EDU) → SEN-0010;
- "Duty Officer" (AVIA) → SEN-0006.

An industry-specific title never needs a new level.

## 3. Operational layer (SEN-0001 to SEN-0005)

| | |
|---|---|
| Purpose of communication | Do the work correctly; serve; inform; ask; report |
| Typical audiences | Customers / guests / patients / students; peers; supervisor |
| Time horizon | Now, this shift, today |
| Evidence used | What I saw or did; procedure |
| Decision rights | Within procedure; escalate the rest |
| Core functions | Greet; introduce; give and ask for information; clarify and read back; request; follow up; update status; report a problem; serve a customer; apologise; handle a routine complaint; escalate; write messages and short emails |
| Genres | Conversation; phone/chat; message; short email; handover note; simple report |

## 4. Supervisory layer (SEN-0006)

Adds the following to the operational layer:
- coordinate a shift;
- brief a team (pre-shift briefing);
- allocate tasks;
- check work;
- handle escalated complaints;
- support and correct staff on the spot;
- communicate with other departments;
- report shift performance;
- write incident reports.

- **Audience:** the team plus the manager.
- **Time horizon:** the shift and the week.

## 5. Combining the axes (CEFR × responsibility)

**What changes with CEFR, for the same content:**

| CEFR | Language treatment | Scaffolding |
|---|---|---|
| A1 | Fixed phrases; very short turns; present simple, imperatives; key nouns | Sentence frames for every turn; glossary for every content word; Bengali/Hindi support where triggered; one task at a time |
| A2 | Short connected sentences; past simple; polite modals (could, would) | Frames for most turns; a model answer before each task |
| B1 | Connected explanation; present perfect; first conditional; linking words | Frames for new functions only; a checklist |
| B2 | Hedging; passive for objectivity; reasons and consequences; register shifts | A rubric; minimal frames |
| C1 | Nuance; diplomatic precision; complex argument; idiomatic but clear | Rubric and self-review |
| C2 | Fully flexible and precise; implication; rhetorical control | Peer/expert review |

**Every combination is permitted:**
- **Low CEFR with high responsibility** (e.g. B1 + General Manager): the *content* stays managerial or executive (business review, decisions), while the *language* is scaffolded. The learner gets fixed frames for high-stakes moves: "The main reason is ___. My recommendation is ___. The risk is ___."
- **High CEFR with low responsibility** (e.g. C1 + Front Office Executive): the content stays operational, while language richness rises (nuanced apology, diplomatic refusal, written complaint replies).
- **Minimum language for very senior content:**
  - A1/A2 combined with Director, MD or Founder produces **"survival leadership English"**: short scripted openings, decisions and closings for meetings and presentations, clearly labelled as such.
  - Full board or investor communication is not attempted below B1 (generation rule; D-R04).

## 6. Manager English layer (SEN-0007 to SEN-0009)

**Not "Executive English with harder words".** The purpose, audience and accountability all change:

| Dimension | Operational | Manager |
|---|---|---|
| Purpose | Do and report | **Achieve results through others**; allocate; decide within the department |
| Audience | Customers, peers, supervisor | Own team; peer managers; senior management; key clients and vendors |
| Time horizon | Today | Week, month, quarter |
| Evidence | What happened | Metrics, trends, causes, options |
| Accountability language | "I did / I will" | "We will; I own this; the team will deliver X by Y" |
| Typical outputs | Messages, updates | Briefings, plans, reports, reviews, proposals |

**Manager function set** (each is a communication-function record):
- delegation;
- briefing;
- performance management (setting goals, reviewing, addressing underperformance);
- feedback;
- coaching;
- running meetings;
- decision-making and communicating decisions;
- problem solving with the team;
- conflict management;
- escalation upward;
- cross-department coordination;
- resource allocation (staff, budget, time);
- performance review;
- reporting to senior management;
- change communication;
- crisis communication;
- strategic communication (translating strategy for the team).

**Core coverage.** The existing core teaches much of this in Levels 4–5. The engine *applies* it to the instance:
- L5 M1 Delegation;
- L5 M2 Feedback & Performance (CF-0004 Underperformance-and-Support);
- L5 M3 Coaching;
- L5 M4 Change;
- L5 M5 Leading Meetings;
- L4 M2 Conflict (CF-0019);
- L4 M4 Decision Communication (CF-0021);
- L4 M6 Crisis (CF-0023).

## 7. GM / Director English layer (SEN-0010)

| Dimension | Manager | GM / Director |
|---|---|---|
| Purpose | Run a department | **Run the business unit or function**; balance departments; own results |
| Audience | Team; senior management | Department heads; owners / management company / board; major clients and partners; regulators (via specialists) |
| Time horizon | Month, quarter | Quarter, year, multi-year |
| Evidence | Department metrics | Business performance (revenue, cost, margin, satisfaction, risk); variance against budget |
| Language demands | Clear, structured | **Strategic, precise, diplomatic, analytical, persuasive, decision-oriented** |

**GM / Director function set:**
- business reviews (monthly and quarterly performance);
- department performance conversations;
- presenting strategy;
- budgets and variance explanation (communication about budgets, not accounting);
- risk communication;
- stakeholder management;
- major-incident leadership;
- cross-functional decisions;
- organisational change;
- leadership-team meetings;
- board / ownership communication;
- client and partner communication;
- public representation (staff addresses; community and industry events).

## 8. MD / Entrepreneur English layer (SEN-0011; SEN-0012 ownership track)

The focus is **professional English**. It is not a business-school course: business concepts appear only as the *content* the learner must express, at the level of job knowledge (see JOB-KNOWLEDGE-LAYER).

**MD functions:**
- vision and mission statements;
- strategy communication;
- explaining the business model;
- growth and investment discussions;
- partnership talks;
- articulating customer value;
- financial-awareness conversations;
- shaping organisational culture;
- hiring senior leaders;
- leading change;
- risk and crisis leadership;
- public speaking;
- company presentations;
- stakeholder communication;
- high-level negotiation;
- business proposals;
- media and public statements (where appropriate; basic, with communications-specialist caveats).

**Entrepreneur / Founder functions** (scale-aware):
- pitching;
- explaining the business in 30 seconds, 2 minutes and 10 minutes;
- describing the problem;
- explaining the solution;
- discussing the market;
- team building and first hires;
- investor communication;
- customer acquisition conversations;
- partnership discussions;
- business negotiation;
- vision statements;
- company presentations.

## 9. Progression qualities

As responsibility rises, generated language must become measurably more:

| Quality | Operational | Supervisory | Managerial | Executive / Enterprise |
|---|---|---|---|---|
| Strategic | — | — | Links tasks to department goals | Links decisions to business strategy |
| Precise | Accurate facts | Accurate facts + times | Metrics and commitments | Quantified outcomes, risks, trade-offs |
| Diplomatic | Polite | Firm and supportive | Balances competing interests | Manages power, reputation and relationships |
| Analytical | Describes | Describes + causes | Diagnoses + options | Weighs scenarios and risk |
| Persuasive | — | Motivates the team | Wins resources and support | Aligns owners, boards, partners and investors |
| Decision-oriented | Asks for decisions | Makes shift decisions | Makes and explains department decisions | Sets direction; explains contested decisions |

These are **rubric criteria** in assessments (ROLE-QA-SPEC, role realism and professional tone checks).

## 10. Example ladders (architecture only; no lessons generated)

### Front office (hospitality)

| Role (level) | Communication focus |
|---|---|
| Front Office Executive (SEN-0003) | Greeting guests; checking reservations; explaining hotel services; handling routine requests |
| Front Office Supervisor (SEN-0006) | Coordinating the shift; handling escalations; supporting staff; communicating with departments |
| Front Office Manager (SEN-0008) | Complex guest issues; staffing; reviewing operational performance; communicating with senior management |
| General Manager (SEN-0010) | Cross-department decisions; guest-experience strategy; operational performance; financial awareness; leadership communication |
| Managing Director (SEN-0011) | Strategic direction; business performance; investment; growth; stakeholder communication |

### Restaurant (hospitality)

- Restaurant Captain (SEN-0006: table allocation, service sequence, shift briefing)
- → Restaurant Supervisor (SEN-0006)
- → Restaurant Manager (SEN-0008: sales, staffing, standards, cost awareness)
- → F&B Manager (SEN-0009)

### Teaching (education)

| Role | Level | Communication focus |
|---|---|---|
| School Teacher | SEN-0004 | Classroom instructions; explaining concepts; checking understanding; correcting mistakes; student feedback; classroom management; parent communication; staff meetings; progress reports |
| Senior Teacher | SEN-0005 | Mentoring new teachers; leading subject discussions |
| Subject Coordinator | SEN-0005 | Coordinating syllabus and assessment across a subject; chairing subject meetings |
| Academic Coordinator | SEN-0007 | Timetabling; assessment calendars; parent escalations; teacher observation feedback |
| Head Teacher / Head of Department | SEN-0009 | Department performance; staffing; difficult parent conversations; reporting to the principal |
| Principal | SEN-0010 | Whole-school decisions; staff addresses; management committee and board; community and parents; crisis |
| Academic Director | SEN-0010 | Multi-school or academic strategy; curriculum policy; leadership meetings |

### Cross-industry ladders

- **HR:** HR Executive (SEN-0003) → HR Manager (SEN-0008) → HR Head (SEN-0009) → HR Director (SEN-0010)
- **Sales:** Sales Executive → Sales Manager → Sales Director
- **Operations:** Operations Executive → Team Leader → Operations Manager → General Manager

All of these are role records linked by `ladder` (next and previous role), so new rungs are data additions.

## 11. Leadership communication by layer

| Function | Operational | Supervisory | Managerial | Executive | Enterprise / Founder |
|---|---|---|---|---|---|
| Delegating | — | Allocating tasks | Delegating ownership | Delegating to managers | Delegating to the leadership team |
| Coaching | — | On-the-spot correction | Coaching conversations | Coaching managers | Mentoring leaders |
| Feedback | Receiving | Giving and receiving | Formal reviews | Leadership-team feedback | Board and investor feedback |
| Motivation | — | Team energy | Engagement and recognition | Unit morale | Culture |
| Performance | Own targets | Shift targets | Department KPIs | Business results | Company performance |
| Decision communication | — | Shift decisions | Department decisions | Cross-functional decisions | Strategic decisions |
| Change | Adapting | Explaining to the team | Leading department change | Leading organisational change | Setting direction |
| Conflict | Peer issues | Team conflicts | Inter-department conflict | Leadership-team conflict | Stakeholder conflict |
| Crisis | Report and follow protocol | Run the shift response | Department response | Lead the incident | Public / stakeholder leadership |
| Strategy | — | — | Translate for the team | Shape and present | Define |
| Stakeholders | Customers | Departments | Senior management, clients, vendors | Owners, board, partners | Investors, partners, public |

Content generation uses this table to choose which functions a role instance's curriculum includes (ROLE-CONTENT-BLUEPRINT §3).
