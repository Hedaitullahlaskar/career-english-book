# Level 1 · Module 2 · First-Day Communication
#
# Continuity: this module was written for a generic office ("a glass office
# building", "Operations", supervisor "Ms. Rahman"), while the rest of the book
# places Arif in a hotel's front office under his supervisor Mr. Hossain
# (Modules 4–7). The setting and supervisor are aligned here; the targeted
# rules at the end of this file rename Ms. Rahman → Mr. Hossain and the
# one-module character "Priya" → Priyanka (Arif's front-office peer elsewhere).
M02 = ["CE-L01-M02-L01", "CE-L01-M02-L02", "CE-L01-M02-L03", "CE-L01-M02-L04", "CE-L01-M02-L05"]
CONT = "Module 2 was set in an office with a different supervisor and team; aligned with the hotel front office used in the rest of the book."

# ---------- 2.1 Arriving and Greeting on Day One ----------
L = "CE-L01-M02-L01"
fix(L, 'Arif is standing outside a glass office building, his offer-letter email open on his phone.',
    'Arif is standing outside the hotel\'s staff entrance, his offer-letter email open on his phone.', CONT, "continuity")
fix(L, 'Reception area, 8:55 AM. Arif approaches the front desk, where Meera is on the phone. Tom, a colleague, is walking past with a coffee.',
    'The staff reception desk, 8:55 AM. Arif walks up to the desk, where Meera is on the phone. Tom, a front-office colleague, is walking past with a coffee.',
    CONT, "continuity")
fix(L, 'Let me just call her. Could you sign in here, please?', 'Let me just call him. Could you sign in here, please?', CONT, "continuity")
fix(L, "I'm Tom, I work with Ms. Rahman's team.", "I'm Tom, I'm on the front-office team.", CONT, "continuity")
fix(L, 'All set — she\'s on her way down now.', 'All set — he\'s on his way down now.', CONT, "continuity")
fix(L, 'Friendly, informal-professional; learner receives this more than produces it in L01',
    'Friendly, informal-professional; you will hear this more often than you say it', "Production language and internal code ('L01').", "production")
fix(L, '<p>Two patterns, taught only as much as this situation needs: "I\'m + verb-ing" for a right-now/today context ("I\'m starting today" — the "true today" use, not the ongoing-action sense) and "I\'m here to + verb" ("I\'m here to see Ms. Rahman" — states purpose simply). No verb-tense lecture — both patterns are drilled only inside the dialogue and the speaking task.</p>\n<p><strong>Sentence pattern(s) taught:</strong> <code>PAT-0001</code> — see.</p>',
    '<p>Two short patterns are all you need on arrival:</p>'
    '<ul><li><strong>Present continuous for an arrangement</strong> — something already planned: "I\'m starting today." (This is not about an action in progress; it states a fixed plan.)</li>'
    '<li><strong>"I\'m here to + verb"</strong> to state your purpose: "I\'m here to see Mr. Hossain."</li></ul>'
    '<p><strong>Sentence pattern <code>PAT-0001</code>:</strong> "I\'m here to + verb" — "I\'m here to see Mr. Hossain." / "I\'m here to collect my ID card."</p>',
    "Production language ('no verb-tense lecture', 'drilled') removed, the grammar label made accurate (arrangement, not 'true today'), and the broken '— see.' reference replaced with the pattern itself.",
    "reference", source="Cambridge Grammar of English, present progressive for future arrangements")
fix(L, '<li>Word stress: STARTing today; here to SEE Ms. RAHman (content words stressed, not "I\'m" or "to").</li>',
    '<li>Sentence stress: "I\'m STARTing toDAY"; "I\'m here to SEE Mr. Hossain" — the content words carry the stress, not "I\'m" or "to".</li>',
    "These are examples of sentence stress, not word stress; 'today' is stressed on its second syllable.", "pronunciation")
