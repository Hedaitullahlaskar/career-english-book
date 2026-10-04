"""Ingest a ChatGPT response packet into the curriculum store and run AI QA.

Usage: python editorial/tools/curriculum/ingest.py RESPONSE.json [--base DIR] [--revise]

Steps (D-U10): validate the response → refuse duplicate generation → validate each object →
vocabulary: reuse existing codes, allocate new V-<SCOPE>-<NUMBER> codes, reject collisions (D-U07) →
store as GENERATED with provenance → AI QA (automated checks) → review records → usage log.
Status after a clean AI QA is AI_QA. Editorial Review is the author's (D-U13b); Specialist and Native
Review are recorded as NOT_REQUIRED for U-1 with reasons. Nothing is approved, compiled or published here.
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
from collections import Counter

from cur import (CODE_TYPES, CORE_CODE, ENGINE_CODE, L1_SCRIPT, core_codes, estimate_tokens, load, next_id, save,
                 schema, scope_codes, store, validate, words)
from plan import LAYER_FIELDS

sys.stdout.reconfigure(encoding="utf-8")
TYPE_LAYER = {"function-exponents": "L0", "situation": "L1", "core-module": "L2", "role-core": "L3",
              "context-overlay": "L4", "seniority-overlay": "L5", "unit": "L6"}
ID_PREFIX = {"L0": "FEX", "L1": "SCN", "L2": "CMC", "L3": "RCO", "L4": "CTX", "L5": "SNO"}
US_SPELLINGS = {"color": "colour", "colors": "colours", "favor": "favour", "favorite": "favourite", "center": "centre", "organize": "organise",
                "organized": "organised", "organization": "organisation", "realize": "realise", "apologize": "apologise", "behavior": "behaviour",
                "neighbor": "neighbour", "analyze": "analyse", "catalog": "catalogue", "check (payment)": "cheque", "license (noun)": "licence",
                "canceled": "cancelled", "traveled": "travelled", "jewelry": "jewellery", "program (plan)": "programme", "mom": "mum"}
US_RE = re.compile(r"\b(" + "|".join(k for k in US_SPELLINGS if " " not in k) + r")\b", re.I)
BRANDS = re.compile(r"\b(Swiggy|Zomato|Uber|Ola|Rapido|Dunzo|Blinkit|Zepto|Amazon|Flipkart|Paytm|PhonePe|GPay|Google Pay|Maruti|Suzuki|Hyundai|Tata|Mahindra|"
                    r"Toyota|Honda|Kia|Infosys|TCS|Wipro|Taj|Oberoi|Marriott|Hilton|ITC)\b")
DRIVING = re.compile(r"\b(seat ?belt|speed limit|brake|indicator|overtak\w*|traffic rules?|helmet|lane|accelerat\w*|steer\w*)\b", re.I)
STOP = set("a an the and or but if then to of in on at for with from by is are was were be been am i you he she we they it this that these those "
           "my your our their his her its me us them do does did not no yes so very can could will would should please ok okay sir madam".split())


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def finding(sev, check, msg, where=""):
    return {"severity": sev, "check": check, "message": msg, "where": where}


def content_of(record):
    return record.get("content", record)


def norm_term(t):
    return re.sub(r"[^a-z0-9 ]+", "", t.lower().replace("-", " ")).strip()


def qa_layer(layer, key, c, cfg):
    out = []
    for f in LAYER_FIELDS[layer]:
        if f not in c:
            out.append(finding("error", "schema", f"missing field '{f}'", key))
    sl = cfg["sizeLimits"]
    if layer == "L0":
        ex = c.get("exponents", [])
        lo, hi = sl["L0"]["exponentsPerFunctionLevel"]
        if not lo <= len(ex) <= hi:
            out.append(finding("warning", "size", f"{len(ex)} exponents (expected {lo}–{hi})", key))
        for e in ex:
            if len(words(e)) > sl["L0"]["maxWordsPerExponent"]:
                out.append(finding("warning", "size", f"exponent over {sl['L0']['maxWordsPerExponent']} words: {e[:60]}", key))
    if layer == "L1" and len(words(c.get("description", ""))) > sl["L1"]["maxDescriptionWords"]:
        out.append(finding("warning", "size", "description too long", key))
    if layer == "L4" and len(words(c.get("differenceStatement", ""))) < 8:
        out.append(finding("error", "industryRealism", "missing or empty differenceStatement (noun-swap risk)", key))
    return out


def text_of_unit(u):
    return " ".join(t["text"] for t in u["notice"]["conversation"]["turns"])


def qa_unit(plan, u, cfg, base, index):
    out = [finding("error", "schema", e) for e in validate(u, schema("unit", base))]
    if out:
        return out
    if u["cefr"] != plan["cefr"]:
        out.append(finding("error", "cefr", f"unit cefr {u['cefr']} ≠ plan {plan['cefr']}"))
    turns = u["notice"]["conversation"]["turns"]
    learner = [t for t in turns if t.get("learner")]
    if not learner:
        out.append(finding("error", "conversation", "no learner turns marked"))
    covered = {f for t in learner for f in t.get("functions", [])}
    for f in plan["functions"]:
        if f not in covered:
            out.append(finding("error", "functionCoverage", f"{f} not realised in a learner turn"))
    for f in plan.get("excludedFunctions", []):
        if any(f["function"] in t.get("functions", []) for t in turns):
            out.append(finding("error", "constraint", f"excluded function {f['function']} used"))
    sl = cfg["sizeLimits"]["L6"]
    lo, hi = sl["conversationTurns"].get(plan["cefr"], [4, 20])
    if not lo <= len(turns) <= hi:
        out.append(finding("warning", "cefrFit", f"{len(turns)} turns (expected {lo}–{hi} at {plan['cefr']})"))
    mx = sl["maxWordsPerLearnerTurn"].get(plan["cefr"], 30)
    for t in learner:
        n = len(words(t["text"]))
        if n > mx:
            out.append(finding("error" if n > mx * 1.5 else "warning", "cefrFit", f"learner turn {t['n']} has {n} words (limit {mx})", f"turn {t['n']}"))
    nv = [v for v in u["understand"]["vocabulary"] if not v.get("existingCode")]
    vlo, vhi = sl["newVocabulary"].get(plan["cefr"], [0, 12])
    if not vlo <= len(nv) <= vhi:
        out.append(finding("warning", "vocabulary", f"{len(nv)} new terms (expected {vlo}–{vhi})"))
    tlo, thi = sl["guidedPracticeTasks"]
    if not tlo <= len(u["guidedPractice"]) <= thi:
        out.append(finding("warning", "size", f"{len(u['guidedPractice'])} guided-practice tasks (expected {tlo}–{thi})"))
    allt = json.dumps(u, ensure_ascii=False)
    if L1_SCRIPT.search(allt):
        out.append(finding("error", "language", "Bengali/Devanagari script found (not allowed in U-1)"))
    for m in sorted({m.group(0).lower() for m in US_RE.finditer(allt)}):
        out.append(finding("warning", "englishUK", f"US spelling '{m}' (UK: {US_SPELLINGS[m]})"))
    for m in sorted({m.group(0) for m in BRANDS.finditer(allt)}):
        out.append(finding("warning", "style", f"real brand/company name '{m}'"))
    if any("driving" in c.lower() or "traffic" in c.lower() for c in plan["constraints"]):
        for m in sorted({m.group(0).lower() for m in DRIVING.finditer(text_of_unit(u))}):
            out.append(finding("warning", "constraint", f"possible driving/safety instruction '{m}' — author to check (DRV constraint)"))
    task_ids = {t["id"] for t in u["guidedPractice"]}
    for a in u["answerKey"]:
        if a["taskRef"] not in task_ids and not a["taskRef"].lower().startswith(("role", "perf", "review")):
            out.append(finding("warning", "assessment", f"answer key refers to unknown task '{a['taskRef']}'"))
    for t in u["guidedPractice"]:
        if not any(a["taskRef"] == t["id"] for a in u["answerKey"]):
            out.append(finding("warning", "assessment", f"task {t['id']} has no answer-key entry (task answers present: {bool(t['answers'])})"))
    rub = u["feedback"].get("rubric", [])
    if rub and sum(r["weight"] for r in rub) != 100:
        out.append(finding("error", "assessment", f"rubric weights total {sum(r['weight'] for r in rub)}, not 100"))
    # genuine difference (anti noun-swap) against the paired unit, if it exists
    pair = plan.get("_differFrom")
    if pair:
        other = load(store("content", "objects", f"{pair}.json", base=base))
        if other:
            a = {w.lower() for w in words(text_of_unit(u))} - STOP
            b = {w.lower() for w in words(text_of_unit(other["content"]))} - STOP
            j = len(a & b) / max(1, len(a | b))
            out.append(finding("error" if j > 0.6 else "info", "industryRealism",
                               f"conversation word overlap with {pair}: {j:.2f} (fails above 0.60)"))
    if plan.get("variantOf"):
        other = load(store("content", "objects", f"{plan['variantOf']}.json", base=base))
        if other:
            avg = lambda unit: sum(len(words(t["text"])) for t in unit["notice"]["conversation"]["turns"] if t.get("learner")) / max(1, sum(1 for t in unit["notice"]["conversation"]["turns"] if t.get("learner")))  # noqa: E731
            if avg(u) >= avg(other["content"]):
                out.append(finding("warning", "cefrFit", f"variant learner turns not shorter than {plan['variantOf']} ({avg(u):.1f} vs {avg(other['content']):.1f} words)"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("response")
    ap.add_argument("--base")
    ap.add_argument("--revise", action="store_true")
    a = ap.parse_args(argv)
    base = a.base
    cfg = load(store("config", "pilot-u1.json", base=base))
    raw = open(a.response, encoding="utf-8").read().strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)          # tolerate Markdown fences
    resp = json.loads(raw)
    errs = validate(resp, schema("response", base))
    req = load(store("requests", f"{resp.get('requestId')}.json", base=base))
    if not req:
        errs.append(f"unknown request {resp.get('requestId')}")
    elif req["status"] == "INGESTED" and not a.revise:
        errs.append(f"{req['requestId']} already INGESTED: duplicate generation refused (use --revise for a revision)")
    elif req["status"] in ("BLOCKED", "STOPPED_BUDGET"):
        errs.append(f"{req['requestId']} is {req['status']}; it was not released for generation")
    if errs:
        print("REJECTED:\n  " + "\n  ".join(errs))
        return 2
    exp = {(o["tempId"], o["key"]) for o in req["expectedOutputs"]}
    got = {(o["tempId"], o["key"]) for o in resp["outputs"]}
    if exp != got:
        print("REJECTED: outputs do not match expectedOutputs", "\n  missing:", sorted(exp - got)[:5], "\n  unexpected:", sorted(got - exp)[:5])
        return 2
    index = load(store("content", "index.json", base=base), {})
    dup = [o["key"] for o in resp["outputs"] if o["key"] in index and not a.revise]
    if dup:
        print("REJECTED: objects already exist (duplicate generation):", dup[:5])
        return 2

    plans = {p["layers"][-1]["key"]: p for p in (load(f) for f in sorted(store("plans", base=base).glob("RIN-*.json")))}
    vocab = load(store("content", "vocabulary.json", base=base), [])
    core = core_codes()
    core_labels = {norm_term(v["label"]): c for c, v in core.items() if c.startswith("V-")}
    scopes = scope_codes(base)
    profiles = {p["id"]: p for p in (load(f) for f in store("role-profiles", base=base).glob("RPF-*.json"))}
    role_industries = Counter(p["role"] for p in profiles.values())
    fam_of = {r["id"]: r["family"] for r in load(store("registry", "roles.json", base=base))}
    existing_ids = [v for v in index.values()]
    reviews = sorted(store("reviews", base=base).glob("REV-*.json")) if store("reviews", base=base).exists() else []
    rev_ids = [r.stem for r in reviews]
    report = {"request": req["requestId"], "objects": [], "vocabulary": {"reused": [], "new": [], "rejected": []}}
    out_chars = 0
    for o in resp["outputs"]:
        layer = TYPE_LAYER.get(o["type"])
        c = content_of(o["record"])
        out_chars += len(json.dumps(c, ensure_ascii=False))
        if layer is None:
            print("REJECTED: unknown output type", o["type"])
            return 2
        if layer == "L6":
            plan = plans[o["key"]]
            oid = plan["id"]
            if plan.get("differFrom"):
                dplan = next(p for p in plans.values() if p["id"] == plan["differFrom"])
                plan["_differFrom"] = index.get(dplan["layers"][-1]["key"])
            findings = qa_unit(plan, c, cfg, base, index)
            # vocabulary (D-U07)
            rp = profiles[plan["roleProfile"]]
            scope = rp["role"] and (fam_of[rp["role"]] if role_industries[rp["role"]] > 1 else rp["industryCode"])
            codes = []
            for v in c["understand"]["vocabulary"]:
                ec = v.get("existingCode")
                if ec:
                    if ec in core or any(x["code"] == ec for x in vocab):
                        report["vocabulary"]["reused"].append(f"{v['term']} → {ec} (given)")
                        codes.append(ec)
                    else:
                        report["vocabulary"]["rejected"].append(f"{v['term']}: existingCode {ec} does not exist")
                        findings.append(finding("error", "vocabulary", f"unknown existingCode {ec}"))
                    continue
                nt = norm_term(v["term"])
                hit = core_labels.get(nt) or next((x["code"] for x in vocab if norm_term(x["term"]) == nt), None)
                if hit:
                    v["existingCode"] = hit
                    report["vocabulary"]["reused"].append(f"{v['term']} → {hit} (matched existing)")
                    codes.append(hit)
                    for x in vocab:
                        if x["code"] == hit:
                            x.setdefault("usedBy", []).append(oid)
                    continue
                n = 1 + max([int(x["code"].split("-")[-1]) for x in vocab if x["scope"] == scope] or [0])
                code = f"V-{scope}-{n:04d}"
                problems = []
                if not ENGINE_CODE.match(code):
                    problems.append("format")
                if scope not in scopes:
                    problems.append("scope not in registry")
                if code in core or CORE_CODE.search(code):
                    problems.append("collides with the live reference index / core pattern")
                if any(x["code"] == code for x in vocab):
                    problems.append("duplicate engine code")
                if problems:
                    report["vocabulary"]["rejected"].append(f"{v['term']}: {code} ({', '.join(problems)})")
                    findings.append(finding("error", "vocabulary", f"code {code} rejected: {', '.join(problems)}"))
                    continue
                entry = {"code": code, "term": v["term"], "pos": v.get("pos", ""), "definition": v["definition"], "example": v["example"],
                         "scope": scope, "cefr": plan["cefr"], "home": oid, "usedBy": [oid], "status": "GENERATED",
                         "provenance": {"source": "generated", "generator": "ChatGPT", "requestId": req["requestId"], "tempId": v.get("tempId")}}
                ve = validate(entry, schema("vocabulary-entry", base))
                if ve:
                    findings.append(finding("error", "vocabulary", "; ".join(ve)))
                    continue
                vocab.append(entry)
                v["existingCode"] = code
                codes.append(code)
                report["vocabulary"]["new"].append(f"{v['term']} → {code}")
            plan.pop("_differFrom", None)
        else:
            oid = next_id(ID_PREFIX[layer], existing_ids)
            findings = qa_layer(layer, o["key"], c, cfg)
            codes = []
        existing_ids.append(oid)
        for sc in resp.get("selfCheck", []):
            if sc["result"] == "not met":
                findings.append(finding("warning", "selfCheck", f"generator reported '{sc['check']}' not met: {sc.get('notes', '')}"))
        errors = [f for f in findings if f["severity"] == "error"]
        stored = {"id": oid, "type": o["type"], "layer": layer, "key": o["key"], "status": "AI_QA" if not errors else "GENERATED",
                  "version": 1, "provenance": {"source": "generated", "generator": "ChatGPT", "model": resp.get("model"),
                                              "requestId": req["requestId"], "ingestedAt": now(), "tempId": o["tempId"]},
                  "review": {"aiQa": "FAIL" if errors else "PASS", "editorial": "PENDING", "specialist": "NOT_REQUIRED", "native": "NOT_REQUIRED"},
                  "prototype": True, "publishable": False, "vocabularyCodes": codes,
                  "contentHash": hashlib.sha1(json.dumps(c, sort_keys=True).encode()).hexdigest()[:16], "content": c}
        if a.revise and o["key"] in index:
            prev = load(store("content", "objects", f"{index[o['key']]}.json", base=base))
            stored["id"] = prev["id"]
            stored["version"] = prev["version"] + 1
            save(store("content", "history", f"{prev['id']}.v{prev['version']}.json", base=base), prev)
        se = validate({k: v for k, v in stored.items() if k != "contentHash"}, schema("stored-object", base))
        if se:
            print("REJECTED: stored envelope invalid:", se[:3])
            return 2
        save(store("content", "objects", f"{stored['id']}.json", base=base), stored)
        index[o["key"]] = stored["id"]
        pol = cfg["reviewPolicy"]
        for stage, reviewer, result, reason, fnd in [
                ("AI_QA", "ai-pipeline (automated checks)", "FAIL" if errors else "PASS", "Automated AI QA (ingest.py)", findings),
                ("EDITORIAL_REVIEW", "author", "PENDING", "Editorial Review is performed by the author (D-U13b)", []),
                ("SPECIALIST_REVIEW", "n/a", "NOT_REQUIRED", pol["specialistReason"], []),
                ("NATIVE_REVIEW", "n/a", "NOT_REQUIRED", pol["nativeReason"], [])]:
            rid = next_id("REV", rev_ids)
            rev_ids.append(rid)
            rec = {"id": rid, "target": stored["id"], "stage": stage, "reviewer": reviewer, "result": result, "reason": reason,
                   "findings": fnd, "date": now()}
            assert not validate(rec, schema("review", base))
            save(store("reviews", f"{rid}.json", base=base), rec)
        report["objects"].append({"id": stored["id"], "key": o["key"], "status": stored["status"],
                                  "errors": len(errors), "warnings": sum(1 for f in findings if f["severity"] == "warning")})
    save(store("content", "index.json", base=base), index)
    save(store("content", "vocabulary.json", base=base), vocab)
    req["status"] = "INGESTED"
    save(store("requests", f"{req['requestId']}.json", base=base), req)
    usage = {"request": req["requestId"], "batch": req["batch"], "model": resp.get("model"), "date": now(),
             "estimatedInputTokens": req["estimate"]["inputTokens"], "estimatedOutputTokens": estimate_tokens(" " * out_chars),
             "note": "estimates (≈4 characters per token); replace with ChatGPT's reported usage if available"}
    with open(store("logs", "usage.jsonl", base=base), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(usage) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
