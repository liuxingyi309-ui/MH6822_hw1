# Task 2: Values audit

## What is the company's mission statement?

The mission is to help compliance teams make AML/KYC decisions that are easier to explain and less dependent on a single global template. The company I am imagining is a small RegTech firm that builds compliance tools for banks operating in more than one jurisdiction.

For this project, the company is not trying to remove human judgment from AML/KYC work, because that would be unrealistic and unsafe. The more realistic aim is to make escalation decisions clearer: why a customer was flagged, which risk signals mattered, which jurisdictional setting applied, and when a compliance officer should review the case.

The company is mainly focused on rule configuration, risk scoring logic, audit trails, and workflow design. I see it as an early-stage company rather than a mature vendor, because the product is still narrow: it focuses on PEP screening across selected jurisdictions, not the whole AML compliance stack. A large cross-border bank such as HSBC would be the natural first customer, because smaller firms may not have enough jurisdictional complexity to justify this type of tool.

## Whose perspective does the tool serve?

The paying client is the bank's compliance function, especially the AML/KYC and financial-crime compliance team. So the tool serves HSBC first. I would not present it as a tool that benefits every stakeholder in the same way, but it still has to consider the regulator and the customer because PEP screening decisions can create harm outside the bank.

The tension is that HSBC wants fewer false positives, lower manual review costs, and a defensible audit trail. Regulators care about the opposite failure: the bank missing serious corruption or money-laundering risks. Customers care about not being delayed, over-scrutinised, or excluded because of a political connection, nationality, name match, or weak adverse media signal.

My design choice is to serve the compliance team, but not only as a cost-cutting tool. I would design it as a decision-support tool rather than an automatic rejection tool. It should help compliance officers understand risk and decide what to review, not simply clear more alerts faster.

## Is the tool measuring genuine risk or documenting compliance?

I want the tool to measure genuine risk, not only document compliance. It will still produce documentation, because banks need audit trails. My concern is that documentation can become the main purpose. A bank can end up with a neat file showing that a customer was screened, while the quality of the decision has barely changed.

The main design choice here is to separate PEP status from overall risk. I do not want the tool to treat PEP status as an automatic high-risk result. The risk score would combine PEP category with other signals, such as transaction activity, source-of-funds risk, adverse media, sanctions match confidence, and whether the customer is a domestic or foreign PEP.

A checklist can create false confidence. It may look compliant on paper, but still fail to distinguish a low-risk domestic political figure from a high-risk foreign official with unexplained wealth. For that reason, the tool should explain the risk drivers behind an escalation instead of just recording that a PEP screening box was ticked.

## Who bears the cost if the tool gets it wrong?

If the tool is too strict, the immediate cost falls on customers. A legitimate customer can face onboarding delays, repeated information requests, enhanced due diligence, or even account refusal. This is especially troubling when the customer is flagged because of a name match, nationality, family connection, or weak adverse media result rather than clear evidence of financial crime.

If the tool is too loose, the cost shifts to the bank, regulators, and the public. HSBC could miss corruption proceeds, sanctions exposure, or money-laundering activity. That creates enforcement risk, reputational damage, and real harm if illicit funds move through the financial system.

The failure mode I am most concerned about is jurisdictional misconfiguration, not just a normal false positive or false negative. A rule that is reasonable in one country can be too aggressive or too weak in another. For example, applying one global PEP threshold across both the United States and the United Kingdom risks ignoring the different regulatory emphasis on proportionality, risk-based treatment, and customer outcomes.

This is why I keep human accountability in the design. The tool can rank risk and explain escalation logic, but I would not let it make the final decision to reject a customer in borderline cases. Someone in the bank still has to own the risk appetite and the final judgment.

The point is not to remove judgment from the process, but to make the reasons for that judgment clearer.

