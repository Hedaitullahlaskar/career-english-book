# Level 2 · Assessment
L = "CE-L02-ASSESSMENT"
QA = "QA review of the reference PDF (assessments)"

L2_PARTS_AND_SCORING = """<h2>Part A — Reading: choose the best response (items 1–8)</h2>
<p>Read each short workplace situation and choose the most appropriate response. There is one item per module, Module 1 through Module 8. (Audio is not available yet, so this part is read, not heard.)</p>
<h2>Part B — Speaking (items 9–16)</h2>
<p>Respond aloud to each prompt, and record yourself if you can. There is no single correct wording: each response is scored with the criteria below, and a sample answer is given in the key so you can compare. One prompt per module, Module 1 through Module 8.</p>
<h2>Part C — Writing (items 17–20)</h2>
<p>Write a short response to each of four scenarios. Each scenario combines two modules' language at once, the same way a real situation rarely announces which lesson it belongs to:</p>
<ul>
<li>Daily Updates + Following Up</li>
<li>Requests + Apologizing/Thanking</li>
<li>Telephone + Digital Messaging</li>
<li>Customer Interaction + Workplace Etiquette</li>
</ul>
<h2>Scoring</h2>
<p><strong>Part A:</strong> 1 point for each correct answer (8 points).</p>
<p><strong>Parts B and C:</strong> score each item from 0 to 3 — one point for each criterion it meets. Only criteria that apply to that kind of task are used:</p>
<table>
<thead>
<tr><th>Criterion (1 point)</th><th>Part B — speaking</th><th>Part C — writing</th></tr>
</thead>
<tbody>
<tr><td>Task</td><td>Does exactly what the prompt asks, using the module's structure (for example done/doing/blocked, or decline + alternative).</td><td>Completes both parts of the two-module task.</td></tr>
<tr><td>Language</td><td>Uses the module's phrases and vocabulary accurately.</td><td>Same, with correct grammar and spelling.</td></tr>
<tr><td>Tone and delivery</td><td>Register fits the listener; clear and easy to understand, without long hesitation or repeated apologies.</td><td>Register fits the reader and the channel (chat, email, note); polite and appropriately brief.</td></tr>
</tbody>
</table>
<p>Maximum: Part A 8 + Part B 24 + Part C 12 = <strong>44 points</strong>.</p>"""

rule("L2-assessment-parts-and-scoring",
     r"<h2>Part A -- Listening comprehension</h2>.*?</table>", L2_PARTS_AND_SCORING,
     "As in Level 1: one weighted rubric was applied to spoken and written items alike (pronunciation cannot be scored in writing), "
     "it cited 'holistic' module role-plays, and no pass mark was given. Part A was called 'listening' although it is read.",
     "assessment", fields=("body_html",), flags=16, targets=[L], expect=1)
fix(L, 'Nothing in Parts A-C is new.',
    '<strong>Pass mark: 31 of 44 (70%), with at least 5 of 8 in Part A.</strong> For any item where you scored 0 or 1, review the module named in the item before the capstone.</p>\n<p>Nothing in Parts A–C is new.',
    "No pass mark or next step was given.", "assessment", source=QA)
fix(L, 'You sent a guest the wrong invoice by mistake, and a colleague caught it before it went out.',
    'You attached the wrong invoice to a guest email, and a colleague spotted it after it was sent.',
    "The item said the invoice was both sent and caught 'before it went out'; the correct option describes sending a corrected one.", "continuity")
fix(L, '<span class="exercise-type">Rewriting</span> <span class="assessment-badge">Assessment</span></div><div class="exercise-prompt"><p>Modules 7 + 8',
    '<span class="exercise-type">Writing</span> <span class="assessment-badge">Assessment</span></div><div class="exercise-prompt"><p>Modules 7 + 8',
    "Item 20 asks for new writing, not a rewrite of a given text.", "assessment")

