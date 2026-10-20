# Finance.

[Library](README.md) · [Run a use case](../toolkit/docs/running-a-use-case.md)

Draft finance explanations, evidence checklists and review questions from synthetic examples. Every result requires an authorized, qualified finance reviewer; no job approves payments, changes records or provides financial advice. Start with a small text brief and follow the [input and output budget guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief); file-loading limits do not guarantee that a full model request will fit. Outputs are privately staged text, and example modes do not guarantee local processing.

- [121. Budget variance commentary](#uc-121)
- [122. Month-end close evidence map](#uc-122)
- [123. Expense documentation checklist](#uc-123)
- [124. Invoice discrepancy note](#uc-124)
- [125. Cash forecast assumptions register](#uc-125)
- [126. Account coding clarification guide](#uc-126)
- [127. Audit evidence request index](#uc-127)
- [128. Financial metric glossary](#uc-128)
- [129. Reconciliation investigation checklist](#uc-129)
- [130. Finance approval matrix gap review](#uc-130)

<a id="uc-121"></a>
## 121. Budget variance commentary.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `variance-example.md` - five synthetic budget lines with periods, currencies and precomputed variances; `owner-notes.md` - fictional explanations labeled as confirmed, tentative or unknown.

**Outputs:** `variance-commentary.md` - a short management commentary separating reported movements from possible explanations.

**Starter prompt:**

> Draft variance-commentary.md from variance-example.md and owner-notes.md, under 500 words. Preserve the supplied figures, units, signs and periods without recalculating them. Cite line IDs and separate confirmed explanations from hypotheses. Flag missing explanations and inconsistent labels. Do not invent causes, forecast results or recommend spending decisions.

**Validation / approval:** A qualified finance reviewer independently checks figures and verifies explanations with authorized owners. The report owner approves the commentary before circulation or use in budgeting, and unresolved causes remain explicitly open.

<a id="uc-122"></a>
## 122. Month-end close evidence map.

**Mode:** `swarm-claude`

**Inputs:** `close-checklist.md` - a fictional close procedure with task IDs and approval roles; `evidence-example.md` - a synthetic inventory of available evidence, dates and missing documents.

**Outputs:** `close-evidence-map.md` - a task-to-evidence table with gaps and review dependencies.

**Starter prompt:**

> Use close-checklist.md and evidence-example.md to produce close-evidence-map.md, under 550 words. Map each close task to supplied evidence and the documented review role. Distinguish evidence listed from evidence actually reviewed. Flag missing dates, unsupported completion claims and dependencies. Do not certify the close, post entries or mark controls complete.

**Validation / approval:** A qualified accountant verifies every mapping and inspects actual evidence separately. The authorized controller approves any close status or record changes; the generated map alone is not proof that a control operated.

<a id="uc-123"></a>
## 123. Expense documentation checklist.

**Mode:** `swarm-ollama`

**Inputs:** `expense-policy.md` - a generic policy excerpt listing documentation and exception requirements; `expense-examples.md` - five synthetic claims with fictional dates, amounts and receipt descriptions.

**Outputs:** `expense-documentation.md` - completeness checks and neutral follow-up questions for the sample claims.

**Starter prompt:**

> Create expense-documentation.md from expense-policy.md and expense-examples.md in at most 500 words. Check only whether required documentation is described. Cite the relevant rule and sample ID for each gap, then draft a clarification question. Preserve uncertainties about receipts. Do not decide reimbursement eligibility, infer misconduct, approve a claim or initiate payment.

**Validation / approval:** A qualified finance reviewer confirms requirements and independently inspects supporting records. The authorized expense owner approves any claimant communication and separately decides reimbursement through the established approval process.

<a id="uc-124"></a>
## 124. Invoice discrepancy note.

**Mode:** `swarm-gpt`

**Inputs:** `invoice-example.md` - one synthetic invoice with line IDs, quantities, rates and stated totals; `order-extract.md` - the corresponding fictional order terms and expected references.

**Outputs:** `invoice-query-draft.md` - an internal discrepancy table and a short unsent clarification note.

**Starter prompt:**

> Use invoice-example.md and order-extract.md to draft invoice-query-draft.md, under 500 words. Identify visible differences in identifiers, quantities, rates and stated terms without asserting fraud or recalculating totals. Reference source line IDs and distinguish discrepancies from missing information. Add a neutral clarification note. Do not contact a supplier, change records or authorize payment.

**Validation / approval:** A qualified accounts payable reviewer checks all values and terms independently. The authorized invoice owner approves the note before sending and separately authorizes any payment or adjustment.

<a id="uc-125"></a>
## 125. Cash forecast assumptions register.

**Mode:** `swarm-ollama-claude`

**Inputs:** `forecast-example.md` - a synthetic forecast excerpt with precomputed figures and labeled assumptions; `scenario-notes.md` - fictional timing uncertainties, dependencies and source owners.

**Outputs:** `forecast-assumptions.md` - a register of assumptions, supporting sources and questions requiring validation.

**Starter prompt:**

> Draft forecast-assumptions.md from forecast-example.md and scenario-notes.md, under 550 words. Connect each stated assumption to its source, affected line and unresolved timing question. Preserve supplied figures and clearly separate assumptions from observed facts. Flag contradictions without choosing a preferred scenario. Do not calculate projections or recommend financing, investment, payment or borrowing decisions.

**Validation / approval:** A qualified finance professional verifies assumptions and independently validates the underlying forecast. The authorized treasury owner approves any subsequent forecast release or financial decision; this register supplies questions only.

<a id="uc-126"></a>
## 126. Account coding clarification guide.

**Mode:** `swarm-ollama-gpt`

**Inputs:** `account-definitions.md` - six fictional account definitions and documented boundaries; `transaction-examples.md` - five synthetic descriptions containing deliberate classification ambiguities.

**Outputs:** `coding-questions.md` - clarification questions linked to the supplied account definitions.

**Starter prompt:**

> Use account-definitions.md and transaction-examples.md to create coding-questions.md, under 500 words. Identify which supplied definition boundaries are unclear for each example and ask for the facts needed to resolve them. Cite definition labels and preserve ambiguity. Do not assign final account codes, invent accounting policy, recommend tax treatment or create journal entries.

**Validation / approval:** A qualified accountant checks that each question is relevant and that definitions are current and authorized. Only the authorized finance team determines accounting treatment and approves any posting after reviewing the underlying evidence.

<a id="uc-127"></a>
## 127. Audit evidence request index.

**Mode:** `swarm-claude`

**Inputs:** `audit-requests.md` - six fictional requests with scope, period and evidence type; `document-inventory.md` - a synthetic list of document labels, owners and described coverage.

**Outputs:** `audit-evidence-index.md` - a draft request-to-document index with missing coverage and owner questions.

**Starter prompt:**

> Create audit-evidence-index.md from audit-requests.md and document-inventory.md, under 550 words. Match requests to documents only where the described period and scope align. Mark partial or uncertain matches and list missing evidence. Use inventory labels without claiming to have inspected underlying files. Do not certify compliance, fabricate evidence or send documents externally.

**Validation / approval:** A qualified finance reviewer confirms matches and inspects original evidence. Authorized audit and document owners approve completeness, confidentiality and recipient scope before any response or external disclosure.

<a id="uc-128"></a>
## 128. Financial metric glossary.

**Mode:** `swarm-gpt`

**Inputs:** `metric-definitions.md` - six fictional internal metric definitions with units and exclusions; `report-captions.md` - synthetic report labels and supplied explanatory notes.

**Outputs:** `finance-glossary.md` - concise definitions and suggested footnotes for ambiguous report labels.

**Starter prompt:**

> Use metric-definitions.md and report-captions.md to draft finance-glossary.md in at most 500 words. Explain each metric using only its supplied definition, retaining units, time basis and exclusions. Identify inconsistent captions and draft clarifying footnotes. Flag missing definitions rather than applying an assumed standard. Do not calculate metrics or provide investment interpretations.

**Validation / approval:** A qualified finance reviewer checks definitions, units and any distinction between internal and externally reported measures. The report owner approves glossary text before distribution or use in a published financial report.

<a id="uc-129"></a>
## 129. Reconciliation investigation checklist.

**Mode:** `swarm-ollama`

**Inputs:** `reconciliation-example.md` - a synthetic exception list with precomputed differences and source references; `investigation-procedure.md` - generic evidence checks and escalation rules.

**Outputs:** `reconciliation-questions.md` - an exception-by-exception investigation checklist with unresolved evidence needs.

**Starter prompt:**

> Draft reconciliation-questions.md from reconciliation-example.md and investigation-procedure.md, under 550 words. For each labeled exception, list the supplied procedure checks, referenced records and missing evidence. Keep timing explanations tentative unless explicitly confirmed. Preserve precomputed differences without recalculation. Do not match transactions automatically, decide write-offs, amend balances or propose unsupported journal entries.

**Validation / approval:** A qualified accountant independently verifies differences and checks original records before accepting an explanation. The authorized finance owner approves any correction, write-off or journal entry through the normal control process.

<a id="uc-130"></a>
## 130. Finance approval matrix gap review.

**Mode:** `swarm-ollama-claude`

**Inputs:** `approval-policy.md` - a fictional authority policy with thresholds, currencies and exceptions; `approval-matrix.md` - a synthetic role matrix with deliberate gaps or conflicting limits.

**Outputs:** `approval-gap-review.md` - a source-referenced list of gaps, conflicts and governance questions.

**Starter prompt:**

> Use approval-policy.md and approval-matrix.md to create approval-gap-review.md, under 550 words. Compare documented thresholds, currencies, exception routes and role boundaries. Cite both sources for conflicts and identify missing coverage. Ask clarifying questions without choosing a new limit or approver. Do not change permissions, approve transactions or infer delegated authority.

**Validation / approval:** A qualified finance governance reviewer verifies each discrepancy. The authorized policy owner approves any revised matrix or delegation before publication, access changes or use in transaction approvals.

[Back to library](README.md)
