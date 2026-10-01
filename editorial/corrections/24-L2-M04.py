# Level 2 · Module 4 · Digital Messaging (WhatsApp/Teams/Slack)
PH = "The answer key contained an unfilled template placeholder ('[open response following: …]'); replaced with a sample answer and what to check."

# ---------- 4.1 Chat Register ----------
L = "CE-L02-M04-L01"
fix(L, "Level 1 Module 7's tone teaching (Casual / Polite / Professional / Formal)",
    "Level 1 Module 7's tone teaching (rude / casual / passive / professional / confident)",
    "The labels did not match the five tones Level 1 Module 7 actually taught.", "reference")
fix(L, '<h2>Professional Tone</h2>\n<blockquote>\n<p>Bengali/Hindi note:', '<h2>Bengali/Hindi support</h2>\n<blockquote>\n<p>Bengali/Hindi note:',
    "The section was headed 'Professional Tone' but contained only the Bengali/Hindi note.", "structure")
fix(L, '<p>Suggested answer: [open response following: chat-register version + email-register version + an example of over-informal shorthand that would misfire in either channel]</p>',
    '<p>Sample (news: the staff lift is out of service until Friday). Chat: "Heads up — staff lift\'s out till Friday, use the service stairs." '
    'Email: "Dear all, Please note that the staff lift will be out of service until Friday for repairs. In the meantime, please use the service stairs. Thank you." '
    'Too informal for either: "lift dead again smh 🙄". Check: the chat version is short but complete; the email has a greeting, full sentences and a sign-off.</p>',
    PH, "production")

# ---------- 4.2 Writing Clear, Short Work Messages ----------
L = "CE-L02-M04-L02"
fix(L, '<p>Suggested answer: [open response following: one heads-up message + one quick-question message + one additional-point message, each on its own]</p>',
    '<p>Sample: "Heads up — the conference room projector isn\'t working." / "Quick question — do you know who has the spare remote?" / "One more thing — the 3 PM group has moved to 3:30." Check: three separate messages, one idea each, each with its signal opener.</p>',
    PH, "production")

# ---------- 4.4 Reading the Room in Group Chats ----------
L = "CE-L02-M04-L04"
fix(L, '<p>Suggested answer: [open response following: one genuinely group-relevant message + one two-person message correctly identified as DM-only, with a one-line reason for each]</p>',
    '<p>Sample. Group: "The guest Wi-Fi password changes tonight — new one is pinned above." (Everyone at the desk gives guests the password.) '
    'DM: "Hi Hasan, could I borrow your locker key after my shift?" (Only Hasan needs to see it.)</p>',
    PH, "production")

# ---------- 4.5 Message, Call, or Talk in Person? ----------
L = "CE-L02-M04-L05"
fix(L, '<p>Suggested answer: [open response following: message + justification, for each of three distinct urgency/sensitivity combinations]</p>',
    '<p>Sample. (1) Message: "Reminder — staff training is moved to Thursday at 10." Reason: routine, not sensitive, no discussion needed. '
    '(2) Call: "Hi Rupa, Room 512\'s guest is arriving in ten minutes and the room isn\'t ready — can you send someone now?" Reason: urgent, needs an answer immediately. '
    '(3) In person: "Have you got a few minutes? I\'d like to talk about the handover notes from this week." Reason: sensitive, needs tone and a two-way conversation. '
    'Score each message 0–2: 1 for a message that suits the situation, 1 for a justification that names urgency, sensitivity or complexity.</p>',
    PH + " The module assessment item also gets a score scale.", "assessment")
