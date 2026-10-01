# Level 5 · Module 5 · Leading Meetings & Decisions
PH = "The answer key contained an unfilled placeholder ('[open response…]', '[decision]'); replaced with a sample answer."
N2 = '<span class="answer-number">2.</span> <p>'
N3 = '<span class="answer-number">3.</span> <p>'
FARHAN = ("Farhan is a front-office team member (Module 2), and he was in the meeting where the decision was made, so he cannot ask whether it is decided; "
          "the questions now come from an events colleague, and Farhan is the front office's link to the events team.")

L = "CE-L05-M05-L01"
fix(L, "That lines up with what events is telling me too.", "That lines up with what the events team is telling me too.",
    "Clarified that Farhan is relaying the events team's figures (he is a front-office team member).", "continuity")
fix(L, "Suggested answer: [open response following: ownership statement + concrete outcome + who decides]",
    "Sample: \"Thanks for coming. As the person leading this, here's what I need us to walk away with today: an agreed plan for covering the lobby renovation week. If we can't agree on the details by eleven, I'll make the final call.\"",
    PH, "production")

L = "CE-L05-M05-L02"
fix(L, "Here's the call I'm making: [decision and reasoning]. I recognize this isn't unanimous,",
    "Here's the call I'm making: we'll trial the new rota for two weeks, because it fixes the gap in Sunday cover, and we'll review it at the end. I recognize this isn't unanimous,",
    PH, "production")
fix(L, "Suggested answer: [open reflection response]",
    "Sample: \"Our team couldn't agree whether to close the gym early during the renovation. Nobody made a call; we said we'd 'look at it next week', and in the end the contractor decided for us. A clear decision, even an unpopular one, would have been better.\"",
    PH, "production")

L = "CE-L05-M05-L03"
fix(L, "plus Farhan's events\ncolleagues, still need to hear about it,", "plus the events team Farhan works with, still need to hear about it,", FARHAN, "continuity")
fix(L, '<span class="dialogue-speaker">Farhan:</span> <span class="dialogue-text">Wait -- so is this actually decided',
    '<span class="dialogue-speaker">Events colleague:</span> <span class="dialogue-text">Wait -- so is this actually decided', FARHAN, "continuity")
fix(L, '<span class="dialogue-speaker">Farhan:</span> <span class="dialogue-text">Got it, that\'s clear. I\'ll get my team\'s preferences to you by Friday.',
    '<span class="dialogue-speaker">Events colleague:</span> <span class="dialogue-text">Got it, that\'s clear. I\'ll get the events team\'s preferences to you by Friday.', FARHAN, "continuity")
fix(L, 'In Scene A, why does Farhan ask "so is this actually decided', 'In Scene A, why does the events colleague ask "so is this actually decided', FARHAN, "answer-key")
fix(L, "Because Farhan disagrees with the decision", "Because the events colleague disagrees with the decision", FARHAN, "answer-key")
fix(L, "Suggested answer: We've decided to [decision]. The reasoning behind this is [reasoning]. I know this wasn't everyone's first choice. Here's what I need from all of us now: [action].",
    "Sample: \"We've decided to change the weekend schedule to rotating shifts from next month. The reasoning behind this is that it shares the Sunday shifts fairly. I know this wasn't everyone's first choice. Here's what I need from all of us now: send me your preferred weekends by Thursday.\"",
    PH, "production")
fix(L, "Suggested answer: [open response using both target expressions]",
    "Sample: \"We've decided to move the monthly team meeting to Tuesday mornings. I know this wasn't everyone's first choice — Monday suited some of you better. Here's what I need from all of us now: update your calendars today, and the first Tuesday meeting is on the 9th.\"",
    PH, "production")

L = "CE-L05-M05-L04"
fix(L, "focus on countdown-\nhour coverage", "focus on countdown-hour coverage", "Stray line break inside a hyphenated word ('countdown- hour').", "typography")
fix(L, "In the interest of time, let's confirm [agenda item], and I'll take anything else offline by email.",
    "In the interest of time, let's confirm the countdown-hour coverage, and I'll take anything else offline by email.",
    PH, "production")
fix(L, "Suggested answer: [open response using both target expressions]",
    "Sample: \"Our training meeting last month turned into a debate about the staff canteen and ran forty minutes over. The chair could have said: 'That's a fair point about the canteen — let's park that for now. In the interest of time, let's finish the training dates, and I'll raise the canteen with HR.'\"",
    PH, "production")
fix(L, "<p>What to listen/look for: The tangent is acknowledged briefly",
    "<p>Score 0–3, one point each: the tangent is parked without being dismissed; the group is brought back to the agenda; the meeting ends on time with the rest taken offline. Pass at 2. What to listen/look for: The tangent is acknowledged briefly",
    "The speaking assessment had no scale.", "assessment")

L = "CE-L05-M05-L05"
fix(L, "we've decided to move the twelve affected loyalty bookings", "we've decided to move the affected loyalty bookings",
    "The VIP group needs twelve rooms; nothing says all twelve must come from loyalty bookings (Rima says 'some loyalty members').", "factual")
fix(L, "check-in opens in half an hour.", "check-in opens in twenty-five minutes.",
    "The meeting started forty minutes before check-in and was planned for fifteen minutes.", "continuity")
fix(L, "as they appear in the dialogue below.</li>", "as they appear in the dialogue above.</li>", "The dialogue is above the Self-Check.", "reference")
fix(L, "everyone clear on\nwhat happens next.</p>",
    "everyone clear on what happens next. Score 0–4, one point per skill shown clearly; pass at 3, and the decision under disagreement must be one of them.</p>",
    "The module assessment had no scale.", "assessment")
fix(L, "Suggested answer: [open reflection response]",
    "Sample: \"Communicating without relitigating is hardest under pressure. When people are stressed, they push back again, and it's tempting to reopen the debate just to calm them down.\"",
    PH, "production")
fix(L, "Suggested answer: Opening:... Deciding:... Communicating:... Closing on time:...",
    "Sample (choosing a venue for the staff party). Opening: \"What I need us to walk away with is one venue, booked today; if we can't agree, I'll decide.\" Deciding: \"I hear both sides — here's the call I'm making: the rooftop, with the restaurant as the rain option.\" Communicating: \"I know it wasn't everyone's first choice; here's what I need now: numbers by Friday.\" Closing: \"We're at time — let's take the menu offline.\"",
    PH, "production")
fix(L, "<p>What to listen/look for: All four module skills are present",
    "<p>Score with the four skills in the Module 5 Assessment section (0–4; pass at 3). What to listen/look for: All four module skills are present",
    "The module assessment had no scale.", "assessment")
