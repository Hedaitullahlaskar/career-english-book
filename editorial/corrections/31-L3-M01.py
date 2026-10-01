# Level 3 · Module 1 · Professional Email Writing
PH = "The answer key contained an unfilled template placeholder ('[open response …]'); replaced with a sample answer."

# ---------- 1.1 Anatomy of a Professional Email ----------
L = "CE-L03-M01-L01"
fix(L, 'the learner is taught to match the rung to the actual relationship', 'the skill is matching the rung to the actual relationship',
    "Production language ('the learner is taught').", "production")

# ---------- 1.2 Making Requests and Sharing Information ----------
L = "CE-L03-M01-L02"
fix(L, 'Arif needs Procurement to approve\na reorder before the weekend\'s group check-in.',
    'Arif needs Ms. Noor to approve a reorder before the weekend\'s group check-in.',
    "The opening said Procurement must approve the reorder, but the email (and Lesson 1.3's follow-up) ask Ms. Noor to approve it.",
    "continuity")
fix(L, '[open response following PAT-0047: greeting + reason for writing + background + clear request with a deadline + closing]',
    'Sample: "Subject: Attendance Report — Needed by Thursday / Hi Rina, / I\'m writing to request last month\'s attendance report. Ms. Noor has asked me to prepare the staff overtime summary, and the report is the main source for it. / Could you send it over by Thursday? / Thanks, Arif"',
    PH, "production")

# ---------- 1.3 Following Up, Reminding, and Confirming ----------
L = "CE-L03-M01-L03"
fix(L, '[three open responses, one following PAT-0048 for the follow-up, one following PAT-0048 for the reminder, and one following PAT-0049 for the confirmation]',
    'Sample. (1) "Hi Priyanka, Just following up on the training schedule I sent on Monday — I wanted to flag it in case it got missed. Let me know if any of the dates don\'t work. Thanks, Arif" '
    '(2) "Hi Mr. Islam, As a gentle reminder, tomorrow\'s delivery window is 9–11 AM at the loading bay. Please let me know if anything changes. Best regards, Arif" '
    '(3) "Hi Hasan, To confirm our conversation just now: Thursday\'s team meeting has moved from 3 PM to 4 PM. Nothing further needed. Best, Arif"',
    PH, "production")

# ---------- 1.4 Apologizing and Responding to a Complaint ----------
L = "CE-L03-M01-L04"
fix(L, '[open response following PAT-0050: acknowledge the complaint + sincere apology naming the specific issue + empathy statement + ownership + a concrete next step]',
    'Sample: "Dear Ms. Kabir, Thank you for letting us know. I sincerely apologize that your 5 AM wake-up call did not come through and that you were late for your flight — I understand your frustration. That\'s on us: the call was logged for the wrong room. I have refunded last night\'s room charge, and we have added a second check of every wake-up request at the night handover. Best regards, Arif"',
    PH, "production")

# ---------- 1.5 Escalating an Issue by Email ----------
L = "CE-L03-M01-L05"
fix(L, 'Arif has already emailed the vendor\nonce (Lesson 1) and followed up once (Lesson 3) -- and four days later, nothing has changed.',
    'Arif has already emailed the vendor once (Lesson 1.1) and followed up once since — and four days later, nothing has changed.',
    "Lesson 1.3's follow-up email is about the towel reorder, not the AC repair.", "continuity")
fix(L, '[open response following PAT-0051: state the issue plainly + what\'s already been tried + who is CC\'d and why + a clear, specific ask + a firm but respectful closing]',
    'Sample: "Subject: Conference Chairs — Delivery Date Needed Today / Hi Mr. Das, I\'m raising this because we still don\'t have a delivery date for the 120 conference chairs, despite my emails on Monday and Wednesday. The conference starts tomorrow at 9 AM. I\'m looping in Ms. Noor, our Front Office Manager, since this now affects the event setup. Given the urgency, could you confirm a delivery time by 3 PM today? Best regards, Arif"',
    PH, "production")

# ---------- 1.6 Putting a Full Email Thread Together ----------
L = "CE-L03-M01-L06"
fix(L, '<h2>Industry Overlays</h2>\n<ul>\n<li>Example variety only in this synthesis lesson -- the same thread discipline (staying anchored,\n matching tone, adding rather than repeating, closing explicitly) applies identically whether\n the thread is about a hotel goodwill gesture, a banking document approval, or an IT ticket\n resolution.</li>\n</ul>\n',
    '<h2>Industry Overlays</h2>\n<ul>\n<li>The same thread discipline (staying anchored, matching tone, adding rather than repeating, closing explicitly) applies whether the thread is about a hotel goodwill gesture, a banking document approval, or an IT ticket.</li>\n</ul>\n',
    "Production language ('Example variety only in this synthesis lesson').", "production")
fix(L, '<span class="exercise-type">Role-Play</span></div><div class="exercise-prompt"><p>Module 1 as',
    '<span class="exercise-type">Writing</span></div><div class="exercise-prompt"><p>Module 1 as',
    "The task is to write an email thread, not a role-play.", "assessment")
fix(L, 'and the thread ends with an explicit confirmation -- avoiding MIS-0080\'s disconnected, restarting-thread pattern.</p>',
    'and the thread ends with an explicit confirmation — avoiding MIS-0080\'s disconnected, restarting-thread pattern. Score 0–4, one point each: (1) at least three email types used correctly; (2) one consistent subject and tone; (3) every message adds something new; (4) an explicit close. 4 = complete; 3 = complete, revise the weak point; 2 or fewer = review Lessons 1.2–1.5.</p>',
    "The module assessment had criteria but no scale.", "assessment")
fix(L, 'Four separate messages -- but to\nthe guest, and to anyone reading the thread later, it needs to read as one clear, connected\nconversation.',
    'Four separate messages — but to anyone reading the thread later, it needs to read as one clear, connected conversation.',
    "The thread is internal (Arif and Ms. Noor); the guest never reads it.", "continuity")
