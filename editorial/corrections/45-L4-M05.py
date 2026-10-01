# Level 4 · Module 5 · Presentations II

fix("CE-L04-M05-L01", "Listen to (or read) both versions", "Read both versions", "No audio recording exists yet.", "audio")

L = "CE-L04-M05-L02"
COST = ("The 'sixty-percent figure' is the drop in check-in time, not a cost figure, so costs cannot be 'included in' it. "
        "The challenge and the answer now refer to the cost comparison, which is what Mr. Kabir is actually questioning.")
fix(L, "the software licensing cost anywhere in here.", "the software licensing cost anywhere in the cost comparison.", COST, "factual")
fix(L, "the software licensing cost anywhere in this figure.", "the software licensing cost anywhere in the cost comparison.", COST, "factual")
rule("L4-5.2-cost-reference", r"included in (?:that|the) sixty-percent figure", "included in the cost comparison",
     COST, "factual", fields=("body_html", "practice_html"), targets=[L], expect=4)

fix("CE-L04-M05-L03", "(recycled, L3-M4-L04)", "(recycled from Level 3, Lesson 4.4)", "Internal lesson code replaced.", "reference")

L = "CE-L04-M05-L04"
fix(L, "(recycled, L04-M05-L01)", "(recycled from Lesson 5.1)", "Internal lesson code replaced.", "reference")
fix(L, "This level's Persuasion &amp; Influence module taught that people are moved by more than facts alone --\na well-chosen example or story does work that a number by itself can't.",
    "This level's Persuasion &amp; Influence module showed that the same fact lands differently depending on how it is framed; a well-chosen example or story is one of the strongest frames, doing work that a number by itself can't.",
    "Module 3 taught framing, not storytelling as such; the sentence now describes what it actually taught.", "reference")
fix(L, "This is the Module 5 assessment task.</p>",
    "Score 0–6, one point for each of CF-0022's six moves shown clearly; pass at 5, and the tough-question move must be one of them.</p>",
    "The module assessment had no scale.", "assessment")
