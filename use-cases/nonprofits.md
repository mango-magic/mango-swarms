# Nonprofits.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Organize program evidence, volunteer records, and community material from fictional or synthetic examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Outputs remain short staged drafts for a fresh reviewer and a human to inspect. Modes are example configurations, not claims of superiority. Verify the actual model and endpoint when local processing matters; mode names alone do not establish privacy.

- [161. Matching gift pool illustration](#uc-161)
- [162. Seed library batch handoff](#uc-162)
- [163. Pantry packing list reconciliation](#uc-163)
- [164. Donor restriction discussion cases](#uc-164)
- [165. Impact story claim tracing](#uc-165)
- [166. Mutual aid request taxonomy](#uc-166)
- [167. Community listening theme map](#uc-167)
- [168. Fundraiser auction lot proofing](#uc-168)
- [169. Program archive finding aid](#uc-169)
- [170. Volunteer rota coverage draft](#uc-170)

<a id="uc-161"></a>
## 161. Matching gift pool illustration.

**Mode:** `swarm-ollama`

**Inputs:** `match-rules.md` - approved fictional multipliers, gift caps, and total matching pool; `sample-gifts.md` - six synthetic gift amounts in recorded order.

**Outputs:** `match-examples.md` - a worked sequence showing provisional matches and the remaining pool.

**Starter prompt:**

> Use match-rules.md and sample-gifts.md to draft match-examples.md. Work through the six gifts sequentially under the supplied arithmetic rules. Show each copied gift amount, provisional match, and remaining matching pool. Apply limits only as explicitly specified and leave undefined edge cases unresolved. Do not process donations, claim deductibility, or imply actual sponsor funding. Keep the illustration below 500 words.

**Validation / approval:** Independently recompute every match and pool balance against the stated limits. A fundraising owner and qualified finance reviewer must approve before using examples in campaign materials.

<a id="uc-162"></a>
## 162. Seed library batch handoff.

**Mode:** `swarm-ollama-claude`

**Inputs:** `batch-records.md` - synthetic seed packet counts and batch identifiers; `handoff-fields.md` - approved administrative handoff fields and status definitions.

**Outputs:** `seed-handoff.md` - a batch handoff record with count discrepancies and missing fields.

**Starter prompt:**

> Prepare seed-handoff.md using batch-records.md and handoff-fields.md for five fictional seed library batches. Map each batch into the approved fields and preserve units, dates, and provenance wording exactly. Show conflicting counts side by side and flag absent labels. Do not infer viability, species identity, planting suitability, or distribution readiness. Finish with at most five administrative questions for the coordinator. Keep the draft below 550 words.

**Validation / approval:** Reconcile every batch ID and copied count with the source records. A program coordinator must approve before updating inventory or using the handoff to organize distribution.

<a id="uc-163"></a>
## 163. Pantry packing list reconciliation.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `packing-template.md` - an approved fictional box template with item IDs; `donation-list.md` - synthetic item names, pack sizes, and available quantities.

**Outputs:** `packing-questions.md` - a textual reconciliation of exact matches and unresolved item differences.

**Starter prompt:**

> Use packing-template.md and donation-list.md to draft packing-questions.md for a planning exercise. Match only identical item IDs and report quantity or pack-size differences in a table. Keep ambiguous names unmatched and list the information needed to reconcile them. Do not recommend substitutions, decide food suitability, assess allergens, or create handling instructions. Preserve template quantities and mark results as a draft for coordinator review. Stay below 550 words.

**Validation / approval:** Check identifiers, units, and arithmetic independently. A pantry coordinator must approve before any purchasing, packing, distribution, or change to the approved template.

<a id="uc-164"></a>
## 164. Donor restriction discussion cases.

**Mode:** `swarm-gpt`

**Inputs:** `restriction-examples.md` - approved fictional donor wording; `review-process.md` - approved steps for escalating ambiguous restrictions to qualified staff.

**Outputs:** `restriction-cases.md` - four discussion cases with source excerpts and escalation questions.

**Starter prompt:**

> Create restriction-cases.md from restriction-examples.md and review-process.md for a learning session. Build four short cases around ambiguities already present in the examples. Quote the relevant donor wording and ask what information a qualified reviewer would need. Connect each case to the approved escalation step. Do not interpret enforceability, authorize spending, or add tax or legal advice. Leave every case unresolved and keep the document below 600 words.

**Validation / approval:** Confirm cases preserve restrictions verbatim and escalation steps match the approved source. A fundraising lead and qualified reviewer must approve before staff training or operational use.

<a id="uc-165"></a>
## 165. Impact story claim tracing.

**Mode:** `swarm-claude`

**Inputs:** `story-draft.md` - a fictional participant story; `story-record.md` - approved synthetic events, quotations, and permission boundaries for that example.

**Outputs:** `story-trace.md` - a sentence-level evidence map and a bounded revision checklist.

**Starter prompt:**

> Use story-draft.md and story-record.md to create story-trace.md. Examine up to twelve sentences for factual support, quotation accuracy, and alignment with the stated permission boundaries. Flag invented chronology, stronger causal claims, and details absent from the record. Suggest a deletion or verification question for each gap without writing a new participant story. Distinguish unsupported wording from contradicted wording. Keep the evidence map and checklist under 650 words.

**Validation / approval:** Verify all quotations and sentence references manually. A communications owner must approve before publication; fictional permission boundaries never establish consent for a real person's story.

<a id="uc-166"></a>
## 166. Mutual aid request taxonomy.

**Mode:** `swarm-ollama`

**Inputs:** `sample-requests.md` - twelve synthetic, nonurgent requests without personal identifiers; `category-rules.md` - approved service labels and category definitions.

**Outputs:** `request-taxonomy.md` - a labeled practice set with ambiguous cases and terminology questions.

**Starter prompt:**

> Read sample-requests.md and category-rules.md to create request-taxonomy.md. Assign each request only supplied descriptive labels that its words support. Allow multiple labels where definitions permit them and leave uncertain cases unclassified. Explain ambiguity using request IDs and exact phrases. Do not decide eligibility, urgency, recipient priority, or service matching. Include at most four questions that would improve the category definitions. Limit the draft to 600 words.

**Validation / approval:** Check that every request appears once and labels follow the approved definitions without sensitive inferences. A program lead must approve before adapting the taxonomy for intake records.

<a id="uc-167"></a>
## 167. Community listening theme map.

**Mode:** `swarm-ollama-claude`

**Inputs:** `listening-notes.md` - fifteen synthetic comments with comment IDs; `session-questions.md` - approved fictional session questions and scope.

**Outputs:** `listening-themes.md` - a theme map retaining contrasting and isolated perspectives.

**Starter prompt:**

> Use listening-notes.md and session-questions.md to draft listening-themes.md. Group the fifteen comments into no more than five descriptive themes, attaching comment IDs to each. Preserve disagreement and give isolated concerns a visible section. Report comment counts only, never population prevalence or community consensus. Do not infer speakers' identities, motivations, or demographics. End with three follow-up questions grounded in unresolved comments. Keep the map below 650 words.

**Validation / approval:** Trace every theme to actual comments, verify counts, and check that minority views remain visible. A session facilitator must approve before sharing findings or using them in program decisions.

<a id="uc-168"></a>
## 168. Fundraiser auction lot proofing.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `lot-records.md` - approved fictional donated-item descriptions and restrictions; `catalog-draft.md` - draft text for eight synthetic auction lots.

**Outputs:** `auction-proof.md` - a lot-by-lot discrepancy list and corrected factual descriptions.

**Starter prompt:**

> Read lot-records.md and catalog-draft.md and create auction-proof.md for the eight listed lots. Compare inclusions, expiry dates, redemption wording, and restrictions using exact lot IDs. Supply a corrected description only where the approved record resolves the difference. Leave conflicts between source records as questions. Do not estimate value, add availability promises, invent donor recognition, or conduct bidding. Keep the combined discrepancy list and proposed descriptions below 650 words.

**Validation / approval:** Check dates, inclusions, restrictions, and lot IDs against the records. A fundraiser organizer must approve before publishing descriptions, contacting donors, or offering any lot for bidding.

<a id="uc-169"></a>
## 169. Program archive finding aid.

**Mode:** `swarm-gpt`

**Inputs:** `archive-index.md` - metadata for twelve fictional program records; `archive-conventions.md` - approved description fields and access labels.

**Outputs:** `program-finding-aid.md` - a concise record guide with explicit metadata gaps.

**Starter prompt:**

> Use archive-index.md and archive-conventions.md to draft program-finding-aid.md. Group the twelve records by their documented program phase and preserve record identifiers, dates, and access labels. Write a description from each supplied summary without implying you inspected the underlying document. Mark unknown dates and phases instead of guessing. Include an index of inconsistent titles for human cleanup. Do not propose retention, deletion, or access changes. Stay below 650 words.

**Validation / approval:** Confirm every record is included once and all access labels remain unchanged. An archive owner must approve before importing the guide, moving records, or sharing descriptions externally.

<a id="uc-170"></a>
## 170. Volunteer rota coverage draft.

**Mode:** `swarm-claude`

**Inputs:** `volunteer-availability.md` - six synthetic volunteers' available times, permitted roles and any stated preferences; `book-sale-coverage.md` - approved fictional desk slots, coverage counts, and assignment limits.

**Outputs:** `volunteer-rota.md` - one proposed coverage table with unfilled slots and unmet preferences.

**Starter prompt:**

> Use volunteer-availability.md and book-sale-coverage.md to draft volunteer-rota.md for four book-sale desk slots. Propose assignments only within stated availability, permitted roles, and assignment limits. Show coverage per slot, leave infeasible slots open, and list any explicitly stated preferences the draft cannot meet. Use volunteer IDs without inferring skills or willingness. Do not contact volunteers or update schedules. Keep the draft below 550 words.

**Validation / approval:** Check every assignment, overlap, coverage count, and limit independently. A volunteer coordinator must approve before confirming assignments, sending messages, or entering the rota into a scheduling system.

[Back to library](README.md)