SAMPLES = {
    9: 'Sample: "I\'ve finished the arrivals list for tomorrow. I\'m working on the group rooming list now. I\'m blocked on the final names from the tour company." Task point: done → doing → blocked, in that order, under 30 seconds.',
    10: 'Sample: "I\'m tied up with the 3 o\'clock check-ins, so I can\'t help with the inventory now. What I can do instead is give you an hour tomorrow morning. Would that work?" Task point: a clear decline, a specific alternative, and "Would that work?"',
    11: 'Sample: "Good morning, Front Desk, this is Nadia speaking. How can I help you today?" Task point: greeting + department + name + offer to help.',
    12: 'Sample: "Heads up — the lift on the east side is out of service, so please send guests to the west lifts." … "Quick question — do you know where the spare key cards are kept?" Task point: two separate messages, each with its signal opener.',
    13: 'Sample: "I\'m sorry — I gave the guest the wrong breakfast times this morning, and she missed breakfast. That\'s on me. Going forward, I\'ll check the times on the board before I answer." Task point: acknowledge + own + prevent.',
    14: 'Sample: "Just following up on the request I sent on Monday for the extra key-card printer ribbon — I wanted to flag it in case it got missed." Task point: a softening opener, the original request named, no blame.',
    15: 'Sample: "Welcome! … Yes, the pool is open until 9 PM — in other words, you can use it after dinner. Does that answer your question? … I understand your concern — your towels should have been replaced. Let me see what I can do right away. … I\'m glad we could sort that out. Is there anything else I can help you with? Have a great stay!" Task point: a plain answer with a check, listen-acknowledge-offer, the full closing formula.',
    16: 'Sample: "Sorry, I\'m running about five minutes behind — I\'ll join the call at 3:05." … "Good evening, Dr. Rahman — the day went smoothly. One guest\'s late check-out was sorted with housekeeping." Task point: a proactive heads-up with a time, then title + surname and a short, substantive update.',
}
for n, text in SAMPLES.items():
    fix(L, f'<span class="answer-number">{n}.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
        f'<span class="answer-number">{n}.</span> <p>{text} Score 0–3 using the Part B criteria.</p>',
        "Unfinished model answer replaced with a sample answer and the item's task requirement.", "assessment", source=QA)

fix(L, '<p>What to listen/look for: The follow-up opens politely', '<p>Score 0–3 (Part C criteria). Sample: (1) "Just following up on the broken chair in the staff room — I wanted to flag it in case it got missed." (2) "I\'ve finished the arrivals check. I\'m working on the late check-out list. I\'m blocked on two room numbers from housekeeping." Task point: the follow-up opens politely',
    "Sample answer and scoring added.", "assessment")
fix(L, '<p>What to listen/look for: The apology names the specific mistake,', '<p>Score 0–3 (Part C criteria). Sample: "Hi Rina, I\'m sorry — I gave you the wrong time for Saturday\'s swap, and it caused you a clash. That\'s on me; I\'ll check the roster before I suggest times from now on. Could we swap your Saturday 2–10 PM shift for my Sunday morning, if that suits you? I can take your Wednesday late in return." Task point: the apology names the specific mistake,',
    "Sample answer and scoring added.", "assessment")
fix(L, '<p>What to listen/look for: The message states what\'s needed in one clear idea,', '<p>Score 0–3 (Part C criteria). Sample: "Quick question — does the spa have any free slots this afternoon for Room 410? This is time-sensitive: I promised to call the guest back within 15 minutes." Task point: the message states what\'s needed in one clear idea,',
    "Sample answer and scoring added.", "assessment")
fix(L, '<p>What to listen/look for: The guest-facing response acknowledges the complaint', '<p>Score 0–3 (Part C criteria). Sample: (1) "I understand your concern — your room should have been cleaned by now. I appreciate you telling me. Let me ask housekeeping to go up straight away. … Is there anything else I can help you with? Have a lovely afternoon." (2) "Good afternoon, Dr. Rahman — a guest in 312 reported a late room clean; housekeeping is on the way up now." Task point: the guest-facing response acknowledges the complaint',
    "Sample answer and scoring added.", "assessment")
