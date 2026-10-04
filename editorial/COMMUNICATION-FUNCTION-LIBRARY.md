# Communication function library

> **Update (4 October 2026):** the registry is now [COMMUNICATION-FUNCTION-LIBRARY.csv](COMMUNICATION-FUNCTION-LIBRARY.csv): 113 functions. CFN-0001…0084 are unchanged from this file; CFN-0085…0113 add frontline, field, trades and scheduling functions.

A **communication function** is what the speaker or writer is *doing* with language: requesting, escalating, delegating, pitching. Functions are the reusable middle layer of the role engine:
- **situations** select functions;
- **conversations, documents, meetings and presentations** realise them;
- the **core book** teaches many of them already.

**What this file contains:**
- the initial registry of **84 functions in 12 groups**;
- links to the existing core book (the lesson where taught, plus CF/PAT/GIC/TL codes), checked against `reference-index.json`;
- the 22 situation categories that select functions;
- CEFR exponent guidance.

**Status:** proposed registry. IDs are stable once approved. Names may change, IDs never.

## 1. Record format

```jsonc
{ "id": "CFN-0024", "name": "Escalate an issue", "group": "G6",
  "layer": "operational",                      // lowest layer where it is typical (seniority §2)
  "modes": ["speak", "write"],
  "skill": "SK-11",                            // skill registry from the earlier architecture
  "coreRefs": ["CE-L03-M01-L05", "CE-L03-M05-L04", "CE-L04-M06-L01"],
  "coreCodes": ["CF-0023"],
  "structure": "why now → to whom → what has been done → what is needed → by when",
  "newInEngine": false }
```

`newInEngine: true` marks a function **not taught in the core book**. The engine must provide its first full teaching, using the core's own lesson template.

**Layers:** Op = operational; Sup = supervisory; Mgr = managerial; Exe = GM / Director; Ent = MD / founder.

## 2. Registry

### G1 Social and relational

| ID | Function | Layer | Core (where taught) | Codes | New |
|---|---|---|---|---|---|
| CFN-0001 | Greet and respond to greetings by status | Op | L1 M3 (3.1) | TL-0002 | |
| CFN-0002 | Introduce yourself (role, background) | Op | L1 M1 (1.2–1.3) | GIC-0002, GIC-0003, CF-0002 | |
| CFN-0003 | Introduce others | Op | L1 M2 (2.2) | | |
| CFN-0004 | Make small talk; redirect unsafe topics | Op | L1 M3 (3.2–3.3) | CF-0003 | |
| CFN-0005 | Close a conversation politely | Op | L1 M3 (3.4); L1 2.5 | TL-0001 | |
| CFN-0006 | Thank specifically | Op | L2 M5 (5.3) | | |
| CFN-0007 | Apologise for your own mistake | Op | L2 M5 (5.1–5.2) | | |
| CFN-0008 | Apologise on behalf of the team or organisation | Sup | L2 M5 (5.4) | | |
| CFN-0009 | Congratulate and recognise | Sup | — | | ✔ |

### G2 Information

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0010 | Give information clearly | Op | L2 M7 (7.2) | | |
| CFN-0011 | Ask for information | Op | L1 M5 | | |
| CFN-0012 | Explain a process or concept to a non-expert | Op | L2 7.2 | | |
| CFN-0013 | Ask for clarification / repetition | Op | L1 M5; L2 3.3 | CF-0001 | |
| CFN-0014 | Confirm and read back (critical details) | Op | L1 M4 (4.2) | CF-0001 | ✔ (safety-critical read-back) |
| CFN-0015 | Check understanding (yours or theirs) | Op | L1 4.2 | | |
| CFN-0016 | Summarise | Sup | L3 M3 (3.4) | | |
| CFN-0017 | Say "I don't know — I'll find out" | Op | L2 M7 (7.3) | | |
| CFN-0018 | Relay a message between people | Op | L2 M2 (2.4); L2 3.2 | GIC-0006 | |

### G3 Action

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0019 | Make a polite request | Op | L1 M7 (7.2); L2 M2 | GIC-0005, TL-0003 | |
| CFN-0020 | Decline / say no professionally | Op | L2 M2 (2.2); L4 M2 (2.1) | TL-0010 | |
| CFN-0021 | Negotiate timing and scope of a task | Op | L2 M2 (2.3) | | |
| CFN-0022 | Follow up and remind | Op | L2 M6 | CF-0007 | |
| CFN-0023 | Make a suggestion or recommendation | Op | L3 M3 (3.3); L3 M2 (2.5) | | |
| CFN-0024 | Escalate an issue | Op | L3 M1 (1.5); L3 M5 (5.4); L4 M6 | CF-0023 | |
| CFN-0025 | Give instructions | Sup | L1 M4 (receiving); L5 M1 (giving) | GIC-0001, GIC-0004 | |
| CFN-0026 | Offer help or an alternative | Op | L2 M7 (7.4) | | |

