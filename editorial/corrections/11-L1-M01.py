# Level 1 · Module 1 · Starting Work
QA = "QA review of the reference PDF"

# ---------- 1.1 Understanding What "Professional" Means at Work ----------
L = "CE-L01-M01-L01"
fix(L, '<span class="dialogue-speaker">Chowdhury:</span>', '<span class="dialogue-speaker">Sadia:</span>',
    "Speaker label used her surname while she introduces herself as Sadia and the exercises call her Sadia.",
    "continuity", count=4)
fix(L, 'Mixing the two up is <code>MIS-0002</code>.',
    'Using one form when you mean the other is <code>MIS-0002</code>.',
    "Aligns with the corrected MIS-0002 explanation (the issue is unclear meaning, not a forbidden sentence).", "grammar")
fix(L, '-- no dedicated Grammar-in-Context card for this lesson; the pattern is light enough to model directly inside the dialogue and practice.',
    '. You will see it throughout the dialogue and the practice.',
    "Internal production note about curriculum cards.", "production")
fix(L, '<div class="callout-wrong">❌ I want to become professional.</div><div class="callout-right">✅ I want to become more professional. / I want to become a professional in this field.</div><div class="callout-why">"Professional" works as an adjective (more professional, be professional) or as a noun with an article (a professional). Dropping the article or the comparative leaves the sentence ambiguous about which sense is meant.</div>',
    '<div class="callout-wrong">⚠️ Unclear: I want to become professional.</div>'
    '<div class="callout-right">✅ About behaviour: I want to become more professional. / I want to be more professional at work.<br>'
    '✅ About a person with skills or training: I want to become a professional in this field.</div>'
    '<div class="callout-why">"I want to become professional" is not ungrammatical, but at work it is unclear. '
    '<em>Professional</em> is an <strong>adjective</strong> when it describes behaviour (<em>be professional</em>, <em>more professional</em>) '
    'and a countable <strong>noun</strong> when it means a trained, skilled person (<em>a professional</em>). '
    'With the adjective, "more professional" sounds natural because professional behaviour is a matter of degree; '
    'with the noun, you need the article "a". (In sport and the arts, "become / turn professional" has a third meaning: '
    'to start being paid for it.) Choose the form that matches what you mean.</div>',
    "The original marked the sentence as simply wrong. It is grammatical; the real problem is ambiguity between the adjective and noun meanings.",
    "grammar", source=QA + " p.14; Cambridge Dictionary, 'professional' (adjective, noun)")
fix(L, 'Word stress: proFESsional, PUNCtual, resPECTful (stress falls on the second syllable in all three).',
    'Word stress: proFESsional and resPECTful are stressed on the second syllable; PUNCtual is stressed on the first.',
    "'Punctual' is stressed on the first syllable (/ˈpʌŋk.tʃu.əl/), so the claim that all three have second-syllable stress was wrong.",
    "pronunciation", source=QA + " p.14; Cambridge Dictionary pronunciation")
fix(L, 'Listen to the dialogue. What three things does Sadia say',
    'Read the dialogue again (or listen to a partner or teacher read it aloud). What three things does Sadia say',
    "No audio recording exists yet; the instruction now works without one.", "audio")
fix(L, '<p>The lesson\'s three core actions are punctuality, listening, and respect.</p>',
    '<p><strong>respectful</strong> — "Being professional means being on time, listening carefully, and being respectful." The blank needs an adjective after "being", parallel to the lesson\'s three actions (punctuality, listening, respect).</p>',
    "The answer key gave the noun 'respect' (and a summary) rather than the required word 'respectful'.",
    "answer-key", source=QA + " pp.16–17")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>Answers will vary. Sample answer: "For me, being professional means being on time and ready to work, listening carefully when someone explains something, and speaking to everyone with respect. It also means keeping my promises, even small ones." A good answer names concrete actions, not just "being good at the job".</p>',
    "Unfinished model answer replaced with a sample answer and success criteria.", "production")

