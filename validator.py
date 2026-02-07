MANDATORY_FIELDS = [
    "Policy Number",
    "Claim Type",
    "Estimated Damage",
    "Date of Incident",
    "Location"
]

def find_missing_fields(data):
    missing = []
    for field in MANDATORY_FIELDS:
        if field not in data or not str(data[field]).strip():
            missing.append(field)
    return missing
