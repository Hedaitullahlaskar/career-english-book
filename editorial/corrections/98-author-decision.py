# Phase: Author decision
# For changes that carry out a decision recorded in editorial/AUTHOR-DECISIONS.md.
#
# Every fix(...) or rule(...) in this file is logged with source "Author decision"
# (apply_corrections.py adds the label; an optional source= adds detail, e.g. source="Decision A (linen contract)").
# Rows are appended after the 941 historical entries, which must not change (correction-log-frozen.json).
# More files for this phase can be added as 98-author-decision-<topic>.py.
#
# Decisions given by the author on 3 October 2026: 1A, 2 approve, 3A, 4 British/UK dates, 5A (keep "to hand": no change).

# --- Decision 1A: the linen contract is a two-year contract (2027-2028), as signed in Level 4 Module 1. ---
# The capstone call now comes as that two-year term ends, and the Lesson 8.2 example returns at the end of the term.
D1 = "Decision 1A (linen contract: two-year term, as signed in Level 4 Module 1)"
WHY1 = "Level 4 Module 1 signs the linen contract for two years at a fixed rate; the renewal now comes at the end of that term, not after one year."
L = "CE-L04-CAPSTONE"
fix(L, "calls about the annual renewal of the linen supply contract Arif first negotiated a year ago in Module 1. This year the conversation opens differently:",
    "calls about renewing the two-year linen supply contract Arif negotiated in Module 1, which ends this quarter. This time the conversation opens differently:",
    WHY1, "continuity", source=D1)
fix(L, "and the tone is noticeably firmer than last year's call.", "and the tone is noticeably firmer than in their first negotiation.",
    WHY1, "continuity", source=D1)
fix(L, "on a relationship that already has a year of history behind it.", "on a relationship that already has two years of history behind it.",
    WHY1, "continuity", source=D1)
fix(L, "and given a year of steady, growing volume with you,", "and given two years of steady, growing volume with you,",
    WHY1, "continuity", source=D1)
fix(L, "if we commit to a two-year term instead of renewing year to year, would that let you come down closer to 7%?",
    "if we commit to another two-year term instead of a one-year renewal, would that let you come down closer to 7%?",
    WHY1, "continuity", source=D1)
fix(L, "we've agreed on an 8% increase on this year's per-unit rate, fixed for a two-year term,",
    "we've agreed on an 8% increase on the current per-unit rate, fixed for a further two-year term,",
    WHY1, "continuity", source=D1)
fix(L, "Good doing business with you again this year.", "Good doing business with you again.",
    WHY1, "continuity", source=D1)
fix(L, "(the vendor relationship's first year, the client relationship's history)",
    "(the vendor relationship's first two years, the client relationship's history)",
    WHY1, "continuity", source=D1)
fix("CE-L04-M08-L02", "returns a year later for the contract's renewal: \"As our relationship has grown this past year, it's worth revisiting the delivery terms as well as the rate.\"",
    "returns at the end of the two-year contract for its renewal: \"As our relationship has grown over the past two years, it's worth revisiting the delivery terms as well as the rate.\"",
    WHY1, "continuity", source=D1)

# --- Decision 2 (approved): one code per vocabulary item. The first code in book order is kept; the later ---
# entry becomes a recycled mention of it. The later codes are retired as gaps; nothing is renumbered.
D2 = "Decision 2 (one code per vocabulary item)"
fix("CE-L01-M02-L01", "<td><code>V-0105</code></td><td><strong>colleague</strong>",
    "<td><code>V-0018</code> (recycled)</td><td><strong>colleague</strong>",
    "\"colleague\" had two codes (V-0018, V-0105); V-0018 is kept and V-0105 retired.", "reference", source=D2)
fix("CE-L01-M02-L02", "<td><code>V-0106</code></td><td><strong>team lead</strong>",
    "<td><code>V-0019</code> (recycled)</td><td><strong>team lead</strong>",
    "\"team lead\" had two codes (V-0019, V-0106); V-0019 is kept and V-0106 retired.", "reference", source=D2)
fix("CE-L01-M06-L01", "<td><code>V-0018</code> / <code>V-0105</code></td>", "<td><code>V-0018</code></td>",
    "The recap table listed both codes for \"colleague\"; V-0105 is retired.", "reference", source=D2)
fix("CE-L01-M06-L01", "<td><code>V-0019</code> / <code>V-0106</code></td>", "<td><code>V-0019</code></td>",
    "The recap table listed both codes for \"team lead\"; V-0106 is retired.", "reference", source=D2)
