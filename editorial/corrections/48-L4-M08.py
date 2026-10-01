# Level 4 · Module 8 · Advanced Client & Vendor Relations
D = 16

L = "CE-L04-M08-L01"
fix(L, "The habit that keeps a relationship strong over the course of our\nrelationship is a simple one:",
    "The habit that keeps a long-term relationship strong is a simple one:",
    "Garbled sentence: the vocabulary phrase 'over the course of our relationship' had been pasted into the explanation.", "language")
fix(L, "Reuses L3-M6-L01's welcome", "Reuses Level 3 Lesson 6.1's welcome", "Internal lesson code replaced.", "reference")

L = "CE-L04-M08-L02"
ANCHOR = ("Module 1 teaches that an anchor states a grounded, specific position; 'a modest increase' gave no figure to negotiate from. "
          "The same figure is used everywhere the anchor is quoted.")
rule("L4-8.2-anchor-figure", r"we'd be looking at a modest increase( per room)?\s+to reflect", r"we'd be looking at an increase of about 8%\1 to reflect",
     ANCHOR, "factual", fields=("body_html",), flags=D, targets=[L], expect=2)
fix(L, "a modest increase reflects the added space", "an increase of about 8% reflects the added space", ANCHOR, "factual")
fix(L, "based on what we've seen with bookings of this size elsewhere, a modest increase.", "based on what we've seen with bookings of this size elsewhere, an increase of about 8%.", ANCHOR, "answer-key")
fix(L, "So, to confirm -- three meeting rooms, four days, at last year's rate, locked in",
    "So, to confirm — three original meeting rooms plus two new ones, four days, at this year's per-room rate, locked in",
    "The worked example confirmed 'three meeting rooms … at last year's rate', contradicting the dialogue and the trade it had just made (five rooms, this year's rate).", "continuity")
rule("L4-8.2-module-1", r"Reused M1 ", "Reused Module 1 ", "Internal abbreviation ('M1') written out.", "reference",
     fields=("body_html",), targets=[L], expect=2)

L = "CE-L04-M08-L04"
fix(L, "state plainly what I can offer is, be upfront about what\ncan't be promised,",
    "state plainly what you can offer (\"What I can offer is...\"), be upfront about what can't be promised,",
    "Garbled sentence: the taught phrase had been dropped into the explanation ungrammatically.", "language")
rule("L4-8.4-original-rooms", r"\btwo original (meeting )?rooms", r"three original \1rooms",
     "The renewed contract (Lesson 8.2 and this lesson's opening) has three original meeting rooms plus two new ones; the offer said 'the two original rooms'.",
     "continuity", fields=("body_html", "practice_html"), targets=[L], expect=4)
fix(L, "(see the exercises below, A03)", "(Exercise 3 below)", "Internal activity code ('A03').", "production")
fix(L, "(see the exercises below, A02)", "(Exercise 2 below)", "Internal activity code ('A02').", "production")
fix(L, "<p>What to listen/look for: The reset names the change plainly,",
    "<p>Score 0–4, one point for each part of PAT-0160 done well; pass at 3, and the change must be raised promptly. What to listen/look for: The reset names the change plainly,",
    "The lesson assessment had no scale.", "assessment")

L = "CE-L04-M08-L05"
TIME = ("Timeline error: this scene is month two of a new two-year renewal, and the event is Meridian's second conference at the hotel, "
        "so Ms. Cruz cannot be 'two years into' the agreement and the relationship is not 'three years' old; the third year is the extension just agreed.")
fix(L, "thinking about adding a workshop day to next year's event.", "thinking about adding a workshop day to this year's event.",
    "In the next scene the workshop day is added to this year's event.", "continuity")
fix(L, "given we're already two years into this agreement?", "given we've just committed to two years with you?", TIME, "continuity")
fix(L, "Ms. Cruz, welcome back -- three years now, and still going strong.", "Ms. Cruz, welcome back — and with three years now agreed ahead of us.", TIME, "continuity")
fix(L, "marking how much the now three-year Meridian relationship means to the hotel.",
    "marking how much the Meridian relationship, now extended to three years, means to the hotel.", TIME, "continuity", count=2)
fix(L, "I'll personally monitor your tickets myself until", "I'll monitor your tickets personally until",
    "Redundant 'personally … myself'.", "language")
rule("L4-8.5-see-dialogue", r"<p>See the dialogue above for the full connected scenario.*?</p>\s*", "",
     "The paragraph only pointed back to the dialogue and repeated the same 'three-year' error.", "structure",
     fields=("body_html",), flags=D, targets=[L], expect=1)
fix(L, "graded holistically using\n CF-0025 (see the exercises below).", "scored with the scale in the answer key for Exercise 3.",
    "'Graded holistically' gave no scale.", "assessment")
fix(L, "from start to finish (1)", "from start to finish: (1)", "Missing colon before the numbered list.", "typography")
fix(L, "(avoiding MIS-0190's compounding-problem trap)", "(avoiding MIS-0189's wait-and-hope trap)",
    "Wrong mistake code: the expectation reset relates to MIS-0189 (waiting and hoping); MIS-0190 is about leaving a small problem unaddressed.", "reference")
fix(L, "Graded holistically, the same style as prior Level 3 and Level 4 module and synthesis assessments, and directly feeding into the Level 4 capstone,",
    "Score 0–5, one point for each CF-0025 stage done well; pass at 4, and the accountability moment and the expectation reset must both be among them. This leads directly into the Level 4 capstone,",
    "The module assessment had no scale.", "assessment")
