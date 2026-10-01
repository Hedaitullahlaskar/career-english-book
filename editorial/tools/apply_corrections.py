"""Rebuild book-data.json from the baseline edition plus the logged corrections,
and regenerate the correction log.

    python editorial/tools/apply_corrections.py          # apply + write log
    python editorial/tools/apply_corrections.py --check  # verify only

Every correction lives in editorial/corrections/*.py as a fix(...) or rule(...)
call. Corrections are applied in file order to the baseline (the reviewed
edition at BASELINE_COMMIT), so each `find` must match the text exactly the
expected number of times -- a stale or ambiguous correction fails loudly
instead of silently doing nothing.
"""
import csv
import html
import json
import re
import subprocess
import sys
from pathlib import Path

from book import DATA, ROOT, by_id, items, plain

BASELINE_COMMIT = "61c769f"
CORR_DIR = ROOT / "editorial" / "corrections"
LOG_MD = ROOT / "editorial" / "CORRECTION-LOG.md"
LOG_CSV = ROOT / "editorial" / "correction-log.csv"
FIELDS = ("title", "objectives_html", "body_html", "practice_html", "purpose")

CATEGORIES = {
    "grammar": "Grammar / usage explanation",
    "pronunciation": "Pronunciation / word stress",
    "answer-key": "Exercise and answer key alignment",
    "assessment": "Assessment instructions and scoring",
    "continuity": "Story continuity",
    "production": "Production language / unfinished material",
    "language": "Natural professional English",
    "l1-support": "Bengali / Hindi support",
    "reference": "Reference codes and links",
    "audio": "Audio availability labelling",
    "structure": "Headings and structure",
    "typography": "Typography and consistency",
    "factual": "Factual / content accuracy",
}


class Entry:
    def __init__(self, kind, **kw):
        self.kind = kind
        self.__dict__.update(kw)


def load_corrections():
    entries = []

    def fix(target, find, replace, reason, category, field=None, count=1, source=None):
        entries.append(Entry("fix", target=target, find=find, replace=replace, reason=reason,
                             category=category, field=field, count=count, source=source,
                             file=current))

    def rule(name, pattern, replace, reason, category, fields=("body_html", "practice_html", "objectives_html"),
             flags=0, targets=None, expect=None):
        entries.append(Entry("rule", name=name, pattern=pattern, replace=replace, reason=reason,
                             category=category, fields=fields, flags=flags, targets=targets,
                             expect=expect, file=current))

    for path in sorted(CORR_DIR.glob("*.py")):
        current = path.name
        exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"),
             {"fix": fix, "rule": rule})
    return entries


def baseline():
    raw = subprocess.check_output(["git", "show", f"{BASELINE_COMMIT}:book-data.json"], cwd=ROOT)
    return json.loads(raw.decode("utf-8"))


def apply(data, entries):
    index = by_id(data)
    errors = []
    for e in entries:
        if e.kind == "fix":
            it = index.get(e.target)
            if not it:
                errors.append(f"[{e.file}] unknown target {e.target}")
                continue
            ref = it["ref"]
            fields = [e.field] if e.field else [f for f in FIELDS if isinstance(ref.get(f), str)]
            # Whitespace-tolerant: any run of whitespace in `find` matches any run in the source,
            # because the source HTML wraps lines mid-sentence.
            rx = re.compile(r"\s+".join(re.escape(p) for p in e.find.split()))
            found = sum(len(rx.findall(ref.get(f, ""))) for f in fields)
            if found != e.count:
                errors.append(f"[{e.file}] {e.target}: expected {e.count} match(es), found {found}: {e.find[:90]!r}")
                continue
            for f in fields:
                if rx.search(ref.get(f, "")):
                    ref[f] = rx.sub(lambda m: e.replace, ref[f])
                    e.field_used = f
        else:
            rx = re.compile(e.pattern, e.flags)
            e.hits = []
            units = list(items(data))
            if "purpose" in e.fields:
                units += [index[k] for k, v in index.items() if v["kind"] == "module"]
            for it in units:
                if e.targets and it["id"] not in e.targets:
                    continue
                for f in e.fields:
                    v = it["ref"].get(f)
                    if not isinstance(v, str):
                        continue
                    new, n = rx.subn(e.replace, v)
                    if n:
                        it["ref"][f] = new
                        e.hits.append((it["id"], f, n))
            total = sum(h[2] for h in e.hits)
            if e.expect is not None and total != e.expect:
                errors.append(f"[{e.file}] rule {e.name}: expected {e.expect} replacements, made {total}")
    return errors


