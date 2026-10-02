"""Build reference-index.json: where each reference code (V-, PAT-, MIS-, CF-, GIC-, TL-, TIP-, P-)
is introduced, a short label for it, and every lesson that uses it.

The book introduces a code before it recycles it, so the first occurrence in reading order is
taken as its home. Usage: python editorial/tools/build_reference_index.py
"""
import json
import re
import sys
from pathlib import Path

from book import ROOT, items, load, plain

sys.stdout.reconfigure(encoding="utf-8")

TYPES = {
    "V": "Vocabulary",
    "PAT": "Sentence patterns",
    "GIC": "Grammar in context",
    "CF": "Communication formulas",
    "TL": "Career English Upgrade Ladders",
    "MIS": "Common mistakes",
    "TIP": "Tips",
    "P": "Useful phrases",
}
CODE = re.compile(r"\b(V|PAT|GIC|CF|TL|MIS|TIP|P)-(\d{3,4})\b")
BLOCK_START = re.compile(r"<(p|li|tr|h2|h3|h4|div class=\"callout-label\")\b[^>]*>")
DASH = r"\s*(?:—|–|-{1,2}|:)\s*"


def block_around(html, pos):
    """The smallest enclosing paragraph-like block of the match at pos."""
    starts = [m for m in BLOCK_START.finditer(html, 0, pos)]
    if not starts:
        return html[max(0, pos - 200):pos + 200]
    m = starts[-1]
    tag = m.group(1).split()[0]
    end = html.find(f"</{tag}>", pos)
    return html[m.start():end if end != -1 else pos + 300]


def clean(label):
    label = re.sub(r"[❌✅⚠️]", "", label)
    quoted = re.match(r'^\s*["“]([^"”]{3,})["”]', label)
    if quoted:  # a pattern quoted and then explained: keep just the quoted pattern
        label = quoted.group(1)
    label = re.sub(r"^(Grammar in Context|Grammar in context|Communication Formula|Common Mistake|Pattern|Structure)\s*:?\s*", "", label)
    label = re.sub(r"^(Unclear|Wrong|Weak|Incorrect)\s*:\s*", "", label.strip())
    label = label.strip(" \"'“”‘’():;,.—–-")
    if label.count("[") > label.count("]"):
        label += "]"
    if label.count("(") > label.count(")"):
        label += ")"

    label = re.sub(r"\s+", " ", label)
    if len(label) > 90:
        label = label[:90].rsplit(" ", 1)[0].rstrip(",;:—–-") + "…"
    if label.count('"') % 2:
        label = label.replace('"', "")
    return label


def label_for(code, block):
    text = plain(block)
    esc = re.escape(code)
    # "<code>V-0015</code> <strong>team</strong>" or a table row: the term follows the code
    m = re.search(esc + r"\s*</code>\s*(?:</strong>)?\s*(?:</td>\s*<td>)?\s*(?:<strong>)?([^<]{2,80})", block)
    if m and m.group(1).strip(" —–-:"):
        cand = m.group(1).strip()
        if not re.match(r"^[—–-]", cand):
            return clean(re.split(r"\s[—–]\s|\s--\s", cand)[0])
    # "Name of the thing (CODE)"
    m = re.search(r"([^()]{3,90})\(\s*" + esc + r"\b[^)]*\)", text)
    if m:
        before = m.group(1)
        pre = block[:block.find(code)]
        adjacent = re.search(r"<(strong|em)>([^<]{1,70})</\1>\s*\(\s*(?:<code>)?\s*$", pre)
        if adjacent:  # "<em>term</em> (CODE)": the term right before the code
            return clean(adjacent.group(2))
        strong = re.findall(r"<strong>(.*?)</strong>", pre)
        if strong and len(plain(strong[-1])) <= 70 and not CODE.search(plain(strong[-1])):
            return clean(plain(strong[-1]))
        return clean(re.split(r"[.!?]\s", before)[-1])
    # "CODE — Name: ..." / "CODE: Name"
    m = re.search(esc + DASH + r"([^.:;(]{3,90})", text)
    if m:
        return clean(m.group(1))
    # "The Polite Redirect Formula — CODE"
    m = re.search(r"([^.:;()]{3,90})" + DASH + esc + r"\s*$", text)
    if m:
        return clean(m.group(1))
    # "<li><strong>term</strong> (note) (CODE) -- ..."
    m = re.match(r"\s*<(?:li|p)[^>]*>\s*<strong>([^<]{1,70})</strong>", block)
    if m and block.find(code) < 200:
        return clean(m.group(1))
    return ""


