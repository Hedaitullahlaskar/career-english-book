"""Build the print edition (one HTML file) from book-data.json and reference-index.json.

The PDF is rendered from this file by editorial/print/render_pdf.js (headless Chrome).
Page numbers for the table of contents and the index come from a previous render
(editorial/print/pages.json); without it, placeholders are used.

Usage: python editorial/tools/build_print.py
"""
import html
import json
import re
import sys
from pathlib import Path

from book import ROOT, load

sys.stdout.reconfigure(encoding="utf-8")
OUT_DIR = ROOT / "editorial" / "print"
OUT = OUT_DIR / "career-english-print.html"
PAGES = OUT_DIR / "pages.json"


def site_css():
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
    return css


def how_to_use_html():
    """Reuse the How to Use text from the website so the two editions never drift apart."""
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    block = re.search(r"var HOW_TO_USE = \[(.*?)\]\.join", src, re.S).group(1)
    parts = re.findall(r"'((?:[^'\\]|\\.)*)'", block)
    text = "".join(p.replace("\\'", "'") for p in parts)
    # in print, the index is in the back matter rather than behind a link
    text = text.replace('<a href="#codes">Reference index</a>', "Reference Index at the back of the book")
    text = text.replace(" The <a", " The <a").replace("codes in the lessons link there too", "use it to find the page where each one is introduced")
    return re.sub(r"<h2>Tracking your progress</h2>.*$", "", text, flags=re.S)


def demote(fragment):
    """Lesson content headings sit below the book's own Level/Module/Lesson headings."""
    fragment = re.sub(r"<(/?)h4\b", r"<\1h6", fragment)
    fragment = re.sub(r"<(/?)h3\b", r"<\1h5", fragment)
    fragment = re.sub(r"<(/?)h2\b", r"<\1h4", fragment)
    return fragment


def tag_languages(fragment):
    fragment = fragment.replace('<span class="bn">', '<span class="bn" lang="bn">')
    return fragment.replace('<span class="hi">', '<span class="hi" lang="hi">')


def esc(s):
    return html.escape(str(s), quote=True)


PRINT_CSS = r"""
@page { size: A4; margin: 20mm 17mm 20mm 17mm; }
@page cover { margin: 0; }
html, body { background: #fff !important; color: #20242B; height: auto; overflow: visible; }
body { font-size: 10.4pt; line-height: 1.5; }
:root { --bg:#fff; --surface:#fff; --shadow:none; }
.page-break { break-before: page; }
.cover-page { page: cover; break-after: page; height: 297mm; width: 210mm; margin: 0; padding: 0; overflow: hidden; }
.cover-page img { width: 210mm; height: 297mm; object-fit: cover; display: block; }
.front { break-before: page; }
.front h1, .level-title h1 { font-size: 26pt; }
.edition p { font-size: 9.5pt; color: #3b434d; }
.toc { break-before: page; }
.toc-level { font-family: var(--font-display); font-weight: 700; font-size: 13pt; margin: 14pt 0 4pt; color: var(--lc); display: flex; }
.toc-module { font-weight: 700; font-size: 9.8pt; margin: 6pt 0 2pt 4mm; display: flex; }
.toc-lesson { font-size: 9.2pt; margin: 0 0 0 9mm; display: flex; }
.toc-row .t { flex: 1; overflow: hidden; white-space: nowrap; }
.toc-row .t::after { content: " . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."; color: #9aa3ad; }
.toc-row .pg { width: 12mm; text-align: right; font-variant-numeric: tabular-nums; flex-shrink: 0; }
.level-title { break-before: page; padding-top: 70mm; }
.level-title .eyebrow { font-size: 11pt; }
.level-title .lede { font-size: 11pt; color: #3b434d; max-width: 140mm; }
.level-title ul { font-size: 10pt; }
.module-title { break-before: page; border-top: 4px solid var(--lc); padding-top: 6mm; }
.module-title h2 { font-size: 19pt; margin: 2mm 0 3mm; }
.module-title .purpose { font-size: 10.5pt; color: #3b434d; }
.module-title ol { font-size: 10pt; }
.lesson { break-before: page; }
.lesson > h3, .special > h2 { font-family: var(--font-display); font-weight: 600; font-size: 18pt; color: var(--slate-dark); margin: 0 0 3mm; text-transform: none; letter-spacing: 0; }
.unit-meta { font-size: 8.8pt; color: #56606B; margin-bottom: 5mm; }
.reader-body h4 { font-family: var(--font-display); font-size: 13pt; margin: 6mm 0 2mm; color: var(--slate-dark); break-after: avoid; }
.reader-body h5 { font-size: 10.5pt; margin: 4mm 0 1.5mm; color: var(--slate-dark); break-after: avoid; }
.reader-body h6 { font-size: 10pt; margin: 3mm 0 1mm; break-after: avoid; }
.exercises-block h4, .answer-key-block h5 { font-family: var(--font-display); font-size: 13pt; color: var(--slate-dark); margin: 6mm 0 2mm; break-after: avoid; }
.answer-key-block { border-top: 1.5px solid var(--lc); padding-top: 2mm; }
.dialogue-box, .exercise, .activity, .mistake-callout, .tip-callout, .obj-box { box-shadow: none !important; break-inside: avoid; }
.dialogue-box { break-inside: auto; }
.dialogue-turn, .answer-item, tr, li, blockquote { break-inside: avoid; }
.reader-body table { display: table; width: 100%; font-size: 8.8pt; overflow: visible; }
.reader-body th { white-space: normal; }
.write-lines span { border-bottom-color: #b9c0c7; }
.exercise { padding: 3mm 4mm; }
.answer-item { font-size: 9.4pt; }
.dialogue-text { font-size: 10.2pt; }
.turn, .dialogue-turn { grid-template-columns: 26mm 1fr; }
a { color: inherit; text-decoration: none; }
code { background: #ECE6D8; }
.index-page { break-before: page; }
.index-page table { width: 100%; border-collapse: collapse; font-size: 8.6pt; }
.index-page th, .index-page td { border-bottom: 0.5px solid #d6d1c4; padding: 1.2mm 1.5mm; text-align: left; vertical-align: top; }
.index-page th { font-size: 7.8pt; text-transform: uppercase; letter-spacing: .03em; color: #56606B; }
.index-page td.code { font-family: var(--font-mono); white-space: nowrap; }
.index-page td.pg { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
.index-page h4 { font-family: var(--font-display); font-size: 13pt; margin: 6mm 0 2mm; break-after: avoid; }
.back-cover { break-before: page; page: cover; height: 297mm; width: 210mm; overflow: hidden; }
.back-cover { background: #0B0A07; display: flex; align-items: center; justify-content: center; }
.back-cover img { max-width: 210mm; max-height: 297mm; width: auto; height: auto; object-fit: contain; display: block; }
.sidebar, .topbar, .intro-screen, .reader-pager, .review-chk, .skip-link, .sitefoot { display: none !important; }
"""