fix(L, '<p>Used only where it prevents a genuine, recurring mistake: "I\'m here to..." is not a word-for-word translation of "<span class="bn">আমি এসেছি</span>..."; Bengali speakers often add an unnecessary "for coming" ("I have come here for...") — the natural English pattern drops that entirely.</p>',
    '<p>"আমি ... জন্য এসেছি" translated word for word gives "I have come here for...", which sounds unnatural in English. Use "I\'m here to + verb" instead: "I\'m here to see Mr. Hossain."</p>',
    "Production language removed; the note now names the actual Bengali source structure.", "l1-support")
fix(L, 'Listen to the dialogue. What does Meera give Arif before he goes upstairs?',
    'Read the dialogue again. What does Meera give Arif before he goes upstairs?', "No audio recording exists yet.", "audio")
fix(L, '<p>"I\'m here to + verb" states your purpose simply.</p>',
    '<p><strong>to</strong> — "I\'m here to see Mr. Hossain." "I\'m here to + verb" states your purpose simply.</p>',
    "The answer key explained the pattern but never gave the answer.", "answer-key")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Sample: "Good morning. I\'m Arif — I\'m starting today. I\'m here to see Mr. Hossain." … "Nice to meet you, Tom. I\'m Arif." … "Thanks! See you around." Check: name and purpose in one or two short sentences, "Nice to meet you" when a colleague introduces himself, a short thank-you to close.</p>',
    "Unfinished model answer replaced with a sample and checklist.", "production")

# ---------- 2.2 Meeting Your Supervisor and Team ----------
L = "CE-L01-M02-L02"
fix(L, 'Ms. Rahman meets Arif at the top of the stairs. "Ready?" she asks with a smile. "Let\'s introduce you to the team." Arif follows her onto the floor, where four faces look up from their desks, one by one.',
    'Mr. Hossain, his supervisor, meets Arif at the top of the stairs. "Ready?" he asks with a smile. "Let\'s introduce you to the team." Arif follows him into the front-office back room, where three faces look up from their desks, one by one.',
    CONT + " The dialogue introduces three colleagues, not four.", "continuity")
fix(L, 'Open-plan office floor. Ms. Rahman walks Arif past three desks.',
    'The front-office back room, behind the front desk. Mr. Hossain walks Arif past three desks.', CONT, "continuity")
fix(L, "Everyone, this is Arif — he's joining us in Operations.", "Everyone, this is Arif — he's joining us on the front desk.", CONT, "continuity")
fix(L, '<td>Sincere, low-pressure — mainly received, not produced, in L02</td>',
    '<td>Sincere, low-pressure — you will usually hear this rather than say it</td>', "Production language and internal code.", "production")
fix(L, '<td><strong>Operations (dept.)</strong> <em>n.</em></td><td>The team that keeps daily work running</td>',
    '<td><strong>Front Office (dept.)</strong> <em>n.</em></td><td>The hotel team that handles check-in, check-out and guest requests at the front desk</td>',
    CONT, "continuity")
fix(L, '<span class="bn">অপারেশন্স বিভাগ</span>', '<span class="bn">ফ্রন্ট অফিস বিভাগ</span>', CONT, "continuity")
fix(L, '<span class="hi">ऑपरेशंस विभाग</span>', '<span class="hi">फ्रंट ऑफिस विभाग</span>', CONT, "continuity")
fix(L, '<em>Operations handles scheduling and logistics.</em>', '<em>Front Office handles check-ins, check-outs and guest requests.</em>', CONT, "continuity")
fix(L, 'contrasted briefly with self-introduction ("I\'m Arif") from L01.', 'contrasted briefly with self-introduction ("I\'m Arif") from Module 1.',
    "Internal code replaced.", "reference")
