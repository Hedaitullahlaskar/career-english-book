# Level 5 · Module 3 · Coaching Through Questions
D = 16

L = "CE-L05-M03-L01"
rule("L5-3.1-bengali-hindi-note", r'(<h2>Bengali/Hindi support</h2>\s*)<p><span class="bn">বাংলা</span>/<span class="bn">.*?</span></p>',
     r'\1<p>In many Bengali- and Hindi-speaking workplaces, a senior person who answers a question directly is seen as more respectful and helpful than one who asks a question back — so learning to coach is a real cultural adjustment, not just a technique.<br>'
     r'<span class="bn">অনেক বাংলাভাষী কর্মক্ষেত্রে সরাসরি উত্তর দেওয়াকে বেশি সম্মানজনক ও সহায়ক মনে করা হয় — তাই কোচিং শেখা একটি সত্যিকারের সাংস্কৃতিক মানিয়ে নেওয়া, শুধু একটি কৌশল নয়।</span><br>'
     r'<span class="hi">कई हिंदीभाषी कार्यस्थलों में सीधा जवाब देना ज़्यादा सम्मानजनक और मददगार माना जाता है — इसलिए कोचिंग सीखना एक वास्तविक सांस्कृतिक समायोजन है, न कि केवल एक तकनीक।</span></p>',
     "The note had no English version, its language tags were misplaced (the word 'বাংলা' tagged alone, Bengali text inside the Hindi tag's sentence), "
     "and the Bengali sentence said 'the instinct to coach is a real adjustment' rather than 'learning to coach is a cultural adjustment'.",
     "l1-support", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "\"Just move the guest to room 412, it's free tonight.\"", "\"Just move the guest to room 415, it's free tonight.\"",
    "Room 412 is the double-booked room; the free room in the dialogue is 415.", "continuity")
fix(L, "Assessment: for each of these five short responses to a colleague's question, label it \"telling\" or \"coaching\" and briefly say how you know.",
    "Quick check: label each response to a colleague's question \"telling\" or \"coaching\" and briefly say how you know. (1) \"Check the booking system first, then call housekeeping.\" (2) \"What do you think the guest is really asking for?\" (3) \"Offer them a late checkout at 2 p.m.\" (4) \"What options have you looked at so far?\" (5) \"Don't you think you should just refund them?\"",
    "The exercise asked about 'these five short responses', but none were printed.", "answer-key")
fix(L, "across all five items.</p>",
    "across all five items. (1) telling — a direct instruction; (2) coaching — the answer is left to the colleague; (3) telling — the solution is given; (4) coaching — it asks for the colleague's own thinking; (5) telling — it is phrased as a question, but the answer is built into it (Lesson 2 calls this a leading question).</p>",
    "The answer key had no answers for the five items.", "answer-key")
fix(L, "Suggested answer: Telling: [direct answer]. Coaching: What have you already tried?",
    "Sample (question: \"Which form do I use for a lost key card?\"). Telling: \"Use the blue incident form in the top drawer.\" Coaching: \"What have you already checked — is there anything in the front-desk folder about key cards?\"",
    "The answer key gave an unfilled template ('[direct answer]'); replaced with a sample answer.", "production")

fix("CE-L05-M03-L02", "Now that Rima understands the difference between telling and\ncoaching, she needs the actual questions",
    "Now that the difference between telling and coaching is clear, Arif needs the actual questions",
    "Rima is the person being coached; it is Arif who needs the questions.", "continuity")

L = "CE-L05-M03-L03"
fix(L, "even when one is obvious to the learner.", "even when one is obvious to you.", "Meta wording ('the learner').", "production")
fix(L, "the obvious fix (bump another guest) is sitting", "the obvious fix (offer the free executive suite as an upgrade) is sitting",
    "The opening named a different 'obvious fix' (bumping another guest) from the one the lesson and its answer key actually discuss.", "continuity")
fix(L, "it's the same price tier, they won't mind.", "it's a higher tier, they won't mind.",
    "The dialogue says the executive suite is a higher tier, not the same tier.", "continuity")

L = "CE-L05-M03-L04"
rule("L5-3.4-empty-dialogue-box", r'<div class="dialogue-box">\s*<div class="dialogue-box-label">[^<]*</div>\s*<div class="dialogue-turns">\s*</div>\s*</div>\s*', "",
     "An empty 'Listen & Read' box (no dialogue) was printed before the story.", "structure", fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "What do scenarios 1, 2, and 3 have in common that makes telling the right call in each?",
    "What do a fire alarm, a strict compliance rule and a total beginner have in common that makes telling the right call in each?",
    "The question referred to 'scenarios 1, 2, and 3', which do not exist in the lesson.", "answer-key")
fix(L, "even though it was the right tool in scenario 4.", "even though coaching is the right tool in most everyday situations.",
    "Referred to a non-existent 'scenario 4'.", "answer-key")
fix(L, "Suggested answer: [open reflection response]",
    "Sample: \"On my first day on reception, a supervisor asked me what I thought the check-in steps were. I had no idea — I had never used the system. Telling would have been right, because there was no context for me to reason from.\"",
    "The answer key contained an unfilled placeholder.", "production")
fix(L, "quality of your coaching, not the outcome of the scenario.</p>",
    "quality of your coaching, not the outcome of the scenario. Score 0–4, one point each: (1) an opening open question; (2) at least one follow-up built on the other person's answer; (3) no leading questions; (4) the answer is never stated, even once it is obvious. Pass at 3.</p>",
    "The module assessment had no scale.", "assessment")
fix(L, "the learner does not state the answer directly", "the coach does not state the answer directly", "Meta wording ('the learner').", "production")
