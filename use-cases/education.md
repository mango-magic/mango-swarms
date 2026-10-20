# Education.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Prepare teaching materials, assessment discussions, and learning activities from fictional or synthetic examples. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. The named outputs are short staged drafts, assessed by a fresh reviewer and then a human. Modes below are suitable examples, not performance rankings. Verify the actual model and endpoint if local processing matters; a mode name alone does not establish privacy.

- [151. Rubric calibration anchors](#uc-151)
- [152. Misconception sorting cards](#uc-152)
- [153. Curriculum prerequisite questions](#uc-153)
- [154. Museum object inquiry stations](#uc-154)
- [155. Source comparison lesson](#uc-155)
- [156. Oral history interviewing rehearsal](#uc-156)
- [157. Field observation notebook guide](#uc-157)
- [158. Family curriculum glossary](#uc-158)
- [159. Capstone exhibition labels](#uc-159)
- [160. Discussion facilitation branches](#uc-160)

<a id="uc-151"></a>
## 151. Rubric calibration anchors.

**Mode:** `swarm-ollama`

**Inputs:** `rubric.md` - approved fictional criteria and level descriptors; `responses.md` - four synthetic student responses with sample IDs.

**Outputs:** `calibration.md` - a compact facilitator packet connecting response excerpts to rubric language.

**Starter prompt:**

> Use rubric.md and responses.md to draft calibration.md for one teacher calibration discussion. Include one evidence table per sample, quoting the relevant response phrase and rubric descriptor. Suggest discussion questions wherever two descriptors could fit. Keep proposed levels explicitly provisional, omit overall grades, and limit the packet to 650 words. Preserve sample IDs and identify any criterion that cannot be assessed from the supplied response.

**Validation / approval:** Check every quotation and descriptor against the inputs. Confirm uncertainty remains visible. A teacher must approve before using the packet in staff training or assessment work.

<a id="uc-152"></a>
## 152. Misconception sorting cards.

**Mode:** `swarm-ollama-claude`

**Inputs:** `concepts.md` - approved fictional lesson explanations; `statements.md` - eight synthetic statements, including deliberately incorrect examples.

**Outputs:** `sorting-cards.md` - numbered cards, an evidence key, and two discussion prompts.

**Starter prompt:**

> Read concepts.md and statements.md and create sorting-cards.md for a single classroom sorting activity. Preserve the eight statement IDs. Place the statements first, followed by a separate teacher key that connects each judgment to an exact source passage. Mark unsupported judgments as unresolved. Add two questions that help learners explain their choices without introducing new subject facts. Keep the full draft below 600 words.

**Validation / approval:** Confirm all eight cards appear once, the key follows the approved explanations, and incorrect statements remain clearly identified in the teacher section. A teacher approves classroom use.

<a id="uc-153"></a>
## 153. Curriculum prerequisite questions.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `units.md` - six fictional unit summaries with stated prerequisites; `catalog.md` - approved learning outcome definitions and identifiers.

**Outputs:** `prerequisite-review.md` - a traceable prerequisite matrix and unresolved curriculum questions.

**Starter prompt:**

> Use units.md and catalog.md to create prerequisite-review.md. Map only explicitly stated prerequisite relationships among the six units. Distinguish a missing reference from a prerequisite that is simply unstated. Include the source unit and outcome IDs in each row. List at most five questions about gaps, circular references, or inconsistent terminology. Do not invent dependencies or propose a new course sequence. Limit the draft to 650 words.

**Validation / approval:** Verify every relationship against the supplied wording and confirm all six units are represented. A curriculum lead must approve before changing course descriptions or teaching plans.

<a id="uc-154"></a>
## 154. Museum object inquiry stations.

**Mode:** `swarm-gpt`

**Inputs:** `objects.md` - approved descriptions of three fictional museum objects; `lesson-goals.md` - observation and evidence goals for one class visit.

**Outputs:** `inquiry-stations.md` - three short station cards and a facilitator evidence key.

**Starter prompt:**

> Draft inquiry-stations.md using objects.md and lesson-goals.md. Create one station for each object, with one description-based observation question, one comparison question, and one question the supplied evidence cannot settle. Put a compact facilitator key after the cards. Distinguish documented facts from possible interpretations, and never invent an object's maker, origin, or cultural meaning. Use text descriptions only and keep the complete set below 600 words.

**Validation / approval:** Check that answerable questions have supporting source passages and open questions remain open. An educator and collection owner must approve before distributing the station cards.

<a id="uc-155"></a>
## 155. Source comparison lesson.

**Mode:** `swarm-claude`

**Inputs:** `source-extracts.md` - two short fictional accounts with author, date, and purpose metadata; `comparison-goals.md` - approved source-literacy objectives.

**Outputs:** `comparison-lesson.md` - a paired-source worksheet and a separate teacher evidence key.

**Starter prompt:**

> Use source-extracts.md and comparison-goals.md to prepare comparison-lesson.md. Write six questions covering agreement, disagreement, perspective, and missing evidence across the two accounts. Provide a teacher key with exact supporting passages and acknowledge questions with multiple defensible answers. Treat the fictional sources as classroom material, not verified history. Do not introduce outside facts or determine credibility from author identity alone. Keep the worksheet and key together under 650 words.

**Validation / approval:** Verify quotation accuracy and ensure questions compare evidence rather than demand one unsupported interpretation. A teacher must approve before assigning or publishing the lesson.

<a id="uc-156"></a>
## 156. Oral history interviewing rehearsal.

**Mode:** `swarm-ollama`

**Inputs:** `interview-guidance.md` - approved fictional workshop guidance; `practice-dialogue.md` - a synthetic interviewer and narrator exchange.

**Outputs:** `interview-rehearsal.md` - an annotated rehearsal identifying leading questions and missed follow-ups.

**Starter prompt:**

> Read interview-guidance.md and practice-dialogue.md to draft interview-rehearsal.md. Identify up to six interviewer turns that could be improved under the supplied guidance. Quote each original turn, explain the relevant guidance, and suggest a neutral alternative or an optional follow-up. Preserve the narrator's words and do not invent experiences, permission, or recording consent. End with three reflection questions for learners. Limit the rehearsal to 600 words.

**Validation / approval:** Confirm annotations cite actual guidance and alternatives avoid presupposing facts about the narrator. A workshop leader must approve before training use; actual interview permissions require separate human handling.

<a id="uc-157"></a>
## 157. Field observation notebook guide.

**Mode:** `swarm-ollama-claude`

**Inputs:** `observation-method.md` - approved fictional geography recording fields; `sample-notes.md` - six synthetic, imperfect field observations.

**Outputs:** `notebook-guide.md` - an annotated practice notebook separating observations from interpretations.

**Starter prompt:**

> Use observation-method.md and sample-notes.md to create notebook-guide.md for one recording-skills lesson. Reformat the six sample notes into the approved fields, preserving original observations and units. Mark absent details as missing rather than filling them in. Identify language that expresses an interpretation and place it in the designated interpretation field, if one exists. Include three source-based recording reminders. Do not add fieldwork routes or procedures. Stay below 600 words.

**Validation / approval:** Check that no measurement, location, or observation was invented and every sample remains traceable. A teacher approves the guide before classroom distribution or adaptation for fieldwork.

<a id="uc-158"></a>
## 158. Family curriculum glossary.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `curriculum-terms.md` - twelve fictional course terms with approved explanations; `approved-translations.md` - corresponding approved translations and language labels.

**Outputs:** `family-glossary.md` - a compact parallel glossary with missing translations visibly flagged.

**Starter prompt:**

> Create family-glossary.md from curriculum-terms.md and approved-translations.md. Include the twelve course terms, their approved explanations, and available approved translations in a consistent table. Copy translated wording exactly; do not supply missing translations or infer regional variants. Flag unmatched term IDs and inconsistencies in a review note. Introduce the glossary with one sentence describing its classroom purpose. Keep the document below 600 words and preserve all language labels.

**Validation / approval:** Compare translated strings character for character and verify every term ID appears once. A teacher and qualified language reviewer must approve before sharing the glossary with families.

<a id="uc-159"></a>
## 159. Capstone exhibition labels.

**Mode:** `swarm-gpt`

**Inputs:** `projects.md` - approved descriptions of four fictional capstone artifacts; `exhibition-brief.md` - audience, learning outcomes, and label length limits.

**Outputs:** `exhibition-labels.md` - four display labels and a short question for each exhibit.

**Starter prompt:**

> Use projects.md and exhibition-brief.md to draft exhibition-labels.md. Write one label per project within the supplied length limit, stating what was made and the associated learning outcome. Add one visitor question that invites examination of the described artifact. Preserve the project's stated limitations and use project IDs instead of student names. Do not invent results, materials, awards, or visitor interaction features. Keep the total below 600 words.

**Validation / approval:** Check all four labels against project descriptions and measure the individual word limits. The project author and educator must approve before public display or online publication.

<a id="uc-160"></a>
## 160. Discussion facilitation branches.

**Mode:** `swarm-claude`

**Inputs:** `discussion-goals.md` - approved fictional seminar goals and participation norms; `sample-thread.md` - a short synthetic discussion with turn IDs.

**Outputs:** `facilitation-branches.md` - a compact map of possible facilitator interventions.

**Starter prompt:**

> Read discussion-goals.md and sample-thread.md and produce facilitation-branches.md. Select four moments where a facilitator could ask for evidence, connect contrasting ideas, clarify terminology, or invite another perspective. For each, cite the turn ID and offer two intervention options with their intended purpose. Keep participant intent uncertain and avoid personal judgments or disciplinary recommendations. Do not continue the conversation on anyone's behalf. Limit the map to 550 words.

**Validation / approval:** Confirm every intervention addresses a real turn and respects the supplied participation norms. A seminar facilitator must approve before using or sharing the options with a class.

[Back to library](README.md)
