# Level 4 · Module 6 · Escalation & Crisis Communication
D = 16
PH = "The answer key contained an unfilled template placeholder; replaced with a sample answer."

L = "CE-L04-M06-L02"
fix(L, "the reservation records for tonight's\nwedding block, entered only in the crashed system two days ago, cannot be recovered before the\nparty arrives. Mr. Abrar Khan,",
    "the reservation records for several of tonight's arrivals, entered only in the crashed system two days ago, cannot be recovered in time. One of them is Mr. Abrar Khan, who,",
    "The opening said the lost records belonged to tonight's wedding block, but the guest affected (Mr. Khan, an anniversary guest) is not part of the wedding.",
    "continuity")
fix(L, "celebrating his twentieth anniversary, booked the hotel's river-view\nsuite months in advance -- and there is no walk-in equivalent available tonight.",
    "celebrating his twentieth anniversary, booked the hotel's river-view suite months in advance — and no other river-view suite is free tonight.",
    "'No walk-in equivalent' was unclear; the point is that no comparable suite is free.", "language")
fix(L, "the same bad news you delivered in A03,", "the same bad news you delivered in Exercise 3,", "Internal activity code ('A03').", "production")
fix(L, "Suggested answer: Client: [name], [order/booking]. Update: [item] unavailable due to [brief honest reason]; client was informed directly. Next step: [specific alternative offered], accepted by the client.",
    "Sample: Client: Ms. Farzana Ali, wedding cake order #318. Update: the three-tier design is unavailable for Saturday because our pastry chef is off sick; the client was informed directly by phone today. Next step: a two-tier cake in the same design at a 20% discount, accepted by the client.",
    PH, "production")

fix("CE-L04-M06-L03", "identify the four parts of Arif's pushback", "identify the four parts of the pushback from Ms. Noor and Arif",
    "In the dialogue the acknowledgment of urgency comes from Ms. Noor, not Arif (as the answer key itself says).", "answer-key")

fix("CE-L04-M06-L04", "Compare worked_example_a and worked_example_b in the dialogue file.", "Compare version A and version B of Arif's email in the Listen &amp; Read section.",
    "Production artifact: the exercise referred to source-file names ('worked_example_a … in the dialogue file').", "production")

L = "CE-L04-M06-L05"
fix(L, "<h2>Full Crisis Scenario</h2>\n<p>The connected sequence below chains together an initial calm alert, a piece of bad news delivered\npartway through, a pushback against an unrealistic deadline, and a written crisis update -- ending\nin resolution. See the dialogue above for the full sequence, including the written update as its own\nscene.</p>\n",
    "", "The section only described the dialogue and pointed to it as both 'below' and 'above'.", "structure")
fix(L, "graded holistically as one connected performance, the same way Level 3's synthesis lesson graded a full professional week.",
    "scored with the scale in the answer key for Exercise 3.", "'Graded holistically' gave no scale.", "assessment")
rule("L4-6.5-prompt-quotes", r"<p>'(Module 6 Assessment:.*?)'</p>", r"<p>\1</p>",
     "Stray quotation marks around the exercise prompt.", "typography", fields=("practice_html",), flags=D, targets=[L], expect=1)
fix(L, "<p>Suggested answer: [open response applying PAT-0144, PAT-0145, PAT-0146, or PAT-0147 to an IT-outage or supply-chain-disruption context, keeping the chosen pattern's structure intact]</p>",
    "<p>Sample (IT outage, calm alert): \"Here's what we know so far: the customer portal went down at 9:12 and logins are failing for every client. We're actively working on it — the database team is on the call now. I'll update you as soon as they confirm the cause, and in any case by 9:45.\" Check: the chosen pattern's structure is kept exactly; only the industry details change.</p>",
    PH, "production")
fix(L, "Graded holistically, the same style as prior Level 3 and Level 4 module and synthesis assessments.",
    "Score 0–5, one point for each of CF-0023's five stages done well; pass at 4, and the calm opening and the written update must both be among them.",
    "The module assessment had no scale.", "assessment")

fix("CE-L04-M06-L01", "I don't even know where to\nstart--\"", "I don't even know where to start—\"",
    "A broken-off sentence is marked with an em dash, not a double hyphen.", "typography")
