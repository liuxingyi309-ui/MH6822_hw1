# Task 3: Tool design

## Chosen option

I chose **Option A: Working Prototype**. For this part, I built a small Python prototype and included the synthetic customer data, generated results, one-page summary, and governance documentation stub.

I chose this option because the project is about showing how jurisdictional rules change the treatment of the same customer profile. A working prototype makes that difference visible in the output. Option B would let me describe the architecture, but the rule differences would still be mostly conceptual. Option C would be useful for a deeper statistical analysis, but my main aim here is to show the core compliance logic in action.

## Tool overview

The tool is called **HSBC PEP Screening: US vs UK**. It supports AML/KYC onboarding by scoring synthetic customers under two jurisdiction settings: the United States and the United Kingdom.

The tool does not connect to real PEP, sanctions, or adverse media databases. It uses synthetic data so that the logic can be demonstrated without using real customer information.

## Input data

The input file is `data/Task3_data.csv`. Each row represents one synthetic customer. The fields include:

- customer ID and name
- country of residence
- occupation
- PEP category
- relationship to a PEP
- adverse media score
- sanctions match score
- monthly transaction volume
- source-of-funds risk
- name match confidence

These fields are simplified, but they are meant to resemble the kinds of signals that an AML/KYC team might review during onboarding.

## Jurisdiction configuration layer

The jurisdiction configuration layer is inside `Task3_tool.py`. The prototype stores the US and UK settings separately in `JURISDICTION_CONFIGS`, so the scoring logic can call the active jurisdiction instead of using one global rule.

The configuration layer includes different point values, review thresholds, and jurisdiction-specific documentation requirements. This is where the tool knows whether it is applying the US or UK version of the screening logic.

## Output

The output file is `Task3_results.csv`. For each customer, the tool generates one US result and one UK result. The output includes:

- jurisdiction
- risk score
- recommended action
- whether human review is required
- jurisdiction-specific requirement
- explanation

The output changes depending on which jurisdiction is active. The score can change, the explanation can change, and the documentation requirement can change. That is the main way the prototype shows jurisdiction awareness rather than just applying one generic PEP screening checklist.

For example, a domestic PEP with low transaction risk can remain under standard due diligence, while the UK output still documents the proportionality assessment. A foreign PEP with adverse media, high transaction volume, and high source-of-funds risk is escalated for enhanced due diligence and senior management approval.

## Why is this product right for the company?

This product fits the hypothetical RegTech company because the company focuses on rule configuration, risk scoring, audit trails, and workflow design. It is not trying to sell a full AML compliance suite. It is trying to solve a narrower problem: how a global bank can apply different jurisdictional expectations in a clearer and more consistent way.

HSBC is also the right kind of client for this tool. A smaller domestic bank may not need this level of jurisdictional configuration, but HSBC operates across markets and has to manage similar AML/KYC risks under different legal and supervisory expectations.

## What problem does this tool solve that a memo or spreadsheet cannot?

A memo can describe the difference between US and UK rules, but it does not apply those differences consistently to individual customers. A spreadsheet can store customer data, but the reasoning behind each escalation can easily become hidden in formulas or manual notes.

This prototype keeps the jurisdiction setting, risk score, recommendation, and explanation together. That lets a compliance officer see not only the result, but also why the result was produced.

## What regulatory divergence does it handle, and how?

The tool handles the difference between the US and UK treatment of PEP risk. In the US configuration, PEP status alone does not automatically trigger enhanced due diligence. The tool therefore looks at the wider risk profile, including source-of-funds risk, adverse media, sanctions match strength, and transaction volume.

In the UK configuration, the tool gives more explicit weight to proportionality. It separates lower-risk and higher-risk PEP relationships and records when a proportionality assessment is required. This means the same customer can produce a different explanation or documentation requirement depending on whether the US or UK setting is active.

## What does it not do, and why?

The tool does not make final onboarding or rejection decisions. It does not replace compliance judgment, and it does not claim that the score is the same thing as legal compliance. I made this boundary choice because PEP screening still requires human judgment, especially when the case is borderline or the data is uncertain.

It also does not cover the entire AML/KYC process. It focuses only on PEP screening logic across the US and UK. Sanctions screening, beneficial ownership, transaction monitoring, and suspicious activity reporting would need deeper treatment in a real system.

## Failure modes

The most important failure mode is jurisdictional misconfiguration. If the US and UK settings are wrong, outdated, or treated as interchangeable, the tool can produce a confident-looking output while applying the wrong regulatory logic.

Other failure modes include weak synthetic inputs, low-confidence name matches, over-reliance on adverse media, and treating the score as a final answer. The prototype addresses this by including human review triggers and a separate governance stub.
