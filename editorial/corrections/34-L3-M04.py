# Level 3 · Module 4 · Presentations I
DATA = ("The satisfaction figures in this module must tell one story: May 3.8, June 3.9, July 4.3, August 4.4 — "
        "a steady rise with a sharp jump between June and July and a levelling-off in August, as the dialogue in Lesson 4.2 says.")

# ---------- 4.1 Opening a Presentation ----------
L = "CE-L03-M04-L01"
rule("L3-4.1-last-month", r"last month was 4\.2", "last month was 4.4",
     DATA + " 'Last month' (August) was 4.4, not 4.2.", "factual", fields=("body_html", "practice_html"), targets=[L], expect=3)
rule("L3-4.1-july", r"in July it was 4\.0", "in July it was 4.3",
     DATA + " July was 4.3, not 4.0.", "factual", fields=("body_html", "practice_html"), targets=[L], expect=2)

# ---------- 4.2 Explaining Slides, Charts, and Data ----------
L = "CE-L03-M04-L02"
rule("L3-4.2-narrated-figures", r"June, 4\.0\. July, 4\.2\.", "June, 3.9. July, 4.3.",
     DATA + " The read-aloud example rose in equal 0.2 steps, which contradicts the 'sharp rise between June and July' and 'leveled off in August' described for the same chart.",
     "factual", targets=[L], expect=2)

# ---------- 4.5 Handling Questions ----------
L = "CE-L03-M04-L05"
fix(L, "This module's continuity character, Arif, delivers one presentation from open to close:",
    "Across this module, Arif delivers one presentation from open to close:", "Production language ('continuity character').", "production")
rule("L3-4.5-assessment-key", r"Suggested answer: \[open response chaining[^\]]*\] What to listen/look for:",
     "Score 0–5, one point for each step shown below (pass at 4, and the question handling must be one of the points):",
     "The module assessment key was a template placeholder pointing to an unspecified holistic grade; the existing criteria now form a 5-point scale.",
     "assessment", fields=("practice_html",), targets=[L], expect=1)
