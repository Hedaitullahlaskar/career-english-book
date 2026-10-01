"""Automated proof checks on the rendered PDF (layout) and on the corrected text (typography).

Usage: python editorial/proof/auto_checks.py <pdftext.json>
  pdftext.json comes from editorial/proof/pdf_text.mjs.
Writes editorial/proof/auto-checks.csv (one row per flag) and prints a summary.
Flags are candidates for editorial review, not confirmed errors.
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from book import ROOT, items, load, plain  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
PROOF = ROOT / "editorial" / "proof"
PRINT = ROOT / "editorial" / "print"


def unit_ranges():
    pages = json.loads((PRINT / "pages.json").read_text(encoding="utf-8"))
    heads = json.loads((PRINT / "headings.json").read_text(encoding="utf-8"))
    starts = sorted(((pages[h["key"]], h["key"]) for h in heads if h["key"] in pages))
    ranges = {}
    for i, (p, key) in enumerate(starts):
        end = starts[i + 1][0] - 1 if i + 1 < len(starts) else None
        ranges[key] = (p, end)
    return ranges, starts


def unit_for_page(starts, page):
    cur = "front-matter"
    for p, key in starts:
        if p <= page:
            cur = key
        else:
            break
    return cur


AN_OK = re.compile(r"^(hour|honest|honorific|honestly|ROI|honou?r|heir|HR|SLA|MBA|IT|FAQ|MP|SMS|NDA|RSVP|FYI|X|M|L|S|F|ID|SOP|ETA|R|N|H)\b")
A_OK = re.compile(r"^(uni|use|usu|euro|one|once|ute|ufo|user|us\b|u\b)", re.I)


def text_checks(uid, text):
    flags = []

    def add(kind, m, note=""):
        s = max(0, m.start() - 50)
        flags.append((kind, text[s:m.end() + 50].replace("\n", " "), note))

    for m in re.finditer(r"\b([A-Za-z]{2,})[ \t]+\1\b", text, re.I):
        if m.group(1).lower() not in ("that", "had", "very", "no", "bye", "knock", "ha", "so"):
            add("repeated word", m)
    for m in re.finditer(r"\s[,;:!?](?!\))|\s\.(?!\.)(?=\s|$)", text):
        add("space before punctuation", m)
    for m in re.finditer(r"(?<!\.)\.\.(?!\.)|,,|;;", text):
        add("doubled punctuation", m)
    for m in re.finditer(r"\ba ([aeiouAEIOU]\w*)", text):
        if not A_OK.match(m.group(1)):
            add("a/an", m, "'a' before a vowel sound?")
    for m in re.finditer(r"\ban ([b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]\w*)", text):
        if not AN_OK.match(m.group(1)):
            add("a/an", m, "'an' before a consonant sound?")
    for m in re.finditer(r"[a-z][,;:!?][A-Za-z]", text):
        add("missing space after punctuation", m)
    for m in re.finditer(r"(?<![-!<])--(?!>)|->|\bTODO\b|\bTBD\b|�|â€", text):
        add("leftover marker", m)
    for m in re.finditer(r"\b(colour|favour|behaviour|organis|apologis|recognis|centre|programme(?! ends| over)|practis|labelled|travelled|cancelled)\w*", text):
        add("British spelling", m)
    for para in re.split(r"\n+", text):
        if para.count("(") != para.count(")"):
            m = re.search(r"[()]", para)
            flags.append(("unbalanced brackets", para[:160], ""))
        if para.count('"') % 2:
            flags.append(("unbalanced quotes", para[:160], ""))
    return flags


def block_text(html):
    """Plain text with block boundaries kept as newlines (so bracket/quote checks stay local)
    and inline tags removed without adding spaces (so spacing checks see the real text)."""
    import html as _h
    html = re.sub(r"\s+", " ", html)  # the source wraps lines mid-paragraph
    html = re.sub(r"<br\s*/?>|</(p|li|tr|td|th|h\d|div|blockquote)>|<(div|p|li|td|th)\b[^>]*>", "\n", html)
    return _h.unescape(re.sub(r"<[^>]+>", "", html))


def main():
    pdftext = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    ranges, starts = unit_ranges()
    rows = []
    # --- layout checks on the rendered PDF ---
    title_keys = {k for k in ranges if k.startswith("level-") or re.match(r"CE-L\d\d-M\d\d$", k)}
    for pg in pdftext:
        n, lines = pg["page"], pg["lines"]
        if n in (1, len(pdftext)):
            continue
        body = [l for l in lines if 45 < l["y"] < 800]
        chars = sum(len(l["text"]) for l in body)
        unit = unit_for_page(starts, n)
        is_title = any(p == n for p, k in starts if k in title_keys)
        if chars < 180 and not is_title and n > 3:
            rows.append(("layout", unit, n, "near-empty page", f"{chars} characters of body text", ""))
        if body:
            last = body[-1]
            if last["size"] >= 12.5 and last["y"] < 140:
                rows.append(("layout", unit, n, "heading at foot of page", last["text"][:120], ""))
        for l in body:
            if l["maxX"] > pg["width"] - 20 or l["minX"] < 30:
                rows.append(("layout", unit, n, "text outside margin", l["text"][:120], f'x {l["minX"]}–{l["maxX"]}'))
                break
    # --- text checks on the corrected source, located by unit ---
    data = load()
    for it in items(data):
        txt = "\n".join(block_text(str(it["ref"].get(f, ""))) for f in ("objectives_html", "body_html", "practice_html"))
        rng = ranges.get(it["id"], (None, None))
        for kind, ctx, note in text_checks(it["id"], txt):
            rows.append(("text", it["id"], f"{rng[0]}–{rng[1]}", kind, ctx, note))
    with open(PROOF / "auto-checks.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["check", "unit", "pdf_page", "flag", "context", "note"])
        w.writerows(rows)
    from collections import Counter
    print(Counter((r[0], r[3]) for r in rows).most_common())
    print(len(rows), "flags written to editorial/proof/auto-checks.csv")


if __name__ == "__main__":
    main()
