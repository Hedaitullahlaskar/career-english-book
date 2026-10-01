# Level 3 · Module 7 · Professional Grammar in Context
# This module carries most of the grammar findings from the QA review of the
# reference PDF (pp. 470–488). Explanations are rewritten against the
# Cambridge Grammar of English (Carter & McCarthy) and Cambridge Dictionary.
CGE = "Cambridge Grammar of English (Carter & McCarthy)"
QA = "QA review of the reference PDF"
PH = "The answer key contained an unfilled template placeholder; replaced with a sample answer."
D = 16  # re.DOTALL

# =====================================================================
# 7.1 Tenses and Aspect for Professional Writing — present perfect
# =====================================================================
L = "CE-L03-M07-L01"
PP_REASON = ("The lesson reduced the present perfect to 'finished versus still going on'. The present perfect very often describes "
             "completed actions (\"I've sent the invoice\"); what decides the tense is whether the time is finished and stated "
             "(past simple) or the action is connected to now — a present result, an unstated time, or a period up to now (present perfect).")

fix(L, 'his tenses keep sliding between "this already\nhappened and is finished" and "this is still going on right now."',
    'his tenses keep sliding between "this happened at a finished time in the past" and "this is connected to now."',
    PP_REASON, "grammar", source=QA + " pp.470–474")

