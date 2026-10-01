# Level 2 · Module 8 · Workplace Etiquette
PH = "The answer key contained an unfilled template placeholder ('[open response …]'); replaced with a sample answer and what to check."

# ---------- 8.1 Punctuality and Time Norms ----------
L = "CE-L02-M08-L01"
fix(L, "there's a delay on my train.", "my bus is stuck in traffic.",
    "The lesson opening says Arif's bus is stuck in traffic, but his message blamed a train.", "continuity", count=2)
fix(L, "<p>Suggested answer: Sorry, I'm running a few minutes behind -- I'll be there shortly, around ten minutes late. Thanks for your patience.</p>",
    "<p>Sample: \"Sorry, I'm running about ten minutes behind — the traffic is heavy. I'll be there around 2:10. Thanks for your patience.\"</p>",
    "'Running a few minutes behind … around ten minutes late' contradicted itself and repeated 'late'.", "language")
fix(L, '<p>Suggested answer: [open response following PAT-0043]</p>',
    '<p>Sample: "Sorry, I\'m running about fifteen minutes behind — my train is delayed. I\'ll be there around 9:15; please start without me." Check: a brief apology, the reason in a few words, a specific time if you know it.</p>',
    PH, "production")

# ---------- 8.2 Digital Etiquette and Confidentiality ----------
L = "CE-L02-M08-L02"
fix(L, '<p>Suggested answer: Draft schedule = confidential; org change rumor = need-to-know; forwarded screenshot = unclear, so treat as need-to-know until confirmed</p>',
    '<p>(1) A client\'s private contact details — confidential: don\'t forward them, even "just this once". (2) An unannounced organisational change — need-to-know until it is officially announced. (3) A screenshot of a private message — treat it as need-to-know and don\'t share it until the person who wrote it confirms you can.</p>',
    "The key labelled the three Listen & Read scenes, not the three scenario cards the exercise refers to (the first card is about a client's contact details).",
    "answer-key")
fix(L, '<p>Suggested answer: [open response following PAT-0044]</p>',
    '<p>Sample: "This guest list for the minister\'s visit is confidential — the visit hasn\'t been announced. Please don\'t forward it without permission." Check: marks it as confidential, gives the reason or scope briefly, sets the sharing boundary.</p>',
    PH, "production")

# ---------- 8.3 Hierarchy, Titles, and Respectful Address ----------
L = "CE-L02-M08-L03"
fix(L, "from this morning -- I'll CC Ms. Noor so she's kept in the loop. Happy to discuss",
    "from this morning — I've copied in Ms. Noor so she's kept in the loop. Happy to discuss",
    "Inside an email that already copies Ms. Noor, 'I'll CC her' is the wrong tense; the email itself should say she has been copied in.", "language")
fix(L, "-- I'll CC Ms. Noor so she's kept in the loop.\"</li>", "— I've copied in Ms. Noor so she's kept in the loop.\"</li>",
    "Same correction in the summary of the three exchanges.", "language")
fix(L, '<p>Suggested answer: [open response following PAT-0045 for each of the three relationships]</p>',
    '<p>Sample. Peer (chat): "Hey Rina, quick question — is the printer on two working?" Supervisor (phone): "Good morning, Mr. Islam, this is Nadia — could I ask you something when you have a moment?" Senior colleague (email): "Dear Dr. Haque, I hope you\'re well. I wanted to ask about the training schedule for next month…" Check: title + surname for the senior and less familiar people, first name for the peer.</p>',
    PH, "production")

# ---------- 8.4 Putting It All Together: A Full Workday ----------
L = "CE-L02-M08-L04"
fix(L, '1:00 PM. Arif realizes he sent a guest the wrong invoice, and Priyanka catches it before it went out (Modules 5 and part of the apology/thanks skill set).',
    '1:00 PM. Priyanka spots that Arif attached the wrong invoice to a guest email this morning. Arif owns the mistake, then thanks her (Module 5).',
    "The setting said Priyanka caught the invoice 'before it went out', while the dialogue says it had been sent and corrected.", "continuity")
fix(L, "I actually attached the wrong invoice to that guest email earlier -- my mistake. I've sent the corrected one now, and I'll double-check attachments before sending from now on.",
    "You're right — I attached the wrong invoice to that guest email this morning. That's on me. I've sent the corrected one now, and I'll double-check attachments before sending from now on.",
    "Aligned with the corrected setting (Priyanka found the mistake).", "continuity")
fix(L, 'No worries, thanks for catching it and fixing it.', 'No worries — thanks for fixing it so fast.',
    "Priyanka was thanking Arif for 'catching' a mistake she caught herself.", "continuity")
fix(L, 'Actually, thank you for flagging it before it went further -- I really appreciate you catching that.',
    'And thank you for flagging it before it went any further — I really appreciate it.', "Aligned with the corrected setting.", "continuity")
fix(L, 'approaches the desk with a question and a mild complaint (Module 7).', 'approaches the desk with a mild complaint (Module 7).',
    "The guest raises only a complaint; there is no question.", "continuity")
fix(L, "Hi -- also, my room wasn't cleaned before I checked in this morning.", "Hi — my room wasn't cleaned before I checked in this morning.",
    "'Also' implied an earlier question that is not in the scene.", "continuity")
fix(L, '<span class="dialogue-text">I\'m glad we could sort that out. Is there anything else I can help you with? Thanks for stopping by -- have a great stay!</span>',
    '<span class="dialogue-text">(A few minutes later) Housekeeping has finished your room. I\'m glad we could sort that out. Is there anything else I can help you with? Thanks for stopping by — have a great stay!</span>',
    "Arif declared the problem sorted in the same breath as promising to look into it; the resolution now happens.", "continuity")
fix(L, "One guest had a room-readiness issue this morning, but it's been resolved.", "One guest had a room-readiness issue this afternoon, but it's been resolved.",
    "The guest raised the issue at 2:30 PM.", "continuity")
fix(L, '(Module 8, this module)', '(Module 8)', "Redundant wording.", "language")
rule("L2-8.4-duplicate-summary", r"<h2>A Full Simulated Workday</h2>\s*<p>.*?</p>\s*", "",
     "This section only described the dialogue again and told the reader to see the dialogue both 'below' and 'above'.",
     "structure", fields=("body_html",), flags=16, targets=[L], expect=1)
fix(L, '<p>Suggested answer: [open response chaining multiple Level 2 skills into one connected simulated workday, graded holistically -- the same style as the Level 1 capstone and the Module 7 assessment]</p>',
    '<p>Use the Listen &amp; Read workday as the model. Score each communication moment 0–2: 1 point for using the right skill for the moment (update, request, call, chat, apology/thanks, customer, hierarchy), 1 point for a clean switch into it without mixing it with the previous moment. Five moments = 10 points. 8–10: Module 8 complete; 6–7: complete, practise the lowest-scoring moment; 5 or fewer: review the modules behind the weakest moments.</p>',
    "The key was a template placeholder pointing to an unspecified 'holistic' grading; it now has a scale.", "assessment")
fix(L, '<p>Suggested answer: [open, reflective response]</p>',
    '<p>Answers will vary — this is a personal reflection. A useful answer names three specific skills (for example, "declining a request", "following up a second time", "addressing the General Manager") and gives a concrete reason for each, such as a situation where it went wrong.</p>',
    PH, "production")