fix(L, '<div>NOTICE THIS: Saying', '<div>Saying', "The label 'Notice this' was printed twice.", "structure")
fix(L, '<div class="matching-list"><div class="matching-row"><span class="matching-left"></span><span class="matching-blank">________</span></div><div class="matching-row"><span class="matching-left"></span><span class="matching-blank">________</span></div><div class="matching-row"><span class="matching-left"></span><span class="matching-blank">________</span></div></div>',
    '<div class="matching-list">'
    '<div class="matching-row"><span class="matching-left">(1) Your supervisor introduces you to the whole team at once.</span><span class="matching-blank">________</span></div>'
    '<div class="matching-row"><span class="matching-left">(2) A second colleague introduces herself, right after the first.</span><span class="matching-blank">________</span></div>'
    '<div class="matching-row"><span class="matching-left">(3) You meet someone you already met downstairs this morning.</span><span class="matching-blank">________</span></div>'
    '</div><p>Responses: (a) "Good to see you again." (b) "Hi everyone, nice to meet you all." (c) "Great to meet you, Priyanka."</p>',
    "The matching exercise had no items to match — the situations and responses were missing.", "answer-key")
fix(L, '<p>→; →; → </p>',
    '<p>(1) → (b) "Hi everyone, nice to meet you all." (2) → (c) "Great to meet you, Priyanka." (3) → (a) "Good to see you again."</p>',
    "The answer key was empty ('→; →; →').", "answer-key")
fix(L, '<span class="answer-number">2.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">2.</span> <p>Sample: 2nd introduction — "Great to meet you, Priyanka." 3rd introduction — "Good to meet you, Faisal. Thanks for the welcome." Any natural variation is correct, as long as it is not the same sentence repeated and it uses the person\'s name.</p>',
    "Unfinished model answer replaced with a sample.", "production")

# ---------- 2.3 Receiving Instructions and Understanding Routines ----------
L = "CE-L01-M02-L03"
fix(L, "At his new desk, Arif's computer is still starting up when", "At the back-office computer, Arif's login screen is still loading when",
    CONT, "continuity")
fix(L, '<p>Sequencing language: first... then..., and then..., before... — used naturally, not as a grammar drill, to structure multi-step instructions. Conditional instructions ("if... just..."): "If anything looks off, just flag it" — a first light exposure to a real-world conditional pattern (full conditional grammar comes at higher levels; here it\'s a fixed useful pattern, not a rule). See GIC-0001 for the structured card.</p>\n<p><strong>Structured Grammar-in-Context card(s):</strong> <code>GIC-0001</code> — see.</p>\n<p><strong>Sentence pattern(s) taught:</strong> <code>PAT-0002</code>, <code>PAT-0003</code> — see.</p>\n<p><strong>Communication formula:</strong> <code>CF-0001</code> — see.</p>',
    '<p><strong><code>GIC-0001</code> Sequencing and simple conditions in instructions</strong></p>'
    '<ul><li><strong>Sequence words</strong> put steps in order: <em>first</em> … <em>then</em> … <em>and then</em> … <em>before lunch</em>. "Check email first, then there\'s a quick huddle at 9:30."</li>'
    '<li><strong>"If" + present simple</strong> gives a condition: "If anything looks off, just flag it." Use the present simple after <em>if</em>, even though it is about the future: "If I <em>see</em> anything, I\'ll message you" (not "if I will see").</li></ul>'
    '<p><strong>Sentence patterns:</strong> <code>PAT-0002</code> "So, [first step] first, and then [second step] — [deadline]." <code>PAT-0003</code> "I\'ll + action + if + condition (present simple)."</p>'
    '<p><strong>Communication formula <code>CF-0001</code>:</strong> Listen → Restate → Clarify. Catch the action and deadline, say them back, and ask about the one part that is unclear.</p>',
    "The grammar card, patterns and formula were only referenced ('— see.'), never shown; their content is now given in place, and production language removed.",
    "reference")