GENERIC = re.compile(r"^(Common Mistakes?|Tip|Mistake|The mistake|Common mistake|Tip ·|(V|PAT|GIC|CF|TL|MIS|TIP|P)-\d{3,4})$", re.I)


def label_after(html, pos):
    """For a code in a heading or callout label, describe it with the text that follows."""
    end = html.find(">", html.find("</", pos)) + 1
    text = plain(html[end:end + 700])
    text = re.sub(r"^\s*" + CODE.pattern + DASH, "", text)
    text = re.sub(r"^\s*(?:[—–-]\s*)?(?:the mistake|mistake|tip)\s*:\s*", "", text, flags=re.I)
    first = re.split(r"(?<=[.!?])\s|\s[—–]\s|\s--\s|:\s", text.strip(), maxsplit=1)[0]
    return clean(first)


def defining_heading(html, code):
    """The label from the heading that introduces a code, e.g.
    <h2>Grammar in Context: Meeting Minutes Structure (PAT-0068)</h2>  ->  Meeting Minutes Structure
    <h2>Common Mistake (MIS-0090)</h2><p><strong>Mistake:</strong> Sending a vague invitation…  ->  that sentence
    Only used for codes whose first mention in the lesson is not already the heading or a labelled definition."""
    h = re.search(r"<h[2-4]>([^<]*)\(\s*" + re.escape(code) + r"\s*\)\s*</h[2-4]>", html)
    if not h:
        return ""
    name = clean(plain(h.group(1)))
    if name and not GENERIC.match(name):
        return name
    mistake = re.match(r"\s*<p><strong>Mistake:</strong>\s*(.*?)</p>", html[h.end():], re.S)
    if mistake:
        return clean(re.split(r"(?<=[.!?])\s|,\s(?:so|which|leaving|instead)\b|\s[—–]\s", plain(mistake.group(1)), maxsplit=1)[0])
    return ""


def main():
    data = load()
    index = {}
    order = []
    for it in items(data):
        html = " ".join(str(it["ref"].get(f, "")) for f in ("body_html", "practice_html"))
        for m in CODE.finditer(html):
            code = m.group(0)
            entry = index.get(code)
            if entry is None:
                entry = index[code] = {"type": m.group(1), "home": it["id"], "label": "", "uses": []}
                order.append(code)
            if not entry["label"] and entry["home"] == it["id"]:
                callout = re.search(r'callout-label">[^<]*<code>' + code + r'</code></div><div class="callout-wrong">(.*?)</div>', html)
                if callout:
                    entry["label"] = '“' + clean(plain(callout.group(1))) + '” (mistake)'
                    continue
                # A pattern or mistake with its own heading in this lesson is named by that heading, even when
                # an earlier paragraph mentions it first ("…following PAT-0061 (Purpose + …)").
                heading = defining_heading(html, code)
                if heading:
                    entry["label"] = heading
                    continue
                label = label_for(code, block_around(html, m.start()))
                if not label or GENERIC.match(label):
                    label = label_after(html, m.start())
                entry["label"] = label
            if it["id"] not in entry["uses"]:
                entry["uses"].append(it["id"])

    units = {}
    for it in items(data):
        if it["kind"] == "lesson":
            ref = f'Level {it["level"]} · Lesson {it["number"]}'
        else:
            ref = f'Level {it["level"]} · {it["kind"].capitalize()}'
        units[it["id"]] = {"ref": ref, "title": it["title"]}

    for e in index.values():
        if e["type"] not in ("V", "P") and e["label"]:
            e["label"] = e["label"][:1].upper() + e["label"][1:]
    out = {
        "types": TYPES,
        "codes": {c: index[c] for c in sorted(index, key=lambda c: (list(TYPES).index(index[c]["type"]), int(c.split("-")[1])))},
        "units": units,
    }
    path = ROOT / "reference-index.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    missing = [c for c, e in index.items() if not e["label"]]
    print(f"{len(index)} codes written to {path.name}; {len(missing)} without a label")
    for c in missing[:40]:
        print("  no label:", c, index[c]["home"])


if __name__ == "__main__":
    main()
