"""Report house-style choices for the author: date formats and the British idiom "to hand".

Usage: python editorial/proof/house_style_report.py <pdftext.json>

Reports only; changes nothing in the book.
Outputs:
  editorial/proof/HOUSE-STYLE-DATES.csv      every date expression, with style, unit and PDF page
  editorial/proof/HOUSE-STYLE-TO-HAND.csv    every "to hand" (idiom) and "on hand", with unit and PDF page
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from book import ROOT, items, load, plain  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
PROOF = ROOT / "editorial" / "proof"
PRINT = ROOT / "editorial" / "print"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
MON = rf"(?:{MONTHS}|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.?"
DAY = r"(?:[12]?\d|3[01])(?:st|nd|rd|th)?"
WEEKDAY = r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"
PATTERNS = [
    ("Month Day (US: September 20)", re.compile(rf"\b(?:{WEEKDAY},? )?{MON} {DAY}\b(?:,? (?:19|20)\d\d)?")),
    ("Day Month (UK: 12 March)", re.compile(rf"\b(?:{WEEKDAY},? )?(?:the )?{DAY} (?:of )?{MON}(?: (?:19|20)\d\d)?\b")),
    ("Ordinal day only (the 15th)", re.compile(
        r"\bthe (?:[12]?\d|3[01])(?:st|nd|rd|th)\b"
        r"(?!(?: and (?:[12]?\d|3[01])(?:st|nd|rd|th))? (?:introduction|floor|time|item|line|row|place)\b)")),
    # Numeric dates (12/03) were checked: the only matches are "24/7" and lesson references ("Lesson 1/2").
    ("Month and year only (March 2027)", re.compile(rf"\b{MON} (?:19|20)\d\d\b")),
]
TO_HAND = re.compile(r"\bto hand\b(?!\s+(?:over|off|in|out|it|them|the|a|an|this|that|him|her|someone|back|each|you|me|us|your|our|their|his|its|guests?|staff|whoever|more))", re.I)
ON_HAND = re.compile(r"\bon hand\b", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def main():
    pdftext = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    page_text = {p["page"]: norm(" ".join(l["text"] for l in p["lines"])) for p in pdftext}
    pages = json.loads((PRINT / "pages.json").read_text(encoding="utf-8"))
    heads = json.loads((PRINT / "headings.json").read_text(encoding="utf-8"))
    starts = sorted((pages[h["key"]], h["key"]) for h in heads if h["key"] in pages)
    rng = {k: (p, starts[i + 1][0] - 1 if i + 1 < len(starts) else len(pdftext)) for i, (p, k) in enumerate(starts)}

    def find_page(unit, context):
        a, b = rng.get(unit, (1, len(pdftext)))
        words = re.findall(r"[A-Za-z0-9]+", context)
        for size in (8, 6, 4):
            for i in range(0, max(1, len(words) - size + 1)):
                probe = norm(" ".join(words[i:i + size]))
                for p in range(a, b + 1):
                    if len(probe) >= 12 and probe in page_text.get(p, ""):
                        return str(p)
        return f"{a}–{b}"

    dates, hands = [], []
    for it in items(load()):
        ref = f'Level {it["level"]} · Lesson {it["number"]}' if it["kind"] == "lesson" else f'Level {it["level"]} · {it["kind"].capitalize()}'
        for field in ("objectives_html", "body_html", "practice_html"):
            text = plain(it["ref"].get(field) or "")
            taken = []
            for style, rx in PATTERNS:
                for m in rx.finditer(text):
                    if any(m.start() < e and s < m.end() for s, e in taken):
                        continue  # already counted under an earlier style
                    taken.append((m.start(), m.end()))
                    ctx = text[max(0, m.start() - 70):m.end() + 70]
                    dates.append({"Style": style, "Date text": m.group(0), "Unit": it["id"], "Lesson": ref,
                                  "Section": field.replace("_html", ""), "PDF Page": find_page(it["id"], ctx),
                                  "Context": "…" + ctx + "…"})
            for rx, kind in ((TO_HAND, "to hand (British idiom: 'available, with me')"), (ON_HAND, "on hand (US/international equivalent)")):
                for m in rx.finditer(text):
                    ctx = text[max(0, m.start() - 90):m.end() + 50]
                    hands.append({"Form": kind, "Unit": it["id"], "Lesson": ref, "Section": field.replace("_html", ""),
                                  "PDF Page": find_page(it["id"], ctx), "Context": "…" + ctx + "…",
                                  "Classification": "HOUSE STYLE / BRITISH ENGLISH DECISION" if "to hand" in kind else "Reference (alternative already used in the book)"})
    with open(PROOF / "HOUSE-STYLE-DATES.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Style", "Date text", "Unit", "Lesson", "Section", "PDF Page", "Context"])
        w.writeheader()
        w.writerows(dates)
    with open(PROOF / "HOUSE-STYLE-TO-HAND.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Form", "Unit", "Lesson", "Section", "PDF Page", "Context", "Classification"])
        w.writeheader()
        w.writerows(hands)
    write_markdown(dates, hands)
    print("dates:", Counter(d["Style"] for d in dates))
    print("hand:", Counter(h["Form"] for h in hands))


def write_markdown(dates, hands):
    styles = Counter(d["Style"] for d in dates)
    L = ["# House-style report: dates and \"to hand\"", "",
         "Generated by `editorial/proof/house_style_report.py`. **Report only: nothing in the book has been changed.** "
         "The author chooses the house style; any change made afterwards is logged as `Author decision`.", "",
         "Full lists: [`HOUSE-STYLE-DATES.csv`](HOUSE-STYLE-DATES.csv) and [`HOUSE-STYLE-TO-HAND.csv`](HOUSE-STYLE-TO-HAND.csv).", "",
         "## 1. Date formats", "",
         "| Style | Occurrences | Units |", "|---|---|---|"]
    for style, n in styles.most_common():
        units = sorted({d["Lesson"] for d in dates if d["Style"] == style})
        L.append(f"| {style} | {n} | {len(units)} |")
    L += ["", "Every full date (day and month), with its location:", "",
          "| Style | Date | Lesson | PDF page | Context |", "|---|---|---|---|---|"]
    for d in dates:
        if not d["Style"].startswith("Ordinal"):
            L.append(f'| {d["Style"]} | {d["Date text"]} | {d["Lesson"]} | {d["Pdf Page"] if "Pdf Page" in d else d["PDF Page"]} | {d["Context"].replace("|", "/")} |')
    by_lesson = Counter((d["Lesson"], d["PDF Page"].split("–")[0]) for d in dates if d["Style"].startswith("Ordinal"))
    L += ["", "Day-only ordinals (\"the 15th\", \"on the 1st\") — no month, so no US/UK order to choose; listed for completeness:", "",
          "| Lesson | First PDF page | Occurrences |", "|---|---|---|"]
    seen = Counter()
    for d in dates:
        if d["Style"].startswith("Ordinal"):
            seen[d["Lesson"]] += 1
    first = {}
    for d in dates:
        if d["Style"].startswith("Ordinal"):
            first.setdefault(d["Lesson"], d["PDF Page"])
    for lesson, n in seen.items():
        L.append(f"| {lesson} | {first[lesson]} | {n} |")
    L += ["", "Checked and not dates: \"24/7\" (Level 3 Lesson 6.3) and lesson references such as \"Lesson 1/2\" and \"Lesson 3/4\"; "
          "\"the 2nd and 3rd introduction\" (Level 1 Lesson 2.2).", "",
          "Also noted (typography, not a date-order question): Level 3 Lesson 1.6 writes a day range as \"the 20th-22nd\" with a hyphen; "
          "elsewhere the book uses an en dash for ranges.", "",
          "**Author decision needed:** one style for full dates — US (\"September 20\", \"Friday, May 14\") or UK (\"12 March\", "
          "\"Friday 14 May\") — or keep both. The book otherwise uses US spelling.", "",
          "## 2. \"to hand\" — HOUSE STYLE / BRITISH ENGLISH DECISION", "",
          "\"I don't have that figure to hand\" is a standard British idiom (meaning: with me, available now). It is not an error, "
          "and in Level 3 Lesson 4.5 it is taught as a key expression. American English would more often say \"on hand\" or "
          "\"with me right now\"; the book uses \"on hand\" once.", "",
          "| Form | Lesson | PDF page | Context | Classification |", "|---|---|---|---|---|"]
    for h in hands:
        L.append(f'| {h["Form"]} | {h["Lesson"]} | {h["PDF Page"]} | {h["Context"].replace("|", "/")} | {h["Classification"]} |')
    L += ["", "**Author decision needed:** keep \"to hand\" as taught (recommended if the book is happy to teach one British idiom "
          "alongside US spelling), or change the taught expression to \"on hand\" / \"with me\" throughout (Level 3 Lesson 4.5's key "
          "expressions, dialogue, answer key, and the recycled uses in Level 4 Lesson 5.2 and Level 5 Lesson 7.2)."]
    (PROOF / "HOUSE-STYLE-REPORT.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
