# PDF proof, batch 2: Level 2 (PDF pp. 176–347).
SRC = "PDF proof, batch 2 · editorial review"

# --- Lesson 1.3: hotel size ---
rule("proof-L2-1.3-rooms", r"all forty-two rooms", "all 120 rooms",
     "The recount said the hotel has forty-two rooms, but Level 3–4 groups book 45 rooms and Level 5 describes a 120-room property.",
     "continuity", fields=("body_html",), targets=["CE-L02-M01-L03"], expect=2, source=SRC)

# --- Module assessments without a score ---
fix("CE-L02-M01-L04", "using present\nperfect for done and present continuous for doing. The written version compresses the same content into 2\nlines without losing the done/doing/blocked information, avoiding MIS-0040's unsorted rambling.",
    "using present perfect for done and present continuous for doing. The written version compresses the same content into 2 lines without losing the done/doing/blocked information, avoiding MIS-0040's unsorted rambling. Score 0–4, one point each: all three parts in order; under 30 seconds; present perfect for done and present continuous for doing; a two-line chat version that keeps all three parts. Pass at 3.",
    "The Module 1 assessment had no score.", "assessment", source=SRC)
fix("CE-L02-M02-L05", "The response states a concrete achievable scope or timing and offers a specific\nalternative, avoiding a vague objection (MIS-0045).",
    "The response states a concrete achievable scope or timing and offers a specific alternative, avoiding a vague objection (MIS-0045). Score 0–3: (1) the request is acknowledged; (2) a concrete achievable scope or time is named with \"realistically\" / \"what's achievable is\"; (3) a specific alternative or phased plan is offered. Pass at 2 on each part of the assessment.",
    "Part A of the Module 2 assessment had no score.", "assessment", source=SRC)

# --- Lesson 3.1 ---
fix("CE-L02-M03-L01", "Good morning, Riverside Clinic reception,", "Good morning, Green Valley Clinic reception,",
    "Riverside is the name of Arif's hotel; the sample for the learner's own workplace now uses a different name.", "continuity", source=SRC)

# --- Lesson 4.4 ---
fix("CE-L02-M04-L04", "Name the four channel options this lesson covers, and when each one fits.",
    "Name the five options this lesson covers (whole group, thread, DM, @mention, pinning), and when each one fits.",
    "The lesson covers five options, not four.", "factual", source=SRC)

# --- Lesson 7.1 ---
L = "CE-L02-M07-L01"
fix(L, "Welcome to [Hotel Name]! How can I help you today?", "Welcome to Riverside Hotel! How can I help you today?",
    "A template slot ('[Hotel Name]') was printed in an example.", "production", source=SRC)
fix(L, "Hi, thanks for reaching out! How can I help you today?</span></div>\n<div class=\"dialogue-turn\"><span class=\"dialogue-speaker\">Chat guest:</span>",
    "Hi, thanks for reaching out! I can check that for you.</span></div>\n<div class=\"dialogue-turn\"><span class=\"dialogue-speaker\">Chat guest:</span>",
    "The guest had already asked a question, so a generic 'How can I help you today?' was the recited-script mismatch the lesson warns against (MIS-0066).",
    "language", source=SRC)

# --- Lesson 7.2: Level 1 Lesson 4.4 was with a supervisor ---
L = "CE-L02-M07-L02"
SUP = "In Level 1 Lesson 4.4 Arif asked his supervisor, Mr. Hossain, to clarify — not a colleague."
fix(L, "(the reverse of Level 1 Lesson 4.4, where Arif asked a colleague to clarify a request)",
    "(the reverse of Level 1 Lesson 4.4, where Arif asked his supervisor to clarify a request)", SUP, "reference", source=SRC)
fix(L, "there, Arif asked a\ncolleague to clarify an unclear request;", "there, Arif asked his supervisor to clarify an unclear request;", SUP, "reference", source=SRC)

# --- Lesson 8.4 ---
fix("CE-L02-M08-L04", "Priyanka, You're right", "Priyanka, you're right", "Capital letter after a comma.", "typography", source=SRC)

# --- Capstone ---
L = "CE-L02-CAPSTONE"
fix(L, "this is Golam from Bengal Linen Supply", "this is Golam from Delta Linens",
    "A third linen supplier ('Bengal Linen Supply') was easily confused with Level 4's Bengal Textile Supplies; Golam now works for Delta Linens, the supplier already introduced in Lesson 3.2.",
    "continuity", source=SRC)
fix(L, "my appointment's earlier than I\nthought. Forty minutes is plenty.", "my appointment's shorter than I thought. Forty minutes is plenty.",
    "'Earlier than I thought' does not explain why forty minutes is enough; 'shorter' does.", "language", source=SRC)
