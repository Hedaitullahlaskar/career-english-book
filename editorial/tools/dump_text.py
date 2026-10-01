"""Write a readable plain-text version of every lesson, one file per module,
for proofreading. Usage: python editorial/tools/dump_text.py OUT_DIR"""
import sys
from pathlib import Path

from book import items, load, to_text

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
data = load()
files = {}
for it in items(data):
    key = f'L{it["level"]}-M{it["module"]:02d}' if it["module"] else f'L{it["level"]}-{it["kind"]}'
    x = it["ref"]
    parts = [f'==================== {it["id"]} · {it["number"]} · {it["title"]}',
             f'[level {it["level"]} · module {it["module_title"]} · {x.get("estimated_minutes")} min]']
    if x.get("objectives_html"):
        parts.append("OBJECTIVES:\n" + to_text("<ul>" + x["objectives_html"] + "</ul>"))
    parts.append(to_text(x.get("body_html")))
    if x.get("practice_html"):
        parts.append("---- PRACTICE ----\n" + to_text(x["practice_html"]))
    files.setdefault(key, []).append("\n\n".join(parts))
for key, chunks in files.items():
    (out / f"{key}.txt").write_text("\n\n\n".join(chunks) + "\n", encoding="utf-8")
print(f"wrote {len(files)} files to {out}")
