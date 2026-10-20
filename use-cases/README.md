# 200 ways to put Swarms to work.

[Back to Swarms](../README.md) · [How to run a recipe](../toolkit/docs/running-a-use-case.md) · [Measure your results](../toolkit/docs/measuring-results.md)

Choose a job, prepare the named text inputs and adapt the starter prompt.
Each recipe defines a concrete file to produce and checks before you use it.
These are candidate workflows to try, not 200 benchmarked successes.

**20 categories · 10 distinct recipes each · all five swarm modes**

## Reach customers.

- [Marketing and content](marketing.md) · 001-010
- [Sales](sales.md) · 011-020
- [Customer success](customer-success.md) · 021-030
- [E-commerce](ecommerce.md) · 031-040
- [Events](events.md) · 041-050

## Build and learn.

- [Product management](product.md) · 051-060
- [Software engineering](software.md) · 061-070
- [Data and analytics](data.md) · 071-080
- [Design](design.md) · 081-090
- [Research](research.md) · 091-100

## Run the organisation.

- [Operations](operations.md) · 101-110
- [People and teams](people.md) · 111-120
- [Finance administration](finance.md) · 121-130
- [Procurement](procurement.md) · 131-140
- [Leadership](leadership.md) · 141-150

## Work in your industry.

- [Education](education.md) · 151-160
- [Nonprofits](nonprofits.md) · 161-170
- [Property](property.md) · 171-180
- [Hospitality](hospitality.md) · 181-190
- [Manufacturing](manufacturing.md) · 191-200

## Read a recipe.

| Field | What you get |
| --- | --- |
| Mode | A suitable provider combination to start with |
| Inputs | The short, explicit text files you must prepare |
| Outputs | The concrete artifacts the prompt asks for |
| Starter prompt | A bounded task to paste into the goal argument |
| Validation / approval | Acceptance checks and the decision a person retains |

A mode recommendation is illustrative, not evidence that one provider is best
at that job. Switch to another installed mode if appropriate for your data and
account. Hybrid modes send selected context and generated artifacts to their
cloud planner and reviewer. `swarm-ollama` is a local inference path only when
its selected model is verified local and cloud use is not enabled.

## Keep the inputs small and the outcome real.

Use synthetic, public or appropriately authorised data. Every file named under
**Inputs** must be selected with `--context`; a filename in the prompt does not
make the toolkit read it. The default reader limits each file to 6,000 UTF-8 bytes and the combined
selected text to 6,000 characters. Ollama has a separate, smaller full-prompt
guard at default settings, which must also fit the instructions, plan and,
during review, generated files. Start with a small sample and a reduced output
cap; the recipe's upper bound is not a fit guarantee.
[Read the budget and one-task guidance](../toolkit/docs/running-a-use-case.md#1-prepare-a-small-text-brief).
Export only the needed text from PDFs, workbooks, websites or apps yourself.

Swarms drafts text files. It does not browse sources, inspect images, connect to
accounts, send messages, make decisions about people, execute transactions or
deploy anything. For a recipe involving those activities, the deliverable is
preparation for an authorised person, not the external action itself. Qualified
review remains essential where the underlying work requires it.

Results are staged by default. Inspect the artifacts and independently check
their facts or behaviour. Applying files and running user-authored commands are
separate opt-ins. [Follow the run guide →](../toolkit/docs/running-a-use-case.md)

[Back to Swarms](../README.md)
