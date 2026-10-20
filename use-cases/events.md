# Events.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

These examples prepare bounded event documents from synthetic briefs and concise supplied extracts. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each goal stages one text artifact; the workflow cannot book venues, contact attendees or operate event systems. Suggested modes demonstrate available configurations without comparative claims.

- [041. Event run of show](#uc-041)
- [042. Speaker preparation brief](#uc-042)
- [043. Sponsor deliverables checklist](#uc-043)
- [044. Attendee reminder message](#uc-044)
- [045. Session description set](#uc-045)
- [046. Panel moderator question route](#uc-046)
- [047. Audio and video contingency cards](#uc-047)
- [048. Accessibility logistics review](#uc-048)
- [049. Event feedback survey](#uc-049)
- [050. Event debrief](#uc-050)

<a id="uc-041"></a>
## 041. Event run of show.

**Mode:** `swarm-gpt`

**Inputs:** `event-timing.md` - a fictional 45-minute event's six segments, fixed durations, transition requirements and assigned production roles.

**Outputs:** `run-of-show.md` - an elapsed-time cue table with role ownership, transitions and unresolved conflicts.

**Starter prompt:**

> Use only event-timing.md to create run-of-show.md, under 400 words. Build a 45-minute timeline using the six supplied segments and account for stated transitions. Show elapsed start and end times, cue text and responsible roles. Flag impossible timing or missing cue ownership instead of shortening fixed segments silently. Do not invent venue equipment, trigger any system or claim the schedule has been rehearsed.

**Validation / approval:** Recalculate elapsed times and inspect transitions for gaps or overlap. A human producer must approve the schedule and rehearse critical cues before distributing it to crew or using it during the event.

<a id="uc-042"></a>
## 042. Speaker preparation brief.

**Mode:** `swarm-ollama-claude`

**Inputs:** `speaker-session.md` - a fictional session's audience, learning outcomes, talk length, format, supplied deadlines and content restrictions.

**Outputs:** `speaker-brief.md` - a briefing with presentation requirements, preparation milestones and unresolved logistics.

**Starter prompt:**

> Use only speaker-session.md to create speaker-brief.md, under 350 words. Explain the audience, desired learning outcomes and talk boundaries. List supplied submission deadlines and format requirements, followed by a concise preparation checklist. Identify missing details the organizer must confirm. Keep guidance distinct from contractual obligations. Do not invent fees, travel arrangements, recording consent, venue amenities or a speaker biography. Preserve all supplied content restrictions.

**Validation / approval:** Check timing, deadlines and requirements against the source and resolve logistics placeholders. A human program owner must approve the brief before sending it to a speaker or treating any proposed requirement as agreed.

<a id="uc-043"></a>
## 043. Sponsor deliverables checklist.

**Mode:** `swarm-claude`

**Inputs:** `sponsor-extract.md` - six synthetic agreed sponsor benefits; `event-inventory.md` - relevant placements, deadlines and responsible role labels.

**Outputs:** `sponsor-checklist.md` - a benefit-to-deliverable checklist showing evidence needed for fulfillment.

**Starter prompt:**

> Use only sponsor-extract.md and event-inventory.md to write sponsor-checklist.md, under 400 words. Map each agreed benefit to a supplied placement or an explicit fulfillment gap. Include owner role, documented deadline and acceptable completion evidence where provided. Distinguish preparing an asset from delivering the benefit. Do not add sponsor rights, promise audience numbers, expose attendee details or mark any benefit fulfilled without supporting evidence.

**Validation / approval:** Account for all six benefits and check placement availability and deadlines manually. A human sponsorship owner must approve the checklist before sharing it with the sponsor, assigning external work or committing to additional benefits.

<a id="uc-044"></a>
## 044. Attendee reminder message.

**Mode:** `swarm-ollama`

**Inputs:** `attendee-logistics.md` - a fictional event's confirmed date, time zone, location or example link, arrival instructions and support route.

**Outputs:** `attendee-reminder.md` - a subject and one reminder message emphasizing essential attendance information.

**Starter prompt:**

> Use only attendee-logistics.md to draft attendee-reminder.md, under 250 words. Present the confirmed date, supplied time zone, arrival or joining instructions and support route clearly. Preserve link placeholders and flag missing access details. Include preparation requirements only when supplied. Do not convert time zones, create calendar invitations, imply registration status or invent parking, transport or accessibility arrangements. Keep the message ready for human verification.

**Validation / approval:** Check date, time zone, venue wording and destination placeholders against confirmed logistics. A human event owner must approve the final message, recipient list and send timing before scheduling or sending it.

<a id="uc-045"></a>
## 045. Session description set.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `session-outlines.md` - three synthetic session outlines, supplied speaker role descriptions, audience levels and approved learning outcomes.

**Outputs:** `session-descriptions.md` - three distinct short descriptions suitable for a draft event program.

**Starter prompt:**

> Use only session-outlines.md to create session-descriptions.md, under 350 words. Write one title and an 80-90 word description for each of the three sessions. Make audience level, topic boundaries and expected learning clear without repeating generic promotional language. Use only supplied speaker credentials. Flag overlaps that could confuse attendees. Do not promise certification, invent hands-on exercises or imply content beyond the supplied outline.

**Validation / approval:** Check word counts, factual credentials and whether descriptions distinguish the sessions accurately. A human program owner and the relevant speakers must approve descriptions before website publication, ticketing updates or promotional distribution.

<a id="uc-046"></a>
## 046. Panel moderator question route.

**Mode:** `swarm-claude`

**Inputs:** `panel-brief.md` - a fictional panel's theme, three participants' stated perspectives, audience questions and prohibited disclosure topics.

**Outputs:** `moderator-route.md` - an opening, six sequenced questions, follow-up cues and a closing prompt.

**Starter prompt:**

> Use only panel-brief.md to write moderator-route.md, under 400 words. Sequence six questions from shared context to meaningful differences and practical takeaways. Direct questions by supplied role labels and balance opportunities to contribute. Include neutral follow-ups that seek examples without assuming disagreement. Respect prohibited topics. Do not invent participant beliefs, quotations or personal experiences. End with a question that helps the audience apply the discussion.

**Validation / approval:** Verify fair role coverage and that questions stay within agreed topics. A human moderator and program owner must approve the route before sharing it with panelists or using it publicly.

<a id="uc-047"></a>
## 047. Audio and video contingency cards.

**Mode:** `swarm-ollama-claude`

**Inputs:** `av-fallbacks.md` - three fictional nonemergency disruptions, venue-approved fallback actions, role ownership and stop conditions.

**Outputs:** `av-cue-cards.md` - one compact cue card per disruption with an announcement and handoff instructions.

**Starter prompt:**

> Use only av-fallbacks.md to create av-cue-cards.md, under 400 words. For each supplied disruption, list the observable trigger, approved fallback, responsible role, audience announcement and stop condition. Keep announcements calm and factual. Flag missing ownership or incompatible actions. Do not invent technical repair steps, operate equipment or write emergency procedures. These cards cover only the three supplied audio or video interruptions.

**Validation / approval:** Check every action against venue-approved fallbacks and rehearse role handoffs. A human technical producer must approve the cards before crew distribution or live use, including confirmation that stop conditions match actual venue procedures.

<a id="uc-048"></a>
## 048. Accessibility logistics review.

**Mode:** `swarm-gpt`

**Inputs:** `access-requirements.md` - a short fictional event access checklist; `venue-extract.md` - supplied venue and platform facts without attendee identities.

**Outputs:** `access-logistics-review.md` - a requirement-to-evidence table with unanswered questions and responsible role suggestions.

**Starter prompt:**

> Use only access-requirements.md and venue-extract.md to create access-logistics-review.md, under 450 words. Mark each supplied requirement documented, partly documented or unknown. Reference the relevant venue fact and list a concrete verification question for every gap. Preserve conditions and exceptions. Do not certify accessibility, infer an attendee's needs or invent venue capabilities. Keep recommendations limited to clarifying and checking the supplied requirements.

**Validation / approval:** A human must verify venue and platform facts with responsible staff and resolve gaps. The event owner must approve arrangements before communicating access assurances, booking services or publishing accessibility information.

<a id="uc-049"></a>
## 049. Event feedback survey.

**Mode:** `swarm-ollama`

**Inputs:** `survey-objectives.md` - three fictional event learning objectives, two logistics decisions to inform and a maximum survey length.

**Outputs:** `event-survey.md` - eight neutral questions with response options and a question-to-decision map.

**Starter prompt:**

> Use only survey-objectives.md to create event-survey.md, under 450 words. Draft eight questions covering the stated objectives and logistics decisions within the supplied length limit. Use balanced response options and include not applicable where useful. Add one optional free-text question within the eight. Explain which decision each question informs. Do not request identifying or sensitive information, use leading language or claim the instrument is validated.

**Validation / approval:** Check question neutrality, response-option coverage and relevance to decisions. A human research or event owner must approve the survey before building it in a survey system or distributing it to attendees.

<a id="uc-050"></a>
## 050. Event debrief.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `event-outcomes.md` - five synthetic aggregate measures with definitions and targets; `crew-observations.md` - six concise fictional operational observations.

**Outputs:** `event-debrief.md` - an evidence-based review with three bounded recommendations for a future event.

**Starter prompt:**

> Use only event-outcomes.md and crew-observations.md to create event-debrief.md, under 450 words. Compare measures with stated targets and identify operational patterns supported by observations. Separate measured results from interpretations and note conflicting evidence. Recommend three specific changes with the evidence each addresses and a verification need. Do not infer attendee sentiment from attendance, claim causal effects or invent cost savings. Keep recommendations proposed, not assigned.

**Validation / approval:** Recheck figures, target comparisons and links between evidence and recommendations. A human event owner must approve conclusions before sponsor reporting, external distribution or commitments to future suppliers and attendees.

[Back to library](README.md)
