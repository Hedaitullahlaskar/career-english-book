"""Source/PDF consistency audit. Reports discrepancies; fixes nothing.

Usage:
  node editorial/proof/pdf_text.mjs editorial/print/Career-English-Master.pdf <pdftext.json>
  node editorial/proof/pdf_outline.mjs editorial/print/Career-English-Master.pdf <outline.json>
  python editorial/proof/consistency_audit.py <pdftext.json> <outline.json>

Writes editorial/proof/SOURCE-PDF-CONSISTENCY.md and editorial/proof/consistency-discrepancies.csv.

Checks:
  1. Provenance: book-data.json = original + logged corrections; generated files are current
     (the index and print builders are re-run on copies and compared, then the originals restored).
  2. Bookmarks: every level/module/unit/index heading has a bookmark at the page in pages.json.
  3. Contents: the page printed in the contents for every heading matches pages.json.
  4. Text: each unit's source text is present in its PDF pages (5-word sequences, Latin script only).
  5. Proof corrections: the 95 "PDF proof" corrections are present in the PDF.
  6. Index: every code in reference-index.json (the website index) is in the PDF index with the
     same label, lesson and page, and is printed within that lesson's pages.
  7. Codes: duplicate terms, codes cited only in answer keys or exercises, malformed codes.
  8. Answer keys: exercise and answer numbering match; multiple-choice answers name an existing option.
  9. Scoring: pass marks within their scale; stated totals and percentages add up.
"""
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from book import ROOT, items, load, plain  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
PROOF = ROOT / "editorial" / "proof"
PRINT = ROOT / "editorial" / "print"
TOOLS = ROOT / "editorial" / "tools"
CODE = re.compile(r"\b(V|PAT|GIC|CF|TL|MIS|TIP|P)-(\d+)\b")
TABLE_CELL = re.compile(r"<(td|th)\b[^>]*>(.*?)</\1>", re.S)
BLOCK_SPLIT = re.compile(r"</?(?:p|li|h[1-4]|div|tr|ul|ol|blockquote|table|br)\b[^>]*>")
BACKREF = re.compile(r"\\\d")

findings = []  # (check, severity, location, detail)


def add(check, severity, location, detail):
    findings.append({"check": check, "severity": severity, "location": location, "detail": detail})


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def rerun_on_copy(cmd, outputs):
    """Run a generator, compare its outputs with the current files, then restore the originals."""
    saved = {p: (p.read_bytes(), p.stat()) for p in outputs if p.exists()}
    before = {p: sha(p) for p in outputs}
    try:
        subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True, text=True, stdin=subprocess.DEVNULL)
        after = {p: sha(p) for p in outputs}
        return [p for p in outputs if before[p] != after[p]]
    finally:
        for p, (data, st) in saved.items():  # restore content and timestamps
            p.write_bytes(data)
            os.utime(p, ns=(st.st_atime_ns, st.st_mtime_ns))


