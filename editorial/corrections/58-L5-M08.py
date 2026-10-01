# Level 5 · Module 8 · Building a Personal Leadership Voice
D = 16
PH = "The answer key contained an unfilled placeholder ('[open, reflective response]'); replaced with a sample answer."
M8 = ["CE-L05-M08-L01", "CE-L05-M08-L02", "CE-L05-M08-L03", "CE-L05-M08-L04"]

rule("L5-M8-lesson-codes", r"\bL0([1-4])('s)?\b", r"Lesson \1\2", "Internal lesson codes ('L01') replaced with the book's lesson numbers.",
     "reference", fields=("body_html", "practice_html"), targets=M8)

L = "CE-L05-M08-L01"
fix(L, "thinking back over a few moments from across the course -- his own material for this lesson's reflection.</em></div>\n</div>",
    "thinking back over a few moments from across the course -- his own material for this lesson's reflection.</em></div>\n</div>\n"
    "<blockquote>\n<p><strong>Arif's notes</strong><br>\n"
    "- First day: I'd rehearsed my introduction so many times that it came out stiff. That wasn't me.<br>\n"
    "- The VIP folders with Rima: I said exactly what I needed and checked she had everything. That was me.<br>\n"
    "- The New Year's staffing meeting: I named both sides, then made the call plainly. Also me.</p>\n</blockquote>",
    "The Listen & Read box introduced Arif's reflection but contained nothing; his notes on the three moments are now shown.", "structure")
fix(L, "Compare these two self-descriptions. Which one sounds",
    "Compare these two self-descriptions: (1) \"I'd say I'm an empowering, visionary communicator who inspires excellence in others.\" (2) \"My instinct is to check in with people before I hand something off, not after.\" Which one sounds",
    "The exercise asked the reader to compare two self-descriptions that were not printed.", "answer-key")
fix(L, "Suggested answer: [open, reflective response naming a real, specific, repeated tendency]",
    "Sample: \"Whether I'm handling a complaint or training someone new, I always repeat the key point back before we finish — 'So the plan is…'. I did it with an angry guest last month and with a new colleague on her first day.\"",
    PH, "production")
fix(L, "states the tendency in the learner's own words", "states the tendency in your own words", "Meta wording ('the learner').", "production")

L = "CE-L05-M08-L02"
rule("L5-8.2-duplicate-scenes",
     r"<h2>Contrastive Scenario: The Same Moment, Two Ways</h2>\s*<p><strong>Scene A.*?</blockquote>\s*<p><strong>Scene B.*?</blockquote>\s*",
     "",
     "Both scenes were printed a second time, word for word, straight after the dialogue; the repeat is removed and its closing comment kept.",
     "structure", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "Suggested answer: [open, reflective response]",
    "Sample: \"When our booking system crashed, a new manager told us to 'stay aligned and solution-focused'. Nobody moved. Then a senior receptionist said, 'Paper check-in — I'll take the queue, you two call the arrivals.' Everyone knew what to do.\"",
    PH, "production")

L = "CE-L05-M08-L03"
fix(L, "\"I wanted to let you know that I'm extending the front-desk shift handover from next Monday,",
    "\"Hi Ms. Noor, I wanted to let you know that I'm extending the front-desk shift handover from next Monday,",
    "The email had no greeting or sign-off, unlike every other email in the course.", "language")
fix(L, "Happy to discuss if you'd like more detail.\"", "Happy to discuss if you'd like more detail. Best regards, Arif\"",
    "The email had no greeting or sign-off, unlike every other email in the course.", "language")
fix(L, "the same update you wrote in A03,", "the same update you wrote in Exercise 3,", "Internal activity code ('A03').", "production")

L = "CE-L05-M08-L04"
fix(L, "with Farhan missing exactly this kind of\nthing.", "with Farhan letting problems sit too long before raising them.",
    "Farhan's development area in Module 2 was escalating problems sooner, not missing billing errors.", "continuity")
fix(L, "full week as a leader, scored holistically.</strong>", "full week as a leader.</strong>", "'Scored holistically' gave no scale; a scale is now given.", "assessment")
fix(L, "it is the direct rehearsal for it,",
    "it is the direct rehearsal for it (score 0–6, one point for each moment that uses its module's tool in your own voice; pass at 4, with no moment slipping into a performed 'leadership persona'),",
    "The module assessment had no scale.", "assessment")
fix(L, "Suggested answer: [open, reflective response connecting back to specific earlier Level 5 modules]",
    "Sample: \"Coaching (Module 3) is hardest for me. When I'm busy, I want to give the answer, and my questions start to sound like hints. My own voice is more direct, so I'm practising one genuinely open question before I say anything else.\"",
    PH, "production")
fix(L, "Suggested answer: 'Delegating:... Feedback:... Coaching:... Change:... Meeting:... Closing update:...'",
    "Sample. Delegating: I'd give Nadia the monthly guest-feedback report to own, start to finish. Feedback: I'd tell Sam that his calm call with the angry guest on Tuesday was exactly right. Coaching: when Rana asks how to handle a group late checkout, I'd ask what the group actually needs. Change: I'd explain that the breakfast cut-off is moving to 10:00 because the kitchen needs the time for events. Meeting: when two colleagues disagree about Eid cover, I'd hear both sides and decide. Closing: I'd tell my manager plainly what went well and what I'd decided.",
    PH, "production")
fix(L, "scored holistically as the direct rehearsal for the Level 5 capstone,", "score 0–6 as described in the Module 8 Assessment (pass at 4); this is the direct rehearsal for the Level 5 capstone,",
    "The module assessment had no scale.", "assessment")
