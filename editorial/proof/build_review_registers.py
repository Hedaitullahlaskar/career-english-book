"""Build the human-review registers for the final proof stage.

Usage: python editorial/proof/build_review_registers.py <pdftext.json>

Outputs (both are working documents for people; re-running this script keeps every
value a reviewer has entered and only refreshes the columns it owns):
  editorial/proof/HUMAN-PROOFREAD-REGISTER.csv   one row per unit (196), plus front and back matter
  editorial/proof/NATIVE-LANGUAGE-REVIEW.csv     one row per Bengali/Hindi item, and per English
                                                 statement about Bengali/Hindi usage or custom

Nothing is ever marked approved here: status columns start as PENDING / NO and are
for reviewers to change.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from book import ROOT, items, load, plain  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
PROOF = ROOT / "editorial" / "proof"
PRINT = ROOT / "editorial" / "print"
BN = re.compile(r"[ঀ-৿]")
HI = re.compile(r"[ऀ-ॿ]")
SPAN = re.compile(r'<span class="(bn|hi)">(.*?)</span>', re.S)
BLOCK_START = re.compile(r"<(p|li|td|th|h[1-4]|div)\b[^>]*>")

HUMAN_COLS = ["Level", "Module", "Unit", "PDF Start Page", "PDF End Page", "Proofread Status",
              "Issues Found", "Corrections Made", "Reviewer", "Date", "Approved"]
HUMAN_OWNED = ["Level", "Module", "PDF Start Page", "PDF End Page"]  # refreshed by this script
NATIVE_COLS = ["Item ID", "Unit", "Lesson", "PDF Page", "Language", "Text Type", "Original Text",
               "Review Required", "Native Review Status", "Reviewer", "Reviewer Notes", "Approved"]
NATIVE_OWNED = ["Unit", "Lesson", "PDF Page", "Language", "Text Type", "Original Text", "Review Required"]
LANG = {"bn": "Bengali", "hi": "Hindi"}


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def unit_ranges(n_pages):
    pages = json.loads((PRINT / "pages.json").read_text(encoding="utf-8"))
    heads = json.loads((PRINT / "headings.json").read_text(encoding="utf-8"))
    starts = sorted((pages[h["key"]], h["key"]) for h in heads if h["key"] in pages)
    rng = {}
    for i, (p, k) in enumerate(starts):
        rng[k] = (p, starts[i + 1][0] - 1 if i + 1 < len(starts) else n_pages - 1)
    return pages, rng


def block_around(html, pos):
    starts = list(BLOCK_START.finditer(html, 0, pos))
    if not starts:
        return pos, html[max(0, pos - 300):pos + 300]
    m = starts[-1]
    tag = m.group(1)
    end = html.find(f"</{tag}>", pos)
    end = end if end != -1 else pos + 400
    return m.start(), html[m.start():end]


def unit_ref(it):
    return f'Level {it["level"]} · Lesson {it["number"]}' if it["kind"] == "lesson" else f'Level {it["level"]} · {it["kind"].capitalize()}'


def merge(path, cols, owned, key, rows):
    """Write rows, keeping reviewer-entered values from an existing file."""
    old = {}
    if path.exists():
        for r in csv.DictReader(open(path, encoding="utf-8")):
            old[r[key]] = r
    out = []
    for r in rows:
        prev = old.get(r[key])
        if prev:
            for c in cols:
                if c not in owned and c != key and prev.get(c, "") != "":
                    r[c] = prev[c]
        out.append(r)
    dropped = set(old) - {r[key] for r in rows}
    for k in sorted(dropped):  # the source text changed: keep any reviewer work and flag it
        prev = old[k]
        if prev.get("Reviewer") or prev.get("Reviewer Notes") or prev.get("Native Review Status") not in ("", "PENDING"):
            prev["Native Review Status"] = "SOURCE TEXT CHANGED — RE-REVIEW"
            prev["Approved"] = "NO"
            out.append(prev)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    return len(out), dropped


def main():
    pdftext = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    page_text = {p["page"]: norm(" ".join(l["text"] for l in p["lines"])) for p in pdftext}
    pages, rng = unit_ranges(len(pdftext))
    units = list(items(load()))

    def find_page(unit, english):
        a, b = rng.get(unit, (1, len(pdftext)))
        words = re.findall(r"[A-Za-z0-9]+", english)
        for size in (8, 6, 4, 3):
            for start in range(0, max(1, len(words) - size + 1)):
                probe = norm(" ".join(words[start:start + size]))
                if len(probe) < 10:
                    continue
                for p in range(a, b + 1):
                    if probe in page_text.get(p, ""):
                        return str(p)
        return f"{a}–{b}"

    # --- Human proofread register ---
    rows = []
    fm_end = pages.get("level-1", 11) - 1
    rows.append({"Level": "—", "Module": "Front matter", "Unit": "FRONT-MATTER — cover, edition page, contents, How to Use",
                 "PDF Start Page": 1, "PDF End Page": fm_end})
    for it in units:
        a, z = rng[it["id"]]
        mod = f'Module {it["module"]} · {it["module_title"]}' if it["module"] else ("Level assessment" if it["kind"] == "assessment" else "Capstone")
        title = f'Lesson {it["number"]}: {it["title"]}' if it["kind"] == "lesson" else f'{it["kind"].capitalize()}: {it["title"]}'
        rows.append({"Level": it["level"], "Module": mod, "Unit": f'{it["id"]} — {title}',
                     "PDF Start Page": a, "PDF End Page": z})
    ix = rng["index"]
    rows.append({"Level": "—", "Module": "Back matter", "Unit": "BACK-MATTER — Reference Index and back cover",
                 "PDF Start Page": ix[0], "PDF End Page": len(pdftext)})
    for r in rows:
        r.update({"Proofread Status": "PENDING", "Issues Found": "", "Corrections Made": "",
                  "Reviewer": "", "Date": "", "Approved": "NO"})
    # rows are keyed by the unit id (the text before " — ")
    for r in rows:
        r["_key"] = r["Unit"].split(" — ")[0]
    path = PROOF / "HUMAN-PROOFREAD-REGISTER.csv"
    old = {}
    if path.exists():
        for r in csv.DictReader(open(path, encoding="utf-8")):
            old[r["Unit"].split(" — ")[0]] = r
    for r in rows:
        prev = old.get(r["_key"])
        if prev:
            for c in HUMAN_COLS:
                if c not in HUMAN_OWNED and c != "Unit" and prev.get(c, "") != "":
                    r[c] = prev[c]
        del r["_key"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HUMAN_COLS)
        w.writeheader()
        w.writerows(rows)
    print(f"{path.name}: {len(rows)} rows ({len(units)} units + front and back matter)")

    # --- Native-language review register ---
    items_out = []
    for it in units:
        uid, ref = it["id"], unit_ref(it)
        n = 0
        for field in ("objectives_html", "body_html", "practice_html"):
            html = it["ref"].get(field) or ""
            # 1) vocabulary-table glosses
            for row in re.finditer(r"<tr>(.*?)</tr>", html, re.S):
                cells = row.group(1)
                if 'class="bn"' not in cells and 'class="hi"' not in cells:
                    continue
                term = plain(re.search(r"<strong>(.*?)</strong>", cells).group(1)) if "<strong>" in cells else ""
                pos_m = re.search(r"</strong>\s*<em>(.*?)</em>", cells)
                pos = f" ({plain(pos_m.group(1))})" if pos_m else ""
                english = plain(re.sub(r'<td class="(bn|hi)">.*?</td>', " ", cells, flags=re.S))
                page = find_page(uid, english)
                for lang in ("bn", "hi"):
                    c = re.search(rf'<td class="{lang}">(.*?)</td>', cells, re.S)
                    if c:
                        n += 1
                        items_out.append({"Item ID": f"{uid}-{n:02d}", "Unit": uid, "Lesson": ref, "PDF Page": page,
                                          "Language": LANG[lang], "Text Type": "Gloss",
                                          "Original Text": f"{term}{pos} → {plain(c.group(1))}"})
            # 2) other Bengali/Hindi text, grouped by the block it sits in
            blocks = {}
            for m in SPAN.finditer(html):
                start, block = block_around(html, m.start())
                if re.match(r'<td class="(bn|hi)"', block):
                    continue  # a vocabulary-table cell, already listed as a gloss
                blocks.setdefault(start, block)
            prev_english = ""
            for start in sorted(blocks):
                block = blocks[start]
                text = plain(block)
                latin = re.findall(r"[A-Za-z]{2,}", plain(re.sub(r'<span class="(bn|hi)">.*?</span>', " ", block, flags=re.S)))
                kind_area = "practice" if field == "practice_html" else ("objectives" if field == "objectives_html" else "body")
                in_cell = re.match(r"<t[dh]\b", block)
                if in_cell:  # a word list in an ordinary table: the English is in the same row
                    row_start = html.rfind("<tr", 0, start)
                    row_end = html.find("</tr>", start)
                    row_text = plain(re.sub(r'<span class="(bn|hi)">.*?</span>', " ", html[row_start:row_end], flags=re.S))
                    latin = re.findall(r"[A-Za-z]{2,}", row_text)
                    text = plain(html[row_start:row_end])
                english = " ".join(latin) if len(latin) >= 4 else (
                    prev_english or " ".join(re.findall(r"[A-Za-z]{2,}", plain(html[max(0, start - 800):start]))[-30:]))
                page = find_page(uid, english) if english else f"{rng[uid][0]}–{rng[uid][1]}"
                for lang in ("bn", "hi"):
                    runs = [plain(s.group(2)) for s in SPAN.finditer(block) if s.group(1) == lang]
                    if not runs:
                        continue
                    script_words = sum(len(r.split()) for r in runs)
                    if in_cell:
                        ttype = "Gloss"
                    elif len(latin) < 3 or (script_words >= 12 and len(latin) * 3 < script_words):
                        ttype = "Translation"  # a note written in Bengali/Hindi, quoting at most a few English words
                    elif kind_area == "practice":
                        ttype = "Other"
                    elif kind_area == "objectives":
                        ttype = "Instruction"
                    elif script_words >= 4:
                        ttype = "Example sentence"
                    else:
                        ttype = "Gloss"
                    shown = " / ".join(runs) if ttype != "Translation" else " ".join(runs)
                    if ttype in ("Gloss", "Example sentence", "Other", "Instruction"):
                        shown = f"{shown}   [in: {text[:160]}{'…' if len(text) > 160 else ''}]"
                    n += 1
                    items_out.append({"Item ID": f"{uid}-{n:02d}", "Unit": uid, "Lesson": ref, "PDF Page": page,
                                      "Language": LANG[lang], "Text Type": ttype, "Original Text": shown})
                if len(latin) >= 4:
                    prev_english = " ".join(latin)
            # 3) English statements about Bengali/Hindi usage or workplace custom
            for m in re.finditer(r"<(p|li)\b[^>]*>(.*?)</\1>", html, re.S):
                inner = m.group(2)
                if SPAN.search(inner) or not re.search(r"\b(Bengali|Hindi)\b", plain(inner)):
                    continue
                text = plain(inner)
                if len(text) < 60:
                    continue
                n += 1
                items_out.append({"Item ID": f"{uid}-{n:02d}", "Unit": uid, "Lesson": ref, "PDF Page": find_page(uid, text),
                                  "Language": "English (statement about Bengali/Hindi)", "Text Type": "Workplace/cultural statement",
                                  "Original Text": text})
    for r in items_out:
        digest = hashlib.sha1((r["Language"] + r["Original Text"]).encode("utf-8")).hexdigest()[:8]
        code = {"Bengali": "BN", "Hindi": "HI"}.get(r["Language"], "EN")
        r["Item ID"] = f'{r["Unit"]}-{code}-{digest}'
        r["Review Required"] = {"Bengali": "Native Bengali speaker", "Hindi": "Native Hindi speaker"}.get(
            r["Language"], "Native Bengali and Hindi speakers (check the claim)")
        r.update({"Native Review Status": "PENDING", "Reviewer": "", "Reviewer Notes": "", "Approved": "NO"})
    count, dropped = merge(PROOF / "NATIVE-LANGUAGE-REVIEW.csv", NATIVE_COLS, NATIVE_OWNED, "Item ID", items_out)
    script_units = {r["Unit"] for r in items_out if r["Language"] in LANG.values()}
    stmt_units = {r["Unit"] for r in items_out if r["Language"] not in LANG.values()}
    from collections import Counter
    print(f"NATIVE-LANGUAGE-REVIEW.csv: {count} items; {len(script_units)} units with Bengali/Hindi text; "
          f"{len(stmt_units - script_units)} more units with only English statements about Bengali/Hindi")
    print(Counter((r["Language"], r["Text Type"]) for r in items_out))
    if dropped:
        print(f"{len(dropped)} earlier rows no longer match the source; any with reviewer work were kept and flagged")


if __name__ == "__main__":
    main()