### G4 Reporting

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0027 | Give a status update (done / doing / blocked) | Op | L2 M1 (1.1) | PAT-0025 | |
| CFN-0028 | Report a problem or delay | Op | L2 M1 (1.2) | | |
| CFN-0029 | Report an incident (facts → evidence → analysis → action) | Op | L3 M2 (2.1, 2.3) | GIC-0010 | |
| CFN-0030 | Report performance / metrics | Sup | L3 M2 (2.4); L3 M4 (4.2–4.3) | GIC-0017 | |
| CFN-0031 | Explain variance against target or budget | Mgr | — | | ✔ |
| CFN-0032 | Match update detail to the audience | Op | L2 M1 (1.3) | | |
| CFN-0033 | Hand over a shift or task | Op | L5 capstone (handover) | | ✔ (as a taught function) |

### G5 Service

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0034 | Welcome a customer / guest / patient / client | Op | L2 M7 (7.1); L3 M6 (6.1) | TL-0007 | |
| CFN-0035 | Identify needs through questions | Op | L3 M6 (6.2) | | |
| CFN-0036 | Explain a policy and its limits | Op | — | | ✔ |
| CFN-0037 | Handle a routine complaint | Op | L2 M7 (7.4) | | |
| CFN-0038 | Listen with empathy and de-escalate | Op | L3 M5 (5.1–5.2) | | |
| CFN-0039 | Present a solution and manage expectations | Op | L3 M5 (5.3); L4 M8 (8.4) | | |
| CFN-0040 | Recover service | Sup | L3 M5 (5.5) | CF-0013 | |
| CFN-0041 | Close a customer interaction | Op | L2 M7 (7.5); L2 3.5 | CF-0008, CF-0005 | |
| CFN-0042 | Upsell / recommend a product or service | Op | — | | ✔ |

### G6 Problem, escalation and crisis

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0043 | Explain a problem (what, impact, cause, next step) | Op | L4 M4 (4.1) | | |
| CFN-0044 | Explore options and trade-offs | Sup | L4 M4 (4.2) | | |
| CFN-0045 | Deliver bad news | Sup | L4 M6 (6.2) | | |
| CFN-0046 | Give a crisis update | Sup | L4 M6 (6.4–6.5) | CF-0023 | |
| CFN-0047 | Communicate calmly under pressure | Op | L4 M6 (6.1) | | |
| CFN-0048 | Admit and report a serious mistake | Op | L4 M2 (2.4) | | |
| CFN-0049 | Manage unrealistic expectations or deadlines | Sup | L4 M6 (6.3) | | |

### G7 Meetings

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0050 | Invite and set an agenda | Sup | L3 M3 (3.1) | | |
| CFN-0051 | Open a meeting and set objectives | Sup | L3 M3 (3.2) | | |
| CFN-0052 | Give and ask for opinions; agree / disagree diplomatically | Op | L3 M3 (3.3) | | |
| CFN-0053 | Interrupt politely; clarify; summarise | Op | L3 M3 (3.4) | | |
| CFN-0054 | Assign action points and close | Sup | L3 M3 (3.5) | CF-0011 | |
| CFN-0055 | Chair a meeting as its owner; keep it on time | Mgr | L5 M5 (5.1, 5.4) | | |
| CFN-0056 | Write minutes and follow up | Sup | L3 M3 (3.6) | | |

### G8 Persuasion, presentation and negotiation

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0057 | Present data and key points | Sup | L3 M4 | CF-0012 | |
| CFN-0058 | Handle questions after a presentation | Sup | L3 M4 (4.5); L4 M5 (5.2) | | |
| CFN-0059 | Build a persuasive argument with evidence | Mgr | L4 M3 | CF-0020 | |
| CFN-0060 | Influence without authority | Sup | L4 M3 (3.4) | | |
| CFN-0061 | Handle objections | Op | L3 M6 (6.4) | TL-0008 | |
| CFN-0062 | Negotiate terms (prepare, anchor, trade, close) | Mgr | L4 M1 | TL-0009, CF-0018 | |
| CFN-0063 | Present to a senior or executive audience | Mgr | L4 M5 (5.1); L5 M6 | TL-0012, CF-0022, CF-0026 | |
| CFN-0064 | Pitch a business idea (problem → solution → value → ask) | Ent | — | | ✔ |

### G9 People leadership

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0065 | Brief a team (pre-shift / daily briefing) | Sup | — (L3 M3 partly) | | ✔ |
| CFN-0066 | Delegate a task and ownership | Sup | L5 M1 | | |
| CFN-0067 | Give everyday feedback | Sup | L5 M2 (2.1); L4 M2 (2.2) | | |
| CFN-0068 | Receive criticism gracefully | Op | L4 M2 (2.3) | | |
| CFN-0069 | Run a formal performance conversation; set goals | Mgr | L5 M2 (2.2–2.3, 2.5) | | |
| CFN-0070 | Address underperformance | Mgr | L5 M2 (2.4) | CF-0004 | |
| CFN-0071 | Coach through questions | Mgr | L5 M3 | | |
| CFN-0072 | Resolve conflict | Sup | L4 M2 (2.5–2.6) | CF-0019, TL-0011 | |
| CFN-0073 | Motivate and recognise a team | Sup | — | | ✔ |

