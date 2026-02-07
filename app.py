from fastapi import FastAPI, UploadFile, File
import json
from extractor import extract_text_from_pdf, extract_fields
from validator import find_missing_fields
from router import route_claim

app = FastAPI(title="Insurance Claims Processing Agent")


@app.post("/process-claim/")
async def process_claim(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    extracted_data = extract_fields(text)

    missing_fields = find_missing_fields(extracted_data)
    route, reasoning = route_claim(extracted_data, missing_fields)

    return {
        "extractedFields": extracted_data,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reasoning
    }
