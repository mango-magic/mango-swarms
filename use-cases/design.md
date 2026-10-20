# Design.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Translate compact written design context into inspectable specifications and content. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. These jobs do not inspect screens, generate binary assets or modify design applications.

- [081. Organize one screen's hierarchy](#uc-081)
- [082. Draft form error microcopy](#uc-082)
- [083. Specify dialog keyboard behavior](#uc-083)
- [084. Map semantic design tokens](#uc-084)
- [085. Specify responsive card behavior](#uc-085)
- [086. Model a disclosure component](#uc-086)
- [087. Draft a visual inspection rubric](#uc-087)
- [088. Review localization fit constraints](#uc-088)
- [089. Map one service handoff](#uc-089)
- [090. Resolve a guideline conflict](#uc-090)

<a id="uc-081"></a>
## 081. Organize one screen's hierarchy.

**Mode:** `swarm-ollama-claude`

**Inputs:** `screen-content.md` - one screen's content and actions; `user-task.md` - its audience, primary task, and mandatory information.

**Outputs:** `screen-outline.md` - a textual hierarchy and reading order.

**Starter prompt:**

> Read screen-content.md and user-task.md. Write only screen-outline.md, within 550 words. Arrange the supplied content into primary, supporting, and deferred sections for this task. Assign one primary action and explain the placement of critical information. Preserve mandatory content and mark uncertain priorities. Provide a numbered reading order and a short rationale, without adding new features, drawing a screen, or claiming usability has been tested.

**Validation / approval:** Check that every mandatory content block appears and that the primary action follows the stated task. A designer must approve the hierarchy before external use or translating it into a visual design.

<a id="uc-082"></a>
## 082. Draft form error microcopy.

**Mode:** `swarm-ollama`

**Inputs:** `form-errors.md` - six validation failures and recovery actions; `voice.md` - tone, terminology, and length rules.

**Outputs:** `error-copy.md` - a message table with recovery wording.

**Starter prompt:**

> Use form-errors.md and voice.md to write only error-copy.md, within 450 words. For each supplied failure, draft a short message stating the problem and the permitted next action. Include the trigger ID, message, recovery label, and any unresolved behavior. Respect the supplied length limits and avoid blaming the user or promising unavailable recovery. Cover only the listed failures; do not alter validation rules or send messages.

**Validation / approval:** Match each message to its actual trigger and verify that its recovery action exists in the source. A designer and product owner must approve the copy before external use or placement in a user interface.

<a id="uc-083"></a>
## 083. Specify dialog keyboard behavior.

**Mode:** `swarm-gpt`

**Inputs:** `dialog.md` - one modal's controls, triggers, and closing conditions; `interaction-rules.md` - keyboard and focus conventions.

**Outputs:** `keyboard-spec.md` - a focus sequence and keyboard interaction table.

**Starter prompt:**

> Read dialog.md and interaction-rules.md. Write only keyboard-spec.md, within 600 words. Specify initial focus, traversal order, supported keys, close behavior, and focus return. Cover disabled controls, validation feedback, and a missing opener only when the supplied conventions define them; otherwise record questions. Trace two keyboard journeys through the proposed behavior. Do not inspect an application, execute accessibility tests, or claim conformance to a standard.

**Validation / approval:** Compare every key action with the supplied conventions and have a human test the implemented journeys with a keyboard. An accessibility reviewer must approve the specification before external use or implementation.

<a id="uc-084"></a>
## 084. Map semantic design tokens.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `legacy-tokens.json` - fifteen token names, values, and usages; `semantic-tokens.md` - approved target tokens and roles.

**Outputs:** `token-map.md` - a semantic mapping with ambiguous usages.

**Starter prompt:**

> Use legacy-tokens.json and semantic-tokens.md to write only token-map.md, within 600 words. Map each legacy token to a target only when its documented usage fits the target role. Include old name, proposed name, usage evidence, and migration caveat. Identify mixed-purpose tokens that need a split rather than forcing a value match. Do not invent target tokens, assess visual contrast, edit stylesheets, or update a design library.

**Validation / approval:** Confirm every legacy token appears once and inspect mappings based on role rather than matching color values. The design-system owner must approve the mapping before external use or applying token substitutions.

<a id="uc-085"></a>
## 085. Specify responsive card behavior.

**Mode:** `swarm-claude`

**Inputs:** `card-group.md` - one card group's content priorities and size constraints; `breakpoints.md` - approved breakpoints and layout conventions.

**Outputs:** `responsive-spec.md` - a rule table for three supplied viewport ranges.

**Starter prompt:**

> Read card-group.md and breakpoints.md. Write only responsive-spec.md, within 600 words. Specify column count, spacing, wrapping, action placement, and content order for the three stated ranges. Include long titles, missing optional metadata, and narrow-width behavior. Preserve the information hierarchy and flag constraints that cannot simultaneously hold. Do not invent device measurements, render layouts, or claim the proposed rules prevent overflow without implementation checks.

**Validation / approval:** Check rule consistency at each breakpoint boundary and have a human inspect implemented examples with short and long content. A designer must approve the specification before external use or translating it into layout code.

<a id="uc-086"></a>
## 086. Model a disclosure component.

**Mode:** `swarm-ollama-claude`

**Inputs:** `disclosure.md` - one component's content, events, and persistence requirements; `component-rules.md` - interaction and labeling conventions.

**Outputs:** `disclosure-states.md` - a component state and transition specification.

**Starter prompt:**

> Use disclosure.md and component-rules.md to write only disclosure-states.md, within 600 words. Define at most eight states and a transition table covering opening, closing, content loading, failure, and retry where supported. Record visible labels, available actions, and persistence behavior per state. Identify unreachable or undefined transitions. Do not add animation timings, fetch content, build the component, or claim the interaction has been tested.

**Validation / approval:** Walk each supported event through the table and confirm that every reachable state has a defined next action. The component owner must approve the model before external use or implementation in a design system.

<a id="uc-087"></a>
## 087. Draft a visual inspection rubric.

**Mode:** `swarm-gpt`

**Inputs:** `visual-rules.md` - one screen's layout, type, spacing, and alignment rules; `states.md` - four required content states.

**Outputs:** `inspection-rubric.md` - a manual visual inspection checklist.

**Starter prompt:**

> Read visual-rules.md and states.md. Write only inspection-rubric.md, within 600 words. Create at most twelve checks, each with a rule ID, state to inspect, observable pass condition, and example failure. Distinguish measurements from judgment calls and note any missing reference value. Make this a checklist for a human viewing the implementation. Do not inspect screenshots, report visual defects, or imply that any screen has already passed.

**Validation / approval:** Confirm each check maps to a supplied rule and can be judged from the stated screen and state. A designer must approve the rubric before external use or recording actual inspection results against it.

<a id="uc-088"></a>
## 088. Review localization fit constraints.

**Mode:** `swarm-ollama`

**Inputs:** `strings.csv` - twelve source strings and translations with IDs; `layout-limits.md` - length, wrapping, and directionality constraints.

**Outputs:** `localization-fit.md` - a fit-risk list and layout questions.

**Starter prompt:**

> Use strings.csv and layout-limits.md to write only localization-fit.md, within 550 words. Identify strings that may conflict with the supplied length or wrapping constraints. Reference string IDs and distinguish character-count risks from rendered-width questions. Preserve all translations and note directionality issues only where the source defines them. Suggest a bounded manual check for each concern. Do not claim translation accuracy, measure rendered text, or edit an interface.

**Validation / approval:** Independently verify any character counts and inspect the translated strings in the actual layout. A localization reviewer and designer must approve the findings before external use or changing translated copy or layout rules.

<a id="uc-089"></a>
## 089. Map one service handoff.

**Mode:** `swarm-claude`

**Inputs:** `handoff.md` - one service transition's five touchpoints, actor roles, and artifacts; `service-rules.md` - responsibilities and response expectations.

**Outputs:** `handoff-blueprint.md` - a small service blueprint identifying ownership and information gaps.

**Starter prompt:**

> Read handoff.md and service-rules.md. Write only handoff-blueprint.md, within 600 words. Map each touchpoint to the user's visible action, backstage responsibility, information needed, and completion signal. Identify gaps between confirmed responsibilities and observed behavior. Propose one clarification for each gap without assigning new commitments. Do not contact participants, change workflows, or assume the observations describe every service interaction.

**Validation / approval:** Check touchpoint order and ownership against both inputs, with unknown responsibilities explicitly labeled. The service owner must approve the blueprint before external use or changing a team's handoff procedure.

<a id="uc-090"></a>
## 090. Resolve a guideline conflict.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `guidelines.md` - two internal guideline excerpts with dates and authority notes; `component-context.md` - one affected component.

**Outputs:** `guideline-decision.md` - an interpretation memo with resolution and authority questions.

**Starter prompt:**

> Use guidelines.md and component-context.md to write only guideline-decision.md, within 550 words. Quote the conflicting rule IDs, describe the concrete component behavior each implies, and identify whether supplied scope or precedence resolves the conflict. Propose a resolution only where supported; otherwise state the authority decision needed. Include consequences for this component. Do not invent policy precedence, inspect external standards, or update the guidelines.

**Validation / approval:** Verify rule wording, dates, and scope against the excerpts and confirm that the memo preserves unresolved authority questions. The design-system owner must approve the interpretation before external use or treating it as an official guideline.

[Back to library](README.md)
