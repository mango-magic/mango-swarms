# Property.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare property records, presentation material, and administrative review questions from fictional or synthetic examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Outputs are short staged drafts assessed by a fresh reviewer and a human, without inspecting buildings or taking operational action. Modes are examples, not quality rankings. Verify the actual model and endpoint when local processing matters; a mode name alone does not establish privacy.

- [171. Building service responsibility questions](#uc-171)
- [172. Move-in condition note reconciliation](#uc-172)
- [173. Meter handover anomaly log](#uc-173)
- [174. Shared-space reservation scenarios](#uc-174)
- [175. Property photography coverage brief](#uc-175)
- [176. Building energy display narrative](#uc-176)
- [177. Commercial space viewing questions](#uc-177)
- [178. Refurbishment scope boundary ledger](#uc-178)
- [179. Vacant-unit staging prop plan](#uc-179)
- [180. Planned works notice consistency](#uc-180)

<a id="uc-171"></a>
## 171. Building service responsibility questions.

**Mode:** `swarm-ollama`

**Inputs:** `service-summary.md` - an approved fictional responsibility summary; `service-queries.md` - eight synthetic administrative questions with query IDs.

**Outputs:** `responsibility-questions.md` - a source-backed routing draft with unresolved responsibilities flagged.

**Starter prompt:**

> Use service-summary.md and service-queries.md to draft responsibility-questions.md. For each query, quote any explicit responsibility assignment in the summary and name only the stated role. Leave ambiguous or absent assignments unresolved and suggest one clarification question. Do not interpret contract obligations, decide liability, or expand a role's duties. Preserve all query IDs and limit the draft to 550 words.

**Validation / approval:** Verify that every proposed role appears in the approved summary and that ambiguity remains visible. A property manager must approve before contacting a service provider or changing any responsibility record.

<a id="uc-172"></a>
## 172. Move-in condition note reconciliation.

**Mode:** `swarm-ollama-claude`

**Inputs:** `condition-notes.md` - synthetic observations from two fictional inspections; `room-index.md` - approved room and fixture identifiers.

**Outputs:** `condition-reconciliation.md` - a neutral comparison of matching, conflicting, and unmatched observations.

**Starter prompt:**

> Create condition-reconciliation.md from condition-notes.md and room-index.md. Compare the two sets of observations for six room or fixture IDs. Preserve dates and descriptive wording, showing conflicting accounts side by side. Separate absent observations from explicit statements of no change. Do not infer damage causes, responsibility, repair needs, or safety. List unresolved identifier matches for human review and stay below 600 words.

**Validation / approval:** Check each observation against its source and confirm no disputed account became a finding. A property manager must approve before updating inspection records or discussing charges with anyone.

<a id="uc-173"></a>
## 173. Meter handover anomaly log.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `meter-register.md` - approved fictional meter serials, measurement units, and reset notes; `handover-readings.md` - synthetic dated readings around a tenancy handover.

**Outputs:** `meter-anomalies.md` - a device-level discontinuity log for checking handover records.

**Starter prompt:**

> Use meter-register.md and handover-readings.md to draft meter-anomalies.md. For six meters, flag decreasing counters without documented resets, changed serials, unit mismatches, and readings dated out of sequence. Preserve original values and explain each flag using record IDs. Do not infer tampering, equipment faults, consumption charges, or tenant liability. Keep the log below 500 words.

**Validation / approval:** Independently compare serials, dates, units, and counter values. A property manager must approve before updating meter records, contacting suppliers, or using readings for billing.

<a id="uc-174"></a>
## 174. Shared-space reservation scenarios.

**Mode:** `swarm-gpt`

**Inputs:** `reservation-rules.md` - approved fictional common-room rules; `scenario-notes.md` - six synthetic requests with dates, durations, and stated purposes.

**Outputs:** `reservation-scenarios.md` - a staff discussion sheet with rule references and unresolved cases.

**Starter prompt:**

> Draft reservation-scenarios.md from reservation-rules.md and scenario-notes.md. For each fictional request, identify relevant explicit rules and show the exact source wording. Highlight missing information or conflicts between rules without deciding an outcome. Add one discussion question per scenario. Do not reserve a room, promise availability, create exceptions, or interpret legal rights. Keep all six cases together below 600 words.

**Validation / approval:** Verify times, durations, and rule quotations independently. A building administrator must approve the training sheet before use and separately approve any real reservation or communication about availability.

<a id="uc-175"></a>
## 175. Property photography coverage brief.

**Mode:** `swarm-claude`

**Inputs:** `property-description.md` - approved fictional room and feature descriptions; `photo-brief.md` - requested presentation goals and approved photography locations.

**Outputs:** `photo-coverage.md` - a text-only shot list connecting features to the presentation brief.

**Starter prompt:**

> Use property-description.md and photo-brief.md to create photo-coverage.md with at most ten proposed shots. For each shot, name the described feature, an approved location, and the presentation purpose. Flag desired coverage that the supplied descriptions cannot support. Do not claim to inspect photographs, invent views or dimensions, or provide access instructions. Keep the shot list below 500 words.

**Validation / approval:** Confirm every feature and location appears in the inputs and that unsupported coverage is flagged. A property representative must approve the brief and photography permissions before arranging or conducting a shoot.

<a id="uc-176"></a>
## 176. Building energy display narrative.

**Mode:** `swarm-ollama`

**Inputs:** `energy-readings.md` - six synthetic monthly totals with units and coverage notes; `display-guide.md` - approved explanatory wording and comparison limits.

**Outputs:** `energy-display.md` - a small readings table and a descriptive noticeboard draft.

**Starter prompt:**

> Create energy-display.md using energy-readings.md and display-guide.md. Reproduce the six monthly totals and describe only comparisons permitted by the guide. Preserve units and incomplete-period notes. If periods are not comparable, explain the limitation rather than calculating a change. Do not attribute causes, claim savings, forecast bills, or recommend equipment. Limit the table and narrative together to 450 words.

**Validation / approval:** Independently verify copied values, any arithmetic, and period comparability. A building manager must approve before displaying the narrative or using it in communications about building performance.

<a id="uc-177"></a>
## 177. Commercial space viewing questions.

**Mode:** `swarm-ollama-claude`

**Inputs:** `space-summary.md` - approved fictional premises features; `use-brief.md` - a synthetic occupier's stated room, storage, and delivery needs.

**Outputs:** `viewing-questions.md` - a focused viewing agenda separating documented facts from open questions.

**Starter prompt:**

> Use space-summary.md and use-brief.md to draft viewing-questions.md. Map up to eight stated operational needs to explicit features, missing information, or questions for the property representative. Preserve dimensions and distinguish a documented feature from assumed suitability. Do not evaluate lease terms, investment value, zoning, accessibility compliance, or structural capacity. Keep the agenda below 550 words and avoid ranking the premises.

**Validation / approval:** Check that every question connects to a supplied need and every factual answer has a source. The prospective occupier must approve before sending the agenda or arranging a viewing.

<a id="uc-178"></a>
## 178. Refurbishment scope boundary ledger.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `work-packages.md` - two approved fictional refurbishment summaries; `scope-labels.md` - administrative categories for included, excluded, and unresolved items.

**Outputs:** `scope-boundaries.md` - a ledger of explicit package boundaries and overlap questions.

**Starter prompt:**

> Read work-packages.md and scope-labels.md to prepare scope-boundaries.md for ten named work items. Quote each item's documented inclusion or exclusion under the two packages. Flag overlapping wording and items neither summary addresses. Do not assign responsibility, modify technical scope, price work, or invent construction methods. Finish with at most five clarification questions for the project owner and keep the ledger below 600 words.

**Validation / approval:** Verify item names and source quotations without treating silence as exclusion. A project owner and relevant qualified professionals must approve before changing scope documents or instructing any contractor.

<a id="uc-179"></a>
## 179. Vacant-unit staging prop plan.

**Mode:** `swarm-gpt`

**Inputs:** `staging-brief.md` - approved fictional room descriptions and presentation goals; `prop-inventory.md` - synthetic decorative props with item IDs and style notes.

**Outputs:** `staging-props.md` - a text staging concept with room assignments and unused inventory.

**Starter prompt:**

> Use staging-brief.md and prop-inventory.md to draft staging-props.md for two vacant-unit rooms. Assign up to six decorative props to room concepts, explaining each choice against the presentation goals. Use each selected item ID once and list unused inventory separately. Do not invent furnishings, specify installation, infer physical fit, or recommend purchases. Keep the concept below 500 words.

**Validation / approval:** Verify every item exists and is assigned once. A staging coordinator must approve the concept and assess placement onsite before moving props or commissioning photography.

<a id="uc-180"></a>
## 180. Planned works notice consistency.

**Mode:** `swarm-claude`

**Inputs:** `approved-logistics.md` - fictional, approved work dates and communication details; `notice-draft.md` - a synthetic resident notice for the same project.

**Outputs:** `notice-review.md` - a discrepancy table and a corrected administrative notice draft.

**Starter prompt:**

> Compare notice-draft.md with approved-logistics.md and write notice-review.md. Check project names, dates, stated service interruptions, and contact labels against the approved facts. Provide a corrected draft only for resolved discrepancies and list remaining questions separately. Copy any supplied approved instructions exactly; do not create procedures, access permissions, guarantees, or tenant-rights advice. Keep both sections together below 600 words.

**Validation / approval:** Verify dates and interruptions manually, including unresolved source conflicts. A property manager must approve before distributing the notice, contacting residents, or making any change to the works schedule.

[Back to library](README.md)
