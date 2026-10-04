"""Plan pilot U-1: role profiles, unit plans (retrieval before generation) and ChatGPT request packets.

Usage: python editorial/tools/curriculum/plan.py [--base DIR]

- Writes role-profiles/RPF-*.json and plans/RIN-*.json (Role Instances: profile + CEFR + situation + stakeholders + functions).
- For every layer an instance needs (L0 function exponents … L6 unit), looks the object up in content/index.json.
  PRESENT objects are reused; only MISSING ones are requested (D-U10: generate the smallest missing delta).
- Builds request packets in requests/ for batches whose dependencies are present; later batches are reserved as BLOCKED.
  Request IDs are stable (requests/index.json). A request that is already SENT/RECEIVED/INGESTED is never rebuilt
  (duplicate-generation prevention).
- Checks each batch against its configured per-batch limits (config/pilot-u1.json); over-limit requests are STOPPED_BUDGET.
- Writes logs/estimates.json (estimated tokens; cost only if prices are configured).
Nothing is generated here: generation is ChatGPT's job.
"""
import argparse
import json
import sys
from collections import defaultdict

from cur import CODE_TYPES, core_codes, estimate_tokens, load, save, schema, store, validate

sys.stdout.reconfigure(encoding="utf-8")
CONTRACT = "1.0"


def registry(base):
    r = lambda n: load(store("registry", f"{n}.json", base=base))  # noqa: E731
    return {n: r(n) for n in ["sectors", "industries", "departments", "role-families", "roles", "situation-templates",
                              "communication-functions", "responsibility-levels", "employment-settings", "core-modules",
                              "seniority-core-modules", "stakeholder-archetypes", "scope-codes"]}


def by(items, k="id"):
    return {x[k]: x for x in items}


LAYER_FIELDS = {
    "L0": {"function": "CFN id", "cefr": "CEFR level", "exponents": "2–4 short model utterances at this CEFR level (strings)",
           "notes": "one sentence on use (string)"},
    "L1": {"situation": "STM id", "description": "≤80 words, industry-neutral", "flow": "3–6 steps (strings)",
           "functions": "CFN ids used", "variationPoints": "what changes by role/industry/CEFR (strings)"},
    "L2": {"coreModule": "CM id", "summary": "≤120 words", "communicationMoves": "4–10 objects {move, functions[CFN]}",
           "qualityCriteria": "what good performance looks like (strings)"},
    "L3": {"role": "ROL id", "parent": "ROL id or null", "responsibilities": "4–8 strings", "stakeholders": "archetype names",
           "keyFunctions": "CFN ids", "jobKnowledge": "3–6 objects {title, text ≤60 words}",
           "deltaFromParent": "what this role adds to its parent (strings; empty if no parent)"},
    "L4": {"profile": "RPF id", "situationsAdded": "strings", "situationsChanged": "strings", "stakeholders": "strings",
           "constraints": "strings", "jobKnowledge": "2–5 objects {title, text}", "register": "string",
           "differenceStatement": "how this context genuinely differs from the same role elsewhere (string)"},
    "L5": {"responsibilityLevel": "SEN id", "scale": "solo/small-team/company or null", "purpose": "string", "audience": "strings",
           "accountabilityLanguage": "example phrases (strings)", "decisionRights": "string"},
}


