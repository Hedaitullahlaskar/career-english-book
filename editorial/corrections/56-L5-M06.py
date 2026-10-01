# Level 5 · Module 6 · Executive Presentation Skills
D = 16
PH = "The answer key gave an unfilled template ('[your own read…]', '[evidence]'); replaced with a sample answer."
KIOSK = ("Level 4 Module 3 already installed a self-service kiosk in the lobby, so the vision cannot be to pilot 'a self-check-in kiosk' as if none existed; "
         "it now extends self-check-in from the existing lobby kiosk.")

L = "CE-L05-M06-L01"
rule("L5-6.1-sample", r"Suggested answer: As I see it, \[your own read of the situation\]\..*?\[the point that matters to you\]\.",
     "Sample: \"As I see it, last week's late-checkout requests are getting out of hand — we had forty, and housekeeping fell behind every day. My call on this is that late checkout after 1 p.m. now needs a supervisor's approval. What I want us to take away is that we can still say yes to guests; we just need to plan it with housekeeping.\"",
     PH, "production", fields=("practice_html",), flags=D, targets=[L], expect=1)

L = "CE-L05-M06-L02"
rule("L5-6.2-hotel", r"\bresort's\b", "hotel's", "The book's setting is a hotel; 'resort' appeared only in this lesson.", "continuity",
     fields=("body_html",), targets=[L], expect=4)
rule("L5-6.2-who-fixed", r"(double-booking (?:headaches|problems)) you and Hasan", r"\1 Rima and Hasan",
     "Arif is answering Farhan, but it was Rima and Hasan who fixed the double-bookings (Modules 3 and 4).", "continuity",
     fields=("body_html", "practice_html"), targets=[L], expect=4)
rule("L5-6.2-kiosk-pilot", r"piloting a self-check-in kiosk by next quarter(, starting with returning guests)?",
     "piloting self-check-in for returning guests by next quarter, building on the lobby kiosk we already have",
     KIOSK, "continuity", fields=("body_html", "practice_html"), targets=[L], expect=3)
fix(L, "(V-0229, recycled from L5-M04-L01)", "(V-0229, recycled from Lesson 4.1)", "Internal lesson code replaced.", "reference")
rule("L5-6.2-sample-2", r"Suggested answer: The reasoning behind this is \[what's driving the change\]\..*?\[a concrete next step\]\.",
     "Sample: \"The reasoning behind this is that we're expecting more conference groups next year. This connects directly to the Monday mornings when the desk is swamped with group check-outs. Where we're headed is group check-out handled the night before, by email. The vision here is a calm Monday desk. What this means for our team is that we trial it with the next two groups.\"",
     PH, "production", fields=("practice_html",), flags=D, targets=[L], expect=1)
rule("L5-6.2-sample-3", r"Suggested answer: The reasoning behind this is \[the driver\]\..*?\[the first concrete step\]\.",
     "Sample: \"The reasoning behind this is that half our complaints are about waiting for information. This connects directly to the calls you take every day asking 'Is my room ready?' Where we're headed is guests getting a text the moment their room is ready. The vision here is no more 'just checking' calls. What this means for our team is that housekeeping and the desk agree one 'room ready' signal this month.\"",
     PH, "production", fields=("practice_html",), flags=D, targets=[L], expect=1)

L = "CE-L05-M06-L03"
rule("L5-6.3-codes", r"recycled from L4-M05-L02", "recycled from Level 4, Lesson 5.2", "Internal lesson code replaced.", "reference",
     fields=("body_html",), targets=[L], expect=2)
fix(L, "Suggested answer: That's a fair challenge, Ms. Noor. Here's the data behind that claim: [evidence]. I'll stand by that, and here's why -- [reason the concern is manageable rather than disqualifying].",
    "Sample: \"That's a fair challenge, Ms. Noor. Here's the data behind that claim: staffed kiosks at the two hotels in our group reached eighty percent adoption within six weeks. I'll stand by that, and here's why — the risk is real, but it's one we already know how to manage with a staff member beside the kiosk.\"",
    PH, "production")
