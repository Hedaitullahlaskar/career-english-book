# Level 2 · Module 7 · Basic Customer Interaction
PH = "The answer key contained an unfilled template placeholder ('[open response following: …]'); replaced with a sample answer and what to check."

# ---------- 7.1 Greeting and Welcoming a Customer ----------
L = "CE-L02-M07-L01"
fix(L, '<p>Suggested answer: [open response following PAT-0039 for each of the three channels]</p>',
    '<p>Sample (a pharmacy). In person: "Welcome! Thanks for coming in — how can I help you today?" Phone: "Good morning, Green Leaf Pharmacy, this is Nadia speaking. Thanks for calling — how can I help you today?" Chat: "Hi, thanks for reaching out! How can I help you today?" Check: each greeting matches its channel.</p>',
    PH, "production")

# ---------- 7.2 Answering Simple Customer Questions Clearly ----------
L = "CE-L02-M07-L02"
fix(L, 'reversed direction from Level 1 Module 4, Lesson 4, where the learner clarified a colleague\'s request',
    'the reverse of Level 1 Lesson 4.4, where Arif asked a colleague to clarify a request',
    "Reader-facing text referred to 'the learner'; lesson reference made consistent.", "production")
fix(L, 'there, the learner asked a\n colleague to clarify', 'there, Arif asked a colleague to clarify',
    "Reader-facing text referred to 'the learner'.", "production")
fix(L, '<p>Suggested answer: [open response following PAT-0040]</p>',
    '<p>Sample (a bank): "Your account has a minimum balance requirement — in other words, as long as you keep at least 5,000 taka in the account, there\'s no monthly fee. Does that answer your question?" Check: no unexplained internal terms, a plain restatement, an understanding check.</p>',
    PH, "production")

# ---------- 7.3 "I Don't Know" — But I'll Find Out ----------
L = "CE-L02-M07-L03"
fix(L, "he's only worked the front desk since spring.", "he hasn't yet worked a winter at this hotel.",
    "'Since spring' implied months on the job, while Level 2 is set a few weeks after his first day; the new wording keeps the point without fixing a date.",
    "continuity")
fix(L, '<p>Suggested answer: [open response following PAT-0041]</p>',
    '<p>Sample (IT support): "That\'s a good question — I\'m not sure whether the new software works on older laptops. Let me check with the vendor and get back to you by tomorrow morning." Check: an honest admission, no guess, a concrete next step with a time.</p>',
    PH, "production")

# ---------- 7.4 Handling a Simple Complaint ----------
L = "CE-L02-M07-L04"
fix(L, '<p>Suggested answer: [open response following PAT-0042]</p>',
    '<p>Sample (a restaurant): "I understand your concern — your soup should have arrived hot. I appreciate you bringing this to my attention. Let me get you a fresh bowl right away." Check: no explanation or excuse before the acknowledgment; a concrete offer.</p>',
    PH, "production")

# ---------- 7.5 Closing a Customer Interaction Well ----------
L = "CE-L02-M07-L05"
fix(L, "This module's continuity character, Arif, handles one guest from greeting to close:", "In the dialogue, Arif handles one guest from greeting to close:",
    "Production language ('continuity character').", "production")
fix(L, 'What are the three parts of CF-0008, and why does each one matter?', 'What are the four parts of CF-0008, and why does each one matter?',
    "CF-0008 has four parts (confirm, check for anything else, thank, warm final line).", "answer-key")
fix(L, 'Suggested answer: [open response chaining PAT-0039 -&gt; PAT-0040 -&gt; PAT-0041 -&gt; PAT-0042 -&gt; CF-0008, graded holistically like the Level 1 capstone] What to listen/look for:',
    'Use the Listen &amp; Read dialogue as the model. Score 0–5, one point for each step shown:',
    "The key contained a template placeholder and referred to a holistic grading scheme without a scale; it now has a 5-point scale.",
    "assessment")
fix(L, 'Closes the interaction using CF-0008 (confirm, check for anything else, thank, warm line).</p>',
    'Closes the interaction using CF-0008 (confirm, check for anything else, thank, warm line). 5 = task complete; 4 = complete, practise the missed step; 3 or fewer = review the lessons for the missed steps.</p>',
    "Scale added for the module assessment.", "assessment")
