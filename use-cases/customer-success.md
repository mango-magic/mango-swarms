# Customer success.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

These examples use small synthetic service and account extracts to prepare staged text. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. The workflow cannot inspect accounts, update systems or send messages. Listed modes are illustrative choices, not quality rankings.

- [021. Onboarding milestone checklist](#uc-021)
- [022. Adoption intervention brief](#uc-022)
- [023. Quarterly review outline](#uc-023)
- [024. Support escalation brief](#uc-024)
- [025. Knowledge base procedure](#uc-025)
- [026. Cancellation reason coding guide](#uc-026)
- [027. Renewal readiness brief](#uc-027)
- [028. Customer training agenda](#uc-028)
- [029. Feature request evidence table](#uc-029)
- [030. Service recovery reply](#uc-030)

<a id="uc-021"></a>
## 021. Onboarding milestone checklist.

**Mode:** `swarm-ollama`

**Inputs:** `onboarding-facts.md` - a fictional customer's agreed outcome, five setup steps, dependencies and responsible role labels.

**Outputs:** `onboarding-checklist.md` - a milestone checklist with prerequisites, owners and observable completion evidence.

**Starter prompt:**

> Use only onboarding-facts.md to create onboarding-checklist.md, under 400 words. Organize the five setup steps in dependency order. For each, identify its prerequisite, supplied owner role and observable completion evidence. Separate customer actions from provider actions. Flag missing ownership or ambiguous success criteria instead of filling them in. Do not invent deadlines, configure accounts or assume a milestone is complete. Include a readiness check for kickoff.

**Validation / approval:** Verify dependency order and that completion evidence reflects the agreed outcome. A human onboarding owner must approve the checklist before sharing it with the customer or assigning work in an account system.

<a id="uc-022"></a>
## 022. Adoption intervention brief.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `adoption-snapshot.md` - four weeks of synthetic aggregate feature usage, measurement definitions and known rollout context.

**Outputs:** `adoption-brief.md` - observed adoption patterns, uncertainty and one proposed enablement intervention.

**Starter prompt:**

> Use only adoption-snapshot.md to write adoption-brief.md, under 350 words. Identify one documented usage gap relative to a supplied objective. Separate measurement facts from possible explanations, checking denominators and time windows. Propose one small enablement activity and a follow-up measure. Do not identify individual users, infer dissatisfaction or predict churn from low usage. State what the account owner must verify before acting.

**Validation / approval:** Recheck aggregate comparisons and ensure the intervention addresses an observed gap. A human success owner must approve the interpretation and any customer outreach, training invitation or account-system change before execution.

<a id="uc-023"></a>
## 023. Quarterly review outline.

**Mode:** `swarm-claude`

**Inputs:** `quarterly-evidence.md` - three fictional customer objectives, aggregate outcomes with dates and two unresolved service issues.

**Outputs:** `quarterly-review.md` - a six-part meeting outline covering outcomes, gaps and decisions needing discussion.

**Starter prompt:**

> Use only quarterly-evidence.md to create quarterly-review.md, under 450 words. Build a six-part outline for a 30-minute review with time allocations totaling 30 minutes. Connect each reported outcome to the supplied objective, identify missing baseline evidence and preserve unresolved issues. Include discussion questions and proposed next decisions. Do not invent return on investment, customer satisfaction, attribution or future targets. Produce an outline, not a slide deck.

**Validation / approval:** Check timing, objective coverage and the distinction between evidence and interpretation. A human account owner must approve metrics and proposed decisions before presenting the review or sharing it with a customer.

<a id="uc-024"></a>
## 024. Support escalation brief.

**Mode:** `swarm-gpt`

**Inputs:** `ticket-extract.md` - a synthetic incident timeline, observed symptoms, attempted remedies, stated impact and existing escalation criteria.

**Outputs:** `escalation-brief.md` - a factual handoff with timeline, unresolved questions and a proposed escalation route.

**Starter prompt:**

> Use only ticket-extract.md to draft escalation-brief.md, under 400 words. Preserve event order and distinguish observed behavior, customer reports and untested hypotheses. Summarize attempted remedies without claiming they worked. Apply only the supplied escalation criteria, marking missing evidence. List information a human should gather next. Do not diagnose root cause, assign blame, promise a resolution time or execute any remedy.

**Validation / approval:** Verify chronology, impact wording and criteria application against the extract. A human support lead must approve severity, routing and any customer communication before escalating in a live system or contacting another team.

<a id="uc-025"></a>
## 025. Knowledge base procedure.

**Mode:** `swarm-ollama-claude`

**Inputs:** `procedure-source.md` - an approved fictional procedure containing prerequisites, six steps, interface labels and known failure conditions.

**Outputs:** `help-procedure.md` - a user-facing article with prerequisites, numbered steps and bounded troubleshooting guidance.

**Starter prompt:**

> Use only procedure-source.md to write help-procedure.md, under 450 words. Preserve the order and exact interface labels of the six supplied steps. Explain prerequisites and expected results, then address only the documented failure conditions. Flag missing details rather than inventing controls, permissions or recovery instructions. Include a stopping point when the documented process cannot resolve an issue. Do not claim the procedure was tested.

**Validation / approval:** A human must perform the procedure in an appropriate test setting and check labels and stopping conditions. A human knowledge owner must approve the article before publishing or sending it to customers.

<a id="uc-026"></a>
## 026. Cancellation reason coding guide.

**Mode:** `swarm-ollama`

**Inputs:** `cancellation-samples.md` - eight synthetic cancellation comments and a short definition of the intended reporting purpose.

**Outputs:** `cancellation-codebook.md` - a small reason taxonomy with inclusion rules and example classifications.

**Starter prompt:**

> Use only cancellation-samples.md to create cancellation-codebook.md, under 450 words. Define at most five reason codes, including an unclear or insufficient-information code. Explain inclusion and exclusion rules, then classify the eight samples using their identifiers. Allow multiple codes only when the text explicitly supports them. Preserve uncertainty and distinguish the stated reason from inferred intent. Do not estimate prevalence beyond this synthetic sample.

**Validation / approval:** Check all samples are accounted for and similar comments receive consistent treatment. A human research owner must approve the taxonomy before applying it to live records, changing reporting fields or sharing conclusions externally.

<a id="uc-027"></a>
## 027. Renewal readiness brief.

**Mode:** `swarm-claude`

**Inputs:** `renewal-context.md` - fictional renewal timing, documented outcomes, unresolved obligations and the customer's stated review criteria.

**Outputs:** `renewal-readiness.md` - a readiness summary and a short list of evidence gaps to resolve.

**Starter prompt:**

> Use only renewal-context.md to write renewal-readiness.md, under 400 words. Assess whether the supplied evidence addresses each stated customer review criterion. Separate achieved outcomes, unresolved obligations and missing information. Prioritize three preparation actions with role-based ownership where supplied. Do not predict renewal probability, set commercial terms, infer sentiment or suggest a discount. Treat dates as context for preparation, not authority to send notices.

**Validation / approval:** Match every readiness statement to a criterion and verify outstanding obligations remain visible. A human account owner must approve the brief before external discussion or changes to renewal status in a live system.

<a id="uc-028"></a>
## 028. Customer training agenda.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `training-brief.md` - a fictional audience's skill level, one workflow, three learning objectives and approved demonstration steps.

**Outputs:** `training-agenda.md` - a 25-minute session plan with one practice activity and a knowledge check.

**Starter prompt:**

> Use only training-brief.md to create training-agenda.md, under 400 words. Allocate exactly 25 minutes across introduction, supplied demonstration steps, one practice activity and a recap. Map each segment to a stated learning objective. Include three short knowledge-check questions with answers supported by the input. Flag missing setup requirements. Do not invent product controls or claim the activity proves competence outside the covered workflow.

**Validation / approval:** Check time totals, objective coverage and answer accuracy; a human trainer should rehearse the demonstration. The trainer must approve the agenda before scheduling or delivering it to customers.

<a id="uc-029"></a>
## 029. Feature request evidence table.

**Mode:** `swarm-gpt`

**Inputs:** `feature-request-samples.md` - six synthetic requests with identifiers, stated workflows and the problem each requester described.

**Outputs:** `feature-evidence.md` - a problem-centered table showing related requests, differences and unresolved questions.

**Starter prompt:**

> Use only feature-request-samples.md to create feature-evidence.md, under 450 words. Group requests only when their underlying problems are demonstrably similar. Preserve source identifiers and distinguish requested solutions from stated needs. Note exceptions within each group and suggest one clarifying question per group. Do not infer market demand, prioritize by revenue or promise roadmap delivery. Keep findings explicitly limited to the six synthetic samples.

**Validation / approval:** Confirm no request was lost and groupings retain material workflow differences. A human product owner must approve the synthesis before adding it to a product system or discussing roadmap implications with customers.

<a id="uc-030"></a>
## 030. Service recovery reply.

**Mode:** `swarm-ollama-claude`

**Inputs:** `recovery-brief.md` - a fictional complaint, verified service facts, approved remedy and any confirmed next-update time.

**Outputs:** `service-reply.md` - a draft response acknowledging the issue and describing only authorized next steps.

**Starter prompt:**

> Use only recovery-brief.md to write service-reply.md, under 250 words. Acknowledge the specific reported impact without speculating about causes. State the approved remedy and any limits in plain language, then give the confirmed next-update time if supplied. Mark missing recipient or timing details as placeholders. Do not admit unverified fault, invent compensation, guarantee resolution or imply a remedy has already been executed.

**Validation / approval:** Check empathy, factual accuracy, remedy authorization and all remaining placeholders. A human support owner must approve the final message and recipient before sending; separate human approval is required before issuing any remedy.

[Back to library](README.md)
