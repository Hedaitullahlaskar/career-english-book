"""Scan the corrected book for leftover production language, placeholders and
known continuity problems. Usage: python editorial/tools/scan.py [LEVEL ...]"""
import re
import sys

import book

sys.stdout.reconfigure(encoding="utf-8")

PATTERNS = {
    "placeholder": r"\[(?!sic\]|pause\])[a-zA-Z][^\]]{2,60}\]",
    "holistic": r"[Hh]olistic",
    "source file": r"\b[\w-]+\.md\b",
    "activity code": r"\bA0\d\b",
    "lesson code": r"\bL\d+-M\d+(?:-L\d+)?\b",
    "curriculum map": r"curriculum map",
    "open-ended": r"Open-ended|open response",
    "old vendor name": r"Hossain|Kabir Hossain",
    "audio claim": r"Listen to \(or read\)|\(audio\)|audio file",
    "theme tag": r"· theme:",
    "double hyphen": r"(?<!-)--(?!-)",
    "dialogue file": r"dialogue file|worked_example",
}
FIELDS = ("objectives_html", "body_html", "practice_html")


def main(levels):
    data = book.load()
    hits = 0
    for it in book.items(data):
        if levels and it["level"] not in levels:
            continue
        text = " ".join(str(it["ref"].get(f, "")) for f in FIELDS)
        key = str(it["ref"].get("practice_html", "")).partition("answer-number")[2]
        for name, pat in PATTERNS.items():
            # bracketed slots are legitimate in structure formulas; only answer keys must be filled in
            if name == "old vendor name" and it["level"] < 4:
                continue  # Mr. Hossain is the Level 1 supervisor; the vendor was renamed from Level 4 on
            for m in re.finditer(pat, key if name == "placeholder" else text):
                src = key if name == "placeholder" else text
                ctx = src[max(0, m.start() - 60):m.end() + 40].replace("\n", " ")
                print(f'{it["id"]:<20} {name:<15} | {ctx}')
                hits += 1
    print(f"{hits} hit(s)")


if __name__ == "__main__":
    main({int(a) for a in sys.argv[1:]})