# ---------- 1.2 Talking About Your Background and Experience ----------
L = "CE-L01-M01-L02"
fix(L, '<p><strong><code>GIC-0002</code></strong> -- past simple vs. present perfect for describing background. See for the full card: what finished ("I studied...") versus still-relevant-now ("I\'ve been interested in...") looks like, with Bengali/Hindi support notes.</p>',
    '<p><strong><code>GIC-0002</code> Past simple vs. present perfect for describing your background</strong></p>'
    '<ul>'
    '<li><strong>Past simple</strong> for a finished event at a finished time, especially when you say or imply <em>when</em>: "I <em>studied</em> hospitality management." "I <em>worked</em> at a small hotel for a year (and then left)."</li>'
    '<li><strong>Present perfect</strong> connects the past to now. Use it for a situation that started in the past and continues now, usually with <em>for</em> or <em>since</em>: "I\'<em>ve been</em> interested in this field since college." Also use it for experience at an unstated time that is relevant now: "I\'<em>ve handled</em> difficult guests before."</li>'
    '<li>Do not use the present perfect with a finished time expression: "I worked there <em>in 2023</em>", not "I have worked there in 2023".</li>'
    '</ul>',
    "The 'See for the full card' reference pointed to a card that is not in the book; the card's content is now given in place.",
    "reference", source="Cambridge Grammar of English §§ present perfect / past simple")
fix(L, '"I\'ve + past participle + for/since..." -- see.</p>',
    '"I\'ve + past participle + for/since..." — for example, "I\'ve worked in retail for two years."</p>',
    "Broken cross-reference ('-- see.') replaced with an example of the pattern.", "reference")
fix(L, 'Word stress: backGROUND, exPERience,', 'Word stress: BACKground, exPERience,',
    "'Background' is stressed on the first syllable (/ˈbæk.ɡraʊnd/).", "pronunciation", source=QA + " p.20; Cambridge Dictionary")
fix(L, 'True or false: present perfect is only used for actions that happened yesterday.',
    'True or false: present perfect can describe something that started in the past and is still true now.',
    "The original item tested a claim no learner would make; the new item checks the lesson's actual point.", "language")
fix(L, 'Listen to the dialogue. What did Arif study,', 'Read the dialogue again. What did Arif study,',
    "No audio recording exists yet.", "audio")
fix(L, '<p>Since pairs with a starting point in time (since college); for would need a duration instead (for four years).</p>',
    '<p><strong>since</strong> — "I\'ve been interested in this field since college." <em>Since</em> pairs with a starting point (since college); <em>for</em> would need a duration instead (for four years).</p>',
    "The answer key explained the rule but never gave the answer.", "answer-key")
fix(L, '<p>Since needs a starting point, not a duration; and a continuing action needs present perfect (continuous), not simple present.</p>',
    '<p>"I <strong>have been working</strong> in customer service <strong>for</strong> three years." (Also correct: "I have worked in customer service for three years.") A duration needs <em>for</em>, not <em>since</em>, and a situation that continues up to now needs the present perfect (continuous), not the present simple.</p>',
    "The answer key explained the rule but never gave the corrected sentence.", "answer-key")
fix(L, '<span class="answer-number">5.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">5.</span> <p>Answers will vary. Sample answer: "I studied business administration, and after that I worked in a supermarket for two years. I\'ve been interested in customer service since then. I\'ve handled a lot of busy weekend shifts, so I\'m used to working under pressure." Check: past simple for finished facts, at least one present perfect sentence with <em>for</em> or <em>since</em>, 3–4 sentences.</p>',
    "Unfinished model answer replaced with a sample answer and checklist.", "production")

# ---------- 1.3 Introducing Yourself Professionally ----------
L = "CE-L01-M01-L03"
fix(L, 'No new grammar structure this lesson -- L03 recombines L01\'s professional-register language and L02\'s background phrasing (past simple / present perfect) into a fixed introduction sequence, rather than teaching something new.',
    'There is no new grammar in this lesson. It combines the professional language of Lesson 1.1 and the background phrasing of Lesson 1.2 (past simple / present perfect) into one introduction sequence.',
    "Internal lesson codes (L01, L02, L03) replaced with the book's lesson numbers.", "reference")
fix(L, '<td>The person you take instructions from and give updates to</td>',
    '<td>To have someone as your direct boss: you take instructions from them and give them updates</td>',
    "The definition described a person, but the entry is a verb phrase.", "language")
fix(L, 'Word stress: TEAM, dePARTment, rePORT (verb, second syllable stressed).',
    'Word stress: dePARTment, rePORT (second syllable, for both the verb and the noun).',
    "'Team' has one syllable, so it has no stress pattern to learn; 'report' is stressed on the second syllable as a noun too, not only as a verb.",
    "pronunciation", source="Cambridge Dictionary")