fix("CE-L01-M07-L01", "<li><code>V-0197</code> <strong>respectful</strong>",
    "<li><code>V-0003</code> <strong>respectful</strong> (recycled from Lesson 1.1, now as a tone label)",
    "\"respectful\" had two codes (V-0003, V-0197); V-0003 is kept and V-0197 retired.", "reference", source=D2)
fix("CE-L02-M04-L02", "<strong>quick question</strong> (V-0289)", "<strong>quick question</strong> (V-0148, recycled from Level 1)",
    "\"quick question\" had two codes (V-0148, V-0289); V-0148 is kept and V-0289 retired.", "reference", source=D2)
fix("CE-L02-M04-L03", "<strong>whenever you get a chance</strong> (V-0294)", "<strong>whenever you get a chance</strong> (V-0138, recycled from Level 1)",
    "\"whenever you get a chance\" had two codes (V-0138, V-0294); V-0138 is kept and V-0294 retired.", "reference", source=D2)
fix("CE-L05-M04-L01", "<li><code>V-0228</code> <strong>the reasoning behind this is</strong>",
    "<li><code>V-0680</code> <strong>the reasoning behind this is</strong> (recycled from Level 4)",
    "\"the reasoning behind this is\" had two codes (V-0680 in Level 4, V-0228 in Level 5); V-0680 is kept and V-0228 retired.", "reference", source=D2)
fix("CE-L05-M06-L02", "<strong>the reasoning behind this is</strong> (V-0228)", "<strong>the reasoning behind this is</strong> (V-0680)",
    "V-0228 is retired in favour of V-0680 (same expression).", "reference", source=D2)
fix("CE-L05-M06-L02", "(V-0228, V-0229)", "(V-0680, V-0229)",
    "V-0228 is retired in favour of V-0680 (same expression).", "reference", source=D2)
fix("CE-L05-M05-L04", "<strong>in the interest of time</strong> (V-0248)", "<strong>in the interest of time</strong> (V-0693, recycled from Level 4)",
    "\"in the interest of time\" had two codes (V-0693 in Level 4, V-0248 in Level 5); V-0693 is kept and V-0248 retired.", "reference", source=D2)

# --- Decision 3A: Arif cites his own Level 4 kiosk pilot when challenged in Level 5 Lessons 6.3-6.4. ---
D3 = "Decision 3A (Arif cites his Level 4 kiosk pilot)"
WHY3 = "Arif's own six-week kiosk pilot (Level 4 Lesson 5.1: check-in time down sixty percent) was seen by both challengers; it is now part of his evidence."
L = "CE-L05-M06-L03"
fix(L, "Here's the data behind that claim — the two hotels in our group that paired a kiosk with a staff member for the first month saw adoption above eighty percent within six weeks.",
    "Here's the data behind that claim — our own six-week kiosk pilot here cut average check-in time by sixty percent, and the two hotels in our group that paired a kiosk with a staff member for the first month saw adoption above eighty percent within six weeks.",
    WHY3, "continuity", source=D3)
fix(L, "Here's the data behind that claim: the two hotels in our group that paired a kiosk with a staff member for the first month saw adoption above eighty percent within six weeks.",
    "Here's the data behind that claim: our own six-week kiosk pilot here cut average check-in time by sixty percent, and the two hotels in our group that paired a kiosk with a staff member for the first month saw adoption above eighty percent within six weeks.",
    WHY3, "continuity", source=D3)
fix(L, "Data: \"the two hotels... saw adoption above eighty percent within six weeks.\"",
    "Data: \"our own six-week kiosk pilot here cut average check-in time by sixty percent, and the two hotels... saw adoption above eighty percent within six weeks.\"",
    WHY3, "answer-key", source=D3)
fix("CE-L05-M06-L04", "Here's the data behind that claim — the two hotels in our group that staffed a kiosk for the first month saw adoption above eighty percent within six weeks.",
    "Here's the data behind that claim — our own six-week kiosk pilot here cut average check-in time by sixty percent, and the two hotels in our group that staffed a kiosk for the first month saw adoption above eighty percent within six weeks.",
    WHY3, "continuity", source=D3)

# --- Decision 4: British/UK date style (20 September). The other four full dates already use it. ---
D4 = "Decision 4 (British/UK date style)"
WHY4 = "House style: dates are written day-month (20 September), as in the book's other full dates."
L = "CE-L04-M02-L04"
fix(L, "On September 20, the", "On 20 September, the", WHY4, "typography", source=D4)
fix(L, "generated on September 25 would", "generated on 25 September would", WHY4, "typography", source=D4)
fix(L, "corrected to C-14 on September 23, the same", "corrected to C-14 on 23 September, the same", WHY4, "typography", source=D4)

# --- Decision 5A: keep "to hand" as an intentional British-English teaching item. No change. ---
