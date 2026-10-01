# Level 4 · Assessment
L = "CE-L04-ASSESSMENT"
QA = "QA review of the reference PDF (assessments)"
D = 16

L4_SCORING = """<h2>Scoring</h2>
<p>Each part is scored on four criteria, 0–3 each (0 = not shown, 1 = partly, 2 = mostly, 3 = fully), so each part is worth 12 points. Watch or read back each performance once in full before scoring; judge the performance as a whole, not individual phrases.</p>
<table>
<thead>
<tr><th>Criterion (0–3)</th><th>Parts A and B (spoken)</th><th>Part C (written)</th></tr>
</thead>
<tbody>
<tr><td>Structure and completeness</td><td>The stages the task calls for are all there, in order. Part A: preparation showing in the opening, an anchor, a conditional trade, the pressure tactic handled, a close that restates every term (Option 2: the pattern named, a firm line, the colleague heard, an agreed change). Part B: claim, evidence, strongest point placed deliberately and a shared-goal close (Option 2: the issues and the core question, two options with trade-offs, a decision with its reasoning).</td><td>States what is known and what is not yet known, what is already being done, and a specific time for the next update.</td></tr>
<tr><td>Strategic judgment</td><td>Reads the real issue or the real doubt (not just the surface complaint or the first objection), and the response fits it; walk-away point and must-have are protected.</td><td>Accurate and honest: no false reassurance, no alarming over-statement, no guessed fix time.</td></tr>
<tr><td>Composure under pressure</td><td>Stays clear and professional through the pushback, pressure tactic or doubt, without freezing, over-apologising or becoming defensive.</td><td>Calm, steady tone that a worried reader would find reassuring because it is factual.</td></tr>
<tr><td>Tone, register and clarity</td><td>Firm without being harsh, warm without becoming vague; organised from the first sentence, without rambling or heavy hedging.</td><td>Register fits department heads and an external-facing list; short, plain sentences; a clear subject line.</td></tr>
</tbody>
</table>
<p>Maximum: Part A 12 + Part B 12 + Part C 12 = <strong>36 points</strong>.</p>"""

rule("L4-assessment-scoring", r"<h2>Scoring rubric</h2>.*?</table>", L4_SCORING,
     "As in Levels 1–3: one weighted rubric was applied 'holistically' to spoken and written parts alike (including a 'Written precision (Part C)' row that cannot apply to Parts A and B), with no scale for each row and no pass mark.",
     "assessment", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "<p>Nothing in Parts A-C",
    "<p><strong>Pass mark: 25 of 36 (70%), with at least 6 of 12 in every part.</strong> If a part scores below 8, review the modules it draws on before the capstone.</p>\n<p>Nothing in Parts A-C",
    "No pass mark was given.", "assessment", source=QA)
fix(L, "ended with its own\nholistic module assessment.", "ended with its own module assessment.", "'Holistic' no longer describes the scoring.", "assessment")
fix(L, "holistically scored as a single connected performance rather", "scored as a single connected performance rather",
    "'Holistically' no longer describes the scoring.", "assessment")

SPOKEN = "Score 0–3 on each of the four spoken criteria in the scoring table (12 points)."
fix(L, "Scored holistically against the rubric in assessment.md, not item by item.", SPOKEN,
    "A source file name ('assessment.md') was printed, and no scale was given.", "production")
fix(L, "Scored holistically against the rubric in assessment.md.", SPOKEN,
    "A source file name ('assessment.md') was printed, and no scale was given.", "production")
fix(L, '<span class="answer-number">1.</span> <p>What to listen/look for:',
    '<span class="answer-number">1.</span> <p>Sample (Option 1, key moments): "Before we start, I\'ll be honest about where we are: our budget is built around last year\'s rate. Based on the volume we\'ve given you over three years, we\'d see a 2% increase as fair. … If you can hold the increase at 4%, we can commit to a two-year renewal. … I\'d rather decide on the merits than on a deadline — if the other offer is real, send me the terms and I\'ll compare them properly. … So, to confirm: a 4% increase, payment at 60 days, five-day turnaround unchanged, two years, and a named contact. I\'ll send that in writing this afternoon." What to listen/look for:',
    "Role-play items had marking notes but no sample answer.", "assessment", source=QA)
fix(L, '<span class="answer-number">2.</span> <p>What to listen/look for:',
    '<span class="answer-number">2.</span> <p>Sample (Option 1, opening): "I\'d like to ask for your help with one thing: the guest-feedback export. If I get it by Wednesday, your team gets the summary a full week before your own planning meeting — which I know matters to you. …" What to listen/look for:',
    "Role-play items had marking notes but no sample answer.", "assessment", source=QA)
fix(L, "dismissive of the disruption's real impact.</p>",
    "dismissive of the disruption's real impact. Score 0–3 on each of the four written criteria (12 points).</p>"
    "<p>Sample: \"Subject: Booking system outage — update 1 (10:15). The booking system has been down since 9:30. Guests can't be checked in or out electronically, so the front desk is using paper registration and the queue is about 15 minutes. "
    "The IT team is working on it now; they have found the fault in the database server but do not yet have a time for the fix. Please don't promise guests a time. "
    "I'll send the next update by 11:00, whether or not it's fixed. — Arif\"</p>",
    "The written item had marking notes but no model answer or score.", "assessment", source=QA)
