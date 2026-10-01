# Level 2 · Module 6 · Following Up
PH = "The answer key contained an unfilled template placeholder ('[open response following: …]'); replaced with a sample answer and what to check."

# ---------- 6.1 The Follow-Up Habit ----------
L = "CE-L02-M06-L01"
rule("L2-6.1-duplicate-reflection", r"<h2>A Reflective Moment</h2>\s*<blockquote>.*?</blockquote>\s*", "",
     "The 'A Reflective Moment' section repeated Arif's thinking lines from the Listen & Read section word for word.",
     "structure", fields=("body_html",), flags=16, targets=[L], expect=1)

# ---------- 6.2 Writing a Polite Follow-Up Message ----------
L = "CE-L02-M06-L02"
fix(L, '<p>Suggested answer: [open response following: "Just following up on..." + the original request + "just wanted to flag it in case it got missed"]</p>',
    '<p>Sample: "Just following up on my request from Monday for two extra key cards for the conference team — I wanted to flag it in case it got missed. Let me know if you need anything from my end." Check: a softening opener, the original request named specifically, a good-faith closing line, no accusation.</p>',
    PH, "production")

# ---------- 6.3 Following Up Without Sounding Pushy ----------
L = "CE-L02-M06-L03"
fix(L, '<p>Suggested answer: [open response following: gentle opener + direct "still haven\'t heard back/becoming time-sensitive" + firm-but-respectful "could you confirm by [specific time]?"]</p>',
    '<p>Sample. Message 1: "Just following up on the projector repair for the Riverside Room." Message 2: "I still haven\'t heard back on this, and it\'s becoming time-sensitive — the room is booked for a presentation on Thursday." '
    'Message 3: "Could you confirm by 3 PM tomorrow whether it will be fixed in time? I need to arrange a spare either way." Check: each message is firmer than the last, none is rude, and the last one asks for a specific time.</p>',
    PH, "production")

# ---------- 6.4 Closing the Loop ----------
L = "CE-L02-M06-L04"
fix(L, 'and a closing acknowledgment once it\'s resolved. Scored on tone-escalation control across all three messages.',
    'and a closing acknowledgment once it\'s resolved. Scoring is in the answer key for Exercise 2.',
    "The assessment named a scoring focus but gave no scale.", "assessment")
fix(L, '<p>Suggested answer: [open response following: PAT-0037 gentle opener -&gt; PAT-0038 direct escalation -&gt; CF-0007 closing acknowledgment]</p>',
    '<p>Sample. (1) "Just following up on the new uniform order — I wanted to flag it in case it got missed." (2) "I still haven\'t heard back on the uniforms, and it\'s becoming time-sensitive — the two new staff start on Monday." '
    '(3) "Thanks for confirming the uniforms are on their way — I really appreciate you chasing the supplier. All sorted on my end." '
    'Score 0–3, one point per message: (1) gentle and reminder-toned; (2) clearly firmer, with the real reason for urgency, and still polite; (3) thanks the person specifically and closes the thread. 3 = task complete; 2 = review the lesson for the weak message.</p>',
    PH + " Scoring added for this module assessment item.", "assessment")
