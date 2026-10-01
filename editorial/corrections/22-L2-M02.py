# Level 2 · Module 2 · Making & Responding to Requests
QA = "QA review of the reference PDF (reported speech, p.480)"

# ---------- 2.1 Requests with Conditions and Trade-offs ----------
L = "CE-L02-M02-L01"
fix(L, '<strong>A condition on your side:</strong> "Could you cover the desk for twenty minutes, if you get a\n chance?" -- leaves room for a genuine no.',
    '<strong>An open condition:</strong> "Could you cover the desk for twenty minutes, if you get a chance?" — leaves room for a genuine no.',
    "Both examples are conditions about the listener's situation; the real contrast is open ('if you get a chance') versus specific ('as long as it doesn't clash with your break').",
    "language")
fix(L, '<strong>A condition on their side:</strong> "As long as it doesn\'t clash with your break, could you cover the\n desk for twenty minutes?"',
    '<strong>A specific condition:</strong> "As long as it doesn\'t clash with your break, could you cover the desk for twenty minutes?"',
    "See previous correction.", "language")

# ---------- 2.4 Relaying a Request Between People ----------
L = "CE-L02-M02-L04"
fix(L, '<p>When you relay what someone said, the tense usually shifts back one step:</p>',
    '<p>Whether the tense changes depends on two things:</p>'
    '<ul><li><strong>The reporting verb.</strong> With a present reporting verb (<em>is asking</em>, <em>wants to know</em>, <em>says</em>), the tense does not change: "He wants to know if you\'re free this afternoon."</li>'
    '<li><strong>Whether it is still true.</strong> With a past reporting verb (<em>said</em>, <em>asked</em>), the tense usually moves back one step ("She said she could help"). '
    'But if the information is still true or still in the future when you relay it, keeping the original tense is also correct and very common in speech: '
    '"Rupa said she\'ll send the towels up in fifteen minutes."</li></ul>',
    "The lesson said the tense 'usually shifts back', but its own table and dialogue use present reporting verbs with no shift. "
    "Backshift depends on the reporting verb and is optional when the reported fact is still true.",
    "grammar", source=QA + "; Cambridge Grammar of English §§ reported speech, backshift")
fix(L, '<td>She said she could help.</td>', '<td>She said she could help. (past reporting verb: tense moves back)</td>', "Each table row now shows why the tense does or does not change.", "grammar")
fix(L, '<td>He wants to know if you\'re free this afternoon.</td>', '<td>He wants to know if you\'re free this afternoon. (present reporting verb: no change)</td>', "See previous correction.", "grammar")
fix(L, '<td>She said she\'d get back to you.</td>', '<td>She said she\'d get back to you. / She said she\'ll get back to you. (both correct: the promise is still in the future)</td>', "See previous correction.", "grammar")
fix(L, 'English reported speech is stricter -- the tense and pronoun shift is what\ntells the listener',
    'In English, the pronoun shift (and, after a past reporting verb, often a tense shift) is what tells the listener',
    "Aligned with the corrected explanation: the pronoun shift is required, the tense shift is not always.", "grammar")
fix(L, '<p>Suggested answer: The guest in [room] wants to know if they can get a late checkout.</p>',
    '<p>Sample: "The guest in Room 215 is asking if she can get a late checkout." (Also correct: "…asked if she could get a late checkout.")</p>',
    "The answer key contained an unfilled placeholder ('[room]').", "production")

# ---------- 2.5 Written Requests: Short and Clear ----------
L = "CE-L02-M02-L05"
fix(L, '<div class="dialogue-box">\n<div class="dialogue-box-label">Listen &amp; Read</div>\n<div class="dialogue-note">Three worked written requests of increasing complexity, in this lesson: (1) a simple request with the ask in the first line, (2) a request with a condition and trade-off (Lesson 1\'s language), and (3) a written decline with a counter-proposal (Lesson 2\'s language).</div>\n</div>',
    '<p>This lesson works through three written requests of increasing complexity: (1) a simple request with the ask in the first line, (2) a request with a condition and trade-off (Lesson 2.1), and (3) a written decline with an alternative (Lesson 2.2).</p>',
    "A 'Listen & Read' box contained no dialogue, only a description of the lesson.", "structure")
fix(L, '<h2>Worked Example 3 (Decline with Counter-Proposal, Written)</h2>', '<h2>Worked Example 3 (Decline with Alternative, Written)</h2>',
    "The example uses Lesson 2.2's decline-with-alternative, not Lesson 2.3's counter-proposal.", "structure")
fix(L, '<h2>Industry Overlays</h2>\n<p>None for this lesson -- the request-first structure applies identically across every written channel and industry.</p>\n',
    '', "An empty section explaining why it was empty.", "production")
fix(L, '<p>Suggested answer: [open response following: request-first structure + condition (as long as/if you get a chance) + trade-off (in return/I can cover for you)]</p>',
    '<p>Sample: "Hi Rupa, could you set aside twenty extra pillows for the conference group arriving on Friday, as long as it doesn\'t clash with your weekend stock count? I can help carry them up to the fifth floor in return. Thanks, Arif" '
    'Score 0–3: (1) the request is in the first line; (2) there is a clear condition (<em>as long as / if you get a chance</em>); (3) there is a specific trade-off.</p>',
    "The answer key contained an unfilled template placeholder; it now has a sample and scoring for this assessment item.", "assessment")
