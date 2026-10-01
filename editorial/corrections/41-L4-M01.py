# Level 4 · Module 1 · Negotiation
# (The vendor's rename, Mr. Kabir Hossain -> Mr. Tariq Mostafa, is applied in 89-names.py.)

fix("CE-L04-M01-L02", "(recycled from L2-M2-L03)", "(recycled from Level 2, Lesson 2.3)", "Internal lesson code replaced.", "reference")

fix("CE-L04-M01-L03", "down to 8%, still above\nArif's walk-away point,", "down to 8% (right at the limit of Arif's walk-away point),",
    "Arif's walk-away point is 'no more than an 8% increase', so 8% is exactly at the limit, not above it.", "factual")

L = "CE-L04-M01-L05"
for old, new in [('Suggested answer: L2: "', 'Suggested answer: Lesson 1.2: "'), (' L3: "If', ' Lesson 1.3: "If'),
                 (' L4: "I understand', ' Lesson 1.4: "I understand'), (' L5: "So, to confirm', ' Lesson 1.5: "So, to confirm')]:
    fix(L, old, new, "Internal lesson codes replaced.", "reference")
fix(L, "from your role-play in A02,", "from your role-play in Exercise 2,", "Internal activity code ('A02').", "production")
fix(L, "Suggested answer: Subject: Confirming Agreed Terms -- [Negotiation Topic]. To confirm our conversation today, we've agreed on [specific term one] and [specific term two], effective from [date/timeframe]. Please confirm this matches your understanding, and let me know if we can proceed to [next step] by [date].",
    "Sample: \"Subject: Confirming Agreed Terms — Staff Uniform Supply 2027 / Dear Ms. Rahim, To confirm our conversation today, we've agreed on a unit price of 1,450 taka per uniform set, fixed for twelve months, with delivery within ten working days of each order. Please confirm this matches your understanding, and let me know if the contract can be ready for signature by Friday 14 May. Best regards, Arif\"",
    "The model answer was a template full of unfilled placeholders ('[specific term one]', '[date]').", "production")
fix(L, '<span class="answer-number">2.</span> <p>What to listen/look for:',
    '<span class="answer-number">2.</span> <p>Score 0–5, one point for each stage done well (preparation shows; an anchor with room to move; a traded concession; composure or a deadlock-breaking question under pressure; a precise close). Pass at 4. What to listen/look for:',
    "The module assessment had criteria but no scale.", "assessment")
