"""Shared helpers for the Career English editorial tools.

book-data.json is the single authoritative content file: index.html (website)
and print.html (PDF edition) both render from it.
"""
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "book-data.json"
TEXT_FIELDS = ("title", "objectives_html", "body_html", "practice_html")


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))


def save(data):
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8", newline="\n")


def items(data):
    """Yield every readable unit (lesson, assessment, capstone) with context."""
    for level in data:
        ln = level["level_number"]
        for mi, mod in enumerate(level["modules"], 1):
            for lesson in mod["lessons"]:
                yield {
                    "kind": "lesson", "id": lesson["lesson_id"], "ref": lesson,
                    "level": ln, "level_title": level["title"],
                    "module": mi, "module_id": mod["module_id"], "module_title": mod["title"],
                    "number": f'{mi}.{lesson["sequence_in_module"]}',
                    "title": lesson["title"],
                }
        for kind in ("assessment", "capstone"):
            if level.get(kind):
                x = level[kind]
                yield {
                    "kind": kind, "id": x["id"], "ref": x,
                    "level": ln, "level_title": level["title"],
                    "module": None, "module_id": None, "module_title": None,
                    "number": kind.capitalize(), "title": x["title"],
                }


def modules(data):
    for level in data:
        for mi, mod in enumerate(level["modules"], 1):
            yield level, mi, mod


def by_id(data):
    """Map lesson/assessment/capstone ids and module ids to their dicts."""
    out = {}
    for it in items(data):
        out[it["id"]] = it
    for level, mi, mod in modules(data):
        out[mod["module_id"]] = {"kind": "module", "id": mod["module_id"], "ref": mod,
                                 "level": level["level_number"], "module": mi,
                                 "module_title": mod["title"], "title": mod["title"],
                                 "number": f"Module {mi}"}
    return out


class _Text(HTMLParser):
    BLOCK = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "table", "ul", "ol", "br"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.cell = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "tr":
            self.out.append("\n|")
        elif tag in ("td", "th"):
            self.out.append(" ")
        elif tag == "div" and cls in ("exercise", "answer-item", "dialogue-turn", "mc-option",
                                      "matching-row", "dialogue-setting", "dialogue-box-label",
                                      "dialogue-scene-label", "callout-label", "callout-wrong",
                                      "callout-right", "callout-why", "dialogue-note"):
            self.out.append("\n")
        elif tag in ("p", "br", "table") or (tag == "div" and cls in ("exercise-prompt", "exercises-block", "answer-key-block")):
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("td", "th"):
            self.out.append(" |")

    def handle_data(self, data):
        self.out.append(re.sub(r"\s+", " ", data))


def to_text(fragment):
    p = _Text()
    p.feed(fragment or "")
    txt = "".join(p.out)
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()


def plain(fragment):
    """Collapse an HTML fragment to a single line of text (for searching)."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment or ""))).strip()
