# Level 3 · Capstone · The Client Review
L = "CE-L03-CAPSTONE"
HOW_TO_SCORE = ("<p><strong>How to score it:</strong> give each row a mark from 0 to 4 (0 = not shown, 1 = rarely, 2 = sometimes, 3 = mostly, 4 = consistently). "
                "Multiply by the row's weight and divide by 4 — for example, 3 for Clarity gives 15 × 3 ÷ 4 ≈ 11 points. Add the rows for a total out of 100. "
                "<strong>70 or more:</strong> Level 3 complete. <strong>Below 70:</strong> repeat the steps that use the modules behind your lowest rows, then perform the whole week again.</p>\n"
                "<p>Score the whole performance, not each step separately.")
WHO = ("In Step 6 it is Arif, not Hasan, who tells Ms. Cruz the price, and the proposal goes out after the 11:00 meeting; "
       "the setup fee was already waived with the client, so the draft cannot call it undecided. Only the facts are changed — every planted grammar error stays, so the explanation that follows still matches.")

fix(L, "<strong>Action:</strong> Confirm the reconfigured layout and the livestream add-on with Ms. Cruz at Friday's\nreview call, and lock in the catering order for 72 covers once she confirms.",
    "<strong>Action:</strong> I have placed a provisional hold on the Garden Suite's theatre layout for all three days and asked the AV team to hold a camera operator.",
    "In Module 2's framework, Action is what has already been done; the report listed future steps there (they belong in the Recommendation).",
    "factual")
fix(L, "and I'll pull everything into a short report and presentation for Wednesday afternoon.",
    "and I'll present the report to the team this afternoon.",
    "The report was already written on Tuesday (Step 2).", "continuity")
rule("L3-cap-who-told-client", r"I told Ms\. Cruz the price", "Arif told Ms. Cruz the price", WHO, "continuity",
     fields=("body_html",), targets=[L], expect=2)
rule("L3-cap-proposal-time", r"(The quote (?:was )?sent to her by email )this morning", r"\1this afternoon", WHO, "continuity",
     fields=("body_html",), targets=[L], expect=2)
fix(L, "The message confirmed the quote, but the setup fee, whether it's waived or not, still\nisn't decided of.",
    "The message confirmed the quote, but the camera position for the livestream still isn't decided of.", WHO, "continuity")
fix(L, "that confirmed the quote, but the setup fee, whether it is waived or not, still is\nnot decided on.",
    "that confirmed the quote, but the camera position for the livestream has still not been decided on.", WHO, "continuity")
fix(L, '<span class="dialogue-text">Mr. Chowdhury, your room is ready now,', '<span class="dialogue-text">(Fifteen minutes later) Mr. Chowdhury, your room is ready now,',
    "The time jump was not marked, so Arif seemed to announce the room was ready seconds after promising fifteen minutes.", "continuity")
fix(L, "It's the same rubric\nLevel 3's own standalone assessment uses -- the capstone deliberately reuses it, so nothing about\nthe scoring format is new on the week that matters most.",
    "It is the same rubric as the Level 1 and Level 2 capstones; every row applies, because the capstone combines written documents with one continuous spoken role-play.",
    "The Level 3 Assessment now scores written and spoken items with criteria that fit each, so it no longer uses this rubric.", "assessment")
fix(L, "<p><strong>How to use it:</strong> this is graded holistically, not step-by-step.", HOW_TO_SCORE,
    "The rubric gave weights but no scale, no method for combining them, and no completion threshold.", "assessment",
    source="QA review of the reference PDF (assessments)")
fix(L, "A learner who handles Step 5's", "Someone who handles Step 5's", "Meta wording ('a learner').", "production")
fix(L, "Do not copy the wording from capstone.md;", "Do not copy the wording from this page;",
    "A source file name ('capstone.md') was printed in the exercise.", "production")
fix(L, "Scored holistically against the capstone's rubric, not step-by-step.</p>", "Score it with the self-assessment rubric above.</p>",
    "Tied the key to the rubric's explicit scoring method.", "assessment")
