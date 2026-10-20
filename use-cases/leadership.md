# Leadership.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare decision support and governance drafts from fictional organizational examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each output is a short text artifact staged privately, with decisions and communications reserved for authorized people. Mode choices illustrate configurations, not performance claims or guaranteed local data processing.

- [141. Strategic option comparison](#uc-141)
- [142. Board pre-read outline](#uc-142)
- [143. Decision record](#uc-143)
- [144. Objective coherence review](#uc-144)
- [145. Stakeholder impact map](#uc-145)
- [146. Strategic risk challenge questions](#uc-146)
- [147. Delegation charter](#uc-147)
- [148. Town hall question brief](#uc-148)
- [149. Cross-team dependency brief](#uc-149)
- [150. Leadership transition briefing](#uc-150)

<a id="uc-141"></a>
## 141. Strategic option comparison.

**Mode:** `swarm-claude`

**Inputs:** `strategy-options.md` - three fictional alternatives with stated benefits, costs and uncertainties; `decision-criteria.md` - approved objectives, constraints and criteria without invented weights.

**Outputs:** `strategy-comparison.md` - a concise comparison separating source-supported tradeoffs from missing evidence.

**Starter prompt:**

> Use strategy-options.md and decision-criteria.md to draft strategy-comparison.md, under 600 words. Compare the three supplied alternatives against each stated criterion. Cite option labels, retain uncertainty and identify evidence needed before choosing. Flag incompatible assumptions rather than resolving them by invention. Do not score alternatives without supplied rules, select a strategy or commit resources.

**Validation / approval:** Verify every tradeoff against the source and have qualified owners check cost assumptions. The authorized leadership group approves any strategy, resource allocation or communication after reviewing the underlying evidence.

<a id="uc-142"></a>
## 142. Board pre-read outline.

**Mode:** `swarm-gpt`

**Inputs:** `board-topics.md` - a fictional meeting's requested topics, decision items and governance boundaries; `status-extract.md` - synthetic approved facts, dated measures and labeled uncertainties.

**Outputs:** `board-preread-outline.md` - an outline organizing evidence, decision requests and open questions for a short pre-read.

**Starter prompt:**

> Draft board-preread-outline.md from board-topics.md and status-extract.md in at most 550 words. Organize sections around the supplied topics and distinguish information items from decisions requested. Attach source labels to factual bullets and flag unsupported claims. Preserve dates and uncertainty. Do not invent financial results, governance conclusions or recommendations beyond the provided material.

**Validation / approval:** The responsible fact owners verify every claim and decision request. An authorized governance reviewer approves the outline and resulting pre-read before board distribution or inclusion in formal records.

<a id="uc-143"></a>
## 143. Decision record.

**Mode:** `swarm-ollama`

**Inputs:** `decision-notes.md` - a fictional meeting extract with a clearly stated decision and rationale; `record-standard.md` - generic fields for authority, alternatives, conditions and review triggers.

**Outputs:** `decision-record.md` - a draft record distinguishing the agreed decision from discussion and unresolved follow-up.

**Starter prompt:**

> Create decision-record.md from decision-notes.md and record-standard.md, under 500 words. Record only the explicitly stated decision, supporting rationale, considered alternatives and supplied conditions. Attribute roles as given and mark missing authority or dates. Keep discussion points separate from commitments. Do not invent consensus, convert suggestions into approvals or alter the decision.

**Validation / approval:** Participants verify the decision, rationale and conditions against the original record. The authorized decision owner approves the final wording before it becomes an official record or triggers implementation.

<a id="uc-144"></a>
## 144. Objective coherence review.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `leadership-objectives.md` - four fictional organizational objectives with horizons and stated priorities; `measure-map.md` - synthetic proposed measures, definitions and objective links.

**Outputs:** `objective-coherence.md` - a short review of missing links, conflicting horizons and ambiguous success definitions.

**Starter prompt:**

> Use leadership-objectives.md and measure-map.md to draft objective-coherence.md, under 550 words. Trace each proposed measure to its stated objective. Identify unmeasured objectives, mismatched time horizons and definitions that could obscure progress. Cite source IDs and ask clarification questions. Do not invent targets, weight priorities, change strategy or evaluate individual employee performance.

**Validation / approval:** Objective owners verify the mappings and a qualified measurement owner checks definitions. Authorized leadership approves any target, measure or priority change before adoption or inclusion in organizational reporting.

<a id="uc-145"></a>
## 145. Stakeholder impact map.

**Mode:** `swarm-claude`

**Inputs:** `initiative-summary.md` - a fictional operational initiative with proposed changes and boundaries; `stakeholder-roles.md` - generic role groups, documented responsibilities and known dependencies.

**Outputs:** `stakeholder-impact.md` - a role-based impact table with consultation questions and evidence gaps.

**Starter prompt:**

> Create stakeholder-impact.md using initiative-summary.md and stakeholder-roles.md in at most 550 words. Map proposed changes to documented responsibilities and identify possible workflow impacts as hypotheses. Suggest neutral consultation questions for affected role groups. Distinguish known dependencies from assumed reactions. Do not infer personal attitudes, protected traits or consent, and do not contact anyone.

**Validation / approval:** Role representatives verify responsibilities and challenge inferred impacts. The initiative owner approves the map and consultation approach before outreach, while employment or policy changes require the appropriate qualified human review.

<a id="uc-146"></a>
## 146. Strategic risk challenge questions.

**Mode:** `swarm-gpt`

**Inputs:** `risk-register-example.md` - five synthetic strategic risks with supplied owners and controls; `planning-assumptions.md` - a fictional strategy's stated dependencies and uncertainty boundaries.

**Outputs:** `risk-challenge-questions.md` - a review sheet testing assumptions, control evidence and missing ownership.

**Starter prompt:**

> Use risk-register-example.md and planning-assumptions.md to produce risk-challenge-questions.md, under 550 words. Draft focused questions about each risk's assumption, existing control, evidence of operation and escalation role. Identify unaddressed dependencies. Keep source ratings unchanged and flag missing support. Do not estimate probabilities, certify control effectiveness, accept risk or prescribe operational actions.

**Validation / approval:** Qualified risk owners verify the questions and underlying evidence. The authorized risk committee or accountable leader approves any rating changes, acceptance decisions or control actions after its own assessment.

<a id="uc-147"></a>
## 147. Delegation charter.

**Mode:** `swarm-ollama-claude`

**Inputs:** `team-mandate.md` - a fictional team's purpose, responsibilities and dependencies; `authority-boundaries.md` - generic reserved decisions, escalation conditions and existing approval roles.

**Outputs:** `delegation-charter.md` - a draft charter distinguishing permitted responsibilities from decisions requiring approval.

**Starter prompt:**

> Draft delegation-charter.md from team-mandate.md and authority-boundaries.md, under 550 words. State the supplied purpose, responsibility boundaries, reserved decisions and escalation triggers. Flag overlaps or gaps between the two sources. Use role names only and leave missing authority unresolved. Do not grant new powers, change access rights or assign obligations to real people.

**Validation / approval:** Responsible leaders verify boundaries and any policy implications with qualified governance reviewers. The authorized delegating officer approves the charter before distribution, and separate permission changes require their own approved process.

<a id="uc-148"></a>
## 148. Town hall question brief.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `sample-questions.md` - eight synthetic workforce questions without personal cases; `approved-announcement.md` - fictional approved messages, confirmed facts and topics awaiting decisions.

**Outputs:** `townhall-question-brief.md` - grouped themes, draft factual answers and questions requiring an authorized response.

**Starter prompt:**

> Use sample-questions.md and approved-announcement.md to create townhall-question-brief.md, under 600 words. Group related questions without dropping distinct concerns. Answer only from approved facts and mark unresolved topics for the relevant supplied role. Retain uncertainty and avoid promises about staffing, compensation or timing. Do not infer employee sentiment or distribute the brief.

**Validation / approval:** Communications and qualified HR reviewers verify factual boundaries and sensitive topics. The authorized speaker approves answers before the event or publication; unanswered questions stay open until an accountable owner responds.

<a id="uc-149"></a>
## 149. Cross-team dependency brief.

**Mode:** `swarm-claude`

**Inputs:** `team-a-plan.md` - a fictional team's deliverables, dates and requested inputs; `team-b-plan.md` - another fictional team's commitments, assumptions and shared interface responsibilities.

**Outputs:** `dependency-brief.md` - a short interface comparison with conflicting assumptions and resolution questions.

**Starter prompt:**

> Create dependency-brief.md from team-a-plan.md and team-b-plan.md, under 550 words. Identify dependencies explicitly described in either plan and compare dates, deliverable definitions and role responsibilities. Cite plan labels and flag one-sided assumptions. Draft questions to resolve conflicts without inventing commitments. Do not reschedule work, assign staff, contact teams or declare a dependency resolved.

**Validation / approval:** Both team owners verify interfaces and distinguish requested inputs from accepted commitments. The accountable sponsor approves any priority, scope or timeline change before plans are updated or communicated.

<a id="uc-150"></a>
## 150. Leadership transition briefing.

**Mode:** `swarm-gpt`

**Inputs:** `leadership-mandate.md` - a fictional leadership role's governance responsibilities and reserved decisions; `transition-notes.md` - synthetic open decisions, dated obligations and referenced document labels.

**Outputs:** `transition-briefing.md` - a concise briefing organizing governance obligations, unresolved decisions and verification questions.

**Starter prompt:**

> Use leadership-mandate.md and transition-notes.md to draft transition-briefing.md, under 600 words. Separate standing responsibilities from dated obligations and open decisions. Cite source labels, preserve known owners and identify missing authority or evidence. Include questions for the incoming leader. Do not infer succession outcomes, disclose personnel assessments, transfer authority or treat proposed commitments as approved.

**Validation / approval:** The outgoing role owner and qualified governance reviewer verify obligations, authority and confidentiality. The authorized sponsor approves the briefing before sharing or making any delegation, personnel or commitment changes.

[Back to library](README.md)
