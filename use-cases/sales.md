# Sales.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

These examples prepare bounded sales drafts from synthetic facts supplied by a human. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each run stages one short text artifact; it cannot research accounts, access a CRM or contact prospects. Modes illustrate supported configurations without claiming comparative quality.

- [011. Discovery question path](#uc-011)
- [012. Account conversation brief](#uc-012)
- [013. Meeting follow-up email](#uc-013)
- [014. Proposal scope boundaries](#uc-014)
- [015. Objection response cards](#uc-015)
- [016. Qualification evidence scorecard](#uc-016)
- [017. Mutual action plan](#uc-017)
- [018. RFP response gap matrix](#uc-018)
- [019. Buying committee coverage](#uc-019)
- [020. Sales-to-delivery handoff](#uc-020)

<a id="uc-011"></a>
## 011. Discovery question path.

**Mode:** `swarm-ollama-claude`

**Inputs:** `discovery-context.md` - one fictional prospect's stated problem, known workflow, meeting length and unresolved commercial questions.

**Outputs:** `discovery-guide.md` - a prioritized question sequence with optional follow-ups and a closing recap.

**Starter prompt:**

> Use only discovery-context.md to create discovery-guide.md, under 350 words. Draft six neutral questions for the stated meeting length. For each, explain the decision it informs and add at most one conditional follow-up. Start with the prospect's stated workflow and avoid leading questions that assume a product fit. End with a proposed recap that invites correction. Keep unknown budget and authority explicitly unknown.

**Validation / approval:** Check that questions resolve different uncertainties and fit the time available. A human salesperson must approve the guide before using it in a prospect conversation or sharing it externally.

<a id="uc-012"></a>
## 012. Account conversation brief.

**Mode:** `swarm-gpt`

**Inputs:** `account-extract.md` - a short synthetic company profile; `product-fit.md` - approved capabilities and known limitations relevant to that profile.

**Outputs:** `account-brief.md` - known facts, three tentative fit hypotheses and questions to verify them.

**Starter prompt:**

> Use only account-extract.md and product-fit.md to write account-brief.md, under 400 words. Summarize the fictional account's documented operating context, then propose three capability-to-need hypotheses. Label each hypothesis as unconfirmed and pair it with a verification question. Include any visible mismatch with product limitations. Do not research the company, infer individual motives or fabricate current projects, technology usage or buying intent.

**Validation / approval:** Trace account facts to the extract and distinguish stated needs from guesses. A human account owner must approve the brief before using its claims in outreach, meetings or CRM updates.

<a id="uc-013"></a>
## 013. Meeting follow-up email.

**Mode:** `swarm-ollama`

**Inputs:** `meeting-notes.md` - synthetic call notes listing agreed points, open questions, role-based action owners and any confirmed dates.

**Outputs:** `follow-up-email.md` - a subject and one concise message recapping only documented agreements.

**Starter prompt:**

> Use only meeting-notes.md to draft follow-up-email.md, under 260 words. Separate confirmed agreements from items needing confirmation. Include the next step, its supplied owner role and any confirmed date. Mark missing recipients or dates with clear placeholders. Keep the tone helpful and direct. Do not turn a tentative idea into a commitment or invent attachments, meeting links, prices or delivery promises.

**Validation / approval:** Match every action and date to the notes and check placeholders are resolved. A human account owner must approve the wording, recipient and commitments before sending the message.

<a id="uc-014"></a>
## 014. Proposal scope boundaries.

**Mode:** `swarm-claude`

**Inputs:** `scope-request.md` - a fictional buyer's requested outcomes; `delivery-catalog.md` - a concise list of supported deliverables, exclusions and dependencies.

**Outputs:** `proposal-scope.md` - a draft scope table with included work, excluded work and unresolved requests.

**Starter prompt:**

> Use only scope-request.md and delivery-catalog.md to create proposal-scope.md, under 450 words. Map each requested outcome to supported deliverables or an explicit gap. State customer dependencies and acceptance evidence where supplied. Keep exclusions visible and label any proposed clarification as unresolved. Do not set prices, invent staffing, promise dates or create contract terms. This is a discussion draft for scope review.

**Validation / approval:** Confirm every requested outcome has a disposition and no deliverable exceeds the catalog. Human sales and delivery owners must approve scope before it enters a customer proposal or contractual discussion.

<a id="uc-015"></a>
## 015. Objection response cards.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `objection-notes.md` - four synthetic objections, approved product evidence and limits on competitive or outcome claims.

**Outputs:** `objection-cards.md` - four short response cards with acknowledgment, evidence and a clarifying question.

**Starter prompt:**

> Use only objection-notes.md to write objection-cards.md, under 400 words. Create one card per objection with a neutral acknowledgment, an evidence-backed response and a question that checks the underlying concern. If the supplied evidence cannot answer an objection, say what needs verification. Respect all claim limits. Avoid pressure tactics, invented customer stories, competitor speculation and guarantees about savings or business outcomes.

**Validation / approval:** Check that responses address different concerns and evidence supports each factual claim. A human sales enablement owner must approve the cards before distribution or use in customer conversations.

<a id="uc-016"></a>
## 016. Qualification evidence scorecard.

**Mode:** `swarm-gpt`

**Inputs:** `qualification-rules.md` - four explicit fictional qualification criteria; `opportunity-notes.md` - short synthetic notes relevant to those criteria.

**Outputs:** `qualification-scorecard.md` - evidence, status and missing information for each criterion.

**Starter prompt:**

> Use only qualification-rules.md and opportunity-notes.md to create qualification-scorecard.md, under 350 words. Apply the supplied criteria without changing their definitions or weights. Mark each as met, unmet or unknown, citing a short source phrase or note label. Distinguish absent evidence from negative evidence. List three questions that would resolve important unknowns. Do not estimate win probability or recommend rejecting a person.

**Validation / approval:** Independently compare criterion assignments with the supplied notes and check unknowns remain visible. A human opportunity owner must approve the assessment before changing a CRM stage or communicating qualification decisions externally.

<a id="uc-017"></a>
## 017. Mutual action plan.

**Mode:** `swarm-ollama-claude`

**Inputs:** `buying-steps.md` - six fictional decision steps, dependencies, owner roles and any dates agreed by both sides.

**Outputs:** `mutual-plan.md` - a proposed milestone table separating agreed actions from items awaiting agreement.

**Starter prompt:**

> Use only buying-steps.md to create mutual-plan.md, under 400 words. Arrange the steps by dependency and show owner role, completion evidence and confirmed date where available. Mark missing dates as undecided. Label each milestone agreed or proposed based on the input, and highlight contradictory dependencies. Do not create new obligations, book meetings or assume customer acceptance. Keep the plan limited to these six steps.

**Validation / approval:** Check dependency order, date consistency and the distinction between agreed and proposed milestones. A human account owner must approve the draft before sharing; customer agreement is required before proposed milestones become commitments.

<a id="uc-018"></a>
## 018. RFP response gap matrix.

**Mode:** `swarm-claude`

**Inputs:** `rfp-extract.md` - six synthetic requirements with identifiers; `capability-extract.md` - concise approved product statements relevant to those requirements.

**Outputs:** `rfp-gap-matrix.md` - requirement coverage, supporting facts and questions for responsible reviewers.

**Starter prompt:**

> Use only rfp-extract.md and capability-extract.md to write rfp-gap-matrix.md, under 450 words. Preserve all six requirement identifiers. Mark each supported, partially supported or unanswered, then quote or reference the relevant supplied fact. Flag requirements needing security, legal or technical verification. Do not infer certifications, compliance, integrations or contractual guarantees. Draft limited response wording only where the input provides direct support.

**Validation / approval:** Check complete requirement coverage and ensure partial support is never presented as full compliance. Human subject owners and the bid owner must approve responses before submission or inclusion in a customer commitment.

<a id="uc-019"></a>
## 019. Buying committee coverage.

**Mode:** `swarm-ollama`

**Inputs:** `committee-notes.md` - a fictional deal's documented participant roles, stated concerns and decision process, with names omitted.

**Outputs:** `committee-coverage.md` - a role-to-question map identifying confirmed involvement and unresolved coverage gaps.

**Starter prompt:**

> Use only committee-notes.md to create committee-coverage.md, under 350 words. Map supplied roles to their documented concerns and decision responsibilities. Distinguish confirmed authority from assumptions. Identify up to three gaps in understanding the buying process and propose respectful questions for the existing contact. Do not infer influence from job titles alone, invent participants or draft unsolicited contact sequences. Keep all references at role level.

**Validation / approval:** Verify role responsibilities against notes and ensure uncertainty is explicit. A human account owner must approve the map before adding it to a CRM, sharing it with a prospect or changing contact plans.

<a id="uc-020"></a>
## 020. Sales-to-delivery handoff.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `deal-summary.md` - synthetic agreed scope, success criteria and constraints; `open-items.md` - five unresolved questions with owner roles.

**Outputs:** `delivery-handoff.md` - a concise handoff separating commitments, assumptions and items needing resolution.

**Starter prompt:**

> Use only deal-summary.md and open-items.md to create delivery-handoff.md, under 450 words. Summarize agreed outcomes, deliverables, customer dependencies and explicit exclusions. Preserve each unresolved item's owner and flag any conflict with agreed scope. Add a short kickoff checklist using only these facts. Do not infer contract acceptance, invent implementation dates or treat sales aspirations as promised outcomes. Keep missing information visible.

**Validation / approval:** Compare commitments with the supplied summary and account for all open items. Human sales and delivery owners must approve the handoff before sharing it with a customer or creating delivery commitments from it.

[Back to library](README.md)
