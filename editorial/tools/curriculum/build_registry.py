"""Build editorial/curriculum/registry/*.json from the approved registry CSVs in editorial/.

Usage: python editorial/tools/curriculum/build_registry.py

Sources (approved 4 October 2026): INDUSTRY-REGISTRY.csv, ROLE-FAMILY-REGISTRY.csv, DEPARTMENT-REGISTRY.csv,
ROLE-UNIVERSE.csv, SITUATION-LIBRARY.csv, COMMUNICATION-FUNCTION-LIBRARY.csv. The CSVs stay the
human-readable source; the JSON files are what the tools read. Counts are checked against the approved
reconciliation (27 sectors, 122 industries, 62 families, 211 scope codes, 402 roles).
"""
import csv
import sys

from cur import CODE_TYPES, CORE_CODE, EDITORIAL, save, store

sys.stdout.reconfigure(encoding="utf-8")


def rows(name):
    return list(csv.DictReader(open(EDITORIAL / name, encoding="utf-8")))


def split(v, sep=";"):
    return [x.strip() for x in (v or "").split(sep) if x.strip()]


def main():
    reg = rows("INDUSTRY-REGISTRY.csv")
    sectors = [{"id": r["ID"], "code": r["Scope code"], "name": r["Name"], "reviewFlags": split(r["Default review flags (sector)"], " ")}
               for r in reg if r["Level"] == "Sector"]
    industries = [{"id": r["ID"], "code": r["Scope code"], "name": r["Name"], "sector": r["Parent"], "aliases": split(r["Search aliases"])}
                  for r in reg if r["Level"] == "Industry"]
    fams = [{"id": r["ID"], "code": r["Scope code"], "name": r["Role family"], "group": r["Family group"],
             "roleCore": split(r["Role core: communication requirements"]),
             "coreModules": [x.split()[0] for x in split(r["Core modules (domain)"])]} for r in rows("ROLE-FAMILY-REGISTRY.csv")]
    deps = [{"id": r["ID"], "name": r["Department / function"], "group": r["Function group"]} for r in rows("DEPARTMENT-REGISTRY.csv")]
    roles = []
    for r in rows("ROLE-UNIVERSE.csv"):
        roles.append({"id": r["Role ID"], "name": r["Role"], "family": r["Family code"],
                      "parent": r["Parent role (inherits role core)"].split(" ")[0] or None,
                      "defaultLevel": r["Default responsibility level"].split(" ")[1],
                      "primaryDepartment": r["Primary department"].split(" ")[0],
                      "employmentSettings": split(r["Employment settings"]),
                      "commonSectors": r["Common in sectors"].split(), "specialisationSectors": r["Specialisation required in sectors"].split(),
                      "special": r["Special-role requirement (author list)"] == "Y",
                      "reviewTriggers": split(r["Specialist review triggers"]),
                      "aliases": split(r["Search aliases (transliterations pending native review)"]), "status": r["Registry status"]})
    sits = [{"id": r["ID"], "category": r["Category ID"], "categoryName": r["Category"], "name": r["Situation template"],
             "functions": r["Typical functions"].split(), "stakeholders": split(r["Typical stakeholders"]), "modes": r["Modes"].split(),
             "layers": r["Typical layers (any CEFR)"].split(), "frontline": r["Frontline-relevant"] == "Y",
             "reviewTriggers": r["Specialist review triggers"].split()} for r in rows("SITUATION-LIBRARY.csv")]
    funcs = [{"id": r["ID"], "group": r["Group"], "groupName": r["Group name"], "name": r["Function"], "layer": r["Lowest typical layer"],
              "newInEngine": r["New in engine (not taught in core book)"] == "Y", "coreLocation": r["Core book location (where taught)"],
              "coreCodes": r["Core codes"].replace(",", " ").split()} for r in rows("COMMUNICATION-FUNCTION-LIBRARY.csv")]

    # Responsibility levels (SENIORITY-PROGRESSION-ARCHITECTURE §2; D-U05: extensible, ranks spaced)
    levels = [("SEN-0001", 10, "Intern / Trainee", "operational", "TRN"), ("SEN-0002", 20, "Assistant / Associate", "operational", "AST"),
              ("SEN-0003", 30, "Executive / Officer", "operational", "EXE"), ("SEN-0004", 35, "Specialist / Professional", "operational", "PRO"),
              ("SEN-0005", 40, "Senior Executive / Senior Specialist / Coordinator", "operational", "SNR"),
              ("SEN-0006", 50, "Supervisor / Team Leader", "supervisory", "SUP"), ("SEN-0007", 60, "Assistant Manager", "managerial", "AM"),
              ("SEN-0008", 70, "Manager", "managerial", "MGR"), ("SEN-0009", 80, "Senior Manager / Department Head", "managerial", "HOD"),
              ("SEN-0010", 90, "Director / General Manager", "executive", "DIR"), ("SEN-0011", 100, "Managing Director / CEO", "enterprise", "MD"),
              ("SEN-0012", None, "Founder / Owner / Entrepreneur (ownership track)", "ownership", "OWN")]
    levels = [{"id": i, "rank": rk, "name": n, "layer": ly, "short": s, "track": "ownership" if s == "OWN" else "main",
               "scales": ["solo", "small-team", "company"] if s == "OWN" else []} for i, rk, n, ly, s in levels]
    settings = [{"id": f"EMP-{i:02d}", "name": n} for i, n in enumerate(
        ["formal employer", "self-employed / own-account", "gig / platform", "public service", "NGO / community", "informal employee / helper",
         "household employer"], 1)]
    cefr = [{"code": c, "order": i, "standard": True} for i, c in enumerate(["Pre-A1", "A1", "A2", "B1", "B2", "C1", "C2"])]
    core_modules = [
        ("CM-01", "Workplace basics", "SC01 SC02 SC11 SC12 SC14"), ("CM-02", "Customer service", "SC02 SC06 SC07"),
        ("CM-03", "Selling", "SC03"), ("CM-04", "Transactions & payment", "SC04"), ("CM-05", "Field & public interaction", "SC08 SC09"),
        ("CM-06", "Delivery & mobility", "SC05"), ("CM-07", "Technical work & safety", "SC10 SC11"), ("CM-08", "Operations & reporting", "SC13 SC14"),
        ("CM-09", "Office & digital communication", "SC12 SC15 SC16"), ("CM-10", "Team supervision", "SC14 SC19 SC20"),
        ("CM-11", "Management", "SC18 SC19 SC20 SC21 SC22 SC23"), ("CM-12", "Executive & ownership", "SC17 SC22"),
        ("CM-13", "Teaching & training", "SC24 SC17"), ("CM-14", "Care & patient communication (non-clinical)", "SC25"),
        ("CM-15", "Public procedures", "SC09")]
    core_modules = [{"id": i, "name": n, "situationCategories": c.split(), "status": "APPROVED_FOR_PILOT (revisable after U-1, D-U03)"}
                    for i, n, c in core_modules]
    seniority_modules = {"SUP": ["CM-10"], "AM": ["CM-10", "CM-11"], "MGR": ["CM-10", "CM-11"], "HOD": ["CM-10", "CM-11"],
                         "DIR": ["CM-11", "CM-12"], "MD": ["CM-11", "CM-12"], "OWN:company": ["CM-12"]}
    archetypes = [{"id": f"STK-{i:04d}", "name": n} for i, n in enumerate(
        ["Customer", "Regular customer", "Supervisor", "Manager", "Colleague", "Supplier", "Patient", "Parent", "Driver", "Technician",
         "HR Manager", "Sales Manager", "Candidate", "Employee / team member", "Restaurant staff", "Support team (platform)",
         "Building guard / receptionist", "Department head", "Finance / loan executive", "Market neighbour (another seller)"], 1)]

    scope = ([{"code": s["code"], "kind": "sector", "recordId": s["id"]} for s in sectors]
             + [{"code": i["code"], "kind": "industry", "recordId": i["id"]} for i in industries]
             + [{"code": f["code"], "kind": "role-family", "recordId": f["id"]} for f in fams])
    codes = [s["code"] for s in scope]
    # approved reconciliation (D, 4 October 2026) and D-U07 safety checks
    assert len(sectors) == 27 and len(industries) == 122 and len(fams) == 62 and len(codes) == 211, (len(sectors), len(industries), len(fams), len(codes))
    assert len(set(codes)) == len(codes), "duplicate scope code"
    assert not set(codes) & CODE_TYPES, "scope code equals a code type"
    assert not [c for c in codes for t in CODE_TYPES if CORE_CODE.search(f"{t}-{c}-0001")], "scope code collides with core pattern"
    assert len(roles) == 402
    sec_codes = {s["code"] for s in sectors}
    for r in roles:
        assert set(r["commonSectors"] + r["specialisationSectors"]) <= sec_codes, r["id"]

    out = store("registry")
    for name, obj in [("sectors", sectors), ("industries", industries), ("role-families", fams), ("departments", deps), ("roles", roles),
                      ("situation-templates", sits), ("communication-functions", funcs), ("responsibility-levels", levels),
                      ("employment-settings", settings), ("cefr-levels", cefr), ("core-modules", core_modules),
                      ("seniority-core-modules", seniority_modules), ("stakeholder-archetypes", archetypes), ("scope-codes", scope)]:
        save(out / f"{name}.json", obj)
    print(f"registry: {len(sectors)} sectors, {len(industries)} industries, {len(fams)} families, {len(deps)} departments, "
          f"{len(roles)} roles, {len(sits)} situation templates, {len(funcs)} functions, {len(core_modules)} core modules, "
          f"{len(levels)} responsibility levels, {len(cefr)} CEFR levels, {len(scope)} scope codes")


if __name__ == "__main__":
    main()
