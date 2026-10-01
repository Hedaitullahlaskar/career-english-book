# PDF proof, batch 3: Level 3 (PDF pp. 348–614).
SRC = "PDF proof, batch 3 · editorial review"
AUTO = "PDF proof, batch 3 · automated check"

# --- Typography: clock-time ranges take an en dash, like the number ranges fixed in batch 1 ---
rule("proof-time-ranges", r"\b(\d{1,2}:\d\d)-(\d{1,2}:\d\d)\b", r"\1–\2",
     "Time ranges were written with a hyphen in some places (7:00-8:00 AM) and an en dash in others (2:00–2:20 PM); they now use the en dash throughout.",
     "typography", fields=("body_html", "practice_html"), source=SRC)

# --- Module 1 ---
fix("CE-L03-M01-L01", "Subject: Next Week's Schedule — Approval Needed by Thursday What to listen/look for:",
    "Subject: Next Week's Schedule — Approval Needed by Thursday. What to listen/look for:",
    "The sample subject line ran straight into the marking note without a full stop.", "typography", source=SRC)
fix("CE-L03-M01-L02", "writing an email that gives Procurement everything they need to say yes",
    "writing an email that gives Ms. Noor everything she needs to say yes",
    "The opening said the email was for Procurement, but the lesson's email asks Ms. Noor to approve the reorder.", "continuity", source=SRC)
fix("CE-L03-M01-L04", "Sample: \"Dear Ms. Kabir,", "Sample: \"Dear Ms. Begum,",
    "The guest in the sample shared a surname with Mr. Kabir, the Head of Finance; renamed to avoid confusion.", "continuity", source=SRC)
fix("CE-L03-M01-L05", "I'm looping in Ms. Noor, our Front Office Manager,", "I'm looping in Ms. Noor, our Front Office Department Head,",
    "Ms. Noor's title is Front Office Department Head (Level 1 Lesson 1.3); 'Front Office Manager' is a different role in Level 5.", "continuity", source=SRC)

# --- Module 5 ---
fix("CE-L03-M05-L01", "an ordinary, calmly-raised complaint", "an ordinary, calmly raised complaint",
    "No hyphen after an -ly adverb.", "typography", source=SRC)
L = "CE-L03-M05-L02"
fix(L, "and which two structures (PAT-0077 or PAT-0078) his Scene B response follows instead.",
    "and which structures (PAT-0077 and PAT-0078) his Scene B response follows instead.",
    "The exercise asked for 'two structures' but wrote 'or'; Scene B uses both.", "answer-key", source=SRC)
fix(L, "follows PAT-0077 (validate, state intent, invite collaboration).",
    "follows PAT-0077 (validate, state intent, invite collaboration), and his next line, 'Let me walk you through exactly what I can offer right now,' completes PAT-0078 (no defending, one honest acknowledgment, then a redirect toward the fix).",
    "The exercise asks for two structures; the answer key named only one.", "answer-key", source=SRC)
L = "CE-L03-M05-L05"
fix(L, "a full CF-0013 service-\nrecovery close.", "a full CF-0013 service-recovery close.",
    "A line break inside the hyphenated word printed as 'service- recovery'.", "typography", source=SRC)
fix(L, "a genuinely angry customer opening (PAT-0077/PAT-0078),",
    "a genuinely angry customer opening, handled with empathetic listening (PAT-0076) and de-escalation (PAT-0077/PAT-0078),",
    "The scoring gives a point for empathetic listening, but the task did not ask for it.", "assessment", source=SRC)

# --- Module 6 ---
fix("CE-L03-M06-L05", "so here's how this solves that crowded feeling you mentioned.</span>",
    "so here's how this solves that boxed-in feeling you mentioned.</span>",
    "In this lesson's dialogue Ms. Cruz says she doesn't want people 'feeling boxed into small rooms'; she never mentions a crowded feeling.", "continuity", source=SRC)

# --- Module 7 ---
fix("CE-L03-M07-L02", "This could fail\nto succeed unless we address the staffing gap.", "This could fail unless we address the staffing gap.",
    "'Fail to succeed' is redundant; the rest of the lesson uses 'This could fail unless…'.", "grammar", source=SRC)
fix("CE-L03-M07-L05", "\"We received a complaint, which was resolved the same day,\" does that work for them.",
    "\"We received a complaint, which was resolved the same day\" does that work for them.",
    "A comma inside the quotation separated the subject from its verb.", "typography", source=SRC)
L = "CE-L03-M07-L06"
fix(L, "relative clauses/gerunds-\ninfinitives,", "relative clauses/gerunds-infinitives,",
    "A line break inside the hyphenated word printed as 'gerunds- infinitives'.", "typography", source=SRC)
fix(L, "one point for each area corrected correctly (pass at 5):", "one point for each area corrected (pass at 5):",
    "'Corrected correctly' is redundant.", "language", source=SRC)

# --- Module 8 ---
fix("CE-L03-M08-L01", "landing hard on the word in <strong>bold capitals</strong> word.",
    "landing hard on the word in <strong>bold capitals</strong>.",
    "A stray 'word' at the end of the instruction.", "typography", source=SRC)

# --- Module 9 ---
fix("CE-L03-M09-L02", "leave no clear resolution .", "leave no clear resolution.",
    "Stray space before the full stop.", "typography", source=AUTO)
fix("CE-L03-M09-L04", "and closed a client relationship on video", "and closed a client booking on video",
    "'Closed a client relationship' reads as ending the relationship; Arif confirms a booking.", "language", source=SRC)

# --- Level 3 Assessment ---
L = "CE-L03-ASSESSMENT"
fix(L, "articles/prepositions/ subject-verb agreement;", "articles/prepositions/subject-verb agreement;",
    "Stray space after the slash.", "typography", count=2, source=SRC)
fix(L, "Sample: \"Mr. Hasan, it's a pleasure to meet you", "Sample: \"Mr. Siddiqui, it's a pleasure to meet you",
    "The new client in the sample was called 'Mr. Hasan', the name of Arif's colleague; renamed to avoid confusion.", "continuity", source=SRC)

# --- Capstone ---
L = "CE-L03-CAPSTONE"
fix(L, "if you can get this to me by Wednesday morning, that gives\nme enough time to put a report together before Wednesday's",
    "if you can get this to me by Tuesday afternoon, that gives me enough time to put a report together before Wednesday's",
    "A Wednesday-morning deadline left no time to write the report before the 9:15 meeting; Priyanka replies on Tuesday in Step 2.", "continuity", source=SRC)
fix(L, "a five-figure client relationship closed out cleanly", "a five-figure client booking closed out cleanly",
    "'Closed out a client relationship' reads as ending it; the closing section says 'a five-figure booking closed out cleanly'.", "language", source=SRC)
