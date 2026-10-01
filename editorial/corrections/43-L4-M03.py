# Level 4 · Module 3 · Persuasion & Influence

rule("L4-3.2-cost-placeholder", r"The kiosk costs \[X\] to install\.", "The kiosk costs around four hundred thousand taka to install.",
     "An unfilled placeholder ('[X]') stood in for a figure the lesson's own dialogue gives.", "production",
     fields=("body_html",), targets=["CE-L04-M03-L02"], expect=3)
rule("L4-3.x-scene-labels", r"Scene_([ab])", lambda m: "Scene " + m.group(1).upper(),
     "Conversion artifact ('Scene_a') in the answer keys.", "typography",
     fields=("practice_html",), targets=["CE-L04-M03-L02", "CE-L04-M03-L03"])

L = "CE-L04-M03-L04"
fix(L, "the Meridian conference arrives -- three hundred guests checking in over two days.",
    "the Meridian conference arrives — forty-five rooms checking in on the same afternoon.",
    "The Meridian group is 45 rooms (Lesson 2.4); 'three hundred guests' contradicted the rest of the book.", "continuity")
fix(L, "This assessment is delivered as this lesson's role-play activity,\nand is scored primarily on whether your response addresses the listener's\nactual doubt, not merely on how confidently the original pitch was delivered.",
    "It is Exercise 3 below. Score 0–4: (1) a clear claim with specific evidence; (2) framing relevant to the listener; (3) the listener's actual doubt is diagnosed and addressed — this point is required to pass; (4) a shared-goal or reciprocity close. Pass at 3.",
    "Production language ('delivered as this lesson's role-play activity') and no scale.", "assessment")
fix(L, "<p>MODULE 3 ASSESSMENT.", "<p>Module 3 assessment.", "Consistent capitalisation with the other module assessments.", "typography")
fix(L, '<span class="answer-number">3.</span> <p>What to listen/look for: Scored',
    '<span class="answer-number">3.</span> <p>Score 0–4 as described in the Module Assessment section above. What to listen/look for: Scored',
    "Tied the key to the scoring scale.", "assessment")
