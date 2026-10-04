"""End-to-end pipeline test with SYNTHETIC placeholder responses, in a temporary copy of the store.

Usage: python editorial/tools/curriculum/tests/run_pipeline_test.py

The real store (editorial/curriculum/) is never written to. Every synthetic string is marked "[FIXTURE]".
This tests the tooling (plan → ingest → dedupe → vocabulary codes → AI QA → compose → validate); it does not
generate curriculum content, which is ChatGPT's job (D-U10).
"""
import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import compose  # noqa: E402
import ingest  # noqa: E402
import plan  # noqa: E402
import validate as validator  # noqa: E402
from cur import STORE, load  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
FX = "[FIXTURE]"
LIMITS = {"A1": 6, "A2": 8, "B1": 10, "B2": 12}


def layer_content(o):
    k, t = o["key"], o["type"]
    if t == "function-exponents":
        return {"function": k.split("|")[1], "cefr": k.split("|")[2], "exponents": [f"{FX} exponent one", f"{FX} exponent two"], "notes": f"{FX} note"}
    if t == "situation":
        return {"situation": k.split("|")[1], "description": f"{FX} neutral description", "flow": [f"{FX} step {i}" for i in range(3)],
                "functions": [], "variationPoints": [f"{FX} varies"]}
    if t == "core-module":
        return {"coreModule": k.split("|")[1], "summary": f"{FX} summary", "communicationMoves": [{"move": f"{FX} move {i}", "functions": []} for i in range(4)],
                "qualityCriteria": [f"{FX} criterion"]}
    if t == "role-core":
        return {"role": k.split("|")[1], "parent": None, "responsibilities": [f"{FX} r{i}" for i in range(4)], "stakeholders": ["Customer"],
                "keyFunctions": [], "jobKnowledge": [{"title": f"{FX} jk{i}", "text": f"{FX} text"} for i in range(3)], "deltaFromParent": []}
    if t == "context-overlay":
        return {"profile": k.split("|")[1], "situationsAdded": [], "situationsChanged": [], "stakeholders": [], "constraints": [],
                "jobKnowledge": [{"title": f"{FX} jk", "text": f"{FX} t"}] * 2, "register": f"{FX}",
                "differenceStatement": f"{FX} this context differs from the same role elsewhere in several concrete ways"}
    if t == "seniority-overlay":
        return {"responsibilityLevel": k.split("|")[1], "scale": None, "purpose": FX, "audience": [], "accountabilityLanguage": [], "decisionRights": FX}
    raise ValueError(t)


def unit_content(brief, text_seed, vocab):
    cefr = brief["cefr"]
    fns = [f["id"] for f in brief["functions"]]
    n = LIMITS[cefr]
    turns = []
    for i, f in enumerate(fns):
        turns.append({"n": len(turns) + 1, "speaker": "Customer", "learner": False, "text": f"{FX} {text_seed} question {i}"})
        turns.append({"n": len(turns) + 1, "speaker": "You", "learner": True, "text": f"{FX} {text_seed} answer {i}", "functions": [f]})
    while len(turns) < n:
        turns.append({"n": len(turns) + 1, "speaker": "Customer", "learner": False, "text": f"{FX} {text_seed} filler {len(turns)}"})
    return {"title": f"{FX} {brief['title']}", "cefr": cefr,
            "context": {"setting": f"{FX} setting", "learnerRole": f"{FX} role", "objective": f"{FX} objective", "constraints": brief["constraints"],
                        "stakeholders": [{"archetype": s, "name": f"{FX} name", "relationship": "external"} for s in brief["stakeholders"]]},
            "notice": {"conversation": {"turns": turns}},
            "understand": {"keyExpressions": [{"text": f"{FX} expression", "function": f} for f in fns], "vocabulary": vocab, "notes": []},
            "jobKnowledge": [],
            "guidedPractice": [{"id": f"T{i}", "type": "recognition", "prompt": f"{FX} prompt", "items": [{"q": f"{FX} q"}], "answers": [f"{FX} a"]} for i in (1, 2)],
            "rolePractice": {"instructions": f"{FX}", "cards": [{"role": "A", "goal": FX}, {"role": "B", "goal": FX}]},
            "performanceTask": {"prompt": FX, "modes": ["speak"], "successCriteria": [FX]},
            "feedback": {"selfCheck": [FX], "rubric": [{"criterion": FX, "weight": 60}, {"criterion": FX, "weight": 40}]},
            "reviewRetrieval": [{"prompt": FX, "answer": FX}], "answerKey": [{"taskRef": "T1", "answer": FX}, {"taskRef": "T2", "answer": FX}]}


