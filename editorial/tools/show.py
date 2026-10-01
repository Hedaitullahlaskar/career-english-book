"""Print raw baseline HTML around a needle, for writing exact corrections.
Usage: python show.py ID "needle" [before] [after]   (searches all text fields)"""
import json
import io
import subprocess
import sys

from book import ROOT, by_id

from apply_corrections import BASELINE_COMMIT

sys.stdout.reconfigure(encoding="utf-8")

data = json.loads(subprocess.check_output(["git", "show", f"{BASELINE_COMMIT}:book-data.json"], cwd=ROOT).decode("utf-8"))
ref = by_id(data)[sys.argv[1]]["ref"]
needle = sys.argv[2]
before = int(sys.argv[3]) if len(sys.argv) > 3 else 100
after = int(sys.argv[4]) if len(sys.argv) > 4 else 500
for f in ("title", "objectives_html", "body_html", "practice_html", "purpose"):
    v = ref.get(f) or ""
    i = v.find(needle)
    while i != -1:
        print(f"----- {f} @{i}")
        print(v[max(0, i - before):i + after])
        i = v.find(needle, i + 1)
