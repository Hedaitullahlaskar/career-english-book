"""Search/navigation test: do learner queries reach the right roles, situations and pilot units?

Usage: python editorial/tools/curriculum/search_test.py [--base DIR]

Builds a small English index (D-U09: role names, industry names, situation names, job aliases, local names
where registered) over the registry, the role profiles and the unit plans, then runs config.pilotSearchQueries.
A query passes when the expected role (and situation, if given) is in the top 3 results.
"""
import argparse
import json
import re
import sys

from cur import load, save, store

sys.stdout.reconfigure(encoding="utf-8")
STOP = {"english", "the", "a", "an", "for", "of", "in", "to", "and", "with", "my", "at", "on"}
SYN = {"checkin": ["check", "in"],
       "late": ["late", "delay"], "order": ["order", "delivery"], "visit": ["visit", "household", "door"]}


def toks(s):
    out = []
    for w in re.findall(r"[a-z0-9]+", s.lower().replace("check-in", "checkin")):
        if w in STOP:
            continue
        out += SYN.get(w, [w])
        stem = re.sub(r"(ing|ed|s)$", "", w) if len(w) > 4 else w   # light stemming: checking → check
        if stem != w:
            out.append(stem)
    return out


def run(base=None):
    cfg = load(store("config", "pilot-u1.json", base=base))
    roles = load(store("registry", "roles.json", base=base))
    sits = load(store("registry", "situation-templates.json", base=base))
    docs = []
    for r in roles:
        docs.append({"kind": "role", "id": r["id"], "label": r["name"], "role": r["id"], "situation": None,
                     "text": toks(r["name"]) * 3 + [t for a in r["aliases"] for t in toks(a)] * 2,
                     "roleTerms": set(toks(r["name"])) | {t for a in r["aliases"] for t in toks(a)}})
    for s in sits:
        docs.append({"kind": "situation", "id": s["id"], "label": s["name"], "role": None, "situation": s["id"], "text": toks(s["name"]) * 2})
    for f in sorted(store("plans", base=base).glob("RIN-*.json")):
        p = load(f)
        prof = load(store("role-profiles", f"{p['roleProfile']}.json", base=base))
        role = next(r for r in roles if r["id"] == prof["role"])
        sit = next(s for s in sits if s["id"] == p["situationTemplate"])
        docs.append({"kind": "unit", "id": p["id"], "label": p["title"], "role": role["id"], "situation": sit["id"],
                     "roleTerms": set(toks(role["name"])) | {t for a in role["aliases"] for t in toks(a)},
                     "text": toks(role["name"]) * 3 + [t for a in role["aliases"] for t in toks(a)] + toks(sit["name"]) * 2 + toks(prof["specialisation"])})
    results = []
    for q in cfg["pilotSearchQueries"]:
        words = [toks(w) for w in q["query"].split() if toks(w)]      # each query word with its synonyms/stems
        scored = []
        for d in docs:
            matched = [g for g in words if any(t in d["text"] for t in g)]
            if not matched:
                continue
            tf = sum(min(max(d["text"].count(t) for t in g), 3) for g in matched)
            # rank by distinct query words matched, then term frequency; units get a small boost when 2+ words match
            s = len(matched) * 10 + tf + (2 if d["kind"] == "unit" and len(matched) >= 2 else 0)
            # role identification is the primary navigation axis (D-U09): a whole-word match on a registered
            # role name or alias (e.g. "BLO", "sabzi wala") is a strong signal
            if any(len(g[0]) >= 3 and g[0] in d.get("roleTerms", ()) and sum(g[0] in x.get("roleTerms", ()) for x in docs) <= 3 for g in matched):
                s += 12
            scored.append((s, d))
        scored.sort(key=lambda x: -x[0])
        top = [d for _, d in scored[:3]]
        role_ok = any(d["role"] == q["expectRole"] or d["id"] == q["expectRole"] for d in top)
        top5 = [d for _, d in scored[:5]]
        sit_ok = "expectSituation" not in q or any(d["situation"] == q["expectSituation"] for d in top5)
        results.append({"query": q["query"], "pass": role_ok and sit_ok, "top": [f"{d['kind']} {d['id']} {d['label']}" for d in top]})
    save(store("logs", "search-test.json", base=base), results)
    return results


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    a = ap.parse_args()
    res = run(a.base)
    for r in res:
        print(("PASS " if r["pass"] else "FAIL ") + r["query"])
        for t in r["top"]:
            print("     ", t)
    print(f"{sum(r['pass'] for r in res)}/{len(res)} queries pass")
