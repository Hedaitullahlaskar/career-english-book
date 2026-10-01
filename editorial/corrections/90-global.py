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

rule("remove-empty-overlay-sections",
     r"<h2>Industry Overlays</h2>\s*<p>None for this lesson[^<]*</p>\s*", "",
     "Sections that existed only to say they were empty ('None for this lesson — … per the curriculum map'). "
     "How to Use This Book already explains that not every lesson uses every section.",
     "production", fields=("body_html",), expect=12)

rule("note-only-listen-boxes",
     r'<div class="dialogue-box">\s*<div class="dialogue-box-label">[^<]*</div>\s*<div class="dialogue-note">(.*?)</div>\s*</div>',
     r"<p>\1</p>",
     "'Listen & Read' boxes that contained no dialogue, only a description of the lesson's worked examples, now read as an introductory paragraph.",
     "structure", fields=("body_html",), flags=16, expect=8)

rule("bengali-hindi-heading",
     r"<h2>Professional Tone</h2>(\s*<blockquote>\s*<p>(?:<strong>)?Bengali/Hindi note)",
     r"<h2>Bengali/Hindi support</h2>\1",
     "Sections headed 'Professional Tone' contained only a Bengali/Hindi note, so the heading misdescribed the content.",
     "structure", fields=("body_html",),
     targets=["CE-L02-M05-L01", "CE-L03-M01-L01", "CE-L03-M02-L01", "CE-L03-M05-L01", "CE-L03-M07-L01",
              "CE-L03-M07-L04", "CE-L03-M08-L01", "CE-L03-M08-L03"], expect=8)

rule("arrow-escaped",
     r"\s*-&gt;\s*", " → ",
     "HTML-escaped ASCII arrows ('-&gt;') replaced with the arrow character.", "typography", fields=ALL)

rule("criteria-list-punctuation",
     r"\.;\s", "; ",
     "Marking-criteria lists were joined with '.;' (a full stop followed by a semicolon).", "typography",
     fields=("practice_html", "body_html"), expect=18)

rule("stage-direction-brackets",
     r"\[(Later|A short while later)\]", r"(\1)",
     "Stage directions use parentheses everywhere else in the book's dialogues.", "typography",
     fields=("body_html", "practice_html"), expect=3)
