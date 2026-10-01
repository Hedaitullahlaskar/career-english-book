# Level 4 · Module 2 · Difficult Conversations & Conflict Management
D = 16

fix("CE-L04-M02-L01", "waive the early-checkout charge on a suite he's kept two extra days past his original reservation,",
    "waive the extra-night charge on a suite he's kept two nights past his original reservation,",
    "He stayed longer, not shorter: the charge is for extra nights (as the dialogue says), not an 'early-checkout' charge.", "factual")

L = "CE-L04-M02-L04"
fix(L, "would under-bill the\naccount by an estimated significant amount.",
    "would under-bill the account by an estimated 210,000 taka (the difference between the C-12 and C-14 rates for 45 rooms over three nights).",
    "'An estimated significant amount' is not an objective figure; an incident report states the estimated amount and how it was calculated.", "factual")
fix(L, "the same mistake you reported in Activity 3,", "the same mistake you reported in Exercise 3,", "Internal activity name ('Activity 3').", "production")
rule("L4-2.4-report-sample", r"Suggested answer: Facts: On \[date\].*?to prevent a repeat\.",
     "Sample: Facts: On 12 March, the pickup for the Rahim family (Booking #8842) was booked for 10:00 PM instead of 10:00 AM. Impact: If uncorrected, the family would have waited about twelve hours at the airport. Immediate action taken: The pickup was corrected to 10:00 AM on 12 March, the same day the error was identified, and the driver confirmed. Recommendation: I recommend that all pickup times are read back to the guest in 24-hour format when booked.",
     "The model answer was a template full of unfilled placeholders ('[date]', '[specific error]').", "production",
     fields=("practice_html",), flags=D, targets=[L], expect=1)

L = "CE-L04-M02-L06"
fix(L, "Hasan, can we take a second on this? The answer is still no on taking the whole weekend alone --",
    "Hasan, can we take a second on this? The answer is no on taking the whole weekend alone —",
    "'Still no' implies an earlier refusal, but this is Arif's first response.", "language")
fix(L, "Hasan, can we take a second on this? -- The answer is still no on taking the whole weekend of\nprep alone;",
    "Hasan, can we take a second on this? The answer is no on taking the whole weekend of prep alone;",
    "'Still no' implies an earlier refusal, but this is Arif's first response.", "language")
fix(L, "agree on a specific, resolution]", "agree on a specific resolution]", "Typo (stray comma).", "typography")
fix(L, "<p>Example variety only, per the curriculum map -- the Conflict Resolution Formula (CF-0019) applies\nwhether",
    "<p>The Conflict Resolution Formula (CF-0019) applies whether",
    "Production language ('Example variety only, per the curriculum map').", "production")
fix(L, "It is graded holistically, in the same style as prior\nLevel 2 and Level 3 module and capstone assessments.",
    "The scoring scale is in the answer key for Exercise 3.", "'Graded holistically' gave no scale.", "assessment")
fix(L, "<p>MODULE 2 ASSESSMENT.", "<p>Module 2 assessment.", "Consistent capitalisation with the other module assessments.", "typography")
fix(L, "Graded holistically, per the module assessment description in the module overview.",
    "Score 0–4, one point each: (1) the real issue is separated from the surface complaint; (2) at least two of the module's skills are used where the conversation calls for them; (3) a shared goal is named; (4) one specific resolution is agreed. Pass at 3.",
    "The module assessment had no scale and referred to a 'module overview' that the reader never sees.", "assessment")