def respond(base, rid, unit_overrides=None):
    req = load(Path(base) / "requests" / f"{rid}.json")
    outs = []
    for o in req["expectedOutputs"]:
        if o["type"] == "unit":
            ov = (unit_overrides or {}).get(o["brief"]["roleInstance"], {})
            vocab = ov.get("vocab", [{"term": f"fixture term {o['brief']['roleInstance']} {i}", "definition": FX, "example": FX, "tempId": f"tmp:v{i}"} for i in range(6)])
            rec = {"content": unit_content(o["brief"], ov.get("seed", o["brief"]["roleInstance"]), vocab)}
        else:
            rec = {"content": layer_content(o)}
        outs.append({"tempId": o["tempId"], "type": o["type"], "key": o["key"], "record": rec})
    resp = {"requestId": rid, "contractVersion": "1.0", "model": "FIXTURE (no model)", "outputs": outs,
            "selfCheck": [{"check": "fixture", "result": "met"}], "assumptions": [], "flags": [], "questions": []}
    p = Path(base) / f"resp-{rid}.json"
    p.write_text(json.dumps(resp), encoding="utf-8")
    return str(p)


def main():
    tmp = Path(tempfile.mkdtemp(prefix="cur-test-"))
    results = {}
    try:
        for d in ("config", "registry", "schemas"):
            shutil.copytree(STORE / d, tmp / d)
        s = plan.build(str(tmp))
        assert not s["errors"], s["errors"]
        ready = [r for r, st in s["requests"].items() if st == "PREPARED"]
        results["initiallyPrepared"] = ready
        for rid in ready:
            assert ingest.main([respond(tmp, rid), "--base", str(tmp)]) == 0, rid
        results["duplicateRefused"] = ingest.main([respond(tmp, ready[0]), "--base", str(tmp)]) == 2
        for _ in range(4):            # unblock B5, then B6 groups, then the variant and the P5 pair
            s = plan.build(str(tmp))
            ready = [r for r, st in s["requests"].items() if st == "PREPARED"]
            for rid in ready:
                over = {}
                req = load(tmp / "requests" / f"{rid}.json")
                for o in req["expectedOutputs"]:
                    ri = o["brief"].get("roleInstance") if o["type"] == "unit" else None
                    if ri in ("RIN-000011", "RIN-000013"):        # identical conversation → must fail the anti-noun-swap check
                        over[ri] = {"seed": "SAME-HR-TEXT"}
                    if ri == "RIN-000011":
                        over[ri]["vocab"] = [{"term": "professional", "definition": FX, "example": FX, "tempId": "tmp:a"},       # core V-0001 → reuse
                                             {"term": "fixture headcount plan", "definition": FX, "example": FX, "tempId": "tmp:b"},  # new → V-HR-…
                                             {"term": "fixture bad code", "definition": FX, "example": FX, "existingCode": "V-9999"}]   # must be rejected
                assert ingest.main([respond(tmp, rid, over), "--base", str(tmp)]) == 0, rid
        idx = load(tmp / "content" / "index.json")
        vocab = load(tmp / "content" / "vocabulary.json")
        objs = {k: load(tmp / "content" / "objects" / f"{v}.json") for k, v in idx.items()}
        units = {o["id"]: o for o in objs.values() if o["layer"] == "L6"}
        results["unitsIngested"] = len(units)
        results["layerObjects"] = {l: sum(1 for o in objs.values() if o["layer"] == l) for l in ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]}
        results["coreVocabularyReused"] = "V-0001" in units["RIN-000011"]["vocabularyCodes"]
        results["newHrCode"] = [v["code"] for v in vocab if v["term"] == "fixture headcount plan"]
        results["vegmScopeCodes"] = sorted({v["code"].rsplit("-", 1)[0] for v in vocab if v["home"] in ("RIN-000001",)})
        results["badExistingCodeRejected"] = units["RIN-000011"]["review"]["aiQa"] == "FAIL"
        revs = [load(f) for f in (tmp / "reviews").glob("REV-*.json")]
        p5 = [r for r in revs if r["target"] == "RIN-000013" and r["stage"] == "AI_QA"][0]
        results["nounSwapDetected"] = any(f["check"] == "industryRealism" and f["severity"] == "error" for f in p5["findings"])
        results["reviewStagesPerUnit"] = sorted({r["stage"] + "=" + r["result"] for r in revs if r["target"] == "RIN-000001"})
        results["compose"] = sum(r["composed"] for r in compose.run(str(tmp)))
        errs, notes = validator.run(str(tmp))
        results["validateErrors"] = errs
        results["vocabularyCollisions"] = notes["vocabulary"]["collisions"]
        results["duplicates"] = notes["duplicates"]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps(results, indent=1))
    ok = (results["duplicateRefused"] and results["unitsIngested"] == 14 and results["coreVocabularyReused"] and results["newHrCode"] == ["V-HR-0001"]
          and results["nounSwapDetected"] and results["badExistingCodeRejected"] and results["compose"] == 14 and not results["validateErrors"])
    print("PIPELINE TEST:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
