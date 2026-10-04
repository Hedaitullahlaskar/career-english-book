# Multi-industry expansion: decisions for the author

**Status: ALL PENDING.** Nothing below has been decided, and no implementation will start until you approve.

How to read this file:
- Each decision lists the options and what each one implies.
- "Proposed in the architecture" shows what [MULTI-INDUSTRY-EXPANSION-ARCHITECTURE.md](MULTI-INDUSTRY-EXPANSION-ARCHITECTURE.md) assumes. It is a proposal, not a decision.
- Only decisions that genuinely need your approval are listed. Technical details that follow from them (file formats, validators) are not.

**How to answer:** for each decision, give the number and your choice, for example "D-01 D; D-02 Option 5; D-03 pilot IT at P band". "Other" with your own wording is always possible.

---

## Structure

### D-01 · Architecture model

| Option | What it means |
|---|---|
| A | Industry modules inside every existing level. The core is reopened and grows. |
| B | A Part VI "Industry English" after Level 5. The core is unchanged, but one volume grows. |
| C | Separate industry tracks banded to the core. There is no role layer. |
| D | Hybrid: core unchanged + industry application modules by band + role filter |

Proposed in the architecture: **D**. See §6.3 for the trade-offs.

### D-02 · Publishing format

| Option | What it means |
|---|---|
| 1 | One large book: about 2,100–3,460 pages with full tracks |
| 2 | Core book + print industry supplements: about 63–168 pages each |
| 3 | Core book + digital industry tracks |
| 4 | Core book + print industry workbooks |
| 5 | Hybrid: core in print; industries digital first, printed once they reach module or track level |

Proposed: **5**.

### D-03 · Initial industries and the pilot

**(a) The pilot industry and band.**
- **No-SME-flag options:** HOSP, IT, RTL, TRV, CORP, PROF.
- **SME needed:** BFS, HLTH, AVN, MFG, LOG, BPO.
- **Factual bases:**
  - HOSP has the strongest existing base;
  - IT, banking, retail and healthcare have overlay bases;
  - BPO, aviation, sports and manufacturing have no base.

**(b) How many industries are in the first production set** (Phase 2). Page scale per industry: about 63 pages per band module, about 168 per full track.

**(c) The first target tier** (T3 one band, or T4 full track).

Proposed: one pilot at T3, choice open.

### D-04 · Corporate / Office

| Option | What it means |
|---|---|
| (a) | A full track |
| (b) | A role layer only (admin, HR, accounts roles) over the core, which already serves general office contexts. Lower duplication. |

Proposed: open; the architecture notes (b) as lower-duplication.

### D-05 · Characters in industry content

| Option | What it means |
|---|---|
| (a) | A new protagonist per industry |
| (b) | An ensemble linked to Arif's world, e.g. the hotel's IT vendor or a guest who is a bank manager |
| (c) | No fixed protagonist: the learner takes the role |

Arif's story in the core is not changed under any option.

### D-06 · Hospitality's position

**(a) Does hospitality remain the central narrative of the core?** The core is unchanged either way. This affects how the expansion is presented: "a hotel story plus industries", or "a universal core plus industries".

**(b) Does the HOSP track extend Arif's hotel** (same hotel, other roles), or use a different property?

### D-07 · Healthcare scope

| Option | What it means |
|---|---|
| (a) | Non-clinical only: front office, patient services, administration |
| (b) | Also clinical communication, which requires clinician authorship and review |

Proposed: (a).

### D-08 · Cricket

| Option | What it means |
|---|---|
| (a) | A cricket context pack inside Sports & Sports Management |
| (b) | A separate Cricket English track |

Evidence: no cricket content in the book; the communicative functions are shared with sports management.

Proposed: (a).

### D-09 · Industry list and IDs

Approve the 14 candidate industries, or a subset, and their IDs:

`HOSP` · `IT` · `BFS` · `HLTH` · `RTL` · `BPO` · `AVN` · `EDU` · `TRV` · `LOG` · `MFG` · `CORP` · `PROF` · `SPRT`

Any merges, splits or renames, e.g. "BPO & Contact Centre" renamed "Customer Support".

