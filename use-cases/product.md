# Product.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Turn a small product question into a decision artifact. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. The modes below are suitable provider arrangements, not performance rankings.

- [051. Problem opportunity brief](#uc-051)
- [052. Acceptance criteria for one story](#uc-052)
- [053. Priority sensitivity review](#uc-053)
- [054. Release scope boundary](#uc-054)
- [055. Feature entitlement matrix](#uc-055)
- [056. Feature retirement transition](#uc-056)
- [057. Instrumentation requirement card](#uc-057)
- [058. Feedback disposition ledger](#uc-058)
- [059. Product decision record](#uc-059)
- [060. Experiment guardrail plan](#uc-060)

<a id="uc-051"></a>
## 051. Problem opportunity brief.

**Mode:** `swarm-ollama-claude`

**Inputs:** `signals.md` - six anonymized workflow observations with IDs; `constraints.md` - target audience, business constraints, and existing alternatives.

**Outputs:** `opportunity.md` - a problem brief with source references and unknowns.

**Starter prompt:**

> Read signals.md and constraints.md. Write only opportunity.md, at most 600 words, for one product opportunity. Separate observed problems, inferred causes, and possible solutions. Reference observation IDs for every evidence claim. Include the affected workflow, current workaround, consequence, and three questions that could invalidate the opportunity. Do not invent market size or customer quotes.

**Validation / approval:** Check every evidence claim against its supplied observation and confirm the brief addresses one audience and workflow. A product owner must approve the interpretation before external use or roadmap discussion.

<a id="uc-052"></a>
## 052. Acceptance criteria for one story.

**Mode:** `swarm-gpt`

**Inputs:** `story.md` - one user story, business rules, and three known edge cases.

**Outputs:** `acceptance.md` - acceptance scenarios and unresolved rule questions.

**Starter prompt:**

> Use story.md to write only acceptance.md. Draft at most ten Given/When/Then scenarios for this story. Cover the normal path and supplied edge cases, adding permission or retry scenarios only where rules define them. Mark missing rules as questions instead of choosing behavior. Map each scenario to a source rule. Do not implement or execute tests.

**Validation / approval:** Confirm every scenario has an observable outcome, follows a stated rule, and avoids adding scope. The product owner and engineer must resolve open rules and approve the scenarios before external use or implementation.

<a id="uc-053"></a>
## 053. Priority sensitivity review.

**Mode:** `swarm-ollama`

**Inputs:** `candidates.csv` - three candidate features with scores and confidence notes; `rubric.md` - the scoring formula and allowed ranges.

**Outputs:** `priority-review.md` - a comparison of ranking sensitivity to uncertain inputs.

**Starter prompt:**

> Read candidates.csv and rubric.md. Write only priority-review.md, within 500 words. Apply the stated formula to all three candidates, showing substitutions for human arithmetic checks. Identify up to two uncertain inputs that can reverse adjacent rankings and describe their breakpoints. Report 'no reversal within supplied ranges' when applicable. Preserve confidence labels and flag missing values instead of estimating them. Recommend one evidence question for each uncertain input.

**Validation / approval:** Independently recompute scores and check breakpoints against allowed ranges. A product owner must approve the assumptions before external use or changing priorities; model review does not verify arithmetic.

<a id="uc-054"></a>
## 054. Release scope boundary.

**Mode:** `swarm-claude`

**Inputs:** `milestone.md` - one release objective and eight candidate capabilities; `limits.md` - confirmed dependencies and delivery constraints.

**Outputs:** `scope-boundary.md` - included, deferred, and unresolved release scope.

**Starter prompt:**

> Using milestone.md and limits.md, write only scope-boundary.md, at most 650 words. Classify each capability as required, deferred, or unresolved for the objective. Explain classifications with source constraints. Identify the smallest coherent user outcome, explicit non-goals, and dependency questions. Do not invent dates, capacity, or capabilities. Keep unresolved decisions visible instead of silently narrowing requirements.

**Validation / approval:** Verify every candidate appears once and that required capabilities form a usable outcome under the listed dependencies. The release owner must approve the boundary before external use or communicating a commitment.

<a id="uc-055"></a>
## 055. Feature entitlement matrix.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `entitlements.md` - rules for three subscription tiers and four features, including downgrade behavior.

**Outputs:** `entitlement-matrix.md` - permissions and transitions with unresolved combinations.

**Starter prompt:**

> Read entitlements.md and write only entitlement-matrix.md. Make a matrix for the supplied tiers and features, then add at most six upgrade or downgrade scenarios. Distinguish viewing existing work, creating work, and exporting it where the rules do. Cite rule IDs, mark unspecified cells unknown, and list contradictions. Stay within twelve tier-feature combinations. Do not change billing or infer prices.

**Validation / approval:** Compare every cell and transition with the source rules, especially access after downgrade. Product and billing owners must approve the matrix before external use or implementing access controls.

<a id="uc-056"></a>
## 056. Feature retirement transition.

**Mode:** `swarm-claude`

**Inputs:** `retirement.md` - one feature, affected workflows, and known alternatives; `requirements.md` - supplied notice, export, and support requirements.

**Outputs:** `transition-plan.md` - a retirement sequence with readiness gates.

**Starter prompt:**

> Use retirement.md and requirements.md to write only transition-plan.md, within 650 words. Propose five stages for retiring the single feature, each with a dependency, owner role, readiness gate, and fallback. Include existing-work access and unresolved migration needs. Use relative milestones unless dates are supplied. Do not write announcements, contact customers, remove functionality, or claim migration has occurred.

**Validation / approval:** Check every requirement has a gate and every affected workflow has an alternative or explicit blocker. Product and support owners must approve the plan before external use or scheduling retirement.

<a id="uc-057"></a>
## 057. Instrumentation requirement card.

**Mode:** `swarm-gpt`

**Inputs:** `flow.md` - one user flow and its success definition; `event-rules.md` - approved naming conventions and property types.

**Outputs:** `event-card.md` - requirements for at most six proposed events.

**Starter prompt:**

> Read flow.md and event-rules.md. Write only event-card.md, within 600 words, defining at most six events. Give each event its trigger, allowed properties, deduplication requirement, and product question. Separate attempted actions from completed outcomes. Use approved property types and flag missing conventions. Do not collect user data, inspect analytics, or claim events are implemented.

**Validation / approval:** Walk through the flow and check unambiguous triggers, valid properties, and separation of success from intent. Product and data owners must approve the card before external use or instrumentation work.

<a id="uc-058"></a>
## 058. Feedback disposition ledger.

**Mode:** `swarm-ollama`

**Inputs:** `feedback.md` - eight anonymized feedback excerpts with IDs; `issues.md` - concise descriptions of six existing product issues.

**Outputs:** `disposition.md` - proposed issue matches and unmatched feedback.

**Starter prompt:**

> Use feedback.md and issues.md to write only disposition.md, within 600 words. Match excerpts to existing issues only when the stated problems agree. Record excerpt ID, proposed issue ID, rationale, confidence, and a counterexample invalidating the match. Leave unmatched feedback unassigned and identify duplicates without deleting them. Do not create tickets, promise fixes, or interpret this sample as a frequency estimate.

**Validation / approval:** Confirm every excerpt appears and inspect proposed matches against issue wording. A product owner must approve assignments before external use or copying proposed changes into an issue tracker.

<a id="uc-059"></a>
## 059. Product decision record.

**Mode:** `swarm-ollama-claude`

**Inputs:** `decision.md` - one choice between two product approaches; `evidence.md` - evidence IDs, constraints, and known tradeoffs.

**Outputs:** `decision-record.md` - a draft decision with rationale and revisit conditions.

**Starter prompt:**

> Read decision.md and evidence.md. Write only decision-record.md, at most 600 words, comparing both approaches against identical constraints. Recommend one only if supported; otherwise identify the decisive missing fact. Record rationale, rejected tradeoffs, assumptions, reversibility, and a revisit trigger. Cite evidence IDs and label the decision as proposed. Do not invent benefits or treat the recommendation as adopted.

**Validation / approval:** Check that both options receive the same criteria and that asserted benefits have supplied evidence. The decision owner must approve the record before external use or adopting its recommendation.

<a id="uc-060"></a>
## 060. Experiment guardrail plan.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `experiment.md` - one feature hypothesis and target population; `metrics.md` - supplied outcome and guardrail definitions.

**Outputs:** `guardrail-plan.md` - an experiment readiness and interpretation checklist.

**Starter prompt:**

> Use experiment.md and metrics.md to write only guardrail-plan.md, within 600 words. Specify exposure, primary outcome, three guardrails at most, contamination risks, and prelaunch questions. Preserve supplied thresholds; leave missing thresholds and statistical parameters unresolved. Explain escalation when outcomes and guardrails conflict. Do not calculate sample size, assign participants, run an experiment, or infer causal results.

**Validation / approval:** Verify exposure, eligibility, and metric windows align and that no missing threshold becomes an invented rule. Product and measurement owners must approve the plan before external use or launching the experiment.

[Back to library](README.md)
