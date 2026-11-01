# AI proofreading and production QA addendum

**Audit date:** 2 November 2026  
**Repository:** `Hedaitullahlaskar/career-english-book`  
**Branch:** `editorial-audit-2026-10`  
**Audited source commit:** `b545cc812080599f07896da7022f71ef4039a986`  
**Book data blob:** `007b5787a9d81d63fbb89abfebb7dc5d30592c25`

## Scope and separation

This addendum reviews the existing five-level core book only. The role-based curriculum pilot under `editorial/curriculum/` is a separate, unpublished prototype and is not merged into the core book.

The repository's 1 October QA report records a full AI editorial read of all 196 core units and a five-batch proof pass of the 1,104-page PDF, with 95 PDF-proof corrections. This addendum does not misrepresent that historical review as a new human review. It adds a fresh, source-wide structural and reference audit, plus targeted AI language review.

## Verified core-book inventory

| Measure | Result |
|---|---:|
| Levels | 5 |
| Modules | 40 |
| Lessons | 186 |
| Level assessments | 5 |
| Capstones | 5 |
| Total units in register | 196 |
| Exercise blocks | 709 |
| Answer-key markers | 709 |
| Reference-index codes | 926 |
| Unit entries in reference index | 196 |

## Fresh source-wide checks

| Check | Result |
|---|---|
| Required objectives/body/practice fields | PASS — 0 missing fields |
| Duplicate unit IDs | PASS — 0 |
| Duplicate unit titles | PASS — 0 |
| Reference-index home/use targets | PASS — 0 broken targets |
| Reference codes mentioned in lesson text | PASS — 0 unknown codes |
| Exercise/answer-key marker count | PASS — counts match (709 / 709) |
| Placeholder patterns in answer-key region | PASS — 0 |
| Basic HTML tag-nesting scan | PASS — 0 flags |
| TODO/TBD/FIXME/XXX and internal production markers | PASS — 0 |
| Old audio claims and retired vendor-name markers | PASS — 0 |
| American-English house-style scan | PASS — 0 British-spelling flags |

Five repeated-word scanner hits were inspected and are intentional teaching examples or grammatically valid sequences: “really really”, “so so”, and “check in in”. They are not treated as errors.

The 29 bracketed patterns found by a broad scan are instructional sentence frames (for example, `[first step]` and `[deadline]`), not unfinished answer-key placeholders. The answer-key-region scan found zero such placeholders.

## Targeted AI language findings

These are editorial findings, not native-speaker sign-off:

1. **Vocabulary V-0011 — graduate (noun/verb).** The Bengali `স্নাতক` and Hindi `स्नातक` entries cover the noun sense but do not show the verb sense used by the example “I graduated last year”. Suggested fuller forms: Bengali `স্নাতক / স্নাতক হওয়া`; Hindi `स्नातक / स्नातक होना`.
2. **Vocabulary — responsible for.** The Bengali `দায়িত্বপ্রাপ্ত` and Hindi `जिम्मेदार` are understandable, but do not explicitly preserve the “for” relationship. Suggested learner-facing forms: Bengali `...-এর জন্য দায়ী / ...-এর দায়িত্বে থাকা`; Hindi `... के लिए ज़िम्मेदार`.
3. **Cultural/localisation statements.** The book contains general statements about Bengali/Hindi workplace communication. Keep qualifiers such as “some”, “many”, and “often”, avoid treating either language community as uniform, and make room for regional, generational, organisational and individual differences.

These proposed language edits are recorded for follow-up; they have not been silently applied to the source data or represented as native-speaker-approved corrections.

## Publication blockers still present in the repository

- Human PDF proofread register: 198 rows remain pending/not approved (the register has 198 rows).
- Bengali/Hindi review register: 243 items remain pending/not approved (243 items).
- Both cover files are recorded in the proof checklist as 1024 × 1536 px (about 131 ppi on A4), below the print target of 2480 × 3508 px at 300 ppi.
- The PDF is ignored by Git and is not present in the repository tree as a committed production artifact.
- Final regeneration, final PDF QA and publication approval remain pending in `editorial/proof/publication-gates.json`.

## AI-only production decision

The source-wide structural checks pass, and the existing AI editorial proof pass is recorded for all 196 units. However, the repository's own publication policy explicitly says that AI review does not replace named human editorial, specialist or native-language review, and that a required review marked NOT_PERFORMED cannot be converted to PASS.

Therefore this addendum records **AI-REVIEWED / NOT HUMAN-APPROVED**. It does not change the publication gates, does not mark the native-language register approved, and does not claim a print-ready final PDF. This protects the author from an inaccurate publication claim.

## Per-unit evidence

See `AI-PROOFREADING-REGISTER-2026-11-02.csv` for all 196 units, including exercise counts, answer-key marker counts, structural checks, and the separate human/native review statuses.