rule("L3-7.1-key-lesson", r"(<h2>Key Workplace Lesson</h2>\s*).*?(?=<div class=\"dialogue-box\">)",
     r"""\1<p>Professional writing almost always needs to answer one quiet question for the reader: is this part of a finished past, or is it connected to now? English answers that with two forms, and mixing them up is one of the most common accuracy problems in workplace writing: the <strong>past simple</strong> and the <strong>present perfect</strong>.</p>
<p>The <strong>past simple</strong> (<em>we completed, I sent, the team finished</em>) places an action in a finished time: it happened then, and that time is over — usually with a time expression that says or implies when (<em>yesterday, on Monday, last week, in Q2</em>).</p>
<p>The <strong>present perfect</strong> (<em>we have completed, I have sent, the team has finished</em>) connects the past to now. It is <em>not</em> only for things that are still going on — it is very often used for actions that are complete:</p>
<ul>
<li>a completed action whose result matters now: "I've sent the invoice" (so it's done — you don't need to chase me);</li>
<li>an action at an unstated time up to now: "We've completed three audits this year";</li>
<li>a situation or series that continues up to now: "We've completed 60% of the follow-up items so far."</li>
</ul>
<p>So the key question is not "finished or unfinished?" but "finished <em>time</em>, or connected to now?" The two forms aren't interchangeable, and a careful reader notices when they're swapped.</p>
""",
     PP_REASON, "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

fix(L, 'And the follow-up items are still ongoing right now, so that part needs present perfect. Try it again.',
    'And the 60% is a result up to now — "so far", the work isn\'t finished — so that part needs present perfect. Try it again.',
    PP_REASON, "grammar", source=QA + " pp.470–474")
fix(L, 'both already introduced in Level 1 (L1-M1-L02), to full professional writing',
    'both already introduced in Level 1 (Lesson 1.2), to full professional writing', "Internal lesson code replaced.", "reference")

rule("L3-7.1-gic-bullets", r"(<h2>Grammar in Context: Present Perfect vs\. Simple Past in Status Writing \(GIC-0007\)</h2>\s*<p><strong>Structure:</strong></p>\s*)<ul>.*?</blockquote>",
     r"""\1<ul>
<li>Use the <strong>past simple</strong> for an action at a finished, stated (or clearly understood) time: a date, a day, "last week", "yesterday", "in Q2". Never combine the present perfect with these expressions.</li>
<li>Use the <strong>present perfect</strong> when the action is connected to now: a completed action whose result matters now ("I've sent the invoice"), an action at an unstated time up to now ("We've completed three audits this year"), or a situation that continues up to now (with <em>so far, since, for, yet, already</em>). This is why a report's opening summary — where things stand <em>as of today</em> — often uses it.</li>
<li>In American English the past simple is also common with <em>just, already</em> and <em>yet</em> ("I already sent it"); in a formal report, the present perfect is the safer choice.</li>
</ul>
<blockquote>
<p><strong>Formula:</strong> <em>[finished, stated time]</em> → past simple. <em>[connected to now: present result / unstated time / up to now]</em> → have/has + past participle.</p>
</blockquote>""",
     PP_REASON, "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

fix(L, '"So far" signals an unfinished, ongoing situation, so it needs present perfect',
    '"So far" connects the result to now, so it needs present perfect',
    PP_REASON, "grammar")

rule("L3-7.1-mis", r"(<h2>Common Mistake \(MIS-0119\)</h2>\s*).*?(?=<h2>)",
     r"""\1<p><strong>Mistake:</strong> Using the present perfect with a finished-time expression (<em>have finished … last Tuesday</em>), or using the past simple with an expression that runs up to now (<em>since then, so far</em>).</p>
<p>❌ "We have completed the client handover last week, and since then the new team used the system every day."</p>
<p>✅ "We completed the client handover last week, and since then the new team has used the system every day."</p>
<p><strong>Why it matters:</strong> A reader uses your tense choice to place events in time: closed and dated, or connected to now. A mismatch makes the timeline harder to follow — and "have completed … last week" is simply ungrammatical in standard English.</p>
""",
     "The original wrong example also marked a correct clause ('the new team started using the system') as an error; the new pair shows two genuine errors.",
     "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

rule("L3-7.1-l1-note", r"(<h2>Professional Tone</h2>\s*<blockquote>\s*<p>)Bengali/Hindi note:.*?(</p>\s*</blockquote>)",
     r"""\1Bengali/Hindi note: Bengali and Hindi both have perfect forms (করেছি, किया है), but they combine freely with a finished time: "আমি গতকাল পাঠিয়েছি" and "मैंने कल भेज दिया है" are natural. Translated directly, they give "I have sent it yesterday", which is wrong in English. Before writing a report sentence, ask: is there a finished time in this sentence (yesterday, last week, on Monday)? If yes, use the past simple.\2""",
     "The note said the L1s simply don't distinguish the two; the precise transfer problem is that Bengali and Hindi perfect forms combine with finished-time words.",
     "l1-support", fields=("body_html",), flags=D, targets=[L], expect=1)

fix(L, '<p>Suggested answer: "Have completed" is wrong because it\'s paired with "last week," a specific finished time, which needs simple past ("completed"). "Started" should instead be present perfect ("has been using"), since the new team\'s use of the system is still ongoing.</p>',
    '<p>Only "have completed" is wrong: it is paired with "last week", a finished time, so it needs the past simple — "We completed the client handover last week." "The new team started using the system" is correct: starting is a single past event. (If you want to stress that they are still using it, you could add "and has used it every day since", but that is an addition, not a correction.)</p>',
    "The key marked a correct past simple ('started') as an error.", "answer-key", source=QA + " pp.470–474")
fix(L, '<p>Suggested answer: "I sent the invoice yesterday, but the client has not confirmed receipt yet."</p>',
    '<p>"I sent the invoice yesterday, but the client has not confirmed receipt yet." (Also note "didn\'t confirmed" → after <em>did/didn\'t</em> the verb is the base form; in American English "the client didn\'t confirm receipt yet" is also common.)</p>',
    "Added the second error in the sentence and the American English variant.", "answer-key")
fix(L, '<p>Suggested answer: "[open response -- one simple-past sentence with a specific time marker, one present-perfect sentence describing an unfinished or unspecified-time result]"</p>',
    '<p>Sample: "We restocked the minibars on Monday." / "We have restocked 40 of the 60 minibars so far." Check: the past simple sentence has a finished time; the present perfect sentence has no finished time and is connected to now.</p>',
    PH, "production")

# =====================================================================
# 7.2 Modals and Conditionals
# =====================================================================
L = "CE-L03-M07-L02"
rule("L3-7.2-struggle-to-succeed", r"could struggle(?: to succeed)?", "could fail",
     "'Could struggle to succeed' is an unnatural, redundant phrase; 'could fail unless…' is the natural hedge of 'will fail'.",
     "language", fields=("body_html", "practice_html"), targets=[L], expect=7)
fix(L, '<p>Suggested answer: "[open response -- one sentence combining a modal softener with a conditional naming a specific, changeable condition]"</p>',
    '<p>Sample: "We may miss the Friday deadline unless the new linen supplier confirms delivery by Wednesday." Check: a modal (<em>may/might/could</em>) instead of <em>will</em>, and a specific condition with <em>if</em> or <em>unless</em>.</p>',
    PH, "production")

# =====================================================================
# 7.3 Passive Voice and Reported Speech
# =====================================================================
L = "CE-L03-M07-L03"
PASSIVE = ("Changing 'Hasan delayed the shipment' to 'The shipment was delayed due to a supplier issue' changes the facts (it names a different cause), "
           "not only the voice. The passive of the sentence is 'The shipment was delayed (by Hasan)'; a cause may be added only if it has been confirmed.")
BACKSHIFT = ("Backshift is not compulsory: when the reported situation is still true or still in the future, keeping the original tense is "
             "correct ('Dr. Rahman said he needs the numbers by Friday', said on Wednesday). What must change are references that no longer fit, "
             "such as 'tomorrow' reported days later.")

rule("L3-7.3-key-lesson", r"(<h2>Key Workplace Lesson</h2>\s*).*?(?=<div class=\"dialogue-box\">)",
     r"""\1<p><strong>Passive voice</strong> — putting the thing affected first, and leaving out or moving the person who acted — isn't weak or evasive writing. In a report, it is often the more professional choice, because it keeps the focus on the event and its impact, especially before responsibility has been established. "Hasan delayed the shipment" names a person, which in an incident report can read as an accusation; "The shipment was delayed" reports the same event without naming anyone.</p>
<p>Notice what the passive does <em>not</em> do: it doesn't change the facts. "The shipment was delayed due to a supplier issue" is not the passive of "Hasan delayed the shipment" — it states a different cause. Only add a cause you have confirmed.</p>
<p><strong>Reported speech</strong> solves a different problem: summarizing what someone said, in writing, after the fact. With a past reporting verb (<em>said, told, mentioned</em>), the tense often moves one step back (a "backshift"): "I need it" → "he said he needed it". The backshift is not compulsory: if what was said is still true or still in the future, you can keep the original tense ("he said he needs it by Friday"). But time words and pronouns must always fit the moment you are writing.</p>
""",
     PASSIVE + " " + BACKSHIFT, "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

fix(L, '<span class="dialogue-text">"The shipment was delayed due to a supplier issue." And when Dr. Rahman called about it',
    '<span class="dialogue-text">"The shipment was delayed by two days." I\'ll add the cause once it\'s confirmed. And when Dr. Rahman called about it',
    PASSIVE, "grammar", source=QA + " pp.479–480")

rule("L3-7.3-gic-passive", r"(<h2>Grammar in Context: Passive Voice for Objective Reporting \(GIC-0010\)</h2>\s*).*?(?=<h2>Grammar in Context: Reported Speech)",
     r"""\1<p><strong>Structure:</strong> [Thing affected] + <em>was/were</em> + [past participle] (+ <em>by</em> + agent, only if the agent genuinely matters).</p>
<p><strong>Worked example:</strong></p>
<p>Active: "Hasan delayed the shipment." → Passive: "The shipment was delayed." (or "…was delayed by Hasan" if the person matters)</p>
<p>The facts stay the same; only the focus changes. If you know the cause, add it as a separate, checkable fact: "The shipment was delayed because the customs paperwork arrived late."</p>
<p>Use passive voice when the event or its result is what the reader needs to know, and naming who did it either isn't relevant yet or isn't the point of the report. Use active voice when the person genuinely matters — for example, when recommending who should fix it.</p>
""",
     PASSIVE, "grammar", fields=("body_html",), flags=D, targets=[L], expect=1, )

rule("L3-7.3-gic-reported", r"(<h2>Grammar in Context: Reported Speech Tense Shifts \(GIC-0011\)</h2>\s*).*?(?=<h2>Common Mistake \(MIS-0121\)</h2>)",
     r"""\1<p><strong>Structure:</strong> [Reporting verb: said / told / mentioned] + (that) + [subject] + [verb — usually backshifted one step].</p>
<p><strong>Worked example:</strong></p>
<p>Direct speech (Monday): Dr. Rahman said, "I need the numbers by Friday."</p>
<p>Reported on Wednesday: "Dr. Rahman said (that) he needed / needs the numbers by Friday." Both are correct: Friday is still ahead, so the present tense is also possible.</p>
<p>Reported the following week: "Dr. Rahman said that he needed the numbers by that Friday." The deadline has passed, so the backshift is needed.</p>
<p><strong>Common backshifts:</strong> need → needed, will → would, can → could, is/are → was/were, have/has → had. <strong>Time words:</strong> today → that day, tomorrow → the next day, yesterday → the day before.</p>
""",
     BACKSHIFT, "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

rule("L3-7.3-mis", r"(<h2>Common Mistake \(MIS-0121\)</h2>\s*).*?(?=<h2>)",
     r"""\1<p><strong>Mistake:</strong> Copying the original speaker's time words into a report written later, so they now point to the wrong day.</p>
<p>❌ (Written on Friday, about something Priyanka said on Monday) "Priyanka said she can finish the draft tomorrow."</p>
<p>✅ "Priyanka said (on Monday) that she could finish the draft the next day."</p>
<p><strong>Why it matters:</strong> "Tomorrow" in a report written on Friday means Saturday — the reader gets the wrong date. Backshift the tense when the situation is over, and always update time words to fit the moment you are writing. (If you are reporting on the same day, "She said she can finish it tomorrow" is perfectly correct.)</p>
""",
     "The original MIS-0121 marked a correct sentence ('He said he needs the numbers by Friday', with Friday still ahead) as wrong. " + BACKSHIFT,
     "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)

fix(L, 'reported speech first touched in L2-M2-L04)', 'reported speech first touched in Level 2, Lesson 2.4)', "Internal lesson code replaced.", "reference")
fix(L, 'Compare "Hasan delayed the shipment" with "The shipment was delayed due to a supplier issue." Using GIC-0010,',
    'Compare "Hasan delayed the shipment" with "The shipment was delayed." Using GIC-0010,',
    PASSIVE, "grammar")
fix(L, '<p>Suggested answer: The passive version ("The shipment was delayed...") is more appropriate, because it reports the event and its cause without naming a person before the facts are confirmed, keeping the report objective rather than accusatory.</p>',
    '<p>The passive version ("The shipment was delayed.") is more appropriate for an objective incident report, because it reports the same event without naming a person before responsibility is confirmed. It does not change the facts — if the cause is known, add it as a separate, checkable statement.</p>',
    PASSIVE, "grammar")
fix(L, '<p>Suggested answer: "Priyanka said that she could finish the draft by the next day."</p>',
    '<p>"Priyanka said (that) she could finish the draft by the next day." (If you are writing on the same day she said it, "Priyanka said she can finish the draft by tomorrow" is also correct.)</p>',
    BACKSHIFT, "grammar")
fix(L, '<p>Suggested answer: "[open response -- one passive-voice sentence focused on an event, one reported-speech sentence with a correctly backshifted verb]"</p>',
    '<p>Sample: "Two room keys were reported missing at 6 PM." / "Rupa said that housekeeping would check the lost-property log." Check: the passive keeps the facts of the active sentence; the reported verb and any time words fit the moment of writing.</p>',
    PH, "production")

# =====================================================================
# 7.4 Articles, Prepositions, and Subject-Verb Agreement
# =====================================================================
L = "CE-L03-M07-L04"
rule("L3-7.4-prepositions", r"(<h2>Grammar in Context: Fixed Preposition Pairings \(GIC-0013\)</h2>\s*).*?(?=<h2>Grammar in Context: Subject-Verb)",
     r"""\1<p><strong>Structure:</strong> Some pairings are fixed — learn them as one unit: <em>responsible for, depend on, consist of, comply with, apologize (to someone) for (something)</em>.</p>
<p>Others change with the meaning, so learn the meaning with the preposition:</p>
<ul>
<li><strong>arrive at</strong> a building or point (<em>arrive at the hotel, at the airport, at a decision</em>); <strong>arrive in</strong> a city or country (<em>arrive in Dhaka, in Delhi</em>). Never "arrive to".</li>
<li><strong>agree with</strong> a person or an opinion (<em>I agree with Ms. Noor</em>); <strong>agree on</strong> a decision or point you settle together (<em>we agreed on the launch date</em>); <strong>agree to</strong> a proposal or request, or + verb (<em>she agreed to the new rate; he agreed to help</em>).</li>
</ul>
<p>❌ "I'm responsible of the inventory." → ✅ "I'm responsible for the inventory."</p>
<p>❌ "The guests arrived to Dhaka at 6." → ✅ "The guests arrived in Dhaka at 6."</p>
""",
     "The lesson listed 'arrive at' and 'agree with' as fixed pairs; the preposition depends on meaning (arrive at/in; agree with/on/to).",
     "grammar", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, '"The list of complaints are increasing."', '"The list of complaints are growing."',
    "A list grows; it does not 'increase'.", "language")
fix(L, '"The list of complaints is increasing."', '"The list of complaints is growing."',
    "A list grows; it does not 'increase'.", "language")
fix(L, '<p><strong>Why it matters:</strong> This is one of the errors that sounds fine when spoken quickly,',
    '<p>Contrast: <em>a number of</em> means "several", so it takes a plural verb: "A number of guests <strong>have</strong> complained." <em>The number of</em> is singular: "The number of complaints <strong>has</strong> gone up."</p>\n<p><strong>Why it matters:</strong> This is one of the errors that sounds fine when spoken quickly,',
    "Added the contrast that learners need to apply the rule correctly.", "grammar", source=CGE)
fix(L, '(correct agreement -- "team" is singular)', '(correct agreement — "team" is singular; in British English "the team are" is also possible)',
    "Collective nouns can take a plural verb in British English.", "grammar", source=CGE)
fix(L, '<p>Suggested answer: "[open response -- three sentences, each correctly applying one of the lesson\'s three grammar points]"</p>',
    '<p>Sample: "The guest in 305 has paid the deposit." / "We agreed on a new check-in time with the tour group." / "Each of the new trainees has completed the fire-safety course." Check: the article fits something specific, the preposition fits the meaning, and the verb agrees with the true subject.</p>',
    PH, "production")

# =====================================================================
# 7.5 Relative Clauses, Gerunds, and Infinitives
# =====================================================================
L = "CE-L03-M07-L05"
rule("L3-7.5-relative-rule", r"<p>Use <em>who</em> for people,.*?</p>",
     r"""<p><strong>Two kinds of relative clause:</strong></p>
<ul>
<li><strong>Defining</strong> (no commas) — tells you <em>which</em> person or thing: "The guest <strong>who</strong> called this morning…", "The complaint <strong>that</strong> came in on Monday…". Use <em>who</em> (or <em>that</em>) for people and <em>that</em> or <em>which</em> for things; <em>that</em> is more common, especially in American English. When the pronoun is the object, you can leave it out: "the report (that) you sent".</li>
<li><strong>Non-defining</strong> (with commas) — adds extra information about something already identified: "Mr. Chen, <strong>who</strong> booked a river-view room, …", "Our new booking system, <strong>which</strong> went live in May, …". Use <em>who</em> or <em>which</em> — never <em>that</em>.</li>
</ul>
<p><em>Which</em> can also refer back to a whole idea: "The delivery was late, which upset the guest."</p>""",
     "The original rule ('which with a comma for things, that without a comma') was incomplete: which also introduces defining clauses, that can refer to people, the pronoun can be omitted, and that is never used in non-defining clauses.",
     "grammar", fields=("body_html",), flags=D, targets=[L], expect=1, )
fix(L, '<p>Suggested answer: "We suggest reviewing the contract before signing. The client sent an email that asked for a refund."</p>',
    '<p>"We suggest reviewing the contract before signing. The client sent an email that (or which) asked for a refund." (Even shorter: "…an email asking for a refund.")</p>',
    "Added the acceptable alternatives, consistent with the corrected rule.", "grammar")
fix(L, '<p>Suggested answer: "[open response -- one sentence with a correctly used relative clause, one sentence with a correctly matched gerund or infinitive after its verb]"</p>',
    '<p>Sample: "The guest who lost her passport has been given a temporary letter." / "We agreed to send the replacement key by courier." Check: the relative clause has the right pronoun and punctuation; the verb is followed by the correct form (agree + to-infinitive, avoid + -ing).</p>',
    PH, "production")

# =====================================================================
# 7.6 Comparatives and Formal Sentence Structures
# =====================================================================
L = "CE-L03-M07-L06"
COMP = ("A comparison must compare like with like: 'Q3 revenue was higher than Q2' compares revenue with a quarter. "
        "The lesson on comparatives itself contained this faulty comparison.")
rule("L3-7.6-faulty-comparison", r"higher than Q2", "higher than in Q2",
     COMP, "grammar", fields=("body_html",), targets=[L], expect=4)
rule("L3-7.6-superlative-hyphen", r"the highest revenue quarter this year", "our highest-revenue quarter this year",
     "Compound modifier before a noun takes a hyphen ('highest-revenue quarter').", "typography",
     fields=("body_html",), targets=[L], expect=2)
fix(L, 'as a synthesis lesson carrying the Module 7 assessment, it deliberately introduces no new terms,\nconsolidating the module\'s grammar points instead.',
    'it brings together the grammar points of the whole module instead.', "Production language ('synthesis lesson carrying the Module 7 assessment').", "production")
fix(L, '(L01-L05)', '(Lessons 7.1–7.5)', "Internal lesson codes replaced.", "reference")
fix(L, '<h2>Module 7 Assessment (Part of L06)</h2>', '<h2>Module 7 Assessment</h2>',
    "Internal code in the heading ('Part of L06').", "production")
fix(L, 'Score the correction on:', 'Score 0–6, one point for each area corrected correctly (pass at 5):',
    "The assessment listed scoring areas but gave no scale or pass mark.", "assessment", source=QA + " (assessments)")
fix(L, 'He said that he had needed it two days earlier.', 'Two days ago, he said that he needed it.',
    "The key changed the meaning: 'He said he had needed it two days earlier' puts the need two days before he spoke. The intended meaning is that he said it two days ago.",
    "answer-key", source=QA + " p.495")
fix(L, '<p>Suggested answer: "[open, reflective response naming one of the module\'s six grammar areas, followed by two correctly formed sentences using it]"</p>',
    '<p>Answers will vary. Sample (articles): "I find articles hardest. — I\'ve attached the report you asked for. A guest left a phone at the front desk." Check: one area named, two correct sentences that use it.</p>',
    PH, "production")
fix(L, 'and it was the fastest response\n time recorded this year."', 'and it recorded our fastest response time this year."',
    "'It was the fastest response time' made 'it' (the server) equal a response time.", "grammar")
