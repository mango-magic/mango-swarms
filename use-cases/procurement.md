# Procurement.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare sourcing drafts and evidence checks using fictional suppliers and generic purchasing requirements. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each result is short text staged for human review, without supplier contact or purchasing authority. Modes are examples; verify provider routing rather than assuming a mode guarantees local processing.

- [131. Purchase specification brief](#uc-131)
- [132. Supplier diligence questionnaire](#uc-132)
- [133. Quote comparison worksheet](#uc-133)
- [134. Service milestone acceptance criteria](#uc-134)
- [135. Contract renewal questions](#uc-135)
- [136. Supplier onboarding evidence checklist](#uc-136)
- [137. Sourcing exception justification draft](#uc-137)
- [138. Supplier performance discussion brief](#uc-138)
- [139. Delivery exception clarification draft](#uc-139)
- [140. Sustainability claim evidence checklist](#uc-140)

<a id="uc-131"></a>
## 131. Purchase specification brief.

**Mode:** `swarm-gpt`

**Inputs:** `purchase-need.md` - a fictional need for nonhazardous office equipment and intended use; `purchase-constraints.md` - generic quantity, compatibility, accessibility and delivery requirements.

**Outputs:** `purchase-specification.md` - a concise specification separating mandatory attributes, preferences and open questions.

**Starter prompt:**

> Use purchase-need.md and purchase-constraints.md to draft purchase-specification.md, under 550 words. Convert supplied needs into observable requirements without adding brands or unprovided technical thresholds. Separate mandatory attributes from preferences and identify missing acceptance details. Preserve quantities and deadlines as supplied. Do not research products, select a supplier or place an order.

**Validation / approval:** Verify each requirement against its source and confirm compatibility with a qualified requester. The budget owner and procurement lead approve the specification before soliciting quotes or committing funds.

<a id="uc-132"></a>
## 132. Supplier diligence questionnaire.

**Mode:** `swarm-ollama-claude`

**Inputs:** `supplier-scope.md` - a fictional service scope and dependencies; `diligence-requirements.md` - generic evidence requirements covering delivery capability, continuity and relevant controls.

**Outputs:** `supplier-questionnaire.md` - a short questionnaire linking each question to a stated diligence requirement.

**Starter prompt:**

> Create supplier-questionnaire.md from supplier-scope.md and diligence-requirements.md, under 600 words. Draft at most ten questions, specifying the evidence type requested and why it relates to the supplied scope. Distinguish mandatory evidence from clarification. Avoid requesting credentials, personal data or irrelevant confidential material. Do not assess a real supplier or send the questionnaire.

**Validation / approval:** Confirm every question traces to an authorized requirement and evidence requests are proportionate. Procurement and relevant qualified control owners approve the questionnaire and recipient before external use.

<a id="uc-133"></a>
## 133. Quote comparison worksheet.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `quote-examples.md` - three synthetic quotes with stated totals, currencies, scope and exclusions; `comparison-criteria.md` - generic required attributes and approved comparison categories.

**Outputs:** `quote-comparison.md` - a source-labeled comparison table with gaps that prevent a fair comparison.

**Starter prompt:**

> Draft quote-comparison.md using quote-examples.md and comparison-criteria.md, under 600 words. Compare stated scope, terms, exclusions and precomputed totals. Preserve currencies and distinguish unknown values from zero. Flag differing units or assumptions without recalculating prices or inventing equivalence. Do not score suppliers, select a winner, negotiate terms or approve spending.

**Validation / approval:** An authorized procurement reviewer checks every quote value and independently normalizes any monetary comparison. The responsible decision and budget owners approve supplier selection and commitments through their existing purchasing process.

<a id="uc-134"></a>
## 134. Service milestone acceptance criteria.

**Mode:** `swarm-claude`

**Inputs:** `service-scope.md` - a fictional service engagement with three deliverables and boundaries; `acceptance-notes.md` - requester-approved quality expectations and evidence types.

**Outputs:** `acceptance-criteria.md` - draft milestone checks with observable evidence and unresolved ambiguities.

**Starter prompt:**

> Use service-scope.md and acceptance-notes.md to produce acceptance-criteria.md, under 550 words. For each supplied deliverable, draft a review question, expected evidence and acceptance role if provided. Separate measurable requirements from subjective preferences. Flag missing thresholds without inventing contractual terms. Do not accept work, release payment or claim the wording is legally sufficient.

**Validation / approval:** The qualified service owner checks feasibility and evidence requirements. Procurement and authorized legal reviewers approve any contractual wording before incorporation into an agreement; acceptance and payment remain separate human approvals.

<a id="uc-135"></a>
## 135. Contract renewal questions.

**Mode:** `swarm-gpt`

**Inputs:** `renewal-extract.md` - a fictional agreement excerpt with labeled renewal and notice clauses; `service-review.md` - synthetic usage concerns, owner questions and stated future needs.

**Outputs:** `renewal-review-questions.md` - a short review sheet connecting contractual uncertainties to business questions.

**Starter prompt:**

> Create renewal-review-questions.md from renewal-extract.md and service-review.md, under 550 words. Preserve quoted dates and clause labels, and list questions about notice requirements, future scope and unresolved service concerns. Distinguish source wording from interpretation. Do not calculate a legally effective deadline, recommend renewal or termination, send notice or offer legal advice.

**Validation / approval:** Authorized procurement and qualified legal reviewers verify the complete agreement, applicable dates and interpretation. The contract owner approves any supplier communication, renewal, termination or spending commitment separately.

<a id="uc-136"></a>
## 136. Supplier onboarding evidence checklist.

**Mode:** `swarm-ollama`

**Inputs:** `onboarding-requirements.md` - a generic supplier onboarding policy with required evidence categories; `supplier-example.md` - a fictional inventory of supplied documents and expiry dates, without account numbers.

**Outputs:** `onboarding-evidence.md` - a completeness checklist identifying missing, stale or unclear evidence descriptions.

**Starter prompt:**

> Use onboarding-requirements.md and supplier-example.md to draft onboarding-evidence.md, under 500 words. Match evidence descriptions to stated requirements and flag missing coverage or explicitly expired items. Do not infer document authenticity. Request clarification through role-based questions without asking for passwords or banking secrets. Do not create supplier records, verify accounts or enable payments.

**Validation / approval:** Authorized procurement and finance reviewers inspect original documents through approved channels. They approve the checklist and separately authorize supplier activation or record changes after required checks are complete.

<a id="uc-137"></a>
## 137. Sourcing exception justification draft.

**Mode:** `swarm-ollama-claude`

**Inputs:** `exception-policy.md` - a fictional competitive sourcing policy and exception evidence requirements; `exception-scenario.md` - synthetic requester statements, constraints and documented alternatives considered.

**Outputs:** `sourcing-exception-draft.md` - a structured justification draft with unsupported assertions and missing evidence marked.

**Starter prompt:**

> Draft sourcing-exception-draft.md from exception-policy.md and exception-scenario.md, under 550 words. Organize supplied facts against each exception requirement and identify where evidence is missing or alternatives were not examined. Keep requester assertions labeled as assertions. Do not manufacture urgency, justify circumventing controls, approve the exception or recommend awarding a contract.

**Validation / approval:** The procurement reviewer verifies evidence and checks that the draft accurately records alternatives. The policy's authorized exception approver decides whether an exception is permitted before any sourcing change or commitment.

<a id="uc-138"></a>
## 138. Supplier performance discussion brief.

**Mode:** `swarm-claude`

**Inputs:** `supplier-metrics.md` - six synthetic service measures with periods and precomputed results; `service-targets.md` - fictional agreed targets, exclusions and review topics.

**Outputs:** `supplier-review-brief.md` - a discussion brief separating visible target differences from unanswered explanations.

**Starter prompt:**

> Use supplier-metrics.md and service-targets.md to create supplier-review-brief.md, under 550 words. Compare supplied results with stated targets, retaining periods, units and exclusions. Cite measure IDs and draft neutral questions for unexplained differences. Distinguish missing data from poor performance. Do not infer causes, recalculate penalties, recommend termination or communicate with the supplier.

**Validation / approval:** Procurement and the qualified service owner verify calculations and contractual applicability independently. The relationship owner approves any external discussion brief; remedies, penalties and contract changes require separate authorized review.

<a id="uc-139"></a>
## 139. Delivery exception clarification draft.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `delivery-record.md` - a synthetic order timeline with promised and reported dates, item IDs and observed shortages; `delivery-terms.md` - generic agreed delivery and notification terms.

**Outputs:** `delivery-clarification.md` - a source-based timeline and an unsent clarification request.

**Starter prompt:**

> Create delivery-clarification.md from delivery-record.md and delivery-terms.md, under 500 words. Separate promised dates, reported events and unverified assumptions. Identify missing quantities or timing details and draft a neutral request for clarification using item IDs. Do not allege breach, calculate compensation, accept substitute goods, amend an order or send the request.

**Validation / approval:** The receiving and procurement owners verify counts, dates and terms against original records. An authorized buyer approves any communication or proposed remedy before contacting the supplier or changing the order.

<a id="uc-140"></a>
## 140. Sustainability claim evidence checklist.

**Mode:** `swarm-gpt`

**Inputs:** `supplier-claims.md` - five fictional environmental statements with supplied supporting descriptions; `evidence-standard.md` - an organization-authored checklist of claim scope, period and evidence requirements.

**Outputs:** `claim-evidence-checklist.md` - a claim-by-claim evidence map and neutral clarification questions.

**Starter prompt:**

> Use supplier-claims.md and evidence-standard.md to draft claim-evidence-checklist.md, under 550 words. Identify the scope, period and described support for each claim. Mark unsupported elements and ask what evidence would meet the supplied checklist. Do not validate certifications, infer environmental impact, award sustainability scores or endorse a supplier's claims.

**Validation / approval:** Procurement and a qualified sustainability reviewer verify original evidence and the applicable criteria. Authorized owners approve any supplier assessment or public statement before selection, publication or use of a claim in marketing.

[Back to library](README.md)