def build(base=None):
    cfg = load(store("config", "pilot-u1.json", base=base))
    R = registry(base)
    roles, inds, sits, funcs = by(R["roles"]), by(R["industries"], "code"), by(R["situation-templates"]), by(R["communication-functions"])
    fams, cms, levels = by(R["role-families"], "code"), by(R["core-modules"]), by(R["responsibility-levels"])
    sec_by_id = by(R["sectors"])
    index = load(store("content", "index.json", base=base), {})          # key -> object id (retrieval)
    errors = []

    # ---------------- role profiles
    profiles, pkey = [], {}
    for i, p in enumerate(cfg["profiles"], 1):
        role, ind = roles[p["role"]], inds[p["industry"]]
        fam = fams[role["family"]]
        lv = levels[p["level"]]
        cm = list(fam["coreModules"])
        add = R["seniority-core-modules"].get(lv["short"] if lv["short"] != "OWN" else f"OWN:{p['ownershipScale']}", [])
        cm += [x for x in add if x not in cm]
        chain, cur = [], role["parent"]
        while cur:
            chain.append(cur)
            cur = roles[cur]["parent"]
        rp = {"id": f"RPF-{i:06d}", "type": "role-profile",
              "name": f"{role['name']} — {ind['name']}", "role": role["id"], "parentRoles": chain,
              "industry": ind["id"], "industryCode": ind["code"], "sector": ind["sector"], "sectorCode": sec_by_id[ind["sector"]]["code"],
              "department": p["department"], "specialisation": p["specialisation"], "responsibilityLevel": p["level"],
              "ownershipScale": p["ownershipScale"], "employmentSetting": p["employmentSetting"], "coreModules": cm,
              "reviewTriggers": role["reviewTriggers"], "pilot": cfg["pilot"], "status": "PROFILED", "prototype": True, "publishable": False,
              "notes": [f"Registry mapping: {role['name']} is " + ("common" if sec_by_id[ind["sector"]]["code"] in role["commonSectors"]
                        else "specialisation" if sec_by_id[ind["sector"]]["code"] in role["specialisationSectors"] else "NOT MAPPED")
                        + f" in sector {sec_by_id[ind['sector']]['code']}"]}
        if "NOT MAPPED" in rp["notes"][0]:
            errors.append(f"{rp['id']}: role {role['id']} not mapped to sector {rp['sectorCode']} in the registry")
        errors += [f"{rp['id']}: {e}" for e in validate(rp, schema("role-profile", base))]
        profiles.append(rp)
        pkey[p["key"]] = rp
        save(store("role-profiles", f"{rp['id']}.json", base=base), rp)

    # ---------------- unit plans (Role Instances)
    plans, ukey = [], {}
    for i, u in enumerate(cfg["units"], 1):
        rp, st = pkey[u["profile"]], sits[u["situation"]]
        excl = {e["function"]: e["reason"] for e in u.get("excludeFunctions", [])}
        fn = [f for f in st["functions"] if f not in excl]
        cat_cms = [c for c in rp["coreModules"] if st["category"] in cms[c]["situationCategories"]]
        layers = [{"layer": "L0", "key": f"L0|{f}|{u['cefr']}"} for f in fn]
        layers.append({"layer": "L1", "key": f"L1|{st['id']}"})
        layers += [{"layer": "L2", "key": f"L2|{c}"} for c in cat_cms]
        layers += [{"layer": "L3", "key": f"L3|{r}"} for r in reversed(rp["parentRoles"])] + [{"layer": "L3", "key": f"L3|{rp['role']}"}]
        layers.append({"layer": "L4", "key": f"L4|{rp['id']}"})
        layers.append({"layer": "L5", "key": f"L5|{rp['responsibilityLevel']}|{rp['ownershipScale'] or '-'}"})
        layers.append({"layer": "L6", "key": f"L6|{rp['id']}|{st['id']}|{u['cefr']}"})
        for L in layers:
            L["objectId"] = index.get(L["key"])
            L["status"] = "PRESENT" if L["objectId"] else "MISSING"
            L["request"] = None
        pol = cfg["reviewPolicy"]
        plan = {"id": f"RIN-{i:06d}", "type": "unit-plan", "pilot": cfg["pilot"], "roleProfile": rp["id"], "situationTemplate": st["id"],
                "title": f"{st['name']} — {roles[rp['role']]['name']} ({u['cefr']})", "cefr": u["cefr"],
                "variantOf": None, "functions": fn,
                "excludedFunctions": [{"function": k, "reason": v} for k, v in excl.items()],
                "stakeholders": u["stakeholders"], "constraints": u.get("constraints", []), "layers": layers,
                "reviewPolicy": {"aiQa": pol["aiQa"], "editorial": pol["editorial"], "specialist": pol["specialist"], "native": pol["native"],
                                 "specialistReason": pol["specialistReason"], "nativeReason": pol["nativeReason"]},
                "maxStatus": "APPROVED", "prototype": True, "publishable": False,
                "searchTerms": [roles[rp["role"]]["name"], *roles[rp["role"]]["aliases"], st["name"], inds[rp["industryCode"]]["name"]]}
        ukey[f"{u['profile']}:{u['situation']}:{u['cefr']}"] = plan
        plans.append((u, plan))
    for u, plan in plans:
        if u.get("variantOf"):
            plan["variantOf"] = ukey[u["variantOf"]]["id"]
        plan["differFrom"] = ukey[u["differFrom"]]["id"] if u.get("differFrom") else None
    users = defaultdict(set)
    for _, plan in plans:
        for L in plan["layers"]:
            users[L["key"]].add(plan["id"])
    for _, plan in plans:
        for L in plan["layers"]:
            L["sharedWith"] = sorted(users[L["key"]] - {plan["id"]})

    # ---------------- requests (stable IDs; per-batch limits)
    ridx = load(store("requests", "index.json", base=base), {})
    groups = {"B1": [], "B2": [], "B3": [], "B4": [], "B5": []}
    for _, plan in plans:
        for L in plan["layers"]:
            b = {"L0": "B1", "L1": "B2", "L2": "B3", "L3": "B4", "L4": "B5", "L5": "B5"}.get(L["layer"])
            if b and L["status"] == "MISSING" and L["key"] not in groups[b]:
                groups[b].append(L["key"])
    unit_groups = defaultdict(list)
    for u, plan in plans:
        g = u["profile"] + ("v" if u.get("variantOf") else "")
        unit_groups[f"B6:{g}"].append((u, plan))
    batch_keys = [k for k in ["B1", "B2", "B3", "B4", "B5"]] + sorted(unit_groups)
    for bk in batch_keys:
        if bk not in ridx:
            ridx[bk] = f"REQ-{len(ridx) + 1:06d}"
    save(store("requests", "index.json", base=base), ridx)
    rid_of_key = {}
    for b, keys in groups.items():
        for k in keys:
            rid_of_key[k] = ridx[b]
    for bk, items in unit_groups.items():
        for u, plan in items:
            rid_of_key[plan["layers"][-1]["key"]] = ridx[bk]
    for _, plan in plans:
        for L in plan["layers"]:
            if L["status"] == "MISSING":
                L["request"] = rid_of_key.get(L["key"])
        errors += [f"{plan['id']}: {e}" for e in validate(plan, schema("unit-plan", base))]
        save(store("plans", f"{plan['id']}.json", base=base), plan)

    content = lambda k: load(store("content", "objects", f"{index[k]}.json", base=base), {}).get("content") if k in index else None  # noqa: E731
    common_ctx = {"pilot": {"id": cfg["pilot"], "purpose": cfg["purpose"]}, "policies": cfg["policies"], "style": cfg["style"],
                  "review": "Output is stored as GENERATED, then AI QA, then Editorial Review by the author. Specialist and native review are NOT_REQUIRED for U-1. It is never published."}
    instructions = [
        "Return ONE JSON object only (no prose, no Markdown fences), conforming to the response format in 'responseFormat'.",
        "Produce exactly the outputs listed in 'expectedOutputs', using their tempId, type and key unchanged.",
        "Generate only these outputs. Do not regenerate objects given in 'context' — use them.",
        "Do not invent IDs or vocabulary codes. Reference existing codes only as given in context; propose new vocabulary with tempIds.",
        "English only: no Bengali/Hindi script or transliteration. No audio references. No real brand or company names.",
        "No legal, medical, financial or safety advice; no invented procedures or rules (D-U11).",
        "Report honestly in selfCheck: 'met', 'not met' or 'uncertain'. Never claim approval, certification or CEFR validation.",
    ]
    response_format = {"requestId": "<copy>", "contractVersion": CONTRACT, "model": "<model name if known>",
                       "outputs": [{"tempId": "<copy>", "type": "<copy>", "key": "<copy>", "record": {"content": "<object per outputSpec>"}}],
                       "selfCheck": [{"check": "<name>", "result": "met | not met | uncertain", "notes": "<text>"}],
                       "assumptions": [], "flags": [], "questions": []}
    estimates, statuses = [], {}

    def emit(bk, layer, expected, ctx, out_spec, depends, max_out):
        rid = ridx[bk]
        existing = load(store("requests", f"{rid}.json", base=base))
        if existing and existing["status"] in ("SENT", "RECEIVED", "INGESTED"):
            statuses[rid] = existing["status"] + " (kept; not rebuilt)"
            return
        missing_deps = [d for d in depends if d not in index]
        req = {"requestId": rid, "contractVersion": CONTRACT, "batch": bk, "mode": "generate", "layer": layer,
               "status": "BLOCKED" if missing_deps else "PREPARED", "dependsOn": missing_deps if missing_deps else depends,
               "expectedOutputs": expected, "context": {**common_ctx, **(ctx if not missing_deps else {})},
               "style": cfg["style"], "limits": cfg["sizeLimits"].get(layer.split("+")[0], cfg["sizeLimits"]),
               "outputSchema": out_spec, "instructions": instructions, "responseFormat": response_format,
               "estimate": {"inputTokens": 0, "maxOutputTokens": max_out}}
        if missing_deps:
            req["context"]["blockedNote"] = f"Built when {len(missing_deps)} dependency objects are PRESENT (re-run plan.py after ingesting earlier batches)."
        req["estimate"]["inputTokens"] = estimate_tokens(json.dumps(req, ensure_ascii=False))
        b = cfg["batches"][bk.split(":")[0]]
        if req["status"] == "PREPARED" and (req["estimate"]["inputTokens"] > b["maxInputTokens"] or max_out > b["maxOutputTokens"]):
            req["status"] = "STOPPED_BUDGET"
        errs = validate(req, schema("request", base))
        errors.extend(f"{rid}: {e}" for e in errs)
        save(store("requests", f"{rid}.json", base=base), req)
        statuses[rid] = req["status"]
        estimates.append({"request": rid, "batch": bk, "layer": layer, "status": req["status"], "outputs": len(expected),
                          "estimatedInputTokens": req["estimate"]["inputTokens"], "maxOutputTokens": max_out})

    fdef = lambda f: {"id": f, "name": funcs[f]["name"], "group": funcs[f]["groupName"], "coreBookLocation": funcs[f]["coreLocation"] or None}  # noqa: E731
    # B1 L0
    if groups["B1"]:
        exp = [{"tempId": f"tmp:{k}", "type": "function-exponents", "key": k, "brief": {"function": fdef(k.split("|")[1]), "cefr": k.split("|")[2]}} for k in groups["B1"]]
        emit("B1", "L0", exp, {"note": "Industry-neutral exponents: realistic in any workplace."}, LAYER_FIELDS["L0"], [], 250 * len(exp))
    # B2 L1
    if groups["B2"]:
        exp = []
        for k in groups["B2"]:
            st = sits[k.split("|")[1]]
            exp.append({"tempId": f"tmp:{k}", "type": "situation", "key": k, "brief": {"situation": st["id"], "name": st["name"], "category": st["categoryName"],
                        "functions": [fdef(f) for f in st["functions"]], "typicalStakeholders": st["stakeholders"], "modes": st["modes"]}})
        emit("B2", "L1", exp, {"note": "Situation templates are industry-neutral; industry detail belongs to L4."}, LAYER_FIELDS["L1"], [], 400 * len(exp))
    # B3 L2
    if groups["B3"]:
        exp = []
        for k in groups["B3"]:
            c = cms[k.split("|")[1]]
            exp.append({"tempId": f"tmp:{k}", "type": "core-module", "key": k, "brief": {"coreModule": c["id"], "name": c["name"],
                        "situationCategories": c["situationCategories"], "usedByFamilies": [f["code"] for f in R["role-families"] if c["id"] in f["coreModules"]]}})
        emit("B3", "L2", exp, {"note": "Core modules are shared by every role family that uses them; keep them role- and industry-neutral."}, LAYER_FIELDS["L2"], [], 600 * len(exp))
    # B4 L3
    if groups["B4"]:
        exp = []
        for k in groups["B4"]:
            r = roles[k.split("|")[1]]
            exp.append({"tempId": f"tmp:{k}", "type": "role-core", "key": k, "brief": {"role": r["id"], "name": r["name"], "parent": r["parent"],
                        "family": fams[r["family"]]["name"], "familyRoleCore": fams[r["family"]]["roleCore"], "aliases": r["aliases"],
                        "defaultLevel": r["defaultLevel"], "employmentSettings": r["employmentSettings"]}})
        emit("B4", "L3", exp, {"note": "Role cores are industry-neutral. A child role states only what it adds to its parent (deltaFromParent)."},
             LAYER_FIELDS["L3"], [], 900 * len(exp))
    # B5 L4 + L5
    if groups["B5"]:
        exp, deps = [], []
        for k in groups["B5"]:
            if k.startswith("L4|"):
                rp = next(p for p in profiles if p["id"] == k.split("|")[1])
                deps += [f"L3|{r}" for r in rp["parentRoles"]] + [f"L3|{rp['role']}"]
                exp.append({"tempId": f"tmp:{k}", "type": "context-overlay", "key": k, "brief": {"profile": rp,
                            "roleCore": content(f"L3|{rp['role']}")}})
            else:
                _, sen, scale = k.split("|")
                exp.append({"tempId": f"tmp:{k}", "type": "seniority-overlay", "key": k, "brief": {"responsibilityLevel": levels[sen],
                            "scale": None if scale == "-" else scale}})
        emit("B5", "L4+L5", exp, {"note": "Overlays store only what changes. A context overlay that only replaces nouns fails review; state the genuine difference."},
             {"L4": LAYER_FIELDS["L4"], "L5": LAYER_FIELDS["L5"]}, sorted(set(deps)), 900 * len(exp))
    # B6 L6 units
    core_v = [f"{c} {v['label']}" for c, v in core_codes().items() if c.startswith("V-")]
    for bk in sorted(unit_groups):
        items = unit_groups[bk]
        exp, deps = [], set()
        for u, plan in items:
            if plan["layers"][-1]["status"] == "PRESENT":
                continue
            for L in plan["layers"][:-1]:
                deps.add(L["key"])
            if plan["variantOf"]:
                deps.add(next(p for _, p in plans if p["id"] == plan["variantOf"])["layers"][-1]["key"])
            if u.get("differFrom"):
                deps.add(ukey[u["differFrom"]]["layers"][-1]["key"])
            exp.append({"tempId": f"tmp:{plan['id']}", "type": "unit", "key": plan["layers"][-1]["key"], "brief": {
                "roleInstance": plan["id"], "title": plan["title"], "cefr": plan["cefr"], "functions": [fdef(f) for f in plan["functions"]],
                "excludedFunctions": plan["excludedFunctions"], "stakeholders": plan["stakeholders"], "constraints": plan["constraints"],
                "variantOf": plan["variantOf"], "differFrom": ukey[u["differFrom"]]["id"] if u.get("differFrom") else None,
                "layers": {L["key"]: content(L["key"]) for L in plan["layers"][:-1]}}})
        if not exp:
            continue
        ctx = {"note": "Compose the unit from the supplied layers. Generate only the unit (L6). Follow the D-U14 cycle.",
               "existingCoreVocabulary": core_v, "existingEngineVocabulary": load(store("content", "vocabulary.json", base=base), [])}
        emit(bk, "L6", exp, ctx, schema("unit", base), sorted(deps), 3500 * len(exp))

    save(store("requests", "index.json", base=base), ridx)
    pricing = cfg["pricing"]
    tot_in = sum(e["estimatedInputTokens"] for e in estimates)
    tot_out = sum(e["maxOutputTokens"] for e in estimates)
    cost = None
    if pricing.get("inputPer1kTokens") is not None and pricing.get("outputPer1kTokens") is not None:
        cost = round(tot_in / 1000 * pricing["inputPer1kTokens"] + tot_out / 1000 * pricing["outputPer1kTokens"], 2)
    save(store("logs", "estimates.json", base=base), {"requests": estimates, "totalEstimatedInputTokens": tot_in,
                                                       "totalMaxOutputTokens": tot_out, "estimatedCost": cost, "pricing": pricing})
    uniq = {L["key"] for _, p in plans for L in p["layers"]}
    refs = sum(len(p["layers"]) for _, p in plans)
    summary = {"profiles": len(profiles), "unitPlans": len(plans), "layerReferences": refs, "uniqueObjects": len(uniq),
               "objectsByLayer": {l: len({k for k in uniq if k.startswith(l + "|")}) for l in ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]},
               "sharedObjects": sum(1 for k in uniq if len(users[k]) > 1), "requests": statuses, "errors": errors,
               "estimatedInputTokens": tot_in, "maxOutputTokens": tot_out, "estimatedCost": cost}
    save(store("logs", "plan-summary.json", base=base), summary)
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    a = ap.parse_args()
    s = build(a.base)
    print(json.dumps({k: v for k, v in s.items() if k != "errors"}, indent=1))
    print("errors:", len(s["errors"]))
    for e in s["errors"][:20]:
        print(" ", e)
    sys.exit(1 if s["errors"] else 0)
