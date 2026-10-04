"""Validate the curriculum store: schemas, references, registry counts, mapping, vocabulary collisions,
duplicates and the pilot boundary.

Usage: python editorial/tools/curriculum/validate.py [--base DIR]   (exit code 1 on any error)
"""
import argparse
import json
import sys
from collections import Counter, defaultdict

from cur import CODE_TYPES, CORE_CODE, ENGINE_CODE, ROOT, core_codes, load, schema, scope_codes, store, validate

sys.stdout.reconfigure(encoding="utf-8")


def run(base=None):
    errors, notes = [], {}
    R = lambda n: load(store("registry", f"{n}.json", base=base))  # noqa: E731
    sectors, industries, fams, roles = R("sectors"), R("industries"), R("role-families"), R("roles")
    scope = R("scope-codes")
    # 1. approved counts (D: 27 / 122 / 211; registry 402 roles)
    counts = {"sectors": len(sectors), "industries": len(industries), "roleFamilies": len(fams), "scopeCodes": len(scope), "roles": len(roles)}
    notes["registryCounts"] = counts
    for k, v in {"sectors": 27, "industries": 122, "roleFamilies": 62, "scopeCodes": 211, "roles": 402}.items():
        if counts[k] != v:
            errors.append(f"registry: {k} = {counts[k]}, approved {v}")
    gen = [s for s in sectors if s["code"] == "GEN"]
    if not gen or any(i["sector"] == gen[0]["id"] for i in industries):
        errors.append("registry: GEN must exist and have no industries")
    codes = [s["code"] for s in scope]
    if len(set(codes)) != len(codes):
        errors.append("registry: duplicate scope codes")
    if set(codes) & CODE_TYPES or any(CORE_CODE.search(f"{t}-{c}-0001") for t in CODE_TYPES for c in codes):
        errors.append("registry: scope code collides with core code types/pattern")
    sec_codes = {s["code"] for s in sectors}
    for r in roles:
        if not set(r["commonSectors"] + r["specialisationSectors"]) <= sec_codes:
            errors.append(f"registry: {r['id']} uses an unknown sector")
    # 2. schemas
    checked = Counter()
    for folder, sch, pat in [("role-profiles", "role-profile", "RPF-*.json"), ("plans", "unit-plan", "RIN-*.json"),
                             ("requests", "request", "REQ-*.json"), ("reviews", "review", "REV-*.json")]:
        for f in sorted(store(folder, base=base).glob(pat)) if store(folder, base=base).exists() else []:
            for e in validate(load(f), schema(sch, base)):
                errors.append(f"{f.name}: {e}")
            checked[folder] += 1
    objs = {}
    if store("content", "objects", base=base).exists():
        for f in sorted(store("content", "objects", base=base).glob("*.json")):
            o = load(f)
            objs[o["id"]] = o
            for e in validate({k: v for k, v in o.items() if k != "contentHash"}, schema("stored-object", base)):
                errors.append(f"{f.name}: {e}")
            if o["layer"] == "L6":
                for e in validate(o["content"], schema("unit", base)):
                    errors.append(f"{f.name} content: {e}")
            checked["objects"] += 1
    notes["schemaChecked"] = dict(checked)
    # 3. references and role/industry mapping
    rid = {r["id"]: r for r in roles}
    ind = {i["id"]: i for i in industries}
    sec = {s["id"]: s for s in sectors}
    deps = {d["id"] for d in R("departments")}
    sens = {s["id"] for s in R("responsibility-levels")}
    emps = {e["id"] for e in R("employment-settings")}
    stms = {s["id"] for s in R("situation-templates")}
    cfns = {c["id"] for c in R("communication-functions")}
    cms = {c["id"] for c in R("core-modules")}
    mapping = []
    profiles = {}
    for f in sorted(store("role-profiles", base=base).glob("RPF-*.json")):
        p = load(f)
        profiles[p["id"]] = p
        for fld, ok in [("role", p["role"] in rid), ("industry", p["industry"] in ind), ("department", p["department"] in deps),
                        ("responsibilityLevel", p["responsibilityLevel"] in sens), ("employmentSetting", p["employmentSetting"] in emps),
                        ("coreModules", set(p["coreModules"]) <= cms)]:
            if not ok:
                errors.append(f"{p['id']}: unknown {fld}")
        r, s = rid[p["role"]], sec[ind[p["industry"]]["sector"]]
        how = "common" if s["code"] in r["commonSectors"] else "specialisation" if s["code"] in r["specialisationSectors"] else None
        mapping.append(f"{p['id']} {r['name']} → {ind[p['industry']]['name']} ({s['code']}): {how or 'NOT MAPPED'}")
        if not how:
            errors.append(f"{p['id']}: {r['name']} not mapped to sector {s['code']} in ROLE-UNIVERSE")
    notes["roleIndustryMapping"] = mapping
    plans = {}
    for f in sorted(store("plans", base=base).glob("RIN-*.json")):
        pl = load(f)
        plans[pl["id"]] = pl
        if pl["roleProfile"] not in profiles:
            errors.append(f"{pl['id']}: unknown profile")
        if pl["situationTemplate"] not in stms:
            errors.append(f"{pl['id']}: unknown situation")
        for fn in pl["functions"]:
            if fn not in cfns:
                errors.append(f"{pl['id']}: unknown function {fn}")
        # pilot boundary
        if pl.get("publishable") or pl.get("maxStatus") != "APPROVED":
            errors.append(f"{pl['id']}: pilot boundary (publishable must be false, maxStatus APPROVED)")
    # 4. duplicates
    index = load(store("content", "index.json", base=base), {})
    dupe_ids = [k for k, n in Counter(index.values()).items() if n > 1]
    hashes = defaultdict(list)
    for o in objs.values():
        hashes[o.get("contentHash")].append(o["id"])
    dupe_content = {h: ids for h, ids in hashes.items() if h and len(ids) > 1}
    if dupe_ids:
        errors.append(f"duplicates: objects indexed under several keys: {dupe_ids}")
    if dupe_content:
        errors.append(f"duplicates: identical content stored more than once: {list(dupe_content.values())}")
    notes["duplicates"] = {"indexKeys": len(index), "duplicateIndexEntries": len(dupe_ids), "duplicateContent": len(dupe_content)}
    # 5. vocabulary collisions (D-U07) against the live reference index
    core = core_codes()
    vocab = load(store("content", "vocabulary.json", base=base), [])
    vc = Counter(v["code"] for v in vocab)
    scopes = scope_codes(base)
    vproblems = []
    for v in vocab:
        c = v["code"]
        if not ENGINE_CODE.match(c) or c.split("-")[1] not in scopes:
            vproblems.append(f"{c}: format/scope")
        if c in core or CORE_CODE.search(c):
            vproblems.append(f"{c}: collides with the live reference index")
        if vc[c] > 1:
            vproblems.append(f"{c}: duplicate code")
    terms = Counter((v["scope"], v["term"].lower()) for v in vocab)
    vproblems += [f"duplicate term in scope: {k}" for k, n in terms.items() if n > 1]
    errors += [f"vocabulary: {p}" for p in vproblems]
    notes["vocabulary"] = {"engineCodes": len(vocab), "coreCodesInLiveIndex": len(core), "collisions": len(vproblems)}
    # 6. pilot boundary: statuses, no compiled output at the site root
    for o in objs.values():
        if o["status"] in ("COMPILED", "PUBLISHED") or o.get("publishable"):
            errors.append(f"{o['id']}: pilot content may not be COMPILED/PUBLISHED or publishable")
        if o["review"]["aiQa"] == "NOT_PERFORMED" and o["status"] not in ("GENERATED",):
            errors.append(f"{o['id']}: AI QA NOT_PERFORMED cannot advance")
    if base is None and (ROOT / "curriculum-data").exists():
        errors.append("curriculum-data/ exists at the site root: nothing may be compiled for U-1")
    if base is None and (ROOT / "curriculum").exists():
        errors.append("top-level /curriculum exists: D-R07 requires editorial/curriculum/")
    notes["contentObjects"] = {l: sum(1 for o in objs.values() if o["layer"] == l) for l in ["L0", "L1", "L2", "L3", "L4", "L5", "L6"]}
    return errors, notes


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    a = ap.parse_args()
    errs, notes = run(a.base)
    print(json.dumps(notes, ensure_ascii=False, indent=1))
    print(f"errors: {len(errs)}")
    for e in errs[:40]:
        print(" ", e)
    sys.exit(1 if errs else 0)
