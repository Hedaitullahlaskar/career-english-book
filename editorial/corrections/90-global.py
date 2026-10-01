# Whole-book mechanical rules. These run after every per-lesson fix
# (files are applied in name order), so per-lesson `find` strings match the
# baseline text, and replacement text is written in final form.

ALL = ("title", "objectives_html", "body_html", "practice_html", "purpose")

rule("restore-lost-blanks",
     r"<strong><em>(.*?)</em></strong>", r"___\1___",
     "Paired '___' blanks in fill-in scaffolds were converted to bold-italic markup, so the blanks "
     "disappeared and the sentence ran together (e.g. \"I'm responsible for . I report to .\").",
     "answer-key", flags=16, expect=5)  # 16 = re.DOTALL

rule("remove-theme-tags",
     r"\s*·\s*theme:[^<]*", "",
     "Internal content-planning tag ('theme: …') printed after the motivation quote.",
     "production", expect=58)

rule("industry-label-case",
     r"<li><strong>(hotel|healthcare|banking|retail):</strong>",
     lambda m: "<li><strong>" + m.group(1).capitalize() + ":</strong>",
     "Industry labels were inconsistently lower-case ('hotel:' beside 'Hotel:').",
     "typography")

rule("industry-label-it",
     r"<li><strong>it:</strong>", "<li><strong>IT:</strong>",
     "'it:' reads as the pronoun; the industry is IT.", "typography")

rule("dash-to-em-dash",
     r"\s+--\s+|\s+--(?=\S)|(?<=\S)--\s+", " — ",
     "Typewriter double hyphens replaced with a spaced em dash, the style already used elsewhere "
     "in the book.", "typography", fields=ALL)

rule("arrow",
     r"\s*->\s*", " → ",
     "ASCII arrows ('->') replaced with the arrow character already used elsewhere in the book.",
     "typography", fields=ALL)

rule("remove-internal-scene-slugs",
     r'<div class="dialogue-scene-label">[a-z0-9]+(?:-[a-z0-9]+)*</div>\s*', "",
     "Internal scene identifiers (e.g. 'step-3', '02-request', 'senior-executive-email') were printed as scene titles.",
     "production", fields=("body_html",), expect=75)
