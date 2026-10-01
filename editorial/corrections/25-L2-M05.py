# Level 2 · Module 5 · Apologizing & Thanking Professionally
PH = "The answer key contained an unfilled template placeholder ('[open response following: …]'); replaced with a sample answer and what to check."

# ---------- 5.1 A Real Apology vs. a Weak One ----------
L = "CE-L02-M05-L01"
fix(L, "I want to acknowledge that forgetting to pass that message on caused real confusion for the guest. That's on me -- I should have flagged it the moment I took it. Going forward, I'll write every message down immediately, so this doesn't happen again.",
    "I'm sorry, Ms. Noor — I forgot to pass that message on, and the guest was left waiting for a callback. That's on me — I should have flagged it the moment I took it. Going forward, I'll write every message down immediately, so this doesn't happen again.",
    "'I want to acknowledge that…' is the language of a formal written statement; spoken to a supervisor, a natural apology starts with 'I'm sorry' and then names the impact.",
    "language")
fix(L, 'message the moment I take it, so this doesn\'t happen again."</p>\n</blockquote>',
    'message the moment I take it, so this doesn\'t happen again."</p>\n</blockquote>\n<p>In speech, it is natural to start with "I\'m sorry" and then acknowledge the impact ("I\'m sorry — I forgot to pass that message on, and…"). "I want to acknowledge that…" is more typical of a formal written apology.</p>',
    "Added the register note that makes the spoken model and the written-style example consistent.", "language")

# ---------- 5.2 Apologizing for Your Own Mistake ----------
L = "CE-L02-M05-L02"
fix(L, '<p>Suggested answer: [open response following: acknowledge + "that was on me" + "going forward, I\'ll..."]</p>',
    '<p>Sample: "Hi all — I want to acknowledge that yesterday\'s shift handover notes went out without the late-arrival list. That was on me. Going forward, I\'ll check the arrivals report before I send the notes." Check: the mistake and its impact, clear ownership with no blame on the system or others, a concrete prevention step.</p>',
    PH, "production")

# ---------- 5.4 Apologizing on Behalf of the Team ----------
L = "CE-L02-M05-L04"
fix(L, '<p>What to listen/look for: The apology includes a specific acknowledgment of impact, clear personal ownership, and a concrete prevention step.</p>',
    '<p>Score 0–3: 1 point each for (1) a specific acknowledgment of the impact, (2) clear personal ownership with no excuse first, (3) a concrete prevention step. Sample: "I\'m sorry I sent the wrong room number to the airport driver this morning — the guest waited twenty minutes. That\'s on me. Going forward, I\'ll read the booking back before I send any pickup details."</p>',
    "The module assessment item had criteria but no scoring or sample.", "assessment")
fix(L, '<p>Suggested answer: [open response following: acknowledge the impact + "we should have..." + a team-level prevention step, with no individual named or blamed]</p>',
    '<p>Sample: "Dear Ms. Ahmed, On behalf of the Front Office team, I\'d like to apologise that your airport pickup was not booked for Saturday. We should have confirmed it when you checked in. We have now added a pickup check to our evening handover so this does not happen again. Kind regards, Arif" '
    'Score 0–3: (1) the impact is acknowledged; (2) "we" ownership, with no individual named; (3) a team-level prevention step.</p>',
    PH + " Scoring added for this module assessment item.", "assessment")