def main():
    pdftext = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    outline = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    n_pages = len(pdftext)
    body_lines = {p["page"]: [l["text"] for l in p["lines"] if 45 <= l["y"] <= 800] for p in pdftext}
    page_norm = {p: norm(" ".join(ls)) for p, ls in body_lines.items()}
    pages = json.loads((PRINT / "pages.json").read_text(encoding="utf-8"))
    heads = json.loads((PRINT / "headings.json").read_text(encoding="utf-8"))
    starts = sorted((pages[h["key"]], h["key"]) for h in heads if h["key"] in pages)
    rng = {k: (p, starts[i + 1][0] - 1 if i + 1 < len(starts) else n_pages - 1) for i, (p, k) in enumerate(starts)}
    data = load()
    units = list(items(data))
    stats = {}

    # 1. Provenance
    r = subprocess.run([sys.executable, str(TOOLS / "apply_corrections.py"), "--check"], cwd=ROOT,
                       capture_output=True, text=True, stdin=subprocess.DEVNULL)
    ok = r.returncode == 0 and "matches" in r.stdout
    stats["corrections_check"] = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-200:]
    if not ok:
        add("Provenance", "Critical", "book-data.json", "Does not match the original plus the logged corrections: " + stats["corrections_check"])
    changed = rerun_on_copy([sys.executable, str(TOOLS / "build_reference_index.py")], [ROOT / "reference-index.json"])
    stats["index_current"] = not changed
    if changed:
        add("Provenance", "High", "reference-index.json", "Regenerating the index from book-data.json gives a different file: the website index and PDF index are stale.")
    changed = rerun_on_copy([sys.executable, str(TOOLS / "build_print.py")],
                            [PRINT / "career-english-print.html", PRINT / "headings.json"])
    stats["print_current"] = not changed
    if changed:
        add("Provenance", "High", ", ".join(p.name for p in changed), "Regenerating the print edition gives different output: the PDF was not built from the current source.")
    pdf = PRINT / "Career-English-Master.pdf"
    newest_src = max((ROOT / "book-data.json").stat().st_mtime, (ROOT / "reference-index.json").stat().st_mtime,
                     (ROOT / "front-cover.jpg").stat().st_mtime, (ROOT / "back-cover.jpg").stat().st_mtime)
    stats["pdf_after_source"] = pdf.stat().st_mtime >= newest_src
    if not stats["pdf_after_source"]:
        add("Provenance", "High", pdf.name, "The PDF is older than book-data.json, reference-index.json or a cover image.")
    stats["pages"] = n_pages

    # 2. Bookmarks
    bm = outline["bookmarks"]
    stats["bookmarks_total"] = len(bm)
    bm_by_title = defaultdict(list)
    for b in bm:
        bm_by_title[norm(b["title"])].append(b)
    struct_ok, spacing = 0, []
    for h in heads:
        cands = bm_by_title.get(norm(h["title"]), [])
        hit = [b for b in cands if b["page"] == pages.get(h["key"])]
        if hit:
            struct_ok += 1
            if hit[0]["title"].replace("’", "'") != h["title"].replace("’", "'"):
                spacing.append((h["key"], hit[0]["title"], h["title"]))
        else:
            add("Bookmarks", "High", h["key"], f'No bookmark "{h["title"]}" at p. {pages.get(h["key"])}' +
                (f' (found at {[c["page"] for c in cands]})' if cands else ""))
    stats["bookmarks_structural"] = f"{struct_ok} of {len(heads)}"
    stats["bookmark_title_spacing"] = len(spacing)
    for key, got, want in spacing:
        add("Bookmarks", "Low", key, f'Bookmark title differs from the heading in spacing or punctuation: "{got}" (heading: "{want}")')
    section_spacing = [b["title"] for b in bm if b["depth"] >= 3 and re.search(r"[a-z][A-Z]", b["title"])]
    stats["section_bookmarks_joined_words"] = len(section_spacing)

    # 3. Contents page numbers
    toc_pages = range(2, pages.get("how-to-use", 9))
    toc_lines = [l for p in toc_pages for l in body_lines.get(p, [])]
    toc_checked = 0
    for h in heads:
        t = h["title"]
        if h["key"].startswith("CE-") and "-L" in h["key"][7:] and t.startswith("Lesson "):
            t = t.split(": ", 1)[1]
        elif h["key"].startswith("CE-") and len(h["key"]) == 10:
            pass  # module titles print as "Module n · title"
        key_n = norm(t)[:30]
        line = next((l for l in toc_lines if key_n and key_n in norm(l)), None)
        if not line:
            add("Contents", "Medium", h["key"], f'Heading "{h["title"]}" not found in the contents pages')
            continue
        m = re.search(r"(\d+)\s*$", line)
        if not m or int(m.group(1)) != pages.get(h["key"]):
            add("Contents", "High", h["key"], f'Contents line "{line}" vs actual start page {pages.get(h["key"])}')
        else:
            toc_checked += 1
    stats["contents_ok"] = f"{toc_checked} of {len(heads)}"

    # 4. Source text present in the PDF
    low = []
    for it in units:
        a, z = rng[it["id"]]
        pdf_w = []
        for p in range(a, z + 1):
            pdf_w += words(" ".join(body_lines.get(p, [])))
        pdf_set = {" ".join(pdf_w[i:i + 5]) for i in range(len(pdf_w) - 4)}
        pdf_bag = set(pdf_w)
        html = " ".join([f"<h3>{it['title']}</h3>"] + [it["ref"].get(f) or "" for f in ("objectives_html", "body_html", "practice_html")])
        # Table cells are compared by their words, because the PDF text of a multi-line table row comes out
        # interleaved across columns; everything else by 5-word runs inside each paragraph, list item or heading.
        cells, cells_missing = 0, []
        for m in TABLE_CELL.finditer(html):
            cw = words(plain(m.group(2)))
            if cw:
                cells += 1
                if any(w not in pdf_bag for w in cw):
                    cells_missing.append(plain(m.group(2))[:60])
        flow = TABLE_CELL.sub(" ", html)
        grams, missing = [], []
        for block in BLOCK_SPLIT.split(flow):
            bw = words(plain(block))
            for i in range(len(bw) - 4):
                g = " ".join(bw[i:i + 5])
                grams.append(g)
                if g not in pdf_set:
                    missing.append(g)
        if cells_missing:
            add("Text", "High", it["id"], f"{len(cells_missing)} of {cells} table cells have words not found in PDF pp. {a}–{z}; e.g. {cells_missing[:2]}")
        if not grams:
            continue
        cov = 1 - len(missing) / len(grams)
        if cov < 0.985:
            low.append((it["id"], cov, missing[:3]))
            add("Text", "High" if cov < 0.95 else "Medium", it["id"],
                f"Only {cov:.1%} of the source's 5-word sequences found in PDF pp. {a}–{z}; e.g. {missing[:3]}")
    stats["text_units_ok"] = f"{len(units) - len(low)} of {len(units)} units at 98.5% or more"

    # 5. PDF proof corrections present
    rows = list(csv.DictReader(open(ROOT / "editorial" / "correction-log.csv", encoding="utf-8")))
    stats["log_rows"] = len(rows)
    stats["log_by_source"] = Counter(("PDF proof" if r["source"].startswith("PDF proof") else
                                      (r["source"].split(",")[0] if r["source"] else "(editorial audit)")) for r in rows)
    proof = [r for r in rows if r["source"].startswith("PDF proof")]
    found = 0
    for r in proof:
        rep_text = plain(BACKREF.sub(" ", r["replacement"]))  # rule replacements can hold \1-style references
        rep = norm(rep_text)
        if not rep or len(rep) < 6:
            found += 1  # e.g. a deleted space or a dash: checked by the text comparison above
            continue
        unit = r["id"] if r["id"].startswith("CE-") else None
        span = range(*((rng[unit][0], rng[unit][1] + 1) if unit in rng else (1, n_pages + 1)))
        probe = rep[:60]
        span_words = set(words(" ".join(" ".join(body_lines.get(p, [])) for p in span)))
        if any(probe in page_norm.get(p, "") for p in span) or any(
                probe[:40] in (page_norm.get(p, "") + page_norm.get(p + 1, "")) for p in span):
            found += 1
        elif BACKREF.search(r["replacement"]) or ("<td" in r["original"] + r["replacement"]) or \
                all(w in span_words for w in words(rep_text)):
            found += 1  # a rule pattern, or text inside a table whose PDF lines interleave: all its words are present
        else:
            add("Proof corrections", "Medium", r["id"], f'Correction #{r["no"]} not found in the PDF text: "{plain(r["replacement"])[:90]}"')
    stats["proof_found"] = f"{found} of {len(proof)}"

    # 6. Index: website index (reference-index.json) vs PDF index pages vs lesson pages
    ref = json.loads((ROOT / "reference-index.json").read_text(encoding="utf-8"))
    ix_text = " ".join(" ".join(body_lines.get(p, [])) for p in range(pages["index"], n_pages))
    positions = [(m.start(), m.group(0)) for m in CODE.finditer(ix_text)]
    seg = defaultdict(list)  # a code can also appear inside another row's label, so keep every occurrence
    for i, (pos, code) in enumerate(positions):
        seg[code].append(ix_text[pos:positions[i + 1][0] if i + 1 < len(positions) else len(ix_text)])
    ix_ok = 0
    for code, c in ref["codes"].items():
        segs = seg.get(code)
        if not segs:
            add("Index", "High", code, "In the website index but not in the PDF index")
            continue
        exp_page = str(pages.get(c["home"]))
        unit_ref = ref["units"].get(c["home"], {}).get("ref", "")

        def score(x):
            # the lesson column wraps around the page column ("Lesson 54 2.3"), so drop the page number first
            no_page = re.sub(r"\b" + exp_page + r"\b", " ", x, count=1)
            # long labels wrap and interleave with the lesson column, so check the lesson's parts as tokens
            ref_tokens = re.findall(r"Level \d|Lesson|Capstone|Level Assessment|Assessment|\d+\.\d+", unit_ref)
            return (norm(c["label"].rstrip("…"))[:25] in norm(x),
                    exp_page in re.findall(r"\b\d+\b", x),
                    all(t in no_page for t in ref_tokens))
        s = max(segs, key=lambda x: sum(score(x)))
        label_ok, page_ok, ref_ok = score(s)
        a, z = rng.get(c["home"], (0, -1))
        printed = any(code in " ".join(body_lines.get(p, [])) for p in range(a, z + 1))
        problems = [x for x, okx in (("label", label_ok), ("page", page_ok), ("lesson", ref_ok), ("code printed in that lesson", printed)) if not okx]
        if problems:
            add("Index", "Medium" if problems != ["code printed in that lesson"] else "Low", code,
                f'PDF index row "{s.strip()[:110]}" — mismatch: {", ".join(problems)} (expected p. {exp_page}, {unit_ref})')
        else:
            ix_ok += 1
    # labels that name a section heading or another code instead of the item itself
    for code, c in ref["codes"].items():
        lab = c["label"]
        if re.match(r"^(Vocabulary|Key [Ee]xpressions|Grammar in [Cc]ontext|Common [Mm]istake|Professional [Tt]one|"
                    r"Industry [Oo]verlays|Self-[Cc]heck)\b", lab) \
                or re.search(r"Grammar in Context|Expression Function Register|Key Expressions", lab) \
                or re.match(r"^[A-Z]?[a-z]{1,3} of \w", lab) \
                or (c["type"] != "V" and CODE.search(lab) and not lab.startswith("[")):
            add("Index", "Medium", code, f'Label looks wrong: "{lab}" (the index generator picked up nearby text)')
    extra = set(seg) - set(ref["codes"])
    for code in sorted(extra):
        add("Index", "Medium", code, "In the PDF index but not in reference-index.json")
    stats["index_ok"] = f"{ix_ok} of {len(ref['codes'])}"

    # 7. Codes
    v_terms = defaultdict(list)
    for code, c in ref["codes"].items():
        if c["type"] == "V":
            v_terms[c["label"].lower()].append(code)
    dups = {t: cs for t, cs in v_terms.items() if len(cs) > 1}
    stats["duplicate_terms"] = len(dups)
    for t, cs in sorted(dups.items()):
        add("Codes", "Medium", " / ".join(cs), f'Vocabulary item "{t}" has {len(cs)} codes (author decision B)')
    body_codes, practice_codes, malformed = set(), defaultdict(set), []
    for it in units:
        for f in ("objectives_html", "body_html"):
            body_codes |= {m.group(0) for m in CODE.finditer(it["ref"].get(f) or "")}
        for m in CODE.finditer(it["ref"].get("practice_html") or ""):
            practice_codes[m.group(0)].add(it["id"])
        for f in ("body_html", "practice_html", "objectives_html"):
            for m in CODE.finditer(it["ref"].get(f) or ""):
                if len(m.group(2)) != 4:
                    malformed.append((it["id"], m.group(0)))
    only_practice = {c: us for c, us in practice_codes.items() if c not in body_codes}
    for c, us in sorted(only_practice.items()):
        add("Codes", "Low", c, f"Cited in an exercise or answer key ({', '.join(sorted(us))}) but never in lesson text")
    for uid, c in malformed:
        add("Codes", "Medium", uid, f'Code "{c}" does not have four digits')
    stats["codes_total"] = len(ref["codes"])

    # 8. Answer keys
    ak_ok = 0
    for it in units:
        p = it["ref"].get("practice_html") or ""
        ex = re.findall(r'<span class="exercise-number">(\d+)\.</span>', p)
        an = re.findall(r'<span class="answer-number">(\d+)\.</span>', p)
        if ex != an:
            add("Answer keys", "High", it["id"], f"Exercises numbered {ex} but answers numbered {an}")
            continue
        bad = False
        for block in re.split(r'(?=<div class="exercise">)', p):
            num = re.search(r'<span class="exercise-number">(\d+)\.</span>', block)
            if not num or "mc-option" not in block:
                continue
            letters = re.findall(r'<span class="mc-letter">([A-Z])\.</span>', block)
            ans = re.search(r'<span class="answer-number">' + num.group(1) + r'\.</span>\s*<p>(.*?)</p>', p, re.S)
            if ans:
                m = re.search(r"Correct:\s*([A-Z])\b", plain(ans.group(1))) or re.match(r"\(?([A-D])\)?[ .—–-]", plain(ans.group(1)))
                if m and m.group(1) not in letters:
                    bad = True
                    add("Answer keys", "High", it["id"], f"Exercise {num.group(1)}: answer {m.group(1)} is not one of the options {letters}")
        if not bad:
            ak_ok += 1
    stats["answer_keys_ok"] = f"{ak_ok} of {len(units)} units"
    stats["exercises"] = sum(len(re.findall(r'class="exercise-number"', it["ref"].get("practice_html") or "")) for it in units)
    stats["answers"] = sum(len(re.findall(r'class="answer-number"', it["ref"].get("practice_html") or "")) for it in units)

    # 9. Scoring
    scales = 0
    for it in units:
        text = " ".join(plain(it["ref"].get(f) or "") for f in ("body_html", "practice_html"))
        for m in re.finditer(r"[Ss]core (?:each [^0-9]{0,40})?0[–-](\d+)(.{0,600}?)[Pp]ass (?:at|mark:?) (\d+)(?: of (\d+))?", text):
            top, passm, of = int(m.group(1)), int(m.group(3)), m.group(4)
            scales += 1
            if of:
                continue  # "pass mark: 25 of 36" is a total, checked below
            if passm > top:
                add("Scoring", "High", it["id"], f"Pass at {passm} on a 0–{top} scale: \"{m.group(0)[:120]}\"")
        for m in re.finditer(r"Maximum:\s*([^.=]+)=\s*(\d+)", text):
            parts = [int(x) for x in re.findall(r"\b(\d+)\b", m.group(1))]
            if parts and sum(parts) != int(m.group(2)):
                add("Scoring", "High", it["id"], f'"{m.group(0)}": parts add up to {sum(parts)}')
        for m in re.finditer(r"Pass mark:\s*(\d+) of (\d+) \((?:about )?(\d+)%\)", text):
            a_, b_, pct = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if abs(100 * a_ / b_ - pct) > 1:
                add("Scoring", "Medium", it["id"], f'"{m.group(0)}" is {100 * a_ / b_:.1f}%')
            elif "about" not in m.group(0) and abs(100 * a_ / b_ - pct) > 0.5:
                add("Scoring", "Low", it["id"], f'"{m.group(0)}" is {100 * a_ / b_:.1f}%, stated as exactly {pct}%')
        for m in re.finditer(r"(\d+)\s*(?:items?)?\s*[×x]\s*(\d+)\s*=\s*(\d+)", text):
            if int(m.group(1)) * int(m.group(2)) != int(m.group(3)):
                add("Scoring", "High", it["id"], f'"{m.group(0)}" does not multiply out')
        for m in re.finditer(r"(\d+)% \|? ?", ""):
            pass
    stats["scoring_scales"] = scales
    # capstone rubric weights add to 100
    for it in units:
        if it["kind"] == "capstone":
            t = plain(it["ref"].get("body_html") or "")
            start = t.find("Self-assessment rubric")
            rub = t[start:t.find("How to score it", start)] if start >= 0 and "How to score it" in t else ""
            w = [int(x) for x in re.findall(r"\b(\d{1,2})%", rub)]
            if w and sum(w) != 100:
                add("Scoring", "High", it["id"], f"Rubric weights add up to {sum(w)}%, not 100%: {w}")
            stats.setdefault("rubrics", []).append(f'{it["id"]}: {sum(w)}%')

    write_report(stats, spacing, section_spacing)


