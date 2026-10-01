# Level 1 · Module 6 · Basic Workplace Vocabulary

rule("L1M06-remove-duplicated-dialogue",
     r"<h2>Modeled in context</h2>\s*<blockquote>.*?</blockquote>\s*", "",
     "Each lesson printed its Listen & Read dialogue a second time, word for word, under 'Modeled in context'.",
     "structure", flags=16, expect=5)  # 16 = re.DOTALL

# ---------- 6.1 People, Roles and Departments ----------
L = "CE-L01-M06-L01"
fix(L, '<code>Priyanka works in Accounts.</code>', '<code>Priyanka works on the front desk.</code>',
    "Priyanka is Arif's front-office peer throughout the book.", "continuity")
fix(L, 'specific staffed counter itself — you\'d say "leave it at the front desk," not usually "leave it\nat the reception." In many workplaces the words are used almost interchangeably, but front desk\nis the more precise choice when you mean the counter itself.</p>',
    'specific staffed counter itself. Both are correct, but they behave differently: <em>reception</em> is normally used <strong>without</strong> "the" after <em>at</em> ("Please wait at reception"), while <em>front desk</em> always takes "the" ("Leave it at the front desk"). "Leave it at the reception" is the mistake to avoid. In hotels, <em>front desk</em> is the usual name for the counter and for the team that works there.</p>',
    "The original implied that 'leave it at reception' was unusual. 'At reception' (no article) is standard; the real error is adding 'the'.",
    "grammar", source="Cambridge Dictionary, 'reception' (UK: at reception)")
fix(L, 'A colleague says: "Ask the reception if you need help with that." Rewrite this using the more precise word for the staffed counter itself, and explain the difference in one sentence.',
    'A colleague says: "Ask the reception if you need help with that." Correct the sentence in two ways: once with "reception" and once with "front desk".',
    "The exercise now tests the article point the corrected explanation teaches.", "answer-key")
fix(L, '<p>Suggested answer: Ask the front desk if you need help with that. ("Reception" is the general area/function; "front desk" is the specific staffed counter.)</p>',
    '<p>"Ask at reception if you need help with that." (no "the") / "Ask the front desk if you need help with that."</p>',
    "Aligned with the corrected explanation.", "answer-key")

# ---------- 6.2 Places, Tools and Documents at Work ----------
L = "CE-L01-M06-L02"
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Answers will vary. Check that the plan labels at least five places or objects with words from this lesson (for example: meeting room, storeroom, printer, notice board, front desk) and that each label is spelled correctly.</p>',
    "Unfinished model answer replaced with marking criteria.", "production")

# ---------- 6.3 Time, Schedules and Deadlines ----------
L = "CE-L01-M06-L03"
fix(L, '<td>Arriving or finishing exactly when expected, not early or late</td>', '<td>At the planned time; not late</td>',
    "'On time' means not late; arriving early is still on time, so 'not early' was wrong.", "language", source="Cambridge Dictionary, 'on time'")

# ---------- 6.5 Core Workplace Verbs and Professional Phrases ----------
L = "CE-L01-M06-L05"
fix(L, 'and escalate to the team lead if Accounts is still pending tomorrow.', 'and escalate to their team lead if Accounts still hasn\'t replied tomorrow.',
    "'Pending' describes a task, not a department ('if Accounts is still pending' is not natural English).", "language")
fix(L, '<td>Module 2 (informal use, "could you tell me")</td>', '<td>Module 2 ("Could you sign in here, please?")</td>',
    "The 'First used' column was vague; it now cites the first use.", "reference")
fix(L, '<td>Module 4/5 (implied throughout)</td>', '<td>Module 5 (Lesson 5.1: "I\'ll take care of both")</td>',
    "'Implied throughout' is not a first use; the phrase first appears in Lesson 5.1.", "reference")
fix(L, '<td>Module 5 (implied)</td>', '<td>New in this lesson</td>',
    "The phrase does not appear anywhere earlier in the book.", "reference")
fix(L, '<td>Module 4/6 (implied)</td>', '<td>Module 6 (this lesson\'s dialogue)</td>',
    "The phrase first appears in this lesson's dialogue.", "reference")
fix(L, '<td>"Got it."</td>\n<td>Module 4</td>', '<td>"Got it."</td>\n<td>Module 2 (Lesson 2.3)</td>',
    "'Got it' is first used in Lesson 2.3, not Module 4.", "reference")
fix(L, '<p><em>These phrases are not re-translated here — each was already glossed in the module where it\nfirst appeared, and repeating the translation would be redundant.</em></p>',
    '<p><em>These are short, fixed phrases: learn each one as a whole, rather than translating it word by word.</em></p>',
    "The note claimed every phrase had been translated earlier, which was not true.", "l1-support")

fix("CE-L01-M06-L03", "Listen to (read) this schedule announcement and answer:", "Read this schedule announcement (or have someone read it aloud) and answer:",
    "No audio exists for this announcement.", "audio")
