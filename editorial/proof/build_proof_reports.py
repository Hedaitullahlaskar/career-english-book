"""Build the proofreading checklist and issue register for the PDF proof.

Usage: python editorial/proof/build_proof_reports.py <pdftext.json>

Inputs
  editorial/print/pages.json, headings.json   where each unit starts in the PDF
  editorial/correction-log.csv                corrections labelled "PDF proof, batch N"
  editorial/proof/findings.csv                findings that did not need a text change
  editorial/proof/auto-checks.csv             automated-check flags (auto_checks.py)
  editorial/proof/review-status.json          which units each batch has reviewed
Outputs
  editorial/proof/PROOF-CHECKLIST.md          one row per unit
  editorial/proof/PROOF-ISSUES.csv            every issue: unit, PDF page, original, correction, reason, status

Nothing is ever marked "approved": approval needs the human proofread and, where Bengali/Hindi
text is present, a native speaker.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from book import ROOT, items, load  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
PROOF = ROOT / "editorial" / "proof"
PRINT = ROOT / "editorial" / "print"


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def main():
    pdftext = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    page_text = {p["page"]: norm(" ".join(l["text"] for l in p["lines"])) for p in pdftext}
    pages = json.loads((PRINT / "pages.json").read_text(encoding="utf-8"))
    heads = json.loads((PRINT / "headings.json").read_text(encoding="utf-8"))
    starts = sorted((pages[h["key"]], h["key"]) for h in heads if h["key"] in pages)
    rng = {}
    for i, (p, k) in enumerate(starts):
        rng[k] = (p, starts[i + 1][0] - 1 if i + 1 < len(starts) else len(pdftext) - 1)

    status = json.loads((PROOF / "review-status.json").read_text(encoding="utf-8"))
    reviewed = {}
    for b in status["batches"]:
        for u in b["units"]:
            reviewed[u] = b

    data = load()
    units = list(items(data))
    has_l1 = {it["id"]: ('class="bn"' in str(it["ref"]) or 'class="hi"' in str(it["ref"])) for it in units}

    def find_page(unit, snippet):
        a, b = rng.get(unit, (1, len(pdftext)))
        words = [w for w in re.findall(r"[A-Za-z0-9]+", snippet)]
        for size in (8, 6, 4):
            for start in range(0, max(1, len(words) - size + 1), 2):
                probe = norm(" ".join(words[start:start + size]))
                if len(probe) < 12:
                    continue
                for p in range(a, b + 1):
                    if probe in page_text.get(p, ""):
                        return str(p)
        return f"{a}–{b}" if unit in rng else ""

    issues = []
    for r in csv.DictReader(open(ROOT / "editorial" / "correction-log.csv", encoding="utf-8")):
        if not r["source"].startswith("PDF proof"):
            continue
        m = re.match(r"PDF proof, batch (\d+)(?: · (.*))?", r["source"])
        batch, how = m.group(1), (m.group(2) or "editorial review")
        unit = r["id"] if r["id"].startswith("CE-") else ""
        page = find_page(unit, r["replacement"]) if unit else "several"
        issues.append({
            "batch": batch, "check": "Automated check" if "automated" in how else "Editorial review",
            "unit": unit or r["id"], "unit_ref": r["lesson"] if unit else r["lesson"], "pdf_page": page,
            "category": r["category"], "original": r["original"], "correction": r["replacement"],
            "reason": r["reason"], "status": "Applied (in correction log #" + r["no"] + ")",
        })
    for r in csv.DictReader(open(PROOF / "findings.csv", encoding="utf-8")):
        issues.append({
            "batch": r["batch"], "check": r["check"], "unit": r["unit"], "unit_ref": r.get("unit_ref", ""),
            "pdf_page": r["pdf_page"], "category": r["category"], "original": r["original"],
            "correction": r["proposed"], "reason": r["reason"], "status": r["status"],
        })
    issues.sort(key=lambda x: (int(x["batch"]), x["unit"], str(x["pdf_page"])))
    with open(PROOF / "PROOF-ISSUES.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["no", "batch", "check", "unit", "unit_ref", "pdf_page", "category",
                                          "original", "correction", "reason", "status"])
        w.writeheader()
        for n, row in enumerate(issues, 1):
            w.writerow({"no": n, **row})

    auto = defaultdict(list)
    for r in csv.DictReader(open(PROOF / "auto-checks.csv", encoding="utf-8")):
        auto[r["unit"]].append(r["flag"])
    per_unit = Counter(i["unit"] for i in issues if i["status"].startswith("Applied"))

    # Human and native-language status come from the registers that reviewers fill in.
    human, approved_units = {}, set()
    hp = PROOF / "HUMAN-PROOFREAD-REGISTER.csv"
    if hp.exists():
        for r in csv.DictReader(open(hp, encoding="utf-8")):
            key = r["Unit"].split(" — ")[0]
            human[key] = r["Proofread Status"] or "PENDING"
            if r["Approved"].strip().upper() == "YES":
                approved_units.add(key)
    native = defaultdict(Counter)
    nl = PROOF / "NATIVE-LANGUAGE-REVIEW.csv"
    if nl.exists():
        for r in csv.DictReader(open(nl, encoding="utf-8")):
            if r["Language"] in ("Bengali", "Hindi"):
                native[r["Unit"]]["approved" if r["Approved"].strip().upper() == "YES" else "open"] += 1

    def native_txt(uid):
        c = native.get(uid)
        if not c:
            return "n/a"
        return "Approved" if not c["open"] else f'Pending ({c["open"]} items)'

    gates = json.loads((PROOF / "publication-gates.json").read_text(encoding="utf-8"))["gates"]
    approval = next(g for g in gates if g["gate"] == "Publication Approval")
    others_open = [g["gate"] for g in gates if g["gate"] != "Publication Approval" and g["status"] != "PASS"]
    if approval["status"].upper() != "NO" and others_open:
        sys.exit(f"Refusing to show Publication Approval = {approval['status']} while these gates are not PASS: {', '.join(others_open)}")

    out = ["# PDF proofreading checklist", "",
           "## Publication gate", "",
           "| Gate | Status |", "|---|---|"]
    out += [f'| {g["gate"]} | {"**" + g["status"] + "**" if g["gate"] == "Publication Approval" else g["status"]} |' for g in gates]
    out += ["", "Evidence for each gate (from `publication-gates.json`):", ""]
    out += [f'- **{g["gate"]}:** {g["evidence"]}' for g in gates]
    out += ["", "**NOT READY FOR PUBLICATION.**", "",
            "## Units", "",
            "One row per unit of the print edition (`editorial/print/Career-English-Master.pdf`).",
            "", "Columns:",
            "- **Automated**: the automated layout and typography checks (`auto_checks.py`) ran on this unit; flags are listed, and each was reviewed (see PROOF-ISSUES.csv).",
            "- **Editorial review**: read in full by Claude, from the rendered PDF text, in the batch shown. This is not a substitute for a human proofread.",
            "- **Proof fixes**: corrections applied during this proof (all are in the correction log).",
            "- **Human proofread**: the status in `HUMAN-PROOFREAD-REGISTER.csv`, entered by the human proofreader.",
            "- **Native speaker (bn/hi)**: open items for this unit in `NATIVE-LANGUAGE-REVIEW.csv` (Bengali/Hindi text only; English statements about Bengali/Hindi are in the register too).",
            "- **Approved**: from the proofread register's Approved column. No unit is approved until the human checks are signed off.", "",
            "| Unit | Ref | Title | PDF pages | Automated | Editorial review | Proof fixes | Human proofread | Native speaker (bn/hi) | Approved |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    fm = rng.get("how-to-use")
    b = reviewed.get("front-matter")
    out.append(f"| front-matter | — | Cover, edition page, contents, How to Use | 1–{fm[1] if fm else ''} | run | "
               f"{'Batch ' + str(b['batch']) if b else 'Not yet reviewed'} | {per_unit.get('front-matter', 0)} | "
               f"{human.get('FRONT-MATTER', 'PENDING')} | n/a | {'Yes' if 'FRONT-MATTER' in approved_units else 'No'} |")
    for it in units:
        a, z = rng.get(it["id"], ("", ""))
        ref = f'L{it["level"]} {it["number"]}' if it["kind"] == "lesson" else f'L{it["level"]} {it["kind"]}'
        flags = Counter(auto.get(it["id"], []))
        a_txt = "run, no flags" if not flags else "run; " + ", ".join(f"{k} ×{v}" for k, v in flags.items())
        b = reviewed.get(it["id"])
        e_txt = f"Batch {b['batch']} (complete)" if b else "Not yet reviewed"
        out.append(f'| {it["id"]} | {ref} | {it["title"]} | {a}–{z} | {a_txt} | {e_txt} | {per_unit.get(it["id"], 0)} | '
                   f'{human.get(it["id"], "PENDING")} | {native_txt(it["id"])} | {"Yes" if it["id"] in approved_units else "No"} |')
    b = reviewed.get("index")
    ix = rng.get("index")
    out.append(f"| index | — | Reference Index and back cover | {ix[0] if ix else ''}–{len(pdftext)} | run | "
               f"{'Batch ' + str(b['batch']) if b else 'Not yet reviewed'} | 0 | {human.get('BACK-MATTER', 'PENDING')} | n/a | "
               f"{'Yes' if 'BACK-MATTER' in approved_units else 'No'} |")
    done = sum(1 for it in units if it["id"] in reviewed)
    h_done = sum(1 for it in units if human.get(it["id"], "PENDING").upper() not in ("PENDING", ""))
    l1_units = [u for u in native]
    n_done = sum(1 for u in l1_units if not native[u]["open"])
    out += ["", f"Editorial review: {done} of {len(units)} units complete. Human proofread: {h_done} of {len(units)}. "
            f"Native-speaker review: {n_done} of {len(l1_units)} units with Bengali/Hindi text. "
            f"Approved: {sum(1 for it in units if it['id'] in approved_units)}."]
    (PROOF / "PROOF-CHECKLIST.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(issues)} issues; editorial review {done}/{len(units)} units")


if __name__ == "__main__":
    main()
