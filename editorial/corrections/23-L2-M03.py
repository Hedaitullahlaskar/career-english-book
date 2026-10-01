# Level 2 · Module 3 · Telephone English Basics

# ---------- 3.1 Answering and Identifying Yourself ----------
L = "CE-L02-M03-L01"
fix(L, '<p>Suggested answer: [open response following: greeting + company/department + "this is [Name] speaking" + "how can I help you today?"]</p>',
    '<p>Sample: "Good morning, Riverside Clinic reception, this is Nadia speaking. How can I help you today?" Check: greeting + organisation or department + "this is … speaking" + an offer to help.</p>',
    "The answer key contained an unfilled template placeholder.", "production")

# ---------- 3.2 Taking a Message Accurately ----------
L = "CE-L02-M03-L02"
rule("L2-3.2-phone-number", r"017-XXX-XXXX", "01711-582403",
     "The lesson teaches confirming a callback number, but every number was masked ('017-XXX-XXXX'), so the restatement could not be practised. "
     "Replaced with a realistic fictional 11-digit mobile number.", "production", targets=[L], expect=8)
rule("L2-3.2-phone-number-overlay", r"018-XXX-XXXX", "01819-306274",
     "Masked number replaced with a realistic fictional one.", "production", targets=[L], expect=1)
rule("L2-3.2-supplier-name", r"Mr\. Rahman", "Mr. Siddique",
     "The linen supplier shared a surname with Dr. Rahman, the hotel's General Manager, which is confusing in a lesson about getting names right.",
     "continuity", targets=[L], expect=8)
fix(L, 'Using the filled-in message note from A01,', 'Using the filled-in message note from Exercise 1,',
    "Internal activity code ('A01').", "production")

# ---------- 3.3 Asking Someone to Repeat or Slow Down ----------
L = "CE-L02-M03-L03"
fix(L, 'zero, one, seven, four, four, one, two, two, three, three.', 'zero, one, seven, one, four, four, one, two, two, three, three.',
    "Bangladeshi mobile numbers have 11 digits; the number had 10.", "factual")
fix(L, '017-441-2233, Chowdhury.', '01714-412233, Chowdhury.', "Matches the corrected 11-digit number.", "factual")

# ---------- 3.4 Putting Someone on Hold and Transferring ----------
L = "CE-L02-M03-L04"
fix(L, '<p>Suggested answer: [open response following: ask permission to hold + thank for waiting + name the person or department being connected]</p>',
    '<p>Sample: "Could you hold the line for a moment while I check with Accounts? … Thanks for waiting — I\'ll put you through to Mr. Islam in Accounts now; he can help with your invoice." Check: permission to hold, thanks on return, the person or department named before the transfer.</p>',
    "The answer key contained an unfilled template placeholder.", "production")

# ---------- 3.5 Handling a Difficult or Unclear Caller & Ending the Call ----------
L = "CE-L02-M03-L05"
fix(L, 'close the call using the full call-closing formula. Scored on message accuracy and composure.',
    'close the call using the full call-closing formula. Scoring is in the answer key for Exercise 3.',
    "The assessment said it was 'scored on message accuracy and composure' but gave no scale.", "assessment")
fix(L, '<p>What to listen/look for: The call opens with a complete greeting,',
    '<p>Scoring (1 point each, 4 = task complete, 3 = complete with one area to practise, 2 or fewer = review Lessons 3.1–3.5): (1) complete greeting; (2) calm clarification instead of guessing; (3) every detail restated correctly; (4) the full closing formula. What a strong call shows: the call opens with a complete greeting,',
    "The module assessment had no scoring scale.", "assessment")
