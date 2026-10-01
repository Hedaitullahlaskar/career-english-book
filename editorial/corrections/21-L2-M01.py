# Level 2 · Module 1 · Daily Work Updates

# ---------- 1.1 Giving a Clear Status Update ----------
L = "CE-L02-M01-L01"
fix(L, "I've wrapped up the morning checklist. I'm about halfway through the recount now -- that part's on track.",
    "I've wrapped up the morning checklist and submitted the maintenance request for the ice machine. I'm about halfway through the recount now — that part's on track.",
    "Arif added a 'done' item after Ms. Noor had already closed the exchange, contradicting the one-pass update the lesson models; the item now sits in the Done part.",
    "language")
fix(L, '<div class="dialogue-turn"><span class="dialogue-speaker">Arif:</span> <span class="dialogue-text">I\'ve also submitted the maintenance request for the ice machine, so that\'s pending on their side now.</span></div>\n',
    '', "Moved into Arif's main update (see previous correction).", "language")
fix(L, 'Bengali/Hindi often uses one simple past-tense-like form for both ideas, which is why English learners sometimes say "I finished" when "I\'ve finished" fits the moment better here: the finished task still matters to what happens next, which is exactly what the present perfect signals.',
    'Bengali and Hindi speakers often use a simple past form where English prefers the present perfect, so they say "I finished the checklist" when "I\'ve finished the checklist" fits a status update better: the finished task still matters to what happens next, which is exactly what the present perfect signals. ("I just finished…" is also common, especially in American English.)',
    "The original said the L1s use 'one form for both ideas' without saying which ideas; the contrast is now stated precisely, with the American English note.",
    "grammar", source="Cambridge Grammar of English, present perfect (current relevance); BrE/AmE usage")

# ---------- 1.2 Reporting Problems and Delays ----------
L = "CE-L02-M01-L02"
fix(L, '<p>Suggested answer: [open response following: what happened + brief cause + what you\'re doing + revised time]</p>',
    '<p>Sample: "The pool towels won\'t be ready by noon — the laundry machine broke down this morning. I\'ve arranged extra towels from the spa, and I\'ll have the pool area stocked by 1 PM." Check: what happened → brief cause → what you are doing → a specific new time.</p>',
    "The answer key contained an unfilled template placeholder in square brackets.", "production")

# ---------- 1.3 Matching Update Detail to Your Audience ----------
L = "CE-L02-M01-L03"
fix(L, 'Same finished task, same finished person answering.', 'Same finished task, same person answering.',
    "'Same finished person' is a copying slip.", "language")
fix(L, '<h2>Industry Overlays</h2>\n<p>None for this lesson -- the audience-calibration judgment is deliberately universal across industries, not shown through varied examples.</p>\n',
    '', "An empty section explaining why it was empty (production language).", "production")

# ---------- 1.4 The Standup Habit ----------
L = "CE-L02-M01-L04"
fix(L, 'Ms. Noor, Hasan, Priyanka, and Arif each get thirty seconds to say what\'s done, what\'s in progress, and what\'s blocked. Then, because Priyanka is running late for the actual morning briefing, Arif types the same update into the team chat so she doesn\'t miss it.',
    'Ms. Noor runs the round, and Hasan, Priyanka and Arif each get thirty seconds to say what\'s done, what\'s in progress, and what\'s blocked. Then, because the evening-shift staff weren\'t there, Arif types the same update into the team chat so they don\'t miss it.',
    "Priyanka takes part in the standup in the dialogue, so she cannot be the person who missed it; Ms. Noor runs the round rather than giving an update.",
    "continuity")
