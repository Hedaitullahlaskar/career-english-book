# Level 5 · Module 1 · Delegation & Instruction-Giving
PH = "The answer key gave an unfilled template ('[reason]', '[deadline]'); replaced with a sample answer."

L = "CE-L05-M01-L01"
fix(L, "the learner is the one giving the\ninstruction,", "you are the one giving the instruction,", "Meta wording ('the learner').", "production")
fix(L, "there, the learner practiced noticing when one of these four parts was missing and asking for it.\nHere, the learner supplies all four",
    "there, you practiced noticing when one of these four parts was missing and asking for it. Here, you supply all four",
    "Meta wording ('the learner').", "production")
fix(L, "Suggested answer: I'd like to hand this off to you. The context here is [reason]. I need it by [deadline]. Here's what done looks like -- [plain description].",
    "Sample: \"I'd like to hand this off to you: the lost-property log. The context here is that two guests have asked about items this week and we couldn't find them quickly. I need it by Friday. Here's what done looks like — every item from this month entered in the log with the date, the room and where it's stored.\"",
    PH, "production")

L = "CE-L05-M01-L02"
rule("L5-1.2-daily-report", r"run (this\s+report|it) every week for three years", r"run \1 every day for three years",
     "The room-status report is daily (the lesson says Hasan has done it 'every day for three years'); 'every week' contradicted that.",
     "continuity", fields=("body_html",), targets=[L], expect=2)
fix(L, "(Module 1, L03 -- calibrating how much detail", "(Lesson 1.3 — calibrating how much detail", "Internal lesson code replaced.", "reference")
fix(L, "(Level 1,\nModule 7, L01)", "(Level 1, Lesson 7.1)", "Internal lesson code replaced.", "reference")
fix(L, "Suggested answer: Beginner: Let me walk you through this in full, since it's your first time... / Experienced: Since you've done this before, I'll trust your judgment on...",
    "Sample (task: the end-of-day cash report). Beginner: \"Let me walk you through this in full, since it's your first time. You'll print the shift summary, count the float, enter both totals in the cash sheet and get me to sign it — I'll do the first one with you.\" Experienced: \"Since you've done this before — the usual cash report tonight. The only change is that the float is now 5,000 taka. I'll trust your judgment on anything that doesn't balance.\"",
    "The answer key gave only the first words of each version; replaced with a complete sample.", "production")

L = "CE-L05-M01-L03"
fix(L, "but PAT-0017 also spells out every step, while PAT-0018", "but PAT-0017 also pins down exactly what done looks like, while PAT-0018",
    "PAT-0017 (task, context, deadline, what done looks like) does not spell out steps; the contrast is with the defined finish line.", "grammar")
fix(L, "appropriate once the\nlearner is delegating", "appropriate once you are delegating", "Meta wording ('the learner').", "production")
fix(L, "In Scene A, why does Hasan get stuck when the guest doesn't want a room change?",
    "In Scene A, why is Hasan unsure what to do if the guest doesn't want a room change?",
    "Scene A never shows the guest refusing; Hasan only asks what to do if they do.", "answer-key")
fix(L, "<p>Suggested answer: The goal here is [outcome]. Use your judgment on [decision point]. I trust you to figure out the details.</p>",
    "<p>Sample: \"The goal here is a conference room that's ready and welcoming when the client walks in at nine. Use your judgment on the layout and whether we need extra chairs. I trust you to figure out the details — just message me when it's set.\"</p>",
    PH, "production")

L = "CE-L05-M01-L04"
fix(L, "combining clear instructions (L01), calibrated detail (L02), and ownership (L03)",
    "combining clear instructions (Lesson 1), calibrated detail (Lesson 2), and ownership (Lesson 3)", "Internal lesson codes replaced.", "reference")
fix(L, "<p><em>(recycled only, synthesis lesson by design — see below)</em>\n- <strong>just following up on</strong> (Level 2, Module 6, L02)",
    "<p>Recycled: <strong>just following up on</strong> (Level 2, Lesson 6.2)",
    "Internal production note and lesson code replaced.", "production")
fix(L, "checking the outcome, not auditing the process).",
    "checking the outcome, not auditing the process). Score each person's delegation 0–4, one point per criterion; pass at 3 for each person, and Completeness must be one of them.",
    "The module assessment had no scale.", "assessment")
fix(L, "Suggested answer: Just following up on [task] -- how did that go? Anything you need from me?",
    "Sample: \"Just following up on the supplier invoices — how did that go? Anything you need from me?\"", PH, "production")
fix(L, "<p>What to listen/look for: Each delegation is complete",
    "<p>Score with the four criteria in the Module 1 Assessment section (0–4 per person). What to listen/look for: Each delegation is complete",
    "The module assessment had no scale.", "assessment")
