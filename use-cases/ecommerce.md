# Ecommerce.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

These examples prepare small store-content and merchandising drafts from synthetic records. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Each run stages one text artifact and cannot access a catalog, verify live stock, change orders or send messages. Mode choices are illustrative, with no comparative performance claim.

- [031. Product detail page copy](#uc-031)
- [032. Catalog attribute normalization](#uc-032)
- [033. Product variant selector](#uc-033)
- [034. Measurement-based size guide](#uc-034)
- [035. Bundle compatibility note](#uc-035)
- [036. Return eligibility decision table](#uc-036)
- [037. Cart reminder draft](#uc-037)
- [038. Stockout alternative comparison](#uc-038)
- [039. Collection ordering proposal](#uc-039)
- [040. Shipping delay FAQ](#uc-040)

<a id="uc-031"></a>
## 031. Product detail page copy.

**Mode:** `swarm-ollama`

**Inputs:** `product-facts.md` - one fictional everyday product's materials, dimensions, included items, care instructions and supported benefits.

**Outputs:** `product-page.md` - a title, short description, five feature bullets and a care section.

**Starter prompt:**

> Use only product-facts.md to create product-page.md, under 350 words. Preserve all supplied measurements and distinguish included items from optional accessories. Translate supported features into clear practical benefits without exaggeration. Include care instructions and flag missing essentials for review. Do not invent certifications, sustainability claims, compatibility, warranties, stock status or customer reviews. Write for someone deciding whether this specific product suits their stated use.

**Validation / approval:** Check dimensions, contents, benefit wording and care details against the input. A human catalog owner must approve factual claims and final copy before publishing a listing or uploading it to a marketplace.

<a id="uc-032"></a>
## 032. Catalog attribute normalization.

**Mode:** `swarm-gpt`

**Inputs:** `catalog-sample.md` - five synthetic SKU records with inconsistent attributes; `attribute-rules.md` - approved field names, units and allowed values.

**Outputs:** `attribute-mapping.md` - proposed normalized values with original values, rule references and unresolved exceptions.

**Starter prompt:**

> Use only catalog-sample.md and attribute-rules.md to create attribute-mapping.md, under 450 words. Preserve SKU identifiers and show before-and-after mappings for affected fields. Apply only explicit normalization rules. Flag missing units, unsupported values or ambiguous abbreviations instead of guessing. Do not merge products, drop original values or generate an import script. Keep the output as a reviewable table for these five records only.

**Validation / approval:** Verify each transformation and confirm every original identifier survives. A human catalog owner must approve mappings and resolve exceptions before manually applying changes or importing any values into a live store.

<a id="uc-033"></a>
## 033. Product variant selector.

**Mode:** `swarm-ollama-claude`

**Inputs:** `variant-facts.md` - three fictional variants, their documented differences, intended uses and shared limitations.

**Outputs:** `variant-selector.md` - a compact comparison table and three choice questions for shoppers.

**Starter prompt:**

> Use only variant-facts.md to write variant-selector.md, under 350 words. Compare the three variants using the same relevant attributes. Draft three questions that help a shopper identify a suitable option from supplied use cases. Include shared limitations and explain tradeoffs without declaring a universal best choice. Flag missing comparison data. Do not infer compatibility, current availability or suitability beyond the documented uses.

**Validation / approval:** Check that comparisons use consistent units and each decision branch follows the supplied facts. A human product owner must approve suitability statements and selector copy before publishing it or using it in customer advice.

<a id="uc-034"></a>
## 034. Measurement-based size guide.

**Mode:** `swarm-claude`

**Inputs:** `size-source.md` - a fictional garment's approved measurement method, three size ranges, units and known fit limitations.

**Outputs:** `size-guide.md` - measurement instructions, a size table and guidance for ambiguous boundary cases.

**Starter prompt:**

> Use only size-source.md to create size-guide.md, under 350 words. Preserve ranges and units exactly. Explain how to take the specified measurements, present the three sizes clearly and identify overlaps or gaps in the ranges. Use the supplied rule for boundary cases; if absent, flag it for clarification. Do not infer body characteristics, convert units without a supplied rule or guarantee fit. Include documented fit limitations.

**Validation / approval:** Independently check measurements, range boundaries and table transcription against the source. A human product owner must approve the guide before publication or use in shopper recommendations.

<a id="uc-035"></a>
## 035. Bundle compatibility note.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `bundle-components.md` - three fictional bundle items and supplied compatibility facts; `bundle-rules.md` - included quantities, exclusions and assembly prerequisites.

**Outputs:** `bundle-note.md` - a contents list, compatibility explanation and visible exclusions.

**Starter prompt:**

> Use only bundle-components.md and bundle-rules.md to create bundle-note.md, under 350 words. Explain how the supplied items work together where compatibility is explicitly documented. List quantities, required additional items and exclusions. Flag any unsupported combination or contradictory prerequisite. Do not infer technical compatibility, promise performance improvements, invent a discount or imply that excluded accessories are included. Keep the draft limited to this one proposed bundle.

**Validation / approval:** Check quantities and each compatibility statement against source facts. A human merchandising owner must approve the contents and compatibility claims before creating the bundle, setting an offer or publishing its description.

<a id="uc-036"></a>
## 036. Return eligibility decision table.

**Mode:** `swarm-gpt`

**Inputs:** `return-rules.md` - concise fictional approved return terms; `return-scenarios.md` - six synthetic scenarios with relevant timing and item-condition facts.

**Outputs:** `return-decision-table.md` - rule-based scenario outcomes with evidence and unresolved exceptions.

**Starter prompt:**

> Use only return-rules.md and return-scenarios.md to write return-decision-table.md, under 450 words. Map each scenario to the exact supplied rule and label it eligible, ineligible or needing human review. Preserve exceptions, identify missing facts and flag contradictory rules. Do not create new conditions, interpret external law, authorize a refund or claim a final customer decision. Keep outcomes provisional for staff review.

**Validation / approval:** Check all six scenarios, rule references and boundary dates manually. A human returns owner must approve interpretations before communicating an outcome, publishing guidance or initiating a return or refund.

<a id="uc-037"></a>
## 037. Cart reminder draft.

**Mode:** `swarm-ollama`

**Inputs:** `cart-message-brief.md` - a fictional cart example, approved product facts, tone, permitted offer and required footer wording.

**Outputs:** `cart-reminder.md` - one subject line and a short message with unresolved fields marked.

**Starter prompt:**

> Use only cart-message-brief.md to create cart-reminder.md, under 220 words. Draft one reminder using the supplied product facts and any explicitly permitted offer. Include required footer wording and placeholders for approved destination links. Avoid invented scarcity, expiry, browsing history or claims that the cart is still available. If no offer is supplied, do not add one. Keep the message suitable for human review before any audience selection.

**Validation / approval:** Verify offer conditions, footer completeness and placeholders. A human lifecycle owner must approve the copy and confirm recipient eligibility before scheduling, activating or sending any reminder.

<a id="uc-038"></a>
## 038. Stockout alternative comparison.

**Mode:** `swarm-ollama-claude`

**Inputs:** `alternative-products.md` - a fictional unavailable item and three alternatives, with dated stock notes, key attributes and known compatibility limits.

**Outputs:** `stockout-options.md` - a comparison of substitutes with explicit differences and checks needed before recommendation.

**Starter prompt:**

> Use only alternative-products.md to create stockout-options.md, under 400 words. Compare the alternatives against the unavailable item's documented purpose using consistent attributes. Explain meaningful compromises and reject any substitution contradicted by supplied compatibility limits. Preserve the date of stock notes and mark availability as unverified. Do not claim equivalence, reserve stock, change an order or assume a shopper accepts a substitute.

**Validation / approval:** Check compatibility, attribute comparisons and dated stock assumptions. A human store owner must verify current availability and approve recommendations before customer contact; any order substitution also requires customer agreement.

<a id="uc-039"></a>
## 039. Collection ordering proposal.

**Mode:** `swarm-claude`

**Inputs:** `collection-brief.md` - five synthetic products, a collection theme, approved inclusion criteria and explicit display constraints.

**Outputs:** `collection-order.md` - a proposed product order with one rationale per position and flagged conflicts.

**Starter prompt:**

> Use only collection-brief.md to write collection-order.md, under 350 words. Order the five products to make the stated collection theme understandable while respecting all supplied constraints. Explain each position using documented attributes. Identify any product that fails an inclusion criterion or makes the requested order impossible. Do not invent sales rankings, margins, customer preferences or conversion predictions. Provide one proposed order without modifying store settings.

**Validation / approval:** Confirm every included product meets the criteria and each display constraint is respected. A human merchandising owner must approve the order and verify live product details before changing a storefront collection.

<a id="uc-040"></a>
## 040. Shipping delay FAQ.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `shipping-update.md` - fictional affected order groups, verified delay facts, approved customer options and the next planned update time.

**Outputs:** `shipping-faq.md` - five concise answers explaining the known situation and available next steps.

**Starter prompt:**

> Use only shipping-update.md to create shipping-faq.md, under 400 words. Answer who is affected, what is known, what remains uncertain, what customers can do and when another update is planned. Preserve distinctions between estimated and confirmed dates. Do not invent tracking information, carrier explanations, refunds or delivery guarantees. Use placeholders for missing approved contact routes and flag contradictions for the operations owner.

**Validation / approval:** Verify affected groups, options and date qualifiers against the supplied update. A human operations owner must approve the FAQ and confirm it remains current before website publication or customer distribution.

[Back to library](README.md)
