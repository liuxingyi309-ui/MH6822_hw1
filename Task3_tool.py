import csv
from pathlib import Path


DATA_PATH = Path("data/Task3_data.csv")
OUTPUT_PATH = Path("Task3_results.csv")


JURISDICTION_CONFIGS = {
    "US": {
        "description": "Risk-based BSA/CDD configuration. PEP status alone does not automatically trigger EDD.",
        "pep_points": {
            "none": 0,
            "domestic_pep": 8,
            "foreign_pep": 24,
            "international_org_pep": 18,
        },
        "relationship_points": {
            "none": 0,
            "family": 10,
            "close_associate": 12,
        },
        "manual_review_threshold": 45,
        "edd_threshold": 65,
        "senior_approval_threshold": 82,
        "domestic_pep_low_risk_cap": None,
        "explicit_proportionality_note": False,
    },
    "UK": {
        "description": "FCA-style proportionality configuration. PEP relationships are separated by risk level rather than treated as one category.",
        "pep_points": {
            "none": 0,
            "domestic_pep": 5,
            "foreign_pep": 26,
            "international_org_pep": 18,
        },
        "relationship_points": {
            "none": 0,
            "family": 8,
            "close_associate": 10,
        },
        "manual_review_threshold": 42,
        "edd_threshold": 62,
        "senior_approval_threshold": 78,
        "domestic_pep_low_risk_cap": 38,
        "explicit_proportionality_note": True,
    },
}


SOURCE_OF_FUNDS_POINTS = {
    "low": 0,
    "medium": 10,
    "high": 22,
}


def point_text(points: int) -> str:
    return "point" if points == 1 else "points"


def volume_points(monthly_transaction_volume_usd: float) -> int:
    if monthly_transaction_volume_usd >= 200000:
        return 16
    if monthly_transaction_volume_usd >= 100000:
        return 10
    if monthly_transaction_volume_usd >= 50000:
        return 6
    return 0


def score_customer(row: dict, jurisdiction: str) -> dict:
    config = JURISDICTION_CONFIGS[jurisdiction]

    pep_category = row["pep_category"]
    relationship = row["relationship_to_pep"]
    adverse_media = float(row["adverse_media_score"])
    sanctions = float(row["sanctions_match_score"])
    transaction_volume = float(row["monthly_transaction_volume_usd"])
    source_of_funds = row["source_of_funds_risk"]
    name_confidence = float(row["name_match_confidence"])

    score = 0
    reasons = []

    pep_score = config["pep_points"][pep_category]
    score += pep_score
    if pep_score:
        reasons.append(f"{pep_category.replace('_', ' ')} adds {pep_score} {point_text(pep_score)}")

    relationship_score = config["relationship_points"][relationship]
    score += relationship_score
    if relationship_score:
        reasons.append(
            f"{relationship.replace('_', ' ')} relationship adds "
            f"{relationship_score} {point_text(relationship_score)}"
        )

    adverse_score = round(adverse_media * 0.25)
    score += adverse_score
    if adverse_score:
        reasons.append(f"adverse media contributes {adverse_score} {point_text(adverse_score)}")

    sanctions_score = round(sanctions * 0.45)
    score += sanctions_score
    if sanctions_score:
        reasons.append(
            f"sanctions/watchlist signal contributes {sanctions_score} {point_text(sanctions_score)}"
        )

    volume_score = volume_points(transaction_volume)
    score += volume_score
    if volume_score:
        reasons.append(f"transaction volume contributes {volume_score} {point_text(volume_score)}")

    funds_score = SOURCE_OF_FUNDS_POINTS[source_of_funds]
    score += funds_score
    if funds_score:
        reasons.append(
            f"{source_of_funds} source-of-funds risk adds {funds_score} {point_text(funds_score)}"
        )

    # Low confidence PEP/name matches should not automatically increase risk;
    # they are treated as a reason for manual review because they may be false positives.
    low_confidence_match = name_confidence < 80 and (pep_category != "none" or relationship != "none")

    if (
        jurisdiction == "UK"
        and config["domestic_pep_low_risk_cap"] is not None
        and pep_category == "domestic_pep"
        and adverse_media < 20
        and sanctions < 5
        and source_of_funds == "low"
    ):
        capped_score = min(score, config["domestic_pep_low_risk_cap"])
        if capped_score != score:
            reasons.append("UK proportionality cap applied for lower-risk domestic PEP")
        score = capped_score

    action = "standard due diligence"
    human_review = "no"

    if score >= config["senior_approval_threshold"]:
        action = "enhanced due diligence + senior management approval"
        human_review = "yes"
    elif score >= config["edd_threshold"]:
        action = "enhanced due diligence"
        human_review = "yes"
    elif score >= config["manual_review_threshold"] or low_confidence_match:
        action = "manual review"
        human_review = "yes"

    if low_confidence_match:
        reasons.append("manual review added because name/PEP match confidence is below 80")

    if config["explicit_proportionality_note"] and pep_category != "none":
        reasons.append("UK proportionality assessment recorded for PEP relationship")

    if jurisdiction == "US":
        jurisdictional_requirement = "risk-based PEP review; PEP status alone does not trigger automatic EDD"
    elif pep_category != "none" or relationship != "none":
        jurisdictional_requirement = "document proportionality assessment for the PEP relationship"
    else:
        jurisdictional_requirement = "standard UK AML/KYC review"

    return {
        "jurisdiction": jurisdiction,
        "risk_score": score,
        "recommended_action": action,
        "human_review_required": human_review,
        "jurisdictional_requirement": jurisdictional_requirement,
        "explanation": "; ".join(reasons) if reasons else "no material risk signal in this simplified model",
    }


def run() -> None:
    with DATA_PATH.open(newline="", encoding="utf-8") as f:
        customers = list(csv.DictReader(f))

    output_rows = []
    for customer in customers:
        for jurisdiction in ("US", "UK"):
            result = score_customer(customer, jurisdiction)
            output_rows.append(
                {
                    "customer_id": customer["customer_id"],
                    "customer_name": customer["customer_name"],
                    "pep_category": customer["pep_category"],
                    "relationship_to_pep": customer["relationship_to_pep"],
                    "country_of_residence": customer["country_of_residence"],
                    **result,
                }
            )

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} jurisdiction-specific results to {OUTPUT_PATH}")
    print()
    print("Example jurisdiction differences:")
    for customer in customers:
        us = score_customer(customer, "US")
        uk = score_customer(customer, "UK")
        if (
            us["recommended_action"] != uk["recommended_action"]
            or us["risk_score"] != uk["risk_score"]
            or us["jurisdictional_requirement"] != uk["jurisdictional_requirement"]
        ):
            print(f"\n{customer['customer_id']} - {customer['customer_name']}")
            print(f"  US score/action: {us['risk_score']} | {us['recommended_action']}")
            print(f"  US requirement:  {us['jurisdictional_requirement']}")
            print(f"  UK score/action: {uk['risk_score']} | {uk['recommended_action']}")
            print(f"  UK requirement:  {uk['jurisdictional_requirement']}")


if __name__ == "__main__":
    run()
