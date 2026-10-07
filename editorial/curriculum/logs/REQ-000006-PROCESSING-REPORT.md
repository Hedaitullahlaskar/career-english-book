# REQ-000006 processing report

Processing date: 8 October 2026 (Asia/Kolkata). Base commit: b089974dc6db2894cf3b5d257260c02db32a9861. Branch: editorial-audit-2026-10.

The previously returned REQ-000006 JSON response was restored from the conversation after scratch workspace maintenance and saved as responses/REQ-000006.json. Its content was not regenerated or revised. Validation checked PROMPT-ENVELOPE-v1.md, the response schema, the request's unit output schema, all three supplied tempId/type/key triples, titles, CEFR levels, communication-function references, role-instance plans and existing dependency keys.

Official ingest.py ingested one response and stored three A1 Vegetable Seller units: RIN-000001 (bargaining), RIN-000002 (quantity/weight), and RIN-000003 (payment). Each reached AI_QA with zero errors and zero warnings. All fourteen unique shared dependencies were reused. All 52 pre-existing stored objects remained byte-for-byte unchanged; the parent Vendor role core ROL-0080 and child Vegetable Seller core ROL-0081 remain separate dependencies.

The store now contains 55 objects: 52 shared L0–L5 objects and three L6 units. Ingestion added twelve review records, giving 220 in total. AI_QA is PASS; EDITORIAL_REVIEW is PENDING; SPECIALIST_REVIEW and NATIVE_REVIEW are NOT_REQUIRED with the configured reasons. Neither specialist nor native review was performed or claimed.

The official allocator assigned fifteen new vocabulary codes, V-VEGM-0001 through V-VEGM-0015, under the registered fresh-produce industry scope. No existing code changed. Original response vocabulary remains temporary proposals; stored unit vocabulary differs only by added officially allocated existingCode references. Post-ingestion QA checks restored the original proposal view for the new-vocabulary count check, which is designed for generation inputs rather than code-assigned stored content.

Official validate.py returned zero errors, zero duplicate index entries, zero duplicate content and zero vocabulary collisions. It checked all 55 objects, 220 review records, fourteen plans, eleven requests and five role profiles. The live reference index retains 926 codes. Validation uses the repository's supported JSON Schema subset, not a claim of full-spec or formal CEFR validation. Supplemental AI review checked role realism, market-stall circumstances, function coverage, A1 turn limits, assessment answers, money arithmetic and specialist boundaries. No specialist or safety advice was introduced.

Official plan.py completed with zero errors. No additional request became unlocked. REQ-000007, REQ-000009 and REQ-000010 remain PREPARED; REQ-000008 and REQ-000011 remain BLOCKED. Prepared packets were refreshed by the planner to include the newly registered vocabulary; their content was not generated.

Official compose.py produced three local editorial review previews; eleven other units await L6 content. These are review aids only, not compilation into the existing book or website. Official search_test.py passed all eight queries.

REQ-000002 / STM-0026 still excludes CFN-0108. The test-drive objects and all other existing shared records remain unchanged, preserving the approved communication-only boundary.

Only files under editorial/curriculum/ changed: the response, three stored units, index and vocabulary store, twelve review records, three previews, planner-maintained plans and request packets, processing logs and this report. Schemas, registries, profiles, tools, book-data.json, reference-index.json, existing book/PDF, website, covers, publication gates and deployment files remain unchanged. No later response was generated. Nothing was compiled or published. The deployment workflow is triggered by pushes to main, not this audit branch; no workflow was invoked.
