# Operations.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Turn small operational extracts into checklists and review briefs. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Outputs are short text drafts staged privately for inspection. Modes are illustrative; confirm provider routing and any Ollama model's locality before supplying authorized information.

- [101. Shift handover brief](#uc-101)
- [102. Process exception triage guide](#uc-102)
- [103. Request intake checklist](#uc-103)
- [104. Service escalation matrix](#uc-104)
- [105. Goods receiving checklist](#uc-105)
- [106. Facility opening and closing checklist](#uc-106)
- [107. Backlog aging review](#uc-107)
- [108. Recurring defect investigation worksheet](#uc-108)
- [109. Continuity tabletop exercise](#uc-109)
- [110. Process change readiness checklist](#uc-110)

<a id="uc-101"></a>
## 101. Shift handover brief.

**Mode:** `swarm-ollama`

**Inputs:** `shift-notes.md` - eight synthetic events with timestamps, status and role owners; `handover-rules.md` - required handover fields and escalation thresholds.

**Outputs:** `handover-brief.md` - a one-page handover with completed work, open actions and unresolved questions.

**Starter prompt:**

> Use shift-notes.md and handover-rules.md to draft handover-brief.md, under 450 words. Preserve timestamps and supplied role owners. Separate completed events from pending actions, flag missing ownership and cite event labels. Highlight threshold breaches without inventing resolution steps. Produce only a draft for the incoming shift lead.

**Validation / approval:** Check every event against the source, confirm open actions remain open and resolve ambiguous times. The outgoing and incoming leads approve the brief before distributing it or acting on escalations.

<a id="uc-102"></a>
## 102. Process exception triage guide.

**Mode:** `swarm-ollama-claude`

**Inputs:** `process-extract.md` - one generic procedure, permitted exceptions and stop conditions; `exception-cases.md` - five fictional deviations labeled by case.

**Outputs:** `exception-guide.md` - a compact table of applicable procedure steps, missing evidence and review routes.

**Starter prompt:**

> Draft exception-guide.md from process-extract.md and exception-cases.md. For each fictional case, identify the relevant procedure clause, questions needed to classify it and the supplied escalation role. Keep the guide under 550 words. Mark unaddressed cases as unresolved; do not invent permissions, waive controls or authorize work to resume.

**Validation / approval:** Verify clause references, stop conditions and role names. A process owner must approve the guidance before anyone changes an exception route or resumes work affected by a stop condition.

<a id="uc-103"></a>
## 103. Request intake checklist.

**Mode:** `swarm-gpt`

**Inputs:** `request-types.md` - three generic service request types with mandatory fields; `sample-requests.md` - six synthetic submissions with deliberate omissions.

**Outputs:** `intake-checklist.md` - reusable completeness checks plus a labeled illustration for each sample.

**Starter prompt:**

> Use request-types.md and sample-requests.md to produce intake-checklist.md, under 550 words. Separate universal checks from request-specific requirements. Show which required fields are absent in each sample and draft one neutral clarification question per incomplete submission. Treat completeness separately from eligibility or approval. Do not infer missing answers or contact requesters.

**Validation / approval:** Confirm every requested field exists in the supplied requirements and each omission is real. The intake owner approves the checklist and any clarification wording before changing a form or contacting a requester.

<a id="uc-104"></a>
## 104. Service escalation matrix.

**Mode:** `swarm-claude`

**Inputs:** `service-commitments.md` - fictional severity definitions and response targets; `coverage-roles.md` - generic ownership, coverage windows and fallback roles.

**Outputs:** `escalation-matrix.md` - a draft severity-to-role matrix with unanswered coverage questions.

**Starter prompt:**

> Create escalation-matrix.md from service-commitments.md and coverage-roles.md. In at most 500 words, map each supplied severity to its trigger, response target, primary role and documented fallback. Preserve the given time zone and distinguish response from resolution. Flag gaps and conflicting ownership instead of assigning new authority. Do not dispatch any escalation.

**Validation / approval:** Reconcile targets, coverage boundaries and fallback availability with the sources. The service owner approves all authority and coverage choices before publishing the matrix or using it in an active incident.

<a id="uc-105"></a>
## 105. Goods receiving checklist.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `receiving-procedure.md` - a generic nonhazardous goods procedure and discrepancy rules; `delivery-example.md` - a synthetic delivery note with item IDs, quantities and packaging observations.

**Outputs:** `receiving-checklist.md` - a one-page inspection checklist with sample discrepancy flags.

**Starter prompt:**

> Use receiving-procedure.md and delivery-example.md to write receiving-checklist.md, under 500 words. Cover identification, quantity confirmation, visible packaging observations and required records using only supplied steps. Link example flags to item IDs. Leave physical condition and counts unverified until a person checks them. Do not accept delivery or update inventory.

**Validation / approval:** Check item identifiers and procedure order. An authorized receiving supervisor approves the checklist; a trained person performs inspections and approves acceptance, rejection or inventory changes.

<a id="uc-106"></a>
## 106. Facility opening and closing checklist.

**Mode:** `swarm-ollama`

**Inputs:** `site-routine.md` - a generic office opening and closing routine without security secrets; `site-constraints.md` - fictional operating hours, accessibility needs and approved safety steps.

**Outputs:** `facility-checklist.md` - two short checklists with completion boxes and unresolved prerequisites.

**Starter prompt:**

> Draft facility-checklist.md from site-routine.md and site-constraints.md, under 500 words. Separate opening and closing steps, preserve required ordering and mark checks requiring a trained person. Include blanks for completion time and role. Surface conflicts or missing prerequisites. Do not invent safety procedures, access codes or instructions to bypass a control.

**Validation / approval:** Confirm ordering, accessibility provisions and safety references with the supplied material. The facilities and safety owners approve the checklist before it is issued or used on site.

<a id="uc-107"></a>
## 107. Backlog aging review.

**Mode:** `swarm-gpt`

**Inputs:** `backlog-snapshot.md` - ten synthetic work items with supplied age bands, status and blockers; `queue-rules.md` - generic service priorities and aging review thresholds.

**Outputs:** `aging-review.md` - a short review brief grouping items by documented aging concern.

**Starter prompt:**

> Use backlog-snapshot.md and queue-rules.md to draft aging-review.md in at most 500 words. Identify items meeting the supplied aging thresholds, distinguish blocked work from awaiting-review work and cite item IDs. Propose questions for a queue review, preserving unknown causes. Do not recalculate dates, change priorities or assign work to individuals.

**Validation / approval:** Verify threshold membership and source statuses; check dates independently if the snapshot is reused. The queue owner approves any priority, assignment or customer communication arising from the review.

<a id="uc-108"></a>
## 108. Recurring defect investigation worksheet.

**Mode:** `swarm-ollama-claude`

**Inputs:** `defect-examples.md` - six synthetic defects with process stage and observation labels; `process-map.md` - a short generic process and available inspection evidence.

**Outputs:** `defect-investigation.md` - a hypothesis worksheet connecting observed patterns to evidence needed.

**Starter prompt:**

> Create defect-investigation.md from defect-examples.md and process-map.md, under 550 words. Group only visibly similar observations. For each group, propose a clearly labeled hypothesis, an alternative explanation and evidence that would distinguish them. Cite defect labels. Separate facts from hypotheses and avoid declaring a root cause, blaming people or prescribing unapproved process changes.

**Validation / approval:** Check each grouping against source observations and ensure hypotheses remain tentative. A quality owner approves the investigation plan before collecting further evidence or changing the process.

<a id="uc-109"></a>
## 109. Continuity tabletop exercise.

**Mode:** `swarm-claude`

**Inputs:** `continuity-extract.md` - a fictional continuity plan with roles and activation rules; `dependency-summary.md` - three generic service dependencies and known fallback assumptions.

**Outputs:** `tabletop-exercise.md` - a facilitator sheet with one scenario, three timed discussion prompts and observation fields.

**Starter prompt:**

> Use continuity-extract.md and dependency-summary.md to draft tabletop-exercise.md, under 600 words. Build one clearly fictional disruption scenario and three discussion stages testing supplied assumptions. Identify expected decision roles and unanswered fallback questions. Include a short debrief. Keep every action simulated; do not activate a plan, contact providers or issue operational instructions.

**Validation / approval:** Verify the scenario matches stated dependencies and does not reveal sensitive infrastructure. The continuity owner approves the exercise and any invitations before scheduling or conducting it.

<a id="uc-110"></a>
## 110. Process change readiness checklist.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `change-proposal.md` - a fictional process change, affected roles and proposed start date; `readiness-criteria.md` - approved training, ownership, documentation and fallback requirements.

**Outputs:** `change-readiness.md` - a checklist showing supplied evidence, missing proof and approval dependencies.

**Starter prompt:**

> Draft change-readiness.md from change-proposal.md and readiness-criteria.md in at most 550 words. Map each readiness requirement to supplied evidence or an explicit gap. Include proposed questions for the change review and identify approval roles already named in the inputs. Do not treat a proposed date as authorization or declare the change ready to launch.

**Validation / approval:** Verify evidence references and distinguish proposed work from completed prerequisites. The process owner and named approvers confirm readiness before announcing a date or implementing the change.

[Back to library](README.md)
