# Level 4 · Module 4 · Advanced Problem-Solving Communication

fix("CE-L04-M04-L01", "This lesson recycles L3-M2-L01's", "This lesson recycles Level 3 Lesson 2.1's", "Internal lesson code replaced.", "reference")

fix("CE-L04-M04-L02", "Module 3's persuasion work taught \"on one hand / on the other hand\" as a way to frame two sides of\nan argument you were making.",
    "\"On one hand / on the other hand\" is the classic way to set two sides of an argument against each other.",
    "The lesson said Module 3 had taught this phrase; it does not appear anywhere in Module 3.", "reference")

L = "CE-L04-M04-L03"
fix(L, "with one agency staff member for the 7:00-11:00\nAM check-in rush, plus Mina",
    "with one agency staff member for the two busiest check-in blocks, plus Mina",
    "The written note gave the agency cover as a single 7–11 AM block, but the spoken announcement and Lesson 4.2 say it covers the two busiest check-in blocks.",
    "continuity")
fix(L, "the decision you announced in A03,", "the decision you announced in Exercise 3,", "Internal activity code ('A03').", "production")

L = "CE-L04-M04-L04"
LOGIC = ("The reasoning contradicted itself: Arif said the plan tests the new backup vendor 'on a lower-stakes day first', then gave that untested vendor "
         "Thursday — the highest-risk day — and the trusted source the quieter day. The assignment is swapped so the stated reasoning holds.")
fix(L, "split it -- Riverside covers the smaller of the two days, and the backup vendor covers the day both the wedding and Crescent Trading are checking in the same morning.",
    "split it — the backup vendor covers the smaller of the two days, and Riverside covers the day both the wedding and Crescent Trading are checking in the same morning.",
    LOGIC, "continuity")
fix(L, "split it -- Riverside covers the\nsmaller day, and the backup vendor covers the day both the wedding and Crescent Trading check in\nthe same morning.",
    "split it — the backup vendor covers the smaller day, and Riverside covers the day both the wedding and Crescent Trading check in the same morning.",
    LOGIC, "continuity")
fix(L, "we've decided to split coverage: Riverside for Wednesday, the backup vendor for Thursday. The reasoning behind this is it protects Thursday, our highest-risk day, with a fresh vendor we're testing carefully, while keeping Wednesday's ask on Riverside small.",
    "we've decided to split coverage: the backup vendor for Wednesday, Riverside for Thursday. The reasoning behind this is it protects Thursday, our highest-risk day, with linens from a source we know, while we test the backup vendor on the smaller day.",
    LOGIC, "continuity", count=2)
fix(L, "We've decided to split it -- Riverside for the smaller day, backup for the bigger one -- because that protects our highest-risk day while testing the backup carefully.",
    "We've decided to split it — the backup vendor for the smaller day, Riverside for the bigger one — because that protects our highest-risk day with a source we know while we test the backup on a lower-stakes day.",
    LOGIC, "answer-key")
fix(L, "This is delivered as this lesson's role-play activity (see\nthe exercises below), and is the Module 4 assessment.",
    "It is Exercise 3 below; the scoring scale is in its answer key.",
    "Production language and no scoring scale.", "assessment")
fix(L, '<span class="answer-number">3.</span> <p>What to listen/look for: Within',
    '<span class="answer-number">3.</span> <p>Score 0–4, one point each: (1) the issues and the core question are named first; (2) at least two options, each with an honest trade-off; (3) a genuine check for blind spots; (4) a plainly stated decision with its reasoning and practical effect. Pass at 3. What to listen/look for: Within',
    "The module assessment had no scale.", "assessment")