def main():
    data = load()
    refs = json.loads((ROOT / "reference-index.json").read_text(encoding="utf-8"))
    pages = json.loads(PAGES.read_text(encoding="utf-8")) if PAGES.exists() else {}

    def pg(key):
        return str(pages.get(key, "000"))

    css = site_css()
    out = []
    w = out.append
    w("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">")
    w("<title>Career English: Professional English for the Real Workplace</title>")
    w("<meta name=\"author\" content=\"Hedai Tullah, Hidayet English Academy\">")
    w('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&family=Noto+Sans+Bengali:wght@400;600&family=Noto+Sans+Devanagari:wght@400;600&display=swap" rel="stylesheet">')
    w("<style>" + css + PRINT_CSS + "</style></head><body>")

    # Cover
    w('<div class="cover-page"><img src="../../front-cover.jpg" alt="Career English book cover"></div>')

    # Title and edition page
    w('<section class="front edition" style="padding-top:60mm">')
    w('<span class="eyebrow">Hidayet English Academy</span>')
    w("<h1>Career English</h1><p style=\"font-size:13pt\">Professional English for the Real Workplace</p>")
    w("<p>Five levels · 40 modules · 186 lessons · 5 level assessments · 5 capstones</p>")
    w('<hr class="gold-rule">')
    w("<p>© Hidayet English Academy. All rights reserved.</p>")
    w("<p>Print edition generated from the corrected online edition. Audio recordings are not yet available: every dialogue in this book can be read, or practiced aloud with a partner or teacher.</p>")
    w("</section>")

    # Contents
    w('<section class="toc"><div class="eyebrow">Contents</div>')
    w(f'<div class="toc-row toc-module" style="margin-left:0"><span class="t">How to Use This Book</span><span class="pg">{pg("how-to-use")}</span></div>')
    for level in data:
        n = level["level_number"]
        w(f'<div class="toc-row toc-level" style="--lc:var(--lvl{n})"><span class="t">{esc(level["title"])}</span><span class="pg">{pg("level-" + str(n))}</span></div>')
        for mi, mod in enumerate(level["modules"], 1):
            w(f'<div class="toc-row toc-module"><span class="t">Module {mi} · {esc(mod["title"])}</span><span class="pg">{pg(mod["module_id"])}</span></div>')
            for les in mod["lessons"]:
                w(f'<div class="toc-row toc-lesson"><span class="t">{mi}.{les["sequence_in_module"]}&nbsp; {esc(les["title"])}</span><span class="pg">{pg(les["lesson_id"])}</span></div>')
        for kind in ("assessment", "capstone"):
            if level.get(kind):
                x = level[kind]
                label = "Level Assessment" if kind == "assessment" else "Capstone"
                w(f'<div class="toc-row toc-module"><span class="t">{label}: {esc(x["title"])}</span><span class="pg">{pg(x["id"])}</span></div>')
    w(f'<div class="toc-row toc-level" style="--lc:var(--slate-dark)"><span class="t">Reference Index</span><span class="pg">{pg("index")}</span></div>')
    w("</section>")

    # How to use (h1: appears in the PDF outline)
    w('<section class="front" data-key="how-to-use"><span class="eyebrow">Front matter</span><h1>How to Use This Book</h1><hr class="gold-rule">')
    w('<div class="reader-body">' + demote(how_to_use_html()) + "</div></section>")

    # Levels
    for level in data:
        n = level["level_number"]
        lc = f'style="--lc:var(--lvl{n}); --lc-bg:var(--lvl{n}-bg);"'
        w(f'<section class="level" {lc}>')
        w(f'<div class="level-title" data-key="level-{n}"><span class="eyebrow">Level {n}</span><h1>{esc(level["title"])}</h1><hr class="gold-rule"><ul>')
        for mi, mod in enumerate(level["modules"], 1):
            w(f"<li>Module {mi} · {esc(mod['title'])}</li>")
        w("</ul></div>")
        for mi, mod in enumerate(level["modules"], 1):
            w(f'<div class="module-title" data-key="{mod["module_id"]}"><span class="eyebrow">Level {n} · Module {mi}</span><h2>{esc(mod["title"])}</h2>')
            if mod.get("purpose"):
                w(f'<p class="purpose">{esc(mod["purpose"])}</p>')
            w("<ol>" + "".join(f"<li>{esc(l['title'])}</li>" for l in mod["lessons"]) + "</ol></div>")
            for les in mod["lessons"]:
                num = f'{mi}.{les["sequence_in_module"]}'
                w(f'<article class="lesson" data-key="{les["lesson_id"]}"><span class="eyebrow">Level {n} · Module {mi} · Lesson {num}</span>')
                w(f'<h3>Lesson {num}: {esc(les["title"])}</h3>')
                if les.get("estimated_minutes"):
                    w(f'<div class="unit-meta">About {les["estimated_minutes"]} minutes</div>')
                if les.get("objectives_html"):
                    w('<div class="obj-box"><div class="callout-label" style="color:var(--lc)">What you\'ll learn</div><ul>' + tag_languages(les["objectives_html"]) + "</ul></div>")
                w('<div class="reader-body">' + tag_languages(demote(les.get("body_html", ""))) + "</div>")
                w(tag_languages(demote(les.get("practice_html", ""))))
                w("</article>")
        for kind in ("assessment", "capstone"):
            x = level.get(kind)
            if not x:
                continue
            label = "Level Assessment" if kind == "assessment" else "Capstone"
            w(f'<article class="lesson special" data-key="{x["id"]}"><span class="eyebrow">Level {n} · {label}</span>')
            w(f'<h2>{label}: {esc(x["title"])}</h2>')
            if x.get("estimated_minutes"):
                w(f'<div class="unit-meta">About {x["estimated_minutes"]} minutes</div>')
            if x.get("objectives_html"):
                w('<div class="obj-box"><div class="callout-label" style="color:var(--lc)">What you\'ll learn</div><ul>' + tag_languages(x["objectives_html"]) + "</ul></div>")
            w('<div class="reader-body">' + tag_languages(demote(x.get("body_html", ""))) + "</div>")
            w(tag_languages(demote(x.get("practice_html", ""))))
            w("</article>")
        w("</section>")

    # Reference index
    w('<section class="index-page" data-key="index"><span class="eyebrow">Back matter</span><h1>Reference Index</h1>')
    w("<p>Every reference code in the book, with the lesson and page where it is introduced.</p>")
    for t, name in refs["types"].items():
        w(f"<h4>{esc(name)} ({t}-)</h4><table><thead><tr><th>Code</th><th>Item</th><th>Introduced in</th><th>Page</th></tr></thead><tbody>")
        for code, c in refs["codes"].items():
            if c["type"] != t:
                continue
            u = refs["units"].get(c["home"], {"ref": c["home"]})
            w(f'<tr><td class="code">{code}</td><td>{esc(c["label"])}</td><td>{esc(u["ref"])}</td><td class="pg">{pg(c["home"])}</td></tr>')
        w("</tbody></table>")
    w("</section>")

    w('<div class="back-cover"><img src="../../back-cover.jpg" alt="Career English back cover"></div>')
    w("</body></html>")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")

    # Headings that become PDF bookmarks, in document order, so render_pdf.js can map pages to keys.
    heads = [{"key": "how-to-use", "title": "How to Use This Book", "level": None}]
    for level in data:
        n = level["level_number"]
        heads.append({"key": f"level-{n}", "title": level["title"], "level": n})
        for mi, mod in enumerate(level["modules"], 1):
            heads.append({"key": mod["module_id"], "title": mod["title"], "level": n})
            for les in mod["lessons"]:
                heads.append({"key": les["lesson_id"], "title": f'Lesson {mi}.{les["sequence_in_module"]}: {les["title"]}', "level": n})
        for kind in ("assessment", "capstone"):
            if level.get(kind):
                label = "Level Assessment" if kind == "assessment" else "Capstone"
                heads.append({"key": level[kind]["id"], "title": f'{label}: {level[kind]["title"]}', "level": n})
    heads.append({"key": "index", "title": "Reference Index", "level": None})
    (OUT_DIR / "headings.json").write_text(json.dumps(heads, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB); page numbers {'from pages.json' if pages else 'are placeholders'}")


if __name__ == "__main__":
    main()