fix(L, '<p>There isn\'t a separate Bengali grammar point in this lesson -- it\'s about switching <em>register</em>, not tense or structure. The formula stays the same in both languages; what shifts is politeness markers (e.g. addressing someone respectfully) rather than sentence structure.</p>',
    '<p>In Bengali, respect is shown partly through the pronoun: আপনি for a senior person, তুমি for a peer. English has only one "you", so the register shift has to come from other places: the greeting ("Good morning" rather than "Hi"), full forms ("my name is" rather than "I\'m"), and a slightly slower pace. The content of the introduction stays the same.</p>',
    "Replaced a note saying there was nothing to note with a specific, accurate contrast that explains where English carries formality.",
    "l1-support")
fix(L, '<p>Same principle in Hindi -- the content of an introduction doesn\'t change between a peer and a senior person, but respectful address and a slightly more measured pace signal the formality shift, just as in English.</p>',
    '<p>Hindi marks respect with आप (formal) versus तुम (informal). English "you" is the same for everyone, so a learner cannot rely on the pronoun: the greeting, full forms and pace carry the formality instead. Do not add "sir" or "ma\'am" to every sentence to make up for it; one respectful greeting is enough.</p>',
    "Made the Hindi note specific and accurate (आप/तुम versus the single English 'you').", "l1-support")
fix(L, 'Listen to both scenes. What team does Arif say he will be part of?',
    'Read both scenes again. What team does Arif say he will be part of?', "No audio recording exists yet.", "audio")
fix(L, '<p>A clear 3-part structure -- name, background/role, closing line -- is more professional and memorable than a long, unfocused one (MIS-0004).</p>',
    '<p>Model answer: "Hi, I\'m Arif. I studied hospitality management and worked at a small hotel for about a year. I\'m looking forward to being part of the team." Keep one sentence for each part (name, background/role, closing line) and remove hesitations and side stories (MIS-0004).</p>',
    "The answer key restated the principle but gave no rewritten introduction.", "answer-key")
fix(L, '<span class="answer-number">5.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">5.</span> <p>Answers will vary. Peer version: "Hi, I\'m Nadia. I studied accounting, and I\'ll be part of the finance team. Really looking forward to working with you all." Manager version: "Good morning, my name is Nadia. I studied accounting and worked at an audit firm for two years. I\'m looking forward to contributing to the department." Check: all three parts in each version, a clear change of register, under 30 seconds.</p>',
    "Unfinished model answer replaced with sample answers and a checklist.", "production")

# ---------- 1.4 Talking About Your Job Role and Responsibilities ----------
L = "CE-L01-M01-L04"
fix(L, 'this isn\'t your background story (that\'s past simple/present perfect, from L02)',
    'this isn\'t your background story (that\'s past simple / present perfect, from Lesson 1.2)',
    "Internal lesson code replaced with the lesson number.", "reference")
fix(L, '<td>The part of the job that\'s yours to handle</td>',
    '<td>Having the duty to do or look after something as part of your job</td>',
    "The definition described a noun ('responsibility'), but the entry is the adjective phrase 'responsible for'.", "language")
fix(L, 'both introduced in L03.)', 'both introduced in Lesson 1.3.)', "Internal lesson code replaced with the lesson number.", "reference")
fix(L, '<p><strong><code>GIC-0003</code></strong> -- present simple for ongoing role facts vs. L02\'s past simple/present perfect for background. See for the full card.</p>',
    '<p><strong><code>GIC-0003</code> Present simple for your role now</strong></p>'
    '<ul>'
    '<li>Use the <strong>present simple</strong> for facts about your job that are true now and generally: "I <em>report</em> to the front-office supervisor." "I <em>work</em> closely with housekeeping."</li>'
    '<li>Use the past simple / present perfect (Lesson 1.2) for your <em>history</em>: "I <em>worked</em> at a small hotel." "I\'<em>ve handled</em> complaints before."</li>'
    '<li>Use the present continuous only for something temporary or happening around now: "This week I\'<em>m shadowing</em> the night manager."</li>'
    '</ul>',
    "The 'See for the full card' reference pointed to a card that is not in the book; the card's content is now given in place.",
    "reference", source="Cambridge Grammar of English, present simple / present progressive")
fix(L, '"I\'m responsible for + gerund" -- see.</p>',
    '"I\'m responsible for + gerund/noun" — for example, "I\'m responsible for managing check-ins."</p>',
    "Broken cross-reference ('-- see.') replaced with an example of the pattern.", "reference")
fix(L, 'Word stress: colLEAGUE, superVISor, MANager, TEAM lead.',
    'Word stress: COLleague, SUpervisor, MANager, TEAM lead.',
    "'Colleague' (/ˈkɒl.iːɡ/) and 'supervisor' (/ˈsuː.pə.vaɪ.zər/) are stressed on the first syllable.",
    "pronunciation", source="Cambridge Dictionary")
