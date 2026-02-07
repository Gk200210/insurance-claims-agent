🧠 Autonomous Insurance Claims Processing Agent
📌 Overview

This project implements an automated agent that processes First Notice of Loss (FNOL) insurance documents and routes claims based on rule-based decision logic.

The system extracts structured information from standardized automobile loss forms (e.g., those published by ACORD), validates mandatory data, and determines the appropriate processing workflow.

🎯 Objective

Build a lightweight AI-inspired document processing pipeline that:

Extracts key fields from FNOL documents

Detects missing or inconsistent data

Classifies and routes claims

Provides reasoning for routing decisions

⚙️ System Architecture
PDF → Text Extraction → Field Extraction → Validation → Rule Engine → JSON Output

🧾 Extracted Information

Policy details

Incident information

Involved parties

Vehicle / asset details

Damage estimates

Claim type

🚦 Claim Routing Logic
Condition	Route
Missing mandatory fields	Manual Review
Estimated damage < 25,000	Fast-track
Suspicious keywords detected	Investigation Flag
Injury claims	Specialist Queue
🛠 Tech Stack

Python

FastAPI

pdfplumber

Regex-based document parsing

▶️ How to Run
pip install -r requirements.txt
python -m uvicorn app:app --reload


Open the API interface:

http://127.0.0.1:8000/docs


Upload an FNOL PDF to test.

📤 Output Format
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}
