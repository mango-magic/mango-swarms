# Data.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Work from small schemas, anonymized examples, and supplied aggregates. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. These jobs produce reviewable text, not database changes, live analysis or executed validation.

- [071. Build a column dictionary](#uc-071)
- [072. Map category normalization](#uc-072)
- [073. Investigate missing values](#uc-073)
- [074. Reconcile a tiny extract](#uc-074)
- [075. Define cohort membership](#uc-075)
- [076. Map transformation lineage](#uc-076)
- [077. Draft synthetic edge cases](#uc-077)
- [078. Inspect join cardinality](#uc-078)
- [079. Draft an analysis decision plan](#uc-079)
- [080. Annotate a metric disruption](#uc-080)

<a id="uc-071"></a>
## 071. Build a column dictionary.

**Mode:** `swarm-ollama`

**Inputs:** `schema.md` - definitions, units, and constraints for twelve columns; `sample.csv` - six anonymized example rows.

**Outputs:** `data-dictionary.md` - documented column meanings separated from inferred ones.

**Starter prompt:**

> Read schema.md and sample.csv. Write only data-dictionary.md, within 650 words. Record meaning, type, unit, allowed nulls, constraints, and one example for each column. Label meanings inferred from examples and question ambiguous names. Do not treat observed values as an exhaustive domain, invent key uniqueness, or profile external data. Cover only the supplied columns.

**Validation / approval:** Compare names and constraints with the schema and verify faithful transcription of examples. The dataset owner must resolve inferred definitions and approve the dictionary before external use or publication in a catalog.

<a id="uc-072"></a>
## 072. Map category normalization.

**Mode:** `swarm-ollama-claude`

**Inputs:** `values.csv` - twenty distinct category strings and counts; `vocabulary.md` - approved canonical labels and matching rules.

**Outputs:** `normalization-map.csv` - raw-to-canonical mappings with rationale and review status.

**Starter prompt:**

> Use values.csv and vocabulary.md to write only normalization-map.csv. Include one row per raw value with raw_value, canonical_value, rationale, and review_status columns. Apply only supplied rules. Leave canonical_value empty for ambiguous or unmatched values and mark them for review. Preserve raw spelling and quote CSV fields correctly. Do not merge categories merely because strings look similar or transform source data.

**Validation / approval:** Check one-to-one coverage of raw values and inspect proposed merges against the vocabulary. A data steward must approve ambiguous mappings before external use or application to a dataset.

<a id="uc-073"></a>
## 073. Investigate missing values.

**Mode:** `swarm-gpt`

**Inputs:** `missingness.md` - a supplied profile of three fields by period and source; `collection.md` - collection rules and known process changes.

**Outputs:** `missingness-plan.md` - a ranked investigation plan for reported missingness.

**Starter prompt:**

> Read missingness.md and collection.md. Write only missingness-plan.md, within 550 words. Identify three competing explanations at most. Give each supporting evidence, a discriminating check, and a result that would weaken it. Separate structural absence from unexpected missingness where rules permit. Do not infer a statistical missingness mechanism from aggregates alone or recommend imputation without further evidence.

**Validation / approval:** Verify each explanation has a distinct feasible check and that supplied aggregates are quoted accurately. The analyst must approve the investigation before external use or commissioning data access or remediation.

<a id="uc-074"></a>
## 074. Reconcile a tiny extract.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `source.csv` - eight anonymized IDs and amounts; `target.csv` - the corresponding small export using identical units.

**Outputs:** `reconciliation.md` - a row-level discrepancy ledger and bounded summary.

**Starter prompt:**

> Compare source.csv and target.csv and write only reconciliation.md, within 500 words. Match records by unique ID. List missing, extra, or duplicate IDs and unequal amounts, quoting both values for differences. Show arithmetic explicitly and separate unmatched rows from matched-value discrepancies. Do not assume one source is authoritative, repair records, extrapolate error rates, or claim reconciliation beyond these extracts.

**Validation / approval:** Independently verify each row match and recompute arithmetic from the extracts. The data owner must approve the discrepancy ledger before external use or corrections to a source system.

<a id="uc-075"></a>
## 075. Define cohort membership.

**Mode:** `swarm-claude`

**Inputs:** `cohort-rules.md` - one cohort's inclusion, exclusion, timezone, and window rules; `examples.csv` - ten fictional boundary cases.

**Outputs:** `cohort-truth-table.md` - membership decisions and explicit rule ambiguities.

**Starter prompt:**

> Use cohort-rules.md and examples.csv to write only cohort-truth-table.md, within 600 words. Classify cases as included, excluded, or unresolved with decisive rules and intermediate date comparisons. Respect supplied timezones, inclusive boundaries, and exclusion precedence. Describe at most three missing boundary cases. Do not silently choose cutoff semantics, calculate cohort statistics, or access participant records.

**Validation / approval:** Manually check dates, boundary inclusivity, and precedence for every case. The metric owner must resolve ambiguous rules and approve the membership definition before external use or implementation against real data.

<a id="uc-076"></a>
## 076. Map transformation lineage.

**Mode:** `swarm-ollama`

**Inputs:** `transformations.md` - eight documented source-to-target transformations with intermediate tables and one source field to trace.

**Outputs:** `lineage.md` - a dependency map with unresolved origins and impact notes.

**Starter prompt:**

> Read transformations.md and write only lineage.md, within 650 words. Link each target field to documented upstream fields and transformation rules in an adjacency table. Identify shared inputs, undocumented origins, and apparent cycles. For the named source field, list downstream fields reachable through supplied rules. Distinguish direct from transitive dependencies. Do not inspect pipelines, infer hidden transformations, or claim complete warehouse coverage.

**Validation / approval:** Trace edges to supplied transformations and manually verify the selected field's downstream paths. The pipeline owner must approve the map before external use or using impact notes to plan changes.

<a id="uc-077"></a>
## 077. Draft synthetic edge cases.

**Mode:** `swarm-gpt`

**Inputs:** `fixture-spec.md` - a tabular schema, constraints, and ten requested edge cases.

**Outputs:** `synthetic-cases.csv` - a fictional fixture of at most fifteen labeled rows.

**Starter prompt:**

> Use fixture-spec.md to write only synthetic-cases.csv, with at most fifteen data rows. Include case_id and expected_validity alongside specified fields. Create fictional values covering boundaries and intentional invalid cases. Make invalidity explicit in case labels and avoid personal identifiers. Use consistent CSV quoting and requested empty-field conventions. Do not copy production records, run validation, or claim the fixture proves schema correctness.

**Validation / approval:** Check coverage of every requested case and confirm only intentionally invalid rows violate the specification. A human must run separate validation checks and approve the fixture before external use or automated-suite inclusion.

<a id="uc-078"></a>
## 078. Inspect join cardinality.

**Mode:** `swarm-ollama-claude`

**Inputs:** `join-samples.md` - two tables totaling twelve rows and their proposed join; `grain.md` - intended output grain and key assumptions.

**Outputs:** `join-audit.md` - a manual cardinality walkthrough and proposed safeguards.

**Starter prompt:**

> Read join-samples.md and grain.md. Write only join-audit.md, within 600 words. Enumerate matches by key and show where one-to-many or many-to-many matches change the intended grain. State how null keys and unmatched rows behave under the proposed join. Suggest uniqueness checks without treating the sample as proof. Do not execute SQL or inspect a database.

**Validation / approval:** Independently enumerate example matches and confirm every claimed multiplication. An analyst must approve safeguards before external use or applying the join to full data; full-dataset cardinality remains unverified.

<a id="uc-079"></a>
## 079. Draft an analysis decision plan.

**Mode:** `swarm-claude`

**Inputs:** `study.md` - one nonclinical question, sampling design, measures, and comparison; `constraints.md` - analysis constraints and predeclared exclusions.

**Outputs:** `analysis-plan.md` - an analysis decision tree with unresolved assumptions.

**Starter prompt:**

> Read study.md and constraints.md. Write only analysis-plan.md, within 650 words. Define analysis unit, target comparison, candidate method, required assumptions, and checks before method selection. Preserve predeclared exclusions and separate exploratory follow-ups. Identify dependence, missingness, or measurement issues preventing the comparison. Do not invent observations, compute significance, assert causality, or execute analysis.

**Validation / approval:** Check that the method matches sampling unit and outcome type, and inspect unresolved assumptions with a qualified analyst. The research owner must approve the plan before external use or analysis of study results.

<a id="uc-080"></a>
## 080. Annotate a metric disruption.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `metric-snapshot.md` - a short metric series, definitions, and reporting windows; `change-log.md` - collection changes and outage intervals.

**Outputs:** `metric-annotation.md` - a dashboard annotation explaining comparability limits.

**Starter prompt:**

> Use metric-snapshot.md and change-log.md to write only metric-annotation.md, at most 350 words. Identify affected windows and distinguish observed movement from possible collection effects. Draft one annotation with supporting source IDs and unresolved questions. Preserve dates and units. Do not attribute causality without evidence, recalculate the series, edit a dashboard, or claim the underlying problem is fixed.

**Validation / approval:** Verify affected intervals against both files and ensure uncertainty is accurately described. The metric owner must approve wording before external use or addition to a stakeholder dashboard.

[Back to library](README.md)
