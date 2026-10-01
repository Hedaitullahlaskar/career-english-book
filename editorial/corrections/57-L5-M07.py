# Level 5 · Module 7 · Career Growth Communication
D = 16
PH = "The answer key gave an unfilled template ('[situation]', '[name]'); replaced with a sample answer."
MISSING = "The exercise asked the reader to compare options that were never printed; the two options are now given (the answer key already assumed this order)."

L = "CE-L05-M07-L01"
fix(L, "contributing to the department's decision to promote him to Front Office Supervisor.",
    "contributing to promotion to Front Office Supervisor.",
    "A CV bullet referred to its own writer as 'him'; CV bullets leave out the pronoun.", "language")
fix(L, "Which of these two CV lines is achievement-led rather than duty-based?</p>",
    "Which of these two CV lines is achievement-led rather than duty-based? (1) \"Was part of the team that handled the hotel's busiest weekends.\" (2) \"Spearheaded a weekend overflow process, resulting in a 30% reduction in check-in wait times.\"</p>",
    MISSING, "answer-key")
fix(L, "Suggested answer: Delivered the monthly inventory count two days ahead of schedule, resulting in fewer stock discrepancies during the year-end audit.",
    "Sample: (1) Delivered the monthly inventory count two days ahead of schedule, resulting in fewer stock discrepancies during the year-end audit. (2) Spearheaded a buddy system for new cashiers, resulting in no till errors in their first month. (3) Contributed to a 15% rise in loyalty sign-ups by suggesting a sign-up prompt at checkout.",
    "The exercise asks for three bullet points; the sample gave only one.", "answer-key")

L = "CE-L05-M07-L02"
fix(L, "uses the Situation-Action-Result Interview Structure (PAT-0166)?</p>",
    "uses the Situation-Action-Result Interview Structure (PAT-0166)? (1) \"I'm a natural leader — people always come to me when there's a problem.\" (2) \"In my previous role, a specific example of this is a fully booked weekend when two staff called in sick. I reorganized the shifts, took the busiest desk myself and briefed the trainee on the basics. Every guest was checked in on time, and what I took away from that was how much a calm plan steadies a stressed team.\"</p>",
    MISSING, "answer-key")
fix(L, "Suggested answer: In my previous role, a specific example of this is [situation]. I [specific action]. As a result, [outcome]. What I took away from that was [reflection].",
    "Sample: \"In my previous role, a specific example of this is a week when our supplier delivered the wrong linen sizes two days before a wedding. I called three other suppliers, found one who could deliver the next morning, and swapped the order. The wedding rooms were ready on time, and what I took away from that was the value of keeping a backup supplier's number to hand.\"",
    PH, "production")

L = "CE-L05-M07-L03"
fix(L, "Tanvir Rahman, Front Office Manager at Lakeview.", "Tanvir Ahmed, Front Office Manager at Lakeview.",
    "Renamed to avoid confusion with Dr. Rahman, the General Manager.", "continuity")
fix(L, "Which follow-up message uses PAT-0167's written structure correctly?</p>",
    "Which follow-up message uses PAT-0167's written structure correctly? (1) \"Hi, nice meeting you. Let's connect!\" (2) \"Hi Tanvir, it was great meeting you at the regional meetup — I enjoyed hearing how your team handled the festival-season overflow. I'd love to stay in touch.\"</p>",
    MISSING, "answer-key")
fix(L, "Suggested answer: Nice to meet you, I'm [name] -- I work in [role/field]. What's it like working on [their area]?",
    "Sample: \"Nice to meet you, I'm Sara — I work in guest relations at a business hotel. What's it like running events at a conference centre this size?\"",
    PH, "production")

L = "CE-L05-M07-L04"
SUP = ("The overflow process was Arif's achievement as a front-desk associate (Lesson 7.1's CV and Lesson 7.2's 'previous role'), so it cannot be evidence of what he delivered "
       "as supervisor over the past eight months; the key-card retraining from Module 6 is used instead.")