fix(L, '"Responsible for" often contracts slightly in speech to sound like "responsible-fer" before a gerund -- natural, not sloppy.',
    'In "responsible for", the word "for" is usually unstressed and weak (/fə/), so it sounds like "responsible-fer". This is natural, not careless.',
    "'Contracts' was the wrong term; this is the weak form of 'for'.", "pronunciation")
fix(L, 'by habit from describing their history a moment earlier (as in L02)',
    'by habit from describing their history a moment earlier (as in Lesson 1.2)', "Internal lesson code replaced.", "reference")
fix(L, 'Listen to the dialogue. Who does Arif say he works closely with?',
    'Read the dialogue again. Who does Arif say he works closely with?', "No audio recording exists yet.", "audio")
fix(L, '<p>Ongoing role facts use present simple, not past tense.</p>',
    '<p><strong>report</strong> — "I report to the front-office supervisor." Ongoing role facts use the present simple.</p>',
    "The answer key explained the rule but never gave the answer.", "answer-key")
fix(L, '<p>Responsible for takes a gerund (training), not a to-infinitive (to train).</p>',
    '<p>"I am responsible <strong>for training</strong> new staff." <em>Responsible for</em> takes a gerund (training), not a to-infinitive (to train).</p>',
    "The answer key explained the rule but never gave the corrected sentence.", "answer-key")
fix(L, '<span class="answer-number">5.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">5.</span> <p>Answers will vary. Sample answer: "I\'m a teller at a bank branch. I\'m responsible for processing customer deposits and withdrawals. I report to the branch manager, and I work closely with the customer-service desk." Check: a "responsible for + -ing/noun" sentence, who you report to, who you work with, all in the present simple.</p>',
    "Unfinished model answer replaced with a sample answer and checklist.", "production")

# ---------- 1.5 Building Basic Workplace Confidence ----------
L = "CE-L01-M01-L05"
fix(L, 'the same HR colleague who called Arif before any of this began (L01)',
    'the same HR colleague who called Arif before any of this began (Lesson 1.1)', "Internal lesson code replaced.", "reference")
fix(L, 'giving your role and responsibilities (L04) their own step instead of folding them into Background alongside your history (L02), into one flowing 30-45 second turn.',
    'giving your role and responsibilities (Lesson 1.4) their own step instead of folding them into Background alongside your history (Lesson 1.2). The result is one flowing turn of 30–45 seconds.',
    "Internal lesson codes replaced; the run-on sentence split.", "reference")
fix(L, 'This is a MODEL MONOLOGUE (single speaker, Arif), not a two-person dialogue, per Chapter 2\'s own design for this synthesis lesson.',
    'This is a model monologue: one speaker, Arif, talking to the group.',
    "Production language ('per Chapter 2's own design').", "production")
fix(L, "It's only been my first day of orientation, but everyone's already been really welcoming.",
    "Today was only my first day of orientation, but everyone's already been really welcoming.",
    "'It's only been my first day' is unnatural; 'today was only my first day' is what a speaker would say.", "language")
fix(L, 'And I\'m really looking forward to being part of the team.',
    'And I\'m really glad to be part of the team.',
    "Two consecutive sentences used 'looking forward to'; the second now varies the closing line.", "language")
fix(L, 'This lesson recycles every key expression from L01-L04 rather than introducing new ones. The model monologue below shows them combined into one continuous turn -- see the individual lesson pages for each expression\'s original context.',
    'This lesson reuses the key expressions from Lessons 1.1–1.4 rather than introducing new ones. The model monologue above shows them combined into one continuous turn.',
    "Internal lesson codes replaced; 'below' corrected to 'above' (the monologue appears earlier on the page).", "reference")
fix(L, 'No new vocabulary this lesson. This is a deliberate synthesis lesson (Chapter 2 Part C) that consolidates <code>V-0007</code>..<code>V-0021</code> (background, role, and reporting-line vocabulary from L02-L04) into one turn, instead of introducing anything new. L01\'s professionalism vocabulary (<code>V-0001</code>..<code>V-0006</code>) underlies the whole module but isn\'t specific language recycled in this particular monologue.',
    'There is no new vocabulary in this lesson. It brings together the background, role and reporting-line vocabulary from Lessons 1.2–1.4 (<code>V-0007</code> to <code>V-0021</code>) in one turn.',
    "Production language ('Chapter 2 Part C') and internal codes removed.", "production")
