# Research.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Structure a narrow research task using supplied excerpts and explicit questions. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. These jobs do not browse, recruit participants, run studies or establish findings beyond the supplied evidence.

- [091. Operationalize a research construct](#uc-091)
- [092. Map claims to supplied evidence](#uc-092)
- [093. Draft an interview discussion guide](#uc-093)
- [094. Audit survey question bias](#uc-094)
- [095. Draft a qualitative codebook](#uc-095)
- [096. Explain conflicting findings](#uc-096)
- [097. Audit a report's limitations](#uc-097)
- [098. Outline a replication protocol](#uc-098)
- [099. Draft an eligibility screener](#uc-099)
- [100. Plan a literature search](#uc-100)

<a id="uc-091"></a>
## 091. Operationalize a research construct.

**Mode:** `swarm-ollama-claude`

**Inputs:** `question.md` - one nonclinical question and population; `constructs.md` - definitions, candidate measures, and constraints.

**Outputs:** `operationalization.md` - a construct-to-observation table and limitations.

**Starter prompt:**

> Read question.md and constructs.md. Write only operationalization.md, within 600 words. Break the focal construct into at most four supplied dimensions, link each to a candidate observable measure, and explain what that measure misses. Distinguish the construct from its proxy and identify confounds or interpretation ambiguities. Suggest one clarification per unresolved dimension. Do not invent validated scales, collect observations, or claim that a proposed measure has established validity.

**Validation / approval:** Check that every dimension follows the supplied definitions and that proxies are labeled accurately. A research owner must approve the operational definitions before external use or incorporating them into a study instrument.

<a id="uc-092"></a>
## 092. Map claims to supplied evidence.

**Mode:** `swarm-gpt`

**Inputs:** `claims.md` - six claims with IDs; `extracts.md` - four short source excerpts with IDs and locations.

**Outputs:** `evidence-map.md` - a claim-to-source matrix with evidence gaps.

**Starter prompt:**

> Use claims.md and extracts.md to write only evidence-map.md, within 650 words. For each claim, list relevant source IDs and excerpt locations, then classify the relationship as support, contradiction, partial support, or insufficient evidence. Explain scope mismatches and distinguish direct findings from background assertions. Use only the supplied extracts. Do not browse, invent citations, generalize beyond reported populations, or imply that unseen full sources were reviewed.

**Validation / approval:** Trace every evidence label to the cited excerpt and verify that qualification language matches its scope. The research owner must approve the matrix before external use or citing it in a report.

<a id="uc-093"></a>
## 093. Draft an interview discussion guide.

**Mode:** `swarm-claude`

**Inputs:** `learning-goals.md` - three workplace-workflow questions and participant role; `session.md` - length, consent wording, and boundaries.

**Outputs:** `interview-guide.md` - a timed guide with prompts and probes.

**Starter prompt:**

> Read learning-goals.md and session.md. Write only interview-guide.md, within 650 words. Draft an opening, at most eight core questions, optional follow-up probes, and a closing. Map each core question to a learning goal and fit the supplied session length. Prefer concrete past experiences to predictions and preserve consent wording. Avoid leading questions and unnecessary personal details. Do not contact participants, conduct interviews, or fabricate responses.

**Validation / approval:** Check timing, neutrality, goal coverage, and exact handling of the supplied consent language. The researcher must approve the guide before external use or reading it to participants during an interview.

<a id="uc-094"></a>
## 094. Audit survey question bias.

**Mode:** `swarm-ollama`

**Inputs:** `survey.md` - ten draft questions and response options; `purpose.md` - objective, population, and required constructs.

**Outputs:** `survey-audit.md` - a question-level critique with replacement suggestions.

**Starter prompt:**

> Use survey.md and purpose.md to write only survey-audit.md, within 650 words. Review each question for leading wording, double-barreled concepts, undefined timeframes, and mismatched response options. Reference question IDs, explain the likely interpretation problem, and propose a replacement only where needed. Preserve the measured construct and mark uncertain changes. Do not add demographic questions, predict response distributions, distribute the survey, or claim that revisions eliminate measurement bias.

**Validation / approval:** Check that each proposed revision measures the original construct and that response options fit the question. A researcher must approve the revisions before external use or testing the survey with respondents.

<a id="uc-095"></a>
## 095. Draft a qualitative codebook.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `excerpts.md` - eight anonymized interview excerpts with IDs; `coding-goal.md` - one question and existing code definitions.

**Outputs:** `codebook.md` - a provisional codebook with boundaries and example references.

**Starter prompt:**

> Read excerpts.md and coding-goal.md. Write only codebook.md, within 650 words. Propose at most six codes relevant to the analytic question. Give each a definition, inclusion rule, exclusion rule, and a supplied excerpt ID where available. Identify overlapping codes and uncertain examples. Preserve existing definitions unless conflicting. Do not invent quotes, infer participant characteristics, claim thematic saturation, or represent this draft as independently double-coded research.

**Validation / approval:** Apply the proposed definitions manually to the supplied excerpts and inspect boundary disagreements. A qualitative researcher must approve the provisional codebook before external use or applying it to additional interview material.

<a id="uc-096"></a>
## 096. Explain conflicting findings.

**Mode:** `swarm-claude`

**Inputs:** `finding-a.md` - one result excerpt with population and method details; `finding-b.md` - a conflicting result excerpt with equivalent details.

**Outputs:** `conflict-analysis.md` - possible reasons the findings differ.

**Starter prompt:**

> Compare finding-a.md and finding-b.md and write only conflict-analysis.md, within 600 words. Separate actual disagreement from differences in population, measurement, timing, and analysis unit. Offer at most three explanations, each with supporting excerpt details and a fact needed to assess it. State when information is insufficient. Do not choose a winner based on presentation, pool incompatible results, browse for missing methods, or treat an explanation as an established cause.

**Validation / approval:** Verify that both findings are represented accurately and that each explanation remains conditional. A researcher must approve the comparison before external use or incorporating it into a literature synthesis.

<a id="uc-097"></a>
## 097. Audit a report's limitations.

**Mode:** `swarm-gpt`

**Inputs:** `report-extract.md` - one nonclinical report's methods and conclusions extract; `review-question.md` - the decision it would inform.

**Outputs:** `limitations.md` - an applicability audit of the supplied sections.

**Starter prompt:**

> Read report-extract.md and review-question.md. Write only limitations.md, within 550 words. Identify up to five supported limitations affecting the decision; allow no supported findings. Distinguish stated limitations from missing information and inferences. Link limitations to claims and describe needed clarification. Do not assert flaws in unseen sections, infer misconduct, search for the report, or treat missing information as evidence that a procedure was omitted.

**Validation / approval:** Trace all criticisms to the supplied text and check that missing information is labeled separately from demonstrated problems. The research owner must approve the audit before external use or relying on it in a decision.

<a id="uc-098"></a>
## 098. Outline a replication protocol.

**Mode:** `swarm-ollama-claude`

**Inputs:** `methods.md` - one nonclinical usability study's methods extract; `replication-scope.md` - replication boundaries and available materials.

**Outputs:** `replication-protocol.md` - a draft procedure with fidelity requirements.

**Starter prompt:**

> Use methods.md and replication-scope.md to write only replication-protocol.md, within 650 words. Reconstruct the documented task sequence, conditions, measurements, and stopping rules. Mark necessary details absent from the extract as unresolved. Distinguish exact replication requirements from explicitly allowed adaptations. Keep the procedure to one study task. Do not recruit participants, run the study, invent results, or claim that the protocol is complete while material details are missing.

**Validation / approval:** Compare each step with the methods extract and confirm that adaptations are authorized by the scope. The study owner must resolve material gaps and approve the protocol before external use or conducting a replication.

<a id="uc-099"></a>
## 099. Draft an eligibility screener.

**Mode:** `swarm-ollama`

**Inputs:** `eligibility.md` - an adult workplace study's inclusion and exclusion rules; `study-purpose.md` - objective and recruitment boundaries.

**Outputs:** `screener.md` - an eligibility questionnaire with routing rules.

**Starter prompt:**

> Read eligibility.md and study-purpose.md. Write only screener.md, within 550 words. Convert the supplied eligibility rules into at most eight neutral questions, with response options and include, exclude, or unresolved routing. Map every routing rule to its source criterion. Ask only what evaluates those criteria and flag unnecessary sensitive details. Do not invent participant profiles, rank people, infer eligibility from unrelated traits, contact candidates, or store responses.

**Validation / approval:** Walk fictional response combinations through the routing and check for contradictions or unsupported exclusions. The researcher must approve the screener before external use or asking prospective participants to complete it.

<a id="uc-100"></a>
## 100. Plan a literature search.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `research-question.md` - one research question and terminology; `search-scope.md` - time range, source types, inclusion criteria, and vocabulary variants.

**Outputs:** `search-plan.md` - a search strategy for separate human execution.

**Starter prompt:**

> Use research-question.md and search-scope.md to write only search-plan.md, within 600 words. Draft three database-neutral Boolean query variants using supplied vocabulary. Explain each query's breadth, list screening criteria and a record of search dates and exclusions. Flag database-specific syntax that a human must adapt. Do not browse, invent retrieved papers, report result counts, or describe the plan as a completed systematic review.

**Validation / approval:** Check that query concepts and screening criteria follow the question and scope without silently adding restrictions. A researcher must approve the plan before external use and test the syntax in each chosen database separately.

[Back to library](README.md)
