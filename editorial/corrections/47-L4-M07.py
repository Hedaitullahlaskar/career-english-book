# Level 4 · Module 7 · Cross-Cultural Workplace Communication
D = 16
SCALE7 = ("Score each part 0–4: respectfulness 0–2 (every adaptation is grounded in the individual, never a category) "
          "and specificity 0–2 (the actual, observable evidence behind each choice is named). Pass at 3 on each part.")

L = "CE-L04-M07-L01"
fix(L, "<li><strong>Low-context communication</strong> -- a style in which",
    "<li><strong>Low-context communication</strong> -- the other end of the same dimension: a style in which",
    "The heading promises four dimensions but lists five items; high- and low-context are the two ends of one dimension, and the text now says so.",
    "structure")
fix(L, "exactly like Alex's pause in\nthis lesson.", "exactly like the guest's pause at checkout in this lesson.",
    "Alex does not pause in this lesson; the pause belongs to the hotel guest in the checkout case.", "continuity")
fix(L, "using at least one of this lesson's four vocabulary terms.", "using at least one of this lesson's vocabulary terms.",
    "The lesson has five vocabulary terms, not four.", "factual")

L = "CE-L04-M07-L02"
fix(L, "He has two very different colleagues in mind for how to word\nit: one who responds well to a short, direct ask, and one who tends to need a softer, more\nformal approach.",
    "He knows two very different ways to word it: a short, direct ask, which some colleagues respond to well, and a softer, more formal approach, which others need.",
    "The sentence said Arif had 'two colleagues in mind' for wording one email to Jordan, which does not make sense.", "language")
fix(L, "Level 1 Module 7 already gave you a tone\nframework -- casual, polite, professional, diplomatic -- and Level 2 Module 2 gave you\nconditional-request language for softening an ask (\"if it's not too much trouble, would it be\npossible to...\").",
    "Level 1 Module 7 already gave you a tone framework — rude, casual, passive, professional, confident and respectful — and Level 2 Module 2 gave you conditional-request language for softening an ask (\"if you get a chance\", \"as long as it doesn't clash with...\").",
    "Wrong cross-references: Level 1 Module 7's tone labels are rude/casual/passive/professional/confident-and-respectful, and 'if it's not too much trouble' was taught there as an example of a passive request, not in Level 2 Module 2.",
    "reference")
fix(L, "<td>Conditional-request softening (recycled, Level 2 Module 2)</td>",
    "<td>Formal softening; keep a clear deadline with it, or it turns into the 'passive' request from Level 1 Module 7</td>",
    "The phrase is not from Level 2 Module 2; Level 1 Module 7 uses it as an example of an over-hedged request.", "reference")
fix(L, "an overdue confirmation, two days\nbefore the deadline.", "a confirmation that is still outstanding, two days before the deadline.",
    "'Overdue … two days before the deadline' contradicts itself.", "language")
fix(L, "\"\nclients like this one\"", "\"clients like this one\"", "Stray space inside the quotation marks.", "typography")
fix(L, "I humbly beseech the budget figures...", "I humbly beseech you to furnish the budget figures...",
    "'Beseech' takes a person as its object; even the deliberately bad example should be grammatical.", "grammar")
fix(L, "You are given a short profile of a colleague's typical email style (either short and direct, or warm and indirect).",
    "Choose one of these profiles. Profile A: replies in one or two lines, goes straight to dates and numbers, and says \"no\" plainly. Profile B: writes longer, warm emails that open with a personal greeting, and rarely refuses anything outright.",
    "The task said 'you are given a profile', but no profile was provided in the book.", "answer-key")
fix(L, "<p>What to listen/look for: The delivered message is calibrated",
    "<p>Score 0–4: calibration matches the chosen profile (0–2); the content and deadline stay identical and the cues are named out loud (0–2). Pass at 3. What to listen/look for: The delivered message is calibrated",
    "The speaking task had no scale.", "assessment")

L = "CE-L04-M07-L03"
rule("L4-7.3-log-dependency", r"flag that dependency to Ms\. Noor right now", "log that dependency in the meeting notes right now",
     "Ms. Noor is in the meeting, so Arif cannot sensibly promise to 'flag it to Ms. Noor' — he records it instead (matching MIS-0182's corrected notes).",
     "continuity", fields=("body_html",), targets=[L], expect=2)
fix(L, "\"Just to confirm -- there's a risk around [the specific thing named], so I'll flag that now rather than assume everything is fully on track.\"",
    "\"Just to confirm — the deadline depends on getting the supplier's figures by Tuesday, so I'll flag that now rather than assume everything is fully on track.\"",
    "The model answer contained an unfilled placeholder.", "production")

L = "CE-L04-M07-L04"
ALEX = ("Lesson 7.1 shows Alex giving a vague answer on the group call and a direct one only in a private message; Lesson 7.2 is about Jordan, not Alex. "
        "The description now matches what Alex has actually shown.")
fix(L, "Delivered to Alex (direct, low-context, based on Alex's own demonstrated style)",
    "Delivered to Alex (a direct private message, based on how Alex answered one-to-one in Lesson 1)", ALEX, "continuity")
fix(L, "(whose own emails and calls, across Lessons 1 and 2, have consistently been short,\ndirect, and low-context):",
    "(who, in Lesson 1, gave a vague answer on the group call but a short, direct, low-context reply as soon as he was asked privately):",
    ALEX, "continuity")
rule("L4-7.4-duplicate-exchange",
     r"(<p>After the meeting in Lesson 3, Hasan and Priyanka are talking about how the deadline conversation\s+with Sam went)\.</p>\s*<p><strong>Hasan \(the mistake\):</strong>.*?</p>\s*<p><strong>Priyanka \(the correction\):</strong>.*?</p>\s*",
     r"\1 (the last part of the dialogue above).</p>\n",
     "The Hasan/Priyanka exchange was printed twice in a row, word for word; the second copy is removed and the analysis now points to the dialogue.",
     "structure", fields=("body_html",), flags=D, targets=[L], expect=1)
rule("L4-7.4-assessment-scale", r"Both parts are scored on <strong>respectfulness</strong>.*?</p>",
     "Both parts are scored on <strong>respectfulness</strong> (grounding every adaptation in the individual, never a category) and <strong>specificity</strong> (naming the actual, observable evidence behind each choice). " + SCALE7 + "</p>",
     "The module assessment named two criteria but gave no scale or pass mark.", "assessment", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "a role-play in which the learner adapts one message", "a role-play in which you adapt one message", "Meta wording ('the learner').", "production")
fix(L, "You are given short style profiles for two colleagues based on their demonstrated communication patterns.",
    "Use these two profiles. Colleague A: replies within minutes, in one or two lines, and says plainly when something won't work. Colleague B: writes friendly, longer messages, agrees in group meetings, and raises concerns only when asked one-to-one.",
    "The task said 'you are given profiles', but no profiles were provided in the book.", "answer-key")
fix(L, "Scored on respectfulness (grounded in the individual) and specificity (named, concrete evidence).</p>",
    SCALE7 + "</p>", "The module assessment had no scale.", "assessment")
rule("L4-7.4-reflection-scale", r"Scored on respectfulness and specificity, alongside the module's role-play activity as the two halves of the Module 7 assessment\.?",
     SCALE7, "The module assessment had no scale.", "assessment", fields=("practice_html",), flags=D, targets=[L], expect=1)