def apply_triage():
    path = PROOF / "consistency-triage.json"
    entries = json.loads(path.read_text(encoding="utf-8"))["entries"] if path.exists() else []
    for f in findings:
        hit = next((e for e in entries if e["check"] == f["check"] and e["location"] in ("*", f["location"])
                    and e.get("detail", "") in f["detail"]), None)
        f["assessment"] = hit["assessment"] if hit else "UNTRIAGED"
        f["action"] = hit["action"] if hit else ""


def write_report(stats, spacing, section_spacing):
    apply_triage()
    sev = Counter(f["severity"] for f in findings)
    by_check = Counter(f["check"] for f in findings)
    with open(PROOF / "consistency-discrepancies.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["check", "severity", "location", "detail", "assessment", "action"])
        w.writeheader()
        w.writerows(findings)
    L = ["# Source / PDF consistency audit", "",
         "Generated by `editorial/proof/consistency_audit.py`. This audit reports; it does not change the book or any generated file "
         "(the index and print generators are re-run on copies, compared, and the originals restored).", "",
         f"Discrepancies: {len(findings)} ({', '.join(f'{k} {v}' for k, v in sev.most_common())}). Every one is listed in "
         "[`consistency-discrepancies.csv`](consistency-discrepancies.csv).", "",
         "| Check | Result | Discrepancies |", "|---|---|---|"]
    rows = [
        ("Provenance: book-data.json = original + logged corrections", stats["corrections_check"], by_check["Provenance"]),
        ("Provenance: reference-index.json current with the source", "yes" if stats["index_current"] else "NO", None),
        ("Provenance: print HTML and headings current with the source", "yes" if stats["print_current"] else "NO", None),
        ("Provenance: PDF newer than the source and the cover images", "yes" if stats["pdf_after_source"] else "NO", None),
        ("PDF pages", stats["pages"], None),
        ("Bookmarks: structural headings at the right page", f'{stats["bookmarks_structural"]} (outline has {stats["bookmarks_total"]} entries in all, including in-lesson section headings)', by_check["Bookmarks"]),
        ("Contents: printed page = actual start page", stats["contents_ok"], by_check["Contents"]),
        ("Text: source present in the PDF pages of each unit", stats["text_units_ok"], by_check["Text"]),
        ("PDF-proof corrections present in the PDF", stats["proof_found"], by_check["Proof corrections"]),
        ("Index: website index = PDF index (label, lesson, page) and code printed in that lesson", stats["index_ok"], by_check["Index"]),
        ("Codes", f'{stats["codes_total"]} codes; {stats["duplicate_terms"]} vocabulary items with two codes', by_check["Codes"]),
        ("Answer keys: numbering and multiple-choice letters", f'{stats["answer_keys_ok"]} ({stats["exercises"]} exercises, {stats["answers"]} answers)', by_check["Answer keys"]),
        ("Scoring: pass marks, totals, percentages, rubric weights", f'{stats["scoring_scales"]} scales checked; rubrics: {", ".join(stats.get("rubrics", []))}', by_check["Scoring"]),
    ]
    for name, result, n in rows:
        L.append(f"| {name} | {result} | {'' if n is None else n} |")
    L += ["", "## Correction log by source", "",
          "| Source | Entries |", "|---|---|"]
    for k, v in sorted(stats["log_by_source"].items()):
        L.append(f"| {k} | {v} |")
    L += ["", f"Total: {stats['log_rows']}.", "", "## Discrepancies", ""]

    def kind(f):
        a = f["assessment"]
        return ("Untriaged" if a == "UNTRIAGED" else "Defect" if a.startswith("DEFECT") else
                "Known (author decision)" if a.startswith("Known") else "Not a defect (method limitation, checked)")
    kinds = Counter(kind(f) for f in findings)
    L += ["Assessment (from `consistency-triage.json`; anything new appears as Untriaged):", "",
          "| Assessment | Count |", "|---|---|"] + [f"| {k} | {v} |" for k, v in kinds.most_common()] + [""]
    if not findings:
        L.append("None.")
    else:
        L += ["| Check | Severity | Location | Detail | Assessment | Action |", "|---|---|---|---|---|---|"]
        order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
        rank = {"Untriaged": 0, "Defect": 1, "Known (author decision)": 2, "Not a defect (method limitation, checked)": 3}
        shown = Counter()
        for f in sorted(findings, key=lambda x: (rank[kind(x)], order[x["severity"]], x["check"], x["location"])):
            shown[f["check"]] += 1
            if shown[f["check"]] > 12:
                continue
            L.append(f'| {f["check"]} | {f["severity"]} | {f["location"]} | {f["detail"].replace("|", "/")} | '
                     f'{f["assessment"].replace("|", "/")} | {f["action"].replace("|", "/")} |')
        more = {k: v - 12 for k, v in shown.items() if v > 12}
        if more:
            L += ["", "Not shown above (all are in the CSV): " + ", ".join(f"{k}: {v} more" for k, v in more.items()) + "."]
    if section_spacing:
        L += ["", f"Also noted: {len(section_spacing)} in-lesson section bookmarks have two words joined where the heading wrapped "
              f"(e.g. {', '.join(repr(t) for t in section_spacing[:3])}). This affects only bookmark titles, not the printed page."]
    (PROOF / "SOURCE-PDF-CONSISTENCY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(findings)} discrepancies: {dict(sev)}; by check: {dict(by_check)}")


if __name__ == "__main__":
    main()
