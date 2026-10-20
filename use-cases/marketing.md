# Marketing.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

These examples turn small synthetic marketing briefs into staged text for human review. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each goal produces one short artifact without browsing, app access or campaign execution. Mode choices are suitable examples, not evidence of superiority.

- [001. Message evidence matrix](#uc-001)
- [002. Landing page experiment brief](#uc-002)
- [003. Buyer question content gaps](#uc-003)
- [004. Newsletter issue draft](#uc-004)
- [005. Campaign link tagging specification](#uc-005)
- [006. Partner announcement draft](#uc-006)
- [007. Two-week editorial schedule](#uc-007)
- [008. Podcast sponsorship script](#uc-008)
- [009. Referral program explainer](#uc-009)
- [010. Campaign retrospective](#uc-010)

<a id="uc-001"></a>
## 001. Message evidence matrix.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `message-evidence.md` - five proposed claims, approved supporting facts and the intended audience for a fictional product.

**Outputs:** `message-matrix.md` - a claim-by-claim table showing evidence, limits and safe wording.

**Starter prompt:**

> Use only message-evidence.md to create message-matrix.md, under 350 words. Map each proposed claim to supplied evidence. Label unsupported or partly supported claims, preserve numerical qualifiers, and suggest narrower wording where possible. Distinguish product facts from expected customer outcomes. Do not invent proof, testimonials or comparisons. Keep unresolved claims visibly blocked for review.

**Validation / approval:** Match every supported statement to an input fact and check that caveats survive the rewrite. A human marketing owner must approve claims before they appear in advertising, a website or sales materials.

<a id="uc-002"></a>
## 002. Landing page experiment brief.

**Mode:** `swarm-claude`

**Inputs:** `page-test.md` - one fictional page section, a user friction hypothesis, one desired action and available aggregate measurements.

**Outputs:** `page-experiment.md` - a single-change test proposal with control, variant and a measurement checklist.

**Starter prompt:**

> Use only page-test.md to write page-experiment.md, under 400 words. Propose one change to the supplied section and explain the user behavior it is intended to affect. Include control and variant copy, the primary measure, guardrails, and unanswered questions about test duration or sample size. Do not predict uplift or claim statistical significance. Leave traffic allocation unset.

**Validation / approval:** Confirm the proposal changes one factor and the available measures can observe the intended action. A human experiment owner must approve the design and any live page or traffic changes before launch.

<a id="uc-003"></a>
## 003. Buyer question content gaps.

**Mode:** `swarm-ollama-claude`

**Inputs:** `buyer-questions.md` - six synthetic questions with purchase stages; `content-summaries.md` - four short summaries of existing fictional articles.

**Outputs:** `content-gap-map.md` - a coverage table and three narrowly scoped content briefs.

**Starter prompt:**

> Use only buyer-questions.md and content-summaries.md to create content-gap-map.md, under 450 words. Mark each question as covered, partly covered or absent based on the summaries. Propose three distinct briefs for the largest documented gaps, each with a target question, outline and evidence needed. Treat summaries as incomplete evidence, not full articles. Do not invent search volume or keyword rankings.

**Validation / approval:** Ensure every proposed brief resolves a listed question and existing coverage is not overstated. A human editor must approve priorities and factual content before commissioning or publishing articles.

<a id="uc-004"></a>
## 004. Newsletter issue draft.

**Mode:** `swarm-ollama`

**Inputs:** `newsletter-brief.md` - three approved fictional updates, supplied link labels, audience, tone and one desired reader action.

**Outputs:** `newsletter-issue.md` - a subject, preview line, short opening, three updates and one closing action.

**Starter prompt:**

> Use only newsletter-brief.md to write newsletter-issue.md, under 320 words. Assemble one coherent issue with a subject under 50 characters and a preview line under 90 characters. Preserve supplied link labels as placeholders. Give each update a distinct purpose and use one closing action. Flag missing destinations instead of inventing URLs. Do not add offers, deadlines or personalization facts.

**Validation / approval:** Check character limits, update accuracy and the consistency of the requested action. A human newsletter owner must approve copy, destinations and the intended recipient list before scheduling or sending.

<a id="uc-005"></a>
## 005. Campaign link tagging specification.

**Mode:** `swarm-gpt`

**Inputs:** `campaign-links.md` - four example.com destinations, placement names, a fictional campaign identifier and existing naming rules.

**Outputs:** `link-tagging-spec.md` - proposed source, medium, campaign and content values for each placement.

**Starter prompt:**

> Use only campaign-links.md to create link-tagging-spec.md, under 350 words. Produce one row per placement with its original destination and proposed tagging values. Follow the supplied capitalization and separator rules. Identify duplicate labels, missing conventions and destinations that already contain query parameters. Describe verification steps without fetching URLs or asserting that links work. Keep personal identifiers out of every value.

**Validation / approval:** Check naming consistency, placement uniqueness and preservation of existing parameters. A human analytics owner must approve the specification and verify assembled URLs before anyone adds links to a live campaign.

<a id="uc-006"></a>
## 006. Partner announcement draft.

**Mode:** `swarm-claude`

**Inputs:** `partner-facts.md` - approved synthetic relationship facts, each party's contribution, prohibited claims and a proposed announcement audience.

**Outputs:** `partner-announcement.md` - a concise announcement with a factual headline and clear relationship boundaries.

**Starter prompt:**

> Use only partner-facts.md to draft partner-announcement.md, under 300 words. Explain what the two fictional organizations are doing together, who benefits and what is available now. Separate current scope from future intentions. Include an unresolved-items list for any missing launch date or destination. Do not invent quotes, endorsements, commercial terms or exclusivity. Preserve the supplied prohibited-claim restrictions.

**Validation / approval:** Confirm each party's contribution is accurate and no future intention reads as a commitment. Human representatives of both organizations must approve names, wording and timing before publication or distribution.

<a id="uc-007"></a>
## 007. Two-week editorial schedule.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `editorial-constraints.md` - four approved themes, two channels, six available publishing slots and fictional production capacity limits.

**Outputs:** `editorial-schedule.md` - six proposed posts with audience purpose, format and preparation dependencies.

**Starter prompt:**

> Use only editorial-constraints.md to create editorial-schedule.md, under 400 words. Assign six distinct post ideas to the supplied two-week slots. Respect channel and production limits, avoid repeating the same theme consecutively, and identify needed source material for each idea. Use role labels rather than people. Mark any scheduling conflict instead of adding capacity. Produce a proposed schedule only, with no full post drafts.

**Validation / approval:** Verify slot counts, capacity limits and feasible preparation order. A human editor must approve assignments, final content and publication dates before entering or activating the schedule in a publishing system.

<a id="uc-008"></a>
## 008. Podcast sponsorship script.

**Mode:** `swarm-ollama-claude`

**Inputs:** `sponsor-read.md` - a fictional product's approved facts, audience, sponsorship disclosure, pronunciation notes and one supplied offer.

**Outputs:** `podcast-read.md` - a roughly 60-second host script and a short pronunciation note.

**Starter prompt:**

> Use only sponsor-read.md to create podcast-read.md. Write a 120-150 word spoken script plus pronunciation notes, keeping the full file under 220 words. Include the supplied sponsorship disclosure and exact offer limits. Use a natural transition, one concrete product explanation and one action. Do not imply that the host personally uses the product or has achieved results unless explicitly stated.

**Validation / approval:** Read the script aloud to assess timing and check offer details and attribution. A human sponsor owner and the host must approve the script before recording, endorsing or broadcasting it.

<a id="uc-009"></a>
## 009. Referral program explainer.

**Mode:** `swarm-gpt`

**Inputs:** `referral-terms.md` - concise fictional program rules covering eligibility, qualifying actions, reward limits, exclusions and expiry.

**Outputs:** `referral-explainer.md` - a plain-language explanation and four questions answered from those rules.

**Starter prompt:**

> Use only referral-terms.md to create referral-explainer.md, under 350 words. Explain who qualifies, what must happen, when a reward becomes eligible and which limits apply. Add four practical questions with answers grounded in the supplied terms. Keep conditions beside the relevant reward statement. If rules conflict or omit a detail, flag it for the owner rather than resolving it yourself.

**Validation / approval:** Compare every reward and eligibility statement with the source and check exceptions remain visible. A human program owner must approve interpretation and customer-facing copy before publication or use in referral invitations.

<a id="uc-010"></a>
## 010. Campaign retrospective.

**Mode:** `swarm-ollama`

**Inputs:** `campaign-results.md` - a small synthetic table of goals, dates and aggregate results for three placements, plus known delivery issues.

**Outputs:** `campaign-retro.md` - a short assessment separating observed results, possible explanations and next questions.

**Starter prompt:**

> Use only campaign-results.md to write campaign-retro.md, under 400 words. Compare supplied results with their stated goals and identify two decisions worth reviewing. Keep facts separate from hypotheses, preserve measurement windows and note missing denominators or inconsistent definitions. Do not attribute causality to placement differences or forecast future returns. Recommend one bounded follow-up investigation using information a human would need to gather.

**Validation / approval:** Recheck copied figures and any arithmetic, and confirm comparable periods are used. A human campaign owner must approve conclusions before external reporting or changes to campaign spending.

[Back to library](README.md)