rule("L5-7.4-evidence", r"the overflow process that cut (?:check-in )?wait times by 30%", "the key-card retraining that ended the complaints",
     SUP, "continuity", fields=("body_html",), targets=[L], expect=2)
fix(L, "-- the overflow process, the team's improved", "— the key-card retraining, the team's improved", SUP, "continuity")
fix(L, "Specific evidence -- the overflow process and improved satisfaction scores.", "Specific evidence — the key-card retraining and improved satisfaction scores.", SUP, "answer-key")
fix(L, "Which opening correctly uses PAT-0168's Evidence-Based Promotion-Case Structure?</p>",
    "Which opening correctly uses PAT-0168's Evidence-Based Promotion-Case Structure? (1) \"I've been here a long time now, so I think it's probably time I moved up.\" (2) \"I'd like to talk about my growth here. Based on what I've delivered this year — the new handover checklist and zero missed VIP arrivals — I'd like to understand what a path to team leader could look like.\"</p>",
    MISSING, "answer-key")
fix(L, "Suggested answer: I'd value your honest feedback on how I've handled [specific responsibility or project] over the past [time period].",
    "Sample: \"I'd value your honest feedback on how I've handled the weekend roster over the past three months — especially the way I've shared out the Sunday shifts.\"",
    PH, "production")

L = "CE-L05-M07-L05"
RANGE = ("The dialogue printed a placeholder ('[X]') instead of a figure, and Arif then referred to 'that range' although no range had been given. "
         "Ms. Noor now states the range and the starting figure.")
rule("L5-7.5-offer", r"we're proposing a starting figure of \[X\]\.",
     "the range is 55,000 to 68,000 taka a month, and we're proposing a starting figure of 55,000.",
     RANGE, "production", fields=("body_html",), targets=[L], expect=2)
fix(L, "Suggested answer: I'd like to discuss compensation for this role. Based on my research and experience with [specific evidence], I was expecting a figure closer to [range]. Is there flexibility on [specific term]?",
    "Sample: \"I'd like to discuss compensation for this role. Based on my research and experience — I've run the night audit team for two years without a single audit error — I was expecting a figure closer to 48,000 taka a month. Is there flexibility on the base salary?\"",
    PH, "production")

L = "CE-L05-M07-L06"
fix(L, "so that the learner builds this skill for whenever they need it themselves,", "so that you build this skill for whenever you need it yourself,",
    "Meta wording ('the learner').", "production")
rule("L5-7.6-years", r"(grown so much here over the past) two years", r"\1 few years",
     "Priyanka greeted Arif on his first day, and his CV shows him at the hotel from 2022, so she has been there longer than two years.", "continuity",
     fields=("body_html",), flags=D, targets=[L], expect=2)
fix(L, "Suggested answer: One thing I'd genuinely suggest is [specific, actionable concern] -- it would help the team going forward. Otherwise, I've valued my time here.",
    "Sample: \"One thing I'd genuinely suggest is a short monthly team meeting where people can raise concerns before they build up — it would help the team going forward. Otherwise, I've valued my time here.\"",
    PH, "production")
fix(L, "Suggested answer: I'm grateful for the opportunity to [specific thing you valued]. I've decided to move on from [role], and I want to make this transition as smooth as possible.",
    "Sample: \"I'm grateful for the opportunity to have learned the reservations system from the ground up here. I've decided to move on from my role as reservations agent, and I want to make this transition as smooth as possible — I can write up my booking checklists before I go.\"",
    PH, "production")
fix(L, "matching the standard set across Lessons 1, 2, and 5.</p>",
    "matching the standard set across Lessons 1, 2, and 5. Score 0–6: summary 0–2 (an achievement-led line; a forward-looking close), behavioral answer 0–2 (all four parts; a genuine reflection), salary answer 0–2 (an evidence-based anchor; a flexibility question asked calmly). Pass at 4, with at least 1 in each part.</p>",
    "The module assessment had no scale.", "assessment")