fix(L, '"The Self-Introduction Formula"', '"The 3-Part Self-Introduction"',
    "The formula had two different names; it now uses the name given where it is introduced (Lesson 1.3).", "reference")
fix(L, '<h2>Bengali support</h2>\n<p>None needed beyond what L01-L04 already cover -- this is a pure synthesis/production lesson (Chapter 2\nPart C).</p>\n<h2>Hindi support</h2>\n<p>None needed beyond what L01-L04 already cover, for the same reason.</p>\n',
    '',
    "Empty support sections that only said no support was needed, with production references; removed.", "production")
fix(L, 'comes from which role and background facts the learner substitutes in, using their own real or target\njob (see L01-L04\'s industry overlays for hotel/healthcare/banking/IT/retail phrasing).',
    'comes from the role and background facts you put in from your own real or target job (see the industry overlays in Lessons 1.1–1.4 for hotel, healthcare, banking, IT and retail phrasing).',
    "Internal lesson codes replaced; addressed to the reader.", "reference")
fix(L, '<p>Read (or listen to) Arif\'s combined self-introduction below. Notice how Open → Background → Role → Close\nflows as one continuous turn, and where the natural pauses fall.</p>\n<p><em>(See the dialogue above for the full line-by-line script with audio references.)</em></p>',
    '<p>Read Arif\'s combined self-introduction (the Listen &amp; Read script above) aloud. Notice how Open → Background → Role → Close flows as one continuous turn, and where the natural pauses fall.</p>',
    "The note said 'below' for text above, and referred to audio references that do not exist.", "audio")
fix(L, 'This is Module 1\'s capstone speaking\nassessment (Chapter 2 Part B).', 'This is Module 1\'s final speaking task.',
    "Production reference ('Chapter 2 Part B') removed.", "production")
fix(L, 'Listen to the model monologue. Which part comes first -- Background or Role?',
    'Read the model monologue again. Which part comes first: Background or Role?', "No audio recording exists yet.", "audio")
fix(L, 'This is Module 1\'s capstone speaking assessment.', 'This is Module 1\'s final speaking task.',
    "Consistent naming with the self-check (the level capstones are separate).", "assessment")
fix(L, '<span class="answer-number">3.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">3.</span> <p>Answers will vary. Sample: "Hi everyone, I\'m Rina. I studied nursing and I\'ve worked at a community clinic for two years. I\'ll be part of the patient-services team. I\'m responsible for scheduling appointments. I report to the ward manager. I\'m looking forward to working with you all."</p>',
    "Unfinished model answer replaced with a sample.", "production")
fix(L, '<span class="answer-number">4.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">4.</span> <p>This is a personal rating, so there is no single answer. If you gave yourself 1 or 2 for any point, practise that part again: for pacing, add the three pauses from the Pronunciation section; for completeness, check that all four parts are there.</p>',
    "Unfinished model answer replaced with guidance for a self-assessment.", "production")
fix(L, '<span class="answer-number">5.</span> <p>Open-ended -- check against the lesson\'s model language.</p>',
    '<span class="answer-number">5.</span> <p>Answers will vary. A strong recording: (1) includes all four parts (Open, Background, Role, Close); (2) uses the past simple for finished history and the present simple for the current role; (3) lasts 60–90 seconds with natural pauses; (4) is spoken, not read.</p>',
    "Unfinished model answer replaced with scoring criteria.", "production")

# ---------- cast continuity (see AUDIT-PROGRESS.md) ----------
fix("CE-L01-M01-L02", 'Hasan, a colleague from another team', 'Hasan, a front-office colleague he hasn\'t met yet',
    "Hasan is Arif's front-office teammate in Lesson 1.3 and in every later level; 'another team' / 'Operations' contradicted that.",
    "continuity", count=2)
fix("CE-L01-M01-L02", "I'm Hasan, from the Operations team.", "I'm Hasan, from the front-office team.",
    "Hasan is Arif's front-office teammate in every later lesson.", "continuity")
rule("L1-1.4-accounts-colleague", r"\bPriyanka\b", "Nusrat",
     "Lesson 1.4 needs a colleague from another department, but Priyanka is Arif's front-office peer everywhere else in the book "
     "(she asks him to cover the front desk in 7.3 and works shifts with him in Levels 2–5). The Accounts colleague is renamed Nusrat.",
     "continuity", targets=["CE-L01-M01-L04"])