def excerpt(s, limit=400):
    t = plain(s)
    return t if len(t) <= limit else t[:limit - 1] + "…"


def write_log(data, entries):
    index = by_id(data)
    rows = []
    for n, e in enumerate(entries, 1):
        if e.kind == "fix":
            it = index[e.target]
            rows.append({
                "no": n, "level": it["level"],
                "module": f'M{it["module"]:02d} {it.get("module_title") or ""}'.strip() if it.get("module") else "—",
                "lesson": f'{it["number"]} {it["title"]}' if it["kind"] != "module" else "(module description)",
                "id": e.target, "category": CATEGORIES[e.category],
                "original": excerpt(e.find), "replacement": excerpt(e.replace) or "(removed)",
                "reason": e.reason, "source": e.source or "",
            })
        elif e.targets and len({h[0] for h in e.hits}) == 1:
            total = sum(h[2] for h in e.hits)
            it = index[e.hits[0][0]]
            rows.append({
                "no": n, "level": it["level"],
                "module": f'M{it["module"]:02d} {it.get("module_title") or ""}'.strip() if it.get("module") else "—",
                "lesson": f'{it["number"]} {it["title"]}', "id": it["id"], "category": CATEGORIES[e.category],
                "original": f"/{e.pattern}/ ({total}×)",
                "replacement": e.replace if isinstance(e.replace, str) else "(computed)",
                "reason": e.reason, "source": "",
            })
        else:
            total = sum(h[2] for h in e.hits)
            ids = sorted({h[0] for h in e.hits})
            rows.append({
                "no": n, "level": "all", "module": "all",
                "lesson": f"{len(ids)} units", "id": "global rule: " + e.name,
                "category": CATEGORIES[e.category],
                "original": f"pattern /{e.pattern}/", "replacement": e.replace if isinstance(e.replace, str) else "(computed)",
                "reason": f"{e.reason} ({total} replacements)", "source": "",
            })
    with LOG_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["no"])
        w.writeheader()
        w.writerows(rows)

    md = ["# Career English — Correction Log", "",
          f"Generated by `editorial/tools/apply_corrections.py` from `editorial/corrections/*.py`.",
          f"Baseline: the reviewed edition at commit `{BASELINE_COMMIT}`. {len(rows)} logged corrections.",
          "", "Original and replacement text are shown as plain text (HTML tags removed).", ""]
    counts = {}
    for r in rows:
        counts[r["category"]] = counts.get(r["category"], 0) + 1
    md += ["| Category | Corrections |", "|---|---|"]
    md += [f"| {k} | {v} |" for k, v in sorted(counts.items(), key=lambda kv: -kv[1])]
    md.append("")
    last = None
    for r in rows:
        head = (r["level"], r["module"], r["lesson"])
        if head != last:
            if r["level"] == "all":
                md.append("\n## Global rules (whole book)\n")
            else:
                md.append(f'\n## Level {r["level"]} · {r["module"]} · {r["lesson"]} (`{r["id"]}`)\n')
            last = head
        md.append(f'**#{r["no"]} — {r["category"]}**' + (f' · source: {r["source"]}' if r["source"] else ""))
        md.append(f'- Original: {md_quote(r["original"])}')
        md.append(f'- Replacement: {md_quote(r["replacement"])}')
        md.append(f'- Reason: {r["reason"]}')
        md.append("")
    LOG_MD.write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    return len(rows)


def md_quote(s):
    return "“" + s.replace("|", "\\|").replace("\n", " ") + "”"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    check = "--check" in sys.argv
    entries = load_corrections()
    data = baseline()
    errors = apply(data, entries)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    out = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    current = DATA.read_text(encoding="utf-8").replace("\r\n", "\n")
    if check:
        ok = current == out
        print("book-data.json matches baseline + corrections" if ok else "book-data.json DIFFERS from baseline + corrections")
        sys.exit(0 if ok else 1)
    DATA.write_text(out, encoding="utf-8", newline="\n")
    n = write_log(data, entries)
    print(f"applied {len(entries)} corrections; log has {n} rows")


if __name__ == "__main__":
    main()
