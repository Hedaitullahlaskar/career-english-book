# Level 3 · Module 5 · Customer Service & Complaint Handling
PH = "The answer key contained an unfilled template placeholder; replaced with a sample answer."
TIME = ("In the dialogue Arif promises Mr. Chen an answer 'within the hour', and Lesson 5.5 resolves it the same evening; "
        "the email said he had been promised an answer by checkout tomorrow.")

rule("L3-M05-continuity-scenario", r"\(this module's continuity scenario\)", "(this module's scenario)",
     "Production language ('continuity scenario').", "production",
     targets=["CE-L03-M05-L02", "CE-L03-M05-L05"], expect=2)

# ---------- 5.4 Escalating a Complaint Internally ----------
L = "CE-L03-M05-L04"
fix(L, 'Guest complaint -- Room 412 (Chen) -- needs your review before checkout tomorrow',
    'Guest complaint — Room 412 (Chen) — needs your review tonight', TIME, "continuity")
fix(L, "I recommend we review this before his checkout tomorrow morning at 11:00, since I've told him\nhe'll have an answer by then.",
    "I recommend we review this tonight: I've told him he'll have an answer within the hour, and he checks out tomorrow at 11:00.",
    TIME, "continuity")
fix(L, "Recommended next step with a timeframe: 'I recommend we review this before his checkout tomorrow morning at 11:00.'",
    "Recommended next step with a timeframe: 'I recommend we review this tonight: I've told him he'll have an answer within the hour.'",
    "Matches the corrected email.", "continuity")
fix(L, "<p>Suggested answer: [open response following PAT-0081's four parts: context, why it needs attention, the customer's request, and a recommended next step with a timeframe]</p>",
    "<p>Sample: \"Subject: Customer request — order #5512 — needs your decision by 4 PM / Hi Mr. Das, A customer's wedding cake was delivered with the wrong design this morning. This needs your attention because the customer is requesting a full refund, which is above the store credit I can approve. I recommend a full refund plus a voucher, decided by 4 PM, since I've promised to call her back then. Thanks, Nadia\"</p>",
    PH, "production")

# ---------- 5.5 Service Recovery ----------
L = "CE-L03-M05-L05"
fix(L, "This module's continuity guest, Mr. David Chen, is handled by Arif",
    "Across this module, Mr. David Chen is handled by Arif", "Production language ('continuity guest').", "production")
fix(L, "<h2>The Full Recovery Scene</h2>\n<p>The connected dialogue below closes out Mr. Chen's arc: Ms. Noor, having reviewed Arif's escalation\nand consulted Dr. Rahman, delivers the recovery in person, with Arif present. See the dialogue above\nfor the full scene.</p>\n",
    "", "The section only described the dialogue and pointed to it as both 'below' and 'above'.", "structure")
fix(L, "recovery close. Graded holistically, in the same style as the Level 1 and Level 2 capstone\nrole-plays.</p>",
    "recovery close. The scoring scale is in the answer key for Exercise 2.</p>",
    "'Graded holistically' gave no scale.", "assessment")
fix(L, "Validate and partner is carried forward from L02, implicit in the warmth of the approach.",
    "Validate and partner: not repeated here — it was done earlier, in Lesson 5.2; Ms. Noor's warm, personal approach carries it on.",
    "Internal lesson code ('L02') replaced, and the point stated plainly.", "reference")
fix(L, "<p>What to listen/look for: Graded holistically: the performance",
    "<p>Score 0–5, one point for each stage shown (empathetic listening, de-escalation, an honest solution, a well-handled escalation where relevant, a close with an above-and-beyond gesture and a direct satisfaction check). Pass at 4. What to listen/look for: the performance",
    "The module assessment had no scale.", "assessment")
fix(L, "We've also arranged [a specific above-and-beyond gesture] to make this right properly.",
    "We've also arranged a complimentary late checkout for you tomorrow, to make this right properly.",
    "The sample answer contained an unfilled placeholder.", "production")
