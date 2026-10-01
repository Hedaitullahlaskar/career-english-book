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
     fields=("practice_html", "body_html"))

rule("stage-direction-brackets",
     r"\[(Later|A short while later)\]", r"(\1)",
     "Stage directions use parentheses everywhere else in the book's dialogues.", "typography",
     fields=("body_html", "practice_html"), expect=3)

rule("dialogue-note-paragraph-breaks",
     r'(<div class="dialogue-note">)(.*?)(</div>)',
     lambda m: m.group(1) + __import__("re").sub(r"\n\s*\n", "<br><br>\n", m.group(2)) + m.group(3),
     "Emails and messages shown inside dialogue boxes kept their blank-line paragraph breaks only in the source; "
     "browsers collapsed them, so subject line, greeting, body and sign-off ran together on one line.",
     "structure", fields=("body_html",), flags=16)

def _blockquote_lines(m):
    import re as _re
    body = m.group(2)
    body = _re.sub(r"\n(?=(?:- |\d+[.)] |<strong>))", "<br>\n", body)
    body = _re.sub(r"((?:Thanks|Best regards|Best|Kind regards|Regards|Many thanks|Warm regards|Sincerely),)\n", r"\1<br>\n", body)
    return m.group(1) + body + m.group(3)

rule("blockquote-line-breaks",
     r"(<blockquote>)(.*?)(</blockquote>)", _blockquote_lines,
     "Model emails, agendas and minutes kept their line structure (list items, labelled lines, sign-offs) only as source line breaks, "
     "which browsers collapse — so 'Agenda: 1. … 2. … 3. …' and 'Thanks, Arif' ran together on one line.",
     "structure", fields=("body_html",), flags=16)

rule("continuity-scenario-label", r"\(this (module|lesson)'s continuity scenario\)", r"(this \1's scenario)",
     "Production language ('continuity scenario') in industry-overlay labels.", "production", fields=("body_html",))
rule("scene-underscore-labels", r"Scene_([ab])", lambda m: "Scene " + m.group(1).upper(),
     "Conversion artifact ('Scene_a') in answer keys.", "typography", fields=("practice_html", "body_html"))

rule("remove-empty-bengali-hindi-sections",
     r"<h2>Bengali/Hindi [Ss]upport</h2>\s*<p><em>\(none for this lesson[^)]*\)</em></p>\s*", "",
     "Sections that existed only to say there was no Bengali/Hindi note 'per the curriculum map'. "
     "How to Use This Book explains that not every lesson uses every section.",
     "production", fields=("body_html",), flags=16)

rule("remove-empty-overlay-sections-2",
     r"<h2>Industry [Oo]verlays</h2>\s*<p>(?:<em>\(none for this lesson[^)]*\)</em>|Example variety only, per the curriculum map\.)</p>\s*", "",
     "Industry Overlays sections whose only content was an internal note ('Example variety only, per the curriculum map').",
     "production", fields=("body_html",), flags=16)

def _cap_after(m):
    return m.group(1).upper()

rule("overlay-curriculum-note",
     r"Example variety only(?:, per the curriculum map| for this lesson)? — (\w)", _cap_after,
     "Internal production note ('Example variety only, per the curriculum map') removed from the start of the overlay text.",
     "production", fields=("body_html",))

rule("parallel-contexts-curriculum-note", r"contexts, per the curriculum map — ", "contexts — ",
     "Internal production note ('per the curriculum map') removed.", "production", fields=("body_html",), expect=1)

_US = {"organis": "organiz", "Organis": "Organiz", "apologis": "apologiz", "Apologis": "Apologiz", "sceptic": "skeptic",
       "finalis": "finaliz", "recognis": "recogniz", "behaviour": "behavior", "labelled": "labeled", "centre": "center",
       "practis": "practic", "enquir": "inquir"}

rule("us-spelling", r"\b(?:" + "|".join(_US) + r")", lambda m: _US[m.group(0)],
     "The book uses American spelling throughout; British spellings that crept into corrected text are normalised.",
     "typography", fields=("body_html", "practice_html", "objectives_html", "purpose"))

rule("listening-comprehension-label", r'exercise-type">Listening Comprehension<', 'exercise-type">Comprehension<',
     "No audio recordings exist yet; every one of these prompts now asks the reader to read the text (or hear a partner read it), so the label no longer promises listening.",
     "audio", fields=("practice_html",), expect=13)


def _tag_indic(m):
    """Wrap Bengali / Devanagari runs that sit outside any bn/hi span, so they get the right font and lang."""
    import re as _re
    html = m.group(0)
    out, stack = [], []
    for part in _re.split(r"(<[^>]+>)", html):
        if part.startswith("<"):
            tag = _re.match(r"</?\s*(\w+)", part)
            if tag and tag.group(1) == "span":
                if part.startswith("</"):
                    if stack:
                        stack.pop()
                else:
                    cls = _re.search(r'class="([^"]*)"', part)
                    stack.append(cls.group(1) if cls else "")
            out.append(part)
        elif any(c in ("bn", "hi") for c in stack):
            out.append(part)
        else:
            part = _re.sub(r"[\u0980-\u09FF]+(?:[ \u0980-\u09FF]*[\u0980-\u09FF])?", lambda x: f'<span class="bn">{x.group(0)}</span>', part)
            part = _re.sub(r"[\u0900-\u0963\u0966-\u097F]+(?:[ \u0900-\u0963\u0966-\u097F]*[\u0900-\u0963\u0966-\u097F])?", lambda x: f'<span class="hi">{x.group(0)}</span>', part)
            out.append(part)
    return "".join(out)


rule("tag-inline-bengali-hindi", r"(?s)\A.*\Z", _tag_indic,
     "Bengali and Hindi words quoted inside English sentences had no language tag, so they could not get the Bengali/Hindi font or lang attribute.",
     "l1-support", fields=("body_html", "practice_html"),
     targets=["CE-L01-M01-L03", "CE-L01-M02-L01", "CE-L01-M02-L04", "CE-L03-M07-L01", "CE-L03-M08-L03"])

rule("danda-language-tag", r'<span class="hi">।</span>', "।",
     "The Bengali full stop (danda, ।) was tagged as Hindi in the middle of Bengali sentences; it is shared punctuation and now takes the surrounding language.",
     "l1-support", fields=("body_html", "practice_html"), expect=18)
