# U-1 Batch 1 processing report

Date: 4 October 2026. Base: e2a529b. Branch: editorial-audit-2026-10.

## Results

- Responses validated: 4; successfully ingested: 4.
- Shared records stored: 44 (L0: 22; L1: 11; L2: 5; L3: 6).
- Review records: 176. AI_QA PASS for all 44; Editorial Review PENDING for all 44. Specialist and Native Review NOT_REQUIRED with reasons; neither performed nor claimed as PASS.
- Lesson units unlocked: 0. Next request unlocked: REQ-000005 (8 L4/L5 overlay objects). REQ-000006 through REQ-000011 remain BLOCKED.
- Official validate.py: 0 errors; duplicate index entries: 0; duplicate content: 0; vocabulary collisions: 0.
- Official search_test.py: 8/8 PASS. compose.py: 0 composed, 14 awaiting layers. This produces local review previews only, not publication output.
- Official isolated synthetic pipeline test: PASS. Its deliberate negative fixtures exercised duplicate refusal, invalid vocabulary rejection and industry-difference checks. Fixture content was not written to the real store.
- Real-content AI QA: 0 errors, 0 warnings. No new vocabulary codes; the live reference index retains its 926 existing codes.

## Contract and boundary checks

The four responses were copied byte-for-byte from the generated files. Their request identifiers, contract versions, tempIds, types and keys match the original packets. Every output uses record.content with exactly the required content fields. L0 CEFR/function values, L1 situation functions and L3 parent/role links are correct. Supplemental checks confirmed limits and references alongside the official repository subset schema validator; no claim of full JSON Schema validation is made.

REQ-000002/STM-0026 contains only CFN-0091 and CFN-0097. Its communication-only constraints remain in place; RIN-000005 explicitly excludes CFN-0108. Stored SCN-000005 covers arranging/coordinating the appointment and customer communication only. Content review found no driving, road-safety, vehicle-operation or safety-training instructions. Negative boundary statements are exclusions, not instructions.

Shared layers resolve to one indexed object per key. Child Vegetable Seller and Car Sales Executive cores retain the Street Vendor and Sales Executive parent links. One shared HR Manager core serves both industries. Vocabulary.json is empty: no new codes or scope assignments are needed in this batch.

## Changes and limitations

Only editorial/curriculum processing files are changed: unchanged response copies, content/index/vocabulary, generated review and usage records, planner-updated layer references and request packets, composition/search/planning logs, and this report. No schemas, registries, role profiles, tooling or existing book/publication files were changed. Planning prepares downstream request packets but does not generate their content.

All real content remains at AI_QA with editorial review pending. No REQ-000005+ content was generated. Nothing was compiled or published. The existing PDF, website, covers, publication gates, book-data.json, reference-index.json and deployment workflow remain unchanged.
