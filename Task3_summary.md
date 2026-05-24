# Task 3: One-page summary

## HSBC PEP Screening: US vs UK

For Task 3, I chose **Option A: Working Prototype**. I built a small Python prototype for a jurisdiction-aware AML/KYC PEP screening tool for HSBC. The aim is not to build a production system, but to show how the same customer profile can be assessed differently when the US or UK setting is active.

The tool uses synthetic onboarding data. Each record includes simplified risk signals such as PEP category, relationship to a PEP, adverse media score, sanctions match score, transaction volume, source-of-funds risk, and name match confidence. No real customer data is used.

The prototype has two jurisdiction settings. The US setting reflects a risk-based approach where PEP status alone does not automatically trigger enhanced due diligence. The UK setting gives more explicit weight to proportionality, especially in how lower-risk and higher-risk PEP relationships are separated.

For each customer, the tool produces a risk score, recommended action, human review flag, jurisdiction-specific requirement, and explanation. It does not only say approve or reject. The same customer can receive a different score, explanation, or documentation requirement depending on which jurisdiction is active.

This is useful because a memo can describe US/UK differences, and a spreadsheet can store customer inputs, but neither is very good at showing how jurisdiction-specific rules change the treatment of individual customers. The prototype keeps the rule setting, score, recommendation, and explanation together.

The tool does not make final onboarding or rejection decisions. It is a decision-support prototype. Borderline cases, low-confidence matches, and high-risk PEP relationships still require human review. The main failure risk is jurisdictional misconfiguration: if the US and UK settings are wrong or outdated, the tool can look consistent while applying the wrong regulatory logic.
