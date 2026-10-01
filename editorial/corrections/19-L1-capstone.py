# Level 1 · Capstone
L = "CE-L01-CAPSTONE"
TIMELINE = ("Level 1 covers Arif's first weeks in the job (the capstone is set 'several weeks into the job'), but he said he had been there "
            "'about eight months' and the title promised a single first week.")

fix(L, 'Your First Week at Work', 'Your First Weeks at Work', TIMELINE, "continuity", field="title")
fix(L, 'under the same conditions a real first week gives you', 'under the same conditions your first weeks in a job give you', TIMELINE, "continuity")
fix(L, 'The Accounts corner, a few minutes later. Priyanka is showing a new hire, Meghla, around.',
    'The back office, a few minutes later. Priyanka is showing a new hire, Meghla, around.',
    "Priyanka is Arif's front-office colleague; the scene is in the front-office back room.", "continuity")
fix(L, 'Meghla, this is Arif -- he handles a lot of the coordination between our floor and Operations.',
    'Meghla, this is Arif — he\'s on the front desk with me.',
    "'Operations' contradicted Arif's front-office role (Lessons 1.3–1.5, 2.2).", "continuity")
fix(L, "I'm Arif -- I've been here about eight months now, mostly on the operations side. Let me know if you ever need help finding your way around.",
    "I'm Arif — I joined the front-office team a few weeks ago, so I still remember how confusing the first days are. Let me know if you ever need help finding your way around.",
    TIMELINE, "continuity")
fix(L, 'Arif, before lunch, can you pull last week\'s client feedback forms and send Priyanka the summary? She needs it before the 3 PM review.',
    'Arif, can you pull last week\'s client feedback forms and send Priyanka a summary? She needs it before the 3 PM review.',
    "The instruction gave two different deadlines ('before lunch' and 'before the 3 PM review'); Arif's restatement and every later step use 3 PM.",
    "continuity")
fix(L, "and Priyanka's confirmed she has what she needs for the 3 PM review.",
    "and Priyanka confirmed she had what she needed for the 3 PM review.",
    "At 5:40 PM the 3 PM review is over, so the present tense was wrong.", "grammar")
fix(L, "It's the same rubric Module 2's\nassessment introduced -- the capstone deliberately reuses it, so nothing about the scoring format\nis new on the day that matters most.",
    "Every row applies here, because the capstone is one continuous spoken role-play.",
    "The rubric was said to come from a 'Module 2 assessment' that does not exist.", "assessment")
fix(L, "<p><strong>How to use it:</strong> this is graded holistically, not step-by-step.",
    "<p><strong>How to score it:</strong> give each row a mark from 0 to 4 (0 = not shown, 1 = rarely, 2 = sometimes, 3 = mostly, 4 = consistently). "
    "Multiply by the row's weight and divide by 4 — for example, 3 for Clarity gives 15 × 3 ÷ 4 ≈ 11 points. Add the rows for a total out of 100. "
    "<strong>70 or more:</strong> Level 1 complete. <strong>Below 70:</strong> repeat the steps that use the modules behind your lowest rows, then perform the whole day again.</p>\n"
    "<p>Score the whole performance, not each step separately.",
    "The rubric gave weights but no scale, no method for combining them, and no completion threshold.", "assessment",
    source="QA review of the reference PDF (assessments)")
fix(L, 'A learner who\nhandles Step 8', 'Someone who\nhandles Step 8', "Meta wording ('a learner') in reader-facing guidance.", "production")
fix(L, 'Level 1 capstone task. Perform all nine steps of "Your First Week at Work"', 'Level 1 capstone task. Perform all nine steps of "Your First Weeks at Work"',
    TIMELINE, "continuity")
fix(L, '<p>What to listen/look for: Completes all nine steps in order,', '<p>Score with the self-assessment rubric above. A strong performance completes all nine steps in order,',
    "Marking note rewritten for the reader and tied to the rubric.", "assessment")
fix(L, 'Scored holistically against the capstone\'s rubric, not step-by-step.</p>', '</p>',
    "Replaced by the explicit scoring method in the rubric section.", "assessment")
