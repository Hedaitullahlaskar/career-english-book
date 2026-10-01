# Level 5 · Capstone · The Handover
L = "CE-L05-CAPSTONE"
D = 16
QA = "QA review of the reference PDF (final capstone)"
HOW_TO_SCORE = ("<p><strong>How to score it:</strong> give each row a mark from 0 to 4 (0 = not shown, 1 = rarely, 2 = sometimes, 3 = mostly, 4 = consistently). "
                "Multiply by the row's weight and divide by 4 — for example, 3 for Delegation calibration gives 15 × 3 ÷ 4 ≈ 11 points. Add the rows for a total out of 100. "
                "<strong>70 or more:</strong> Level 5 — and the course — complete. <strong>Below 70:</strong> repeat the steps that use the modules behind your lowest rows, then perform the whole week again.</p>\n"
                "<p>Score the whole performance, not each step separately.")
RUBRIC = "The Level 5 Assessment now scores each part with its own criteria, so the capstone no longer 'reuses the same rubric'."
STAFF = ("Staffing contradiction: in Step 4 Arif had already granted Hasan's senior-heavy roster for the launch weekend, yet Step 5 holds a meeting to decide the same "
         "question and reaches a different answer (one senior paired with one newer person), which it then calls 'Hasan's version'. Step 4 now defers the decision to the "
         "Step 5 meeting, and Step 5 names the compromise accurately.")
ROSTER = ("Hasan was given full ownership of the front-desk roster in Step 1, so Farhan cannot be the one who 'builds the schedule'; Farhan now briefs the newer staff, "
          "and the decision reaches him with its reasoning, as Module 5 teaches.")

# Objectives, About and rubric
fix(L, "against the same rubric used for the Level 5 assessment,", "against a weighted leadership rubric,", RUBRIC, "assessment")
fix(L, "the same rubric the Level 5 assessment used, reused deliberately --", "with the rows adapted to Level 5 --", RUBRIC, "assessment")
fix(L, "This is the same rubric the Level 5 Assessment used -- reused deliberately, so nothing about how\nyou're scored changes on the week that matters most.",
    "It uses the same weighted 0–4 format as the earlier capstones, with rows adapted to Level 5; every row applies, because the week includes delegation, feedback, a contested decision, a briefing and a career conversation.",
    RUBRIC, "assessment")
fix(L, "<p><strong>How to use it:</strong> score the whole eight-step performance once, as a single connected piece, not\nstep by step.",
    HOW_TO_SCORE, "The rubric gave weights but no scale, no method for combining them, and no completion threshold.", "assessment", source=QA)
fix(L, "A learner who fumbles a word in Step 1", "Someone who fumbles a word in Step 1", "Meta wording ('a learner').", "production")
fix(L, "Scored holistically against the capstone's rubric, not step-by-step.", "Score it with the self-assessment rubric above.",
    "Tied the key to the rubric's explicit scoring method.", "assessment")

# Timeline
fix(L, "<h2>The simulation: the week before the handover</h2>", "<h2>The simulation: the first week of the handover</h2>",
    "The steps take place during Arif's first week covering for Ms. Noor, not the week before.", "continuity", source=QA)
fix(L, "have been late three shifts running this week, with small details missing each\ntime",
    "have started arriving late, with small details missing each time",
    "On Monday afternoon (the first conversation) the notes could not yet have been late 'three shifts running this week'; by Wednesday Farhan himself counts three.",
    "continuity", source=QA)
fix(L, "Six months ago, you caught a billing error nobody else noticed.", "A few weeks ago, you caught a billing error nobody else noticed.",
    "The setting says the billing catch was 'not long ago' (and the Level 5 Assessment places it 'last week'), not six months ago.", "continuity", source=QA)
fix(L, "from the new mobile\ncheck-in pilot before", "from the mobile check-in pilot (the first step in the self-check-in plan Arif presented in Module 6) before",
    "Linked the pilot to the self-check-in plan approved in Module 6, which otherwise disappears from the story.", "continuity")
fix(L, "the mobile check-in pilot's early results\ndirectly to Dr. Rahman", "the mobile check-in pilot's launch plan directly to Dr. Rahman",
    "The briefing is on Thursday and the pilot launches on Friday, so there can be no 'early results' yet.", "continuity", source=QA)

# Staffing and participants
fix(L, "If I can hold the senior-heavy roster through just the launch weekend before easing back to what Rima wants, I think it's manageable.",
    "If we staff the launch weekend properly — not just hope it goes smoothly — I think it's manageable.", STAFF, "continuity", source=QA)
fix(L, "Done. Adjust the roster your way for the launch weekend -- we'll revisit after that.",
    "Agreed. Let's settle the launch-weekend staffing this afternoon, with you and Rima both in the room.", STAFF, "continuity", source=QA)
fix(L, "Both real concerns. We're going with Hasan's version for this one weekend only -- one senior person paired with one newer person per shift, not a fully senior roster, but never a trainee alone either. Rima, I know that's not your first choice.",
    "I hear both sides of this — both are real concerns. Here's the call I'm making: for this one weekend, one senior person paired with one newer person on every shift. That's not the fully senior roster Hasan wants, but never a trainee alone either. I recognize this isn't unanimous. Rima, I know it's more cautious than your first choice.",
    STAFF, "continuity", source=QA)
fix(L, "Farhan -- for Friday through Sunday, it's one senior-paired-with-one-newer per shift for mobile check-in launch, full stop. Hasan and Rima didn't fully agree on it, but that's the call, and it's only for this one weekend.",
    "Farhan — for the mobile check-in launch, Friday through Sunday, every shift is one senior person paired with one newer person. The reasoning is that it covers the risk of a brand-new system without the overtime of a fully senior roster. Hasan and Rima didn't fully agree, but that's the call, and it's for this one weekend only. Here's what I need from you: brief the newer staff on who they're paired with — Hasan is posting the roster tonight.",
    ROSTER, "continuity", source=QA)
fix(L, "launch weekend only. I'll build the schedule around that.", "launch weekend only. I'll brief the newer staff today.", ROSTER, "continuity", source=QA)

# Wording
fix(L, "A long-\nstaying guest", "A long-staying guest", "Stray line break inside a hyphenated word.", "typography")
fix(L, "since the double- booking problems started.", "since the double-booking problems started.", "Stray space after the hyphen.", "typography")
fix(L, "Let's put together the actual case together over the next few weeks.", "Let's build the actual case together over the next few weeks.",
    "'Put together … together' repeated the word.", "language")
fix(L, "three different registers\n(a trainee, a peer, a General Manager),",
    "four different audiences (a newer colleague, experienced peers, a struggling colleague and a General Manager),",
    "Nobody in the capstone is a trainee, and the rubric itself lists four audiences, not three.", "factual")
fix(L, "audience in turn -- a trainee, a peer in disagreement,", "audience in turn — a newer colleague, a peer in disagreement,",
    "Nobody in the capstone is a trainee; Rima is a newer colleague.", "factual")
fix(L, "for each audience (a trainee, a peer, a struggling colleague, and a General Manager)", "for each audience (a newer colleague, a peer, a struggling colleague, and a General Manager)",
    "Nobody in the capstone is a trainee; Rima is a newer colleague.", "factual")
fix(L, "chaired a room a General Manager sat in.", "briefed a room the General Manager sat in.",
    "In Step 6 Arif presents at the department-head briefing; he does not chair it.", "factual")