fix(L, 'Stress on key content words in Line 01:', 'Stress on key content words in Mr. Hossain\'s first line:', "Internal script reference ('Line 01').", "production")
fix(L, '<td>Received, not produced, by the learner here</td>', '<td>You will usually hear this, not say it</td>', "Production language.", "production")
fix(L, '<h2>Production notes</h2>\n<p>Dual audio track: a natural-speed FULL track plus a slowed FULL-SLOW scaffold track, both referencing the same LINE0X transcript (Chapter 3 Part N.3\'s production-template refinement) — this is the one lesson in the module with a slowed variant.</p>\n',
    '', "Internal audio-production notes printed in the lesson.", "production")
fix(L, "Listen to Ms. Rahman's instruction. What are the two tasks, and what is the deadline?",
    "Read Mr. Hossain's instruction again. What are the two tasks, and what is the deadline?", "No audio recording exists yet.", "audio")
fix(L, '<p>Put the steps of the morning routine in the correct order.</p></div><div class="matching-list"><div class="matching-row"><span class="matching-left"></span><span class="matching-blank">________</span></div><div class="matching-row"><span class="matching-left"></span><span class="matching-blank">________</span></div></div>',
    '<p>Put the steps of the morning routine in the correct order: (a) the team huddle at 9:30 (b) checking email</p></div><div class="matching-list"><div class="matching-row"><span class="matching-left">First:</span><span class="matching-blank">________</span></div><div class="matching-row"><span class="matching-left">Then:</span><span class="matching-blank">________</span></div></div>',
    "The ordering exercise had no steps to order.", "answer-key")
fix(L, '<p>→; → </p>', '<p>First: (b) check email. Then: (a) the team huddle at 9:30.</p>', "The answer key was empty ('→; →').", "answer-key")
fix(L, '<p>Listen to a new 2-part instruction, restate it, then ask one clarifying question about the unclear part.</p>',
    '<p>A partner reads you this instruction: "Can you print the client list, and then pop a copy in the tray for the night team before you go?" Restate it, then ask one clarifying question about the unclear part.</p>',
    "The task asked learners to respond to an instruction that was not provided (and to listen to audio that does not exist).", "audio")
fix(L, '<span class="answer-number">1.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">1.</span> <p>Tasks: (1) set up his email signature, (2) go through the client list Priyanka sends. Deadline: before lunch.</p>',
    "The key gave no answer to a question with a single correct answer.", "answer-key")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Sample: "So, print the client list first, and then put a copy in the tray for the night team before I go. Just to check — which tray do you mean? The one at the front desk, or the one in the back office?"</p>',
    "Unfinished model answer replaced with a sample.", "production")
fix(L, '<p>"I\'ll + action + if + condition" (present tense in the if-clause) — this is PAT-0003, practiced with the exact sentence Arif uses in the dialogue.</p>',
    '<p>"I\'ll <strong>message</strong> you directly if I <strong>see</strong> anything unusual." Use the present simple after <em>if</em> (PAT-0003).</p>',
    "The answer key described the pattern but never gave the completed sentence.", "answer-key")

# ---------- 2.4 Finding Your Way and Asking Where Things Are ----------
L = "CE-L01-M02-L04"
fix(L, 'Open floor, near Priya\'s desk.', 'The back office, near Priyanka\'s desk.', CONT, "continuity")
fix(L, '(undermines the learner unnecessarily)', '(undermines the speaker unnecessarily)', "Meta reference to 'the learner' inside a model-language example.", "production")
fix(L, 'taught through the dialogue and the floor-plan activity, not as a standalone list.',
    'shown in the dialogue and in the directions list below.', "The floor-plan activity it referred to does not exist in the book.", "production")
fix(L, '<p><strong>Sentence pattern(s) taught:</strong> <code>PAT-0004</code>, <code>PAT-0005</code> — see.</p>',
    '<p><strong>Sentence patterns:</strong> <code>PAT-0004</code> "Could you tell me where + [place] + is?" (statement word order after "where": "where the washroom <em>is</em>", not "where <em>is</em> the washroom"). <code>PAT-0005</code> "Go straight down…, and it\'s on your left/right, (just) past/before…"</p>',
    "Broken '— see.' reference replaced with the patterns, including the word-order point that makes embedded questions difficult.", "reference")
