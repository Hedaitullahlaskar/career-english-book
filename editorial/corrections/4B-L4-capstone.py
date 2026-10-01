# Level 4 · Capstone · The Difficult Quarter
L = "CE-L04-CAPSTONE"
D = 16
HOW_TO_SCORE = ("<p><strong>How to score it:</strong> give each row a mark from 0 to 4 (0 = not shown, 1 = rarely, 2 = sometimes, 3 = mostly, 4 = consistently). "
                "Multiply by the row's weight and divide by 4 — for example, 3 for Composure gives 20 × 3 ÷ 4 = 15 points. Add the rows for a total out of 100. "
                "<strong>70 or more:</strong> Level 4 complete. <strong>Below 70:</strong> repeat the steps that use the modules behind your lowest rows, then perform the whole quarter again.</p>\n"
                "<p>Score the whole performance, not each step separately.")
REL = ("The Meridian relationship began with the Level 3 conference about a year before Module 8, so it is not 'three years' old; "
       "the three years in Lesson 8.5 are the extended agreement still ahead.")

fix(L, "given four years of steady, growing volume with you,", "given a year of steady, growing volume with you,",
    "The linen contract was first negotiated a year ago in Module 1 (Lesson 8.2 says that negotiation 'started from zero'), so there cannot be four years of volume.", "continuity")
fix(L, "Arif, good to hear from you. I'll be straightforward", "Arif, thanks for taking my call. I'll be straightforward",
    "Mr. Mostafa is the one calling, so 'good to hear from you' does not fit.", "language")
fix(L, "In the six weeks since the renewal call,", "In the two weeks since the renewal call,",
    "The renewal call is in Week 2 and this conversation is in Week 4.", "continuity")
fix(L, "a persuasion campaign for the kiosk rollout,", "preparing the early online check-in request,",
    "The kiosk rollout is long finished (Step 3); the current project is early online check-in.", "continuity")
SICK = ("Colleagues cannot 'call in sick' in Week 8 for a weekend two weeks later (Week 10); the absence is now planned medical leave.")
fix(L, "Two front-desk colleagues call in sick on the same morning Arif and Hasan learn that the",
    "Two front-desk colleagues will be on medical leave over the Week 10 weekend, and on the same morning Arif and Hasan learn that the", SICK, "continuity")
fix(L, "learns two front-desk colleagues are out sick the same weekend", "learns two front-desk colleagues will be on medical leave the same weekend", SICK, "continuity")
fix(L, "two of us are out this weekend,", "two of us are out that weekend,", SICK, "continuity")
STAGGER = ("The decision said the wedding check-in would be moved, but also that the 'small window shift' was Meridian's; the stagger is now described the same way everywhere: wedding party first, Meridian 45 minutes later.")
fix(L, "stagger the wedding party by forty-five minutes instead of ninety,", "stagger the two check-ins by forty-five minutes instead of ninety,", STAGGER, "continuity")
fix(L, "we've decided to stagger the wedding check-in by forty-five minutes", "we've decided to stagger the two check-ins by forty-five minutes, wedding party first,", STAGGER, "continuity")
fix(L, "a forty-five-minute stagger on the wedding check-in", "a forty-five-minute stagger between the two check-ins", STAGGER, "continuity")
fix(L, "housekeeping swap with your supervisor before end of day?", "housekeeping swap with the housekeeping supervisor before end of day?",
    "Hasan works in Front Office; the swap must be agreed with the housekeeping supervisor.", "continuity")
fix(L, "built under pressure in the last two days,", "built under pressure in a single morning last week,",
    "Step 4 (the plan) is in Week 8 and this presentation is in Week 9.", "continuity")
fix(L, "Confirmed commitments from both coordinators and housekeeping is exactly", "Confirmed commitments from both coordinators and housekeeping are exactly",
    "Subject–verb agreement ('commitments … are').", "grammar")
fix(L, "All four affected guests have been moved", "All four affected bookings have been moved", "The four rooms hold more than four guests.", "factual")
fix(L, "Resolved as of 11:15 AM.", "Resolved as of 10:55 AM.",
    "The first update promised the next one 'by 11:00 AM'; sending it at 11:15 broke the promise that Module 6 teaches.", "continuity")
fix(L, "and all four guests are comfortably settled", "and the guests from all four rooms are comfortably settled", "The four rooms hold more than four guests.", "factual")
fix(L, "Hasan is frustrated, and mutters something", "Hasan was frustrated, and now he says something", "Tense mismatch in the setting paragraph.", "grammar")
fix(L, "define a three-year relationship.", "define the relationship.", REL, "continuity")
fix(L, "Honestly, three years in, one rough morning", "Honestly, after everything we've done together, one rough morning", REL, "continuity")
fix(L, "three years with Meridian is something we genuinely value,", "our partnership with Meridian is something we genuinely value,", REL, "continuity")
fix(L, "the client relationship's three years)", "the client relationship's history)", REL, "continuity")
fix(L, "a full review credit on those two rooms", "a full credit for those two rooms", "'Review credit' is not a recognised term; a credit for the two rooms is meant.", "language")
fix(L, "against a holistic, high-stakes workplace communication rubric", "against a weighted, high-stakes workplace communication rubric",
    "The rubric now has an explicit scale.", "assessment")
fix(L, "It deliberately reuses the same higher-stakes rubric the standalone Level 4 Assessment used -- so nothing about how you're scored is new on the day that matters most.",
    "It uses the same weighted 0–4 format as the Level 1–3 capstones, with rows adapted to Level 4; every row applies, because the capstone is one continuous spoken performance.",
    "The Level 4 Assessment now scores spoken and written parts with criteria that fit each, so it no longer uses this rubric.", "assessment")
fix(L, "<p><strong>How to use it:</strong> this is graded holistically, not step by step.", HOW_TO_SCORE,
    "The rubric gave weights but no scale, no method for combining them, and no completion threshold.", "assessment")
fix(L, "A learner who handles Step 6's", "Someone who handles Step 6's", "Meta wording ('a learner').", "production")
fix(L, "Scored holistically against the capstone's rubric, not step by step.", "Score it with the self-assessment rubric above.",
    "Tied the key to the rubric's explicit scoring method.", "assessment")
