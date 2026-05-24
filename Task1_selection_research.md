# Task 1: Selection and research

## Project

**HSBC PEP Screening: US vs UK**

I am proposing a jurisdiction-aware AML/KYC screening tool for HSBC, focused on politically exposed person (PEP) screening. I want to look at how the same customer profile may need to be handled differently in the United States and the United Kingdom.

## Regulated entity and domain

I chose **HSBC** as the case study because it is a real global banking group with operations in both the United States and the United Kingdom. A bank like HSBC cannot rely on one universal AML/KYC rulebook for all markets. It has to apply similar financial-crime controls under different legal and supervisory environments.

The domain is **AML/KYC, with a focus on PEP screening**. This includes customer due diligence, enhanced due diligence, sanctions and watchlist screening, adverse media checks, and ongoing monitoring after onboarding.

PEP screening is useful for this assignment because it involves a real trade-off. The bank has to detect corruption and money-laundering risk, but it should not treat every political connection as automatically suspicious. If screening is too strict, legitimate customers may face delays, unnecessary enhanced due diligence, or exclusion from banking services. If screening is too weak, the bank may miss serious financial crime risk.

## Why the US and UK

I compare the **United States** and the **United Kingdom** because both use risk-based AML principles, but their expectations around PEP screening are not identical.

FATF Recommendation 12 provides the international starting point: financial institutions need systems to identify PEPs and apply extra measures where the relationship is higher risk. FATF gives the baseline, but it does not tell a bank exactly how to treat every PEP relationship in every country.

In the United States, the Bank Secrecy Act and customer due diligence framework take a risk-based approach. U.S. regulators have clarified that PEP status alone should not automatically trigger a fixed checklist of additional due diligence. The bank still needs to look at the actual risk of the relationship.

In the United Kingdom, the FCA's PEP guidance puts more explicit weight on proportionality. Firms are expected to distinguish lower-risk and higher-risk PEP relationships, rather than treating all PEPs, family members, and close associates as the same level of concern. This is relevant to my project because over-screening can create unfair outcomes for customers.

## Why this is a RegTech problem

The tool is not meant to replace compliance judgment. I see it as a way to make that judgment more structured and consistent across jurisdictions.

It would use synthetic onboarding data, including occupation, country of residence, PEP category, relationship to a PEP, adverse media score, sanctions match score, transaction volume, and source-of-funds risk. The US and UK versions of the tool would then use different settings to recommend standard due diligence, enhanced due diligence, manual review, senior management approval, or closer ongoing monitoring.

The output should do more than say "approve" or "reject." It should explain why a customer was escalated, which jurisdictional setting affected the result, and where human review is needed. For example, I would not want the tool to treat a domestic political figure with low transaction risk in the same way as a foreign senior official with unexplained wealth or adverse media links. The same profile could also lead to different escalation decisions under the US and UK settings.

This is why I see the project as jurisdiction-aware rather than just a generic PEP screening exercise. The regulatory question is not only whether a customer appears on a PEP list. The harder question is what HSBC should do with that information in a particular jurisdiction.

## References

- HSBC UK, About HSBC: https://www.about.hsbc.co.uk/
- HSBC USA, HSBC in the USA: https://www.about.us.hsbc.com/investor-relations/hsbc-usa
- FATF, Guidance on Politically Exposed Persons, Recommendations 12 and 22: https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Peps-r12-r22.html
- FinCEN, Customer Due Diligence Final Rule: https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule
- FinCEN and U.S. banking regulators, Joint Statement on BSA due diligence requirements for customers who may be considered PEPs: https://www.fincen.gov/index.php/news/news-releases/agencies-issue-statement-bank-secrecy-act-due-diligence-requirements-customers
- FCA, Treatment of Politically Exposed Persons for Anti-Money Laundering Purposes: https://www.fca.org.uk/publications/guidance-consultations/gc24-4-proposed-amendments-guidance-treatment-politically-exposed-persons

