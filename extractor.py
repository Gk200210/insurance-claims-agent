import pdfplumber
import re


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


def search(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_fields(text):
    data = {}

    # Policy Information
    data["Policy Number"] = search(r"POLICY NUMBER[:\s]*([A-Z0-9\-]+)", text)
    data["Policyholder Name"] = search(r"NAME OF INSURED.*?\n([A-Z ,.'-]+)", text)
    data["Effective Dates"] = ""  # Often not present in ACORD auto FNOL

    # Incident Info
    data["Date of Incident"] = search(r"DATE OF LOSS.*?(\d{2}/\d{2}/\d{4})", text)
    data["Time of Incident"] = search(r"DATE OF LOSS AND TIME.*?(AM|PM)", text)
    data["Location"] = search(r"LOCATION OF LOSS.*?\n(.+)", text)
    data["Description"] = search(r"DESCRIPTION OF ACCIDENT.*?\n(.+)", text)

    # People Involved
    data["Claimant"] = data["Policyholder Name"]
    data["Third Parties"] = search(r"OTHER VEHICLE / PROPERTY DAMAGED.*?\n(.+)", text)
    data["Contact Details"] = search(r"PHONE #.*?PRIMARY.*?(\d{10})", text)

    # Asset Details (Vehicle)
    data["Asset Type"] = "Automobile"
    data["Asset ID"] = search(r"V\.I\.N\.[:\s]*([A-Z0-9]+)", text)
    data["Estimated Damage"] = search(r"ESTIMATE AMOUNT[:\s]*\$?([0-9,]+)", text)

    # Other Required Fields
    data["Claim Type"] = "Auto"
    data["Attachments"] = "None"
    data["Initial Estimate"] = data["Estimated Damage"]

    return data
