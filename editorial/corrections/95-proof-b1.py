# PDF proof, batch 1: front matter and Level 1 (PDF pp. 1–175).
# Runs after the book-wide rules, so find strings use the final text (em dashes, US spelling).
SRC = "PDF proof, batch 1 · editorial review"
AUTO = "PDF proof, batch 1 · automated check"
D = 16

# --- Typography: number ranges take an en dash (the book already writes 0–4, 30–45) ---
rule("proof-number-ranges", r"(?<![\w:/.\-–])(\d{1,3})-(\d{1,3})(?![\w\-–])", r"\1–\2",
     "Number ranges were written with a hyphen in some places (2-3 sentences) and an en dash in others (0–4); ranges now use the en dash throughout.",
     "typography", fields=("objectives_html", "body_html", "practice_html"), source=SRC)
rule("proof-year-ranges", r"\b((?:19|20)\d\d)-((?:19|20)\d\d)\b", r"\1–\2",
     "Year ranges take an en dash.", "typography", fields=("body_html", "practice_html"), source=SRC)

# --- Objectives that called the learner "they" under the heading "What you'll learn" ---
OBJ = "The objectives sit under 'What you'll learn' but referred to the learner in the third person; they now address the reader."
fix("CE-L01-M01-L04", "State their job title and main responsibility clearly.", "State your job title and main responsibility clearly.", OBJ, "language", source=SRC)
fix("CE-L01-M01-L04", "who they report to and who they work with.", "who you report to and who you work with.", OBJ, "language", source=SRC)
fix("CE-L01-M01-L05", "Self-assess their own confidence level", "Self-assess your own confidence level", OBJ, "language", source=SRC)
fix("CE-L01-M02-L01", "Greet a receptionist and state their name and purpose on arrival.", "Greet a receptionist and state your name and purpose on arrival.",
    "Under 'What you'll learn', 'their name' read as the receptionist's name.", "language", source=SRC)
fix("CE-L01-M02-L03", "accurately in their own words.", "accurately in your own words.", OBJ, "language", source=SRC)
fix("CE-L01-M03-L01", "based on who they're speaking to.", "based on who you're speaking to.", OBJ, "language", source=SRC)
fix("CE-L01-M03-L01", "Recognize when a greeting they've heard", "Recognize when a greeting you've heard", OBJ, "language", source=SRC)
fix("CE-L01-M04-L04", "Avoid pretending to understand when they don't.", "Avoid pretending to understand when you don't.", OBJ, "language", source=SRC)
fix("CE-L01-M06-L01", "in a spoken sentence about their own or a target workplace.", "in a spoken sentence about your own or a target workplace.", OBJ, "language", source=SRC)

# --- Lesson 1.1 ---
fix("CE-L01-M01-L01", '"Being professional means being on time") .', '"Being professional means being on time").',
    "Stray space before the full stop.", "typography", source=AUTO)

# --- Lesson 1.5 ---
L = "CE-L01-M01-L05"
fix(L, "The result is one flowing turn of 30–45 seconds.", "The result is one flowing turn of about a minute.",
    "The lesson said the combined turn lasts 30–45 seconds, but the module task and its answer key ask for 60–90 seconds.", "factual", source=SRC)
fix(L, "both appear in the model monologue below,", "both appear in the model monologue above,",
    "The model monologue is in Listen & Read, above this section.", "reference", source=SRC)

# --- Lesson 2.1 ---
fix("CE-L01-M02-L01", "Thanks! I'll head up now.", "Thanks! I'll wait here for him, then.",
    "Arif said he would head upstairs, but the receptionist had called Mr. Hossain and then says he is on his way down.", "continuity", source=SRC)

# --- Lesson 2.3 ---
fix("CE-L01-M02-L03", "Let me walk you through how mornings usually work here,\" she says,", "Let me walk you through how mornings usually work here,\" he says,",
    "Mr. Hossain was referred to as 'she'.", "continuity", source=SRC)

# --- Lesson 3.1: Mr. Kabir is the same person as Level 4–5's Mr. Zahid Kabir, Head of Finance ---
L = "CE-L01-M03-L01"
KAB = "Mr. Kabir appears in Levels 4–5 as Mr. Zahid Kabir, Head of Finance; Level 1 now introduces him in that role instead of as an unnamed 'department director'."
rule("proof-L1-3.1-kabir", r"\b[Tt]he department director, Mr\. Kabir,", "Mr. Kabir, the Head of Finance,", KAB, "continuity",
     fields=("body_html",), targets=[L], expect=1, source=SRC)
