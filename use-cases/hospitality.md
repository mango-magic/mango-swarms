# Hospitality.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Draft guest information, event records, and training material from fictional or synthetic examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each short output is staged for a fresh reviewer and human approval; the toolkit does not contact guests or operate booking systems. Modes are example configurations, not performance rankings. Verify the actual model and endpoint if local processing matters; mode names alone do not establish privacy.

- [181. Menu provenance notes](#uc-181)
- [182. Hotel room category distinctions](#uc-182)
- [183. Event run sheet contradiction review](#uc-183)
- [184. Tasting flight comparison placemat](#uc-184)
- [185. Lost property record normalization](#uc-185)
- [186. Special request training dialogues](#uc-186)
- [187. Audio tour script length review](#uc-187)
- [188. Banquet place card proofing](#uc-188)
- [189. Itinerary promise audit](#uc-189)
- [190. Room status handover chronology](#uc-190)

<a id="uc-181"></a>
## 181. Menu provenance notes.

**Mode:** `swarm-ollama`

**Inputs:** `menu-items.md` - six fictional dish descriptions with item IDs; `supplier-stories.md` - approved synthetic origin and producer notes.

**Outputs:** `menu-provenance.md` - short provenance notes with source references and unsupported claims flagged.

**Starter prompt:**

> Create menu-provenance.md using menu-items.md and supplier-stories.md. Draft one brief provenance note for each dish with a documented producer or origin connection. Cite the supporting story ID and leave missing connections unresolved. Preserve the scope of seasonal and sourcing statements. Do not invent traditions, certifications, sustainability benefits, ingredients, or health and allergen claims. Keep all six entries together below 500 words.

**Validation / approval:** Check each origin and producer connection against the approved source, including time qualifiers. A restaurant owner and source owner must approve before printing menus or sharing provenance claims with guests.

<a id="uc-182"></a>
## 182. Hotel room category distinctions.

**Mode:** `swarm-ollama-claude`

**Inputs:** `room-types.md` - approved fictional specifications for four room categories; `training-questions.md` - synthetic guest questions about stated room features.

**Outputs:** `room-category-cards.md` - a comparison matrix and source-grounded front desk practice answers.

**Starter prompt:**

> Use room-types.md and training-questions.md to create room-category-cards.md. Compare the four categories using only stated features, preserving differences between guaranteed features and requests. Answer up to six practice questions from those specifications and mark missing information explicitly. Do not imply availability, promise upgrades, infer accessibility suitability, or recommend a booking. Keep the matrix and answers together below 600 words.

**Validation / approval:** Verify each category and feature qualifier against the source. A front desk manager must approve before training use or guest communication, with live availability checked separately by authorized staff.

<a id="uc-183"></a>
## 183. Event run sheet contradiction review.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `event-agenda.md` - an approved fictional six-segment agenda; `venue-run-sheet.md` - synthetic room, equipment, and timing notes for that event.

**Outputs:** `event-conflicts.md` - a compact discrepancy table and questions for the event coordinator.

**Starter prompt:**

> Compare event-agenda.md and venue-run-sheet.md to create event-conflicts.md. Check segment names, start and end times, room labels, and explicitly listed equipment. Show disagreements side by side with source references, distinguishing conflicts from missing details. Do not reschedule segments, assign staff, resolve equipment availability, or invent setup requirements. Include at most eight review questions and keep the document below 550 words.

**Validation / approval:** Independently check time intervals and exact room identifiers. An event coordinator must approve before changing the run sheet, reserving equipment, or communicating revised arrangements to participants.

<a id="uc-184"></a>
## 184. Tasting flight comparison placemat.

**Mode:** `swarm-gpt`

**Inputs:** `tasting-notes.md` - approved fictional descriptions of four nonalcoholic drinks; `flight-brief.md` - presentation order and approved sensory vocabulary.

**Outputs:** `flight-placemat.md` - four concise comparison panels and optional observation prompts.

**Starter prompt:**

> Draft flight-placemat.md from tasting-notes.md and flight-brief.md. Follow the supplied order and summarize each drink using only its documented sensory descriptions. Add one observation question per panel that permits a guest to disagree with the description. Preserve distinctions among aroma, texture, and flavor. Do not infer ingredients, allergens, nutritional effects, or production methods. Keep the complete placemat text below 400 words.

**Validation / approval:** Check order, product IDs, and every descriptive term against the inputs. A tasting host and product owner must approve before printing the placemat or presenting it to guests.

<a id="uc-185"></a>
## 185. Lost property record normalization.

**Mode:** `swarm-claude`

**Inputs:** `found-item-notes.md` - eight synthetic records without personal identifiers; `register-fields.md` - approved fictional register fields and item description conventions.

**Outputs:** `lost-property-draft.md` - standardized record text with ambiguities and possible duplicates flagged.

**Starter prompt:**

> Use found-item-notes.md and register-fields.md to create lost-property-draft.md. Convert each record into the approved field order while preserving item IDs, dates, and locations. Mark absent information as unknown. Flag similar records for manual comparison without merging them or claiming they describe the same item. Do not identify owners, decide entitlement, set retention periods, or arrange returns. Keep all eight records below 600 words.

**Validation / approval:** Verify original details and ensure every source record remains separately traceable. An authorized property custodian must approve before updating the live register, contacting anyone, or releasing an item.

<a id="uc-186"></a>
## 186. Special request training dialogues.

**Mode:** `swarm-ollama`

**Inputs:** `service-boundaries.md` - approved fictional policy for late checkout and room preferences; `request-cases.md` - four synthetic guest requests.

**Outputs:** `request-dialogues.md` - four short role-play exchanges with policy reference notes.

**Starter prompt:**

> Create request-dialogues.md using service-boundaries.md and request-cases.md. Write a brief practice exchange for each case that acknowledges the request, states the approved boundary, and asks any required clarification. Preserve distinctions between an available option and an option requiring staff authorization. Cite the relevant policy passage after each dialogue. Do not promise availability, waive fees, issue refunds, or change reservations. Stay below 600 words.

**Validation / approval:** Check every offered option and stated boundary against the policy. A guest services manager must approve before training use or adapting any dialogue for a real guest interaction.

<a id="uc-187"></a>
## 187. Audio tour script length review.

**Mode:** `swarm-ollama-claude`

**Inputs:** `tour-script.md` - approved fictional narration for three attraction stops; `segment-limits.md` - editorial word limits and facts that must be retained.

**Outputs:** `tour-script-review.md` - proposed shortened segments and a factual preservation checklist.

**Starter prompt:**

> Use tour-script.md and segment-limits.md to prepare tour-script-review.md. Shorten only segments exceeding their editorial word limits and preserve every listed required fact. Keep stop IDs and distinguish proposed narration from review notes. Do not invent anecdotes, access directions, or historical claims. Explain any limit that cannot be met without dropping required information. Treat word limits as editorial targets, not guaranteed speaking durations. Stay below 600 words.

**Validation / approval:** Independently count words and compare retained facts. A tour editor must approve before recording or publishing; a human read-through establishes actual narration timing.

<a id="uc-188"></a>
## 188. Banquet place card proofing.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `seating-record.md` - an approved synthetic table assignment list; `card-text.md` - draft text for twelve fictional place cards with guest IDs.

**Outputs:** `place-card-proof.md` - exact spelling, duplication, omission, and table-label discrepancies.

**Starter prompt:**

> Compare card-text.md with seating-record.md and produce place-card-proof.md. Check the twelve fictional guest IDs, display names, and table labels exactly as supplied. Report missing cards, duplicate IDs, and mismatched wording in a compact table. Keep unresolved source conflicts as questions. Do not reseat guests, infer relationships, add titles, or include dietary assumptions. Limit the proofing report to 450 words.

**Validation / approval:** Verify every discrepancy character for character and confirm all source IDs were considered. An event host must approve before printing cards, changing assignments, or sharing the seating list with venue staff.

<a id="uc-189"></a>
## 189. Itinerary promise audit.

**Mode:** `swarm-gpt`

**Inputs:** `package-description.md` - fictional visitor package copy; `included-services.md` - approved synthetic inclusions, exclusions, and conditional service notes.

**Outputs:** `itinerary-promises.md` - a promise-to-source matrix with proposed factual corrections.

**Starter prompt:**

> Read package-description.md and included-services.md to draft itinerary-promises.md. Extract up to ten service promises and compare each with the approved inclusions, exclusions, and conditions. Flag language that turns a conditional feature into a guarantee. Suggest corrected wording only when the source resolves the issue. Do not propose destinations, check availability, change prices, or make reservations. Keep the matrix below 600 words.

**Validation / approval:** Check each promise and its qualifier against the approved service record. A package owner must approve before changing sales material or communicating inclusions to guests or suppliers.

<a id="uc-190"></a>
## 190. Room status handover chronology.

**Mode:** `swarm-claude`

**Inputs:** `status-sequence.md` - approved fictional status definitions and transition descriptions; `handover-log.md` - eight synthetic timestamped room-status messages.

**Outputs:** `handover-chronology.md` - a room-by-room chronology with missing events and conflicting timestamps flagged.

**Starter prompt:**

> Use status-sequence.md and handover-log.md to create handover-chronology.md. Order each room's recorded events by timestamp, preserving message IDs. Quote the approved transition description where applicable and flag absent intermediate events or conflicting times as questions. Do not infer that missing events occurred, decide room readiness, create cleaning procedures, or change live statuses. Keep all eight messages traceable and stay below 600 words.

**Validation / approval:** Verify timestamps and every transition reference without treating a record gap as an operational failure. A housekeeping manager must approve before incorporating the chronology into records or changing any room status.

[Back to library](README.md)
