# Level 3 · Module 2 · Report Writing
PH = "The answer key contained an unfilled template placeholder ('[open response …]'); replaced with a sample answer."

# ---------- 2.1 The Facts → Evidence → Analysis → Action → Recommendation Framework ----------
L = "CE-L03-M02-L01"
rule("L3-2.1-delay-arithmetic", r"35 minutes after the promised", "25 minutes after the promised",
     "Arithmetic error: ordered at 7:10 with a 30-minute promise means delivery was due at 7:40; delivered at 8:05 is 25 minutes late, not 35.",
     "factual", targets=[L], expect=3)

# ---------- 2.2 Daily and Weekly Reports ----------
L = "CE-L03-M02-L02"
fix(L, '[open response following: Summary + "Over the past week..." facts + Analysis + Recommendation + Key takeaway]',
    'Sample: "Summary: Front desk operations over the past week — steady arrivals, two late airport pickups. Facts: Over the past week, the desk handled 312 check-ins. Two airport pickups (Tuesday, Friday) arrived 30+ minutes late. Analysis: Both late pickups were booked after 9 PM, when the transport desk is closed and requests go by email only. Recommendation: I recommend that the night agent confirm every after-9 PM pickup by phone with the driver. Key takeaway: a normal week; the only recurring issue is late-evening pickup bookings."',
    PH, "production")

# ---------- 2.3 Incident and Complaint Reports ----------
L = "CE-L03-M02-L03"
rule("L3-2.3-blame-example-name", r"Priyanka", "Rupa",
     "The blame example had Priyanka, a front-office agent, leaving a housekeeping mop bucket; the example now names a housekeeping colleague, which keeps the point (never name and blame a colleague in the facts).",
     "continuity", fields=("body_html", "practice_html"), targets=[L], expect=5)
fix(L, '[open response following: Facts (occurred at/was observed that) + Evidence + Analysis + Contributing factor + Immediate action taken + Recommendation]',
    'Sample: "Facts: The incident occurred at approximately 7:20 PM in the restaurant. A guest received a dish containing peanuts after telling the server about a peanut allergy. The guest did not eat the dish. Evidence: The order ticket does not show the allergy note. Analysis: The allergy information appears not to have reached the kitchen. Contributing factor: the order system has no mandatory allergy field. Immediate action taken: the dish was replaced and the chef spoke to the guest. Recommendation: I recommend adding a required allergy field to the order screen this week."',
    PH, "production")

# ---------- 2.4 Performance and Operational Reports ----------
L = "CE-L03-M02-L04"
fix(L, 'the first version only lists the raw numbers, avoiding none of MIS-0086\'s data-dump problem.',
    'the first version only lists the raw numbers, which is exactly MIS-0086\'s data-dump problem.',
    "'Avoiding none of' was garbled.", "language")
fix(L, '[open response following: Facts stating the figures and their change + Analysis using an increase/decrease of, compared to, or on average + a specific Recommendation]',
    'Sample: "Facts: Room-service orders averaged 46 a day this week, compared to 38 a day last week — an increase of about 21%. Analysis: The increase began on Tuesday, the day the new in-room menu cards were introduced, which suggests the cards are driving more orders. Recommendation: I recommend adding one room-service server from 7 to 9 PM, the busiest window, for the next two weeks while we confirm the trend."',
    PH, "production")

# ---------- 2.5 Writing a Recommendation That Gets Acted On ----------
L = "CE-L03-M02-L05"
fix(L, 'for every report that lands on her desk:', 'for every report that lands on his desk:',
    "Dr. Rahman, the General Manager, is referred to as 'he' throughout the rest of the book.", "continuity")
fix(L, 'by early afternoon on at least one Tuesday and one Friday each week.', 'by early afternoon on every Tuesday and Friday.',
    "'At least one Tuesday and one Friday each week' is meaningless (each week has only one of each); the evidence that follows shows it happened on all of them.",
    "factual")
fix(L, 'by 3:00 PM on 4 of the last 4 Tuesdays and Fridays,', 'by 3:00 PM on all eight Tuesdays and Fridays in that period,',
    "'4 of the last 4 Tuesdays and Fridays' miscounts: four weeks contain eight such days.", "factual")
fix(L, 'This assessment is\ndelivered as this lesson\'s writing activity.', 'This is Exercise 3 below.',
    "Production language ('delivered as this lesson's writing activity').", "production")
fix(L, 'focused on the double-booking error observed in three of the last five bookings.', 'focused on the three double-booking errors logged in the past two weeks.',
    "'Three of the last five bookings' would mean most bookings were double-booked, which is not what the example intends.", "language")
fix(L, '<p>Suggested answer: [open response: a full report following the five-part framework, closing with a recommendation that names a specific action, who/what it involves, and ties back to the evidence and analysis already given] What to listen/look for:',
    '<p>Score 0–5, one point for each framework part that is present and correctly separated. Pass at 4 (the Recommendation must be one of the points). What to listen/look for:',
    "The module assessment key was a template placeholder with no scale.", "assessment")