### G10 Decision and direction

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0074 | Communicate a decision and its reasoning | Mgr | L4 M4 (4.3); L5 M5 (5.3) | CF-0021 | |
| CFN-0075 | Announce a change; address resistance | Mgr | L5 M4 (4.2–4.3) | | |
| CFN-0076 | Explain the "why" behind a strategy | Exe | L5 M4 (4.1); L5 M6 (6.2) | | |
| CFN-0077 | Allocate resources and set priorities | Mgr | — (L1 M4 receiving priorities) | | ✔ |

### G11 Stakeholder and external

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0078 | Report to ownership / board (business review) | Exe | — | | ✔ |
| CFN-0079 | Manage a client or vendor relationship over time | Mgr | L4 M8 | CF-0025, TL-0014 | |
| CFN-0080 | Represent the organisation publicly (address, statement) | Exe | — | | ✔ |
| CFN-0081 | Communicate with investors and partners | Ent | — | | ✔ |

### G12 Teaching and training

| ID | Function | Layer | Core | Codes | New |
|---|---|---|---|---|---|
| CFN-0082 | Give classroom or training instructions | Op | — | | ✔ |
| CFN-0083 | Explain a concept to learners and check understanding | Op | — | | ✔ |
| CFN-0084 | Correct errors and give learner feedback; report progress to parents | Op | — | | ✔ |

### Totals

- **84 functions.**
- **16 are marked new** (✔): 13 not taught in the core at all, and 3 the core covers only partly (CFN-0014 safety-critical read-back, CFN-0033 handover, CFN-0065 team briefing).
- **The other 68** cite where the core teaches them. Their engine content *applies* the core teaching to role instances rather than re-teaching it.

**Cross-cutting core resources:**
- Career self-advocacy: CF-0027, L5 M7.
- Personal leadership voice: CF-0028, L5 M8.
- Channel choice: CF-0006, L2 M4; CF-0017, L3 M9.
- Email threads: CF-0009, L3 M1.

These attach to many functions through `coreCodes`.

## 3. Situation categories → typical function groups

| # | Situation category (brief §18) | Typical groups |
|---|---|---|
| 1 | Daily work | G2, G3, G4 |
| 2 | Customer / client interaction | G5, G1 |
| 3 | Internal communication | G2, G3 |
| 4 | Manager communication | G4, G3, G6 |
| 5 | Team communication | G9, G3 |
| 6 | Meeting | G7 |
| 7 | Email | Any (mode = write) |
| 8 | Report | G4 |
| 9 | Presentation | G8 |
| 10 | Problem | G6 |
| 11 | Complaint | G5 |
| 12 | Escalation | G6 (CFN-0024) |
| 13 | Conflict | G9 (CFN-0072) |
| 14 | Crisis | G6 (CFN-0046) |
| 15 | Negotiation | G8 (CFN-0062) |
| 16 | Feedback | G9 |
| 17 | Performance | G9, G4 |
| 18 | Training | G12, G9 |
| 19 | Leadership | G9, G10 |
| 20 | Decision | G10 |
| 21 | Change | G10 |
| 22 | Stakeholder communication | G11, G8 |

Email, report and presentation are both situation categories and output *modes*. A situation records its category and the modes it requires.

## 4. CEFR exponent guidance

Each function record holds `exponents` by CEFR level: typical language, not scripts. Generation uses the level-appropriate exponents (see SENIORITY §5).

| Function | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| CFN-0024 Escalate | "I need help with this. Can you call the manager?" | "I need to escalate this because the guest is still waiting and I can't solve it." | "I'm escalating this now because it's outside what I'm authorised to offer, and the guest needs an answer within the hour." | "I'm bringing this to you directly: we've exhausted the options at desk level, and further delay carries a real reputational risk." |
| CFN-0074 Communicate a decision | "We will start at 9. This is the new time." | "We've decided to start at 9 because the morning is busier." | "The decision is to move the start to 9. The reason is ___; what doesn't change is ___." | "I know not everyone agreed, and I've weighed that. Here's the call and why I'm confident in it." |
| CFN-0064 Pitch | "We help small hotels. Our app saves time." | "Small hotels lose bookings because ___. Our app ___." | "The problem is ___; our solution ___; early results show ___; we're looking for ___." | "Here's a problem costing ___ a year; here's why existing answers fail and why we're positioned to win." |

A1 and C2 exponents are added when those ranges are approved for production (D-R04).
