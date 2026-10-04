"""Compose Role Instances from layers L0–L6 for local review (author Editorial Review).

Usage: python editorial/tools/curriculum/compose.py [--base DIR]

For each unit plan, collects the layer objects by key. When the L6 unit and all its layers are present, writes
previews/RIN-*.md (a readable review copy with layer provenance). Missing layers are listed, never invented.
Previews are review aids under editorial/ only: nothing is compiled into the website or the book.
"""
import argparse
import json
import sys

from cur import load, save, store

sys.stdout.reconfigure(encoding="utf-8")


def md_unit(plan, profile, objs, layers):
    u = objs[plan["layers"][-1]["key"]]["content"]
    L = [f"# {plan['id']} — {u['title']}", "",
         f"**PROTOTYPE (U-1 architecture validation). Not approved for publication.** Status: {objs[plan['layers'][-1]['key']]['status']}; "
         f"AI QA: {objs[plan['layers'][-1]['key']]['review']['aiQa']}; Editorial Review: author (PENDING until recorded); "
         f"Specialist: NOT_REQUIRED; Native: NOT_REQUIRED.", "",
         f"- Role Profile: {profile['id']} {profile['name']} · {profile['specialisation']}",
         f"- CEFR: {plan['cefr']} · Situation: {plan['situationTemplate']} · Functions: {', '.join(plan['functions'])}",
         "- Layers used: " + "; ".join(f"{x['layer']} {objs[x['key']]['id']}" for x in layers), "",
         "## 1. Context", f"{u['context']['setting']}", f"- You are: {u['context']['learnerRole']}",
         "- People: " + "; ".join(f"{s['name']} ({s['archetype']}, {s['relationship']})" for s in u['context']['stakeholders']),
         f"- Goal: {u['context']['objective']}"] + [f"- Note: {c}" for c in u["context"]["constraints"]] + [
         "", "## 2. Notice"]
    L += [f"**{t['speaker']}:** {t['text']}" + (f"  _{', '.join(t.get('functions', []))}_" if t.get("functions") else "") for t in u["notice"]["conversation"]["turns"]]
    L += ["", "## 3. Understand"] + [f"- **{k['text']}** ({k['function']}) {k.get('note', '')}" for k in u["understand"]["keyExpressions"]]
    L += [f"- {v['term']} — {v['definition']} _{v['example']}_ [{v.get('existingCode') or 'new'}]" for v in u["understand"]["vocabulary"]]
    for j in u.get("jobKnowledge", []):
        L += [f"- Job knowledge: **{j['title']}** — {j['text']}"]
    L += ["", "## 4. Guided practice"]
    for t in u["guidedPractice"]:
        L += [f"**{t['id']} ({t['type']})** {t['prompt']}"] + [f"  - {i['q']}" + (f" ({' / '.join(i['options'])})" if i.get("options") else "") for i in t["items"]]
    L += ["", "## 5. Role practice", u["rolePractice"]["instructions"]] + [f"- **{c['role']}**: {c['goal']} {c.get('info', '')}" for c in u["rolePractice"]["cards"]]
    L += ["", "## 6. Performance task", u["performanceTask"]["prompt"]] + [f"- {c}" for c in u["performanceTask"]["successCriteria"]]
    L += ["", "## 7. Feedback"] + [f"- {c}" for c in u["feedback"]["selfCheck"]] + [f"- {r['criterion']}: {r['weight']}%" for r in u["feedback"].get("rubric", [])]
    L += ["", "## 8. Review / retrieval"] + [f"- {r['prompt']} → {r['answer']}" for r in u["reviewRetrieval"]]
    L += ["", "## Answer key"] + [f"- {a['taskRef']}: {a['answer']}" for a in u["answerKey"]]
    return "\n".join(L) + "\n"


def run(base=None):
    index = load(store("content", "index.json", base=base), {})
    objs = {k: load(store("content", "objects", f"{v}.json", base=base)) for k, v in index.items()}
    out = []
    for f in sorted(store("plans", base=base).glob("RIN-*.json")):
        plan = load(f)
        profile = load(store("role-profiles", f"{plan['roleProfile']}.json", base=base))
        missing = [x["key"] for x in plan["layers"] if x["key"] not in objs]
        row = {"id": plan["id"], "title": plan["title"], "missingLayers": len(missing), "composed": False}
        if not missing:
            save_path = store("previews", f"{plan['id']}.md", base=base)
            save_path.parent.mkdir(parents=True, exist_ok=True)
            save_path.write_text(md_unit(plan, profile, objs, plan["layers"][:-1]), encoding="utf-8")
            row["composed"] = True
            row["layerObjects"] = [objs[x["key"]]["id"] for x in plan["layers"]]
        else:
            row["missing"] = missing[:3] + (["…"] if len(missing) > 3 else [])
        out.append(row)
    save(store("logs", "compose.json", base=base), out)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    a = ap.parse_args()
    res = run(a.base)
    print(json.dumps({"units": len(res), "composed": sum(r["composed"] for r in res),
                      "awaitingLayers": sum(not r["composed"] for r in res)}, indent=1))