fix(L, "Suggested answer: That's a fair challenge -- let me address that directly. [Push back gently on any flawed assumption, if needed.] Here's the data behind that claim: [evidence]. I'll stand by that, and here's why -- [reason].",
    "Sample (question: \"Isn't a four-day training plan too long for a busy month?\"): \"That's a fair challenge — let me address that directly. I'd push back gently on 'too long': it's four one-hour sessions, not four days off the desk. Here's the data behind that claim: last year's one-day training left us with twelve booking errors in the first week. I'll stand by that, and here's why — shorter sessions cost us less than fixing those errors.\"",
    PH, "production")

L = "CE-L05-M06-L04"
KABIR = ("Ms. Noor raised this exact challenge in Lesson 6.3 and accepted Arif's answer; repeating it a month later made no sense. "
         "It now comes from Mr. Zahid Kabir (Head of Finance), one of the other department heads, who asked the tough questions in Level 4.")
fix(L, "with Dr. Rahman, Ms. Noor, and two\nother department heads in the room.", "with Dr. Rahman, Ms. Noor, Mr. Zahid Kabir from Finance and another department head in the room.", KABIR, "continuity")
fix(L, '<span class="dialogue-speaker">Ms. Noor:</span> <span class="dialogue-text">I agree with the direction, but I remember our 2019 attempt',
    '<span class="dialogue-speaker">Mr. Kabir:</span> <span class="dialogue-text">I agree with the direction, but I remember our 2019 attempt', KABIR, "continuity")
fix(L, "That's a fair challenge, Ms. Noor -- let me address that directly.", "That's a fair challenge, Mr. Kabir -- let me address that directly.", KABIR, "continuity")
fix(L, '<span class="dialogue-speaker">Ms. Noor:</span> <span class="dialogue-text">That\'s a fair answer. Staff it properly, and I\'m on board.',
    '<span class="dialogue-speaker">Mr. Kabir:</span> <span class="dialogue-text">That\'s a fair answer. Staff it properly, and I\'m on board.', KABIR, "continuity")
fix(L, "the exchange with Ms. Noor, ending", "the exchange with Mr. Kabir, ending", KABIR, "answer-key")
fix(L, "self-check-in for most guests, starting with a kiosk pilot.", "self-check-in for most guests, starting with a pilot for returning guests that builds on our lobby kiosk.", KIOSK, "continuity")
fix(L, "This lesson introduces no new vocabulary or pattern.", "This lesson introduces no new vocabulary or sentence pattern; the formula below simply combines the module's three patterns.",
    "The lesson does introduce a formula (CF-0026), so 'no new pattern' needed qualifying.", "factual")
fix(L, "as they appear in the dialogue below.</li>", "as they appear in the dialogue above.</li>", "The dialogue is above the Self-Check.", "reference")
fix(L, "not only on the\ncontent of the proposal itself.</p>",
    "not only on the content of the proposal itself. Score 0–4, one point per move of CF-0026 done well; pass at 3, and the challenge-response must be one of them.</p>",
    "The module assessment had no scale.", "assessment")
rule("L5-6.4-sample-2", r"Suggested answer: As I see it, \[your read of the situation\]\..*?The vision here is \[what it looks like\]\.",
     "Sample: \"As I see it, our wedding business is growing faster than our banquet team can handle. My call on this is that we hire a dedicated wedding coordinator. The reasoning behind this is that we booked twenty-two weddings this year, up from twelve. This connects directly to the weekends your teams have spent covering for each other. Where we're headed is one person who owns every wedding from enquiry to send-off. The vision here is couples who deal with one name, not five.\"",
     PH, "production", fields=("practice_html",), flags=D, targets=[L], expect=1)
fix(L, "Suggested answer: Opening:... Vision:... Hard question handled:... Closing:...",
    "Sample (moving staff training online). Opening: \"As I see it, our classroom training can't keep up with new starters; my call is to move the basics online.\" Vision: \"Where we're headed is new staff who arrive on day one already knowing the systems.\" Hard question: \"That's a fair challenge about cost — here's the data: the platform costs less than two classroom days a year; I'll stand by that.\" Closing: \"What I want us to take away is that we start with the booking-system module next month.\"",
    PH, "production")
fix(L, "This is the Module 6 assessment task.</p>", "Score with the scale in the Module 6 Assessment section (0–4; pass at 3).</p>",
    "Production language and no scale.", "assessment")
