# Level 1 · Module 5 · Asking for Help & Clarification

# ---------- 5.1 Asking Someone to Repeat or Explain ----------
L = "CE-L01-M05-L01"
fix(L, 'Could you explain that + a different way / a different way?', 'Could you explain that + in a different way / another way?',
    "The pattern repeated the same option twice ('a different way / a different way').", "language")

# ---------- 5.2 Asking the Right Clarifying Question ----------
L = "CE-L01-M05-L02"
fix(L, "Arif understood almost all of Priyanka's message about the weekly report -- except one detail.",
    "Arif understood almost all of Priyanka's request for the updated numbers — except one detail: which meeting she means.",
    "The opening described a 'weekly report', but the dialogue is about numbers for one of two meetings.", "continuity")
fix(L, 'Just to check — do you mean the sales numbers for this week, or the client meeting at 4 PM?',
    'Just to check — do you mean the team meeting at 11, or the client meeting at 4 PM?',
    "The two options did not match: Arif's confusion is about which meeting, so both options must be meetings.", "language")
fix(L, "No problem, I'll have it ready by 3:30.", "No problem, I'll have them ready by 3:30.",
    "'Numbers' is plural, so the pronoun should be 'them'.", "grammar")
fix(L, '<span class="hi">आप क्या मतलब कह रहे हैं</span>', '<span class="hi">आपका क्या मतलब है</span>',
    "'आप क्या मतलब कह रहे हैं' is not natural Hindi; the everyday question is 'आपका क्या मतलब है?'.", "l1-support", count=2)
fix(L, "(this week's sales numbers vs. the 4 PM meeting)", "(the 11 o'clock team meeting vs. the 4 PM client meeting)",
    "Aligned with the corrected dialogue.", "answer-key")

# ---------- 5.3 Asking Colleagues vs. Asking Supervisors ----------
L = "CE-L01-M05-L03"
fix(L, '<p>Small, routine, low-stakes questions (the stapler, the printer) go to a colleague. Anything involving an approval, a decision, or a deadline change goes to a supervisor, even if a colleague happens to know the answer.</p>',
    '<p>(1) Colleague. (2) Supervisor. (3) Colleague. (4) Supervisor. Small, routine questions (the stapler, the printer) go to a colleague; anything involving an approval, a decision or a deadline change goes to a supervisor, even if a colleague happens to know the answer.</p>',
    "The key stated the rule but did not answer the four items.", "answer-key")
