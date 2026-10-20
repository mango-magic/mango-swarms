# People.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare bounded drafts for authorized HR and manager review using fictional roles and synthetic situations. These jobs do not assess real people or make employment decisions. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Outputs are staged text; example modes do not establish privacy or a provider's locality.

- [111. Role onboarding path](#uc-111)
- [112. Job description clarity audit](#uc-112)
- [113. Structured interview questions](#uc-113)
- [114. Training practice exercises](#uc-114)
- [115. Employee policy FAQ](#uc-115)
- [116. Manager discussion guide](#uc-116)
- [117. Team working agreement](#uc-117)
- [118. Leave handover template](#uc-118)
- [119. Recognition evidence template](#uc-119)
- [120. Knowledge capture interview guide](#uc-120)

<a id="uc-111"></a>
## 111. Role onboarding path.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `role-summary.md` - a fictional role's responsibilities, dependencies and learning goals; `onboarding-extract.md` - generic orientation tasks, approved training and role owners.

**Outputs:** `onboarding-path.md` - a short staged learning path with prerequisites and completion evidence.

**Starter prompt:**

> Use role-summary.md and onboarding-extract.md to draft onboarding-path.md, under 550 words. Group supplied activities into orientation, guided practice and readiness discussion. State prerequisites, documented support roles and possible completion evidence. Flag missing training details. Do not invent access permissions, evaluate an employee or decide when someone may work independently.

**Validation / approval:** Verify all requirements and ownership against the extracts. Authorized HR and the role manager approve the path before assigning training; the appropriate qualified supervisor separately confirms readiness for any restricted duties.

<a id="uc-112"></a>
## 112. Job description clarity audit.

**Mode:** `swarm-claude`

**Inputs:** `role-draft.md` - a fictional job description with responsibilities and requirements; `role-criteria.md` - approved essential duties, terminology and distinction between required and preferred skills.

**Outputs:** `role-clarity-audit.md` - a table of ambiguous phrases, source conflicts and proposed clarifications.

**Starter prompt:**

> Review role-draft.md against role-criteria.md and create role-clarity-audit.md, under 550 words. Quote only short phrases needing clarification, explain each ambiguity and suggest wording grounded in the approved duties. Flag unsupported requirements and distinguish essential from preferred criteria. Do not add qualifications, infer protected traits or evaluate applicants.

**Validation / approval:** Check every proposed criterion against authorized duties and confirm no unsupported barriers were added. A qualified HR reviewer and hiring manager approve the description before publication or recruitment use.

<a id="uc-113"></a>
## 113. Structured interview questions.

**Mode:** `swarm-gpt`

**Inputs:** `interview-objectives.md` - five job-relevant capabilities for a fictional role; `interview-guidance.md` - generic approved question boundaries and interview duration.

**Outputs:** `interview-questions.md` - five consistent questions, optional neutral probes and objective mappings.

**Starter prompt:**

> Create interview-questions.md from interview-objectives.md and interview-guidance.md in at most 550 words. Draft one question per supplied capability, with a neutral follow-up and a note explaining the job relevance. Keep the set within the supplied duration. Avoid personal circumstances, protected characteristics and candidate scoring. Produce questions only, without hiring recommendations.

**Validation / approval:** Confirm capability coverage, consistent administration and compliance with the provided boundaries. A qualified HR reviewer approves the questions before interviews; authorized humans alone assess candidates and make employment decisions.

<a id="uc-114"></a>
## 114. Training practice exercises.

**Mode:** `swarm-ollama`

**Inputs:** `training-extract.md` - a generic workplace procedure and three learning objectives; `learner-context.md` - a fictional audience's assumed knowledge and permitted practice setting.

**Outputs:** `practice-exercises.md` - two short fictional exercises with facilitator discussion notes.

**Starter prompt:**

> Use training-extract.md and learner-context.md to write practice-exercises.md, under 600 words. Create two independent, fictional practice situations covering the supplied objectives. Include learner instructions, discussion prompts and facilitator notes citing procedure steps. Keep practice within the permitted setting. Do not certify competence, score employees or introduce safety instructions beyond the source.

**Validation / approval:** Trace each exercise to a learning objective and check the facilitator notes against the procedure. The training owner and a qualified subject expert approve the material before delivery or practical use.

<a id="uc-115"></a>
## 115. Employee policy FAQ.

**Mode:** `swarm-ollama-claude`

**Inputs:** `policy-extract.md` - a fictional policy section with clause labels and effective date; `sample-questions.md` - six generic questions without employee circumstances or personal data.

**Outputs:** `policy-faq.md` - six concise draft answers with policy references and unresolved interpretation flags.

**Starter prompt:**

> Draft policy-faq.md from policy-extract.md and sample-questions.md, under 550 words. Answer each question only where the extract supports an answer and cite its clause label. Preserve dates and exceptions. Route unsupported interpretations to the named policy owner if supplied. Do not give legal advice, decide eligibility or promise an employee outcome.

**Validation / approval:** Verify each answer, exception and reference against the current authorized policy. A qualified HR policy owner approves the FAQ before staff distribution or use in an individual case.

<a id="uc-116"></a>
## 116. Manager discussion guide.

**Mode:** `swarm-claude`

**Inputs:** `team-scenario.md` - a synthetic situation involving unclear priorities and handoffs; `conversation-principles.md` - generic manager guidance on listening, clarification and follow-up.

**Outputs:** `manager-discussion.md` - a short one-to-one agenda with open questions and an action-record template.

**Starter prompt:**

> Use team-scenario.md and conversation-principles.md to draft manager-discussion.md, under 500 words. Focus on clarifying work expectations, available support and mutually understood next steps. Separate supplied observations from assumptions. Include neutral questions and blank action fields. Do not diagnose motivation, infer personal circumstances or recommend discipline, promotion or other employment outcomes.

**Validation / approval:** Confirm questions are neutral and grounded in the scenario. An authorized manager and qualified HR reviewer approve the guide before use; any employment matter follows the organization's separate human process.

<a id="uc-117"></a>
## 117. Team working agreement.

**Mode:** `swarm-gpt`

**Inputs:** `team-preferences.md` - fictional preferences on meetings, handoffs and communication; `work-boundaries.md` - generic operating hours, existing policy constraints and decision roles.

**Outputs:** `working-agreement.md` - a draft agreement separating supported common ground from choices needing discussion.

**Starter prompt:**

> Create working-agreement.md from team-preferences.md and work-boundaries.md in at most 550 words. Cover meeting preparation, communication expectations, handoffs and review cadence. Distinguish shared preferences from conflicting requests and leave disputed terms as discussion points. Respect supplied policy and working-hour boundaries. Do not impose new obligations, monitor workers or infer consent.

**Validation / approval:** Check that no preference was presented as unanimous without support. The team and authorized manager approve the agreement, with qualified HR review of policy-sensitive terms, before adopting or distributing it.

<a id="uc-118"></a>
## 118. Leave handover template.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `responsibility-example.md` - a fictional role's recurring work, open tasks and deadlines; `handover-standard.md` - generic coverage fields, escalation boundaries and documentation rules.

**Outputs:** `leave-handover-template.md` - a reusable template illustrated with synthetic task references.

**Starter prompt:**

> Draft leave-handover-template.md using responsibility-example.md and handover-standard.md, under 500 words. Include current status, next action, proposed coverage role, source reference and unresolved dependency fields. Distinguish proposed cover from confirmed agreement. Keep reasons for absence and personal details out of the template. Do not assign access, transfer authority or contact colleagues.

**Validation / approval:** Verify task references, deadlines and escalation limits; remove unnecessary personal fields. The responsible manager and authorized HR reviewer approve the template, and coverage owners confirm arrangements before duties or permissions change.

<a id="uc-119"></a>
## 119. Recognition evidence template.

**Mode:** `swarm-ollama`

**Inputs:** `recognition-criteria.md` - a fictional recognition program's approved criteria and exclusions; `contribution-examples.md` - four synthetic contribution descriptions without real identities.

**Outputs:** `recognition-template.md` - a nomination template with evidence prompts and clearly fictional examples.

**Starter prompt:**

> Use recognition-criteria.md and contribution-examples.md to produce recognition-template.md, under 500 words. Ask for observable contribution, relevant criterion, supporting evidence and acknowledgment of collaborators. Use the examples only to demonstrate complete and incomplete evidence. Flag unsupported claims without rating people. Do not rank nominees, select recipients or recommend compensation or promotion.

**Validation / approval:** Check that evidence prompts reflect the supplied criteria and examples remain explicitly fictional. A qualified HR program owner approves the template before circulation; authorized reviewers separately decide any recognition outcome.

<a id="uc-120"></a>
## 120. Knowledge capture interview guide.

**Mode:** `swarm-ollama-claude`

**Inputs:** `role-knowledge-map.md` - a fictional role's recurring decisions, document types and dependencies; `capture-boundaries.md` - generic sharing permissions and excluded confidential topics.

**Outputs:** `knowledge-capture-guide.md` - an interview guide for documenting permitted operational knowledge during a planned handover.

**Starter prompt:**

> Create knowledge-capture-guide.md from role-knowledge-map.md and capture-boundaries.md, under 550 words. Draft questions about recurring work, exception handling, useful document locations and unresolved dependencies. Include a blank follow-up log. Ask for references rather than credentials or confidential contents. Do not infer reasons for departure, solicit private personnel information or assess an employee.

**Validation / approval:** Verify questions respect sharing boundaries and exclude secrets. The role owner and qualified HR reviewer approve the guide before an interview; document owners approve any subsequent knowledge transfer.

[Back to library](README.md)
