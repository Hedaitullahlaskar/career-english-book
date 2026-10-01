# Level 3 · Module 9 · Digital & Cross-Platform Communication
PH = "The answer key contained an unfilled template placeholder; replaced with a sample answer."
D = 16

L = "CE-L03-M09-L01"
fix(L, "<p>Suggested answer: '[open response chaining an audio/video check, a screen-share confirmation, one recovered connection issue, and a professional close]'</p>",
    "<p>Sample: \"Good morning — can everyone hear and see me okay? … I'll share my screen now — can you see the floor plan? … Sorry, you're breaking up a little — could you say that last part again? … Great, that covers everything. I'll send a summary by email this afternoon — thanks for joining.\" Check: an audio check before starting, a screen-share check, a calm, non-blaming connection fix, and a close with a next step.</p>",
    PH, "production")

L = "CE-L03-M09-L02"
fix(L, "(L2-M4-L01); the three-way channel-selection framework, <strong>CF-0006</strong> (L2-\n M4-L05).",
    "(Level 2, Lesson 4.1); the three-way channel-selection framework, <strong>CF-0006</strong> (Level 2, Lesson 4.5).",
    "Internal lesson codes replaced.", "reference")
fix(L, "-- exactly the failure this level's\nH.1 review flagged when an early lesson draft used a similar case narrowly around named apps\nrather than the underlying judgment.",
    ".", "An internal editorial note about an earlier draft ('this level's H.1 review flagged…') was printed in the lesson.", "production")
fix(L, "<p>Suggested answer: '[open, reflective response -- the specific tools differ by workplace, but urgency, sensitivity, complexity, and visual need decide the choice in both cases]'</p>",
    "<p>Sample: \"The tools are different because each workplace has its own habits — a hotel desk lives on the phone and WhatsApp, an office on Teams and email. But the decision is the same: it's urgent, so it needs the fastest live channel each workplace actually uses.\" Check: the answer separates the tool from the judgment (urgency, sensitivity, complexity, visual need).</p>",
    PH, "production")

L = "CE-L03-M09-L03"
fix(L, "<strong>register</strong> (L2-M4-L01).", "<strong>register</strong> (Level 2, Lesson 4.1).", "Internal lesson code replaced.", "reference")
fix(L, "<p>Suggested answer: '[open response producing three consistent, channel-appropriate versions of the same true content]'</p>",
    "<p>Sample. Email: \"Dear Mr. Islam, I wanted to let you know that the replacement key-card printer has been delivered and installed. All staff can print cards at the front desk again from today. Best regards, Arif\" Chat: \"Key-card printer's back — all fixed.\" Spoken: \"Quick update — the new key-card printer's in and working, so we're back to normal at the desk.\" Check: the same facts in all three; only the register changes.</p>",
    PH, "production")

L = "CE-L03-M09-L04"
fix(L, "Facts: weekday occupancy averaged 78% last quarter, up from 71% the quarter before. Evidence: the increase tracks closely with the new corporate-rate package launched in March. Analysis: the Chowdhury Group's proposed dates fall within our highest-occupancy window. Recommendation:",
    "Facts: weekday occupancy averaged 78% last quarter, up from 71% the quarter before. Evidence: the property-management system's occupancy reports for both quarters (attached). Analysis: the rise began after the corporate-rate package launched in March, and the Chowdhury Group's proposed dates fall within our highest-occupancy window. Action: I've placed a provisional hold on 20 rooms for their dates. Recommendation:",
    "The report used Module 2's framework, but labelled an interpretation as 'Evidence' and left out the Action step.", "factual")
fix(L, "Since you mentioned the group size earlier, I can offer a small additional discount on the block booking itself, on top of the corporate rate -- that should bring it closer to what you're looking for.",
    "Since you mentioned the group size earlier, I checked with Ms. Noor, and we can offer an additional 5% on the block booking itself, on top of the corporate rate — that should bring it closer to what you're looking for.",
    "Arif offered a discount on his own authority, contradicting Lesson 6.4 (no unauthorized discount on the spot) and Module 5 (honesty about the limits of your authority).",
    "continuity")
fix(L, "(Modules 9 and the hierarchy-aware address carried over from Level 2)", "(Module 9, plus the hierarchy-aware address from Level 2)",
    "Garbled wording.", "language")
fix(L, "<h2>A Full Simulated Professional Week</h2>\n<p>The connected sequence below chains together: a request email, a short report, a meeting update, a\npresentation snippet, a customer complaint, a client conversation, and a closing video call -- in\nthe order a genuinely busy week might actually produce them. See the dialogue above for the full\nsequence.</p>\n",
    "", "The section only described the dialogue and pointed to it as both 'below' and 'above'.", "structure")
rule("L3-9.4-prompt-quotes", r"<p>'(Module 9 Assessment:.*?)'</p>", r"<p>\1</p>",
     "Stray quotation marks around the exercise prompt.", "typography", fields=("practice_html",), flags=D, targets=[L], expect=1)
fix(L, "<p>Suggested answer: [open, reflective response]</p>",
    "<p>Answers will vary — this is a personal reflection. A useful answer names three specific formats (for example, \"the incident report\", \"handling a client's price objection\", \"opening a video call\") and gives a concrete reason for each.</p>",
    PH, "production")
rule("L3-9.4-assessment-key", r"<p>Suggested answer: '\[open response chaining multiple Level 3 skills.*?\]'</p>",
     "<p>Use the Listen &amp; Read week as the model. Score each communication moment 0–2: 1 point for choosing the right document or channel (CF-0017), 1 point for keeping the quality of that document or conversation. Six moments = 12 points. 10–12: Module 9 complete; 8–9: complete, practise the weakest moment; 7 or fewer: review the modules behind the weakest moments. This activity leads directly into the Level 3 capstone, \"The Client Review\".</p>",
     "The module assessment key was a template placeholder with an unspecified holistic grade.", "assessment",
     fields=("practice_html",), flags=D, targets=[L], expect=1)
