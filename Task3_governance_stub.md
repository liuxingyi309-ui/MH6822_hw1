# Task 3: Governance stub

## Tool purpose

This prototype supports PEP screening for AML/KYC onboarding at a global bank such as HSBC. It takes synthetic customer data and produces a risk score, recommended action, jurisdiction-specific requirement, and explanation.

## Assumptions

The synthetic input data is treated as accurate for the purpose of testing the prototype logic. PEP category, relationship to a PEP, adverse media score, sanctions match score, transaction volume, and source-of-funds risk are treated as relevant screening signals.

## Boundaries

The tool does not connect to real sanctions, PEP, or adverse media databases. It does not make final onboarding or account closure decisions, and it does not replace compliance officer judgment.

It also does not verify whether the synthetic customer data is true. The prototype is limited to PEP screening logic and does not cover the full AML compliance stack.

## Failure points

A customer can be incorrectly escalated because of weak adverse media or a name match. A customer can also be under-escalated if the synthetic inputs miss important information.

The jurisdiction configuration can be wrong or outdated. A global threshold can hide local regulatory differences, and the tool can create a false sense of compliance if users treat the score as the final answer.

## Human review

Human review is required when the score crosses the manual review threshold, enhanced due diligence is recommended, senior management approval is recommended, or the PEP/name match confidence is low.

It is also required when the customer is a foreign PEP with adverse media or high source-of-funds risk, or when the case is borderline and the explanation does not fit the compliance officer's judgment.
