def route_claim(data, missing_fields):
    description = str(data.get("Description", "")).lower()
    claim_type = str(data.get("Claim Type", "")).lower()

    try:
        damage = float(data.get("Estimated Damage", 0))
    except:
        damage = 0

    # Rule 1: Missing fields
    if missing_fields:
        return "Manual Review", "Mandatory fields are missing."

    # Rule 2: Fraud keywords
    suspicious_words = ["fraud", "staged", "inconsistent"]
    if any(word in description for word in suspicious_words):
        return "Investigation Flag", "Suspicious wording detected in description."

    # Rule 3: Injury claims
    if claim_type == "injury":
        return "Specialist Queue", "Claim involves injury."

    # Rule 4: Low damage fast-track
    if damage < 25000:
        return "Fast-track", "Damage estimate below threshold."

    return "Standard Processing", "No special routing conditions triggered."