rule("proof-L1-3.1-director", r"\bthe department director\b", "Mr. Kabir, the Head of Finance", KAB, "continuity",
     fields=("body_html",), targets=[L], source=SRC)
fix(L, "Match each greeting to the person it fits best.</p>",
    "Match each greeting to the person it fits best: (a) a senior director you barely know; (b) a peer you already know a little; (c) someone you don't know well, or aren't sure about.</p>",
    "The matching exercise listed the greetings but not the people to match them to.", "answer-key", source=SRC)

# --- Matching answer keys that ran into the explanation without a full stop ---
rule("proof-matching-fullstop", r"([a-z]) (Familiarity and seniority|Each department maps|Each phrase does|All five versions ask|Each response type has)",
     r"\1. \2", "The last match in the answer key ran straight into the explanation without a full stop.", "typography",
     fields=("practice_html",), targets=["CE-L01-M03-L01", "CE-L01-M06-L01", "CE-L01-M06-L05", "CE-L01-M07-L01", "CE-L01-M07-L03"], expect=5, source=SRC)

# --- Lesson 4.3 ---
fix("CE-L01-M04-L03", "Based on the dialogue, put these three tasks in the correct order to do them.",
    "Based on the dialogue, put these three tasks in the correct order to do them: (a) file yesterday's receipts; (b) set up the meeting room; (c) reply to the client.",
    "The exercise said 'these three tasks' but did not list them.", "answer-key", source=SRC)

# --- Lesson 4.4 ---
L = "CE-L01-M04-L04"
rule("proof-L1-4.4-group", r"Rahman group", "Haque group", "The client group shared a name with Dr. Rahman, the General Manager; renamed to avoid confusion.",
     "continuity", fields=("practice_html",), targets=[L], expect=2, source=SRC)
fix(L, "Could you clarify what exactly you mean by [term]?", "Could you clarify what exactly you mean by \"escalate it\"?",
    "The model answer contained a template slot ('[term]').", "production", source=SRC)

# --- Lesson 5.1 ---
fix("CE-L01-M05-L01", "Check the discount code with Priyanka, apply it to the quote, and hold it before the printer until it's confirmed.",
    "Check the discount code with Priyanka, apply it to the quote, and don't send the quote to the printer until the code's confirmed.",
    "'Hold it before the printer' was unclear.", "language", source=SRC)

# --- Lesson 5.2 ---
fix("CE-L01-M05-L02", "after Priyanka's message about the report,", "after Priyanka's request,",
    "Priyanka's request in the dialogue is about the numbers for a meeting, not a report.", "continuity", source=SRC)

# --- Lesson 6.1 ---
fix("CE-L01-M06-L01", "Match each role/department to what it's responsible for.</p>",
    "Match each role/department to what it's responsible for: (a) money, invoices and payments; (b) cleaning and maintaining rooms and areas; (c) hiring, pay, leave and workplace policy; (d) fixing computer and network problems.</p>",
    "The matching exercise listed the departments but not the responsibilities to match them to.", "answer-key", source=SRC)

# --- Lesson 6.5 ---
fix("CE-L01-M06-L05", "Match each phrase to the situation it fits best.</p>",
    "Match each phrase to the situation it fits best: (a) politely asking for a repeat; (b) being honest that you don't know the answer yet; (c) formally restating an instruction before acting on it; (d) confirming you own a task, without over-explaining.</p>",
    "The matching exercise listed the phrases but not the situations to match them to.", "answer-key", source=SRC)

# --- Lesson 7.1 ---
fix("CE-L01-M07-L01", "Match each one to its tone label.</p>",
    "Match each one to its tone label: rude, casual, passive, professional, or confident and respectful.</p>",
    "The exercise asked for tone labels without listing them.", "answer-key", source=SRC)

# --- Lesson 7.2 ---
fix("CE-L01-M07-L02", "the invoice for the Rahman account,", "the invoice for the Haque account,",
    "The client account shared a name with Dr. Rahman, the General Manager; renamed to avoid confusion.", "continuity", source=SRC)

# --- Level 1 Assessment ---
fix("CE-L01-ASSESSMENT", "Good morning, I'm [Name] — I'm starting today,", "Good morning, I'm Nadia — I'm starting today,",
    "A template slot ('[Name]') was printed in an answer option; the book's other samples use Nadia.", "production", source=SRC)