fix(L, '<h2>Bengali support</h2>\n<p>None beyond vocabulary glossing — this lesson is close to universal and low-risk for direct-translation errors.</p>\n<h2>Hindi support</h2>\n<p>None beyond vocabulary glossing, for the same reason.</p>\n',
    '<h2>Bengali/Hindi support</h2>\n<p>Bengali and Hindi keep the normal question order inside a longer question, so learners often say "Could you tell me where <em>is</em> the washroom?" In English, the inner question uses statement order: "Could you tell me where the washroom <em>is</em>?" (বাংলা: "ওয়াশরুম কোথায়?" → English: "where the washroom is"; हिंदी: "वॉशरूम कहाँ है?" → "where the washroom is".)</p>\n',
    "The sections said no support was needed; embedded-question word order is a real and common difficulty for these learners.",
    "l1-support", source="Cambridge Grammar of English, indirect/embedded questions")
fix(L, '<h2>Interactive floor-plan activity</h2>\n<p>interactive floor-plan (Section H.2 Type H — Interactive Visual). On-screen instruction: <em>"Tap a location to hear directions from Arif\'s desk."</em></p>\n<p>Hotspots: Reception, Desk, Printer, Washroom, Break Room</p>\n<p><strong>Print fallback:</strong> Static labeled diagram (5 numbered locations) plus a printed direction list in PAT-0005\'s exact wording, e.g. "5. Break room — go straight down the hallway, and it\'s on your right, past the printer."</p>',
    '<h2>Directions from Arif\'s desk</h2>\n<ol>'
    '<li><strong>Front desk</strong> — go back through the door behind you, and it\'s straight ahead.</li>'
    '<li><strong>Mr. Hossain\'s office</strong> — go down the hallway, and it\'s the first door on your right.</li>'
    '<li><strong>Printer</strong> — go straight down the hallway, and it\'s on your left, just before the washroom.</li>'
    '<li><strong>Washroom</strong> — go straight down the hallway, and it\'s on your left, just past the printer.</li>'
    '<li><strong>Break room</strong> — go straight down the hallway, and it\'s on your right, past the printer.</li>'
    '</ol>',
    "The section described an interactive floor plan and a print fallback that were never produced (production specification text). Replaced with the directions list the activity was meant to use (PAT-0005 wording).",
    "production")
fix(L, '<p>Listen to the directions. Where is the washroom?</p>', '<p>Read Priyanka\'s directions in the dialogue again. Where is the washroom?</p>',
    "No audio recording exists yet.", "audio")
fix(L, '<span class="exercise-type">Floor Plan Interaction</span></div><div class="exercise-prompt"><p>Tap the hotspot for the location described in the audio.</p>',
    '<span class="exercise-type">Reading Directions</span></div><div class="exercise-prompt"><p>Use the "Directions from Arif\'s desk" list. Which place is described? (a) "Go down the hallway, and it\'s the first door on your right." (b) "Go straight down the hallway, and it\'s on your right, past the printer."</p>',
    "The exercise depended on an interactive hotspot and audio that do not exist.", "audio")
fix(L, '<span class="answer-number">2.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">2.</span> <p><strong>where</strong> — "Sorry to bother you, but could you tell me where the printer is?" (Statement order: "where the printer is".)</p>',
    "The key gave no answer to a fill-in item with one correct answer.", "answer-key")
