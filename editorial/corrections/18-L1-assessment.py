# Level 1 · Assessment
L = "CE-L01-ASSESSMENT"
QA = "QA review of the reference PDF (assessments)"

L1_PARTS_AND_SCORING = """<h2>Part A — Reading: choose the best response (items 1–7)</h2>
<p>Read each short workplace situation and choose the most appropriate response. There is one item per module, in order. (Audio is not available yet, so this part is read, not heard.)</p>
<h2>Part B — Speaking (items 8–14)</h2>
<p>Respond aloud to each prompt, and record yourself if you can. There is no single correct wording: each response is scored with the criteria below, and a sample answer is given in the key so you can compare.</p>
<h2>Part C — Writing (items 15–18)</h2>
<p>Write a short response to each scenario. Most combine two modules' language, the same way real situations rarely stay inside one lesson.</p>
<h2>Scoring</h2>
<p><strong>Part A:</strong> 1 point for each correct answer (7 points).</p>
<p><strong>Parts B and C:</strong> score each item from 0 to 3 — one point for each criterion it meets. Only criteria that apply to that kind of task are used:</p>
<table>
<thead>
<tr><th>Criterion (1 point)</th><th>Part B — speaking</th><th>Part C — writing</th></tr>
</thead>
<tbody>
<tr><td>Task</td><td>Does exactly what the prompt asks (for example, names both options, states the purpose, restates the deadline).</td><td>Same.</td></tr>
<tr><td>Language</td><td>Uses the module's workplace phrases and vocabulary accurately.</td><td>Same, with correct grammar and spelling.</td></tr>
<tr><td>Tone and delivery</td><td>Register fits the listener; clear and easy to understand, without long hesitation or repeated apologies.</td><td>Register fits the reader; polite, clear and appropriately brief.</td></tr>
</tbody>
</table>
<p>Maximum: Part A 7 + Part B 21 + Part C 12 = <strong>40 points</strong>.</p>"""

rule("L1-assessment-parts-and-scoring",
     r"<h2>Part A -- Listening comprehension</h2>.*?</table>", L1_PARTS_AND_SCORING,
     "The rubric applied the same weighted criteria to spoken and written tasks (pronunciation and 'delivery' cannot be scored in writing), "
     "referred to 'Module 2's pilot assessment', and never explained how to turn a score into a result. Part A was called 'listening' "
     "although it is read. Replaced with criteria that apply to each part and a points total.",
     "assessment", fields=("body_html",), flags=16, targets=[L], expect=1)

fix(L, 'Nothing in Parts A-C is new.',
    '<strong>Pass mark: 28 of 40 (70%), with at least 4 of 7 in Part A.</strong> For any item where you scored 0 or 1, review the module named in the item before moving on to the capstone.</p>\n<p>Nothing in Parts A–C is new.',
    "No pass mark or next step was given.", "assessment", source=QA)
fix(L, '<span class="exercise-type">Rewriting</span> <span class="assessment-badge">Assessment</span></div><div class="exercise-prompt"><p>Modules 6 + 7 -- Write',
    '<span class="exercise-type">Writing</span> <span class="assessment-badge">Assessment</span></div><div class="exercise-prompt"><p>Modules 6 + 7 -- Write',
    "Item 18 asks for a new message, not a rewrite of a given text.", "assessment")

SAMPLES = {
    8: 'Sample: "Hi, I\'m Nadia. I studied business, and I\'ve worked in retail for two years. I\'ll be on the front-office team — really looking forward to working with you." Task point: name, background or role, and a welcoming close.',
    9: 'Sample: "Good morning. I\'m Nadia — I\'m starting today. I\'m here to see Mr. Hossain." Task point: greeting, name, and purpose (PAT-0001).',
    10: 'Sample: "Pretty busy, actually — it\'s been non-stop since nine. How about you?" Task point: a short answer plus a returned question.',
    11: 'Sample: "So, before I leave, I\'ll email the vendor the updated order and copy you on it." Task point: the action, the object, the person to copy and the deadline ("before I leave") are all restated.',
    12: 'Sample: "Just to check — do you mean the numbers in this week\'s sales report, or the figures in the client invoice?" Task point: names the specific options instead of "What do you mean?" (MIS-0010).',
    13: 'Sample: "The client report is in progress — the invoice section is still pending, and I\'ll submit it by Thursday." Task point: at least one status word used correctly.',
    14: 'Sample: "Could you send me the updated rota before 5 today? I need it to plan tomorrow\'s shifts." Task point: a softened request with a time and a reason.',
}
for n, text in SAMPLES.items():
    fix(L, f'<span class="answer-number">{n}.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
        f'<span class="answer-number">{n}.</span> <p>{text} Score 0–3 using the Part B criteria.</p>',
        "Unfinished model answer replaced with a sample answer and the item's task requirement.", "assessment", source=QA)

fix(L, '<p>What to listen/look for: Acknowledges the misunderstanding, corrects it plainly,',
    '<p>Sample: "I think my comment this morning came out wrong — I didn\'t mean it as a criticism at all. I only meant the queue was long. Thanks for telling me." Score 0–3 (Part C criteria). Task point: acknowledges the misunderstanding, corrects it plainly,',
    "Sample answer added; marking note kept as the task requirement.", "assessment")
fix(L, '<p>What to listen/look for: Restates the instruction accurately before asking a targeted',
    '<p>Sample: "Just to confirm — you\'d like the full inventory report by 3 PM today? Could you tell me which section is most urgent, so I can finish that first?" Score 0–3 (Part C criteria). Task point: restates the instruction accurately before asking a targeted',
    "Sample answer added.", "assessment")
fix(L, '<p>What to listen/look for: Adapts the three-part self-introduction to a group setting',
    '<p>Sample: "Hi everyone, nice to meet you all. I\'m Nadia — I studied business and I\'ve worked in retail for two years. I\'ll be on the front desk with you, and I\'m really looking forward to working with you all." Score 0–3 (Part C criteria). Task point: adapts the three-part self-introduction to a group setting',
    "Sample answer added.", "assessment")
fix(L, '<p>What to listen/look for: Uses a softened request pattern, states the reason briefly,',
    '<p>Sample: "Hi Mr. Hossain, the monthly report is in progress — I\'ve finished the sales section, but the expense figures are still pending from Accounts. Would it be possible to have one extra day, until Thursday, to finish it? Thanks, Nadia." Score 0–3 (Part C criteria). Task point: uses a softened request pattern, states the reason briefly,',
    "Sample answer added.", "assessment")
