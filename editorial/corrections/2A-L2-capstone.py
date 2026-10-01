# Level 2 · Capstone
L = "CE-L02-CAPSTONE"
HOW_TO_SCORE = ("<p><strong>How to score it:</strong> give each row a mark from 0 to 4 (0 = not shown, 1 = rarely, 2 = sometimes, 3 = mostly, 4 = consistently). "
                "Multiply by the row's weight and divide by 4 — for example, 3 for Clarity gives 15 × 3 ÷ 4 ≈ 11 points. Add the rows for a total out of 100. "
                "<strong>70 or more:</strong> Level {n} complete. <strong>Below 70:</strong> repeat the steps that use the modules behind your lowest rows, then perform the whole {unit} again.</p>\n"
                "<p>Score the whole performance, not each step separately.")

fix(L, "the front desk's second keycard encoder finally arrived this morning after a couple of follow-ups",
    "the front desk's second keycard encoder finally arrived yesterday after a couple of follow-ups",
    "Engineering confirmed on Thursday that the encoder would arrive by 11 AM that day (Step 6), and the exercise key says it has run 'since Thursday'; on Friday it cannot have arrived 'this morning'.",
    "continuity")
fix(L, 'eight situations, six different people, at least\nfour registers (peer, supervisor, external caller, guest, General Manager)',
    'eight situations, seven different people and teams, five registers (peer, supervisor, external caller, guest, General Manager)',
    "The counts did not match the scenes: seven speakers/teams appear (Ms. Noor, Hasan, Golam, Priyanka, Engineering, a guest, Dr. Rahman) and five registers are listed.",
    "continuity")
fix(L, "It's the same rubric Level 1's\ncapstone and Level 2's own Assessment use -- reused deliberately, so nothing about the scoring\nformat is new on the week that matters most.",
    "It is the same rubric as the Level 1 capstone. Every row applies here, because the capstone is one continuous spoken role-play.",
    "The Level 2 Assessment now scores speaking and writing with criteria that fit each part, so it no longer uses this rubric.", "assessment")
fix(L, "<p><strong>How to use it:</strong> this is graded holistically, not step-by-step.",
    HOW_TO_SCORE.format(n=2, unit="week"),
    "The rubric gave weights but no scale, no method for combining them, and no completion threshold.", "assessment",
    source="QA review of the reference PDF (assessments)")
fix(L, "A learner who handles Step 6's", "Someone who handles Step 6's", "Meta wording ('a learner') in reader-facing guidance.", "production")
fix(L, "Scored holistically against the capstone's rubric, not step-by-step.</p>", "Score it with the self-assessment rubric above.</p>",
    "Tied the key to the rubric's explicit scoring method.", "assessment")
