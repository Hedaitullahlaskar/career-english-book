# Level 5 · Module 4 · Strategic & Change Communication
PH = "The answer key gave an unfilled template ('[reason]', '...'); replaced with a sample answer."
N2 = '<span class="answer-number">2.</span> <p>'
N3 = '<span class="answer-number">3.</span> <p>'

L = "CE-L05-M04-L01"
fix(L, "Suggested answer: The reasoning behind this is [reason]. This connects directly to [something the audience cares about]. What this means for our team is [concrete implication].",
    "Sample: \"We're switching booking systems next month. The reasoning behind this is the double-booking issues we've had this quarter. This connects directly to the extra time you've all spent fixing those conflicts at the desk. What this means for our team is fewer conflicts and less firefighting at check-in.\"",
    PH, "production")
fix(L, "Suggested answer: The reasoning behind this is... This connects directly to... What this means for our team is...",
    "Sample: \"Breakfast will now close at 10:00 instead of 10:30. The reasoning behind this is that the kitchen needs the extra half hour to prepare for lunch events. This connects directly to the late room-service orders you've been apologising for. What this means for our team is fewer delayed orders to explain to guests.\"",
    PH, "production")

L = "CE-L05-M04-L02"
fix(L, N2 + "Suggested answer: What's changing is... What's staying the same is... The reasoning behind this is... Here's what to expect next...",
    N2 + "Sample: \"What's changing is the software we use to manage bookings — we're moving to a new system next month. What's staying the same is our team, our shifts and how we look after guests. The reasoning behind this is the double-booking issues we've had this quarter. Here's what to expect next: training sessions next week, and the new system goes live on the 1st.\"",
    PH, "production")
fix(L, N3 + "Suggested answer: What's changing is... What's staying the same is... The reasoning behind this is... Here's what to expect next...",
    N3 + "Sample: \"What's changing is the shift-swap process: swaps now go through the scheduling app instead of the paper book. What's staying the same is the rota itself and who approves swaps. The reasoning behind this is that two swaps were lost last month. Here's what to expect next: a ten-minute demo on Monday, and the paper book stops on the 15th.\"",
    PH, "production")
fix(L, "Play Arif's part -- announce the booking-system change to the team from scratch, without looking at the dialogue, using a hotel, retail, or IT change scenario of your choice.",
    "Play Arif's part — announce the booking-system change to the team from scratch, without looking at the dialogue. (Or announce a retail or IT change of your choice in the same way.)",
    "The task asked for the booking-system change and 'a scenario of your choice' at the same time.", "answer-key")

L = "CE-L05-M04-L03"
fix(L, "what's worrying you specifically....This is genuinely hard", "what's worrying you specifically. … This is genuinely hard",
    "Missing space and an extra full stop between the two quoted parts.", "typography")
fix(L, N2 + "Suggested answer: I hear that this is a real concern. Let's talk through what's worrying you specifically.",
    N2 + "Sample: \"I hear that this is a real concern. Let's talk through what's worrying you specifically — is it the system itself, or the timing?\"",
    "The answer keys for Exercises 2 and 3 were identical and generic; each now has its own sample.", "answer-key")
fix(L, N3 + "Suggested answer: I hear that this is a real concern. Let's talk through what's worrying you specifically.",
    N3 + "Sample (objection: \"I just don't think the new rota is a good idea\"): \"I hear that this is a real concern. Let's talk through what's worrying you specifically.\" — \"It's the Friday nights; I'd lose my evening class.\" — \"That's useful to know. The new rota is still going ahead, because it covers the late arrivals, but let's see whether you can swap Fridays with Farhan.\"",
    "The answer keys for Exercises 2 and 3 were identical and generic; each now has its own sample.", "answer-key")

L = "CE-L05-M04-L04"
fix(L, "Arif sends a short written check-in to the whole front office team.</em></div>\n</div>",
    "Arif sends a short written check-in to the whole front office team.</em></div>\n</div>\n"
    "<blockquote>\n<p><strong>Subject:</strong> New booking system — three weeks in<br>\nHi all,<br>\n"
    "Just following up on the booking-system switch — we're three weeks in now. I'm checking in on how the transition is going for everyone. "
    "How is this landing so far? If anything isn't working the way we expected — even something small, like a report you can't find — reply here or come and find me.<br>\n"
    "Thanks,<br>\nArif</p>\n</blockquote>",
    "The Listen & Read box introduced Arif's written check-in, but the message itself was missing; the exercises depend on it.", "structure")
fix(L, "Rewrite this into a genuine check-in message following up on a change",
    "Write a genuine check-in message following up on a change",
    "There was nothing to rewrite; the task is to write a new message.", "answer-key")
fix(L, "Suggested answer: Checking in on how the transition is going for everyone. How is this landing so far?",
    "Sample: \"Hi all, just following up on the new uniform policy — we're three weeks in. Checking in on how the transition is going for everyone. How is this landing so far? Let me know if anything isn't working.\"",
    PH, "production")
fix(L, "Suggested answer: Checking in on how [the change] is going. How is this landing so far? Let me know if anything isn't working the way we expected.",
    "Sample: \"Hi team, checking in on how the new handover checklist is going now that we've used it for a month. How is this landing so far? Let me know if anything isn't working the way we expected — especially on night shifts.\"",
    PH, "production")

L = "CE-L05-M04-L05"
fix(L, "scenario, graded holistically.</strong>", "scenario.</strong>", "'Graded holistically' gave no scale; a scale is now given.", "assessment")
fix(L, "message some time after the announcement (Lesson 4).</p>",
    "message some time after the announcement (Lesson 4). Score 0–4, one point per stage done well; pass at 3, and the resistance conversation must be one of them.</p>",
    "The module assessment had no scale.", "assessment")
fix(L, "Suggested answer: [open reflection response]",
    "Sample: \"The alignment check is skipped most often. Once the announcement is made, managers move on to the next problem, and silence looks like success — until people drift back to the old way.\"",
    "The answer key contained an unfilled placeholder.", "production")
fix(L, "Suggested answer: Reasoning:... Announcement:... Resistance:... Alignment check:...",
    "Sample (moving to digital guest-feedback forms). Reasoning: I'd explain to Hasan that paper forms are lost and we can't see trends. Announcement: I'd tell the team what changes (tablets at checkout), what stays the same (we still ask every guest) and what happens next. Resistance: I'd ask anyone uneasy what worries them specifically. Alignment check: I'd message the team three weeks later to ask how it's landing.",
    PH, "production")
fix(L, "<p>What to listen/look for: All four moments are present",
    "<p>Score with the four stages in the Module 4 Assessment section (0–4; pass at 3). What to listen/look for: All four moments are present",
    "The module assessment had no scale.", "assessment")
