# PDF proof, batch 5: Level 5, Reference Index and back cover (PDF pp. 861–1104).
SRC = "PDF proof, batch 5 · editorial review"

# --- Typography ---
rule("proof-pm-compact", r"\b(\d{1,2})pm\b", r"\1 PM", "The book writes clock times as '5 PM'; a few places used '5pm'.",
     "typography", fields=("body_html", "practice_html"), source=SRC)
fix("CE-L05-M03-L01", "\"Offer them a late checkout at 2 PM\" (4)", "\"Offer them a late checkout at 2 PM.\" (4)",
    "The full stop was lost when '2 p.m.' became '2 PM' (batch 4); the other quoted items end with punctuation.", "typography", source=SRC)

# --- Module 1 ---
rule("proof-L5-1.2-column", r"comments column", "notes column",
     "The same column of the room-status report was called both the 'notes column' and the 'comments column'.",
     "continuity", fields=("body_html", "practice_html"), targets=["CE-L05-M01-L02"], expect=2, source=SRC)

# --- Module 4 ---
fix("CE-L05-M04-L01", "The parallel hotel/retail/IT contexts from the curriculum\nmap appear fully in Lesson 2's announcement.",
    "The parallel hotel, retail and IT contexts appear in Lesson 2's announcement.",
    "'The curriculum map' is an internal production document, not something the learner has.", "production", source=SRC)

# --- Module 5: internal production wording ---
fix("CE-L05-M05-L03", "No new pattern ID is minted for this lesson — it directly extends",
    "No new pattern is introduced in this lesson — it directly extends",
    "'Pattern ID is minted' is internal production wording.", "production", source=SRC)
fix("CE-L05-M05-L04", "No new pattern ID is\nminted — the addition is", "No new pattern is introduced — the addition is",
    "'Pattern ID is minted' is internal production wording.", "production", source=SRC)

# --- Module 7: a second Tanvir ---
rule("proof-L5-7.3-tanvir", r"\bTanvir\b", "Imran",
     "Tanvir is already Priyanka's colleague at Riverside (Level 4 Lesson 2.6); the front-office manager Arif meets at another hotel is now Imran Ahmed.",
     "continuity", fields=("body_html", "practice_html"), targets=["CE-L05-M07-L03"], expect=11, source=SRC)

# --- Module 8 ---
fix("CE-L05-M08-L03", "I'm extending the front-desk shift handover from next Monday,\nfrom fifteen to thirty minutes.",
    "I'm extending the front-desk shift handover from fifteen to thirty minutes, starting next Monday.",
    "'From next Monday, from fifteen to thirty' was awkward.", "language", source=SRC)
fix("CE-L05-M08-L04", "avoided deciding and said they'd \"circle back.\"", "avoided deciding and said he'd \"circle back.\"",
    "The subject is the first supervisor ('he'), not the team.", "grammar", source=SRC)

# --- Level 5 Assessment ---
fix("CE-L05-ASSESSMENT", "Levels 1 and 2 tested one module's skill at a time, in short, discrete items,",
    "Levels 1–3 tested one module's skill at a time, in short, discrete items,",
    "Level 3's assessment also tested one item per module (its Part A); Level 4's explains the same.", "factual", source=SRC)

# --- Capstone: US spelling ---
rule("proof-L5-capstone-program", r"([Pp])rogramme", r"\1rogram", "US spelling: 'program', as elsewhere in the book.",
     "language", fields=("body_html",), targets=["CE-L05-CAPSTONE"], source=SRC)
