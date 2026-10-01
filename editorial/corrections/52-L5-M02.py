# Level 5 · Module 2 · Feedback & Performance Conversations
D = 16
PH = "The answer key gave an unfilled template ('[specific detail]', '[summary]'); replaced with a sample answer."

rule("L5-guest-satisfaction-hyphen", r"guest-\s+satisfaction", "guest-satisfaction",
     "Stray space after the hyphen ('guest- satisfaction').", "typography",
     fields=("body_html",), targets=["CE-L05-M02-L02", "CE-L05-M02-L05"], expect=3)

L = "CE-L05-M02-L01"
fix(L, "(Module 2, L02: \"here's what you\ndid,", "(Lesson 2.2: \"here's what you did,", "Internal lesson code replaced.", "reference")
fix(L, "Suggested answer: Quick note on yesterday's task -- something I noticed was [specific detail]. Worth flagging while it's fresh.",
    "Sample: \"Quick note on yesterday's task — something I noticed was how you called the guest back to confirm the airport pickup. Worth flagging while it's fresh: that's exactly what stops a missed pickup.\"",
    PH, "production")
fix(L, "Suggested answer: Quick note on [task] -- something I noticed was [specific detail]. Worth flagging while it's fresh.",
    "Sample: \"Quick note on this morning's group check-in — something I noticed was that you had every key card ready before the coach arrived. Worth flagging while it's fresh: it cut the wait to almost nothing.\"",
    PH, "production")

L = "CE-L05-M02-L02"
fix(L, "This three-part shape is new to the course -- the first named structure for an entire formal\nconversation, rather than a single exchange -- and it deliberately puts strengths first by design,",
    "This three-part shape gives a whole formal conversation its outline, not just a single exchange, and it deliberately puts strengths first,",
    "The claim that this was the course's first named structure for a whole conversation was not true (for example, Level 4's Conflict Resolution Formula, CF-0019).", "factual")
fix(L, "Suggested answer: Let's start with what's going well -- [specific strength]. An area I'd like to see grow is how quickly you escalate issues. Overall, [summary].",
    "Sample: \"Let's start with what's going well — guests regularly mention how calm you are at busy check-ins, and your satisfaction scores show it. An area I'd like to see grow is how quickly you escalate issues you can't solve alone. Overall, you're in a strong position, and this is the one thing that would take you further.\"",
    PH, "production")
fix(L, "Suggested answer: Let's start with what's going well -- [strength]. An area I'd like to see grow is [area]. Overall, [summary].",
    "Sample: \"Let's start with what's going well — your night-audit reports are accurate and always on time. An area I'd like to see grow is speaking up in the morning briefing when you've spotted a problem overnight. Overall, you're a reliable member of the team, and this would make your work more visible.\"",
    PH, "production")

L = "CE-L05-M02-L03"
fix(L, "the learner asks the other person to restate it", "you ask the other person to restate it", "Meta wording ('the learner').", "production")
fix(L, "the\n goal is [Farhan restates it in his own words].", "the goal is... <em>(Farhan restates it in his own words.)</em>",
    "A stage direction was printed in square brackets, like a template slot.", "typography")
fix(L, "Suggested answer: What would you like to focus on?...Does that feel achievable?...Just to confirm, what's the goal in your own words?",
    "Sample: \"Given what we've discussed, what would you like to focus on this quarter? … So, escalating any issue that isn't solved within the hour — does that feel achievable? … Great. Just to confirm, what's the goal, in your own words?\"",
    "The answer key gave only the opening words of each step; replaced with a complete sample.", "production")
fix(L, "Suggested answer: What would you like to focus on?...Does that feel achievable?...Let's check in on this in [timeframe].",
    "Sample: \"What would you like to focus on over the next two months? … So, finishing the shift handover notes before you leave, every shift — does that feel achievable? … Let's check in on this in three weeks.\"",
    PH, "production")

L = "CE-L05-M02-L04"
fix(L, "(Module 2,\nL02) into a formal, higher-stakes context where the learner is accountable",
    "(Lesson 2.2) into a formal, higher-stakes context where you are accountable",
    "Internal lesson code and meta wording ('the learner') replaced.", "reference")
fix(L, "What does Farhan actually learn from Scene A that he doesn't learn from Scene B?",
    "What does Farhan actually learn from Arif in Scene A?",
    "The question was phrased backwards (what Scene A teaches that Scene B doesn't), which made the intended answer, 'Nothing specific', illogical.", "answer-key")
fix(L, "Suggested answer: This isn't meeting the expectation we set. Here's what needs to change -- [specific requirement]. How can I support you in getting there?",
    "Sample: \"This isn't meeting the expectation we set last month — two escalations went past the hour again. Here's what needs to change: escalate at 45 minutes, not 60. How can I support you in getting there?\"",
    PH, "production")
fix(L, "Suggested answer: This isn't meeting the expectation we set: [gap]. Here's what needs to change: [requirement]. How can I support you in getting there?",
    "Sample: \"This isn't meeting the expectation we set: the lost-property log has been empty for three of the last five shifts. Here's what needs to change: every item is logged before the end of the shift. How can I support you in getting there?\"",
    PH, "production")

L = "CE-L05-M02-L05"
fix(L, "role-play, graded holistically.</strong>", "role-play.</strong>", "'Graded holistically' gave no scale; a scale is now given.", "assessment")
fix(L, "clearer about where they stand and motivated\n about what's ahead.</p>",
    "clearer about where they stand and motivated about what's ahead. Score 0–4, one point per element; pass at 3, and the confirmed goal (element 3) must be one of them.</p>",
    "The module assessment had no scale.", "assessment")
fix(L, "Which parts of Modules 2's earlier lessons", "Which parts of Module 2's earlier lessons", "Typo ('Modules 2's').", "typography")
fix(L, "A strengths-first opening (L02), acknowledgment of a past goal (L03/L04), and a new collaboratively set, confirmed goal (L03)",
    "A strengths-first opening (Lesson 2), acknowledgment of a past goal (Lessons 3–4), and a new collaboratively set, confirmed goal (Lesson 3)",
    "Internal lesson codes replaced.", "reference")
fix(L, "Only the underperformance formula from L04", "Only the underperformance formula from Lesson 4", "Internal lesson code replaced.", "reference")
fix(L, "Suggested answer: Let's start with what's going well -- [specific strength]. That's real progress. An area I'd like to see grow this quarter is...",
    "Sample: \"Let's start with what's going well — you've hit the escalation goal every week for two months, and guests still mention how calm you are at busy check-ins. That's real progress. An area I'd like to see grow this quarter is...\"",
    PH, "production")
fix(L, "Suggested answer: Let's start with what's going well -- I've noticed [specific progress since last time]...",
    "Sample: \"Let's start with what's going well — last time we agreed you'd finish your handover notes before every shift ends, and I've noticed they've been complete every day this month. That's exactly what we were aiming for...\"",
    PH, "production")
fix(L, "<p>What to listen/look for: Opens with specific, genuine strengths",
    "<p>Score with the four elements in the Module 2 Assessment section (0–4; pass at 3). What to listen/look for: Opens with specific, genuine strengths",
    "The module assessment had no scale.", "assessment")
