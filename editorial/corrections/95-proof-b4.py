# PDF proof, batch 4: Level 4 (PDF pp. 615–860).
SRC = "PDF proof, batch 4 · editorial review"
AUTO = "PDF proof, batch 4 · automated check"

# --- Typography ---
rule("proof-pm", r"(\d) p\.m\.", r"\1 PM", "The book writes clock times as '4:40 PM'; a few places used 'p.m.'.",
     "typography", fields=("body_html", "practice_html"), source=SRC)
rule("proof-am", r"(\d) a\.m\.", r"\1 AM", "The book writes clock times as '9:00 AM'; a few places used 'a.m.'.",
     "typography", fields=("body_html", "practice_html"), source=SRC)
rule("proof-parts-range", r"Parts A-C", "Parts A–C", "Letter ranges take an en dash.", "typography",
     fields=("body_html",), targets=["CE-L04-ASSESSMENT", "CE-L05-ASSESSMENT"], expect=2, source=SRC)
rule("proof-pass-mark", r"25 of 36 \(70%\)", "25 of 36 (about 70%)",
     "25 of 36 is 69.4%, so the percentage is approximate.", "assessment",
     fields=("body_html",), targets=["CE-L04-ASSESSMENT", "CE-L05-ASSESSMENT"], expect=2, source=SRC)

# --- Module 1: Negotiation ---
fix("CE-L04-M01-L01", "Walk-away point: no lower than a set minimum hourly rate.", "Walk-away point: no lower than 1,500 taka an hour.",
    "The answer key asks for a 'specific, measurable walk-away point', but the sample gave none.", "answer-key", source=SRC)
fix("CE-L04-M01-L02", "A 3% adjustment doesn't come close to covering our cost increase on our end.",
    "A 3% adjustment doesn't come close to covering our cost increase.",
    "'Our … on our end' was redundant.", "language", source=SRC)
L = "CE-L04-M01-L04"
NOREV = "The must-haves set in Lesson 1.1 are the delivery window and the replacement policy; 'no review clause' is what Arif asked for in return for the 8% in Lesson 1.3."
fix(L, "and Arif's must-haves say no\nreview clause.", "and a fixed rate with no review clause is exactly what Arif asked for in return for the 8%.",
    NOREV, "continuity", source=SRC)
fix(L, "Arif's must-haves rule it out.", "Arif asked for no review clause in exchange for the 8%.", NOREV, "continuity", source=SRC)
fix("CE-L04-M01-L05", "The role-play moves cleanly through all four stages without skipping any,",
    "The role-play moves cleanly through all five stages without skipping any,",
    "The score above lists five stages.", "assessment", source=SRC)

# --- Module 2: Difficult conversations ---
fix("CE-L04-M02-L01", "on a suite he's kept two nights past his original reservation,",
    "on a suite he's kept one night past his original reservation,",
    "In the dialogue Mr. Talukder says 'it's one night'.", "continuity", source=SRC)
fix("CE-L04-M02-L06", "draws on at least two of the module's five prior skills appropriately",
    "draws on at least two of the module's four skills named in the task appropriately",
    "The assessment task lists four skills (firm refusal, feedback, receiving criticism, pattern-naming).", "assessment", source=SRC)

# --- Module 3: Persuasion ---
L = "CE-L04-M03-L03"
fix(L, "That changes things. If your team isn't the one carrying the extra work,",
    "That changes things. If my team isn't the one carrying the extra work,",
    "Ms. Noor is talking about her own team.", "language", source=SRC)
fix(L, "Your team's only involvement is one one-hour walkthrough before it goes live.",
    "Your team's only involvement is a single one-hour walkthrough before it goes live.",
    "'One one-hour' read as a typing error; the worked example says 'a single one-hour walkthrough'.", "language", source=AUTO)

# --- Module 4: Problem-solving (Mina covers afternoons Tuesday to Friday) ---
HALF = "Mina covers the afternoon shift Tuesday to Friday, so housekeeping loses her for half of each day, not for 'half a day'."
rule("proof-L4-4.2-halfday", r"loses someone for half a day, not the\s+whole week\.", "loses someone for half of each day, not the whole day.",
     HALF, "continuity", fields=("body_html",), targets=["CE-L04-M04-L02"], expect=2, source=SRC)
rule("proof-L4-4.3-halfday", r"housekeeping only loses someone for half a day\.", "housekeeping only loses someone for half of each day.",
     HALF, "continuity", fields=("body_html",), targets=["CE-L04-M04-L03"], expect=2, source=SRC)
fix("CE-L04-M04-L03", "Mina's schedule shifts Tuesday-Friday next week only;", "Mina's schedule shifts Tuesday–Friday next week only;",
    "Day ranges take an en dash.", "typography", source=SRC)

# --- Module 7: Alex and Sam are referred to by name, not pronoun, throughout the module ---
fix("CE-L04-M07-L04", "as soon as he was asked privately", "as soon as Alex was asked privately",
    "Module 7 refers to Alex and Sam by name throughout; this was the one place Alex was given a pronoun.", "continuity", source=SRC)

# --- Module 8 ---
fix("CE-L04-M08-L05", "That works well for us. Let's do the three-year extension.", "That works well for us. Let's extend it to three years.",
    "'The three-year extension' read as three extra years; Arif proposed adding a third year.", "language", source=SRC)

# --- Capstone ---
L = "CE-L04-CAPSTONE"
rule("proof-L4-capstone-wedding", r"Ahsan-Karim", "Haider-Karim",
     "The Ahsan-Karim wedding block was already used for Module 4's March crisis week; the capstone's wedding is a different event.",
     "continuity", fields=("body_html",), targets=[L], expect=3, source=SRC)
fix(L, "Sam told us he'd have the overflow feature ready", "Sam told us the overflow feature would be ready",
    "Module 7 refers to Sam by name, not pronoun.", "continuity", source=SRC)
