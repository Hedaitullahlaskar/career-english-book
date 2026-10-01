# Level 3 · Assessment
L = "CE-L03-ASSESSMENT"
QA = "QA review of the reference PDF (assessments)"
D = 16

L3_SCORING = """<h2>Scoring</h2>
<p><strong>Part A (items 1–9):</strong> item 5 is multiple choice — 1 point if correct. Every other Part A item is scored 0–3, one point for each criterion below that it meets (8 items × 3 = 24).</p>
<p><strong>Part B (item 10):</strong> 0–6 — one point for each of Module 7's six grammar areas corrected without introducing new errors.</p>
<p><strong>Part C (items 11–12):</strong> the email and the spoken update are each scored 0–3 (6 points).</p>
<table>
<thead>
<tr><th>Criterion (1 point)</th><th>Written items</th><th>Spoken items</th></tr>
</thead>
<tbody>
<tr><td>Task and structure</td><td>Follows the taught structure (email anatomy, the Facts → Evidence → Analysis → Action → Recommendation framework, a specific recommendation) and answers exactly what was asked.</td><td>Follows the taught arc (meeting opening and action point, answer-or-defer, welcome and open question, filler-free delivery).</td></tr>
<tr><td>Language</td><td>Level 3 vocabulary and grammar used accurately; no contractions or fragments where formality requires.</td><td>Level 3 phrases used accurately.</td></tr>
<tr><td>Tone and delivery</td><td>Register fits the reader (client, manager, colleague); diplomatic where needed.</td><td>Register fits the listener; clear stress and falling intonation on statements, without filler words.</td></tr>
</tbody>
</table>
<p>Maximum: Part A 25 + Part B 6 + Part C 6 = <strong>37 points</strong>.</p>"""

rule("L3-assessment-scoring", r"<h2>Scoring rubric</h2>.*?</table>", L3_SCORING,
     "As in Levels 1–2: one weighted rubric (including pronunciation) was applied to written and spoken items alike, the explanation had typos "
     "('Parts A's role-play items'), and no pass mark was given.", "assessment", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, 'Nothing in Parts A-C is new.',
    '<strong>Pass mark: 26 of 37 (70%), with at least 4 of 6 in Part B.</strong> For any item where you scored 0 or 1, review the module named in the item before the capstone.</p>\n<p>Nothing in Parts A–C is new.',
    "No pass mark was given.", "assessment", source=QA)
fix(L, 'Hi [Name],\nCould you send me the occupancy report', 'Dear Ms. Cruz,\nCould you send me the occupancy report',
    "Unfilled placeholder in the model answer.", "production")
fix(L, 'but he actually had not.', 'but in fact he has not finished it yet.',
    "The schedule is still unfinished at the time of writing, so the present perfect is needed ('has not finished … yet').", "grammar")
fix(L, 'A note was sent from the front desk this morning that came from the front desk supervisor and asked for more staff.',
    'A note from the front desk supervisor, which asked for more staff, was sent this morning.',
    "The model answer's relative clause was separated from its noun ('a note was sent … this morning that came from…'), which is exactly the kind of sentence Module 7 teaches learners to fix.",
    "grammar")
fix(L, 'Best regards, [Name]"', 'Best regards, Arif"', "Unfilled placeholder in the model answer.", "production")

for n, extra in {
    3: 'Sample: "Thanks for joining. The goal of this meeting is to agree how we handle the delayed linen delivery today. … Hasan, could you call the supplier by 11 for a confirmed time? … Let\'s wrap up there — thanks, everyone." ',
    4: 'Sample: "That\'s a good question — it connects back to the check-in changes I mentioned: the shorter forms cut the wait by about four minutes. … That\'s a fair question. I don\'t have the cost breakdown by shift with me, but I\'ll send it to you by Thursday." ',
    6: 'Sample: "Mr. Hasan, it\'s a pleasure to meet you — thank you for making the time. … What matters most to you about this event — the schedule, the budget, or the setting?" ',
    8: 'Sample second reading: "The NUMbers are GOOD this MONTH." (pauses where the fillers were). ',
    12: 'Sample: "Quick update on Mr. Alam\'s Thursday booking: the room\'s available, the confirmation was delayed because the setup details weren\'t finalised, and I\'ve told him he\'ll have full confirmation within 30 minutes — I\'m finishing it now." ',
}.items():
    fix(L, f'<span class="answer-number">{n}.</span> <p>What to listen/look for:',
        f'<span class="answer-number">{n}.</span> <p>{extra}Score 0–3 (spoken criteria). What to listen/look for:',
        "Role-play items had marking notes but no sample answer or score.", "assessment", source=QA)
