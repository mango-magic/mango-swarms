# Manufacturing.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare administrative production records and training drafts from fictional or synthetic text examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Short outputs are staged for a fresh reviewer and a human; they do not establish engineering suitability or production approval. Modes are example configurations, not performance rankings. Verify the actual model and endpoint when local processing matters; a mode name alone does not establish privacy.

- [191. Defect code revision crosswalk](#uc-191)
- [192. Bill of materials naming collisions](#uc-192)
- [193. Traveler form completeness check](#uc-193)
- [194. Engineering change review questions](#uc-194)
- [195. Maintenance log recurrence index](#uc-195)
- [196. Tool crib alias dictionary](#uc-196)
- [197. Customer sample submission cover note](#uc-197)
- [198. Packaging artwork text reconciliation](#uc-198)
- [199. Inventory count recording practice](#uc-199)
- [200. Scrap reason tally reconciliation](#uc-200)

<a id="uc-191"></a>
## 191. Defect code revision crosswalk.

**Mode:** `swarm-ollama`

**Inputs:** `prior-codebook.md` - an approved fictional earlier code list; `current-codebook.md` - its approved synthetic replacement with revision notes.

**Outputs:** `defect-code-crosswalk.md` - a revision comparison with explicit mappings and unresolved code relationships.

**Starter prompt:**

> Compare prior-codebook.md and current-codebook.md to create defect-code-crosswalk.md for eight code entries. Show unchanged identifiers, definition changes, and retirements or replacements explicitly documented in revision notes. Quote the evidence for every proposed mapping and leave undocumented relationships unresolved. Do not infer equivalence from similar wording, recode production records, set tolerances, or decide product acceptance. Preserve revision labels and stay below 600 words.

**Validation / approval:** Check all identifiers, revision labels, and mapping evidence. A qualified quality records owner must approve before adopting the crosswalk, changing documentation, or applying any mapping to real records.

<a id="uc-192"></a>
## 192. Bill of materials naming collisions.

**Mode:** `swarm-ollama-claude`

**Inputs:** `bom-extract.md` - twelve synthetic component rows; `naming-rules.md` - approved fictional identifier and naming conventions.

**Outputs:** `bom-name-review.md` - an identifier-focused list of duplicate names and naming inconsistencies.

**Starter prompt:**

> Read bom-extract.md and naming-rules.md to create bom-name-review.md. Check the twelve rows for repeated identifiers, conflicting names under one identifier, and deviations from explicit naming rules. Preserve revision markers, units, and punctuation that carry meaning. Flag possible duplicates without merging records or assuming interchangeability. Do not propose substitute parts or engineering changes. Include source row IDs and keep the review below 550 words.

**Validation / approval:** Check each finding against exact source strings and distinguish naming similarity from identical identity. A master-data owner must approve before editing any bill of materials or purchasing record.

<a id="uc-193"></a>
## 193. Traveler form completeness check.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `traveler-example.md` - a synthetic production traveler text extract; `required-fields.md` - approved administrative field definitions and applicability rules.

**Outputs:** `traveler-gaps.md` - a field completeness report with unanswered recordkeeping questions.

**Starter prompt:**

> Use traveler-example.md and required-fields.md to draft traveler-gaps.md for one fictional traveler. Mark each required administrative field as present, missing, contradictory, or explicitly not applicable under the supplied rules. Preserve original entries and cite their field names. Do not fill signatures, infer completed operations, assess process quality, or authorize release. List the questions needed to resolve missing records and stay below 550 words.

**Validation / approval:** Confirm field applicability and ensure blank entries remain blank in the source record. A qualified production records owner must approve before correcting records or using the report in release review.

<a id="uc-194"></a>
## 194. Engineering change review questions.

**Mode:** `swarm-gpt`

**Inputs:** `change-summary.md` - an approved fictional change proposal; `review-template.md` - approved departmental review headings and required evidence labels.

**Outputs:** `change-questions.md` - a meeting brief showing supplied evidence and unresolved review questions.

**Starter prompt:**

> Create change-questions.md from change-summary.md and review-template.md. Organize the proposal under the supplied review headings and identify which required evidence labels have explicit supporting information. Ask one focused question for each unresolved heading, preserving component IDs and revision references. Do not judge design adequacy, select materials, invent testing, or approve implementation. Limit the brief to eight questions and 600 words.

**Validation / approval:** Verify evidence references and confirm that absence is framed as an open question. The change owner and relevant qualified reviewers must approve before circulating formal review material or advancing the change.

<a id="uc-195"></a>
## 195. Maintenance log recurrence index.

**Mode:** `swarm-claude`

**Inputs:** `maintenance-extract.md` - ten synthetic historical notes with asset IDs; `index-conventions.md` - approved descriptive labels and date formatting.

**Outputs:** `maintenance-index.md` - an index of repeated recorded terms with source-entry references.

**Starter prompt:**

> Use maintenance-extract.md and index-conventions.md to produce maintenance-index.md. Group explicitly repeated descriptions by asset ID and approved descriptive label, retaining dates and original wording. Distinguish repeated entries from confirmed repeated events when the notes are unclear. Do not diagnose causes, predict failures, prioritize maintenance, or propose inspection and repair procedures. List ambiguous references for human review and keep the index below 550 words.

**Validation / approval:** Check all dates, counts, and grouping decisions against the ten source entries. A qualified maintenance records owner must approve before incorporating the index into operational records or planning discussions.

<a id="uc-196"></a>
## 196. Tool crib alias dictionary.

**Mode:** `swarm-ollama`

**Inputs:** `tool-catalog.md` - approved fictional catalog IDs and names; `alias-notes.md` - synthetic shorthand entries with explicitly documented catalog links.

**Outputs:** `tool-aliases.md` - a traceable alias dictionary with unresolved shorthand separated.

**Starter prompt:**

> Create tool-aliases.md using tool-catalog.md and alias-notes.md. Map shorthand to catalog IDs only where the supplied notes explicitly establish the connection. Preserve size, revision, and model text exactly. List ambiguous aliases separately, including any alias linked to multiple IDs. Do not infer equivalence from similar names, suggest substitutions, or describe tool suitability. Keep the dictionary to twelve aliases and 500 words.

**Validation / approval:** Compare mappings character for character with the catalog and documented links. A tool crib owner must approve before creating labels, merging inventory entries, or using the dictionary to issue equipment.

<a id="uc-197"></a>
## 197. Customer sample submission cover note.

**Mode:** `swarm-ollama-claude`

**Inputs:** `sample-record.md` - approved synthetic sample IDs and measurement entries; `submission-template.md` - approved cover-note fields and attachment labels.

**Outputs:** `sample-cover-note.md` - a draft submission note preserving recorded measurements and unresolved gaps.

**Starter prompt:**

> Use sample-record.md and submission-template.md to draft sample-cover-note.md for three fictional samples. Populate only fields directly supported by the record, preserving identifiers, units, precision, and measurement conditions. Reference only listed attachments and mark missing information as unresolved. Do not infer conformance, certify quality, create inspection results, or claim attachments were examined. Keep the note below 500 words.

**Validation / approval:** Check every numeric string, unit, sample ID, and attachment label against the approved record. A qualified quality representative must approve before sending the note, releasing samples, or making any customer assurance.

<a id="uc-198"></a>
## 198. Packaging artwork text reconciliation.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `approved-pack-copy.md` - fictional approved packaging text with panel IDs; `proof-transcript.md` - manually prepared synthetic text from a packaging proof.

**Outputs:** `pack-copy-differences.md` - a panel-level list of omissions, additions, and wording differences.

**Starter prompt:**

> Compare approved-pack-copy.md and proof-transcript.md to write pack-copy-differences.md. Match text by panel ID and report exact wording, punctuation, quantity, and identifier differences. Mark unclear panel mappings as unresolved. Work only from the supplied transcripts; do not claim to inspect artwork or assess placement, legibility, regulatory compliance, or product safety. Keep the reconciliation below 550 words.

**Validation / approval:** Verify every difference against the transcripts and confirm a human separately checks the actual artwork. The packaging owner and required qualified reviewers must approve before releasing files for printing or production.

<a id="uc-199"></a>
## 199. Inventory count recording practice.

**Mode:** `swarm-gpt`

**Inputs:** `count-recording-guide.md` - approved fictional administrative recording instructions; `practice-counts.md` - six synthetic entries with units and documented discrepancies.

**Outputs:** `count-practice.md` - a practice worksheet and source-referenced answer key.

**Starter prompt:**

> Draft count-practice.md from count-recording-guide.md and practice-counts.md. Build six questions about recording units, preserving original entries, and documenting discrepancies exactly as the guide describes. Place the source-referenced answer key after the worksheet. Keep uncertain cases unresolved when the guide gives no answer. Do not add counting procedures, authorize adjustments, or update stock records. Limit the worksheet and key to 600 words.

**Validation / approval:** Verify each answer against the approved guide and independently check any arithmetic. An inventory controller must approve before training use or adapting any answer for a real stock adjustment.

<a id="uc-200"></a>
## 200. Scrap reason tally reconciliation.

**Mode:** `swarm-claude`

**Inputs:** `scrap-tallies.md` - synthetic counts from two shift summaries; `reason-codes.md` - approved fictional reporting codes and unit definitions.

**Outputs:** `scrap-reconciliation.md` - a comparison table with unmatched codes and accounting questions.

**Starter prompt:**

> Use scrap-tallies.md and reason-codes.md to create scrap-reconciliation.md. Compare the two summaries by exact reason code and unit, preserving each source total. Flag unknown codes, incompatible units, and arithmetic discrepancies without reallocating counts. Separate recorded reasons from any unsupported explanation of causes. Do not attribute blame, change process settings, or recommend technical remedies. Limit the table and questions to 550 words.

**Validation / approval:** Recalculate every total independently and verify code mappings against the approved definitions. A production reporting owner must approve before correcting records, sharing performance figures, or initiating any operational follow-up.

[Back to library](README.md)