## Codes and data

### D-10 · Vocabulary code architecture

| Option | Example | Effect |
|---|---|---|
| 1 | `IND-IT-V-0001` | **Collides** with the current tools (read as `V-0001`); tested |
| 2 | Continue `V-0793…` with an industry tag | No tool change; industry not visible in the code |
| 3 | `V-IT-0001`, `PAT-BFS-0001` | No collision; one-time pattern extension |
| 4 | New type per industry (`ITV-0001`) | Type count explodes |

New universal terms would continue the core sequence from V-0793. Existing codes are never renumbered under any option.

Proposed: **3**, with the core sequence for new universal terms.

### D-16 · Data placement

| Option | What it means |
|---|---|
| A | Inside `book-data.json`. Breaks current consumers and the baseline+corrections check. |
| B | One sidecar `industry-data.json` |
| C | A registry + one file per industry |

Proposed: **C**.

## Learning design

### D-11 · Role tracks

| Option | What it means |
|---|---|
| (a) | A role filter in the website/app only |
| (b) | Role tracks also in print (role index pages in supplements) |
| (c) | No role layer |

### D-12 · CEFR structure

**(a) Adopt the proposed mapping?**

| Core level | Proposed CEFR |
|---|---|
| L1 | A2+–B1 |
| L2 | B1 |
| L3 | B1+–B2 |
| L4 | B2–C1 |
| L5 | C1 |

The bands follow from this: Entry A2+–B1, Professional B1+–B2, Leadership C1.

**(b) Show CEFR labels publicly only after validation**, or not at all.

**(c) A1 pre-course:** yes or no. (C2 is not targeted.)

The book makes no CEFR claim today.

### D-13 · Assessment structure

**(a)** Use all six types (diagnostic, practice, formative, module test, performance assessment, capstone), or a subset.

**(b)** Capstone per band (3 per track), or one per track.

**(c)** Pass marks and whether results are recorded beyond the learner's device.

### D-14 · Learning cycle

Adopt "Learn → Understand → Observe → Practice → Perform → Reflect → Improve" as house methodology for industry lessons?

It is **not** in the current book. The core's existing framework (PURPOSE → AUDIENCE → MESSAGE → TONE → ACTION) stays either way.

### D-17 · Coverage tiers and claim thresholds

Approve the content-depth standard (architecture §23.1):

| Tier | Name |
|---|---|
| T0 | Universal |
| T1 | Examples (10+ examples over 3+ levels) |
| T2 | Application (6 Entry-domain lessons) |
| T3 | Module (one full band + documents + tests + capstone + SME sign-off) |
| T4 | Full track (all three bands) |

Also approve the rule that no public claim may exceed the computed tier.

## Language support and review

### D-15 · Bengali/Hindi depth and reviewers

**(a) Depth:**
- the triggers listed in architecture §19 only, or broader glosses;
- denser in the Entry band, or uniform.

**(b) Reviewers.** You have said no separate native-language reviewer will be available. Choose one:
- keep industry script content minimal and recorded as **NOT PERFORMED / unreviewed**;
- secure reviewers before any script-heavy module;
- omit script from industry content.

### D-19 · Specialist (SME) review

How SME review will be sourced for BFS, HLTH, AVN, MFG, LOG, BPO, and for safeguarding in EDU and SPRT.

Industries without an SME stay at T1/T2 (no module or track claim) until one is found.

## Media and sequencing

### D-18 · Audio

| Option | What it means |
|---|---|
| (a) | Produce audio for industry dialogues, which enables listening claims and BPO/aviation work |
| (b) | Print/read only. "Listening" may not be claimed. |

### D-20 · Sequencing relative to the core book

The core book is **not ready for publication**: human proofread NOT PERFORMED; native review NOT PERFORMED; covers PENDING; publication approval NO.

| Option | What it means |
|---|---|
| (a) | Finish and publish the core first, then start Phase 1 |
| (b) | Run Phase 1 in parallel, keeping the core files untouched |
| (c) | Pause the core |

---

**Record of decisions:** none yet. When you answer, the decisions will be recorded here with the date, and only then will an implementation phase be planned.
