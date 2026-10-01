# Level 5 · Assessment
L = "CE-L05-ASSESSMENT"
D = 16

L5_SCORING = """<h2>Scoring</h2>
<p>Each part is scored on four criteria, 0–3 each (0 = not shown, 1 = partly, 2 = mostly, 3 = fully), so each part is worth 12 points. Watch or read back each part once in full before scoring.</p>
<table>
<thead>
<tr><th>Part</th><th>Criteria (0–3 each)</th></tr>
</thead>
<tbody>
<tr><td>A — Delegation and feedback</td><td>(1) Detail is calibrated to Rima's experience with this task. (2) Real ownership of the outcome is handed over, with the deadline and what done looks like. (3) Feedback to Farhan names the exact action and its impact. (4) Register shifts between the two moments while the voice stays the same.</td></tr>
<tr><td>B — Chairing a contested decision</td><td>(1) The meeting opens with the outcome needed, and both sides are heard fully. (2) A clear decision is made, with its reasoning, and named as not unanimous. (3) The version given to Farhan matches the decision, with reasoning and next steps, without reopening the debate. (4) Calm, fair, firm tone throughout.</td></tr>
<tr><td>C — Career-growth conversation</td><td>(1) A genuine, specific request for feedback. (2) A case for more responsibility built on specific, checkable evidence. (3) Compensation discussed without underselling or overreaching, anchored in delivered value. (4) Confident, respectful register with a manager, in your own voice.</td></tr>
</tbody>
</table>
<p>Maximum: Part A 12 + Part B 12 + Part C 12 = <strong>36 points</strong>.</p>"""

rule("L5-assessment-scoring", r"<h2>Scoring rubric</h2>.*?</table>", L5_SCORING,
     "As in Levels 1–4: one weighted rubric was applied 'holistically' to all three parts (rows such as 'Composure on compensation' cannot apply to Parts A and B), with no scale and no pass mark.",
     "assessment", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "<p>Nothing in Parts A-C is new.",
    "<p><strong>Pass mark: 25 of 36 (70%), with at least 6 of 12 in every part.</strong> If a part scores below 8, revisit the modules it draws on before the capstone.</p>\n<p>Nothing in Parts A-C is new.",
    "No pass mark was given.", "assessment")
fix(L, "Each one is scored holistically, the same way the capstone that follows it will be.",
    "Each part is scored on four criteria, explained under Scoring below.", "'Scored holistically' gave no scale.", "assessment")
fix(L, "This is scored against the rubric below, not\nmatched against a model answer.", "It is scored with the criteria below, not matched against a model answer.",
    "Points to the new scoring section.", "assessment")
fix(L, "Rima joined guest relations recently and has never run the VIP welcome-packet routine on her own\nbefore.",
    "Rima has helped with VIP welcome folders before (Module 1), but she has never run the full welcome-packet and room-upgrade routine for a corporate group on her own.",
    "Rima prepared the VIP welcome folders in Lesson 1.1 and had been on the team for months by Level 5, so she is not a new joiner who has never done the routine.", "continuity")
fix(L, "(less than you'd give Hasan, more than you'd give\n someone who'd done it ten times) -- and hand her real ownership, not step-by-step instructions.",
    "(more than you'd give Hasan, who has done it many times) — and hand her real ownership of the outcome, not a checklist to follow.",
    "The calibration was backwards: Module 1 teaches that someone new to a task needs more detail than an experienced colleague, not less.", "factual")
fix(L, '<span class="answer-number">1.</span> <p>What to listen/look for:',
    '<span class="answer-number">1.</span> <p>Sample: "Rima, I\'d like you to own the welcome packets and the room-upgrade list for Thursday\'s group. You\'ve done the VIP folders, so you know the standard — this time it\'s forty guests, and the upgrade list has to match the client\'s seniority list, which I\'ll send you. I need a draft by Wednesday noon; done looks like every packet labelled and the list checked against the rooming list. Come to me with anything you\'re unsure about. … Farhan — quick note while it\'s fresh: last week you spotted the double charge on Mr. Alam\'s bill before he checked out. That saved us a complaint and a refund. That\'s exactly the kind of check I want to see more of." Score 0–3 on each of Part A\'s four criteria (12 points). What to listen/look for:',
    "Role-play items had marking notes but no sample answer or score.", "assessment")
fix(L, '<span class="answer-number">2.</span> <p>What to listen/look for:',
    '<span class="answer-number">2.</span> <p>Sample (key moments): "What I need us to walk away with is a posted roster by two o\'clock. … I hear both sides of this. Here\'s the call I\'m making: a senior person on every shift, but one fewer person on Sunday and Monday nights. I recognize this isn\'t unanimous." To Farhan: "We\'ve decided to keep one senior on every shift and drop one person on Sunday and Monday nights. The reasoning is that it covers the risk without overstaffing a quiet weekend. I know it wasn\'t everyone\'s first choice; here\'s what I need from you: post the roster and confirm the night swaps by six." Score 0–3 on each of Part B\'s four criteria (12 points). What to listen/look for:',
    "Role-play items had marking notes but no sample answer or score.", "assessment")
fix(L, '<span class="answer-number">3.</span> <p>What to listen/look for:',
    '<span class="answer-number">3.</span> <p>Score 0–3 on each of Part C\'s four criteria (12 points). What to listen/look for:',
    "The item had no score.", "assessment")
