# Level 1 · Module 4 · Understanding Instructions

# ---------- 4.1 Listening for Key Information ----------
L = "CE-L01-M04-L01"
fix(L, '<div class="dialogue-box">\n<div class="dialogue-box-label">Listen &amp; Read</div>\n<div class="dialogue-turns">\n</div>\n</div>\n',
    '', "An empty 'Listen & Read' box with no dialogue in it.", "structure")
fix(L, '<p><em>(In the full digital course, these play as short audio clips of increasing speed. Read each one\nbelow as if it were spoken quickly and naturally -- not slowed down for you.)</em></p>',
    '<p><em>(Audio for these clips is not available yet. Read each one quickly, as if it were spoken at a natural speed, or ask a partner or teacher to read them aloud to you, getting faster each time.)</em></p>',
    "The note referred to a digital course with audio that does not exist.", "audio")
fix(L, '<strong>Clip 1 (retail, easier pace):</strong>', '<strong>Clip A (retail, easier pace):</strong>',
    "The clips were numbered 1–3 here but lettered A–C in the exercises.", "structure")
fix(L, '<strong>Clip 2 (office, natural pace, two parts):</strong>', '<strong>Clip B (office, natural pace, two parts):</strong>',
    "The clips were numbered 1–3 here but lettered A–C in the exercises.", "structure")
fix(L, '<strong>Clip 3 (IT, fastest, two actions):</strong>', '<strong>Clip C (IT, fastest, two actions):</strong>',
    "The clips were numbered 1–3 here but lettered A–C in the exercises.", "structure")
fix(L, 'In Clip 2 above, what\'s the deadline?', 'In Clip B above, what\'s the deadline?', "Consistent clip lettering.", "structure")
fix(L, '<span class="bn">এবং কখনের মধ্যে করতে হবে</span>', '<span class="bn">এবং কোন সময়ের মধ্যে করতে হবে</span>',
    "'কখনের' is not a Bengali word; 'কোন সময়ের মধ্যে' (by what time) is the intended meaning.", "l1-support")
fix(L, 'Listen to (read) Clip C and note down', 'Read Clip C (or have a partner read it aloud) and note down', "No audio recording exists yet.", "audio")
fix(L, '<p>The deadline is given at the end of the sentence -- "before your shift ends."</p>',
    '<p>"Before your shift ends." Note that the deadline comes at the very end of the sentence.</p>', "Answer first, then the reason.", "answer-key")
fix(L, '<p>The instruction is "file these invoices, AND make sure the totals match" -- the second action (checking totals) is easy to lose if you stop listening after "file."</p>',
    '<p>Make sure the totals match the report (before sending it up). The second action is easy to lose if you stop listening after "file".</p>',
    "Answer first, then the reason.", "answer-key")

# ---------- 4.3 Understanding Priorities, Sequence and Deadlines ----------
L = "CE-L01-M04-L03"
fix(L, '<li>❌ <strong>Missed priority:</strong> doing the three tasks in the exact order they were mentioned, without noticing that the urgent one was actually listed second.</li>',
    '<li>❌ <strong>Missed priority:</strong> doing the three tasks in the exact order they were mentioned, without noticing that the urgent one was actually mentioned last.</li>',
    "In the dialogue the urgent client reply is mentioned last, not second.", "continuity")
fix(L, '"So the client reply is urgent -- I\'ll do that first, then the filing, then set up the room since that\'s not needed until this afternoon."',
    '"So the client reply is urgent — I\'ll do that first, then set up the room for this afternoon, and file the receipts whenever I get a chance after that."',
    "The ✅ example put the filing ('whenever you get a chance') before the room needed this afternoon, contradicting the dialogue and the lesson's priority rule.",
    "answer-key")
fix(L, '<p>The client reply is explicitly marked urgent, so it comes first, even though it was mentioned last in the instruction.</p>',
    '<p>1. Reply to the client (marked urgent, although it was mentioned last). 2. Set up the meeting room (needed this afternoon). 3. File yesterday\'s receipts ("whenever you get a chance").</p>',
    "The key explained the first task only; the exercise asks for all three in order.", "answer-key")

# ---------- 4.4 Saying When Something Is Unclear ----------
L = "CE-L01-M04-L04"
fix(L, 'because it only works well once you already know how to listen for key information (L01), confirm accurately (L02), and sort priority (L03).',
    'because it only works well once you already know how to listen for key information (Lesson 4.1), confirm accurately (Lesson 4.2), and sort priority (Lesson 4.3).',
    "Internal lesson codes replaced.", "reference")
fix(L, '<h2>Module 4 assessment</h2>\n<p>This lesson\'s final activity (A04) is the Module 4 capstone: a listening comprehension check\ncombined with a confirmation role-play, drawing on all four lessons -- catching the key\ninformation (L01), confirming it accurately (L02), sorting priority if more than one task is\ninvolved (L03), and flagging the one specific part that\'s genuinely unclear (L04).</p>',
    '<h2>Module 4 final task</h2>\n<p>Exercise 4 is the final task for Module 4. It combines all four lessons: catching the key information (Lesson 4.1), confirming it accurately (Lesson 4.2), sorting priority when there is more than one task (Lesson 4.3), and flagging the one part that is genuinely unclear (Lesson 4.4).</p>',
    "Internal codes (A04, L01–L04) replaced; 'capstone' is reserved for the level capstones.", "reference")
fix(L, 'Module 4 capstone. Listen to (read) an instruction with a task, a deadline, and one unfamiliar term. Confirm the parts you understood, flag the specific unclear term, and once it\'s explained, restate the full instruction back in priority order if more than one task is involved.',
    'Module 4 final task. A partner reads you this instruction: "Can you print the rooming list for the Rahman group and leave it at the front desk before 2? Oh, and reconcile the deposit sheet by end of day." Confirm the parts you understood, flag the unfamiliar term, and once your partner explains it ("check that the deposits on the sheet match the payments in the system"), restate both tasks in order.',
    "The assessment told learners to respond to an instruction that was never provided, and to listen to audio that does not exist.",
    "assessment")
fix(L, '<p>What to listen/look for: Demonstrates all four Module 4 skills in one exchange -- accurately confirms the clear parts of the instruction, names the specific unclear term rather than saying "I don\'t understand," and restates the full instruction correctly once clarified.</p>',
    '<p>Sample: "Got it — print the rooming list for the Rahman group and leave it at the front desk before 2. I\'m not sure I understood the last part, though — what exactly do you mean by \'reconcile the deposit sheet\'?" … "So, first the rooming list by 2, then I\'ll check the deposit sheet against the system by end of day." '
    'Scoring (1 point each): confirms the first task accurately; names the unclear term ("reconcile") instead of saying "I don\'t understand"; restates both tasks with their deadlines; keeps the order (2 PM before end of day). 4 = task complete; 3 = complete with one area to practise; 2 or fewer = review the lesson for the missed skill.</p>',
    "The key gave criteria only for an instruction that did not exist; it now has a sample answer and a scoring scale.", "assessment")