fix(L, '<span class="answer-number">3.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">3.</span> <p>(a) Mr. Hossain\'s office. (b) The break room.</p>', "Answer added for the rewritten exercise.", "answer-key")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Sample: "Sorry to bother you — could you tell me where the break room is?" … "Down the hallway, on the right, past the printer — got it. Thank you so much." Check: one softener, the embedded question in statement order, the directions repeated back, a thank-you.</p>',
    "Unfinished model answer replaced with a sample and checklist.", "production")
fix(L, '<span class="answer-number">5.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">5.</span> <p>"Go straight down the hallway, and it\'s on your right, past the printer."</p>',
    "The key gave no answer although the directions list fixes the answer.", "answer-key")

# ---------- 2.5 Ending Your First Day Professionally ----------
L = "CE-L01-M02-L05"
fix(L, "Arif's screen is still open, but the office is starting to quiet down.", "Arif's screen is still open, but the back office is starting to quiet down.",
    CONT, "continuity")
fix(L, 'stops by his desk on her way out.', 'stops by his desk on his way out.', CONT, "continuity")
fix(L, 'Directly recycles/mirrors L01\'s arrival greeting — a deliberate symmetry', 'Mirrors the arrival greeting from Lesson 2.1',
    "Production language and internal code.", "production")
fix(L, 'No new vocabulary items in this lesson — a deliberate design choice, consistent with the Chapter 2 map\'s synthesis-lesson pattern (this lesson consolidates Module 2\'s language rather than introducing more).',
    'There is no new vocabulary in this lesson: it brings together the language of Module 2.', "Production language ('Chapter 2 map').", "production")
fix(L, '<p><strong>Sentence pattern(s) taught:</strong> <code>PAT-0006</code> — see.</p>\n<p><strong>Tone ladder:</strong> <code>TL-0001</code> — see.</p>',
    '<p><strong>Sentence pattern <code>PAT-0006</code>:</strong> "Have a good + [evening / weekend / day off]."</p>\n'
    '<p><strong>Tone ladder <code>TL-0001</code>: Leaving at the end of the day</strong></p>\n<ul>'
    '<li>❌ Too casual: (leaving without a word) / "Bye."</li>'
    '<li>Basic: "See you."</li>'
    '<li>Better: "See you tomorrow!"</li>'
    '<li>✅ Professional (taught rung): "Thanks — have a good evening. See you tomorrow at 9."</li>'
    '<li>❌ Too formal: "I shall now take my leave. I wish you a pleasant evening."</li></ul>',
    "The pattern and tone ladder were only referenced ('— see.'), never shown; their content is now given in place.", "reference")
fix(L, '<h2>Bengali support</h2>\n<p>None needed — this lesson deliberately avoids new translation load, closing the module the way it closes the day: simply.</p>\n<h2>Hindi support</h2>\n<p>None needed, for the same reason.</p>\n',
    '', "Empty support sections that only said no support was needed; removed.", "production")
fix(L, '<span class="answer-number">2.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">2.</span> <p>At 9 o\'clock (9 AM) — "Same time tomorrow, 9 o\'clock?" "Perfect, I\'ll see you at 9."</p>',
    "The key gave no answer to a question with a single correct answer.", "answer-key")
fix(L, '<span class="answer-number">3.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">3.</span> <p><strong>evening</strong> — "Great. Have a good evening, Arif."</p>', "The key gave no answer to a fill-in item.", "answer-key")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Sample: "Really good, thank you — a lot to take in, but I enjoyed it." … "Perfect, I\'ll see you at 9." … "Thanks, you too. See you tomorrow!" … "Thanks, Priyanka — see you tomorrow." Check: an honest, positive comment; the next-day time confirmed; a goodbye to each person.</p>',
    "Unfinished model answer replaced with a sample and checklist.", "production")

# ---------- names, applied last so the fixes above match the original text ----------
rule("L1M02-supervisor-name", r"Ms\. Rahman", "Mr. Hossain", CONT, "continuity", targets=M02)
rule("L1M02-priya-to-priyanka", r"\bPriya\b", "Priyanka", CONT, "continuity", targets=M02)
